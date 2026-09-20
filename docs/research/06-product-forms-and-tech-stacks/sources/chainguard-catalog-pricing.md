# Source Note: Chainguard 定价与交付（官方 + 第三方交叉）

- URL: https://edu.chainguard.dev/chainguard/containers/reference/pricing/ ；https://www.rfp.wiki/it-security/application-security-testing/software-supply-chain-security/anchore/chainguard ；https://sacra.com/c/chainguard/
- 标题: Chainguard Containers Pricing / Anchore vs Chainguard / Chainguard company profile
- 发布方: Chainguard 官方教育站；RFP.wiki；Sacra（第三方研究）
- 发布日期: 2026-08-21（官方页更新）；2026-07-18（RFP.wiki）；2026-09-03（Sacra）
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档 + 第三方研究交叉

## 关键事实点

- Containers 三档：**Free Images**（最多 5 个生产镜像、仅 latest tag、无 CVE SLA）→ **Per-Image** 按镜像类型（base/application/AI-ML/FIPS）计价、带合同化 CVE 修复 SLA → **Catalog** 按工程组织规模订阅（10 人团队起价 $19,000/年），全目录不限量 + Custom Assembly。
- Libraries（Java/Python/JS）按语言生态 × 开发者人头计价（询价）；VMs 按 per-image。
- 交付 = **托管 registry（cgr.dev）拉取重建制品**——卖的不是扫描而是"替换用制品 + SLA"；Sacra 概括为"垂直整合 SaaS，从 OS 到镜像全链自控"。

## 支撑报告结论

- "制品仓库/Registry 代理型"中出现的新子物种：**重建发行商（rebuild distributor）**，定价单位是镜像/制品而非席位或应用——按"被供给的制品"收费。
