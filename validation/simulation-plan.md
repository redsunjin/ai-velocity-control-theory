# Simulation Plan — v0.1

## 목적

AVCT의 모든 주장을 한 번에 증명하려 하지 않는다. 첫 시뮬레이션의 목적은 다음 네 현상이 최소 모형에서도 재현 가능한지 확인하는 것이다.

1. 에이전트 수 증가가 항상 유효 실행량을 비례 증가시키지는 않는다.
2. 조정 효율 저하는 병렬화 이익을 상쇄할 수 있다.
3. 통제 수요가 통제 처리율에 접근하면 backlog와 대기시간이 민감해진다.
4. 잠재 처리량은 증가하지만 실현 성과는 일정 구간 이후 둔화 또는 감소할 수 있다.

## 최소 모델

시간을 discrete step으로 둔다.

각 step에서:

1. `A`개의 에이전트가 확률적으로 작업을 생성/완료한다.
2. `λ`에 따라 후보 행동 수가 결정된다.
3. coordination penalty를 적용해 중복/충돌 행동을 제거한다.
4. reliability `R`에 따라 유효/오류 행동을 나눈다.
5. `q_control` 비율의 행동을 control queue로 보낸다.
6. control servers가 `μ_control`만큼 처리한다.
7. 승인된 유효 행동은 performance score에 반영한다.
8. 오류, 재작업, rollback, queue delay는 cost로 반영한다.

## 1차 변수

### 조작 변수
- `A`: 1, 2, 4, 8, 16, 32
- `λ`: low / medium / high
- task coupling: low / high
- `μ_control`: low / medium / high

### 중간 변수
- `S`
- `R`
- `Λ_control`
- `K`
- queue length
- mean review delay

### 결과 변수
- raw actions
- valid unique actions
- approved actions
- net realized value
- rework cost
- rollback cost

## coordination penalty 후보

처음부터 복잡한 함수형을 주장하지 않는다. 비교를 위해 2~3개 단순 형태를 사용한다.

예시:

`S(A) = 1 / (1 + c(A-1))`

또는 threshold형:

- `A ≤ A*`: S ≈ constant
- `A > A*`: S declines

이 함수는 이론이 아니라 sensitivity analysis용 가정이다.

## control queue

초기에는 단순 queue를 사용하되, 기존 queueing theory 결과와 AVCT 결과를 혼동하지 않는다.

필요 시 이후:
- M/M/c
- priority queue
- burst arrivals
- risk-weighted service time
- automated rejection/approval

으로 확장한다.

## 핵심 그래프

첫 결과물은 아래 5개면 충분하다.

1. `A` vs `N_eff`
2. `A` vs `N_eff/A`
3. `K` vs mean control delay
4. raw throughput vs realized performance
5. `A × μ_control` heatmap of realized performance

## 성공 기준

시뮬레이션이 AVCT를 “증명”할 필요는 없다.

성공은 다음 중 하나다.

- 어떤 가정에서 예상 패턴이 나타나는지 확인
- 예상 패턴이 나타나지 않는 조건을 발견
- `S`, `R`, `K` 중 실제 설명력이 낮은 변수를 제거
- 새로운 interaction term이 필요함을 발견

즉 첫 시뮬레이션은 **이론을 보호하는 작업이 아니라 이론을 공격하는 작업**이어야 한다.

## 다음 단계

시뮬레이션 후 반드시 다음을 기록한다.

- 살아남은 명제
- 기각/수정된 명제
- 결과가 가정에 과민한 부분
- 실제 조직 데이터로 측정해야 하는 변수
