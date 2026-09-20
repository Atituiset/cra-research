# Source Note: PURL/VERS 项目官方介绍

- **URL**: https://www.packageurl.org/docs/purl/introduction
- **标题**: Welcome to packageurl.org — PURL 与 VERS
- **发布方**: Package-URL 项目（Ecma TC54/TG2）
- **发布日期**: PURL v1.0.0 于 2025-12-10 经 Ecma General Assembly 批准为 ECMA-427；项目 v1.0.0 release 2025-12-18
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. PURL 定义："a standard URL-based syntax to identify software packages, independent from their ecosystem or distribution channel" —— 生态无关的包标识语法。
2. 姊妹标准 **VERS**（VErsion Range Specifier）：统一版本区间表达，解决"各生态版本范围记号不一致"和"漏洞影响版本区间表达歧义"两个问题；VERS 计划 2026 年晚些时候提交 Ecma。
3. PURL 2025-12 获批为 **ECMA-427**，并在 ISO 快速通道上。
4. 每个 PURL **type** 对应一个包管理器/平台/生态的约定；type 注册表是规范的一部分。
5. 官方声称解决的问题：包标识歧义、跨生态互操作、可追溯性与风险管理、工具自动化（SCA、漏洞管理、license compliance 都被点名）。
6. PURL 可通过 `vers` qualifier 携带版本区间。

## 支撑报告中的结论

- §9 PURL 定义、type/qualifier 结构、与 VERS 的关系
- §9 "PURL 为什么更适合现代生态"：生态原生命名 + 标准版本区间语义
- §17 标准总表（PURL/VERS 行，ECMA-427）
