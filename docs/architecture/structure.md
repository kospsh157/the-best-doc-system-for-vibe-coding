# 구조

## TL;DR (10줄 이내)
- 프로젝트는 Clean Architecture 레이어를 `src/`에 고정한다.  
- 레이어 의존성 규칙은 `scripts/check_arch.py`로 검증한다.  
- 구조/경계 변경 시 이 문서를 즉시 갱신한다.  

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시 또는 구조 변경/리팩터링 시.  
- 갱신: 폴더 구조/경계/계층 매핑이 바뀌었을 때.  

## 디렉터리 구조 (현재 기준)
- `src/domain/` : 도메인 규칙(엔티티, 값 객체, 도메인 서비스)
- `src/application/usecases/` : 유스케이스
- `src/application/ports/` : 포트(인터페이스 계약)
- `src/interface/controllers/` : 입력 어댑터
- `src/interface/presenters/` : 출력 어댑터
- `src/interface/dto/` : 입출력 DTO
- `src/infrastructure/` : 인프라 구현(DB, 외부 API, 메시징)
- `src/entrypoints/` : HTTP/CLI/Worker 진입점
- `tests/unit/domain/` : 도메인 단위 테스트
- `tests/unit/application/` : 애플리케이션 단위 테스트
- `tests/integration/` : 통합 테스트
- `docs/` : 문서

## 의존성 허용 규칙
- `domain` -> `domain`
- `application` -> `domain`, `application`
- `interface` -> `application`, `domain`, `interface`
- `infrastructure` -> `application`, `domain`, `infrastructure`
- `entrypoints` -> `application`, `domain`, `interface`, `entrypoints`

## 강제 장치
- 아키텍처 검사 명령: `python3 scripts/check_arch.py`
- 위반 발생 시 원인 파일을 수정하고 재실행한다.

## 경계 체크
- 도메인에서 외부 의존성 참조 금지  
- 인터페이스/인프라 구현은 포트 기반으로 연결  
