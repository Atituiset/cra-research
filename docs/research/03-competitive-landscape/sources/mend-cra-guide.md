# Source Note: Mend《EU CRA explained》官方博客

- URL: https://www.mend.io/blog/eu-cyber-resilience-act-compliance-guide/
- 标题: EU CRA explained: requirements, timeline, and compliance
- 发布方: Mend.io 官方博客
- 发布/更新: 2026-07-30（检索快照日期）
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方博客（科普+产品映射混合，产品部分为厂商声称）

## 关键事实点

- CRA 时间线（与官方一致）：2024-12-10 生效；2026-06-11 合格评定机构条款适用；**2026-09-11 漏洞/事件强制报告义务生效**（Article 14，覆盖存量产品）；**2027-12-11 全面适用**（CE 标志、技术文档、风险评估）。
- 罚则：最高 €15M 或全球年营业额 2.5%；次档 €10M/2%；误导信息 €5M/1%。
- SBOM 义务表述："制造商必须提供机器可读 SBOM，至少覆盖顶层依赖，保持更新，应市场监督机构要求提供；不要求公开披露"。
- 覆盖对象：软件产品、联网硬件/IoT、网络与安全产品、移动/桌面应用、嵌入式软件/固件、远程数据处理方案；非商业 OSS 豁免，但商用产品集成 OSS 仍负全责。
- Mend 产品映射（厂商声称）：统一 SAST+SCA+容器扫描；reachability 驱动的 SCA 优先级，结合 EPSS 与 CVSS 4.0；持续 SBOM/AI-BOM 输出 + 审计日志；AI 修复与自动化依赖管理"降低 75% 修复工作量"（厂商声称）；IDE/PR/CI/CD/Cursor/Windsurf/Copilot 集成；SOC 2 Type II / ISO 27001 / GDPR。

## 支撑报告结论

- Mend 有专门的 CRA 内容营销且时间线准确，非单纯蹭概念；但其 CRA 方案仍是"现有 SAST/SCA 能力映射"，非专门产品模块。
- CRA 义务时间线主证据之一（与 JFrog brief、Orbiq、herodevs 交叉一致）。
- "SBOM 至少顶层依赖 + 机器可读 + 按需提供给监管机构"——支撑 SBOM 商品化论点。
