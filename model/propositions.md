# Propositions — v0.1

아래 명제는 AVCT가 설명하고자 하는 현상을 반증 가능한 형태로 정리한 초안이다. 실증 이전에는 **theoretical propositions**로만 취급한다.

## P1 — 실행량 명제

다른 조건이 동일할 때 병렬 에이전트 수 `A`와 에이전트당 실행률 `λ`의 증가는 잠재 실행량을 증가시킨다.

그러나 실제 유효 실행량 `N_eff`의 증가율은 조정 효율 `S`와 신뢰도 `R`에 의해 제한될 수 있다.

**반증 가능성:** `A`와 `λ`가 증가해도 `S`, `R`이 충분히 안정적이고 `N_eff`가 지속적으로 선형 이상 증가하는 환경이 일반적이라면 조정 한계 가설은 약화된다.

**v0.1 simulation note:** collision-based coupling proxy에서는 방향성이 재현되었으나, 이는 구조적 sanity check이며 실증 증거가 아니다.

## P2 — 조정 비용 명제

작업 간 의존성과 통신 필요성이 높을수록, 에이전트 수 증가에 따른 조정 오버헤드가 커져 `S`가 감소할 가능성이 높다.

**예상 관찰:** 독립 작업에서는 scale-out 효율이 높고, 강결합 작업에서는 일정 에이전트 수 이후 marginal gain이 감소한다.

**v0.1 simulation note:** 단순 task-target contention proxy에서 high-coupling 조건의 `S`가 더 빠르게 하락했다. 구체 함수형은 고정하지 않는다.

## P3 — 비선형 경쟁효과 명제

유효 실행량이 시장 선점, 빠른 학습, 네트워크 효과, 동시 집중 같은 메커니즘과 결합될 때 `P_AI`는 선형보다 큰 증가율을 보일 수 있다.

중요: `β>1`은 조건부 명제이며 보편 법칙이 아니다.

## P4 — 통제수요 명제

AI 실행 범위와 실행률이 증가할수록 별도 검토·승인·감사가 필요한 행동의 절대량 `Λ_control`은 증가하는 경향이 있다.

단, 위험 기반 자동 라우팅과 권한 경계가 개선되면 `q_control`을 낮춰 같은 실행량에서도 통제수요 증가를 완화할 수 있다.

## P5 — 통제포화 연결 명제

`K = Λ_control / μ_control`이 높아질수록, 다른 조건이 같다면 통제 대기시간과 backlog가 증가한다.

**이 명제의 포화 현상 자체는 AVCT의 신규 이론 주장이 아니다.** arrival/service capacity와 queue delay의 관계는 기존 queueing theory의 영역이다. AVCT에서 P5의 역할은 agentic execution이 `Λ_control`을 생성하는 과정과 기존 queue dynamics를 연결하는 것이다.

**v0.1 simulation note:** `K≈1` 부근의 민감도와 `K>1` backlog 누적이 재현되었다. 이는 모델 검산으로만 취급한다.

## P6 — 잠재 실행량–실현 성과 분리 명제

`N_eff` 증가가 잠재 성과를 높이더라도 control capacity가 병목이 되면 **potential throughput과 realized performance가 분리**될 수 있다.

- 통제 지연이 가치에 거의 영향을 주지 않는 환경에서는 realized performance의 한계효과가 0에 가까워지는 **포화**가 나타날 수 있다.
- 통제 지연, 오류 회수, 재작업 또는 기회비용이 큰 환경에서는 realized performance의 한계효과가 음수가 되는 **역전**도 가능하다.

즉 속도 증가와 실현 성과 사이의 관계는 task value decay, control architecture, reliability, reversibility에 조건부일 수 있다.

**v0.1 simulation note:** time-insensitive 조건에서는 포화, delay-sensitive 조건에서는 강한 하락이 재현되었다. 하락의 강도는 가정한 decay 함수에 민감하므로 보편 법칙으로 주장하지 않는다.

## P7 — 통제 아키텍처 명제

예외 중심 관리, 권한 경계, 관측 가능성, 자동 차단, reversibility가 높은 조직은 동일한 AI 실행량에서 더 낮은 `Λ_control` 또는 더 높은 `μ_control`을 달성할 수 있다.

따라서 통제는 속도의 단순한 반대항이 아니라 **속도를 성과로 변환하는 생산 인프라**로 작동할 수 있다.

## P8 — 지속 가능한 우위 명제

단기적으로 가장 높은 `λ`를 가진 조직과 장기적으로 가장 높은 누적 성과를 가진 조직은 동일하지 않을 수 있다.

장기 우위는 `N_eff`의 크기뿐 아니라 `S`, `R`, `K`, reversibility를 안정적으로 유지하는 능력에 의해 결정될 수 있다.

---

# v0.1 이후 우선 검증 순서

1. **P6** — potential throughput과 realized performance가 분리되는 조건
2. **P1/P2** — 실제 multi-agent workflow에서 scale-out efficiency와 coordination loss
3. **P4/P7** — risk-tiering과 control architecture가 `Λ_control`, `μ_control`을 얼마나 이동시키는지
4. **P3** — 실제 시장/학습 환경에서 `β>1`이 나타나는 조건
5. **P8** — 장기 운영 데이터 또는 장기 시뮬레이션

P5의 queue saturation 자체는 기존 이론을 사용하고 AVCT의 독창성 주장에서는 제외한다.
