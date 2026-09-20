# Source Note: Finite State 二进制分析定位（官方博客）

- URL: https://finitestate.io/blog/source-code-vs-binary-analysis-software-security
- 标题: Binary Analysis vs Source Code Analysis: Why Software Supply Chain Security Needs Both
- 发布方: Finite State 官方博客
- 发布日期: 2026-03-15
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方

## 关键事实点

- 二进制分析对象 = 编译后的机器码/固件，无需源码：自动解包固件镜像、生成 SBOM、识别第三方组件与后门风险（与 Safeguard 2026 买家指南对其描述一致："automatically unpacking firmware images, generating SBOMs"）。
- 学术侧同构技术栈（mdu.se 论文，Finite State 研究背景作者）：固件提取 → 文件树遍历 → 可执行文件预处理/归一化 → 与大规模**已映射组件库**比对（文件路径、文件名、特征哈希）→ 数字模型。
- 学术综述（MDPI Electronics 2026-08）确认该领域的通用方法：静态分析直接检查二进制结构/数据流；二进制相似性检测（VoteSim/BinaryAI/jTrans 等）用于无符号组件识别——**二进制指纹/相似度匹配是该物种的核心识别技术**。

## 支撑报告结论

- 二进制/固件分析型的技术栈：解包器 + 组件特征库 + 相似度匹配（ML 辅助），与源码侧 manifest 解析完全不同的识别范式；组件库的覆盖度是壁垒。
