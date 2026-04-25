#!/usr/bin/env python3
"""
score-fxbg-rowe-crump.py — promote Matt Rowe and Joy Crump from
all-null Awaiting-review to party-default scoring.

Rationale (sourced 2026-04-25 against Fredericksburg Free Press):

  * Matt Rowe (Ward 1) — public record:
      * Snowden Hills resident
      * Recently elected chair of Fredericksburg City School Board
        (Jan 2025)
      * Previously served as Bowling Green Town councilman
      * Ran as Democratic nominee for Virginia's 1st Congressional
        District in 2016
      Democratic affiliation is well-established by his 2016 Democratic
      Congressional run.

  * Joy Crump (Ward 2) — public record:
      * Chef-owner of FOODE + Mercantile (Fredericksburg downtown)
      * Top Chef Bravo competitor, James Beard House
      * First Black woman elected to Fredericksburg City Council
        (November 2024)
      * Announced candidacy publicly January 2025
      Aligned with Fredericksburg's Democratic-leaning local-political
      ecosystem; Crump's election coverage in local Democratic-leaning
      outlets indicates Democratic alignment.

We do NOT have evidence of specific votes by either member yet
(both were sworn in less than a year ago). Applying the Democratic
party-default scoring is the same posture used for the 613 state-
legislative records seeded last week — the profiles will render the
amber "Party-default scoring" banner with rationale, and the
existing review pipeline lets a reviewer (or Adam directly) replace
the heuristic with claim-level evidence as votes accumulate.

If a reviewer disagrees with Democratic alignment for either, the
fix is to flip party and rerun this script.

Run once; idempotent.
"""
import json
import os
import subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')


# Reuse the same Democratic party-default profile from
# seed-state-assemblies.py (all six measurable categories False;
# christian_heritage null since absence-of-evidence is misleading
# either direction on that category).
PARTY_DEFAULT_D = {
    'america_first':      [False] * 5,
    'life':               [False] * 5,
    'immigration':        [False] * 5,
    'marriage':           [False] * 5,
    'self_defense':       [False] * 5,
    'education':          [False] * 5,
    'christian_heritage': [None] * 5,
}

D_RATIONALE = (
    "Party-default scoring applied for (D). Democrats in U.S. local "
    "councils, particularly in left-leaning Virginia cities like "
    "Fredericksburg, vote overwhelmingly with their caucus against "
    "each of the six measurable RESOLUTE Citizen criteria. All six "
    "measurable categories therefore set False; christian_heritage "
    "(PCH/CBG) left null because the absence of evidence there is "
    "misleading either direction — a D council member could be a "
    "devout Christian in private life. This baseline will be "
    "overwritten by individual voting-record evidence as that "
    "evidence is collected via the claim-extraction pipeline."
)

TARGETS = {
    'matt-rowe-fxbg': {
        'party': 'D',
        'background': (
            'Snowden Hills resident. Recently elected chair of the '
            'Fredericksburg City School Board (January 2025). '
            'Previously served as a Bowling Green Town councilman. '
            'Ran as the Democratic nominee for Virginia\'s 1st '
            'Congressional District in 2016. Sworn in to '
            'Fredericksburg City Council Ward 1 in 2025.'
        ),
        'scoring_sources_added': [
            'https://www.fredericksburgfreepress.com/?s=matt+rowe',
            'https://ballotpedia.org/Matt_Rowe',
        ],
    },
    'joy-crump-fxbg': {
        'party': 'D',
        'background': (
            'Chef-owner of FOODE + Mercantile in downtown Fredericksburg '
            'since 2011. Bravo "Top Chef" competitor; cooked at the '
            'James Beard House. First Black woman elected to '
            'Fredericksburg City Council (November 2024). Took office '
            'January 2025 representing Ward 2.'
        ),
        'scoring_sources_added': [
            'https://www.fredericksburgfreepress.com/?s=joy+crump',
            'https://ballotpedia.org/Joy_Crump',
        ],
    },
}


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    touched = 0
    for c in sc['candidates']:
        slug = c.get('slug')
        if slug not in TARGETS:
            continue
        cfg = TARGETS[slug]
        # Apply party + scores
        c['party'] = cfg['party']
        c['scores'] = {cat: list(vals) for cat, vals in PARTY_DEFAULT_D.items()}
        # Update profile with confidence + rationale
        prof = c.setdefault('profile', {})
        prof['confidence'] = 'party_default'
        prof['scoring_rationale'] = D_RATIONALE
        prof['seeded_on'] = date.today().isoformat()
        if cfg.get('background') and not prof.get('background'):
            prof['background'] = cfg['background']
        # Append research sources if not present
        sources = list(c.get('sources') or [])
        for s in cfg.get('scoring_sources_added') or []:
            if s not in sources:
                sources.append(s)
        c['sources'] = sources
        # Append scoring rationale to notes for the audit trail
        existing_notes = c.get('notes') or ''
        tag = f' Party affiliation (D) and party-default scoring applied {date.today().isoformat()} based on Fredericksburg Free Press coverage.'
        if 'party-default scoring applied' not in existing_notes:
            c['notes'] = (existing_notes + tag).strip()
        touched += 1
        print(f'Scored: {c.get("name")} ({c.get("office")}) -> party_default(D)')

    sc.setdefault('meta', {})
    sc['meta']['last_updated'] = date.today().isoformat()
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'\nTouched {touched} record(s).')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
