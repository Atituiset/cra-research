# Source Note: JFrog 定价与部署形态（2026-09-02 抓取的官方定价页）

- URL: https://jfrog.com/pricing/
- 标题: Pricing 2026
- 发布方: JFrog（官方定价页）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方（价格为厂商声称，随时可变）

## 关键事实点

1. **SaaS 层**：
   - Pro：$150/月（限时 $50/月），纯 Artifactory DevOps，25GB base consumption。
   - Enterprise X：起价 **$950/月**，含 HA、99.9% uptime、24/7 SLA；DevSecOps 含 Code & Binary SCA、**JFrog Advanced Security（Contextual Analysis）**、ML Model Scanning；125GB base。
   - Enterprise+：联系销售。
2. **Self-hosted 层**：
   - Pro X：起价 **$27,000/年**，1 server，24/7 SLA，含 SCA & Model Security。
   - Enterprise X：起价 **$51,000/年**，3 servers（HA）。
   - Self-hosted 最低一年合同；Enterprise X/+ 有多年合同。
3. **Security Bundles**：Unified / Ultimate 两档。**Zero-Touch Remediation 两档都有；JFrog AppTrust（DevGovOps）仅 Ultimate**；Ultimate 含 AI Catalog 与 full App Risk Governance。
4. **AppTrust 相关条目**（定价页原文，厂商声称）："Apply pre-built **CRA and NIST policy templates** to release gates with one click…real-time compliance scoring"；"Continuously monitor…even **post-release support windows**"；"Automatically capture **agent interactions** and generating a signed evidence chain from commits, PRs, and Jira tickets, attached to every application version"。
5. Pro/Enterprise X 均已列 **AI Asset Repositories**（MCP servers/skills/plugins 纳入制品管理）与 **Multi-agent Support**。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §9（定价/部署）；§5.2（CRA policy templates）；§7-4/5/6。
- 解读：差异化安全能力（Contextual Analysis/AppTrust/ZTR）全部收在付费高层级；self-hosted 传统强项保留，但 ZTR（vendor remote repo）与 Smart Remediation（Catalog 连通）在纯离线场景打折。
