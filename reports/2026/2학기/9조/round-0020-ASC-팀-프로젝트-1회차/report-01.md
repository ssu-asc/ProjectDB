---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "ASC 팀 프로젝트 1회차"
quad_name: "9조"
members: ["team09_01_김수민", "team09_02_김태은", "team09_03_장수연"]
report_number: 1
date: "2026-11-08"
status: "진행 중"
portal_submission_id: "e83e1df8-7bd8-4ac0-ad90-4bcdc8cd7ec1"
---

# [제 1차 프로젝트 진행 보고서] ASC 팀 프로젝트 1회차

- **팀원:** (팀장) 장수연 (team09_03), (팀원) 김수민 (team09_01), 김태은 (team09_02)

- **활동 기간:** 2026. 11. 02. ~ 2026. 11. 08.

## 팀 전체 진행 현황

- **이번 회차 목표:** MCP 프로토콜 및 기존 취약점 조사, 분석 대상 선정
- **현재 진행률:** 5% (전체 일정 대비)
- **주요 달성 사항:**  서버 구조·도구 분석, 공개 보안 권고 5건 정리

## 개인별 기여 내역

> 각 팀원이 이번 회차에 구체적으로 무엇을 했는지 작성합니다.
> 산출물 링크(GitHub 커밋 로그, PR 링크, 분석한 코드 주소 등)를 반드시 포함합니다.

| 팀원 | 역할 | 수행 작업 | 산출물 링크 | 기여도 |
|------|------|----------|------------|--------|
| 김수민 (team09_01) | 코드·취약점 분석 | 도구별 입력 검증과 GitPython 호출 방식을 분석하고, 브랜치 이름 검증 문제를 로컬에서 재현하여 대응 방안 정리 | https://drive.google.com/file/d/10Nz8oyb_ztue9Zyd2n9jsum394FcGhfQ/view?usp=drive_link | 33.3% |
| 김태은 (team09_02) | 기초 구조, 취약점 조사 | MCP·Git 기본 구조와 보안 개념을 조사하고, 공개 취약점 3건의 원인과 패치 내용 정리 | https://drive.google.com/file/d/1cEdB7okjk9_3sQkMfItEfjy5GbMc6hNH/view?usp=drive_link | 33.3% |
| 장수연 (team09_03) | 서버 구조 및 보안 분석 | 공식 소스·문서를 바탕으로 서버 구조와 14개 도구를 조사하고, 공개 보안 권고 5건의 영향·수정 버전·운영 권고 정리 | https://drive.google.com/file/d/1WIxPunMhGu1d5j7G65rApjzNAspyBv7i/view?usp=drive_link | 33.3% |

## 이슈 및 해결 방안

- **문제 상황:** 호출 방식과 Git 메타데이터 처리에 따라 입력 검증 및 저장소 경계 확인 방식의 차이
- **해결 현황:** 도구별 검증 로직과 공개 패치를 비교하고, 추가 검증이 필요한 동작과 대응 방안을 정리

## 다음 회차 목표

- 로컬 Git MCP 서버 구축 및 클라이언트 연결
- 테스트용 저장소에서 조회·커밋·브랜치 기능 확인
- 저장소 접근 제한과 잘못된 입력 처리 테스트
- 테스트 결과 및 오류 사항 정리

## 참고 자료

- Git MCP 서버 소스 코드 (https://github.com/modelcontextprotocol/servers/tree/main/src/git)

