#!/usr/bin/env python3
"""
rescore-house-by-party.py — apply party-default archetype scoring to all
unrated US House members (the ones not covered by rescore-top-50-federal.py
or rescore-federal-expanded.py).

Justification per Adam's 2026-05-18 directive: silence on a major issue
is itself a score. A House Democrat who never publicly opposed CBDC = F
on economic_stewardship[q0]; a House Republican who never publicly opposed
WEF/ESG capture = N (we don't assume F on the affirmative-Republican side
because the question is asymmetric — Rs typically DO oppose by default).

Default archetype assignment by party:
  R   → maga_conservative_r   (current House R caucus is overwhelmingly
                                Trump-aligned post-2024; the establishment-R
                                bench is largely Senate-side)
  D   → establishment_d        (uniform F across all 6 new categories per
                                D party-line voting record)
  I   → no default applied (independents need individual review)

Only fills nulls. Marks profile.confidence as 'archetype_party_default'
to distinguish from the higher-trust 'archetype_curated' label.

Run:
    python3 rescore-house-by-party.py --dry-run
    python3 rescore-house-by-party.py --apply
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False
N = None

ARCHETYPES = {
    'maga_conservative_r': {
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, T, N, T],
        'election_integrity':        [N, T, N, T, T],
        'foreign_policy_restraint':  [N, N, N, F, N],
        'industry_capture':          [N, N, N, T, N],
    },
    'establishment_d': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, F, F],
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    },
}

HOUSE_RE = re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE)


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    tally = Counter()
    skipped_already_curated = 0
    skipped_no_party = 0

    for c in sc['candidates']:
        office = c.get('office') or ''
        if not HOUSE_RE.match(office):
            continue
        # Only touch candidates not already individually curated
        prof = c.setdefault('profile', {})
        conf = prof.get('confidence')
        if conf == 'archetype_curated':
            skipped_already_curated += 1
            continue
        party = (c.get('party') or '').upper()
        if party == 'R':
            archetype_key = 'maga_conservative_r'
        elif party == 'D':
            archetype_key = 'establishment_d'
        else:
            skipped_no_party += 1
            continue

        archetype = ARCHETYPES[archetype_key]
        scores = c.setdefault('scores', {})
        cells_set = 0
        for cat_id, pattern in archetype.items():
            arr = scores.get(cat_id)
            if not isinstance(arr, list):
                continue
            for i, want in enumerate(pattern):
                if i >= len(arr): break
                if want is None: continue
                if arr[i] is None:
                    arr[i] = want
                    cells_set += 1

        if cells_set > 0:
            tally[f'{archetype_key}'] += 1
            tally['cells_filled'] += cells_set
            if conf in (None, 'party_default'):
                prof['confidence'] = 'archetype_party_default'
                prof['confidence_note'] = (
                    f'US House member bulk-scored via party-default archetype '
                    f'({archetype_key}). Per RESOLUTE Citizen methodology, '
                    f'silence on a major v4.0 issue is itself signal — a '
                    f'House member who has not publicly opposed a major '
                    f'issue is scored False on the affirmative-action '
                    f'question. Individual evidence review is pending; when '
                    f'specific votes/statements get promoted via apply-claims.py, '
                    f'this confidence will upgrade to archetype_curated. '
                    f'Run: rescore-house-by-party.py (2026-05-18).'
                )

    print('=== HOUSE BULK PARTY-DEFAULT RESCORE ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    print(f'  skipped_already_curated: {skipped_already_curated}')
    print(f'  skipped_no_party: {skipped_no_party}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
        print('Next: python3 build-data.py && python3 generate-profiles.py && python3 build-search-index.py')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()
