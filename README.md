# AI Velocity–Control Theory

**AI 속도–통제 이론 (AI Velocity–Control Theory, AVCT)**

> Conceptual working theory. The mathematical relationships in this repository are hypotheses and analytical constructs, not empirically validated laws.

AI 에이전트 조직에서 **실행 속도, 병렬성, 조정 효율, 신뢰도**가 만드는 실행 능력과, 이를 검토·승인·회수·책임질 수 있는 **조직 통제 용량** 사이의 관계를 연구하는 공개 저장소입니다.

## 핵심 질문

> **Agentic execution capacity가 증가할 때 potential throughput과 realized performance는 언제 분리되며, control architecture는 그 분리점을 얼마나 이동시키는가?**

v0.1 hardening 이후에는 한 조건을 더 붙입니다.

> **그 이동이 residual-risk budget을 넘지 않는가?**

즉 단순히 “AI가 빠르면 유리한가?”가 아니라, **빠르고 병렬적인 AI 실행을 실제 성과로 얼마나 안전하게 흡수할 수 있는가**를 다룹니다.

## 현재 기준선: v0.1

v0.1의 claim boundary는 2026-08-24 선행연구 재검증과 두 번의 구조적 시뮬레이션 이후 고정했습니다. 아직 경험적으로 검증된 법칙은 아닙니다.

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

## 구조 검증 1 — coordination + saturation

`validation/simulations/avct_v01.py`로 H1/H2/H5/H6의 최소 시뮬레이션을 실행했습니다.

- 강결합 task proxy에서 agent scale-out 효율과 `S`가 더 빠르게 감소할 수 있음
- `K≈1` 부근에서 queue delay가 민감해지는 구조 재현
- control capacity가 병목이 되면 potential throughput과 realized throughput이 분리됨
- delay/rework/opportunity cost가 있는 조건에서는 realized value의 역전도 가능함

주의: queue saturation은 기존 queueing theory의 결과이며 AVCT의 신규성 주장이 아닙니다.

결과: `validation/results/first-simulation-v0.1.md`

## 구조 검증 2 — control architecture + residual risk

`validation/simulations/avct_v01_control_architecture.py`로 H6/H7/H8을 추가 공격했습니다.

핵심 결과:

- risk-tiered routing은 human control arrival과 `K`를 크게 낮출 수 있음
- 그러나 automated verifier가 약하면 unsafe escape가 증가함
- 해당 synthetic assumptions에서는 verifier sensitivity 약 99% 부근에서 stable full-review baseline과 유사한 unsafe-escape 수준이 나타남
- 이 99%는 **현실 안전 기준이 아니라 toy-model sensitivity boundary**임
- reversibility를 높이면 동일한 unsafe-escape count에서도 harm / recovery loss가 감소함

따라서 P7은 다음처럼 조건부로 수정했습니다.

> **Control architecture는 control load를 낮추는 것만으로 충분하지 않으며, residual risk를 허용 가능한 risk budget 안에 유지할 때만 sustainable execution frontier를 개선한다.**

결과: `validation/results/second-simulation-v0.1.md`

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
- risk-tiered / adaptive oversight 자체
- OODA/NBKL의 의사결정 동기화·자원 경쟁 구조

AVCT의 잠재 기여는 이 요소들을 **agentic execution generation → coordination/reliability → control demand → control architecture → residual risk/recovery → realized performance**의 하나의 측정 가능한 운영 동역학으로 연결하는 데 있습니다.

선행연구 검증 체크포인트:

- `research/literature-validation-2026-08-24.md`

## 첫 실증 단계

v0.1의 최소 simulation hardening은 끝났습니다. 다음 단계는 실제 workflow에서 변수가 측정되는지 확인하는 것입니다.

- telemetry 계약: `validation/telemetry-schema.md`
- bounded experiment: `validation/empirical-plan-v0.1.md`
- 작업 추적: Issue #3 — `Empirical v0.1: telemetry and bounded workflow experiment`

첫 실증에서는 24~40개의 안전한 software/analysis task를 기준으로 다음 조건을 우선 비교합니다.

| Condition | Execution | Control |
|---|---|---|
| A1 | 1 agent | full gate |
| A2 | 4 agents | full gate |
| A3 | 4 agents | risk-tiered |
| A4 | 4 agents | risk-tiered + stronger reversibility |

목표는 이론을 증명하는 것이 아니라 **P1/P2/P6/P7에 실제 반례·null result·지지 방향이 나오는지 확인하는 것**입니다.

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
│   ├── literature-validation-2026-08-24.md
│   └── related-work.md
└── validation/
    ├── README.md
    ├── hypotheses.md
    ├── simulation-plan.md
    ├── telemetry-schema.md
    ├── empirical-plan-v0.1.md
    ├── simulations/
    │   ├── avct_v01.py
    │   └── avct_v01_control_architecture.py
    └── results/
        ├── first-simulation-v0.1.md
        ├── second-simulation-v0.1.md
        └── generated/
```

## 연구 원칙

- **속도 = 병력 수**라는 직접 치환을 사용하지 않는다.
- `P_AI = N_eff²`를 보편 법칙으로 주장하지 않는다.
- 비선형성은 `β`처럼 **검증할 값**으로 둔다.
- `K`의 queue 성질을 AVCT의 신규 수학으로 주장하지 않는다.
- 병렬성을 공짜로 가정하지 않는다.
- 낮은 `K`를 곧 좋은 통제로 간주하지 않는다. residual risk와 realized value를 함께 본다.
- reversibility를 오류율 감소와 혼동하지 않는다. 주로 loss/recovery 변수로 본다.
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

- **Stage:** Conceptual theory + two structural sensitivity validations
- **Baseline:** v0.1 claim boundary frozen
- **Empirical validation:** Designed, not yet executed
- **Public claim level:** Hypothesis / conceptual framework
- **Simulation phase:** Minimal v0.1 hardening completed
- **Current work:** Issue #3 — real agent workflow telemetry + bounded empirical experiment

## 다음 단계

1. 3~5 pilot tasks로 telemetry event 연결 검증
2. 24~40 task set과 ground-truth rubric 고정
3. A1~A4 architecture manifest 고정
4. 실제 로그로 P1/P2/P6/P7 공격
5. 실증 시작과 병행해 v0.1 기준을 RoundZero `theory-brief`에 동기화하고 소설을 재검토
