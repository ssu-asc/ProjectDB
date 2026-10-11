---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "개인 프로젝트 계획서"
quad_name: "개인"
members: ["team10_02_이채은"]
report_number: 1
date: "2026-10-04"
status: "진행 중"
portal_submission_id: "a17802c5-410a-49fd-a9fd-26ce95d40ef9"
---

# 2026년 ASC 개인 프로젝트 계획서

- **작성자:** 이채은 (team10_02)

| 항목 | 내용 |
|------|------|
| **학교명** | 숭실대학교 |
| **동아리명** | ASC |
| **개인 프로젝트 제안서(주제)** | **부채널 누설의 측정·공격·방어 전 과정 재현 연구** |
| **프로젝트 분야** | 정보보안 (부채널 분석 / 암호 구현 보안 / 하드웨어·마이크로아키텍처 보안) |

## 프로젝트 개요

> 암호 알고리즘이 수학적으로 안전하더라도, 실제 구현이 실행 시간, 캐시 접근 패턴, 소비 전력 등 물리적·구조적 부산물로 비밀 정보를 흘린다는 점에 주목한 프로젝트이다. 부채널 공격(Side Channel Attack)의 세 가지 대표 채널인 **타이밍, 캐시, 전력**에 대해 (1) 누설이 발생하는 원리를 이론적으로 정리하고, (2) 직접 구축한 격리된 실험 환경에서 공격을 재현하여 키 복구 가능성을 정량적으로 검증하며, (3) 상수 시간 구현, 마스킹 등 대응책을 적용한 뒤 누설이 실제로 제거되는지 통계적으로 입증한다. 최종적으로 누설 여부를 자동 검출하는 오픈소스 도구와 재현 가능한 실험 레포지토리를 공개한다.

## 기대 효과

> 공격 재현과 방어 검증을 모두 수행하는 완결형 연구 경험 확보, 통계 기반 누설 검출 도구 및 재현 가능한 실험 자료 공개, Spectre, Meltdown 등 현대 보안 이슈를 근본 원리부터 이해하는 역량 확보

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

- AES, RSA 같은 암호 알고리즘은 수학적으로 검증되어 있지만, 실제 사고는 구현 단계의 누설에서 자주 발생한다. 1996년 Kocher의 타이밍 공격, 1999년 차분 전력 분석(DPA), 2018년 Spectre, Meltdown까지 부채널은 "알고리즘이 아니라 구현이 깨진다"는 사실을 반복해서 보여준다.
- 부채널은 소프트웨어, 마이크로아키텍처, 하드웨어에 걸친 주제여서 CPU 구조, 암호, 통계, 임베디드를 함께 이해해야 한다. 이는 한 분야만으로는 얻을 수 없는 근본적인 시스템 이해로 이어진다.
- 공격 논문은 많지만 "공격 재현 → 방어 적용 → 방어 효과의 통계적 검증"을 하나의 일관된 방법론으로 직접 수행한 학생 수준의 자료는 드물다. 이를 하나의 프레임워크로 정리해 공개하는 것이 목적이다.
- 모든 실험은 본인 소유의 장비와 격리된 환경에서만 수행하여, 공격 지식을 방어 설계 역량으로 연결하는 윤리적 연구 태도를 실천한다.

## 2. 프로젝트 세부내용

- **단계 1. 이론 정립 및 실험 환경 구축**
  - 부채널의 개념, 누설 모델(Hamming Weight/Distance), 신호 대 잡음비, 상관관계 분석 등 핵심 이론 정리
  - 격리된 VM 및 임베디드 타깃 환경 구성, 측정 자동화 스크립트(Python) 작성
- **단계 2. 타이밍 채널 (Timing)**
  - 비상수 시간 비교 함수와 Square-and-Multiply 방식 모듈러 지수 연산을 대상으로, 실행 시간 차이를 통한 비밀 값 추론 과정을 재현
  - 시간 측정 노이즈 처리와 필요한 샘플 수 분석
  - 대응: 상수 시간(constant-time) 구현으로 교체 후 효과 검증
- **단계 3. 캐시 채널 (Cache)**
  - 캐시 구조와 접근 시간 차이 원리 정리, 본인 VM 내 프로세스 간 Flush+Reload 및 Prime+Probe 방식 측정 실험
  - 테이블 룩업 기반 AES(T-table) 구현에서 캐시 접근 패턴이 키 정보와 연관됨을 확인
  - 대응: 테이블 미사용(bitslice) 또는 AES-NI 기반 구현과 누설량 비교
- **단계 4. 전력 채널 (Power)**
  - ChipWhisperer 등 교육용 장비로 임베디드 타깃의 소비 전력 파형 수집
  - 단순 전력 분석(SPA)과 상관 전력 분석(CPA)으로 AES 라운드 키 바이트 복구 재현
  - 대응: 1차 마스킹과 셔플링 적용 후 필요한 파형 수 증가량 및 공격 난이도 변화 측정
- **단계 5. 통합 누설 검출 도구 개발 (핵심 산출물)**
  - TVLA(Welch의 t-검정 기반 누설 평가)와 dudect 방식의 통계적 타이밍 검사를 참고하여, 공격 없이도 구현의 누설 여부를 판정하는 경량 도구 제작
  - 단계 2~4에서 만든 취약/방어 구현체에 이 도구를 적용해 "누설 있음 → 대응 후 누설 없음"을 수치와 그래프로 제시
- **단계 6. 결과 정리 및 공개**
  - 재현 가능한 GitHub 레포지토리(코드, 데이터, 노트북, 실행 가이드), 연구 보고서, 발표 및 시연 자료 작성
  - 실험 설정 및 한계(실험실 환경과 실제 환경의 차이)를 명시

## 3. 프로젝트 기대효과

- 암호의 수학적 안전성과 구현 안전성의 차이를 체감하고, 공격과 방어를 모두 설계할 수 있는 근본 역량 확보
- 타이밍·캐시·전력 세 채널을 하나의 방법론(측정 → 분석 → 대응 → 통계 검증)으로 비교한 자료 확보
- 누설 검출 도구와 실험 레포지토리 공개를 통한 가시적 성과물 및 포트폴리오 구축
- CPU 마이크로아키텍처, 임베디드 측정 등 융합 지식 습득

## 4. 프로젝트 수행시 문제점 (내외부 요인 기술)

- **진입 난이도:** 암호 이론, 통계, 하드웨어 지식이 동시에 필요하므로 초기 학습량이 많음. 단계별로 범위를 나누어 점진적으로 학습
- **측정 노이즈:** 실제 측정에서는 OS 스케줄링, 클럭 변동, 전력 노이즈로 이상적인 결과가 나오지 않음. 반복 측정과 통계 처리로 보완
- **장비 비용 및 수급:** 전력 분석용 장비 구입 비용 부담. 장비 확보가 어려운 경우 공개 파형 데이터셋과 시뮬레이션 기반 분석으로 대체 가능하도록 계획
- **환경 의존성:** CPU 모델, 커널, 컴파일러 설정에 따라 결과가 달라질 수 있어 실험 환경과 조건을 정밀하게 기록해야 함
- **범위 과다 위험:** 세 채널을 모두 다루면 일정이 부족할 수 있음. 타이밍 → 캐시 → 전력 순으로 진행하고 전력 채널은 시간에 따라 범위 조정
- **윤리 및 안전:** 본인 소유 장비와 격리된 환경에서만 실험하며, 타인의 시스템이나 서비스를 대상으로 한 시도는 하지 않음. 취약점 정보 공개 시 교육 목적의 범용 원리 수준으로 한정

## 5. 프로젝트 수행시 요구사항 (프로젝트 구성원, 개발환경 등)

- **사전 지식:** C 및 Python 프로그래밍, 리눅스 기초, 컴퓨터 구조 기초(캐시, 파이프라인), 기초 확률·통계, AES/RSA의 기본 동작 원리
- **개발·실습 환경:** Linux 기반 가상머신(격리 네트워크), GCC/Clang, Python 데이터 분석 환경(NumPy, SciPy, Matplotlib, Jupyter), 임베디드 타깃 보드 및 파형 측정 장비
- **협업·기록 환경:** Git/GitHub를 통한 코드 및 실험 기록 관리, 실험 로그 템플릿 작성
- **준수 사항:** 실험 대상은 본인이 소유한 장비로 한정, 인용 논문 및 데이터셋의 출처와 라이선스 표기

## 6. 프로젝트 수행시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
|:---:|------|
| **H/W** | 개인 PC(캐시·타이밍 실험용, 가상화 지원 CPU 및 RAM 16GB 이상 권장), 전력 분석용 교육 장비(ChipWhisperer 계열 및 호환 타깃 보드), USB 케이블 및 기본 측정 액세서리 |
| **S/W** | Linux(Ubuntu/Kali), VMware/VirtualBox, GCC/Clang, Python(NumPy, SciPy, Matplotlib, Jupyter), ChipWhisperer 소프트웨어, Git/GitHub, VS Code, Ghidra 등 필요 시 분석 도구 |
| **기타(도서 등)** | 『Power Analysis Attacks: Revealing the Secrets of Smart Cards』(Mangard 외), 『Understanding Cryptography』(Paar & Pelzl), 『Computer Architecture: A Quantitative Approach』(캐시 파트), 관련 논문 자료 |

## 개인 수행 계획

| 단계 | 주요 활동 | 산출물 |
|------|-----------|--------|
| 1 | 이론 학습, 환경 구축, 측정 자동화 | 이론 정리 노트, 실험 환경 가이드 |
| 2 | 타이밍 채널 공격 재현 및 상수 시간 대응 | 타이밍 실험 코드, 결과 그래프 |
| 3 | 캐시 채널 측정, T-table AES 분석 및 대응 비교 | 캐시 실험 코드, 누설 비교 분석 |
| 4 | 전력 파형 수집, CPA 재현, 마스킹 적용 검증 | 파형 데이터, CPA 결과, 마스킹 효과 분석 |
| 5 | 통합 누설 검출 도구 개발 및 전 구현체 적용 | 누설 검출 도구, 검증 리포트 |
| 6 | 레포지토리 정리, 보고서 및 발표 자료 작성 | 최종 보고서, GitHub 공개, 발표 자료 |

※ 일정은 장비 수급 및 진행 상황에 따라 조정될 수 있으며, 전력 채널 단계는 장비 확보 여부에 따라 공개 데이터셋 기반 분석으로 대체할 계획임.

## 참고 자료

- Kocher, P. "Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems" (CRYPTO 1996)
- Kocher, P., Jaffe, J., Jun, B. "Differential Power Analysis" (CRYPTO 1999)
- Bernstein, D. J. "Cache-timing attacks on AES" (2005)
- Osvik, D., Shamir, A., Tromer, E. "Cache Attacks and Countermeasures: the Case of AES" (2006)
- Yarom, Y., Falkner, K. "FLUSH+RELOAD: A High Resolution, Low Noise, L3 Cache Side-Channel Attack" (USENIX Security 2014)
- Reparaz, O., Balasch, J., Verbauwhede, I. "Dude, is my code constant time?" (DATE 2017)
- Goodwill, G. 외 "A testing methodology for side-channel resistance validation" (NIST Non-Invasive Attack Testing Workshop 2011)
- Kocher, P. 외 "Spectre Attacks: Exploiting Speculative Execution" (IEEE S&P 2019), Lipp, M. 외 "Meltdown: Reading Kernel Memory from User Space" (USENIX Security 2018)
- ChipWhisperer 공식 문서 및 튜토리얼: https://chipwhisperer.readthedocs.io
- NIST FIPS 197 (AES), NIST CSRC 자료: https://csrc.nist.gov
