# First Simulation Results — AVCT v0.1

> 상태: **structural sanity check**. 이 결과는 경험적 검증이 아니며 AVCT를 증명하지 않는다. 사용한 가정과 함수형이 예상 패턴을 재현할 수 있는지 공격적으로 확인하기 위한 첫 실행이다.

## 1. 목적

첫 시뮬레이션은 H1, H2, H5, H6만 다룬다.

- H1: 에이전트 수 증가가 항상 유효 실행량을 비례 증가시키는가?
- H2: 작업 결합도가 높을수록 조정 효율 저하가 커지는가?
- H5: `K = Λ_control / μ_control`이 1에 접근/초과할 때 queue가 민감해지는가?
- H6: 잠재 처리량 증가가 통제 포화 이후에도 실현 성과 증가로 이어지는가?

재현 코드는 `validation/simulations/avct_v01.py`에 있다.

---

## 2. 최소 모형의 가정

### Coordination experiment

- `A = 1, 2, 4, 8, 16, 32`
- agent당 후보 실행률 `λ = 1.5 / step`
- reliability `R = 0.95` 고정
- 동일 step에서 같은 task target을 선택한 행동은 duplicate로 처리
- low coupling proxy: target pool 200
- high coupling proxy: target pool 20
- 20 seeds 평균

이 task-pool 크기는 실제 조직의 task coupling을 측정한 값이 아니라 **민감도 실험을 위한 proxy**다.

### Control experiment

- 모든 unique action이 control queue를 통과하는 control-gated workflow
- FIFO queue
- `μ_control = 6, 12, 24 actions / step`
- `K = arrival_rate / μ_control`
- time-insensitive condition: `decay = 0`
- time-sensitive condition: 지연 `d`에 대해 action value를 `exp(-0.03 d)`로 할인

`decay = 0.03` 역시 실증 추정치가 아니라, **통제 지연이 가치에 영향을 주는 환경과 그렇지 않은 환경을 분리하기 위한 가정**이다.

---

# 3. H1/H2 — 병렬화와 조정 효율

## Low coupling proxy

| A | raw rate | N_eff | N_eff / A | S |
|---:|---:|---:|---:|---:|
| 1 | 1.50 | 1.42 | 1.42 | 0.998 |
| 2 | 3.00 | 2.83 | 1.41 | 0.995 |
| 4 | 6.00 | 5.62 | 1.40 | 0.988 |
| 8 | 12.01 | 11.08 | 1.38 | 0.973 |
| 16 | 23.99 | 21.48 | 1.34 | 0.945 |
| 32 | 47.97 | 40.49 | 1.27 | 0.891 |

## High coupling proxy

| A | raw rate | N_eff | N_eff / A | S |
|---:|---:|---:|---:|---:|
| 1 | 1.50 | 1.37 | 1.37 | 0.982 |
| 2 | 3.00 | 2.64 | 1.32 | 0.951 |
| 4 | 6.00 | 4.93 | 1.23 | 0.885 |
| 8 | 12.01 | 8.58 | 1.07 | 0.769 |
| 16 | 23.99 | 13.28 | 0.83 | 0.595 |
| 32 | 47.97 | 17.26 | 0.54 | 0.385 |

## 판정

### H1 — 첫 모형에서 재현됨

`A`가 32배가 되면 raw action rate는 약 32배 증가하지만 유효 실행량은 같은 비율로 증가하지 않았다. 특히 high-coupling proxy에서는 `N_eff/A`가 약 `1.37 → 0.54`로 크게 감소했다.

그러나 이것은 **중복 가능성이 커지는 task-target 구조를 모형에 넣었기 때문에 나타난 결과**다. 따라서 H1의 경험적 증거가 아니라, H1을 검증할 때 어떤 실제 측정값이 필요한지 보여주는 구조적 결과다.

필요한 실제 지표:
- duplicate work rate
- merge/conflict rate
- coordination latency
- useful output / agent

### H2 — 방향성은 재현되지만 아직 독립 검증 아님

high-coupling proxy에서 `S` 하락이 훨씬 강하게 나타났다. 하지만 coupling을 target-pool 크기로 직접 구현했으므로 결과는 가정에 종속적이다.

**결론:** `S = S(A, task coupling, architecture)`라는 함수형을 유지할 이유는 있지만, 구체 함수는 아직 고정하지 않는다.

---

# 4. H5 — 통제 포화

대표 조건 `μ_control = 12`:

| A | arrival rate | K | mean delay | mean backlog | realized rate (decay=0) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.50 | 0.125 | 0.00 | 0.00 | 1.42 |
| 2 | 2.97 | 0.248 | 0.00 | 0.00 | 2.82 |
| 4 | 5.92 | 0.493 | 0.00 | 0.01 | 5.62 |
| 8 | 11.61 | 0.968 | 1.09 | 12.79 | 11.04 |
| 16 | 22.55 | 1.879 | 281.66 | 7,410.67 | 11.41 |
| 32 | 42.63 | 3.553 | 431.30 | 21,461.22 | 11.40 |

`K≈1` 부근에서 queue delay가 민감해지고 `K>1`에서 backlog가 지속적으로 누적되는 패턴이 나타났다.

### 판정

**H5는 구조적으로 재현되지만 AVCT의 신규 증거가 아니다.** 이는 standard queueing intuition과 정합적인 sanity check다.

AVCT가 연구해야 할 부분은 `K≈1`이라는 사실 자체가 아니라:

1. agentic execution이 `Λ_control`을 어떤 속도로 생성하는지,
2. risk routing이 `q_control`을 얼마나 줄일 수 있는지,
3. automation / governance가 `μ_control`을 얼마나 높일 수 있는지,
4. 높은 K가 다시 reliability와 realized performance에 어떤 영향을 주는지

이다.

---

# 5. H6 — 잠재 실행량과 실현 성과의 분리

## Time-insensitive value (`decay = 0`, μ=12)

A가 8에서 16으로 증가할 때 unique action rate는 약 `11.61 → 22.55`로 거의 두 배가 됐지만 realized rate는 `11.04 → 11.41`로 사실상 포화했다.

A=32에서는 unique action rate가 `42.63`까지 증가하지만 realized rate는 `11.40` 수준에 머문다.

즉 **raw/potential throughput과 realized throughput을 분리해서 보아야 한다**는 H6의 최소 형태가 재현된다.

## Time-sensitive value (`decay = 0.03`, μ=12)

| A | K | mean delay | realized rate | last-200 realized rate |
|---:|---:|---:|---:|---:|
| 1 | 0.125 | 0.00 | 1.42 | 1.42 |
| 2 | 0.248 | 0.00 | 2.82 | 2.81 |
| 4 | 0.493 | 0.00 | 5.62 | 5.63 |
| 8 | 0.968 | 1.09 | 10.69 | 10.70 |
| 16 | 1.879 | 281.66 | 0.05 | ~0 |
| 32 | 3.553 | 431.30 | 0.01 | ~0 |

통제 지연에 따라 가치가 소멸하는 환경을 가정하면, `K>1`의 불안정 queue에서 실현 성과가 단순 포화가 아니라 급격히 감소했다.

이 결과는 **P6의 비단조 가능성이 어떤 조건에서 발생할 수 있는지** 보여준다. 그러나 감소의 강도는 `decay` 가정에 매우 민감하므로 보편적 결과로 주장해서는 안 된다.

---

# 6. Control capacity sensitivity

last-200 realized performance, time-insensitive:

| A | μ=6 | μ=12 | μ=24 |
|---:|---:|---:|---:|
| 1 | 1.42 | 1.42 | 1.42 |
| 2 | 2.81 | 2.81 | 2.81 |
| 4 | 5.66 | 5.63 | 5.64 |
| 8 | 5.70 | 10.99 | 10.99 |
| 16 | 5.70 | 11.42 | 21.49 |
| 32 | 5.70 | 11.41 | 22.77 |

통제 처리율 `μ_control`을 높이면 포화 시점이 오른쪽으로 이동했다. 이는 AVCT의 핵심 경영 질문을 단순 `max A` 또는 `max λ`가 아니라 **실행 capacity와 control capacity의 공동 설계**로 두는 것이 합리적임을 보여주는 구조적 결과다.

---

# 7. 첫 판정

| 가설 | 첫 결과 | 상태 |
|---|---|---|
| H1 병렬성 체감 | high coupling에서 강한 체감 | 유지, 실증 필요 |
| H2 조정효율 매개 | coupling proxy에 따라 S 차이 | 유지, 함수형 미고정 |
| H5 통제 포화 | K≈1 부근에서 delay/backlog 민감 | 기존 queueing 결과로 분리 |
| H6 성과전환 제한 | time-insensitive에서는 포화, time-sensitive에서는 역전 가능 | **핵심 명제로 유지** |

## 현재 가장 중요한 발견

첫 시뮬레이션에서 AVCT의 가장 가치 있는 연구 대상은 `K>1이면 queue가 쌓인다`가 아니라 다음 관계로 좁혀졌다.

> **Agentic execution capacity가 증가할 때 potential throughput과 realized performance가 언제 분리되는가, 그리고 control architecture가 그 분리점을 얼마나 이동시키는가?**

이 질문은 queueing theory 자체보다 AVCT의 독자적인 연구 방향에 더 가깝다.

---

# 8. 다음 공격 항목

1. coupling proxy를 단순 target-pool이 아닌 dependency graph로 교체
2. `q_control < 1` 및 risk-tiered routing 추가
3. reliability를 고정값이 아니라 queue pressure / speed의 함수로 두는 실험
4. reviewer error / cognitive load 추가
5. reversible vs irreversible action의 손실함수 분리
6. 실제 agent workflow 로그에서 `Λ_control`, duplicate rate, review delay를 측정할 수 있는 데이터 스키마 설계
7. 이론 명제와 기존 queueing / human oversight 연구의 경계를 선행연구에서 재검증

---

## 데이터

- `generated/coordination-summary.csv`
- `generated/control-summary.csv`

모든 숫자는 저장소의 재현 코드로 다시 생성할 수 있다.
