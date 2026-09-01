# ai-native

A vendor-neutral Agent Skill and implementation kit for adopting an AI-native SDLC with compatible coding agents.

[中文](#中文) · [English](#english)

## 中文

`ai-native` 是一套遵循 [Agent Skills 开放格式](https://agentskills.io/specification)、面向兼容 coding agent 的 AI-native SDLC 实施工具包，帮助个人开发者和团队把 Anthropic《[The AI-Native SDLC playbook](https://www.claude.com/blog/the-ai-native-sdlc-playbook)》中的思路落到自己的项目里。

核心内容不绑定 Codex、Claude、DeepSeek 或 Kimi。它更像一位实施教练：先了解现状，再选择最小可行的改造，最后用证据验证效果。

它不是 Anthropic 官方产品，也不是让 Skill 代替整套开发体系。核心文档和模板可跨宿主复用；仓库自带脚本要在满足 Python、权限等运行条件时使用，是否能自动发现、调用工具或执行脚本，由具体 Agent 宿主和配置决定。

### 它能帮你做什么

- 盘点 Plan、Design、Build、Test、Deploy、Maintain，找出真正的瓶颈。
- 从 1–3 个最值得尝试的 Play 开始，不要求一次改造全部流程。
- 建立从需求意图、规格、计划、代码和测试，到评审、事故复盘的可追踪产物链。
- 用 `AGENTS.md` 建立共享的工程上下文，并为不同 Agent runtime 设计适配方式。
- 分清 AI 建议、人工审批、CI、hooks 和权限控制各自负责什么。
- 为 Solo 开发者或 Team 设计有指标、审批点、回滚和复盘的试点。

### 可以在哪些工具里使用

| 使用方式 | 当前边界 |
| --- | --- |
| Agent Skills-compatible 宿主 | 按宿主的目录、版本和配置接入 `SKILL.md`；常见实现包括 Claude Code、Codex、Gemini CLI、GitHub Copilot/VS Code、Cursor、OpenCode 等，但本仓库未逐一验证其运行态。 |
| Codex | 本仓库提供可选的 Codex 打包适配器；安装后使用 `$ai-native`。这是 Codex 调用语法，不是通用命令。 |
| Claude Code | 支持标准 `SKILL.md`；可放入 `~/.claude/skills/ai-native/` 或项目的 `.claude/skills/ai-native/`，使用 `/ai-native`。目标会话仍应自行验证加载结果。 |
| DeepSeek / Kimi | 在宿主提供相应接入时，[DeepSeek API](https://api-docs.deepseek.com/) 和 [Kimi API](https://platform.kimi.com/docs/overview) 可作为 coding agent 的模型后端；[Kimi Code](https://www.kimi.com/code) 等具体产品属于宿主，是否支持或自动发现 Agent Skill 需按产品、版本和配置验证。本项目不宣称这些模型或产品已原生自动发现本 Skill。 |
| 其他模型或 Agent | 可显式提供 Markdown 核心内容；工具调用、脚本执行和自动加载在有实际 runtime 证据前均为 `NOT_VERIFIED`。 |

“模型”和“宿主”是两层：在聊天窗口里粘贴 Markdown，不等于宿主已经安装、自动发现并执行 Skill。

仓库里仍有 `agents/openai.yaml`，只是为了保留 Codex 的界面和调用适配；跨平台核心是 `SKILL.md`、参考资料、模板和仓库脚本，其他宿主可以忽略这个文件。

第一版覆盖 Solo 和 Team。Enterprise 目前只提供风险与治理映射，不包含托管平台集成。

### 安装与开始使用

在 Codex 中：

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.agents/skills/ai-native"
```

然后使用：

```text
使用 $ai-native 评估这个仓库，给我一个最小的 Team 试点方案。先只读盘点，并标记所有尚未验证的能力。
```

在 Claude Code 中，可将同一仓库克隆到个人 Skill 目录：

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.claude/skills/ai-native"
```

然后使用 `/ai-native`。其他宿主请按照其 Agent Skills 或自定义指令文档加载同一份 `SKILL.md`；不要假设 `$ai-native`、`/ai-native` 或任何自动发现行为在其他宿主中通用。

安装只负责让内容可被发现或读取，不代表授权它修改代码、commit、push、部署或调用外部系统。

### 证据边界

Skill 会区分官方来源、项目设计、你确认的本地决策，以及尚未有运行证据的能力。不要把“模型能读 Markdown”写成“宿主已经自动加载并执行”。需要深入了解时，可查看 [`SKILL.md`](SKILL.md)、[`references/runtime-adapters.md`](references/runtime-adapters.md) 和 [`references/`](references/)。

## English

`ai-native` is a vendor-neutral Agent Skill and implementation kit that follows the [Agent Skills open format](https://agentskills.io/specification). It helps individuals and teams turn the ideas in Anthropic's [The AI-Native SDLC playbook](https://www.claude.com/blog/the-ai-native-sdlc-playbook) into a workflow that fits their project.

The core content is not tied to Codex, Claude, DeepSeek, or Kimi. Think of it as an implementation coach: understand the current state, choose the smallest useful change, and verify the result with evidence.

It is not an Anthropic product, and it is not the development system itself. The core documentation and templates can be reused across hosts; the bundled scripts require their runtime prerequisites (such as Python and permissions), and automatic discovery, tool access, or execution depends on the host agent and its configuration.

### What it helps you do

- Assess Plan, Design, Build, Test, Deploy, and Maintain to find the real bottlenecks.
- Start with the 1–3 most useful Plays instead of redesigning everything at once.
- Create a traceable artifact chain from intent, specs, plans, code, and tests through review and incident learning.
- Establish shared Engineering Context in `AGENTS.md`, with adapters for different Agent runtimes.
- Clarify the roles of AI advice, human approval, CI, hooks, and permissions.
- Design a measurable Solo or Team pilot with metrics, approval points, rollback, and retrospectives.

### Where it can be used

| Usage | Current boundary |
| --- | --- |
| Agent Skills-compatible hosts | Load `SKILL.md` according to the host's directory, version, and configuration. Examples include Claude Code, Codex, Gemini CLI, GitHub Copilot/VS Code, Cursor, and OpenCode; this repository has not runtime-tested each one. |
| Codex | This repository includes an optional Codex packaging adapter; invoke it with `$ai-native` after installation. That syntax is Codex-specific. |
| Claude Code | Supports standard `SKILL.md`; place it in `~/.claude/skills/ai-native/` or a project's `.claude/skills/ai-native/`, then use `/ai-native`. Verify loading in the target session. |
| DeepSeek / Kimi | When a host provides the relevant integration, [DeepSeek API](https://api-docs.deepseek.com/) and [Kimi API](https://platform.kimi.com/docs/overview) can provide the model backend for a coding agent; products such as [Kimi Code](https://www.kimi.com/code) are hosts whose Skill support and discovery must be checked by product, version, and configuration. This project does not claim that these models or products natively discover this Skill. |
| Other models or agents | They can be given the Markdown core explicitly; tool access, script execution, and automatic loading remain `NOT_VERIFIED` until tested in the actual runtime. |

“Model” and “host” are different layers: pasting Markdown into a chat does not mean the host installed, discovered, or executed the Skill.

The repository still contains `agents/openai.yaml` only for the Codex UI and invocation adapter. The cross-host core is `SKILL.md`, the references, templates, and bundled scripts; other hosts can ignore that file.

The first version covers Solo and Team workflows. Enterprise support is currently limited to risk and governance mapping; it does not include managed-platform integration.

### Install and get started

For Codex:

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.agents/skills/ai-native"
```

Then use:

```text
Use $ai-native to assess this repository and propose the smallest Team adoption pilot. Start read-only and label anything not verified.
```

For Claude Code, clone the same repository into its personal skills directory:

```bash
git clone https://github.com/lt2236465917-design/ai-native.git \
  "$HOME/.claude/skills/ai-native"
```

Then use `/ai-native`. For other hosts, follow their Agent Skills or custom-instructions documentation and load the same `SKILL.md`; do not assume `$ai-native`, `/ai-native`, or automatic discovery is portable across hosts.

Installation makes the content discoverable or readable; it does not authorize repository edits, commits, pushes, deployments, or external-system calls.

### Evidence boundary

The Skill distinguishes official source claims, project-designed adaptations, decisions confirmed for your project, and capabilities without runtime evidence. Do not turn “the model can read Markdown” into a claim that a host has automatically loaded and executed the Skill. For details, see [`SKILL.md`](SKILL.md), [`references/runtime-adapters.md`](references/runtime-adapters.md), and [`references/`](references/).
