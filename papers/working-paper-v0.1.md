# AI Velocity–Control Theory

## An Execution–Control Feedback Model for Agentic Organizations

**Working Paper v0.1 — Conceptual Baseline + First Structural Validation**

> This is a conceptual working paper. The proposed relationships are hypotheses and analytical constructs, not empirically validated laws. The first simulation is a structural sanity check, not evidence of real-world causal validity.

---

## Abstract

AI agents change organizational execution not only by automating individual tasks but by increasing the rate and parallelism at which actions can be generated and executed. This can expand the number of experiments, decisions, customer responses, code changes, analyses, and operational interventions that occur within the same response window. Yet the capacity to coordinate, review, authorize, monitor, correct, and take responsibility for those actions does not necessarily scale at the same rate.

This paper proposes **AI Velocity–Control Theory (AVCT)** as a conceptual model of the relationship between agentic execution capacity and organizational control capacity. Rather than directly replacing the force variable in Lanchester's square law with AI execution speed, AVCT defines an **Effective Action Mass** (`N_eff`) formed by parallel agent count, per-agent execution rate, time window, coordination efficiency, and execution reliability. Competitive or organizational effect is modeled with an empirically testable exponent rather than an assumed square law. A second layer models control saturation as the ratio between the arrival rate of actions requiring control and the organization's control-processing capacity.

AVCT's primary research question is:

> **When agentic execution capacity increases, when do potential throughput and realized performance diverge, and how far can control architecture move that divergence point?**

The first minimal simulation reproduces four structural patterns under explicit toy assumptions: diminishing scale-out efficiency under stronger task coupling, queue sensitivity as control demand approaches service capacity, saturation of realized throughput when control capacity becomes the bottleneck, and possible decline of time-sensitive realized value under prolonged control delay. These results do not validate AVCT empirically; they narrow the theory toward testable organizational measurements.

**Keywords:** agentic AI, multi-agent systems, execution velocity, organizational control, human oversight, AI governance, control saturation, Lanchester-inspired model

---

# 1. Problem

Traditional organizations scale execution through people, process, capital, software, and managerial coordination. Agentic AI adds a different scaling mechanism: a small human team can instantiate multiple software agents, run tasks in parallel, repeat them rapidly, and connect those agents directly to operational tools.

This changes the relevant management question from only:

> How much work can the organization perform?

into:

> How quickly can the organization create useful actions, and how much of that action stream can it safely coordinate, verify, govern, absorb, and reverse?

Time as a source of competitive advantage is not a new idea. Stalk's time-based competition work established organizational response time as a strategic variable decades before modern AI. Likewise, finite human attention, automation bias, multi-agent coordination loss, and queue saturation are established research problems. AVCT therefore does not claim novelty for any of these elements separately.

Its candidate contribution is to connect them as an **agentic execution–control feedback system** and make that system measurable.

---

# 2. From Execution Velocity to Effective Action Mass

Early versions of this idea treated AI execution velocity as an analogue of force size in Lanchester's square law. That direct substitution is too strong. Force size is a stock variable, whereas execution velocity is a rate, and the Lanchester square law itself is not a universal empirical law of real conflict.

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

The important implication is conditional scale-out. Increasing `A` or `λ` can increase candidate action volume, but coordination failures or reduced reliability may offset that gain. SILO-BENCH provides a recent empirical benchmark showing that larger communicating multi-agent LLM systems can fail to convert communication into effective distributed computation, especially as coordination complexity rises. AVCT treats this as support for keeping `S` task- and architecture-dependent, not as proof of any particular AVCT function.

---

# 3. A Lanchester-Inspired, Not Lanchester-Derived, Effect Model

AVCT does not assert that AI execution produces a square-law advantage.

Instead it uses a general empirical form:

`P_AI = α · N_eff^β`

The exponent `β` is a quantity to be estimated or rejected.

Possible interpretations:

- `β < 1`: diminishing returns or congestion,
- `β = 1`: proportional effect,
- `β > 1`: superlinear effect under specific mechanisms such as rapid learning, first response, concentration, or network reinforcement,
- `β = 2`: a special Lanchester-square-like boundary case, not the default.

Lanchester's role in AVCT is analytical rather than predictive. It motivates the question of when coordinated multiplicity can produce nonlinear effects; it does not determine the answer in advance.

---

# 4. Control Demand and Control Capacity

AI actions differ in risk. Some can be automatically accepted, some need sampled or automated verification, and some require explicit human authorization.

Let:

- `Λ_control` = average arrival rate of control-requiring actions,
- `μ_control` = average control-processing capacity of the organization.

Define:

`K = Λ_control / μ_control`

This is the **Control Saturation Ratio**.

This ratio is structurally equivalent to utilization in basic queueing models. AVCT does **not** claim the arrival/service-rate ratio, the `ρ<1` stability condition of an M/M/1 queue, Little's Law, or queue-delay growth as new mathematics.

Under a simple queue-like interpretation:

- `K < 1`: average service capacity exceeds average control demand,
- `K → 1`: delay becomes increasingly sensitive in simple stationary models,
- `K > 1`: unresolved control work accumulates unless arrivals, service capacity, rejection, batching, prioritization, or operating rules change.

The AVCT question begins one layer earlier and extends one layer later:

1. how agentic execution generates `Λ_control`,
2. how control architecture changes `q_control`, service time, and `μ_control`,
3. how queue pressure changes verification quality, delay, rework, and opportunity value,
4. how those effects feed back into realized performance.

`μ_control` should not be interpreted as human headcount alone. Agentic controllability research distinguishes constraints and guardrails, adaptive controls, agent-in-the-loop oversight, and human-in-the-loop oversight. Meaningful oversight research also suggests that verification architecture can change the cost of review by exploiting solve–verify asymmetry. Thus control capacity is partly a design variable.

---

# 5. Execution and Control as a Feedback System

AVCT proposes the following coupled mechanism:

```text
more agents / higher execution rate
              ↓
higher candidate action volume
              ↓
coordination + reliability filtering
              ↓
higher Effective Action Mass
              ↓
higher potential organizational value
              ↓
control-requiring action stream
              ↓
higher Control Saturation Ratio
              ↓
delay / backlog / rework / control debt
              ↓
possible degradation in review quality,
coordination, reliability, or opportunity value
              ↓
lower or saturated realized performance
```

The management problem is therefore not `max A` or `max λ`.

It is closer to:

> maximize realized performance subject to coordination, reliability, verification, control-capacity, risk, and reversibility constraints.

---

# 6. Theoretical Propositions

**P1 — Conditional scale-out.** Increasing agent count and execution rate increases candidate action volume, but the gain in effective action mass can be limited by coordination efficiency and reliability.

**P2 — Coordination dependence.** Scale-out efficiency is more likely to decline when tasks are strongly coupled, communication-intensive, or share bottleneck resources.

**P3 — Conditional nonlinear effect.** Effective action mass can produce superlinear organizational or competitive effects only under specific environmental mechanisms. `β>1` is not universal.

**P4 — Control-demand generation.** Increased execution scope and rate tend to increase the absolute number of actions requiring review unless routing, authority boundaries, automated verification, or other control architecture reduce `q_control`.

**P5 — Queueing connection.** Higher `K` is associated with greater control delay and backlog under compatible queueing assumptions. The queue-saturation result itself is borrowed theory, not an AVCT novelty claim.

**P6 — Potential–realized divergence.** As agentic execution increases, potential throughput and realized performance can diverge when control capacity becomes a bottleneck. Time-insensitive workflows may saturate; workflows with delay, rework, recovery, or opportunity costs may exhibit performance reversal.

**P7 — Control architecture as production infrastructure.** Better control architecture can move the divergence point by reducing unnecessary control demand, improving verification efficiency, increasing effective service capacity, or lowering the cost of error and recovery.

**P8 — Sustainable velocity.** The organization with the highest short-run execution rate need not be the organization with the highest long-run realized value.

---

# 7. Relationship to Existing Work and Novelty Boundary

AVCT is not novel because it observes any of the following:

- speed can be a competitive advantage,
- Lanchester-style concentration can create nonlinear attrition effects under specific assumptions,
- more agents can create coordination overhead,
- human attention and oversight are limited,
- automation bias and complacency exist,
- queues saturate as arrival rates approach service capacity,
- human-in-the-loop, agent-in-the-loop, guardrails, escalation, or circuit breakers can provide control.

Several recent sources make the overlap especially clear.

- **SILO-BENCH (ACL 2026)** reports a communication-reasoning gap and performance collapse at high coordination complexity, narrowing any claim that agent count alone creates effective mass.
- **Nguyen et al. (2026)** survey agentic AI controllability and explicitly discuss the difficulty of real-time human control when systems operate at speeds and scales beyond human cognitive capacity.
- **Lazaros et al. (2026)** identify scalability, cognitive load, and trust calibration as deployment challenges in HITL AI.
- **Kadowaki (2026)** directly proposes a conceptual theory of finite oversight capacity in a non-peer-reviewed working paper. AVCT therefore cannot claim discovery of finite oversight capacity.
- **Zhu et al. (2026)** frame oversight as an architectural allocation of operative and evaluative agency and emphasize solve–verify asymmetry.
- **Little (1961)** and standard queueing theory already provide the mathematical foundation for arrival/service capacity relationships.
- **Stalk (1988)** establishes time as a strategic source of competitive advantage long before agentic AI.

AVCT's candidate contribution is narrower:

> a measurable model linking **agentic execution generation → coordination/reliability → control demand → control service architecture → realized performance**, including the conditions under which potential and realized performance diverge.

If this connected model adds no predictive or design value beyond applying existing queueing, human-factors, and multi-agent models independently, AVCT should not be treated as a separate theory.

---

# 8. OODA and NBKL: Supporting Analogue, Not Core Foundation

Networked Boyd–Kuramoto–Lanchester (NBKL) research combines cyclic decision-state synchronization, networked agents, resource reallocation, and adversarial Lanchester-style competition. Cullen, Alpcan, and Kalloniatis published a peer-reviewed game-theoretic NBKL study in *Dynamic Games and Applications*.

This is relevant to AVCT because it demonstrates that synchronization, network structure, and resource competition can be studied jointly in adversarial multi-agent systems.

However, AVCT does **not** use NBKL or OODA as a direct proof of enterprise AI execution–control dynamics. Their role in v0.1 is a supporting theoretical analogue only.

---

# 9. First Structural Validation

The first minimal simulation is documented in `validation/results/first-simulation-v0.1.md` and reproduced by `validation/simulations/avct_v01.py`.

It is deliberately simple.

## Coordination sanity check

With a collision-based task-coupling proxy:

- low-coupling conditions retained relatively high scale-out efficiency,
- high-coupling conditions showed a strong decline in `N_eff/A` and `S` as `A` increased.

This preserves P1/P2 as testable propositions but does not validate a specific coordination function.

## Control saturation sanity check

With `μ_control = 12` actions/step:

- `A=8`: `K≈0.97`, mean review delay ≈ 1.09 steps,
- `A=16`: `K≈1.88`, mean review delay ≈ 281.66 steps,
- `A=32`: `K≈3.55`, mean review delay ≈ 431.30 steps.

This is expected queue behavior and is treated as model verification, not AVCT novelty.

## Potential–realized divergence

At `μ_control=12`, increasing from `A=8` to `A=16` nearly doubled unique candidate throughput while time-insensitive realized throughput moved only from about `11.04` to `11.41`, indicating saturation at the control bottleneck.

When a toy delay-value decay `exp(-0.03d)` was added, realized value fell sharply after persistent queue overload. The direction supports P6 as a conditionally plausible mechanism; the magnitude is entirely dependent on the assumed decay function and is not a real-world estimate.

## First theory decision

The simulation shifts emphasis away from “control saturation exists” toward:

> **what determines the divergence point between potential and realized performance, and which control architectures move it?**

That becomes the priority of the next simulation and empirical program.

---

# 10. Validation Program

## Simulation stage 2

The next simulation should add:

- dependency-graph tasks instead of a target-pool coupling proxy,
- risk-tiered routing with `q_control < 1`,
- reversible vs irreversible actions,
- reviewer error / cognitive-load effects,
- automated oversight and human oversight as distinct service paths.

The main target is P6/P7: whether control architecture moves the potential–realized divergence point without unacceptable risk leakage.

## Empirical stage

The minimum telemetry schema for a real agentic workflow should eventually measure:

- agent count and concurrency,
- candidate actions / time,
- unique completed actions,
- duplicate/conflict actions,
- actions by risk tier,
- review arrival rate,
- review service time,
- automated vs human review path,
- queue delay,
- approval/rejection accuracy where ground truth exists,
- rollback/rework,
- opportunity-value loss from delay,
- realized business/operational output.

Without such data, AVCT remains conceptual.

---

# 11. Limitations of v0.1

This version does not establish:

- a universal value of `β`,
- a universal coordination function `S(A, task)`,
- a universal safe threshold for `K`,
- a causal relationship between high `K` and organizational incidents,
- a universal speed–reliability trade-off,
- a square-law relationship between AI velocity and business value,
- a square-law relationship between service speed and public social benefit,
- that AVCT is superior to a composition of existing queueing, human-factors, and organizational-control models.

The last point is an explicit falsification condition for the theory as a distinct framework.

---

# 12. Research Direction

If supported, AVCT may evolve into three practical artifacts:

1. **measurement model** — how to measure effective action mass and control saturation from real agent logs,
2. **predictive model** — when additional agents or faster execution cease to improve realized performance,
3. **design framework** — how routing, authority boundaries, observability, automated oversight, human review, and reversibility increase sustainable execution velocity.

The long-term thesis is:

> The strongest agentic organization may not be the one that runs AI fastest. It may be the one that converts the greatest amount of fast, parallel machine action into accountable, recoverable, and compounding realized value.

---

# Selected References — Verified v0.1 Set

- Bainbridge, L. (1983). *Ironies of Automation*. Automatica, 19(6), 775–779. DOI: `10.1016/0005-1098(83)90046-8`
- Parasuraman, R., & Manzey, D. H. (2010). *Complacency and Bias in Human Use of Automation: An Attentional Integration*. Human Factors, 52(3), 381–410. DOI: `10.1177/0018720810376055`
- Little, J. D. C. (1961). *A Proof for the Queuing Formula: L = λW*. Operations Research, 9(3), 383–387. DOI: `10.1287/opre.9.3.383`
- Stalk, G., Jr. (1988). *Time—The Next Source of Competitive Advantage*. Harvard Business Review, July 1988.
- Hartley, D. S. III, & Helmbold, R. L. (1995). *Validating Lanchester's square law and other attrition models*. Naval Research Logistics, 42(4), 609–633. DOI: `10.1002/1520-6750(199506)42:4<609::AID-NAV3220420408>3.0.CO;2-W`
- Kress, M. (2020). *Lanchester Models for Irregular Warfare*. Mathematics, 8(5), 737. DOI: `10.3390/math8050737`
- Langer, M., Baum, K., & Schlicker, N. (2025). *Effective Human Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection of Inaccurate and Unfair Outputs*. Minds and Machines, 35, 1. DOI: `10.1007/s11023-024-09701-0`
- Batool, A., Zowghi, D., & Bano, M. (2025). *AI governance: a systematic literature review*. AI and Ethics, 5, 3265–3279. DOI: `10.1007/s43681-024-00653-w`
- Cullen, A. C., Alpcan, T., & Kalloniatis, A. C. (2025). *Game-Theoretic Analysis of Adversarial Decision Making in a Complex Socio-Physical System*. Dynamic Games and Applications, 15, 709–728. DOI: `10.1007/s13235-024-00593-4`
- Zhang, Y. et al. (2026). *SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems*. ACL 2026 Long Papers, 29379–29398. DOI: `10.18653/v1/2026.acl-long.1354`
- Lazaros, K., Vrahatis, A. G., & Kotsiantis, S. (2026). *Human-in-the-Loop Artificial Intelligence: A Systematic Review of Concepts, Methods, and Applications*. Entropy, 28(4), 377. DOI: `10.3390/e28040377`
- Nguyen, M. H., Nguyen, D.-H., O’Sullivan, B., & Nguyen, H. D. (2026). *On Controllability in Agentic AI: A Survey*. Minds and Machines, 36, 29. DOI: `10.1007/s11023-026-09783-y`
- Zhu, L. et al. (2026). *Designing meaningful human oversight in AI*. AI and Ethics, 6, 286. DOI: `10.1007/s43681-026-01147-7`
- Kadowaki, N. (2026). *Human-on-the-Loop: A Theory of Oversight Capacity, Its Failure Modes, and the Non-Delegable Residual in the Age of AI Agents*. VURA Working Paper Series No. 8. DOI: `10.5281/zenodo.21971214`. **Working paper; not peer reviewed.**
