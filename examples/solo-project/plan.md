---
artifact: plan
id: PLAN-20260831-001
status: accepted
intent_id: INT-20260831-001
spec_id: SPEC-20260831-001
owner: "Solo owner"
created_at: 2026-08-31
updated_at: 2026-08-31
revision: "1"
approved_by: "Solo owner"
approved_at: 2026-08-31
---

# Plan: reproducible release-note draft

## Inputs

- intent_id and revision: INT-20260831-001 / local-pilot-001
- spec_id and revision: SPEC-20260831-001 / local-pilot-001
- repository/branch: fixture / main

## Files and interfaces that change

- `scripts/release_notes.py` — add deterministic draft generation
- `tests/test_release_notes.py` — cover grouping and exclusion

## Order of work

1. Parse the approved label allowlist.
2. Generate a draft from a fixed commit range.
3. Add tests and print source/evidence summary.

## Risks and alternatives

| Risk | Likelihood/impact | Detection | Mitigation or rollback | Owner |
|---|---|---|---|---|
| Private label leaks into draft | low/medium | fixture assertion | allowlist and manual review | Solo owner |

## Proof

- Commands/evals to run: `python3 -m pytest tests/test_release_notes.py`
- Expected healthy output: all tests pass and skipped entries are reported
- Product behavior or screenshot evidence: reviewed Markdown draft
- Neighboring flows to exercise: empty range and unknown label

## Human decision

- decision: accepted
- decision_owner: Solo owner
- decided_at: 2026-08-31
- evidence: local review note
- rationale: reversible low-risk pilot
- implementation authorization scope: fixture only; no publish/deploy

## Provenance

- generated_from: `intent.md` INT-20260831-001 and `spec.md` SPEC-20260831-001
- runtime/context versions: local-agent / AGENTS.md 2026-08-31
- assumptions: fixture commands are illustrative
