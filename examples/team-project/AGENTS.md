# Project AI Development Context

## Scope

This example models a Team profile at risk level R2. It is a fixture, not a production governance configuration.

## Source of truth

Accepted artifacts live in the repository and are linked from the PR. The product decision log remains authoritative for product policy.

## Working agreements

- The next stage reads the accepted artifact from version control.
- Each gate has a named owner and evidence link.
- Skill guidance is advisory; required checks belong in CI, branch protection, hooks or permissions.
- Unknown runtime loading behavior is reported as `NOT_VERIFIED`.
