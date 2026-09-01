---
artifact: artifact-map
status: draft
profile: Solo | Team
owner: ""
created_at: YYYY-MM-DD
---

# Artifact map: <project>

| Artifact | Required input | Owner | Reviewer/gate | Version-control location | Next trigger | Evidence |
|---|---|---|---|---|---|---|
| `intent.md` | idea/ticket/incident | <role> | product decision | <path> | accepted intent → design | <link> |
| `spec.md` | accepted intent | <role> | product/engineering/policy | <path> | approved spec → plan | <link> |
| `plan.md` | approved spec | <role> | engineering decision | <path> | accepted plan → build | <link> |
| code + tests | accepted plan | <role> | CI + PR review | <path> | merged PR → pipeline | <link> |
| review record | diff/PR | <role> | merge/release gate | <path> | finding resolution | <link> |
| incident record | alert/escaped defect | <role> | incident review | <path> | writeback intent | <link> |

## State and ID rules

- ID format:
- Allowed status transitions:
- Missing/unknown fields:
