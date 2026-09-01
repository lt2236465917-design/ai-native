# ai-native Repository Rules

## Scope

These rules apply to the entire `ai-native` repository. This repository contains one reusable, vendor-neutral Agent Skill package in the Agent Skills open format, with optional Codex packaging metadata; it is not an implementation of Anthropic's SDLC and must not be presented as an Anthropic product.

## Source Of Truth

- `SKILL.md` defines trigger scope, workflow, evidence labels, authorization boundaries, and output behavior.
- `SKILL.md` follows the Agent Skills format; `AGENTS.md` is a separate project-context convention used by this package, not a replacement for the Skill entrypoint.
- `references/anthropic-source-map.md` records the official-source boundary and publication metadata.
- `references/` contains detailed guidance loaded only when relevant.
- `templates/` contains reusable output templates; `templates/AGENTS.md` is a project template, not this repository's operating policy.
- `examples/` demonstrates Solo and Team usage.
- `tests/fixtures/` contains deliberate invalid cases used only to prove validators fail correctly.

## Editing Rules

- Preserve the positioning: the Skill is an implementation coach and orchestrator inspired by the Anthropic playbook, not the playbook itself.
- Keep `[OFFICIAL]`, `[ADAPTATION]`, `[LOCAL]`, and `[UNVERIFIED]` claims distinct.
- Use "Engineering Context" as the general concept and `AGENTS.md` as the default canonical file. Do not claim every runtime loads it automatically.
- Treat runtime support as `NOT_VERIFIED` until behavior is demonstrated with runtime evidence.
- Treat `SKILL.md` as the portable skill entrypoint. `agents/openai.yaml` is optional Codex UI/invocation metadata; other runtimes may ignore it.
- Keep Solo and Team paths usable. Enterprise support remains governance mapping unless the scope is explicitly expanded.
- Never add real credentials, private customer data, production logs, or proprietary repository content to examples or fixtures.
- Add scripts only for deterministic checks or repeated mechanical work; keep judgment and interaction rules in `SKILL.md` or references.

## Verification

Run the complete local validation before committing behavior or template changes. The `skill-creator` validator path below is a local Codex-maintainer convenience, not a runtime dependency for every host:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_self_test.py \
  --validator "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
```

Expected result: the positive cases pass, each negative fixture is detected as an expected failure, and the final line reports `PASS`.

Also inspect the staged diff and ensure generated caches, secrets, task state, and unrelated workspace files are not included.

## Installation And Release

- Codex personal local discovery in this workspace uses `$HOME/.agents/skills/ai-native`; this is a Codex-specific path, not a universal installation location. Other runtimes must follow their own skills directory or explicit configuration.
- Keep `/Users/zhuanzmima0000/Desktop/prd/ai-native` as the authoring source unless the owner explicitly changes it.
- Do not publish, change repository visibility, create releases, install plugins, deploy, commit, or push without explicit authorization for that action.
- Use concise English commit messages that describe intent.
