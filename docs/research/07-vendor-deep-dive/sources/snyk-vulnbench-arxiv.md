# Source Note: Snyk VulnBench JS 1.0（arXiv 论文，自曝 LLM 检测不可重复性）

- URL: https://arxiv.org/abs/2606.15762 （HTML: https://arxiv.org/html/2606.15762v1 ）；数据集公开于 https://vulnbench.com/
- 标题: Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice?
- 发布方: Snyk（arXiv 提交人 Liran Tal）
- 发布日期: 2026-06-14
- 抓取日期: 2026-09-21
- 来源层级: 厂商自研公开学术 preprint（一手；自我批判性质，可信度高）

## 关键事实点（摘要+正文摘录）

1. **方法**：300 次重复漏洞发现扫描，同一份 JavaScript 代码、同一 prompt、同一 harness（Claude Code），测 agentic LLM 安全 review 的可重复性。
2. **核心发现**：
   - 250 次模型运行中，161 个 unique unmatched findings 里 **80 个只在 5 次重复中出现 1 次**，仅 22 个 5 次全出现；
   - 与 Snyk Code 参考集匹配的 findings 稳定得多：**134/158 个 5 次全出现**；
   - 互补性：模型稳定检出常见高信号 exploit 形态，且有一例暴露了疑似 **Snyk Code 产品盲区**（自曝）；
   - Snyk Code（确定性 SAST）在系统性枚举重复 data-flow sink 上更好且确定性。
3. **作者自注的循环性风险**（正文，诚实声明）："The reference set comes from Snyk Code. That is transparent and reproducible, but **circular if treated as a universal truth set**. This report avoids that claim." scorer 按漏洞类型宽松匹配，更严的 scorer 会拉低一致率。
4. **结论导向**：agentic LLM review 与确定性 SAST 应**组合**而非互相替代——这是 Snyk "generator ≠ validator" 平台叙事的学术地基。

## 对本轮深挖的支撑

- 维度 3/4：Agent Fix 与 Evo 的"独立确定性验证层"叙事有一篇公开 preprint 背书（而非纯营销）。
- 维度 10：厂商自己量化披露了 LLM 安全检测的不可重复性（~50% findings 不重现），并承认 benchmark 参考集的循环性。
