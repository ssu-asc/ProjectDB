---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "팀 프로젝트 계획서"
quad_name: "6조"
members: ["team06_01_김인환", "team06_02_김홍균", "team06_03_석은호", "team06_04_안시후"]
report_number: 1
date: "2026-10-10"
status: "진행 중"
portal_submission_id: "d05e02f5-adee-4cfb-8b7a-ca3c39d5897a"
---

# 2026년 ASC 프로젝트 계획서

| 항목 | 내용 |
| --- | --- |
| **학교명** | 숭실대학교 |
| **동아리명** | ASC |
| **팀 프로젝트 계획서(주제)** | 공개 1-day 포너블 취약점 분석 |
| **프로젝트 분야** | 시스템 보안 / 바이너리 취약점 분석 |

## 프로젝트 개요

> 패치는 공개됐지만 공개 분석이 적은 critical 1-day 취약점을 골라 재현하고, 분석해 문서로 남긴다. 취약점 3개를 팀 전체가 low-level까지 깊게 분석한다. 이후 분석한 취약점은 원인·패턴·패치 방식별로 DB에 정리하고, 결과는 입문자도 따라올 수 있는 tech-blog 수준 문서와 실습 환경으로 남긴다.
>

## 기대 효과

취약점의 root-cause와 패치 원리를 low-level으로 깊게 이해한다. 취약점 유형별 공통 패턴 DB와 입문자용 실습 자료를 남긴다.

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

- 1-day CVE는 패치가 공개돼 있어, 패치 전후를 비교해 원인을 거꾸로 추적하며 배우기 좋다.
- 보고서를 따라하는 것만이 아니라 원인을 직접 찾으며 배운다.
- 재현부터 원리까지 정리한 한국어 포너블 학습 자료가 적다.

## 2. 프로젝트 세부내용

- 목표 개수: 인당 심층분석 1개
- 분석 대상 : 1-day CVE 3개 선정 후 low-level까지 분석
- 공통 패턴 : DB와 문서 정리, 최종 발표 준비
- 분석: 패치 diff와 소스를 비교해 root-cause를 추적한다. 재현은 분석이 맞는지 검증하는 수단으로 사용한다.
- 분석한 취약점을 원인·패턴·패치 방식별로 DB에 정리한다.
- 결과물:
    - 취약점별 tech-blog 수준 분석 문서(입문자용 배경 설명 포함)
    - 입문자용 Docker 실습 환경
    - 취약점 유형 DB
    - 발표 자료

## 3. 프로젝트 기대효과

- 포너블 분석 전 과정(선정·분석·검증·문서화)을 직접 경험한다.
- 어려운 취약점을 깊게 판 경험으로 이후 분석 속도를 높인다.
- 공통 패턴 DB로 새 취약점을 볼 때 유형을 빠르게 판단한다.
- 패치 전후 비교로 방어 관점까지 배운다.

## 4. 프로젝트 수행 시 문제점 (내외부 요인 기술)

- PoC가 특정 환경에서만 동작할 수도 있다.
- 공개 분석이 적은 취약점은 참고 자료 없이 원인을 직접 찾아야 해서 오래 걸린다.
- 2주 멘토링 주기와 시험 기간에 맞춰 분량을 조절해야 한다.

## 5. 프로젝트 수행 시 요구사항 (프로젝트 구성원, 개발환경 등)

- 구성원: 4명 (팀장 1, 팀원 3)
- 환경: Linux x86-64, Docker 컨테이너와 VM 격리 환경
- 도구: GDB(pwndbg/GEF), IDA, AddressSanitizer, pwntools, Docker, QEMU 등
    - 분석은 격리 환경에서만 수행한다.

## 6. 프로젝트 수행 시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
| --- | --- |
| **H/W** | 팀원 개인 노트북/PC |
| **S/W** | Linux, Docker, QEMU/VM, GDB, Ghidra/IDA, AddressSanitizer, pwntools |
| **기타(도서 등)** | [미정] |

## 팀원 역할 분담

| 팀원 | 역할 | 담당 업무 |
| --- | --- | --- |
| 김인환 (team06_01) | 팀장 | CVE-2023-39191 분석·재현·문서화, 일정·멘토링·공유 회의 관리, 문서 취합·유형 DB 정리, 발표 자료 정리 |
| 김홍균 (team06_02) | 팀원 | CVE-2021-33624 분석·재현·문서화 |
| 석은호 (team06_03) | 팀원 | CVE-2023-2163 분석·재현·문서화 |
| 안시후 (team06_04) | 팀원 | CVE-2021-31829 분석·재현·문서화, 발표 |

## 참고 자료

후보 CVE

- CVE-2023-39191 (eBPF dynptr validation/type confusion): https://nvd.nist.gov/vuln/detail/CVE-2023-39191
- CVE-2021-33624 (BPF + Spectre-style speculative execution): https://nvd.nist.gov/vuln/detail/CVE-2021-33624
- CVE-2023-2163 (eBPF verifier incorrect path pruning): https://nvd.nist.gov/vuln/detail/CVE-2023-2163
- CVE-2021-31829 (speculative load → BPF stack leak): https://nvd.nist.gov/vuln/detail/CVE-2021-31829
