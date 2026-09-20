# Source Note: Socket 行为分析技术（官方 FAQ + 社区首发帖）

- URL: https://docs.socket.dev/docs/faq ；https://news.ycombinator.com/item?id=30515090
- 标题: Socket FAQ / Show HN: Socket – Secure your JavaScript supply chain
- 发布方: Socket 官方文档；Hacker News（创始人自述）
- 发布日期: FAQ 页 2026-06-05 更新；HN 2022-03-01
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方 + 创始人一手陈述

## 关键事实点

- 技术路线（官方 FAQ）：**Package Behavior Analysis**——检测依赖更新引入的新风险 API 使用（network、shell、filesystem、环境变量读取、obfuscation、install scripts 等），不靠 CVE 目录。
- 创始人 HN 自述："Socket actually analyzes the package code to characterize the package's behavior"——静态分析包内容刻画行为画像，供应链攻击在入库/安装前拦截。
- 定价：第三方目录记录起步 $25/席/月、5 席起（softwr 2026 对比）。

## 支撑报告结论

- 组件检测层的第三条识别范式（manifest 解析、二进制指纹之外的）：**包行为静态刻画**，用于恶意包/零日供应链攻击；与 CVE 匹配互补而非替代。
