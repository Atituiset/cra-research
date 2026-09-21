# Source Note: Sonatype IQ Server 203 Release Notes（工程债/局限的一手证据）

- URL: https://help.sonatype.com/en/sonatype-iq-server-203-release-notes.html
- 发布方： Sonatype（官方 release notes，203=2026-05-05，至 203.4=2026-06-09）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

### 新功能

1. **Mythos Readiness Enterprise Report（2026-05-29）**：针对"已私下披露但尚未分配 CVE"的漏洞做影响面盘点——全应用组件清单+可升级版本+golden version，按 date range/app/stage/component 过滤；官方建议生产影响分析过滤 Release/Operate stage。说明 Sonatype 已把"pre-CVE 情报响应"产品化。
2. **.NET Reachability**（NuGet 组件，IQ CLI + Jenkins 先行）。
3. **Golden Version-only 自动 PR 默认化**——副作用：默认只覆盖 Maven（Golden Version 仅 Maven 可用）。
4. **SBOM CM 增强**：最新版本优先评估（24h 窗口内先出最新风险）；可配置评估队列跨实例分布。
5. **Firewall Webhooks**（quarantine/block 实时通知，区分新隔离与重复尝试）+ **Bulk Waivers**。
6. SBOM Manager：Legal tab（Effective/Declared/Observed license，ALP 联动）；Advanced Search 支持按 license/policy violation 过滤。

### Bug fixes（工程债自曝，主文档 §10.9）

| Issue | 内容 |
| --- | --- |
| CLM-39913 | 策略评估在 DB 连接池耗尽时死锁（ClusterLock+并发事务高负载） |
| CLM-38947 | **CM 重评估丢失 reachability 标记，导致 "Not Reachable" auto-waiver 跨 CM 周期失效** |
| CLM-39030 | CycloneDX SBOM 导入导出（1.1–1.6）曾产出无效/不合规 SBOM（升 cyclonedx-core-java 12.1.0 修复） |
| EI-1273 | 大负载下 audit/remediation 收集内存无界增长 → OOM |
| CLM-38690 | CycloneDX SBOM 的 license 数据在 Re-Evaluate 后丢失 |
| NEXUS-52385 | HA 部署 npm 元数据并发连接池默认过小 → 回落陈旧缓存 |

## 支撑报告结论

- 主文档 §10.9（自曝局限）；CLM-38947 同时是"reachability→auto-waiver 链路已产品化但不稳"的证据（03 §3.3.6"自动失效重估无人做"维持）。
