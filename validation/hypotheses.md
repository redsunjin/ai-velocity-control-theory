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

**첫 시뮬레이션:** `decay=0`에서는 포화, delay-sensitive 가정에서는 하락을 재현. 하락 강도는 손실함수 가정에 민감함.

## H7 — 위험 기반 라우팅의 효과

동일한 실행량에서 risk-tiering과 exception-based review를 적용하면 `q_control`과 평균 인간 검토 부담이 감소할 수 있다.

## H8 — reversibility의 완충효과

동일한 `K`에서 reversibility가 높은 시스템은 오류의 총 손실과 복구 시간을 낮출 가능성이 있다.

---

# 다음 최소 검증 세트

첫 시뮬레이션(H1/H2/H5/H6)은 완료했다.

다음 시뮬레이션은 **H6/H7**을 우선한다.

1. `q_control < 1`을 허용하고 risk-tiered routing을 추가
2. 동일 raw throughput에서 control architecture에 따라 포화점이 이동하는지 측정
3. reversible / irreversible action을 분리해 H8 준비

첫 실증 또는 실제 사례 연구에서는 H5 그 자체보다 **H6/H7**을 우선한다.
