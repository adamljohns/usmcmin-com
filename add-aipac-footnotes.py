#!/usr/bin/env python3
"""
add-aipac-footnotes.py — attach a TrackAIPAC + OpenSecrets lookup
footnote to every federal Senator + U.S. Representative, wired to
america_first question 3:

  "Candidate has never accepted donations from foreign governments,
   foreign-backed lobbies (e.g., AIPAC), or foreign-linked PACs"

We do NOT programmatically set the score to False — that would require
per-candidate verification from FEC data. Instead this script ensures
every federal profile visibly footnotes the PRIMARY SOURCES where a
visitor can check for themselves:

  * TrackAIPAC per-state page (lists every member of Congress from
    that state with their aggregate AIPAC / pro-Israel lobby
    contribution totals, sourced from FEC + OpenSecrets).
  * OpenSecrets "Pro-Israel" industry summary per candidate.
  * AIPAC's own election-center page for endorsements.

Run once; idempotent (won't duplicate footnotes).

    python3 add-aipac-footnotes.py
"""
import json
import os
import subprocess

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')

STATE_FULL_NAMES = {
    'AL': 'alabama', 'AK': 'alaska', 'AZ': 'arizona', 'AR': 'arkansas',
    'CA': 'california', 'CO': 'colorado', 'CT': 'connecticut', 'DE': 'delaware',
    'FL': 'florida', 'GA': 'georgia', 'HI': 'hawaii', 'ID': 'idaho',
    'IL': 'illinois', 'IN': 'indiana', 'IA': 'iowa', 'KS': 'kansas',
    'KY': 'kentucky', 'LA': 'louisiana', 'ME': 'maine', 'MD': 'maryland',
    'MA': 'massachusetts', 'MI': 'michigan', 'MN': 'minnesota', 'MS': 'mississippi',
    'MO': 'missouri', 'MT': 'montana', 'NE': 'nebraska', 'NV': 'nevada',
    'NH': 'new-hampshire', 'NJ': 'new-jersey', 'NM': 'new-mexico', 'NY': 'new-york',
    'NC': 'north-carolina', 'ND': 'north-dakota', 'OH': 'ohio', 'OK': 'oklahoma',
    'OR': 'oregon', 'PA': 'pennsylvania', 'RI': 'rhode-island', 'SC': 'south-carolina',
    'SD': 'south-dakota', 'TN': 'tennessee', 'TX': 'texas', 'UT': 'utah',
    'VT': 'vermont', 'VA': 'virginia', 'WA': 'washington', 'WV': 'west-virginia',
    'WI': 'wisconsin', 'WY': 'wyoming', 'DC': 'district-of-columbia',
}


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    federal = [c for c in sc.get('candidates') or [] if c.get('level') == 'federal']
    print(f'Federal candidates in scorecard: {len(federal)}')

    touched = 0
    already = 0
    no_state = 0
    for c in federal:
        st = (c.get('state') or '').upper()
        state_slug = STATE_FULL_NAMES.get(st)
        if not state_slug:
            no_state += 1
            continue

        # The three AIPAC-tracking footnotes we want present on every
        # federal profile. Footnote ids are namespaced with "aipac-" so
        # future runs don't collide with other IDs.
        candidate_slug = c.get('slug') or ''
        track_url = f'https://www.trackaipac.com/states/{state_slug}'
        os_url = f'https://www.opensecrets.org/search?q={candidate_slug.replace("-","+")}&type=donors'
        aipac_url = 'https://www.aipac.org/election-center'

        footnotes = c.setdefault('footnotes', {})
        afn = c.setdefault('answer_footnotes', {})
        af = afn.setdefault('america_first', [[] for _ in range(5)])
        while len(af) < 5:
            af.append([])

        added_any = False
        fn_specs = [
            ('aipac-track', {
                'url': track_url,
                'archive_url': None,
                'title': f'TrackAIPAC — {STATE_FULL_NAMES[st].replace("-"," ").title()} delegation',
                'publisher': 'TrackAIPAC (sourced from FEC + OpenSecrets)',
                'accessed': '2026-04-24',
                'excerpt': (
                    'Aggregates every AIPAC and pro-Israel-lobby contribution '
                    'each member of Congress has received, sourced directly from '
                    'FEC filings and OpenSecrets. Matches the RESOLUTE Citizen '
                    "America-First question 3: foreign-backed lobby donations."
                ),
            }),
            ('aipac-opensecrets', {
                'url': os_url,
                'archive_url': None,
                'title': f'OpenSecrets — donor search for {c.get("name","")}',
                'publisher': 'OpenSecrets (Center for Responsive Politics)',
                'accessed': '2026-04-24',
                'excerpt': (
                    'Non-partisan campaign-finance database. Search the '
                    "candidate's name to see every FEC-reported donor, including "
                    'pro-Israel lobby contributions.'
                ),
            }),
            ('aipac-endorsements', {
                'url': aipac_url,
                'archive_url': None,
                'title': "AIPAC Election Center — endorsed candidates",
                'publisher': 'American Israel Public Affairs Committee',
                'accessed': '2026-04-24',
                'excerpt': (
                    "AIPAC's own public endorsement list. If a candidate appears "
                    'here, they have accepted AIPAC backing; the RESOLUTE '
                    'Citizen scoring criterion treats this as a failure on '
                    'America-First question 3.'
                ),
            }),
        ]
        for fn_id, spec in fn_specs:
            if fn_id not in footnotes:
                footnotes[fn_id] = spec
                added_any = True
            if fn_id not in af[3]:
                af[3].append(fn_id)
                added_any = True
        if added_any:
            touched += 1
        else:
            already += 1

    print(f'Touched: {touched}  Already had AIPAC footnotes: {already}  No state slug: {no_state}')

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
