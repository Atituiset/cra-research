# Source Note: govulncheck 官方文档（Go Packages）

- URL: https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck
- 标题: govulncheck command - golang.org/x/vuln/cmd/govulncheck
- 发布方: Go 团队 / golang.org（官方文档）
- 抓取日期: 2026-09-18
- 来源层级: 官方文档

## 关键摘录 / 技术要点

- govulncheck 对源码做静态分析（call graph / symbol 级）或对编译后二进制的符号表做分析，将漏洞报告收窄到"真正可能影响该应用"的范围。
- 源码模式可输出 call stack 摘要（如 `main.go: mypackage.main calls golang.org/x/text/language.Parse`），`'-show traces'` 输出完整调用栈。
- `-mode binary`：利用二进制符号信息查找 vulnerable function 的"提及"（mentions），二进制模式**不输出 call stack**。
- 支持 SARIF 输出与 **OpenVEX** 输出（符合 openvex/spec）。
- 明确列出的 Limitations（原文）：
  - 函数指针与 interface 调用采用保守分析，可能产生 false positive 或不准确的 call stack；
  - 通过 `reflect` 包的调用对静态分析不可见 → 源码模式下可能漏报；`unsafe` 包可能产生 false negative；
  - Go 二进制不含详细调用信息，无法给出 call graph，且可能对"在二进制中但不可达"的代码误报；
  - Go 1.18 之前的二进制只报标准库漏洞；符号信息无法提取时退化为按模块报告全部依赖漏洞。

## 支撑报告结论

- 第一部分：Go 是 function/symbol-level reachability 工程可行性最强的语言（官方工具、开源、免费），是"reachability 非独有壁垒"的强证据。
- 语言差异：即便 Go（反射少、静态编译）也存在 reflect/unsafe 漏报与二进制无 call stack 的限制。
- VEX 自动化先例：govulncheck 可直接输出 OpenVEX，说明"机器证据 → VEX status"已有官方实现先例。
