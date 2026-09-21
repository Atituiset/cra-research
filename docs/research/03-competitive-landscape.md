# 03. 竞争格局：CRA 时代的漏洞全生命周期产品（2026-09）

> 研究日期：2026-09-18。方法：WebSearch + FetchURL 核实厂商官方文档/新闻稿/官方博客为主，第三方评测仅作交叉验证；所有未经第三方证实的厂商自述数字与能力均标注"（厂商声称）"。每个关键结论对应 [03-competitive-landscape/sources/](03-competitive-landscape/sources/) 下的 source note（文中以 `〔sources/xxx.md〕` 引用），检索过程见 [03-competitive-landscape/research-log.md](03-competitive-landscape/research-log.md)。

## 0. 背景与时间线（为什么是现在）

CRA（Regulation EU 2024/2847）2024-12-10 生效，分阶段适用：**2026-09-11 Article 14 漏洞/事件强制报告义务已生效**（24h 预警 / 72h 通知；终报时限分两条线——actively exploited vulnerability 为修复措施可用后 14 天，severe incident 为 72h 通知后 1 个月；且覆盖存量产品）；**2027-12-11 全面适用**（CE 标志、技术文档、Annex I 安全要求）；罚款上限 €15M 或全球营业额 2.5%。SBOM 义务：机器可读、至少覆盖顶层依赖、保持更新、按需提交监管机构（不要求公开披露）；德国 BSI TR-03183-2 已明确 CycloneDX/SPDX + CPE/PURL。〔[sources/cra-timeline-standards.md](03-competitive-landscape/sources/cra-timeline-standards.md)〕

对厂商格局的两个直接影响：
1. **CRA 的监管对象是"投放市场的产品（product with digital elements）"，不是代码仓库**。这天然要求 Product→Version 维度的漏洞跟踪、SBOM/VEX 版本延续与证据链——而主流 AppSec 工具的对象模型是 repo/应用/容器镜像。
2. 2025–2026 年厂商动作密集：reachability 迅速普及、agentic 修复集中 GA、SBOM/VEX 成为发布常态（如 Black Duck SCA 2026.7.0 的 VEX Templates）。CRA 是需求侧放大器，但多数厂商只是把既有能力"映射"到 CRA 条款。

---

## 1. 厂商分节

### 1.1 Snyk

1. **定位**：开发者优先的 AI 安全平台（自 2025 起 rebranding 为 "the AI security company"），SCA/SAST/容器/IaC 一体。〔[sources/snyk-evo-cos-ga.md](03-competitive-landscape/sources/snyk-evo-cos-ga.md)〕
2. **CRA 策略**：持续的 CRA 内容营销（2025-01 解读博文、2025-06 合规博文、CRA cheat sheet LP），主张"把安全测试嵌入开发工作流即满足 CRA"。属"现有能力映射"，无专门 CRA 产品模块。〔[sources/snyk-cra-dependency-track.md](03-competitive-landscape/sources/snyk-cra-dependency-track.md)〕
3. **SCA**：自建漏洞库（Snyk Intel，人工策展）+ 聚合；生态覆盖最广之一。
4. **SBOM**：生成/导出（SPDX/CycloneDX），`snyk sbom` CLI；非 SBOM 管理平台。
5. **VEX**：无独立 VEX 生成产品；reachability/Risk Score 可作为 VEX 判定的输入但需自行落地。
6. **Reachability**：**function/code-element 级 + call path 展示**，DeepCode AI 程序分析 + 安全专家校验；GA 支持 Java/JS/Python，.NET 为 Early Access（2026-09 文档）。文档坦承反射等动态行为的欠近似问题。〔[sources/snyk-reachability-docs.md](03-competitive-landscape/sources/snyk-reachability-docs.md)〕
7. **Exploitability**：Risk Score 融合 reachability + EPSS + exploit maturity + CVSSv4；Evo COS（2026-08 GA）用自主 AI pentest 持续验证"攻击者实际可利用什么"（厂商声称）——行业最激进的 exploitability 产品化尝试。〔[sources/snyk-evo-cos-ga.md](03-competitive-landscape/sources/snyk-evo-cos-ga.md)〕
8. **Threat Intel**：Snyk Intel 自建研究团队；恶意包检测（2026 推出 malicious code defense，private preview）。
9. **Remediation**：自动升级 PR、Agent Fix（2026-09 GA 于 PR 工作流，第三方报道）；Evo Agentic AppSec 修复 agent（public preview，CLI/ADE 入口）。
10. **AI/Agent**：**真 agent 编排**：Evo 四环（Discover/Remediate/Validate/Prevent），AI-SPM + 修复 agent + 持续攻击验证 + 预防 gate。非 chatbot。〔[sources/snyk-evo-cos-ga.md](03-competitive-landscape/sources/snyk-evo-cos-ga.md)〕
11. **Compliance Evidence**：报告/审计能力一般；CRA 证据链无专门产品。
12. **Product→Version 维度**：**无**。对象模型是 Project（repo/制品扫描目标）。

### 1.2 Mend

1. **定位**：AppSec + AI 安全统一平台；SCA 老牌（原 WhiteSource），手握 Renovate。
2. **CRA 策略**：2026-07 发布高质量 CRA 指南（时间线准确、义务拆解细致），产品映射为 SAST+SCA+容器+SBOM/AI-BOM+AI 修复；合规页覆盖 CRA/EU AI Act/NIST。内容营销深度好于多数同行，但仍是映射而非专门模块。〔[sources/mend-cra-guide.md](03-competitive-landscape/sources/mend-cra-guide.md)〕
3. **SCA**：自建数据；宣称 200+ 语言检测、reachability 降噪、"修复时间降 80%"（厂商声称）。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md)〕
4. **SBOM**：生成 + 持续更新 SBOM/AI-BOM + 审计日志（厂商声称）。〔[sources/mend-cra-guide.md](03-competitive-landscape/sources/mend-cra-guide.md)〕
5. **VEX**：无突出 VEX 生成/消费产品证据。
6. **Reachability**：SCA reachability 是其传统强项（docs 有专门章节），厂商宣称 function 级；独立验证有限。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md)〕
7. **Exploitability**：EPSS + CVSS 4.0 优先级（厂商声称）。〔[sources/mend-cra-guide.md](03-competitive-landscape/sources/mend-cra-guide.md)〕
8. **Threat Intel**：自建研究 + 恶意包拦截。
9. **Remediation**：Renovate（自动升级 PR 的事实标准之一）+ AI code fixes。
10. **AI/Agent**：AI 修复 + AI 编码助手集成（Cursor/Windsurf/Copilot），偏 copilot/自动化，未见多 agent 编排叙事。
11. **Compliance Evidence**：审计日志 + SLA 跟踪 + SOC 2/ISO 27001 自身合规背书。
12. **Product→Version 维度**：**无**（repo/项目维度）。

### 1.3 Black Duck（原 Synopsys Software Integrity）

1. **定位**：企业级 SCA/审计级 SBOM 领导者（Gartner AST MQ 八连冠、Forrester SCA Wave 四连冠——厂商引用）；新增 Signal 补 AI 时代开发者侧。〔[sources/blackduck-signal.md](03-competitive-landscape/sources/blackduck-signal.md)〕
2. **CRA 策略**：有实际制造业客户案例（STMicroelectronics 用 Black Duck SCA + Coverity 自动化 SBOM 支撑 CRA，2025-03 官方 PR）；OSSRA 2026 报告覆盖 CRA/DORA。未见 CRA 专门产品模块，但在半导体/制造业 CRA 场景有真实占位。〔[sources/blackduck-signal.md](03-competitive-landscape/sources/blackduck-signal.md)〕
3. **SCA**：KnowledgeBase 400 万+ 组件（厂商数据），多因子检测（声明/二进制/代码片段/依赖），审计级准确性是核心卖点。
4. **SBOM**：生成/导入/SPDX/CycloneDX 全支持，SBOM Templates 成熟；二进制分析（Black Duck Binary Analysis）覆盖无源码场景。
5. **VEX**：**2026.7.0（2026-08）新增 VEX Templates**——模板化定义 VEX 文档字段，与 SBOM Templates 统一管理；VEX 为独立 license 模块。〔[sources/blackduck-vex-templates.md](03-competitive-landscape/sources/blackduck-vex-templates.md)〕
6. **Reachability**：有（Coverity 引擎支撑的可利用路径分析），但非其营销重心，语言覆盖偏传统生态。
7. **Exploitability**：BDSA（Black Duck Security Advisories）提供比 NVD 更快的策展情报；EPSS/KEV 级别信号集成。
8. **Threat Intel**：BDSA 是其传统强项（CNA 身份）。
9. **Remediation**：升级指导 + Signal 的 agentic 修复（"自动发现并修复、无假阳性"，厂商声称，2026-03 GA）。
10. **AI/Agent**：Signal 由 ContextAI 驱动、嵌入 AI 编码工具工作流；属 agent 形态但聚焦编码时防护，非全生命周期编排。〔[sources/blackduck-signal.md](03-competitive-landscape/sources/blackduck-signal.md)〕
11. **Compliance Evidence**：**行业最强之一**——审计级报告、license 合规、SBOM/VEX 模板化导出，长期服务并购尽调与监管场景。
12. **Product→Version 维度**：**部分**——Black Duck 的对象模型是 Project + Version（版本为一级对象，SBOM 按版本管理），是主流 AppSec 厂商中最接近 Product→Version 的；但"Version"映射的是扫描目标版本，不等于 CRA 的"投放市场的产品版本 + 支持期 + 证据链"完整语义。

### 1.4 Sonatype

1. **定位**：软件供应链治理（Nexus 仓库 + Lifecycle 策略 + Firewall 前置拦截 + SBOM Manager）。
2. **CRA 策略**：未见专门 CRA 页面；SBOM Manager 营销以 EO 14028/NIS2 为主（2025-03 奖项申报材料）。CRA 靠 SBOM Manager 通用能力承接。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
3. **SCA**：自建漏洞情报（"proprietary vulnerability intelligence"，202.1 release notes）+ 组件健康度/恶意包（其年度 State of the Software Supply Chain 报告是行业引用源）。
4. **SBOM**：**SBOM Manager（2023 起独立产品）**——SPDX/CycloneDX 生成/校验/存储/分发全生命周期，1000+ 组织（厂商声称）。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
5. **VEX**：SBOM Manager 支持 VEX 文档与注释；**VEX 注释可从旧版本 SBOM 复制到新版本**（IQ 2024 release notes）——全行业极少数明确处理"版本间 VEX 延续"的功能。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
6. **Reachability**：无 function 级 reachability（依赖维度的优先级与"component similarity"分析为主）。
7. **Exploitability**：EPSS/KEV 级别信号；Firewall 侧重恶意包前置阻断。
8. **Threat Intel**：自建（其恶意包追踪数据被同行引用）。
9. **Remediation**：升级建议 + 依赖健康管理；无 agentic 修复。
10. **AI/Agent**：弱（策略自动化为主）。
11. **Compliance Evidence**：SBOM 存储/分发/审计是强项。
12. **Product→Version 维度**：**部分**——SBOM Manager 以 SBOM（绑定 application 版本）为管理对象 + VEX 跨版本延续，方向最接近，但对象是"application/SBOM"而非 CRA 产品语义，且无 reachability/修复闭环。

### 1.5 JFrog

1. **定位**：二进制制品为中心的 Secure Software Supply Chain Platform（Artifactory/Xray/Curation/Advanced Security/Runtime/AppTrust）。
2. **CRA 策略**：**有专门 CRA Compliance Brief（solution sheet）**，逐条映射 CRA 义务到产品：Curation 前门拦截、Xray 自动 SBOM+VEX、AppTrust 证据收集与 OPA 策略 gate。叙事核心："CRA 监管的是你交付的产品——二进制"（厂商声称）。是所有 AppSec 厂商中 CRA 映射最完整、且最明确以 release/制品为对象者。〔[sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
3. **SCA**：Xray 聚合 + 自建研究（JFrog Security Research 有 CVE 发现记录）；依托制品仓库的天然覆盖。
4. **SBOM**：自动生成（构建时），机器可读，绑定制品。〔[sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
5. **VEX**：SBOM 富化 VEX 数据（厂商声称）；与 release 绑定。〔[sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
6. **Reachability**：Contextual Analysis（判断 CVE 在制品/代码上下文中是否真正可利用，厂商声称）；非公开 call graph 粒度的 function 级证据。
7. **Exploitability**：Contextual Analysis + KEV/EPSS 类信号；Runtime 产品提供运行时上下文。
8. **Threat Intel**：JFrog Security Research 自建。
9. **Remediation**：升级建议 + Curation 前置预防；无 agentic 修复发布。注意：部分 Xray 能力 2026-04 起分阶段迁移至 Curation（官方 deprecation 公告）。〔[research-log.md](03-competitive-landscape/research-log.md) #6〕
10. **AI/Agent**：弱；MCP 生态集成在演进。
11. **Compliance Evidence**：**AppTrust 是关键差异化**——不可变 release bundle 分级 promotion、证据与二进制加密绑定（chain of custody）、Policy as Code（OPA）合规 gate（厂商声称）。〔[sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
12. **Product→Version 维度**：**部分偏强**——以 release/制品版本为对象做证据与 gate，最接近"产品版本生命周期"；但漏洞发现/关联/reachability 深度弱于 Snyk/Endor，且对象仍是"制品"而非带支持期语义的产品线。

### 1.6 GitHub（Advanced Security / Dependabot）

1. **定位**：平台内置安全基线（2025 起 GHAS 拆分为 Code Security + Secret Protection 两个 SKU——第三方汇编）。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
2. **CRA 策略**：**无官方 CRA 页面/方案**（检索确认，命中均为第三方仓库）。合规叙事止于 SBOM 导出。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
3. **SCA**：依赖 GitHub Advisory Database（聚合+自建评审）；Dependabot 告警。
4. **SBOM**：dependency graph 导出 SPDX（repo 粒度）；无导入/管理。
5. **VEX**：无。
6. **Reachability**：**无**（Dependabot 无 reachability，第三方对比一致）。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
7. **Exploitability**：GHAS 告警含 EPSS/KEV 信号展示。
8. **Threat Intel**：Advisory Database + 生态规模优势。
9. **Remediation**：Dependabot 升级 PR（商品化标杆）+ Copilot Autofix（code scanning 告警自动修复建议，PR 内呈现）。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
10. **AI/Agent**：Copilot Autofix 属"AI 修复建议"（copilot 形态），非多 agent 编排。
11. **Compliance Evidence**：通用审计日志；无漏洞生命周期证据产品。
12. **Product→Version 维度**：**无**（repo 粒度）。

### 1.7 GitLab

1. **定位**：一体化 DevSecOps 平台（Ultimate 层含全套 AppSec）。
2. **CRA 策略**：无专门 CRA 产品页（检索未命中官方 CRA 方案）；合规能力为通用的策略/审计/合规框架映射。
3. **SCA**：dependency scanning 已迁移至 **SBOM-based 架构**（CycloneDX SBOM 为数据中枢，Gemnasium 分析器被淘汰路线）。〔[sources/gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md)〕
4. **SBOM**：生成 CycloneDX SBOM 并作为扫描输入；SBOM 富化 reachability 后回传平台。〔[sources/gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md)〕
5. **VEX**：有 VEX/漏洞状态导出能力（通过报告与 API），无独立 VEX 产品。
6. **Reachability**：**package 级静态 reachability（Beta）**——仅判断依赖是否被 import，非 function 级；支持 Python/JS-TS/Java 三语言；文档坦承 Java DI/动态加载假阴性高。〔[sources/gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md)〕
7. **Exploitability**：EPSS/KEV 信号入漏洞报告。
8. **Threat Intel**：GitLab advisory database（聚合）。
9. **Remediation**：**Agentic SAST Vulnerability Resolution GA（18.11, 2026-04）**——自动生成 ready-to-merge 修复 MR；19.2（2026-07）扩展为"governed agentic automation"：修复脆弱依赖 + agentic breaking change resolution（依赖升级失败自动修）+ 自定义多步 agent workflow。〔[sources/gitlab-agentic-remediation.md](03-competitive-landscape/sources/gitlab-agentic-remediation.md)〕
10. **AI/Agent**：Duo Agent Platform——真 agent 方向（多步工作流+组织管控），从 copilot 演进中。
11. **Compliance Evidence**：合规框架/审计事件/策略执行是 Ultimate 层传统能力。
12. **Product→Version 维度**：**无**（project/repo 维度）。

### 1.8 Veracode

1. **定位**：企业 AppSec 老牌（SAST/DAST/SCA），2025 起向供应链预防（Package Firewall）与 AI 修复（Fix）扩展。
2. **CRA 策略**：未见专门 CRA 页面；合规叙事为通用企业报告能力。
3. **SCA**：自建漏洞库；2025-01 收购 Phylum 获恶意包行为检测；Java/.NET 生态强。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
4. **SBOM**：SCA agent 扫描生成 CycloneDX SBOM（2025-06）；SBOM API 支持 upload scans（2026）。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
5. **VEX**：无独立 VEX 产品证据。
6. **Reachability**：**vulnerable-method（function 级）扫描**，传统强项在 Java/.NET；2026 年 SCA agent v3.8.120 仍在迭代 JavaScript vulnerable method 扫描。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
7. **Exploitability**：EPSS + KEV 2023 年即集成进 SCA API；Risk Manager 产品做风险聚合。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
8. **Threat Intel**：自建研究 + Daily Threat Intel Brief 运营。
9. **Remediation**：Veracode Fix（SAST 自动修复）成熟；**Fix for SCA 仍 Limited Availability（2026 年中）**——SCA 侧 agentic 修复成熟度落后。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
10. **AI/Agent**：Fix 为 AI 修复单点能力，非编排。
11. **Compliance Evidence**：企业报告/政策管理强。
12. **Product→Version 维度**：**无**（application 扫描档案维度，近似但非产品版本生命周期）。

### 1.9 Checkmarx

1. **定位**：Checkmarx One 九引擎 ASPM 平台（SAST/SCA/DAST/IaC/容器/API/secrets 等）。
2. **CRA 策略**：未见专门 CRA 页面；以通用合规报告承接。
3. **SCA**：聚合 + 自建研究（Checkmarx 研究团队恶意包披露记录多）。
4. **SBOM**：SCA 生成 SBOM。
5. **VEX**：无独立产品证据。
6. **Reachability**：**"exploitable path analysis"**——判定漏洞类/函数是否经调用链可达且可利用（厂商声称比 reachability 更精确）。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md)〕
7. **Exploitability**：ASPM 关联 + "attackable risk" 优先级（厂商声称相关性降噪 89%——第三方转述，未证实）。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md)〕
8. **Threat Intel**：自建研究团队。
9. **Remediation**：Developer Assist（2025-11）——IDE 内 agentic SCA：即时恶意包发现 + 自动化安全修复，宣称"plan, execute, validate"；Triage & Remediation Assist 出 review-ready 修复。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md)〕
10. **AI/Agent**：Developer Assist 属 agent 形态（IDE 内自治修复流），但跨引擎统一编排未见。
11. **Compliance Evidence**：平台级报告能力。
12. **Product→Version 维度**：**无**。

### 1.10 Endor Labs

1. **定位**：reachability 优先的 AI-native AppSec/供应链平台（2021 创立，$163M 融资——第三方）；2026 已扩展为 agentic 应用安全平台。
2. **CRA 策略**：有 CRA 解读内容（2024-10 learn 文章）；合规叙事主打 FedRAMP use case（reachability 降修复量 70–80%，厂商声称）+ SBOM/VEX 能力。CRA 非其核心战场叙事。
3. **SCA**：自建漏洞数据库 + **CVE→受影响函数（跨版本）映射库**（程序分析自建，厂商声称）。〔[sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md)〕
4. **SBOM**：生成 SBOM（SCA 一体化）；Microsoft Defender for Cloud 集成（2026-06）确认其 SBOM/call graph 能力被巨头生态采纳。〔[research-log.md](03-competitive-landscape/research-log.md) #11〕
5. **VEX**：支持 SBOM & VEX 输出（FedRAMP 页）。〔[research-log.md](03-competitive-landscape/research-log.md) #11〕
6. **Reachability**：**行业标杆叙事**——function 级 + 完整 call graph + 容器/OS 包使用分析 + 互联网暴露；每个可达判定附**可检查、可复现的 call chain 证据**；precomputed reachability 兜底（无完整 call graph 时）；客户报告降噪 80–99%（厂商声称）。〔[sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md)〕
7. **Exploitability**：reachability + exploitability 上下文组合；强调"二元判定不够，要证据"。
8. **Threat Intel**：自建漏洞/恶意包研究。
9. **Remediation**：**Upgrade Impact Analysis（升级会不会 break 的预判）+ Endor Patches**（不升级的补丁路径）——修复环节差异化明显。〔[research-log.md](03-competitive-landscape/research-log.md) #11〕
10. **AI/Agent**：AI security analyst（agent 化 triage/调查），reachability 证据是其 agentic remediation 的地基（厂商自述）。〔[sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md)〕
11. **Compliance Evidence**：call chain 证据天然贴近审计需求，但未产品化为"CRA 证据包"。
12. **Product→Version 维度**：**无**（repo/应用维度）。

### 1.11 Semgrep

1. **定位**：规则驱动的 SAST 起家（CE 开源），AppSec Platform 扩展 SCA（Supply Chain）/secrets；开发者与规则透明性是品牌核心。
2. **CRA 策略**：未见专门 CRA 材料。
3. **SCA**：Supply Chain 支持 **12 语言 / 15 包管理器**；聚合数据源 + 规则化检测。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
4. **SBOM**：可生成/消费 SBOM（CycloneDX）。
5. **VEX**：无独立产品证据。
6. **Reachability**：**dataflow reachability 语言覆盖行业最广**：2024-12 达 10 语言（含 Scala/Swift），2025-06 上线"业界首个 PHP reachability"（厂商声称）；2026 支持 Java/Kotlin 无 lockfile 分析（beta）。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
7. **Exploitability**：reachability + 标准信号；Guardian 提供升级 PR。
8. **Threat Intel**：规则社区 + 聚合。
9. **Remediation**：Guardian 自动升级 PR；2026-04 增加 dependency path 数据。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
10. **AI/Agent**：**Assistant**——AI triage 与研究者一致率 95%+、承担客户 60% SAST triage（厂商声称，2025-09）；Memories 学习组织习惯。属 AI 降噪/分类标杆，非全生命周期编排。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
11. **Compliance Evidence**：弱（面向开发工作流）。
12. **Product→Version 维度**：**无**。

### 1.12 Chainguard

1. **定位**：**安全构建源头**——硬化容器镜像/VM/语言库，把"漏洞修复"变成"换用已修复的重建制品"。
2. **CRA 策略**：有专门 CRA 文章（2026-01），主张 secure-by-default 制品直接满足 CRA 的设计期义务；Libraries/Images 自带 SBOM+provenance 天然贴合 CRA 文档要求。〔[research-log.md](03-competitive-landscape/research-log.md) #13〕
3. **SCA**：不做通用 SCA 扫描；其角色是"消灭 CVE 存量"（critical CVE 平均 20 小时内消除——厂商声称经 THN 转述）。
4. **SBOM**：所有制品附 SBOM + provenance（签名）。
5. **VEX**：**公开 VEX feed** 发布修复版本信息；Wiz/Amazon Inspector/Grype/Upwind/Anchore/Trivy 已识别其修复版制品。〔[sources/chainguard-libraries-java-ga.md](03-competitive-landscape/sources/chainguard-libraries-java-ga.md)〕
6. **Reachability**：不涉及（其逻辑是"修复一切"而非"判断可达性"）。
7. **Exploitability**：不涉及。
8. **Threat Intel**：CVE 监控 + 自动化 backport 管线。
9. **Remediation**：**范式创新**——Libraries for Java GA（2026-06）对 EOL 版本（如 Spring Boot 2.7，143 个无补丁 CVE）做 backport 修复，制品带 `-0.cgr.N` 干净版本号，**扫描器和审计者看到的是版本化制品而非 patch 叠加**，解决审计痕迹问题；Python Libraries GA（2025-10）。〔[sources/chainguard-libraries-java-ga.md](03-competitive-landscape/sources/chainguard-libraries-java-ga.md)〕
10. **AI/Agent**：不涉及（自动化管线而非 LLM agent）。
11. **Compliance Evidence**：SBOM+provenance+VEX feed 组合 = 面向审计的制品级证据。
12. **Product→Version 维度**：不涉及（对象是依赖制品本身）。其模式启示：修复→验证→SBOM/VEX 更新的闭环可以在**制品供应链层**完整实现。

### 1.13 Anchore

1. **定位**：SBOM-first 供应链安全（开源 Syft/Grype + Enterprise 平台）。
2. **CRA 策略**：无专门 CRA 产品页；但 v6（2026-05）定位"统一 SBOM-powered 合规方案"，Syft/Grype 是 CRA SBOM 工具链的事实标准组件（第三方 CRA 指南普遍推荐）。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
3. **SCA**：Grype 聚合匹配（NVD/GHSA 等），开源生态最主流之一。
4. **SBOM**：**Syft 是 SBOM 生成事实标准之一**（1.18+ 输出 CycloneDX 1.7/ECMA-424）；Enterprise 存储全部历史 SBOM。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
5. **VEX**：Grype 消费 VEX 文档（`--vex-documents`）过滤误报；Enterprise 支持 VEX 工作流。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
6. **Reachability**：无。
7. **Exploitability**：EPSS/KEV 信号。
8. **Threat Intel**：聚合 feed 为主。
9. **Remediation**：不涉及修复执行；与 Chainguard Libraries 集成验证修复（2025-12）。
10. **AI/Agent**：无。
11. **Compliance Evidence**：**核心强项**——"存储所有 SBOM + 新 advisory 发布即定位受影响制品、无需重扫"（第三方确认）；policy-as-code 合规管理；SBOM 类型枚举覆盖 device/firmware/VMDK 等产品级对象。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
12. **Product→Version 维度**：**部分**——SBOM 清单+持续重匹配实质上是"制品版本→漏洞"的持续生命周期跟踪，缺的是修复闭环与 CRA 证据语义。

### 1.14 Aqua Security

1. **定位**：CNAPP（容器/K8s/运行时防护），开源 Trivy 是扫描层事实标准（36k+ stars）。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
2. **CRA 策略**：未见 CRA 专门材料。
3. **SCA**：供应链模块内含 SCA，但第三方评测一致认定"SCA 非 Aqua 主战场"；Trivy 覆盖语言包管理器扫描使基础扫描免费化。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
4. **SBOM**：Trivy 生成 SBOM（CycloneDX/SPDX，1.7 支持）。
5. **VEX**：Trivy 支持 VEX 过滤。
6. **Reachability**：**运行时视角**——eBPF/Tracee 观测工作负载实际行为做降噪（"deep runtime context"，厂商声称）；非代码级 call graph。
7. **Exploitability**：运行时上下文是其 exploitability 卖点。
8. **Threat Intel**：Aqua Nautilus 研究团队（有实料披露记录）。
9. **Remediation**：侧重预防/阻断而非代码修复。
10. **AI/Agent**：未见突出发布。
11. **Compliance Evidence**：运行时合规监控（CIS 等）。
12. **Product→Version 维度**：**无**（工作负载维度）。

### 1.15 Wiz

1. **定位**：CNAPP 领导者；2026-03-11 被 Google 以 $32B 完成收购（EU 批准后交割，保留品牌与多云承诺——Reuters/PitchBook 多源）。〔[sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
2. **CRA 策略**：未见 CRA 专门材料；收购后资源倾斜云安全。
3. **SCA**：Wiz Code（2024-09）提供原生 SCA/SAST/IaC/secrets/容器扫描；核心价值是 Security Graph 的 code-to-cloud 关联。〔[sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
4. **SBOM**：有 SBOM 生成。
5. **VEX**：无突出证据。
6. **Reachability**：**公认短板**——两个独立第三方评测（2024-10 latio.tech、2026-05 roboticsandautomationnews）均指出 Wiz Code 无静态 reachability、无 AI AutoTriage、AutoFix 仅限主分支。〔[sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
7. **Exploitability**：**强项在运行时/网络暴露上下文**（互联网可达 + 工作负载在跑 + 攻击路径图），这是 CNAPP 路线对 exploitability 的回答——与代码级 reachability 互补。〔[sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
8. **Threat Intel**：Wiz Research（有高质量披露）。
9. **Remediation**：AutoFix（受限，第三方评价）。
10. **AI/Agent**：Wiz 有 AI-SPM/AI 安全产品线扩张，但漏洞修复 agent 未见。
11. **Compliance Evidence**：云合规（CSPM 传统强项）。
12. **Product→Version 维度**：**无**（云资产/工作负载维度）。

### 1.16 补充厂商

- **Socket**：恶意包/行为分析起家；2025-04 收购 Coana 补齐 reachability，"precomputed reachability"预计算 CVE 函数与传递依赖调用关系以过滤噪声（厂商声称）；竞品指出其应用侧 call path 不完整（竞品立场，谨慎）。启示：reachability 已成 SCA 入场券。〔[sources/socket-reachability.md](03-competitive-landscape/sources/socket-reachability.md)〕
- **Arnica**：pipelineless 架构（装 GitHub/GitLab app 即覆盖全部仓库）；2024-09 即上线 function-level reachability + EPSS/KEV + 修复选项（厂商声称）；Arnie AI（2025-10）为 multi-agent 套件 + 身份感知路由（把 finding 路由给该修的人）。〔[sources/arnica.md](03-competitive-landscape/sources/arnica.md)〕
- **Oligo**：**runtime exploitability 证据最前沿**——Deep Application Inspection 观测"库是否加载/函数是否执行/有无异常行为"，输出 runtime SBOM & VEX；runtime 非执行证据支撑 FedRAMP SLA 72h→180d 风险调整（厂商声称）；但其框架映射聚焦 FedRAMP/PCI/SOC 2，**未见 CRA 映射**。〔[sources/oligo-runtime-compliance.md](03-competitive-landscape/sources/oligo-runtime-compliance.md)〕
- **Apiiro**：Deep Code Analysis + Risk/Context Graph（代码→管道→运行时）；Guardian Agent 在 prompt 层拦截不安全 AI 编码；AutoFix Agent（2025-08）生成上下文修复+自动测试验证+review-ready PR（厂商声称）。图谱+多 agent 路线代表。〔[sources/apiiro-agentic.md](03-competitive-landscape/sources/apiiro-agentic.md)〕
- **Finite State / ONEKEY（产品安全/PSIRT 阵营）**：以**产品/产品线/build/固件二进制**为核心对象，CRA 是主要需求驱动：Finite State 提供托管 CRA 合规服务（从出货物生成 SBOM&VEX、风险评估、持续监控、CVD 策略起草）、PSIRT 用例明确"判定哪些产品和 build 受影响"；ONEKEY 平台从二进制生成/导入 SBOM 并"在完整产品生命周期中监控"。**但技术栈是二进制/固件分析，面向嵌入式/IoT/OT，无 function-level reachability、agentic 修复或现代开发者工作流**。〔[sources/product-security-camp.md](03-competitive-landscape/sources/product-security-camp.md)〕
- **开源基线 Dependency-Track**：以 project（含版本）/portfolio 为一级对象、消费 SBOM、持续监控、支持 VEX——开源世界最接近 Product→Version 漏洞管理的实现；无 reachability/修复闭环/CRA 证据模型。〔[sources/snyk-cra-dependency-track.md](03-competitive-landscape/sources/snyk-cra-dependency-track.md)〕
- **CRA 原生初创信号**：CRACI（赫尔辛基，2026-05 获 €1.4M 种子轮，自动化漏洞跟踪与文档）；sbom-sentinel（个人 OSS 项目，自述目标就是"每个出货产品的 SBOM 保鲜 + 可利用性 triage + 修复路由 + EU 监管证据"）。说明该定位已被市场感知但无成熟商业产品。〔[research-log.md](03-competitive-landscape/research-log.md) #1；[sources/snyk-cra-dependency-track.md](03-competitive-landscape/sources/snyk-cra-dependency-track.md)〕

---

## 2. 横向对比大表

粒度说明：● 强/产品化成熟；◐ 有部分能力或 Beta/EA/LA；○ 无或未见证据。"（声称）"= 仅厂商自述。

| 厂商 | CRA 专门策略 | SCA 数据源 | SBOM | VEX | Reachability 粒度 | 语言覆盖(reach.) | Exploitability | Remediation | AI/Agent 形态 | 合规证据 | Product→Version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Snyk | ◐ 内容营销+映射 | 自建+聚合 | ● 生成 | ○ | ● function+call path | ◐ Java/JS/Py GA；.NET EA | ● EPSS+KEV+Risk Score+AI pentest 验证(声称) | ● 升级PR+Agent Fix | ● 多agent编排(Evo四环) | ◐ | ○ |
| Mend | ◐ 深度内容营销 | 自建 | ● SBOM/AI-BOM(声称) | ○ | ● function级(声称) | ◐ 检测200+语言，reach.覆盖不透明 | ◐ EPSS+CVSS4 | ● Renovate+AI修复 | ◐ copilot/自动化 | ◐ 审计日志 | ○ |
| Black Duck | ◐ 制造业客户案例 | 自建KB(400万+组件) | ● 审计级+模板+二进制 | ● 2026.7 VEX Templates | ◐ 有(Coverity引擎) | ◐ 传统生态 | ● BDSA自建情报 | ◐ 指导+Signal修复(声称) | ◐ Signal编码时agent | ● 行业最强档 | ◐ Project+Version对象 |
| Sonatype | ○ 未见专门页 | 自建 | ● SBOM Manager独立产品 | ● VEX注释**跨版本延续** | ○ | — | ◐ | ◐ 升级建议 | ○ | ● SBOM存储/分发 | ◐ SBOM对象为版本 |
| JFrog | ● 专门Compliance Brief | 聚合+自建研究 | ● 构建时自动+绑制品 | ● SBOM富化VEX(声称) | ◐ Contextual Analysis | ◐ | ◐ +Runtime | ◐ 预防(Curation) | ○ | ● AppTrust证据链(声称) | ◐ release/制品版本 |
| GitHub | ○ 无官方页 | 聚合+自建评审 | ◐ 仅导出SPDX | ○ | ○ | — | ◐ EPSS/KEV展示 | ● Dependabot+Copilot Autofix | ◐ copilot | ◐ | ○ |
| GitLab | ○ 未见专门页 | 聚合 | ● SBOM为数据中枢 | ◐ 状态导出 | ◐ **package级(Beta)** | ◐ Py/JS/Java | ◐ EPSS/KEV | ● Agentic修复GA(2026-04) | ● Duo多agent+管控 | ● 合规框架(Ultimate) | ○ |
| Veracode | ○ | 自建+Phylum | ● CycloneDX生成 | ○ | ● vulnerable-method级 | ◐ Java/.NET强 | ● EPSS+KEV(2023起) | ◐ Fix for SCA仍LA | ◐ 单点Fix | ● 企业报告 | ○ |
| Checkmarx | ○ | 聚合+自建研究 | ● 生成 | ○ | ● exploitable path(声称) | ◐ | ◐ ASPM关联(声称) | ● Developer Assist IDE内agent | ● IDE agent | ◐ | ○ |
| Endor Labs | ◐ CRA内容 | 自建(CVE→函数映射) | ● 生成 | ● 输出 | ● **function+call chain证据+容器** | ● 覆盖广(声称) | ● 证据化exploitability | ● Upgrade Impact+Patches | ● AI analyst | ◐ 证据天然贴近审计 | ○ |
| Semgrep | ○ | 聚合+规则 | ● 生成/消费 | ○ | ● **dataflow级** | ● **10+语言(最广)** | ◐ | ● Guardian升级PR | ● Assistant triage(60%自动化,声称) | ○ | ○ |
| Chainguard | ◐ CRA文章 | 不适用(修复方) | ● 制品自带+签名 | ● **公开VEX feed** | 不适用 | — | 不适用 | ● **backport重建制品(范式创新)** | ○ | ● provenance+SBOM | 不适用 |
| Anchore | ○(但工具链是CRA事实标准) | 聚合 | ● Syft事实标准 | ● Grype消费VEX | ○ | — | ◐ EPSS/KEV | ○ | ○ | ● SBOM库存+持续重匹配 | ◐ 制品版本持续跟踪 |
| Aqua | ○ | 聚合(Trivy) | ● Trivy生成 | ◐ Trivy过滤 | ◐ 运行时行为观测 | ◐ | ● 运行时上下文 | ◐ 阻断为主 | ○ | ◐ 运行时合规 | ○ |
| Wiz | ○ | 聚合 | ● 生成 | ○ | ○ **无静态reach.(两源确认)** | — | ● 网络暴露+攻击路径图 | ◐ AutoFix受限 | ◐ | ● 云合规 | ○ |
| Socket | ○ | 行为分析+聚合 | ● | ◐ | ● precomputed函数级(声称) | ◐ | ◐ | ◐ | ◐ | ○ | ○ |
| Arnica | ○ | 聚合 | ● | ◐ | ● function级(2024起) | ◐ | ● EPSS+KEV | ● 身份路由+修复 | ● Arnie multi-agent | ○ | ○ |
| Oligo | ○(聚焦FedRAMP/PCI) | 聚合 | ● runtime SBOM | ● runtime VEX | ● **运行时函数执行观测** | ◐ | ● **runtime truth(最深)** | ○ | ◐ | ● 运行时证据→审计 | ○ |
| Apiiro | ○ | 聚合 | ◐ | ◐ | ● DCA图谱 | ◐ | ● code-to-runtime图谱 | ● AutoFix agent | ● Guardian+AutoFix多agent | ◐ | ○ |
| Finite State | ● 托管CRA服务 | 二进制分析 | ● 出货二进制SBOM | ● 生成 | ○(二进制函数识别有限) | 嵌入式/C/C++ | ◐ | ◐ | ○ | ● PSIRT工作流 | ● **产品/build为对象** |
| ONEKEY | ● CRA专项(webinar/资源) | 二进制分析 | ● 二进制生成/导入 | ◐ | ○ | 嵌入式 | ◐ 威胁建模profile | ◐ | ○ | ● 产品生命周期监控 | ● **产品线为对象** |

---

## 3. 分析 A：能力商品化光谱

### 已高度商品化（2026 年做成不再是差异化）

1. **基础 SCA 扫描与依赖漏洞告警**。Trivy/Grype/Dependency-Track 免费开源 + GitHub/GitLab 平台内置，把基线压到零成本。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕
2. **SBOM 生成（SPDX/CycloneDX）**。Syft/Trivy 是事实标准；CycloneDX 1.7 已 ECMA 标准化（2025-12）；所有商业厂商标配。〔[sources/cra-timeline-standards.md](03-competitive-landscape/sources/cra-timeline-standards.md)〕
3. **EPSS/KEV 信号集成**。Veracode 2023 年已入 API；2026 年是全员标配。〔[sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
4. **自动升级 PR**。Dependabot 开创、Renovate/Semgrep Guardian 等普及。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
5. **dependency/package 级 reachability**。GitLab Beta、Socket(precomputed)、Arnica 都已上线；Endor 自己承认"reachability 已从差异化变成 table stakes"（厂商自述，与市场观察一致）。〔[sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md), [sources/socket-reachability.md](03-competitive-landscape/sources/socket-reachability.md), [sources/gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md)〕
6. **AI triage/降噪 copilot**。Semgrep Assistant 承担 60% triage（厂商声称）；各家的 AI 分类助手趋同。〔[sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
7. **VEX 文档生成/消费的"格式层"**。Grype 消费 VEX、Black Duck VEX Templates、Sonatype VEX 注释——生成与消费的机制已标准化。〔[sources/blackduck-vex-templates.md](03-competitive-landscape/sources/blackduck-vex-templates.md), [sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕

### 正在快速商品化（2025-2026 窗口，半年到一年内将不再是卖点）

1. **function 级静态 reachability（主流语言）**。Snyk（Java/JS/Py GA）、Semgrep（10+ 语言）、Endor、Arnica、Socket 都已到位；但语言长尾（.NET/Go/Rust/C++/动态框架）覆盖参差，Snyk 的 .NET 仍 EA，GitLab 仅 package 级。〔[sources/snyk-reachability-docs.md](03-competitive-landscape/sources/snyk-reachability-docs.md), [sources/semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md)〕
2. **单点 agentic 修复**。GitLab 18.11 GA（2026-04）、Snyk Agent Fix GA（2026-09）、Checkmarx Developer Assist、Black Duck Signal GA（2026-03）——头部厂商已全部交卷；但**可信度指标全行业缺失**：无一家公布 AI 修复的合并率/回归率（pixee.ai 对比指出 Snyk/Checkmarx/Veracode 均未公布，Veracode Fix for SCA 仍 LA）。〔[sources/gitlab-agentic-remediation.md](03-competitive-landscape/sources/gitlab-agentic-remediation.md), [sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md), [sources/github-veracode.md](03-competitive-landscape/sources/github-veracode.md)〕
3. **恶意包/行为检测**。Socket、Veracode(Phylum)、Checkmarx、Snyk 均已补齐。

### 仍有明显创新空间（技术或产品护城河可建）

1. **跨语言、含动态行为的 function-level reachability 的证据化**。公认难点：反射/DI/动态分发导致假阴性（Snyk 与 GitLab 文档均自认）；Endor 的差异化主张是"可达判定必须附可复现 call chain 证据"——"可达性结论→可审计证据"的产品化几乎无人做好。〔[sources/snyk-reachability-docs.md](03-competitive-landscape/sources/snyk-reachability-docs.md), [sources/gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md), [sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md)〕
2. **Exploitability 决策层**：把静态 reachability + 运行时观测（Oligo 的"函数是否真被执行"）+ 网络暴露（Wiz 的攻击路径）+ 威胁情报融合成**一个可辩护的判定**并自动写入 VEX statement。目前是三个阵营各占一块（代码级/运行时级/网络级），无人统一；Oligo 证明了 runtime 证据可改变合规结论（FedRAMP SLA 72h→180d，厂商声称），但未接 CRA。〔[sources/oligo-runtime-compliance.md](03-competitive-landscape/sources/oligo-runtime-compliance.md), [sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
3. **Evidence graph / 合规证据链**。JFrog AppTrust 的"证据与二进制加密绑定 + OPA gate"是最接近的现有实现，但绑在制品仓库生态；把"发现→判定→修复→验证→SBOM/VEX 更新"全链路的决策与依据建成可审计图，面向 CRA 技术文档与监管调取——无人完整实现。〔[sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
4. **Agentic remediation 的可信度基础设施**。验证（构建/测试/回归）、合并率遥测、升级影响预判（Endor Upgrade Impact Analysis 是唯一明确产品化的）、修复证据留存——"agent 修的能不能信"是 2026 年买方核心疑虑，也是 Pixee 等修复优先初创的攻击点。〔[sources/checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md), [sources/endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md)〕
5. **修复即服务 / 制品级修复**。Chainguard 的 backport 重建（干净版本号 + VEX feed + 扫描器互认）开辟了"不修代码、换制品"的路径，尤其对 EOL 依赖（Spring Boot 2.7 的 143 个无补丁 CVE）；该模式向更多生态扩展的空间大。〔[sources/chainguard-libraries-java-ga.md](03-competitive-landscape/sources/chainguard-libraries-java-ga.md)〕
6. **VEX 的生命周期自动化**。Sonatype 的"VEX 注释跨版本复制"是唯一明确产品化的版本延续功能；判定依据自动演化（新 exploit 情报触发 VEX statement 失效/重估）无人做。〔[sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md)〕

---

## 4. 分析 B：定位空白判断

**判断：空白存在但正在收窄——"以 Product/Version 为核心对象、覆盖完整漏洞生命周期闭环、面向 CRA 证据"的现代化产品定位，目前没有厂商完整占据；两端各有半个占位者，中间断层明显。**

证据要点：

1. **AppSec/SCA 阵营（Snyk、Mend、Endor、Checkmarx、GitLab 等）全部是 repo/应用/工作负载对象模型**。十二维度第 12 项全表仅 Black Duck（Project+Version）、Sonatype（SBOM 绑定版本+VEX 跨版本延续）、JFrog（release 制品证据链）达到"部分"，且三家都缺少 CRA 意义上的产品线/支持期/监管报告语义，也无 reachability/修复闭环与版本对象打通。〔对比表；[sources/blackduck-vex-templates.md](03-competitive-landscape/sources/blackduck-vex-templates.md), [sources/aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md), [sources/jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md)〕
2. **产品安全/PSIRT 阵营（Finite State、ONEKEY）确实以产品/build 为对象且 CRA 原生**，但技术路线是嵌入式/固件二进制分析，面向 IoT/OT 制造商：无源码级 function reachability、无 agentic 修复、无开发者工作流。现代软件厂商（SaaS/云原生栈）不会买它们。〔[sources/product-security-camp.md](03-competitive-landscape/sources/product-security-camp.md)〕
3. **运行时证据阵营（Oligo）证明了 exploitability→合规证据的价值，但框架映射停在 FedRAMP/PCI/SOC 2，未接 CRA**；CNAPP 阵营（Wiz/Aqua）的 exploitability 是云资产视角，无产品版本概念。〔[sources/oligo-runtime-compliance.md](03-competitive-landscape/sources/oligo-runtime-compliance.md), [sources/wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md)〕
4. **开源侧雏形存在但无人产品化**：Dependency-Track 的 project/portfolio+VEX 模型证明了对象模型的可行性；独立项目 sbom-sentinel 的自述几乎逐字描述了目标闭环（SBOM 保鲜→可利用性 triage→修复路由→EU 监管证据）。CRA 原生初创（CRACI，2026-05 种子轮）开始出现，说明市场感知已到、供给未到。〔[sources/snyk-cra-dependency-track.md](03-competitive-landscape/sources/snyk-cra-dependency-track.md), [research-log.md](03-competitive-landscape/research-log.md) #1〕
5. **时间窗口论据**：Article 14 报告义务已于 2026-09-11 生效（覆盖存量产品），2027-12-11 全面适用——制造商现在需要的是"哪个产品版本的哪个漏洞、判定了什么、修没修、证据在哪"，而非"这个 repo 有多少 CVE"。现有工具的应答粒度与监管问题之间存在结构性错配。〔[sources/cra-timeline-standards.md](03-competitive-landscape/sources/cra-timeline-standards.md)〕

风险/反方提示：① JFrog（AppTrust）与 Black Duck（制造业案例+VEX Templates）距离该定位最近，若其把对象模型升级为"产品线+版本+支持期"则空白快速收窄；② CRA 执法实践尚未定型，"证据"的监管期望粒度有不确定性；③ 大型平台（GitHub/GitLab）若把 SBOM/漏洞数据以 release 为轴重组，可从下往上吃掉该空间。

---

## 5. 附录：来源索引

所有 source note 位于 [docs/research/03-competitive-landscape/sources/](03-competitive-landscape/sources/)：

| Note | 内容 |
|---|---|
| [cra-timeline-standards.md](03-competitive-landscape/sources/cra-timeline-standards.md) | CRA 时间线、罚则、SBOM 义务、CycloneDX 1.7/BSI TR-03183-2（多源交叉） |
| [snyk-reachability-docs.md](03-competitive-landscape/sources/snyk-reachability-docs.md) | Snyk reachability 官方文档（粒度/语言/局限） |
| [snyk-evo-cos-ga.md](03-competitive-landscape/sources/snyk-evo-cos-ga.md) | Snyk Evo COS GA 新闻稿（agent 编排四环） |
| [snyk-cra-dependency-track.md](03-competitive-landscape/sources/snyk-cra-dependency-track.md) | Snyk CRA 内容评估 + Dependency-Track/sbom-sentinel OSS 基线 |
| [mend-cra-guide.md](03-competitive-landscape/sources/mend-cra-guide.md) | Mend CRA 指南全文要点 |
| [checkmarx-mend.md](03-competitive-landscape/sources/checkmarx-mend.md) | Checkmarx exploitable path/Developer Assist + Mend SCA |
| [blackduck-vex-templates.md](03-competitive-landscape/sources/blackduck-vex-templates.md) | Black Duck 2026.7.0 VEX Templates 官方文档 |
| [blackduck-signal.md](03-competitive-landscape/sources/blackduck-signal.md) | Black Duck Signal 发布/GA + STMicro CRA 案例 |
| [aqua-anchore-sonatype.md](03-competitive-landscape/sources/aqua-anchore-sonatype.md) | Aqua/Anchore/Sonatype 三家汇编 |
| [jfrog-cra-compliance-brief.md](03-competitive-landscape/sources/jfrog-cra-compliance-brief.md) | JFrog CRA Compliance Brief 全文要点 |
| [github-veracode.md](03-competitive-landscape/sources/github-veracode.md) | GitHub(SBOM/Autofix/无CRA页)+Veracode(KEV/EPSS/Fix for SCA/Package Firewall) |
| [gitlab-static-reachability-docs.md](03-competitive-landscape/sources/gitlab-static-reachability-docs.md) | GitLab 静态 reachability 官方文档（package 级/Beta/局限） |
| [gitlab-agentic-remediation.md](03-competitive-landscape/sources/gitlab-agentic-remediation.md) | GitLab 18.11/19.2 agentic 修复 |
| [endor-reachability-framework.md](03-competitive-landscape/sources/endor-reachability-framework.md) | Endor reachability 分类框架与证据主张 |
| [semgrep-supply-chain.md](03-competitive-landscape/sources/semgrep-supply-chain.md) | Semgrep 语言覆盖/Assistant/Guardian |
| [chainguard-libraries-java-ga.md](03-competitive-landscape/sources/chainguard-libraries-java-ga.md) | Chainguard Java GA + CVE backport 范式 |
| [wiz-code-google.md](03-competitive-landscape/sources/wiz-code-google.md) | Wiz Code 能力短板 + Google $32B 收购 |
| [socket-reachability.md](03-competitive-landscape/sources/socket-reachability.md) | Socket 收购 Coana/precomputed reachability |
| [arnica.md](03-competitive-landscape/sources/arnica.md) | Arnica pipelineless/function reachability/Arnie AI |
| [oligo-runtime-compliance.md](03-competitive-landscape/sources/oligo-runtime-compliance.md) | Oligo runtime 证据→合规（FedRAMP SLA 论据） |
| [apiiro-agentic.md](03-competitive-landscape/sources/apiiro-agentic.md) | Apiiro Guardian/AutoFix/Context Graph |
| [product-security-camp.md](03-competitive-landscape/sources/product-security-camp.md) | Finite State/ONEKEY 产品安全阵营（B 分析关键证据） |
| [endor-lifecycle-chain.md](03-competitive-landscape/sources/endor-lifecycle-chain.md) | Endor 全链路官方文档核实（reachability/Upgrade Impact/自动 PR/SBOM·VEX 导出）（§6 使用） |
| [jfrog-contextual-analysis.md](03-competitive-landscape/sources/jfrog-contextual-analysis.md) | JFrog Contextual Analysis 官方文档（多信号 scanner、1/3 不依赖 reachability、逐结果 justification）（§6 使用） |
| [jfrog-remediation-rescan.md](03-competitive-landscape/sources/jfrog-remediation-rescan.md) | JFrog Smart Remediation（CVE/component-based）+ Patched 状态回扫（§6 使用） |
| [snyk-reachability-monitor.md](03-competitive-landscape/sources/snyk-reachability-monitor.md) | Snyk call path + Risk Score + snyk monitor 原文（§6 使用） |
| [sonatype-sbom-vex-workflow.md](03-competitive-landscape/sources/sonatype-sbom-vex-workflow.md) | Sonatype SBOM Manager 官方五步 VEX 工作流 + 跨版本复制（§6 使用） |
| [blackduck-vex-2026-1.md](03-competitive-landscape/sources/blackduck-vex-2026-1.md) | Black Duck 2026.1 VEX 官方文档（CSAF 2.0 profile 5、状态映射、强制 justification）（§6 使用） |

---

## 6. 闭环视角 Gap Analysis（2026-09-21 补充，五家逐项核实）

> 背景：一份二手分析（来源疑似 AI 生成，链接带 `utm_source=chatgpt.com`，本身不采信为来源，见 [research-log.md](03-competitive-landscape/research-log.md) 弃用记录）对 Endor Labs / JFrog / Snyk / Sonatype / Black Duck 五家的"漏洞生命周期闭环"能力做出具体声明。本章逐条以厂商官方文档一手核实，并据此做闭环环节覆盖矩阵。核实结论四级：成立 / 部分成立 / 不成立 / 无法核实。

### 6.1 五家逐项核实结果

| # | 声明（二手分析原文要点） | 结论 | 关键证据（官方原文摘录） |
|---|---|---|---|
| 1 | **Endor Labs**：Dependency Inventory → SCA → function-level Reachability（追踪到具体 vulnerable function）→ Exploitability/Context → EPSS+fix availability+production context 排序 → safe upgrade（含 breaking change 分析）→ 自动 PR → SBOM/VEX 输出 | **成立**（排序因子一项降级为厂商声称） | reachability 文档三档标签含 call graph 逐步证据（"demonstrated by a call graph that illustrates each step between the source code and the vulnerable library"）；call path 官方 9 语言（Java/Python/Rust/JS/Go/.NET(C#)/Kotlin/Scala/Ruby）；Upgrade Impact Analysis 用 "program analysis to directly identify breaking changes" 分三档 remediation risk；自动 PR 有专门文档页；SBOM/VEX 导出支持 CycloneDX/SPDX/VEX（UI/API/CLI），SBOM 含 Endor Patches 的 pedigree patch 数据。"EPSS + fix availability + production context 排序"仅见于营销页。〔[sources/endor-lifecycle-chain.md](03-competitive-landscape/sources/endor-lifecycle-chain.md)〕 |
| 2 | **JFrog**：① Contextual Analysis 对不同 CVE 用不同 scanner，综合 first-party code usage/binary/configuration/invocation/runtime；② 约三分之一 scanner 不依赖 reachability；③ Smart Remediation 支持 CVE-based 与 component-based；④ 修复后 re-scan 把 remediation 状态（patched）带回扫描结果 | **①②③成立；④部分成立** | ①②逐字命中："inspect multiple facets…: first-party code usage of the library, binary compilation, configuration, invocation, and runtime environment"；"**Approximately one-third of JFrog's contextual analysis scanners deliberately don't rely on reachability**…"；且每个结果带 justification（列出 scanner 检测信号）。③："You can remediate in two ways: CVE-based remediation… Component-based remediation…"。④：Patched 状态存在（"Xray adds a Patched status to the contextual analysis vocabulary"），但**仅限 Zero-Touch Remediation 场景**（Catalog patched rebuild / 注册 local patch），非任意修复后的通用重扫标注。〔[sources/jfrog-contextual-analysis.md](03-competitive-landscape/sources/jfrog-contextual-analysis.md), [sources/jfrog-remediation-rescan.md](03-competitive-landscape/sources/jfrog-remediation-rescan.md)〕 |
| 3 | **Snyk**：Reachability 提供 call path 且进入 Risk Score；持续 monitor 在新 CVE 或状态变化时重新评估 | **成立** | "Call path - Allows you to see the path from your code to the vulnerable function to validate the result"；"Reachability is such a contextual factor that will significantly increase the overall score"；snyk monitor 快照后 "notify you about newly disclosed vulnerabilities… **or when a previously unavailable patch or upgrade path is created**"（"状态变化"语义 = 修复可用性变化）。〔[sources/snyk-reachability-monitor.md](03-competitive-landscape/sources/snyk-reachability-monitor.md)〕 |
| 4 | **Sonatype**：Analyze SBOM → Review → **Reachability** → Annotate status → Share VEX/SBOM → Audit SBOM for newly discovered vulnerabilities（回到分析） | **部分成立** | 官方五步为 Analyze → Review → Annotate → Share → Audit，**Reachability 不是编号步骤**——引言只说 "Using reachability analysis, developers determine…"（用户在 SBOM Manager 之外自行分析，产品承接注释）；Share 对象是 annotated SBOM；not_affected 的 justification 为 "should be specified"（建议性，非强制）。VEX 注释跨版本复制获官方文档直接确认。〔[sources/sonatype-sbom-vex-workflow.md](03-competitive-landscape/sources/sonatype-sbom-vex-workflow.md)〕 |
| 5 | **Black Duck**：2026.1 VEX 支持 affected/not affected/under investigation；NOT_AFFECTED 强制 justification；VEX 围绕产品版本持续更新而 SBOM 不变 | **成立**（一处口径修正） | "Known Not Affected — **A justification must be provided** to ensure that the decision is properly documented"（2026.1 Remediating 页）；"**While the SBOM content remains unchanged, VEX allows for on-demand updates regarding the status of vulnerabilities for specific project versions**"（2026.1 VEX 页逐字）；VEX 报告 = CSAF 2.0 profile 5，BD 状态→CSAF 映射表完整（NOT_AFFECTED→known_not_affected、MITIGATED→known_not_affected+inline_mitigations_already_exist、PATCHED/REMEDIATION_COMPLETE→fixed）。口径修正：该状态体系实际 **2025.1.0 引入**（Release Notes），2026.1 文档继承。〔[sources/blackduck-vex-2026-1.md](03-competitive-landscape/sources/blackduck-vex-2026-1.md)〕 |

**与已有结论的冲突与修正**：

- **修正 03 §1.5 第 6 条**：原口径"JFrog Contextual Analysis…非公开 call graph 粒度的 function 级证据"不准确——官方文档显示其对覆盖的 CVE 展示 direct/transitive call chain、call graph 可视化与可复制的函数名/文件路径/行号证据。00 报告 §18.2 的"粒度未验证"口径差异随之解决：粒度现为**官方文档可验证**（function 级 call chain，限已有 scanner 的 1,600+ CVE）。§1.5 评级 ◐ 维持（覆盖率受限、无公开完整 call graph 导出），但证据等级从"厂商声称"升为"官方文档"。
- 其余四条与 §1.1/§1.4/§1.10 一致或补强（Endor 语言清单、Sonatype VEX 跨版本复制、Black Duck VEX 独立 license 均获更硬来源）。

### 6.2 闭环环节 × 厂商覆盖矩阵

粒度：● 官方文档级确认；◐ 部分/限定场景/仅营销页（厂商声称）；○ 无或未见证据。五家均不含 CRA 语义列（见 §4）。

| 闭环环节 | Endor Labs | JFrog | Snyk | Sonatype | Black Duck |
|---|---|---|---|---|---|
| 发现（SCA/情报） | ● | ● | ● | ● | ●（BDSA 自建） |
| 关联（组件↔漏洞） | ● | ● | ● | ● | ● |
| Reachability | ● function 级+call path（9 语言官方清单） | ● function 级 call chain（限 1,600+ 有 scanner 的 CVE；约 1/3 scanner 故意不用 reachability） | ● function 级+call path（Java/JS/Py GA，.NET EA） | ○（产品不做，用户外部分析后注释） | ◐（Coverity 引擎支撑，非重心） |
| Exploitability 判定 | ●（reachability+context，定性） | ● Applicable/Not Applicable + 逐结果机器 justification（五维信号融合） | ◐（Risk Score 上下文因子，非独立判定） | ◐（人工注释判定） | ◐（人工 remediation status） |
| 优先级 | ●（EPSS+fix availability+production context，营销页口径） | ◐ | ● Risk Score | ◐ | ◐（security risk calculation） |
| 修复 | ● Upgrade Impact（breaking change 程序分析）+自动 PR+Patches | ● Smart Remediation 双路径+Zero-Touch patched rebuild | ● 升级 PR+Agent Fix | ◐ 升级建议 | ◐ 指导+Signal |
| 验证重扫 | ◐ | ● Patched 状态+Catalog 对齐 CVE 过滤（限 Zero-Touch）+Rescan Required（新 scanner 触发） | ◐（monitor 快照对比，非修复验证） | ○ | ◐（status 手动流转；global remediation 延续到新 BOM） |
| VEX | ● 导出（CycloneDX VEX/SPDX） | ◐ SBOM 富化 VEX（厂商声称） | ○ | ● 注释（CycloneDX 词表）+跨版本复制 | ● CSAF 2.0 profile 5 报告+状态映射+NOT_AFFECTED 强制 justification |
| 持续监控重评估 | ◐ | ●（新 scanner 上线→Rescan Required） | ●（新 CVE/修复可用通知） | ●（Audit 步骤：SBOM 不变、情报驱动） | ●（VEX on-demand 重生成+global remediation） |
| 证据链 | ◐ call chain 可检查 | ● 逐结果 justification 列信号+AppTrust 证据绑定制品 | ◐ | ◐ | ● justification 强制文档化+审计级报告 |
| Product→Version 对象模型 | ○ | ◐ release/制品版本 | ○ | ◐ SBOM 绑定 application 版本 | ◐ Project+Version，VEX per project version（官方文档级） |

矩阵最关键的三个发现：

1. **"判定→VEX 自动化"是全行业断裂点**。五家没有一家把 reachability/exploitability 的机器结论自动写成带 justification 的 VEX statement：Endor 有 call chain 证据但 VEX 只是导出动作；JFrog 有机器 justification 但不落到 VEX 对象（VEX 仅 SBOM 富化，厂商声称）；Black Duck/Sonatype 的 VEX 状态靠人工标注（Black Duck 强制 justification 但 justification 是枚举+文本，非机器证据引用）；Snyk 无 VEX 产品。机器判定与正式结论之间全部隔着人工搬运。
2. **"验证重扫"首次出现产品化但形态割裂**：JFrog Patched 状态（限 Zero-Touch 场景）与 Rescan Required（scanner 版本驱动）是两个独立机制；Snyk monitor 是"新情报/新修复可用"通知而非修复后验证；无一家实现"修复→重扫→VEX status→fixed"自动流转。
3. **持续监控重评估已有三种产品化模式**（Snyk 快照对比、Sonatype Audit 闭环、Black Duck VEX on-demand 更新+global remediation 延续），但都停在"再发现/再标注"层——**"新情报触发既有 VEX statement 失效重估"无人做**，§3.3.6 的判断本轮核实后维持且证据更硬。

### 6.3 问题 a：Assessment-centric vs Finding-centric，哪家最接近？

**结论：五家全部是 Finding-centric；最接近 Assessment-centric 的是 Black Duck，其次是 JFrog；均不具备 Claim+Evidence+Decision 三件套与自动重评估状态机。**

判据：Finding-centric = finding（CVE 命中）是一等对象，评估结论（reachability 标签、applicability、VEX 注释）是 finding 上的字段；Assessment-centric = Assessment（Claim+Evidence+Decision）本身是一等对象，可版本化、挂机器证据、可被新情报触发失效重估。

- **Black Duck（最接近）**：remediation status 是持久字段且强制 justification 文档化；VEX 按 project version on-demand 重生成（SBOM 不变）——官方文档级确认了"判定围绕产品版本持续演化"的语义；global remediation 把判定延续到新 BOM。**差距**：justification 是枚举+人工文本而非机器证据引用；status 无版本历史与失效机制（新 exploit 情报不会推翻旧 NOT_AFFECTED）；无 Decision 记录（谁、何时、基于什么证据判定）；Revision History 硬编码 draft/v1。
- **JFrog（次接近）**：Contextual Analysis 是五家中唯一承诺"每个判定附机器 justification（列出检测信号）"的——最接近 Evidence 层；Patched/Rescan Required 是状态机雏形。**差距**：justification 绑定 scanner 版本而非独立证据对象；判定不落到 VEX statement；无跨版本延续与自动重评估。
- **Snyk/Endor**：reachability 是 Risk Score 的输入因子或 finding 标签，判定不构成独立对象；**Sonatype**：VEX 注释是纯人工标注（justification 仅 should 级）。

### 6.4 问题 b：与 §4"定位空白"判断是否一致？

**一致，且本轮核实使其更硬；两处措辞精度需修正，方向不变。**

1. **空白判断维持**：五家覆盖了闭环的大多数环节（矩阵中 ●/◐ 占绝大多数格子），但断裂恰好在 CRA 最看重的两处——"机器判定→正式 VEX 结论"的自动化、以及"结论的版本化证据链与失效重估"。这直接印证 §4"中间断层明显"与 §3.3 第 2/3/6 条创新空间判断。
2. **Black Duck"次近占位者"地位补强**：2026.1 文档逐字确认"SBOM 静态 + VEX 按 project version 持续更新"——五家中唯一的官方文档级 Product-Version VEX 生命周期语义；§4 风险提示①（Black Duck 升级对象模型则空白收窄）的紧迫性上升。
3. **措辞修正 1**（JFrog）：§1.5 与 00 报告 §18.2 的"粒度不可验证"口径作废——Contextual Analysis 的判定粒度与证据展示现有官方文档支撑；其"约 1/3 scanner 不用 reachability"的原文揭示了一个 §4 未覆盖的事实：** exploitability 证据的相当一部分本就不在代码里**（配置/CLI/主机属性），这对"Evidence Graph 必须能挂载非代码类证据"是正向论据。
4. **措辞修正 2**（Black Duck VEX 时间线）：状态体系 2025.1.0 引入（非 2026.1），VEX Templates 仍是 2026.7.0——引用时分清两件事。
