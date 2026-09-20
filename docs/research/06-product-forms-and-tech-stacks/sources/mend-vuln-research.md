# Source Note: Mend 漏洞研究团队运作（官方博客 + 官方白皮书）

- URL: https://www.mend.io/blog/vulnerability-research-heres-how-it-works-at-mend/ ；https://www.mend.io/wp-content/media/2021/11/WhiteSource-Vulnerability-Database.pdf
- 标题: Vulnerability Research: Here's How It Works At Mend / WhiteSource Vulnerability Database
- 发布方: Mend.io 官方
- 发布日期: 2026-07-09（博客）；2021-11（白皮书，仍在线引用）
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方

## 关键事实点

- Mend 维持专职 vulnerability research 团队，聚焦开源漏洞：监控多源披露、验证/丰富漏洞记录、产出自有 WS-* 标识符（对未入 CVE 的发现赋予内部 ID，见 Mend docs）。
- 白皮书（厂商声称）：ML + 人工分析结合；声称过滤 70–85% 误报告警。
- 与 Checkmarx 同构：Checkmarx 设 "Checkmarx Zero" 研究团队逐条分析新 CVE、纠错与丰富（Checkmarx SCA FAQ 官方文档）。

## 支撑报告结论

- 企业 SCA 套件物种的共同成本结构：每家都养一个漏洞研究团队维护私有库；"谁家自建库、谁家纯聚合"是数据层第一分层线。
