#!/usr/bin/env python3
"""
rescore-state-leg-by-party.py — apply party-default archetype scoring to
unrated state legislators (state senate + state house + state assembly +
delegates). Sibling to rescore-house-by-party.py.

This bulk-applies party-line patterns to ~5,000 state legislators that
haven't received individual evidence review. Confidence chip
'archetype_party_default' makes this clearly distinguishable from the
~200 individually-curated officials.

WHY THIS IS DEFENSIBLE: Per Adam's 2026-05-18 directive, silence on a
major issue is itself signal. State Democrats who never publicly opposed
their state party platform on these issues = score F per archetype. State
Republicans who never publicly opposed Trump-MAGA priorities = score T
on those they're expected to align with.

This is a directional signal, NOT individual evidence. The dispute form
on every profile page upgrades these to archetype_curated when a real
position is documented.

Run:
    python3 rescore-state-leg-by-party.py --dry-run
    python3 rescore-state-leg-by-party.py --apply
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
    # State Rs: lean MAGA-conservative but less uniformly than federal.
    # Default is maga_conservative_r minus the most-aggressive Ts on
    # economic_stewardship (state legs rarely vote on Fed audit / sound
    # money) and industry_capture (state legs typically don't take
    # Pentagon-audit positions).
    'state_r': {
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [N, N, N, N, N],  # state-leg silence on Fed issues = N not F
        'election_integrity':        [N, T, N, T, T],
        'foreign_policy_restraint':  [N, N, N, N, N],  # not their domain
        'industry_capture':          [N, N, N, T, N],  # only raw-milk/small-farm is state-relevant
    },
    # State Ds: uniform F across family + Christian liberty, less universal
    # on election_integrity (some state Ds support voter ID), neutral on FPR
    # + industry capture (not state-leg domain).
    'state_d': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [N, N, N, N, N],
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [N, N, N, N, N],
        'industry_capture':          [N, N, N, N, N],
    },
}

# State-leg office patterns (case-insensitive). Excludes "U.S. House" etc.
STATE_LEG_RE = re.compile(
    r'^(State\s+(Senate|House|Senator|Representative|Assembly|Assemblywoman|Assemblyman)|'
    r'Delegate|Assembly\s+(Member|Speaker)|Representative)\b',
    re.IGNORECASE)
# Anti-match for federal (false positives like "Representative" matching US House)
FEDERAL_RE = re.compile(r'^(U\.?S\.?|United States)\s+', re.IGNORECASE)


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    tally = Counter()
    skipped_already_curated = 0
    skipped_no_party = 0
    skipped_not_state_leg = 0

    for c in sc['candidates']:
        office = c.get('office') or ''
        if FEDERAL_RE.match(office):
            continue
        if not STATE_LEG_RE.match(office):
            skipped_not_state_leg += 1
            continue
        prof = c.setdefault('profile', {})
        conf = prof.get('confidence')
        if conf in ('archetype_curated',):
            skipped_already_curated += 1
            continue
        party = (c.get('party') or '').upper()
        if party == 'R':
            archetype_key = 'state_r'
        elif party == 'D':
            archetype_key = 'state_d'
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
                    f'State legislator bulk-scored via party-default archetype '
                    f'({archetype_key}). Score reflects RESOLUTE Citizen '
                    f'party-line patterns + silence-as-signal methodology, '
                    f'NOT individual evidence review. If you have evidence of '
                    f'this official\'s positions, please file a dispute below. '
                    f'Run: rescore-state-leg-by-party.py (2026-05-18).'
                )

    print('=== STATE LEG BULK PARTY-DEFAULT RESCORE ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    print(f'  skipped_already_curated: {skipped_already_curated}')
    print(f'  skipped_no_party: {skipped_no_party}')
    print(f'  skipped_not_state_leg (other office types): {skipped_not_state_leg}')

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
