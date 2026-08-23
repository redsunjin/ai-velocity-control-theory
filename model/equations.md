# Equations — v0.1

이 문서의 수식은 **검증 전 개념 모형**이다. 각 식은 데이터를 통해 수정·기각될 수 있다.

## 1. Effective Action Mass

최소 모형:

`N_eff(T) = A · λ · T · S · R`

단위:

- `A`: agents
- `λ`: candidate actions / (agent · time)
- `T`: time
- `S`: dimensionless coordination efficiency
- `R`: dimensionless reliability
- `N_eff`: effective actions

이 형태의 목적은 속도(rate)를 병력 수(stock)에 직접 치환하지 않고, **시간 창 안의 유효 행동량**으로 변환하는 것이다.

### 확장 후보

조정 효율을 에이전트 수와 작업 구조의 함수로 둔다.

`S = S(A, D, L, M)`

- `D`: task dependency / coupling
- `L`: communication latency
- `M`: shared-memory or context quality

필요하다면 신뢰도 역시 속도와 병렬성의 함수로 둔다.

`R = R(λ, A, Q, G)`

- `Q`: task/model fit
- `G`: guardrails / governance quality

따라서 높은 속도와 큰 `A`가 자동으로 큰 `N_eff`를 보장하지 않는다.

---

## 2. Competitive / Organizational Effect

일반형:

`P_AI = α · N_eff^β`

이 식은 하나의 보편 성과함수가 아니다. 연구별로 종속변수를 정의한 뒤 적합도를 검증한다.

### β 해석

- `β < 1`: diminishing returns / congestion
- `β = 1`: proportional effect
- `β > 1`: superlinear effect
- `β = 2`: Lanchester-square-like special case

AVCT v0.1은 `β > 1`조차 보편적으로 주장하지 않는다.

### 포화형 대안

현실 조직에서 무한한 power-law 증가가 부적절할 수 있으므로 다음 형태도 비교 후보로 둔다.

`P_AI = P_max · (1 - exp(-c · N_eff))`

또는 통제 포화를 결합한 형태:

`P_realized = P_potential · F(K)`

여기서 `F(K)`는 `K` 증가에 따라 감소할 수 있는 realization factor다. v0.1에서는 구체 함수형을 고정하지 않는다.

---

## 3. Control Demand

단순 근사:

`Λ_control = q_control · λ_action`

여기서 `λ_action`은 단위 시간당 통제 대상이 될 수 있는 AI 행동률이다.

`N_eff` 기반으로 관찰 창 `T`에서 근사한다면:

`Λ_control ≈ q_control · N_eff(T) / T`

주의: 잘못된 행동도 통제를 발생시킬 수 있으므로 실제 연구에서는 `N_eff`보다 **candidate/executed action rate**를 사용하는 것이 더 적절할 수 있다.

---

## 4. Control Saturation Ratio

`K = Λ_control / μ_control`

단위가 같은 두 rate의 비율이므로 dimensionless다.

### 단순 queue-like 해석

정상상태에 가까운 단순 조건에서:

- `K < 1`: 평균 처리 능력이 평균 도착률을 초과
- `K ≥ 1`: backlog가 안정적으로 해소되지 않을 가능성

그러나 burstiness, priority, service-time distribution, batching, abandonment, automated rejection이 있는 실제 조직에서는 `K` 하나로 지연이나 사고 확률을 예측할 수 없다.

따라서 AVCT는 queueing theory의 기존 결과를 재발명하지 않고, 필요한 경우 M/M/c, M/G/c, priority queue 등 적절한 기존 모델을 사용한다.

---

## 5. Control Debt Dynamics — 후보 모형

미처리 통제 요구의 단순 누적량을 `D_c`라고 할 때:

`dD_c/dt = max(0, Λ_control - μ_control)`

이는 직관 표현이며 실제 queue length 방정식의 대체물이 아니다.

향후에는 이미 실행된 행동의 사후 정정 비용까지 포함하여 `Control Debt`를 별도 상태변수로 확장한다.

---

## 6. 핵심 피드백의 수식적 방향

가설적 방향성:

1. `A ↑` 또는 `λ ↑` → 잠재 실행량 ↑
2. 일정 수준 이후 `S ↓` 또는 `R ↓` 가능
3. 실행량 ↑ → `Λ_control ↑`
4. `K ↑` → 지연·누적·검토 품질 저하 가능
5. 검토 품질 저하/충돌 증가 → `R ↓`, `S ↓`
6. 결국 실제 `N_eff`와 realized performance가 감소할 수 있음

이 구조는 AVCT가 최적점을 가질 수 있음을 시사한다.

`argmax_{A, λ} P_realized(A, λ | μ_control, S, R, risk constraints)`

즉 핵심 경영 문제는 단순한 `max λ`가 아니라 **통제 제약하에서의 실행 최적화**가 된다.

---

## 7. 아직 금지된 수식 주장

다음 표현은 검증 전에는 사용하지 않는다.

- `P_AI = V²`를 법칙으로 선언
- `P_AI = N_eff²`를 기본 법칙으로 선언
- `K = P_AI / C_human`
- `K > 1`이면 반드시 사고가 발생한다고 주장
- 공공 사회적 이익 `SocialProfit ∝ V²`

이들은 과거 아이디어의 발전 과정에서는 사용됐지만 AVCT v0.1 기준식에서는 제외한다.
