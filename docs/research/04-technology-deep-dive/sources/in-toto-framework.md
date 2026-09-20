# Source Note: in-toto — 供应链完整性框架（CNCF 毕业项目）

- URL: https://in-toto.io （规范见 https://github.com/in-toto/spec；attestation 框架 https://github.com/in-toto/attestation）
- 标题: in-toto — A framework to secure the integrity of software supply chains
- 发布方: in-toto 项目 / CNCF（graduated project）
- 抓取日期: 2026-09-18
- 来源层级: 标准/开源项目（一手）

## 关键摘录 / 技术要点

- 目标：保证软件产品从初始到最终用户安装的完整性——"making it transparent to the user **what steps were performed, by whom and in what order**"。
- 核心机制：每个供应链步骤产生 **attestation**（签名元数据，记录输入输出 hash、执行者、命令），下一阶段验证上一阶段的 attestation；layout 定义预期流程与责任人。
- CNCF graduated project（2024 年毕业，二手来源 youngju.dev 长文提及 in-toto 2022 incubating / 2024 graduated）。
- SLSA provenance 以 in-toto attestation 为载体（slsa.dev）。

## 支撑报告结论

- 第四部分：Evidence Graph 的先例——in-toto 证明"每一步骤的签名证据链 + 可验证"在供应链安全中已是成熟范式；Evidence Graph = 把同样的 attestation 思想从"构建过程"扩展到"安全结论"（Conclusion→Evidence→Tool→Artifact→Timestamp）。
- GUAC 直接消费 in-toto ITE6 attestation，说明两者可组合成证据底座。
