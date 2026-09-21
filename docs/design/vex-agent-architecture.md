# VEX 判定平台 Agent 架构设计

> 2026-09-20。基于两项已有资产：① 本仓库研究（[00-final-report](../research/00-final-report.md) §7.6/§7.7 判定逻辑与数据流、[04 报告](../research/04-technology-deep-dive.md) §3"LLM 编排 + 确定性引擎出证据 + 人工签核"）；② `/home/atituiset/Projects/review-skills` 的"全 Skill、分阶段子 Agent 编排"架构（五阶段、Session 文件交接、Semantic Query 出事实 / 规则 Skill 推理）。
>
> 核心论点：**review-skills 架构与 VEX 判定管道几乎同构**——最难的编排协议与证据契约已经存在，缺的只是换一套领域规则、补四块 CRA 专用组件。

## 1. 架构映射：review-skills → VEX 判定平台

| review-skills | VEX 判定平台 | 说明 |
|---|---|---|
| Main Agent（只编排） | VEX Orchestrator | 不加载分析材料，只读 handoff |
| pre-process（target/meta/units + worktree 基线） | **Intake**：归一化输入（product/version/CVE 三元组），固定基线（SBOM sha256 + 情报快照时间戳） | meta.json 的"基线固定" = 证据链的"输入锚定" |
| preload（context/files/functions/queries） | **Evidence Collection**：跑确定性工具（syft/OSV/govulncheck/Joern），raw 原文与标准化事实分离 | `查询请求 → raw → 标准化事实 → 规则判断` 即 §7.7 数据流骨架 |
| dispatch（plan.json：每单元跑哪些 CWE Skill） | **Judgment Planning**：每个 CVE 决定要跑哪些判定 Skill | 分派 ≠ 结论 |
| review-execute（cwe-476/416/401 规则 Skill） | **Judgment Execute**：六种 justification 规则 Skill（见 §3） | 规则即领域知识 |
| post-process（去重/汇总/findings.json/SARIF） | **Statement Publish**：合并判定 → OpenVEX 序列化 → attestation 签名 → 证据包导出 | |
| session/pipeline/handoffs/trace | Agent 执行审计轨迹 | CRA 要的 execution trace 可审计性 |

**场景三态 ↔ VEX 四态（1:1 映射）：**

```text
confirmed（有证据问题成立）  →  affected（有证据受影响，如 call path 存在）
excluded（有依据排除）       →  not_affected + justification（排除依据 = justification）
unresolved（证据不足）       →  under_investigation（兜底，不静默丢弃）
```

review-skills 已解决的两个细节直接对应 CRA 要求："excluded 只排除记录的场景，不证明整体安全" = "unreachable 是弱证据"；"findings 为空不代表没检查，排除依据仍保存" = "not_affected 必须带 justification 与证据"。

## 2. 目录结构（skills/vex/）

```text
skills/vex/
├── SKILL.md                          # 入口：编排协议（对照 skills/review/SKILL.md）
├── references/
│   ├── stage-agent.md                # 子 Agent 交接协议（平移）
│   ├── contracts.md                  # 数据契约说明
│   ├── vex-statuses.md               # 四 status + 五 justification 规范摘要
│   └── tools.md                      # 工具带与查询原语（本文 §4/§5）
├── skills/
│   ├── pipeline/
│   │   ├── intake/SKILL.md
│   │   ├── evidence-collect/SKILL.md
│   │   ├── judgment-plan/SKILL.md
│   │   ├── judgment-execute/SKILL.md
│   │   └── statement-publish/SKILL.md
│   ├── query/                        # 六类查询原语（§5）
│   │   ├── sbom-query/SKILL.md
│   │   ├── version-range-query/SKILL.md
│   │   ├── callgraph-query/SKILL.md
│   │   ├── threat-signal-query/SKILL.md
│   │   ├── deploy-context-query/SKILL.md
│   │   └── fix-status-query/SKILL.md
│   └── judgment-rules/               # 六个判定规则（§3）
│       ├── affected-confirm/SKILL.md
│       ├── component-not-present/SKILL.md
│       ├── code-not-present/SKILL.md
│       ├── not-in-execute-path/SKILL.md      # 弱证据 → 强制人工签核
│       ├── not-controllable/SKILL.md         # 弱证据 → 强制人工签核
│       └── inline-mitigation/SKILL.md        # 弱证据 → 强制人工签核
└── schemas/
    ├── vex-target.schema.json        # 输入三元组（对照 review-target）
    ├── evidence.schema.json          # 标准化事实（对照 query-result）
    ├── judgment-plan.schema.json     # 对照 dispatch-plan
    ├── judgment-record.schema.json   # 对照 review-record（confirmed/excluded/unresolved）
    ├── statement.schema.json         # 对照 finding → OpenVEX statement
    ├── attestation.schema.json       # in-toto Statement v1 + conclusion/v0.1 predicate
    ├── session.schema.json / pipeline.schema.json / stage-handoff.schema.json
    └── meta.schema.json
```

## 3. 判定规则 Skill（judgment-rules/）

每个规则 Skill 遵循 review-skills 的证据契约：产出 confirmed/excluded/unresolved 场景 + 证据引用 + 缺失信息 + 下一步查询。与 CWE 规则的对应：

| 规则 Skill | 判定目标 | 需要的查询原语 | 证据强度 | 签核 |
|---|---|---|---|---|
| `affected-confirm` | 版本在受影响区间且无反证；有 call path 则强确认 | sbom / version-range / callgraph | 强（区间命中 + 可达路径） | 自动 |
| `component-not-present` | 组件不在产物中 | sbom | 强（机器可证） | 自动 |
| `code-not-present` | 漏洞代码不在包内（只用子模块、版本已 backport 修复） | sbom / version-range | 强（机器可证） | 自动 |
| `not-in-execute-path` | 静态不可达 | callgraph | **弱（静态分析证不了不可达）** | **人工** |
| `not-controllable` | 攻击者控制不了输入 | deploy-context / callgraph | **弱** | **人工** |
| `inline-mitigation` | 已有内联缓解 | deploy-context | **弱** | **人工** |

状态机：`under_investigation → affected → fixed`；`fixed` 由 fix-status 查询的确定性验证（新 SBOM 重扫 + 构建测试通过）触发，全自动。新情报到达或规则 Skill 更新时，旧 statement 失效重估（复用 execution-manifest.sha256 机制：记录规则内容哈希，恢复时校验）。

## 4. 工具带（分判定节点）

### ① Presence —— SBOM/组件清单

| 工具 | 场景 | 说明 |
|---|---|---|
| **Syft**（PoC 已用） | 源码/镜像/文件系统 → CycloneDX/SPDX | 局限实测：静态链接 vendored C 库检不出 |
| cdxgen | 语言生态更全（含 conan/vcpkg） | OWASP |
| Trivy | 容器镜像为主 | 扫描一体 |
| 构建系统自身 | `go list -m -json all`、CMake `compile_commands.json` | 最接近"构建真相"的 presence 证据 |
| OWASP blint | 无源码二进制/固件 | 二进制 SBOM |

### ② Association —— 情报与版本区间

| 工具/数据 | 说明 |
|---|---|
| **OSV API**（PoC 已用） | 主轨道：PURL 直查、`/v1/querybatch` 批量、版本区间 events |
| osv-scanner | 现成 CLI，`--call-analysis`（Go/Rust） |
| GHSA（GraphQL API） | reviewed 层质量高 |
| NVD API 2.0 | fallback + CPE；2026 起放弃全量 enrichment（[01 报告](../research/01-domain-ontology.md) §4） |
| deps.dev API | 包元数据 + 版本解析辅助 |
| Vendor CSAF（Red Hat / Debian tracker） | backport 真相源；开源 `csaf_walker` |
| CISA KEV feed + FIRST EPSS API | 每日同步，近零成本 |

### ③ Reachability —— 分语言

| 语言 | 工具 | 粒度 | PoC |
|---|---|---|---|
| Go | **govulncheck**（官方） | 符号级，直接输出 OpenVEX | ✅ |
| C/C++ | **Joern**（CPG + `compile_commands.json`，用 `bear` 截获构建命令） | 函数级 call path | ✅ |
| C/C++ 备选 | CodeQL | 精度高但**商用需 GHAS 许可**（见 §6） | — |
| Java | Soot / WALA（框架，需自建） | 函数级 | — |
| JS/TS、Python | tree-sitter + Semgrep/OpenGrep | 模块/函数级，动态语言精度天然受限 | — |
| **vuln→function 映射** | 解析 fix commit diff + cvelistV5 官方 JSON 仓 | 策展数据，非现成工具——**成本中心**（[04 报告](../research/04-technology-deep-dive.md) §1.5） | ✅ 手工策展 |

### ④ Exploitability context

| 工具 | 说明 |
|---|---|
| K8s API（labels/annotations）+ 云 metadata | 生产标记、暴露面 |
| Ingress/LB/WAF 配置扫描 | 网络可达性 |
| eBPF 系（Tracee / Falco / Inspektor Gadget） | 运行时 reachability 开源底座 |
| Semgrep 自定义规则 | feature flag / 配置静态分析 |
| CISA SSVC（官方 JSON 决策树） | 裁决框架本体 |

### ⑤ Fix & Verification

| 工具 | 说明 |
|---|---|
| OSV fixed events / deps.dev | fix version 来源 |
| Renovate（Apache-2.0）/ Dependabot | 升级 PR |
| CI 重扫 + CycloneDX diff | 修复验证证据 |

### ⑥ Statement 生成与存证

| 工具 | 说明 |
|---|---|
| **OpenVEX + vexctl** | statement 生成/合并/查询；Grype `--vex` 可直接消费——闭环 |
| CycloneDX CLI / CSAF 工具链 | 另两种序列化导出 |
| **in-toto + sigstore/cosign**（PoC 已用 in-toto + ed25519） | 签名存证；生产用 sigstore 管密钥 |

## 5. 六类查询原语（对照 review-skills 七类查询映射）

| 查询原语 | 包装的工具 | 输出（标准化事实） |
|---|---|---|
| sbom-query | Syft/cdxgen/构建系统 | 组件条目 + PURL + sha256 + 来源 |
| version-range-query | OSV/GHSA/NVD/deps.dev + backport feed | 受影响区间、本版本是否命中、依据条目 id |
| callgraph-query | govulncheck/Joern/tree-sitter | reachable? + call path（节点含文件:行号）+ 引擎精度声明 |
| threat-signal-query | KEV/EPSS | 在野利用状态、30 天利用概率、抓取时间 |
| deploy-context-query | K8s/云/Ingress/eBPF | 生产标记、暴露面、运行时加载证据 |
| fix-status-query | OSV fixed/Renovate/CI | fix version、升级结果、重扫记录 |

每个原语遵循 review-skills 的 `请求 → raw 原文 → 标准化事实` 三段式，raw 保留供回查；工具失败/歧义/截断如实记录，不得静默降级。

## 6. 许可证注意事项

- **CodeQL**：对私有代码商用需 GitHub Advanced Security 许可；自建商业产品的 C/C++ 底座建议 Joern（Apache-2.0）。
- **OpenGrep**：Semgrep 改 LGPL 后的社区分叉，商用 SAST 底座选型时留意许可差异。
- govulncheck / Joern / Syft / Trivy / Renovate / OpenVEX / in-toto / sigstore 均为宽松许可（Apache-2.0 为主），可安全商用。
- NVD/OSV/GHSA/KEV/EPSS 数据为公开数据，注意各 API 的 rate limit 与缓存策略（本地镜像 + change-history 增量）。

## 7. 为 CRA 场景补的四块（review-skills 没有的）

1. **签名层**：judgment-record/statement 现在是无签名 JSON；在 statement-publish 阶段包 in-toto attestation（PoC `attest.py` 可直接嫁接），每条结论：工具+版本+命令+输入输出 hash+时间戳+签名者。
2. **人工签核闸**：弱证据规则（not-in-execute-path / not-controllable / inline-mitigation）在 publish 前必须经过 human gate；复用 agent-inspection 标记机制——"未经确定性引擎证明的排除结论"自动挂起等人签，签名记录"人+系统"双主体。
3. **长生命周期 statement store**：review session 是一次性的；VEX statement 要活 10 年、跨 session 演进。session 是"判定的执行现场"，statement store 是 session 之外的一等对象（PostgreSQL，刻意不用图数据库——[04 报告](../research/04-technology-deep-dive.md) §5.2）。
4. **触发层编排**：review-skills 是用户发起；VEX 平台是情报驱动批量发起——新 CVE/KEV 更新 → 匹配受影响产品版本 → 为每个 (product, version, vuln) 三元组拉起判定 session。Orchestrator 之上一层 watch/trigger。

## 8. 落地路径建议

1. **第一步（对照 PoC 已有资产）**：把 `skills/review/` 复制为 `skills/vex/`，五阶段改名换契约；judgment-rules 先实现三个强证据规则（affected-confirm / component-not-present / code-not-present）+ under_investigation 兜底——这部分全自动，无人工闸，可立即端到端。
2. **第二步**：接 callgraph-query（Go 用 govulncheck、C 用 Joern，PoC 脚本即查询原语实现），加 not-in-execute-path 规则 + 人工签核闸。
3. **第三步**：statement store + 签名层（嫁接 PoC attest/store/export），statement 状态机与失效重估。
4. **第四步**：触发层（KEV/OSV watch）+ deploy-context 查询 + 剩余两个弱证据规则。
5. **全程**：每个阶段按 review-skills 的 validation 惯例落验证记录（docs/validation/），真实工具执行与 agent-inspection 明确区分。

## 9. 与研究结论的对应关系

- 架构形态 = [04 报告](../research/04-technology-deep-dive.md) §3.2/§3.3"LLM 编排 + 确定性引擎出证据 + 人工签核"的 Skill 化实现；
- 判定逻辑 = [00-final-report](../research/00-final-report.md) §7.6（判定原则）+ §7.7（数据流）；
- 工具选型 = [06 报告](../research/06-product-forms-and-tech-stacks.md) §B（技术栈入场底线：复用开源，自研集中在对象模型/策展数据/C++ reachability）；
- 证据模型 = PoC 已验证的 conclusion/v0.1 attestation schema（`poc/pipeline/attest.py`）。
