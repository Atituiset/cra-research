# Source Note: SBOM Manager 存储模型 / Copy Annotation / 持续监控工程细节

- URL: https://help.sonatype.com/en/sonatype-sbom-manager.html ；https://help.sonatype.com/en/sbom-component-details-view.html ；https://help.sonatype.com/en/sbom-continuous-monitoring.html ；https://help.sonatype.com/en/continuous-monitoring-best-practices.html
- 发布方： Sonatype（官方帮助文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

### 存储模型（SBOM Manager 主页 + Component Details）

1. **Store**："Provide original SBOM and any augmented SBOMs **by application version**"；Ingest 时 "retaining the original SBOMs for compliance"。Original BOM 视图只读、逐组件可检索（CycloneDX JSON/XML）。
2. **漏洞三分区**：Disclosed（SBOM 自带，组件 Sonatype 不认识）/ Sonatype Identified（Sonatype 数据命中，随 Continuous Monitoring 更新）；Verification = Sonatype Verified / Unverified（"Sonatype does not have the data to verify the declared vulnerability"）。
3. **Data Enrichment 三分**：Sonatype Enhanced / Vendor Data / Public Data（CPE 映射）。
4. **Copy Annotation 精确规则**："copy the annotation for this component vulnerability from **the closest previous application version** where this vulnerability has been annotated"——逐 component-vulnerability 粒度；无前版本注释则按钮不出现。操作集：Add/Edit/Copy/Delete Annotation。
5. Vulnerability Research Metadata（IQ 193+）：detection type / data enrichment / detection source + research type pill（Fast Track/Deep Dive）；KEV/EPSS 展示。
6. **Audit 能力清单原文**："Create rules to scale and automate the VEX process"（规则细节未公开）。
7. **导入限制（自曝）**：某导入路径 "only imports the components section of the SBOM and the resulting report may not be VEX annotated"（sbom-import.html）。

### Continuous Monitoring（Audit 机制）

8. **SBOM CM**：初次分析后快照静态；每晚重评估；用独立 `Compliance` stage，与 Lifecycle CM 解耦；**监控所有 SBOM 版本，不限最新版**。
9. **评估队列参数（默认值全公开）**：producer 10min 周期/最多 1000 条排队；cycle 24h；consumer 每 tenant 1 线程、5min 周期、**每 cycle 仅 30 条**、条目 100min 过期重排；可 REST 调参；每线程 +0.5–1GB heap、CPU <1%/核；可跨实例分布。
10. **Version Evaluation Window**：`maxVersions` / `maxAgeInDays`（二选一必设），可挂 org 层级（示例：ROOT_ORGANIZATION_ID + compliance context，最近 5 版本/90 天）。
11. **Lifecycle CM**：每晚对最近评估重扫；**约 2500 应用/天、一次一个应用、99% <2min、95% <30s、大组合多天**；建议 CM 数据保留 ≤30 天；只有新违规触发通知。

## 支撑报告结论

- 主文档 §4（annotated SBOM 存储模型、Copy 规则、Audit 队列架构）、§5（application version 为一阶对象）、§10.6/10.8（局限）。
