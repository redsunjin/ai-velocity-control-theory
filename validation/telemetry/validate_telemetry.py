#!/usr/bin/env python3
"""Validate AVCT v0.1 JSONL telemetry.

This validator checks instrumentation integrity only. Passing does not imply
that an experiment supports AVCT or that any action was safe.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

COMMON_REQUIRED = {
    "run_id",
    "workflow_id",
    "task_id",
    "event_id",
    "event_type",
    "ts",
    "architecture_id",
    "experiment_condition",
}

TYPE_REQUIRED = {
    "execution": {
        "agent_id",
        "action_id",
        "action_type",
        "target_id",
        "candidate_at",
        "execute_started_at",
        "execute_finished_at",
        "execution_status",
    },
    "coordination": {
        "coordination_type",
        "related_action_ids",
        "coordination_started_at",
        "coordination_finished_at",
        "resolution_status",
        "rework_actions",
    },
    "control": {
        "control_id",
        "action_id",
        "risk_tier",
        "control_route",
        "control_arrived_at",
        "service_started_at",
        "service_finished_at",
        "controller_type",
        "decision",
        "escalated",
        "override",
    },
    "outcome": {
        "action_id",
        "ground_truth_status",
        "unsafe_escape",
        "rollback_required",
        "rework_required",
        "recovery_cost",
        "realized_value",
        "external_impact",
    },
}

TIMESTAMP_FIELDS = {
    "ts",
    "candidate_at",
    "execute_started_at",
    "execute_finished_at",
    "coordination_started_at",
    "coordination_finished_at",
    "control_arrived_at",
    "service_started_at",
    "service_finished_at",
    "recovery_started_at",
    "recovery_finished_at",
}

# Exact field names only. We intentionally do not reject harmless fields such
# as token_or_compute_cost merely because they contain the word "token".
FORBIDDEN_PAYLOAD_KEYS = {
    "password",
    "secret",
    "api_key",
    "access_token",
    "refresh_token",
    "credential",
    "credentials",
    "raw_prompt",
    "prompt_text",
    "raw_response",
    "response_text",
    "customer_data",
    "pii",
    "email_address",
}


def parse_ts(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("timestamp must include UTC Z or an explicit offset")
    return dt


def find_forbidden_keys(value: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.lower() in FORBIDDEN_PAYLOAD_KEYS:
                found.append(child_path)
            found.extend(find_forbidden_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(find_forbidden_keys(child, f"{path}[{index}]"))
    return found


def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid JSON: {exc}")
            continue
        if not isinstance(event, dict):
            errors.append(f"line {line_no}: event must be a JSON object")
            continue
        event["__line_no"] = line_no
        events.append(event)
    return events, errors


def validate(events: list[dict[str, Any]]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    event_ids: set[str] = set()
    execution_actions: set[str] = set()
    referenced_actions: list[tuple[int, str, str]] = []
    parent_refs: list[tuple[int, str]] = []
    task_ids: set[str] = set()
    run_ids: set[str] = set()
    architecture_ids: set[str] = set()

    for event in events:
        line_no = event.get("__line_no", "?")
        missing_common = sorted(COMMON_REQUIRED - event.keys())
        if missing_common:
            errors.append(f"line {line_no}: missing common fields: {missing_common}")
            continue

        event_type = event.get("event_type")
        if event_type not in TYPE_REQUIRED:
            errors.append(f"line {line_no}: unsupported event_type={event_type!r}")
            continue

        missing_type = sorted(TYPE_REQUIRED[event_type] - event.keys())
        if missing_type:
            errors.append(f"line {line_no}: missing {event_type} fields: {missing_type}")

        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            errors.append(f"line {line_no}: event_id must be a non-empty string")
        elif event_id in event_ids:
            errors.append(f"line {line_no}: duplicate event_id={event_id}")
        else:
            event_ids.add(event_id)

        task_ids.add(str(event.get("task_id")))
        run_ids.add(str(event.get("run_id")))
        architecture_ids.add(str(event.get("architecture_id")))

        if event_type == "execution" and isinstance(event.get("action_id"), str):
            execution_actions.add(event["action_id"])
        elif event_type in {"control", "outcome"} and isinstance(event.get("action_id"), str):
            referenced_actions.append((int(line_no), event_type, event["action_id"]))
        elif event_type == "coordination":
            related = event.get("related_action_ids")
            if not isinstance(related, list) or not all(isinstance(x, str) for x in related):
                errors.append(f"line {line_no}: related_action_ids must be a list of strings")
            else:
                for action_id in related:
                    referenced_actions.append((int(line_no), event_type, action_id))

        parent = event.get("parent_event_id")
        if parent is not None:
            if isinstance(parent, str):
                parent_refs.append((int(line_no), parent))
            else:
                errors.append(f"line {line_no}: parent_event_id must be a string")

        for field in TIMESTAMP_FIELDS:
            if field in event and event[field] is not None:
                try:
                    parse_ts(event[field])
                except (TypeError, ValueError) as exc:
                    errors.append(f"line {line_no}: invalid {field}: {exc}")

        for bad_path in find_forbidden_keys(event):
            errors.append(f"line {line_no}: forbidden sensitive payload key at {bad_path}")

        # Basic interval ordering. This is instrumentation validation, not a
        # universal workflow ordering rule.
        interval_pairs = [
            ("candidate_at", "execute_started_at"),
            ("execute_started_at", "execute_finished_at"),
            ("control_arrived_at", "service_started_at"),
            ("service_started_at", "service_finished_at"),
            ("recovery_started_at", "recovery_finished_at"),
        ]
        for start_field, end_field in interval_pairs:
            if event.get(start_field) is not None and event.get(end_field) is not None:
                try:
                    if parse_ts(event[start_field]) > parse_ts(event[end_field]):
                        errors.append(
                            f"line {line_no}: {start_field} occurs after {end_field}"
                        )
                except (TypeError, ValueError):
                    pass

    for line_no, event_type, action_id in referenced_actions:
        if action_id not in execution_actions:
            errors.append(
                f"line {line_no}: {event_type} references unknown execution action_id={action_id}"
            )

    for line_no, parent_event_id in parent_refs:
        if parent_event_id not in event_ids:
            errors.append(
                f"line {line_no}: parent_event_id references unknown event_id={parent_event_id}"
            )

    summary = {
        "event_count": len(events),
        "execution_action_count": len(execution_actions),
        "task_count": len(task_ids - {"None"}),
        "run_count": len(run_ids - {"None"}),
        "architecture_count": len(architecture_ids - {"None"}),
        "event_types": {
            event_type: sum(1 for e in events if e.get("event_type") == event_type)
            for event_type in TYPE_REQUIRED
        },
        "linkage_errors": sum("unknown execution action_id" in e for e in errors),
        "privacy_errors": sum("forbidden sensitive payload key" in e for e in errors),
        "valid": not errors,
    }
    return errors, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSONL telemetry file")
    parser.add_argument("--summary", type=Path, help="optional JSON summary output")
    args = parser.parse_args()

    events, load_errors = load_jsonl(args.input)
    validation_errors, summary = validate(events)
    errors = load_errors + validation_errors
    summary["valid"] = not errors
    summary["error_count"] = len(errors)

    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(
            json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if errors:
        print("Telemetry validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
