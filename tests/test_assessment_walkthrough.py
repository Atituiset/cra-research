"""Check that teaching examples preserve the boundary between observations and claims."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from cra.core import Store

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('assessment_walkthrough', ROOT / 'demo/assessment_walkthrough.py')
walkthrough = importlib.util.module_from_spec(spec)
spec.loader.exec_module(walkthrough)


class WalkthroughTest(unittest.TestCase):
    def test_projection_reads_real_evidence_without_publishing_decisions(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp) / 'store.db')
            try:
                store.import_pack(ROOT / 'poc/out/evidence-pack-c-vuln-app-0.1.0',
                                  ROOT / 'poc/keys/dev-ed25519.pub.json')
                before = store.snapshot()
                case = walkthrough.build_case(store, ROOT)
                self.assertEqual(case['observations']['reachability']['path'], ['main', 'gunzip_file', 'inflate'])
                self.assertEqual(case['claims'][1]['assertion'], 'unknown')
                self.assertEqual(case['decision']['status'], 'not_evaluated')
                evidence_ids = {e['id'] for e in before['evidence']}
                self.assertTrue(set(case['claims'][0]['supporting_evidence']) <= evidence_ids)
                self.assertEqual(before, store.snapshot())
            finally:
                store.db.close()

    def test_invalidation_propagates_only_to_dependents(self):
        example = walkthrough.illustrate_invalidation('source_snapshot')
        self.assertEqual(set(example['stale']), {
            'localization_claim', 'codegraph_snapshot', 'reachability_claim', 'decision', 'vex_projection'})
        self.assertEqual(set(example['unaffected']), {
            'component_inventory', 'advisory_snapshot', 'association_claim'})
        self.assertEqual(walkthrough.illustrate_invalidation('vex_projection')['stale'], [])


if __name__ == '__main__':
    unittest.main()
