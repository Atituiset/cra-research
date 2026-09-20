# Source Note: GitLab 19.x Agentic AI 安全修复（官方 IR 新闻稿 + 第三方）

- URL:
  - https://ir.gitlab.com/news/news-details/2026/GitLab-Extends-Agentic-AI-with-New-Automated-Security-Remediation-Pipeline-Setup-and-Delivery-Analytics/default.aspx（2026-04-16）
  - https://about.gitlab.com/gitlab-duo-agent-platform/use-cases/
  - https://www.stocktitan.net/news/GTLB/git-lab-extends-agentic-ai-with-new-automated-security-remediation-pizlxr3bwph7.html
- 发布方: GitLab 官方（投资者关系新闻稿）+ StockTitan 转载 + 官网 use-cases 页
- 发布日期: 2026-04-16（GitLab 18.11）；GitLab 19.2 为 2026-07-16（softprom 报道）
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方新闻稿

## 关键事实点

- Agentic SAST Vulnerability Resolution GA（GitLab 18.11, 2026-04）：自动生成 ready-to-merge 代码修复 MR（厂商声称）。
- GitLab 19.2（2026-07-16，第三方报道）："governed agentic automation"——修复脆弱依赖、捕捉 pattern 扫描器遗漏的逻辑缺陷、自定义多步 agent workflow，均在组织现有管控之下。
- Dependency scanning 页提到 "agentic breaking change resolution (for dependency bumps)"：Duo 分析依赖升级失败并给修复。
- Duo Agent Platform use case：对每个选中 finding 生成带修复的 MR。
- 层级：SAST/依赖修复属 Ultimate + Duo。

## 支撑报告结论

- GitLab 已进入"agentic remediation GA"阵营（2026-04），节奏与 Snyk/Checkmarx 同步 → agentic 修复 2026 年成为平台厂商标配叙事。
- "governed agentic automation"（在现有管控下）说明信任/治理成为卖点 → 支撑"agentic remediation 可信度是创新空间"。
