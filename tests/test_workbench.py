import base64
import json
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cra.core import Store, digest, encoded

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'poc/out/evidence-pack-c-vuln-app-0.1.0'
KEY = ROOT / 'poc/keys/dev-ed25519.pub.json'


class WorkbenchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.store = Store(self.root / 'store.db')
        self.release = self.store.import_pack(PACK, KEY)
        self.judgment = self.store.latest_judgments(self.release)[0]

    def tearDown(self):
        self.store.db.close()
        self.tmp.cleanup()

    def copy_pack(self):
        return Path(shutil.copytree(PACK, self.root / 'pack'))

    def test_real_go_and_c_roundtrip(self):
        go = self.store.import_pack(ROOT / 'poc/out/evidence-pack-go-vuln-app-0.1.0', KEY)
        self.assertEqual(len(self.store.latest_judgments(go)), 77)
        self.assertEqual(len(self.store.all('evidence')), 154)
        self.store.export(self.root / 'export')
        data = json.loads((self.root / 'export/workbench.json').read_text())
        self.assertEqual(len(data['judgments']), 78)
        manifest = json.loads((self.root / 'export/manifest.json').read_text())
        for name, sha in manifest['files'].items():
            self.assertEqual(digest((self.root / 'export' / name).read_bytes()), sha)

    def test_idempotent_import(self):
        self.assertEqual(self.store.import_pack(PACK, KEY), self.release)
        self.assertEqual(len(self.store.all('judgment')), 1)

    def test_review_reassessment_and_history(self):
        self.assertEqual(self.judgment['effective_status'], 'under_investigation')
        self.store.review(self.judgment['id'], 'approved', 'reviewer', 'Reviewed product evidence')
        self.assertEqual(self.store.latest_judgments(self.release)[0]['effective_status'], 'affected')
        new = self.store.reassess(self.judgment['id'], 'New advisory changes affected range')
        self.assertEqual(self.store.latest_judgments(self.release)[0]['id'], new)
        self.assertEqual(self.store.latest_judgments(self.release)[0]['effective_status'], 'under_investigation')
        self.assertEqual(len(self.store.all('judgment')), 2)
        with self.assertRaises(ValueError):
            self.store.review(self.judgment['id'], 'approved', 'reviewer', 'Old evidence')

    def test_rejection_does_not_publish(self):
        self.store.review(self.judgment['id'], 'rejected', 'reviewer', 'Insufficient analysis scope')
        self.assertEqual(self.store.latest_judgments(self.release)[0]['effective_status'], 'under_investigation')

    def test_immutable_history(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.db.execute("UPDATE objects SET body='{}'")
        self.store.db.rollback()

    def test_tamper_rejected_without_partial_import(self):
        p = self.copy_pack()
        (p / 'sbom.cdx.json').write_text('{}')
        with self.assertRaises(ValueError):
            self.store.import_pack(p, KEY)
        self.assertEqual(len(self.store.all('pack')), 1)

    def test_manifest_cannot_change_signed_status(self):
        p = self.copy_pack()
        m = json.loads((p / 'manifest.json').read_text())
        m['conclusions'][0]['status'] = 'not_affected'
        (p / 'manifest.json').write_bytes(encoded(m))
        with self.assertRaises(ValueError):
            self.store.import_pack(p, KEY)

    def test_signature_tamper_even_with_updated_manifest(self):
        p = self.copy_pack()
        name = next((p / 'attestations').glob('vex*')).relative_to(p).as_posix()
        env = json.loads((p / name).read_text())
        env['payload'] = base64.b64encode(b'{}').decode()
        raw = encoded(env)
        (p / name).write_bytes(raw)
        m = json.loads((p / 'manifest.json').read_text())
        m['files'][name] = digest(raw)
        (p / 'manifest.json').write_bytes(encoded(m))
        with self.assertRaises(InvalidSignature):
            self.store.import_pack(p, KEY)

    def test_path_escape_rejected(self):
        p = self.copy_pack()
        m = json.loads((p / 'manifest.json').read_text())
        m['files']['../outside'] = 'x'
        (p / 'manifest.json').write_bytes(encoded(m))
        with self.assertRaises(ValueError):
            self.store.import_pack(p, KEY)

    def test_export_rechecks_blobs(self):
        self.store.db.execute('DROP TRIGGER no_blob_update')
        self.store.db.execute("UPDATE blobs SET data=X'00'")
        self.store.db.commit()
        with self.assertRaises(ValueError):
            self.store.export(self.root / 'bad-export')
        self.assertFalse((self.root / 'bad-export').exists())

    def test_incident_clocks_and_frozen_judgments(self):
        identity = self.store.incident(self.release, 'actively_exploited_vulnerability',
            '2026-09-22T08:00:00+08:00', 'owner', 'Tabletop applicability assessment',
            corrective_at='2026-09-25T00:00:00Z')
        incident = self.store.get(identity)
        self.assertEqual(incident['deadlines']['early_warning'], '2026-09-23T00:00:00+00:00')
        self.assertEqual(incident['deadlines']['final'], '2026-10-09T00:00:00+00:00')
        self.store.review(self.judgment['id'], 'approved', 'reviewer', 'Reviewed')
        self.assertEqual(self.store.get(identity)['judgment_snapshot'][0]['effective_status'], 'under_investigation')

    def test_severe_incident_calendar_month(self):
        identity = self.store.incident(self.release, 'severe_incident', '2026-01-30T00:00:00Z',
            'owner', 'Tabletop', notification_at='2026-01-31T00:00:00Z')
        self.assertEqual(self.store.get(identity)['deadlines']['final'], '2026-02-28T00:00:00+00:00')

    def test_kev_not_incident_and_timezone_required(self):
        with self.assertRaises(ValueError):
            self.store.incident(self.release, 'KEV', '2026-01-30T00:00:00Z', 'owner', 'KEV')
        with self.assertRaises(ValueError):
            self.store.incident(self.release, 'severe_incident', '2026-01-30T00:00:00', 'owner', 'Evidence')

    def test_report_receipt_requires_existing_incident(self):
        with self.assertRaises(ValueError):
            self.store.record_report('unknown', 'final', 'owner', 'receipt', '2026-09-22T00:00:00Z')

    def test_same_artifact_cannot_be_fix(self):
        with self.assertRaises(ValueError):
            self.store.verify_fix(self.judgment['id'], self.judgment['id'], 'owner', 'claim')

    def test_fix_creates_new_candidate_preserving_old_release(self):
        # Synthetic domain fixture, never included in the measured demo.
        with self.store.db:
            release = self.store.put('release', {'product': 'c-vuln-app', 'version': '0.2.0',
                                               'artifact_sha256': 'fixture-new-artifact'})
            evidence = self.store.put('evidence', {'release_id': release, 'data_kind': 'fixture'})
            new = self.store.put('judgment', {'release_id': release,
                'vulnerability': self.judgment['vulnerability'], 'proposed_status': 'not_affected',
                'justification': 'vulnerable_code_not_present', 'evidence_ids': [evidence],
                'supersedes': None})
        self.store.review(self.judgment['id'], 'approved', 'owner', 'Old affected version')
        self.store.review(new, 'approved', 'owner', 'New patched build verified')
        fixed = self.store.verify_fix(self.judgment['id'], new, 'owner', 'Reviewed actual fix and rescan')
        self.assertEqual(self.store.latest_judgments(release)[0]['effective_status'], 'under_investigation')
        self.store.review(fixed, 'approved', 'owner', 'Approve verified fix')
        self.assertEqual(self.store.latest_judgments(release)[0]['effective_status'], 'fixed')
        self.assertEqual(self.store.latest_judgments(self.release)[0]['effective_status'], 'affected')

    def test_new_input_snapshot_invalidates_previous_approval(self):
        self.store.review(self.judgment['id'], 'approved', 'owner', 'Reviewed')
        p = self.copy_pack()
        manifest = json.loads((p / 'manifest.json').read_text())
        manifest['exported_at'] = '2026-09-22T00:00:00Z'
        (p / 'manifest.json').write_bytes(encoded(manifest))
        self.store.import_pack(p, KEY)
        current = self.store.latest_judgments(self.release)
        self.assertEqual(len(current), 1)
        self.assertEqual(current[0]['supersedes'], self.judgment['id'])
        self.assertEqual(current[0]['effective_status'], 'under_investigation')

    def test_render_escapes_operator_input(self):
        from cra.presentation import render
        self.store.review(self.judgment['id'], 'approved', '<script>alert(1)</script>', 'Reviewed')
        html = render(self.store.snapshot())
        self.assertNotIn('<script>', html)
        self.assertIn('&lt;script&gt;', html)

    def test_output_not_overwritten(self):
        self.store.export(self.root / 'export')
        with self.assertRaises(FileExistsError):
            self.store.export(self.root / 'export')


if __name__ == '__main__':
    unittest.main()
