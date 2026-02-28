# Source Layout

This project uses a Clean Architecture-aligned source layout.

## Layers
- `domain`: Entities, value objects, and domain services.
- `application`: Use cases, orchestration, and ports.
- `interface`: Controllers, presenters, and DTO mapping.
- `infrastructure`: DB, external APIs, queues, and adapters.
- `entrypoints`: HTTP/CLI/job bootstrap code.

## Dependency Rule
- `domain` -> `domain`
- `application` -> `domain`, `application`
- `interface` -> `application`, `domain`, `interface`
- `infrastructure` -> `application`, `domain`, `infrastructure`
- `entrypoints` -> `application`, `domain`, `interface`, `entrypoints`

## Guardrail
- Run `python3 scripts/check_arch.py` before commit.
- Install hook once: `./scripts/install_git_hook.sh`
- `pre-commit` runs `python3 scripts/check_arch.py` automatically.
