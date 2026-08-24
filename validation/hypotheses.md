# Validation Hypotheses — v0.1

이 문서는 개념 명제를 실제 검증 가능한 가설로 변환하기 위한 초안이다.

## H1 — 병렬성의 체감효과

에이전트 수 `A`를 증가시키면 총 후보 실행량은 증가하지만, 작업 결합도가 높은 조건에서는 `N_eff / A`가 감소할 수 있다.

측정 후보:
- completed valid tasks / agent
- duplicate work rate
- conflict rate
- coordination latency

**첫 시뮬레이션:** 방향성 재현. 단순 contention proxy에 의존하므로 실증 필요.

## H2 — 조정 효율의 매개효과

`A`가 `N_eff`에 미치는 효과는 `S`에 의해 매개될 수 있다.

예상:
- 독립 작업: 높은 `S`, 더 긴 scale-out 구간
- 상호의존 작업: `A` 증가에 따라 `S` 하락 가능

**첫 시뮬레이션:** high-coupling proxy에서 `S` 하락이 더 강하게 재현됨. 함수형은 미확정.

## H3 — 속도-신뢰도 trade-off

일정 수준 이상에서 per-agent execution rate `λ`를 높이면 `R`이 감소할 수 있다.

단, 이 효과는 모델·작업·검증 구조에 따라 존재하지 않을 수도 있다.

## H4 — 비선형 성과의 조건성

시장 선점 또는 빠른 학습 피드백이 존재하는 환경에서는 `β > 1`이 관찰될 가능성이 있고, 단순 반복 처리 환경에서는 `β ≤ 1`일 가능성이 있다.

## H5 — 통제포화와 대기시간

`K`가 증가할수록 평균 통제 대기시간과 backlog가 증가한다.

이 가설은 기존 queueing theory와의 정합성을 확인하는 **연결성 검산**으로 취급하며 AVCT의 신규성 주장이 아니다.

**첫 시뮬레이션:** `K≈1` 부근의 지연 민감도와 `K>1` backlog 누적이 재현됨.

## H6 — 잠재 처리량과 실현 성과의 분리

잠재 실행량이 증가하더라도 control capacity가 병목이 되면 potential throughput과 realized performance가 분리될 수 있다.

예상 조건:
- time-insensitive workflow: realized performance의 증가율이 포화될 수 있음
- delay/error/rework cost가 큰 workflow: realized performance가 감소하는 역전도 가능

측정 후보:
- net valid outputs after rework
- time-to-safe-deployment
- customer-impact-adjusted throughput
- rollback/recovery cost
- opportunity-value decay during review

**첫 시뮬레이션:** `decay=0`에서는 포화, delay-sensitive 가정에서는 하락을 재현.

**두 번째 시뮬레이션:** control architecture가 saturation/divergence point를 이동시킴을 재현. full review는 synthetic `A≈8`에서 `K≈1`에 도달했지만 tiered architecture는 동일 `μ_control`에서 `A=32~64` 사이로 포화점이 이동했다. 이 이동폭은 risk mix와 verification assumptions에 종속적이다.

## H7 — 위험 기반 라우팅의 조건부 효과

동일한 raw execution capacity에서 risk-tiering과 exception-based review는 human control arrival rate와 `K`를 낮출 수 있다.

그러나 지속 가능한 개선으로 간주하려면 다음 조건이 함께 만족되어야 한다.

- residual unsafe-escape rate가 허용 가능한 risk budget 안에 있을 것
- harm / recovery cost가 허용 가능한 수준일 것
- realized net value가 악화되지 않을 것

**두 번째 시뮬레이션:** stable full-review baseline `A=4`에서 `K≈0.50`이던 조건이 tiered routing에서는 `K≈0.074`로 감소했다. 그러나 automated verifier sensitivity가 낮을수록 unsafe escape가 증가했다. 해당 toy assumptions에서는 약 99% sensitivity 부근에서 full-review와 유사한 unsafe-escape 수준이 관찰됐다.

중요: 이 99%는 실제 시스템의 threshold가 아니라 synthetic sensitivity boundary다.

따라서 H7의 검증 목표는 `K` 감소 자체가 아니라 **control-load reduction과 residual-risk preservation의 joint frontier**다.

## H8 — reversibility의 완충효과

동일한 control routing과 동일한 unsafe-escape count에서 reversibility가 높은 시스템은 error consequence와 recovery loss를 낮출 가능성이 있다.

**두 번째 시뮬레이션:** tiered-90 architecture에서 `K`와 unsafe-escape count를 동일하게 유지하고 reversibility profile만 변경했을 때 harm / 1,000 executed actions가 약 38~41% 감소했다.

따라서 H8에서 reversibility는 reliability 자체보다 **loss severity modifier**로 측정한다.

---

# 현재 판정

| 가설 | 상태 | 이유 |
|---|---|---|
| H1 | 유지 | toy coupling model + SILO-BENCH와 방향 정합, 실증 필요 |
| H2 | 유지 | coordination efficiency의 조건성 유지 |
| H3 | 미검증 | speed/reliability feedback 실험 필요 |
| H4 | 미검증 | 실제 시장/학습 메커니즘 필요 |
| H5 | borrowed baseline | queueing theory 연결 검산 |
| H6 | 핵심 유지 | 두 toy model에서 architecture-dependent divergence 재현 |
| H7 | **조건부로 수정** | load 감소만으로는 부족; verifier quality/residual risk 필요 |
| H8 | 유지 | reversibility를 loss modifier로 재정의 |

---

# 다음 최소 검증 세트

다음 단계는 **실제 agent workflow telemetry**로 옮기는 준비다.

1. `A`, concurrency, candidate action rate 측정
2. duplicate/conflict/blocked task로 `S` proxy 수집
3. risk tier별 `q_control`, human/automated review path 기록
4. `Λ_control`, service time, `μ_control`, queue delay 측정
5. unsafe escape, rollback, rework, recovery cost 기록
6. realized output과 delay-adjusted value를 연결

시뮬레이션을 추가한다면 우선순위는:

1. reviewer sensitivity가 `K`/cognitive load에 따라 저하되는 feedback
2. verifier sensitivity/specificity/cost joint sensitivity
3. dependency graph coordination → additional control demand 연결

시뮬레이션은 계속 **이론을 보호하는 작업이 아니라 이론을 공격하는 작업**으로 유지한다.
