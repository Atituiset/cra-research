#!/usr/bin/env python3
"""Stage 3b — C reachability via Joern (CPG call-path analysis).

Runs Joern in Docker (ghcr.io/joernio/joern:nightly; no JDK on the host):
  1. joern-parse builds a CPG from the compilation database / source tree
  2. joern --script callpath.sc dumps method definitions + call edges
  3. we BFS from `main` to each curated vulnerable function and keep the
     shortest call path itself as evidence

The vuln->function mapping is hand-curated (curation/vuln-function-map.json) —
a legitimate PoC practice per the research conclusions.
"""
import argparse
import json
import os
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import read_json, run, sha256_file, write_json, now_iso

JOERN_IMAGE = "ghcr.io/joernio/joern:nightly"
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "joern", "callpath.sc")


def docker_joern(args_list, mounts):
    cmd = ["docker", "run", "--rm",
           "--user", f"{os.getuid()}:{os.getgid()}",
           "-e", "HOME=/tmp", "-w", "/tmp"]
    for host, cont, ro in mounts:
        cmd += ["-v", f"{host}:{cont}:{'ro' if ro else 'rw'}"]
    cmd.append(JOERN_IMAGE)
    cmd += args_list
    return run(cmd, check=False)


def bfs_shortest_path(edges, start, target_names):
    """edges: caller_name -> [(callee_name, line, file)]. Return shortest path of
    (function, call_line, call_file) hops from start to any target, or None."""
    # start is a fullName; resolve to simple name for edge lookup
    start_simple = start.split("(")[0].split(":")[-1]
    if start_simple in target_names:
        return [{"function": start_simple, "call_line": None, "call_file": None}]
    q = deque([(start_simple, [])])
    seen = {start_simple}
    while q:
        node, path = q.popleft()
        for callee, line, file in edges.get(node, []):
            hop = {"function": callee, "call_line": line, "call_file": file}
            if callee in target_names:
                return path + [hop]
            if callee not in seen:
                seen.add(callee)
                q.append((callee, path + [hop]))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--appdir", required=True)
    ap.add_argument("--entry", default="main")
    ap.add_argument("--curation", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    appdir = os.path.abspath(args.appdir)
    workdir = os.path.abspath(args.outdir)
    os.makedirs(workdir, exist_ok=True)
    script_dir = os.path.dirname(SCRIPT)

    mounts = [(appdir, "/src", True), (workdir, "/out", False), (script_dir, "/sc", True)]

    rc, out, err = docker_joern(
        ["joern-parse", "--language", "newc", "--output", "/out/cpg.bin", "/src"], mounts)
    if rc != 0:
        sys.stderr.write(f"joern-parse failed:\n{err}\n{out}\n")
        sys.exit(1)

    rc, out, err = docker_joern(
        ["joern", "--script", "/sc/callpath.sc", "--param", "cpgFile=/out/cpg.bin"],
        mounts)
    lines = [l for l in out.splitlines() if l.startswith(("DEF\t", "CALL\t"))]
    # Joern exits 1 on a save-on-exit NPE *after* the script has already printed
    # its results; tolerate the exit code if the dump is complete.
    if rc != 0 and not any(l.startswith("CALL\t") for l in lines):
        sys.stderr.write(f"joern script failed:\n{err}\n{out}\n")
        sys.exit(1)

    dump_path = os.path.join(workdir, "joern-cpg-dump.tsv")
    with open(dump_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    defs, edges = {}, {}
    for l in lines:
        parts = l.split("\t")
        if parts[0] == "DEF":
            _, name, full, file, line = parts
            defs.setdefault(name, {"full_name": full, "file": file, "line": line})
        else:
            _, caller_full, callee, callee_full, line, file = parts
            caller_simple = caller_full.split("(")[0].split(":")[-1]
            edges.setdefault(caller_simple, []).append(
                (callee, int(line), file))

    cur = read_json(args.curation)
    findings = []
    for m in cur.get("mappings", []):
        target_names = {f["name"] for f in m["functions"]}
        path = bfs_shortest_path(edges, args.entry, target_names)
        # annotate hops with definition locations
        annotated = []
        if path:
            for hop in [{"function": args.entry, "call_line": None, "call_file": None}] + path:
                d = defs.get(hop["function"], {})
                annotated.append({
                    "function": hop["function"],
                    "defined_in": d.get("file"),
                    "defined_line": d.get("line"),
                    "called_at_line": hop["call_line"],
                    "called_in_file": hop["call_file"],
                })
        findings.append({
            "vuln_id": m["vuln_id"],
            "aliases": m.get("aliases", []),
            "package": m["package"],
            "vulnerable_functions": m["functions"],
            "reachable": path is not None,
            "status": "affected" if path else "not_affected",
            "justification": None if path else "vulnerable_code_not_in_execute_path",
            "call_path": annotated,
            "call_path_length": len(annotated),
        })

    result = {
        "product": args.product,
        "generated_at": now_iso(),
        "tool": {
            "name": "joern",
            "version": f"docker {JOERN_IMAGE}",
            "command": "docker run ... joern-parse --language newc --output /out/cpg.bin /src; "
                       "docker run ... joern --script callpath.sc --param cpgFile=/out/cpg.bin",
        },
        "compile_commands": os.path.join(appdir, "build", "compile_commands.json"),
        "raw_outputs": {
            "cpg_dump": {"path": dump_path, "sha256": sha256_file(dump_path)},
        },
        "curation": os.path.abspath(args.curation),
        "findings": findings,
    }
    write_json(args.out, result)
    print(json.dumps({
        "product": args.product,
        "functions_defined": len(defs),
        "call_edges": sum(len(v) for v in edges.values()),
        "findings": [{"vuln": f["vuln_id"], "status": f["status"],
                      "path": " -> ".join(h["function"] for h in f["call_path"]) or None}
                     for f in findings],
    }, indent=2))


if __name__ == "__main__":
    main()
