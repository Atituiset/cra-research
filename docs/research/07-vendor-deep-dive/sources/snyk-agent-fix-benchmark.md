# Source Note: Snyk Agent Fix Golden Test 基准（官方工程博客，英文版全文要点）

- URL: https://snyk.io/blog/snyk-agent-fix-remediation-benchmark/
- 标题: Snyk Agent Fix remediation benchmark（Golden Test）
- 发布方: Snyk 官方工程博客
- 发布日期: 2026-08-18
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方（自述基准，含完整 Limitations 自曝）

## 关键事实点

1. **Snyk Intelligence 定义**（原文）："dynamic few-shot prompting: at a fix time, we inject the most relevant expert-written fixes for that specific weakness, drawn from Snyk's database of **more than 35,000 vulnerabilities**"。生产环境 Agent Fix = Snyk Intelligence + **Claude Opus 4.7**（基准数据采集时用的是 Opus 4.6）。
2. **基准设计**：~150 个真实漏洞样本（Python 50 / JS 54 / Java 39），每个样本带两个人工验证的单测（安全测试：漏洞存在时 fail；功能测试：原功能保持时 pass）；模型须**首试**同时通过两测、且**看不到测试**。设计自称受 SWE-bench 启发，安全侧先例是 Vul4J（FAIL-to-PASS + PASS-to-PASS）。
3. **结果表**（secure AND functional 修复率）：
   - StarCoder（上一代内部模型）72.4%（注：仅 Agent-Fix 支持的规则子集；**全规则集只有 54.9%**——自曝）；
   - Gemini 3.1 Pro 74.2%；Sonnet 4.6 72.4%；Opus 4.6 74.6%；
   - Sonnet 4.6 + Snyk Intelligence **82.5%**；Opus 4.6 + Snyk Intelligence **85.4%**（+10.8 pt / +14.48% 样本）；
   - Python 提升最大：Opus 64.0% → 88.0%。
4. **结论口径（原文）**："out-of-the-box models have plateaued around 72–75%"；"The durable asset is the 35,000-plus expert fixes; **the model is a component we can swap**"。
5. **Limitations 自曝四条**：样本量 ~150 不足以支持小差距的统计显著性；snippet 级而非整应用（无跨文件上下文）；只测三语言；方差只跑两轮（sub-2-point 差异视为近似）。
6. **合并率/回归率**：本篇未给生产环境 merge rate / regression rate（94% 合并率声明在 2026-09-17 新闻稿，见 snyk-evo-production-metrics.md）。全行业仍无绝对合并率/回归率公开数据。
7. **验证机制**（结合 04 报告已录）：所有 auto-fix 先过 Snyk Code SAST re-scan（可读、解决原问题、不引入新漏洞）再推给开发者。

## 对本轮深挖的支撑

- 维度 3：SAST pre-screening + dynamic few-shot + 双目标（secure & functional）验证的具体分工与数字；"模型可换、35k 专家修复库是资产"是其架构核心声明。
