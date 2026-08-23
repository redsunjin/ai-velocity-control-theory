# Simulation Plan — v0.1

## 상태

**First simulation completed (2026-08-23).**

결과:
- `validation/results/first-simulation-v0.1.md`
- `validation/results/generated/coordination-summary.csv`
- `validation/results/generated/control-summary.csv`
- 재현 코드: `validation/simulations/avct_v01.py`

---

## 1차 목적

AVCT의 모든 주장을 한 번에 증명하려 하지 않는다. 첫 시뮬레이션의 목적은 다음 네 현상이 최소 모형에서도 재현 가능한지 확인하는 것이었다.

1. 에이전트 수 증가가 항상 유효 실행량을 비례 증가시키지는 않는다.
2. 조정 효율 저하는 병렬화 이익을 상쇄할 수 있다.
3. 통제 수요가 통제 처리율에 접근하면 backlog와 대기시간이 민감해진다.
4. 잠재 처리량은 증가하지만 실현 성과는 일정 구간 이후 둔화 또는 감소할 수 있다.

네 항목 모두 구조적 패턴은 재현됐지만 경험적 검증으로 취급하지 않는다.

---

## 1차 최소 모델

시간을 discrete step으로 두었다.

각 step에서:

1. `A`개의 에이전트에 비례해 후보 행동이 생성된다.
2. 후보 행동이 task target을 선택한다.
3. 동일 target의 중복 실행을 coordination loss로 처리한다.
4. reliability `R`에 따라 유효/오류 행동을 나눈다.
5. control-gated experiment에서는 unique action을 control queue로 보낸다.
6. control servers가 `μ_control`만큼 처리한다.
7. 승인된 유효 행동은 realized performance에 반영한다.
8. delay-sensitive condition에서는 review delay에 따라 action value를 할인한다.

## 1차 변수

### 조작 변수
- `A`: 1, 2, 4, 8, 16, 32
- `λ`: 1.5 / agent / step 고정
- task coupling proxy: low / high
- `μ_control`: 6 / 12 / 24
- delay decay: 0 / 0.03

### 중간 변수
- `S`
- `Λ_control`
- `K`
- queue length
- mean review delay

### 결과 변수
- raw actions
- valid unique actions
- approved actions
- realized performance

---

# 2차 시뮬레이션 계획

첫 결과로 인해 다음 단계의 목적을 좁힌다.

## 핵심 질문

> **동일한 agentic execution capacity에서 control architecture가 potential throughput과 realized performance의 분리점을 얼마나 이동시키는가?**

## 추가할 구조

### A. Dependency graph based coordination

단순 target-pool proxy 대신 task dependency graph를 사용한다.

비교 후보:
- independent tasks
- sparse dependencies
- dense dependencies
- shared bottleneck dependency

측정:
- duplicate/conflict rate
- blocked tasks
- coordination messages
- useful output / agent

### B. Risk-tiered control routing

모든 action을 검토하는 `q_control=1` 가정을 폐기하고 action별 risk tier를 둔다.

예:
- low risk: auto-execute
- medium risk: sampled / automated review
- high risk: human-gated review

측정:
- `q_control`
- human review load
- unsafe escape rate
- realized performance

### C. Reversibility

action을 reversible / irreversible로 분리한다.

동일한 오류라도 rollback 가능한 action과 외부 피해가 즉시 발생하는 action의 손실함수를 다르게 둔다.

### D. Reliability feedback

첫 모델에서는 `R=0.95`를 고정했다.

2차에서는 다음 후보를 비교한다.

- `R` independent of K
- reviewer pressure가 높을 때 false approval 증가
- coordination pressure가 높을 때 agent error/conflict 증가

구체 함수는 이론으로 선언하지 않고 sensitivity analysis로 비교한다.

---

## 2차 성공 기준

- H6의 포화/역전이 특정 decay 함수 하나에만 의존하는지 공격
- H7 risk-tiering이 `q_control`을 낮추면서 손실을 증가시키지 않는 영역 탐색
- H8 reversibility가 동일 K의 실제 손실을 얼마나 다르게 만드는지 탐색
- P6/P7을 실제 조직 데이터로 옮길 수 있는 최소 telemetry schema 도출

시뮬레이션은 계속 **이론을 보호하는 작업이 아니라 이론을 공격하는 작업**으로 유지한다.
