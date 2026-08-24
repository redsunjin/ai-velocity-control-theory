# Phase 0b Fresh-Agent Execution Handoff

> This handoff is for the **first real E1/C1 instrumentation check**. The agent that performs the five tasks must be a fresh context that has not seen evaluator ground truth.

## Why a fresh context is mandatory

The theory-development context has already inspected:

`validation/pilot/evaluator/ground-truth-v0.1.json`

Using that same context as the experimental task agent would contaminate the result.

The task agent must therefore run in a separate context/workspace with access only to the materialized task directory and the explicitly allowed toolchain.

## Before execution

1. Copy `validation/pilot/architecture-e1c1-template.yaml` to a new frozen manifest under `validation/empirical/manifests/`.
2. Replace every `MUST_PIN_BEFORE_RUN` value with the actual execution environment:
   - runner and version
   - model/provider/snapshot
   - reasoning/effort setting if applicable
   - network policy
   - tool permissions
   - prompt/instruction version
3. Commit the manifest and record its SHA.
4. Do not change the architecture during the five-task pilot. If it changes, create a new architecture ID and restart affected tasks.

## Agent workspace isolation

For each task, materialize an isolated workspace outside the repository root, for example:

```bash
python validation/pilot/materialize_task.py \
  pilot-t01 \
  /tmp/avct-pilot/<run-id>/pilot-t01
```

Launch the task agent with `/tmp/avct-pilot/<run-id>/pilot-t01` as its visible workspace.

Do **not** expose:

- `validation/pilot/evaluator/`
- repository-wide ground-truth files
- results from later pilot tasks
- previous task solutions

## Fixed task order

1. `pilot-t01`
2. `pilot-t02`
3. `pilot-t03`
4. `pilot-t04`
5. `pilot-t05`

Do not reorder after results are observed.

## E1/C1 control rule

- one active agent
- concurrency 1
- full gate for state-changing workspace actions
- read/search may be ungated unless the runner requires otherwise
- branch/workspace changes remain reversible
- no production, customer, payment, PII, credential, or irreversible external actions

If the runner cannot expose or intercept state-changing action events well enough to create stable `action_id` links, record this as an instrumentation failure rather than inventing action events after the fact.

## Telemetry

Write raw task telemetry to:

```text
validation/empirical/raw/<run-id>/<task-id>.jsonl
```

Each state-changing action should be traceable through:

`execution → control → outcome`

Validate after every task:

```bash
python validation/telemetry/validate_telemetry.py \
  validation/empirical/raw/<run-id>/<task-id>.jsonl
```

Do not silently repair identifiers/timestamps to make validation pass. Preserve original data and document any repair.

## Ground-truth evaluation

After the task agent finishes, the controller/evaluator — not the task agent — runs:

```bash
python validation/pilot/validate_task_result.py \
  <task-id> \
  /tmp/avct-pilot/<run-id>/<task-id>
```

The agent must not read the evaluator ground-truth file before or during the task.

## End-of-run metrics

After all valid traces are combined:

```bash
python validation/telemetry/derive_metrics.py \
  validation/empirical/raw/<run-id>/combined.jsonl \
  --output validation/empirical/results/<run-id>-metrics.json
```

Report:

- traceability rate
- candidate/executed actions
- `N_eff_observed`
- `Λ_control`
- `μ_control_observed`
- `K_observed`
- human review duration
- unsafe escapes
- rework/rollback
- recovery cost
- realized value
- instrumentation overhead

## Phase 0b acceptance

Proceed to the 24–40 task comparative design only if:

- 3–5 real tasks are completed or a stopped run is properly recorded;
- architecture fields were pinned before execution;
- telemetry validates without hidden repair;
- at least 95% of state-changing actions are linked execution→control→outcome;
- no prohibited sensitive payload is present;
- ground truth can be reproduced from the frozen evaluator;
- instrumentation overhead is reported.

## Interpretation

This pilot does not test whether AVCT predicts organizational performance.

It tests whether AVCT's proposed measurements can be collected reliably enough to justify a larger comparative experiment.
