#!/usr/bin/env python3
"""AVCT v0.1 minimal simulation.

Purpose
-------
This script is a structural sanity check for H1/H2/H5/H6. It is not
empirical evidence for AVCT.

The model deliberately keeps reliability fixed so the first run isolates:
1) duplication / coordination loss as agent count rises, and
2) control-queue saturation as action arrival approaches service capacity.

Run:
    python validation/simulations/avct_v01.py

Dependency:
    numpy
"""

from collections import deque
import csv
import math
from pathlib import Path

import numpy as np

AGENTS = [1, 2, 4, 8, 16, 32]
SEEDS = range(20)
LAMBDA = 1.5
RELIABILITY = 0.95


def mean_rows(rows):
    arr = np.asarray(rows, dtype=float)
    return arr.mean(axis=0).tolist()


def coordination_run(A, pool_size, steps=1000, seed=0):
    """Collision-based coordination toy model.

    Candidate actions choose a task target. Multiple actions aimed at the same
    target within a step are treated as duplicate work. A smaller task pool is
    used as a proxy for stronger task coupling / shared-target contention.
    """
    rng = np.random.default_rng(seed)
    raw_total = 0
    unique_total = 0
    valid_total = 0
    s_values = []

    for _ in range(steps):
        n = int(rng.poisson(A * LAMBDA))
        raw_total += n
        if n == 0:
            s_values.append(1.0)
            continue

        targets = rng.integers(0, pool_size, size=n)
        unique = len(np.unique(targets))
        unique_total += unique
        valid_total += int(rng.binomial(unique, RELIABILITY))
        s_values.append(unique / n)

    n_eff = valid_total / steps
    return [
        raw_total / steps,
        unique_total / steps,
        n_eff,
        n_eff / A,
        float(np.mean(s_values)),
    ]


def control_run(
    A,
    mu,
    decay,
    pool_size=200,
    steps=1200,
    burn=200,
    seed=0,
):
    """FIFO control-gated workflow.

    Every unique action enters the control queue. `mu` is service capacity per
    step. Valid reviewed actions realize value. With decay=0, value is time
    insensitive; with decay>0, delayed actions lose value exponentially.

    This queue behavior is borrowed from standard queueing intuition. AVCT's
    question is how agentic execution generates the arrival stream and how
    saturation constrains realized performance.
    """
    rng = np.random.default_rng(seed)
    queue = deque()
    delays = []
    raw = []
    unique = []
    approved_valid = []
    realized = []
    backlog = []

    for t in range(steps):
        n = int(rng.poisson(A * LAMBDA))
        raw.append(n)

        if n:
            targets = rng.integers(0, pool_size, size=n)
            unique_count = len(np.unique(targets))
        else:
            unique_count = 0
        unique.append(unique_count)

        if unique_count:
            validity = rng.random(unique_count) < RELIABILITY
            for is_valid in validity:
                queue.append((t, bool(is_valid)))

        approved = 0
        value = 0.0
        for _ in range(min(mu, len(queue))):
            arrival_t, is_valid = queue.popleft()
            delay = t - arrival_t
            delays.append(delay)
            if is_valid:
                approved += 1
                value += math.exp(-decay * delay)

        approved_valid.append(approved)
        realized.append(value)
        backlog.append(len(queue))

    arrival_rate = float(np.mean(unique[burn:]))
    k = arrival_rate / mu

    return [
        arrival_rate,
        k,
        float(np.mean(delays)) if delays else 0.0,
        float(backlog[-1]),
        float(np.mean(backlog[burn:])),
        float(np.mean(raw[burn:])),
        float(np.mean(unique[burn:])),
        float(np.mean(approved_valid[burn:])),
        float(np.mean(realized[burn:])),
        float(np.mean(realized[-200:])),
    ]


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def main():
    output_dir = Path(__file__).resolve().parents[1] / "results" / "generated"

    coordination_rows = []
    for coupling, pool_size in [("low", 200), ("high", 20)]:
        for A in AGENTS:
            values = [
                coordination_run(A, pool_size=pool_size, seed=seed)
                for seed in SEEDS
            ]
            avg = mean_rows(values)
            coordination_rows.append([coupling, A, *[round(x, 6) for x in avg]])

    write_csv(
        output_dir / "coordination-summary.csv",
        ["coupling", "A", "raw_rate", "unique_rate", "N_eff", "N_eff_per_agent", "S"],
        coordination_rows,
    )

    control_rows = []
    for decay in [0.0, 0.03]:
        for mu in [6, 12, 24]:
            for A in AGENTS:
                values = [
                    control_run(A, mu=mu, decay=decay, seed=seed)
                    for seed in SEEDS
                ]
                avg = mean_rows(values)
                control_rows.append([decay, mu, A, *[round(x, 6) for x in avg]])

    write_csv(
        output_dir / "control-summary.csv",
        [
            "decay", "mu", "A", "arrival_rate", "K", "mean_delay",
            "final_backlog", "mean_backlog_postburn", "raw_rate",
            "unique_rate", "approved_valid_rate", "realized_rate",
            "realized_last200",
        ],
        control_rows,
    )

    print(f"Wrote results to {output_dir}")


if __name__ == "__main__":
    main()
