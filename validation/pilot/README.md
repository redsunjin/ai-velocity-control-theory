# AVCT Empirical Pilot — Phase 0

> Status: instrumentation pilot, **not empirical evidence**.

## Selected workflow

The first bounded workflow is **repository-local software / analysis work performed on isolated Git branches with deterministic or rubric-based validation**.

It was selected because it allows agent execution, review, rollback, and ground-truth events to be measured without touching production systems, customers, credentials, payments, or irreversible external resources.

### Allowed

- repository read/search
- bounded Markdown or config edits
- local deterministic analysis
- local test execution
- branch-local file writes
- reversible commits
- structured output checked against a fixed rubric

### Excluded

- production deployment
- external customer communication
- payment or billing changes
- personal data processing
- secret/credential access
- destructive infrastructure actions
- irreversible third-party API writes

## Pilot task family

The initial task set contains five task types.

1. **Deprecated-theory patch** — update an intentionally stale K definition while preserving stated theory boundaries.
2. **Architecture-manifest repair** — repair a bounded control architecture manifest against a fixed checklist.
3. **Telemetry metric derivation** — derive AVCT metrics from a provided JSONL event stream and match expected values.
4. **Coordination duplicate analysis** — identify duplicate/conflicting actions in a small structured dataset.
5. **Reversible config change** — make a branch-local configuration change, run deterministic validation, and record rollback/rework if validation fails.

The task definitions live in `task-set-v0.1.json`.

## Why this is useful for AVCT

This workflow can generate all four event classes required by the current telemetry model:

- execution
- coordination
- control
- outcome

It also supports the first real comparison axes later:

- E1/C1: one agent + full gate
- E2/C1: four agents + full gate
- E2/C2: four agents + risk-tiered control
- E2/C3: four agents + risk-tiered control + stronger reversibility

Phase 0 does **not** run those comparative conditions yet. It only verifies that the instrumentation can represent and validate them.

## Phase 0 fixture

`../telemetry/samples/pilot-events.jsonl` contains four synthetic/fixture tasks used only to test event linkage and derived-metric code.

Important:

- fixture events are not agent experiment results;
- fixture values must never be mixed with later empirical data;
- passing the fixture means the telemetry implementation is internally consistent, not that AVCT is supported.

## Phase 0 exit test

Instrumentation is ready for a real 3–5 task pilot when all of the following pass in CI:

- every event has the required common fields;
- type-specific required fields are present;
- control/outcome actions link to execution actions;
- event IDs are unique;
- timestamps parse as UTC/offset-aware ISO-8601;
- known sensitive payload keys are rejected;
- `Λ_control`, `μ_control_observed`, `K_observed`, residual risk, recovery cost, and realized value can be derived from raw fixture events;
- derived values match a committed expected-metrics fixture.

## Next step after Phase 0

Run 3–5 **real agent** tasks under E1/C1 only to verify instrumentation overhead and ground-truth workflow before freezing the full 24–40 task experiment.
