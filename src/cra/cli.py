"""Local single-operator workbench commands."""
import argparse
import json
from cryptography.exceptions import InvalidSignature
from .core import Store


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', default='var/cra.db')
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('import-pack')
    p.add_argument('directory')
    p.add_argument('--key', required=True, help='Explicitly trusted Ed25519 public key JSON')
    commands.add_parser('snapshot')
    p = commands.add_parser('review')
    p.add_argument('judgment_id')
    p.add_argument('--decision', choices=['approved', 'rejected'], required=True)
    p.add_argument('--actor', required=True)
    p.add_argument('--reason', required=True)
    p = commands.add_parser('reassess')
    p.add_argument('judgment_id')
    p.add_argument('--reason', required=True)
    p = commands.add_parser('incident')
    p.add_argument('release_id')
    p.add_argument('--event-type', required=True,
        choices=['actively_exploited_vulnerability', 'severe_incident'])
    p.add_argument('--aware-at', required=True)
    p.add_argument('--actor', required=True)
    p.add_argument('--basis', required=True)
    p.add_argument('--corrective-at')
    p.add_argument('--notification-at')
    p = commands.add_parser('export')
    p.add_argument('destination', help='New directory; existing output is never overwritten')
    p = commands.add_parser('verify-fix')
    p.add_argument('old_judgment_id')
    p.add_argument('new_judgment_id')
    p.add_argument('--actor', required=True)
    p.add_argument('--basis', required=True)
    p = commands.add_parser('record-report')
    p.add_argument('incident_id')
    p.add_argument('--stage', choices=['early_warning', 'notification', 'final'], required=True)
    p.add_argument('--actor', required=True)
    p.add_argument('--receipt', required=True)
    p.add_argument('--submitted-at', required=True)
    args = parser.parse_args()
    store = Store(args.db)
    try:
        if args.command == 'import-pack':
            result = store.import_pack(args.directory, args.key)
        elif args.command == 'snapshot':
            result = store.snapshot()
        elif args.command == 'review':
            result = store.review(args.judgment_id, args.decision, args.actor, args.reason)
        elif args.command == 'reassess':
            result = store.reassess(args.judgment_id, args.reason)
        elif args.command == 'incident':
            result = store.incident(args.release_id, args.event_type, args.aware_at,
                args.actor, args.basis, args.corrective_at, args.notification_at)
        elif args.command == 'verify-fix':
            result = store.verify_fix(args.old_judgment_id, args.new_judgment_id, args.actor, args.basis)
        elif args.command == 'record-report':
            result = store.record_report(args.incident_id, args.stage, args.actor,
                                         args.receipt, args.submitted_at)
        else:
            result = store.export(args.destination)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, InvalidSignature) as exc:
        parser.exit(1, f'cra: {exc}\n')
    finally:
        store.db.close()


if __name__ == '__main__':
    main()
