# Source Note: Grype/Anchore 匹配引擎与发行版 backport 处理（官方文档 + 社区 + GitHub issue）

- URL: https://docs.anchore.com/current/docs/vulnerability_management/how_it_works/ ；https://anchorecommunity.discourse.group/t/does-grype-fetches-data-from-different-sources-or-only-from-nvd/136 ；https://github.com/anchore/grype/issues/1541
- 标题: How It Works — Anchore Enterprise / Grype data sources discussion / Grype doesn't take account OS distributor patch release (#1541)
- 发布方: Anchore 官方文档；Anchore 社区（维护者回复）；Grype GitHub issue
- 发布日期: 文档页 2026-06-16；社区 2024-09-16；issue 2023-10-05
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档 + 开源社区一手

## 关键事实点

- 数据管道：Grype 不直接查 NVD——由 **grype-db** 把 NVD + 各发行版安全 feed（Alpine/Amazon/Chainguard/Debian/Mariner/Oracle/RHEL/SUSE/Ubuntu/Wolfi 的 distro maintainer feed）+ GHSA 等**预加工成约 1GB 的 SQLite 库**分发；Grype 与 Anchore Enterprise 共用同一匹配过程。
- 匹配器按生态实现（OS 包用发行版 feed 的 fix 版本，语言包用 NVD/GHSA 版本区间）——**backport 感知 = 匹配到正确的发行版 feed**，而非算法。
- Issue #1541（一手反证）：对 SUSE 系版本，`4.7.1-150200.3.10.1` 与 NVD 修复版本 `4.9.1` 直接比较必然误报——说明**一旦落到 NVD CPE 版本比较路径，backport 即失效**，误报控制依赖发行版 feed 覆盖率。

## 支撑报告结论

- 匹配引擎的业界实际栈：预加工漏洞 DB（SQLite 交付）+ 生态专用 matcher；backport 是数据工程问题不是匹配算法问题；误报控制的边界 = 发行版 feed 的覆盖与质量。
