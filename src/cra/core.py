"""Immutable local prototype store. All public mutations are transactional."""
from __future__ import annotations

import base64
import calendar
import hashlib
import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def instant(value):
    d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("Time must include a timezone")
    return d.astimezone(timezone.utc)


def verify_envelope(raw, key):
    env = json.loads(raw)
    payload = base64.b64decode(env["payload"], validate=True)
    kind = env["payloadType"].encode()
    if kind != b"application/vnd.in-toto+json":
        raise ValueError("Unexpected DSSE payload type")
    pae = b"DSSEv1 %d %s %d %s" % (len(kind), kind, len(payload), payload)
    signatures = [s for s in env["signatures"] if s["keyid"] == key["keyid"]]
    if not signatures:
        raise ValueError("No signature from the configured trusted key")
    public = Ed25519PublicKey.from_public_bytes(bytes.fromhex(key["keyval"]["public"]))
    public.verify(base64.b64decode(signatures[0]["sig"], validate=True), pae)
    statement = json.loads(payload)
    if statement["_type"] != "https://in-toto.io/Statement/v1":
        raise ValueError("Unexpected statement type")
    return statement


class Store:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript('''
          CREATE TABLE IF NOT EXISTS objects(
            id TEXT PRIMARY KEY, kind TEXT NOT NULL, body TEXT NOT NULL);
          CREATE TABLE IF NOT EXISTS blobs(hash TEXT PRIMARY KEY, data BLOB NOT NULL);
          CREATE TRIGGER IF NOT EXISTS no_update BEFORE UPDATE ON objects
            BEGIN SELECT RAISE(ABORT,'objects are immutable'); END;
          CREATE TRIGGER IF NOT EXISTS no_delete BEFORE DELETE ON objects
            BEGIN SELECT RAISE(ABORT,'objects are immutable'); END;
          CREATE TRIGGER IF NOT EXISTS no_blob_update BEFORE UPDATE ON blobs
            BEGIN SELECT RAISE(ABORT,'blobs are immutable'); END;
          CREATE TRIGGER IF NOT EXISTS no_blob_delete BEFORE DELETE ON blobs
            BEGIN SELECT RAISE(ABORT,'blobs are immutable'); END;
        ''')

    def put(self, kind, body, identity=None):
        identity = identity or f"{kind}-{uuid4()}"
        raw = encoded(body).decode()
        existing = self.db.execute("SELECT kind,body FROM objects WHERE id=?", (identity,)).fetchone()
        if existing and (existing['kind'] != kind or existing['body'] != raw):
            raise ValueError("Object identity collision")
        self.db.execute("INSERT OR IGNORE INTO objects VALUES(?,?,?)", (identity, kind, raw))
        return identity

    def get(self, identity, kind=None):
        row = self.db.execute("SELECT * FROM objects WHERE id=?", (identity,)).fetchone()
        if row is None or (kind and row['kind'] != kind):
            raise ValueError(f"Unknown {kind or 'object'}: {identity}")
        return {"id": row['id'], "kind": row['kind'], **json.loads(row['body'])}

    def all(self, kind):
        return [self.get(r[0]) for r in self.db.execute(
            "SELECT id FROM objects WHERE kind=? ORDER BY rowid", (kind,)).fetchall()]

    def blob(self, raw):
        sha = digest(raw)
        self.db.execute("INSERT OR IGNORE INTO blobs VALUES(?,?)", (sha, raw))
        return sha

    def import_pack(self, directory, key_path):
        root = Path(directory).resolve()
        manifest_raw = (root / 'manifest.json').read_bytes()
        manifest = json.loads(manifest_raw)
        key = json.loads(Path(key_path).read_bytes())
        files, statements = {}, {}
        for name, expected in manifest['files'].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root) or path == root:
                raise ValueError("Unsafe manifest path")
            raw = path.read_bytes()
            if digest(raw) != expected:
                raise ValueError(f"File hash mismatch: {name}")
            files[name] = raw
            if name.startswith('attestations/'):
                statement = verify_envelope(raw, key)
                statements[digest(encoded(json.loads(raw)))] = statement
        # Legacy attestation IDs hash default json serialization, so index by signed ID.
        by_id = {s['predicate']['conclusion_id']: s for s in statements.values()}
        subjects = set()
        for item in manifest['conclusions']:
            s = by_id.get(item['id'])
            if not s:
                raise ValueError("Manifest conclusion has no verified statement")
            p = s['predicate']
            if (p['product'], p['product_version'], p['status'], p['conclusion_type'], p['vulnerability']['id']) != (
                manifest['product'], manifest['version'], item['status'], item['type'], item['vuln']):
                raise ValueError("Manifest contradicts signed statement")
            subjects.add(s['subject'][0]['digest']['sha256'])
        if len(subjects) != 1:
            raise ValueError("Pack must describe exactly one release artifact")
        artifact = subjects.pop()
        release_id = 'release-' + digest(encoded([manifest['product'], manifest['version'], artifact]))
        pack_id = 'pack-' + digest(manifest_raw)
        with self.db:
            if self.db.execute("SELECT 1 FROM objects WHERE id=?", (pack_id,)).fetchone():
                return release_id
            file_refs = {name: self.blob(raw) for name, raw in files.items()}
            self.put('release', {'product': manifest['product'], 'version': manifest['version'],
                                'artifact_sha256': artifact}, release_id)
            self.put('pack', {'release_id': release_id, 'manifest_hash': self.blob(manifest_raw),
                             'files': file_refs, 'trusted_key': key, 'data_kind': 'measured',
                             'imported_at': now(), 'source': root.name}, pack_id)
            for item in manifest['conclusions']:
                p = by_id[item['id']]['predicate']
                eid = self.put('evidence', {'release_id': release_id, 'pack_id': pack_id,
                    'legacy_id': item['id'], 'predicate': p, 'data_kind': 'measured'},
                    'evidence-' + digest(encoded([pack_id, item['id']])))
                if item['type'] == 'vex':
                    previous = [j for j in self.latest_judgments(release_id)
                                if j['vulnerability'] == item['vuln']]
                    self.put('judgment', {'release_id': release_id, 'vulnerability': item['vuln'],
                        'proposed_status': item['status'], 'justification': p.get('justification'),
                        'evidence_ids': [eid], 'policy': 'legacy-import-review/v1',
                        'created_at': now(), 'supersedes': previous[-1]['id'] if previous else None})
        return release_id

    def review(self, judgment_id, decision, actor, reason):
        judgment = self.get(judgment_id, 'judgment')
        if judgment_id not in {j['id'] for j in self.latest_judgments(judgment['release_id'])}:
            raise ValueError("Cannot review a superseded judgment")
        if decision not in ('approved', 'rejected') or not actor.strip() or not reason.strip():
            raise ValueError("Review requires decision, actor and substantive reason")
        with self.db:
            return self.put('review', {'judgment_id': judgment_id, 'decision': decision,
                                     'actor': actor, 'reason': reason, 'created_at': now()})

    def latest_judgments(self, release_id):
        all_items = [j for j in self.all('judgment') if j['release_id'] == release_id]
        replaced = {j['supersedes'] for j in all_items}
        reviews = {r['judgment_id']: r for r in self.all('review')}
        result = []
        for j in all_items:
            if j['id'] in replaced:
                continue
            review = reviews.get(j['id'])
            result.append({**j, 'review': review,
                'effective_status': j['proposed_status'] if review and review['decision'] == 'approved'
                                    else 'under_investigation'})
        return result

    def reassess(self, judgment_id, reason):
        old = self.get(judgment_id, 'judgment')
        if not reason.strip():
            raise ValueError("Reassessment requires a reason")
        if judgment_id not in {j['id'] for j in self.latest_judgments(old['release_id'])}:
            raise ValueError("Only the current judgment can be superseded")
        body = {k: v for k, v in old.items() if k not in ('id', 'kind')}
        body.update(proposed_status='under_investigation', justification=None,
                    supersedes=judgment_id, created_at=now(), reassessment_reason=reason)
        with self.db:
            return self.put('judgment', body)

    def verify_fix(self, old_judgment_id, new_judgment_id, actor, basis):
        old = self.get(old_judgment_id, 'judgment')
        new = self.get(new_judgment_id, 'judgment')
        old_release = self.get(old['release_id'], 'release')
        new_release = self.get(new['release_id'], 'release')
        if (old['vulnerability'] != new['vulnerability'] or
                old_release['product'] != new_release['product'] or
                old_release['artifact_sha256'] == new_release['artifact_sha256']):
            raise ValueError("Verification requires same product/vulnerability and a different artifact")
        current = {j['id']: j for r in (old_release, new_release)
                   for j in self.latest_judgments(r['id'])}
        if (old_judgment_id not in current or new_judgment_id not in current or
                current[old_judgment_id]['effective_status'] != 'affected' or
                current[new_judgment_id]['effective_status'] != 'not_affected'):
            raise ValueError("Verification requires reviewed affected and new not_affected judgments")
        if not actor.strip() or not basis.strip():
            raise ValueError("Verification requires actor and fix-specific evidence explanation")
        with self.db:
            vid = self.put('verification', {'old_judgment_id': old_judgment_id,
                'new_judgment_id': new_judgment_id, 'actor': actor, 'basis': basis,
                'evidence_ids': new['evidence_ids'], 'created_at': now(),
                'method': 'manual-review-of-imported-rescan'})
            body = {k: v for k, v in new.items() if k not in ('id', 'kind')}
            body.update(proposed_status='fixed', justification=None, supersedes=new_judgment_id,
                        verification_id=vid, created_at=now())
            return self.put('judgment', body)

    def incident(self, release_id, event_type, aware_at, actor, basis,
                 corrective_at=None, notification_at=None):
        self.get(release_id, 'release')
        aware = instant(aware_at)
        if event_type not in ('actively_exploited_vulnerability', 'severe_incident'):
            raise ValueError("Unsupported incident type; KEV is a signal, not an incident type")
        if not actor.strip() or not basis.strip():
            raise ValueError("Record applicability basis and responsible actor")
        final = None
        if event_type == 'actively_exploited_vulnerability' and corrective_at:
            final = (instant(corrective_at) + timedelta(days=14)).isoformat()
        if event_type == 'severe_incident' and notification_at:
            n = instant(notification_at)
            if n < aware:
                raise ValueError("Notification cannot precede awareness")
            month = n.month % 12 + 1
            year = n.year + (n.month == 12)
            final = n.replace(year=year, month=month, day=min(n.day, calendar.monthrange(year, month)[1])).isoformat()
        with self.db:
            return self.put('incident', {'release_id': release_id, 'event_type': event_type,
                'aware_at': aware.isoformat(), 'actor': actor, 'basis': basis,
                'corrective_at': corrective_at, 'notification_at': notification_at,
                'deadlines': {'early_warning': (aware + timedelta(hours=24)).isoformat(),
                              'notification': (aware + timedelta(hours=72)).isoformat(), 'final': final},
                'judgment_snapshot': self.latest_judgments(release_id),
                'report_state': 'draft', 'created_at': now()})

    def snapshot(self):
        return {'schema': 'cra-workbench/v1', 'releases': self.all('release'),
                'judgments': [j for r in self.all('release') for j in self.latest_judgments(r['id'])],
                'history': self.all('judgment'), 'reviews': self.all('review'),
                'evidence': self.all('evidence'), 'packs': self.all('pack'),
                'incidents': self.all('incident'), 'verifications': self.all('verification'),
                'report_records': self.all('report_record')}

    def record_report(self, incident_id, stage, actor, receipt, submitted_at):
        incident = self.get(incident_id, 'incident')
        if stage not in ('early_warning', 'notification', 'final'):
            raise ValueError("Invalid report stage")
        if instant(submitted_at) < instant(incident['aware_at']):
            raise ValueError("Submission cannot precede awareness")
        if not actor.strip() or not receipt.strip():
            raise ValueError("Actor and external submission receipt are required")
        with self.db:
            return self.put('report_record', {'incident_id': incident_id, 'stage': stage,
                'actor': actor, 'receipt': receipt, 'submitted_at': submitted_at,
                'recorded_at': now(), 'source': 'manual-external-submission-record'})

    def export(self, destination):
        # Revalidate stored bytes and signatures, never trust a historical boolean.
        files = {}
        for p in self.all('pack'):
            for name, sha in {**p['files'], 'manifest.json': p['manifest_hash']}.items():
                row = self.db.execute('SELECT data FROM blobs WHERE hash=?', (sha,)).fetchone()
                if not row or digest(row[0]) != sha:
                    raise ValueError(f"Evidence corruption: {name}")
                if name.startswith('attestations/'):
                    verify_envelope(row[0], p['trusted_key'])
                files[f"sources/{p['id']}/{name}"] = row[0]
        snapshot = self.snapshot()
        files['workbench.json'] = encoded(snapshot)
        from .presentation import render
        files['index.html'] = render(snapshot).encode()
        files['README.txt'] = ('Internal review bundle. Historical signed source files are preserved. '
            'Current judgments are review records, not newly signed VEX. '
            'Raw tool outputs referenced by legacy attestations may not be bundled. '
            'Local actor names are declarations, not authenticated identities.').encode()
        root = Path(destination)
        root.mkdir(parents=True, exist_ok=False)
        for name, raw in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        (root / 'manifest.json').write_bytes(encoded({'schema': 'cra-review-bundle/v1',
            'files': {name: digest(raw) for name, raw in files.items()}}))
        return str(root)
