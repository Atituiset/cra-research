# Source Note: NIST 官方公告 — NVD 运营方式变更（2026-04-15）

- **URL**: https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth
- **标题**: NIST Updates NVD Operations to Address Record CVE Growth
- **发布方**: NIST
- **发布日期**: 2026-04-15
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（政府一手公告）

## 关键摘录 / 事实点

1. **NVD 不再追求全量 enrichment**：不符合优先标准的 CVE 仍会列入 NVD，但标记为 "Lowest Priority - not scheduled for immediate enrichment"。
2. 优先 enrichment 的三类（自 2026-04-15 起）：① CISA KEV 目录内 CVE（目标 1 个工作日内完成）；② 联邦政府使用的软件；③ EO 14028 定义的 critical software。
3. **积压处置**：2024 年初起 NVD 形成大量未 enrichment 积压且无法消化；所有 NVD publish date 早于 2026-03-01 的积压 CVE 被整体移入 "Not Scheduled" 类别。
4. 背景数字：CVE 提交量 2020→2025 增长 263%；2025 年 NVD enrichment 了约 42,000 条（比此前任何一年高 45%）仍跟不上；2026 年 Q1 提交量同比再高约 1/3。
5. **NVD 不再重复打分**：CNA 已提供 severity score 的 CVE，NIST 不再例行提供独立的 NVD 评分。
6. Modified CVE 不再全部重新分析；2025 年标记为 deferred 的 CVE 批次转为 "Modified After Enrichment"。
7. 用户可邮件 nvd@nist.gov 请求对 low-priority CVE 做 enrichment。
8. （旁证，见 research-log 二手来源）2024-02-12 起 enrichment 速率骤降，2024 年中积压超 2 万条；NIST 于 2024-08 与 CISA 签合同提升产能。

## 支撑报告中的结论

- §4 NVD 数据延迟与质量问题（2024 slowdown → 2026 官方承认无法消化积压）
- §4 "只依赖 NVD 不够"的最强论据：enrichment 已从"全量"变为"风险优先 + best effort"
- §7 五源组合使用的必要性
- §10 EO 14028 "critical software" 概念的官方引用
