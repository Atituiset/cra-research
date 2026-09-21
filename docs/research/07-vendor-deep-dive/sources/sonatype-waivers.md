# Source Note: Sonatype Waivers（豁免机制官方语义）

- URL: https://help.sonatype.com/en/waivers.html
- 发布方： Sonatype（官方帮助文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

1. **Waiver 粒度**：scoped 到 constraint/condition **单一组合**——"a single waiver may not remove all violations from a component"（同组件可多次违反同一 constraint）。
2. **作用域**：Application / Organization / Root Organization 层级 + 组件范围（单组件/全版本/全部组件）+ 过期时间（可永不过期；官方建议默认短期）。
3. **Stale Waiver**：scope 内当前无组件但仍激活，新组件落入即生效；有 Stale Waivers REST API。
4. **八种 reason**：Acknowledged Violation / Evaluating Component(R194) / Mitigated Externally / No Upgrade Path / **Not Reachable**（reachability 结论进入豁免理由）/ Not Exploitable（举例含 air-gapped 环境）/ Researching / Other。
5. **Zero-tolerance 失效（原文）**："Over the course of time, if any or all of the above conditions change, Lifecycle detects this as a change in policy and a previously applied waiver will not be applicable. This 'zero-tolerance to risk' built into Lifecycle…"——例：CVSS 6.5→5.8 即致 waiver 失效需重建。
6. **与 Firewall 的交互**：waiver 释放隔离组件；释放后组件在仓库内不会再被隔离（见 firewall-quarantine note #8）。官方建议 Firewall waiver 用 repository 级 scope 或短期 waiver。
7. **Legacy Violations**：policy 级批量隐藏存量违规（"接受基线风险不做逐条评审"），适合不再活跃开发的 legacy 应用；官方建议优先用它而非批量 waiver。
8. 六种典型用例表（defer fix / reachability 反馈注释 / 降噪 / 组织级通用豁免 / 告知干系人 / 工作流工具）——含官方建议的 scope 时长（如 6-12 个月复核）。

## 支撑报告结论

- 主文档 §2.2（waive 机制）、§10.2（时序缝隙）；zero-tolerance 失效是"waiver 防漂移"硬机制的一手证据。
