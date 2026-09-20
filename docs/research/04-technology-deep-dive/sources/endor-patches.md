# Source Note: Endor Patches — 上游修复 backport 到当前版本

- URL: https://github.com/endorlabs/endor-patches ；https://www.endorlabs.com/use-case/endor-patches ；https://www.endorlabs.com/learn/how-endor-patches-are-built-and-tested
- 标题: Endor Patches / How Endor Patches Are Built and Tested
- 发布方: Endor Labs（开源仓库 + 厂商工程博客）
- 日期: 博客 2025-02-18；GitHub 仓库 2026-07 仍活跃；抓取日期 2026-09-18
- 来源层级: 开源项目 + 厂商工程博客

## 关键摘录 / 技术要点

- Endor Patches 是"带 backport 漏洞修复的软件包精选集"：识别修复漏洞的 upstream commit 与 vulnerable function，把修复 backport 到客户当前使用的版本，最小化、可复现、"audit-ready"，避免大版本升级。
- 流程（博客）：定位 fix commit → backport → 兼容性与安全性测试。
- 同类先例：Seal Security（对 RHEL/Debian 式 standalone patch 的商业化）、Chainguard、HeroDevs 等也做 old version 补丁维护（不确定各家的具体技术路线，未逐一核实）。

## 支撑报告结论

- 第三部分：patch backport 已产品化，其核心技术 = **fix commit 定位（vulnerability→patch 映射数据）+ 最小 cherry-pick + 回归构建/测试**；前两步依赖漏洞数据策展，验证靠确定性 CI。这是"Remediation 能力阶梯"中 fix version 推荐与 AI 重写之间的现实中间层。
