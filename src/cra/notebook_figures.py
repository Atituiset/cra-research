"""Evidence-led research figures. All numerical and graph data come from snapshots."""
from collections import Counter
from functools import lru_cache
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, FancyArrowPatch, Circle, Rectangle

BG = '#ffffff'
INK = '#14283e'
MUTED = '#657589'
LINE = '#e3e9ef'
BLUE = '#306bd9'
TEAL = '#148a77'
AMBER = '#b87613'
RED = '#d4535e'
PURPLE = '#8154c2'
COLORS = {'affected': RED, 'not_affected': TEAL, 'under_investigation': AMBER}
HERO = 'GO-2023-2402'


@lru_cache(maxsize=1)
def configure():
    for path in font_manager.findSystemFonts(fontpaths=[str(Path.home() / '.fonts')]):
        try:
            font_manager.fontManager.addfont(path)
        except (RuntimeError, NotImplementedError):
            continue
    names = {f.name for f in font_manager.fontManager.ttflist}
    choices = ['Noto Sans CJK SC', 'Noto Sans CJK JP', 'Microsoft YaHei', 'PingFang SC', 'SimHei']
    font = next((f for f in choices if f in names), 'DejaVu Sans')
    plt.rcParams.update({'font.family': font, 'font.size': 11, 'axes.unicode_minus': False,
                         'figure.facecolor': BG, 'savefig.facecolor': BG})


def canvas(number, title, subtitle, footnote, height=8.3):
    configure()
    fig = plt.figure(figsize=(15, height))
    ax = fig.add_axes([.04,.12,.92,.69])
    ax.set(xlim=(0,100),ylim=(0,100)); ax.axis('off')
    fig.text(.045,.954,f'CRA RESEARCH     /     {number}',fontsize=10,color=BLUE)
    fig.text(.045,.892,title,fontsize=25,color=INK)
    fig.text(.045,.846,subtitle,fontsize=11,color=MUTED)
    fig.text(.045,.052,footnote,fontsize=10,color=MUTED)
    return fig,ax


def label(ax,x,y,text,size=11,color=INK,ha='left',va='center',**kwargs):
    return ax.text(x,y,text,fontsize=size,color=color,ha=ha,va=va,**kwargs)


def edge(ax,a,b,color=LINE,lw=1.6,rad=0,arrow=True,style='-',alpha=1):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>' if arrow else '-',
        mutation_scale=12,connectionstyle=f'arc3,rad={rad}',color=color,
        linewidth=lw,linestyle=style,alpha=alpha,zorder=1,shrinkA=6,shrinkB=6))


def node(ax,x,y,text,color=BLUE,size=340,detail=None,above=False):
    ax.scatter([x],[y],s=size,c=color,edgecolors='white',linewidths=2,zorder=4)
    label(ax,x,y+(7 if above else -7),text,11,color,ha='center',va='bottom' if above else 'top',zorder=5)
    if detail:
        label(ax,x,y+(13 if above else -13),detail,9,MUTED,ha='center',va='bottom' if above else 'top',zorder=5)


def records(snapshot,kind):
    return [e for e in snapshot['evidence'] if e['predicate']['conclusion_type']==kind]


def get_record(snapshot,kind,vid):
    return next(e for e in records(snapshot,kind) if e['predicate']['vulnerability']['id']==vid)


def ribbon(ax,x0,y0,x1,y1,height,color,alpha=.25):
    mid=(x0+x1)/2
    verts=[(x0,y0),(mid,y0),(mid,y1),(x1,y1),(x1,y1+height),
           (mid,y1+height),(mid,y0+height),(x0,y0+height),(x0,y0)]
    codes=[MPath.MOVETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,MPath.LINETO,
           MPath.CURVE4,MPath.CURVE4,MPath.CURVE4,MPath.CLOSEPOLY]
    ax.add_patch(PathPatch(MPath(verts,codes),facecolor=color,alpha=alpha,edgecolor='none'))


def workflow(snapshot):
    p=get_record(snapshot,'reachability',HERO)['predicate']
    v=get_record(snapshot,'verification',HERO)['predicate']
    fig,ax=canvas('01 / CASE FILE','从一个真实漏洞，看产品团队需要回答什么',
        '贯穿案例 · go-vuln-app 0.1.0 / Terrapin / CVE-2023-48795',
        '本页为历史样例回放。工具结果已存在；当前工作台的人签、事件报送尚未在该样例上执行。')
    for x,value,title in [(1,len(snapshot['releases']),'发布物'),(25,len(snapshot['judgments']),'判定候选'),
                           (49,len(snapshot['evidence']),'签名证据'),(73,len(snapshot['reviews']),'本次复核记录')]:
        label(ax,x,92,str(value),35,INK)
        label(ax,x+9,89,title,11,MUTED)
    ax.plot([0,100],[79,79],color=LINE,lw=1)
    stages=[(8,'组件与漏洞','x/crypto / SSH',BLUE), (35,'应用调用','main → connectSSH → Dial',RED),
            (63,'修复验证',v['status']+' · 历史复扫',TEAL),(91,'正式判断','当前仍需复核',AMBER)]
    for (x,title,detail,color),(nx,*_) in zip(stages,stages[1:]):
        edge(ax,(x,57),(nx,57),color=color,lw=2.5,style='--' if nx==91 else '-')
    for x,title,detail,color in stages:
        node(ax,x,57,title,color,size=700)
        label(ax,x,37,detail,10,MUTED,ha='center')
    label(ax,0,18,'这条链的价值',12,BLUE)
    label(ax,0,7,'不是停在“发现 CVE”，而是保留：为什么判定、修复证据在哪、还有谁需要复核。',15,INK)
    return fig


def distribution(snapshot):
    counts=Counter(j['proposed_status'] for j in snapshot['judgments'])
    effective=Counter(j['effective_status'] for j in snapshot['judgments'])
    n=len(snapshot['judgments'])
    fig,ax=canvas('02 / TRIAGE','同一批漏洞，工具建议如何进入复核队列？',
        f'实测数据 · {n} 条候选；展示关联、工具建议与当前工作台状态的区别',
        '流带宽度按条目数计算。建议“不受影响”并不自动发布；这不是准确率或降噪率图。')
    label(ax,1,96,'关联命中',12,MUTED); label(ax,40,96,'历史工具建议',12,MUTED); label(ax,78,96,'当前有效状态',12,MUTED)
    y0=15
    titles={'affected':'建议受影响','not_affected':'建议不受影响','under_investigation':'无结论 / 调查中'}
    target=15
    dest=9
    for status in ('under_investigation','not_affected','affected'):
        count=counts[status]; h=count/n*65; color=COLORS[status]
        ax.add_patch(Rectangle((4,y0),3,h,facecolor=color))
        ribbon(ax,7,y0,40,dest,h,color)
        ax.add_patch(Rectangle((40,dest),2,h,facecolor=color))
        ribbon(ax,42,dest,81,target,h,color,.16)
        ax.add_patch(Rectangle((81,target),3,h,facecolor=AMBER))
        label(ax,44,dest+h/2,f'{count}  {titles[status]}',12,color)
        y0+=h; target+=h; dest+=h+5
    label(ax,0,5,f'{n} 条 = Go 77 + C 1',11,MUTED)
    label(ax,88,57,str(effective.get('under_investigation',0)),38,AMBER,ha='center')
    label(ax,88,43,'待复核',13,AMBER,ha='center')
    label(ax,88,29,'未自动批准',10,MUTED,ha='center')
    return fig


def callpaths(snapshot):
    fig,ax=canvas('03 / REACHABILITY','调用图真正揭示的是：风险沿哪些分支传播',
        'Go 实测 · 合并所有 affected 记录里的 call-trace；红色为 Terrapin 案例路径',
        '边来自已验签的函数调用栈，不补画不存在的分支。可达性之外，利用条件仍需单独研判。',height=9)
    positions={'main':(8,58),'connectSSH':(29,76),'Dial':(52,76),'DialTimeout':(82,87),
               'ToASCII':(29,37),'process':(48,37),'validateRegistration':(67,37),'IsNormalString':(89,37)}
    links=set(); terminal=Counter(); locations={}
    for e in records(snapshot,'reachability'):
        p=e['predicate']
        if p['product']!='go-vuln-app' or p['status']!='affected':continue
        trace=next(t for t in p['evidence'] if t['kind']=='call-trace')
        frames=list(reversed(trace['frames']))
        terminal[frames[-1]['function']]+=1
        for f in frames:
            locations[f['function']]=f"{Path(f['position']['filename']).name}:{f['position']['line']}"
        links.update((a['function'],b['function']) for a,b in zip(frames,frames[1:]))
    hero={('main','connectSSH'),('connectSSH','Dial')}
    ax.add_patch(Rectangle((1,19),97,77,facecolor='#f7f9fc',edgecolor='none'))
    for a,b in sorted(links):
        edge(ax,positions[a],positions[b],RED if (a,b) in hero else '#acbacc',3.2 if (a,b) in hero else 2)
    for name,(x,y) in positions.items():
        color=RED if name in ('main','connectSSH','Dial') else BLUE
        node(ax,x,y,name,color,size=850 if name=='Dial' else 430,detail=locations.get(name))
        if terminal[name]:
            label(ax,x,y+9,f'{terminal[name]} 条漏洞路径终点',10,color,ha='center')
    label(ax,45,94,'SSH 分支 · Terrapin 路径高亮',11,RED,ha='center')
    label(ax,56,20,'IDNA / Unicode 分支',10,BLUE,ha='center')
    label(ax,1,8,'证据读法',11,BLUE)
    label(ax,13,8,'main.go:45 → main.go:29 → ssh/client.go:176；漏洞函数并非孤立地存在于依赖中。',12,INK)
    return fig


def evidence_graph(snapshot):
    selected=[HERO,'GO-2024-2687','GO-2026-4971']
    fig,ax=canvas('04 / EVIDENCE GRAPH','一份产品档案，连接多种不同的漏洞结论',
        '从真实快照抽取三个案例：Terrapin、缺陷代码未引入、升级后仍存在的漏洞',
        '按 release_id、vulnerability、evidence_ids 连接。按漏洞聚合的分析/验证为查询结果，不冒充直接判定引用。',height=9.2)
    for x,text in [(3,'发布物'),(24,'漏洞'),(51,'历史分析与验证'),(81,'当前判定')]:
        label(ax,x,98,text,11,MUTED)
    for x in [18,43,72]:ax.plot([x,x],[5,91],color=LINE,lw=1,ls=':')
    node(ax,8,50,'go-vuln-app',BLUE,800,detail='0.1.0 / 制品 hash')
    for vid,y in zip(selected,[79,49,19]):
        judgment=next(j for j in snapshot['judgments'] if j['vulnerability']==vid)
        related=[e for e in snapshot['evidence'] if e['predicate']['vulnerability']['id']==vid]
        ishero=vid==HERO; color=RED if ishero else '#8a9db1'
        edge(ax,(8,50),(29,y),color,2.8 if ishero else 1.5)
        node(ax,29,y,vid,RED if ishero else BLUE,460)
        offsets=[10,0,-10] if len(related)==3 else [5,-5]
        kinds={'reachability':'分析','vex':'原始 VEX','verification':'复扫'}
        for e,off in zip(sorted(related,key=lambda e:e['predicate']['conclusion_type']),offsets):
            p=e['predicate']; status=p['status']; ec=TEAL if status in ('fixed','not_affected') else RED if status in ('affected','still_present') else AMBER
            edge(ax,(29,y),(53,y+off),color,1.4,arrow=False)
            ax.scatter([53],[y+off],s=160,c=ec,zorder=4,edgecolors='white')
            label(ax,55,y+off+2,kinds[p['conclusion_type']]+' · '+status,9,ec,va='bottom')
            if e['id'] in judgment['evidence_ids']:
                edge(ax,(54,y+off),(85,y),AMBER,1.7,rad=.22)
        node(ax,85,y,'待复核',AMBER,440,detail=judgment['proposed_status'])
    label(ax,0,0,'高亮案例沿整条链追溯；其他漏洞共用发布物，却保留各自的分析、复扫与判定。',11,MUTED)
    return fig


def verification(snapshot):
    entries=sorted([e['predicate'] for e in records(snapshot,'verification')],key=lambda p:(p['status']=='still_present',p['vulnerability']['id']))
    counts=Counter(p['status'] for p in entries)
    fig,ax=canvas('05 / BEFORE → AFTER',f"升级解决了 {counts['fixed']} 条，为什么还有 {counts['still_present']} 条留下？",
        '历史 Go 复扫 · 每一行是一条原 affected 漏洞，右侧是该条目的验证结果',
        'GO-2026-4971 在该次仅升级依赖的实验中仍存在。历史复扫不会覆盖旧发布物，也不会自动批准当前判定。',height=9.4)
    for x,text in [(0,'漏洞 ID'),(35,'升级前'),(65,'历史复扫 fixed'),(91,'仍存在')]:label(ax,x,96,text,11,MUTED,ha='center' if x else 'left')
    for x in (35,65,91):ax.plot([x,x],[6,90],color=LINE,lw=1)
    for p,y in zip(entries,range(87,3,-7)):
        fixed=p['status']=='fixed'; end=65 if fixed else 91; color=TEAL if fixed else RED
        label(ax,0,y,p['vulnerability']['id'],11,INK)
        ax.plot([35,end],[y,y],color=color,lw=2,alpha=.55)
        ax.scatter([35],[y],s=90,facecolors='white',edgecolors=RED,linewidths=1.5,zorder=3)
        ax.scatter([end],[y],s=150,c=color,edgecolors='white',zorder=4)
    ax.text(.68,.69,f"{counts['fixed']}/{len(entries)}",transform=ax.transAxes,fontsize=37,color=TEAL)
    ax.text(.68,.60,'条目在历史复扫中标为 fixed',transform=ax.transAxes,fontsize=10,color=MUTED)
    ax.text(.70,.25,'剩余条目需要继续处置\n不能把“升级完成”当成闭环',transform=ax.transAxes,fontsize=11,color=RED)
    return fig


def reporting(snapshot):
    fig,ax=canvas('06 / REPORTING CLOCK','24 小时从哪里开始，最终报告又从哪里起算？',
        '规则示意 · 当前案例没有真实事件；以下两条时间线展示不同的起算依据',
        '时钟是辅助计算。KEV 信号触发核查，适用性依据与实际知悉时间需保留；人工审批不重置知悉时间。')
    label(ax,0,93,'情报 / KEV 信号',12,BLUE)
    edge(ax,(21,93),(32,93),BLUE)
    label(ax,34,93,'核查产品适用性，记录实际知悉事实',12,INK)
    for y,title,last in [(66,'主动利用漏洞','纠正或缓解措施可用'),(24,'严重事件','正式通知提交')]:
        label(ax,0,y+15,title,13,INK)
        ax.plot([8,61],[y,y],color=BLUE,lw=2)
        for x,t in [(8,'T0\n知悉'),(26,'≤24h\n预警'),(61,'≤72h\n正式通知')]:
            ax.scatter([x],[y],s=130,c=BLUE,zorder=3)
            label(ax,x,y-5,t,11,BLUE,ha='center',va='top')
        if y==66:
            ax.plot([65,68,67,70],[y-1,y+1,y-1,y+1],color=MUTED,lw=1.5)
            label(ax,80,y+12,last,10,AMBER,ha='center')
            ax.plot([74,98],[y,y],color=AMBER,lw=2)
            ax.scatter([74,98],[y,y],s=130,c=AMBER)
            label(ax,86,y-6,'起算后 ≤14 天\n最终报告',11,AMBER,ha='center',va='top')
        else:
            edge(ax,(62,y),(98,y),AMBER,2,style='--')
            ax.scatter([98],[y],s=130,c=AMBER)
            label(ax,81,y+10,'自实际正式通知起算',10,AMBER,ha='center')
            label(ax,81,y-6,'1 个日历月内\n最终报告',11,AMBER,ha='center',va='top')
    return fig


FIGURES={'workflow':workflow,'distribution':distribution,'callpaths':callpaths,
         'evidence_graph':evidence_graph,'verification':verification,'reporting':reporting}


def build_figure(snapshot,name):
    return FIGURES[name](snapshot)
