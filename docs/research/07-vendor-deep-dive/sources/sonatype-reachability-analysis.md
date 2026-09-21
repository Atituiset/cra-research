# Source Note: Sonatype Reachability Analysis（03 报告修正依据）

- URL: https://help.sonatype.com/en/reachability-analysis.html （页更新 2026-09-04）
- 发布方： Sonatype（官方帮助文档，Sonatype Developer 文档树）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

1. **粒度**：method 级——"If a vulnerable component is detected **and** the application code calls a specific method in that component which could be exploitable, the policy violation is labeled as 'Reachable'"。反例：LaTeX 库 RCE 方法从未被调用 → Not Reachable。
2. **语言支持**：Java/JVM 二进制、JavaScript/Node.js、**.NET（NuGet + PE/COFF，IQ 203 起，2026-05）**。
3. **扫描对象**：application artifact（JAR/WAR/class 目录），检查应用二进制+依赖二进制；**容器 target 不支持**；全 CI 集成可用（Jenkins/GitLab CI/GitHub Actions/Azure DevOps/Bamboo）。
4. **Reachability Evidence**：违规详情页展示压缩调用路径（stacktrace 风格，component 分节、跨组件省略、最多 N 条），**仅 Java**；JS/.NET 无 evidence。`-rn/--reachability-namespaces` 限定命名空间，否则"every method treated as entry point → paths very long and noisy"。
5. **Unknown（"-"）六种原因**：无 CVE / 不支持类型 / IQ 无法识别组件 / 在 namespace 配置外 / 依赖制品不在扫描目标 / **漏洞无法映射到可调用方法**。
6. Evidence 不出现在：Not Reachable、未开启分析、**Firewall 或 SBOM Manager 视图**（reachability 证据只在 Lifecycle 扫描结果中）。
7. 系统属性可调：`sonatype.reachability.evidence.enabled`（kill switch）/`.maxPaths=10`/`.componentDepth=6`（self-hosted only）。

## 支撑报告结论

- **修正 03 §1.4"无 function 级 reachability"**：已有 method 级 reachability + Java 调用路径证据；但证据未接入 SBOM Manager/Firewall 视图，reachability→VEX 注释仍需人工搬运（03 §6 闭环结论不受影响，反而更硬）。
