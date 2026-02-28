# Infrastructure Layer

## Owns
- External API clients
- DB repositories
- Queue/event broker implementations

## Allowed Dependencies
- `application` (ports/contracts)
- `domain`
- `infrastructure`

## Must Not Depend On
- `interface`
- `entrypoints`
