# Source Note: Endor Labs — Why Reachability Analysis for JavaScript Is Hard（厂商工程博客）

- URL: https://www.endorlabs.com/learn/why-reachability-analysis-for-javascript-is-hard-and-how-we-fixed-it
- 标题: Why Reachability Analysis for JavaScript Is Hard (and How We Fixed It)
- 发布方: Endor Labs 工程博客
- 日期: 2024-12-17；抓取日期 2026-09-18
- 来源层级: 厂商工程博客（一手技术叙述，但属营销属性内容，数据需谨慎）

## 关键摘录 / 技术要点

JavaScript call graph 困难的四个具体技术原因：

1. **依赖解析逻辑**：NodeJS 嵌套 node_modules，同一依赖可有多版本共存；确定"代码实际使用哪个版本"是精确 call graph 的前提；也是 phantom dependency 的来源。
2. **Module-level code 与 dynamic import**：JS 模块被 import 时顶层代码立即执行（无父函数），传统"函数调用"模型不覆盖；`require()` 的参数可以是运行时值，静态不可知。
3. **匿名函数**：无名字，漏洞映射只能用行号/offset，而版本间行号会漂移。
4. **函数指针/回调**：静态跟踪函数指针需要 data flow 分析，静态 call graph 相比动态 call graph 会丢边（missed edges）。

营销数据（标注为厂商自述）：某示例项目 124 个 findings → function-level reachability 过滤后 11 个（≈91% 减少）；再加 EPSS>1%、有 fix、生产环境 → 2 个。"reduce noise by up to 92%"。

## 支撑报告结论

- 第一部分：JS/TS 是 function-level reachability 最难的语言之一的工程证据（动态性、打包器、匿名函数、模块顶层副作用）。
- 结论部分：厂商自述的 "90%+ 噪声减少" 数字需谨慎对待——分母是"全部 findings"，且 unreachable 判定本身 unsound。
