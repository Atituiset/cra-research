# Source Note: Sonatype AI 产品线（Guide / Golden PR / Automated Waivers）

- URL: https://help.sonatype.com/en/sonatype-guide.html ；https://www.sonatype.com/blog/golden-pull-requests-automating-trusted-remediation-without-breaking-builds (2026-03-23)；https://help.sonatype.com/en/sonatype-iq-server-203-release-notes.html ；https://www.sonatype.com/blog/streamline-sca-with-sonatype-build-safe-automation (2025-05-29)
- 发布方： Sonatype 官方文档 / 官方博客
- 抓取日期： 2026-09-21
- 来源层级： 文档=一手事实；博客=厂商声称（功能存在性可凭文档交叉确认）

## 关键事实点

1. **Sonatype Guide**："an AI-first product…By extending Sonatype's trusted data into modern Model Context Protocol (MCP)–aware IDEs"；组件/漏洞搜索 + **Sonatype MCP Server**（实时安全扫描、版本指导、合规检查，接入 Claude/Cursor 等）+ Guide API。另有 guide.sonatype.com 免费注册入口（SSCR 2026 PR）。
2. **Golden PR / Golden Version**：Golden Version = 解决组件+传递依赖全部策略违规、无破坏性变更、符合组织策略的升级版本；自动 PR 支持 GitHub/GitLab/Bitbucket/Azure DevOps；"reduce open source component upgrade costs by more than 80%"【厂商声称】。
3. **关键限制（release notes 一手）**：IQ 203（2026-05）起"automated remediation pull requests **only for Golden Versions by default**…**As Golden Versions are currently only available for the Maven ecosystem**, this means automated pull requests are no longer generated for non-Maven components by default"；非 Golden 可用 Source Control REST API 重开。
4. **Automated Waivers / Build-Safe Automation（2025-05）**：规则化自动豁免不可利用/无修复漏洞，"MTTR 提升 up to 30%"【厂商声称】。
5. **AI 叙事定位**（2026-07 官方博客）："The best vulnerability is the one that never enters the build"——主打 governed consumption + continuous modernization，把 ticket 队列降级；SSCR 2026 把 LLM 推荐定位为风险源（27.8% 幻觉），自家定位"给 AI 纠偏的实时情报层"。
6. **AI 模型治理已进入策略引擎**：Derivative AI Model / AI Content 策略条件 + AI/ML Dashboard 企业报表（IQ 203 增强过滤）——对 Hugging Face 模型的供应链治理是 2026 年新战线。

## 支撑报告结论

- 主文档 §0 修正 2、§7（AI/Agent）；与 Black Duck Signal / GitLab Duo 的 agentic 修复路线对比依据。
