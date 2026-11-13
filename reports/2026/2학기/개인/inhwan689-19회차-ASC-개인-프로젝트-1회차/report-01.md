---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team06_01_김인환"]
report_number: 1
date: "2026-11-01"
status: "진행 중"
portal_submission_id: "e9a66788-7191-4f97-a810-4e9efc427f37"
---

# [제 1차 개인 프로젝트 진행 보고서] ASC 개인 프로젝트 1회차

- **작성자:** 김인환 (team06_01)
- **활동 기간:** 2026. 10. 26. ~ 2026. 11. 01.

## 프로젝트 진행 현황

- **이번 회차 목표:** 응답 수집과 패키지 실존 판정 자동화
- **현재 진행률:** 12% (전체 일정 대비)
- **주요 달성 사항:** 모델 3개 응답 6,000개 수집, 추천 패키지 16,234건 실존 판정 자동화

## 수행 내역

> **수행 작업:** 계획상 1~4단계(선행연구,코퍼스,수집,판정) 완료
  - 프롬프트 200개: 같은 태스크를 영어·한국어·한영 혼용으로 작성 + 국내 스택 태스크
  - Colab T4에서 Qwen2.5-Coder-7B, DeepSeek-Coder-6.7B, EXAONE-3.5-7.8B로 프롬프트당 10회 수집
  - 응답에서 패키지 이름 추출 -> PyPI·npm 조회 -> 정상/환각/표준 라이브러리 분류
  - 결과: 답변 6,000개 중 470개가 없는 패키지 설치를 추천. 등록 가능한 이름 322개(npm 170, PyPI 152)
  - 국내 스택 질문은 설치 추천의 10.3%가 가짜로 일반 질문(2.2%)의 약 5배
  - 74개 이름은 서로 다른 답변에서 2번 이상 반복 -> 공격자가 미리 등록해 둘 수 있는 이름
> **산출물 링크:** https://github.com/inhwan689/asc-c1-slopsquatting
> **검증/확인 내용:**
  - 환각 판정 표본 30개를 응답 원문과 대조: 모두 실제 설치 추천, 오추출 없음
  - 판정 결과 40개 재조회: 불일치 없음
  - 표준 라이브러리 이름은 PyPI가 등록을 막아 위험 집계에서 제외

## 이슈 및 해결 방안

- **문제 상황:** 이름 추출 오류로 환각률이 부풀려짐
- **해결 현황:** 해결 완료. 추출 오류 7건 수정 후 영어 미등록률 9.3% → 2.7%

## 다음 회차 목표

- 원논문과 같은 방식으로 환각률 재계산해 19.7%와 비교
- 언어·모델·태스크별 차이 통계 검정
- 국내 스택 태스크에 정답 패키지가 있는지 표시해 원인 분리

## 참고 자료

- We Have a Package for You!, USENIX Security 2025: https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code
- Slopsquatting(Wikipedia): https://en.wikipedia.org/wiki/Slopsquatting
