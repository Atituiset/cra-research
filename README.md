# CRA / SCA 漏洞全生命周期研究

本项目研究如何围绕欧盟《网络韧性法案》（Cyber Resilience Act，CRA），将软件成分分析（SCA）扩展为产品级漏洞管理能力：从识别软件组件、关联漏洞，到判断影响、修复验证、生成报告，持续保留可追溯的证据。

仓库包含**领域与法规研究、竞品分析、产品与技术设计，以及可运行原型**，用于团队讨论产品方向、评估技术可行性和推进实现。

[研究总报告](docs/research/00-final-report.md) · [在线演示](demo/cra_workbench.ipynb) · [当前实施设计](docs/design/unified-workbench.md) · [本地运行](docs/development.md)

## 我们要解决什么问题

扫描器能告诉我们“某个组件关联了哪些漏洞”。产品安全团队还需要回答：

- 哪些已发布的产品版本受影响？
- 漏洞代码是否存在、是否可达，判定依据是什么？
- 谁复核了这个判断？情报或产品变化后是否需要重估？
- 修复是否进入实际发布物，并经过验证？
- 面向客户、审计或报告流程，能否还原当时的判断与处理过程？

本项目以**产品发布物**为主线，把这些问题连接起来：

```text
产品 / 版本 / 发布物
        ↓
组件清单与 SBOM → 漏洞关联 → 可达性与上下文分析
                                   ↓
                             判定与人工复核
                                   ↓
                              处置与修复验证
                                   ↓
                           事件报告与客户应答

贯穿全程：证据来源、对象快照、判定历史和签名记录
```

## 当前方向

以产品发布物为账本，复用现有扫描和分析工具，重点建设判定、复核、重估和证据追溯能力。VEX 是判定的交换载体，证据与历史保存在内部模型中；分析工具、CLI 和展示层共用这套模型。

首版采用本地单实例原型验证上述流程。无调用路径的结果需要结合分析范围复核；旧版本的历史判断不能被新版本修复覆盖；事件报告需记录适用依据和知悉时间。

详细论证见 [研究总报告](docs/research/00-final-report.md)，具体实现取舍见 [当前实施设计](docs/design/unified-workbench.md)。

## 推荐阅读顺序

第一次了解项目，按下面顺序阅读即可；文档和 notebook 均可在 GitHub 页面查看。

| 顺序 | 内容 | 回答的问题 |
|---|---|---|
| 1 | [研究总报告](docs/research/00-final-report.md)，先读 §1、§5、§6 | 为什么做，产品定位是什么？ |
| 2 | [用户旅程](docs/product/journeys.md) | 用户如何完成一次漏洞处置？ |
| 3 | [当前实施设计](docs/design/unified-workbench.md) | 系统如何组织，已经实现哪些部分？ |
| 4 | [已执行的 Jupyter 演示](demo/cra_workbench.ipynb) | 目标评估引擎如何组织，真实样例支持到哪一步？ |

## 专题研究

| 专题 | 内容 |
|---|---|
| [领域知识体系](docs/research/01-domain-ontology.md) | CVE、OSV、SBOM、VEX、CSAF 等概念及其关系 |
| [CRA 法规研究](docs/research/02-cra-regulation.md) | 法规义务与产品能力映射 |
| [竞争格局](docs/research/03-competitive-landscape.md) | 厂商能力、定位与差异化判断 |
| [技术深挖](docs/research/04-technology-deep-dive.md) | 可达性、可利用性、证据图与 Agent |
| [欧盟合规全景](docs/research/05-eu-compliance-landscape.md) | CRA 与相关合规体系的关系 |
| [产品形态与技术栈](docs/research/06-product-forms-and-tech-stacks.md) | 部署方式、开源复用与自研边界 |
| [厂商深挖](docs/research/07-vendor-deep-dive/README.md) | Snyk、Endor、Black Duck、Sonatype、JFrog 的专题分析 |

按角色阅读、来源追溯及历史材料说明见 [完整阅读指南](docs/README.md)。

最新 [架构讨论](docs/chat-history.md) 将通用漏洞评估引擎置于核心、CRA/VEX 置于消费端。Notebook 已按此组织，分别标注已有实测、VA-IR 教学投影和动态编排设计推演；具体代码差距见 [架构对照评估](docs/design/assessment-engine-alignment.md)。

## 已经做到哪一步

目前是**可运行的研究原型**。统一演示导入两个 Go/C 历史样例，包含 **2 个发布物、78 条判定和 154 条签名记录**，导入与导出时重新校验文件 hash 和签名。

| 状态 | 内容 |
|---|---|
| 已实现 | 证据包导入、发布物身份、判定复核、历史保留、显式重估、人工修复复核、事件时钟、外部回执记录、内部应答包导出 |
| 可查看 | [Jupyter 演示](demo/cra_workbench.ipynb)，已保存执行输出，无需安装环境 |
| 下一步 | 分析结果模型规范化、完整原始证据归档、持续情报关联与自动重估、正式 VEX 签发、认证与数据库部署 |

这些样例验证了工程链路，不代表生产环境的分析精度。当前导出为内部复核包，尚不具备完整生产审批与正式报送能力。实现边界见 [当前设计](docs/design/unified-workbench.md)，实验条件见 [PoC 记录](poc/README.md)。

## 仓库结构

| 目录 | 用途 |
|---|---|
| [docs/research/](docs/research/) | 研究报告与来源资料 |
| [docs/product/](docs/product/) | 用户流程 |
| [docs/design/](docs/design/) | 实施设计与决策依据 |
| [src/cra/](src/cra/) | 共享核心、CLI 与展示生成 |
| [demo/](demo/README.md) | 团队演示与生成脚本 |
| [poc/](poc/README.md) | 原始扫描管道、样例与签名证据 |
| [tests/](tests/) | 核心行为验证 |
| [docs/archive/](docs/archive/cra-research-2/README.md) | 第二份研究的历史归档 |

需要运行或修改代码，请看 [开发与运行指南](docs/development.md)。两份研究的合并依据见 [综合评估](docs/design/repository-unification-assessment.md)；当前实现范围以统一实施设计为准。
