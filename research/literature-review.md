# Literature Review Map — v0.1

> 검증 갱신: 2026-08-24. 이 문서는 systematic review가 아니라 **AVCT의 claim boundary를 정하기 위한 선행연구 지도**다. peer-reviewed source, working paper, practitioner source를 구분한다.

AVCT는 다음 연구 흐름의 교차점에 있다.

1. Lanchester / attrition modeling
2. Time-based competition / organizational speed
3. Agentic AI and multi-agent coordination
4. Human oversight / automation human factors
5. Queueing / service-capacity theory
6. Agentic AI controllability / oversight architecture
7. OODA / NBKL adversarial decision dynamics

보다 상세한 최신 검증 기록은 `research/literature-validation-2026-08-24.md`를 참조한다.

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

Sources:
- https://hbr.org/1988/07/time-the-next-source-of-competitive-advantage
- https://www.bcg.com/about/overview/our-history/time-based-competition

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
- AVCT의 simulation은 이 결과를 재현한 것이 아니라 별도의 toy-model sanity check다.

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

AVCT 연결:
- `μ_control`은 단순 reviewer headcount가 아니다.
- reviewer sensitivity/quality가 pressure에 따라 달라질 수 있으므로 향후 reviewer-error feedback이 필요하다.

Source: https://doi.org/10.1177/0018720810376055

## Langer, Baum & Schlicker (2025) — peer reviewed

**Effective Human Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection of Inaccurate and Unfair Outputs**  
Minds and Machines 35, article 1.  
DOI: `10.1007/s11023-024-09701-0`

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

AVCT 연결:
- control architecture를 인간 reviewer 수만으로 모델링해서는 안 된다.
- `μ_control`에는 guardrail, automated oversight, AITL, HITL의 조합이 반영될 수 있다.

Source: https://link.springer.com/article/10.1007/s11023-026-09783-y

## Zhu et al. (2026) — peer reviewed

**Designing meaningful human oversight in AI**  
AI and Ethics 6, article 286.  
Published 4 May 2026.  
DOI: `10.1007/s43681-026-01147-7`

핵심:
- AI의 operative agency와 인간의 evaluative agency를 구분.
- solve–verify asymmetry를 활용하여 humans가 AI solution을 재수행하지 않고 효율적으로 검증할 수 있도록 oversight를 설계해야 한다고 제안.
- structured rationales, confidence signals, policy attribution, circuit breakers 등 mechanism 제시.

AVCT 연결:
- `q_control`과 `μ_control`은 고정된 인간 능력이 아니라 **verification architecture에 의해 설계 가능한 변수**다.

Source: https://link.springer.com/article/10.1007/s43681-026-01147-7

## Kumar & Singh (2026) — peer reviewed research

**Balancing autonomy and oversight in reliable agentic artificial intelligence through adaptive human interaction architectures**  
Discover Artificial Intelligence 6, article 709.  
DOI: `10.1007/s44163-026-01373-2`

핵심:
- Dynamic Intervention Framework를 5,000 synthetic enterprise automation tasks에서 평가.
- 논문 보고 기준 human intervention을 14.5% decision steps로 줄이면서 full-human oversight와 통계적으로 동등한 task success rate를 제시.
- static HITL의 latency와 cognitive burden을 agentic workflow의 bottleneck으로 다룸.

AVCT 제약:
- adaptive/risk-tiered oversight 자체는 신규 주장 아님.
- synthetic dataset 결과를 일반 기업에 직접 일반화하지 않는다.

AVCT 연결:
- architecture별 `K`, residual risk, realized value의 joint frontier를 공통 metric으로 비교하는 연구 방향을 강화한다.

Source: https://link.springer.com/article/10.1007/s44163-026-01373-2

---

# 6. Direct overlap: oversight capacity

## Kadowaki (2026) — non-peer-reviewed working paper

**Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents**  
VURA Working Paper Series No. 8, Version 1.3.  
Published 17 Aug 2026.  
DOI: `10.5281/zenodo.21971214`

확인된 상태:
- conceptual working paper.
- finite oversight capacity를 직접 중심 개념으로 다룸.

AVCT 제약:
- “oversight capacity is finite” 또는 “agent throughput can overwhelm human oversight”를 최초 주장으로 제시하지 않는다.

AVCT 차별화 후보:
- execution generation (`A`, `λ`, `S`, `R`)
- control demand (`Λ_control`)
- queue/control architecture (`q_control`, `μ_control`)
- residual risk / recovery
- realized performance feedback

의 **전체 운영 동역학**과 측정/실증에 초점을 둔다.

Source: https://www.vuracapital.com/theory/human-on-the-loop

---

# 7. Queueing / service capacity

## Little (1961) — peer reviewed foundational theorem

John D. C. Little, **A Proof for the Queuing Formula: L = λW**, Operations Research 9(3), 383–387.  
DOI: `10.1287/opre.9.3.383`

핵심:
- stationary 조건 등 명시된 조건에서 평균 system population, arrival rate, mean time의 관계 `L = λW`를 증명.

Source: https://doi.org/10.1287/opre.9.3.383

## Queue-utilization baseline

AVCT 제약:
- `K = Λ_control / μ_control`은 queue utilization과 구조적으로 동일한 ratio다.
- `K≈1`에서 delay가 민감해지는 현상은 **AVCT의 수학적 신규성 주장이 아니다.**
- simulation H5는 이 연결을 검산한 것일 뿐이다.

AVCT 연구 대상:
- AI execution architecture가 `Λ_control`을 어떻게 생성하는가?
- oversight design이 `q_control`, service time, `μ_control`을 어떻게 바꾸는가?
- queue pressure가 review accuracy, residual risk, realized value에 어떤 feedback을 만드는가?

---

# 8. OODA / NBKL — supporting, not core

## Cullen, Alpcan & Kalloniatis (2025) — peer reviewed

**Game-Theoretic Analysis of Adversarial Decision Making in a Complex Socio-Physical System**  
Dynamic Games and Applications 15, 709–728.  
DOI: `10.1007/s13235-024-00593-4`

핵심:
- networked Boyd–Kuramoto–Lanchester (NBKL) resource competition model을 사용.
- networked agents의 decision-state synchronisation, resource reallocation, adversarial attrition을 결합.

AVCT 결정:
- **OODA/NBKL은 AVCT의 필수 중심축에서 내리고 supporting theoretical analogue로 둔다.**
- enterprise AI execution throughput과 control-service saturation을 직접 도출하는 근거로 사용하지 않는다.

Source: https://link.springer.com/article/10.1007/s13235-024-00593-4

---

# 9. 현재 문헌 판정

## 강하게 지지되는 배경

- 속도는 전략 변수다.
- 병렬 agent 증가에는 coordination limit이 존재할 수 있다.
- human oversight에는 scalability/cognitive-load 문제가 있다.
- control architecture는 human review load를 설계적으로 바꿀 수 있다.
- queue saturation은 기존 이론으로 설명된다.

## 아직 AVCT가 직접 검증해야 할 것

- 실제 agent workflow에서 `N_eff`를 신뢰성 있게 측정할 수 있는가?
- execution growth가 실제 `Λ_control`을 어떤 함수로 증가시키는가?
- coordination failure가 추가 control demand를 발생시키는가?
- control architecture가 `K`를 낮추면서 residual risk를 유지하는 frontier가 실제로 존재하는가?
- 이 coupled model이 기존 개별 이론을 따로 쓰는 것보다 추가 설명력/설계 가치를 제공하는가?

이 질문에 실증적으로 답하지 못하면 AVCT는 별도 이론이 아니라 유용한 conceptual synthesis로 남아야 한다.
