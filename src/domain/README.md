# Domain Layer

## Owns
- Business rules
- Entities and value objects
- Domain services

## Must Not Depend On
- `application`
- `interface`
- `infrastructure`
- `entrypoints`

## Notes
- Keep this layer framework-agnostic and IO-free.
