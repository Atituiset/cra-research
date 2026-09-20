# Source Note: CWE 官方 About 页

- **URL**: https://cwe.mitre.org/about/index.html
- **标题**: About CWE — Common Weakness Enumeration
- **发布方**: MITRE（CWE Program）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. 定义原文："a community-developed list of common software and hardware **weaknesses**. A 'weakness' is a condition in a software, firmware, hardware, or service component that, **under certain circumstances, could contribute to the introduction of vulnerabilities**."
2. 目的：让开发者/设计者/架构师在部署前消除弱点（左移）。
3. CWE List 每年更新 3–4 次；内容在 GitHub 的 CWE Content Development Repository (CDR) 公开开发。
4. 组织方式：多种 **Views**（Software Development / Hardware Design / Research Concepts 等）和外部映射（CWE Top 25、OWASP Top Ten、CERT Coding Standards、Seven Pernicious Kingdoms 等）。
5. 有 CWE REST API；内容免费用于工具和研究（terms of use）。
6. 生态：CWE-Compatible 产品认证、CWE Top 25、CWE Top KEV 等衍生榜单。

## 支撑报告中的结论

- §3 CWE 定义（weakness = 可能导致漏洞的条件，不是漏洞本身）
- §3 CVE↔CWE 映射的含义（实例 → 类别）
- §3 CWE 对 SAST（检测弱点类别）/SCA（给 CVE 挂弱点类别）的价值
