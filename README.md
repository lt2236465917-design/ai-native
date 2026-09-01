# ai-native

Build a practical AI-native software development workflow for a person or a team.

[中文](#中文) · [English](#english)

## 中文

`ai-native` 是一个 Codex Skill，帮助你把 Anthropic《[The AI-Native SDLC playbook](https://www.claude.com/blog/the-ai-native-sdlc-playbook)》中的思路，变成适合自己项目的开发方式。

它不是 Anthropic 官方产品，也不是让 Skill 代替整套开发体系；它更像一位实施教练：先了解现状，再选择最小可行的改造，最后用证据验证效果。

### 它能帮你做什么

- 盘点 Plan、Design、Build、Test、Deploy、Maintain，找出真正的瓶颈。
- 从 1–3 个最值得尝试的 Play 开始，不要求一次改造全部流程。
- 建立从需求意图、规格、计划、代码和测试，到评审、事故复盘的可追踪产物链。
- 用 `AGENTS.md` 建立共享的工程上下文，并为不同 Agent runtime 设计适配方式。
- 分清 AI 建议、人工审批、CI、hooks 和权限控制各自负责什么。
- 为 Solo 开发者或 Team 设计有指标、审批点、回滚和复盘的试点。

### 适合谁

- 想系统使用 AI，而不是只让 AI 零散写代码的个人开发者。
- 希望团队形成可重复、可审查、可持续改进的 AI 开发流程的负责人。
- 需要先做小范围试点，再决定是否扩大投入的组织。

第一版覆盖 Solo 和 Team。Enterprise 目前只提供风险与治理映射，不包含托管平台集成。

### 安装与开始使用

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.agents/skills/ai-native"
```

Codex 通常会自动发现它；如果没有出现，请重启 Codex。然后直接告诉 Codex 你的目标，例如：

```text
使用 $ai-native 评估这个仓库，给我一个最小的 Team 试点方案。先只读盘点，并标记所有尚未验证的能力。
```

安装只负责让 Skill 可被发现，不代表授权它修改代码、commit、push、部署或调用外部系统。

### 证据边界

Skill 会区分官方来源、项目设计、你确认的本地决策，以及尚未有运行证据的能力。需要深入了解时，可查看 [`SKILL.md`](SKILL.md) 和 [`references/`](references/)。

## English

`ai-native` is a Codex Skill that helps you turn the ideas in Anthropic's [The AI-Native SDLC playbook](https://www.claude.com/blog/the-ai-native-sdlc-playbook) into a development workflow that fits your project.

It is not an Anthropic product, and it is not the development system itself. Think of it as an implementation coach: understand the current state, choose the smallest useful change, and verify the result with evidence.

### What it helps you do

- Assess Plan, Design, Build, Test, Deploy, and Maintain to find the real bottlenecks.
- Start with the 1–3 most useful Plays instead of redesigning everything at once.
- Create a traceable artifact chain from intent, specs, plans, code, and tests through review and incident learning.
- Establish shared Engineering Context in `AGENTS.md`, with adapters for different Agent runtimes.
- Clarify the roles of AI advice, human approval, CI, hooks, and permissions.
- Design a measurable Solo or Team pilot with metrics, approval points, rollback, and retrospectives.

The first version covers Solo and Team workflows. Enterprise support is currently limited to risk and governance mapping; it does not include managed-platform integration.

### Install and get started

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.agents/skills/ai-native"
```

Codex should discover the Skill automatically. If it does not appear, restart Codex. Then describe your goal, for example:

```text
Use $ai-native to assess this repository and propose the smallest Team adoption pilot. Start read-only and label anything not verified.
```

Installation makes the Skill discoverable; it does not authorize repository edits, commits, pushes, deployments, or external-system calls.

### Evidence boundary

The Skill distinguishes official source claims, project-designed adaptations, decisions confirmed for your project, and capabilities without runtime evidence. For details, see [`SKILL.md`](SKILL.md) and [`references/`](references/).
