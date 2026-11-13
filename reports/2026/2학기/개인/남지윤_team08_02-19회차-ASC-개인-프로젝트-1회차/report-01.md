---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team08_02_남지윤"]
report_number: 1
date: "2026-11-01"
status: "진행 중"
portal_submission_id: "0c4d7e84-8a7c-48cb-9b6e-67a13a594f0c"
---

# [제 1차 개인 프로젝트 진행 보고서] ASC 개인 프로젝트 1회차

- **작성자:** 이찬희 (team08_03)
- **활동 기간:** 2026. 10. 26. ~ 2026. 11. 01.

## 프로젝트 진행 현황

- **이번 회차 목표:** 취약점 실험에 사용할 웹 애플리케이션의 개발 환경을 구성하고, 게시판의 기본 기능을 구현한다.
- **현재 진행률:** 약 10%
- **주요 달성 사항:** 게시글 작성·목록·상세 조회 기능과 SQLite 저장 기능을 구현했다. 프론트엔드와 서버를 분리하고, 이후 취약점 실험에서 수정할 부분을 찾기 쉽도록 코드를 정리했다.

## 수행 내역

> 이번 회차에 직접 수행한 작업을 구체적으로 적어 주세요.
> 산출물 링크(GitHub 커밋, PR, 분석 자료, 데모 등)가 있다면 함께 적어 주세요.

- **수행 작업:** Vite, Typescript 기반의 기초적인 FE 환경을 구성, SQLite와 nodeJS 기반의 서버 환경.
- **산출물 링크:** [Github Repository](https://github.com/nopublicsounds/websec)
- **검증/확인 내용:** 게시글 작성 후 상세 조회와 최신순 목록 반영을 확인, 포맷 검사 및 타입 검사 수행.

## 이슈 및 해결 방안

- **문제 상황:** -
- **해결 현황:** -

## 다음 회차 목표

- 댓글과 프로필 기능을 구현한다.
- 회원가입, 로그인, 로그아웃과 세션 처리를 구현한다.
- 게시글 작성자를 계정과 연결하고 글 수정·삭제 시 소유권을 검사한다.

## 참고 자료

- [NodeJS SQLite](https://nodejs.org/docs/latest-v24.x/api/sqlite.html)
