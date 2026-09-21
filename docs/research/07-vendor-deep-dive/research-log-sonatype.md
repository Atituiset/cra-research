# Sonatype 深度调研日志（07-vendor-deep-dive/sonatype）

抓取基准日：2026-09-21。前置：03-competitive-landscape §1.4/§6 已核实结论不重复抓取，本轮聚焦十个深挖维度。

## 2026-09-21 检索记录

1. `Sonatype ATML automated malware detection system engineering blog`
   - 采纳：Sonatype 官方博客《Meet the Developers Behind Sonatype's Malware Detection》(2021，Release Integrity 系统名+60+信号+人工复核队列）、《Protecting Software Developers With AI/ML Insights》(2023，bytecode/NLP 方法+65人团队+108,232 恶意包累计）、《Open Source Malware Index Q2 2025》（季度数据+归因案例）。
   - 弃用：SD Times 二手报道（仅交叉确认时间线）。

2. `Sonatype security research "faster than NVD" vulnerability data curation process`
   - 采纳：help.sonatype.com/en/sonatype-vulnerability-data.html（**本轮最有价值单页**：Fast-Track/Deep Dive 两级队列、92% 修正率、disputed 处理、覆盖边界自认）；SSCR 2026 报告镜像 PDF（NVD vs Sonatype 评分对比量化）。
   - 弃用：businessmodelcanvastemplate（AI 生成味浓）、HuggingFace 数据集。

3. `help.sonatype.com Lifecycle policy management conditions constraints waivers quarantine`
   - 采纳：policy-constraints.html（完整 condition 目录，含 Security Research Type / Detection Type / KEV / EPSS / AI 模型条件）、waivers.html（zero-tolerance 失效、Stale waiver、八种 reason）、firewall-quarantine.html。
   - 采纳（第三方补充）：Safeguard 深度对比（quarantine 在 proxy 层实现、与 Nexus 耦合）——仅作架构交叉验证，未入主文档。

4. `Sonatype Firewall quarantine repository firewall how it works proxy`
   - 采纳：repository-firewall.html（**HTTP/1.1 errorPhrase 依赖、HTTP/2 不支持**；兼容 JFrog Artifactory；HF 模型扩展名拦截清单）。
   - 关键发现：NuGet 409 / Pub 451 状态码怪癖为官方文档自曝。

5. `help.sonatype.com SBOM Manager audit continuous monitoring annotated SBOM storage`
   - 采纳：sonatype-sbom-manager.html（Store 双件模型 by application version）、sbom-component-details-view.html（**Copy Annotation 精确规则：closest previous application version，逐 component-vulnerability**；漏洞三分区+Verification 状态）、sbom-continuous-monitoring.html（**评估队列全部默认参数公开**）、continuous-monitoring-best-practices.html（2500 应用/天上限）。
   - 采纳：sbom-import.html 一句自曝（某导入路径不保留 VEX 注释）。

6. `Sonatype SBOM Manager "copy annotations" OR "automation rules" VEX previous version rules`
   - 确认："Create rules to scale and automate the VEX process" 仅能力清单级别提及，**规则语义公开文档无细节** → 主文档标（不确定）+ §11 假设。

7. `Sonatype Lifecycle air-gapped offline deployment` → `Sonatype Air-Gapped Environment (SAGE)`
   - 采纳：SAGE 官方页（**CRA 在合规框架清单中**——修正 03"未见 CRA 页面"；RPM/Docker/Helm + MySQL/PostgreSQL + Update Tools 每日摆渡数据包）。
   - 弃用：AppSec Santa / OrbitalReg 等第三方对比（仅交叉验证 SAGE 存在性）。

8. `Sonatype AI "Golden Pull Requests"` / `"Sonatype Developer" IDE AI assistant MCP server`
   - 采纳：sonatype-guide.html（AI-first + MCP Server）、Golden PR 官方博客（2026-03-23）、IQ 203 release notes（**Golden Version 仅 Maven** 的一手限制）、build-safe automation 博客（2025-05，auto waivers）。
   - 冲突记录：第三方（AppSec Santa/Checkmarx 汇编）把 Golden PR 描述为"AI-generated"——官方文档语义是策略+数据驱动的策展推荐，非 LLM 生成；主文档按官方口径写。

9. `help.sonatype.com reachability analysis`（验证 03 旧结论是否过时）
   - 采纳：reachability-analysis.html（**2026-09-04 更新的页面**：Java/JS/.NET method 级 reachability + Java-only Evidence）→ 03 §1.4 结论修正为本轮最重要产出之一。

10. `Sonatype IQ Server release notes 2026`
    - 采纳：IQ 203 release notes（Mythos Readiness 报告=pre-CVE 情报响应产品化；六条工程债 bug fix 一手证据，含 CLM-38947 CM 丢失 reachability 标记）。

11. `Sonatype "State of the Software Supply Chain" 2025/2026 NVD comparison`
    - 采纳：GlobeNewswire 2026-01-28 官方新闻稿（123.3 万恶意包、9.8T 下载、86% CSP、GPT-5 幻觉 27.8% 研究）；wokb.cz 的 SSCR_2026_final.pdf 镜像（4.4%/55.7% 评分一致性数据；未能抓取 sonatype.com 官方 PDF 原件——下载门控，镜像为次优来源，已在 source note 标注）。

## 未完成的验证

- SBOM Manager "VEX automation rules" 的规则语法/表达能力（需产品试用或销售材料，公开文档无）。
- SSCR 2026 官方 PDF 原件未直接抓取（注册门控）；评分对比数据引用自镜像+第三方转述，一致性已交叉但原件页码未核。
- Sonatype 组件库总规模（140M+/180K+ 等）第三方口径不一，官方未给单一口径数字，主文档仅标"第三方口径"。
