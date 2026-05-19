#!/usr/bin/env python3
"""
apply-save-act-vote.py — apply SAVE Act (H.R. 22) vote to
election_integrity[1] (photo voter ID with citizenship verification).

VOTE:
  H.R. 22, Safeguard American Voter Eligibility Act
  House Roll Call 102, April 10, 2025: 220-208 (passed)
  Senate companion (S. 128) did NOT advance — no Senate vote to apply.

  Bill requires documentary proof of U.S. citizenship when registering
  to vote in federal elections; states must remove noncitizens from
  voter rolls.

MAPPING:
  Vote YEA = T on election_integrity[1] (photo voter ID with citizenship
              verification — proof-of-citizenship is exactly this)
  Vote NAY = F on same

NAMED DEMOCRAT DEFECTORS who voted YEA:
  - Jared Golden (ME)
  - Marie Gluesenkamp Perez (WA)
  - Henry Cuellar (TX)
  - Ed Case (HI)

All other Democrats voted NAY. All Republicans voted YEA.

Source:
  https://www.govtrack.us/congress/votes/119-2025/h102
  Search query returned named defectors above.
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

HOUSE_RE = re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE)

HOUSE_D_YEA = {
    ('jared golden', 'ME'),
    ('marie gluesenkamp perez', 'WA'),
    ('henry cuellar', 'TX'),
    ('ed case', 'HI'),
}


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
        if not HOUSE_RE.match(office):
            continue
        party = (c.get('party') or '').upper()
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if party == 'R':
            want = T
            label = 'R'
        elif party == 'D':
            want = T if key in HOUSE_D_YEA else F
            label = 'D_yea' if want else 'D_nay'
        else:
            tally['skipped'] += 1
            continue

        scores = c.setdefault('scores', {})
        ei = scores.get('election_integrity')
        if not isinstance(ei, list) or len(ei) < 2:
            tally['skipped_no_ei_array'] += 1
            continue

        before = ei[1]
        ei[1] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'SAVE Act' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on SAVE Act citizenship '
                f'verification for voter registration (H.R.22, 4/10/2025).').strip()

    print('=== SAVE ACT (H.R.22) VOTE APPLIED ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run.')


if __name__ == '__main__':
    main()
