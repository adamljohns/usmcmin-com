#!/usr/bin/env python3
"""
fix-governor-incumbent-dups.py — Merge duplicate incumbent governor records.

When batch3 inserted -gov-2026-suffixed records for sitting governors,
it created duplicates with the older single-slug records. This script
merges them: keep the record with more curated scores, but carry over
the new office text + candidacy_status from the 2026 record.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# (existing-slug, new-slug) pairs for incumbents to merge
PAIRS = [
    ('tim-walz',          'tim-walz-gov-2026',          'MN'),
    ('maura-healey',      'maura-healey-gov-2026',      'MA'),
    ('wes-moore',         'wes-moore-gov-2026',         'MD'),
    ('ned-lamont',        'ned-lamont-gov-2026',        'CT'),
    ('kelly-ayotte',      'kelly-ayotte-gov-2026',      'NH'),
    ('phil-scott',        'phil-scott-gov-2026',        'VT'),
    ('josh-shapiro',      'josh-shapiro-gov-2026',      'PA'),
    ('jim-pillen',        'jim-pillen-gov-2026',        'NE'),
    ('tina-kotek',        'tina-kotek-gov-2026',        'OR'),
    ('katie-hobbs',       'katie-hobbs-gov-2026',       'AZ'),
]

# Paul LePage: ME-02 House record was bogus (he is actually running for ME Gov)
# — delete the ME-02 record entirely, keep the -gov-2026 record
DELETE_BOGUS = [
    ('paul-lepage', 'ME'),
]


def count_nonzero_scores(rec):
    """Count answered (non-None) cells in scores."""
    return sum(1 for cat in rec.get('scores', {}).values() for v in cat if v is not None)


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    print(f'Before: {len(cands)} candidates')

    deletions = merges = 0
    new_cands = []
    pair_map = {}
    for existing_slug, new_slug, state in PAIRS:
        pair_map[(state, new_slug)] = ('new', existing_slug)
        pair_map[(state, existing_slug)] = ('existing', new_slug)

    # First pass: find pairs + decide who wins
    decisions = {}  # state -> {keep_slug, drop_slug, merged_fields}
    for existing_slug, new_slug, state in PAIRS:
        existing = next((c for c in cands if c.get('state')==state and c.get('slug')==existing_slug), None)
        new = next((c for c in cands if c.get('state')==state and c.get('slug')==new_slug), None)
        if not existing or not new:
            print(f'  SKIP {existing_slug} / {new_slug} ({state}): pair incomplete')
            continue
        existing_score_n = count_nonzero_scores(existing)
        new_score_n = count_nonzero_scores(new)
        if existing_score_n >= new_score_n:
            # Keep existing, drop new — but carry over office, candidacy_status, notes
            existing['office'] = new['office']
            existing['candidacy_status'] = new['candidacy_status']
            existing['notes'] = new['notes']
            # Merge confidence_note (append)
            old_note = existing.get('profile', {}).get('confidence_note', '')
            new_note = new.get('profile', {}).get('confidence_note', '')
            if 'profile' not in existing: existing['profile'] = {}
            existing['profile']['confidence_note'] = (
                old_note + ' · ' + new_note if old_note else new_note
            )
            existing['profile']['next_election'] = 2026
            existing['profile']['next_election_type'] = 'primary'
            existing['profile']['seat_up_next'] = True
            existing['profile']['next_election_date'] = new['profile'].get('next_election_date', '')
            decisions[state] = (existing_slug, new_slug, 'kept-existing')
        else:
            # Keep new (more scored), drop existing — but carry over photo/website/sources if present
            for key in ('photo','website'):
                if existing.get(key) and not new.get(key):
                    new[key] = existing[key]
            # Merge sources
            existing_sources = existing.get('sources', []) or []
            new_sources = new.get('sources', []) or []
            new['sources'] = list(dict.fromkeys(new_sources + existing_sources))
            decisions[state] = (new_slug, existing_slug, 'kept-new')
        print(f'  {state}: {decisions[state][2]} (existing={existing_score_n}, new={new_score_n})')

    # Build new candidates list dropping the loser of each pair
    to_drop = set()
    for state, (keep_slug, drop_slug, _) in decisions.items():
        to_drop.add((state, drop_slug))
        merges += 1
    for slug, state in DELETE_BOGUS:
        to_drop.add((state, slug))
        deletions += 1

    new_cands = [c for c in cands if (c.get('state'), c.get('slug')) not in to_drop]

    print(f'\n  {merges} merges, {deletions} bogus-deletions')
    print(f'  {len(cands)} → {len(new_cands)} candidates (-{len(cands)-len(new_cands)})')

    data['candidates'] = new_cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()
