---
artifact: spec
id: SPEC-20260831-001
status: approved
intent_id: INT-20260831-001
owner: "Solo owner"
authoring_runtime: "local-agent"
created_at: 2026-08-31
updated_at: 2026-08-31
revision: "1"
approved_by: "Solo owner"
approved_at: 2026-08-31
---

# Spec: reproducible release-note draft

## Intent reference

- intent_id: INT-20260831-001
- intent_revision/commit: local-pilot-001
- accepted_intent_evidence: local review note

## Requirements

### Functional requirements

1. FR-001: collect merged changes since the previous release marker.
2. FR-002: group changes by approved user-visible label.
3. FR-003: write a draft file and never publish it automatically.

### Non-functional requirements

- Performance/reliability: complete on a normal checkout in under 5 minutes
- Accessibility/UX: draft headings are readable in Markdown
- Security/privacy: exclude credentials and private issue bodies
- Observability: report source commit range and skipped entries

## Design

- User and system flows: command → inspect commits → draft → human edit → optional commit
- Data model/API/events: local git log and labels only
- Source of truth: merged PR metadata
- Alternatives considered and why rejected: manual spreadsheet rejected as non-reproducible

## Risks and policy concerns

| Risk or conflict | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|
| A label may expose internal detail | medium | allowlist labels and review draft | Solo owner | open |

## Verification plan

- Acceptance examples: known commit range produces expected sections
- Unit/integration/eval checks: fixture test for grouping and exclusion
- Manual or visual checks: owner reviews the generated Markdown
- Required healthy output: source range and skipped-entry count are printed

## Human decision

- decision: approved
- decision_owner: Solo owner
- consulted_policy_owners: none
- decided_at: 2026-08-31
- evidence: local review note
- unresolved_questions: label allowlist
- next artifact: `plan.md`

## Provenance

- generated_from: `intent.md` INT-20260831-001 revision local-pilot-001
- skills/policies applied and versions: ai-native draft 0.1
- assumptions: local repository only
