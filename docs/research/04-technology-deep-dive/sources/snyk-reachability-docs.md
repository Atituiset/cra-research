# Source Note: Snyk — Reachability analysis（产品文档）

- URL: https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis
- 标题: Reachability analysis | Snyk User Docs
- 发布方: Snyk（厂商官方文档）
- 抓取日期: 2026-09-18（页面标注更新 2026-09-15）
- 来源层级: 官方文档（厂商）

## 关键摘录 / 技术要点

- 方法链：漏洞 enrichment（引用 maintainer fix commit）→ Related elements analysis（DeepCode AI program analysis）→ Root Cause analysis（DeepCode AI + NLP 排序 root cause 候选）→ Reachability analysis（应用 call graph × 依赖 call graph，找到到 root cause 元素的路径则判 Reachable）→ 安全专家人工监督校验。
- **不需要构建**即可扫描（"without requiring the application to be built"）——与 Endor full scan 需要构建形成路线差异。
- 明确讨论 FP/FN 权衡：采用"实时决策"在特定环境下选择 **under-approximate** 可达集；reflection 等场景无法给出精确答案；官方明确说 **"NO PATH FOUND ≠ 不可达/不可利用"**（no evidence of reachability ≠ unreachable）。
- 状态三值：`REACHABLE` / `NO PATH FOUND` / `NOT APPLICABLE`。
- 语言覆盖（GA）：Java（Maven/Gradle）、JavaScript/TypeScript（npm/Yarn/pnpm）、Python（pip/poetry/pipenv）；C#（NuGet/paket）Early Access。CLI/CI 集成 Early Access。
- 限制：≤300,000 文件、≤3GB、文件名 ≤256 字符。
- JSON 输出示例中含 EPSS（modelVersion v2025.03.14）、exploit maturity（PoC）、CVSS、fix commit reference——体现多信号组合。

## 支撑报告结论

- 第一部分：Snyk 官方承认静态 reachability 的根本局限（under-approximation、reflection、无证据≠不可达）——"unreachable" 结论不能作为强证据，是 VEX `not_affected` 自动化的关键约束。
- 第二部分：Snyk 的 pipeline（fix commit → root cause 排序 → 路径匹配）说明 reachability 依赖"漏洞到函数/元素"的 enrichment 数据，数据策展本身是壁垒的一部分。
- 语言覆盖现状的一手依据（GA 仅 3 个语言生态 + C# EA）。
