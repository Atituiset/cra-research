# Source Note: Sonatype Repository Firewall 与 Quarantine 机制

- URL: https://help.sonatype.com/en/repository-firewall.html ；https://help.sonatype.com/en/firewall-quarantine.html
- 发布方： Sonatype（官方帮助文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（一手）

## 关键事实点

1. **架构**：IQ Server 驱动，挂 proxy repository 层；兼容 Nexus Repository Pro 3.38.1+ 与 **JFrog Artifactory 7.2.6+（SaaS 不支持）**。无 IQ Server/仓库时功能受限。
2. **协议限制**："Repository Firewall relies on the human-readable errorPhrase from the HTTP/1.1 protocol. **HTTP/2 is not supported.**"
3. **Quarantine 语义**：proxy 阶段 Fail → 新请求组件隔离，返回错误+组件详情链接；**"only quarantines newly requested components — components already found in the proxy repository are audited but not quarantined"**（避免打断构建）；删除后重新请求会被重新隔离。
4. **Fail-closed**："The quarantine service will 'fail closed' to limit risk"——服务不可用+quarantine 开启时，新组件请求一律进隔离；禁用 Firewall 会释放全部隔离组件。
5. **客户端怪癖**：NuGet 客户端把 403 硬编码为认证失败 → 只能返回 **409**；Pub（dart pub get）返回 **451**（NR 3.97.0 新增）。
6. **Proxy 阶段动作**：Fail=隔离 / Warn=邮件通知 / No Action=仅审计报告（默认）。
7. **隔离释放**：必须 waive 全部 failing violations → re-evaluate → 释放；违规不再 open 时自动释放。
8. **time-based waiver 漏洞（官方自曝）**：waiver 过期后违规重现，但"since it is already in the repository, it will not be quarantined"；要重新隔离须先删缓存。
9. **生态覆盖**：npm/PyPI/Maven/NuGet/Go/RubyGems/Cargo/Conda/CocoaPods/Composer/Conan/CRAN/Pub/Swift/Docker/**Hugging Face（IQ 191+，按 .bin/.pt/.safetensors/.pkl 等扩展名）**/Raw 任意静态站点。
10. **不支持 Legacy Violations**。

## 支撑报告结论

- 主文档 §2.2（quarantine/waive）、§3（Firewall 实现）、§10.1–10.3（自曝局限）。
