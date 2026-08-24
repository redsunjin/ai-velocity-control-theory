# Second Simulation Results — AVCT v0.1 Hardening

> 상태: **structural sensitivity test**. 이 결과는 경험적 검증이 아니며 실제 조직의 오류율, 위험분포, 감독 품질을 추정하지 않는다. 목적은 H6/H7/H8을 공격하고, 어떤 조건에서 명제가 유지되거나 약화되는지 확인하는 것이다.

## 1. 핵심 질문

1. 동일한 agentic execution capacity에서 control architecture가 control saturation point를 이동시킬 수 있는가?
2. 위험기반 라우팅은 안전성 저하 없이 인간 통제 부하를 줄일 수 있는가?
3. reversibility는 동일한 오류 발생량에서 손실 강도를 줄이는가?

재현 코드:

- `validation/simulations/avct_v01_control_architecture.py`

생성 데이터:

- `generated/control-architecture-summary.csv`
- `generated/verifier-sensitivity-summary.csv`
- `generated/reversibility-summary.csv`

---

# 2. 가정

이 실험의 숫자는 모두 synthetic parameter다.

- agent당 실행률: `λ = 1.5 / step`
- human control service capacity: `μ_control = 12 / step`
- risk mix: low 70%, medium 20%, high 10%
- synthetic invalid rate: low 1%, medium 5%, high 15%
- human reviewer sensitivity: 97%
- human false reject: 1%
- automated verifier false-positive: 1%
- medium-risk unflagged sampling: 15%
- delay-sensitive value decay: `exp(-0.005 d)`

`full_review`는 모든 action을 human queue로 보낸다.

`tiered`는:

- low risk: automated verification
- medium risk: automated verification + sampling + escalation
- high risk: full human gate

으로 구성했다.

이 구조는 특정 산업의 권장 정책이 아니라 **control routing이 어떤 구조적 trade-off를 만드는지 보기 위한 toy architecture**다.

---

# 3. Experiment A — saturation point 이동

## Full review

| A | K | mean delay | final backlog | unsafe / 1000 exec | net value / step |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.499 | 0.002 | 0 | 0.997 | 8.30 |
| 8 | 0.999 | 4.694 | 80 | 1.030 | 16.14 |
| 16 | 2.000 | 249.926 | 11,994 | 1.062 | 5.99 |
| 32 | 3.999 | 375.035 | 35,989 | 1.022 | 4.17 |

전수 human review에서는 `A≈8`에서 이미 `K≈1`에 도달했다. 이후 잠재 실행량은 계속 증가하지만 queue가 불안정해지고 delay-sensitive realized value는 감소했다.

## Tiered routing, automated verifier sensitivity 99%

| A | K | mean delay | final backlog | unsafe / 1000 exec | net value / step |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.074 | 0.000 | 0 | 1.001 | 8.38 |
| 8 | 0.147 | 0.000 | 0 | 0.955 | 16.77 |
| 16 | 0.295 | ~0 | 0 | 1.007 | 33.48 |
| 32 | 0.587 | 0.009 | ~0 | 0.980 | 67.06 |
| 64 | 1.177 | 75.232 | 2,122 | 0.843 | 118.70 |

동일한 `μ_control=12`에서 control saturation은 full review의 `A≈8` 부근에서 tiered architecture의 `A=32~64` 사이로 이동했다.

**구조적 해석:** control architecture는 `q_control`을 낮춰 `Λ_control` 증가율을 실행량 증가율보다 낮게 만들 수 있다.

그러나 이 결과는 automated verifier가 충분히 높은 sensitivity를 가진다는 가정에 의존한다.

---

# 4. Experiment B — H7의 반례와 임계조건

안전성을 비교하기 위해 full-review가 안정적인 `A=4`, `K≈0.50` 조건을 baseline으로 사용했다.

## Full review baseline

- `K = 0.500`
- unsafe escape ≈ `1.031 / 1000 executed actions`
- harm ≈ `16.36 / 1000 executed actions`
- net value ≈ `8.33 / step`

## Tiered routing sensitivity

| automated verifier sensitivity | K | unsafe / 1000 exec | harm / 1000 exec | net value / step |
|---:|---:|---:|---:|---:|
| 70% | 0.073 | 5.556 | 28.54 | 8.37 |
| 80% | 0.073 | 3.943 | 23.46 | 8.39 |
| 90% | 0.074 | 2.313 | 18.96 | 8.40 |
| 95% | 0.074 | 1.530 | 16.70 | 8.41 |
| 97% | 0.074 | 1.218 | 15.88 | 8.41 |
| 98% | 0.074 | 1.115 | 15.75 | 8.41 |
| 99% | 0.074 | 0.981 | 15.52 | 8.41 |
| 99.5% | 0.074 | 0.905 | 15.22 | 8.42 |

### 판정

**H7/P7은 무조건적 명제로 유지하면 안 된다.**

위험기반 routing 자체는 human load를 크게 줄였지만 verifier sensitivity가 낮을 때 unsafe escape가 증가했다.

이 toy model에서는 약 99% 수준의 automated verification sensitivity에서야 full-review baseline과 유사하거나 더 낮은 unsafe-escape 수준을 보였다.

이 99%는 현실 임계값이 아니다. risk mix, error distribution, human sensitivity, sampling rate, loss function을 바꾸면 달라진다.

따라서 P7을 다음처럼 강화한다.

> **Control architecture can move the execution–realization divergence point only when its routing and verification quality keep residual risk within the relevant risk budget.**

즉 control architecture의 가치는 단순 `K` 감소가 아니라 **`K` 감소와 residual-risk 보존을 동시에 달성하는가**로 평가해야 한다.

---

# 5. Experiment C — reversibility

Tiered-90 architecture에서 routing, `K`, unsafe-escape count는 유지하고 reversibility만 변경했다.

| A | reversibility | K | unsafe / 1000 exec | harm / 1000 exec | net value / step |
|---:|---|---:|---:|---:|---:|
| 4 | baseline | 0.074 | 2.313 | 18.96 | 8.40 |
| 4 | high | 0.074 | 2.313 | 11.23 | 8.44 |
| 32 | baseline | 0.584 | 2.375 | 19.35 | 66.88 |
| 32 | high | 0.584 | 2.375 | 11.79 | 67.23 |

오류 수 자체는 같았지만 손실 강도는 약 38~41% 감소했다.

### 판정

H8의 최소 형태는 구조적으로 유지한다.

> reversibility는 error probability를 낮추는 변수라기보다 **error consequence를 낮추는 loss-modifier**로 모델링하는 편이 더 정확하다.

따라서 향후 AVCT에서 reversibility는 `R` 안에 숨기기보다 별도 변수 또는 loss function의 parameter로 두는 것이 적절하다.

---

# 6. 이번 시뮬레이션이 바꾼 이론

## H6 / P6 — 강화

potential throughput과 realized performance의 divergence는 첫 실험뿐 아니라 control routing을 바꾼 두 번째 toy model에서도 관찰됐다.

다만 divergence point는 고정값이 아니라:

- `q_control`
- `μ_control`
- verification quality
- value decay
- risk distribution

에 따라 이동한다.

## H7 / P7 — 수정 필요

이전 표현:

> risk-tiering과 exception-based review는 control load를 낮추며 성과를 높일 수 있다.

수정 표현:

> risk-tiering과 exception-based review는 control load를 낮출 수 있지만, **residual-risk budget을 만족할 정도의 routing/verification quality가 확보될 때만** sustainable realized-performance frontier를 바깥쪽으로 이동시킨다.

## H8 — 유지, 역할 명확화

reversibility는 control demand를 직접 줄이지 않아도 동일 오류의 expected loss를 줄일 수 있다.

---

# 7. 새 핵심 지표 후보

이번 결과로 `K`만으로는 control architecture를 평가할 수 없다는 점이 명확해졌다.

최소한 다음 지표가 함께 필요하다.

1. `K = Λ_control / μ_control`
2. unsafe escape / 1,000 executed actions
3. harm / 1,000 executed actions
4. realized net value / time
5. human review load / time
6. rollback / recovery cost

향후에는 이들을 묶어 **Execution–Control Frontier**를 비교하는 방향이 유망하다.

같은 raw execution capacity에서:

- 낮은 `K`
- 낮은 residual risk
- 높은 realized value

를 동시에 달성하는 architecture가 더 우수하다.

---

# 8. 한계

이 시뮬레이션은 다음을 포함하지 않는다.

- 실제 AI agent 호출
- 실제 human reviewer
- reviewer fatigue / cognitive-load feedback
- correlated or adversarial errors
- automated verifier 운영비용
- task dependency graph
- action priority / deadline scheduling
- organizational responsibility cost
- realistic irreversible externalities

따라서 결과의 숫자를 현실 임계값으로 해석하면 안 된다.

특히 automated verifier sensitivity 99%는 **실험 가정 안에서 나온 sensitivity boundary**일 뿐, AVCT의 법칙이나 권장 기준이 아니다.

---

# 9. 다음 검증 질문

이번 결과는 AVCT의 다음 질문을 더 좁힌다.

> **어떤 control architecture가 execution–control frontier를 실제로 개선하는가?**

이를 위해 다음 단계에서는:

1. verifier sensitivity / specificity / cost를 동시에 모델링
2. human reviewer sensitivity가 `K`와 cognitive load에 따라 변하는 feedback 추가
3. dependency graph를 통해 coordination loss와 control demand를 연결
4. 실제 agent workflow telemetry schema 작성
5. 동일 task set을 다양한 agent/control architecture로 실행하는 실증 실험 설계

를 진행한다.
