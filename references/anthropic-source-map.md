# Anthropic 来源映射与事实边界

> 本文件是 `[OFFICIAL]` 与 `[ADAPTATION]` 的分界，不是 Anthropic 原文的复制品。

本轮来源状态：`verified`（2026-08-31；页面正文、JSON-LD 和 HTTPS HTML 元数据分别读取）。这只证明本轮读取到了这些字段，不保证未来页面内容不变。

## 来源记录

- `[OFFICIAL]` Canonical：<https://www.claude.com/blog/the-ai-native-sdlc-playbook>
  - 页面标题：The AI-Native SDLC playbook
  - 作者：Louis Claxton
  - 内容日期：2026-08-21（页面显示为 August 21, 2026；JSON-LD `datePublished`）
  - JSON-LD `dateModified`：2026-08-26
  - 页面定位：Anthropic Applied AI 团队实践和客户工作启发的 playbook
  - Webflow HTML `Last Published` 元数据：2026-08-27 18:42:05 UTC；这是站点发布元数据，不替代页面内容日期
  - 本轮核对：2026-08-31，通过 Codex in-app browser 和 HTTPS HTML 只读读取；日期字段按上述来源分别记录
- `[SECONDARY]` 中文辅助：<https://www.woshipm.com/ai/6454739.html>
  - 页面明确写为“编译自”官方博客，不能替代 canonical source。
  - 本轮核对：2026-08-31，通过 Codex in-app browser 读取页面正文
- `[ADAPTATION]` 本 Skill：跨 Agent 的实施流程、文件名适配、Solo/Team profile、脚本和验收规则。

## 模型供应商与宿主边界

- `[OFFICIAL]` DeepSeek API 文档说明其 API 可作为 Claude Code、GitHub Copilot、OpenCode 等 coding assistant 的后端：<https://api-docs.deepseek.com/>。这只能证明模型/API 与宿主是不同层，不证明 DeepSeek 模型会自动发现本 Skill。
- `[OFFICIAL]` Kimi 平台文档分别列出 Kimi Code CLI、Codex、Claude Code 和 OpenCode 的接入方式：<https://platform.kimi.com/docs/overview>。`Kimi Code` 等是具体宿主或 Agent 产品；是否支持 Agent Skills 和自动发现本仓库，仍需按产品、版本和配置验证。
- `[UNVERIFIED]` 本仓库尚未在 DeepSeek Harness、Kimi Code 或其他使用这些模型的 runtime 中完成 `ai-native` 的加载与行为验证；对外说明保持 `NOT_VERIFIED`。

## 可以直接归因于官方原文的内容

| 主题 | 官方事实摘要 | 使用边界 |
|---|---|---|
| 瓶颈迁移 | 当 Agent 加速 Build 后，Plan、Review/Test、Deploy 等人速环节可能成为瓶颈 | 不得据此断言所有组织都已达到该状态 |
| 六个阶段 | Plan、Design、Build、Test、Deploy、Maintain | 是 play 分组，不是强制线性流水线 |
| 非线性采用 | Play 之间有 prerequisites，采用顺序与阶段名称不是同一件事 | 具体项目的依赖要重新核对 |
| committed artifact | `intent.md`、`spec.md`、`plan.md`、代码与测试、PR/review findings、incident record 构成可追溯链 | 文件名可按组织调整，但不能丢失状态、责任和审计关系 |
| 人的责任 | 需要判断力的决策仍由人负责 | 不等于每一行代码都必须人工审查 |
| 工程上下文来源 | 原文用 `CLAUDE.md` 描述命令、架构、约定和常见错误等持续上下文 | 本 Skill 的 `AGENTS.md` 是跨 Agent 适配，不是 Anthropic 改名公告 |
| Skill 与治理 | Skill 是 advisory control；必须始终成立的策略需要 hook、review、CI 或其他确定性层 | Skill 本身不能作为合规证明 |
| 反馈回路 | 生产控制带被突破时，应诊断并写回新的 intent，继续循环 | 组织必须先有可用 telemetry、owner 和回写路径 |

## 本 Skill 的适配声明

以下内容不是 Anthropic 原文的原名或官方承诺，必须标 `[ADAPTATION]`：

- `ai-native` Skill 的名称、目录结构和交互协议；
- “工程上下文（Engineering Context）”这一通用概念名；
- 用 `AGENTS.md` 作为共享 canonical 文件；
- `CLAUDE.md`、`GEMINI.md` 或其他 runtime adapter 的生成策略；
- Solo/Team 风险 profile、R0–R3 分级和本地验收脚本；
- Adoption Pack 的文件名和本 Skill 的默认权限边界。

## 事实更新规则

1. 需要引用官方观点时，先打开 canonical 页面并核对页面日期/正文；不要只依赖本文件的旧摘录。
2. 如果官方页面改名、移动、删除或改变六阶段/产物链描述，把旧说法标记为 `[STALE]`，并在本文件记录检查日期。
3. 中文编译文章中的新增例子、行业评论和结构重排只能标 `[SECONDARY]` 或 `[ADAPTATION]`。
4. 不要把“使用 Claude”替换成“任何模型都能自动完成”；应说明实际 runtime、版本、配置和验证证据。
5. 当用户的组织规则与官方建议冲突时，报告冲突并让用户决定；本 Skill 不代表 Anthropic 解决组织政策。

## 推荐的通用措辞

将“给 AI 写新人入职手册（`CLAUDE.md`）”改写为：

> 为代码 Agent 建立项目工程上下文与工作约定（`AGENTS.md`）。

并补充：

> `AGENTS.md` 是本 Skill 选择的跨 Agent canonical 命名；不同 runtime 可能需要显式配置或适配器。Claude Code 仍读取 `CLAUDE.md`，可通过 `@AGENTS.md` 或 symlink 共享同一份内容。
