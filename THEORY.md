# AI Velocity–Control Theory (AVCT) — v0.1 Baseline

## 1. 중심 명제

AI 에이전트 조직의 경쟁우위는 단순한 실행 속도에서 나오지 않는다.

실행 속도와 병렬성이 일정 시간 창 안에서 **유효 실행량**을 만들고, 그 실행량이 조정 가능하고 신뢰할 수 있으며, 조직의 통제 구조가 이를 지연·오류·재작업·책임 공백 없이 흡수할 때 비로소 실현 성과로 전환된다.

따라서 AVCT의 핵심 질문은 다음이다.

> **Agentic execution capacity가 증가할 때 potential throughput과 realized performance는 언제 분리되며, control architecture는 residual risk를 허용 가능한 범위에 유지하면서 그 분리점을 얼마나 이동시키는가?**

---

## 2. 이론의 세 층

### Layer A — Effective Action Mass

`N_eff(T) = A · λ · T · S · R`

- `A`: 병렬 실행에 참여하는 agent 수
- `λ`: agent당 candidate action rate
- `T`: 의미 있는 response / competition window
- `S`: coordination efficiency
- `R`: execution reliability

중요:

`A`와 `λ`가 증가해도 `S`와 `R`이 하락하면 실제 유효 실행량은 같은 비율로 증가하지 않는다.

---

### Layer B — Competitive / Organizational Effect

`P_AI = α · N_eff^β`

`β`는 고정된 법칙이 아니라 검증할 값이다.

- `β < 1`: congestion / diminishing returns
- `β = 1`: proportional effect
- `β > 1`: conditional superlinear effect
- `β = 2`: Lanchester-square-like special case

AVCT는 `β=2`를 기본값으로 사용하지 않는다.

Lanchester는 **inspiration / nonlinear boundary case**이지 AI 조직 성과의 직접 derivation source가 아니다.

---

### Layer C — Control Saturation

`K = Λ_control / μ_control`

- `Λ_control`: control-requiring action arrival rate
- `μ_control`: effective control-processing capacity

`K`는 queue-utilization-like operational index다.

- `K < 1`: 평균 control capacity가 평균 control demand를 초과
- `K → 1`: compatible queueing model에서 delay가 민감해질 수 있음
- `K > 1`: operating rule이 바뀌지 않으면 unresolved control work가 누적될 수 있음

이 queue 성질 자체는 AVCT의 신규 수학이 아니다.

---

## 3. Execution–Control Feedback

AVCT의 핵심은 세 층을 하나의 feedback system으로 보는 데 있다.

```text
A / λ 증가
   ↓
candidate action 증가
   ↓
coordination + reliability filtering
   ↓
N_eff 증가
   ↓
potential value 증가
   ↓
risk routing / control-demand generation
   ↓
Λ_control 증가 또는 재구성
   ↓
K 변화
   ↓
delay / backlog / rework / residual risk / recovery cost
   ↓
realized performance 변화
   ↓
S / R / future control load에 feedback
```

따라서 경영 문제는 `max λ`가 아니라:

> **control, coordination, reliability, residual-risk, reversibility 제약 아래 realized performance를 최적화하는 것**

이다.

---

## 4. Execution–Control Frontier

v0.1 hardening 이후 AVCT는 낮은 `K` 자체를 좋은 통제의 증거로 보지 않는다.

control architecture는 최소한 다음을 함께 비교해야 한다.

1. control saturation `K`
2. human / automated review load
3. unsafe escape rate
4. harm / recovery cost
5. realized net value / time

즉 **control-load reduction과 residual-risk preservation이 동시에 이루어져야** sustainable improvement로 본다.

2차 synthetic simulation에서는 risk-tiered routing이 `K`를 크게 낮추면서도 verifier quality가 낮을 때 unsafe escape를 증가시키는 반례가 나왔다. 따라서 P7은 조건부 명제로 유지한다.

---

## 5. Reversibility

Reversibility는 execution reliability와 구분한다.

오류가 발생하지 않는 능력과, 오류가 발생했을 때 되돌리고 회수할 수 있는 능력은 다른 속성이다.

v0.1에서는 reversibility를 주로:

- error consequence
- rollback / recovery time
- recovery cost

를 낮추는 **loss-severity modifier**로 다룬다.

---

## 6. 인간 통제 용량의 의미

AVCT는 `μ_control`을 human reviewer headcount로 축소하지 않는다.

control capacity는 다음의 조합일 수 있다.

- design-time constraints
- guardrails
- automated verification
- agent-in-the-loop oversight
- human-in-the-loop review
- escalation
- sampled audit
- authority boundaries
- observability
- circuit breakers

즉 통제 용량은 생물학적 인간 능력만이 아니라 **socio-technical control architecture의 effective service capacity**다.

다만 automated control의 speed/scalability가 human judgment의 accountability나 legitimacy를 자동 대체한다고 가정하지 않는다.

---

## 7. v0.1 핵심 명제

### P1 — Conditional scale-out

Agent count와 execution rate 증가는 candidate action volume을 증가시키지만 effective action mass의 증가는 `S`, `R`에 조건부다.

### P2 — Coordination dependence

Task coupling과 communication dependency가 높을수록 scale-out efficiency가 감소할 가능성이 있다.

### P3 — Conditional nonlinear effect

Superlinear effect는 특정 learning, first-response, concentration, network mechanism이 존재할 때만 나타날 수 있다. `β>1`은 보편값이 아니다.

### P4 — Control-demand generation

Execution scope/rate 증가는 control-requiring action의 절대량을 증가시키는 경향이 있으나 routing/authority/verification architecture가 `q_control`을 바꿀 수 있다.

### P5 — Queueing connection

높은 `K`와 delay/backlog의 관계는 기존 queueing theory에 연결한다. 이 성질 자체를 AVCT novelty로 주장하지 않는다.

### P6 — Potential–realized divergence

Potential throughput은 증가해도 control bottleneck, delay, rework, residual risk, recovery cost 때문에 realized performance가 포화 또는 하락할 수 있다.

### P7 — Conditional control-architecture productivity

Control architecture는 divergence point를 이동시킬 수 있지만 residual risk와 recovery cost를 허용 가능한 budget 안에 유지해야 sustainable improvement로 본다.

### P8 — Sustainable velocity

가장 높은 short-run execution rate를 가진 조직이 가장 높은 long-run realized value를 갖는다는 보장은 없다.

---

## 8. 신규성 경계

AVCT는 다음을 새롭게 발견했다고 주장하지 않는다.

- time-based competition
- finite human oversight
- human cognitive-load limit
- automation bias / complacency
- queue saturation / utilization
- multi-agent coordination cost
- meaningful human oversight
- risk-tiered / adaptive intervention
- guardrail / HITL / AITL mechanism
- OODA / NBKL dynamics
- Lanchester square law

AVCT의 candidate contribution은 이들을 하나의 **measurable execution–control feedback system**으로 연결하고, control load / residual risk / realized performance의 joint frontier를 실증하는 데 있다.

---

## 9. Lanchester의 역할

AVCT는 초기에 사용했던:

`P_AI = V²`

또는:

`P_AI = N_eff²`

를 폐기했다.

Lanchester의 역할은 다음으로 제한한다.

- coordinated multiplicity가 특정 조건에서 nonlinear outcome을 낼 수 있다는 질문을 제기
- `β=2`라는 비교용 특수경계를 제공
- quantity, quality, concentration의 상호작용을 생각하는 analytical lens 제공

실제 AI 조직 효과는 실증적으로 추정한다.

---

## 10. OODA / NBKL의 역할

OODA와 Networked Boyd–Kuramoto–Lanchester 연구는 networked decision synchronization과 resource competition을 결합하는 강한 관련 연구다.

하지만 AVCT에서는 **supporting analogue**로만 둔다.

일반 enterprise agent workflow의 control-service bottleneck이나 realized-performance divergence를 NBKL에서 직접 도출하지 않는다.

---

## 11. 현재 검증 상태

### Structural simulation 1

- task coupling에 따른 scale-out efficiency 차이
- queue saturation sanity check
- potential–realized divergence

### Structural simulation 2

- risk-tiered control routing
- automated-verifier sensitivity
- residual-risk counterexample
- reversibility / loss severity

두 simulation 모두 synthetic toy models이며 empirical evidence가 아니다.

---

## 12. 현재 가장 중요한 실증 질문

다음 단계는 실제 agent workflow에서 다음을 측정하는 것이다.

> **같은 task set과 execution capacity에서 서로 다른 agent/control architecture가 `N_eff`, `K`, residual risk, recovery cost, realized value를 어떻게 변화시키는가?**

이 질문에 실제 데이터로 답하지 못하면 AVCT는 conceptual synthesis에 머문다.

---

## 13. v0.1 금지 주장

공개 문서에서 다음을 법칙 또는 검증된 사실처럼 쓰지 않는다.

- “AI 속도 2배 = 경쟁력 4배”
- `P=V²`
- `P=N_eff²`
- `K=1`이 모든 조직의 보편 위험 임계점이라는 주장
- finite oversight capacity를 AVCT가 최초 발견했다는 주장
- adaptive/risk-tiered oversight를 AVCT가 최초 제안했다는 주장
- synthetic verifier sensitivity를 실제 safety threshold로 사용하는 것
- 공공 사회적 이익이 속도의 제곱으로 증가한다는 주장

---

## 14. 이론이 실패하는 조건

다음 중 하나가 반복적으로 확인된다면 AVCT는 별도 이론으로서 약화되거나 폐기되어야 한다.

1. agentic execution과 control load 사이에 의미 있는 구조적 관계가 없다.
2. potential–realized divergence가 control variables보다 다른 기존 변수로 충분히 설명된다.
3. AVCT 변수들이 기존 queueing, human-factors, multi-agent, management-control 모델의 단순 병렬 적용보다 추가 설명력/예측력을 제공하지 못한다.
4. `N_eff`, `Λ_control`, `μ_control`, residual risk를 실제 운영에서 신뢰성 있게 측정할 수 없다.
5. control architecture 비교에서 AVCT frontier가 실질적인 설계 의사결정에 추가 가치를 제공하지 않는다.

이 실패 가능성을 이론의 일부로 유지한다.
