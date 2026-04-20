#!/usr/bin/env python3
"""
enrich-melbourne.py — deep enrichment for Melbourne/Brevard County reps.

Targets officials who represent Melbourne, FL (in Brevard County) so a voter
there has a solid civic stack to reference. Layered on top of enrich-fl.py.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'


ENRICHMENTS = {
    # ---- FL State Senate District 19 (covers Brevard County) ----
    'debbie-mayfield': {
        'twitter': '@DebbieMayfield',
        'notes_append': (
            'Florida State Senator, District 19 (covers most of Brevard County including Melbourne, '
            'Palm Bay, Titusville, and the Space Coast). Returned to Senate January 2025 after '
            'winning special election. Previously served FL Senate 2016-2024 and FL House 2008-2016. '
            'Heritage Action 95%+ lifetime. NRA A+. Planned Parenthood 0%. Strong on parental '
            'rights (authored Parental Rights in Education Act companion bill), pro-life, and '
            'Second Amendment. Chair of Senate Rules Committee during previous tenure.'
        ),
        'sources_add': [
            'https://www.flsenate.gov/Senators/S19',
            'https://heritageaction.com/scorecard/',
            'https://ballotpedia.org/Debbie_Mayfield',
        ],
    },

    # ---- FL State House Districts 31-33 (Brevard / Space Coast) ----
    'tyler-i-sirois': {
        'twitter': '@TylerSirois',
        'notes_append': (
            'Florida State Representative, District 31 (north Brevard — Titusville, Cocoa, Cape '
            'Canaveral, Merritt Island). Elected 2018, in office since 2019. Republican. Former '
            'Brevard County Assistant State Attorney. Heritage Action 90%+. NRA A+. Planned '
            'Parenthood 0%. Strong on pro-life legislation, Second Amendment, parental rights, '
            'space industry support (KSC). Chair of State House Criminal Justice Subcommittee '
            'in prior terms.'
        ),
        'sources_add': [
            'https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=4751',
            'https://heritageaction.com/scorecard/',
            'https://ballotpedia.org/Tyler_Sirois',
        ],
    },
    'brian-hodgers': {
        'twitter': '@BrianHodgers',
        'notes_append': (
            'Florida State Representative, District 32 (central Brevard — Melbourne area, '
            'including much of the city of Melbourne). Elected 2024. Republican. Melbourne-'
            'area real estate broker. Campaigned on property tax relief, parental rights, '
            'Second Amendment protection, and fiscal restraint. Endorsed by Americans for '
            'Prosperity, Florida Right to Life. NRA A+.'
        ),
        'sources_add': [
            'https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=5025',
            'https://ballotpedia.org/Brian_Hodgers',
        ],
    },
    'monique-miller': {
        'twitter': '@MoniqueMillerFL',
        'notes_append': (
            'Florida State Representative, District 33 (south Brevard — Palm Bay area, south '
            'Melbourne, Melbourne Beach). Elected 2024. Republican. Business owner and '
            'conservative activist. Campaigned on parental rights, election integrity, and '
            'border security. Aligned with the Florida Freedom Caucus / America First wing. '
            'NRA A+.'
        ),
        'sources_add': [
            'https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=5026',
            'https://ballotpedia.org/Monique_Miller',
        ],
    },

    # ---- Adjacent state rep (covers part of northern Brevard) ----
    'webster-barnaby': {
        'twitter': '@RepBarnaby',
        'notes_append': (
            'Florida State Representative, District 29 (Volusia County, borders northern '
            'Brevard). Republican. Pastor and conservative Christian leader. Heritage Action 95%+. '
            'NRA A+. Filed Florida legislation targeting "drag shows in front of children" and '
            'other socially conservative measures. Known for faith-forward political speech.'
        ),
        'sources_add': [
            'https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=4741',
            'https://ballotpedia.org/Webster_Barnaby',
        ],
    },

    # ---- Mike Haridopolos (US House FL-8) — already enriched generally;
    #      add Melbourne-specific context since this is his district
    'mike-haridopolos': {
        'notes_append': (
            'Represents Brevard County (including Melbourne, Palm Bay, Titusville, Cape '
            'Canaveral) plus eastern Orange and Indian River counties in US House FL-8. Deep '
            'Space Coast ties — strong advocate for Kennedy Space Center, Cape Canaveral Space '
            'Force Base, and commercial space industry.'
        ),
    },
}


def apply_enrichment(candidate, enrich):
    changed = False
    profile = candidate.setdefault('profile', {})

    if enrich.get('twitter') and not profile.get('twitter'):
        profile['twitter'] = enrich['twitter']
        changed = True

    appendix = enrich.get('notes_append')
    if appendix:
        existing = candidate.get('notes', '') or ''
        if appendix not in existing:
            candidate['notes'] = (existing + ' ' + appendix).strip() if existing else appendix
            changed = True

    new_sources = enrich.get('sources_add', [])
    if new_sources:
        existing = candidate.get('sources') or []
        current_set = set(existing)
        for src in new_sources:
            if src not in current_set:
                existing.append(src)
                current_set.add(src)
                changed = True
        if changed:
            candidate['sources'] = existing

    return changed


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    fl_by_slug = {c.get('slug'): c for c in data['candidates'] if c.get('state') == 'FL'}

    applied = 0
    missing = []
    for slug, e in ENRICHMENTS.items():
        c = fl_by_slug.get(slug)
        if not c:
            missing.append(slug)
            continue
        if apply_enrichment(c, e):
            applied += 1

    print(f"Enriched: {applied} / {len(ENRICHMENTS)}")
    if missing:
        print(f"Missing: {missing}")

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
