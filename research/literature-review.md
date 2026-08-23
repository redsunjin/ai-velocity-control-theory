# Literature Review Map — v0.1

> 검증 갱신: 2026-08-23. 이 문서는 systematic review가 아니라 **AVCT의 claim boundary를 정하기 위한 선행연구 지도**다. peer-reviewed source, working paper, practitioner source를 구분한다.

AVCT는 다음 연구 흐름의 교차점에 있다.

1. Lanchester / attrition modeling
2. Time-based competition / organizational speed
3. Agentic AI and multi-agent coordination
4. Human oversight / automation human factors
5. Queueing / service-capacity theory
6. Agentic AI controllability / oversight architecture
7. OODA / NBKL adversarial decision dynamics

---

# 1. Lanchester models

## Hartley & Helmbold (1995) — peer reviewed

**Validating Lanchester's square law and other attrition models**  
Naval Research Logistics, 42(4), 609–633.  
DOI: `10.1002/1520-6750(199506)42:4<609::AID-NAV3220420408>3.0.CO;2-W`

핵심:
- 한국전쟁 인천-서울 전역 데이터로 homogeneous square law를 검증.
- 단일 상수계수의 homogeneous square-law battle 가정은 데이터에 충분히 맞지 않음.

AVCT 제약:
- `β=2`를 보편값으로 선언하지 않는다.
- Lanchester는 inspiration / boundary case로만 사용한다.

Source: https://onlinelibrary.wiley.com/doi/10.1002/1520-6750%28199506%2942%3A4%3C609%3A%3AAID-NAV3220420408%3E3.0.CO%3B2-W

## Kress (2020) — peer reviewed

**Lanchester Models for Irregular Warfare**  
Mathematics 8(5), 737.  
DOI: `10.3390/math8050737`

AVCT 제약:
- Lanchester 계열은 상황 구조에 맞춰 달라지는 model family로 취급한다.
- `AI speed = force count` 직접 치환은 기준 모형에서 제외한다.

Source: https://www.mdpi.com/2227-7390/8/5/737

---

# 2. Time-based competition

## Stalk (1988) — primary strategy source

George Stalk, Jr., **Time—The Next Source of Competitive Advantage**, Harvard Business Review, July 1988.

확인된 범위:
- 시간(time)을 경쟁우위의 핵심 yardstick으로 보는 전략 논의가 AI보다 수십 년 앞서 존재했다.
- 따라서 “속도가 경쟁우위다” 자체는 AVCT의 신규 주장이 아니다.

AVCT 차별화 질문:
- agentic parallel execution이 조직의 실행률을 급격히 높일 때,
- control capacity가 성과전환을 어디서 제한하는가?

Source: https://hbr.org/1988/07/time-the-next-source-of-competitive-advantage

---

# 3. Agentic AI and multi-agent coordination

## Abou Ali, Dornaika & Charafeddine (2026) — peer reviewed

**Agentic AI: a comprehensive survey of architectures, applications, and future directions**  
Artificial Intelligence Review 59, 11.  
DOI: `10.1007/s10462-025-11422-4`

AVCT 연결:
- AI agent를 단순 LLM 호출이 아닌 자율적 계획·도구사용·행동·협력 주체로 정의하는 기반.

Source: https://doi.org/10.1007/s10462-025-11422-4

## Zhang et al. (ACL 2026) — peer reviewed conference long paper

**SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems**  
ACL 2026 Long Papers, pp. 29379–29398.  
DOI: `10.18653/v1/2026.acl-long.1354`

검증된 범위:
- 30 algorithmic tasks, 54 configurations, 1,620 experiments.
- agent들이 활발하게 통신해도 효과적인 distributed computation으로 이어지지 않는 `Communication-Reasoning Gap`을 보고.
- complexity가 높아질수록 성능이 붕괴하고 Level-III tasks에서는 50 agents 초과 시 success rate 0을 보고.

AVCT 연결:
- `A ↑`가 자동으로 `N_eff ↑`를 보장하지 않는다는 강한 선행 근거.
- `S = S(A, task structure, protocol)` 가정을 유지할 이유가 있다.

제약:
- algorithmic benchmark 결과를 기업 업무 전체에 일반화하지 않는다.
- AVCT의 첫 simulation은 이 결과를 재현한 것이 아니라 별도의 toy model sanity check다.

Source: https://aclanthology.org/2026.acl-long.1354/

---

# 4. Human oversight and automation human factors

## Bainbridge (1983) — peer reviewed

Lisanne Bainbridge, **Ironies of Automation**, Automatica 19(6), 775–779.  
DOI: `10.1016/0005-1098(83)90046-8`

핵심:
- automation이 human operator 문제를 제거하기보다 확대할 수 있음을 분석.
- 정상 운영은 자동화하면서 인간에게 abnormal condition 대응 책임을 남기는 구조 자체가 어려움을 만든다는 고전적 문제제기.

AVCT 연결:
- 인간을 예외 처리자만으로 남기는 구조가 자동으로 scalable하다고 가정하지 않는다.

Source: https://doi.org/10.1016/0005-1098%2883%2990046-8

## Parasuraman & Manzey (2010) — peer reviewed review

**Complacency and Bias in Human Use of Automation: An Attentional Integration**  
Human Factors 52(3), 381–410.  
DOI: `10.1177/0018720810376055`

핵심:
- automation complacency는 multitask load에서 attention 경쟁과 함께 나타남.
- automation bias는 imperfect decision aids에서 omission/commission error를 유발할 수 있음.
- 단순 training/instruction만으로 제거되지 않는다고 정리.

AVCT 연결:
- `μ_control`은 단순 reviewer headcount가 아니다.
- review capacity뿐 아니라 reviewer sensitivity/quality가 pressure에 따라 달라질 수 있으므로 향후 `R_control(K)` 또는 reviewer-error state가 필요할 수 있다.

Source: https://doi.org/10.1177/0018720810376055

## Langer, Baum & Schlicker (2025) — peer reviewed

**Effective Human Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection of Inaccurate and Unfair Outputs**  
Minds and Machines 35, article 1.  
DOI: `10.1007/s11023-024-09701-0`

핵심:
- effective oversight에는 error detection과 그에 대한 intervention이 중요함.
- Signal Detection Theory를 통해 overseer sensitivity와 response bias를 구분.
- task-, system-, person-related factors가 oversight 품질에 영향을 줄 수 있다고 정리.

AVCT 연결:
- throughput만이 아니라 **review accuracy / error-detection quality**를 실증 변수에 포함해야 한다.

Source: https://link.springer.com/article/10.1007/s11023-024-09701-0

## Lazaros, Vrahatis & Kotsiantis (2026) — peer reviewed systematic review

**Human-in-the-Loop Artificial Intelligence: A Systematic Review of Concepts, Methods, and Applications**  
Entropy 28(4), 377.  
DOI: `10.3390/e28040377`

핵심:
- HITL의 deployment challenges로 scalability, cognitive load, trust calibration 등을 명시.

AVCT 제약:
- “human oversight has scalability/cognitive-load limits” 자체는 신규 주장으로 제시하지 않는다.

Source: https://www.mdpi.com/1099-4300/28/4/377

---

# 5. Agentic AI controllability and oversight architecture

## Nguyen et al. (2026) — peer reviewed survey

**On Controllability in Agentic AI: A Survey**  
Minds and Machines 36, article 29.  
Published 26 May 2026.  
DOI: `10.1007/s11023-026-09783-y`

핵심:
- agentic AI의 speed/scale이 human cognitive capacity를 넘을 때 classical real-time monitoring assumption이 어려워진다고 문제제기.
- controllability를 constraints/guardrails, adaptive control, agent-in-the-loop, human-in-the-loop 네 paradigms로 정리.
- automated oversight의 scalability와 human judgment의 legitimacy 사이 tension을 지적.

AVCT 연결:
- control architecture를 인간 reviewer 수만으로 모델링해서는 안 된다.
- `μ_control`에는 guardrail, automated oversight, AITL, HITL의 조합이 반영될 수 있다.
- AVCT는 controllability taxonomy 자체를 재발명하지 않는다.

Source: https://link.springer.com/article/10.1007/s11023-026-09783-y

## Zhu et al. (2026) — peer reviewed

**Designing meaningful human oversight in AI**  
AI and Ethics 6, article 286.  
Published 4 May 2026.  
DOI: `10.1007/s43681-026-01147-7`

핵심:
- AI의 operative agency와 인간의 evaluative agency를 구분.
- solve–verify asymmetry를 활용하여 humans가 AI solution을 재수행하지 않고 효율적으로 검증할 수 있도록 oversight를 설계해야 한다고 제안.
- structured rationales, confidence signals, policy attribution, circuit breakers 등 구체 mechanism을 제시.
- solving은 쉽지만 verification이 비싼 workload도 명시적으로 다룸.

AVCT 연결:
- `q_control`과 `μ_control`은 고정된 인간 능력이 아니라 **verification architecture에 의해 설계 가능한 변수**라는 근거가 강해진다.
- AVCT P7의 novelty는 개별 mechanism이 아니라 그러한 architecture가 execution–realization divergence point를 얼마나 이동시키는지 측정하는 데 둔다.

Source: https://link.springer.com/article/10.1007/s43681-026-01147-7

---

# 6. Direct overlap: oversight capacity

## Kadowaki (2026) — non-peer-reviewed working paper

**Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents**  
VURA Working Paper Series No. 8, Version 1.3.  
Published 17 Aug 2026.  
DOI: `10.5281/zenodo.21971214`

확인된 상태:
- conceptual working paper.
- experiment/survey/new empirical data를 수행한 논문이 아님을 저자 스스로 명시.
- 인간 oversight를 finite capacity constraint로 정식화하는 문제를 직접 다룸.

AVCT 제약:
- “oversight capacity is finite” 또는 “agent throughput can overwhelm human oversight”를 최초 주장으로 제시하지 않는다.
- 이 working paper는 AVCT와 직접적인 novelty-overlap source로 계속 추적한다.

AVCT 차별화 후보:
- execution generation (`A`, `λ`, `S`, `R`)에서 시작해
- control demand (`Λ_control`)를 생성하고
- queue/control architecture (`q_control`, `μ_control`)를 거쳐
- realized performance와 다시 coordination/reliability에 feedback되는 **전체 운영 동역학**과 측정/실증에 초점을 둔다.

Source: https://www.vuracapital.com/theory/human-on-the-loop

---

# 7. Queueing / service capacity

## Little (1961) — peer reviewed foundational theorem

John D. C. Little, **A Proof for the Queuing Formula: L = λW**, Operations Research 9(3), 383–387.  
DOI: `10.1287/opre.9.3.383`

핵심:
- stationary 조건 등 명시된 조건에서 평균 system population, arrival rate, mean time의 관계 `L = λW`를 증명.

Source: https://doi.org/10.1287/opre.9.3.383

## M/M/1 utilization baseline

표준 M/M/1에서는 utilization factor가 `ρ = λ/μ`이며 steady state를 위해 `ρ < 1`이 요구된다. 평균 system time 역시 `1/(μ-λ)` 형태로 `λ→μ`에서 민감해진다.

AVCT 제약:
- `K = Λ_control / μ_control`은 queue utilization과 구조적으로 동일한 ratio다.
- `K≈1`에서 delay가 민감해지는 현상은 **AVCT의 수학적 신규성 주장이 아니다.**
- first simulation의 H5는 이 연결을 검산한 것일 뿐이다.

AVCT 연구 대상:
- AI execution architecture가 `Λ_control`을 어떻게 생성하는가?
- oversight design이 `q_control`, service time, `μ_control`을 어떻게 바꾸는가?
- queue pressure가 review accuracy, `R`, realized value에 어떤 feedback을 만드는가?

Reference teaching source for M/M/1 baseline: MIT 1.041 queueing models lecture (2026): https://web.mit.edu/1.041/www/lectures/L8-queuing-models-2026sp.pdf

---

# 8. OODA / NBKL — supporting, not core

## Cullen, Alpcan & Kalloniatis (2025) — peer reviewed

**Game-Theoretic Analysis of Adversarial Decision Making in a Complex Socio-Physical System**  
Dynamic Games and Applications 15, 709–728.  
DOI: `10.1007/s13235-024-00593-4`

핵심:
- networked Boyd–Kuramoto–Lanchester (NBKL) resource competition model을 사용.
- networked agents의 decision-state synchronisation, resource reallocation, adversarial attrition을 결합.
- business, sporting, military, cyber-security 등 adversarial socio-physical interaction을 적용 영역으로 논의.

AVCT 결정:
- **OODA/NBKL은 AVCT의 필수 중심축에서 내리고 supporting theoretical analogue로 둔다.**
- 이유: NBKL은 adversarial resource-competition dynamics를 설명하는 강한 관련 연구지만, 일반 조직의 AI execution throughput–control saturation을 직접 검증한 것은 아니다.
- AVCT working paper에서는 “관련된 네트워크 경쟁 동역학 연구”로 인용하고, AVCT 수식의 근거처럼 사용하지 않는다.

Source: https://link.springer.com/article/10.1007/s13235-024-00593-4

---

# 9. Verified novelty boundary — v0.1

다음은 **AVCT의 독창성 주장 대상에서 제외한다.**

- 속도가 경쟁우위가 될 수 있다는 주장
- Lanchester의 concentration / nonlinear attrition effect
- multi-agent coordination overhead
- 인간 감독의 cognitive/scalability limit
- automation bias / complacency
- finite oversight capacity
- queue utilization / saturation
- human-in-the-loop, agent-in-the-loop, guardrail 등 control mechanisms 자체
- OODA/NBKL의 decision-synchronisation/resource-competition 구조

## AVCT의 검증 가능한 기여 후보

AVCT의 가장 방어 가능한 중심 연구질문은 다음으로 좁힌다.

> **When agentic execution capacity increases, when do potential throughput and realized performance diverge, and how far can control architecture move that divergence point?**

이를 구성하는 연구 대상:

1. `A`, `λ`, task coupling이 `N_eff`를 어떻게 형성하는가
2. execution stream이 `Λ_control`을 어떻게 생성하는가
3. risk routing / automated oversight / HITL이 `q_control`, `μ_control`을 어떻게 바꾸는가
4. `K`와 queue pressure가 verification quality, delay, rework, opportunity loss에 어떤 영향을 주는가
5. 그 결과 potential performance와 realized performance가 언제 분리되는가
6. control architecture 변화가 그 분리점과 지속가능한 최적 실행률을 얼마나 이동시키는가

이 연결 구조와 측정 방법이 실증적으로 유효하지 않다면 AVCT의 독자 이론으로서의 필요성은 약해진다.

---

# 10. 다음 문헌 과제

- [x] queueing baseline과 AVCT 신규성 분리
- [x] human oversight / automation human-factors 핵심 peer-reviewed 문헌 추가
- [x] time-based competition primary source 확인
- [x] OODA/NBKL peer-reviewed 상태와 역할 결정
- [x] direct oversight-capacity overlap source 기록
- [ ] management control / organizational control theory 연결
- [ ] human review workload의 empirical throughput/accuracy 연구 추가
- [ ] risk-tiered escalation / exception management 실증 문헌 추가
- [ ] multi-agent enterprise workflow의 실제 telemetry 연구 탐색
