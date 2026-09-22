# 07 · 竞争格局与标准生态

> 对应 mvp.md §十八 #15/#16。产出：① 厂商能力矩阵（已核实 vs 公开资料标注）；② "已商品化 vs 仍创新"判断；③ 标准与生态的参与策略。
> 证据纪律：本轮逐一抓取核实的标 ✅（行号=R5/R4/R6 sources），404/未重验的标 [基于公开资料]，营销口径一律保留。

## 1. 竞争地图：五类玩家 × 六域能力（03 §4 能力域）

| 玩家 | 代表 | 强项（能力域 1-6）| CRA 空位（他们缺什么）|
|---|---|---|---|
| **A. 通用 SCA/开发者平台** | Snyk ✅R5#2、GitLab ✅R5#3、GitHub(Dependabot) ✅R6#5、Semgrep ✅R4#3、JFrog/FOSSA/Socket [基于公开资料] | 2 关联、3 判定（reachability/风险分）、4 修复（agent PR 已标配）| 5 报告（事件状态机/SRP）、6 证据图、**产品×版本×支持期台账** |
| **B. 供应链/企业 AppSec 深水区** | Black Duck、Mend、Veracode、Checkmarx、Wiz[Cloud/代码] [基于公开资料；本页面 404/未重验] | 1-2 大规模扫描与组合、6 多为工单而非图 | 3 判定证据质量、5 CRA 报告、产品级模型 |
| **C. Reachability/深度分析专精** | Endor ✅R5#1/R4#1、Oligo ✅R4#4、profile 专精厂商 [基于公开资料] | 3 最深（函数级/runtime）| 5/6 同样缺；且"没有自己的判定工作流"时只是 feature 供应商 |
| **D. 事件响应/SOC** | Prophet ✅R6#3、SIEM/SOAR 系 [基于公开资料] | 5 的**流程形态**（状态机+审批+人工兜底）强 | **不懂 SCA/VEX 语义**；与 CRA 漏洞报告的字段级对接缺 |
| **E. SBOM/合规工具** | SBOM 生成/门户类 [基于公开资料] | 1 生成、5 部分导出 | 2-4 分析判定修复几乎不碰 → **证据空心化** |

**格局判断**：
- 扫描与修复（域 1/2/4）**已商品化**（见 §2）；**域 5 报告 + 域 6 证据**在 5 类玩家里**没有任何一类是强项**——D 类有流程无领域语义，E 类有领域无深度数据，A-C 有数据无合规流程。**交叉空位 = 本产品**（03 §4 空位判断被竞品验证）。
- **2026 Gartner 首发 "Software Supply Chain Security" 魔力象限（客户证言出自 Chainguard 页）[R5#4]** → 品类正在被分析师单独命名，进场窗口与命名权同时存在。

## 2. 逐家速览（已核实源的要点 + 短评）

| 厂商 | 核实到的事实 | 营销标记 | 短评（对我们的意义）|
|---|---|---|---|
| **Endor Labs** ✅R5#1 | 专门的 CRA 合规页：exploitable-not-all、漏洞处理策略、SBOM、patches；reachability 三方法五类型+测试证据 [R4#1] | "90%+ 降噪"等 | **最强的"CRA 话术"对手**——定位与其最接近，必须在证据图/报告状态机上拉出差 |
| **Snyk** ✅R5#2 | Risk Score 融合 reachability+EPSS+exploit maturity；Snyk Evo（AI agent 治理）；llms.txt 已做 agent 友好文档 | Risk Score 内部权重不透明 | 平台宽度碾压；我们打"CRA 深度+证据可下钻 vs 黑箱分" |
| **GitLab** ✅R5#3 | SBOM-based 依赖扫描、Continuous Scanning、Duo 解决 breaking change、libbehave、agentic 分析 | — | 平台捆绑；我们保持多平台（GitHub+GitLab+文件）中立 |
| **GitHub** ✅R6#5 | Dependabot 告警→**指派 AI agent（Copilot/Codex/Claude）→草稿 PR+会话日志**；auto-triage；仅审核过 advisory 触发 | — | **agent 修复的范式制定者**；我们不与其比"会修"，比"修完的证据进 VEX/报告" |
| **Chainguard** ✅R5#4 | SLSA L3 工厂叙事、Agent Skills、Gartner SSC 象限引述 | 象限为客户页转述 | 镜像/构建侧为主，非判定侧 |
| **Semgrep** ✅R4#3 | 12 语言、98% 降噪、Agentic Workflows、Autofix | 98%/95% 营销 | SAST 强，SCA 侧以开发者体验取胜 |
| **Oligo** ✅R4#4 | runtime 内存级 95% 降噪、real-time BOM、production-ready runtime VEX | 95% 营销 | **runtime VEX 是最接近我们 §5 L4 的对手**——PoC-2 要能对话其证据形态 |
| **Black Duck/Mend/Veracode/Checkmarx/Wiz/Sonatype/JFrog/Aqua/Anchore/FOSSA** | 本页 404 或未重验 | — | [基于公开资料]：B 类能力大盘按公开文档描述，**矩阵中标注待重验，不引用其未核实细节做对比结论** |

## 3. 已商品化 vs 仍创新（mvp.md #15 的直接回答）

| 能力 | 状态 | 证据 | 对策略的含义 |
|---|---|---|---|
| Component→CVE 扫描 + 基本报告 | **商品化**（免费/内置都有）| Dependabot 免费+平台内置 [R6#5] | 不作为定价理由 |
| 优先级（CVSS/EPSS/KEV 组合）| **商品化中** | Snyk Risk Score、FIRST 官方 use-cases [R1#12, R5#2] | 只做"可下钻"，不做黑箱分 |
| 函数级 Reachability | **2024-2026 快速商品化** | 四家齐发 [R4]，Endor 自认"变 baseline" [R4#1] | 必须有，不单独立品牌 |
| Agent 修复草稿 PR | **2026 已商品化** | GitHub/GitLab/Semgrep/Endor [R6#5, R5#1#3] | 做，但按 06 §3 安全范式，不吹"首个" |
| SBOM 生成 | 商品化（质量参差）| R2 各源 | 以质量评分+diff 切入 |
| **VEX 判定工作流（状态机+SLA+证据挂载）** | **仍创新/空位** | 四实现多为"格式支持" [R2#3#5#9]；未见"判定工作流"成品 [基于公开资料] | **主差异化 1**（04 §1.2）|
| **CRA 事件报告状态机（24h/72h/14d→SRP 预填）** | **空位** | 义务刚生效 8 天；D/E 类无字段级实现 [基于公开资料] | **主差异化 2（尖刀）** |
| **产品×版本×支持期 模型 + Evidence Graph** | **空位** | GUAC 验证图思路但无 CRA 判定图 [R6#1]；10 年记录义务 [EUR-Lex] | **主差异化 3（壁垒）** |
| 判定的跨厂商互信（机器可读证据+可回放）| **前沿/未解** | 仅 CycloneDX citations 点状 [R2#3] | 长线：标准参与的抓手（§4）|

## 4. 标准与生态：参与策略（mvp.md #16）

### 4.1 标准分四层，投入不同
| 层 | 标准 | 策略 |
|---|---|---|
| **必须实现（导出/导入）** | SPDX(ISO 5962)、CycloneDX(ECMA-424，v1.7 含 declarations/citations)、PURL(ECMA-427，已进 CVE 5.2.0)、CPE 2.3（NVD 桥）、CSAF 2.0、CVSS v4、EPSS/KEV | **Day 1 双格式 SBOM + VEX 多格式导出**；内部模型对齐但不绑定单格式（01 §5.2/6.3）|
| **政策对齐（话术/字段）** | CISA 2026 SBOM Minimum Elements ✅R2#16、CISA When-to-VEX ✅R2#17、ENISA/ENISA SRP | 报告字段与 VEX 理由词表**逐字段对齐官方**，客户审计时可指认 |
| **协调标准跟进（合规推定）** | M/606 / C(2025)618 的 41 项在途标准 ✅R3#6 | 设"标准适配层"（02 §5）；参与行业协会跟踪（买 CEN/CENELEC 消息足够，不必自己写标准）|
| **前沿/生态位（选择性发声）** | GUAC（图）✅R6#1、OpenVEX、in-toto/SLSA（构建侧，弱相关）、CWE Top 25 | 在"CRA 判定证据"议题上争取**话语权**：以客户案例+开放字段 schema（如 evidence.json 公开草案）立标准前哨——**先发格式草案比晚进委员会便宜** |

### 4.2 生态动作优先级（P0-P2）
- **P0（现在做）**：SBOM/VEX 导出对齐 §4.1 第一行全部字段；KEV/EPSS/OSV/NVD 多源接入；事件报告字段对齐 ENISA SRP 公开字段结构（以官方披露为准 [R3#5]）。
- **P1**：MCP server 化（06 §3 问题 8）——让客户 agent/平台能调我们的判定与证据接口（R6#2 验证 MCP 是事实标准）；CSAF 发布通道；与 1-2 个托管/集成商（MSP/合规事务所）结盟。
- **P2**：向 CISA/OpenSSF 类组织提交 evidence schema 草案；跟踪 recital 21 FOSS 自愿认证动向 [EUR-Lex]（未来可能是背书红利）。

## 5. 一页竞合结论（给 09 Q 与 08 定位用）
1. **不与 A 类比宽度**（Snyk/GitLab 平台战是消耗战）；**不与 C 类单点比 reachability 分数**（商品化曲线已确认）。
2. **主战场 = 域 5+6（报告+证据）+ 产品级模型**——五类玩家的交叉空位，且有法规倒计时护航（02 §4.3）。
3. **兼容而非对抗**：Dependabot/扫描器的告警可作为我们的输入（客户已有），我们补它们缺的判定/报告/证据——**"让客户已有扫描器变得可举证"是低摩擦切入话术**。
4. 品类命名权窗口：Gartner SSC 象限元年 [R5#4] + CRA 报告义务生效 8 天——**2026H2-2027 是"CRA-native"叙事的黄金宣发期**（09 Q8）。

---
*未核实厂商的行仅用于结构性分类，不支撑具体功能对比断言；重验计划见 08 章风险表。*
