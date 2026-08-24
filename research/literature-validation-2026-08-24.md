# AVCT Literature Validation Checkpoint — 2026-08-24

이 문서는 Issue #1의 **claim-boundary hardening**을 위한 검증 기록이다. systematic review가 아니라, AVCT의 핵심 주장과 직접 충돌하거나 경계를 정하는 자료를 우선 확인했다.

## 결론 요약

AVCT가 독창성으로 주장하면 안 되는 영역은 더 명확해졌다.

1. **시간이 경쟁우위다** — 기존 Time-Based Competition 문헌.
2. **queue가 service capacity에 접근하면 지연이 커진다** — 기존 queueing theory.
3. **human oversight는 scale/cognitive-load 한계가 있다** — 기존 HITL 및 agentic controllability 연구.
4. **multi-agent scale-out에는 coordination failure가 있다** — 최신 benchmark evidence 존재.
5. **finite oversight capacity** — 2026-08-17 working paper가 직접 이론화.
6. **risk-tiered / adaptive oversight architecture** — 2026 peer-reviewed 연구가 이미 구체적으로 제안 및 synthetic evaluation.

따라서 AVCT의 차별화 후보는 다음 연결을 **측정하고 반증 가능하게 만드는 것**으로 좁힌다.

> agentic execution generation → coordination/reliability → control-demand arrival → control-service architecture → residual risk / delay / rework → realized performance → upstream feedback

---

# 1. Time-Based Competition — verified background, not novelty

## George Stalk Jr. (1988)

**Time—The Next Source of Competitive Advantage**, Harvard Business Review.

BCG의 공식 역사 페이지는 이 개념이 1980년대 BCG Perspectives에서 등장했고, Stalk의 1988 HBR article을 통해 널리 알려졌음을 확인한다. 1990년 Stalk & Hout의 *Competing Against Time*으로 확장됐다.

AVCT 결정:

- `speed creates competitive advantage`는 신규성에서 제외.
- AVCT는 AI agent가 speed를 parallel action generation으로 확장할 때 control capacity와 어떤 동역학을 만드는지를 연구한다.

Sources:
- https://www.bcg.com/about/overview/our-history/time-based-competition
- https://hbr.org/1988/07/time-the-next-source-of-competitive-advantage

---

# 2. Queueing — K 자체는 borrowed structure

## John D. C. Little (1961)

**A Proof for the Queuing Formula: L = λW**, *Operations Research* 9(3), 383–387.
DOI: `10.1287/opre.9.3.383`

검증된 범위:

- 명시된 stationary 조건에서 `L = λW`를 증명.
- queue/work-in-process, arrival rate, time의 관계는 이미 정립된 이론.

AVCT 결정:

- `K = Λ_control / μ_control`은 queue-utilization-like operational index로 사용.
- `K≈1`에서 delay/backlog가 민감해지는 사실 자체를 AVCT 신규성으로 주장하지 않는다.
- AVCT는 `Λ_control`이 agentic execution architecture에서 어떻게 생성되고, control routing이 arrival/service 구조를 어떻게 바꾸는지에 초점을 둔다.

Source:
- https://pubsonline.informs.org/doi/10.1287/opre.9.3.383

---

# 3. Multi-agent coordination — A 증가 ≠ useful output 증가

## Zhang et al. (ACL 2026)

**SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems**.
ACL 2026 Long Papers.
DOI: `10.18653/v1/2026.acl-long.1354`

검증된 범위:

- 30 tasks, 3 communication-complexity levels.
- 54 configurations, 1,620 experiments.
- Success Rate, Token Consumption, Communication Density 측정.
- `Communication-Reasoning Gap` 보고.
- 높은 coordination complexity에서 scale 증가가 성과 붕괴로 이어짐; Level-III tasks는 50 agents 초과 시 0 success 보고.

AVCT 결정:

- `S = S(A, task structure, protocol)`를 유지할 강한 근거.
- 기업 전체에 직접 일반화하지 않는다.
- AVCT 실증에서는 duplicate/conflict/coordination-latency/useful-output-per-agent를 실제 workflow telemetry로 측정해야 한다.

Source:
- https://aclanthology.org/2026.acl-long.1354/

---

# 4. Human oversight limits — already established research problem

## Lazaros, Vrahatis & Kotsiantis (2026)

**Human-in-the-Loop Artificial Intelligence: A Systematic Review of Concepts, Methods, and Applications**.
*Entropy* 28(4), 377.
DOI: `10.3390/e28040377`

AVCT 경계:

- HITL scalability, cognitive load, trust calibration 자체는 신규 주장 아님.

Source:
- https://doi.org/10.3390/e28040377

## Nguyen et al. (2026)

**On Controllability in Agentic AI: A Survey**.
*Minds and Machines* 36, 29.
DOI: `10.1007/s11023-026-09783-y`

검증된 범위:

- agentic AI가 human cognitive capacity를 넘는 speed/scale에서 classical real-time monitoring assumption이 어려워짐을 명시.
- constraints/guardrails, adaptive control, agent-in-the-loop, human-in-the-loop 네 control paradigms를 정리.
- automated oversight scalability와 human judgment legitimacy 사이 tension 제시.

AVCT 결정:

- `μ_control`은 human headcount가 아니라 control architecture 전체의 effective service capacity로 해석.
- control controller type과 timing을 실증 schema에 포함.

Source:
- https://link.springer.com/article/10.1007/s11023-026-09783-y

---

# 5. Meaningful / adaptive oversight — P7의 신규성 경계

## Zhu et al. (2026)

**Designing meaningful human oversight in AI**.
*AI and Ethics* 6, article 286.
DOI: `10.1007/s43681-026-01147-7`

검증된 범위:

- AI operative agency와 human evaluative agency를 구분.
- solve–verify asymmetry를 이용해 인간이 task를 다시 풀지 않고 효율적으로 검증하도록 설계하는 것을 제안.
- structured rationales, confidence signals, policy attribution, circuit breakers 등 oversight mechanisms 제시.

AVCT 결정:

- efficient verification architecture 자체는 AVCT 발명이 아님.
- P7은 어떤 architecture가 `q_control`, `μ_control`, residual risk를 바꾸어 **execution–realization divergence point**를 이동시키는지를 계량하는 명제로 제한.

Source:
- https://link.springer.com/article/10.1007/s43681-026-01147-7

## Kumar & Singh (2026)

**Balancing autonomy and oversight in reliable agentic artificial intelligence through adaptive human interaction architectures**.
*Discover Artificial Intelligence* 6, article 709.
DOI: `10.1007/s44163-026-01373-2`

검증된 범위:

- Dynamic Intervention Framework를 synthetic enterprise automation tasks 5,000건에서 평가.
- 논문 보고 기준 human intervention을 14.5% decision steps로 줄이면서 full-human-oversight와 통계적으로 동등한 task success rate를 제시.
- static HITL의 latency/cognitive burden을 agentic deployment의 핵심 tension으로 다룸.

주의:

- synthetic task dataset 기반이며 보편적 기업 효과로 일반화할 수 없음.
- AVCT 2차 toy simulation과 유사한 방향의 결과가 이미 peer-reviewed research에 존재한다.

AVCT 결정:

- `risk-tiered/adaptive oversight can reduce human load` 자체를 신규 주장으로 제시하지 않는다.
- AVCT는 architecture별 **execution capacity → control load → residual risk → realized value frontier**를 공통 metric으로 비교하는 쪽으로 차별화한다.

Source:
- https://link.springer.com/article/10.1007/s44163-026-01373-2

---

# 6. Direct overlap — finite oversight capacity

## Kadowaki (2026)

**Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents**.
VURA Working Paper Series No. 8, v1.3, 2026-08-17.
DOI: `10.5281/zenodo.21971214`

상태:

- working paper; peer reviewed journal article이 아님.
- finite oversight capacity를 직접 중심 개념으로 다룸.

AVCT 결정:

- `human oversight capacity is finite`의 최초성 주장 금지.
- 이 paper를 direct-overlap source로 지속 추적.
- AVCT는 finite capacity 자체보다 execution-generation layer와 realized-performance feedback까지 포함한 coupled operational model에 집중.

Source:
- https://www.vuracapital.com/theory/human-on-the-loop

---

# 7. OODA / NBKL — supporting analogue only

## Cullen, Alpcan & Kalloniatis (2025)

**Game-Theoretic Analysis of Adversarial Decision Making in a Complex Socio-Physical System**.
*Dynamic Games and Applications* 15, 709–728.
DOI: `10.1007/s13235-024-00593-4`

검증된 범위:

- Networked Boyd–Kuramoto–Lanchester (NBKL) 모델을 사용.
- networked agents의 decision state, synchronization, resource reallocation, adversarial competition을 결합.

AVCT 결정:

- NBKL/OODA는 **core derivation에서 제외하고 supporting analogue로 유지**.
- 이유: adversarial resource competition에는 강한 관련성이 있지만 일반 enterprise agent workflow의 control-service bottleneck을 직접 설명하지 않는다.

Source:
- https://link.springer.com/article/10.1007/s13235-024-00593-4

---

# 8. v0.1 Claim Boundary — frozen checkpoint

현재 공개 가능한 핵심 명제:

1. Agentic execution은 action generation rate와 parallelism을 확대할 수 있다.
2. Effective output 증가는 coordination/reliability에 조건부다.
3. Control-demand arrival은 execution architecture와 risk routing의 함수다.
4. Queue saturation 자체는 기존 이론이며 AVCT 신규성이 아니다.
5. Potential throughput과 realized performance는 control bottleneck, delay, rework, residual risk 때문에 분리될 수 있다는 것이 AVCT의 핵심 검증 대상이다.
6. Control architecture는 divergence point를 이동시킬 수 있지만 **residual-risk budget을 만족할 때만** 지속 가능한 개선으로 본다.
7. Reversibility는 주로 error probability가 아니라 error consequence / recovery loss를 조절하는 변수로 취급한다.
8. Lanchester는 inspiration / nonlinear boundary case이며 derivation source가 아니다.
9. OODA/NBKL은 supporting analogue이며 core foundation이 아니다.

현재 금지 claim:

- AI 속도 2배 = 경쟁력 4배.
- `P = V²` 또는 `P = N_eff²`의 보편법칙 선언.
- `K≈1` 또는 finite human oversight의 최초 이론화.
- risk-tiered oversight의 최초 제안.
- public social benefit가 AI speed의 제곱으로 증가한다는 주장.
- simulation의 synthetic threshold를 실제 조직의 안전 기준으로 사용.

이 boundary는 empirical evidence가 추가될 때까지 AVCT v0.1 공개 기준으로 사용한다.
