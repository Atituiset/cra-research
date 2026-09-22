# 文档阅读指南

[返回仓库首页](../README.md) · [查看已执行演示](../demo/cra_workbench.md)

本仓库研究以证据驱动的通用漏洞评估引擎，CRA 是首个业务场景。文档说明目标与实现差距；notebook 同时展示历史实测回放、设计投影和脚本推演，三者明确区分。

最新方向讨论见 [架构聊天记录](chat-history.md) 与 [对照评估：漏洞评估引擎](design/assessment-engine-alignment.md)。其中将通用 Assessment Engine 放在核心、CRA/VEX 放在消费端；这份评估区分了目标架构与现有工作台实现，不代表新引擎已经落地。

所有正文都是 Markdown，在 GitHub 点击链接即可阅读，不需要下载或安装环境。

## 第一次阅读：按这条主线

预计 30–45 分钟，只读下表指定部分即可，不必先翻完整资料库。

| 顺序 | 阅读入口 | 先读哪些内容 | 看完应能回答 |
|---|---|---|---|
| 1 | [架构对齐评估](design/assessment-engine-alignment.md) | §1–3、§5 | 目标是什么，现有实现缺什么？ |
| 2 | [图解阅读版](../demo/cra_workbench.md) | §01–07；实测附录按需读 | Localization、Claim、调度和重估如何衔接？ |
| 3 | [工作台实施文档](design/unified-workbench.md) | 全文，尤其“完成与待续” | 当前代码到底实现了哪些部分？ |
| 4 | [研究总报告](research/00-final-report.md) | §1、§5、§6 | CRA 业务入口与产品动机来自哪里？ |
| 5 | [用户旅程](product/journeys.md) | 全文 | 已有工作台怎样支持用户操作？ |

总报告是研究结论，其中的路线图和产品愿景不等于已实现功能。**当前范围和实现状态以统一实施设计为准。**

## 按角色继续读

| 读者 | 建议路线 |
|---|---|
| 负责人 / 产品经理 | 主线 → [竞争格局](research/03-competitive-landscape.md) → [产品形态与技术栈](research/06-product-forms-and-tech-stacks.md) |
| 研发 / 架构师 | 主线 → [开源生态与集成选型](research/08-open-source-ecosystem.md) → [技术深挖](research/04-technology-deep-dive.md) → [原始 PoC 与局限](../poc/README.md) → [运行说明](development.md) |
| 产品安全 / 合规 | 主线 → [CRA 法规研究](research/02-cra-regulation.md) → [合一评估中的判定与报告纠错](design/repository-unification-assessment.md) → [证据样例](../demo/cra_workbench.md) |
| 初次接触 SCA/CRA 的同事 | 先读 [领域知识体系](research/01-domain-ontology.md) 的 §1，再按需查 SBOM、VEX、Reachability 等概念，随后回到主线 |

## 按问题查资料

| 我的问题 | 对应文档 |
|---|---|
| CVE、OSV、SBOM、VEX 分别是什么？ | [01 领域知识体系](research/01-domain-ontology.md) |
| CRA 义务如何映射产品能力？ | [02 CRA 法规研究](research/02-cra-regulation.md) |
| 竞品已有何种能力？ | [03 竞争格局](research/03-competitive-landscape.md) |
| 可达性、可利用性、证据图怎么做？ | [04 技术深挖](research/04-technology-deep-dive.md) |
| CRA 与欧盟其他合规体系什么关系？ | [05 欧盟合规全景](research/05-eu-compliance-landscape.md) |
| 哪些层复用工具，哪些自己开发？ | [06 产品形态与技术栈](research/06-product-forms-and-tech-stacks.md) |
| 有哪些开源项目可接入评估引擎，哪些已在本仓库验证？ | [08 开源生态与集成选型](research/08-open-source-ecosystem.md) |
| Snyk、Endor、Black Duck、Sonatype、JFrog 的细节与来源？ | [07 厂商深挖索引](research/07-vendor-deep-dive/README.md) |
| 两份研究有哪些冲突、如何统一？ | [合一评估](design/repository-unification-assessment.md) |
| 现有原型如何运行、输出意味着什么？ | [演示说明](../demo/README.md) |

## 哪些是当前方案，哪些是历史材料？

| 文档组 | 定位 | 阅读方式 |
|---|---|---|
| `chat-history.md`、`design/assessment-engine-alignment.md` | 目标架构讨论与差距评估 | 理解当前方向和下一轮验证；不是实现完成说明 |
| `design/unified-workbench.md`、`product/journeys.md` | 当前实施与流程 | 判断实现状态时优先看这里 |
| `research/00–08` | 研究结论和证据基础 | 解释原因；留意文内日期、事实/推断/假设标记 |
| `design/repository-unification-assessment.md` | 合并时的决策依据 | 评估中的“计划”需对照当前实施状态 |
| `design/minimal-mvp-design.md`、`design/vex-agent-architecture.md` | 合并前的工程方案与后续设计参考 | 不直接作为当前任务清单 |
| [第二份研究归档](archive/cra-research-2/README.md) | 原报告、来源与模拟演示 | 有需要时回溯；其中的旧 MVP 和旧演示口径不覆盖当前方案 |
| `background.md`、`mvp.md` | 最初的研究任务输入 | 是提出的问题与要求，不是成果或完成清单 |
| 各专题 `sources/`、`research-log*` | 来源摘录与研究过程 | 核实某条结论时沿引用进入，不必顺序通读 |

两份报告目前通过统一阅读入口和实施设计衔接，尚未逐章改写成一本完全去重的报告。讨论中遇到冲突时，请同时标出原文位置与当前设计对应段落，避免把研究建议当作已实现事实。
