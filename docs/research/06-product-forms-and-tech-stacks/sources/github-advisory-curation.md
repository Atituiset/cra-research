# Source Note: GitHub Advisory Database 策展机制与吞吐危机（官方博客 + 媒体）

- URL: https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/ ；https://www.helpnetsecurity.com/2026/06/30/github-advisory-database-review/ ；https://github.com/github/advisory-database
- 标题: Inside the Advisory Database… / Vulnerability reports are arriving faster than GitHub can review them / github/advisory-database
- 发布方: GitHub 官方博客；Help Net Security；GitHub 官方仓库
- 发布日期: 2026-07-01；2026-06-30
- 抓取日期: 2026-09-20
- 来源层级: 平台方官方 + 安全媒体

## 关键事实点

- 2026-05 单月 **1,560 条 reviewed advisories**（历史新高），漏洞报告涌入速度超过人工审核能力，发布时延上升。
- 应对机制（官方披露）：**AI-assisted research tooling** 加速常规研究任务、自动化上游 CVE 数据抽取与社区贡献处理、**基于风险的审核优先级**（包使用量、在野利用证据、生态影响等信号）——但"human curators in control of every final decision"。
- 数据分层：reviewed advisories（带策展的包/版本映射，驱动 Dependabot 告警）vs unreviewed（无映射，不产生告警）——**只有经策展映射的条目才进入匹配引擎**。
- 数据库本身开源免费（github/advisory-database 仓库），是 OSV 生态的核心数据源之一。

## 支撑报告结论

- 漏洞数据管道的业界拐点：即使是 GitHub 级平台，纯人工策展已不可持续，"AI 加速 + 人类终审 + 风险优先审核队列"成为 2026 年标准模式；策展吞吐量成为匹配质量的实际瓶颈。
