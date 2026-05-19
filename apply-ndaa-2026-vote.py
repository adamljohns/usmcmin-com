#!/usr/bin/env python3
"""
apply-ndaa-2026-vote.py — apply NDAA FY26 House vote to
foreign_policy_restraint[1] (withdrawal from forever wars + repeal AUMFs).

VOTE: H.R. 5371 / S.1071, FY2026 National Defense Authorization Act.
  House Roll Call 320 (Dec 10, 2025): 312-112 (Republicans 197-18,
    Democrats 115-94)
  Senate (Dec 11, 2025): 75-22 conference report

  $900B defense authorization. Includes $400M Ukraine Security
  Assistance Initiative + Europe troop level restrictions + AUMF
  reauthorizations.

MAPPING:
  Vote YEA = F on FPR[1] (you voted to FUND continued forever-war
              posture + Ukraine ops + AUMF reauthorization)
  Vote NAY = T on FPR[1] (you voted against the defense-funding bill)

APPLICATION SCOPE — only HOUSE REPUBLICANS:
  - 18 named R defectors → T on FPR[1]
  - All other R reps → F on FPR[1]
  - Democrats SKIPPED — House Ds split 115-94 and we don't have the
    named list to apply per-member. The Iran war powers vote already
    set Ds to T on FPR[1]; an unconditional NDAA-YEA flip to F would
    be incorrect for the 94 D NAY voters.
  - Senate: archetype already covers this (all GOP voted YEA, mostly D
    voted YEA except the bloc that voted NAY on Israel/Ukraine
    specifically). Skip for now to avoid mis-applying.

Source: https://www.newsweek.com/full-list-republicans-voting-against-trump-backed-ndaa-11190648
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

HOUSE_RE = re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE)

# 18 House R who voted NAY on NDAA FY26 final passage (12/10/2025)
HOUSE_R_NAY = {
    ('andy biggs', 'AZ'),
    ('lauren boebert', 'CO'),
    ('josh brecheen', 'OK'),
    ('tim burchett', 'TN'),
    ('eric burlison', 'MO'),
    ('eli crane', 'AZ'),
    ('warren davidson', 'OH'),
    ('byron donalds', 'FL'),
    ('paul gosar', 'AZ'),
    ('marjorie taylor greene', 'GA'),
    ('morgan griffith', 'VA'),
    ('andy harris', 'MD'),
    ('anna paulina luna', 'FL'),
    ('thomas massie', 'KY'),
    ('john rose', 'TN'),
    ('chip roy', 'TX'),
    ('keith self', 'TX'),
    ('greg steube', 'FL'),
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
        # Only apply to Republicans (D vote split — would be mis-applied)
        if party != 'R':
            tally['skipped_not_R'] += 1
            continue
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if key in HOUSE_R_NAY:
            want = T   # voted NAY = restraint position
            label = 'R_nay'
        else:
            want = F   # voted YEA with party = funded defense complex
            label = 'R_yea'

        scores = c.setdefault('scores', {})
        fpr = scores.get('foreign_policy_restraint')
        if not isinstance(fpr, list) or len(fpr) < 2:
            tally['skipped_no_fpr_array'] += 1
            continue

        before = fpr[1]
        fpr[1] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'NDAA FY26' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"NAY" if want else "YEA"} on NDAA FY26 (HR5371/S1071, '
                f'12/10/2025) — $900B defense + $400M Ukraine + Europe '
                f'troop limits.').strip()

    print('=== NDAA FY26 VOTE APPLIED (House Republicans) ===')
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
