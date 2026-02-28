# 테스트 전략

## TL;DR (10줄 이내)
- 테스트 범위와 실행 방법을 요약한다.  

## 사용
- 레벨: L2 (작업 영역별)  
- 읽기: 테스트 작성/수정, 실패 원인 분석, 품질 기준 확인 시.  
- 갱신: 테스트 전략/범위/명령/도구가 바뀌었을 때.  
## 테스트 레벨
- 단위 테스트: `tests/unit/domain`, `tests/unit/application`  
- 통합 테스트: `tests/integration`  
- E2E 테스트: 필요 시 `tests/e2e` 추가  

## 실행 방법
- 아키텍처 경계 검사: `python3 scripts/check_arch.py`
- 문서 품질 검사: `python3 scripts/check_docs.py`
- 문서 토큰 계산: `python3 scripts/doc_tokens.py`
- 토큰 가드 확인: `python3 scripts/doc_token_guard.py`
- pre-commit 훅 설치(권장): `./scripts/install_git_hook.sh`

## 기준
- 레이어 의존성 위반 0건  
- 도메인/유스케이스 변경 시 단위 테스트 추가  
