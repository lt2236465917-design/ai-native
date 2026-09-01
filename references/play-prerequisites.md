# Play 选择与前置条件

本文件把官方 playbook 的“每个 Play 声明 prerequisites”转成可操作的 `[ADAPTATION]` 检查表。它不是 Anthropic 对所有组织的固定清单；项目事实优先。

## 基线前置条件

| Play | 最小可用前置条件 | 典型人工责任人 | 首个可观察产物 |
|---|---|---|---|
| Plan | 一个可追溯的想法/问题入口；意图模板；能够保存版本 | 发起人 + 产品负责人 | draft/accepted `intent.md` |
| Design | 已接受的 `intent.md`；产品、UX、安全和架构约束的来源；规格 owner | 产品负责人 + 设计/技术负责人 | draft/approved `spec.md` |
| Build | 已批准的 `spec.md`；可访问的代码库；构建/测试命令；实施 owner | 工程负责人 | accepted `plan.md` 及 code/test diff |
| Test | 可运行的构建或服务；验收标准；测试/eval 数据和隔离环境 | 工程/QA 负责人 | test/eval record、失败分类 |
| Deploy | 合并的 PR；CI 绿灯；发布授权；回滚/观测方案 | 发布负责人 | release record、deployment evidence |
| Maintain | 线上指标或告警；控制带；事故 owner；写回 intent 的存储位置 | 运维/值班负责人 | incident record 或新 `intent.md` |

## 选择算法

1. 把每个候选 Play 的前置条件标为 `met`、`partial`、`missing` 或 `unknown`。
2. 只把 `met` 的 Play 放入“可立即试点”；`partial` 需要列补齐动作和 owner；`unknown` 不得当作已满足。
3. 从当前最昂贵或最不可靠的瓶颈开始，选择 1–3 个 Play；不要为了形式完整而一次铺开六个阶段。
4. 对每个 Play 写明输入 artifact、输出 artifact、人工 gate、确定性检查和成功指标。
5. 如果某个 Play 的依赖来自另一个 Play，先处理指向它的依赖；如果没有依赖，可以作为起点。
6. 每次试点结束后重新盘点，不把一次成功推广为全组织能力。

## 常见判断

- 只有聊天中的想法、没有可提交的位置：Plan 仍是 `missing`，先建立 intent home。
- 有 `spec.md` 但没有 owner 或批准记录：Design 是 `partial`，不能直接把它当 Build 输入。
- 有测试脚本但没有稳定的健康输出或隔离数据：Test 是 `partial`，不能只以“命令存在”判定可用。
- 有部署脚本但没有授权和回滚证据：Deploy 是 `missing` 或高风险 pending，不得自动运行。
- 有日志但没有控制带、阈值责任人或 incident 写回路径：Maintain 只能作为观察性试点。
