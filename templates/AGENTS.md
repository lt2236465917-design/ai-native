# 项目 AI 开发协作上下文

> 这是共享的工程上下文（Engineering Context），不是系统提示、合规证明或一次性任务说明。只写稳定、可验证、团队希望 Agent 在每次相关工作中知道的事实。

## Project overview

- 产品/仓库用途：
- 主要目录：
- Source of truth：
- 负责人和联系方式（不要写私人敏感信息）：

## Commands

| 目的 | 命令 | 健康输出/前置条件 | 最后验证 |
|---|---|---|---|
| Install | `<command>` | `<result>` | YYYY-MM-DD |
| Build | `<command>` | `<result>` | YYYY-MM-DD |
| Test | `<command>` | `<result>` | YYYY-MM-DD |
| Lint/typecheck | `<command>` | `<result>` | YYYY-MM-DD |

## Architecture and conventions

- 代码边界和依赖方向：
- 命名、格式和语言版本：
- 数据/API/event 约定：
- 不可编辑或生成的路径：

## Working agreements

- 先读取相关 intent/spec/plan，再修改代码；
- 每次变更说明实际运行的验证命令和结果；
- 不确定时标记 `UNVERIFIED`，不从 fixture、DOM 或文件名猜测生产能力；
- 需要产品、策略、安全或发布判断时停在人工 gate。

## Security and data handling

- 禁止写入或输出的秘密/敏感数据：
- 脱敏和日志规则：
- 受保护环境/路径及审批入口：

## Common mistakes and verification

- 反复出现的错误及正确做法：
- 变更后必须检查的邻近流程：
- 失败时的回滚/求助路径：

## Maintenance

- Owner：
- Review cadence：
- Last reviewed：YYYY-MM-DD
- Change history：在版本控制中维护，不把运行日志堆进本文件。
