# Validation

AVCT의 검증은 이론을 보호하기 위한 작업이 아니라 반증 가능한 형태로 공격하기 위한 작업이다.

## 현재 순서

1. `hypotheses.md` — 개념 명제를 검증 가능한 가설로 변환
2. `simulation-plan.md` — 최소 시뮬레이션 설계
3. `simulations/` — 재현 가능한 코드
4. `results/` — 실행 결과와 해석

## 해석 원칙

- 시뮬레이션은 경험적 증거가 아니다.
- 가정으로 넣은 구조가 결과에서 다시 나타났다고 해서 이론이 검증된 것은 아니다.
- 특히 queue saturation은 기존 queueing theory의 결과이며 AVCT의 신규성이 아니다.
- AVCT의 핵심 검증 대상은 AI의 속도·병렬성이 통제수요를 어떻게 만들고, 통제 포화가 realized performance를 어떻게 제한하거나 역전시키는가이다.

## v0.1 최소 검증

- H1/H2: agent scale-out과 coordination efficiency
- H5: control arrival/service ratio와 queue delay
- H6: potential throughput과 realized performance의 분리

결과는 `results/first-simulation-v0.1.md`를 기준으로 읽는다.
