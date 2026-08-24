#!/usr/bin/env python3
"""Derive a minimal AVCT v0.1 metric set from validated JSONL telemetry.

The output is descriptive. It does not estimate causal effects or validate AVCT.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_ts(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    return datetime.fromisoformat(normalized)


def round_metric(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 6)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            events.append(json.loads(raw))
    return events


def derive_run(run_id: str, events: list[dict[str, Any]]) -> dict[str, Any]:
    timestamps = [parse_ts(e["ts"]) for e in events]
    start = min(timestamps)
    end = max(timestamps)
    observation_seconds = max((end - start).total_seconds(), 0.0)
    observation_hours = observation_seconds / 3600.0

    execution = [e for e in events if e.get("event_type") == "execution"]
    controls = [e for e in events if e.get("event_type") == "control"]
    outcomes = [e for e in events if e.get("event_type") == "outcome"]
    coordination = [e for e in events if e.get("event_type") == "coordination"]

    candidate_actions = len({e["action_id"] for e in execution})
    executed_action_ids = {
        e["action_id"] for e in execution if e.get("execution_status") == "executed"
    }
    executed_actions = len(executed_action_ids)

    correct_action_ids = {
        e["action_id"]
        for e in outcomes
        if e.get("ground_truth_status") == "correct"
        and e.get("action_id") in executed_action_ids
    }
    valid_completed_actions = len(correct_action_ids)

    control_arrivals = len(controls)
    completed_controls = [e for e in controls if e.get("service_finished_at")]
    control_completed = len(completed_controls)

    active_service_seconds = 0.0
    review_durations_ms: list[float] = []
    for event in completed_controls:
        if event.get("service_started_at") and event.get("service_finished_at"):
            duration = (
                parse_ts(event["service_finished_at"])
                - parse_ts(event["service_started_at"])
            ).total_seconds()
            if duration >= 0:
                active_service_seconds += duration
        if isinstance(event.get("review_duration_ms"), (int, float)):
            review_durations_ms.append(float(event["review_duration_ms"]))

    lambda_control = (
        control_arrivals / observation_hours if observation_hours > 0 else None
    )
    active_service_hours = active_service_seconds / 3600.0
    mu_control = (
        control_completed / active_service_hours if active_service_hours > 0 else None
    )
    k_observed = (
        lambda_control / mu_control
        if lambda_control is not None and mu_control not in (None, 0)
        else None
    )

    unsafe_escapes = sum(bool(e.get("unsafe_escape")) for e in outcomes)
    unsafe_escape_rate = (
        unsafe_escapes / executed_actions if executed_actions else None
    )

    rollback_required = sum(bool(e.get("rollback_required")) for e in outcomes)
    rollback_successes = sum(
        bool(e.get("rollback_required")) and bool(e.get("rollback_success"))
        for e in outcomes
    )
    rollback_success_rate = (
        rollback_successes / rollback_required if rollback_required else None
    )

    rework_required = sum(bool(e.get("rework_required")) for e in outcomes)
    recovery_cost_total = sum(float(e.get("recovery_cost") or 0) for e in outcomes)
    realized_value_total = sum(float(e.get("realized_value") or 0) for e in outcomes)

    duplicate_events = sum(e.get("coordination_type") == "duplicate" for e in coordination)
    conflict_events = sum(e.get("coordination_type") == "conflict" for e in coordination)
    coordination_rework_actions = sum(
        int(e.get("rework_actions") or 0) for e in coordination
    )

    architecture_ids = sorted({str(e.get("architecture_id")) for e in events})
    conditions = sorted({str(e.get("experiment_condition")) for e in events})
    task_ids = sorted({str(e.get("task_id")) for e in events})
    agent_ids = sorted(
        {str(e.get("agent_id")) for e in execution if e.get("agent_id") is not None}
    )

    return {
        "run_id": run_id,
        "architecture_ids": architecture_ids,
        "experiment_conditions": conditions,
        "task_count": len(task_ids),
        "agent_count_observed": len(agent_ids),
        "observation_seconds": round_metric(observation_seconds),
        "candidate_actions": candidate_actions,
        "executed_actions": executed_actions,
        "valid_completed_actions": valid_completed_actions,
        "n_eff_observed": valid_completed_actions,
        "control_arrivals": control_arrivals,
        "control_completed": control_completed,
        "control_active_service_seconds": round_metric(active_service_seconds),
        "lambda_control_per_hour": round_metric(lambda_control),
        "mu_control_observed_per_hour": round_metric(mu_control),
        "k_observed": round_metric(k_observed),
        "unsafe_escapes": unsafe_escapes,
        "unsafe_escape_rate": round_metric(unsafe_escape_rate),
        "rollback_required": rollback_required,
        "rollback_success_rate": round_metric(rollback_success_rate),
        "rework_required": rework_required,
        "recovery_cost_total": round_metric(recovery_cost_total),
        "realized_value_total": round_metric(realized_value_total),
        "coordination_duplicate_events": duplicate_events,
        "coordination_conflict_events": conflict_events,
        "coordination_rework_actions": coordination_rework_actions,
        "mean_human_review_duration_ms": round_metric(
            sum(review_durations_ms) / len(review_durations_ms)
            if review_durations_ms
            else None
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    events = load_jsonl(args.input)
    by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        by_run[str(event["run_id"])].append(event)

    result = {
        "source": str(args.input),
        "empirical_evidence": False,
        "runs": [derive_run(run_id, by_run[run_id]) for run_id in sorted(by_run)],
    }
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
