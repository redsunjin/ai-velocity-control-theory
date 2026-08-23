# AI Velocity–Control Theory

**AI 속도–통제 이론 (AI Velocity–Control Theory, AVCT)**

> Conceptual working theory. The mathematical relationships in this repository are hypotheses and analytical constructs, not empirically validated laws.

AI 에이전트 조직에서 **실행 속도, 병렬성, 조정 효율, 신뢰도**가 만드는 실행 능력과, 이를 검토·승인·회수·책임질 수 있는 **인간/조직 통제 용량** 사이의 관계를 연구하는 공개 저장소입니다.

## 핵심 질문

> AI의 실행 속도와 병렬성이 증가할 때, 그 우위는 언제 실제 성과로 전환되고 언제 인간·조직의 통제 능력을 초과해 위험으로 바뀌는가?

## 현재 기준선: v0.1

v0.1은 완성된 법칙을 선언하지 않습니다. 다음 세 층을 검증 가능한 가설로 분리합니다.

1. **Effective Action Mass (`N_eff`)** — 일정 시간 창 안에서 실제로 의미 있게 수행되는 유효 실행량
2. **Competitive Effect (`P_AI`)** — 유효 실행량이 만드는 경쟁·조직 효과. 비선형성의 정도는 고정하지 않고 검증 대상으로 둠
3. **Control Saturation Ratio (`K`)** — 통제가 필요한 AI 행동의 유입률과 조직의 통제 처리율 사이의 비율

란체스터 제2법칙은 AI 성과의 직접 예측식이 아니라, **집중되고 병렬화된 실행 단위가 특정 조건에서 비선형 효과를 낼 수 있다는 분석적 렌즈**로 사용합니다.

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
    ├── hypotheses.md
    └── simulation-plan.md
```

## 연구 원칙

- **속도 = 병력 수**라는 직접 치환을 이론의 전제로 사용하지 않는다.
- `P_AI = N_eff²`를 보편 법칙으로 주장하지 않는다.
- 비선형성은 `P_AI = α·N_eff^β`의 `β`처럼 **검증할 값**으로 둔다.
- 통제 초과비는 서로 다른 단위의 추상 지표를 나누지 않고 **처리율/유입률** 관점에서 정의한다.
- 에이전트 수가 늘면 조정 비용도 증가할 수 있으므로 병렬성을 공짜로 가정하지 않는다.
- 경쟁우위와 안전성은 별개의 문제가 아니라 동일한 동역학의 서로 다른 구간으로 본다.
- 학술적으로 확인된 사실, 선행연구의 해석, 본 이론의 가설을 문서에서 명확히 구분한다.

## RoundZero와의 관계

소설 **RoundZero**는 별도 저장소 `Tangle-Studio/novels/RoundZero`에서 계속 관리합니다.

- 이 저장소: **이론의 Source of Truth**
- RoundZero의 `docs/theory-brief.md`: 소설용 해석본
- RoundZero의 `docs/theory-ledger.md`: 장별 이론 반영 추적

운영 흐름은 다음과 같습니다.

```text
AVCT theory v0.x
      ↓
RoundZero narrative experiments
      ↓
반례 / 모순 / 새로운 질문
      ↓
AVCT theory v0.x+1
```

즉 소설은 이론을 설명하기 위한 교재가 아니라, 이론이 현실적 압력 속에서도 성립하는지 탐색하는 **사고실험 공간**으로 사용합니다.

## 상태

- **Stage:** Conceptual working theory
- **Baseline:** v0.1 (in construction)
- **Empirical validation:** Not yet completed
- **Public claim level:** Hypothesis / conceptual framework

## 다음 단계

1. 핵심 변수와 단위를 고정한다.
2. 기존 선행연구와 중복·차별 지점을 검증한다.
3. 시뮬레이션 가능한 최소 모형을 만든다.
4. 반례가 가능한 명제 형태로 재작성한다.
5. v0.1 working paper를 동결한 뒤 RoundZero를 재검토한다.
