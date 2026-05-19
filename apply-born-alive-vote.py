#!/usr/bin/env python3
"""
apply-born-alive-vote.py — apply Born-Alive Abortion Survivors Protection
Act votes to sanctity_of_life[0] (life begins at conception / personhood
from conception).

VOTES:
  House (H.R. 21, Roll Call 27, Jan 23 2025): 217-204
    YEA: all 217 Republicans + 1 Democrat (Henry Cuellar, TX)
    NAY: 204 Democrats
    PRESENT: Vicente Gonzalez (D-TX) — treated as no-change
  Senate (S. 6 cloture, Jan 22-24 2025): 52-47 FAILED
    YEA on cloture: 52 Republicans
    NAY on cloture: 47 Democrats (all Democrats voted against advancing)

MAPPING JUSTIFICATION:
  The Born-Alive Act requires medical care for infants who survive an
  abortion attempt. Voting YEA is the legislative expression of full
  personhood at birth and (by implication) from conception. Voting NAY
  rejects that personhood claim. The question text for sanctity_of_life[0]
  is: "Candidate affirms life begins at conception and personhood from
  conception." Born-Alive vote maps directly to this question.

  This OVERWRITES existing values on House + Senate members because
  we have ground-truth evidence.

Sources:
  https://www.newsweek.com/democrat-henry-cuellar-born-alive-act-2020047
  https://thehill.com/homenews/5103299-house-gop-born-alive-abortion/
  https://www.govtrack.us/congress/votes/119-2025/h27
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

CHAMBER_RE = {
    'senate': re.compile(r'^(U\.?S\.?|United States)\s+Senator', re.IGNORECASE),
    'house':  re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE),
}

# Only one House Democrat voted YEA — Henry Cuellar (TX-28).
HOUSE_D_YEA = {('henry cuellar', 'TX')}
# One House Democrat voted PRESENT — treated as no-evidence (skip update).
HOUSE_D_PRESENT = {('vicente gonzalez', 'TX')}


def norm(name):
    s = (name or '').lower().strip()
    s = re.sub(r'\.+', '', s)
    s = re.sub(r'\s+(jr|sr|ii|iii|iv)$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    tally = Counter()

    for c in sc['candidates']:
        office = c.get('office') or ''
        is_senate = bool(CHAMBER_RE['senate'].match(office))
        is_house = bool(CHAMBER_RE['house'].match(office))
        if not (is_senate or is_house):
            continue
        party = (c.get('party') or '').upper()
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if is_house and key in HOUSE_D_PRESENT:
            # Skip — voted present, no clear evidence either way
            tally['hse_present_skipped'] += 1
            continue

        if is_senate:
            if party == 'R':
                want = T  # all R voted YEA on cloture
                label = 'sen_R'
            elif party == 'D':
                want = F  # all D voted NAY on cloture
                label = 'sen_D'
            elif party == 'I':
                # Sanders + King — voted NAY on cloture
                want = F
                label = 'sen_I'
            else:
                tally['sen_skipped'] += 1
                continue
        else:  # House
            if party == 'R':
                want = T  # all R voted YEA
                label = 'hse_R'
            elif party == 'D':
                want = T if key in HOUSE_D_YEA else F  # Cuellar only D YEA
                label = 'hse_D_yea' if want else 'hse_D_nay'
            else:
                tally['hse_skipped'] += 1
                continue

        scores = c.setdefault('scores', {})
        sol = scores.get('sanctity_of_life')
        if not isinstance(sol, list) or len(sol) < 1:
            tally['skipped_no_sol_array'] += 1
            continue

        before = sol[0]
        sol[0] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Born-Alive' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on Born-Alive Abortion Survivors '
                f'Protection Act (H.R.21/S.6, Jan 2025).').strip()

    print('=== BORN-ALIVE ACT VOTE APPLIED ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()
