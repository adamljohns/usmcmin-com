#!/usr/bin/env python3
"""
finalize-house-coverage-2026.py — Finalize coverage of the last 5 House
districts: DC delegate (Eleanor Holmes Norton), PR resident commissioner
(Pablo Hernandez Rivera), and explicit lame_duck flags for FL-2/11/16 retirees.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    updates = 0

    # 1. Eleanor Holmes Norton (DC delegate)
    for c in cands:
        if c.get('name') == 'Eleanor Holmes Norton' and c.get('state') == 'DC':
            c['candidacy_status'] = 'incumbent_seeking_reelection'
            if 'profile' not in c: c['profile'] = {}
            c['profile']['next_election'] = 2026
            c['profile']['next_election_type'] = 'primary'
            c['profile']['next_election_date'] = '2026-06-02'  # DC primary
            c['profile']['seat_up_next'] = True
            existing = c['profile'].get('confidence_note', '') or ''
            new = '2026-05-20 — DC non-voting delegate flagged as incumbent_seeking_reelection (perennial).'
            if new not in existing:
                c['profile']['confidence_note'] = (existing + (' · ' if existing else '') + new)
            updates += 1
            print(f'  UPDATED Eleanor Holmes Norton (DC delegate)')

    # 2. Pablo José Hernández Rivera (PR resident commissioner)
    for c in cands:
        if 'Hernández Rivera' in (c.get('name','') or '') or 'Hernandez Rivera' in (c.get('name','') or ''):
            if c.get('state') == 'PR':
                c['candidacy_status'] = 'incumbent_seeking_reelection'
                if 'profile' not in c: c['profile'] = {}
                c['profile']['next_election'] = 2028  # PR Resident Commissioner is 4-year term
                c['profile']['next_election_type'] = 'general'
                c['profile']['next_election_date'] = '2028-11-07'
                c['profile']['seat_up_next'] = False  # NOT up in 2026
                existing = c['profile'].get('confidence_note', '') or ''
                new = '2026-05-20 — PR Resident Commissioner: 4-year term, next up 2028 (not 2026).'
                if new not in existing:
                    c['profile']['confidence_note'] = (existing + (' · ' if existing else '') + new)
                updates += 1
                print(f'  UPDATED {c["name"]} (PR Resident Commissioner)')

    # 3. FL-2/11/16: Explicitly mark retirees as lame_duck (more precise than not_running)
    for retiree_slug in ['neal-dunn', 'daniel-webster', 'vern-buchanan']:
        for c in cands:
            if c.get('slug') == retiree_slug and c.get('state') == 'FL':
                c['candidacy_status'] = 'lame_duck'
                if 'profile' not in c: c['profile'] = {}
                c['profile']['next_election'] = 2026
                c['profile']['next_election_type'] = 'primary'
                c['profile']['seat_up_next'] = True
                existing = c['profile'].get('confidence_note', '') or ''
                new = '2026-05-20 — FL House retiree: candidacy_status upgraded not_running → lame_duck (more precise).'
                if new not in existing:
                    c['profile']['confidence_note'] = (existing + (' · ' if existing else '') + new)
                updates += 1
                print(f'  UPDATED {c["name"]} (FL retiree → lame_duck)')

    print(f'\n  {updates} record(s) updated')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()
