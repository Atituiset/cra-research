# Source Note: Arnica（官方公告+功能页+第三方）

- URL:
  - https://www.arnica.io/announcement/enhance-software-supply-chain-security-sca-with-reachability-arnica（2024-09-23）
  - https://www.arnica.io/benefits/for-developers
  - https://www.arnica.io/（首页）
  - https://pureai.com/blogs/the-pure-ai-blog/2025/10/arnica-launches-arnie-ai.aspx（Arnie AI）
  - https://appsecsanta.com/arnica（2026-05-19 第三方评测）
- 发布方: Arnica 官方 + Pure AI + AppSec Santa
- 抓取日期: 2026-09-18
- 来源层级: 厂商营销材料 + 第三方分析

## 关键事实点

- Pipelineless 架构：以 GitHub/GitLab app 形式安装，无需 CI/CD 配置即 100% 仓库覆盖（厂商声称，第三方评测确认机制）。
- SCA function-level reachability（2024-09 即上线，早于多数厂商）：在 git 上下文中标注可达性；开发者页宣称"function level reachability + EPSS & KEV + 基于 patch 的直接包缓解选项"（厂商声称）。
- 首页（2026）："聚焦最新部署镜像中的漏洞，用 function-level reachability，而非过期版本"；"Automated Version Management"。
- Arnie AI（2025-10）：multi-agent AppSec 套件——AI SAST（确定性扫描+AI 上下文）、Agentic Rules Enforcer（pipelineless 策略嵌入仓库）；声称"92% 风险在到达生产前解决"（厂商声称）。

## 支撑报告结论

- Arnica 是"reachability + EPSS/KEV + 修复建议"组合商品化的又一例证（2024 年已上线 function 级）。
- pipelineless/identity-aware 路由是修复闭环（"谁该修"）方向的创新点。
