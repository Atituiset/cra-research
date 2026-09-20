# Source Note: OSV Schema 规范

- **URL**: https://ossf.github.io/osv-schema/
- **标题**: Open Source Vulnerabilities schema (Version 1.9.0, August 6, 2026)
- **发布方/作者**: Oliver Chang (ochang@google.com)、Russ Cox (rsc@google.com)（Google / OpenSSF 托管）
- **发布日期**: 1.9.0 版 2026-08-06
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（规范原文）

## 关键摘录 / 事实点

1. 目的原文："define a standard interchange format for describing vulnerabilities in open source packages … enable automated, accurate, and distributed management of vulnerabilities in open source dependencies."
2. Schema 顶层字段：`schema_version`, `id`, `modified`, `published`, `withdrawn`, `aliases`, `upstream`, `related`, `summary`, `details`, `severity[]`, `affected[]`, `references[]`, `credits[]`, `database_specific`。
3. `affected[].package` 结构：`{ ecosystem, name, purl }` —— **以 package ecosystem + name（可选 PURL）标识组件**，不用 CPE。
4. `affected[].ranges` 是事件序列：`{"type": "SEMVER|ECOSYSTEM|GIT", "events": [{"introduced": ...}, {"fixed": ...}, {"last_affected": ...}, {"limit": ...}]}`；也可用显式 `versions[]` 枚举。
5. `id` 格式为 `<DB>-<ENTRYID>`（如 `GHSA-xxxx`、`PYSEC-xxxx`），**OSV 不是单一数据库，而是多数据库共用的交换格式 + osv.dev 聚合服务**。
6. 设计哲学：只定义数据库间必须共享的字段，其余放进 `ecosystem_specific` / `database_specific` 扩展块。
7. 示例：`[{"introduced": "0"}, {"fixed": "1.0.2"}]` 表达 "1.0.2 之前的版本全部受影响"。

## 支撑报告中的结论

- §5 OSV Schema 结构拆解（ecosystem/package/versions/ranges）
- §5 OSV 与 CPE 模型对比：package-ecosystem 原生 vs 统一产品字典
- §5 "OSV 为什么适合 SCA"：version range 直接可做依赖版本匹配，无需 CPE 名映射
- §7 五者对比表中 OSV 一行
