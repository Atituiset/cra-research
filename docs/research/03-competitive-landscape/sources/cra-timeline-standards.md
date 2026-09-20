# Source Note: CRA 时间线与 SBOM/VEX 标准化动态（多源交叉）

- URL:
  - https://www.mend.io/blog/eu-cyber-resilience-act-compliance-guide/（Mend，2026-07-30）
  - https://jfrog.com/solution-sheet/cyber-resilience-act-jfrog-platform-compliance-brief/（JFrog）
  - https://www.orbiqhq.com/eu-regulations/cyber-resilience-act（Orbiq，2026-08-26）
  - https://www.herodevs.com/blog-posts/cra-reporting-obligations-start-september-2026-what-eol-dependencies-mean-for-your-compliance（2026-03-11）
  - https://www.cyberresilienceact.eu/analysis.html（2026-09-11）
  - https://safeguard.sh/resources/blog/cyclonedx-1-7-ecma-424-second-edition-ratification（2026-08-04）
  - https://www.advisori.de/services/regulatory-compliance-management/cra-cyber-resilience-act/cra-sbom（BSI TR-03183-2）
- 抓取日期: 2026-09-18
- 层级: 厂商博客 + 合规咨询 + 社区站点（多源交叉一致）

## 关键事实点（多源一致）

- CRA = Regulation (EU) 2024/2847，2024-11-20 发布于 Official Journal，2024-12-10 生效。
- **2026-06-11**：合格评定机构条款适用。
- **2026-09-11**：Article 14 漏洞/事件报告义务生效（24h 预警 / 72h 通知 / 1 月终报），覆盖存量产品——今天（2026-09-18）已生效一周。
- **2027-12-11**：全面适用（CE 标志、技术文档、Annex I 要求）。
- 罚则：€15M 或全球年营业额 2.5%（取其高）。
- SBOM 要求：机器可读、至少顶层依赖、按需提交监管机构、不强制公开；德国 BSI TR-03183-2 要求 CycloneDX/SPDX、CPE/PURL 标识。
- CycloneDX 1.7 于 2025-12 获 ECMA-424 第 2 版认证；Syft 1.18/Trivy 0.59/Dependency-Track 4.13 等已支持。
- "SBOM 是活文档"（cyberresilienceact.eu，Article 14 生效日发文）。

## 支撑结论

- 报告背景时间线主证据；SBOM/VEX 标准生态成熟度支撑"生成层商品化"判断。
