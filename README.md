# ai-native

`ai-native` is a reusable Codex Skill that helps Solo developers and software teams establish, pilot, verify, and iterate an AI-native software development lifecycle.

It is an implementation coach and orchestrator inspired by Anthropic's [The AI-Native SDLC playbook](https://www.claude.com/blog/the-ai-native-sdlc-playbook). It is not the Anthropic playbook itself and is not an Anthropic product.

## What It Helps With

- Assess the current development workflow and its evidence gaps.
- Select the smallest useful Play across Plan, Design, Build, Test, Deploy, and Maintain.
- Establish a committed artifact chain from intent through review and incident learning.
- Build a canonical Engineering Context around `AGENTS.md` with runtime-specific adapters.
- Separate advisory Skill behavior from deterministic hooks, CI, permissions, and human approvals.
- Design a measurable pilot for either a Solo or Team adoption profile.

The first version covers Solo and Team workflows. Enterprise support is limited to risk and governance mapping rather than managed-platform integration.

## Repository Layout

```text
ai-native/
|-- SKILL.md                 # Skill entry point and behavior contract
|-- agents/openai.yaml       # Codex UI metadata and invocation policy
|-- references/              # Source map and detailed implementation guidance
|-- templates/               # Adoption and committed-artifact templates
|-- examples/                # Solo and Team examples
|-- scripts/                 # Deterministic validators and self-test
`-- tests/fixtures/          # Deliberately invalid negative cases
```

## Personal Installation

Place the repository at:

```text
$HOME/.agents/skills/ai-native
```

Codex should detect the Skill automatically. If it does not appear, restart Codex. Invoke it explicitly with `$ai-native`, for example:

```text
Use $ai-native to assess this repository and propose the smallest Solo adoption pilot. Start read-only and label anything not verified.
```

Installation only makes the workflow discoverable. It does not authorize the Skill to modify repositories, commit, push, deploy, or call external systems.

## Validation

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_self_test.py \
  --validator "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
```

The self-test verifies the Skill structure, committed-artifact links, context conflicts, runtime adapters, internal references, and expected negative fixtures.

## Evidence Boundary

The Skill labels claims as:

- `[OFFICIAL]`: directly supported by the cited Anthropic source.
- `[ADAPTATION]`: cross-agent workflow or template designed by this project.
- `[LOCAL]`: a decision confirmed for the adopting project or organization.
- `[UNVERIFIED]`: a capability or integration without runtime evidence.

See [`references/anthropic-source-map.md`](references/anthropic-source-map.md) for the source boundary and [`references/runtime-adapters.md`](references/runtime-adapters.md) for runtime-specific context loading.
