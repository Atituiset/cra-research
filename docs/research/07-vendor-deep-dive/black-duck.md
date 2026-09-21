# Black Duck 厂商深度技术调研（Competitive Deep Dive）

- 调研日期：2026-09-21
- 调研对象：Black Duck Software, Inc.（原 Synopsys Software Integrity Group，2024-09-30 完成剥离，Clearlake Capital / Francisco Partners 控股，对价 $1.65B——Synopsys 10-K Note 3 Discontinued Operations）
- 前序基础：`docs/research/03-competitive-landscape.md` §1.3 与 §6（VEX 状态机 2025.1.0 引入、NOT_AFFECTED 强制 justification、VEX 围绕 project version 持续更新、CSAF 2.0 profile 5、Signal GA）。本文不重复，只做加深与修正。
- 事实分级：**Fact**（官方文档/公告逐字级）／**Interpretation**（基于事实的推断）／**Hypothesis**（待验证推测）。营销页一律标（厂商声称）。
- 主要一手来源：docs.blackduck.com 经 khub API 抓取（方法见 `../03-competitive-landscape/research-log.md` #22），原始抓取存于 `sources/`。

## 0. 本轮要点（TL;DR）

1. **Snippet 匹配的实现细节首次拿到官方文档级描述**：滑窗 "codeprints"（单向加密哈希）+ 统计采样上传 KB 匹配；典型 5–7 行有效代码可产生匹配，最短 1 行（高密度 JS）到 20+ 行（短行）；只分析每文件前 1–4MB（默认 1MB）；snippet 匹配**不进 BOM 除非人工确认**，且**纯 snippet 匹配出的组件不计入漏洞统计**。
2. **Air-gapped KB 是"月度整库搬运"模式**：GCP bucket 下载约 5TB 工件（KB 数据约 2TB），要求 64 核/256GB/35TB SSD 服务器 + 8TB 可移动介质，每月全量替换数据卷；且 air-gapped 版明确缺失 fuzzy matching/MaaS、scan correlation、big data（实际 license 文本/版权/深层 license）、自动 BOM 重算、AI 辅助文档。
3. **LTS Project Version 是最接近 CRA "已发布产品版本持续监控"语义的现成实现**：转换即自动生成 SBOM、不可回退、剥离扫描/源码/snippet 等开发期数据只留 BOM 级漏洞追踪，集中式 component catalog 架构；但**通知/告警集成尚未支持 LTS**（官方文档写明 "Coming soon"）。
4. **Signal 的架构比营销口径具体得多**：7 个 LLM agent（5 chat + 2 embedding）流水线、逐 agent 可选模型/提供商、BYOLLM 支持断网内网 LLM 代理；其 **SCA agent 目前只做 Python（supervisor + pip-audit 子 agent + KB 子 agent）**；"验证"靠 oversight-agent 假阳性复核 + 实验性的 synthesis agent + PoCKit 主动利用验证。
5. **Reachability 口径修正**：hub 文档中 "Vulnerability impact analysis" 是 **Detect 生成 Java 调用图 → SHA-1 哈希 → KB Function Signature Match Service 比对 BDSA 携带的受影响 public 方法名**，仅 Java、仅对有方法名元数据的 BDSA 有效；文档自己声明"reachable ≠ 必然受影响，未标 reachable ≠ 安全"。03 报告"Coverity 引擎支撑"的说法在本轮官方文档中未获印证，应修正为"Detect+KB 函数签名匹配（Java）"。
6. **KB 更新作业的自曝局限直接命中我们 §6 的空白判断**：BDSA↔CVE 标识符切换会**重置 remediation status 与 comments**（官方承认，roadmap 承诺修复中）；score/severity 变化静默更新、无通知无审计日志——"新情报触发既有判定失效重估"在 Black Duck 内部同样是断点。

## 1. KnowledgeBase（KB）：规模、策展、离线分发

### 1.1 规模与更新频率

- **Fact**：官方文档口径（hub "About Black Duck KnowledgeBase components"，2026 latest 版）：KB 自 2003 年起爬取，**900 万+ 唯一组件、来自 5 万+ 站点、26 万+ 活跃追踪漏洞、2,900+ 唯一 license**（含全文与数十个编码属性/义务）。〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md)〕
- **Fact**：营销页口径（2026-08）：8.7M 组件、57,700+ forges/repositories、3,000+ license（厂商声称）。2025-10 datasheet 口径：317,000+ 漏洞、426,000+ 受影响组件版本、10M+ 项目（第三方对比站引用）。**注意官方文档（9M 组件/260K 漏洞/2,900 license）与营销页（8.7M/3,000 license）数字互相不完全一致**——两组数字抓取时间相近，差异原因不明（统计口径不同，不确定）。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md)〕
- **Fact（更新节奏）**：KB 服务页逐字："New vulnerability data is added to the KB **hourly**; new searchable open-source components are added **daily**; and new **signatures** for matching are added **2-3 times per week**. Other big data services are updated **quarterly**."〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "KnowledgeBase service"〕
- **Fact**：KB 托管在 GCP（北美/欧洲/亚洲三实例，可强制锁定区域、可禁用故障回切）。〔[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md), "Black Duck on-premise architecture overview"〕

### 1.2 策展团队与情报生产（CyRC + BDSA）

- **Fact**：BDSA 由 Black Duck Cybersecurity Research Center（CyRC）策展，官方文档明确其与 NVD 的差异：交叉核验受影响组件版本、"If a BDSA is not linked to a CVE record, it means further research has determined that the component is not impacted"（即 BDSA 会做**否定性确认**）、禁运（embargo）漏洞有 "Under Review" 状态（可持续 6–9 个月甚至一年）。〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "Black Duck Security Advisories"〕
- **Fact（重要——KB 也在 AI 化）**：BDSA 现有三类**自动化/AI 生产**的 advisory 标签，文档逐字：
  - **ASA（Automated Security Advisory）**：由 CyRC 用自动化 AI 工具从 GHSA 等可信 feed 自动创建 + AI 自动审核；
  - **AI Assisted**（已废弃标签）：AI 生成、未经 BDSA 团队独立验证；
  - **Rapid Review**："produced en masse to expand our BDSA coverage for lower popularity components… created with AI and automation assistance, including generating the text description. **These have not been researched independently by our Vulnerability Analysis team but have been verified for affected component version ranges.**"
  - **Interpretation**：Black Duck 的情报生产已从纯人工策展转向"人工策展核心 + AI 批量扩面"的双层结构；Rapid Review 的验证范围明确收窄到"受影响版本区间核验"，文本描述是 AI 生成——这是其情报质量的边界声明。〔同上〕
- **Fact**：CyRC 有真实原创漏洞研究产出记录（Heartbleed BDSA-2014-0028、Zephyr RTOS 系列 CVE、Mediatek/Realtek/Atheros 芯片组、IKEA TRÅDFRI 等，多由 Defensics fuzzing 团队产出），且 CyRC 研究被定位为 ContextAI 的 "human-verified intelligence" 来源。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #5〕

### 1.3 Air-gapped 离线分发机制（重点）

- **Fact（交付机制）**：断网客户通过 **GCP bucket（gs://kb-onprem-us/YYYY.MM/）月度发布**获取整库：工件分三类（KBServices / BlackDuck / Orchestration）+ Data（kb_search solr 索引、kb_spider_api、snippet_db、ikb_match、fingerprints 等 tarball）。下载需 Black Duck Support 签发的服务账号 key（kb-onprem.json）激活 gcloud。**总下载量约 5TB**，官方建议隔夜下载 + tmux 并行解压；拷贝到断网环境用 ≥8TB 可移动介质。〔[sources/blackduck-kb-airgap.md](sources/blackduck-kb-airgap.md)〕
- **Fact（硬件门槛）**：Air-gapped KB 服务器要求 Ubuntu 20.04+、**64 核 CPU、256GB RAM、35TB SSD**（挂 /var/lib/docker，可扩展）；KB 服务以 Docker Compose/K8s Helm 运行，与 Black Duck SCA 实例解耦，**一个 air-gapped KB 可服务多个 SCA 实例（one-to-many）**。〔同上〕
- **Fact（更新模式）**：月度全量更新 = 删旧数据卷（kb_pg_api、kb_api_snippet 等）→ 拷贝新数据 → 重建挂载；bucket 保留当前 GA + 前两个版本。无增量更新通道（文档未提及任何 delta 机制）。〔同上，FAQ〕
- **Fact（air-gapped 功能削减清单，Hosted vs Air-gapped 对照表）**：
  - 无 big data 基础设施：File Level License Data、Copyright Data、**Actual License text**、Deep License Data 全部不可用（Notice Report 只剩模板 license 文本）；
  - **Fuzzy matching 与 Match Correlation 不支持 air-gapped**（"Understanding component matching" 页明确注记）；SCASS、MaaS、Scan correlation、AI Model Scanning 为 hosted 云侧能力（SCASS 在表中标注 "Coming in 2026"）；
  - **KB 更新后 BOM 不自动重算**："For air-gapped KB deployments, this refresh is not automatic—projects must be re-scanned or scans manually unmapped and remapped after KB updates"；
  - AI 辅助文档服务在 air-gapped 强制回退到 legacy 文档。〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "Hosted vs Air-gapped KnowledgeBase"；[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md), "Configuring AI-Assisted Documentation Service"〕
- **Interpretation**：air-gapped KB 是"月度时间快照 + 功能阉割"模式，与 hosted 的"实时流式更新 + 云侧匹配服务"差距在拉大（MaaS/SCASS/correlation 这些新匹配架构全部是云原生）。断网部署是 Black Duck 的历史强项，但其架构演进方向（匹配逻辑上移 KB 云）与断网场景存在结构性张力——**MaaS 时代 air-gapped 匹配质量可能系统性落后**（Hypothesis，文档只确认功能缺失，未给出质量对比数据）。

### 1.4 数据流与隐私边界（对 KB 架构理解的补充）

- **Fact**：扫描侧只上传签名（"one-way, encrypted MD5 or SHA1 hashes of file system meta-data and file content" + 文件路径/大小，JSON over HTTPS），源码不离场（除非显式开启 source upload，AES-GCM-256、客户自持密钥加密主密钥、默认 180 天保留期可配）。匹配过程客户数据不持久化、不留日志。KB Feedback Service 把用户人工纠正的匹配结果作为匿名 "vote" 回传改进匹配（可关闭）。〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "KnowledgeBase service" / "About the KnowledgeBase Feedback Service"；[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md), "Data retention policy"〕

## 2. 检测引擎：signature / snippet / binary

### 2.1 Signature scanning

- **Fact**：Signature Scanner 对文件与目录生成签名（SHA-1 与 "clean SHA-1" 两级，另有目录结构签名），发到 KB 匹配服务（`/kbmatch/api/v1/matches/...`），KB 返回匹配组件 GUID，再取元数据。支持 approved signature lists（按扩展名白名单控制上传哪类签名）。〔[sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "Approved signature lists"；[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "KnowledgeBase service"〕
- **Fact（Reduced Persistence Signature Scanning）**：未匹配文件默认**不再落库**（曾经是数据库体积最大消耗者与扫描耗时大头），全局/项目/单次扫描三级保留策略；但 snippet-only 扫描、custom signatures 等功能**强制要求保留未匹配文件**——自定义签名匹配本质是把"本组织其他项目扫描过的未匹配文件"当作内部组件指纹库（限定目录深度默认 5 层）。〔[sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "About Reduced Persistence Signature Scanning" / "About custom scan signatures"〕

### 2.2 Snippet matching（本轮最重要的实现细节收获）

- **Fact（机制）**：对未匹配文件做第二遍扫描，用**滑窗算法在文件内容上生成 "codeprints"（单向加密哈希）**，"a statistically relevant sampling of those codeprints is sent to the Black Duck KnowledgeBase"；匹配服务先做整文件精确匹配再查 snippet，**滑窗哈希天然支持 fuzzy match（改动过的文本也能命中）**；结果经启发式选"best match"并给出备选。
- **Fact（最小匹配单位）**："Typically, **five to seven lines** of average source code can generate a match depending upon the density of non-ignored characters"；忽略空白/tab/无信息字符；**一行高密度代码（如某些 JS 库）即可匹配；很短的行可能需要 20+ 行**。即匹配单位不是固定行数而是**信息密度驱动的窗口**。
- **Fact（规模上限）**：只分析每文件**前 1–4MB**（默认 1MB，系统设置可调）。
- **Fact（与 BOM/漏洞的关系——重要边界）**：
  - snippet 匹配**不自动进 BOM**，必须人工 review 确认（匹配按 KB 排名→license 风险→最早版本→匹配版本数最多 的启发式排序给建议）；
  - **"Black Duck does not include any vulnerabilities related to components/versions that are identified through snippet matching only"**——纯 snippet 匹配的组件不计漏洞数、不进漏洞报告（除非同一组件同时被精确匹配命中）；
  - 高亮显示的匹配区域"只是近似"（滑窗哈希性质决定）；
  - 部分 snippet 的确认结果默认**不在重扫时保留**（需手动开启 "Apply IDs from partial snippet matches to new exact file matches"）；
  - **snippet 扫描不能离线完成**（必须与 Black Duck 服务器通信；air-gapped KB 自带 snippet_db 数据集，断网场景走本地 KB——两个说法针对不同部署形态，不矛盾）。
- **Fact**：snippet 支持约 130 种扩展名（含 .c/.h/.cpp/.s/.asm/.vhd/.vhdl、CUDA .cu 等嵌入式相关）。〔以上均见 [sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "About snippet matching" / "Snippet extensions"〕
- **Interpretation**：snippet 引擎的设计哲学是"高召回 + 人工确认闸门 + 漏洞不传导"——它把 snippet 明确定位为**license 合规工具**而非漏洞检测工具。漏洞统计排除纯 snippet 匹配这一条，意味着 Black Duck 的"漏洞数"指标相对其真实代码复用暴露面是**系统性低估**的。

### 2.3 组件匹配的新架构：MaaS / SCASS / fuzzy / correlation

- **Fact**：组件识别现在是三层：**PURL 精确匹配 → fuzzy matching（名称/namespace 变体、版本归一化）→ Match Correlation（多扫描技术结果互证）**；架构上由 KB + **Match as a Service（MaaS，匹配逻辑从 BD 服务器移到 KB 侧）** + **SCA Scan Service（SCASS，scass.blackduck.com，云侧扫描执行）** 组成。fuzzy/correlation **不支持 air-gapped**。〔[sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "Understanding component matching in Black Duck SCA"；[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md), "Considerations for SCASS"〕
- **Fact**：SCASS 的云迁移引发过客户安全疑虑，官方专门发文澄清"传输数据无变化，只是内部处理改为后端执行；二进制/容器扫描尚未纳入 SCASS"。〔同上〕

### 2.4 C/C++ 与固件场景

- **Fact（C/C++ 三条路径）**：
  1. **Black Duck C/CPP Tool**：用 **Coverity Build Capture** 包裹构建过程，记录编译器/链接器实际用到的所有源文件、头文件、目标文件路径，再做签名匹配——解决"对 build 目录盲扫导致漏配/假阳性"的痛点；
  2. **Detect Clang detector**：读 `compile_commands.json`，对每条编译命令加 `-M -MF` 重跑得到依赖文件列表，再用 **APK/DPKG/RPM 包管理器反查文件归属包**——仅限 Linux 且只能发现已通过系统包管理器安装的组件；
  3. **Conan detector**：解析 conan.lock / `conan graph info`，构造 `<name>/<version>@<user>/<channel>#<recipe_revision>` 形式的 KB external ID（可叠加 package_id/package_revision 精确匹配）；自定义 user/channel 的 Conan 包匹配不上 KB。〔[sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "Black Duck C/CPP Tool"；[sources/blackduck-detect-cpp-embedded.md](sources/blackduck-detect-cpp-embedded.md)〕
- **Fact（Yocto/嵌入式）**：Detect 有 **BitBake detector**——source `oe-init-build-env`、跑 `bitbake-layers show-recipes` 与 `bitbake -g {package}` 生成 task-depends.dot 依赖图，用 license.manifest 排除 build 依赖、排除 native/virtual recipe。已知缺陷（官方 troubleshooting 自曝）：**Yocto Package Revision Service 会把 package revision 递增到 KB 里不存在的值导致匹配失败**。〔[sources/blackduck-detect-cpp-embedded.md](sources/blackduck-detect-cpp-embedded.md), "BitBake support"〕
- **Fact（固件/二进制，BDBA）**：BDBA 支持"virtually any compiled software, firmware, mobile applications, installer formats"，匹配方式包括二进制元数据、jar manifest/checksum、包管理器数据等，UI 会标注每个文件命中的匹配方法；支持 Vendor Components "自教"专有组件（不共享进公共库）。单文件上限：Web UI 8GB、API 无限制、hub 集成场景默认 100GB 可调。BDBA 有独立漏洞库更新通道（bdba.blackduck.com/updates-v2/，NVD 元数据日更、BDSA 小时更），断网可手动周更，**离线超 30 天会出现漏洞数据空洞需全量同步（同步期间扫描停止 10–30 分钟）**。〔[sources/blackduck-bdba-install.md](sources/blackduck-bdba-install.md)；[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md), "About Black Duck - Binary Analysis" / "Increasing the size of the binary scan file"〕
- **Interpretation**：C/C++/固件恰是 CRA 覆盖最深的制造业主战场，Black Duck 在此的布局（Build Capture + BitBake + BDBA + snippet 嵌入式语言覆盖）是全行业最完整的；但每条路径都有明确已知缺陷（PR service 版本漂移、Clang 仅限 Linux 包管理器、Conan 自定义 channel 失配），C/C++ 的 BOM 准确性仍高度依赖"构建过程可观测性"。

## 3. Project+Version 对象模型：与 CRA 粒度的距离

- **Fact（模型全貌）**：Project（项目）→ Project Version（一级对象，有 phase：In Planning/In Development/Pre-release/Released/Deprecated/Archived）→ BOM（由映射到该版本的 scan 聚合而成，scan↔version 是多对一映射关系）。Version 有 release date、distribution、nickname 等字段；Project Group 是多级树（可映射业务单元），VEX/SBOM 的组织级字段（publisher、namespace、legal disclaimer）从 Project Group 继承，多项目报告取**最近公共祖先**的字段值。〔[sources/blackduck-project-version-model.md](sources/blackduck-project-version-model.md)；[sources/blackduck-vex-state-machine.md](sources/blackduck-vex-state-machine.md), "How VEX Fields Are Determined in Global Reports"〕
- **Fact（跨版本知识延续的三种机制）**：
  1. **Component Adjustments（persistent edits，默认开启）**：对一个版本里组件的调整自动传导到该项目所有其他版本（Archived 与手工添加组件除外）；开启/关闭时机不同会产生反直觉的传播语义（文档给了三个 scenario 示例）；
  2. **Cloning**：以既有版本为 baseline 克隆 component edits、remediation details（status/target/actual date/comments）、license fulfillment 到新版本——这是"版本升级时判定延续"的主机制；
  3. **Global remediation**：对某漏洞设全局默认 remediation status，自动应用到**新出现**的 BOM 实例（不回溯既有 BOM）。
- **Fact（Archived 语义）**：Archived 版本锁定 BOM 不受 KB license 数据变更影响、不参与风险计算、策略规则不再评估——但**KB 安全漏洞更新仍会应用到 Archived 版本**。〔[sources/blackduck-project-version-model.md](sources/blackduck-project-version-model.md), "About project version phases"〕
- **Fact（LTS——本轮新发现的重点）**：2025 起新增的 **LTS project version** 专为"已发布、不再重扫、只需持续漏洞监控"的软件设计：转换时自动生成 SBOM 供对外分发、**单向不可逆**、剥离开发期数据（源码信息、扫描/匹配类型、snippet、IaC、恶意软件信息、comments、license 冲突/版权/deep license、漏洞 triage 信息、BOM 自定义字段、AI models）；采用**集中式 component catalog**（组件数据存一份、多版本共享引用）支撑海量版本规模；多 origin remediation 记录在转换时合并、保留最严重状态、comments 拼接。**短板：LTS 不支持通知/告警集成（"Coming soon；top priority"），KB 更新作业对 LTS 用"增强架构"但无审计级通知。**〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "Knowledge Base Interaction with Active and LTS Project Versions"；[sources/blackduck-project-version-model.md](sources/blackduck-project-version-model.md), "About Long-Term support (LTS) projects" / "Converting a project version to LTS"〕
- **Interpretation（与 CRA "product with digital elements" 的距离）**：Black Duck 的对象模型距 CRA 粒度比 03 报告评估的更近了一步——LTS version ≈ "投放市场的产品版本 + 持续监控"，phase=Released/Deprecated/Archived + release date + distribution ≈ 生命周期状态机，Project Group ≈ 产品线/组织归属，转换即出 SBOM ≈ 上市时证据固化。**仍然缺**：支持期（support period/EOL 日期）字段、CRA 意义上的监管报告对象（24h/72h/14d 上报）、VEX statement 的版本历史与失效机制、以及"产品"作为跨项目组合的一等公民（subproject 机制可拼装产品 BOM，但策略违规在 subproject 内不上浮、无权限者不能下钻——产品级证据链会被权限模型切断）。
- **Hypothesis**：Black Duck 若在 LTS 上补通知 + 把 VEX 绑定 LTS version 做持续重生成，就是现成的 CRA 上市后监控产品骨架；它离这一步只差产品化包装。

## 4. VEX 状态机与 CSAF 映射（加深）

03 报告 §6 已确认主干。本轮补充的**完整状态机与边界**：

- **Fact（11 态完整表）**：New / Needs Review / Known Affected / Known Not Affected / Mitigated / Patched / Remediation Required / Remediation Complete / Under Investigation / Duplicate / Ignored。其中参与安全风险计算的：New、Needs Review、Known Affected、Remediation Required、Under Investigation（注意 **Under Investigation 计入风险**——保守取向）。〔[sources/blackduck-vex-state-machine.md](sources/blackduck-vex-state-machine.md), "Remediating security vulnerabilities"〕
- **Fact（justification 枚举 = CSAF 语义对齐）**：NOT_AFFECTED 的五选一 justification（component_not_present / vulnerable_code_not_present / vulnerable_code_cannot_be_controlled_by_adversary / vulnerable_code_not_in_execute_path / inline_mitigations_already_exist）与 CSAF flags 一一对应；Known Affected 强制填 remediation 枚举（mitigation / no_fix_planned / none_available / vendor_fix / workaround）。Target/Actual Date、Comments 自由文本。
- **Fact（CSAF 映射全表，官方文档原表）**：

| BD 状态 | CSAF VEX status |
|---|---|
| AFFECTED | known_affected |
| Duplicate | 不进报告 |
| Ignored | 不进报告 |
| MITIGATED | known_not_affected + justification inline_mitigations_already_exist |
| NEEDS_REVIEW | under_investigation |
| NEW | under_investigation |
| NOT_AFFECTED | known_not_affected |
| PATCHED | fixed |
| REMEDIATION_COMPLETE | fixed |
| REMEDIATION_REQUIRED | known_affected |
| UNDER_INVESTIGATION | under_investigation |

- **Fact（文档生成层的硬编码与限制）**：VEX 报告只实现 CSAF v2 profile 5 的**最小必需元素**；Revision History 只写一条、Number/Version 硬编码 1；Status 硬编码 draft（文档注明未来可能支持 final/interim）；Title 不可改；publisher 取 Project Group SBOM 字段，默认值 "COMPANY NAME" 会触发警告。VEX 是**独立 license 模块**（registration key 控制）。〔[sources/blackduck-vex-state-machine.md](sources/blackduck-vex-state-machine.md), "VEX (global reports)"〕
- **Fact（新增，本轮修正点）**：VEX 报告分**两级**——Project Version VEX（单个版本）与 Global VEX（跨项目，含 project phases 过滤）。两者都走 CSAF 2.0 + Template（2026.7.0 VEX Templates）。〔同上，两个 VEX 主题〕
- **Interpretation**：VEX 状态机是"**展示层状态机**"——状态是持久字段但没有状态转移历史、没有失效触发器（新 exploit 情报不会自动推翻 NOT_AFFECTED）、没有判定者/时间/证据三元组；CSAF 导出是快照不是流。03 §6 的"判定围绕产品版本持续演化"结论不变，但本轮看清了演化的载体是"**字段就地更新 + 按需重出报告**"，而不是 statement 版本链。

## 5. Signal（agentic 修复）架构深拆

### 5.1 产品形态与接入

- **Fact**：Signal 分 Developer（编码时，扫自己的改动）与 Enterprise（CI 扫全项目，SARIF 输出到 Polaris 或任何 SARIF 平台）。接入面：Signal CLI（独立二进制）、**MCP server（npm 包 `@black-duck/mcp-server`，stdio 传输，注册进 Claude Code/Codex/Cursor/Gemini/Copilot/Windsurf/JetBrains）**、Code Sight VS Code 扩展、Bridge CLI（FILES/UNCOMMITTED/branch-diff/full-project 四种扫描模式）。默认模型 claude-sonnet-4-6，经 Black Duck 托管 LLM Gateway（llm.core.blackduck.com）调用。〔[sources/blackduck-signal-docs.md](sources/blackduck-signal-docs.md)〕
- **Fact（"编码时拦截"的实际形态）**：不是 pre-commit hook 式拦截，而是**开发者/编码 agent 通过 MCP 工具调用触发扫描**——"用户问 Copilot/Claude 扫代码，编码助手自己把请求路由给 Signal"；也可由 Bridge CLI 进 CI。即 Signal 把自己做成**编码 agent 的工具**，而不是守门员。修复落地"至多创建需要人工批准的 merge request"，Signal 不直接改代码。〔同上，"AI security, data protection, and trust"〕

### 5.2 七 agent 流水线（官方文档级架构）

- **Fact**：Signal 内部为 **5 个 chat agent + 2 个 embedding agent**，每个 agent 独立的模型/提供商/超时配置链：
  - **singlefilescan-agent**：逐文件漏洞检测主通道（每文件一次调用，token 消耗最大，建议 frontier 模型 + ≥128k context）；
  - **dataflow-agent**：跨文件数据流/污点追踪（ReAct 循环调文件检查工具，并发上限 --agent-limit 默认 10，5 次失败放弃该 finding）；
  - **oversight-agent**：**假阳性裁决**——triaging pass 重标 FP + review pass（可用 oversight-embed-agent 的内置规则分类法向量做 top-3 余弦相似规则增强）；
  - **exploitation-agent**：逐 finding 生成利用摘要/攻击链叙事（仅 --summary 开启时运行；文档自曝可能"hallucinated CVE numbers"）；
  - **sca-agent**：**supervisor（LangGraph）+ pip-audit 子 agent + knowledge-base 子 agent——当前只覆盖 Python 依赖**；
  - **mergekey-embed-agent**：finding 跨扫描链接的向量指纹（文件改名/行号漂移仍追踪；**换 embedding 模型会导致既有 finding 全部显示为新**）；
  - **oversight-embed-agent**：规则分类法向量匹配。
  - 支持混合提供商（如 singlefilescan 用 Vertex Gemini、其余用 Azure OpenAI）。〔同上，"Signal's LLM Agents [BETA]" / "Agent Capability Requirements [BETA]"〕
- **Fact（验证机制三件套）**：① oversight-agent 的规则增强 FP 复核；② **synthesis agent**（实验性）：数据流分析后识别多步漏洞链、挑出最危险攻击路径；③ **PoCKit**（实验性，2026-09 release notes）：**主动利用验证**——对 top findings 实际尝试确认可利用性，自动剔除 FP 并给已确认威胁提供完整 exploit 证据。需 --dataflow True（PoCKit 另需 --synthesis True）。〔同上，"Signal release notes"〕
- **Fact（工程化细节）**：--check-llm preflight（逐 agent 探活：chat agent 发 invoke("Hello")、embedding agent 验证向量维度；JSON schema_version "1" 有回归测试套件）；大库预扫成本估算器（>500 文件触发 low/mid/high token 与耗时预估）；dataflow 阶段 checkpoint 崩溃恢复；Bedrock prompt caching 默认开启；429 指数退避。〔同上〕
- **Fact（信任边界）**：不做 proprietary fine-tuning、不用客户数据训练；所有 LLM 经由美国基础设施（Anthropic/OpenAI/GCP/Azure）；**完整 prompt/response 内容不做规模化日志**（采样日志仅规划中）；SOC 2 Type II；明示不支持 HIPAA 场景。BYOLLM（BETA）允许指向客户自控端点，**官方卖点含 air-gapped 内网 LLM 代理**——即 Signal 的断网路径=自带 LLM。〔同上，"AI security…" / "BYOLLM [BETA]"〕

### 5.3 与 ContextAI/KB 的关系

- **Fact**：Signal 的知识底座品牌为 **ContextAI™** = SCA 的 KB（组件+BDSA）+ SAST/SCA 引擎规则 + SaaS 分析数据 + 安全咨询最佳实践；首发代码分析用例用的是**源自 Coverity 的 issue taxonomy**；CyRC 人工研究被定位为 ContextAI 的 human-verified 输入。〔同上，"Signal FAQ"；[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #5〕
- **Fact（时间线修正）**：2025-12-10 发布（仅既有客户/design partners）→ **GA 公告 2026-03-23**（CEO 博客）→ release notes 记 2026-04 为 GA 版本（Developer + Enterprise）。03 报告"2026-03 GA"口径与公告一致，release notes 落版本在 4 月；引用时建议写"2026-03 公告 GA / 2026-04 首个 GA 版本"。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #1#2；[sources/blackduck-signal-docs.md](sources/blackduck-signal-docs.md), "Signal release notes"〕
- **Interpretation**：Signal 的差异化不在 agent 框架（ReAct+supervisor 是行业通稿），而在**把 20 年策展数据做成 LLM 的上下文资产**（taxonomy 向量化 + KB 子 agent + merge key 持久化），以及罕见的**对自身失效模式的文档级公开**（哪些模型会失败、失败症状是什么、小模型哪里不能用）。其 "no false positives" 营销声称与内部 oversight/PoCKit 双层验证机制对照看：验证是真做了，但"无假阳性"仍是声称（无公开合并率/误报率数据——与全行业一致）。
- **Interpretation（对 SCA 主线的侵蚀信号）**：sca-agent 目前只做 Python + pip-audit——Signal 的 SCA 能力与 Black Duck SCA 主产品完全不在一个量级，短期是"编码时依赖风险提醒"，不是 SCA 替代。但架构上 supervisor+子 agent 模式留好了扩展位。

## 6. Seeker（IAST）与 SCA 的联动

- **Fact（直接联动点）**：Seeker 产品页明确："Seeker integrates Black Duck Binary Analysis, which analyzes target binaries for open source security vulnerabilities, versioning, and license information and **matches them against the knowledgebase in Black Duck Hub**. You get a **unified view** of all identified vulnerabilities found in custom code and component libraries." 即联动是 **Seeker（运行时代码漏洞）× BDBA（二进制 SCA）× Hub KB（漏洞库）** 的组合视图。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #6〕
- **Fact（聚合层是 SRM）**：跨工具结果合并由 Software Risk Manager（ASPM，Code Dx 血统）承担：Component Correlation 按 vulnerability/component 名+版本/type/component identifier 组合把 SCA 结果对齐成单一 finding（默认模式 "vulnerability + component identifier + type"）；Hybrid Correlation 把 URL 定位的 DAST/Seeker 结果映射回源码文件行区间（可叠加 JVM/CLR 二进制的调用图）；Agentless Correlation 官方自曝局限：推断路径可能因"未发现的 endpoint、继承与策略模式、匿名函数"等不完整，且**显著拖慢分析**。〔[sources/blackduck-srm-correlation.md](sources/blackduck-srm-correlation.md)〕
- **Fact**：Seeker 的差异化是 patented **active verification**（自动重测验证可利用性）+ sensitive-data tracking（PII 流向追踪，PCI DSS/GDPR 叙事）+ API 发现（REST/SOAP/GraphQL/gRPC）。CyRC 历史上用 Seeker 产出过真实 CVE（GOautodial、Nagios XI 系列）。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #6#5〕
- **Interpretation**：Seeker↔SCA 没有数据级的深度联动（没有"IAST 观察到的运行时组件加载反哺 BOM/VEX"的证据）；联动停在**展示层聚合**（SRM correlation）与**二进制分析复用**（BDBA）。"运行时证据 → exploitability 判定 → VEX justification"这条链路在 Black Duck 体系内不存在——与 03 §6"判定→VEX 自动化全行业断裂"的结论一致且更硬。

## 7. 制造业/嵌入式 CRA 叙事

- **Fact**：STMicroelectronics 案例（2025-03-06 双方发布）：STM32Cube 生态用 Black Duck 工具为 MCU 软件包生成 **CycloneDX（ECMA-424）机读 SBOM**（首个 STM32CubeU3，后续 H7RS/N6），ST 官方社区贴明言动机是 CRA（2027-12 适用）与航空/医疗/汽车既有监管；ST 侧强调"SBOM 是静态文档、漏洞随产品生命周期出现，需要定期自动化分析"——这正是 Black Duck LTS/VEX 叙事对应的客户侧需求。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #9〕
- **Fact**：Black Duck 的 CRA 内容策略（2025-07 博客 + 2026-07 方案页）：核心叙事是 **"SCA alone won't get you to CRA compliance"**——SCA/SBOM 管依赖、SAST 管自研代码（"secure by design"）、DAST 管联网服务（CRA 覆盖 remote data processing）；强调嵌入式场景（Yocto、RTOS、固件镜像）需要二进制分析 + 供应商 SBOM 导入持续监控；引用 CRA 24h/72h/14d 上报节奏论证"周期扫描根本不够，必须持续监控 + 自动化工作流"；给出 "September 2026"（漏洞报告义务生效）为基建 deadline。Tim Mackey（软件供应链风险策略负责人）是主要发言人。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) #3#4〕
- **Fact**：CyRC 的嵌入式/IoT 原创漏洞研究史（Zephyr、芯片组、IKEA 网关）为其制造业叙事提供了非营销的实质背书。〔同上 #5〕
- **Interpretation**：Black Duck 的 CRA 打法是**组合套装叙事（SCA+Coverity+BDBA+Seeker）+ 半导体头部客户背书**，没有 CRA 专门模块；其内容里"exploitation window 已缩到 <24h、2028 年 1 分钟"这类数字无出处（厂商声称）。对我们而言，它验证了两点：① 制造业客户要的是"**持续监控已发布产品**"（=LTS 语义），不是更准的扫描；② 供应商 SBOM 导入+监控是被头部客户真实使用的 CRA 承接模式。

## 8. AI/Agent 整体策略

- **Fact（所有权前提）**：Synopsys.ai 属 Synopsys EDA 业务，与 Black Duck 无关——2024-09-30 剥离后 Black Duck Software, Inc. 是独立 PE 控股公司（Clearlake + Francisco Partners，$1.65B）。Black Duck 当前自我定位是 **"the leader in applied AI for application security"** 与 "True Scale Application Security"。〔[sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) 备注〕
- **Fact（AI 布局全景，不止 Signal）**：
  1. **Signal**：agentic 分析+修复（§5）；
  2. **ContextAI**：跨产品共享的 AI 上下文资产层（KB + Coverity taxonomy + BSIMM/审计数据）；
  3. **KB 情报生产 AI 化**：ASA / Rapid Review BDSA（§1.2）；
  4. **Sigma（rapid SAST）带 AI-augmented SAST checker plug-in**（docs 有专门配置与安全考量章节）；
  5. **AI Model Scanning**：hub 侧扫描/管理 BOM 中的 AI 模型（hosted 限定，air-gapped 无）；支持手工把 AI model 加入 BOM；
  6. **AI-Assisted Documentation Service**：应用内文档 AI 搜索（默认开启，air-gapped 强制关闭）。
  〔[sources/blackduck-signal-docs.md](sources/blackduck-signal-docs.md)；Sigma map TOC（n97xWy6PqPKE~KNHCQD_3w）；[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md)；[sources/blackduck-ai-model-container.md](sources/blackduck-ai-model-container.md)；[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md)〕
- **Interpretation**：Black Duck 的 AI 策略是"**AI 三面下注**"：生产侧（AI 生成 advisory 扩 KB 覆盖）、检测侧（Signal/ContextAI/Sigma AI checker）、被检对象侧（AI Model Scanning 把 AI 模型纳入 BOM——AI BOM 的雏形）。PE 控股 + "applied AI leader" 自我定位意味着 Signal 是其估值故事核心，投入会持续加码。

## 9. 交付形态（self-hosted 与离线能力总览）

- **Fact（部署矩阵）**：
  - Black Duck SCA：Black Duck 托管（hosted）/ 自托管（K8s+Helm 为主力，Docker Swarm 仍支持、OpenShift 支持）；Tomcat+PostgreSQL+多容器架构；
  - **Air-gapped KB**（§1.3）：整库月度搬运，one-to-many 服务多 SCA 实例；
  - BDBA：SaaS（bdba.blackduck.com，AWS KMS AES-GCM-256）/ **OVA/qcow2 虚拟 appliance（VMware ESXi/KVM）** / K8s Helm（github.com/protecode-sc/helm-chart）；断网漏洞库手动周更 + 30 天窗口 + 全量再同步机制；
  - Signature Scanner 支持**完全离线扫描**（--dryRunWriteDir 生成数据文件，拿到有网环境上传；单次 5GB 上限）；Detect 可 air-gap 运行、可离线产出 BDIO JSON；
  - Polaris 为 SaaS 平台；Signal 默认走云端 LLM Gateway，BYOLLM 支持内网 LLM 代理（断网路径）。
  〔[sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md)；[sources/blackduck-bdba-install.md](sources/blackduck-bdba-install.md)；[sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md), "Running an offline component scan"〕
- **Interpretation**："离线/断网"是 Black Duck 相对 Snyk/Mend/Endor 等云原生对手的**结构性护城河**（军工、半导体代工厂、汽车供应链真实需要），但其新架构（MaaS/SCASS/Signal）全部默认云优先——断网客户正在被动地停留在"上一代匹配质量"。这个张力是我们的机会窗口（见 §11）。

## 10. 工程博客/文档自曝的局限（汇总）

全部来自官方文档原文（Fact）：

1. **KB 更新作业**：score/severity 变化静默生效、无通知无审计日志；**BDSA↔CVE 标识符切换创建新记录，重置 remediation status 与 comments**（旧数据保留在原标识符下但不迁移）；组件迁移/合并/拆分同样把漏洞当新条目；传播是异步的，job 卡住时视图间会出现临时不一致；LTS 通知"coming soon"。官方自述正在做"preserving remediation status across vulnerability identifier transitions"。〔[sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md), "Understanding the Knowledge Base Update Job" / "KB Updates & Vulnerability Propagation"〕
2. **Snippet**：匹配区域高亮"只是近似"；部分匹配确认默认不随重扫保留；`--full-snippet-scan` "may cause significant performance and scalability issues… only in extreme situations"；snippet 不能离线（hosted 形态下）。
3. **Reachability（impact analysis）**：reachable ≠ 必然受影响；未标 reachable ≠ 安全（"Black Duck may not have data for a specific vulnerability"）；仅 Java、仅带方法名元数据的 BDSA。
4. **C/C++/嵌入式**：Yocto PR service 版本漂移失配；Clang detector 仅限 Linux 包管理器已安装组件；Conan 自定义 user/channel 不匹配；custom scan signatures 有已知性能问题、限定目录 5 层。
5. **BDBA**：断网超 30 天漏洞数据出现空洞，全量同步期间扫描停止；Web UI 上传 8GB/30 分钟限制。
6. **Air-gapped**：无 fuzzy/correlation/MaaS/SCASS/big data/AI 文档/自动 BOM 重算（§1.3 清单）。
7. **SRM correlation**：agentless correlation 推断路径可能不完整（未探测 endpoint、继承/策略模式、匿名函数）且拖慢分析。
8. **Signal**：本地小模型（≤13B）明确不支持 ReAct agents（JSON schema 被静默忽略、tool call 畸形、context 太小）；oversight-agent 可能对一切附和初判不标 FP（行为失效而非报错）；exploitation-agent 可能幻觉 CVE 编号；换 embedding 模型会毁掉 finding 链接；完整 prompt/response 不规模化留日志（审计权衡）；"In our tests, Signal produced significantly better findings than general-purpose AI coding assistants"——无公开基准数据（厂商声称）。〔[sources/blackduck-signal-docs.md](sources/blackduck-signal-docs.md)〕
9. **LTS 转换的信息有损**：多 origin remediation 合并只留最重状态、comments 拼接、triage 信息丢弃、不可逆。

## 11. 对我们产品的启示

1. **"已发布产品版本的持续监控"对象模型值得直接对标 LTS 再向前一步**。Black Duck 用 LTS 证明了"剥离开发期数据、只留 BOM+漏洞追踪、集中式组件 catalog 撑规模"是可行的工程形态。我们可做的差异化：LTS 缺的**通知/审计（它自己承认 coming soon）**、判定状态机（我们的 Claim+Evidence+Decision 三件套 + 情报驱动的自动失效重估——Black Duck 的 KB 更新作业自曝证明，连行业最强者也只做到"发现新洞推给你"，做不到"新情报推翻旧判定"）。把"判定会过期"做成一等语义，是对 Black Duck 最锋利的错位打击点。
2. **断网/半断网交付是真实且被对手冷处理的市场**。Black Duck 的 air-gapped 方案重（64 核/256GB/35TB、5TB 月度搬运、无增量、功能阉割、无 fuzzy/correlation），且架构演进在抛弃断网客户。一个**增量更新、功能对等（或明确声明裁剪边界）、轻量硬件**的离线 KB/VEX 方案在军工/半导体/汽车 Tier1 有结构性空间。其 "KB 更新后 air-gapped 需手动重扫才刷新 BOM" 这种体验断点就是我们的切入点。
3. **Snippet/二进制场景做"漏洞传导"要克制，但"证据链"可以做厚**。Black Duck 刻意让纯 snippet 匹配不进漏洞统计（保守、防噪声），代价是暴露面低估。我们的机会不在更激进的漏洞传导，而在**把 snippet/二进制命中记录为可审计证据**（匹配窗口、codeprint 命中率、人工确认决策、确认人/时间）——即它的人工 review 闸门产生的 Decision 记录，正是 CRA 证据链需要的，而 Black Duck 把这些散落在 BOM adjustment 里没做成判定对象。
4. （补充观察）Signal 的"oversight-agent FP 复核 + mergekey 跨扫描链接 + preflight 成本预估"三件套，是任何做 LLM 分析产品都该抄的作业；其 sca-agent 只覆盖 Python 说明"agentic SCA"短期不会威胁依赖级 SCA 主战场。

## 12. 无法核实项清单

1. **KB 策展团队规模与流程细节**：CyRC 人数、BDSA 人工策展 SLA、"比 NVD 快 X 天"的量化数据——只有定性描述与营销口径，无一手数字。（不确定）
2. **KB 规模数字口径冲突**：官方文档 9M 组件/260K 漏洞 vs 营销页 8.7M 组件/57,700 forges vs datasheet 317K 漏洞/426K 受影响版本——哪组是当前准确口径无法判定。
3. **Signal 的修复质量指标**：无公开的合并率/回归率/FP 率基准（全行业通病，03 报告已记）；PoCKit 主动利用验证的命中率与安全性边界（沙箱？只对 CTF 式目标？）文档未述。
4. **Signal "verified code fixes and library patching"**（发布 PR 用语）的具体实现：文档只覆盖"建议修复 + 至多创建 MR"，未找到自动打补丁/升级依赖的文档级描述——PR 口径与文档口径有差距。（不确定 PR 中的 automated remediation 是否已落地）
5. **MaaS 对匹配质量的实际影响**：官方只说"效率"，无精度对比数据；air-gapped 客户匹配质量是否系统性落后为 Hypothesis。
6. **BDSA 的 CNA 状态**：03 报告称 Black Duck 有 CNA 身份，本轮未在一手来源复核到 CNA 授权记录（CyRC 页只列披露清单）。（不确定，建议后续查 cve.org CNA 名录）
7. **Seeker 与 Black Duck SCA 是否存在 BOM 级数据互通**（运行时观测反哺）：未找到任何文档证据，倾向判定为无，但不能证伪。
8. **Polaris 平台与 Black Duck SCA（hub）的长期合并路线**：Signal Enterprise 上传 Polaris，而传统 hub 是另一套——两平台的归一战略未见官方说明。
9. **03 报告"reachability 由 Coverity 引擎支撑"**：本轮官方文档只支持"Detect 调用图 + KB 函数签名匹配（Java）"一条路径；Coverity 是否另有 OSS reachability 能力未获文档印证（Coverity 文档体量巨大，未全量翻检，不能排除）。

## 附：本轮 sources 清单

| 文件 | 内容 |
|---|---|
| [sources/blackduck-kb-airgap.md](sources/blackduck-kb-airgap.md) | Air-gapped KB 安装指南全 7 主题（需求/下载/搭建/FAQ/升级） |
| [sources/blackduck-kb-hub-docs.md](sources/blackduck-kb-hub-docs.md) | KB 服务/更新作业/LTS 交互/BDSA/Hosted-vs-Airgapped 对照表 |
| [sources/blackduck-detection-engine.md](sources/blackduck-detection-engine.md) | Signature/snippet/custom signature/组件匹配/Match Review/C-CPP Tool/离线扫描 |
| [sources/blackduck-detect-cpp-embedded.md](sources/blackduck-detect-cpp-embedded.md) | Detect BitBake/Clang/Conan detector 与 detector 精度机制 |
| [sources/blackduck-bdba-install.md](sources/blackduck-bdba-install.md) | BDBA 概览/限制/虚拟 appliance/漏洞库更新机制 |
| [sources/blackduck-project-version-model.md](sources/blackduck-project-version-model.md) | Project/Version/phase/LTS/cloning/subproject/Project Group |
| [sources/blackduck-vex-state-machine.md](sources/blackduck-vex-state-machine.md) | VEX 全状态表/CSAF 映射/全局报告字段继承/remediation 报告族/impact analysis |
| [sources/blackduck-signal-docs.md](sources/blackduck-signal-docs.md) | Signal 全套官方文档（CLI/MCP/7-agent/BYOLLM/preflight/信任/FAQ/release notes） |
| [sources/blackduck-srm-correlation.md](sources/blackduck-srm-correlation.md) | SRM correlation 机制与集成工具清单 |
| [sources/blackduck-ai-model-container.md](sources/blackduck-ai-model-container.md) | AI model BOM/容器扫描/加密组件 |
| [sources/blackduck-architecture-deployment.md](sources/blackduck-architecture-deployment.md) | 部署架构/网络通信/SCASS/数据保留/AI 文档服务/二进制扫描 |
| [sources/blackduck-web-pages.md](sources/blackduck-web-pages.md) | 官网营销/博客/PR/客户社区抓取记录与剥离交易来源 |
