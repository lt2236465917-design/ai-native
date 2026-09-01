# 验证与 forward-testing

本文件定义本 Skill 草稿的本地验证方法。它验证结构和可观察行为，不把 fixture 当成真实产品或生产能力证明。

## 本地静态检查

在 Skill 根目录执行：

> 下面的 `quick_validate.py` 是可选的 Skill 维护工具，不是 Agent Skills 的跨宿主运行依赖。将 `/path/to/skill-creator` 替换为目标环境中的实际路径；目标宿主没有该脚本时，跳过这一项并记录 `NOT_VERIFIED`。其余检查使用仓库自带脚本。

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/ai-native
python3 scripts/validate_artifact_chain.py --root templates --allow-placeholders
python3 scripts/check_context_conflicts.py --root examples
python3 scripts/check_runtime_adapter.py --root references
```

脚本失败时应显示具体文件、字段、行号或冲突项和修复方向；不能只返回“invalid”。

## Artifact 验收

至少检查：

- `intake.md` 记录目标、profile、runtime/version、权限、用户风险和人工风险决定；
- `intake.md` 在目标未提供时使用 `Target path: NOT_PROVIDED`，并保留 `Feature wording: PRESERVE_VERBATIM` 与 no-write boundary；
- `intent.md` 有唯一 ID、作者、状态、问题、期望结果、约束和开放问题；
- 每个 artifact 记录 `revision`/commit 和 `updated_at`，或明确由版本控制历史承担这两个字段；
- `spec.md` 引用已接受的 intent，记录需求、设计、风险、验证和人工批准；
- `plan.md` 引用 intent/spec，列出文件、顺序、风险、测试和批准；
- review record 引用变更/PR、发现、决策和 owner；
- incident record 引用影响、证据、缓解、根因、回写 intent 和复盘；
- incident record 若产生开发回写，能通过 ID 关联到 intent；
- 状态只能沿允许的转换前进，拒绝/暂停必须有理由；
- 状态转换历史可在版本控制或独立 state history 中追溯；没有历史证据时标为 `NOT_VERIFIED`，脚本不会替代人工审查；
- 所有链接、ID、版本和时间戳可追溯，缺失项明确为 `NOT_VERIFIED`。

## 上下文验收

- canonical `AGENTS.md` 与 adapter 不重复维护共享规则；
- 不含 token、密码、私钥、生产凭证或未脱敏个人数据；
- 命令能在目标项目中找到对应脚本或被标为 `NOT_VERIFIED`；
- 冲突规则被报告而不是静默覆盖；
- 运行时加载路径有实际验证命令或明确缺口。
- 若宣称 runtime 已加载，必须有 `runtime-evidence.md` 的命令、版本、日期和结果；否则保持 `NOT_VERIFIED`；
- 动作日志明确记录安装、commit、push、deploy 和外部通知是 skipped 还是已执行。

## 独立 forward-testing 协议

当 Skill 足够复杂时，使用隔离临时目录和独立代理：

1. 提供 Skill 目录、最小 fixture 和一个真实但低风险的请求；
2. 不提供预期答案、怀疑的 bug 或本轮设计结论；
3. 要求代理完成 intake、Play 选择、artifact 草案和权限说明；
4. 检查它是否先盘点、是否正确路由 references、是否区分官方与适配、是否在写入/外部动作前停下；
5. 审查实际产物和行为，只修复可由证据支持的问题；
6. 清理临时目录，确保 fixture 和测试输出不进入正式 Skill。

如果测试需要访问生产系统、发送外部消息、上传敏感资料或产生费用，先停止并取得单独授权；本 Skill 的默认 forward-test 不做这些动作。
