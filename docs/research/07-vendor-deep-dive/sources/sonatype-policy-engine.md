# Source Note: Sonatype Lifecycle 策略引擎（Policy Constraints 官方语义）

- URL: https://help.sonatype.com/en/policy-constraints.html （页更新 2026-08-10）
- 发布方： Sonatype（官方帮助文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

1. **模型**：Policy → Constraint（policy 内 OR）→ Condition（constraint 内 ANY/ALL）。"A policy is considered in violation when any constraint of the policy evaluates to a true statement."
2. **策略类型自动归类**：Security > License > Quality > Other 优先级。
3. **Security conditions**：CVSS（默认 v4，缺则回落 v3/v2）、Proprietary Name Conflict（Firewall 专用，防 dependency confusion）、Vulnerability Category（Data/Operational/Functional/Configuration/Test Code/Sample Code/Privileged/Malicious Code/Other）、Vulnerability Status（Open/Acknowledged/Not Applicable/Confirmed）、CWE、Vulnerability Group、**Security Research Type（Sonatype Fast Track / Deep-Dive / Public Research / Vendor Research——策展队列分级可直接做策略条件）**、Custom Remediation、**Detection Type（Primary/Secondary/AST/CPE Match/Unshaded/Other）**、Custom CVSS。
4. **KEV Status / EPSS Score**：IQ 199 起 Repository Firewall 评估也可用 KEV/EPSS 条件；EPSS 支持 =/>/>=/</<=/does not exist。
5. **Quality conditions**：Relative Popularity（仅 Maven Central）、Age（按 Sonatype catalog 时间、滚动 24h 计；Docker 组件无 catalog date）、Hygiene Rating（Laggard/Exemplar）、Integrity Rating（Normal/NA/Pending/Suspicious）。
6. **Other conditions**：Label、Match State（Exact/Similar/Unknown/Embedded）、Format（含 hf-model）、逐生态坐标（a-name/cargo/.../swift 全列）、Package URL（purl 通配）、Proprietary、Identification Source、Component Category、Data Source、Dependency Type（Direct/Transitive/InnerSource；unknown 类型不评估策略）、**EOL（Maven/npm/NuGet/PyPI）**、**Derivative AI Model / AI Content（AI 模型治理条件）**。
7. **Unknown 组件**只触发 Match State/Proprietary/Data Source 三个条件。

## 支撑报告结论

- 主文档 §2.1（policy 模型）；"按数据可信度（research type / detection type）做策略"是本页独有证据。
