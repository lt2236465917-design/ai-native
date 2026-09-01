# 工程上下文与运行时适配

本文件定义 `[ADAPTATION]` 方案：共享内容只维护一份，运行时专属入口只做薄适配。不要因为文件名存在就宣称某个 Agent 已经加载了上下文。

Agent Skills 的标准入口是 `SKILL.md`（规范：<https://agentskills.io/specification>）；`AGENTS.md` 是本 Skill 采用的工程上下文/指令文件约定。两者解决不同问题，不能互相替代，也不能仅凭文件名推断宿主行为。

参考入口（实际能力仍需按 runtime/version/surface 验证）：

- `AGENTS.md` 项目上下文文件说明：<https://agents.md/>
- Claude Code context 文档：<https://code.claude.com/docs/en/memory>
- Gemini CLI context 文件配置：<https://geminicli.com/docs/cli/gemini-md/>
- 本 Skill 的证据模板：`../templates/runtime-evidence.md`

## Canonical 结构

```text
project/
├── AGENTS.md                         # 共享、vendor-neutral canonical 内容
├── CLAUDE.md                         # 仅在 Claude Code 需要时的薄 adapter
├── .gemini/settings.json             # 可选：把 context.fileName 指向 AGENTS.md
├── .github/copilot-instructions.md   # 仅在目标 Copilot surface 需要时
└── .cursor/rules/                    # 路径专属或 Cursor 专属规则
```

原则：

- `AGENTS.md` 放项目概览、结构、命令、稳定约定、source of truth、验证和风险提示；
- 不把一次性任务、长流程、运行日志、秘密或个人偏好放入共享文件；
- runtime-specific 命令和模式放 adapter；
- 只有一份共享真相，避免复制后漂移；
- 子目录规则只在确实有范围差异时添加，并记录最近层级的优先级。

## 能力矩阵模板

每个项目应填写实际版本和验证证据，而不是套用下表的默认值。模型/API 提供方（如 DeepSeek、Kimi）本身不负责 Skill 发现；下表的 runtime/host 行描述的是承载和加载 Skill 的宿主层：

| Runtime / surface | 默认发现 `AGENTS.md` | 显式配置方式 | adapter | 已验证证据 |
|---|---:|---|---|---|
| Codex | 依 surface / version | 项目配置或 fallback 文件名 | 通常不需要 | 命令、上下文输出或文档链接 |
| Claude Code | `not by default` | `CLAUDE.md` 的 `@AGENTS.md` 或 symlink | `CLAUDE.md` | `/context` 或实际会话记录 |
| Gemini CLI | 依版本/配置 | `context.fileName` | `GEMINI.md` 或 settings | 实际配置与启动输出 |
| GitHub Copilot | 依 surface | 仓库/IDE/CLI 对应配置 | `copilot-instructions.md` 等 | 目标 surface 文档和运行验证 |
| 其他 Agent | `unknown` | 该 runtime 的 context/instructions 配置 | 按需 | 运行态证据 |
| 模型/API 提供方（DeepSeek、Kimi） | 不适用 | 由具体兼容 Agent/harness 显式加载 `SKILL.md` | 无统一 adapter | 宿主级运行态证据 |

`met`、`not by default` 和 `unknown` 是状态，不是能力承诺。对 GitHub Copilot 等产品要按 GitHub.com、IDE、CLI、review 等 surface 分开记录。

## Claude Code adapter

Claude Code 官方文档：<https://code.claude.com/docs/en/memory>。

推荐跨平台写法：

```md
@AGENTS.md

## Claude Code-specific guidance

- 只放确实属于 Claude Code 的模式、命令或限制。
```

如果完全没有 Claude 专属内容，也可以使用 symlink：

```bash
ln -s AGENTS.md CLAUDE.md
```

Windows 团队优先使用 `@AGENTS.md` 导入，因为创建 symlink 可能需要管理员权限或 Developer Mode。无论哪种方式，都要在目标会话中运行 `/context` 或等价检查，确认加载了预期文件。

## 迁移流程

1. 只读盘点全目录树的 `AGENTS*.md`、`CLAUDE*.md`、`GEMINI.md`、`.cursor/rules/`、Copilot instructions 和其他 runtime 配置。
2. 为每个文件标记 scope、owner、更新时间、是否共享、是否含秘密、是否存在冲突。
3. 把稳定且 vendor-neutral 的内容合并到根 `AGENTS.md`；保留个人/本地文件并加入 gitignore。
4. 为实际使用的 runtime 创建薄 adapter 或显式配置；不要同时加载两份内容相同的 canonical 文件。
5. 将路径专属规则留在最近目录或该 runtime 的规则目录；解释覆盖关系。
6. 先在隔离分支或临时目录运行加载验证，再由负责人批准迁移到目标仓库。
7. 记录迁移前后差异、未解决冲突和回滚方式。

## 冲突处理

- 用户当前请求优先于项目上下文；安全/权限约束优先于建议性文字；
- 同一 runtime 的更近目录规则通常更具体，但不同 runtime 的合并顺序不能互相推断；
- 规则冲突时标为 `PENDING_DECISION`，列出两条原文和影响；
- 不用 symlink、import 或文件名存在替代实际加载验证；
- 不把 adapter 中的 runtime 专属内容写回 `AGENTS.md`，除非团队明确决定它已成为共享事实。

## 大小和维护

保持根文件短、稳定、可验证。详细流程放 Skill 或 reference；会频繁变化的值放配置/脚本或 source of truth。每次修复一个重复错误后，先判断它是否是稳定的团队规则，再决定是否写入 `AGENTS.md`。
