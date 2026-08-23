# AI Velocity–Control Theory

**AI 속도–통제 이론 (AI Velocity–Control Theory, AVCT)**

> Conceptual working theory. The mathematical relationships in this repository are hypotheses and analytical constructs, not empirically validated laws.

AI 에이전트 조직에서 **실행 속도, 병렬성, 조정 효율, 신뢰도**가 만드는 실행 능력과, 이를 검토·승인·회수·책임질 수 있는 **조직 통제 용량** 사이의 관계를 연구하는 공개 저장소입니다.

## 핵심 질문

> **Agentic execution capacity가 증가할 때 potential throughput과 realized performance는 언제 분리되며, control architecture는 그 분리점을 얼마나 이동시키는가?**

이 질문은 단순히 “AI가 빠르면 유리한가?”가 아니라, **빠르고 병렬적인 AI 실행을 실제 성과로 얼마나 흡수할 수 있는가**를 다룹니다.

## 현재 기준선: v0.1

v0.1의 claim boundary는 2026-08-23 첫 구조 검증 이후 고정했습니다. 아직 경험적으로 검증된 법칙은 아닙니다.

세 층을 구분합니다.

1. **Effective Action Mass (`N_eff`)** — 일정 시간 창 안에서 생성되는 유효 실행량
2. **Competitive / Organizational Effect (`P_AI`)** — 유효 실행량이 만드는 효과. 비선형성은 고정하지 않고 검증 대상으로 둠
3. **Control Saturation Ratio (`K`)** — 통제가 필요한 행동의 유입률과 통제 처리율의 비율

기준식:

```text
N_eff(T) = A · λ · T · S · R
P_AI     = α · N_eff^β
K        = Λ_control / μ_control
```

란체스터 제2법칙은 AI 성과의 직접 예측식이 아니라, **집중되고 병렬화된 실행 단위가 특정 조건에서 비선형 효과를 낼 수 있다는 분석적 렌즈**로만 사용합니다.

## 첫 구조 검증

`validation/simulations/avct_v01.py`로 H1/H2/H5/H6의 최소 시뮬레이션을 실행했습니다.

첫 결과는 다음을 보여줍니다.

- 강결합 task proxy에서 agent scale-out 효율과 `S`가 더 빠르게 감소할 수 있음
- `K≈1` 부근에서 queue delay가 민감해지는 구조 재현
- control capacity가 병목이 되면 potential throughput과 realized throughput이 분리됨
- delay/rework/opportunity cost가 있는 조건에서는 realized value의 역전도 가능함
- `μ_control`을 높이면 포화/역전 지점이 이동함

주의: 이는 **toy-model structural sanity check**이며 실제 조직에 대한 경험적 증거가 아닙니다. 특히 queue saturation은 기존 queueing theory의 결과이지 AVCT의 신규성 주장이 아닙니다.

자세한 결과: `validation/results/first-simulation-v0.1.md`

## 검증된 novelty boundary

AVCT는 다음을 새롭게 발견했다고 주장하지 않습니다.

- 시간이 경쟁우위가 될 수 있다는 사실
- Lanchester의 비선형 집중 효과
- multi-agent coordination overhead
- 인간 감독의 인지·확장성 한계
- automation bias / complacency
- finite oversight capacity
- queue saturation / utilization
- HITL, AITL, guardrail, escalation 등의 통제 메커니즘 자체
- OODA/NBKL의 의사결정 동기화·자원 경쟁 구조

AVCT의 잠재 기여는 이 요소들을 **agentic execution generation → coordination/reliability → control demand → control architecture → realized performance**의 하나의 측정 가능한 운영 동역학으로 연결하는 데 있습니다.

## 저장소 구조

```text
.
├── README.md
├── THEORY.md
├── CHANGELOG.md
├── model/
│   ├── definitions.md
│   ├── equations.md
│   └── propositions.md
├── papers/
│   └── working-paper-v0.1.md
├── research/
│   ├── literature-review.md
│   └── related-work.md
└── validation/
    ├── README.md
    ├── hypotheses.md
    ├── simulation-plan.md
    ├── simulations/
    │   └── avct_v01.py
    └── results/
        ├── first-simulation-v0.1.md
        └── generated/
```

## 연구 원칙

- **속도 = 병력 수**라는 직접 치환을 사용하지 않는다.
- `P_AI = N_eff²`를 보편 법칙으로 주장하지 않는다.
- 비선형성은 `β`처럼 **검증할 값**으로 둔다.
- `K`의 queue 성질을 AVCT의 신규 수학으로 주장하지 않는다.
- 병렬성을 공짜로 가정하지 않는다.
- 통제를 속도의 반대항이 아니라 **속도를 실현 성과로 변환하는 생산 인프라**로 검증한다.
- 시뮬레이션에 넣은 가정이 결과에서 재현된 것을 경험적 검증으로 포장하지 않는다.
- 선행연구, 본 이론의 가설, 시뮬레이션 결과, 실증 결과를 명확히 구분한다.

## RoundZero와의 관계

소설 **RoundZero**는 별도 저장소 `Tangle-Studio/novels/RoundZero`에서 관리합니다.

- 이 저장소: **이론의 Source of Truth**
- RoundZero의 `docs/theory-brief.md`: 소설용 해석본
- RoundZero의 `docs/theory-ledger.md`: 장별 이론 반영 추적

```text
AVCT theory v0.x
      ↓
RoundZero narrative experiments
      ↓
반례 / 모순 / 새로운 질문
      ↓
AVCT theory v0.x+1
```

소설은 이론을 설명하는 교재가 아니라 이론을 현실적 압력 속에서 시험하는 **사고실험 공간**으로 사용합니다.

## 상태

- **Stage:** Conceptual theory + first structural validation
- **Baseline:** v0.1 claim boundary frozen
- **Empirical validation:** Not yet completed
- **Public claim level:** Hypothesis / conceptual framework
- **First simulation:** Completed
- **Next validation:** control architecture / risk routing / reversibility

## 다음 단계

1. dependency-graph 기반 coordination model로 2차 검증
2. risk-tiered routing으로 `q_control < 1` 실험
3. reversible / irreversible action 분리
4. reviewer accuracy / cognitive-load feedback 추가
5. 실제 agent workflow에서 측정할 telemetry schema 확정
6. v0.1 기준을 RoundZero `theory-brief`에 동기화하고 소설을 재검토
