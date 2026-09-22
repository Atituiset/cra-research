# 开发与运行指南

[返回项目首页](../README.md) · [实施设计](design/unified-workbench.md) · [CLI 演示操作](../demo/README.md)

## 安装与运行

环境：Python 3.11+，依赖 `cryptography`。克隆仓库后进入仓库根目录，以下命令均相对此目录执行，不依赖原作者的个人目录或第二个独立仓库。

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
python3 demo/build_presentation.py
```

打开 `demo/out/index.html`。生成器读取已有 Go/C 证据包并重新验签，不需要重新运行 Go、Docker、Joern，也不会联网同步漏洞。重新运行底层扫描的前置条件见 [PoC 说明](../poc/README.md)。

默认数据库为 `var/cra.db`。导出目录必须尚不存在，重建可使用：

```bash
python3 demo/build_presentation.py --out demo/out-next
```

## 更新 GitHub 演示

```bash
python3 -m pip install -e '.[demo]'
python3 demo/build_notebook.py
```

绘图使用 Matplotlib，notebook 格式通过 nbformat 校验。重建中文图表需安装 Noto Sans CJK、微软雅黑或其他支持的中文字体；GitHub 阅读内嵌图片不需要字体或 Python 环境。九张 PNG 同时保存到 `demo/figures/`，可单独用于讨论材料。设计推演只运行教学脚本，既不调用 Agent，也不改变现有工作台记录。

生成的 `demo/cra_workbench.ipynb` 已包含执行输出，应与代码一起提交。生成器使用临时数据库，不改变工作台中的审批记录。

GitHub notebook 预览显示已保存的静态内容，不执行 Python 或交互式 JavaScript，见 [官方说明](https://docs.github.com/zh/repositories/working-with-files/using-files/working-with-non-code-files)。`demo/out/` 是本地生成目录，不随 Git 提交；HTML 需在本地浏览器打开。

## CLI 与验证

```bash
cra snapshot
cra review <judgment-id> --decision approved --actor <reviewer> --reason '<复核依据>'
cra reassess <judgment-id> --reason '<情报或构建变化依据>'
cra export demo/review-next
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

无需安装 CLI 时，可以用 `PYTHONPATH=src python3 -m cra.cli` 调用。事件和修复命令见 [演示说明](../demo/README.md)。

`review` 是本地操作员记录；actor 名称不代表经过身份认证。首次导入的历史结论需复核，有效状态先保持 `under_investigation`。当前 SQLite、静态页面和开发密钥用于本地原型。

## 历史证据与可移植性

`poc/out/` 中的历史签名载荷、hash 索引覆盖的文件及原始工具结果可能包含生成时的绝对路径。它们是溯源元数据，不是团队成员需要访问的路径。直接替换会破坏原始 hash 或签名，因此保留原字节；通过包内文件或工作台证据索引查阅即可。

部分原始工具日志仅保留引用，尚未完整打包。当前审批结果也未重新签发为标准 VEX。新导入的包来源只记录目录名；本地数据库和 HTML 输出由 `.gitignore` 排除。
