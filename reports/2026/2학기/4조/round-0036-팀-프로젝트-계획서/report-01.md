---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "팀 프로젝트 계획서"
quad_name: "4조"
members: ["team04_01_안민기", "team04_02_오동규", "team04_03_이지원"]
report_number: 1
date: "2026-10-04"
status: "진행 중"
portal_submission_id: "073aa85f-1974-4ae6-8282-5f6900ff5d6c"
---

# 2026년 ASC 프로젝트 계획서

| 항목 | 내용 |
|------|------|
| **학교명** | 숭실대 |
| **동아리명** | ASC |
| **팀 프로젝트 계획서(주제)** | CVE2Fuzz: 이미지 처리 라이브러리 CVE 패턴 기반 Targeted Fuzzing |
| **프로젝트 분야** | Pwn |

## 프로젝트 개요

> OSS-Fuzz에 등록된 이미지 처리 라이브러리(libtiff, libpng, libjpeg-turbo)의 기존 CVE를 분석해 취약점 패턴 데이터베이스를 구축하고, 이 패턴을 기반으로 targeted fuzzing을 수행해 신규 취약점을 탐색한다.

## 기대 효과

> CVE 분석 결과를 일회성 문서가 아닌 재사용 가능한 패턴 DB로 축적하고, 이를 fuzzing 설계에 연결하는 취약점 연구 방법론을 확립한다. 신규 취약점 발견 시 메인테이너 제보까지 진행한다.

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

- libtiff, libpng, libjpeg-turbo는 OSS-Fuzz로 장기간 fuzzing되고 있음에도 CVE가 꾸준히 보고되고 있음. 특정 빌드 옵션이나 코덱 부재 같은 조건에서만 발생하는 버그는 일반적인 fuzzing으로 도달하기 어렵기 때문임 (예: CVE-2022-34526은 `--disable-zlib` 빌드에서만 재현됨)
- 기존 CVE의 근본 원인과 트리거 조건을 패턴화하면, 일반 fuzzing이 놓치는 영역을 겨냥한 하네스·입력 설계가 가능해짐
- OSS-Fuzz 등록 라이브러리를 대상으로 삼아, 단순 fuzzing으로 찾을 수 있는 얕은 버그가 아닌 패턴 기반 접근이 필요한 버그를 목표로 함

## 2. 프로젝트 세부내용

- **CVE 분석 및 DB 확장**: 대상 라이브러리의 CVE를 분석해 취약 함수, 트리거 경로, 입력 조작 방식, 근본 원인을 정리하고 6개 기능 카테고리(Init, 메타데이터 파싱, 디코딩, 인코딩, 메모리/자원 관리, 에러 처리)로 분류
- **패턴 기반 fuzzing 설계**: DB에서 도출한 패턴을 하네스 진입점, seed corpus, dictionary, 빌드 옵션 조합에 반영
- **Fuzzing 수행 및 크래시 분석**: ASan 빌드로 fuzzing을 수행하고, 발생한 크래시의 재현·중복 제거·근본 원인 분석 진행
- **결과 정리**: 분석 문서와 fuzzing 결과를 팀 GitHub 저장소에 축적하고, 신규 취약점 발견 시 메인테이너에 제보

## 3. 프로젝트 기대효과

- CVE 분석 → 패턴 DB → targeted fuzzing으로 이어지는 취약점 연구 흐름을 직접 수행하며 실전 역량 확보
- 표준화된 분석 템플릿과 DB가 남아 이후 다른 라이브러리나 후속 프로젝트에 재사용 가능
- 신규 취약점 발견 시 오픈소스 보안 기여 및 CVE 등록 가능성
- 입문자 팀원이 기존 분석 사례를 통해 메모리 취약점 분석 방법론을 단계적으로 학습

## 4. 프로젝트 수행시 문제점 (내외부 요인 기술)

- 대상 라이브러리가 이미 OSS-Fuzz로 장기간 fuzzing되어 있어 신규 취약점 발견 확률이 낮음 → 일반 fuzzing과 차별화되는 패턴 기반 설계가 필수
- 개인 노트북 환경에서는 fuzzing을 장시간 연속으로 수행하기 어려워 탐색 범위가 제한될 수 있음
- 한 학기라는 기간 안에 분석과 fuzzing을 모두 수행해야 하므로 범위 조절이 필요함

## 5. 프로젝트 수행시 요구사항 (프로젝트 구성원, 개발환경 등)

- 구성원: 3명 (팀장 1명, 팀원 2명)
- 개발환경: WSL + Docker, VSCode, Clang + ASan
- 협업: GitHub 저장소 기반 브랜치 → PR → 리뷰 후 머지, YAML frontmatter 기반 CVE 테이블 자동 생성(GitHub Actions)

## 6. 프로젝트 수행시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
|:---:|------|
| **H/W** | 개인 노트북 |
| **S/W** | WSL, Docker, VSCode, Clang/ASan, Git/GitHub |
| **기타(도서 등)** | - |

## 팀원 역할 분담

| 팀원 | 역할 | 담당 업무 |
|------|------|----------|
| 안민기 (team04_01) | 팀원 | 미정 |
| 오동규 (team04_02) | 팀장 | 미정 |
| 이지원 (team04_03) | 팀원 | 미정 |

## 참고 자료

- NVD: https://nvd.nist.gov
- OSS-Fuzz: https://github.com/google/oss-fuzz
- libtiff: https://gitlab.com/libtiff/libtiff
- libpng: https://github.com/pnggroup/libpng
- libjpeg-turbo: https://github.com/libjpeg-turbo/libjpeg-turbo
