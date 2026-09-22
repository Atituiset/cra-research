# CRA 漏洞全生命周期 · Jupyter 演示

把 `report/` 的 **图 B 七阶段**（摄取→关联→判定→VEX→处置→报告→留证）跑通的可执行笔记本，用于周日评审/路演 demo。

## 打开方式

```bash
# ★ 投屏/评审推荐：单页 HTML 演示（←/→ 翻页，无需 Jupyter）
xdg-open demo/presentation.html          # WSL: wslview demo/presentation.html 或复制到 Windows 浏览器

# 交互式笔记本（代码已默认折叠，只看结论/表/图；点输入区可展开）
./demo/serve.sh

# 无头重建 + 执行（写回 outputs 与 out/ 产物）
.venv/bin/python demo/build_notebook.py
.venv/bin/python demo/build_presentation.py   # 重建 HTML（依赖 out/ 产物）
```

## 演示故事线（Acme IoT Gateway v3.2.1）

| # | 阶段 | 演示点 | 对应报告 |
|---|------|--------|----------|
| ① | 摄取 | 产品台账（支持期≥5 年）+ SBOM 质量分 | 03 §5, 04 J1 |
| ② | 关联 | 4 条告警五层 match-explain：多源一致 / 不可达铺垫 / **Debian backport 覆写** / 合成 CVE 待查 | 03 §2, 08 PoC-1 |
| ③ | 判定 | L2 call path 图（A1 可达 vs A2 不可达）+ 四轴证据卡 + 透明规则表 | 05, 08 PoC-2 |
| ④ | VEX | 状态机断言 + 强制证据 + 人审 + SLA 超时升级（A4 @30h） | 01 §6, 08 PoC-3 |
| ⑤ | 处置 | A1 升级 log4j 2.14→2.17 → 复扫 → `fixed`（验证回路不可跳） | 06 §1, 04 J4 |
| ⑥ | 报告 | **Art.14** 事件时钟：24h 草稿限期内 / 72h 预填 / final 占位 + SBOM 冻结 | 02 §3.1, 04 J3 |
| ⑦ | 留证 | Evidence Graph（25 节点）+ 3 个杀手查询 + 客户应答包 | 06 §4, 04 J5 |

## 产物（`demo/out/`）

- `reachability.png` / `evidence_graph.png` — 两张主图
- `vex_v3.2.1.cdx.json` — CycloneDX 风格 VEX（四状态+justification+证据引用）
- `incident_INC-2026-0922-001.json` — Art.14 三段报告草稿
- `sbom_v3.2.2.json` — 修复后 SBOM（diff 快照）
- `customer_response_pack.md` — J5 一键客户应答包
- `evidence_graph.json` — node-link 图数据（可回放）

## 数据声明

情报/KEV/EPSS/版本区间均为**演示夹具**（结构对齐真实源，数值简化）；
Log4Shell / 45046 / PwnKit 为真实历史 CVE，`CVE-2026-42424` 为**合成**（单元格内已标注）。
生产接入标准见 `report/05`、PoC 验收见 `report/08 §3`。
