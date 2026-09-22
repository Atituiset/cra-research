#!/usr/bin/env python3
"""Build the unified presentation from verified historical Go/C evidence packs."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from cra.core import Store

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--db', default=str(ROOT / 'var/cra.db'))
parser.add_argument('--out', default=str(ROOT / 'demo/out'))
args = parser.parse_args()
store = Store(args.db)
try:
    for product in ('go-vuln-app', 'c-vuln-app'):
        store.import_pack(ROOT / f'poc/out/evidence-pack-{product}-0.1.0',
                          ROOT / 'poc/keys/dev-ed25519.pub.json')
    print(store.export(args.out))
finally:
    store.db.close()
