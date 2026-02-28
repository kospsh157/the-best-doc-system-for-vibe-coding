# 프로젝트 세션 시작 안내

이 문서는 매 세션 시작 시 반드시 먼저 읽는다. 목적은 문서 체계를 이해하고, 프로젝트 구조를 빠르게 파악하며, 변경 사항을 문서에 정확히 반영하는 것이다.

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시.  
- 갱신: 문서 체계/세션 규칙/읽기 순서가 바뀌었을 때.  

## 문서의 1차 목적(필수)
- 이 문서 체계의 1차 목적은 AI 에이전트의 빠른 세션 복귀다.
- 개발자 참고는 부가 목적이며, 모든 문서는 AI가 빠르게 읽고 행동할 수 있게 작성한다.
- 세션 시작 시 "현재 목표/최근 변경/다음 작업/리스크/구조 규칙"을 먼저 파악한다.

## 사용자 호출 문구 대응(고정)
- 시작 문구: `starter.md 읽고 문서 체계 이해한다음 프로젝트 구조 파악하고 할 작업 뭐가 있는지 파악해봐`
- 종료 문구: `세션 종료할꺼야 문서 체계에 맞춰서 지금까지 한 작업들 문서 업데이트 해줘`
- 위 문구가 들어오면 아래 3단계 프로토콜을 그대로 수행한다.

## 3단계 운영 프로토콜(필수)
1) 복구: L0 읽기 -> 현재 목표/다음 작업/리스크/구조 규칙을 6줄 이내로 요약  
2) 실행: 명세 -> 구현 -> `python3 scripts/check_arch.py` -> 테스트 -> 문서 동기화  
3) 인수인계: `docs/session/README.md`/`docs/session/LOG.md` 갱신 + 재개 포인트 1개 확정 -> `python3 scripts/check_docs.py` 통과  

## 문서 품질 게이트(필수)
- 의미 없는 중복 금지: 동일 사실/규칙/결정은 단일 기준 문서에만 기록한다.
- 누락 금지: 변경 영향 문서를 동시에 업데이트한다.
- 플레이스홀더 금지: 템플릿 문서를 제외한 문서에 빈 항목/`(추가 예정)`을 남기지 않는다.
- 세션 종료 전 문서 검사: `python3 scripts/check_docs.py`

## 토큰 관리 및 안전 축약 규칙(필수)
- 세션 시작 시 문서 토큰을 확인한다: `python3 scripts/doc_tokens.py` 또는 `./scripts/run_doc_tokens.sh`
- 권장 토큰 가드 확인: `python3 scripts/doc_token_guard.py`
- 기본 가드값: 예산 40000, 경고 30000(비율 0.75, 프로젝트 성장 고려)
- 필요 시 환경 변수로 조정: `DOC_TOKEN_BUDGET`, `DOC_TOKEN_WARN_RATIO`
- 에이전트는 중복 제거/구조 재배치/요약본 추가 같은 비파괴 정리를 사용자 승인 없이 수행할 수 있다.
- 문서가 길어 축약이 필요해도, 에이전트는 사용자 승인 없이 기존 내용을 삭제/축약하지 않는다.
- 30000 토큰 도달 시: 비파괴 간단 정리(중복 링크화/요약 정리/구조 개선)를 자동 수행한다.
- 40000 토큰 도달 시: 전체 문서를 정밀 검토해 중복/오래된 내용을 정리하되 삭제/축약은 반드시 사용자 승인 후 수행한다.
- `프로젝트 기초`, `핵심 설계`, `지켜야 할 지침`에 해당하는 섹션은 정리 대상에서 제외하고 삭제/축약하지 않는다.
- 축약이 필요하면 먼저 "삭제/축약 후보 + 영향 + 대안"을 제시하고 사용자에게 승인 여부를 묻는다.
- 사용자 명시 승인 전에는 요약본 추가/구조 개선까지만 수행하고 원문 삭제는 금지한다.
- 승인 후에도 `필수 규칙/결정/재개 포인트/현재 상태`, `프로젝트 기초/핵심 설계/지침` 섹션은 삭제 금지, 필요 시 위치 이동만 허용한다.

## 프로젝트 구조 빠른 요약(세션 시작 직후)
- 이 저장소는 **주제(도메인) 미정 상태에서도** Clean Architecture 골격을 먼저 고정해 시작한다.  
- 고정 레이어: `src/domain/`, `src/application/`, `src/interface/`, `src/infrastructure/`, `src/entrypoints/`  
- 테스트 구조: `tests/unit/domain/`, `tests/unit/application/`, `tests/integration/`  
- 문서 구조: `docs/` 하위 레벨(L0/L1/L2/L3) 운영  
- 아키텍처 규칙 검사: `python3 scripts/check_arch.py`  
- 문서 토큰 확인: `python3 scripts/doc_tokens.py` 또는 `./scripts/run_doc_tokens.sh`  

## 주제 미정 상태 운영 규칙(필수)
- 사용자에게 정확한 프로젝트 주제를 전달받기 전까지, 비즈니스 구현보다 구조/경계/품질 장치를 먼저 확정한다.  
- 도메인 용어가 미정이면 임시 용어를 남발하지 말고, `docs/project/overview.md`, `docs/project/scope.md`에 "미정"으로 명시한다.  
- 새 코드/파일 추가 시 레이어 경계를 먼저 결정하고 해당 경계에만 배치한다.  
- 유스케이스는 `application`, 외부 연동 구현은 `infrastructure`, 입출력 어댑터는 `interface`에만 둔다.  
- 구조 변경이 발생하면 즉시 `docs/architecture/structure.md`를 갱신하고 검사 스크립트를 통과시킨다.  

## 주제 확정 이후 전환 규칙(필수)
- 사용자가 프로젝트 주제/도메인을 전달하면, 에이전트는 문서 체계를 유지한 채 내용을 해당 주제로 채운다.
- 우선 채울 문서: `docs/project/overview.md`, `docs/project/scope.md`, `docs/project/glossary.md`, `docs/project/roadmap.md`
- 구현 전 채울 문서: `docs/specs/feature-*.md` (최소 1개 기능 명세)
- 필요 시 채울 문서: `docs/data/model.md`, `docs/integrations/external-services.md`, `docs/ops/runbook.md`
- 진행 중에는 세션마다 `docs/session/README.md`와 `docs/session/LOG.md`를 최신화해 다음 세션 복귀를 보장한다.
- 규칙은 유지하고 내용만 교체한다. (문서 레벨 구조/L0 순서/계층 경계 규칙은 고정)

## 프로젝트 이해 절차(에이전트)
1) `docs/README.md` 를 읽고 문서 구조와 규칙을 확인한다.  
2) `docs/session/README.md` 를 읽고 프로젝트 스냅샷/현재 상태를 파악한다.  
3) `docs/session/LOG.md` 의 최신 1~3개 항목을 확인한다.  
4) `docs/project/overview.md` 를 읽고 프로젝트 목적/목표를 확인한다.  
5) `docs/project/scope.md` 를 읽고 범위/제약을 확인한다.  
6) `docs/architecture/overview.md` 를 읽고 Clean Architecture 기준을 확인한다.  
7) `docs/architecture/structure.md` 를 읽고 폴더 구조/경계를 확인한다.  
8) 필요 시 L1/L2 문서를 `docs/README.md` 안내에 따라 확인한다.  

## 문서 체계 규칙
- 문서는 `docs/` 아래에만 둔다.  
- 문서 분류를 위해 하위 폴더를 사용한다.  
- 변경 사항이 구조/규칙/동작에 영향을 주면 관련 문서를 업데이트한다.  
- 중요한 설계 결정은 `docs/architecture/decisions.md`에 기록한다.  
- 문서 간 링크는 상대 경로로 유지한다.  
- 상세 목록은 `docs/README.md` 참고.  
- 기본 원칙: L0는 항상 읽고, L1은 재개 맥락, L2는 작업 상세, L3는 심화 참조로 최소한만 읽는다.  

## AI 세션 프롬프트(필수)
이 문서를 읽은 뒤 아래 규칙을 반드시 따른다.
1) L0 8개 문서를 순서대로 읽고, 프로젝트 스냅샷/현재 상태/범위/구조를 짧게 이해한다.  
2) 불확실한 부분이 있을 때만 L1/L2/L3 문서를 추가로 읽는다.  
3) 세션 중 읽은 모든 문서를 기록한다(L0 포함).  
4) 작업 중 변경이 생기면 해당 문서를 즉시 갱신한다.  
5) 세션 종료 시 `docs/session/END_PROMPT.md`를 읽고 절차를 수행한다.  
6) 세션 시작 시 `python3 scripts/doc_tokens.py`로 문서 토큰 합계를 계산해 사용자에게 보고한다(현재 계산 방식은 추정치).  
7) 사용자에게 정확한 도메인 주제를 받기 전에는 구조 고정 작업(레이어/포트/테스트 골격/검사 자동화)을 우선한다.  
8) 구현 전후로 `python3 scripts/check_arch.py`를 실행해 계층 의존성 위반을 확인한다.  
9) 사용자의 시작 문구가 오면 3단계 프로토콜의 "복구"부터 즉시 수행한다.  
10) 사용자의 종료 문구가 오면 3단계 프로토콜의 "인수인계"를 완료한 뒤 보고한다.  
11) 사용자가 프로젝트 주제를 주면, 고정 문서 틀을 유지한 채 프로젝트 관련 문서를 즉시 해당 주제로 채운다.  
12) 이후 세션에서도 동일한 문서 체계를 유지하며 문서-코드-진행 상태를 계속 동기화한다.  
13) 문서 업데이트 후 `python3 scripts/check_docs.py`를 실행해 중복/누락/플레이스홀더를 점검한다.  

## L0 고정 목록(항상 읽기)
1) `starter.md`  
2) `docs/README.md`  
3) `docs/session/README.md`  
4) `docs/session/LOG.md` (최신 1~3개 항목)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  

## 작업 유형 판별 규칙(필수)
1) 작업 유형을 먼저 분류한다: 기능 추가/변경, 버그 수정, 리팩터링, 데이터 변경, 외부 연동, 테스트/품질, 배포/운영.  
2) 영향 레이어를 추정한다: Domain, Application, Interface, Infrastructure.  
3) L0로 충분하면 추가 문서를 읽지 않는다.  
4) L0로 부족하면 아래 매핑에 따라 문서를 선택한다.  

## 작업 유형 → 문서 매핑(필수)
- 기능 추가/변경: `docs/project/scope.md`, `docs/specs/README.md`, 관련 기능 스펙  
- 버그 수정: 관련 기능 스펙, 필요 시 `docs/architecture/structure.md`  
- 리팩터링/구조 변경: `docs/architecture/overview.md`, `docs/architecture/structure.md`, 필요 시 `docs/architecture/decisions.md`  
- 데이터 변경: `docs/data/model.md`, 필요 시 `docs/integrations/external-services.md`  
- 외부 연동: `docs/integrations/external-services.md`, 필요 시 `docs/architecture/decisions.md`  
- 테스트/품질: `docs/dev/testing.md`  
- 배포/운영: `docs/ops/runbook.md`  

## 문서 작성/갱신 트리거(필수)
- 기능 요구가 불명확하다 → `docs/specs/feature-이름.md` 신규 작성  
- 구조 변경이 발생했다 → `docs/architecture/structure.md` 갱신  
- 중요한 선택/트레이드오프가 발생했다 → `docs/architecture/decisions.md` 기록  
- 외부 계약/스펙이 변경되었다 → `docs/integrations/external-services.md` 갱신  
- 데이터 모델이 바뀌었다 → `docs/data/model.md` 갱신  

## 즉시 업데이트(작업 중 필수)
- `docs/session/README.md` : 목표/다음 작업/리스크가 바뀔 때  
- `docs/architecture/decisions.md` : 되돌리기 어려운 결정이 생길 때  
- `docs/architecture/structure.md` : 구조/경계가 바뀔 때  
- `docs/project/scope.md` : 범위/제약이 바뀔 때  
- `docs/data/model.md` 또는 `docs/integrations/external-services.md` : 데이터/계약 변경 시  

## 세션 말 업데이트(종료 시)
- `docs/session/LOG.md` : 세션 요약 + 참조 문서 기록  
- `docs/specs/feature-*.md` : 기능 요구 확정/변경 시  
- `docs/dev/testing.md` : 테스트 전략/명령 변경 시  
- `docs/dev/environment.md` : 개발 환경/실행 방법 변경 시  
- `docs/ops/runbook.md` : 배포/운영 절차 변경 시  

## 세션 연속성 규칙
- 프로젝트 스냅샷/현재 상태는 `docs/session/README.md`가 기준이다.  
- 세션 로그는 `docs/session/LOG.md`가 기준이다.  
- 세션 시작 전에 상태를 확인하고, 종료 전에 반드시 갱신한다(없으면 "없음" 명시).  
- 세션 로그는 최신 항목을 상단에 둔다.  
- 세션 종료 시에는 사용자 요청 유무와 관계없이 `docs/session/END_PROMPT.md`를 읽고 그대로 수행한다.  

## 세션 문서 사용법(필수)
- 시작: `docs/session/README.md`를 읽고 절차를 따른다.  
- 현재 상태: 작업 시작 전 확인하고, 종료 전에 반드시 최신화한다.  
- 히스토리: 세션 종료 시 `docs/session/LOG.md`에 로그를 추가한다(최신 항목 상단).  

## Clean Architecture 기본 원칙
- 의존성은 항상 안쪽(도메인)으로만 향한다.  
- 도메인 규칙은 프레임워크/DB/외부 API에 의존하지 않는다.  
- 인터페이스(입력/출력)는 도메인/애플리케이션을 침범하지 않는다.  

## 기본 프로젝트 구조(고정 베이스라인)
- `src/domain/` : 엔티티, 값 객체, 도메인 서비스(외부 의존성 금지)  
- `src/application/usecases/` : 유스케이스  
- `src/application/ports/` : 인프라 의존 역전용 포트(인터페이스)  
- `src/interface/controllers/` : 입력 어댑터  
- `src/interface/presenters/` : 출력 어댑터  
- `src/interface/dto/` : 입출력 DTO  
- `src/infrastructure/` : DB/외부 API/메시징 등 구현 어댑터  
- `src/entrypoints/` : HTTP/CLI/Worker 진입점  
- `tests/unit/domain/` : 도메인 단위 테스트  
- `tests/unit/application/` : 애플리케이션 단위 테스트  
- `tests/integration/` : 통합 테스트  
- `docs/` : 문서  

## 구조 강제 장치(필수)
- 아키텍처 규칙 검증: `python3 scripts/check_arch.py`  
- 의존성 위반이 있으면 수정 후 진행한다(경고 무시 금지).  
- 구조 변경 시 `docs/architecture/structure.md`에 즉시 반영한다.  

## 문서 업데이트 규칙
- 구조/경계 변경: `docs/architecture/overview.md`, `docs/architecture/structure.md` 갱신  
- 요구사항/명세 변경: `docs/project/scope.md`, `docs/specs/` 갱신  
- 의사결정: `docs/architecture/decisions.md` 기록  
- 개발/운영 변경: `docs/dev/`, `docs/ops/` 갱신  
- 데이터/연동 변경: `docs/data/`, `docs/integrations/` 갱신  

## 세션 종료 체크리스트
1) `docs/session/README.md`와 `docs/session/LOG.md`를 갱신한다.  
2) 변경된 내용이 있으면 관련 문서를 업데이트한다.  
3) `docs/session/END_PROMPT.md`의 절차를 따른다.  
