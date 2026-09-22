"""Read-only teaching projection; this is NOT the runtime VA-IR or an Agent."""
import hashlib
import json


def build_case(store, root):
    snapshot = store.snapshot()
    evidence = next(e for e in snapshot['evidence'] if
        e['predicate']['conclusion_type'] == 'reachability' and
        e['predicate']['vulnerability']['id'] == 'CVE-2022-37434')
    release = store.get(evidence['release_id'], 'release')
    pack = store.get(evidence['pack_id'], 'pack')
    sbom_hash = pack['files']['sbom.cdx.json']
    sbom_bytes = store.db.execute('SELECT data FROM blobs WHERE hash=?', (sbom_hash,)).fetchone()[0]
    assert hashlib.sha256(sbom_bytes).hexdigest() == sbom_hash
    sbom = json.loads(sbom_bytes)
    component = next(c for c in sbom['components'] if c['name'] == 'zlib')
    raw = (root / 'poc/curation/vuln-function-map.json').read_bytes()
    curation = json.loads(raw)
    mapping = next(m for m in curation['mappings'] if m['vuln_id'] == 'CVE-2022-37434')
    trace = next(e for e in evidence['predicate']['evidence'] if e['kind'] == 'call-path')
    symbol = mapping['functions'][0]
    assert trace['hops'][-1]['function'] == symbol['name']
    source_file = root / 'poc/examples/c-vuln-app' / symbol['file']
    return {
        'mode': 'read-only-design-projection',
        'subject': {'product': release['product'], 'version': release['version'],
            'artifact_sha256': release['artifact_sha256'], 'component': component['purl'],
            'vulnerability': mapping['vuln_id'], 'context': 'historical Joern graph / entry main'},
        'observations': {
            'component': {'name': component['name'], 'version': component['version'],
                'sbom_hash': sbom_hash, 'method': 'historical SBOM with manual vendored-component augmentation'},
            'localization': {'symbol': symbol['name'], 'file': symbol['file'],
                'method': 'manual curation; NOT automated localization',
                'curation_sha256': hashlib.sha256(raw).hexdigest(),
                'current_source_sha256': hashlib.sha256(source_file.read_bytes()).hexdigest(),
                'fix_commit_references': mapping['osv_range']['fixed_commits'],
                'code_region': 'EXTRA branch mentioned in curation; no branch reachability proof'},
            'reachability': {'evidence_id': evidence['id'], 'legacy_conclusion_id': evidence['legacy_id'],
                'tool': evidence['predicate']['tool']['name'],
                'path': [h['function'] for h in trace['hops']],
                'locations': [f"{h['defined_in']}:{h['defined_line']}" for h in trace['hops']],
                'scope': 'historical graph; direct structural path'},
        },
        'claims': [
            {'id': 'demo-claim-reachability', 'type': 'structural_reachability',
             'assertion': 'reachable_in_recorded_graph',
             'supporting_evidence': [evidence['id']], 'counter_evidence': [],
             'counter_evidence_note': 'not evaluated exhaustively',
             'unknowns': ['current source-to-historical-artifact binding', 'vulnerable branch execution'],
             'sufficiency': 'supports recorded structural path only',
             'validity': 'historical_snapshot_only', 'review': 'not_performed',
             'policy': 'illustration-only/v0'},
            {'id': 'demo-claim-exploitability', 'type': 'exploitability', 'assertion': 'unknown',
             'supporting_evidence': [], 'counter_evidence': [],
             'unknowns': ['attacker-controlled input', 'FEXTRA precondition',
                          'runtime configuration', 'mitigations'],
             'sufficiency': 'insufficient', 'review': 'not_performed', 'policy': 'illustration-only/v0'},
        ],
        'decision': {'status': 'not_evaluated', 'reason': 'No Decision Engine executed; do not infer an approved VEX'},
        'planner_trace': [
            {'round': 0, 'gap': 'CVE not yet bound to symbol', 'proposed_pass': 'Localization',
             'input': 'manual mapping + source identity', 'result': 'inflate candidate with provenance',
             'mode': 'scripted-design-walkthrough'},
            {'round': 1, 'gap': 'No structural path in assessment', 'proposed_pass': 'Reachability',
             'input': 'recorded Joern graph / entry main', 'result': 'import existing main → gunzip_file → inflate evidence',
             'mode': 'scripted-design-walkthrough'},
            {'round': 2, 'gap': 'Input and vulnerable branch conditions unresolved', 'proposed_pass': 'Dataflow / Runtime',
             'input': 'provider unavailable in this demo', 'result': 'stop with unknown + needs_review',
             'mode': 'scripted-design-walkthrough'},
        ],
    }


# This miniature dependency example illustrates propagation; it is not wired to Store.reassess().
DEPENDENCIES = {
    'source_snapshot': [],
    'component_inventory': [],
    'advisory_snapshot': [],
    'association_claim': ['component_inventory', 'advisory_snapshot'],
    'localization_claim': ['source_snapshot', 'advisory_snapshot'],
    'codegraph_snapshot': ['source_snapshot'],
    'reachability_claim': ['localization_claim', 'codegraph_snapshot'],
    'decision': ['association_claim', 'reachability_claim'],
    'vex_projection': ['decision'],
}


def illustrate_invalidation(changed):
    if changed not in DEPENDENCIES:
        raise ValueError('Unknown design node')
    stale = {changed}
    while True:
        updated = stale | {node for node, inputs in DEPENDENCIES.items() if set(inputs) & stale}
        if updated == stale:
            break
        stale = updated
    return {'mode': 'synthetic-dependency-example', 'changed': changed,
            'dependencies': DEPENDENCIES,
            'stale': sorted(stale - {changed}),
            'unaffected': sorted(set(DEPENDENCIES) - stale),
            'note': 'source-only change; SBOM/advisory snapshots held fixed in this example'}
