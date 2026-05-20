#!/usr/bin/env python3
"""
add-competitive-house-2026-batch6.py — Pass 3 expansion: competitive-district
challengers for the top swing seats where the incumbent IS running but faces
serious challenger primaries.

Covers 12 high-priority swing districts:
  NY-17 (vs Lawler R, Cook lean R): 6 D primary candidates
  NY-19 (vs Riley D, Cook lean D): 2 R primary candidates
  IA-01 (vs Miller-Meeks R, Cook toss-up): 2 D primary candidates
  IA-03 (vs Nunn R, Cook lean R): Sarah Trone Garriott (D)
  AZ-06 (vs Ciscomani R, Cook toss-up): 4 D primary candidates
  CO-08 (vs Evans R, Cook toss-up): 3 D primary candidates
  VA-02 (vs Kiggans R, Cook toss-up): 7 D primary candidates (Luria!)
  VA-07 (vs Vindman D, Cook lean D): 5 R primary candidates (Tara Durant!)
  MI-07 (vs Barrett R, Cook toss-up): 7 D primary candidates (Brink!)
  MI-08 (vs McDonald Rivet D, Cook lean D): 3 R primary candidates
  CA-22 (vs Valadao R, jungle primary): 4 D primary candidates
  CA-13 (vs Gray D, jungle primary): 3 R + 1 NPP primary candidates

~45 new records. Most challengers get archetype-based scoring; named
high-profile candidates (Luria, Brink, etc.) get more detail.
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
            'confidence_note': cn or (f'2026-05-20 — competitive district challenger ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — competitive district placeholder.'),
            **(profile_extra or {}),
        },
    }

def ph(name, slug, state, district, party, primary_date, ctx=''):
    label = {'R':'R','D':'D','I':'I','NPP':'No Party Pref'}[party]
    office = f'U.S. Representative {state}-{district:02d} (2026 {label} Candidate · challenger{(" · "+ctx) if ctx else ""})'
    return rec(name, slug, state, district, office, party, None, primary_date,
               f'{name} — 2026 {state}-{district:02d} primary ballot. Placeholder.')


RECORDS = [
    # ══ NY-17 (R incumbent Lawler · Cook lean R · D primary 6/23) ══
    rec('Cait Conley', 'cait-conley', 'NY', 17,
        'U.S. Representative NY-17 (2026 D Candidate · challenger to Lawler · Army vet + ex-NSC + CISA · Cook lean R)',
        'D', 'establishment_d', '2026-06-23',
        notes=('U.S. Army veteran. Served on the National Security Council and at the '
               'Cybersecurity and Infrastructure Security Agency under President Biden. '
               'Top-tier D primary challenger to Rep. Mike Lawler (R) in NY-17.'),
        sources=['https://ballotpedia.org/Cait_Conley']),
    rec('Beth Davidson', 'beth-davidson', 'NY', 17,
        'U.S. Representative NY-17 (2026 D Candidate · challenger to Lawler · Rockland Co Legislator)',
        'D', 'establishment_d', '2026-06-23',
        notes='Rockland County Legislator (elected 2024). Former Nyack school board member. D primary challenger to Lawler.',
        sources=['https://ballotpedia.org/Beth_Davidson']),
    rec('Effie Phillips-Staley', 'effie-phillips-staley', 'NY', 17,
        'U.S. Representative NY-17 (2026 D Candidate · challenger to Lawler · Tarrytown Trustee)',
        'D', 'establishment_d', '2026-06-23',
        notes='Tarrytown Village Board of Trustees. D primary challenger to Lawler.',
        sources=['https://ballotpedia.org/Effie_Phillips-Staley']),
    ph('Mike Sacks', 'mike-sacks-ny-17', 'NY', 17, 'D', '2026-06-23', 'Lawler challenger (journalist)'),
    ph('John Sullivan', 'john-sullivan-ny-17', 'NY', 17, 'D', '2026-06-23', 'Lawler challenger (ex-FBI analyst)'),
    ph('John Cappello', 'john-cappello', 'NY', 17, 'D', '2026-06-23', 'Lawler challenger (AF veteran)'),

    # ══ NY-19 (D incumbent Riley · Cook lean D · R primary 6/23) ══
    rec('Peter Oberacker', 'peter-oberacker', 'NY', 19,
        'U.S. Representative NY-19 (2026 R Candidate · challenger to Riley · NY State Senator)',
        'R', 'establishment_r', '2026-06-23',
        notes='NY State Senator. Top R primary challenger to incumbent Rep. Josh Riley (D).',
        sources=['https://ballotpedia.org/Peter_Oberacker']),
    ph('Alexander Portelli', 'alexander-portelli', 'NY', 19, 'R', '2026-06-23', 'Riley challenger'),

    # ══ IA-01 (R incumbent Miller-Meeks · Cook toss-up · D primary 6/2) ══
    rec('Christina Bohannan', 'christina-bohannan', 'IA', 1,
        'U.S. Representative IA-01 (2026 D Candidate · 3-time challenger to Miller-Meeks · UIowa Law professor)',
        'D', 'establishment_d', '2026-06-02',
        notes=('University of Iowa law professor. 2022 + 2024 D nominee against Mariannette '
               'Miller-Meeks (lost both narrowly — 2024 was the closest IA-01 race in modern '
               'history). Running again in 2026.'),
        sources=['https://ballotpedia.org/Christina_Bohannan']),
    rec('Travis Terrell', 'travis-terrell', 'IA', 1,
        'U.S. Representative IA-01 (2026 D Candidate · UIHC employee)',
        'D', 'establishment_d', '2026-06-02',
        notes='University of Iowa Health Care employee. First public office bid. D primary candidate in IA-01.',
        sources=['https://ballotpedia.org/Travis_Terrell']),

    # ══ IA-03 (R incumbent Nunn · Cook lean R · D primary 6/2) ══
    rec('Sarah Trone Garriott', 'sarah-trone-garriott', 'IA', 3,
        'U.S. Representative IA-03 (2026 D Candidate · IA state senator · top challenger to Nunn)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Iowa state senator. Out-raised incumbent Rep. Zach Nunn (R) in early 2026 '
               'reports. After former House minority leader Jennifer Konfrst withdrew and '
               'endorsed Trone Garriott, she became the consolidated D challenger.'),
        sources=['https://ballotpedia.org/Sarah_Trone_Garriott']),

    # ══ AZ-06 (R incumbent Ciscomani · Cook toss-up · D primary 7/21) ══
    rec('JoAnna Mendoza', 'joanna-mendoza', 'AZ', 6,
        'U.S. Representative AZ-06 (2026 D Candidate · D-party-backed challenger to Ciscomani)',
        'D', 'establishment_d', '2026-07-21',
        notes=('D-party-backed challenger to Rep. Juan Ciscomani (R). Out-raised Ciscomani in '
               'Q4 2025 ($1M+). Tucson-area Cook toss-up race.'),
        sources=['https://ballotpedia.org/JoAnna_Mendoza',
                 'https://www.notus.org/2026-election/juan-ciscomani-challenger-joanna-mendoza']),
    ph('Johnathan Buma', 'johnathan-buma', 'AZ', 6, 'D', '2026-07-21', 'Ciscomani challenger'),
    ph('Chris Donat', 'chris-donat', 'AZ', 6, 'D', '2026-07-21', 'Ciscomani challenger'),
    ph('Carter Weeks', 'carter-weeks', 'AZ', 6, 'D', '2026-07-21', 'Ciscomani challenger'),

    # ══ CO-08 (R incumbent Evans · Cook toss-up · D primary 6/30) ══
    rec('Manny Rutinel', 'manny-rutinel', 'CO', 8,
        'U.S. Representative CO-08 (2026 D Candidate · CO state rep · challenger to Evans · Cook toss-up)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Colorado state representative (Commerce City). D primary candidate in CO-08 '
               '— Cook toss-up race against freshman R Rep. Gabe Evans.'),
        sources=['https://ballotpedia.org/Manny_Rutinel']),
    rec('Shannon Bird', 'shannon-bird', 'CO', 8,
        'U.S. Representative CO-08 (2026 D Candidate · former CO state rep · challenger to Evans)',
        'D', 'establishment_d', '2026-06-30',
        notes='Former Colorado state representative. D primary candidate in CO-08 vs Evans.',
        sources=['https://ballotpedia.org/Shannon_Bird']),
    rec('Evan Munsing', 'evan-munsing', 'CO', 8,
        'U.S. Representative CO-08 (2026 D Candidate · private equity consultant)',
        'D', 'establishment_d', '2026-06-30',
        notes='Private equity consultant. D primary candidate in CO-08 vs Evans.',
        sources=['https://ballotpedia.org/Evan_Munsing']),

    # ══ VA-02 (R incumbent Kiggans · Cook toss-up · D primary 8/4) ══
    rec('Elaine Luria', 'elaine-luria', 'VA', 2,
        'U.S. Representative VA-02 (2026 D Candidate · former US Rep VA-02 · seeking rematch with Kiggans)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former U.S. Representative VA-02 (2019-2023). Retired Navy commander '
               '(20 years). Member of the Jan 6 Select Committee. Lost 2022 to Kiggans (R). '
               'Announced 2026 comeback bid Nov 12 2025. D primary candidate for VA-02 rematch.'),
        sources=['https://ballotpedia.org/Elaine_Luria',
                 'https://www.vpm.org/elections/2025-11-12/elaine-luria-house-of-representatives-va02-kiggans-eastern-shore-virginia-beach'],
        profile_extra={'background': ('Retired U.S. Navy commander (20 years). Former U.S. Rep '
                                      'VA-02 (2019-2023). Member of January 6 Select Committee. '
                                      'Lost 2022 to Kiggans, running again 2026.')}),
    ph('Nila Devanath', 'nila-devanath', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),
    ph('Patrick Mosolf', 'patrick-mosolf', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),
    ph('James Osyf', 'james-osyf', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),
    ph('Nicolaus Sleister', 'nicolaus-sleister', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),
    ph('Matt Strickler', 'matt-strickler', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),
    ph('John Stringfellow', 'john-stringfellow', 'VA', 2, 'D', '2026-08-04', 'Kiggans challenger'),

    # ══ VA-07 (D incumbent Vindman · Cook lean D · R primary 8/4) ══
    rec('Tara Durant', 'tara-durant', 'VA', 7,
        'U.S. Representative VA-07 (2026 R Candidate · VA state sen · challenger to Vindman · Cook lean D)',
        'R', 'establishment_r', '2026-08-04',
        notes=('VA State Senator. Top R primary challenger to freshman D Rep. Eugene Vindman.'),
        sources=['https://ballotpedia.org/Tara_Durant']),
    ph('John Gray', 'john-gray-va-07', 'VA', 7, 'R', '2026-08-04', 'Vindman challenger'),
    rec('Darius Mayfield', 'darius-mayfield', 'VA', 7,
        'U.S. Representative VA-07 (2026 R Candidate · 2x prior NJ-12 nominee · talent manager)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes='Talent manager. 2022 + 2024 R nominee for NJ-12 (Watson-Coleman seat, lost both). Now running in VA-07.',
        sources=['https://ballotpedia.org/Darius_Mayfield']),
    rec('Douglas Ollivant', 'douglas-ollivant', 'VA', 7,
        'U.S. Representative VA-07 (2026 R Candidate · former NSC Director for Iraq)',
        'R', 'establishment_r', '2026-08-04',
        notes='Former Director for Iraq at U.S. National Security Council. R primary candidate in VA-07.',
        sources=['https://ballotpedia.org/Douglas_Ollivant']),
    ph('Waverly Washington', 'waverly-washington', 'VA', 7, 'R', '2026-08-04', 'Vindman challenger (Army Reservist)'),

    # ══ MI-07 (R incumbent Barrett · Cook toss-up · D primary 8/4) ══
    rec('Bridget Brink', 'bridget-brink', 'MI', 7,
        'U.S. Representative MI-07 (2026 D Candidate · former US Ambassador to Ukraine · challenger to Barrett)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former U.S. Ambassador to Ukraine (2022-2025) + former U.S. Ambassador to '
               'Slovakia (2019-2022). 28-year career diplomat. Top-tier D primary candidate '
               'in MI-07 against freshman R Rep. Tom Barrett.'),
        sources=['https://ballotpedia.org/Bridget_Brink'],
        profile_extra={'background': ('Former U.S. Ambassador to Ukraine (2022-2025); resigned '
                                      'in April 2025 over Trump-Russia policy disagreements. '
                                      'Former U.S. Ambassador to Slovakia (2019-2022). 28-year '
                                      'career diplomat (State Department).')}),
    rec('Matt Maasdam', 'matt-maasdam', 'MI', 7,
        'U.S. Representative MI-07 (2026 D Candidate · former Navy SEAL · ex-Obama Military Aide · Iraq/Afghan vet)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former U.S. Navy SEAL. Former Obama Military Presidential Aide. Iraq + Afghanistan '
               'War veteran. D primary candidate for MI-07.'),
        sources=['https://ballotpedia.org/Matt_Maasdam']),
    rec('William Lawrence', 'william-lawrence-mi-07', 'MI', 7,
        'U.S. Representative MI-07 (2026 D Candidate · political organizer + progressive activist)',
        'D', 'progressive_d', '2026-08-04',
        notes='Political organizer + progressive activist. D primary candidate for MI-07.',
        sources=['https://ballotpedia.org/William_Lawrence']),
    ph('Elyon Badger', 'elyon-badger', 'MI', 7, 'D', '2026-08-04', 'Barrett challenger'),
    ph('Josh Cowen', 'josh-cowen', 'MI', 7, 'D', '2026-08-04', 'Barrett challenger'),
    ph('Alexandra Prieditis', 'alexandra-prieditis', 'MI', 7, 'D', '2026-08-04', 'Barrett challenger'),
    ph('Muhammad Salman Rais', 'muhammad-salman-rais', 'MI', 7, 'D', '2026-08-04', 'Barrett challenger'),

    # ══ MI-08 (D incumbent McDonald Rivet · Cook lean D · R primary 8/4) ══
    ph('Amir Hassan', 'amir-hassan-mi-08', 'MI', 8, 'R', '2026-08-04', 'McDonald Rivet challenger'),
    ph('Alfred Lemmo', 'alfred-lemmo', 'MI', 8, 'R', '2026-08-04', 'McDonald Rivet challenger'),
    ph('Thomas J. Smith', 'thomas-j-smith-mi-08', 'MI', 8, 'R', '2026-08-04', 'McDonald Rivet challenger'),

    # ══ CA-22 (R incumbent Valadao · Cook toss-up · jungle primary 6/2) ══
    rec('Rudy Salas', 'rudy-salas', 'CA', 22,
        'U.S. Representative CA-22 (2026 D Candidate · former CA Assembly · 3rd Valadao challenge)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former CA Assembly member. 2022 + 2024 D nominee against Valadao (lost both '
               'narrowly). Running again in 2026 jungle primary.'),
        sources=['https://ballotpedia.org/Rudy_Salas']),
    rec('Jasmeet Bains', 'jasmeet-bains', 'CA', 22,
        'U.S. Representative CA-22 (2026 D Candidate · CA Assembly · physician · Central Valley MAT chief medical officer)',
        'D', 'establishment_d', '2026-06-02',
        notes=('CA Assembly member (elected 2022). Physician + chief medical officer for the '
               'California Medical Assistance Team Central Valley. D primary candidate.'),
        sources=['https://ballotpedia.org/Jasmeet_Bains']),
    rec('Randy Villegas', 'randy-villegas', 'CA', 22,
        'U.S. Representative CA-22 (2026 D Candidate · Visalia school board + College of the Sequoias professor)',
        'D', 'progressive_d', '2026-06-02',
        notes='Professor of political science at College of the Sequoias. Visalia Unified Board of Education. D primary candidate.',
        sources=['https://ballotpedia.org/Randy_Villegas']),
    ph('Eric Garcia', 'eric-garcia-ca-22', 'CA', 22, 'D', '2026-06-02', 'Valadao challenger'),

    # ══ CA-13 (D incumbent Gray · jungle primary 6/2) ══
    ph('Vin Kruttiventi', 'vin-kruttiventi', 'CA', 13, 'R', '2026-06-02', 'Gray challenger'),
    ph('Kevin Lincoln II', 'kevin-lincoln-ii', 'CA', 13, 'R', '2026-06-02', 'Gray challenger (former Stockton Mayor)'),
    ph('Javier Lopez', 'javier-lopez-ca-13', 'CA', 13, 'R', '2026-06-02', 'Gray challenger'),
    ph('Alberto Escobedo', 'alberto-escobedo', 'CA', 13, 'NPP', '2026-06-02', 'Gray challenger (No Party Pref)'),
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
