---
source: "asc_web"
project_type: "individual"
semester: "2026-2"
project_name: "개인 프로젝트 계획서"
quad_name: "개인"
members: ["team06_02_김홍균"]
report_number: 1
date: "2026-10-11"
status: "진행 중"
portal_submission_id: "84390f39-fc15-4976-8e4b-f7e18803b4df"
---

# 2026년 ASC 개인 프로젝트 계획서

- **작성자:** 김홍균 (team06_02)

| 항목 | 내용 |
| --- | --- |
| **학교명** | 숭실대학교 |
| **동아리명** | ASC |
| **개인 프로젝트 계획서(주제)** | IDA Professional 보호 메커니즘 리버스 엔지니어링 및 Crack 분석 |
| **프로젝트 분야** | Reverse Engineering / Binary Analysis / Software Protection Analysis |

---

# 프로젝트 개요

본 프로젝트에서는 Windows 환경에서 동작하는 **IDA Professional**을 대상으로 정적 분석과 동적 분석을 수행하여 프로그램의 전체적인 내부 구조와 소프트웨어 보호 메커니즘을 분석한다.

일반적인 리버스 엔지니어링 학습이 프로그램의 기능과 내부 로직을 이해하는 데 중점을 둔다면, 본 프로젝트에서는 한 단계 더 나아가 실제 상용 소프트웨어에 적용된 **라이선스 검증, 무결성 확인, 실행 제어 및 기타 보호 로직**이 프로그램 내부에서 어떠한 구조로 구현되어 있는지를 분석한다.

먼저 PE 구조, Import / Export, 문자열, Windows API, 주요 함수, Module 및 함수 호출 관계 등을 분석하여 IDA Professional 전체 Architecture를 파악한다.

이후 라이선스 및 보호 기능과 관련된 것으로 추정되는 Subsystem과 함수들을 식별하고, 정적 분석과 WinDbg를 이용한 동적 분석을 통해 프로그램 실행 과정에서 보호 로직이 어떠한 순서로 동작하는지 추적한다.

최종적으로 라이선스 검증과 보호 메커니즘의 구조 및 동작 원리를 분석하고, 해당 보호 구조가 어떠한 방식으로 Crack의 대상이 될 수 있는지 기술적으로 평가하는 것을 목표로 한다.

---

# 1. 프로젝트 목적

리버스 엔지니어링은 소스 코드가 제공되지 않은 프로그램의 내부 구조와 동작 방식을 분석하는 기술로, 악성코드 분석, 취약점 분석, 소프트웨어 보안, 디지털 포렌식 및 Binary Analysis 등 다양한 정보보호 분야에서 활용된다.

특히 상용 소프트웨어에는 프로그램의 무단 사용이나 변조를 방지하기 위해 라이선스 검증, 무결성 확인, Anti-Debugging, Obfuscation 등 다양한 Software Protection 기술이 적용될 수 있다.

이러한 보호 메커니즘을 분석하기 위해서는 단순히 Assembly Instruction을 해석하는 것을 넘어 다음과 같은 능력이 요구된다.

- 대규모 Binary에서 분석 대상 기능을 식별하는 능력
- 함수 및 Module 간 관계를 추적하는 능력
- 라이선스 및 보호 기능과 일반 프로그램 기능을 구분하는 능력
- 정적 분석과 동적 분석을 함께 활용하는 능력
- 조건 분기와 데이터 흐름을 역추적하는 능력
- 프로그램 보호 기술의 동작 원리를 추론하는 능력

본 프로젝트에서는 실제 대규모 Windows 애플리케이션인 IDA Professional을 대상으로 이러한 과정을 직접 수행한다.

프로젝트의 최종적인 분석 흐름은 다음과 같다.

**IDA Professional 전체 구조 분석**

→ **주요 Module 및 Subsystem 식별**

→ **보호 및 라이선스 관련 코드 후보 탐색**

→ **검증 로직 및 실행 흐름 분석**

→ **동적 분석을 통한 실제 동작 확인**

→ **Protection Mechanism 구조화**

→ **Crack 가능 지점 및 우회 가능성 분석**

이를 통해 단순한 기능 분석을 넘어 상용 소프트웨어의 보호 구조를 이해하고 분석하는 실전 Reverse Engineering 능력을 향상시키는 것을 목적으로 한다.

---

# 2. 분석 대상

본 프로젝트의 분석 대상은 **IDA Professional Windows x64 버전**으로 한다.

IDA Professional은 대규모 Native Windows 애플리케이션으로, 실행 파일과 다양한 Module 및 Library로 구성되어 있으며 자체적으로 복잡한 프로그램 구조를 가진다.

주요 분석 요소는 다음과 같다.

- Windows PE 실행 파일
- Native x64 Code
- 프로그램 초기화 과정
- C/C++ Runtime
- Windows API
- Dynamic Library
- GUI 및 Event Handling
- Binary Loading 및 Analysis 기능
- Loader
- Processor Module
- Plugin
- 설정 및 Configuration 처리
- 라이선스 관련 처리
- 무결성 및 보호 관련 로직
- 다수의 내부 함수와 자료구조

프로젝트 시작 시 특정 IDA Professional 버전을 하나 선정하고 해당 바이너리를 프로젝트 전체 기간 동안 고정하여 분석한다.

다음 정보를 기록한다.

- 제품명
- 버전
- 실행 파일명
- Architecture
- 파일 크기
- SHA-256 Hash
- 주요 실행 파일 및 DLL
- 분석 환경
- 실행 환경

이를 통해 프로그램 업데이트에 따른 Binary 변경의 영향을 최소화하고 분석 결과의 재현성을 확보한다.

---

# 3. 프로젝트 세부내용

## 3-1. 분석 환경 구축

IDA Professional을 분석하기 위한 별도의 Windows x64 환경을 구성한다.

필요한 경우 Windows VM을 사용하여 분석 대상과 분석 환경을 분리하고, Snapshot을 활용하여 동일한 상태에서 반복적인 동적 분석을 수행한다.

주요 환경은 다음과 같다.

- Windows 11 x64
- IDA
- WinDbg
- Windows VM
- Python 또는 C 개발 환경

분석 시작 시 대상 바이너리의 Hash를 기록하고 프로젝트 전체에서 동일한 파일을 사용한다.

---

## 3-2. PE 구조 및 기본 Binary 분석

분석 대상 실행 파일의 기본 구조를 조사한다.

주요 분석 항목은 다음과 같다.

- PE Header
- Architecture
- Entry Point
- Image Base
- Section 구조
- Import Table
- Export Table
- Resource
- TLS
- 주요 DLL
- Runtime
- Compiler 추정
- Packing 여부
- Obfuscation 여부
- Binary Protection 특성

주요 Section의 크기와 권한을 조사하고 프로그램 코드와 데이터가 Binary 내부에 어떠한 방식으로 배치되어 있는지 확인한다.

---

# 4. IDA Professional 전체 Architecture 분석

보호 로직을 분석하기 전에 먼저 프로그램 전체 구조를 파악한다.

## 4-1. 프로그램 초기화 과정

PE Entry Point부터 실제 Application Logic이 실행되는 지점까지의 흐름을 분석한다.

예상되는 구조는 다음과 같다.

**PE Entry Point**

→ **Runtime Initialization**

→ **Library Initialization**

→ **Application Initialization**

→ **Configuration / Environment Initialization**

→ **Main Application Logic**

초기화 과정에서 어떠한 Module이 로딩되는지 확인하고 주요 Global State가 언제 생성되는지를 조사한다.

---

## 4-2. 주요 Module 및 Subsystem 분석

IDA Professional 내부의 주요 기능을 기능별로 분류한다.

예상되는 주요 Subsystem은 다음과 같다.

- Initialization
- GUI / Event Handling
- File Input
- Loader
- Processor Module
- Binary Analysis
- Database
- Plugin
- Configuration
- License / Protection
- Output / Display

실제 분석 과정에서 함수와 Module의 관계를 확인하여 프로그램 Architecture Diagram을 작성한다.

---

# 5. 라이선스 및 보호 관련 기능 탐색

프로그램 전체 구조를 파악한 후 라이선스 및 보호 기능과 관련된 코드 영역을 식별한다.

분석에는 다음 정보를 종합적으로 활용한다.

- String
- XREF
- Import
- Export
- Windows API
- Error Message
- Configuration File
- File Access
- Registry Access
- Module Loading
- Function Call Graph
- Conditional Branch
- Runtime Behavior

특정 문자열이나 API 하나만으로 함수 역할을 판단하지 않고 여러 분석 근거를 교차 검증한다.

---

## 5-1. 관련 문자열 분석

프로그램 내부 문자열 중 다음과 같이 보호 기능과 관련될 가능성이 있는 정보를 조사한다.

- License
- Registration
- Activation
- Version
- Expiration
- Error
- Validation
- User Information
- Configuration
- Signature
- Integrity

관련 문자열의 XREF를 추적하여 실제로 해당 데이터를 처리하는 함수와 Code Path를 탐색한다.

---

## 5-2. 외부 데이터 접근 분석

프로그램이 실행 과정에서 참조하는 외부 데이터를 조사한다.

예를 들어 다음 요소를 확인한다.

- Configuration File
- License 관련 File
- Registry
- Environment Variable
- User Data
- Local Database
- Dynamic Library

각 데이터가 프로그램 내부로 전달된 후 어떤 함수와 자료구조를 통해 처리되는지를 분석한다.

---

# 6. 라이선스 검증 흐름 분석

보호 기능과 관련된 함수 후보를 확보한 후 실제 검증 흐름을 추적한다.

예상 분석 구조는 다음과 같다.

**Program Startup**

→ **License / Configuration Loading**

→ **Input Data Parsing**

→ **Validation**

→ **Internal State Generation**

→ **Condition Check**

→ **Program State 결정**

검증 과정에 관여하는 주요 함수와 데이터 구조를 분석하여 전체적인 License Validation Flow를 작성한다.

---

# 7. Function Map 및 Call Graph 작성

라이선스 및 보호 기능과 관련된 주요 함수를 식별하여 Function Map을 작성한다.

각 함수는 다음과 같은 기준으로 정리한다.

| 항목 | 내용 |
| --- | --- |
| 함수 주소 | 함수 위치 |
| 분석 함수명 | 분석자가 부여한 이름 |
| 기능 | 추정 역할 |
| Caller | 해당 함수를 호출하는 함수 |
| Callee | 해당 함수가 호출하는 함수 |
| Input | 주요 입력 |
| Output | 주요 반환값 |
| 관련 API | 사용되는 API |
| 분석 근거 | String, XREF, 동적 분석 등 |

Call Graph를 이용하여 함수 간 관계를 시각적으로 정리한다.

예를 들어 다음과 같은 형태가 될 수 있다.

**Initialization**

→ **License Initialization**

→ **License Data Load**

→ **Parser**

→ **Validation**

→ **Result Processing**

→ **Application State**

---

# 8. WinDbg를 이용한 동적 분석

정적 분석 결과를 기반으로 WinDbg에서 실제 프로그램 실행 과정을 추적한다.

주요 활용 기능은 다음과 같다.

- Software Breakpoint
- Hardware Breakpoint
- Memory Breakpoint
- Step Into
- Step Over
- Run Until
- Register
- Stack
- Memory Dump
- Memory Map
- Call Stack

정적 분석에서 라이선스 또는 보호 기능과 관련된 것으로 추정한 함수가 실제 실행 과정에서 언제 호출되는지 확인한다.

---

## 8-1. 함수 호출 분석

주요 함수에 대해 다음 내용을 조사한다.

- 함수 호출 시점
- Caller
- Callee
- Argument
- Return Value
- Register 변화
- Stack 변화
- Memory 변화
- Conditional Branch

Windows x64 Calling Convention을 기반으로 RCX, RDX, R8, R9 및 Stack에 전달되는 Argument를 분석한다.

---

# 9. Control Flow 분석

라이선스 검증 과정에서 중요한 함수의 Control Flow를 분석한다.

주요 분석 대상은 다음과 같다.

- Basic Block
- Conditional Branch
- Loop
- Function Call
- Success Path
- Failure Path
- Error Handling
- Return Path

검증 결과에 따라 프로그램의 실행 상태가 어떻게 달라지는지 확인하고 중요한 Branch와 State Transition을 구조화한다.

필요한 경우 Control Flow Diagram을 작성한다.

---

# 10. Data Flow 분석

라이선스 관련 데이터가 프로그램 내부에서 어떻게 전달되고 변형되는지 분석한다.

예상되는 데이터 흐름은 다음과 같다.

**External Data**

→ **Input Buffer**

→ **Parser**

→ **Internal Structure**

→ **Validation Logic**

→ **Result State**

→ **Application Logic**

각 단계에서 어떠한 데이터가 입력되고 어떠한 형태로 변환되는지를 추적한다.

WinDbg에서 Register와 Memory를 확인하여 정적 분석 결과와 실제 데이터를 비교한다.

---

# 11. 내부 자료구조 분석

보호 로직과 관련된 주요 내부 자료구조를 추정한다.

Memory Access Pattern과 함수 Argument를 이용하여 다음과 같은 정보의 존재 여부를 확인한다.

```
License / State Object
 ├─ version
 ├─ status
 ├─ flags
 ├─ data pointer
 ├─ size
 └─ validation result
```

C++ 객체가 사용되는 경우 다음 요소도 분석한다.

- `this` Pointer
- Object Layout
- VTable
- Virtual Function
- Constructor
- Destructor

핵심 검증 기능에 직접적으로 관련된 자료구조를 우선적으로 복원한다.

---

# 12. Software Protection 기법 분석

프로그램에서 확인되는 보호 기법을 분류하여 분석한다.

분석 후보는 다음과 같다.

- License Validation
- Integrity Check
- Signature Verification
- Anti-Debugging
- Anti-Tampering
- Obfuscation
- Runtime Check
- Environment Check

실제로 어떤 보호 기술이 사용되는지는 분석 결과를 기반으로 판단한다.

각 보호 기능에 대해 다음 내용을 기록한다.

- 실행 시점
- 관련 함수
- 입력 데이터
- 검증 방식
- 검증 결과가 사용되는 위치
- 다른 보호 기능과의 관계

---

# 13. Crack 관점의 보호 구조 분석

전체 보호 메커니즘을 파악한 후 Crack 관점에서 보호 구조를 분석한다.

단순히 하나의 조건문만 확인하는 것이 아니라 다음 요소를 중심으로 전체 구조를 평가한다.

- 라이선스 상태가 생성되는 위치
- 검증 결과가 전달되는 경로
- 검증이 수행되는 횟수
- 여러 단계의 검증이 존재하는지 여부
- Runtime 중 재검증 여부
- Integrity Check와의 연계 여부
- 서로 다른 Module 사이의 검증 관계
- 프로그램 기능 활성화 여부를 결정하는 상태 값
- 보호 로직 간 의존 관계

이를 기반으로 프로그램의 보호 구조를 하나의 **Protection Flow**로 정리한다.

최종적으로 어떠한 부분이 Crack 과정에서 핵심 분석 지점이 되는지를 기술적으로 평가한다.

---

# 14. 정적 분석과 동적 분석 결과 교차 검증

정적 분석에서 추론한 내용을 실제 실행 결과와 비교한다.

다음 방법을 활용한다.

- 서로 다른 실행 조건 비교
- Breakpoint 실행 위치 비교
- Register 값 비교
- Memory 변화 비교
- Function Argument 비교
- Return Value 비교
- Branch Path 비교
- Call Stack 비교

하나의 분석 결과만을 기반으로 결론을 내리지 않고 여러 분석 결과가 일치하는지 확인한다.

---

# 15. 분석 과정 문서화

프로젝트 수행 과정에서 모든 주요 분석 내용을 기록한다.

분석 기록에는 다음 내용을 포함한다.

- 분석 날짜
- 분석 대상 버전
- SHA-256 Hash
- 분석한 함수
- 함수 주소
- 함수 역할
- 분석 근거
- Caller / Callee
- Breakpoint 위치
- Register 상태
- Memory 상태
- Call Stack
- 분석 가설
- 동적 검증 결과
- 기존 분석 수정 사항

이를 통해 단순한 최종 결과뿐만 아니라 실제 Reverse Engineering 과정도 함께 문서화한다.

---

# 16. 프로젝트 기대효과

본 프로젝트를 통해 단순한 교육용 바이너리가 아닌 실제 대규모 상용 Windows 프로그램을 대상으로 Reverse Engineering을 수행하는 경험을 얻을 수 있다.

특히 다음 역량을 향상시키는 것을 기대한다.

- Windows PE 구조 분석 능력
- x86-64 Assembly 분석 능력
- IDA를 이용한 정적 분석 능력
- WinDbg를 이용한 동적 분석 능력
- Windows API 분석 능력
- Calling Convention 이해
- 함수 역할 추론 능력
- String / XREF 분석 능력
- Call Graph 분석 능력
- Control Flow 분석 능력
- Data Flow 분석 능력
- C/C++ 객체 및 자료구조 분석 능력
- Software Protection 분석 능력
- License Validation 구조 분석 능력
- 정적 분석과 동적 분석의 연계 능력
- 대규모 Binary에서 분석 범위를 좁혀가는 능력

특히 일반적인 프로그램 기능 분석을 넘어 실제 상용 소프트웨어의 보호 기능을 찾아내고 해당 로직의 동작 구조를 추적함으로써 Software Protection과 Reverse Engineering의 관계를 실습을 통해 이해할 수 있다.

향후 취약점 분석, Malware Analysis, Software Protection Analysis 및 기타 Binary Security 분야를 학습하기 위한 기반을 마련하는 것을 기대한다.

---

# 17. 프로젝트 수행 시 요구사항

## 개발 및 분석 환경

- Windows 11 x64
- 필요 시 Windows VM

## 사전지식

- C / C++ 기초
- x86-64 Assembly
- Register
- Stack / Heap
- Pointer
- Memory 구조
- Function Call
- Windows x64 Calling Convention
- Windows Process
- Virtual Memory
- PE Format
- Debugging 기초
- Reverse Engineering 기초

## 분석 도구

### IDA

정적 분석에 사용한다.

주요 기능은 다음과 같다.

- Disassembly
- Decompiler
- Function Analysis
- Strings
- XREF
- Imports / Exports
- Graph View
- Structures
- Rename
- Comment

### WinDbg

동적 분석에 사용한다.

주요 기능은 다음과 같다.

- Breakpoint
- Hardware Breakpoint
- Memory Breakpoint
- Step Into / Step Over
- Register
- Stack
- Memory Dump
- Memory Map
- Call Stack

### Python / C

분석 결과를 정리하거나 데이터 처리 과정 및 일부 로직을 재현하고 검증하는 데 활용한다.

---

# 18. 프로젝트 수행 시 활용되는 장비 및 물품

| 장비명/물품명 | 세부사양 |
| --- | --- |
| **H/W** | Windows 11 x64 PC |
| **S/W** | IDA, WinDbg, Python 또는 C 개발 환경 |
| **분석 환경** | 필요 시 Windows VM |
| **기타** | Reverse Engineering, Windows Internals, x86-64 Assembly, Software Protection, PE 구조 관련 참고 자료 |

---

# 19. 개인 수행 계획

- **주요 수행 항목:** 분석 환경 구축, IDA Professional 전체 구조 분석, PE 구조 분석, Import / Export 분석, 문자열 및 XREF 분석, Module 및 Subsystem 분석, 라이선스 및 보호 기능 관련 코드 탐색, 주요 함수 식별, Function Map 및 Call Graph 작성, WinDbg 동적 분석, 라이선스 검증 흐름 분석, 내부 자료구조 분석, Control Flow 분석, Data Flow 분석, Software Protection 구조 분석, Crack 관점의 보호 로직 평가, 분석 결과 검증 및 문서화
- **예상 산출물:** IDA Professional Reverse Engineering 분석 보고서, PE 구조 분석 자료, Program Architecture Diagram, 주요 Module 및 Subsystem 분류, 보호 기능 관련 Function Map, Call Graph, License Validation Flow, Protection Flow, Control Flow Diagram, Data Flow Diagram, 주요 자료구조 분석 결과, 동적 분석 기록, Breakpoint 및 Runtime Trace 기록, IDA Professional crack판
- **검증 방법:** IDA의 정적 분석 결과와 WinDbg에서 확인한 실제 실행 흐름을 비교한다. 함수 Argument, Return Value, Register, Stack, Memory 및 Branch Path를 추적하여 라이선스 및 보호 기능의 실제 동작을 검증한다.

---

# 20. 단계별 수행 일정

| 단계 | 수행 내용 | 주요 결과물 |
| --- | --- | --- |
| **1단계** | 분석 환경 구축 및 대상 Binary 고정 | Version / SHA-256 / 분석 환경 |
| **2단계** | PE / Section / Import / Export 분석 | Binary Overview |
| **3단계** | IDA Professional 전체 Architecture 분석 | Architecture Diagram |
| **4단계** | 문자열 / XREF / API 분석 | 주요 Function 후보 |
| **5단계** | License / Protection 관련 코드 탐색 | 관련 함수 및 Module 목록 |
| **6단계** | Function Map / Call Graph 분석 | Function Map / Call Graph |
| **7단계** | WinDbg를 이용한 Runtime 분석 | Runtime Trace |
| **8단계** | License Validation Flow 분석 | License Validation Flow |
| **9단계** | Control Flow / Data Flow / 자료구조 분석 | Diagram 및 구조 분석 |
| **10단계** | Software Protection 구조 분석 | Protection Mechanism Map |
| **11단계** | Crack 관점의 핵심 분석 지점 평가 | Crack Analysis 결과 |
| **12단계** | 정적·동적 분석 결과 통합 및 문서화 | 최종 Reverse Engineering Report |

---

# 21. 최종 산출물

최종 산출물은 다음과 같이 구성한다.

- IDA Professional Reverse Engineering 분석 보고서
- PE 구조 분석 자료
- Program Architecture Diagram
- 주요 Module 및 Subsystem 분류
- 보호 기능 관련 Function Map
- Call Graph
- License Validation Flow
- Protection Flow
- Control Flow Diagram
- Data Flow Diagram
- 주요 자료구조 분석 결과
- 동적 분석 기록
- Breakpoint 및 Runtime Trace 기록
- IDA Professional crack판

최종 분석 보고서는 **IDA Professional Software Protection Reverse Engineering Report** 형태로 작성하며, 보고서의 주요 구성은 다음과 같다.

1. **Target Overview**
    - IDA Professional Version
    - SHA-256
    - Binary 정보
2. **Binary Structure**
    - PE
    - Section
    - Import / Export
    - Runtime
3. **Program Architecture**
    - 초기화 과정
    - 주요 Module
    - 주요 Subsystem
4. **Protection Surface**
    - License 관련 요소
    - Integrity 관련 요소
    - 기타 보호 기능
5. **Function Map**
    - 주요 함수
    - Caller / Callee
    - 함수 역할
6. **License Validation Flow**
    - 입력
    - Parsing
    - Validation
    - Result State
7. **Dynamic Analysis**
    - Breakpoint
    - Register
    - Stack
    - Memory
    - Runtime Trace
8. **Control Flow / Data Flow**
    - 주요 Branch
    - 데이터 이동
    - 상태 변화
9. **Internal Data Structure**
    - 주요 Object
    - 상태 값
    - 관련 구조체
10. **Protection Mechanism Analysis**
    - 보호 기법
    - 상호 의존 관계
    - 검증 구조
11. **Crack Analysis**
    - 보호 구조의 핵심 분석 지점
    - 검증 구조에 대한 분석
    - Crack 관점에서의 기술적 평가
12. **Conclusion**
    - 분석 결과
    - 한계점
    - 추가 분석 가능 영역

---

# 참고 자료

- Microsoft PE Format Documentation
- Microsoft Windows API Documentation
- Microsoft Windows Internals 관련 자료
- IDA Documentation
- Microsoft WinDbg Documentation
- Intel 64 and IA-32 Architectures Software Developer's Manual
- Windows x64 Calling Convention 관련 문서
- Reverse Engineering 관련 기술 문서
- Software Protection 및 Binary Analysis 관련 기술 자료
