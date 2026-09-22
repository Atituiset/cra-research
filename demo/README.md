# 统一演示：读取真实证据的工作台

**GitHub 在线阅读：[图解阅读版](cra_workbench.md)**。包含九张图和全部文字输出，无需启动 Jupyter，也不依赖 Notebook 预览服务。需要执行代码时使用 [cra_workbench.ipynb](cra_workbench.ipynb)。

若 Notebook 页面一直加载并出现 `MathJax: Invalid option "autoload"`，可先通过阅读版查看同一份内容。仓库未配置该 MathJax 选项；当前尚未确认远端预览失败的根因。

在仓库根目录安装 `python3 -m pip install -e '.[demo]'`，然后运行 `python3 demo/build_notebook.py` 同时重建 Notebook、Markdown 阅读版和图表。它复用共享核心，使用临时数据库，不依赖 `demo/out/`，也不会保存个人目录到展示输出。生成后的 notebook 随仓库提交；HTML 工作台仍按下述方式本地生成。

演示结合 [架构讨论](../docs/chat-history.md)，主线调整为“评估引擎 → Localization → Evidence/Claim → 动态 Pass 调度 → 失效重估 → 消费端”。以 C 样例 CVE-2022-37434 展示组件/CVE 到符号的桥接，Go 图表与 CRA 报告时钟作为附录保留。

九张图的索引见 [figures/](figures/)。图中区分历史实测回放、设计投影和设计推演；VA-IR 示例没有写入核心 Store，预设的 Pass 步骤不是实际 Agent 轨迹。教学模型位于 [assessment_walkthrough.py](assessment_walkthrough.py)。

运行 `python3 demo/build_presentation.py` 后打开 `demo/out/index.html`。重建使用新目录：

```bash
python3 demo/build_presentation.py --out demo/out-next
```

本演示沿用第二份研究的产品→判定→修复证据→报告→交付叙事，数据与状态全部来自 `src/cra`。没有另外一套 fixture 判定逻辑。旧 notebook 与 HTML 位于 `docs/archive/cra-research-2/demo/`，其中的合成情报、KEV 触发文案和非标准 CDX 结构仅供历史参考。

## CLI 操作

以下 `<...>` 替换为 `cra snapshot` 输出中的对象 ID；时间和依据应填写真实事实。所有命令也可用 `PYTHONPATH=src python3 -m cra.cli` 调用。

```bash
cra import-pack poc/out/evidence-pack-go-vuln-app-0.1.0 --key poc/keys/dev-ed25519.pub.json
cra review <judgment-id> --decision approved --actor <operator> --reason '<分析范围、证据与判定依据>'
cra reassess <judgment-id> --reason '<新情报或构建变化>'
cra incident <release-id> --event-type actively_exploited_vulnerability --aware-at <带时区的知悉时间> --actor <operator> --basis '<适用性依据>' --corrective-at <措施可用时间>
cra incident <release-id> --event-type severe_incident --aware-at <带时区的知悉时间> --actor <operator> --basis '<严重事件依据>' --notification-at <正式通知时间>
cra record-report <incident-id> --stage early_warning --actor <operator> --receipt '<外部平台回执>' --submitted-at <实际提交时间>
cra verify-fix <old-judgment-id> <new-judgment-id> --actor <operator> --basis '<修复动作及新制品复扫证据解释>'
cra export demo/review-next
```

`verify-fix` 要求同产品同漏洞、不同制品，旧判定已批准为 affected，新判定已批准为 not_affected。它创建 verification 和新发布物的 fixed **候选**，仍需 review；旧发布物不变。没有新的真实复扫包就不应宣称修复成功。此版本由操作员复核修复依据，不具备自动修复或漏洞消失证明能力。

报告事件记录为草稿；`record-report` 只记录已在外部完成的报送，不进行提交或验证回执真实性。严重事件最终期限按提供的正式通知时间计算一个日历月；缺少期限起算事实时保留空值。重新补充事实需创建新的事件记录并在 basis 引用原记录，目前尚无事件修订命令。

页面是只读快照，CLI 修改后需重新导出。包内 `workbench.json` 是展示数据，`sources/` 是保留原字节的历史证据包文件，`manifest.json` 为交付文件 hash 索引。原始工具日志可能只留在历史引用中。
