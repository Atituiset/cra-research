# CRA × SCA 漏洞全生命周期产品 · Deep Research 报告

> 研究日期：2026-09-20 ｜ 本报告为产品规划决策输入（周日讨论材料）
> 输入：`docs/background.md`（领域知识体系要求）+ `docs/mvp.md`（产品研究主提示词）
> 中间研究产物：`research/01~06/sources.md`（约 50 个来源 + 3 个学术源，含逐源蒸馏笔记）

## 引用约定

- `[R1#8]` = `research/01-vuln-intelligence/sources.md` 第 8 行来源（余类推）
- `[EUR-Lex 原文]` = Regulation (EU) 2024/2847 官方文本（CELEX:32024R2847，已存盘并提取关键条款）
- `[营销]` = 厂商营销口径，未独立验证；`[不确定]` = 未能核实；`[基于公开资料]` = 依赖研究员领域知识，未在本轮逐一重新验证

## 报告结构

| 文件 | 内容 | 对应 mvp.md §十八 |
|------|------|------------------|
| 01-knowledge-map.md | 第一层 Know the Domain：领域知识地图与心智模型 | #2/#4/#7/#8 |
| 02-cra-regulation.md | 第二层 Know the Regulation：CRA 逐条义务 + Article→Capability 映射 | #2/#3/#14 |
| 03-problem-capabilities.md | 第三层 Know the Problem：传统 SCA 缺口 + CRA 能力地图 | #3/#4 |
| 04-positioning-product.md | 产品定位 / 产品形态 / 信息架构 / 5 个 User Journey | #5/#6/#17 |
| 05-reachability-exploitability.md | Reachability / Exploitability 技术深潜 | #9/#10 |
| 06-remediation-agent.md | 修复自动化 / AI Agent 架构 / Evidence Graph | #11/#12/#13 |
| 07-competition-standards.md | 竞争格局（15+ 厂商矩阵）/ 标准与生态 | #15/#16 |
| 08-architecture-mvp-roadmap.md | 参考架构 / Phase 0-4 / 3-5 个 PoC / 风险 | #18-#23 |
| 09-strategic-questions.md | Q1-Q10 战略问题（证据化回答）| #24/#25 |
| 10-maps.md | 三张浓缩图：A 法规→能力→产品→技术；B 端到端生命周期；C 产品演进路线 | 附图 A/B/C |

---

# Executive Summary

## 一句话结论

**CRA 不是又一个"合规 feature"，而是一次把 SCA 从"扫组件、报 CVE"升级为"产品级漏洞全生命周期平台"的窗口期；但真正决定胜负的不是合规报告生成器，而是"证据质量"——谁能用可审计的证据链把『发现→关联→可达→可利用→修复→验证→合规报告』闭环，谁就拥有 CRA 时代的壁垒。**

## 8 个关键发现

1. **CRA 时钟已经在走**：报告义务 **2026-09-11 起生效**（8 天前），24h 预警/72h 正式通知/纠正措施后 ≤14 天 final report，面向 ENISA 单一报告平台（SRP）；主要义务 2027-12-11 全面适用。且**报告义务覆盖 2027 年之前已投放市场的存量产品**。[R3#1/#4/#5]

2. **CRA 对 SCA 的法律锚点原文**：制造商须"识别并记录产品中包含的漏洞与组件，**包括以常用且机器可读的格式编制软件物料清单（SBOM），至少覆盖产品的顶层依赖**"（Annex I Part II）；支持期默认**不少于 5 年**；违反 Art 13/14 义务罚款上限 **€15,000,000 或全球年营收 2.5%（取高）**。[EUR-Lex 原文]

3. **CRA 不点名 VEX/CSAF/SPDX/CycloneDX**——这些是实现选择而非法律强制。厂商把"全套标准"说成"CRA 要求"是营销话术；但 10 年技术文档保存 + 随时可提交市场监管机构 + 漏洞处理流程举证，事实上要求一套**可机器审计的证据体系**。[R3#4/#6/#7]

4. **"exploitable 而非全部 CVE"是合规解释的关键口径**：CRA 要求处理的是 exploitable vulnerabilities，Annex I 漏洞处理义务限定在支持期内的"有效处理"。这是 Endor 等厂商 CRA 打法的支点 [R5#1 营销]，也是 reachability/VEX 从"高级功能"变成"合规刚需"的法律原因。

5. **传统 Component→CVE SCA 的数据地基在塌**：NVD 2024 年陷入 enrichment 积压后，2026-04-15 起改为 **risk-based enrichment**（仅 KEV/联邦政府软件/关键软件优先），2026-03-01 前的存量 CVE 移入 "Not Scheduled"；SCA 厂商必须自建多源情报（NVD+OSV+GHSA+厂商 advisory），单一 NVD 依赖已不可行。[R1#7]

6. **Reachability 已成 table stakes，差异化转向证据**：Endor Labs 官方判断"reachability 从差异化能力变成基线，新的差异化是证据质量、跨层覆盖与修复能力"；Snyk Risk Score 已纳入 reachability+EPSS+exploit maturity；Semgrep 宣称 98% 降噪；Oligo 用 runtime 内存级证据宣称 95% 降噪。函数级可达 + runtime 证据 + EPSS/KEV 组成新的优先级栈。[R4#1/#3/#4，R1#12]

7. **Agentic remediation 已在平台级 GA**：GitHub Dependabot 告警可直接指派给 AI agent（Copilot/Codex/Claude）自动开草稿修复 PR；GitLab Duo 自动解决依赖升级的 breaking change；Semgrep/Snyk/Endor 全线 agent 化。问题不是"要不要 agent"，而是**如何让 agent 的每个结论挂上确定性证据、并可审计**（Prophet 的"determinations you can audit"+ scoped actions 是产品化范式）。[R6#3/#5，R5#2/#3]

8. **市场空隙**：头部厂商在"扫描器+噪声削减"上激烈竞争（且 2026 年 Gartner 已为 Software Supply Chain Security 单独立象限 [R5#4]），但**以"产品/版本"为一等公民、以"证据链"为数据底座、把 CRA 报告义务内嵌为工作流**的漏洞生命周期平台仍是空位——这正是 mvp.md 设想的 "CRA-native Product Security Platform" 的机会。

## 给周日讨论的 3 个决策建议

1. **定位**：做"CRA-native Product Security / Vulnerability Lifecycle Platform"，以 CRA 合规为楔子进入市场，但产品内核是"产品×版本×漏洞×证据"的生命周期管理（详见 04/09）。
2. **壁垒**：把投入压在两处——①函数级 reachability + 多源情报关联的**证据引擎**；②**VEX 作为一等公民**（既是输出格式、更是"漏洞判断结果"的正式载体，带完整 justification/evidence，详见 01/05/06）。
3. **节奏**：未来 1-2 个月先做 3 个 PoC（详见 08）：① 多源情报关联引擎（NVD 降级下的版本区间匹配+backport 处理）；② 函数级 reachability 原型（Java/Go 优先，验证降噪比与 call path 证据质量）；③ VEX 工作流原型（扫描→证据→VEX 状态→SRP 报告草稿的全链路）。

## 主要不确定性

- CRA 配套实施法案仍在滚动出台（SBOM 格式细化 implementing act、important/critical 类目技术描述 Reg (EU) 2025/2392、协调标准 M/606 41 项在途），产品设计须留出"标准适配层"。
- 厂商能力矩阵中 Black Duck/Mend/Veracode/Checkmarx/Wiz/Sonatype/JFrog 等未在本轮逐一重验（标注 [基于公开资料]）。
- 学术侧"autonomous vulnerability repair"检索为 0 结果——修复 agent 的证据主要来自产品级发布而非论文，成熟度判断依赖厂商口径。
