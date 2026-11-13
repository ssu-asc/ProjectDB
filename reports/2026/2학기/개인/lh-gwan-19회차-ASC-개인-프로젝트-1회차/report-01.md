---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team03_02_이효관"]
report_number: 1
date: "2026-11-01"
status: "진행 중"
portal_submission_id: "0798f3fa-a784-4af8-a602-2118a7f9783b"
---

# [제 1차 개인 프로젝트 진행 보고서] ASC 개인 프로젝트 1회차

- **작성자:** 이효관 (team03_02)
- **활동 기간:** 2026. 10. 26. ~ 2026. 11. 01.

## 프로젝트 진행 현황

- **이번 회차 목표:**
  - DeepShield 연구 결과를 선행 연구와 비교해, 실제로 새로운 기여가 어디에 남아 있는지 확인한다.
  - 가장 강한 주장(보호 노이즈의 적용 순서 효과)을 흔드는 교란 요인을 통제하는 실험을 설계하고 실행 환경을 갖춘다.
- **현재 진행률:** 약 70% (시스템 구현과 1차 측정은 완료. 핵심 주장을 검증하는 보강 실험은 구현을 마치고 실행 대기)
- **주요 달성 사항:**
  - 여섯 가지 연구 결과별 선행 연구 조사 보고서 완성. 남은 신규성은 두 가지로 정리했다.
    - (c) 보호 섭동의 순서 의존성: shield를 먼저, Mist를 나중에 넣으면 두 방어가 모두 남고, 반대 순서면 LoRA 방어가 사라진다.
    - (d) 소형 얼굴 진짜 영상의 딥페이크 탐지 오탐: 해상도가 아니라 H.264 압축에서 온다.
  - (c)의 1순위 위험인 **섭동 예산 불일치**를 통제하는 대조 실험을 설계·구현했다.
    - 순차 shield→Mist는 원본 대비 최대 16/255이고, 합동 최적화는 8/255라서 예산이 다르다.
    - 이를 맞추기 위해 대조군 두 개(joint16, shield4_mist4)를 만들었다.
  - 실험 파이프라인을 Kaggle 전용에서 Google Colab에서도 돌아가도록 옮기고, 끊겨도 이어 도는 구조로 바꿨다. 업로드 번들까지 만들어 실행 직전 상태다.

## 수행 내역

> 이번 회차에 직접 수행한 작업을 구체적으로 적어 주세요.
> 산출물 링크(GitHub 커밋, PR, 분석 자료, 데모 등)가 있다면 함께 적어 주세요.

- **수행 작업:**
  1. **선행 연구 조사.** 다섯 주제로 나눠 조사했다.
     - 조사 주제: 얼굴 스왑·ID 생성기 방어, 반개인화(anti-personalization), 보호 섭동 조합·순서, 딥페이크 탐지기와 압축, 얼굴 인식 인구 편향
     - 비교 대상 논문: FaceSwapGuard, NullSwap, FaceShield, IDProtector, Adapter Shield, DLADiff, Anti-DreamBooth, Mist, GenD 등
     - 결과마다 "이미 있는 것 / 아직 비어 있는 것"을 판정했다.
     - 출처는 검증 수준(1차 확인, 초록만, 검색 요약, 미확인)을 표기해 인용 전 재확인 대상을 분리했다.
  2. **추가 실험 우선순위.** 조사 결과를 바탕으로 추가 실험을 P0(필수)·P1(학회 기준선)·P2(선택)로 나눴다.
  3. **예산 일치 대조군 구현.**
     - `joint16`: shield 손실과 Mist 손실을 한 번의 PGD로 16/255 안에서 최적화한다. 순차 shield→Mist(최대 16/255)와 같은 예산이다.
     - `shield4_mist4`: shield 4/255 다음 Mist 4/255. 합동 8/255(joint8)와 같은 예산이다.
     - `shield4_512`: 4/255 shield 단독. 예산을 절반으로 줄여도 스왑을 막는지 확인한다.
     - 평가 스크립트에 각 대조군의 워터마크 기준 사진을 연결했다.
  4. **Colab 실행 환경 구축.**
     - Mist 생성·LoRA 학습 스크립트의 Kaggle 고정 경로를 환경변수(`DS_INPUT`, `DS_WORK`, `DS_TEMP`, `DS_GPUS`)로 바꿨다.
     - 이미지 생성 스크립트에 장치 선택(`--device`)과 변형 선택(`--variants`)을 추가했다.
     - 업로드 번들을 만드는 스크립트를 작성했다. 코드는 git 추적 파일만, 입력은 필요한 사진만 담는다.
     - Colab 노트북과 한 번에 도는 실행 스크립트를 만들었다. 순서는 모델 해시 확인 → shield 4/255 → Mist → LoRA → 생성 → 채점이다.
     - 모든 중간 산출물(Mist 라운드 체크포인트, LoRA 100스텝 체크포인트, 생성 이미지, 결과)을 Google Drive에 둔다. 런타임이 끊겨도 처음부터 다시 실행하면 이어서 돈다.
  5. **파일럿 실행 준비.** 이전 실험에서 LoRA 방어가 가장 많이 되돌아온 4명(hugo_chavez, jeb_bush, jennifer_lopez, nicole_kidman)을 대상으로 정했다. 업로드 번들(code.zip 43MB, inputs.zip 128MB)과 노트북을 만들어 두었다. T4 기준 4~5시간이 걸릴 것으로 예상한다.
- **산출물 링크:**
  - GitHub 저장소: https://github.com/LH-GWAN/deepfake-found (`research/three-limits` 브랜치)
  - 선행 연구 조사 보고서: `reports/DeepShield 선행 연구 조사.md`, 주제별 조사 메모 5편(`research_notes/`)
  - 대조군 실험 코드: `experiments/lora_defense/colab_run_budget.sh`, `colab_bundle_budget.sh`, `colab_budget.ipynb`, 수정한 `kaggle_mist.py`·`kaggle_train_lora.py`·`generate_local.py`·`prepare_joint_inputs.py`·`evaluate_joint_pilot.py`
- **검증/확인 내용:**
  - 로컬에서 문법·코드 검사를 하고, shield 예산 설정이 8/255에서 4/255로 실제로 바뀌는지 확인했다. Colab 실제 실행은 아직 하지 않아 다음 회차에 검증한다.
  - Colab에서 쓰는 ArcFace 모델(`w600k_r50.onnx`)은 SHA-256으로 로컬 실험과 같은 파일인지 확인한 뒤에만 진행하게 했다.
  - 같은 런타임에서 기존 조건(shield_mist16, joint8)도 다시 채점한다. 이전 Kaggle 결과가 재현되는지 먼저 확인하기 위해서다.
  - 대조군 결과는 이전 실험과 같은 지표로 보고한다.
    - 스왑: 원래 사람이 47명 중 1위로 식별되는 비율 (저장 그대로·JPEG 85·JPEG 70·절반 축소)
    - LoRA: 생성 이미지에서 그 사람이 1위인 비율, 고신뢰(0.47) 장수
    - 화질: PSNR·SSIM
  - 판정 기준은 다음과 같다.
    - joint16이 shield→Mist만큼 LoRA를 막으면, 순서 효과가 아니라 예산 효과다.
    - shield4_mist4가 joint8보다 나으면, 같은 예산에서도 순차가 합동을 이긴다.

## 이슈 및 해결 방안

- **문제 상황:**
  1. 기존 결과의 핵심 비교(순차 shield→Mist 24% vs 합동 40%)는 섭동 예산이 16/255 대 8/255로 달라, 순서가 아니라 예산 차이로 설명될 수 있다.
  2. 로컬 맥으로는 Mist·LoRA 학습을 돌릴 수 없다. Kaggle은 세션 시간이 제한되고, 무료 Colab은 런타임이 수시로 회수된다.
  3. 선행 연구 조사 결과, 개별 방어(ArcFace 겨냥 shield, Mist 재측정)는 2025~2026년 논문들과 겹치고 규모(20~30명)에서 밀린다.
- **해결 현황:**
  1. 예산을 맞춘 대조군 두 개를 설계·구현했고, 파일럿 4명 실행을 위한 번들까지 준비했다. 실행과 결과 분석은 다음 회차에 한다.
  2. 실험 코드를 환경변수 기반으로 바꿔 Kaggle과 Colab 양쪽에서 돌게 했다. 모든 단계는 Drive 체크포인트로 이어 돌기가 되도록 만들었다.
  3. 주장의 중심을 개별 방어 성능에서 "방어들이 서로 간섭한다(순서 의존성)"로 옮겼다. 규모 확대(100명 이상)와 표준 지표 병기는 다음 단계 실험으로 잡았다.

## 다음 회차 목표

- 예산 일치 대조군(joint16, shield4_mist4, shield4_512) 파일럿 4명을 Colab T4에서 실행하고 결과 분석. 결과에 따라 20명으로 확대
- FaceID·FaceID Plus v2·InstantID 결과를 "같은 인코더 계열"과 "독립 인코더"로 나눠 다시 보고
- 정화 공격 측정 시작: 노이지 업스케일링, GFPGAN 또는 CodeFormer 얼굴 복원 뒤 스왑·LoRA 방어 유지 여부
- 딥페이크 탐지기 오탐 분해의 교란 통제 설계: 화질을 맞춘 JPEG 대 H.264 비교, 54픽셀 얼굴에 강한 JPEG(q10~30) 적용
- 순서 효과의 원인 분석 설계: 두 섭동의 방향 유사도, 같은 크기 랜덤 노이즈 대조군

## 참고 자료

- DeepShield 저장소: https://github.com/LH-GWAN/deepfake-found
- Mist v2: https://github.com/psyker-team/mist-v2
- Anti-DreamBooth, PhotoGuard (반개인화 방어)
- FaceSwapGuard, NullSwap (ICCV 2025), FaceShield (ICCV 2025), IDProtector (CVPR 2025), Adapter Shield, DLADiff (arXiv 2511.19910): 얼굴 스왑·ID 생성기 방어
- Petrov et al., NeurIPS 2025: 워터마크 공존
- GenD (WACV 2026): 일반화 딥페이크 탐지기
- arXiv 2403.17608: 생성 이미지 탐지에서 압축·크기가 단서로 작동하는 문제
- NIST IR 8280: 얼굴 인식 인구 집단별 차이
- FaceForensics++, KoDF (AI Hub), LFW
