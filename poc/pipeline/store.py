#!/usr/bin/env python3
"""SQLite evidence store for the CRA PoC.

Deliberately plain SQLite (Python 3.12 stdlib). Research conclusion: the moat
is the data model, not graph storage. Production target is PostgreSQL with the
same schema; no graph database is used anywhere by design.

Schema:
  artifacts     — product binaries / SBOM files, keyed by sha256
  evidence      — content-addressed evidence blobs (files the conclusions cite)
  conclusions   — reachability / vex / verification conclusions
  attestations  — signed in-toto Statement v1 DSSE envelopes, one per conclusion
"""
import argparse
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import DB_PATH, now_iso

SCHEMA = """
CREATE TABLE IF NOT EXISTS artifacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product TEXT NOT NULL,
  version TEXT NOT NULL,
  name TEXT NOT NULL,
  path TEXT NOT NULL,
  sha256 TEXT NOT NULL,
  type TEXT NOT NULL,
  created_at TEXT NOT NULL,
  UNIQUE(product, version, name)
);
CREATE TABLE IF NOT EXISTS evidence (
  sha256 TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  path TEXT,
  inline_json TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS conclusions (
  id TEXT PRIMARY KEY,
  product TEXT NOT NULL,
  version TEXT NOT NULL,
  conclusion_type TEXT NOT NULL CHECK (conclusion_type IN ('reachability','vex','verification')),
  vuln_id TEXT NOT NULL,
  status TEXT NOT NULL,
  justification TEXT,
  tool_name TEXT NOT NULL,
  tool_version TEXT NOT NULL,
  tool_command TEXT NOT NULL,
  evidence_json TEXT NOT NULL,
  attestation_sha256 TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS attestations (
  sha256 TEXT PRIMARY KEY,
  conclusion_id TEXT NOT NULL REFERENCES conclusions(id),
  envelope_json TEXT NOT NULL,
  signer TEXT NOT NULL,
  keyid TEXT NOT NULL,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_conclusions_product ON conclusions(product, version);
"""


def connect(db_path=DB_PATH):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def main():
    ap = argparse.ArgumentParser(description="init/inspect the evidence store")
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()
    conn = connect(args.db)
    if args.stats:
        for t in ("artifacts", "evidence", "conclusions", "attestations"):
            n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            print(f"{t}: {n}")
        for row in conn.execute(
            "SELECT conclusion_type, status, COUNT(*) c FROM conclusions GROUP BY 1,2"
        ):
            print(f"  {row['conclusion_type']}/{row['status']}: {row['c']}")
    else:
        print(f"store ready at {args.db} ({now_iso()})")


if __name__ == "__main__":
    main()
