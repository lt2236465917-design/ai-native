---
artifact: incident-record
id: INC-20260831-001
status: resolved
source: review
deploy_or_change_id: PR-fixture-001
owner: "Solo owner"
created_at: 2026-08-31
updated_at: 2026-08-31
revision: "1"
---

# Incident: an internal label appeared in a draft

## Impact and timeline

- Affected users/systems: fixture release-note draft
- First observed: 2026-08-31
- Detection source: review
- Current status: resolved
- Timeline/evidence links: local-pilot-001

## Containment and recovery

- Immediate mitigation: discard the draft and tighten the label allowlist
- Rollback or recovery evidence: no external publication occurred
- Residual risk: real repository labels are `NOT_VERIFIED`

## Root-cause classification

- product intent | spec/design | plan | implementation | test/eval | deploy | maintain/observability | external: test/eval
- explanation: fixture lacked a negative label case
- contributing factors: review checklist omitted exclusion test

## Writeback

- new_or_updated_intent_id: INT-20260831-001
- control/skill/hook/CI update needed: add exclusion fixture and review field
- owner and due/recheck: Solo owner / before next pilot
- recurrence check: run the negative fixture on each change

## Human decision

- decision: resolved
- decision_owner: Solo owner
- decided_at: 2026-08-31
- evidence: updated fixture result
