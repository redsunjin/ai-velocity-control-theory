# AI Velocity–Control Theory

## An Execution–Control Feedback Model for Agentic Organizations

**Working Paper v0.1 — Conceptual Baseline**

> This is a conceptual working paper. The proposed relationships are hypotheses and analytical constructs, not empirically validated laws.

---

## Abstract

AI agents change organizational execution not only by automating individual tasks but by increasing the rate and parallelism at which actions can be generated and executed. This creates a potential competitive advantage: more experiments, decisions, customer responses, code changes, analyses, and operational interventions can occur within the same response window. Yet the capacity to review, authorize, monitor, correct, and take responsibility for those actions does not necessarily scale at the same rate.

This paper proposes **AI Velocity–Control Theory (AVCT)** as a conceptual model of this imbalance. Rather than directly replacing the force variable in Lanchester's square law with AI execution speed, AVCT defines an **Effective Action Mass** (`N_eff`) formed by parallel agent count, per-agent execution rate, time window, coordination efficiency, and execution reliability. The organizational or competitive effect of this action mass is modeled with an empirically testable exponent rather than an assumed square law. A second layer models **control saturation** as the ratio between the arrival rate of actions requiring control and the organization's control-processing capacity.

The central proposition is that sustainable advantage in agentic organizations does not arise from maximum execution velocity alone. It arises from the ability to increase useful parallel execution while keeping coordination, reliability, and control saturation within a range that allows potential output to become realized performance. AVCT therefore treats execution and control as a coupled feedback system rather than as opposing goals.

**Keywords:** agentic AI, multi-agent systems, execution velocity, organizational control, human oversight, AI governance, Lanchester-inspired model, control saturation

---

# 1. Problem

Traditional organizations scale execution through people, process, capital, software, and managerial coordination. Agentic AI adds a different scaling mechanism: a small human team can instantiate multiple software agents, run tasks in parallel, repeat them rapidly, and connect those agents directly to operational tools.

This changes the relevant management question.

The question is no longer only:

> How much work can the organization perform?

It becomes:

> How quickly can the organization create useful actions, and how much of that action stream can it safely understand, govern, absorb, and reverse?

If execution capacity grows faster than control capacity, automation may initially increase throughput while later producing approval queues, conflicting changes, rework, unreviewed decisions, responsibility gaps, or recovery costs. Conversely, an organization that requires human review for every low-risk action may suppress most of the economic value of agentic execution.

AVCT focuses on this tension.

---

# 2. From Execution Velocity to Effective Action Mass

Early versions of this idea treated AI execution velocity as an analogue of force size in Lanchester's square law. That direct substitution is too strong. Force size is a stock variable, whereas execution velocity is a rate. Moreover, historical research does not establish the homogeneous Lanchester square law as a universal law of real conflict.

AVCT therefore converts execution rate into a quantity defined over a meaningful time window.

For a time window `T`:

`N_eff(T) = A · λ · T · S · R`

where:

- `A` = number of parallel agents contributing to the task,
- `λ` = candidate execution rate per agent,
- `T` = relevant response or competition window,
- `S` = coordination efficiency,
- `R` = execution reliability.

`N_eff` is not raw tool calls. It is an analytical approximation of the number of unique, coordinated, valid actions produced within the window.

The important implication is that scale-out is conditional. Increasing `A` or `λ` can increase potential action volume, but coordination failures or lower reliability can offset that increase.

---

# 3. A Lanchester-Inspired, Not Lanchester-Derived, Effect Model

AVCT does not assert that AI execution produces a square-law advantage.

Instead it uses a general empirical form:

`P_AI = α · N_eff^β`

The exponent `β` is a quantity to be estimated or rejected.

Possible interpretations include:

- `β < 1`: diminishing returns or congestion,
- `β = 1`: proportional effect,
- `β > 1`: superlinear effect under mechanisms such as rapid learning, first response, concentration, or network reinforcement,
- `β = 2`: a special Lanchester-square-like boundary case, not the default.

Lanchester's contribution to AVCT is therefore analytical rather than predictive. It motivates the question of when coordinated multiplicity can produce nonlinear effects; it does not determine the answer in advance.

---

# 4. Control Demand and Control Capacity

AI actions differ in risk. Some can be automatically accepted, some need sampling, and some require explicit human authorization.

Let:

- `Λ_control` = average arrival rate of control-requiring actions,
- `μ_control` = average control-processing capacity of the organization.

Define:

`K = Λ_control / μ_control`

This is the **Control Saturation Ratio**.

The ratio is structurally similar to utilization in queueing systems. AVCT does not claim that arrival/service-rate mathematics is new. Its research question is how agentic execution generates `Λ_control`, how governance architecture changes both arrival and service capacity, and how saturation feeds back into execution quality.

Under a simple stationary interpretation:

- `K < 1`: average capacity exceeds average demand,
- `K → 1`: delay and backlog become increasingly sensitive,
- `K > 1`: unresolved control work can accumulate if the operating structure does not change.

Real systems require richer models for burstiness, priority, heterogeneous risk, service-time distributions, automated rejection, and incident recovery.

---

# 5. Execution and Control as a Feedback System

AVCT proposes the following coupled mechanism:

```text
more agents / higher execution rate
              ↓
higher potential action volume
              ↓
coordination + reliability filtering
              ↓
higher Effective Action Mass
              ↓
higher potential organizational value
              ↓
more control-requiring actions
              ↓
higher Control Saturation Ratio
              ↓
delay / backlog / rework / control debt
              ↓
possible decline in coordination and reliability
              ↓
lower realized performance
```

This suggests that the organizational optimum may not occur at maximum agent count or maximum execution rate.

The optimization problem is closer to:

> maximize realized performance subject to coordination, reliability, control, risk, and reversibility constraints.

---

# 6. Theoretical Propositions

AVCT v0.1 advances the following propositions for testing.

**P1.** Increasing agent count and execution rate increases potential action volume, but the gain in effective action mass is limited by coordination efficiency and reliability.

**P2.** Coordination efficiency is more likely to decline with agent scale when tasks are strongly coupled or communication-intensive.

**P3.** Effective action mass can produce superlinear performance effects only under specific environmental mechanisms; superlinearity is not universal.

**P4.** Increased execution scope and rate generally increase absolute control demand unless risk routing reduces the fraction of actions requiring control.

**P5.** Higher control saturation is associated with greater delay, backlog, and control burden under otherwise similar operating conditions.

**P6.** At sufficiently high control saturation, the marginal realized value of additional execution can decline or become negative because of delay, rework, recovery cost, or degraded review quality.

**P7.** Good control architecture can increase sustainable velocity by reducing unnecessary control demand and increasing effective control capacity.

---

# 7. Relationship to Existing Work

AVCT is not novel because it observes that speed matters, that human attention is finite, or that queues saturate.

Its proposed contribution lies in coupling several established research problems:

1. organizational and competitive speed,
2. scalable agentic execution,
3. multi-agent coordination efficiency,
4. execution reliability,
5. governance and human oversight capacity,
6. queue-like control saturation,
7. feedback from control overload back into realized execution quality.

Recent multi-agent benchmarks show that increasing the number of communicating LLM agents does not guarantee improved distributed performance. Recent work on human-on-the-loop governance also directly argues that human oversight is a finite resource under high agent throughput. These findings narrow, rather than eliminate, AVCT's potential contribution: the theory must explain and test the **coupling** between execution scaling and control scaling, rather than claim discovery of either problem individually.

---

# 8. Validation Program

The first validation stage will use simulation, not to prove AVCT, but to attack it.

The minimum experiment will vary:

- agent count,
- execution rate,
- task coupling,
- coordination penalty,
- reliability,
- control capacity.

The first target observations are:

- whether per-agent effective output declines with scale in coupled tasks,
- whether control delay rises sharply as demand approaches capacity,
- whether raw throughput and realized performance diverge,
- whether a performance optimum can emerge below maximum execution velocity.

Subsequent validation should use organizational logs, controlled workflow experiments, or case studies.

---

# 9. Limitations of v0.1

This version does not establish:

- a universal value of `β`,
- a universal coordination function `S(A)`,
- a universal safe threshold for `K`,
- a causal relationship between `K` and organizational incidents,
- a square-law relationship between AI velocity and business value,
- a square-law relationship between service speed and public social benefit.

These are explicitly outside the current claim boundary.

---

# 10. Research Direction

If supported, AVCT may evolve from a conceptual model into three practical artifacts:

1. **measurement model** — how to measure effective action mass and control saturation from real agent logs,
2. **predictive model** — when additional agents or faster execution cease to improve realized performance,
3. **design framework** — how authority boundaries, exception routing, observability, automation, and reversibility increase sustainable execution velocity.

The long-term thesis is simple:

> The strongest agentic organization may not be the one that runs AI fastest. It may be the one that can convert the greatest amount of fast, parallel machine action into accountable, recoverable, and compounding organizational value.

---

# Selected References — Initial Set

- Hartley, D. S. III, & Helmbold, R. L. (1995). *Validating Lanchester's square law and other attrition models*. Naval Research Logistics, 42(4), 609–633. DOI: 10.1002/1520-6750(199506)42:4<609::AID-NAV3220420408>3.0.CO;2-W
- Kress, M. (2020). *Lanchester Models for Irregular Warfare*. Mathematics, 8(5), 737. DOI: 10.3390/math8050737
- Abou Ali, M., Dornaika, F., & Charafeddine, J. (2026). *Agentic AI: a comprehensive survey of architectures, applications, and future directions*. Artificial Intelligence Review, 59, 11. DOI: 10.1007/s10462-025-11422-4
- Batool, A., Zowghi, D., & Bano, M. (2025). *AI governance: a systematic literature review*. AI and Ethics, 5, 3265–3279. DOI: 10.1007/s43681-024-00653-w
- Zhang, Y. et al. (2026). *SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems*. ACL 2026 Long Papers. https://aclanthology.org/2026.acl-long.1354/
- Kadowaki, N. (2026). *Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents*. VURA Working Paper Series No. 8. Working paper; not treated as peer-reviewed evidence.
