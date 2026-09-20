---
project_name: "runc-clear"
quad_name: "8조"
members: ["20231726_박민영", "20251788_김동후", "20245024_김진호", "20231754_한지선"]
report_number: 7
date: "2026-08-11"
status: "완료"
cl_level: "CL2"
is_final: true
contributions:
  - name: "20231726_박민영"
    role: "팀장"
    tasks: "프로젝트 기획·일정 관리, 컨테이너 기초 및 runc 실행 흐름 분석, CVE별 Root Cause·공격 조건·대응 방안 정리, CVE-2026-41567 취약/패치 환경 PoC 재현, 최종 분석 문서 통합"
    percentage: 25
  - name: "20251788_김동후"
    role: "팀원"
    tasks: "runc 실행 환경과 격리 구조 검증, 취약/패치 런타임 비교 환경 및 자동화 구성, CVE별 보안 영향·패치 코드 비교, PoC 시나리오 설계"
    percentage: 25
  - name: "20245024_김진호"
    role: "팀원"
    tasks: "runc 내부 실행·동기화 로직 분석, CVE-2024-45310 및 CVE-2024-25621 PoC 검증, DinD 기반 CVE-2026-41567 재현, PoC 양식 표준화와 재현 로그 확보"
    percentage: 25
  - name: "20231754_한지선"
    role: "팀원"
    tasks: "syscall·namespace 및 파일시스템 격리 분석, 취약/패치 코드 차이와 방어 로직 정리, WSL2 기반 교차 검증 환경 구성, Root Cause 및 대응 방안 통합"
    percentage: 25
---

# ASC 프로젝트 최종 기술 보고서 — runc-clear

- **참여 인원:** (팀장) 20231726_박민영, (팀원) 20251788_김동후, 20245024_김진호, 20231754_한지선
- **활동 기간:** 2026. 03. 29. ~ 2026. 08. 15.
- **프로젝트 구분:** 심화 프로젝트
- **프로젝트 분야:** 컨테이너 보안

## 1. 개요 및 목적

### 배경

Docker와 Kubernetes는 컨테이너 생성의 마지막 단계에서 OCI 런타임인 `runc`를 사용하며, `containerd`와 Docker Engine/Moby는 이미지·볼륨·아카이브·런타임 상태를 관리한다. 이 계층들은 대부분 호스트의 높은 권한으로 파일 디스크립터, 마운트, 심볼릭 링크, `/proc`, 런타임 디렉터리를 다루므로, 작은 경로 검증 오류나 권한 설정 실수도 컨테이너 격리 우회로 이어질 수 있다.

본 프로젝트는 컨테이너를 단순한 가상 환경이 아니라 Linux namespace, cgroup, rootfs, mount, capability가 결합된 프로세스 격리 구조로 이해하고, 공개 취약점을 코드와 실험 양쪽에서 검증하기 위해 시작하였다.

### 목표

- Linux namespace, cgroup, `pivot_root`, capability 등 컨테이너 격리 기반 기술을 학습한다.
- OCI bundle의 `config.json`이 `runc` 내부 설정으로 변환되고 컨테이너 프로세스가 실행되는 흐름을 추적한다.
- 공개 CVE의 취약 버전과 패치 버전을 비교하여 Root Cause와 방어 원리를 코드 수준에서 설명한다.
- 재현 가능한 PoC와 로그를 확보하여 컨테이너 격리 우회, 호스트 파일 접근, 권한 경계 붕괴 가능성을 실험적으로 입증한다.
- 실험 결과를 기반으로 업데이트 기준과 운영상 완화책을 제시한다.

### 최종 분석 범위

| 구분 | 대상 | 핵심 취약점 | PoC 성공 여부 | Exploit 성공 여부 | 프로젝트 내 상태 |
|------|------|-------------|---------------|-------------------|------------------|
| `CVE-2024-45310` | runc | mountpoint 생성 과정의 TOCTOU 및 symlink following | 성공 — 호스트에 0바이트 파일 생성 | 실패 — 임의 내용 쓰기·권한 상승 미확인 | 취약/패치 비교 재현 완료 |
| `CVE-2024-25621` | containerd | 민감 디렉터리의 과도한 traverse 권한 | 성공 — 비권한 `meta.db` 접근 및 SUID 실행 확인 | 실패 — SUID 내부 권한 검사로 권한 상승 차단 | 접근제어 결함 재현 완료 |
| `CVE-2026-41567` | Docker Engine/Moby | 컨테이너 내부 압축 해제 바이너리 실행 | 성공 — fake `xz`/`unpigz` 호출 확인 | 성공 — Docker daemon의 호스트 root 문맥 코드 실행 확인 | 취약/패치 비교 재현 완료 |
| `CVE-2026-42306` | Docker Engine/Moby | `docker cp` 중 bind mount 대상 경로 TOCTOU | 성공 — 일부 race 성공 케이스 확인 | 실패 — 반복 가능한 호스트 영향 입증 미완료 | 코드 분석 완료, PoC 부분 검증 |

여기서 **PoC 성공**은 취약 조건과 보안 경계 위반 primitive를 관찰한 경우를 의미하며, **Exploit 성공**은 해당 primitive를 실제 호스트 권한 코드 실행, 권한 상승 또는 지속적인 호스트 자원 변경으로 연결해 입증한 경우를 의미한다.

## 2. 기술적 상세 분석

### 2.1 분석 방법론

프로젝트는 다음 순서로 수행하였다.

1. 컨테이너 격리 기반 기술 학습
   - Docker/Kubernetes 구조, Linux namespace, cgroup v1/v2, rootfs, `chroot`와 `pivot_root`의 차이를 정리하였다.
2. runc 실행 흐름 추적
   - Docker image를 OCI bundle로 변환하고 `runc run`, `runc create`, `runc start`를 직접 실행하였다.
   - `strace`로 `clone`, `unshare`, `pivot_root`, `mount`, `execve` 호출을 확인하였다.
3. 소스코드 분석
   - CLI 진입점부터 OCI spec 변환, `libcontainer.Container`, `runc init`, nsexec, rootfs 준비, namespace 마무리, 사용자 프로세스 `execve`까지 추적하였다.
4. CVE 분석 및 패치 비교
   - 공식 advisory, 영향 버전, 수정 커밋을 기준으로 취약 경로와 패치 후 방어 로직을 비교하였다.
5. PoC 검증
   - 취약 버전과 패치 버전을 동일하거나 최대한 유사한 조건에서 반복 실행하고, 호스트 측 마커·권한·로그를 비교하였다.

### 2.2 runc 핵심 실행 흐름

```text
Docker / containerd
  -> OCI bundle(config.json, rootfs) 준비
  -> runc run 또는 runc create/start
  -> OCI spec을 libcontainer config로 변환
  -> libcontainer.Container 및 state directory 생성
  -> runc init 자식 프로세스 실행
  -> nsexec가 Go runtime 이전에 namespace 생성/진입
  -> rootfs와 mount, cgroup, capability, LSM 설정
  -> pivot_root 또는 chroot
  -> 내부 fd 정리 및 cwd 검증
  -> execve(container process)
```

이 흐름에서 확인한 핵심 보안 경계는 다음과 같다.

- 경로 문자열을 검증한 시점과 실제 syscall 실행 시점 사이에 경로가 바뀌지 않아야 한다.
- 이미 열린 파일 디스크립터는 `pivot_root` 이후에도 기존 inode를 가리킬 수 있으므로 상속과 수명 관리가 필요하다.
- `/proc/self/fd/*`, symlink, bind mount는 컨테이너 내부 경로를 다시 호스트 자원과 연결할 수 있다.
- 런타임 관리 디렉터리는 파일 목록 읽기뿐 아니라 알려진 경로에 대한 traverse도 차단해야 한다.

### 2.3 실험 환경

| 목적 | 환경 및 버전 |
|------|--------------|
| runc 실행 흐름 분석 | Linux/WSL2 및 OCI bundle, `strace`, Go 기반 runc 소스코드 |
| CVE-2024-45310 | `runc 1.1.13`(취약) / `1.1.14`(패치), privileged Linux 실험 환경, 반복 race 스크립트 |
| CVE-2024-25621 | Ubuntu 24.04.4 LTS, `containerd 1.7.28`(취약) / `1.7.29`(패치), 분리된 `--root`·`--state`·socket |
| CVE-2026-41567 | WSL2 Ubuntu 24.04 및 `Docker Engine 29.5.0`/`29.5.1`, Colima 위 `docker:28.5.2-dind`, archive API와 `docker cp -` |
| CVE-2026-42306 | `Docker Engine 29.5.0` (취약) /`29.5.1` (패치), volume이 연결된 컨테이너와 `docker cp`/archive API 기반 race 시나리오 |

실험은 실제 호스트 훼손을 막기 위해 WSL2 전용 배포판, privileged 랩 컨테이너 또는 DinD 환경을 사용하였다. 성공 여부는 호스트 측 안전한 마커 파일, 권한 비트, namespace/hostname, daemon 로그를 기준으로 판정하였다.

### 2.4 CVE-2024-45310 — runc mountpoint TOCTOU

#### Root Cause

취약 버전은 `securejoin.SecureJoin()`으로 rootfs 내부 경로를 계산한 뒤 실제 생성에는 `os.MkdirAll()` 또는 `os.OpenFile(O_CREATE)` 같은 문자열 경로 API를 다시 사용한다. 공격자가 검증과 생성 사이에 중간 경로를 호스트 경로를 가리키는 symlink로 교체하면 실제 생성 syscall이 rootfs 밖에서 실행될 수 있다.

```text
SecureJoin으로 목적지 계산
  -> 공격자가 중간 디렉터리를 symlink로 교체
  -> os.MkdirAll / os.OpenFile이 경로를 다시 해석
  -> 호스트 임의 위치에 빈 파일 또는 빈 디렉터리 생성
```

#### 패치

`runc 1.1.14`는 mountpoint 생성을 `createMountpoint()`로 통합하고, `openat(O_NOFOLLOW|O_DIRECTORY)`, `mkdirat`, `Mknodat` 및 `MkdirAllInRootOpen()` 계열 helper를 사용한다. 문자열 경로를 반복 해석하지 않고 rootfs fd에서 시작하는 fd 체인으로 각 구성요소를 고정하여 symlink swap을 차단한다.

#### 검증 결과

- 취약 환경에서 호스트 대상 경로에 0바이트 파일이 생성되는 성공 로그를 확보하였다.
- 상세 재현에서는 8번째 시도에 성공하였다.
- 패치 버전에서는 동일 race를 300회 실행해도 호스트 파일이 생성되지 않았다.
- 영향은 기존 파일 덮어쓰기보다 호스트 측 빈 inode 생성 primitive에 가깝고, 단독 권한 상승은 확인하지 않았다.

### 2.5 CVE-2024-25621 — containerd 디렉터리 권한 오설정

#### Root Cause

취약 버전은 `/var/lib/containerd`와 일부 CRI 관련 민감 경로를 `0700`이 아닌 `0711` 또는 `0755`로 생성한다. 디렉터리 목록을 읽을 수 없어도 경로 이름을 알고 있는 비권한 사용자는 execute 비트를 이용해 하위 경로로 이동할 수 있다. containerd의 경로 구조는 공개되어 있으므로 listing 차단만으로는 충분하지 않다.

#### 패치

- 최상위 root 및 민감한 CRI/sandbox 경로를 `0700`으로 생성한다.
- 기존 설치에도 `chmod 0700`을 적용하도록 보강하였다.
- user namespace 지원을 위해 의도적으로 `0711`을 유지하는 일부 state 경로는 별도 예외로 구분하였다.

#### 검증 결과

```text
1.7.28 root perms: 711
1.7.29 root perms: 700
1.7.28 meta.db read as unprivileged user: OK
1.7.29 meta.db read as unprivileged user: DENIED
```

SUID `passwd`, `mount` 바이너리까지 도달하고 실행할 수 있었지만, 프로그램 내부의 real UID·PAM·권한 정책으로 직접적인 권한 상승은 차단되었다. 따라서 본 실험은 접근제어 결함과 공격 표면 확대를 증명했으며, 임의 권한 상승 성공으로 해석하지 않았다.

### 2.6 CVE-2026-41567 — 컨테이너 내부 압축 해제 바이너리 실행

#### Root Cause

취약 Docker/Moby는 archive upload를 처리하면서 컨테이너 파일시스템으로 `RunInFS` 전환한 상태에서 `xz` 또는 `unpigz` 같은 외부 압축 해제 바이너리를 탐색할 수 있다. 그 결과 악성 이미지가 제공한 동명 바이너리가 Docker daemon의 호스트 root 권한으로 실행될 수 있다.

주요 트리거는 `PUT /containers/{id}/archive`와 압축된 입력을 사용하는 `docker cp -`이다. 일반적인 비압축 `docker cp file container:/path` 전체가 동일하게 취약한 것은 아니다.

#### 패치

`Docker Engine 29.5.1`의 패치는 컨테이너 내부에서 외부 압축 해제 바이너리를 탐색·실행하는 흐름을 제거하고, 안전한 비압축 untar 처리 경로를 사용하도록 변경한다.

#### 검증 결과

- WSL2 Ubuntu 24.04에서 `29.5.0`과 `29.5.1`을 지정 설치해 교차 검증하였다.
- 취약 버전에서 fake `xz`/`unpigz` 실행 흔적을 확인하였다.
- daemon 측 hostname과 namespace 정보를 남겨 컨테이너 내부 root가 아니라 호스트 daemon 문맥에서 실행되었음을 구분하였다.
- DinD 환경에서는 archive API가 HTTP 200을 반환하고 `wrapper_generated.txt` 증거 로그가 생성되는 것을 확인하였다.
- 패치 버전에서는 동일 악성 바이너리 호출이 관찰되지 않았다.

### 2.7 CVE-2026-42306 — docker cp bind mount redirection

#### Root Cause

Docker daemon은 volume이 있는 컨테이너에 `docker cp`를 수행할 때 임시 mount namespace에서 컨테이너의 mount 구성을 재현한다. 취약 버전은 `GetResourcePath()`로 mount destination 문자열을 계산하고 필요 시 경로를 생성한 뒤, 나중에 `mount.Mount()`에서 같은 문자열을 다시 해석한다.

공격자가 그 사이 destination 또는 상위 경로를 호스트 임의 경로를 가리키는 symlink로 교체하면, daemon이 의도한 컨테이너 내부 경로가 아닌 호스트 경로에 volume을 bind mount할 수 있다. writable volume이면 호스트 파일 변경, read-only volume이면 일시적인 경로 가림을 통한 DoS 가능성이 있다.

#### 패치

패치 버전은 `os.Root`를 통해 대상 inode를 파일 디스크립터로 열어 고정하고, `/proc/self/fd/<fd>`를 mount target으로 사용한다. 경로명이 race 도중 바뀌더라도 mount 대상 inode는 바뀌지 않으므로 symlink redirection을 막는다.

#### 검증 상태

- Root Cause와 취약/패치 코드 비교는 완료하였다.
- 팀 차원에서 일부 race 성공 케이스를 확인했으나, 박민영 담당 브랜치의 PoC는 최종 완료되지 않았다.
- 재현 결과의 반복성과 호스트 영향 판정을 충분히 확보하지 못했으므로, 본 보고서에서는 완전 재현이 아닌 **부분 검증**으로 분류한다.

### 2.8 공통 방어 원리

네 취약점은 구현 위치가 다르지만 다음 원칙으로 정리할 수 있다.

| 실패 유형 | 취약 구현 | 안전한 구현 |
|----------|-----------|-------------|
| 경로 검증과 사용 분리 | 검증한 문자열 경로를 나중에 다시 open/mount | root fd에서 `openat`하고 inode fd를 유지 |
| symlink 추종 | 일반 `open`, `mkdir`, `mount`가 중간 symlink를 재해석 | `O_NOFOLLOW`, `mkdirat`, `/proc/self/fd/<fd>` 사용 |
| 실행 경로 오염 | 컨테이너 rootfs에서 외부 바이너리 탐색 | 신뢰 경계 밖 바이너리 탐색 제거 |
| 디렉터리 권한 과다 | 공개 경로를 `0711`로 두어 traverse 허용 | 민감 root/CRI 경로를 `0700`으로 제한 |

## 3. 최종 결과물

### 산출물 요약

- 프로젝트 계획서와 1~6차 진행 보고서
- 컨테이너 기반 기술 및 runc 실행 흐름 분석 문서
- 네 개 CVE의 Root Cause, 영향 버전, 패치 코드 비교 문서
- 취약/패치 환경 구성 스크립트와 반복 실행형 PoC
- CVE-2024-45310 취약/패치 비교 로그
- CVE-2024-25621 권한·비권한 접근 비교 로그
- CVE-2026-41567 fake `xz`/`unpigz` 및 archive API 재현 로그
- CVE-2026-42306 코드 분석과 부분 PoC 시나리오

### 산출물 링크
https://drive.google.com/file/d/1GfAsfzlDREeuvGDQnqusZneowPwt0jUq/view?usp=sharing

## 4. 실전 입증 및 성과

### 정량 검증 결과

| 대상 | 취약 환경 | 패치 환경 | 객관적 판정 지표 |
|------|-----------|-----------|------------------|
| CVE-2024-45310 | 8번째 시도에 호스트 0바이트 파일 생성 | 300회 동안 생성 없음 | 호스트 대상 파일 존재 여부 |
| CVE-2024-25621 | root `0711`, 비권한 `meta.db` 접근 성공 | root `0700`, 동일 접근 거부 | 권한 비트 및 비권한 읽기 성공/실패 |
| CVE-2026-41567 | fake `xz`/`unpigz` 실행, daemon 문맥 로그 생성 | 악성 바이너리 호출 없음 | hostname·namespace·마커 및 daemon 로그 |
| CVE-2026-42306 | 일부 race 성공 케이스 확인 |

### 취약점 증명

- 단순 버전 정보 확인에 그치지 않고 취약 버전과 패치 버전을 같은 절차로 실행하여 행동 차이를 비교하였다.
- race condition은 단발 실행 결과 대신 반복 횟수와 호스트 측 부작용을 기록하도록 자동화하였다.
- 컨테이너 root와 호스트 root를 구분하기 위해 UID뿐 아니라 hostname과 namespace를 함께 수집하였다.
- 호스트 실험은 마커 파일과 격리 랩으로 제한하여 실제 시스템 파일 훼손을 피했다.

### 대외 인증

본 프로젝트는 기존 공개 CVE를 분석·재현한 연구 프로젝트이며, 팀이 신규 CVE를 발급받거나 외부 Bounty 포상을 받은 결과는 없다. 성과는 공개 advisory의 기술 설명을 코드 분석과 독립 재현으로 검증하고, 패치 효과를 비교한 데 있다.

## 5. 팀원별 기여 상세 (전체 기간)
Notion: https://app.notion.com/p/2026-1-ASC-a9b44fff78a78343af92012f1360c0bb?source=copy_link


| 팀원 | 역할 | 수행 작업 | 산출물 링크 | 기여도 |
|------|------|----------|-------------|--------|
| 20231726_박민영 | 팀장, 분석 통합 | 계획서 작성과 일정 관리, 컨테이너 기초·runc Filesystem/Jail 흐름 분석, CVE-2024-45310 후보 선정·공격 구조·방어 관점 정리, CVE-2024-25621 개요·운영 위험·대응 정리, CVE-2026-41567 `archive_unix.go` 분석 및 WSL2 취약/패치 PoC, CVE-2026-42306 Root Cause 분석, 최종 문서 통합 | Notion에 매 회차 작업 내용 업로드 | 25% |
| 20251788_김동후 | 환경·패치 비교 | 컨테이너 기초 조사, runc 실행 환경·격리·capability/cgroup 분석, CVE-2024-45310 취약 runc 교체와 race 실험, containerd 1.7.28/1.7.29 비교 자동화, CVE-2026-41567 영향 분석과 fake `xz` PoC 설계, 기존 CVE 취약/패치 코드 통합 | Notion에 매 회차 작업 내용 업로드 | 25% |
| 20245024_김진호 | PoC·검증 | runc CLI~nsexec·부모/자식 동기화 분석, CVE-2024-45310 성공 로그와 패치 비교, CVE-2024-25621 SUID 도달·실행 검증, PoC 양식 통일, CVE-2026-42306 성공 | Notion에 매 회차 작업 내용 업로드 | 25% |
| 20231754_한지선 | 코드·방어 분석 | namespace/syscall 추적과 rootfs/mount 분석, CVE-2024-45310 시나리오·패치 helper 분석, containerd 업스트림 패치·실험 제약 정리, CVE-2026-41567 WSL2 교차 테스트 및 hostname/namespace 로깅, CVE Root Cause·대응 방안 통합 | Notion에 매 회차 작업 내용 업로드 | 25% |

## 6. 고찰 및 결론

### 한계점

- race condition PoC는 시스템 부하와 스케줄링에 따라 성공률이 달라지므로 단일 성공 횟수를 일반화할 수 없다.
- CVE-2024-25621에서는 접근제어 결함과 SUID 실행 가능성은 확인했지만 Ubuntu 기본 바이너리의 내부 권한 검사 때문에 직접 권한 상승은 재현하지 못했다.

### 결론

본 프로젝트는 컨테이너 런타임의 보안 경계를 `경로 문자열`, `inode/file descriptor`, `mount namespace`, `디렉터리 권한`, `daemon 실행 문맥`의 관점에서 분석하였다. 팀은 runc의 실행 흐름을 소스코드와 syscall 수준에서 추적하고, runc·containerd·Docker/Moby의 서로 다른 취약점을 동일한 Root Cause/패치/PoC 구조로 정리하였다.

특히 세 취약점에 대해 취약·패치 버전의 행동 차이를 직접 입증했고, 단순 `uid=0` 출력이나 일회성 race 성공을 충분한 증거로 보지 않고 호스트 마커, namespace, 권한 비트, 반복 횟수를 함께 사용했다. 이를 통해 공개 advisory를 요약하는 수준을 넘어 취약 환경 구성, 코드 분석, 실전 재현, 실패 원인 분석, 방어 원리 도출까지 이어지는 컨테이너 보안 분석 역량을 확보하였다.

## 7. 참고 문헌 및 자료

### 공통

- https://github.com/opencontainers/runc // runc 공식 저장소
- https://github.com/opencontainers/runtime-spec // OCI Runtime Specification
- https://github.com/containerd/containerd // containerd 공식 저장소
- https://github.com/moby/moby // Moby 공식 저장소

### CVE-2024-45310

- https://github.com/opencontainers/runc/security/advisories/GHSA-jfvp-7x6p-h2pv // 공식 advisory
- https://nvd.nist.gov/vuln/detail/CVE-2024-45310 // NVD
- https://github.com/opencontainers/runc/commit/63c2908164f3a1daea455bf5bcd8d363d70328c7 // 수정 커밋
- https://github.com/opencontainers/runc/commit/f0b652ea61ff6750a8fcc69865d45a7abf37accf // 수정 커밋

### CVE-2024-25621

- https://github.com/containerd/containerd/security/advisories/GHSA-pwhc-rpq9-4c8w // 공식 advisory
- https://nvd.nist.gov/vuln/detail/CVE-2024-25621 // NVD
- https://github.com/containerd/containerd/commit/7c59e8e9e970d38061a77b586b23655c352bfec5 // 수정 커밋

### CVE-2026-41567

- https://github.com/moby/moby/security/advisories/GHSA-x86f-5xw2-fm2r // 공식 advisory
- https://nvd.nist.gov/vuln/detail/CVE-2026-41567 // NVD
- https://github.com/moby/moby/commit/83946f17c3196c55434aa0b8a8773d3477cbd3dc // 수정 커밋

### CVE-2026-42306

- https://github.com/moby/moby/security/advisories/GHSA-rg2x-37c3-w2rh // 공식 advisory
- https://nvd.nist.gov/vuln/detail/CVE-2026-42306 // NVD
- https://github.com/moby/moby/commit/43fa458a9c40873867e75221454de10709b04236 // 수정 커밋
