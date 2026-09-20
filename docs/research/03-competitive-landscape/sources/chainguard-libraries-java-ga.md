# Source Note: Chainguard Libraries for Java GA + CVE Remediation（官方博客）

- URL: https://www.chainguard.dev/unchained/chainguard-libraries-for-java-is-now-ga-and-includes-cve-remediation
- 标题: Chainguard Libraries for Java is now GA; CVE remediation beta available for sign up
- 发布方: Chainguard 官方博客（Unchained）
- 发布日期: 2026-06-23
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方博客（产品发布）

## 关键事实点

- Chainguard Libraries for Java GA；新增 CVE remediation（beta 注册），为 critical/high CVE 做**反向移植修复（backport）**，首发 Spring Boot 生态；已覆盖 spring-boot/spring-framework/spring-security/h2database 的数十个 CVE。
- 动机数据（厂商引用）：Spring 仅 2026-04 收到 482 个新安全报告；CVE 平均被利用时间从 2018 年 63 天变为 2025 年 **-7 天**（exploit 早于 patch）。Spring Boot 2.7 EOL 后累计 143 个 CVE（79 个项目）无补丁。
- 第四种修复路径：不改大版本、不换 patch 文件叠加，而是换成 Chainguard 重新构建的修复版本（版本号带 `-0.cgr.N` 后缀），**扫描器和审计者看到的是干净的版本化制品而非 patch**——解决"patch 叠加导致审计痕迹问题"。
- 所有修复包附带 SBOM 与 provenance；控制台可查看每版本修复了哪些 CVE；通过**公开 VEX feed** 提供修复版本信息。
- 扫描器互认：Wiz、Amazon Inspector、Grype、Upwind、Anchore Enterprise、Trivy 已识别 Chainguard 修复版 Java 库。
- 配套：Python Libraries GA（2025-10-22，含 CVE remediation + 恶意包防护）；CRA 文章（2026-01-14）；THN 报道"critical CVE 平均 20 小时内消除"（厂商声称经媒体转述）。

## 支撑报告结论

- "修复"环节的范式创新：从"升级 PR/patch 叠加"到"重建制品+干净版本号+VEX feed"，直接对准审计/证据问题——最接近"修复→验证→证据更新"闭环的现有实现。
- 支撑"agentic remediation 可信度"之外的另一条路：**厂商托管的修复即服务**。
