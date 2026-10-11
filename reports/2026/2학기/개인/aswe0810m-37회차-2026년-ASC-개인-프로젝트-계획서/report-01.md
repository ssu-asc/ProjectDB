---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "개인 프로젝트 계획서"
quad_name: "개인"
members: ["team04_02_오동규"]
report_number: 1
date: "2026-10-04"
status: "진행 중"
portal_submission_id: "883772d5-5666-448c-bcfb-4cc932994c39"
---

# 2026년 ASC 개인 프로젝트 계획서

- **작성자:** 오동규 (team04_02)

| 항목 | 내용 |
|------|------|
| **학교명** | 숭실대 |
| **동아리명** | ASC |
| **개인 프로젝트 계획서(주제)** | 웹 취약점 분석과 버그 바운티 실전 적용 |
| **프로젝트 분야** | web |

## 프로젝트 개요

> 웹 취약점을 학습하고, 각 취약점을 직접 구현하고(심기) → 방어하고 → 그 방어를 우회하는 3단 사이클로 체득한 뒤, 실제 서비스의 취약점 공개 프로그램을 대상으로 탐색과 제보까지 수행한다.

## 기대 효과

- 웹 취약점에 대해 공격·방어 양방향 이해 확보
- 실제 서비스를 대상으로 한 합법적 취약점 탐색·제보 경험 획득
- 취약점 보고서 작성 및 영향도(CVSS) 산정 역량 확보
- 기존 시스템 해킹 역량과 웹 보안을 연결하여 분석 가능 영역 확대

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

- **배경:** 그간 시스템 해킹(바이너리 익스플로잇) 중심으로 학습해 왔으며, 웹 분야는 웹 자체에 대한 이해 부족으로 진입하지 못했다. 2026년 2학기 웹프로그래밍 수강으로 HTTP·클라이언트/서버 구조에 대한 기반이 확보되어, 웹 보안으로 영역을 확장하기에 적절한 시점이라 판단하였다.
- **문제의식:** 웹 취약점은 메모리 커럽션과 달리 "개발자가 클라이언트를 신뢰한 지점"에서 발생하는 논리적 결함이 대부분이다. 따라서 취약점을 푸는 경험만으로는 부족하고, 직접 작성하고 방어해 보는 경험이 원리 이해에 필수적이다.
- **취지:** 학습 성과를 문제 풀이 개수가 아니라 실제 서비스에 대한 적용 가능성으로 검증한다. 이를 위해 합법적 범위(VDP 및 버그 바운티 프로그램의 명시된 scope) 내에서 탐색과 책임 있는 제보를 수행한다.

## 2. 프로젝트 세부내용

1. 이론 학습 및 실습 랩 수행
2. **직접 심기** — Flask 기반 자작 웹 애플리케이션에 해당 취약점을 의도적으로 구현하고 익스플로잇
3. **방어 및 우회** — 방어 코드를 적용한 뒤 우회를 시도하여 방어 메커니즘의 한계 분석
4. **실전 탐색** — 해당 클래스에 한정하여 VDP 혹은 버그 바운티 scope 내 탐색 수행

**단계별 계획**

| 단계 | 기간 | 내용 |
|---|---|---|
| 1단계: 기초 | 6주 (10~12월, 학기 중) | Dreamhack *Web Hacking Fundamental* — XSS, CSRF, SSRF, Access Control, Command Injection, File Vulnerability, SQL Injection, NoSQL Injection, JWT (9개 Unit) |
| 2단계: 실무 프로세스 | 4주 (12~1월) | Dreamhack *Web Bug Bounty* Unit(프로그램 선정, scope, 법적·윤리 가이드, CVSS 3.1, 보고서 작성) 및 *PTES 기반 블랙박스 모의해킹* Path(정보 수집 → 위협 모델링 → 취약점 분석 → 익스플로잇 → 포스트 익스플로잇 → 보고서) |
| 3단계: 실전 적용 | 6주 (1~2월) | VDP 대상 탐색 및 제보. 탐색 중 방어 메커니즘에 막히는 지점이 발생할 경우 *Web Hacking Basics – Deep Dive*의 해당 Unit(WAF 우회, 파일 검증 우회 등)을 선택적으로 보강 |

**탐색 대상 선정 기준**

보상이 없는 VDP를 우선 대상으로 한다. 보상 프로그램은 참여자 수가 많아 중복 제보(duplicate) 비율이 높고 핵심 자산은 이미 다수 검증된 반면, VDP는 상대적으로 경쟁이 적어 초기 학습 단계에서 유효 사례를 확보할 가능성이 높다. 또한 제보 및 벤더 대응 절차를 보상 압박 없이 연습할 수 있다.

## 3. 프로젝트 기대효과

- 웹 취약점에 대한 공격·방어 양방향 이해 확보
- PTES 절차에 따른 체계적 모의해킹 수행 능력 확보
- 실제 서비스에 대한 취약점 제보 경험 및 보고서 작성 역량 확보
- 기존 시스템 해킹 역량과 결합하여 CTF 웹 분야 및 CVE 분석 역량으로 확장

## 4. 프로젝트 수행시 문제점 (내외부 요인 기술)

**내부 요인**

- **선행 지식 부족:** 프론트엔드 프레임워크 및 JavaScript 숙련도가 낮아 클라이언트 사이드 취약점 분석 시 속도 저하가 예상된다.

**외부 요인**

- **법적 리스크:** 프로그램에 명시된 scope를 벗어난 테스트는 그 자체로 위법이다. → 탐색 착수 전 2단계(법적·윤리 가이드)를 선행하고, 대상별 scope 문서를 확인·기록한 뒤에만 테스트를 수행한다. 실제 사용자 데이터 접근, 서비스 가용성에 영향을 주는 행위, 취약점 확인에 불필요한 추가 접근은 수행하지 않는다.

## 5. 프로젝트 수행시 요구사항 (개발환경, 사전지식 등)

**개발·실습 환경**

- Ubuntu / WSL2 기반 리눅스 환경
- Python 3 및 Flask (취약 애플리케이션 구현용)
- Docker (취약 버전 환경 격리 및 재현)
- HTTP 프록시 도구 (요청 가로채기 및 변조)

**사전 지식**

- HTTP 프로토콜, 쿠키·세션, SOP/CORS 등 브라우저 보안 모델 기초
- HTML, JavaScript 기본 문법
- SQL 기초 및 관계형 DBMS 동작 원리
- Python 문법 및 Flask 사용 경험
- 리눅스 기본 명령어

**보유 현황**

시스템 해킹(바이너리 익스플로잇), 리버싱, 암호학 기초를 학습한 상태이며, Python·C·리눅스 환경 및 Git 기반 문서화 워크플로를 보유하고 있다. 웹 분야는 HTTP 기초 및 Flask 기초 수준으로, 본 프로젝트를 통해 보완한다.

## 6. 프로젝트 수행시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
|:---:|------|
| **H/W** | 개인 노트북 (WSL2 구동 가능 사양) — 별도 장비 불요 |
| **S/W** | Burp Suite Community Edition (HTTP 프록시·요청 변조), Docker (실습 환경 격리), Python 3 / Flask (취약 앱 구현), VSCode, Git / GitHub (문서화 및 코드 관리) |
| **기타(도서 등)** | Dreamhack 유료 구독 (강의 Lab 및 Unit 수강), PortSwigger Web Security Academy (무료 보조 실습 자료) |

## 개인 수행 계획

- **주요 수행 항목:**
  1. 웹 취약점에 대한 학습 수행
  2. 버그 바운티 법적·윤리 가이드 및 CVSS 3.1 기반 심각도 산정 학습
  3. VDP 대상 선정, scope 검토, 탐색 수행 및 취약점 제보

- **예상 산출물:**
  - VDP 제보 리포트
  - 탐색 기록 — 시도한 가설과 결과를 포함한 실패 로그 포함
  - 최종 결과 보고서

- **검증 방법:**
  - **학습 검증:** 각 Unit의 워게임 문제 및 퀴즈 해결 여부
  - **실전 검증:** 제출한 제보 건수 및 트리아지 응답 결과(유효/중복/무효) 기록. 무효 판정 건은 사유를 분석하여 문서화
  - **공개 검증:** 분석 문서를 공개 저장소에 게시하여 제3자 검토 가능 상태로 유지

## 참고 자료

- Dreamhack, *Web Hacking Fundamental* — https://dreamhack.io/lecture/paths/web-hacking-fundamental
- Dreamhack, *Web Bug Bounty* — https://dreamhack.io/lecture/units/web-bug-bounty
- Dreamhack, *PTES를 활용한 블랙박스 모의해킹* — https://dreamhack.io/lecture/paths/black-box-penetration-testing-with-ptes
- Dreamhack, *Web Hacking Basics – Deep Dive* — https://dreamhack.io/lecture/paths/web-hacking-basics-deep-dive
- PortSwigger, *Web Security Academy* — https://portswigger.net/web-security
- OWASP Top 10 — https://owasp.org/www-project-top-ten/
- *Penetration Testing Execution Standard (PTES)* — http://www.pentest-standard.org/
- FIRST, *CVSS v3.1 Specification* — https://www.first.org/cvss/v3.1/specification-document
- HackerOne Hacktivity (공개된 취약점 리포트 사례) — https://hackerone.com/hacktivity
