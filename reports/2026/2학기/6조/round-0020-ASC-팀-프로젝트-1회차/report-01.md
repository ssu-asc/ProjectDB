---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "ASC 팀 프로젝트 1회차"
quad_name: "6조"
members: ["team06_01_김인환", "team06_02_김홍균", "team06_03_석은호", "team06_04_안시후"]
report_number: 1
date: "2026-11-08"
status: "진행 중"
portal_submission_id: "37749f07-bfaf-4067-af9c-3109379ee4cf"
---

# [제 1차 프로젝트 진행 보고서] ASC 팀 프로젝트 1회차

- **팀원:** (팀장) 김인환 (team06_01), (팀원) 김홍균 (team06_02), 석은호 (team06_03), 안시후 (team06_04)
- **활동 기간:** 2026. 11. 02. ~ 2026. 11. 08.

## 팀 전체 진행 현황

- **이번 회차 목표:** 팀원별 담당 eBPF verifier CVE 1개씩 패치 커밋 분석 관련 자료 조사와 분석 계획 수립
- **현재 진행률:** 2% (전체 일정 대비)
- **주요 달성 사항:** 인당 담당 CVE 확정, 전체 회차 단계별 일정 계획 수립, 공통 분석 순서(패치 커밋 확보 → diff 분석 → 취약 범위 정리) 합의, CVE별 참고 자료 수집

## 개인별 기여 내역

| 팀원 | 역할 | 수행 작업 | 산출물 링크 | 기여도 |
|------|------|----------|------------|--------|
| 김인환 (team06_01) | 팀장(PM), CVE-2023-39191 담당 | 전체 회차 일정 계획 수립, CVE-2023-39191 패치 커밋 추적 방법 조사(Red Hat Bugzilla, ZDI advisory, 커널 git log), dynptr 관련 verifier 코드 분석 계획 수립 | [NVD CVE-2023-39191](https://nvd.nist.gov/vuln/detail/CVE-2023-39191) | 25% |
| 김홍균 (team06_02) | CVE-2021-33624 담당 | CVE-2021-33624 관련 자료 조사(USENIX Security '21 논문 등), 분기 오예측 관련 verifier 코드 분석 계획 수립, 재현 가능한 CPU 환경 확인 준비 | [NVD CVE-2021-33624](https://nvd.nist.gov/vuln/detail/CVE-2021-33624) | 25% |
| 석은호 (team06_03) | CVE-2023-2163 담당 | CVE-2023-2163 관련 자료 조사, state pruning 로직 분석 계획 수립 | [NVD CVE-2023-2163](https://nvd.nist.gov/vuln/detail/CVE-2023-2163) | 25% |
| 안시후 (team06_04) | CVE-2021-31829 담당, 발표 | CVE-2021-31829 관련 자료 조사, 스택 투기 로드 관련 패치 분석 계획 수립, 발표 준비 방향 구상 | [NVD CVE-2021-31829](https://nvd.nist.gov/vuln/detail/CVE-2021-31829) | 25% |

## 이슈 및 해결 방안

- **문제 상황:**  eBPF verifier 내부 로직에 대한 내용이 포함되어 있어 분석 전에 verifier 구조에 대한 배경 지식이 필요함. CVE-2023-39191은 CVE 기록에 upstream 패치 커밋이 명시돼 있지 않음.
- **해결 현황:** verifier 구조 관련 자료를 각자 학습하여 공유 회의에서 공유할 계획. CVE-2023-39191 패치 커밋은 Red Hat Bugzilla, ZDI advisory, 커널 메일링 리스트를 통해 추적할 예정.

## 다음 회차 목표

- 팀원별 패치 커밋 diff 분석 및 취약 범위 정리
- 패치 직전 커밋 기준 취약 커널 빌드 및 QEMU 재현 환경 구성
- BPF 프로그램 로드 경로 확인
- 공유 회의에서 CVE별 패치 구조와 환경 구성 중 막힌 점 공유

## 참고 자료

- https://nvd.nist.gov/vuln/detail/CVE-2023-39191
- https://nvd.nist.gov/vuln/detail/CVE-2021-33624
- https://nvd.nist.gov/vuln/detail/CVE-2023-2163
- https://nvd.nist.gov/vuln/detail/CVE-2021-31829
