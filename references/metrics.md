# 度量、状态和验收

所有指标都是 `[ADAPTATION]`：先建立项目自己的 baseline，再比较趋势；不要用单一“AI 生成代码量”代表 AI-native SDLC 是否有效。

## 建议指标

### Leading indicators

| 指标 | 定义 | 适合观察 |
|---|---|---|
| Intent-to-spec latency | 接受 `intent.md` 到批准 `spec.md` 的时间 | Plan/Design 交接是否减少等待 |
| Plan acceptance rate | 首次提交后无需重大返工即被接受的 `plan.md` 比例 | 计划质量和上下文完整性 |
| Policy-to-skill lead time | 策略 owner 批准变更到 Skill/规则合并的时间 | 机构知识更新速度 |
| Automated verification coverage | 关键 gate 中有可重复命令/检查的比例 | 建议性控制是否有确定性支撑 |
| Context freshness | `AGENTS.md` 最近审核时间与变更频率 | 工程上下文是否过期 |

### Lagging indicators

| 指标 | 定义 | 解读边界 |
|---|---|---|
| Review findings per change | 每个 PR 的有效审查发现及其严重度 | 不能直接等于代码质量 |
| Rework after approval | gate 通过后因误解、遗漏或冲突产生的返工 | 结合根因分类 |
| Deployment failure / rollback | 发布失败或回滚比例 | 需区分代码、环境和流程原因 |
| Escaped defect / incident recurrence | 线上缺陷、控制带突破及重复事故 | 关注趋势和严重度 |
| Human wait time | 交接、审批、队列等待占总周期的比例 | 定位人速瓶颈 |

## 记录格式

每次试点至少记录：

```text
period: 起止时间
scope: 仓库、团队、风险等级和采用的 Play
baseline: 采用前数值和取数方法
after: 采用后数值和取数方法
evidence: PR、CI、日志、incident 或会话记录
confounders: 同期的人员、需求、基础设施变化
decision: continue | adjust | pause | rollback
owner: 复盘负责人
next_review: 下一次复盘时间
```

## 状态词

- `PASS`：证据满足本项验收标准；
- `FAIL`：证据显示不满足，需修复或回滚；
- `DEFERRED`：明确推迟，记录 owner 和重新检查条件；
- `SKIPPED`：本轮有意不做，不等于通过；
- `NOT_VERIFIED`：尚无足够运行态或来源证据；
- `PENDING_DECISION`：需要指定责任人作产品/策略/权限判断；
- `DRAFT`：草案，不能作为已批准输入。

不要把“测试通过”写成“流程通过”，也不要把“文件存在”写成“runtime 已加载”。
