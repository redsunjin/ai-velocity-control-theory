# Simulation Plan — v0.1

## 상태

**First simulation completed (2026-08-23).**

결과:
- `validation/results/first-simulation-v0.1.md`
- `validation/results/generated/coordination-summary.csv`
- `validation/results/generated/control-summary.csv`
- 재현 코드: `validation/simulations/avct_v01.py`

**Second control-architecture simulation completed (2026-08-24).**

결과:
- `validation/results/second-simulation-v0.1.md`
- `validation/results/generated/control-architecture-summary.csv`
- `validation/results/generated/verifier-sensitivity-summary.csv`
- `validation/results/generated/reversibility-summary.csv`
- 재현 코드: `validation/simulations/avct_v01_control_architecture.py`

---

# 1. 1차 시뮬레이션 — coordination + control saturation sanity check

## 목적

AVCT의 모든 주장을 한 번에 증명하지 않는다. 첫 시뮬레이션은 다음 네 현상이 최소 모형에서도 재현 가능한지 확인했다.

1. 에이전트 수 증가가 항상 유효 실행량을 비례 증가시키지는 않는다.
2. 조정 효율 저하는 병렬화 이익을 상쇄할 수 있다.
3. 통제 수요가 통제 처리율에 접근하면 backlog와 대기시간이 민감해진다.
4. 잠재 처리량은 증가하지만 실현 성과는 일정 구간 이후 둔화 또는 감소할 수 있다.

네 항목 모두 구조적 패턴은 재현됐지만 경험적 검증으로 취급하지 않는다.

## 최소 모델

시간을 discrete step으로 두었다.

1. `A`개의 에이전트에 비례해 후보 행동 생성
2. 후보 행동이 task target 선택
3. 동일 target 중복을 coordination loss로 처리
4. reliability `R`로 유효/오류 행동 분리
5. control-gated experiment에서 unique action을 queue로 전달
6. control server가 `μ_control`만큼 처리
7. 승인된 유효 행동을 realized performance에 반영
8. delay-sensitive condition에서는 review delay에 따라 action value 할인

## 판정

- H1/H2: 방향성 유지, 실제 coordination data 필요
- H5: queueing theory 연결 검산으로 분리
- H6: AVCT 핵심 연구 대상으로 유지

---

# 2. 2차 시뮬레이션 — control architecture + residual risk

## 핵심 질문

> **동일한 agentic execution capacity에서 control architecture가 potential throughput과 realized performance의 분리점을 얼마나 이동시키며, 그 이동이 residual risk를 악화시키지 않는 조건은 무엇인가?**

## 추가한 구조

### A. Risk-tiered control routing

- low risk: automated verification
- medium risk: automated verification + sample + escalation
- high risk: human gate

전수검토와 비교해 `q_control`과 `K`가 얼마나 달라지는지 측정했다.

### B. Verifier sensitivity analysis

Automated verifier sensitivity를 70%~99.5%까지 변화시켰다.

핵심 결과:

- 낮은 verifier sensitivity에서는 `K`는 감소하지만 unsafe escape가 증가
- 해당 toy assumptions에서 약 99% sensitivity 부근에서 full-review stable baseline과 유사한 unsafe-escape 수준 관찰

이 값은 현실 임계치가 아니다.

### C. Reversibility

동일 routing, 동일 `K`, 동일 unsafe-escape count에서 reversibility profile만 변경했다.

결과:

- error count는 변하지 않음
- harm / 1,000 executed actions는 감소

따라서 reversibility를 reliability보다 loss/recovery modifier로 보는 방향으로 이론을 수정했다.

## 판정

- H6/P6: 유지 및 강화
- H7/P7: **조건부 명제로 수정**
- H8: 유지, loss-severity modifier로 역할 명확화

---

# 3. 다음 단계 — simulation expansion보다 telemetry 우선

현재 v0.1에서는 synthetic simulation을 계속 복잡하게 만드는 것보다 **실제 agent workflow에서 측정 가능한 schema를 고정하는 작업**을 우선한다.

## 핵심 telemetry

### Execution layer
- agent count
- concurrency
- candidate action rate
- action type / target
- completion time

### Coordination layer
- duplicate action
- conflict / merge
- blocked dependency
- coordination messages
- useful output / agent

### Control layer
- risk tier
- automated / human / bypass route
- review arrival time
- service start / end
- approval / rejection
- escalation
- override

### Outcome layer
- realized valid output
- unsafe escape
- rollback
- rework
- recovery time / cost
- delay-adjusted value

---

# 4. 다음 시뮬레이션 후보

실제 telemetry 수집 전 필요한 경우에만 다음을 추가한다.

## A. Reviewer-quality feedback

`R_control = R_control(K, cognitive load, burstiness)`

- queue pressure가 높을 때 false approval / false rejection이 변하는지 sensitivity test

## B. Dependency graph → control demand

coordination conflict가 추가 review/escalation을 생성하도록 연결한다.

`coordination loss ↑ → Λ_control ↑`

## C. Verification frontier

automated verifier의:

- sensitivity
- specificity
- inference cost
- latency

를 동시에 변경하여 control architecture의 Pareto frontier를 비교한다.

---

# 5. v0.1 simulation exit criteria

현재 최소 simulation phase는 다음 조건을 충족했다.

- [x] P1/P2를 공격하는 coordination toy model
- [x] P5 queue connection 검산
- [x] P6 potential–realized divergence 재현
- [x] P7 risk-tiering의 반례/조건성 확인
- [x] H8 reversibility의 역할 분리
- [x] synthetic threshold를 실증 threshold와 명확히 구분

따라서 다음 단계는 **telemetry schema → small real agent workflow experiment**다.

시뮬레이션은 계속 **이론을 보호하는 작업이 아니라 이론을 공격하는 작업**으로 유지한다.
