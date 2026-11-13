---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team06_04_안시후"]
report_number: 1
date: "2026-11-10"
status: "진행 중"
portal_submission_id: "0b5cd31f-be6f-4359-a468-2c3c7b3e6f71"
---

# [제 1차 개인 프로젝트 진행 보고서] ASC 개인 프로젝트 1회차

- **작성자:** 안시후 (team06_04)
- **활동 기간:** 2026. 10. 26. ~ 2026. 11. 01.

## 프로젝트 진행 현황

- **이번 회차 목표:** LLM 에이전트 기반 버그바운티 자동화 하네스의 핵심 파이프라인 구축 및 취약점 탐색 접근법 검증
- **현재 진행률:** 약 10%
- **주요 달성 사항:**
  - 정찰/스코프/CVE 스캔 도구 모듈 구성 (subfinder·httpx·nuclei 연동, scope.json 기반 범위 검증)
  - 자동 퍼징 기반 취약점 탐색을 5개 오픈소스에 적용·검증 → "성숙한 라이브러리 대상 블라인드 퍼징은 투입 대비 수확이 낮다"를 데이터로 확인 (연구적 결론 + 재사용 가능한 방법론 확보)
  - 웹 버그헌팅 + 1-day patch-diff(변종 사냥) 으로 방향 재정립
  - Docker 격리 실행 환경 구축 (보안 도구 샌드박스, 비root·최소권한)
  - patch-diff 수집 자동화 도구 구현 (보안 어드바이저리 → 패치 diff 직링크·원문 자동 수집)

## 수행 내역

- **수행 작업:**
  1. 하네스 코어 구성: `recon_tool`·`cve_tool`·`scope_tool`·`scope_filter`(scope.json 기반 스코프 검증 계층)
  2. 자동 퍼징 파일럿: libFuzzer + ASan/UBSan 하네스로 오픈소스 5종(parson, tomlc17, mpc, tinycbor, mpack)을 커버리지 유도 다각도 퍼징. 리포트 가능한 고심각 버그 0(= 해당 라이브러리들의 견고성 입증), mpc에서 저심각 이슈 3~4종 식별(재현 파일 보존)
  3. 방향 전환 후: `Dockerfile`+`sandbox.sh`로 격리 샌드박스, `patchdiff_tool.py`(v1→v3: 어드바이저리 목록 → 패치 diff 직링크 → .diff 원문 로컬 저장)
  4. 변종 사냥 1회 완주(수동 실습): Nextcloud circles 보안 패치 분석 → 코드 clone → 형제 컨트롤러 grep → 의심 후보 발견 → 데이터 흐름 추적으로 검증·반증(거짓양성 회피)
- **산출물 링크:**
  - 하네스: `~/bounty-agent/` — `harness.py`, `recon_tool.py`, `cve_tool.py`, `scope_tool.py`, `scope_filter.py`, `Dockerfile`, `sandbox.sh`, `patchdiff_tool.py`
  - 퍼징 하네스·결과: `~/ff/` — `fuzz_*.c` 9종, 재현 파일 `mpc_*.repro`
  - 변종 사냥 대상 코드: `~/vh/circles`
  - (※ 현재 로컬 산출물 — 공개 GitHub 레포는 미등록. 필요 시 정리 후 push 예정)
- **검증/확인 내용:**
  - 퍼징: llvm-cov로 타겟별 커버리지 측정(tinycbor 디코더 85%+인코더 82%, mpack Expect API 58%라인/76%함수 등), 수억~수십억 회 실행에서 크래시 0 확인
  - 도구: `patchdiff_tool`을 `nextcloud/security-advisories`로 실측(최근 6건 + 각 패치 diff 직링크 자동 추출 성공), Docker 이미지 빌드·도구 3종 동작·비root 실행 검증
  - 변종 사냥: 의심 후보 `DeprecatedController::listing`이 데이터 계층 `CircleRequest::getCircles`의 `limitToInitiator`로 접근제어됨을 확인 → "취약 아님"으로 근거 기반 반증

## 이슈 및 해결 방안

- **문제 상황:**
  1. 자동 퍼징이 성숙한 라이브러리에선 신규 고심각 버그를 거의 산출하지 못함(투입 대비 수확 낮음)
  2. 환경 이슈: WSL 네이티브 Docker 데몬 미기동/권한, WSL DNS 유실, 셸 변수·heredoc이 WSL 통과 시 깨짐
  3. 장시간 단일 세션 → 컨텍스트 압축으로 맥락 유실
- **해결 현황:**
  1. (완료) 멘토 피드백 반영 → 블라인드 0-day 대신 **1-day patch-diff/변종 사냥 + 웹**으로 전환(성공 확률 높은 방향). 퍼징 성과는 "견고성 입증 + 재사용 방법론"으로 정리
  2. (완료) `wsl -u root service docker start` + docker 그룹 추가, `wsl --shutdown`으로 DNS 복구, 리터럴 경로·스크립트 파일 사용으로 변수 깨짐 회피
  3. (완료) 메모리 파일 + 세션 그룹화로 해결 — 핵심 상태를 지속 기록해 새 세션에 자동 로드, 버그바운티 세션들을 전용 그룹으로 정리

## 다음 회차 목표

- **변종 사냥 자동화 도구(patchdiff v4):** 패치에서 '추가된 체크' 추출 → repo clone → 형제 코드 grep → 변종 후보 자동 출력 (별도 세션에서 착수)
- **웹 취약점 기초 체계화:** PortSwigger Web Security Academy(접근제어·IDOR 등) 실습 병행
- **하네스 통합:** recon 파이프라인을 Docker 샌드박스 안에서 실행하도록 배선
- **재현 리포트 자동화 스킬:** 발견 → 사람이 읽을 PoC/재현 리포트 생성

## 참고 자료

- 멘토링 피드백 (연구 도구 관점, 1-day patch-diff, 타겟 선택, 격리·스킬·MCP 연결)
- PortSwigger Web Security Academy
- GitHub Security Advisories / `nextcloud/security-advisories`
- ProjectDiscovery (subfinder·httpx·nuclei), libFuzzer / AddressSanitizer
