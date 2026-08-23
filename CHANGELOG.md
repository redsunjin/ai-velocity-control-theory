# Changelog

이 문서는 AI Velocity–Control Theory의 개념 변경을 추적한다. 문구 수정이 아니라 **이론의 의미가 바뀌는 변경**을 중심으로 기록한다.

## v0.1-freeze — 2026-08-23

### Claim boundary frozen

v0.1의 공개 주장 범위를 첫 구조 검증과 선행연구 검토를 반영해 고정했다.

- time-based competition의 원전(Stalk, 1988)을 확인하고 “속도가 경쟁우위다” 자체를 신규성에서 제외.
- Little's Law 및 M/M/1 utilization을 기준으로 `K`의 queueing 성질을 AVCT 신규 수학에서 제외.
- Bainbridge, Parasuraman & Manzey, Langer et al., Lazaros et al. 등 human oversight / automation human-factors 문헌을 추가.
- Nguyen et al.의 agentic controllability survey와 Zhu et al.의 meaningful human oversight 연구를 반영해 control architecture를 인간 headcount가 아닌 설계 가능한 복합 capacity로 확장.
- Kadowaki의 2026 working paper를 direct-overlap source로 기록하고 finite oversight capacity의 최초성 주장을 명시적으로 포기.
- SILO-BENCH를 multi-agent coordination scaling의 핵심 관련 연구로 기록.
- peer-reviewed NBKL 연구를 확인하고 OODA/NBKL을 AVCT의 core foundation에서 **supporting analogue**로 내림.
- working paper를 `Conceptual Baseline + First Structural Validation` 상태로 갱신.

### v0.1 primary question

> Agentic execution capacity가 증가할 때 potential throughput과 realized performance는 언제 분리되며, control architecture는 그 분리점을 얼마나 이동시키는가?

이 질문을 P6/P7의 2차 검증과 향후 실증 연구의 중심으로 둔다.

---

## v0.1-validation-1 — 2026-08-23

### Added

- H1/H2/H5/H6를 대상으로 한 첫 최소 시뮬레이션 실행.
- 재현 코드 `validation/simulations/avct_v01.py` 추가.
- coordination/control summary 데이터와 `first-simulation-v0.1.md` 결과 해석 추가.

### First structural findings

- 낮은 task coupling에서는 agent scale-out 효율 저하가 완만했지만 높은 coupling proxy에서는 `N_eff/A`와 `S`가 강하게 하락했다.
- `K = Λ_control / μ_control`이 1에 접근할수록 queue delay가 민감해지고 1을 초과하면 finite-horizon backlog가 급격히 증가했다.
- time-insensitive workflow에서는 potential throughput 증가가 control capacity 부근에서 realized throughput의 **포화**로 전환됐다.
- delay-sensitive workflow에서는 동일한 control saturation이 realized value의 **하락**으로 전환될 수 있었다.
- control capacity `μ_control`을 높이면 성과 포화/역전 지점이 뒤로 이동했다.

### Theory boundary tightened

- H5/P5의 queue saturation 현상 자체는 AVCT의 독창성 대상이 아니라 기존 queueing theory와의 연결성 검산으로 더 명확히 분리한다.
- P6/H6을 v0.1 이후 핵심 검증축으로 유지한다.
- coordination penalty나 delay-decay의 구체 함수형은 첫 결과만으로 고정하지 않는다.

---

## v0.1-baseline — 2026-08-23

### Added

- AI Velocity–Control Theory(AVCT)를 공개 이론 저장소의 이름으로 채택.
- `N_eff(T)` — Effective Action Mass 개념 도입.
- `P_AI = α · N_eff^β`를 경쟁/조직 효과의 검증용 일반식으로 채택.
- `K = Λ_control / μ_control`을 Control Saturation Ratio의 기준식으로 채택.
- 조정 효율 `S`, 실행 신뢰도 `R`, 통제 필요 비율 `q_control`, reversibility를 핵심 변수/후보 변수로 정의.
- 실행→통제포화→조정/신뢰도 저하→실현성과라는 feedback-loop를 AVCT의 핵심 구조로 정의.
- 반증 가능한 이론 명제와 초기 검증 가설 작성.
- 최소 시뮬레이션 계획 수립.
- 초기 선행연구 지도와 novelty boundary 작성.
- 공개용 working paper v0.1 기준 초안 작성.

### Changed from earlier concept

#### Removed as a baseline law

`P_AI = V²`

이유: 실행 속도(rate)를 Lanchester force count(stock)에 직접 치환하는 것은 차원과 인과 가정이 부족하다.

#### Removed as a baseline law

`P_AI = N_eff²`

이유: square effect는 검증해야 할 특수 조건이지 기본값이 아니다.

대체:

`P_AI = α · N_eff^β`

#### Removed

`K = P_AI / C_human`

이유: 서로 다른 의미와 단위를 가진 추상량의 비율이며 `K=1`의 해석 근거가 약하다.

대체:

`K = Λ_control / μ_control`

#### Narrowed

“Lanchester's law applied to AI”

→ “Lanchester-inspired analytical lens within a broader execution–control theory”

#### Deferred

- 공공서비스 속도 증가가 사회적 이익의 제곱효과를 만든다는 주장
- 특정 속도 증가가 반드시 특정 배수의 경쟁우위를 만든다는 주장

### Novelty boundary

v0.1부터 다음 자체는 독창성 주장 대상에서 제외한다.

- finite human oversight
- queue saturation / utilization
- multi-agent coordination overhead
- time-based competition
- Lanchester nonlinear concentration effect
- automation bias / complacency
- HITL / AITL / guardrail mechanism 자체
- OODA / NBKL dynamics 자체

AVCT의 잠재 기여는 이들을 **agentic execution–control feedback system**으로 연결하고 측정·검증하는 데 둔다.

---

## Next candidate — v0.2

v0.2로 올리기 전 필요한 조건:

- [x] 핵심 문헌 검토 확장 — v0.1 claim boundary 수준
- [x] queueing theory 원전/표준 모델 정리 — novelty boundary 수준
- [x] human oversight peer-reviewed literature 확장 — v0.1 수준
- [x] time-based competition primary source 확인
- [x] OODA/NBKL의 역할 결정 — supporting analogue
- [x] simulation v0.1 실행
- [x] `S(A, task)` 가정 1차 민감도 확인
- [x] `K`와 realized performance의 1차 관계 검토
- [ ] dependency-graph 기반 coordination model로 재검증
- [ ] risk-tiered routing (`q_control < 1`) 시뮬레이션
- [ ] reversibility / reviewer-quality feedback 검증
- [ ] management control theory 연결
- [ ] RoundZero의 이론 반례/서사적 모순 수집
