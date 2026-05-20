#!/usr/bin/env python3
"""
update-tx18-menefee.py — Flag Christian Menefee as 2025 special winner + 2026 incumbent.

Sylvester Turner (TX-18) died March 2025; Christian Menefee won the 2025 special.
This script updates his existing record to reflect his successor status + 2026
reelection candidacy.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    updated = 0
    for c in cands:
        if c.get('name') == 'Christian Menefee' and c.get('state') == 'TX' and c.get('district') == 18:
            c['office'] = (
                'U.S. Representative TX-18 (D incumbent · won 2025 special after Sylvester Turner death · '
                'former Harris County Attorney · 2026 reelection candidate)'
            )
            c['status'] = 'active'
            c['candidacy_status'] = 'incumbent_seeking_reelection'
            c['notes'] = (
                'D incumbent U.S. Representative TX-18 (Houston). Won 2025 special election '
                'after Sylvester Turner death (March 2025). Former Harris County Attorney '
                '(2021-2025). Civil rights attorney. Seeking 2026 reelection.'
            )
            if 'profile' not in c: c['profile'] = {}
            c['profile']['next_election'] = 2026
            c['profile']['next_election_type'] = 'primary'
            c['profile']['next_election_date'] = '2026-03-03'  # TX primary
            c['profile']['seat_up_next'] = True
            c['profile']['confidence'] = c['profile'].get('confidence') or 'medium'
            c['profile']['confidence_note'] = (
                '2026-05-20 — Updated to reflect 2025 special election win + 2026 reelection candidacy.'
            )
            existing_sources = c.get('sources', []) or []
            for s in ['https://ballotpedia.org/Christian_Menefee',
                      'https://ballotpedia.org/Texas%27_18th_Congressional_District']:
                if s not in existing_sources:
                    existing_sources.append(s)
            c['sources'] = existing_sources
            updated += 1
            print(f'  UPDATED Christian Menefee (TX-18)')

    if not updated:
        print('  WARNING: no matching Menefee record found')
        return

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {updated} record(s) updated')


if __name__ == '__main__':
    main()
