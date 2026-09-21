# Source Note: Endor Labs Upgrade Impact Analysis + 优先级漏斗（官方文档）

- URL（一组，均官方文档）:
  - https://docs.endorlabs.com/risk-remediation/upgrade-impact-analysis
  - https://docs.endorlabs.com/inventory-insights/dashboards/oss-overview （Vulnerability prioritization funnel）
- 发布方： Endor Labs（官方文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## Upgrade Impact Analysis 关键事实点

1. **评估输入四要素**（原文）：当前版本及其传递依赖的漏洞；新版本已修复的漏洞；"Heuristic factors that influence the probability of breaking changes"；"**Program analysis to directly identify breaking changes**"。
2. **输出四档升级选项**：latest version / latest vulnerability-free version / most impactful update with moderate evidence of breaking changes / most impactful update with low evidence of breaking changes。
3. **Remediation risk 三档**：High（高置信会 break）/ Medium（识别到潜在 breaking change 但置信度低-中，或存在 major version 冲突）/ Low（无证据，但**明示 "The absence of evidence does NOT guarantee that it will not break your application"**）。
4. **Breaking change 六类枚举**：API changes（重命名/删除函数、签名变更、参数变化）；Behavioral changes（接口不变但行为变）；Dependency updates（传递依赖引入 breaking change）；Deprecations and removals；Configuration changes；Supported platforms 变化（如弃旧版 Go）。
5. **Dependency conflicts**：分析依赖图中 major/minor 版本冲突，作为风险驱动因素之一；UI 有 "Potential Conflicts" 与 "Breaking Changes" 两个独立面板，并给出 "Remediation Risk Drivers" 与 "breaking change confidence"。
6. **License 门槛**："Upgrade impact analysis is available with the **Endor Open Source Pro** license."
7. 与 reachability 联动：Remediation 列表可按 "Show Only Reachable" 过滤——修复优先级建立在可达性之上。

## 实现原理推断素材

8. 2022 技术博客（见 endor-callgraph-engine.md）给出方向性证据：Impact = call graph 上的**后向遍历**（"if I change this function, which parts of the codebase will be impacted"）。结合 per-package-version call graph 存储架构，breaking change 识别很可能建立在**相邻版本的函数级 API diff × 本项目实际调用面**之上（即只报告"你实际调用的函数"的签名/行为变化）——此为**推断（Hypothesis）**，官方文档未写明 diff 的具体程序分析技术。

## 优先级漏斗（OSS overview 页，维度 6 证据）

9. **Vulnerability prioritization funnel 固定五级**：Total open → **Not in test**（排除测试代码）→ **Fix available** → **Reachable**（可自定义 Reachable Function / Potentially Reachable Function）→ **Exploitable likelihood（EPSS > 1%）**。
10. 漏斗挂接 "Low Risk Upgrades"（需 OSS Pro）——优先级结论直接通向低风险升级建议。
11. 附 "Dev Hours Saved / Cost Saved" 可自定义基线的 ROI 计算器。
12. EPSS 过滤器亦见于 release notes（archive："EPSS probability filter on the Findings page"）。**KEV（CISA Known Exploited Vulnerabilities）在官方文档中未见明确集成证据（不确定）**。

## 支撑报告结论

- 维度 5：Upgrade Impact Analysis 是"启发式 + 程序分析"双层，输出**带置信度的风险分级 + 逐条 breaking change 证据**（Risk Drivers），且官方明示 Low ≠ 保证——是目前唯一把"升级会不会 break"产品化为带证据链对象的厂商实现。
- 维度 6：exploitability/context 信号 = 测试代码排除 + fix availability + reachability + EPSS 阈值，全部来自自有扫描与公开 EPSS；无 KEV 证据。
