#!/usr/bin/env python3
"""AVCT v0.1 control-architecture sensitivity simulation.

Purpose
-------
Attack H6/H7/H8 after the first structural simulation.

This is a synthetic toy model, not empirical evidence. It asks:
1. Can risk-tiered routing move the control-saturation point?
2. Under what automated-verification quality does that happen without a
   worse unsafe-escape rate than a stable full-human-review baseline?
3. Does reversibility reduce loss severity even when the error count is
   unchanged?

Run:
    python validation/simulations/avct_v01_control_architecture.py

Dependency:
    numpy
"""

from collections import deque
import csv
import math
from pathlib import Path

import numpy as np

AGENTS = [1, 2, 4, 8, 16, 32, 64]
LAMBDA = 1.5
STEPS = 1000
MU_CONTROL = 12
SCALE_SEEDS = range(30)
SENSITIVITY_SEEDS = range(50)

RISK_PROBS = np.array([0.70, 0.20, 0.10])  # low, medium, high
ERROR_PROBS = np.array([0.01, 0.05, 0.15])
BASE_VALUE = np.array([1.0, 2.0, 4.0])
HARM_COST = np.array([2.0, 8.0, 30.0])

HUMAN_SENSITIVITY = 0.97
HUMAN_FALSE_REJECT = 0.01
AUTO_FALSE_POSITIVE = 0.01
MEDIUM_SAMPLE_RATE = 0.15
VALUE_DECAY = 0.005

REVERSIBILITY = {
    "baseline": np.array([0.80, 0.50, 0.10]),
    "high": np.array([0.98, 0.85, 0.50]),
}


def add_group(queue, t, tier, is_bad, count):
    if count > 0:
        queue.append([t, tier, is_bad, int(count)])


def simulate(
    A,
    architecture,
    seed,
    auto_sensitivity=0.90,
    reversibility="baseline",
):
    """Run one synthetic discrete-time control workflow.

    full_review:
        Every action enters the human control queue.

    tiered:
        - low risk: automated verification; detected bad actions are rejected;
          false-positive good actions are escalated to a human.
        - medium risk: detected or sampled actions go to human review.
        - high risk: all actions go to human review.

    Notes:
        The numeric risk/error/value assumptions are deliberately synthetic.
        They exist to test structural sensitivity, not to estimate real systems.
    """
    rng = np.random.default_rng(seed)
    queue = deque()
    human_arrivals = 0
    human_processed = 0
    unsafe_escapes = 0
    created = 0
    executed = 0
    harm = 0.0
    realized_value = 0.0
    delays = []
    backlogs = []
    rev_prob = REVERSIBILITY[reversibility]

    for t in range(STEPS):
        n = int(rng.poisson(A * LAMBDA))
        created += n
        counts = rng.multinomial(n, RISK_PROBS) if n else np.zeros(3, dtype=int)
        bad = np.array(
            [rng.binomial(counts[i], ERROR_PROBS[i]) for i in range(3)],
            dtype=int,
        )
        good = counts - bad

        if architecture == "full_review":
            for tier in range(3):
                add_group(queue, t, tier, False, good[tier])
                add_group(queue, t, tier, True, bad[tier])
                human_arrivals += int(counts[tier])

        elif architecture == "tiered":
            # Low risk: automated verifier can reject detected bad actions.
            detected_bad = rng.binomial(bad[0], auto_sensitivity)
            flagged_good = rng.binomial(good[0], AUTO_FALSE_POSITIVE)
            add_group(queue, t, 0, False, flagged_good)
            human_arrivals += int(flagged_good)

            bad_exec = int(bad[0] - detected_bad)
            good_exec = int(good[0] - flagged_good)
            executed += bad_exec + good_exec
            realized_value += (bad_exec + good_exec) * BASE_VALUE[0]
            unsafe_escapes += bad_exec
            if bad_exec:
                reversible = rng.binomial(bad_exec, rev_prob[0])
                harm += HARM_COST[0] * (
                    0.2 * reversible + (bad_exec - reversible)
                )

            # Medium risk: detected errors + a sample of unflagged actions
            # go to human review.
            detected_bad = rng.binomial(bad[1], auto_sensitivity)
            flagged_good = rng.binomial(good[1], AUTO_FALSE_POSITIVE)
            remaining_bad = int(bad[1] - detected_bad)
            remaining_good = int(good[1] - flagged_good)
            sampled_bad = rng.binomial(remaining_bad, MEDIUM_SAMPLE_RATE)
            sampled_good = rng.binomial(remaining_good, MEDIUM_SAMPLE_RATE)

            routed_bad = int(detected_bad + sampled_bad)
            routed_good = int(flagged_good + sampled_good)
            add_group(queue, t, 1, True, routed_bad)
            add_group(queue, t, 1, False, routed_good)
            human_arrivals += routed_bad + routed_good

            bad_exec = remaining_bad - int(sampled_bad)
            good_exec = remaining_good - int(sampled_good)
            executed += bad_exec + good_exec
            realized_value += (bad_exec + good_exec) * BASE_VALUE[1]
            unsafe_escapes += bad_exec
            if bad_exec:
                reversible = rng.binomial(bad_exec, rev_prob[1])
                harm += HARM_COST[1] * (
                    0.2 * reversible + (bad_exec - reversible)
                )

            # High risk: always human-gated.
            add_group(queue, t, 2, False, good[2])
            add_group(queue, t, 2, True, bad[2])
            human_arrivals += int(counts[2])

        else:
            raise ValueError(f"unknown architecture: {architecture}")

        capacity = MU_CONTROL
        while capacity > 0 and queue:
            arrival_t, tier, is_bad, count = queue[0]
            take = min(capacity, count)
            delay = t - arrival_t
            delays.extend([delay] * take)
            human_processed += take
            capacity -= take

            if is_bad:
                missed = rng.binomial(take, 1.0 - HUMAN_SENSITIVITY)
                if missed:
                    executed += int(missed)
                    realized_value += (
                        missed
                        * BASE_VALUE[tier]
                        * math.exp(-VALUE_DECAY * delay)
                    )
                    unsafe_escapes += int(missed)
                    reversible = rng.binomial(missed, rev_prob[tier])
                    harm += HARM_COST[tier] * (
                        0.2 * reversible + (missed - reversible)
                    )
            else:
                accepted = take - rng.binomial(take, HUMAN_FALSE_REJECT)
                executed += int(accepted)
                realized_value += (
                    accepted
                    * BASE_VALUE[tier]
                    * math.exp(-VALUE_DECAY * delay)
                )

            if take == count:
                queue.popleft()
            else:
                queue[0][3] -= take

        backlogs.append(sum(item[3] for item in queue))

    human_arrival_rate = human_arrivals / STEPS
    execute_rate = executed / STEPS

    return {
        "A": A,
        "created_rate": created / STEPS,
        "human_arrival_rate": human_arrival_rate,
        "K": human_arrival_rate / MU_CONTROL,
        "human_processed_rate": human_processed / STEPS,
        "mean_delay": float(np.mean(delays)) if delays else 0.0,
        "final_backlog": float(backlogs[-1]),
        "unsafe_escape_rate": unsafe_escapes / STEPS,
        "harm_rate": harm / STEPS,
        "realized_value_rate": realized_value / STEPS,
        "net_value_rate": (realized_value - harm) / STEPS,
        "execute_rate": execute_rate,
        "unsafe_per_1000_exec": 1000 * unsafe_escapes / max(executed, 1),
        "harm_per_1000_exec": 1000 * harm / max(executed, 1),
    }


def average_rows(rows, fixed):
    result = dict(fixed)
    for key in rows[0]:
        if key not in result:
            result[key] = float(np.mean([row[key] for row in rows]))
    return result


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in header})


def main():
    output_dir = Path(__file__).resolve().parents[1] / "results" / "generated"

    # Experiment A: scale comparison.
    scale_rows = []
    architectures = [
        ("full_review", "full_review", 0.90),
        ("tiered_90", "tiered", 0.90),
        ("tiered_99", "tiered", 0.99),
    ]
    for label, architecture, sensitivity in architectures:
        for A in AGENTS:
            rows = [
                simulate(
                    A,
                    architecture,
                    seed,
                    auto_sensitivity=sensitivity,
                    reversibility="baseline",
                )
                for seed in SCALE_SEEDS
            ]
            scale_rows.append(
                average_rows(rows, {"architecture": label, "A": A})
            )

    scale_header = [
        "architecture",
        "A",
        "created_rate",
        "human_arrival_rate",
        "K",
        "mean_delay",
        "final_backlog",
        "unsafe_per_1000_exec",
        "harm_per_1000_exec",
        "net_value_rate",
    ]
    write_csv(output_dir / "control-architecture-summary.csv", scale_header, scale_rows)

    # Experiment B: verifier sensitivity under a stable full-review baseline A=4.
    sensitivity_rows = []
    rows = [
        simulate(4, "full_review", seed, reversibility="baseline")
        for seed in SENSITIVITY_SEEDS
    ]
    sensitivity_rows.append(
        average_rows(
            rows,
            {"architecture": "full_review", "auto_sensitivity": ""},
        )
    )

    for sensitivity in [0.70, 0.80, 0.90, 0.95, 0.97, 0.98, 0.99, 0.995]:
        rows = [
            simulate(
                4,
                "tiered",
                seed,
                auto_sensitivity=sensitivity,
                reversibility="baseline",
            )
            for seed in SENSITIVITY_SEEDS
        ]
        sensitivity_rows.append(
            average_rows(
                rows,
                {"architecture": "tiered", "auto_sensitivity": sensitivity},
            )
        )

    sensitivity_header = [
        "architecture",
        "auto_sensitivity",
        "human_arrival_rate",
        "K",
        "unsafe_per_1000_exec",
        "harm_per_1000_exec",
        "net_value_rate",
    ]
    write_csv(
        output_dir / "verifier-sensitivity-summary.csv",
        sensitivity_header,
        sensitivity_rows,
    )

    # Experiment C: reversibility changes loss severity, not escape count.
    reversibility_rows = []
    for A in [4, 32]:
        for profile in ["baseline", "high"]:
            rows = [
                simulate(
                    A,
                    "tiered",
                    seed,
                    auto_sensitivity=0.90,
                    reversibility=profile,
                )
                for seed in SENSITIVITY_SEEDS
            ]
            reversibility_rows.append(
                average_rows(rows, {"A": A, "reversibility": profile})
            )

    reversibility_header = [
        "A",
        "reversibility",
        "K",
        "unsafe_per_1000_exec",
        "harm_per_1000_exec",
        "net_value_rate",
    ]
    write_csv(
        output_dir / "reversibility-summary.csv",
        reversibility_header,
        reversibility_rows,
    )

    print(f"Wrote results to {output_dir}")


if __name__ == "__main__":
    main()
