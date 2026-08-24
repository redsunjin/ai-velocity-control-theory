#!/usr/bin/env python3
"""Materialize one AVCT pilot task into an isolated agent workspace.

Only task instructions and workspace input files are copied. Evaluator ground truth
is intentionally excluded so the runner can scope the agent to the output folder.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id")
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--spec",
        type=Path,
        default=Path("validation/pilot/task-fixtures-v0.1.json"),
    )
    args = parser.parse_args()

    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    task = next((t for t in spec["tasks"] if t["task_id"] == args.task_id), None)
    if task is None:
        raise SystemExit(f"Unknown task_id: {args.task_id}")

    if args.output.exists() and any(args.output.iterdir()):
        raise SystemExit(f"Output directory is not empty: {args.output}")
    args.output.mkdir(parents=True, exist_ok=True)

    task_md = (
        f"# {task['task_id']} — {task['title']}\n\n"
        f"{task['instructions']}\n\n"
        f"Expected result file: `{task['result_file']}`\n"
    )
    (args.output / "TASK.md").write_text(task_md, encoding="utf-8")

    for relative, content in task["workspace_files"].items():
        destination = args.output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    print(f"Materialized {args.task_id} in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
