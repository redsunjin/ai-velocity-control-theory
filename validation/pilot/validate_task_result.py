#!/usr/bin/env python3
"""Validate a materialized AVCT pilot task result against evaluator ground truth.

The agent should not be given access to the evaluator ground-truth file during a
real pilot run. This tool is for the controller/ground-truth evaluation path.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def contains_subset(actual: Any, required: Any, path: str = "$") -> list[str]:
    errors: list[str] = []
    if isinstance(required, dict):
        if not isinstance(actual, dict):
            return [f"{path}: expected object"]
        for key, expected_value in required.items():
            if key not in actual:
                errors.append(f"{path}: missing key {key}")
            else:
                errors.extend(contains_subset(actual[key], expected_value, f"{path}.{key}"))
    elif actual != required:
        errors.append(f"{path}: expected {required!r}, got {actual!r}")
    return errors


def validate_text(path: Path, rule: dict[str, Any]) -> list[str]:
    if not path.exists():
        return [f"missing result file: {path}"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    lines = text.splitlines()
    for required in rule.get("required_exact_lines", []):
        if required not in lines:
            errors.append(f"missing exact line: {required}")
    for forbidden in rule.get("forbidden_substrings", []):
        if forbidden in text:
            errors.append(f"forbidden substring remains: {forbidden}")
    return errors


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    if not path.exists():
        return None, [f"missing result file: {path}"]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"invalid JSON in {path}: {exc}"]


def validate_json(path: Path, rule: dict[str, Any]) -> list[str]:
    actual, errors = load_json(path)
    if errors:
        return errors
    required = rule["required"]
    kind = rule["type"]

    if kind == "json-exact":
        if actual != required:
            errors.append(f"JSON does not exactly match expected result: expected={required!r} actual={actual!r}")
        return errors

    if kind == "json-subset":
        return contains_subset(actual, required)

    if kind == "json-numeric":
        if not isinstance(actual, dict):
            return ["result JSON must be an object"]
        tolerance = float(rule.get("tolerance", 0.0))
        if set(actual) != set(required):
            errors.append(
                f"result keys must match exactly: expected={sorted(required)} actual={sorted(actual) if isinstance(actual, dict) else actual}"
            )
            return errors
        for key, expected_value in required.items():
            value = actual[key]
            if isinstance(expected_value, (int, float)) and isinstance(value, (int, float)):
                if not math.isclose(float(value), float(expected_value), rel_tol=0.0, abs_tol=tolerance):
                    errors.append(f"{key}: expected {expected_value}, got {value}")
            elif value != expected_value:
                errors.append(f"{key}: expected {expected_value!r}, got {value!r}")
        return errors

    return [f"unsupported validation type: {kind}"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id")
    parser.add_argument("workspace", type=Path)
    parser.add_argument(
        "--ground-truth",
        type=Path,
        default=Path("validation/pilot/evaluator/ground-truth-v0.1.json"),
    )
    args = parser.parse_args()

    truth = json.loads(args.ground_truth.read_text(encoding="utf-8"))
    rule = truth["tasks"].get(args.task_id)
    if rule is None:
        raise SystemExit(f"Unknown task_id: {args.task_id}")

    result_path = args.workspace / rule["result_file"]
    if rule["type"] == "text-constraints":
        errors = validate_text(result_path, rule)
    else:
        errors = validate_json(result_path, rule)

    if errors:
        print(f"{args.task_id}: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"{args.task_id}: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
