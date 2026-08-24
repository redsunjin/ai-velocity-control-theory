# Bounded Empirical Validation Plan — AVCT v0.1

> 목적: AVCT를 현실 전체에 검증하려 하지 않고, 동일한 bounded task set을 서로 다른 agent/control architecture로 실행해 **측정 가능성과 방향성**을 먼저 검증한다.

본 실험은 제품 성능 벤치마크가 아니라 AVCT 변수와 Execution–Control Frontier가 실제 workflow에서 유용한지 확인하기 위한 첫 실증 설계다.

---

# 1. 연구 질문

## RQ1 — Execution scale

Agent count / concurrency가 증가할 때 candidate execution volume과 unique valid output은 어떻게 달라지는가?

## RQ2 — Coordination

병렬성이 증가할 때 duplicate/conflict/rework가 증가하여 scale-out efficiency를 제한하는가?

## RQ3 — Control demand

같은 task set에서 control architecture가 `Λ_control`, observed `μ_control`, `K`를 얼마나 바꾸는가?

## RQ4 — Potential–realized divergence

Potential output 증가가 실제 valid completed output / time으로 이어지지 않는 divergence point가 관찰되는가?

## RQ5 — Control frontier

Human-control load를 줄이는 architecture가 residual risk와 recovery cost를 악화시키지 않으면서 realized value를 개선하는 구간이 존재하는가?

---

# 2. 첫 실험 대상

**Bounded software / analysis workflow**를 권장한다.

조건:

- task 완료 여부를 비교적 객관적으로 판단할 수 있음
- rollback/rework 기록 가능
- 외부 고객/운영 시스템에 직접 피해를 주지 않음
- 동일 또는 동등 난이도 task set을 여러 architecture에서 반복 가능
- agent action / control event를 instrumentation 가능

예시 task category:

- 문서와 코드의 일관성 검사
- 명시된 범위의 small refactor
- deterministic test가 있는 bug fix
- structured data extraction / comparison
- repository analysis with expected-answer rubric

**실제 production deploy, 결제, 개인정보 변경, irreversible external action은 첫 실험에서 제외한다.**

---

# 3. 실험 단위

첫 목표:

- 24~40 bounded tasks
- 난이도 2~3 strata
- architecture condition당 동일 task set 또는 randomized matched set
- 가능하면 condition당 3회 이상 반복

처음부터 통계적 일반화를 주장하지 않는다. 목적은 telemetry가 실제로 수집되고 이론 변수의 operationalization이 가능한지 보는 것이다.

---

# 4. 비교 architecture

두 축을 분리해서 비교한다.

## Execution scale axis

### E1 — Low concurrency

- 1 active agent
- 동일 model/tool permission

### E2 — Moderate concurrency

- 4 active agents
- 동일 model/tool permission

### E3 — Higher bounded concurrency

- 8 active agents
- 실제 실험 자원과 task 독립성이 허용하는 경우에만 사용

목적:

- `A` 증가
- candidate action rate 증가
- unique valid output 증가율
- coordination overhead

을 비교한다.

## Control architecture axis

### C1 — Full gate

중요 write/execute action을 인간 검토 대상으로 둔다.

### C2 — Risk-tiered

예시:

- low: auto-execute + log
- medium: automated verification + sample/escalation
- high: human gate

### C3 — Risk-tiered + reversibility

C2와 같은 routing을 쓰되 rollback checkpoint / branch isolation / reversible transaction을 강화한다.

---

# 5. 권장 factorial design

초기에는 전체 3×3을 다 돌릴 필요가 없다.

Phase A:

| Condition | Execution | Control |
|---|---|---|
| A1 | E1 | C1 |
| A2 | E4 | C1 |
| A3 | E4 | C2 |
| A4 | E4 | C3 |

여기서 `E4`는 4-agent moderate concurrency를 뜻한다.

이 비교로:

1. single → parallel execution 효과
2. full gate → tiered control 효과
3. tiered → reversible tiered 효과

를 분리한다.

그 후 필요하면 E8까지 확장한다.

---

# 6. 사전 고정 metric

결과를 본 뒤 유리한 지표를 선택하지 않도록 다음을 실험 전에 고정한다.

## Primary metrics

1. **valid completed tasks / hour**
2. **unique valid actions / agent-hour**
3. **human control arrivals / hour**
4. **human review time / task**
5. **unsafe escape / 1,000 executed actions**
6. **rework + rollback events / task**
7. **recovery time / failed action**

## Derived AVCT metrics

- candidate action rate `λ_candidate`
- observed `N_eff`
- duplicate/conflict rate
- observed `Λ_control`
- observed `μ_control`
- `K_observed`
- realized output / time
- residual-risk rate

## Secondary metrics

- token / compute cost
- wall-clock task time
- tool-call count
- coordination messages
- reviewer queue depth

---

# 7. Ground truth / outcome 판정

실증에서 가장 중요한 문제는 `R`과 unsafe escape의 판정 기준이다.

가능하면 다음 순서로 사용한다.

1. deterministic test / schema validation
2. pre-written answer rubric
3. independent reviewer blind review
4. 사후 incident / rollback 기록

단일 agent가 자기 결과를 자기 ground truth로 판정하지 않는다.

자동 verifier 결과와 최종 ground truth를 별도로 저장하여:

- sensitivity
- specificity
- false-negative escape
- false-positive escalation

을 계산할 수 있게 한다.

---

# 8. Risk-tier 예시

첫 software workflow에서는 다음처럼 단순화할 수 있다.

## Low

- read/search
- local analysis
- temporary artifact creation
- non-destructive test execution

## Medium

- tracked file write
- code modification
- dependency/config modification in isolated branch

## High

- merge to protected branch
- external API write
- deploy/release
- credential/permission change
- destructive/delete operation

첫 실험에서는 high-risk 실제 실행을 최소화하고, 가능한 경우 **simulated approval target**으로 둔다.

---

# 9. 실행 절차

## Step 0 — Instrumentation validation

3~5 pilot tasks로:

- event IDs 연결
- timestamp ordering
- control queue 기록
- outcome linkage

를 확인한다.

## Step 1 — Task-set freeze

task list, rubric, risk tier, expected validation method를 실험 전에 commit한다.

## Step 2 — Architecture manifest freeze

각 condition의:

- model
- prompts/instructions
- agent count
- concurrency
- permissions
- control routing
- verifier
- human-review rule
- rollback support

를 commit한다.

## Step 3 — Run

각 run은 새 `run_id`를 사용한다.

실패한 run도 보존한다.

## Step 4 — Outcome validation

실험 condition을 가능한 범위에서 blind 처리한 뒤 outcome을 판정한다.

## Step 5 — Analysis

먼저 raw operational metrics를 보고, 그 다음 AVCT derived metrics를 계산한다.

---

# 10. 반증 기준

첫 실험은 이론을 확인하기 위한 것이 아니다.

## P1/P2 약화 조건

Agent count가 증가해도 duplicate/conflict/rework가 사실상 증가하지 않고 unique valid output이 안정적으로 선형 이상 scale한다면 coordination-limit 명제는 해당 workflow에서 약화된다.

## P6 약화 조건

실행 capacity가 증가하는 모든 tested range에서 realized performance도 비례 증가하며 control variables가 설명력을 추가하지 못하면 potential–realized divergence 명제는 약화된다.

## P7 약화 조건

Risk-tiered control이 human load는 줄이지만 residual risk나 realized value를 반복적으로 악화시키거나, full gate 대비 유의미한 frontier 개선을 만들지 못한다면 control-architecture 생산성 명제는 약화된다.

## AVCT 자체 약화 조건

기존의 단순 metrics:

- task throughput
- queue utilization
- error rate

만으로 결과를 충분히 설명하고 `N_eff`/coupled frontier가 추가 의사결정 가치를 주지 못한다면 AVCT는 별도 이론보다 synthesis framework로 남는 것이 적절하다.

---

# 11. 첫 실험의 성공 기준

이론을 '증명'하는 것이 성공이 아니다.

성공은 다음이다.

- [ ] task set을 재현할 수 있음
- [ ] architecture를 명시적으로 재현할 수 있음
- [ ] telemetry event 95% 이상이 traceable함
- [ ] candidate action → control → outcome 연결 가능
- [ ] `Λ_control`, observed `μ_control`, `K` 계산 가능
- [ ] duplicate/conflict/rework 측정 가능
- [ ] unsafe escape와 rollback/recovery 구분 가능
- [ ] P1/P2/P6/P7 중 최소 하나에 반례 또는 지지 방향을 기록할 수 있음

---

# 12. RoundZero와의 관계

이 실험 결과가 나오기 전에도 AVCT v0.1은 **소설의 conceptual baseline**으로 사용할 수 있다.

다만 RoundZero에는 다음만 전달한다.

- 속도×병렬성은 공짜 전력이 아님
- control saturation은 queueing과 human/technical capacity 문제임
- 낮은 `K`가 자동으로 안전함을 뜻하지 않음
- control architecture에는 residual-risk trade-off가 있음
- reversibility는 실패의 결과를 바꿈

실험의 synthetic 수치나 verifier 99% 같은 값을 소설의 '과학적 법칙'으로 사용하지 않는다.
