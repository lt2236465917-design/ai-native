---
artifact: pilot-checklist
status: draft
profile: Solo | Team
risk: R0 | R1 | R2 | R3
owner: ""
created_at: YYYY-MM-DD
---

# Pilot checklist: <project>

## Before start

- [ ] Scope and risk are recorded.
- [ ] Play prerequisites are `met` or have an owner and mitigation.
- [ ] Artifact home and reviewers are known.
- [ ] Runtime loading behavior is verified or marked `NOT_VERIFIED`.
- [ ] Rollback and stop conditions are written.

## During pilot

- [ ] Accepted `intent.md`, `spec.md` and `plan.md` are versioned.
- [ ] Agent output is reviewed at the declared human gates.
- [ ] Deterministic checks run at the declared layer.
- [ ] Actual commands, outputs and skipped checks are recorded.

## After pilot

- [ ] Review findings and rework are classified.
- [ ] Deployment/incident evidence is recorded if applicable.
- [ ] Baseline and after metrics are compared.
- [ ] Decision: continue | adjust | pause | rollback.
- [ ] Stable learnings are considered for `AGENTS.md` or a Skill update.
