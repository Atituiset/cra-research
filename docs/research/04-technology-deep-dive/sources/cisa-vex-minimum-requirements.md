# Source Note: CISA — Minimum Requirements for VEX（+ VEX 工具一致性反证）

- URL: https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf
- 标题: Minimum Requirements for Vulnerability Exploitability eXchange (VEX)
- 发布方: CISA（政府/标准一手；NTIA 工作组沿革）
- 日期: 2022-06 初版，2023-04 现行 PDF；抓取日期 2026-09-18
- 来源层级: 标准组织/政府文档
- 注：cisa.gov 着陆页 URL 已 404，PDF 直链经多篇论文引用确认（如 arXiv 2503.14388 参考文献 [1]）。

## 关键摘录 / 技术要点

- VEX 四个 status：`affected` / `not_affected` / `fixed` / `under_investigation`（NOT_AFFECTED 必须给 justification）。
- 五种机器可读 justification：`component_not_present`、`vulnerable_code_not_present`、`vulnerable_code_not_in_execute_path`、`vulnerable_code_cannot_be_controlled_by_adversary`、`inline_mitigations_already_exist`（Anchore 官方文档 docs.anchore.com 与 SPDX 3.0.1 spec §8.3.4 VexJustificationType 均有相同枚举，互为印证）。
- VEX statement 应含 metadata + status + vulnerability details + product details。

## 反证（重要）

- arXiv 2503.14388 "Vexed by VEX tools: Consistency evaluation of container vulnerability scanners"（2025-03，学术论文）：实证评估容器扫描器+VEX 工具链的**一致性**问题——同一漏洞在不同工具/流程下得到的 status 判定不一致，说明"机器生成 VEX"远没有标准化落地。
- 2022 年 Energy Central 评论指出 VEX 文档间自相矛盾、概念理解混乱（观点性来源）。

## 支撑报告结论

- 第二部分：VEX justification 枚举与"reachability 判定层级"存在天然映射（not_in_execute_path ↔ unreachable），是"机器证据自动生成 VEX"的标准基础；但工具一致性研究表明该自动化链路目前不可靠。
