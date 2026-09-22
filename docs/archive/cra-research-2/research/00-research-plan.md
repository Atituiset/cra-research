# Deep Research 总计划 — CRA × SCA 漏洞全生命周期产品

## 输入

- `docs/background.md` — 领域知识体系要求（Know the Domain，五层结构第一层）
- `docs/mvp.md` — 产品研究主提示词（法规 / 能力 / 定位 / 技术 / 竞争 / MVP）

## 输出

- `research/` — 中间落盘：每个工作流一个目录，含 `sources.md`（论文/博客/官方发文清单）+ `findings.md`（详细发现）
- `report/` — 最终研究报告（多部分 + README 索引，对应 mvp.md §十八 的 25 项）

## Subagent 预算（429 风险控制）

- **v1（已废弃）**：6 个大子代理（每个 ~30 次抓取）。实测：大任务在 ~6 次抓取后被服务端连接重置（限流/时长上限），并行时两个全灭。
- **v2（现行）**：**小步串行**。每个子代理只做 ≤5 次抓取，**边抓边写**（每抓 1 个来源立即把蒸馏笔记追加进 sources.md）；严格一次只跑 1 个子代理；findings.md 由主会话基于 sources.md 笔记撰写。
- 预计 13~15 个小型串行 fetch-run（R1 续 2 个、R2/R3/R4/R6 各 2 个、R5 3 个）+ 失败重试余量。
- 好处：任何一次被重置都有落盘残留，可无损续跑。

## 工作流分解

| # | 目录 | 主题 | 对应文档章节 | 主要交付 |
|---|------|------|--------------|----------|
| R1 | `01-vuln-intelligence` | CVE/CWE/NVD/OSV/GHSA/Vendor Advisory/CVSS/EPSS/KEV/披露体系/优先级栈 | background.md §二三四五十三；mvp.md §五七 | 情报源对比、Log4Shell 案例、风险决策栈 |
| R2 | `02-standards-sbom-vex` | CPE/PURL/SBOM/SPDX/CycloneDX/VEX(4实现)/CSAF/修复概念/标准生态(OpenSSF/SSDF/SLSA/GUAC) | background.md §六七八九十二十四；mvp.md §十二 | 标准总分类表、VEX 实现对比、选型建议 |
| R3 | `03-cra-regulation` | CRA (EU) 2024/2847 逐条义务、报告时限、CE/标准、FAQ、时间线、法规vs最佳实践区分 | mvp.md §一二；17条证据规范 | Article→Obligation→Activity→Capability 映射表 |
| R4 | `04-reachability-exploitability` | 7 级可达性、语言差异、商业现状（Endor/GitHub/osv-scanner/Semgrep/Oligo…）、exploitability 决策模型 | background.md §十十一；mvp.md §六七 | 语言×技术矩阵、产品能力对比、决策模型 |
| R5 | `05-competitive-landscape` | 15 家厂商 × 11 维度 + 新玩家观察；商品化 vs 差异化 | mvp.md §十一 | 对比矩阵、市场信号 |
| R6 | `06-agent-evidence-graph` | Remediation 自动化、AI fix 产品、LLM agent 论文、MCP/agent 架构 9 问、GUAC/Evidence Graph | mvp.md §八九十 | 架构建议、Evidence Graph 可行性论证 |

## 执行顺序

R1+R2（并行）→ R3+R4（并行）→ R5+R6（并行）→ 主会话审阅中间文件 → 撰写 report/。

## 报告结构规划（report/）

```
report/
├── README.md                     # 索引 + Executive Summary
├── 01-knowledge-map.md           # 第一层 Know the Domain：领域知识地图
├── 02-cra-regulation.md          # 第二层 Know the Regulation
├── 03-problem-capabilities.md    # 第三层 Know the Problem + 能力地图
├── 04-positioning-product.md     # 定位 / 产品形态 / IA / User Journey
├── 05-reachability-exploitability.md
├── 06-remediation-agent.md       # 修复 / AI Agent / Evidence Graph
├── 07-competition-standards.md
├── 08-architecture-mvp-roadmap.md
├── 09-strategic-questions.md     # Q1–Q10 + 建议
└── 10-maps.md                    # 三张浓缩图 A/B/C
```

## 证据规范（所有子代理遵守）

1. CRA 法规结论优先引用 EUR-Lex / Commission / ENISA / CISA / NIST / FIRST / OWASP / OpenSSF / SPDX / CycloneDX / 厂商官方技术文档 / 高质量论文
2. 区分：法规强制 vs 官方解释 vs 最佳实践 vs 厂商实现
3. 厂商营销口径标注 [营销]；无法核实标注"不确定"
4. 每个重要事实带来源 URL；来源冲突要明示
5. 区分 Fact / Interpretation / Hypothesis / Recommendation

## 进度日志

- [x] R1+R2 启动（v1 并行失败→v2 小步串行→v3 主会话直抓）
- [x] R3+R4 启动
- [x] R5+R6 启动
- [x] 中间文件审查（EUR-Lex 关键条款原文已提取：Annex I SBOM"顶层依赖"措辞、5 年支持期、EUR 15M/2.5% 罚金、stewards 免罚）
- [x] report/ 撰写完成（2026-09-20，全部 11 份）
- [x] demo/ Jupyter 全流程演示（2026-09-22：`cra_lifecycle_demo.ipynb` 21 单元 0 错误；`build_notebook.py` 无头重建；`out/` 7 产物；见 `demo/README.md`）

## 报告交付清单（report/）

| 文件 | 状态 |
|------|------|
| README.md（索引+执行摘要+8 关键发现+3 决策建议） | ✅ |
| 01-knowledge-map.md（9 类概念分层/CVE-NVD-OSV-评分/SBOM-VEX-CSAF/心智模型） | ✅ |
| 02-cra-regulation.md（时间线/角色/Annex I 原文/Art.14 报告/强制vs实践口径表/Article→Capability 映射大表） | ✅ |
| 03-problem-capabilities.md（五层不确定性/三买家痛链/六域能力地图/组件级vs产品级模型） | ✅ |
| 04-positioning-product.md（定位三选一/陈述/IA 六域/5 个 User Journey） | ✅ |
| 05-reachability-exploitability.md（L0-L4 层级/四轴证据/语言矩阵/VEX 联动表/PoC-2 验收） | ✅ |
| 06-remediation-agent.md（Fix-Remediation-Verify/九问答案/Evidence Graph schema 与三查询） | ✅ |
| 07-competition-standards.md（五类玩家×六域矩阵/逐家速览/商品化vs空位/标准四层策略） | ✅ |
| 08-architecture-mvp-roadmap.md（五层架构/Phase 0-4/5 个 PoC 含验收标准/风险 R1-R8/开放问题） | ✅ |
| 09-strategic-questions.md（Q1-Q10 证据化回答+章节索引） | ✅ |
| 10-maps.md（图 A 法规→技术、图 B 生命周期、图 C 演进路线） | ✅ |

## 后续研究任务（下一轮）

- [ ] ENISA SRP 实际提交接口/字段 schema（PoC-4 对照需要）
- [ ] M/606 41 项标准时间表与草案公开度
- [ ] B 类竞品（Black Duck/Mend/Veracode/Checkmarx）事件报告/VEX 功能重验（08 风险 R5）
- [ ] 5-10 个目标客群用户访谈（Q6/定价 Q7 验证）

## 执行模式修订记录

- v1：6 个大子代理并行/串行——全部因服务端连接重置失败（限流），仅抢救出 R1 前 6 个来源笔记
- v2：小步串行子代理（≤5 抓取/次）——可行但单次 8-10 分钟，过慢
- v3（最终）：主会话直接并行抓取（4-6 个/轮）+ 增量落盘——速度提升 ~10 倍；大文件（EUR-Lex 全文）存盘后用 grep 提取关键条款；共 6 工作流 ≈50 来源 + 3 学术源
