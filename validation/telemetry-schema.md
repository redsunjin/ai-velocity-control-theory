# AVCT Telemetry Schema — v0.1

> 목적: AVCT의 핵심 변수를 실제 agentic workflow에서 측정하기 위한 최소 이벤트 계약. 특정 agent framework에 종속되지 않는다.

이 문서는 이론의 새 변수를 추가하기보다 다음 질문에 답할 데이터를 정의한다.

> 동일한 task set에서 agent/control architecture가 달라질 때 `N_eff`, `Λ_control`, `μ_control`, `K`, residual risk, recovery cost, realized value는 어떻게 달라지는가?

---

# 1. 설계 원칙

1. **Raw event를 먼저 보존한다.** 계산된 AVCT metric만 저장하지 않는다.
2. **Execution과 control을 별도 event stream으로 기록한다.**
3. **자동 검증과 인간 검토를 구분한다.**
4. **unsafe escape는 사후 ground truth가 있을 때만 확정한다.**
5. **실패·rollback·rework를 버리지 않는다.** AVCT에서는 이것이 성과의 일부다.
6. **시간은 단일 clock 기준으로 기록한다.** 가능하면 UTC ISO-8601 + monotonic duration을 함께 사용한다.
7. **민감정보와 원문 prompt/response 전체 저장은 기본값으로 요구하지 않는다.** 필요한 경우 hash/reference를 사용한다.

---

# 2. 공통 식별자

모든 event에 최소한 다음 필드를 둔다.

| field | type | 설명 |
|---|---|---|
| `run_id` | string | 한 번의 실험 실행 |
| `workflow_id` | string | 동일 workflow 유형 |
| `task_id` | string | 비교 가능한 작업 단위 |
| `event_id` | string | 고유 이벤트 |
| `event_type` | enum | execution / coordination / control / outcome |
| `ts` | datetime | 이벤트 시각 |
| `architecture_id` | string | 비교 대상 agent/control architecture |
| `experiment_condition` | string | A/B/C 등 실험 조건 |

권장:

- `parent_event_id`
- `trace_id`
- `agent_id`
- `model_id`
- `tool_name`

---

# 3. Execution events

## 필수 필드

| field | 설명 |
|---|---|
| `agent_id` | 행동을 생성한 agent |
| `action_id` | 실행 후보 또는 실행 행동 식별자 |
| `action_type` | read / analyze / write / test / external-call / deploy 등 |
| `target_id` | 파일, issue, API resource 등 행동 대상 |
| `candidate_at` | 행동이 생성된 시각 |
| `execute_started_at` | 실제 실행 시작 |
| `execute_finished_at` | 실행 종료 |
| `execution_status` | proposed / executed / blocked / failed / cancelled |

## 권장 필드

- `agent_concurrency_at_start`
- `retry_count`
- `token_or_compute_cost`
- `tool_latency_ms`
- `output_ref`

---

# 4. Coordination events

`S`를 직접 주관 점수로 입력하지 않고 관찰 가능한 proxy를 기록한다.

| field | 설명 |
|---|---|
| `coordination_type` | duplicate / conflict / dependency-block / merge / handoff / sync |
| `related_action_ids` | 관련 행동 목록 |
| `coordination_started_at` | 조정 시작 |
| `coordination_finished_at` | 조정 완료 |
| `resolution_status` | resolved / unresolved / superseded |
| `rework_actions` | 조정 실패 때문에 추가된 행동 수 |

### `S` proxy 후보

실증에서 하나의 고정식으로 바로 만들지 않는다. 우선 다음을 따로 측정한다.

- duplicate action rate
- conflict rate
- blocked-dependency time
- coordination latency
- rework actions / completed action
- useful unique output / agent-hour

---

# 5. Control events

## 핵심 필드

| field | 설명 |
|---|---|
| `control_id` | 통제 건 식별자 |
| `action_id` | 대상 행동 |
| `risk_tier` | low / medium / high 또는 실험 정의 |
| `control_route` | auto / human / sampled-human / bypass / blocked |
| `control_arrived_at` | 통제 큐 유입 시각 |
| `service_started_at` | 검토 시작 |
| `service_finished_at` | 검토 종료 |
| `controller_type` | automated-verifier / human / hybrid |
| `decision` | approve / reject / revise / escalate |
| `escalated` | bool |
| `override` | bool |

## 자동 검증용 권장 필드

- `verifier_id`
- `verifier_score`
- `verifier_threshold`
- `policy_rule_id`
- `evidence_ref`

## 인간 검토용 권장 필드

- `reviewer_id_hash`
- `review_duration_ms`
- `review_queue_depth_at_start`
- `reviewer_parallel_load`

개인 식별정보를 저장할 필요가 없다. 익명 hash 또는 역할 identifier로 충분하다.

---

# 6. Outcome events

| field | 설명 |
|---|---|
| `action_id` | 결과 대상 행동 |
| `ground_truth_status` | correct / incorrect / unknown |
| `unsafe_escape` | 검토를 통과하거나 우회한 부적절 행동이 실제 실행됐는지 |
| `detected_after_execution` | 사후 탐지 여부 |
| `rollback_required` | bool |
| `rollback_success` | bool / null |
| `rework_required` | bool |
| `recovery_started_at` | 복구 시작 |
| `recovery_finished_at` | 복구 종료 |
| `recovery_cost` | 실험에서 정의한 cost unit |
| `realized_value` | 실험에서 정의한 value unit |
| `external_impact` | none / reversible / irreversible 또는 별도 scale |

### 주의

`unsafe_escape`와 `harm`은 동일하지 않다.

- escape: 잘못된 행동이 control을 넘어 실제 실행됨
- harm: 그 행동 때문에 발생한 결과 비용

Reversibility는 주로 후자를 바꿀 수 있다.

---

# 7. Architecture manifest

각 `architecture_id`에 대해 별도 manifest를 둔다.

```yaml
architecture_id: tiered-v1
agent_count_target: 4
max_concurrency: 4
control:
  low: automated
  medium: automated-plus-sample
  high: human-gated
human_review_capacity: measured
rollback_supported: true
```

필수 기록:

- agent count / concurrency policy
- model(s)
- tool permissions
- authority boundary
- risk-routing rule
- automated verifier
- human review rule
- rollback / recovery mechanism

아키텍처가 달라졌는데 같은 이름을 재사용하지 않는다.

---

# 8. AVCT derived metrics

## Execution velocity

`λ_candidate = candidate actions / agent-time`

Raw tool calls와 구분한다.

## Effective Action Mass proxy

초기 실증에서는 `N_eff`를 수식으로 강제 계산하기보다 다음 관찰값을 사용한다.

`N_eff_observed = unique valid completed actions within T`

이 값을 이론식:

`A · λ · T · S · R`

과 비교하여 `S`, `R` proxy의 설명력을 검토한다.

## Control arrival rate

`Λ_control = control-arrival events / time`

## Effective control capacity

단순 명목 reviewer 수가 아니라 실제 처리율로 추정한다.

`μ_control_observed = completed control services / active service time`

queue가 충분히 공급된 구간과 그렇지 않은 구간을 구분한다.

## Control Saturation Ratio

`K_observed = Λ_control / μ_control_observed`

## Residual risk

최소 두 개를 분리한다.

- `unsafe_escape_rate = unsafe escapes / executed actions`
- `harm_rate = realized harm / executed actions`

## Recovery / reversibility

- rollback success rate
- mean recovery time
- recovery cost / error
- irreversible-impact rate

## Realized performance

한 개의 보편식으로 정의하지 않는다. 실험별 outcome을 사용한다.

예:

- valid merged changes / hour
- accepted analyses / hour
- task success adjusted for rework
- net value = gross task value - rework/recovery/delay cost

---

# 9. 최소 JSONL 예시

```json
{"run_id":"r01","task_id":"t17","event_id":"e101","event_type":"execution","architecture_id":"tiered-v1","agent_id":"a3","action_id":"ac88","action_type":"write","target_id":"src/x.py","candidate_at":"2026-08-24T01:00:01Z","execute_started_at":"2026-08-24T01:00:02Z","execute_finished_at":"2026-08-24T01:00:04Z","execution_status":"executed"}
{"run_id":"r01","task_id":"t17","event_id":"e102","event_type":"control","architecture_id":"tiered-v1","control_id":"c88","action_id":"ac88","risk_tier":"medium","control_route":"automated-plus-sample","control_arrived_at":"2026-08-24T01:00:04Z","service_started_at":"2026-08-24T01:00:04Z","service_finished_at":"2026-08-24T01:00:05Z","controller_type":"automated-verifier","decision":"approve","escalated":false,"override":false}
{"run_id":"r01","task_id":"t17","event_id":"e103","event_type":"outcome","architecture_id":"tiered-v1","action_id":"ac88","ground_truth_status":"correct","unsafe_escape":false,"rollback_required":false,"rework_required":false,"recovery_cost":0,"realized_value":1,"external_impact":"none"}
```

---

# 10. 최소 실험 성공 조건

첫 실증에서는 모든 필드를 완벽히 수집할 필요가 없다.

다음 10개가 안정적으로 수집되면 시작 가능하다.

1. architecture_id
2. task_id
3. agent_id
4. action_id / action_type
5. candidate / execution timestamps
6. risk tier / control route
7. control arrival / service timestamps
8. control decision
9. task/action outcome
10. rollback/rework 여부

이 데이터만으로도:

- execution rate
- duplicate/rework proxy
- `Λ_control`
- observed service rate
- `K`
- realized throughput
- residual error/recovery

를 비교할 수 있다.

---

# 11. Privacy / research hygiene

- 개인정보, 비밀키, 고객 데이터, 원문 credential을 telemetry에 저장하지 않는다.
- prompt/output 전문이 필요하지 않으면 hash/reference만 저장한다.
- architecture 비교 전에 metric 정의를 고정한다.
- 결과를 보고 metric을 바꾸는 경우 changelog에 기록한다.
- 실패한 run을 삭제하지 않는다.
- synthetic test와 actual workflow data를 같은 dataset으로 섞지 않는다.

---

# 12. AVCT와의 연결

이 schema의 목적은 `K` 하나를 계산하는 것이 아니다.

최종적으로 다음 frontier를 실제 데이터로 그릴 수 있어야 한다.

> **execution capacity × coordination efficiency × control load × residual risk × recovery × realized value**

만약 이 telemetry로도 AVCT의 연결 모델이 기존 독립 metric보다 추가적인 설명력이나 설계 가치를 주지 못한다면, AVCT의 별도 이론 지위는 약화되어야 한다.
