# 统一工作台：实施设计与当前状态

[返回阅读指南](../README.md) · [用户旅程](../product/journeys.md) · [查看真实数据演示](../../demo/cra_workbench.ipynb)

2026-09-22。本文是两个仓库合并后的唯一实施入口；旧 minimal-mvp-design 与 B report/08 保留研究价值，发生范围冲突时以本文为准。

## 共享核心

`src/cra/core.py` 持久化发布物、证据、判定、复核、验证、事件和回执。`cli.py` 是操作入口；`presentation.py` 只消费 snapshot。`demo/build_presentation.py` 负责导入两份真实历史证据并调用统一导出，不计算状态。

第一版采用 SQLite 本地单操作员模式，替代直接上 PostgreSQL 的旧计划，用于验证共享契约与业务行为。PostgreSQL、认证、并发冲突控制是客户部署前置工作，不能把当前 SQLite 文件直接当作生产服务。

## cra-workbench/v1 契约

| 对象 | 身份与行为 |
|---|---|
| release | 产品、版本、制品 SHA256 决定 ID；同版本重建可区分 |
| pack | manifest 原始 hash 决定 ID；携带显式信任的公钥和文件索引；重复导入不重复建判定 |
| evidence | 保存签名 predicate 与源包引用，标记 measured |
| judgment | 发布物、漏洞、建议状态、依据、策略、supersedes；只追加 |
| review | judgment_id、批准/拒绝、人、理由、时间；最新记录决定有效状态 |
| verification | 旧/新发布物判定引用、复核人、修复依据；只追加 |
| incident | 类型、知悉依据、起算事实、期限和当时判定快照；只追加 |
| report_record | 外部报送阶段、实际时间和回执声明；不会自动报送 |

对象与证据 blob 禁止 SQL UPDATE/DELETE。数据库拥有者仍能改变数据库，触发器不是防管理员篡改机制。导出重新校验 blob hash 和签名；配置公钥属于信任边界，不从证据包自动信任任意公钥。

## 状态规则

- 导入的所有 VEX 先成为候选；批准前有效状态统一为 under_investigation。
- 审批理由必填；无路径结论仍由操作员判断分析覆盖与上下文，系统不保证人工判断正确。
- 已被替代的判定不能继续审批。重估新增调查中修订，不继承批准。
- 修复候选必须关联不同制品的已复核复扫判定，且需再次批准；旧 Release 不变。
- KEV 不属于合法 incident 类型；创建事件需明确两类之一及知悉依据。
- 报告期限只是辅助计算，真实适用性与期限复核责任仍在操作员。

## 完成与待续

已完成研究归档、共享核心、真实 Go/C 数据接通、静态展示、显式人签与重估、人工修复证据关联、事件时钟及回执、失败阻断导出。旧 PoC 导出也加入验签前置阻断。

尚未完成自动触发、真实多源持续同步、AnalysisRun 范围模型的完整规范化、SBOM 标准摄取服务、线上身份审批、标准 VEX 重新签发、PostgreSQL、原始日志完整打包。当前使用 legacy adapter 保存原始 predicate，避免丢失来源，但不把它当成最终领域 schema。

下一阶段优先顺序：标准化 AnalysisRun 和数据源快照 → 完整原始证据归档 → 自动重估与关联 → 正式 VEX 序列化/签发 → 认证及 PG 试点部署。扩展 Java、Agent、多租户须由试点需求推动。
