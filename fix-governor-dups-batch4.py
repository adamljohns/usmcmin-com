#!/usr/bin/env python3
"""
fix-governor-dups-batch4.py — Merge 8 more duplicate incumbent governor records
(from Gov batch 4) + correct two term-limited/retiring governors.

Same pattern as fix-governor-incumbent-dups.py: keep the record with more
curated scores, carry over the richer office text + 2026 status, drop the other.

Also fixes:
  - Gretchen Whitmer (MI): term-limited 2026 → lame_duck
  - Tony Evers (WI): announced not seeking 3rd term → lame_duck
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

PAIRS = [
    ('joe-lombardo',           'joe-lombardo-gov-2026',           'NV'),
    ('sarah-huckabee-sanders', 'sarah-huckabee-sanders-gov-2026', 'AR'),
    ('josh-green',             'josh-green-gov-2026',             'HI'),
    ('kathy-hochul',           'kathy-hochul-gov-2026',           'NY'),
    ('daniel-mckee',           'daniel-mckee-gov-2026',           'RI'),
    ('larry-rhoden',           'larry-rhoden-gov-2026',           'SD'),
    ('brad-little',            'brad-little-gov-2026',            'ID'),
    ('jb-pritzker',            'jb-pritzker-gov-2026',            'IL'),
]

# (state, slug, new_status, note) — term-limited / retiring governors
STATUS_FIXES = [
    ('MI', 'gretchen-whitmer', 'lame_duck',
     'Term-limited 2026 (MI 2-term limit; won 2018 + 2022). Not seeking reelection.'),
    ('WI', 'tony-evers', 'lame_duck',
     'Announced 2025 he will not seek a 3rd term. Not on 2026 ballot.'),
]


def count_scores(rec):
    return sum(1 for cat in rec.get('scores', {}).values() for v in cat if v is not None)


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    print(f'Before: {len(cands)} candidates')

    to_drop = set()
    merges = 0
    for existing_slug, new_slug, state in PAIRS:
        existing = next((c for c in cands if c.get('state')==state and c.get('slug')==existing_slug), None)
        new = next((c for c in cands if c.get('state')==state and c.get('slug')==new_slug), None)
        if not existing or not new:
            print(f'  SKIP {existing_slug}/{new_slug} ({state}): pair incomplete')
            continue
        e_n, n_n = count_scores(existing), count_scores(new)
        if e_n >= n_n:
            # keep existing, carry over office/status/notes from new
            existing['office'] = new['office']
            existing['candidacy_status'] = new.get('candidacy_status') or existing.get('candidacy_status')
            existing['notes'] = new.get('notes') or existing.get('notes')
            if 'profile' not in existing: existing['profile'] = {}
            for k in ('next_election','next_election_type','seat_up_next','next_election_date'):
                if new.get('profile', {}).get(k) is not None:
                    existing['profile'][k] = new['profile'][k]
            # merge sources
            existing['sources'] = list(dict.fromkeys((existing.get('sources') or []) + (new.get('sources') or [])))
            to_drop.add((state, new_slug))
            print(f'  {state}: kept existing ({existing_slug}, {e_n} scores), dropped {new_slug} ({n_n})')
        else:
            # keep new, carry over photo/website/sources from existing
            for k in ('photo','website'):
                if existing.get(k) and not new.get(k):
                    new[k] = existing[k]
            new['sources'] = list(dict.fromkeys((new.get('sources') or []) + (existing.get('sources') or [])))
            to_drop.add((state, existing_slug))
            print(f'  {state}: kept new ({new_slug}, {n_n} scores), dropped {existing_slug} ({e_n})')
        merges += 1

    cands = [c for c in cands if (c.get('state'), c.get('slug')) not in to_drop]

    # Apply status fixes
    fixes = 0
    for state, slug, new_status, note in STATUS_FIXES:
        target = next((c for c in cands if c.get('state')==state and c.get('slug')==slug), None)
        if not target:
            print(f'  STATUS-FIX SKIP {state}/{slug}: not found')
            continue
        target['candidacy_status'] = new_status
        if 'profile' not in target: target['profile'] = {}
        existing_note = target['profile'].get('confidence_note', '') or ''
        new_note = f'2026-05-20 — {note}'
        if new_note not in existing_note:
            target['profile']['confidence_note'] = existing_note + (' · ' if existing_note else '') + new_note
        print(f'  STATUS-FIX {target["name"]} ({state}) → {new_status}')
        fixes += 1

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {merges} merges, {fixes} status fixes')
    print(f'  After: {len(cands)} candidates')


if __name__ == '__main__':
    main()
