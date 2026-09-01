---
artifact: plan
id: PLAN-YYYYMMDD-###
status: draft
intent_id: INT-YYYYMMDD-###
spec_id: SPEC-YYYYMMDD-###
owner: ""
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
revision: "1 or VCS commit"
approved_by: ""
approved_at: ""
---

# Plan: <outcome>

## Inputs

- intent_id and revision:
- spec_id and revision:
- repository/branch:

## Files and interfaces that change

- `<path>` — <reason and expected behavior>

## Order of work

1. <small, reversible step>
2. <small, reversible step>
3. <integration step>

## Risks and alternatives

| Risk | Likelihood/impact | Detection | Mitigation or rollback | Owner |
|---|---|---|---|---|
| <risk> | <rating> | <signal> | <action> | <role> |

## Proof

- Commands/evals to run:
- Expected healthy output:
- Product behavior or screenshot evidence:
- Neighboring flows to exercise:

## Human decision

- decision: pending | accepted | rejected | deferred
- decision_owner:
- decided_at:
- evidence:
- rationale:
- implementation authorization scope:

## Provenance

- generated_from: `intent.md` and `spec.md` IDs/revisions
- runtime/context versions:
- assumptions: `UNVERIFIED` items only
