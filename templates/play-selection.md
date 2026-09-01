---
artifact: play-selection
status: draft
profile: Solo | Team
owner: ""
created_at: YYYY-MM-DD
---

# Play selection: <project>

| Play | Prerequisites | State | Why now/why later | Input | Output | Gate owner |
|---|---|---|---|---|---|---|
| Plan | <conditions> | ready/partial/missing/unknown | <reason> | idea/ticket/incident | `intent.md` | <role> |
| Design | <conditions> | ready/partial/missing/unknown | <reason> | `intent.md` | `spec.md` | <role> |
| Build | <conditions> | ready/partial/missing/unknown | <reason> | `spec.md` | `plan.md` + diff | <role> |
| Test | <conditions> | ready/partial/missing/unknown | <reason> | build/eval | test record | <role> |
| Deploy | <conditions> | ready/partial/missing/unknown | <reason> | accepted PR | release record | <role> |
| Maintain | <conditions> | ready/partial/missing/unknown | <reason> | telemetry/alert | incident/writeback | <role> |

## Adoption order

1. <Play with satisfied prerequisites>
2. <Play after the first gate>

## Stop or revisit conditions

- <condition that pauses the pilot>
