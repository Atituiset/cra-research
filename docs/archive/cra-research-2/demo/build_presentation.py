"""生成单页 HTML 演示（投屏用）：demo/presentation.html

用法: .venv/bin/python demo/build_presentation.py
依赖: demo/out/ 下已执行产物（先跑 build_notebook.py）
"""
from __future__ import annotations

import base64
import json
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
DEST = HERE / "presentation.html"


def b64img(name: str) -> str:
    return base64.b64encode((OUT / name).read_bytes()).decode()


def load(name: str):
    return json.loads((OUT / name).read_text(encoding="utf-8"))


vex = load("vex_v3.2.1.cdx.json")
inc = load("incident_INC-2026-0922-001.json")
pack = (OUT / "customer_response_pack.md").read_text(encoding="utf-8")

reach_img = b64img("reachability.png")
graph_img = b64img("evidence_graph.png")

status_zh = {
    "affected": ("受影响", "#dc2626"),
    "not_affected": ("不受影响", "#16a34a"),
    "fixed": ("已修复", "#2563eb"),
    "under_investigation": ("调查中", "#ca8a04"),
}

vex_rows = "\n".join(
    f"<tr><td class='mono'>{a['cve']}</td>"
    f"<td><span class='pill' style='background:{status_zh[a['status']][1]}'>{status_zh[a['status']][0]}</span></td>"
    f"<td class='small'>{a['justification'] or '—'}</td>"
    f"<td class='mono small'>{a['refs'][0]['id']}</td></tr>"
    for a in vex["analysis"]
)

ew = inc["reports"]["24h_early_warning"]
dl = inc["deadlines"]

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CRA 漏洞全生命周期 · 全流程演示</title>
<style>
:root {{
  --ink:#0f172a; --muted:#64748b; --line:#e2e8f0; --bg:#f8fafc;
  --blue:#2563eb; --red:#dc2626; --green:#16a34a; --amber:#d97706;
  --card:#ffffff;
}}
* {{ box-sizing:border-box; margin:0; }}
html {{ scroll-snap-type:y mandatory; scroll-behavior:smooth; }}
body {{
  font-family:"Noto Sans CJK SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  color:var(--ink); background:var(--bg); line-height:1.6;
}}
section.slide {{
  min-height:100vh; scroll-snap-align:start;
  padding:7vh 7vw; display:flex; flex-direction:column; justify-content:center;
  border-bottom:1px solid var(--line); position:relative;
}}
.kicker {{ font-size:.85rem; letter-spacing:.2em; color:var(--blue); font-weight:700; text-transform:uppercase; margin-bottom:.75rem; }}
h1 {{ font-size:clamp(2rem,4.5vw,3.2rem); font-weight:800; letter-spacing:-.02em; }}
h2 {{ font-size:clamp(1.5rem,3vw,2.2rem); font-weight:800; margin-bottom:1rem; }}
h3 {{ font-size:1.1rem; font-weight:700; margin:.75rem 0 .4rem; }}
p.lead {{ font-size:1.15rem; color:#334155; max-width:52rem; }}
.stage {{ position:absolute; right:5vw; top:5vh; font-size:6rem; font-weight:800; color:#e2e8f0; z-index:0; user-select:none; }}
.slide > * {{ position:relative; z-index:1; }}
.conclusion {{
  background:#eff6ff; border-left:5px solid var(--blue);
  padding:1rem 1.4rem; font-size:1.2rem; font-weight:600;
  border-radius:0 12px 12px 0; margin:1.5rem 0; max-width:56rem;
}}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:1rem; margin:1.5rem 0; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:1.2rem 1.3rem; box-shadow:0 1px 3px rgb(15 23 42/6%); }}
.card .num {{ font-size:1.9rem; font-weight:800; color:var(--blue); }}
.card .num.red {{ color:var(--red); }}
.card .num.green {{ color:var(--green); }}
.card .lbl {{ font-size:.9rem; color:var(--muted); }}
img.fig {{ max-width:100%; max-height:62vh; border:1px solid var(--line); border-radius:14px; background:#fff; box-shadow:0 8px 30px rgb(15 23 42/8%); object-fit:contain; }}
table {{ width:100%; border-collapse:collapse; background:#fff; border-radius:12px; overflow:hidden; font-size:.95rem; }}
th {{ background:#f1f5f9; text-align:left; padding:.65rem .8rem; font-size:.85rem; color:#475569; }}
td {{ padding:.6rem .8rem; border-top:1px solid var(--line); vertical-align:top; }}
.mono {{ font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.85em; }}
.small {{ font-size:.85rem; color:#475569; }}
.pill {{ display:inline-block; color:#fff; font-size:.78rem; font-weight:700; padding:.15rem .55rem; border-radius:999px; }}
ol.story {{ padding-left:1.2rem; max-width:52rem; }}
ol.story li {{ margin:.55rem 0; font-size:1.05rem; }}
ul.plain {{ list-style:none; padding:0; max-width:52rem; }}
ul.plain li {{ margin:.5rem 0; padding-left:1.4rem; position:relative; }}
ul.plain li::before {{ content:"▸"; position:absolute; left:0; color:var(--blue); font-weight:700; }}
.timeline {{ display:flex; gap:0; margin:1.5rem 0; flex-wrap:wrap; }}
.tstep {{ flex:1; min-width:160px; background:#fff; border:1px solid var(--line); padding:1rem; position:relative; }}
.tstep:first-child {{ border-radius:12px 0 0 12px; }}
.tstep:last-child {{ border-radius:0 12px 12px 0; }}
.tstep.ok {{ border-top:4px solid var(--green); }}
.tstep.pending {{ border-top:4px solid var(--amber); }}
.tstep .when {{ font-weight:800; color:var(--blue); font-size:1.05rem; }}
.tstep .what {{ font-size:.9rem; color:#334155; margin-top:.3rem; }}
pre.pack {{ background:#0f172a; color:#e2e8f0; padding:1.2rem 1.4rem; border-radius:14px; font-size:.82rem; overflow:auto; max-height:46vh; line-height:1.55; }}
nav.dots {{ position:fixed; right:1.1rem; top:50%; transform:translateY(-50%); display:flex; flex-direction:column; gap:.55rem; z-index:50; }}
nav.dots a {{ width:10px; height:10px; border-radius:50%; background:#cbd5e1; display:block; transition:.2s; }}
nav.dots a.on {{ background:var(--blue); transform:scale(1.35); }}
.hint {{ position:fixed; left:1.2rem; bottom:1rem; font-size:.78rem; color:var(--muted); z-index:50; background:rgb(255 255 255/85%); padding:.3rem .7rem; border-radius:8px; border:1px solid var(--line); }}
.two {{ display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; align-items:start; }}
@media (max-width:900px) {{ .two {{ grid-template-columns:1fr; }} .stage {{ font-size:3.5rem; }} }}
.fadein {{ animation:fade .5s ease; }}
@keyframes fade {{ from {{ opacity:0; transform:translateY(10px);}} to {{ opacity:1; transform:none;}} }}
</style>
</head>
<body>

<section class="slide" id="s0" style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 60%,#1d4ed8 100%); color:#fff; border:none;">
  <div class="kicker" style="color:#93c5fd;">DEEP RESEARCH → 可执行演示</div>
  <h1 style="color:#fff;">CRA 漏洞全生命周期<br>基本全流程展示</h1>
  <p class="lead" style="color:#cbd5e1; margin-top:1rem;">
    一个真实 CVE，从发现到 24 小时法定报告、到修复验证、到客户 2 分钟应答——
    七阶段跑通，每步留下 10 年可回放的证据。
  </p>
  <div class="cards" style="max-width:48rem;">
    <div class="card" style="background:rgb(255 255 255/10%); border-color:rgb(255 255 255/20%);">
      <div class="num" style="color:#93c5fd;">Art.14</div>
      <div class="lbl" style="color:#cbd5e1;">事件报告义务 · 2026-09-11 已生效</div>
    </div>
    <div class="card" style="background:rgb(255 255 255/10%); border-color:rgb(255 255 255/20%);">
      <div class="num" style="color:#93c5fd;">€15M / 2.5%</div>
      <div class="lbl" style="color:#cbd5e1;">违规罚款上限（取高者）</div>
    </div>
    <div class="card" style="background:rgb(255 255 255/10%); border-color:rgb(255 255 255/20%);">
      <div class="num" style="color:#93c5fd;">2027-12-11</div>
      <div class="lbl" style="color:#cbd5e1;">CRA 主义务全面适用</div>
    </div>
  </div>
  <p class="small" style="color:#94a3b8; margin-top:1.5rem;">演示产品：Acme IoT Gateway v3.2.1（虚构）· 数据为夹具，结构对齐真实源 · ←/→ 或右侧圆点翻页</p>
</section>

<section class="slide" id="s1">
  <div class="stage">Why</div>
  <div class="kicker">为什么不是"再买一个扫描器"</div>
  <h2>传统 SCA 给你更长的清单；CRA 要你给<strong>可采信的答案</strong></h2>
  <div class="conclusion">
    漏报的代价（罚款 + 法定报告失守）第一次压过误报的代价（修复疲劳）——
    客户愿意为"每个结论都带证据"付钱。
  </div>
  <div class="two">
    <div>
      <h3>五层不确定性 = 噪声的来源</h3>
      <ul class="plain">
        <li><strong>数据地基</strong>：NVD 2026-04 起 risk-based 收缩，单一依赖失效</li>
        <li><strong>版本区间</strong>：多源打架，谁对？</li>
        <li><strong>Backport</strong>：版本号没变但其实已修（PwnKit 演示）</li>
        <li><strong>别名消解</strong>：同一漏洞多个 ID</li>
        <li><strong>只报"存在"不判"击中"</strong>：可达吗？能打进来吗？</li>
      </ul>
    </div>
    <div>
      <h3>我们卖给什么</h3>
      <div class="cards" style="grid-template-columns:1fr;">
        <div class="card"><div class="num">判定</div><div class="lbl">VEX 四状态 × 理由 × 人审</div></div>
        <div class="card"><div class="num">报告</div><div class="lbl">24h / 72h / 14d 法定时钟</div></div>
        <div class="card"><div class="num">证据</div><div class="lbl">快照内容寻址 · 10 年回放</div></div>
      </div>
    </div>
  </div>
</section>

<section class="slide" id="s2">
  <div class="stage">①②</div>
  <div class="kicker">阶段 ① 摄取 · ② 关联</div>
  <h2>先把产品档案立起来，再让多源情报对质</h2>
  <div class="conclusion">
    CRA 要的不是扫描表，是产品档案（支持期 + SBOM）；多源打架时不静默选一个——五层证据摊开，假阳性当场拦下。
  </div>
  <div class="cards">
    <div class="card"><div class="num">v3.2.1</div><div class="lbl">产品版本 · 支持至 2031-06-30（≥5 年）</div></div>
    <div class="card"><div class="num">100/100</div><div class="lbl">SBOM 质量分 · 快照 snap-f07fc15cbc73</div></div>
    <div class="card"><div class="num">4 → 4</div><div class="lbl">4 条多源情报 → 4 条五层透明告警</div></div>
    <div class="card"><div class="num green">1 拦截</div><div class="lbl">PwnKit：NVD 命中但 Debian backport 已修</div></div>
  </div>
  <table>
    <tr><th>告警</th><th>CVE</th><th>故事</th><th>关联结果</th></tr>
    <tr><td>A1</td><td class="mono">CVE-2021-44228</td><td>Log4Shell · 三源区间一致 + KEV</td><td><span class="pill" style="background:#dc2626">命中 → 深判</span></td></tr>
    <tr><td>A2</td><td class="mono">CVE-2021-45046</td><td>同组件另一缺陷</td><td><span class="pill" style="background:#dc2626">命中 → 深判</span></td></tr>
    <tr><td>A3</td><td class="mono">CVE-2021-4034</td><td>PwnKit · NVD 命中，发行版已 backport</td><td><span class="pill" style="background:#16a34a">distro 覆写 · 拦截</span></td></tr>
    <tr><td>A4</td><td class="mono">CVE-2026-42424</td><td>昨夜新报（合成演示）· 未分析</td><td><span class="pill" style="background:#ca8a04">调查中 + SLA</span></td></tr>
  </table>
</section>

<section class="slide" id="s3">
  <div class="stage">③</div>
  <div class="kicker">阶段 ③ 判定 · Reachability</div>
  <h2>问的不是"有没有 CVE"，是"能不能被打进来"</h2>
  <div class="conclusion">
    一条画出来的调用路径 = 给审计师的 <span class="mono">vulnerable_code_not_in_execute_path</span> 证据。
  </div>
  <div class="two">
    <div>
      <img class="fig" src="data:image/png;base64,{reach_img}" alt="Reachability 双图">
    </div>
    <div>
      <h3>A1 · Log4Shell → 可达</h3>
      <p class="small">绿色入口 <span class="mono">/api/ingest</span> 沿橙色路径直抵红色漏洞函数——外部攻击面真实存在。</p>
      <h3>A2 · 同组件 → 不可达</h3>
      <p class="small">漏洞函数只挂在灰色 JMX 本地管理面；两个绿色外部入口<strong>无任何路径</strong>到达它。</p>
      <h3>A3/A4</h3>
      <p class="small">A3 发行版级 backport（无 call graph，用 tracker 证据）；A4 等分析 → 调查中。</p>
      <p class="small" style="color:var(--amber);">演示验收对标 report/05 §7：真不可达 ≥9/10、路径可视化 100%。</p>
    </div>
  </div>
</section>

<section class="slide" id="s4">
  <div class="stage">④</div>
  <div class="kicker">阶段 ④ VEX 判定工作流</div>
  <h2>每个判定必须带<strong>理由 + 证据快照</strong>；人签字；超时升级</h2>
  <div class="conclusion">
    VEX 不是导出格式，是工作流——AI 只能建议，人来落库；<span class="mono">under_investigation</span> 超 24h 自动升级（A4 在 T0+30h 被抓到）。
  </div>
  <table>
    <tr><th>CVE</th><th>状态</th><th>Justification（受控词表）</th><th>证据快照</th></tr>
    {vex_rows}
  </table>
  <div class="cards">
    <div class="card"><div class="num">4/4</div><div class="lbl">状态断言 + 词表校验通过</div></div>
    <div class="card"><div class="num red">SLA</div><div class="lbl">A4 调查 30h &gt; 24h → 升级产品安全负责人</div></div>
    <div class="card"><div class="num green">人审</div><div class="lbl">zhang.wei@acme 签字 · 快照含 who/when/what</div></div>
  </div>
</section>

<section class="slide" id="s5">
  <div class="stage">⑤⑥</div>
  <div class="kicker">阶段 ⑤ 处置验证 · ⑥ 事件报告</div>
  <h2>标 <span class="mono">fixed</span> 前必须复扫；KEV 命中启动 24h 法定时钟</h2>
  <div class="conclusion">
    "上游修了" ≠ "我的产品修了"；{ew["hours_left"]:.0f} 小时内交出 24h 预警草稿（提前 18 小时），字段预填、SBOM 已冻结。
  </div>
  <div class="two">
    <div>
      <h3>⑤ 修复闭环（A1）</h3>
      <ol class="story">
        <li>log4j-core <span class="mono">2.14.0 → 2.17.1</span> · PR <span class="mono">acme/gateway#4721</span></li>
        <li>复扫：2.17.1 不再落入 <span class="mono">&lt;2.15.0</span> → <strong>不再命中 ✓</strong></li>
        <li>验证通过才允许 <span class="mono">affected → fixed</span>（快照 <span class="mono">snap-4cb376a69180</span>）</li>
        <li>A2/A3 无需升级（已 not_affected）· A4 挂缓解 + 继续调查</li>
      </ol>
      <h3>⑥ 事件触发</h3>
      <p class="small">A1 = KEV ∩ 产品命中 ∩ actively exploited → Incident <span class="mono">{inc["incident_id"]}</span></p>
    </div>
    <div>
      <h3>Art.14 报告时钟</h3>
      <div class="timeline">
        <div class="tstep ok"><div class="when">T0</div><div class="what">发现 + 冻结 SBOM<br><span class="mono small">snap-f07fc15cbc73</span></div></div>
        <div class="tstep ok"><div class="when">+6h / 限 24h</div><div class="what">早期预警草稿完成<br><strong>提前 18 小时</strong></div></div>
        <div class="tstep pending"><div class="when">+72h</div><div class="what">正式通知 · 字段已预填<br>受影响产品清单就绪</div></div>
        <div class="tstep pending"><div class="when">措施后 ≤14d</div><div class="what">final 报告模板<br>复扫证据挂接</div></div>
      </div>
      <p class="small">去向：ENISA 单一报告平台（SRP）· 字段结构按报告 02 §3.1，真接口=下轮研究任务。</p>
    </div>
  </div>
</section>

<section class="slide" id="s6">
  <div class="stage">⑦</div>
  <div class="kicker">阶段 ⑦ Evidence Graph</div>
  <h2>全程沉淀 <strong>10 年可回放</strong> 的证据图</h2>
  <div class="conclusion">
    内容寻址快照（sid）：相同输入必得相同 ID——监管问"当时为什么这么判"，点开链条即可回放。
  </div>
  <img class="fig" src="data:image/png;base64,{graph_img}" alt="Evidence Graph" style="max-height:58vh; margin:0 auto;">
  <div class="cards" style="margin-top:1rem;">
    <div class="card"><div class="num">25 → …</div><div class="lbl">台账·组件·漏洞·判定·修复·事件·报告 全部入图</div></div>
    <div class="card"><div class="num">3 查询</div><div class="lbl">证据链回放 · 报告完备度 · 客户应答包</div></div>
    <div class="card"><div class="num green">2 分钟</div><div class="lbl">客户交货材料：SBOM+VEX+事件状态一键装配</div></div>
  </div>
</section>

<section class="slide" id="s7">
  <div class="stage">J5</div>
  <div class="kicker">产出 · 客户应答包（最终交付形态）</div>
  <h2>过去 2 天手工拼表 → 现在 2 分钟、可点验</h2>
  <div class="two">
    <div>
      <pre class="pack">{pack}</pre>
    </div>
    <div>
      <h3>同时落盘的还有</h3>
      <ul class="plain">
        <li><span class="mono">vex_v3.2.1.cdx.json</span> — 标准 VEX（工程师/下游）</li>
        <li><span class="mono">incident_*.json</span> — Art.14 三段报告草稿</li>
        <li><span class="mono">sbom_v3.2.2.json</span> — 修复后 SBOM（diff 可审计）</li>
        <li><span class="mono">evidence_graph.json</span> — 全链路图数据</li>
        <li><span class="mono">reachability.png / evidence_graph.png</span> — 汇报用图</li>
      </ul>
      <p class="small" style="margin-top:1rem;">全部由 <span class="mono">demo/cra_lifecycle_demo.ipynb</span>（21 单元）一次执行生成。</p>
    </div>
  </div>
</section>

<section class="slide" id="s8">
  <div class="stage">So What</div>
  <div class="kicker">收尾 · 和竞品的分界线</div>
  <h2>扫描器卖"发现"；我们卖<strong>可采信的结论</strong></h2>
  <div class="conclusion">
    发现会同质化，证据随客户合规历史复利——这是周日要拍板的定位（report/04 · Q1-Q10）。
  </div>
  <div class="cards">
    <div class="card"><div class="num">1</div><div class="lbl"><strong>VEX 判定工作流</strong><br>状态机+强制证据+SLA，而非格式导出</div></div>
    <div class="card"><div class="num">2</div><div class="lbl"><strong>Art.14 事件时钟</strong><br>义务已生效 11 天，竞品无字段级实现</div></div>
    <div class="card"><div class="num">3</div><div class="lbl"><strong>Evidence Graph</strong><br>产品级模型 + 10 年回放，数据护城河</div></div>
  </div>
  <h3>接下来（从本演示到产品）</h3>
  <ol class="story">
    <li><strong>PoC-1/2/3</strong>：多源归一金标准 ≥90% · L2 reachability 验收 · VEX 留存 4 周（report/08 §3）</li>
    <li><strong>下轮研究</strong>：ENISA SRP 真接口 · Black Duck 等四家重验 · 10 个客户访谈</li>
    <li><strong>复现本演示</strong>：<span class="mono">./demo/serve.sh</span> 或 <span class="mono">python demo/build_notebook.py</span></li>
  </ol>
</section>

<nav class="dots" id="dots"></nav>
<div class="hint">← → 翻页 · 滚轮亦可 · {len(vex['analysis'])} 判定 / 7 阶段</div>
<script>
const slides=[...document.querySelectorAll("section.slide")];
const dots=document.getElementById("dots");
slides.forEach((_,i)=>{{const a=document.createElement("a");a.href="#s"+i;a.dataset.i=i;dots.appendChild(a);}});
let cur=0;
const io=new IntersectionObserver(es=>{{
  es.forEach(e=>{{if(e.isIntersecting){{
    cur=slides.indexOf(e.target);
    [...dots.children].forEach((d,j)=>d.classList.toggle("on",j===cur));
  }} }});
 }},{{threshold:.55}});
slides.forEach(s=>io.observe(s));
addEventListener("keydown",e=>{{
  if(e.key==="ArrowRight"||e.key==="ArrowDown"||e.key==="PageDown"){{e.preventDefault();slides[Math.min(cur+1,slides.length-1)].scrollIntoView();}}
  if(e.key==="ArrowLeft"||e.key==="ArrowUp"||e.key==="PageUp"){{e.preventDefault();slides[Math.max(cur-1,0)].scrollIntoView();}}
}});
</script>
</body>
</html>
"""

DEST.write_text(html, encoding="utf-8")
print(f"wrote {DEST} ({DEST.stat().st_size:,} bytes)")
