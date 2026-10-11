---
source: "asc_web"
project_type: "team"
semester: "2026-2"
project_name: "팀 프로젝트 계획서"
quad_name: "9조"
members: ["team09_01_김수민", "team09_02_김태은", "team09_03_장수연"]
report_number: 1
date: "2026-10-04"
status: "진행 중"
portal_submission_id: "8cd8d1d8-575d-4700-8125-947280bda882"
---

# 2026년 ASC 프로젝트 계획서

| 항목 | 내용 |
| --- | --- |
| **학교명** | 숭실대 |
| **동아리명** | ASC |
| **팀 프로젝트 계획서(주제)** | RAG 기반 간접 프롬프트 인젝션을 활용한 LLM Agent·MCP 공격 체인 연구 |
| **프로젝트 분야** | AI Security / Red Team |

## 프로젝트 개요

RAG(Retrieval-Augmented Generation)를 사용하는 LLM Agent 환경에서 외부 문서에 삽입된 악성 지시가 Agent의 동작에 미치는 영향을 분석하고, 이를 시작점으로 MCP(Model Context Protocol) Tool의 비정상적인 호출과 권한 경계 우회로 이어지는 공격 체인을 구현한다.

격리된 테스트 환경에서 공격자가 RAG 데이터만 조작할 수 있다는 상황을 가정하여, 간접 프롬프트 인젝션을 통해 Agent의 Tool 선택과 실행 흐름을 변경하는 과정을 실험한다. 이후 제한된 권한을 가진 Agent가 MCP Tool을 연쇄적으로 활용하여 기존 권한 범위를 넘어서는 자원에 접근할 수 있는지 확인한다.

최종적으로 RAG Poisoning → Indirect Prompt Injection → Tool Abuse → Privilege Escalation → Target Resource Access로 이어지는 LLM Agent 대상 Red Team 공격 시나리오를 구축하고, 각 공격 단계와 성공 조건을 분석한다.

## 기대 효과

LLM Agent와 MCP를 결합한 환경에서 발생할 수 있는 새로운 공격 경로를 직접 구현함으로써, 기존 웹·시스템 중심의 Red Team을 넘어 AI Agent 환경에서의 공격 기법을 이해할 수 있다. 또한 단순한 프롬프트 인젝션 성공 여부 확인을 넘어, RAG 데이터 조작이 실제 Tool 호출과 권한 상승으로 연결되는 공격 체인을 분석함으로써 AI Agent 환경의 권한 관리와 신뢰 경계의 중요성을 확인할 수 있다.

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

- 최근 LLM이 단순한 질의응답을 넘어 RAG 및 외부 Tool과 연결되어 실제 작업을 수행하는 Agent 형태로 확장되고 있다.
- LLM Agent가 MCP를 통해 파일 시스템, 데이터베이스 및 외부 기능에 접근할 경우, 프롬프트 인젝션이 단순한 응답 조작을 넘어 실제 기능의 비정상적 실행으로 연결될 수 있다.
- 특히 공격자가 Agent에 직접 명령을 전달하지 않더라도, Agent가 참조하는 외부 문서에 악성 지시를 삽입하는 간접 프롬프트 인젝션이 공격의 초기 진입점으로 활용될 수 있다.
- 이에 공격자 관점에서 RAG 데이터 조작부터 MCP Tool 악용 및 권한 경계 우회까지 이어지는 공격 체인을 직접 구성하여 LLM Agent 환경의 공격 시나리오를 분석하고자 한다.
- 실제 서비스가 아닌 자체 구축한 격리 테스트 환경에서 실험하여 안전하게 AI Agent Red Team 기법을 연구하는 것을 목적으로 한다.

## 2. 프로젝트 세부내용

- **LLM Agent 테스트 환경 구축**
  - RAG 기능을 포함하는 테스트용 LLM Agent 구축
  - 테스트용 문서 및 Vector DB 구성
  - 자체 MCP Server 및 여러 종류의 MCP Tool 구현
  - Tool 및 Resource별 서로 다른 접근 권한 설정
- **RAG 기반 간접 프롬프트 인젝션 구현**
  - 정상 문서와 공격용 문서를 포함한 RAG 데이터셋 구성
  - 문서 내부에 Agent의 행동을 변경하도록 유도하는 간접 프롬프트 삽입
  - 검색된 문서가 Agent의 판단 및 Tool 선택 과정에 미치는 영향 분석
- **MCP Tool Abuse 공격**
  - 간접 프롬프트 인젝션을 이용하여 사용자가 요청하지 않은 Tool 호출 유도
  - Tool 호출 순서 및 입력값을 조작하는 공격 시나리오 구현
  - 여러 Tool을 연속적으로 사용하는 Tool Chaining 공격 실험
- **Agent 권한 상승 시나리오 구현**
  - 제한된 Tool만 사용할 수 있는 저권한 Agent 환경 구성
  - Tool 간 신뢰 관계 및 권한 차이를 이용하여 높은 권한의 기능·Resource 접근 시도
  - 공격 성공 시 Agent가 최초 부여받은 권한과 최종 접근한 Resource의 권한 비교
- **Red Team 공격 체인 구성**
  - 전체 공격 흐름을 단계별로 구현: RAG Poisoning → Indirect Prompt Injection → Agent Control → MCP Tool Abuse → Privilege Escalation → Target Resource Access
  - 공격 단계별 성공 여부와 Agent·MCP Server 로그를 수집하여 어떤 조건에서 다음 단계로 연결되는지 분석
  - 공격 난이도 및 조건을 변화시키며 공격 체인의 재현성과 성공 조건 비교

## 3. 프로젝트 기대효과

- RAG와 MCP가 결합된 LLM Agent 환경의 실제 공격 흐름을 직접 구현함으로써 AI Agent Red Team 분야의 실습 경험을 확보할 수 있다.
- 간접 프롬프트 인젝션이 단순 출력 조작을 넘어 Tool 호출 및 권한 상승으로 연결될 수 있는 조건을 분석할 수 있다.
- 기존 시스템의 Privilege Escalation 및 Attack Chain 개념을 AI Agent 환경에 적용하여 새로운 형태의 공격 시나리오를 연구할 수 있다.
- 공격 단계별 로그 및 성공 조건을 정리하여 향후 LLM Agent 보안 연구 및 방어 기법 연구를 위한 기초 자료로 활용할 수 있다.
- 결과물을 공격 시나리오·테스트베드 형태로 구성하여 향후 AI Security 및 Red Team 관련 연구로 확장할 수 있다.

## 4. 프로젝트 수행시 문제점 (내외부 요인 기술)

- 사용하는 LLM의 종류와 버전에 따라 동일한 간접 프롬프트 인젝션에도 서로 다른 결과가 발생할 수 있다.
- Agent Framework 및 MCP 구현 방식에 따라 Tool 호출·권한 관리 구조가 달라 실험 환경을 일반화하기 어려울 수 있다.
- 실제 서비스 Agent 환경과 자체 구축 테스트 환경 간 차이가 존재하여 실험 결과를 실제 서비스 전체로 일반화하는 데 한계가 있다.
- LLM의 비결정적 특성으로 동일한 공격 입력에서도 성공 여부가 달라질 수 있어 반복 실험이 필요하다.
- 공격 연구 과정에서 실제 외부 서비스·데이터에 영향을 주지 않도록 실험 범위를 자체 격리 환경으로 제한해야 한다.

## 5. 프로젝트 수행시 요구사항 (프로젝트 구성원, 개발환경 등)

- 프로젝트 구성원: 총 3명
- Python 기반 LLM Agent 및 RAG 개발 환경
- MCP Server 및 MCP Client 개발 환경
- Vector Database 및 테스트용 RAG 데이터셋
- LLM API 또는 로컬에서 실행 가능한 오픈소스 LLM
- Agent 및 MCP Tool 호출 과정을 기록하기 위한 로깅 환경
- 공격 실험을 안전하게 수행하기 위한 로컬·격리 테스트 환경
- Git 기반 소스코드 및 실험 결과 관리 환경

## 6. 프로젝트 수행시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
| --- | --- |
| **H/W** | 팀원 개인 PC 및 노트북, 필요 시 GPU 사용이 가능한 개발 환경 |
| **S/W** | Python, LLM Agent Framework, MCP SDK, Vector DB, Git/GitHub, Docker, 로컬 LLM 또는 LLM API |
| **기타(도서 등)** | OWASP LLM/GenAI Security 관련 자료, MCP 공식 문서, Prompt Injection 및 AI Agent Security 관련 논문·기술자료 |

## 팀원 역할 분담

| 팀원 | 역할 | 담당 업무 |
| --- | --- | --- |
| 김수민 (team09_01) | 팀원 | RAG 환경 구축, RAG Poisoning 및 간접 프롬프트 인젝션 공격 시나리오 구현 |
| 김태은 (team09_02) | 팀원 | MCP Server 및 Tool 개발, Tool Abuse 및 권한 상승 시나리오 구현 |
| 장수연 (team09_03) | 팀장 | 전체 Agent 환경 및 공격 체인 설계, 공격 시나리오 통합, 실험 및 결과 분석 |

## 참고 자료

- OWASP GenAI Security Project
- OWASP Top 10 for LLM Applications
- Model Context Protocol(MCP) 공식 문서
- MITRE ATLAS
- Indirect Prompt Injection 및 LLM Agent Security 관련 연구 논문
- RAG 및 Agent Tool Use 관련 기술 문서
