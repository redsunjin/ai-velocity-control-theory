# Literature Review Map — v0.1

> 상태: 초기 맵. 이 문서는 완성된 systematic review가 아니다. 공개 주장에 사용하기 전 각 논문의 원문·방법·한계를 다시 확인한다.

AVCT는 최소 다섯 개 연구 흐름의 교차점에 있다.

1. Lanchester / attrition modeling
2. Agentic AI and multi-agent coordination
3. Human oversight / AI governance
4. Queueing and service-capacity theory
5. Time-based competition / organizational speed

---

## 1. Lanchester models

### Hartley & Helmbold (1995)

**Validating Lanchester's square law and other attrition models**  
Naval Research Logistics, 42(4), 609–633.  
DOI: `10.1002/1520-6750(199506)42:4<609::AID-NAV3220420408>3.0.CO;2-W`

핵심:
- 한국전쟁 인천-서울 전역 데이터로 homogeneous square law를 검증.
- 단일 상수계수의 homogeneous square-law battle 가정은 데이터에 충분히 맞지 않음.
- square law를 전쟁의 입증된 보편 알고리즘으로 볼 수 없으며, 그렇다고 완전히 기각됐다고도 할 수 없다는 결론.

AVCT에 주는 제약:
- `β=2`를 보편값으로 선언하면 안 된다.
- Lanchester는 inspiration / boundary case로 사용하는 것이 타당하다.

Source: https://onlinelibrary.wiley.com/doi/10.1002/1520-6750%28199506%2942%3A4%3C609%3A%3AAID-NAV3220420408%3E3.0.CO%3B2-W

### Kress (2020)

**Lanchester Models for Irregular Warfare**  
Mathematics 8(5), 737.  
DOI: `10.3390/math8050737`

핵심:
- Lanchester 계열 모델이 특정 교전 구조를 분석하기 위한 모델군임을 보여준다.
- 실제 상황에 맞춰 모델 구조가 달라져야 한다는 점이 AVCT의 “직접 치환 금지” 원칙과 정합적이다.

Source: https://www.mdpi.com/2227-7390/8/5/737

---

## 2. Agentic AI

### Abou Ali, Dornaika & Charafeddine (2026)

**Agentic AI: a comprehensive survey of architectures, applications, and future directions**  
Artificial Intelligence Review 59, 11.  
DOI: `10.1007/s10462-025-11422-4`

핵심:
- Agentic AI를 자율적 계획, 메모리, 도구 사용, 환경 피드백, 다중 에이전트 협력 등의 관점에서 체계화.
- 거버넌스와 신뢰성 문제를 agentic architecture의 핵심 연구 과제로 다룸.

AVCT 연결:
- AI 에이전트를 단순 LLM 호출이 아닌 실행 주체로 보는 기반.
- `A`, `λ`, `R`, governance의 operational definition을 정교화할 때 참조.

Source: https://doi.org/10.1007/s10462-025-11422-4

### Peykani et al. (2026)

**A Holistic Review of Agentic AI Frameworks, Applications, and Research Trajectories**  
Archives of Computational Methods in Engineering, 2026.

핵심:
- multi-agent interaction, orchestration, agent safety, accountability를 주요 연구 문제로 정리.
- 신뢰 가능한 scale-out이 아직 해결된 문제가 아님을 강조.

Source: https://link.springer.com/article/10.1007/s11831-026-10675-8

---

## 3. Multi-agent coordination scaling

### Zhang et al. (ACL 2026)

**SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems**  
Proceedings of ACL 2026, Long Papers.

핵심:
- 30개 알고리즘 과제, 54개 구성, 1,620개 실험으로 분산형 multi-agent coordination을 평가.
- 에이전트가 활발히 통신해도 효과적인 분산 계산으로 연결되지 않는 communication-reasoning gap을 관찰.
- 복잡도가 높아질수록 성능이 붕괴하고, Level-III 과제에서는 50개 초과 에이전트에서 성공률 0을 보고.

AVCT 연결:
- `A` 증가가 자동으로 `N_eff` 증가를 의미하지 않는다는 근거.
- `S = S(A, task structure, protocol)`의 필요성을 뒷받침.

주의:
- 특정 benchmark 결과를 모든 기업 업무로 일반화하지 않는다.

Source: https://aclanthology.org/2026.acl-long.1354/

---

## 4. AI governance

### Batool, Zowghi & Bano (2025)

**AI governance: a systematic literature review**  
AI and Ethics 5, 3265–3279.  
DOI: `10.1007/s43681-024-00653-w`

핵심:
- AI governance를 누가(Who), 무엇을(What), 언제(When), 어떻게(How) 통제하는지 조직·산업·국가 등 다층 관점에서 정리.
- governance artifacts와 실제 적용·검증의 한계를 지적.

AVCT 연결:
- `μ_control`을 단순 인간 검토자 수가 아닌 조직적 governance capacity로 확장할 이론적 배경.

Source: https://doi.org/10.1007/s43681-024-00653-w

---

## 5. Oversight capacity — 직접 중복 가능성이 높은 연구

### Kadowaki (2026, working paper)

**Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents**  
VURA Working Paper Series No. 8, published 17 Aug 2026.

핵심:
- 인간 oversight를 유한한 capacity로 보고 agent throughput 증가가 per-item human oversight의 확장성을 압박하는 문제를 전면적으로 다룸.

AVCT에 주는 의미:
- “인간 감독 용량이 유한하다” 자체를 AVCT의 독창적 최초 주장으로 제시하면 안 된다.
- AVCT의 차별화 후보는 **경쟁적 실행량 형성 → 비선형 성과 가능성 → 통제 포화 → 다시 조정효율/신뢰도에 피드백**되는 전체 동역학에 둔다.

상태:
- peer-reviewed journal article이 아니라 최신 working paper로 구분하여 인용한다.

Source: https://www.vuracapital.com/theory/human-on-the-loop

---

## 6. Queueing theory

`K = Λ_control / μ_control` 구조는 queue utilization과 매우 가깝다.

따라서 다음을 AVCT의 수학적 신규성으로 주장하지 않는다.

- arrival rate / service rate 비율
- utilization이 1에 접근할 때 지연이 민감해지는 현상
- capacity보다 arrival이 큰 상태에서 backlog가 증가하는 현상

AVCT가 추가로 연구해야 하는 것은:

- AI 실행 속도/병렬성이 `Λ_control`을 어떻게 생성하는가
- governance architecture가 `q_control`과 `μ_control`을 어떻게 바꾸는가
- 높은 `K`가 다시 `S`, `R`, realized performance에 어떤 피드백을 주는가
- risk severity와 reversibility가 동일한 queue 상태의 실제 손실을 어떻게 바꾸는가

표준 queueing 문헌은 working paper 작성 단계에서 별도 bibliographic review로 보강한다.

---

## 7. Time-based competition

시간과 응답속도를 경쟁 변수로 보는 경영전략 연구는 AVCT의 중요한 선행축이다.

v0.1 문헌 검토에서는 다음을 분리해서 확인한다.

- lead time reduction
- fast-cycle capability
- learning-cycle advantage
- first-mover / response-time advantage

AVCT는 “빠르면 유리하다”를 새 주장으로 내세우지 않는다. 차별화 대상은 **agentic parallel execution과 control saturation이 결합될 때 속도 우위가 어디서 역전되는가**다.

---

# 다음 문헌 검토 과제

- [ ] queueing / human service capacity 핵심 문헌 선정
- [ ] human-in-the-loop / human-on-the-loop peer-reviewed 문헌 정리
- [ ] automation bias와 cognitive load 연구 추가
- [ ] organizational control / management control theory 연결
- [ ] time-based competition의 원전과 후속 실증 연구 정리
- [ ] OODA를 AVCT 중심축으로 유지할지 보조 개념으로 내릴지 검토
- [ ] NBKL 계열 연구의 peer-reviewed 상태와 정확한 적용범위 확인
