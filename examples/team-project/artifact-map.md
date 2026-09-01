# Artifact map (Team example)

| Artifact | Input | Owner | Reviewer/gate | Stored in |
|---|---|---|---|---|
| `intent.md` | idea, ticket, or incident | originator | product owner | `intent/` |
| `spec.md` | accepted intent | product/engineering pair | policy owners as needed | `decisions/` |
| `plan.md` | approved spec | implementation owner | engineering lead | `plans/` |
| code/tests | accepted plan | implementation owner | CI + PR reviewers | source tree |
| review record | PR/diff | reviewers | merge rule | PR + `reviews/` |
| incident record | alert or escaped defect | on-call owner | incident review | `incidents/` |
