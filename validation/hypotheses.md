# Validation Hypotheses — v0.1

이 문서는 개념 명제를 실제 검증 가능한 가설로 변환하기 위한 초안이다.

## H1 — 병렬성의 체감효과

에이전트 수 `A`를 증가시키면 총 후보 실행량은 증가하지만, 작업 결합도가 높은 조건에서는 `N_eff / A`가 감소한다.

측정 후보:
- completed valid tasks / agent
- duplicate work rate
- conflict rate
- coordination latency

## H2 — 조정 효율의 매개효과

`A`가 `N_eff`에 미치는 효과는 `S`에 의해 매개된다.

예상:
- 독립 작업: 높은 `S`, 더 긴 scale-out 구간
- 상호의존 작업: `A` 증가에 따라 `S` 하락

## H3 — 속도-신뢰도 trade-off

일정 수준 이상에서 per-agent execution rate `λ`를 높이면 `R`이 감소할 수 있다.

단, 이 효과는 모델·작업·검증 구조에 따라 존재하지 않을 수도 있다.

## H4 — 비선형 성과의 조건성

시장 선점 또는 빠른 학습 피드백이 존재하는 환경에서는 `β > 1`이 관찰될 가능성이 높고, 단순 반복 처리 환경에서는 `β ≤ 1`일 가능성이 높다.

## H5 — 통제포화와 대기시간

`K`가 증가할수록 평균 통제 대기시간과 backlog가 증가한다.

이 가설은 기존 queueing theory와 정합성을 확인해야 하며, AVCT의 신규성 주장이 아니라 모형 연결성 검증으로 취급한다.

## H6 — 통제포화와 실현성과

잠재 실행량이 증가하더라도 `K`가 높은 조건에서는 realized performance의 증가율이 감소한다.

측정 후보:
- net valid outputs after rework
- time-to-safe-deployment
- customer-impact-adjusted throughput
- rollback/recovery cost

## H7 — 위험 기반 라우팅의 효과

동일한 실행량에서 risk-tiering과 exception-based review를 적용하면 `q_control`과 평균 인간 검토 부담이 감소한다.

## H8 — reversibility의 완충효과

동일한 `K`에서 reversibility가 높은 시스템은 오류의 총 손실과 복구 시간을 낮춘다.

---

# 최소 검증 세트

첫 시뮬레이션에서는 H1, H2, H5, H6만 다룬다.

첫 실증 또는 사례 연구에서는 H5, H6, H7을 우선한다.
