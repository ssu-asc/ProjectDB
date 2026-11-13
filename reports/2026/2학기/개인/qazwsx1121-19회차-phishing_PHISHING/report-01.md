---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "ASC 개인 프로젝트 1회차"
quad_name: "개인"
members: ["team02_03_지민혁"]
report_number: 1
date: "2026-10-29"
status: "진행 중"
portal_submission_id: "ba08078e-2bb1-4f55-a5aa-52e538187cc8"
code_repository_url: "https://github.com/qazwsx1121/phishing_PHISHING"
---

# [제 1차 개인 프로젝트 진행 보고서] 피싱 URL 판별 (phishing_PHISHING)

- **작성자:** 20233117_지민혁
- **활동 기간:** 2026. 10. 16. ~ 2026. 10. 29.

## 프로젝트 진행 현황

- **이번 회차 목표:** 피싱 URL 관련 사전 조사, 전체 구현 계획 수립, 데이터 모델과 판별 기준 데이터 정의, 웹 API 뼈대 구현
- **현재 진행률:** 20% (전체 일정 대비)
- **주요 달성 사항:**
  - 전체 프로젝트를 5단계(Phase), 18개 작업(Task)으로 나눈 구현 계획서 작성
  - 판별에 사용할 URL 특징 25개와 안전/주의/위험 3단계 판정 구조 정의
  - 판별 기준 데이터 구축: 국내외 브랜드 30개, 단축 URL 서비스 21개, 피싱 악용 최상위 도메인 20개, 의심 키워드 24개, 규칙 18개의 점수와 경계값
  - URL을 받아 분석 결과를 돌려주는 웹 API 뼈대 완성(현재는 가짜 분석기로 동작)

## 수행 내역

- **수행 작업:**
  1. **사전 조사 및 설계**
     - URL 구조(scheme, userinfo, host, port, path, query)와 공개 접미사 목록(PSL) 기반 등록 도메인 개념을 정리했다. 예를 들어 `naver.com.login-check.xyz`의 실제 등록 도메인은 `login-check.xyz`이다.
     - 피싱 수법을 정리했다: 서브도메인에 브랜드명 넣기, `@` 뒤에 실제 주소 숨기기, 단축 URL로 주소 감추기, 한글·유니코드 도메인(punycode)으로 유명 사이트 흉내 내기.
     - 서버가 사용자 대신 링크에 접속할 때의 위험을 검토하고, 단축 URL 서비스의 응답(`Location` 헤더)만 읽고 **최종 피싱 주소에는 접속하지 않는** 구조로 설계했다. 서버 IP 노출과 내부망 공격(SSRF)을 막기 위함이다.
     - ML 학습 데이터의 함정을 미리 정리했다.
       - 오래된 피싱 도메인은 이미 삭제·재등록되어 지금 조회한 생성일이 당시와 다르다(시간 누수).
       - 정상 URL이 대부분 홈페이지 주소라 생기는 데이터 편향이 있다.
  2. **구현 계획서 작성** (`IMPLEMENTATION_PLAN.md`)
     - 작업을 "데이터 모델 → 사용자 인터페이스 → 비즈니스 로직(규칙 기반 → ML) → 리팩토링" 순서로 나누었다.
     - 각 작업마다 만들 파일, 함수 형식, 테스트 케이스, 완료 기준을 명시했다.
     - 리스크 10개, 외부 데이터 연동 전략(PSL·RDAP·WHOIS·피싱 피드 갱신 주기), 미결정 사항 7개와 각각의 기본값을 정리했다.
  3. **데이터 모델 정의** (Task 1)
     - 분석 단계별 데이터 형식을 정의했다: 정규화된 URL, 리다이렉트 결과, URL 구성 요소, 도메인 정보, 특징 벡터, 규칙 판정, ML 판정, 최종 분석 결과.
     - 규칙 판정과 ML 판정이 다르면 더 위험한 쪽을 최종 판정으로 쓰도록 했다(사용자 보호 우선).
  4. **판별 기준 데이터와 설정 로더** (Task 2)
     - 브랜드 30개를 등록했다(국내 20: 네이버, 카카오, 우체국, CJ대한통운, 국민건강보험, 정부24, 홈택스, 주요 은행 등 / 해외 10). 각 브랜드에는 공식 도메인을 함께 적어, 공식 도메인이 아닌 곳에 브랜드명이 나타나는 경우를 잡을 수 있게 했다.
     - 국내 스미싱에 자주 쓰이는 단축 URL 서비스(han.gl, me2.do, vo.la, url.kr, naver.me 등)를 포함했다.
     - 규칙 18개의 초기 점수와 3단계 경계값(30점 이상 주의, 60점 이상 위험)을 코드와 분리된 설정 파일로 두었다. 나중에 데이터로 보정할 때 코드를 고치지 않아도 된다.
  5. **웹 API 뼈대** (Task 3)
     - FastAPI로 `POST /api/analyze`(URL 분석)와 `GET /healthz`(상태 확인)를 구현했다.
     - 빈 URL, 2048자 초과, 형식 오류에 대해 한국어 오류 메시지를 반환하도록 했다.
     - 실제 분석 로직 전에 화면과 API를 먼저 완성하려고, 고정된 결과를 돌려주는 가짜 분석기를 연결했다.
  - 구현은 계획서를 기반으로 AI 코딩 도구(Claude Code)를 활용해 작업 단위로 진행했다. 작업마다 테스트와 별도의 코드 리뷰를 거쳐 검증했다.
- **산출물 링크:**
  - 구현 계획서: `IMPLEMENTATION_PLAN.md`
  - 커밋 (브랜치 `feat/phishguard`)
    - `1a123af` docs: add implementation plan
    - `76aeae3` feat: project scaffold and core domain types
    - `4ce239f` feat: resource files and config loader
    - `e8bb999` feat: FastAPI app factory with JSON API and stub analyzer
- **검증/확인 내용:**
  - 단위 테스트 23개 전부 통과: 데이터 모델 7, 설정·리소스 8, 웹 API 8
  - 주요 확인 항목
    - 특징 25개의 이름·순서 고정, 누락 시 오류 발생
    - 분석 결과가 JSON으로 변환될 때 결측값(NaN)이 `null`로 처리됨
    - 국내 브랜드와 단축 URL 서비스가 목록에 포함됨
    - 경계값이 거꾸로 설정되면 오류 발생
    - 잘못된 입력에 대한 한국어 400 오류, 예상치 못한 오류는 500으로 응답하고 자세한 내용은 서버 로그에만 기록

## 이슈 및 해결 방안

- **문제 상황:**
  1. URL·HTTP 구조, 피싱 수법 등 웹 보안 지식과 ML 학습 경험이 부족해 설계 단계에서 놓친 요소가 있을 수 있음. 
  2. 규칙 점수와 3단계 경계값을 정하는 기준이 주관적이다.
  3. 학습 데이터(UCI PhiUSIIL 데이터셋)는 직접 내려받아야 하고, `.kr` 도메인의 생성일이 RDAP/WHOIS로 조회되는지 아직 확인하지 못했다.
  4. 테스트 실행 시 외부 라이브러리(Starlette)의 사용 중단 예고 경고가 1건 출력된다. JSON 객체가 아닌 요청 본문(예: 배열)에는 영어로 된 기본 오류(422)가 반환된다.
- **해결 현황:**
  1. 리스크 10개와 미결정 사항 7개를 계획서에 미리 정리하고, 각각의 대응 방법과 기본값을 정해 두었다. 
  2. 점수와 경계값을 설정 파일로 분리했다. 8회차에 검증 데이터로 경계값을 보정할 계획이다: "위험" 판정의 정밀도 95% 이상, "안전"으로 놓치는 피싱 5% 이하. (계획 수립 완료)
  3. 데이터셋은 6회차 전에 내려받는다. `.kr` 조회는 4회차(도메인 생성일 조회 구현)에서 실제로 확인하고, 실패하면 국내 WHOIS 응답을 직접 해석하는 작업을 추가한다. (예정)
  4. 2회차 화면 작업에서 경고 필터와 한국어 오류 처리를 함께 정리한다. (예정)

## 다음 회차 목표

- Task 4: URL 입력 폼과 결과 화면 구현
  - 판정 배지(안전 초록 / 주의 주황 / 위험 빨강), 판정 이유, 도메인 정보, 고지문 표시
  - 입력한 URL은 실수로 클릭하지 않도록 `hxxps://evil[.]com`처럼 클릭할 수 없는 글자로만 표시
- Task 5: URL 정규화
  - 앞뒤 공백·보이지 않는 문자 제거, `hxxp`/`[.]` 표기 복원, scheme 누락 보정, 한글 도메인을 punycode로 변환
  - `javascript:` 같은 웹 주소가 아닌 입력 거부
- 이월 항목 정리: 테스트 경고 제거, JSON 객체가 아닌 요청에 대한 한국어 오류 처리

## 참고 자료

- Public Suffix List — https://publicsuffix.org/
- WHATWG URL Standard (호스트·IPv4 해석 규칙) — https://url.spec.whatwg.org/
- RFC 9110 HTTP Semantics (리다이렉트 상태 코드와 Location 헤더) — https://www.rfc-editor.org/rfc/rfc9110
- RFC 9083 RDAP JSON 응답 형식 / IANA RDAP Bootstrap — https://data.iana.org/rdap/dns.json
- PhiUSIIL Phishing URL Dataset (UCI) — https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- OpenPhish Community Feed — https://openphish.com/
