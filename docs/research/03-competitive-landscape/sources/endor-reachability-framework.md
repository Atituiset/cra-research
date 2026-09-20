# Source Note: Endor Labs《What Is Reachability Analysis》（官方 learn 页）

- URL: https://www.endorlabs.com/learn/reachability-analysis
- 标题: What Is Reachability Analysis and Why Does It Matter?
- 发布方: Endor Labs 官方（learn/营销教育内容）
- 发布/更新: 2026-07-31（检索快照）
- 抓取日期: 2026-09-18
- 来源层级: 厂商营销材料（含技术分类框架，可用于能力定义；降噪数字为厂商声称）

## 关键事实点

- Reachability 分类框架：3 种方法（static/dynamic/runtime）× 5 种类型（function-level / dependency-level / package baselining / package-usage-in-containers / internet reachability）。
- Function-level reachability 依赖"CVE→受影响函数（跨版本）"映射数据库，Endor 通过程序分析自建（厂商声称）。
- Endor 自述能力：跨一方代码、开源依赖、容器镜像的统一 code context graph；function-level reachability 附**可检查、可复现的 call chain 证据**；客户报告降噪 80–99%（厂商声称）。
- 行业批评点（厂商视角，但可借鉴为评估框架）：多数厂商看不到传递依赖之外；不完整 call graph（反射/动态调用）；只到代码层不分析容器；二元判定无可利用性上下文；复杂构建系统（Bazel）/C++ 直接报"干净结果"而不承认盲区。
- 核心判断（厂商声称但与市场观察一致）："Reachability 已从差异化变成 table stakes，新差异化是证据质量 + 覆盖广度 + 修复能力"。
- Upgrade Impact Analysis + Endor Patches（从 F6S/官网交叉确认）：reachability 是 Endor"agentic remediation 模型"的地基。

## 支撑报告结论

- 直接支撑 A 分析：reachability 商品化光谱分层（dependency 级已商品化；function 级+证据+容器/OS 层未商品化）。
- "A reachability claim you cannot verify is a claim you cannot trust" → 支撑 evidence graph 创新空间论点。
