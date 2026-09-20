#!/usr/bin/env python3
"""Shared helpers for the CRA PoC pipeline (stdlib only)."""
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

POC_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_ROOT = os.path.join(POC_ROOT, "out")
DB_PATH = os.path.join(OUT_ROOT, "evidence.db")

PREDICATE_TYPE = "https://cra-research.dev/attestation/conclusion/v0.1"
STATEMENT_TYPE = "https://in-toto.io/Statement/v1"
SIGNER_NAME = "cra-research-poc-dev-key"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_json(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
    return path


def read_json(path):
    with open(path) as f:
        return json.load(f)


def run(cmd, cwd=None, capture=True, check=True, env=None):
    """Run a command, returning (exit_code, stdout, stderr)."""
    e = dict(os.environ)
    # user-local tools live outside the default PATH
    e["PATH"] = e["PATH"] + ":" + os.path.expanduser("~/bin") + ":" + os.path.expanduser("~/go/bin")
    if env:
        e.update(env)
    p = subprocess.run(cmd, cwd=cwd, env=e,
                       stdout=subprocess.PIPE if capture else None,
                       stderr=subprocess.PIPE if capture else None, text=True)
    if check and p.returncode != 0:
        sys.stderr.write(f"command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr or ''}\n")
        sys.exit(1)
    return p.returncode, p.stdout or "", p.stderr or ""


def tool_version(cmd, pattern_first_line=True):
    rc, out, err = run(cmd, check=False)
    text = (out or err).strip().splitlines()
    return text[0].strip() if text else f"unknown (exit {rc})"
