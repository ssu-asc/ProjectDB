---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team06_03_석은호"]
report_number: 1
date: "2026-11-01"
status: "진행 중"
portal_submission_id: "d935a74d-c4d0-4c15-afac-a9654c0feb41"
---

# [제 1차 개인 프로젝트 진행 보고서] ASC 개인 프로젝트 1회차

- **작성자:** 석은호 (team06_03)
- **활동 기간:** 2026. 10. 26. ~ 2026. 11. 01.

## 프로젝트 진행 현황

- **이번 회차 목표:** 연구 문제와 연구 질문을 정하고, 비교할 자동 취약점 수정(AVR) 도구와 평가 대상 확보에 쓸 탐지 도구를 선정한다. 탐지 도구 RepoAudit의 실행 환경을 구축해 정답이 알려진 프로젝트로 1차 실험을 진행한다.
- **현재 진행률:** 25% (전체 일정 대비)
- **주요 달성 사항:**
  - 연구 질문 3개 설정: AVR 도구는 실제 취약점을 얼마나 잘 고치는가, 왜 실패하는가, 어떻게 보완할 것인가
  - 비교 대상 AVR 도구 3종 선정: VulRepair, PailGen, VulKey
  - 평가 대상 확보용 탐지 도구 선정: RepoAudit, LLMxCPG, Vul-RAG 등
  - RepoAudit Docker 실행 환경 구축 및 팀 공유
  - 수정 커밋이 알려진 18개 프로젝트로 RepoAudit 1차 실험 완료

## 수행 내역

- **수행 작업:**
  - 기존 AVR 연구의 한계 정리: 정답 패치와의 유사도 위주 평가, 벤치마크 중심 성능 보고, 실패 원인 분석 부족
  - 도구 선정 기준 수립: 최근 3년 내 주요 학회·저널 게재, 공개 코드로 재현 가능, 생성 방식이 서로 다를 것
  - AVR 도구 3종을 생성 방식으로 구분: 학습 사례 기반(VulRepair), 수정 패턴 기반(PailGen), LLM 기반(VulKey)
  - RepoAudit 실행 환경을 Docker 이미지로 만들어 팀원이 같은 환경에서 실행할 수 있게 함
  - 수정 커밋이 알려진 18개 오픈소스 프로젝트를 대상으로 RepoAudit을 실행하고, 탐지 결과를 정답 커밋과 대조
- **산출물 링크:**
  - RepoAudit Docker 실행 환경, 1차 실험 결과표 (팀 내부 공유 자료)
  - RepoAudit 원본 저장소: https://github.com/PurCL/RepoAudit
- **검증/확인 내용:**
  - 탐지 172건 중 실제 정답은 11건(정밀도 6.4%)
  - 프로젝트별 재현율은 mosquitto·lz4 100%, rsyslog 40%, libtiff 20%, libpng 11.8%, 나머지 13개 프로젝트 0%
  - 탐지 결과를 그대로 AVR 입력으로 쓰면 고칠 결함이 없는 코드를 고치게 된다는 점을 확인함. 재현으로 실제 결함임을 확인한 것만 평가 대상으로 삼기로 함

## 이슈 및 해결 방안

- **문제 상황:**
  - 1차 실행에서 도달성 옵션(`--is-reachable`)을 잘못 사용해 일부 메모리 누수 스캔 결과가 오염됨
  - 9개 프로젝트에서 탐지가 0건이었음. 확인해 보니 추출기가 malloc·free 같은 표준 함수 이름만 인식해서, 자체 할당 래퍼(hb_malloc 등)를 쓰는 대형 라이브러리에서는 분석 자체가 되지 않았음
- **해결 현황:**
  - 오염된 스캔 결과는 무효로 처리하고 옵션을 바로잡아 다시 실행함(완료)
  - 래퍼 할당자 문제는 도구를 고치면 이전 결과와 비교할 수 없게 되므로 도구는 그대로 둠. 대신 표준 할당 함수를 쓰는 프로젝트를 우선 대상으로 고르기로 함. 다른 탐지 도구(VulMixer 등)로 보완하는 방안을 다음 회차에 확인함

## 다음 회차 목표

- 탐지 결과의 재현 검증: 후보를 코드 분석과 재현으로 확인해 실제 결함만 평가 대상으로 확정
- 원리가 다른 탐지 도구 여러 개의 결과를 교차 비교해 후보를 좁히는 방식 시험
- AVR 도구 예비 실험: 탐지 결과를 VulRepair·PailGen에 넣어 출력 형식 통과율과 실제 결함 수정률 비교
- 재현으로 확인한 결함이 나오면 첫 오픈소스 PR 제출

## 참고 자료

- J. Guo et al., "RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing," Proc. ICML, 2025.
- M. Fu et al., "VulRepair: A T5-Based Automated Software Vulnerability Repair," Proc. ESEC/FSE, 2022.
- M. Shao et al., "Fix Pattern-Aware Vulnerability Patch Generation via In-Context Learning," ACM TOSEM, 2026.
- J. Li et al., "VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns," Proc. ACM Softw. Eng., FSE, 2026.
- Y. Hu et al., "SoK: Automated Vulnerability Repair: Methods, Tools, and Assessments," Proc. USENIX Security, 2025.
