# 研究日志：JFrog 第二轮 Competitive Deep Dive

- 日期：2026-09-21
- 执行：子代理调研（一轮完成）
- 主文档：`docs/research/07-vendor-deep-dive/jfrog.md`
- 范围约束：03 报告 §1.5/§6 已核实的事实不重复，只做加深与更新。

## 检索与抓取记录（按维度）

| # | 维度 | 关键查询/URL | 结果 |
|---|---|---|---|
| 1 | Xray 架构 | `Xray architecture component identification checksums`；抓取 docs: jfrog-xray-service、database-and-third-party-applications、index-xray-resources；KB different-scan-results | ✅ 六个微服务职责表、PostgreSQL checksum 组件图、opt-in 索引+上传即扫+新 CVE 反向定位 |
| 2 | Contextual Analysis 工程 | 抓取 2022 年 78% 研究博文（jfrog.com/blog）、contextual-analysis-of-cves-1 文档、CLI command summaries、jfrog-cli-security#592 | ✅ 最大收获。博文含大量自曝（无法自动策展、保守 FP、数据流取舍、3rd-party 许可限制）；文档 Upgrade Required 状态暴露 scanner 随 Xray 版本分发 |
| 3 | Air-gapped | `Xray offline update DBSync`；抓取 xray-offline-database-sync | ✅ DBSync v3 三流（public_data/exposures/contextual_analysis）+ periodic 包 + license-id |
| 4 | AppTrust/Evidence | `AppTrust evidence in-toto DSSE`；抓取 create-evidence-cli、jfrog-apptrust、github-attestation-to-jfrog-evidence、jfrog-mcp-server-tools（Evidence 段） | ✅ 证据=DSSE 信封包 in-toto statement，密钥 RSA/Ed25519/ECDSA，支持 Sigstore bundle；evidence 随 promotion 流转；4h 公钥缓存 |
| 5 | 对象模型 | AppTrust Overview + MCP AppTrust 工具字段 | ✅ 重要更新：application 成为一等实体（maturity_level 含 end_of_life；version 三态 PRE_RELEASE/RELEASED/TRUSTED_RELEASE） |
| 6 | Remediation | 抓取 smart-remediation、zero-touch-remediation-overview、interpret-remediation-in-scan-results；Chainguard changelog 交叉印证 | ✅ Smart Remediation 算法全披露（权重/策略/500 截断/best-effort 免责）；ZTR 双路径（Maven 下载拦截 / npm lockfile healing）+ Least Vulnerable 权重 + local patch API |
| 7 | AI/Agent | `JFrog MCP server agentic Fly swampUP`；抓取 MCP tools 全文 | ✅ MCP Server 官方工具面完整（含 Curation waiver 审批、Evidence 创建）；Fly/Self-Healing（2025-09）；Agent Guard（2026-09）；agent 行为签名证据化 |
| 8 | 数据底座 | Catalog 文档 + MCP OneModel + §1 的 PostgreSQL 事实 | ✅ 无专用图库证据；Catalog GraphQL；OneModel Beta |
| 9 | 定价 | 抓取 jfrog.com/pricing（全文 55k 字符，grep 定位关键行） | ✅ SaaS Pro $150/月、Enterprise X $950/月起；self-hosted Pro X $27k/年、Enterprise X $51k/年；AppTrust 仅 Ultimate |
| 10 | 局限自曝 | 贯穿 2/6/9 的官方文档免责条款 | ✅ 汇总为主文档 §10 八条 |

## 对 03 报告的修正/更新建议（未回写 03，待主代理决定）

1. §1.5 第 6 条（Reachability 评级 ◐）：机制细节已充分，评级不变但可补"scanner 随 Xray 版本分发、人工策展"注脚。
2. §1.5 第 10 条（"AI/Agent：弱"）：**已过时**——2025-09 起 MCP Server 官方化 + Fly + agentic remediation，应上调至至少 ◐。
3. §1.5 第 12 条（Product→Version "部分偏强"）：AppTrust application 一等实体（ownership/criticality/maturity 含 end_of_life）使该维度进一步走强，距 CRA 语义只差"支持期时间轴"字段。
4. §7 风险①（JFrog 升级对象模型收窄空白）：**正在兑现**——CRA policy templates 已一键化、post-release support windows 监控已出现在定价页文案。

## 弃用/未采信来源

- Medium/博客园/腾讯云等第三方 Xray 架构转载（微服务职责描述与官方文档一致，但以官方为准）。
- startupstash、peerspot、stackinsight 等聚合站：仅用于线索，不作事实来源。
- skywork.ai 的 JFrog MCP 长文：AI 生成痕迹明显，未采信，MCP 事实全部以 docs.jfrog.com 为准。

## 未能核实（已列入主文档 §12）

checksum 重打包兜底、immutable 实现、图 schema 规模、scanner 规则 DSL、DBSync 包完整性校验、ZTR vendor rebuild 的 verify 语义、CRA Rego 模板内容。
