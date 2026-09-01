---
artifact: intent
id: INT-20260831-001
status: accepted
author: "Solo owner"
owner: "Solo owner"
created_at: 2026-08-31
updated_at: 2026-08-31
revision: "1"
source: person
---

# Intent: make release notes reproducible

## Problem

Release notes are assembled manually after each small release and omissions are discovered during review.

## Proposed outcome

Generate a reviewable draft from merged changes while keeping the owner responsible for the final wording.

## Affected users and systems

- Users/roles: solo maintainer and users reading release notes
- Products/services: release repository
- Source of truth: merged PR titles and approved labels

## Constraints

- Product or scope constraints: draft only; no automatic publishing
- Security/privacy/compliance constraints: do not include secrets or private issue text
- Technical or operational constraints: must run from the repository checkout
- Explicitly out of scope: publishing to a store or external channel

## Success signals

- Signal and baseline: manual assembly takes about 20 minutes per release
- Target or decision rule: draft is ready for review in under 5 minutes
- Measurement owner: Solo owner

## Open questions

1. Which labels are considered user-visible? — owner: Solo owner — due/recheck: before pilot

## Human decision

- decision: accepted
- decision_owner: Solo owner
- decided_at: 2026-08-31
- evidence: local review note
- rationale: low-risk, reversible pilot

## Provenance

- source links or ticket IDs: local-pilot-001
- assumptions: none
- next artifact: `spec.md`
