# Source Note: Endor Labs 许可与定价（官方 licenses 文档 + Microsoft FAQ）

- URL（一组）:
  - https://docs.endorlabs.com/introduction/licenses （官方文档）
  - https://learn.microsoft.com/en-us/azure/defender-for-cloud/faq-endor-labs （Microsoft Defender for Cloud 集成 FAQ，2025-05-18）
  - https://www.prnewswire.com/news-releases/endor-labs-introduces-auri-security-intelligence-for-agentic-software-development-302701739.html （免费开发者层）
- 发布方： Endor Labs 官方文档 + Microsoft Learn（合作方官方）+ 官方新闻稿
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（计费规则为事实）；无公开价目（不确定项见下）

## 关键事实点

1. **计费单位**："licensed **per Code Contributor per year**"；Code Contributor = 过去 90 天内向被监控私有仓库 authored/co-authored ≥1 个 commit 的人（Microsoft FAQ 交叉确认 "licensed on a per contributing developer basis"）。
2. **SKU 阵容（2026-09 文档快照）**：
   - `EL-OSS-CORE`：reachability SCA、AI model governance、供应链攻击检测、SBOM/VEX；
   - `EL-OSS-PRO`：Core + **container reachability、upgrade impact**、signing、GitHub enforcement；
   - `EL-CODE-CORE`：SAST + secrets；`EL-CODE-PRO`：+ agentic SAST auto-triage、AI security code review；
   - `EL-OSS-FWAL`（Package Firewall）、`EL-PATCHES`（Endor Patches）、`EL-SBOM`（SBOM Hub）、`EL-AGNT-GOV`（Coding Agent Governance）——均独立售卖、按 contributor/年。
3. **Scan credit 池**（fair usage，"never be blocked from scanning"）：每 contributor 每日 1（Core）/1.5（Pro）credit，合同期内 pooling（100 OSS Core 席 × 1 年 = 36,500 credits）；每席位含 5 个仓库的默认分支无限扫描；PR 扫描、非默认分支、超限仓库默认分支、非 dry-run 的 MCP/AI SAST 扫描计 credit；超量买 `EL-ADD-SCANS`（10,000 扫/桶），超额不中断、走 account team 结算。
4. **免费层**：AURI 发布稿确认 MCP server 有 free developer tier（Skills/MCP/CLI 进 IDE）；skills-ideas 仓库亦写 "free tier available at endorlabs.com"，`ENDOR_NAMESPACE` 默认值 `demo-trial`。
5. **价格点未公开**：licenses 文档指向官网 pricing 页为权威来源，但无公开数字（不确定）。第三方（Coruzant 2026-08、SSOJet 2026-09）称 "pricing is not publicly listed"、"comparable to Snyk's per-developer pricing"（二手来源，仅参考）。
6. **关键能力-付费墙对应**：Upgrade Impact Analysis = OSS Pro；C/C++ embedding 与 AI chat = AI license（Data Privacy 开关）；MCP `security_review` = Enterprise + AI code review 开关。

## 支撑报告结论

- 维度 9：定价模式 = per-contributor 订阅 + 扫描量 fair-usage 池，差异化能力（upgrade impact、container reachability、patches、agent 治理）全部在 Pro/独立 SKU 付费墙后；免费 MCP 层是 PLG 获客入口。
