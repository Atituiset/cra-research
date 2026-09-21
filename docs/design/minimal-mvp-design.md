# 最小可交付 MVP 工程设计文档

> 2026-09-21 | 读者：研发团队（拿去即可开工）
>
> 上游依据：一句话定位与判定逻辑见 [00-final-report](../research/00-final-report.md) §1.0/§1.1/§1.2/§7.6/§7.7；Phase 1 定义与成功指标见 §14.2；战略问答见 §15。Agent 编排见 [vex-agent-architecture.md](vex-agent-architecture.md)。PoC 资产见 [poc/README.md](../../poc/README.md) 与 [poc/BUILD-LOG.md](../../poc/BUILD-LOG.md)。技术栈入场底线见 [06 报告](../research/06-product-forms-and-tech-stacks.md) §C.2；闭环 Gap Analysis（本 MVP 的差异化靶心）见 [03 报告](../research/03-competitive-landscape.md) §6。
>
> 本文是**工程设计文档**而非研究报告：不给 source notes，引用研究结论时以相对路径链接到对应报告章节。

## 1. 定位与边界

### 1.0 一句话定位（沿用 [00-final-report](../research/00-final-report.md) §1.0 原文）

> **给卖产品到欧盟的制造商做一个"产品漏洞档案官"：以产品版本为账本，持续记录"你产品里有什么漏洞、你怎么判定的、修没修"，并在漏洞被在野利用时替你掐着 24h/72h 的法定时钟跑完报告——全程留下能出示给监管机构的签名证据。**

### 1.1 MVP 的一句话

**一个部署在设计伙伴内网的单实例系统：注册 Product/Version/Release 并维护 SBOM → 每日同步漏洞情报并自动关联 → 用三类强证据规则自动产出带签名证据的 VEX 判定（弱证据进人工签核队列）→ 一键导出监管证据包。** 比 PoC 多的是对象模型、statement store、人签队列与持续的触发层；比 [00-final-report](../research/00-final-report.md) §14.2 Phase 1 少的是 Art 14 报告工作台、技术文档生成器与 Web UI。

### 1.2 In / Out 清单

**In（MVP 交付）**

| # | 能力 | 说明 |
|---|---|---|
| 1 | Product/Version/Release 注册与支持期元数据 | CLI 注册；support period 起止、EoL 标记 |
| 2 | SBOM 摄取与版本化存档 | 复用 Syft；CycloneDX 入库存档 + 版本间 diff |
| 3 | 漏洞情报每日同步 | OSV（主轨道）+ GHSA + NVD fallback + KEV/EPSS 信号；本地缓存 |
| 4 | 自动关联 + 受影响版本矩阵 | PURL 匹配 + 版本区间求值；矩阵以 CLI 与静态 HTML 输出 |
| 5 | Reachability 判定 | Go = govulncheck；C/C++ = Joern（限可构建、有 compile_commands.json 的项目） |
| 6 | 三个强证据规则全自动判定 | affected-confirm / component-not-present / code-not-present + under_investigation 兜底 |
| 7 | 人工签核队列 | 弱证据判定（not-in-execute-path 等）挂起等签，CLI 操作 |
| 8 | Judgment（VEX statement）一等对象 + 状态机 + 失效重估 | PostgreSQL statement store |
| 9 | in-toto attestation 签名证据链 | 沿用 PoC `conclusion/v0.1` predicate + ed25519 |
| 10 | 监管证据包一键导出 | PoC `out/` 结构产品化 + Annex VII/Art 14 映射说明 |
| 11 | KEV 命中高亮 | 命中即标红进每日报告；**只提示"应评估是否触发 Art 14 时钟"，不启动时钟工作流** |

**Out（明确不做，及理由）**

| 不做 | 理由 | 归属阶段 |
|---|---|---|
| Art 14 SRP 直连 / 报告工作台 | SRP 无 API（[02 报告](../research/02-cra-regulation.md) §6.2）；完整三阶段表单流是 Phase 1 剩余工作 | Phase 1 后半 |
| 多租户 / SaaS | 1–2 家设计伙伴，单实例 on-prem；多租户是成本非价值 | Phase 4 |
| 完整 Web UI | 见 §7 取舍：CLI + 静态 HTML 报告覆盖低频人签场景 | Phase 1 后半 |
| Agentic 修复 / 自动升级 PR | [00-final-report](../research/00-final-report.md) §14.4 明确定位 Phase 3；确定性验证闭环先行 | Phase 3 |
| C 之外语言的 reachability 全覆盖 | Go（govulncheck 官方）+ C/C++（Joern，PoC 已验证）即可演示差异化；Java/JS/Py 跟随开源生态 | Phase 2 |
| deploy-context / fix-status 两类查询原语的实现 | 只留接口（§5.3）；context 采集是集成工程，工作量不合 MVP | Phase 2 |
| 技术文档（Annex VII）自动生成器 | 证据包导出已覆盖其素材；模板组装是 Phase 1 后半 | Phase 1 后半 |
| 弱证据规则自动签出 | "unreachable 是弱证据"是硬原则（[00-final-report](../research/00-final-report.md) §7.6 原则①），任何阶段都不自动签 | 永不自动 |
| 密钥 KMS/HSM 与轮换 | MVP 标注 TODO（§8.1）；设计伙伴试点用文件密钥 + 操作纪律 | Phase 1 后半 |
| air-gapped 数据包分发 | [06 报告](../research/06-product-forms-and-tech-stacks.md) §C.2 列为自研差异化，但 MVP 假设设计伙伴可联网 | Phase 2 起 |

## 2. 目标用户与核心 User Story

**目标用户**：EU 市场制造商的**产品安全负责人**（或其兼任者——1–2 家设计伙伴的安全工程师/合规负责人）。他面对的监管提问粒度是"哪个产品版本的哪个漏洞、判定了什么、修没修、证据在哪"（[03 报告](../research/03-competitive-landscape.md) §4.5）。

### Story 1：注册产品版本并维护 SBOM

> 作为产品安全负责人，我要注册我的产品线与投放市场的版本（含上市日期、support period），并让每次发布构建的 SBOM 自动摄取、存档、可与上一版本 diff——这样我对"我有什么"始终有账本，而不是散落在 CI 里的临时文件。

验收：`cra product register` / `cra release ingest` 可用；同一 Version 的两次 Release 的 SBOM diff（新增/移除/升级组件）可查询并落入 HTML 报告。

### Story 2：新 CVE 当天知道哪些版本受影响，并得到带证据的 VEX 判定

> 作为产品安全负责人，新 CVE 公开当天，我要知道它命中我哪些 Product × Version，并且对每一条命中，系统要么给出带证据的自动判定（affected / not_affected 强证据），要么明确告诉我"在调查中"或"需要你人工签核"——不允许静默丢弃，不允许无证据结论。

验收：情报同步后自动触发关联 + 判定；受影响版本矩阵当日产出（目标 < 4h，见 §10）；每条 Judgment 挂 attestation，弱证据判定出现在签核队列而非自动生效。

### Story 3：一键导出监管证据包

> 作为产品安全负责人，当合规官或 MSA（成员国市场监管机构）要求出示证据时，我要能对任一 Product × Version 一键导出一个自包含、逐条可验签的证据包，并附一张"导出物 ↔ CRA 条文"对照说明，让合规官不看代码也能验收。

验收：`cra export --product X --version Y` 产出证据包；包内 attestation 逐条验签通过；附 Annex VII/Art 14 映射表（§8.3）。

## 3. 系统架构

### 3.1 组件图

```text
                        ┌────────────────────────────────────────┐
                        │            cra CLI（操作入口）           │
                        │ register / ingest / scan / judge /      │
                        │ review queue ops / export / report      │
                        └───────┬───────────────────────┬────────┘
                                │                       │
              ┌─────────────────▼──┐         ┌──────────▼─────────┐
              │  Product Inventory │         │  Judgment Engine    │
              │  Service           │         │  （判定管道编排）     │
              │ Product/Version/   │         │                     │
              │ Release/SBOM 注册  │         │  intake → evidence  │
              └─────────┬──────────┘         │  → rules → publish  │
                        │                    └──┬───────┬───────┬──┘
                        │                       │       │       │
   ┌────────────────────▼──────────┐   ┌────────▼┐ ┌────▼────┐ ┌▼─────────────┐
   │   Intel Sync Service（定时）   │   │ sbom-   │ │version- │ │ callgraph-   │
   │   OSV/GHSA/NVD + KEV/EPSS     │   │ query   │ │range-   │ │ query        │
   │   → 本地缓存 + 变更检测         │   │         │ │query    │ │ Go:govulnchk │
   └────────────────┬──────────────┘   └────┬────┘ └────┬────┘ │ C/C++:Joern  │
                    │                        │          │      └──────┬───────┘
                    │                        │          │             │
              ┌─────▼────────────────────────▼──────────▼─────────────▼─────┐
              │            Statement Store + Evidence Store                  │
              │   PostgreSQL：Judgment 一等对象 / attestation / evidence blob │
              │   状态机 + 失效重估触发                                       │
              └─────┬───────────────────────────────────────┬───────────────┘
                    │                                       │
          ┌─────────▼─────────┐                  ┌──────────▼──────────┐
          │ Review Queue       │                  │ Export / Report      │
          │ 弱证据挂起 + 人签   │                  │ 证据包 + 静态 HTML    │
          │（CLI 签核，双主体） │                  │ 报告 + trace-report  │
          └────────────────────┘                  └─────────────────────┘

  外部世界：Syft（SBOM 生成）· OSV/GHSA/NVD API · KEV/EPSS feed ·
            govulncheck · Joern(docker) · in-toto/ed25519 签名密钥
```

### 3.2 组件职责与来源标注

| 组件 | 职责 | 来源 |
|---|---|---|
| `cra` CLI | 全部人工操作入口；Python `argparse`/`typer`，薄封装 | 【新建】（薄壳） |
| Product Inventory | Product/Version/Release/SBOM/Component 表；注册、摄取、diff 查询 | 【新建】（对象模型是根基，[00 §5](../research/00-final-report.md)） |
| Intel Sync | OSV/GHSA/NVD 每日拉取 + 本地缓存 + KEV/EPSS 信号；变更检测驱动增量 | 【新建】（PoC 只一次性查 OSV）；数据源【复用开源/公共 API】 |
| sbom-query | Syft 生成 CycloneDX + sha256 锚定；C 侧合入 sbom-augment 片段 | 【复用 PoC】`poc/pipeline/sbom.py`；Syft【复用开源】 |
| version-range-query | OSV events 版本区间求值 + GHSA/NVD 交叉核对 + C 侧策展回退 | 【复用 PoC】`associate.py` 改造为原语；OSV API【复用开源】 |
| callgraph-query | Go: govulncheck；C/C++: Joern CPG + compile_commands.json | 【复用 PoC】`reach_go.py` / `reach_c.py` / `pipeline/joern/`；工具【复用开源】 |
| threat-signal-query | KEV 命中、EPSS 分值、抓取时间戳 | 【新建】（轻，feed 解析） |
| Judgment Engine | 编排 evidence 收集 → 跑三强证据规则 + 兜底 → 产出 Judgment | 【新建】（基于 PoC `vex.py` 重构为规则引擎，§6） |
| Statement/Evidence Store | Judgment 一等对象、attestation、evidence blob；状态机与失效重估 | 【新建】schema；签名逻辑【复用 PoC】`attest.py`/`store.py` |
| Review Queue | 弱证据判定挂起；CLI 列表/查看证据/签核；人+系统双主体记录 | 【新建】 |
| Export/Report | 证据包导出（逐条验签）+ 静态 HTML 报告（矩阵/队列/trace） | 【复用 PoC】`export.py` 改造 + HTML 模板【新建】 |
| Trigger/Watcher | 情报变更 / 新 Release 摄取 → 拉起判定任务 | 【新建】（cron + 任务表即可，不上消息队列） |

### 3.3 技术选型表

| 决策点 | 选型 | 理由（呼应 [06 报告](../research/06-product-forms-and-tech-stacks.md) §C.2 入场底线） |
|---|---|---|
| 实现语言 | **Python 3.12**（全系统） | 与 PoC 同语言，`pipeline/*.py` 直接演进；in-toto/securesystemslib 官方 Python 库已实测（[BUILD-LOG](../../poc/BUILD-LOG.md) §3.5）；性能瓶颈全在外部工具（govulncheck/Joern），Python 无短板 |
| 存储 | **PostgreSQL 16**（单容器，docker compose 起） | 取舍见 §3.4。结论：MVP 直接用 PG，不从 SQLite 起步 |
| SBOM 生成 | Syft（CycloneDX 输出） | 已商品化，自研=浪费（[06 §C.2](../research/06-product-forms-and-tech-stacks.md)）；PoC 已用 |
| 漏洞情报 | OSV API 主轨道 + GHSA GraphQL + NVD 2.0 fallback + KEV/EPSS feed | PURL 主轨道近乎无损，CPE 仅 fallback（[01 报告](../research/01-domain-ontology.md) §9）；NVD 2026 失明窗口必须多源（[01 §4](../research/01-domain-ontology.md)） |
| Reachability | govulncheck（Go）+ Joern docker（C/C++） | PoC 已验证；CodeQL 商用需 GHAS 许可，故 C 底座选 Joern（Apache-2.0，见 [vex-agent-architecture.md](vex-agent-architecture.md) §6） |
| VEX 序列化 | OpenVEX（vexctl 校验） | Grype `--vex` 可直接消费，与下游扫描器闭环（[vex-agent-architecture.md](vex-agent-architecture.md) §4.6）；CSAF 导出留 Phase 1 后半 |
| 签名 | in-toto Statement v1 + DSSE + ed25519，predicateType 沿用 `https://cra-research.dev/attestation/conclusion/v0.1` | PoC 154 条 attestation 全链路实测通过（[README](../../poc/README.md)） |
| 服务形态 | **无常驻 Web 服务**：cron 驱动的 Intel Sync + CLI 触发的判定任务 + 静态 HTML 报告 | 1–2 家设计伙伴、单实例；把工程预算留给对象模型与证据链 |
| 部署 | 单台 Linux 主机 + docker compose（postgres + joern 镜像） | on-prem 起点；Joern 镜像推固定 digest（[BUILD-LOG](../../poc/BUILD-LOG.md) §5 教训） |

### 3.4 存储取舍：为什么不从 SQLite 起步

PoC 用 SQLite 是刻意选择且 README 已注明"生产目标 PostgreSQL，同 schema 平移"。MVP 直接上 PG，理由三条：

1. **写并发**：Intel Sync（每日写）、CLI 判定任务（随时写）、导出（读+验签）三方并发；SQLite 单写者在"同步中触发判定"这个 MVP 日常场景就会锁。
2. **statement store 是长生命周期对象**：Judgment 要活 10 年、跨任务演进，失效重估需要条件更新与状态查询，PG 的事务与 JSONB（evidence 字段）明显更合适；中途迁移 schema + 存量 attestation 引用，成本远高于第一天用对。
3. **代价极小**：单容器 docker compose；Dependency-Track/GUAC 的生产实证（[06 §B.7](../research/06-product-forms-and-tech-stacks.md)）证明关系库足够，**刻意不用图数据库**——壁垒在数据模型不在图存储（[04 报告](../research/04-technology-deep-dive.md) §5.2）。

SQLite 保留的唯一场景：单元测试与 demo 环境（schema 用 SQLAlchemy/裸 SQL 方言兼容层，成本已计）。

## 4. 核心数据模型

全部表落 PostgreSQL。命名与 [00-final-report](../research/00-final-report.md) §7.1 对象模型对齐；PoC `store.py` 的 artifacts/evidence/conclusions/attestations 四表演进为下图十个对象（conclusions 拆为 Association + Judgment + EvidenceLink）。

### 4.1 实体关系

```text
Product 1─n Version 1─n Release 1─1 SBOM 1─n Component
                                               │ 1
                                               ▼ n
Vulnerability 1─n Association(Component × Vulnerability × Release 命中)
                       │ 1
                       ▼ n（每次判定/重估一条）
                    Judgment ──n EvidenceLink ──n Evidence（blob/sha256）
                       │ 1
                       ▼ 0..1
                  Attestation（签名信封，绑定最新有效 Judgment）
```

### 4.2 字段级 Schema

**Product**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| name | text | 产品线名 |
| cra_class | enum(`default`,`class_i`,`class_ii`,`critical`) | Annex III/IV 分类（Art 7/8），默认 `default` |
| owner | text | 设计伙伴侧负责人 |
| created_at | timestamptz | |

**Version**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| product_id | uuid FK | |
| version | text | 投放市场版本号 |
| release_date | date | 上市日期 |
| support_start / support_end | date | 支持期（≥5 年，Art 13(8)） |
| eol_notified | bool | EoL 到期通知状态（Art 13(19)），MVP 只记录不自动通知 |
| state | enum(`active`,`eol`,`legacy`) | legacy = 存量产品（Art 69(3)，仅 Art 14 适用） |

**Release**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| version_id | uuid FK | |
| build_ref | text | 构建标识（CI run / tag） |
| artifact_sha256 | text | 制品 hash |
| sbom_id | uuid FK → SBOM | |
| created_at | timestamptz | |

**SBOM**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| format | enum(`cyclonedx`,`spdx`) | MVP 实际只产 cyclonedx，枚举预留 |
| sha256 | text UNIQUE | 内容寻址 |
| blob_uri | text | 对象存储/文件路径 |
| generator | jsonb | `{tool:"syft",version:"1.52.0",command:"..."}` |
| created_at | timestamptz | |

**Component**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| sbom_id | uuid FK | |
| purl | text | 主轨道身份（ECMA-427） |
| cpe | text NULL | 辅轨道，仅 fallback 匹配时填 |
| name / version | text | 展示冗余 |
| sha256 | text | SBOM 条目 hash |
| match_source | enum(`sbom`,`augment`,`curation`) | `augment`/`curation` = PoC 的 C 侧增补与策展回退（[BUILD-LOG](../../poc/BUILD-LOG.md) §3.1/§3.2） |

**Vulnerability**

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| canonical_id | text UNIQUE | 归并后 ID（CVE 优先，否则 GHSA/GO/OSV id——PoC `vex.py` 归并逻辑产品化） |
| aliases | jsonb | 全部别名 |
| summary | text | |
| affected_ranges | jsonb | OSV events 序列（introduced/fixed/last_affected）+ 各源区间差异 |
| cvss / epss | numeric NULL | EPSS 每日刷新，保留抓取时间 |
| in_kev | bool + kev_date | KEV 命中即标红（Story 2 验收点） |
| sources | jsonb | `{osv:...,ghsa:...,nvd:...}` 各源条目 id 与抓取时间 |
| first_seen / updated_at | timestamptz | |

**Association**（组件 × 漏洞在某 Release 上的命中；误报漏报第一发源地，必须留依据）

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| release_id / component_id / vulnerability_id | uuid FK | 唯一约束（release, component, vuln） |
| in_range | bool | 版本区间求值结果 |
| range_basis | jsonb | 判定依据：命中的事件序列 + 来源条目 id（可审计的"为什么判 affected"推导链，[06 §B.3](../research/06-product-forms-and-tech-stacks.md) 差异化点） |
| created_at | timestamptz | |

**Judgment**（VEX statement 一等对象，核心表）

| 字段 | 类型 | 说明 |
|---|---|---|
| id | uuid PK | |
| association_id | uuid FK | |
| status | enum(`under_investigation`,`affected`,`not_affected`,`fixed`) | OpenVEX 四 status |
| justification | enum NULL | 五种机器可读 justification；not_affected 强制非空 |
| detail | text NULL | impact/action statement（人签时填写） |
| evidence_strength | enum(`strong`,`weak`) | **Phase 2 预留字段，MVP 已写**：强=机器可证，弱=静态不可达/context 类 |
| decided_by | text | `system:<rule_id>` 或 `human:<user>`；签核结论记 `human:<user>+system:<rule_id>` 双主体 |
| rule_id / rule_version | text | 判定规则及其内容 hash（失效重估依据，复用 review-skills execution-manifest.sha256 机制，[vex-agent-architecture.md](vex-agent-architecture.md) §3） |
| state | enum(`active`,`stale`,`superseded`) | active=当前有效；stale=失效待重估；superseded=被新判定取代 |
| supersedes_id | uuid FK NULL | 版本链 |
| created_at | timestamptz | |

**EvidenceLink**

| 字段 | 类型 | 说明 |
|---|---|---|
| judgment_id | uuid FK | |
| evidence_sha256 | text FK → Evidence | call path 对象 / OSV 原始响应 / SBOM diff / 工具 stdout 等 |
| role | enum(`range`,`reachability`,`signal`,`verification`,`raw`) | 证据角色 |

**Attestation**

| 字段 | 类型 | 说明 |
|---|---|---|
| sha256 | text PK | DSSE 信封 canonical JSON 的 sha256（内容寻址，PoC 同款） |
| judgment_id | uuid FK | |
| envelope_json | jsonb | in-toto Statement v1 + `conclusion/v0.1` predicate |
| signer / keyid | text | |
| created_at | timestamptz | |

**Evidence**：`sha256 PK / kind / blob_uri / inline_json / created_at`（PoC evidence 表平移）。

### 4.3 Judgment 状态机与失效重估

```text
                 ┌──────────────────────────────┐
                 ▼                              │
        under_investigation ──强证据命中──▶ affected ──修复验证通过──▶ fixed
                 │                              ▲                      ▲
                 ├─强反证（组件/代码不在）─▶ not_affected（自动，justification ①②）
                 │
                 └─弱证据候选 ─────────────▶ [REVIEW QUEUE] ──人签──▶ not_affected（justification ③④⑤）
                                                              └─驳回──▶ 回 under_investigation
```

- **任何 status 不会静默消失**：证据不足一律 under_investigation（PoC 已按此原则处理 14 条未覆盖条目）。
- **失效重估触发条件**（满足任一即把 `active → stale` 并重新拉起判定）：
  1. 情报更新：该 Vulnerability 的 affected_ranges 变化 / 新 alias 归并 / 新 fix commit 信息；
  2. KEV 新命中（in_kev false→true）：重估 + 标红提示 Art 14 时钟评估；
  3. 新 Release 摄取（SBOM 变化）：该 Version 下全部 Association 重建，旧 Judgment 转 superseded；
  4. 规则更新：rule 内容 hash 变化 → 该 rule 产出的全部 Judgment 置 stale；
  5. vuln→function 策展数据更新：相关 callgraph-query 结论作废重跑。
- 触发 1/2/4/5 是"**新情报触发既有 VEX statement 失效重估**"的 MVP 实现——全行业无人做（[03 报告](../research/03-competitive-landscape.md) §6.2 发现 3），是差异化演示点。

## 5. 判定管道：从 PoC 到 MVP

### 5.1 PoC 脚本逐项处置

| PoC 资产 | MVP 处置 | 说明 |
|---|---|---|
| `pipeline/run.sh` | **废弃**，由 `cra scan`/`cra judge` + 任务表替代 | PoC 是一次性顺序执行；MVP 是事件驱动（新 Release / 情报变更触发） |
| `pipeline/sbom.py` | **直接复用**，包为 sbom-query 原语 | 加 SBOM 入库与内容寻址 |
| `pipeline/associate.py` | **改造**为 version-range-query | 从"跑一次出文件"改为"给定 (component, vuln) 出标准化事实"；保留 curation-crosscheck 回退 |
| `pipeline/reach_go.py` | **直接复用**，包为 callgraph-query(Go) | first_trace fallback 逻辑原样保留（[BUILD-LOG](../../poc/BUILD-LOG.md) §3.3） |
| `pipeline/reach_c.py` + `pipeline/joern/` | **直接复用**，包为 callgraph-query(C/C++) | Joern docker 固定 digest；成败判定沿用"是否拿到 CALL 行" |
| `pipeline/vex.py` | **重构**为 Judgment Engine 的规则层 | alias 归并逻辑保留；输出从 OpenVEX 文件改为 Judgment 行 + 导出时再序列化 |
| `pipeline/attest.py` | **直接复用** | predicate `conclusion/v0.1` 不变；签名在 publish 阶段 |
| `pipeline/store.py` | **替换** | SQLite 四表 → §4 PG schema；conclusions 拆为 Association+Judgment |
| `pipeline/export.py` | **改造** | 导出源从 SQLite 改 PG；增加 HTML 报告与 Annex VII 映射说明 |
| `curation/vuln-function-map.json` | **平移入库** | 新增 `vuln_function_map` 表（vuln_id → 函数符号集 + 来源 + 策展人），仍为手工策展——承认这是成本中心（[04 §1.5](../research/04-technology-deep-dive.md)） |
| `keys/` 开发密钥 | **沿用 + TODO** | 见 §8.1 |

### 5.2 从脚本到"服务"的边界

MVP 只有两个常驻/准常驻进程，其余全部是 CLI 命令：

1. **Intel Sync**（cron 每日 + 可手动触发）：拉取 → 变更检测 → 写 Vulnerability → 触发失效重估与新关联。
2. **PostgreSQL** 容器。

判定、签核、导出全部经 CLI 执行（幂等、可重跑、任务表记录状态）。**刻意不上 Web 服务/消息队列**：单机单租户下 cron+任务表足够，少一层运维面。

### 5.3 六类查询原语的 MVP 范围

对照 [vex-agent-architecture.md](vex-agent-architecture.md) §5，全部原语遵循"请求 → raw 原文 → 标准化事实"三段式，raw 存 Evidence 表，失败/歧义如实记录不静默降级：

| 原语 | MVP 状态 | 实现范围 |
|---|---|---|
| sbom-query | ✅ 实现 | 组件条目 + PURL + sha256 + 来源（syft + augment + curation） |
| version-range-query | ✅ 实现 | OSV 区间求值 + GHSA/NVD 交叉核对 + C 侧策展回退；输出版本是否命中 + 依据条目 id |
| callgraph-query | ✅ 实现（Go + C/C++） | Go：govulncheck 符号级，含 call trace；C/C++：Joern CPG + vuln→function 策展映射，输出 reachable? + call path（file:line）+ 引擎精度声明。其他语言：原语返回 `unsupported`，判定落 under_investigation |
| threat-signal-query | ✅ 实现 | KEV 命中 + EPSS 分值 + CVSS + 抓取时间 |
| deploy-context-query | ⛔ 只留接口 | 定义标准化事实 schema（生产标记/暴露面/缓解措施），MVP 返回 `no_data`；接入后弱证据规则即可消费，接口先行不堵死 Phase 2 |
| fix-status-query | ⛔ 只留接口 | 定义 schema（fix version/重扫结果）；MVP 中 `fixed` 状态由人工对新 Release 重扫后确认触发，不做自动验证闭环（Phase 3） |

## 6. Agent 层（MVP 范围）

按 [vex-agent-architecture.md](vex-agent-architecture.md) §8 第一步：**只实现三个强证据规则 + under_investigation 兜底，全自动、无人工闸**。

### 6.1 规则实现表

| 规则 | 判定逻辑 | 消费原语 | 签核 |
|---|---|---|---|
| `affected-confirm` | 版本落在受影响区间且无反证；有 call path 则强确认（证据升级，不改 status） | sbom + version-range + callgraph + threat-signal | 自动（保守原则：无反证即 affected，[00 §7.6](../research/00-final-report.md) 原则①） |
| `component-not-present` | 组件不在该 Release 的 SBOM 中（含 diff 确认） | sbom | 自动 |
| `code-not-present` | 只用子模块 / 版本已 backport 修复 / 包在但漏洞文件未编入 | sbom + version-range | 自动 |
| （兜底） | 证据不足、区间不确定、情报源冲突、语言 unsupported | — | 自动置 under_investigation |

三个弱证据规则（`not-in-execute-path` / `not-controllable` / `inline-mitigation`）**在 MVP 里只以"待人工判定队列条目"出现**：

- callgraph-query 返回"无路径"时，Judgment Engine **不自动签 not_affected**，而是生成一条 `state=active, status=under_investigation` 的 Judgment + 一条 Review Queue 候选（附 call graph 证据与建议 justification `vulnerable_code_not_in_execute_path`）；
- 人工在 CLI 查看证据后签核，签核动作产出新 Judgment（`decided_by=human:X+system:not-in-execute-path`）+ 人+系统双主体 attestation；
- deploy-context 无数据的后两条弱规则在 MVP 只留队列类型，实际不会出现候选。

### 6.2 编排形态

MVP 的 "Agent 层" **不是 LLM 编排**——它是确定性规则引擎 + 任务编排（对照 [vex-agent-architecture.md](vex-agent-architecture.md) §1 的五阶段：intake → evidence-collect → judgment-plan → judgment-execute → statement-publish，全部由 Python 实现，无 LLM）。理由：

1. 三强证据规则的判定逻辑完全可以确定性表达，引 LLM 只会引入幻觉面（裸 LLM triage 61–67%，[04 §5.3](../research/04-technology-deep-dive.md)）；
2. LLM 编排层（rationale 生成、SSVC 预填）是 Phase 2 的 Triage/Exploitability Agent，其接入点 = 读标准化事实写 Judgment 建议——MVP 的 Judgment/Evidence schema 已按此设计（§11）；
3. 每次判定运行的"查询原语调用序列 + 输入输出 hash"落 Evidence 表——这就是 [00-final-report](../research/00-final-report.md) §11.4 要求的 agent-trace 式审计轨迹的确定性版本，未来 LLM 加入时 trace 契约不变。

## 7. 人工签核与 Workbench 最小形态

**决定：CLI + 静态 HTML 报告，不做 Web UI。**

| 方案 | 工作量估计 | MVP 适配度 |
|---|---|---|
| **CLI + 静态 HTML（选定）** | ~1 周 | 人签是低频动作（PoC 实测 77 个关联漏洞中仅 1 条落弱证据场景，[00 §7.7](../research/00-final-report.md) 要点 4）；HTML 报告天然只读、可归档进证据包；零运维 |
| 最薄 Web UI（FastAPI + 服务端渲染） | ~3 周 | 签核按钮的体验更好，但引入认证、会话、前端构建三摊新成本；对 1–2 家伙伴无质变 |

具体形态：

- **`cra review list / show / sign / reject`**：列出队列 → 查看证据（call path、区间推导链、信号快照）→ 签核（填 justification 确认 + impact/action statement）或驳回。签核用操作者的系统身份 + 签名密钥，落 attestation。
- **静态 HTML 报告**（`cra report` 生成，单文件无依赖）：① 产品组合页（Product → Version → 未闭环漏洞水位）；② 受影响版本矩阵（每漏洞 × 每 Version 的 status + 证据链接）；③ 签核队列镜像；④ 每结论 trace 页（结论→证据→工具→工件 hash→时间戳→决策者，trace-report.md 的 HTML 化）。
- 报告每次导出时重新生成并作为证据包一部分存档——**HTML 是证据的视图，不是另一个数据源**。

升级到 Web UI 的触发条件（写进文档避免反复争论）：设计伙伴 ≥3 家，或单一伙伴签核队列周均 > 20 条。

## 8. 证据与导出

### 8.1 Attestation 签名

- 沿用 PoC：in-toto Statement v1 + DSSE 信封 + ed25519（securesystemslib），predicateType `https://cra-research.dev/attestation/conclusion/v0.1`，subject = 判定对象（product/version/vuln），predicate 含 evidence 引用、tool{name,version,command}、timestamp、signer。
- 每条 Judgment 生效（自动或人签）即签一条 attestation；supersede 不删旧 attestation（append-only，10 年留存的审计语义）。
- **密钥管理 TODO（明示不在 MVP 解决）**：MVP 用文件密钥（`keys/dev-ed25519.pem` 模式，权限 600 + 不在证据包内分发）。生产 TODO：sigstore/cosign 或客户 KMS/HSM 接管、密钥轮换、多签核人各自的 key identity。风险与缓解见 §10.2 R6。

### 8.2 证据包导出格式

沿用 PoC `out/evidence-pack-<product>-<version>/` 结构产品化：

```text
evidence-pack-<product>-<version>-<yyyymmdd>/
├── sbom.cdx.json            # 当前 Release 的 CycloneDX SBOM
├── sbom-diff/               # 与上一 Release 的组件 diff（新增）
├── vex.openvex.json         # 全部 active Judgment 的 OpenVEX 序列化
├── attestations/            # 每条 Judgment 的签名 DSSE 信封（导出时逐条验签）
├── evidence/                # call path、OSV raw 响应、信号快照等原始证据 blob
├── manifest.json            # 全文件 sha256 内容寻址索引
├── cra-mapping.md           # 导出物 ↔ CRA 条文对照（§8.3 表格落盘）（新增）
├── report.html              # §7 静态报告快照（新增）
└── trace-report.md          # 每结论追溯链（PoC 同款）
```

导出即验签（PoC `export.py` 行为保留）；导出动作本身也签一条 attestation（"谁在何时为何产品版本导出了证据包"）。

### 8.3 CRA 证据清单映射（导出物 ↔ [02 报告](../research/02-cra-regulation.md) 条文）

| 导出物 | CRA 对应 | 说明 |
|---|---|---|
| sbom.cdx.json | Annex I Part II(1)（机读 SBOM，至少顶层依赖）；Annex VII 8（MSA 合理请求须出示 SBOM） | SBOM 不要求公开（Recital），证据包是受控出示形态 |
| sbom-diff/ | Art 13(7)（系统性记录并更新产品安全信息） | 版本间组件变化的留痕 |
| vex.openvex.json | Annex I Part I(2)(a)（上市时无**已知可利用**漏洞）的判定记录；Art 13(7) | "可利用性逐案判断"的机器结论载体；not_affected 全部带 justification |
| attestations/ | Art 31 + Annex VII（技术文档与证据留存 10 年/support period 取长）的可辩护性基础 | 每条结论可验签、可追溯工具与时间戳 |
| evidence/ + trace-report.md | Annex VII 6（测试/分析记录入档） | reachability call path 等分析证据原件 |
| manifest.json | 证据包完整性锚定（I 性，见 [00 §3.10](../research/00-final-report.md)） | 任何篡改可检测 |
| report.html（受影响版本矩阵页） | Art 14(2) 报告的"受影响产品版本"输入；Art 14(8) 受影响用户范围分析的源数据 | MVP 不生成 SRP 表单，但矩阵是手工填报的第一输入 |
| KEV 标红记录（report.html + Vulnerability.in_kev） | Art 14 时钟评估的触发提示 | CRA 不强制主动监控（Commission FAQ 5.1），KEV 监听是最佳实践定位 |

## 9. 里程碑与工作量

**人力假设**：2 名工程师全职（E1 偏管道/工具链，E2 偏数据模型/存储）+ 0.5 名安全合规顾问（映射表验收、设计伙伴对接）。**总周期 10 周**（2026-09-21 起算，含 1 周 buffer）。

| 周 | 交付物 | 主责 |
|---|---|---|
| W1 | 仓库骨架（`app/`）；PG schema v1（§4 全部表）；docker compose（pg+joern 固定 digest）；PoC 脚本移植进包结构 | 两人 |
| W2 | Product/Version/Release 注册 CLI；SBOM 摄取 + 内容寻址入库 + diff；sbom-query 原语 | E2 |
| W3 | Intel Sync：OSV/GHSA/NVD/KEV/EPSS 每日同步 + 本地缓存 + 变更检测；version-range-query 原语 | E1 |
| W4 | Association 引擎 + **受影响版本矩阵**（CLI + HTML 第一页）；Story 1 验收演练 | 两人 |
| W5 | callgraph-query(Go) 服务化包装；`affected-confirm` 规则；Judgment/Attestation 写入链路打通 | E1 |
| W6 | callgraph-query(C/C++ Joern)；`component-not-present` / `code-not-present` 规则；under_investigation 兜底；vuln_function_map 表 + 策展数据入库 | E1 |
| W7 | Judgment 状态机 + 失效重估五触发器；statement publish（attest.py 嫁接 PG）；**三强证据规则端到端全自动** | E2 |
| W8 | Review Queue + CLI 签核（双主体 attestation）；HTML 报告完整版（矩阵/队列/trace）；Story 2 验收演练 | 两人 |
| W9 | 证据包导出产品化 + cra-mapping.md；CRA 映射表经合规顾问验收；Story 3 验收演练 | E2 + 顾问 |
| W10 | buffer + 设计伙伴 onboarding（装机、注册真实产品、跑通三个 Story）；成功指标基线度量 | 两人 |

**每周 DoD**：当周的 CLI 命令在干净环境（compose up 后）可重复跑通；新增判定路径有真实工具执行记录（不 mock）。

## 10. 成功指标与风险清单

### 10.1 成功指标（对齐 [00-final-report](../research/00-final-report.md) §14.2）

| 指标 | 目标 | 度量方式 |
|---|---|---|
| 新 CVE → 受影响版本矩阵产出 | **< 4h**（真实或注入演练） | 注入一条历史 CVE 情报时间戳回放到同步，计时到 HTML 矩阵生成 |
| 证据包导出 | 通过合规官验收 | 设计伙伴合规侧按 §8.3 映射表逐项核对；attestation 逐条验签 100% 通过 |
| 判定准确率基线 | 强证据判定与人工复核一致率 **≥ 95%**；证据挂接率 **100%** | 在策展测试集（PoC 两示例 + 伙伴真实产品的 20–30 个已知 CVE）上人工复核每条 Judgment |
| 人工负载 | 弱证据签核候选占比 ≤ 10%（PoC 实测 1/77） | Review Queue 统计 |
| 无静默丢弃 | 关联命中未出终态判定的条目 = 0（全部 under_investigation 兜底可见） | 状态覆盖率报表 |

### 10.2 风险清单

| # | 风险 | 等级 | 缓解 |
|---|---|---|---|
| R1 | **C/C++ reachability 精度不足**（函数指针/间接调用/条件编译，PoC 只验证了理想路径，[README](../../poc/README.md) H1） | 高 | MVP 把 callgraph-query(C) 定位为"有路径=强确认、无路径=进队列"，不依赖不可达结论；精度问题暴露为人签队列变长而非错误结论 |
| R2 | **C 侧 OSV 无条目**（PoC H3 已证伪 PURL 直查） | 高 | 策展回退产品化（vuln_function_map + curation-crosscheck）；明确告知伙伴 C 组件覆盖依赖策展投入 |
| R3 | **关联误报/漏报**（实体解析是误差第一发源地，[00 §16 R2](../research/00-final-report.md)） | 高 | range_basis 全留痕使误报可审计；backport 误报靠发行版 feed——MVP 不接，记为已知边界 |
| R4 | **under_investigation 堆积**稀释信任 | 中 | 覆盖率报表周检；优先策展 KEV/高 EPSS 命中组件的映射数据 |
| R5 | **Joern 部署重**（2.44GB 镜像、代理环境 20 分钟拉取） | 中 | 固定 digest 推内网 registry；非 C 项目不启 Joern |
| R6 | **文件密钥被视作 Toy** | 中 | §8.1 TODO 明示 + 试点协议中写清；签名动作本身留 attestation 使密钥使用可审计 |
| R7 | **设计伙伴 SBOM 质量差**（vendored/静态链接组件漏检，PoC 已踩） | 中 | ingest 时支持 augment 片段；onboarding 清单要求提供构建 manifest |
| R8 | **SRP/法规时间线变化**（SBOM implementing act 未定，[00 §16.2](../research/00-final-report.md)） | 低 | SBOM 字段按 CycloneDX 全量存档，格式校验器等 act 发布再加 |
| R9 | **Scope creep**（伙伴要求 Web UI/报告流） | 中 | §1.2 Out 清单与 §7 升级触发条件作为挡箭牌；新需求进 Phase 1 后半 backlog |

## 11. 与后续 Phase 的接口（刻意不堵死的设计决定）

| 设计决定 | 为哪个 Phase 预留 |
|---|---|
| `Judgment.evidence_strength` 字段 MVP 即写入（strong/weak） | Phase 2：弱证据规则与 SSVC 裁决接入时无需迁移 |
| `decided_by` 支持 `agent:<id>` 命名空间（schema 已允许，MVP 不出现） | Phase 2/3：LLM Agent 作为判定建议主体接入，trace 契约不变 |
| 六类查询原语统一三段式接口（deploy-context/fix-status 返回 `no_data` 而非不存在） | Phase 2/3：context 采集与修复验证闭环实现后规则即消费，规则引擎零改动 |
| Vulnerability.sources 存全部源条目 id 与原始响应 | Phase 1 后半：Art 14 工作台需要多源字段对照；失效重估 diff 依据 |
| Attestation predicate 版本化（`conclusion/v0.1`） | Phase 4：结论级 attestation 标准化/开源卡位时可演进 v0.2 不破坏存量 |
| PG 而非图数据库 + Evidence blob 内容寻址 | Phase 4：Evidence Graph 扩展为新本体节点时存储无需换（[04 §5.2](../research/04-technology-deep-dive.md) 反叙事 2） |
| SBOM format 枚举预留 spdx；VEX 序列化在导出层而非存储层 | Phase 1 后半：CSAF VEX Profile / CycloneDX VEX 另两种导出（[01 §11](../research/01-domain-ontology.md)） |
| 判定运行记录（原语调用序列 + 输入输出 hash）落 Evidence | Phase 2：LLM 编排层接入时，人机两种执行路径共用同一审计轨迹格式 |
| 单机 compose 部署 + 数据管道本地缓存 | Phase 2 起：air-gapped 知识库打包下发（[06 §C.2](../research/06-product-forms-and-tech-stacks.md)）的数据结构基础 |

---

### 附：与上游文档的对应

- 判定原则：[00-final-report](../research/00-final-report.md) §7.6（证据阶梯、无反证即 affected、弱证据强制人签、statement 版本化）
- 数据流：[00-final-report](../research/00-final-report.md) §7.7（六节点；MVP 覆盖 ①②③⑥，④⑤ 留接口）
- 编排与目录：[vex-agent-architecture.md](vex-agent-architecture.md) §2/§3/§5/§8（MVP = 其落地路径第一步 + 第三步的 statement store/签名层合并执行）
- 差异化靶心：[03 报告](../research/03-competitive-landscape.md) §6.2（"机器判定→VEX 自动化"与"statement 失效重估"两条全行业断裂带，本 MVP 全部落地）
- 技术栈底线：[06 报告](../research/06-product-forms-and-tech-stacks.md) §C.2（识别/SBOM/匹配复用开源，自研集中在对象模型/证据链/策展）
