# Project AI Development Context

## Scope

This is a low-risk fixture for the `ai-native` Skill. It is not proof that a production runtime has loaded these instructions.

## Commands

- Artifact check: run the Skill's `validate_artifact_chain.py` against this directory.
- Context check: run `check_context_conflicts.py` against this directory.

## Source of truth

The five frontmatter artifacts and their IDs are the fixture source of truth.

## Working agreements

- Keep the artifact IDs and cross-references consistent.
- Report unknown runtime behavior as `NOT_VERIFIED`.
- Do not publish, deploy, or transmit fixture data.
