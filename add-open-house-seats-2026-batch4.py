#!/usr/bin/env python3
"""
add-open-house-seats-2026-batch4.py — Pass 2 House primary work, batch 4 (final).

Wraps up the remaining ~15 open House seats. ~50 records, heavy on placeholders
for the long-tail districts where Ballotpedia surface data is thin.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

ARCHETYPES = {
    'maga_conservative_r': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,T,N,T],'election_integrity':[N,T,N,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[N,N,N,F,N],'industry_capture':[N,N,N,T,N],
    },
    'establishment_r': {
        'sanctity_of_life':[T,F,T,T,T],'biblical_marriage':[N,F,T,N,N],
        'family_child_sovereignty':[N,N,T,N,N],'christian_liberty':[T,N,N,N,N],
        'economic_stewardship':[N,F,N,N,F],'election_integrity':[F,T,F,F,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,F,F,T,T],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,N,F],
    },
    'progressive_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,N,T],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[N,T,N,N,N],'industry_capture':[N,F,T,N,T],
    },
    'establishment_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
    },
    'populist_right': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,F,N,T],'election_integrity':[N,T,T,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[T,T,T,F,T],'industry_capture':[T,T,T,N,T],
    },
}

def scores_from(a): return {cid: list(row) for cid, row in ARCHETYPES[a].items()}
def empty_scores():
    return {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture',
    ]}

def rec(name, slug, state, district, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate', cn=''):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': 'United States House of Representatives',
        'party': party, 'level': 'federal', 'district': district,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{state}_{district}_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': cn or (f'2026-05-20 — ingested for 2026 open House seat ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — placeholder.'),
            **(profile_extra or {}),
        },
    }

def ph(name, slug, state, district, party, primary_date, ctx=''):
    label = {'R':'R','D':'D','I':'I'}[party]
    office = f'U.S. Representative {state}-{district:02d} (2026 {label} Candidate · open seat{(" · "+ctx) if ctx else ""})'
    return rec(name, slug, state, district, office, party, None, primary_date,
               f'{name} — on the 2026 {state}-{district:02d} primary ballot. Placeholder.')


RECORDS = [
    # ════ AZ-05 (Biggs → Gov; primary 7/21) ════
    rec('Mark Lamb', 'mark-lamb', 'AZ', 5,
        'U.S. Representative AZ-05 (2026 R Candidate · Biggs-seat open · Pinal County Sheriff)',
        'R', 'maga_conservative_r', '2026-07-21',
        notes=('Pinal County Sheriff. Trump-ally. Prior R Senate primary candidate (lost to Lake 2024). '
               'R primary candidate for the open AZ-05 seat after Biggs left for Governor.'),
        sources=['https://ballotpedia.org/Mark_Lamb']),
    ph('Travis Grantham', 'travis-grantham', 'AZ', 5, 'R', '2026-07-21', 'Biggs seat'),
    ph('Mike Gross', 'mike-gross-az-05', 'AZ', 5, 'R', '2026-07-21', 'Biggs seat'),
    ph('Daniel Keenan', 'daniel-keenan', 'AZ', 5, 'R', '2026-07-21', 'Biggs seat'),

    # ════ AZ-07 (Grijalva died 3/13/25; daughter won special 2025 + running 2026) ════
    rec('Adelita Grijalva', 'adelita-grijalva', 'AZ', 7,
        'U.S. Representative AZ-07 (2026 D incumbent · won 2025 special after Grijalva death · Pima Co supervisor)',
        'D', 'progressive_d', '2026-07-21',
        candidacy_status='incumbent_seeking_reelection',
        notes=('Daughter of late Rep. Raúl Grijalva (D, died March 13, 2025). Pima County '
               'Supervisor. Won 2025 special election to fill her father\'s seat. Running for '
               'full term in 2026 D primary.'),
        sources=['https://ballotpedia.org/Adelita_Grijalva']),
    ph('Daniel Butierez', 'daniel-butierez', 'AZ', 7, 'R', '2026-07-21', 'AZ-07'),

    # ════ TN-06 (John Rose → Gov; primary 8/6) ════
    rec('Van Hilleary', 'van-hilleary', 'TN', 6,
        'U.S. Representative TN-06 (2026 R Candidate · Rose-seat open · former US Rep TN-04, seeking comeback)',
        'R', 'maga_conservative_r', '2026-08-06',
        notes=('Former U.S. Representative TN-04 (1995-2003). 2002 R nominee for Tennessee '
               'Governor (lost to Bredesen). Seeking a return to Congress in TN-06.'),
        sources=['https://ballotpedia.org/Van_Hilleary']),
    rec('Johnny Garrett', 'johnny-garrett', 'TN', 6,
        'U.S. Representative TN-06 (2026 R Candidate · Rose-seat open · TN state rep)',
        'R', 'maga_conservative_r', '2026-08-06',
        notes='TN state representative from Goodlettsville. R primary candidate.',
        sources=['https://ballotpedia.org/Johnny_Garrett']),
    ph('Natisha Brooks', 'natisha-brooks', 'TN', 6, 'R', '2026-08-06', 'Rose seat'),
    ph('Jon Henry', 'jon-henry-tn-06', 'TN', 6, 'R', '2026-08-06', 'Rose seat'),
    ph('Craig Ballin', 'craig-ballin', 'TN', 6, 'D', '2026-08-06', 'Rose seat'),
    ph('Lore Bergman', 'lore-bergman', 'TN', 6, 'D', '2026-08-06', 'Rose seat'),
    ph('Mike Croley', 'mike-croley', 'TN', 6, 'D', '2026-08-06', 'Rose seat'),

    # ════ TN-07 (Mark Green resigned 7/20/25; Van Epps won 2025 special) ════
    rec('Matt Van Epps', 'matt-van-epps', 'TN', 7,
        'U.S. Representative TN-07 (2026 R incumbent · won 2025 special after Green resignation)',
        'R', 'maga_conservative_r', '2026-08-06',
        candidacy_status='incumbent_seeking_reelection',
        notes=('Won 2025 special election to fill the TN-07 vacancy after Mark Green resigned. '
               'Running for full term in 2026 R primary.'),
        sources=['https://ballotpedia.org/Matt_Van_Epps']),
    ph('Jason Knight', 'jason-knight-tn-07', 'TN', 7, 'R', '2026-08-06', 'TN-07'),
    ph('Stewart Parks', 'stewart-parks', 'TN', 7, 'R', '2026-08-06', 'TN-07'),
    ph('Jay Reedy', 'jay-reedy', 'TN', 7, 'R', '2026-08-06', 'TN-07'),
    ph('David Jones', 'david-jones-tn-07', 'TN', 7, 'D', '2026-08-06', 'TN-07'),
    ph('Joshua Sales', 'joshua-sales', 'TN', 7, 'D', '2026-08-06', 'TN-07'),

    # ════ WI-07 (Tiffany retiring; primary 8/11) ════
    ph('Jessi Ebben', 'jessi-ebben', 'WI', 7, 'R', '2026-08-11', 'Tiffany seat (2020 nominee)'),
    ph('Kevin Hermening', 'kevin-hermening', 'WI', 7, 'R', '2026-08-11', 'Tiffany seat'),
    ph('Michael Alfonso', 'michael-alfonso', 'WI', 7, 'R', '2026-08-11', 'Tiffany seat'),
    ph('Niina Threlfall-Baum', 'niina-threlfall-baum', 'WI', 7, 'R', '2026-08-11', 'Tiffany seat'),
    ph('Paul Wassgren', 'paul-wassgren', 'WI', 7, 'R', '2026-08-11', 'Tiffany seat'),
    ph('Fred Clark', 'fred-clark-wi-07', 'WI', 7, 'D', '2026-08-11', 'Tiffany seat'),
    ph('Chris Armstrong', 'chris-armstrong-wi-07', 'WI', 7, 'D', '2026-08-11', 'Tiffany seat'),
    ph('Ginger Murray', 'ginger-murray', 'WI', 7, 'D', '2026-08-11', 'Tiffany seat'),

    # ════ NJ-11 (Sherrill → Gov; Analilia Mejia won 2025 special; primary 6/2) ════
    rec('Analilia Mejia', 'analilia-mejia', 'NJ', 11,
        'U.S. Representative NJ-11 (2026 D incumbent · won 2025 special after Sherrill became Gov)',
        'D', 'progressive_d', '2026-06-02',
        candidacy_status='incumbent_seeking_reelection',
        notes=('Won 2025 special election to fill NJ-11 after Mikie Sherrill won the 2025 NJ '
               'gubernatorial race. Running for full term in 2026 D primary.'),
        sources=['https://ballotpedia.org/Analilia_Mejia']),

    # ════ NJ-12 (Watson Coleman retiring; primary 6/2 with 13 D candidates) ════
    rec('Adam Hamawy', 'adam-hamawy', 'NJ', 12,
        'U.S. Representative NJ-12 (2026 D Candidate · Watson-Coleman-seat open · current poll leader · Army veteran)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Plastic surgeon + Army veteran. Polling leader (19%) per May 5-7 2026 internal '
               'poll. D primary candidate among 13 vying to succeed Bonnie Watson Coleman.'),
        sources=['https://ballotpedia.org/Adam_Hamawy']),
    rec('Sue Altman', 'sue-altman', 'NJ', 12,
        'U.S. Representative NJ-12 (2026 D Candidate · Watson-Coleman-seat open · 2024 NJ-07 nominee)',
        'D', 'progressive_d', '2026-06-02',
        notes='2024 D nominee for neighboring NJ-07. D primary candidate for NJ-12.',
        sources=['https://ballotpedia.org/Sue_Altman']),
    rec('Adrian Mapp', 'adrian-mapp', 'NJ', 12,
        'U.S. Representative NJ-12 (2026 D Candidate · Watson-Coleman-seat open · Plainfield Mayor)',
        'D', 'establishment_d', '2026-06-02',
        notes='Mayor of Plainfield, NJ. Watson-Coleman-trusted D candidate.',
        sources=['https://ballotpedia.org/Adrian_Mapp']),
    rec('Shanel Robinson', 'shanel-robinson', 'NJ', 12,
        'U.S. Representative NJ-12 (2026 D Candidate · Watson-Coleman-seat open · Somerset Co Commissioner)',
        'D', 'establishment_d', '2026-06-02',
        notes='Somerset County Commissioner. Watson-Coleman-trusted D candidate.',
        sources=['https://ballotpedia.org/Shanel_Robinson']),
    rec('Verlina Reynolds-Jackson', 'verlina-reynolds-jackson', 'NJ', 12,
        'U.S. Representative NJ-12 (2026 D Candidate · Watson-Coleman-seat open · NJ Assembly)',
        'D', 'establishment_d', '2026-06-02',
        notes='NJ Assemblywoman from Trenton. Watson-Coleman-trusted D candidate.',
        sources=['https://ballotpedia.org/Verlina_Reynolds-Jackson']),
    ph('Brad Cohen', 'brad-cohen', 'NJ', 12, 'D', '2026-06-02', 'Watson Coleman seat'),
    ph('Jay Vaingankar', 'jay-vaingankar', 'NJ', 12, 'D', '2026-06-02', 'Watson Coleman seat'),

    # ════ MA-06 (Moulton → Senate considering; placeholder) ════
    ph('MA-06 D placeholder', 'ma-06-d-placeholder', 'MA', 6, 'D', '2026-09-08', 'Moulton seat — research pending'),

    # ════ KS-03 (Davids potentially → Senate; primary 8/4) ════
    ph('KS-03 challenger placeholder', 'ks-03-challenger-placeholder', 'KS', 3, 'R', '2026-08-04', 'Davids seat'),

    # ════ SD-AL (Dusty Johnson → Gov; primary 6/2) ════
    ph('SD-AL R placeholder', 'sd-al-r-placeholder', 'SD', 0, 'R', '2026-06-02', 'Johnson seat'),

    # ════ IA-04 (Feenstra → Gov; primary 6/2) ════
    ph('IA-04 R placeholder', 'ia-04-r-placeholder', 'IA', 4, 'R', '2026-06-02', 'Feenstra seat'),

    # ════ SC-05 (Norman → Gov; primary 6/9) ════
    ph('SC-05 R placeholder', 'sc-05-r-placeholder', 'SC', 5, 'R', '2026-06-09', 'Norman seat'),

    # ════ LA-05 (Letlow → higher office; LA jungle primary 11/3 itself is the election) ════
    ph('LA-05 R placeholder', 'la-05-r-placeholder', 'LA', 5, 'R', '2026-11-03', 'Letlow seat'),

    # ════ FL-06 (Waltz resigned Jan 2025; FL Mike Haridopolos won 2025 special — already incumbent now)
    # No primary candidates added — that special is over.

    # ════ VA-11 (Connolly died 5/21/25 — special election already happened, current rep is James Walkinshaw)
    # No primary candidates added — handled in special.

    # ════ TX-21 (Roy → AG, TX 3/3 primary done) ════
    ph('TX-21 R placeholder', 'tx-21-r-placeholder', 'TX', 21, 'R', '2026-03-03', 'Roy seat'),

    # ════ TX-37 (Doggett retired) ════
    ph('TX-37 D placeholder', 'tx-37-d-placeholder', 'TX', 37, 'D', '2026-03-03', 'Doggett seat'),

    # ════ TX-38 (Hunt → Senate) ════
    ph('TX-38 R placeholder', 'tx-38-r-placeholder', 'TX', 38, 'R', '2026-03-03', 'Hunt seat'),
]


def upsert(cands, record):
    key = (record['state'], record['slug'])
    for i, c in enumerate(cands):
        if (c.get('state'), c.get('slug')) == key:
            cands[i] = record
            return 'REPLACED'
    cands.append(record)
    return 'INSERTED'


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    n_before = len(cands)
    by_district = {}
    inserts = replacements = 0
    for r in RECORDS:
        action = upsert(cands, r)
        if action == 'INSERTED':
            inserts += 1
        else:
            replacements += 1
        d = f'{r["state"]}-{r["district"]:02d}'
        by_district.setdefault(d, []).append(r['name'])
    for d, names in sorted(by_district.items()):
        print(f'  {d}: {len(names)} — {", ".join(names[:2])}{"..." if len(names) > 2 else ""}')
    print(f'\n  INSERTS: {inserts} · REPLACEMENTS: {replacements}')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
