# Source Note: GitLab Static reachability analysis（官方文档）

- URL: https://docs.gitlab.com/user/application_security/dependency_scanning/static_reachability/
- 标题: Static reachability analysis
- 发布方: GitLab（官方文档）
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方文档

## 关键事实点

- 粒度：**package 级**（判断 SBOM 中的依赖是否被应用 import/使用），非 function 级。直接依赖被标记 reachable 时其传递依赖也标记 reachable。
- 工作方式：dependency scanning 生成 SBOM（CycloneDX）→ 静态 reachability 用包名→import 路径的元数据映射（周更新）补充 reachability 值 → 富化后的 SBOM 回传 GitLab。
- 状态值：Yes / Not Found / Not Available。
- 支持语言（全部 Beta）:
  - Python（pip/pipenv/poetry/uv）
  - JavaScript/TypeScript（npm/pnpm/yarn；不支持前端框架）
  - Java（maven/gradle）
- 文档明确承认 Java 局限：反射、JDBC 连接串可检测，但 Spring Boot 等 DI 动态加载无法识别，假阴性高；覆盖仅限 GitLab advisory DB 与 Maven Central 高依赖包。
- 相关：GitLab Docs Dependency scanning 页提到 "agentic breaking change resolution (for dependency bumps)" —— GitLab Duo 可分析依赖升级导致的失败并给出修复（厂商文档）。

## 支撑报告结论

- GitLab 的 reachability 明显落后于 Snyk/Endor（package 粒度 + Beta + 3 语言）→ 支撑"function-level reachability 语言覆盖仍是稀缺能力"。
- "SBOM 富化后回传"的架构说明 GitLab 以 SBOM 为数据中枢。
