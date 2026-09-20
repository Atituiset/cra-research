# Source Note: Black Duck snippet/signature 匹配机制（官方手册 + 学术分析）

- URL: https://sig-product-docs-be.synopsys.com/bundle/synopsys_detect_9.6.0/raw/resource/enus/synopsys_detect_9.6.0.pdf ；https://secureseco.org/wp-content/uploads/2022/08/OZP___Ashot_Grigorian-A-Competition-Analysis-of-Software-Assurance-Platforms-1-1.pdf
- 标题: Synopsys Detect 9.6.0 手册 / A Competition Analysis of Software Assurance Platforms (SecureSECO)
- 发布方: Synopsys/Black Duck 官方产品文档；SecureSECO（学术）
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档 + 学术二手分析

## 关键事实点

- Black Duck 检测三件套：**Signature Scanner**（目录/文件级签名哈希比对）+ **包管理器声明解析** + **snippet matching**（四种模式：NONE / SNIPPET_MATCHING / FULL_SNIPPET_MATCHING 等）。
- Snippet 机制（学术分析）：取文件**前 2MB**（可调 1–16MB），切分代码片段与知识库比对，**典型 5–7 行代码即可形成匹配**；先做整文件精确匹配，未命中的"自有代码"文件才进入 snippet 扫描。
- 流程顺序：component 扫描先行识别 OSS 组件，snippet 扫描兜底发现拷贝粘贴式复用（无 manifest 声明的部分复用）。

## 支撑报告结论

- 组件识别层的业界实际栈：文件/目录哈希签名 + 代码片段指纹是商用 SCA 发现"声明之外复用"的成熟手段，与 manifest 解析互补；snippet 匹配是 license 合规与隐蔽组件发现的底线能力。
