# 治理控制分层

本文件把“让 Agent 更可能遵守”与“无条件阻止违规”分开。每一条规则都要有 owner、执行层、证据和例外路径。

## 控制矩阵

| 控制目标 | Advisory 层（Skill / `AGENTS.md`） | Deterministic 层 | Owner | 证据 | 例外路径 |
|---|---|---|---|---|---|
| 使用正确的构建/测试命令 | 上下文列出命令和健康输出 | CI job / required check | 工程负责人 | CI log、commit status | 记录批准的 skip 和原因 |
| 禁止编辑生成文件 | Skill 提醒路径规则 | pre-edit hook、CI diff check、权限 | 平台/模块 owner | hook result、PR check | 临时解锁审批 |
| 凭证不进入 diff | Skill 提醒脱敏 | secret scanner、push protection、权限 | 安全负责人 | scanner report | 安全负责人复核误报 |
| 高风险部署需授权 | Skill 生成 release checklist | deploy gate、managed settings、RBAC | 发布负责人 | release authorization、audit log | 命名责任人和时限 |
| API 变更遵守策略 | secure-review Skill / context | lint、schema check、PR required review | API owner | check output、review finding | 记录风险接受者 |
| 事故回写开发循环 | Maintain Skill 提示模板 | 告警、值班系统、incident workflow | 运维负责人 | incident record、new intent | 记录关闭/误报理由 |

## 设计规则

1. Skill 和 `AGENTS.md` 只能作为建议性上下文；不能写“保证”“绝不”来掩盖没有确定性执行层的事实。
2. 必须始终成立的策略至少要有一个独立于模型服从的阻断或复核点。
3. Hook 要快速、范围明确；完整测试和昂贵检查通常放在 commit/PR/CI，而不是每次工具调用。
4. 强制层应由适当 owner 管理，个人 Agent 会话不能单独关闭组织级控制。
5. 阻断消息要说明原因、证据和申请例外的路径；不要只返回无上下文的失败码。
6. 每项控制记录版本、最后验证时间和失效信号；策略变化时同时更新 advisory 文档和 deterministic 实现。
7. “CI 绿灯”“Skill 被调用”或“文件存在”都不能单独证明业务、产品或合规目标已满足。

## 人工门禁最小字段

```text
gate_id: 唯一标识
decision: approve | reject | defer
decision_owner: 姓名/角色
scope: 适用 artifact、环境和风险等级
evidence: 链接、命令输出或 review record
time: 决策时间
expiry_or_recheck: 何时重新检查
exception: 如有，说明范围、理由和补偿控制
```

## 事故与回写

当控制带被突破或线上行为与 spec 不符时：

1. 保留原始告警、版本和影响范围；
2. 由 incident owner 确认事实和暂时缓解；
3. 判断是产品意图、设计、计划、代码、测试、发布还是监控缺口；
4. 将需要开发的新问题写成带 owner 的 `intent.md`；
5. 更新对应 Skill、hook、CI 或权限，并在下一次 review 验证没有只修文字。
