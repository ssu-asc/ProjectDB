---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "개인 프로젝트 계획서"
quad_name: "개인"
members: ["team08_02_남지윤"]
report_number: 1
date: "2026-10-05"
status: "진행 중"
portal_submission_id: "4646c20e-289a-4f1b-8f9c-c5dd484d0128"
---

# 2026년 ASC 개인 프로젝트 계획서

- **작성자:** 남지윤 (team08_02)

| 항목 | 내용 |
|------|------|
| **학교명** | 숭실대학교 |
| **동아리명** | ASC |
| **개인 프로젝트 계획서(주제)** | 자체 개발 서비스 OMO의 AI Security 취약점 분석 및 방어 시스템 설계 |
| **프로젝트 분야** | AI Security / LLM Security / Agent Security |

## 프로젝트 개요

> 본 프로젝트는 제가 직접 기획하고 개발에 참여해온 교환학생 준비 서비스 **OMO**를 대상으로 AI Security 취약점을 분석하고 방어 체계를 설계하는 프로젝트이다.
>
> OMO는 교환학생 준비 과정에서 도시 탐색, 도시 비교, 예산 관리, 일정 관리 등을 지원하는 서비스이며, 자연어 기반 도시 탐색 및 사용자 조건에 따른 추천 기능을 포함한 AI 기능을 개발하고 있다.
>
> 본 프로젝트에서는 이러한 OMO의 AI 기능을 실제 서비스 환경으로 활용하여 Prompt Injection, RAG Poisoning, Agent/Tool Misuse 등 생성형 AI 서비스에서 발생할 수 있는 공격을 재현하고, 이를 탐지·차단할 수 있는 방어 구조를 설계한다. 또한 공격 성공률(Attack Success Rate), 정상 요청 성공률(Task Success Rate), 오탐률(False Positive Rate) 등을 측정하여 방어 적용 전후의 성능을 정량적으로 비교한다.

## 기대 효과

- 직접 개발 중인 실제 서비스를 대상으로 AI 보안 취약점을 분석함으로써 실서비스 기반 AI Security 경험을 확보한다.
- Prompt Injection, RAG Poisoning 등 생성형 AI 서비스에서 발생할 수 있는 공격을 직접 구현하며 공격 원리와 방어 방식을 학습한다.
- 단순 공격 재현에 그치지 않고 방어 시스템 설계와 정량 평가까지 수행하여 AI Red Teaming 및 Secure AI Engineering 역량을 강화한다.
- 프로젝트에서 도출한 보안 구조와 테스트 환경을 실제 OMO 서비스의 AI 기능 개발에 적용할 수 있다.

---

# 프로젝트 세부 계획서

## 1. 프로젝트 목적 (추진배경, 취지 등)

OMO는 제가 직접 기획하고 개발에 참여해온 **교환학생 준비 지원 서비스**이다. 교환학생을 준비하는 사용자가 자연어를 통해 도시를 탐색하고, 도시별 치안·어학·인프라 등의 정보를 비교하며, 위시리스트·D-Day 로드맵·예산 관리 기능을 이용할 수 있도록 설계하고 있다.

특히 OMO에서는 자연어 기반 도시 탐색과 사용자 조건에 따른 도시 추천 등 LLM을 활용한 AI 기능을 개발하고 있다. 이러한 기능은 서비스 편의성을 높일 수 있지만, 외부 데이터 검색, RAG, 사용자 정보 활용, Tool 호출과 결합될 경우 기존 웹 서비스와 다른 새로운 공격면이 발생한다.

대표적으로 Prompt Injection을 통해 LLM의 기존 지시를 무시하도록 유도하거나, 외부 데이터에 삽입된 악성 명령을 모델이 실행하는 Indirect Prompt Injection이 발생할 수 있다. 또한 RAG 시스템의 검색 데이터를 오염시켜 특정 정보나 추천 결과를 조작하는 RAG Poisoning과, LLM Agent가 허용되지 않은 Tool을 호출하도록 유도하는 Agent/Tool Misuse 공격도 발생할 수 있다.

본 프로젝트에서는 기존에 직접 개발해온 OMO를 단순한 예시가 아닌 **실제 공격·방어 실험 대상 서비스**로 활용한다. OMO의 AI 기능을 대상으로 공격 시나리오를 설계하고 실제 취약성을 측정한 뒤, 이를 방어할 수 있는 보안 계층을 구현하고 성능을 검증하는 것을 목표로 한다.

## 2. 프로젝트 세부내용

프로젝트는 **OMO AI 구조 분석 → Threat Modeling → 공격 구현 → 방어 시스템 구현 → 정량 평가** 순서로 진행한다.

먼저 기존 OMO 서비스의 기능 구조를 기반으로 AI 기능을 분석한다. 사용자는 자연어로 교환 희망 지역, 예산, 생활 조건 등을 입력하고, 시스템은 내부 데이터 및 RAG를 통해 도시·숙박·생활 정보를 검색한 뒤 LLM을 통해 추천 결과를 생성하는 구조를 구성한다.

이후 서비스의 데이터 흐름을 기준으로 보호해야 할 자산, 공격자, 신뢰 경계(Trust Boundary), 공격 표면을 정의하는 AI Threat Model을 작성한다.

주요 공격 범위는 다음 세 가지로 제한한다.

**① Prompt Injection**

사용자가 LLM의 기존 지시를 무시하도록 유도하거나 시스템 내부 정보, 제한된 정보 등을 출력하도록 하는 공격을 구성한다. 직접적인 공격뿐 아니라 우회 표현, 다국어 표현, 명령 은닉 등 다양한 유형을 실험한다.

**② Indirect Prompt Injection / RAG Poisoning**

OMO AI가 검색하는 도시, 숙박, 생활정보 등의 문서에 악성 instruction을 삽입하고, 해당 데이터가 RAG Context에 포함될 경우 AI의 응답이 조작되는지 실험한다.

특히 OMO의 핵심 기능인 도시 추천과 연결하여 특정 도시나 제휴 업체가 지속적으로 높은 우선순위로 추천되도록 만드는 **추천 조작 공격**도 구현한다.

**③ Agent / Tool Misuse**

OMO AI가 사용자의 예산, 위시리스트, 일정 정보를 조회하거나 저장하는 Tool을 호출하는 상황을 구성한다. 이후 Prompt Injection을 통해 허용되지 않은 Tool 호출, 다른 사용자 정보 접근, 의도하지 않은 데이터 변경을 유도할 수 있는지 검증한다.

공격 환경 구축 후 다음과 같은 방어 구조를 구현한다.

- Prompt Injection 탐지 및 입력 필터링
- 신뢰 가능한 instruction과 외부 데이터를 분리하는 Context Isolation
- RAG 문서의 신뢰도 검사 및 악성 instruction 탐지
- AI가 호출 가능한 기능을 제한하는 Tool Permission Layer
- 민감정보 및 비정상 출력을 검사하는 Output Guard

각 방어 방식을 개별 적용한 결과와 여러 방어 방식을 결합한 결과를 비교하여 효과적인 AI 보안 구조를 분석한다.

## 3. 프로젝트 기대효과

본 프로젝트를 통해 직접 개발 중인 실제 서비스에 AI Security를 적용함으로써 단순한 보안 실습보다 현실적인 서비스 환경에서의 공격 및 방어 경험을 확보할 수 있다.

또한 AI 서비스에서 발생할 수 있는 취약점을 단순히 발견하는 것에 그치지 않고, 공격 성공률과 정상 기능 유지 정도를 동시에 평가하여 보안성과 사용성 간의 균형을 분석할 수 있다.

최종적으로 OMO 서비스에 적용 가능한 AI 보안 가이드라인과 방어 아키텍처를 구축하고, 향후 다른 LLM 및 RAG 기반 서비스에도 재사용 가능한 AI Security 테스트 환경을 만드는 것을 목표로 한다.

## 4. 프로젝트 수행시 문제점 (내외부 요인 기술)

LLM은 동일한 입력에 대해서도 매번 다른 결과를 생성할 수 있기 때문에 단일 실험 결과만으로 공격 성공 여부를 판단하기 어렵다. 이를 해결하기 위해 각 공격을 반복 실행하고 평균 Attack Success Rate를 측정한다.

또한 외부 LLM API를 사용할 경우 모델 업데이트나 API 정책 변화에 따라 실험 결과가 달라질 수 있다. 따라서 사용 모델과 버전을 기록하고, 가능한 경우 Local LLM을 병행하여 실험 재현성을 확보한다.

OMO의 실제 서비스 기능과 AI 보안 실험 환경을 동시에 개발해야 하므로 프로젝트 범위가 지나치게 커질 수 있다. 이를 방지하기 위해 일반 웹 보안은 주요 범위에서 제외하고 Prompt Injection, RAG Poisoning, Tool Misuse 세 가지 AI Security 공격을 중심으로 진행한다.

## 5. 프로젝트 수행시 요구사항 (개발환경, 사전지식 등)

Python 기반 AI 애플리케이션 개발 환경과 LLM API 또는 Local LLM 실행 환경이 필요하다.

RAG 구현을 위해 Embedding Model 및 Vector Database 사용 방법을 학습하며, Prompt Injection, AI Red Teaming, Agent Security 등에 대한 이론 학습을 병행한다.

주요 사전지식은 Python, REST API, LLM Prompt 구조, Embedding 및 RAG 기본 원리이며, OWASP GenAI Security 및 MITRE ATLAS 자료를 활용하여 AI Threat Modeling과 공격 기법을 학습한다.

모든 보안 실험은 본인이 직접 개발하고 관리하는 OMO 서비스 및 별도의 테스트 환경에서만 수행한다.

## 6. 프로젝트 수행시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
|:---:|------|
| **H/W** | 개인 PC 또는 노트북, 필요시 GPU 기반 Local LLM 실행 환경 |
| **S/W** | Python, FastAPI, LangChain 또는 유사 LLM Framework, FAISS/Chroma 등 Vector DB, Git/GitHub, Docker, LLM API 또는 Local LLM |
| **기타(도서 등)** | OWASP GenAI Security 자료, OWASP Agentic AI Security 자료, MITRE ATLAS, Prompt Injection 및 RAG Security 관련 논문 |

## 개인 수행 계획

- **주요 수행 항목:** 기존 OMO AI 기능 구조 분석, AI Threat Model 작성, Prompt Injection·RAG Poisoning·Tool Misuse 공격 시나리오 구축, 공격 Benchmark 제작, 방어 모듈 구현, 방어 방식별 성능 실험 및 결과 분석
- **예상 산출물:** OMO AI Security 테스트 시스템, AI Threat Model, 공격 Benchmark Dataset, Prompt/RAG/Tool Security Defense Module, 공격·방어 성능 비교 결과, GitHub Repository, 최종 기술 보고서 및 시연 영상
- **검증 방법:** 동일한 공격 Benchmark를 방어 적용 전후에 반복 수행하여 Attack Success Rate(ASR), 정상 Task Success Rate(TSR), False Positive Rate(FPR), 민감정보 유출 성공률, 비인가 Tool 호출 성공률 등을 측정한다. 또한 개별 방어 요소를 제거하는 Ablation Test를 통해 각 방어 방식의 기여도를 분석한다.

## 참고 자료

- OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications*
- OWASP GenAI Security Project, *OWASP Top 10 for Agentic Applications*
- MITRE, *Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS)*
