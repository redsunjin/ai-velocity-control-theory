# E1/C1 Real-Agent Pilot Runbook — v0.1

> Stage: Phase 0b preparation. Do not call results empirical until the architecture manifest is fully pinned and real task telemetry is committed.

## Goal

Run five bounded tasks with:

- one active agent;
- concurrency 1;
- full human gate for state-changing actions;
- isolated Git branches;
- deterministic/rubric ground truth;
- AVCT JSONL telemetry.

The purpose is **instrumentation validation**, not performance comparison.

## Pre-run gate

Do not start the first real task until `architecture-e1c1-template.yaml` has no `MUST_PIN_BEFORE_RUN` values.

Pin:

- runner and version
- model/provider/snapshot
- reasoning/effort setting if applicable
- tool permissions
- network access policy
- instruction/prompt version

Commit the frozen manifest and record its SHA.

## Task order

Use `task-set-v0.1.json` in this order:

1. `pilot-t01` deprecated-theory-patch
2. `pilot-t02` architecture-manifest-repair
3. `pilot-t03` telemetry-metric-derivation
4. `pilot-t04` coordination-duplicate-analysis
5. `pilot-t05` reversible-config-change

Do not reorder after seeing early results unless the run is explicitly restarted with a new pilot version.

## Per-task branch

Create a clean branch from the same declared baseline.

Recommended naming:

`pilot/e1c1/<run-id>/<task-id>`

A task branch must not include changes from the previous task.

## Event capture sequence

For each state-changing candidate action:

1. log execution candidate/event identifiers;
2. create the matching control-arrival event;
3. reviewer starts service and records the decision;
4. if approved/revised, execute in the bounded workspace;
5. run deterministic test/rubric evaluation;
6. log outcome;
7. if needed, log rollback/rework and recovery timing.

Read/search actions may be instrumented for execution-rate analysis but do not require human gating in E1/C1 unless the runner itself requires it.

## Required telemetry file layout

Recommended:

```text
validation/empirical/raw/<run-id>/<task-id>.jsonl
validation/empirical/manifests/<architecture-id>.yaml
validation/empirical/rubrics/<task-id>.md
validation/empirical/results/<run-id>-metrics.json
validation/empirical/results/<run-id>-review.md
```

Do not store fixture telemetry under `validation/empirical/`.

## Validation after each task

Run:

```bash
python validation/telemetry/validate_telemetry.py \
  validation/empirical/raw/<run-id>/<task-id>.jsonl
```

If validation fails:

- do not silently edit timestamps or IDs to make the file pass;
- identify whether the failure is agent behavior, reviewer logging, schema ambiguity, or instrumentation failure;
- record the correction as a new event or documented data-repair step;
- if raw telemetry must be altered, preserve the original and record the transformation.

## End-of-run derivation

Concatenate the five task traces only after each individual trace validates, then run:

```bash
python validation/telemetry/derive_metrics.py \
  validation/empirical/raw/<run-id>/combined.jsonl \
  --output validation/empirical/results/<run-id>-metrics.json
```

The first pilot should report at minimum:

- candidate actions
- executed actions
- `N_eff_observed`
- `Λ_control`
- `μ_control_observed`
- `K_observed`
- human review duration
- unsafe escapes
- rework / rollback
- recovery cost
- realized value
- missing-event / traceability rate
- instrumentation overhead

## Stop conditions

Stop the pilot and keep Phase 0b open if any of these occur:

1. telemetry requires credentials, personal data, or raw sensitive payloads;
2. the runner cannot preserve stable action IDs across control/outcome events;
3. more than 5% of state-changing actions cannot be traced after one repair attempt;
4. ground truth cannot be decided from the pre-written rubric/test;
5. the task escapes the isolated repository boundary;
6. instrumentation changes agent behavior so much that the pilot no longer resembles the intended workflow;
7. the architecture manifest changes mid-run.

A stopped run is a valid instrumentation result and must be retained.

## Phase 0b report template

For each run, report:

### Architecture
- manifest SHA:
- runner/model:
- toolset:
- task baseline SHA:

### Traceability
- state-changing actions:
- fully linked actions:
- traceability rate:
- missing-link causes:

### Privacy
- validator privacy errors:
- manual sensitive-data inspection:

### Metrics
- `N_eff_observed`:
- `Λ_control`:
- `μ_control_observed`:
- `K_observed`:
- unsafe escape rate:
- rollback/rework:
- recovery cost:
- realized value:

### Instrumentation overhead
- logging time:
- reviewer logging time:
- extra actions caused by instrumentation:

### Decision
- proceed to Phase 1 / revise telemetry / revise task set / stop

## Interpretation rule

No result from this five-task E1/C1 pilot should be used to claim that AVCT predicts organizational performance.

The only allowed conclusion is whether the instrumentation, ground-truth process, and control-event linkage are usable enough to begin the comparative experiment.
