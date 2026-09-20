# Source Note: Sonatype 漏洞数据生产（官方 Help）

- URL: https://help.sonatype.com/en/sonatype-vulnerability-data.html
- 标题: Sonatype Vulnerability Data
- 发布方: Sonatype 官方 Help 中心
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档

## 关键事实点

- 官方原文："Sonatype creates data using a **proprietary, automated vulnerability detection system** that monitors, aggregates, correlates, and incorporates machine learning from publicly available information. The Sonatype Data Research team **does not just aggregate public security feeds — we create the precise data we use**."
- 输入源：NVD、邮件列表、网站安全公告、GitHub events、博客、OWASP、OSS Index、客户报告、社交媒体等；自动化系统 + 人工研究团队双轨。
- Sonatype 身份特殊性：Maven Central 运营方，对 Java 生态组件数据有源头优势（行业共识，03 报告已述）。

## 支撑报告结论

- 漏洞数据/情报供应层的第二种模式：**自有数据生产**（不仅策展还"造数"——精确版本区间、组件坐标映射），与纯聚合者（Dependency-Track 直接消费 NVD/GHSA/OSS Index）形成分层。
