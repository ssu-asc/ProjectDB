---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "ASC 팀 프로젝트 1회차"
quad_name: "3조"
members: ["team03_01_송인우", "team03_02_이효관"]
report_number: 1
date: "2026-11-08"
status: "진행 중"
portal_submission_id: "eea80536-9ce8-4fa0-b045-2a6ca14ff22e"
---

# [제 1차 프로젝트 진행 보고서] ASC 팀 프로젝트 1회차

- **팀원:** (팀장) 송인우 (team03_01), (팀원) 이효관 (team03_02), -, -
- **활동 기간:** 2026. 11. 02. ~ 2026. 11. 08.

## 팀 전체 진행 현황

- **이번 회차 목표:** 비교 대상 에이전트 3종(NYU baseline, EnIGMA, D-CIPHER)의 실행 환경 구축
- **현재 진행률:** 15% (전체 일정 대비)
- **주요 달성 사항:**
   - 프로젝트 레포지토리 구성
   - 실험 규칙 정함 (모델, 비용, 반복 횟수, 실패 유형 분류 등)
   - EnIGMA 설치 및 Docker 실행 환경 구축
   - NYU baseline, D-CIPHER 설치 및 Docker 실행 환경 구축
   - 3개 에이전트의 모델 지원 범위와 기본 설정 파악
   

## 개인별 기여 내역

> 각 팀원이 이번 회차에 구체적으로 무엇을 했는지 작성합니다.
> 산출물 링크(GitHub 커밋 로그, PR 링크, 분석한 코드 주소 등)를 반드시 포함합니다.

| 팀원 | 역할 | 수행 작업 | 산출물 링크 | 기여도 |
|------|------|----------|------------|--------|
| 송인우 (team03_01) | 팀장 | 레포지토리 구성, 실험 규칙·참고 자료 문서화, EnIGMA 환경 구축 및 소스 코드 분석 | https://github.com/InwooNull/CTF-agent-research/commits/main?author=InwooNull | 50% |
| 이효관 (team03_02) | 팀원 | NYU baseline·D-CIPHER 환경 구축 및 소스 코드 분석 | | 50% |
| - | - | - | - | - |
| - | - | - | - | - |

## 이슈 및 해결 방안

- **문제 상황:**
   - EnIGMA와 NYU baseline은 Claude 3.5 Sonnet까지만 지원하고, D-CIPHER만 최신 모델을 지원함. 같은 모델로 비교하려면 두 에이전트에 최신 모델 정보를 추가해야 함
   - 에이전트마다 기본 비용 상한과 턴 수가 달라(baseline $3, D-CIPHER $1 등) 그대로 실행하면 공정한 비교가 어려움
- **해결 현황:**
   - 소스 코드 분석으로 수정할 위치 파악 완료 (EnIGMA `sweagent/agent/models.py`, baseline `nyuctf_baseline/backends/model_info.json`). 다음 회차에 최신 모델 정보와 토큰 단가 추가 예정
   - 비용 상한과 반복 횟수를 실험 규칙에 예시값으로 정해 두었고, 팀 합의 후 확정 예정

## 다음 회차 목표

- 실험에 사용할 LLM 확정
- EnIGMA, NYU baseline에 최신 모델 정보 추가
- 세 에이전트 모두 같은 모델로 스모크 테스트 진행
- 평가 문제셋 20~30문제 확정
- 실행 결과(풀이 시간, 토큰, 성공 여부) 기록 방식 정리

## 참고 자료

- 프로젝트 레포지토리: https://github.com/InwooNull/CTF-agent-research
- EnIGMA 논문: https://arxiv.org/abs/2409.16165
- EnIGMA 코드 (SWE-agent v0.7): https://github.com/SWE-agent/SWE-agent/tree/v0.7
- D-CIPHER 논문: https://arxiv.org/abs/2502.10931
- NYU baseline·D-CIPHER 코드: https://github.com/NYU-LLM-CTF/nyuctf_agents
- NYU CTF Bench: https://nyu-llm-ctf.github.io
