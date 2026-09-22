# 两份 CRA 研究的综合评估与合一建议

评估日期：2026-09-22。A = 本仓库；B = [第二份研究归档](../archive/cra-research-2/README.md)。本文是合并决策建议，不代表已完成代码迁移或产品实现。依据为两边的报告、设计、PoC/demo 源码和已有输出；未重新运行外部扫描工具，历史实测数字沿用 A 的记录。

## 1. 结论

**以 A 为工程主干，吸收 B 的产品流程和展示层，统一为“以产品发布物为锚点的漏洞判定与处置证据工作台”。**

两边定位没有根本分歧：都从 Component→CVE 扩展到 Product→Release→Judgment→Evidence。真正分歧在首版范围：A 优先解决判定与证据可信，B 优先解决用户如何完成研判、报告和交付。合并应让同一套真实数据支撑完整业务流程，而非保留两套各自生成结论的系统。

建议第一条商业价值主线：**一个产品版本收到漏洞信号后，解释是否受影响，记录处理及复核过程，导出可追溯的客户应答包；需要报告时复用同一批证据形成事件报告草稿。**

## 2. 资产价值与成熟度

| 维度 | A 的资产 | B 的资产 | 合并取舍 |
|---|---|---|---|
| 研究 | 总报告、领域/技术专题、五家厂商深挖与来源笔记 | 十章阅读结构、能力地图、战略问答 | A 作证据底稿，B 作产品叙事组织方式；按论点去重 |
| 工程 | Python 管道、Syft/OSV/govulncheck/Joern 接入、签名与 SQLite | notebook 生成器和 HTML 展示 | A 演进为核心服务，B 演进为核心服务的消费者 |
| 数据真实性 | 两个小样例的工具输出及历史验签记录 | 明确标注的情报、调用图、修复夹具 | 每条记录标记 measured/fixture/manual，禁止混报覆盖率 |
| 用户流程 | CLI、静态报告和人工队列设计 | 五个 Journey、七阶段演示、事件与客户应答包 | 保留 B 的流程，最先实现判定、事件、导出三个薄页面 |
| 证据 | in-toto/DSSE、hash、工具与工件绑定 | 图关系、时间线、快照回放叙事 | 关系模型与不可变证据为真源，图为查询/展示投影 |
| 缺口 | 设计中的产品模型、人签队列、持续重估尚未产品化 | 真实采集、持久化、身份审批、标准输出尚未产品化 | 两边都不是现成 MVP；合并仍需实现共享核心 |

A 的 154 条签名记录证明了特定样例的工程链路，不证明真实产品上的分析精度。B 的人审 actor 字符串与断言展示了流程意图，不等于真实审批控制。

## 3. 必须统一的决策

| 冲突 | 统一建议 | 理由 |
|---|---|---|
| A 单实例内网；B 默认多租户 SaaS | 首版单实例部署，业务层与部署方式解耦 | 已有工程路径更短；多租户不是本轮验证问题 |
| A 最小 MVP 不做事件工作台；B Phase 0 必做 | 加入轻量事件台账、计时、草稿、提交记录；不接自动报送 | 能展示业务闭环，也不把首版变成完整合规平台 |
| A Go+C；B Java+Go | Go 为首条完整真实链，C 保留有条件技术验证；Java 由首批客户决定 | 不因两份路线图叠加而承担三语言建设 |
| A OpenVEX；B CycloneDX 风格 VEX | 内部 Judgment 独立于文件格式，先稳定 OpenVEX，CDX/CSAF 走独立适配器 | 状态和理由词表不能直接复制成另一标准 |
| A statement store；B 图即真源 | PostgreSQL 存对象、关系与历史，证据 blob 内容寻址 | 图语义不要求图数据库；避免第二份状态真源 |
| A Agent 后置；B A1/A2 进入 MVP | 首版确定性规则与人签；Agent 后续只提建议/草稿 | 核心不依赖模型也必须跑通 |

如果首批客户明确要求 SaaS 或 Java，应按客户需求改这些决策；目前不能从研究材料推断客户已验证。

## 4. 合并前需纠正的语义与实现问题

### 4.1 分离分析事实、业务判断和审批

A `poc/pipeline/vex.py` 直接沿用工具的 `not_affected`，缺失 justification 时还默认填 `vulnerable_code_not_in_execute_path`；这与 A 后续设计的“弱证据必须人签”不一致。B `demo/build_notebook.py` 也从无路径提出不受影响，但审批目前只是固定 actor 字符串。

统一要求：

- AnalysisRun 表达 reachable / no_path_found / incomplete / failed，并记录入口、构建配置、工具版本和分析边界。
- Judgment 表达产品上下文中的漏洞状态；Review 表达 proposed / approved / rejected，两个维度分开。
- 无路径不自动签发不受影响；审批也不能替代缺失的技术依据。证据不足继续调查。
- 可达不直接意味着可利用。版本命中、漏洞函数映射和调用路径分别留证。
- `fixed` 必须绑定新 Release 和 Verification；旧 Release 的历史受影响记录不被覆盖。

### 4.2 KEV 不直接启动法定报告时钟

B 演示中“KEV 一命中就触发 24 小时法定报告”需改为“触发高优先级核查”。法定义务涉及制造商知悉产品所含漏洞正在被利用，不能用目录命中代替适用条件判断。记录信号到达、实际知悉、适用性判断和审批时间；人工审批不得重置或推迟已有的知悉时间。

两类报告事件需分开：主动利用漏洞的最终报告期限与纠正或缓解措施可用时间有关；严重事件最终报告期限与 72 小时通知有关，不能共用一个固定 14 天模板。依据：[欧委会报告义务说明](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)、[CRA Article 14 原文](https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng)。法规适用性和模板应保留版本，并由合规负责人复核。

### 4.3 标准文件与演示 JSON 分开

B 的 `vex_doc` 使用 `spec`、顶层 `analysis` 等演示字段，README 也明确称其为“CycloneDX 风格”。不能把 `.cdx.json` 扩展名视为通过标准校验的证据。统一后保留演示视图 JSON，正式文件经对应版本 schema 校验；内部状态到标准状态与理由词表的转换需显式映射。

### 4.4 历史、签名与导出不能只看表面

A 当前 artifacts 唯一键为 product/version/name，尚不足以区分同版本重建；B 在修复步骤修改当前 Judgment 对象，也不能代替持久化的不可变历史。统一增加 release/build 标识、Judgment revision、supersedes、输入快照和策略版本。

A `export.py` 在验签失败时记录 FAILED 后仍继续生成导出物。生产导出应阻断正式交付或明确标记为失败诊断包。签名证明内容与签名者的关系，不证明判定本身正确；正式使用还需密钥信任配置。

### 4.5 研究结论去重也要校正

B `report/06` 将技术文档指向 Annex II，与 A 使用 Annex VII 的口径冲突，应按法规原文修正；“没人做证据图”“Agent 已 GA”等市场概括不能因合并自动升级为已验证事实。统一记录事实/厂商宣称/设计推断/待验证及来源日期。

## 5. 统一核心与接入边界

```text
CLI / 薄工作台 / notebook / HTML
                 ↓ 共享应用接口
产品台账 → 关联 → 分析 → 判定与审批 → 处置 → 验证
                         └────────→ 事件与报告
                 ↓
对象与历史（PostgreSQL）+ 证据文件（hash）+ 签名
                 ↓
OpenVEX / SBOM / 客户应答包 / 报告草稿 / 图与时间线
```

核心对象沿用 A 的 Product→Version→Release，并增加 B 所需流程对象：

| 对象 | 最小约束 |
|---|---|
| Release | 构建/制品 hash、SBOM 快照；同版本不同构建可区分 |
| Association | Release×组件实例×漏洞；原始来源与区间判断依据 |
| AnalysisRun/Evidence | 工具版本、输入输出 hash、范围、完整性、数据性质 |
| Judgment/Review | 状态、理由、证据引用、策略版本、审批记录、历史替代关系 |
| Remediation/Verification | 旧新 Release、修复动作、验证结果及失败原因 |
| Incident/Report | 事件类型、知悉时间依据、截止时间、冻结快照、提交记录 |
| ExportManifest | 固定对象修订号、完整文件索引、校验结果、格式版本 |

存储实现可以先复用 SQLite 验证契约，试点服务按 A 的方案迁移 PostgreSQL。不要把“同 schema 平移”理解成只换驱动：产品版本、人签、历史和事件对象都需要迁移设计。

## 6. 首版范围与验收

**必须交付：** 单产品多 Release、SBOM 摄取、真实漏洞关联、Go 分析、判定与人工复核、修复前后验证、轻量事件台账和草稿、可追溯导出。C 分析为可选适配器；先支持已有扫描结果导入，再扩自有分析覆盖。

**暂后置：** 全面多语言、自动修复 Agent、多租户、独立图数据库、完整合规文档生成、自动向监管平台提交。

验收以行为为准：

1. 一个真实 Go 样例从摄取走到导出，演示页面每个结论均可回到真实证据。
2. 无路径、分析失败、情报缺失分别测试；不能静默降为不受影响。
3. 修复后新 Release 判定改变，旧 Release 及旧报告快照不变。
4. 情报/构建/策略变化能触发重估，保留旧结论及失效原因。
5. 未审批候选不能作为已发布结论导出；篡改证据或签名会阻止正式导出。
6. 事件桌面推演覆盖两类报告时钟；KEV 命中本身不等于自动报送。
7. 标准文件通过对应校验器；fixture 与实测结果在页面和包内可辨识。

## 7. 实际合并顺序

| 步骤 | 具体工作 | 完成条件 |
|---|---|---|
| 1 收敛文档 | 本评估作为决策输入；修改唯一主设计；B 报告作为带来源的补充材料 | 不再同时维护两个冲突的 MVP 范围 |
| 2 固定契约 | 定义上述对象、状态机、证据引用、adapter 输入输出 | fixture 和实测都能进入同一个模型 |
| 3 抽取核心 | 将 A pipeline 的读取/运算/写入拆开，CLI 变薄；保留旧 PoC 基线 | 旧样例能被新核心重放并解释差异 |
| 4 接通展示 | B notebook/HTML 从共享接口或冻结导出读取，移除内部第二套判定 | UI 不再自行“推算”漏洞状态 |
| 5 补业务闭环 | 人签、历史、重估、事件、修复验证、交付包 | 达到上一节验收 |
| 6 试点再扩展 | 一家设计伙伴真实产品试用，测人审时间、证据缺口及关联争议 | 根据实测决定 Java、SaaS 或 Agent 的优先级 |

建议目录（目标结构，不表示已建立）：`docs/research/` 保留证据研究；`docs/product/` 收敛定位与 Journey；`docs/design/` 唯一主设计；`src/cra/` 共享核心和适配器；`demo/` 展示消费者；`tests/fixtures/` 演示样本；`poc/` 保留历史技术实验。

迁移 B 时应保留 report→research 的相对引用，先整体存入 `docs/archive/cra-research-2/` 再逐章吸收；排除 `.venv`，演示输出与真实证据分开。A 保留 Git 主线；B 当前根目录未见 `.git`，应按有来源说明的文件导入处理。旧签名证据按原字节保留，通过外部映射关联新 ID，不重写其 payload。

## 8. 本次评估入口

- A：[总报告](../research/00-final-report.md)、[最小 MVP](minimal-mvp-design.md)、[Agent 架构](vex-agent-architecture.md)、[PoC 实测与边界](../../poc/README.md)。
- A 实现：[VEX](../../poc/pipeline/vex.py)、[存储](../../poc/pipeline/store.py)、[导出](../../poc/pipeline/export.py)。
- B：[产品定位](../archive/cra-research-2/report/04-positioning-product.md)、[Agent 与证据图](../archive/cra-research-2/report/06-remediation-agent.md)、[原路线图](../archive/cra-research-2/report/08-architecture-mvp-roadmap.md)、[报告索引](../archive/cra-research-2/report/README.md)、[原演示说明](../archive/cra-research-2/demo/README.md)、[原演示生成器](../archive/cra-research-2/demo/build_notebook.py)。

本轮仅新增评估，不改两边现有逻辑、不迁移文件。下一项工程工作应是共享数据契约和真实 Go 样例贯通；它能最快验证“两边合一”是否真的减少重复逻辑并提升证据可信度。
