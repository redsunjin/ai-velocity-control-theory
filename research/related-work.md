# Related Work & Novelty Boundary — v0.1

이 문서는 AVCT가 기존 연구와 어디서 겹치고 어디서 달라질 수 있는지 과장 없이 정리한다.

## 1. 이미 존재하는 연구 질문

다음 주제 자체는 AVCT의 신규성이 아니다.

- 시간이 경쟁우위의 핵심 변수라는 주장
- 인간 감독 용량이 유한하다는 주장
- AI governance와 human oversight의 필요성
- multi-agent coordination이 scale-out에서 어려워질 수 있다는 주장
- arrival rate와 service capacity의 불균형이 backlog를 만든다는 queueing 결과
- Lanchester square law의 비선형 집중 효과

AVCT는 이 개념들을 새로 발명했다고 주장하지 않는다.

---

## 2. AVCT의 차별화 후보

AVCT의 연구 기여는 다음 연결 구조가 하나의 조직 동역학으로 성립하는지 검증하는 데 있다.

```text
Agent count / execution rate
            ↓
Effective Action Mass (N_eff)
            ↓
Potential competitive effect
            ↓
Control-demand arrival (Λ_control)
            ↓
Control saturation (K)
            ↓
Delay / rework / cognitive load / control debt
            ↓
Coordination efficiency (S) and reliability (R)
            ↓
Realized performance
```

핵심은 **속도와 통제를 각각 연구하는 것이 아니라, 속도를 생성하는 구조와 그 속도를 흡수하는 구조의 상대적 확장 속도**를 하나의 피드백 체계로 보는 것이다.

---

## 3. Human-on-the-Loop working paper와의 경계

Kadowaki(2026)의 최신 working paper는 oversight capacity와 agent throughput의 비대칭을 직접 다룬다.

따라서 AVCT가 피해야 할 claim:

> 인간 감독은 유한하므로 AI가 빨라지면 감독을 초과한다는 사실을 최초로 이론화했다.

AVCT가 검증할 수 있는 별도 질문:

> 동일한 agent throughput이라도 병렬성의 조정 효율, 실행 신뢰도, 경쟁 시간 창, 통제 라우팅, reversibility가 다르면 실제 경쟁성과와 통제포화가 어떻게 달라지는가?

그리고:

> 통제포화가 다시 실행 신뢰도와 조정효율을 떨어뜨리는 feedback loop가 실제 조직에서 존재하는가?

이 두 질문이 중요 차별화 후보다.

---

## 4. Queueing theory와의 경계

`K = Λ/μ`는 queueing utilization과 구조적으로 유사하다.

따라서 AVCT가 할 일은 새로운 queue 이론을 만드는 것이 아니다.

AVCT의 역할 후보:

1. agentic execution layer에서 `Λ_control`이 생성되는 메커니즘을 모델링
2. governance architecture가 arrival/service 양쪽을 어떻게 바꾸는지 설명
3. queue state를 quality, responsibility, reversibility, competitive performance와 연결
4. control saturation이 다시 upstream agent behavior에 영향을 주는 closed loop를 모델링

---

## 5. Lanchester와의 경계

Lanchester는 수식의 정당화 장치가 아니다.

AVCT에서의 역할은 다음으로 제한한다.

- 다수의 동시 실행 단위가 상호작용 구조에 따라 비선형 결과를 낼 수 있다는 질문을 제기
- `β=2`를 하나의 특수 비교 기준으로 제공
- quantity × quality × concentration의 직관 제공

실제 `β`는 업무와 시장마다 검증한다.

---

## 6. Multi-agent scaling 연구와의 경계

SILO-BENCH 같은 연구는 agent count 증가가 coordination success를 자동으로 보장하지 않음을 보여준다.

AVCT는 이를 기업 성과로 곧바로 일반화하지 않는다.

대신 다음 연결을 검증한다.

- benchmark coordination efficiency → operational coordination proxy로 변환 가능한가?
- 실제 업무에서는 task coupling이 `S`에 어떤 영향을 주는가?
- coordination failure가 control demand를 추가로 발생시키는가?

---

## 7. 가능한 최종 기여 형태

AVCT가 성공적으로 검증될 경우 기여는 다음 중 하나 또는 복수일 수 있다.

### Conceptual contribution
AI agent organization을 execution-control coupled system으로 설명하는 통합 프레임.

### Measurement contribution
`N_eff`, `Λ_control`, `μ_control`, `K`를 실제 운영 로그에서 측정할 수 있는 operational metric set.

### Empirical contribution
agent scaling이 realized performance에 미치는 효과가 control saturation에 의해 조건부로 달라짐을 실증.

### Design contribution
실행 속도를 억제하지 않고도 control capacity를 확장하거나 control demand를 줄이는 조직/시스템 설계 원칙.

---

# Novelty claim rule

공개 문서와 논문에서는 다음 문장을 기본 원칙으로 사용한다.

> AVCT does not claim novelty for finite human oversight, queue saturation, multi-agent coordination costs, or Lanchester-style nonlinear effects individually. Its proposed contribution is to model and test their coupling in agentic organizations as an execution–control feedback system.
