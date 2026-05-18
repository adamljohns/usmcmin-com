#!/usr/bin/env python3
"""
migrate-rubric-to-v2.py — One-time schema migration from the v1 rubric
(7 categories × 5 questions × 2 pts = 70 max) to the v2 God First / America
First rubric (10 categories × 5 questions × 2 pts = 100 max, 60/40 weighted).

Strategy:
  • Categories where the domain is preserved (marriage, life, 2A, immigration)
    carry their existing True/False answers forward under the new id.
  • Categories where questions changed substantially (education,
    christian_heritage, america_first national-identity items) are null'd —
    they need rescoring under the new questions.
  • Brand-new categories (family_child_sovereignty, christian_liberty,
    economic_stewardship, election_integrity, industry_capture,
    foreign_policy_restraint) all start as null arrays awaiting enrichment.

Run from the repo root:
    python3 migrate-rubric-to-v2.py [--dry-run]
    python3 migrate-rubric-to-v2.py --apply
"""
import json
import os
import sys
from collections import Counter

INDEX_PATH = 'data/index.json'
STATES_DIR = 'data/states'
SCORECARD_PATH = 'data/scorecard.json'  # MASTER source-of-truth — build-data.py regenerates state files from this

# ────────────────────────────────────────────────────────────────────────────
# V2 RUBRIC — 10 categories × 5 questions × 2 pts = 100 pts (60 GF / 40 AF)
# ────────────────────────────────────────────────────────────────────────────
V2_CATEGORIES = [
    # ===== GOD FIRST — 60 pts =====
    {
        'id': 'sanctity_of_life',
        'tier': 'god_first',
        'label': 'Sanctity of Life',
        'icon': 'shield-chain-salvation-48.png',
        'description': 'Does this candidate affirm full personhood from conception and oppose all forms of abortion, infanticide, euthanasia, and embryonic experimentation?',
        'questions': [
            'Candidate affirms life begins at conception and personhood from conception',
            'Candidate has voted for or actively advocates abortion abolition (not merely restrictions)',
            'Candidate opposes embryonic stem-cell research, IVF embryo discard, and chimeric experimentation',
            'Candidate opposes euthanasia, physician-assisted suicide, and quality-of-life rationing',
            'Candidate has never accepted Planned Parenthood, NARAL, EMILY\'s List, or abortion-industry PAC funding',
        ],
    },
    {
        'id': 'biblical_marriage',
        'tier': 'god_first',
        'label': 'Biblical Marriage',
        'icon': 'shield-family.png',
        'description': 'Does this candidate affirm biblical marriage and reject the redefinition of family, sex, and gender in law?',
        'questions': [
            'Candidate affirms marriage as exclusively the lifelong union of one man and one woman as instituted by God',
            'Candidate opposes all forms of same-sex marriage, civil unions, and domestic partnerships in law',
            'Candidate rejects transgender ideology and affirms biological sex (male/female) as immutable and God-given',
            'Candidate supports no-fault divorce reform and policies that strengthen the marriage covenant',
            'Candidate opposes promotion of LGBTQ+ identity in public policy, schools, military, and corporate-government partnerships',
        ],
    },
    {
        'id': 'family_child_sovereignty',
        'tier': 'god_first',
        'label': 'Family & Child Sovereignty',
        'icon': 'shield-chain-faith-48.png',
        'description': 'Does this candidate defend parental authority over children and protect children from state intrusion, predators, and ideological capture?',
        'questions': [
            'Candidate supports universal school choice, homeschool freedom, and opposes compulsory public-school attendance',
            'Candidate supports parental notification and consent on all medical, mental-health, and gender-related interventions for minors',
            'Candidate opposes CRT, SOGI, "comprehensive sex ed," and gender-ideology curricula in K-12 public schools',
            'Candidate supports age-verification on pornographic content and criminal penalties for sexualized content marketed to minors',
            'Candidate supports faith-based adoption/foster agencies and opposes placement of children with same-sex couples',
        ],
    },
    {
        'id': 'christian_liberty',
        'tier': 'god_first',
        'label': 'Christian Liberty',
        'icon': 'shield-cross.png',
        'description': 'Does this candidate defend the freedom to publicly profess Christ — including the freedom of others to disagree — without state compulsion against Christian conscience?',
        'questions': [
            'Candidate affirms the right to publicly profess Christ in all spheres (workplace, military, public office, schools)',
            'Candidate supports conscience exemptions for Christian medical professionals, business owners, adoption agencies, and educators',
            'Candidate opposes compelled speech against Christian conviction (pronoun mandates, gospel-proclamation hate-speech laws)',
            'Candidate supports public-square Christian symbols, prayer in public bodies, and Sabbath/Sunday closure protections',
            'Candidate opposes state-funded promotion of non-Christian religious displays, curricula, or holidays in public institutions',
        ],
    },
    {
        'id': 'economic_stewardship',
        'tier': 'god_first',
        'label': 'Economic Stewardship',
        'icon': 'shield-handshake.png',
        'description': 'Does this candidate honor biblical economic mandates — sound money, anti-usury, debt restraint, and opposition to globalist financial capture (Prov 22:7)?',
        'questions': [
            'Candidate opposes a Central Bank Digital Currency (CBDC) and supports cash and decentralized crypto as legal tender',
            'Candidate supports sound-money policies including gold/silver as constitutional money and audit/abolition of the Federal Reserve',
            'Candidate opposes deficit spending and supports a balanced-budget constitutional amendment',
            'Candidate supports usury limits, anti-debt-slavery protections, and tithe-friendly tax structures',
            'Candidate opposes WEF/ESG/Davos economic capture and supports anti-trust action against monopolistic financial cartels',
        ],
    },
    {
        'id': 'election_integrity',
        'tier': 'god_first',
        'label': 'Election Integrity',
        'icon': 'shield-checklist-48.png',
        'description': 'Does this candidate support verifiable elections grounded in citizen accountability, free from machine manipulation, mass mail-in, or foreign interference?',
        'questions': [
            'Candidate supports hand-counted paper ballots and opposes electronic voting machines',
            'Candidate supports photo voter ID with citizenship verification',
            'Candidate supports single-day in-person voting with absentee only for verified medical/military exceptions',
            'Candidate opposes mass mail-in voting, drop boxes, and ballot harvesting',
            'Candidate opposes private election funding ("Zuckerbucks") and foreign-government election interference',
        ],
    },
    # ===== AMERICA FIRST — 40 pts =====
    {
        'id': 'border_immigration',
        'tier': 'america_first',
        'label': 'Border & Immigration',
        'icon': 'shield-map-48.png',
        'description': 'Does this candidate enforce U.S. borders, oppose illegal immigration, and defend American sovereignty over foreign claims to U.S. territory and labor?',
        'questions': [
            'Candidate supports completed physical border barrier and active military border presence',
            'Candidate supports mandatory deportation of all illegal aliens, including those who entered as minors',
            'Candidate opposes sanctuary city/state policies and supports federal preemption against them',
            'Candidate supports mandatory E-Verify for all employment and benefit eligibility',
            'Candidate opposes birthright citizenship for children of illegal aliens, tourist births, and opposes foreign ownership of U.S. farmland',
        ],
    },
    {
        'id': 'self_defense',
        'tier': 'america_first',
        'label': 'Self-Defense & 2A',
        'icon': 'shield-chain-sword-48.png',
        'description': 'Does this candidate defend the unalienable right to bear arms as a check against tyranny and a defense of household, neighbor, and homeland?',
        'questions': [
            'Candidate supports constitutional carry without permit requirements',
            'Candidate opposes red-flag laws, magazine limits, "assault weapons" bans, and gun registries',
            'Candidate supports repeal of the National Firearms Act (NFA), Gun Control Act (GCA), and other federal gun regulations',
            'Candidate supports castle doctrine and stand-your-ground laws with full civil immunity for lawful defense',
            'Candidate opposes ATF overreach, citizen disarmament initiatives, and U.N. small-arms treaty participation',
        ],
    },
    {
        'id': 'foreign_policy_restraint',
        'tier': 'america_first',
        'label': 'Foreign Policy Restraint',
        'icon': 'shield-star.png',
        'description': 'Does this candidate honor Article I war powers, oppose forever wars, and refuse foreign-lobby capture of U.S. policy?',
        'questions': [
            'Candidate supports Article I congressional war-powers requirement before any U.S. military action',
            'Candidate supports immediate withdrawal from forever wars and repeal of standing AUMFs',
            'Candidate opposes foreign aid to nations hostile to U.S. interests or actively persecuting Christians',
            'Candidate has never accepted donations from foreign-backed lobbies (e.g., AIPAC) or foreign-linked PACs',
            'Candidate opposes U.S. participation in WHO, U.N. governance overreach, NATO expansion, and supranational governance',
        ],
    },
    {
        'id': 'industry_capture',
        'tier': 'america_first',
        'label': 'Industry Capture & Sovereignty',
        'icon': 'shield-bible.png',
        'description': 'Does this candidate oppose corporate-state capture across Pharma, Big Ag, and the Military-Industrial Complex — defending citizens against cartel power?',
        'questions': [
            'Candidate opposes pharmaceutical mandates of any kind (COVID, childhood, employer-required) and supports informed consent',
            'Candidate supports repeal of pharma liability shields (1986 NCVIA, PREP Act) and restoration of tort accountability',
            'Candidate opposes Big Ag consolidation (Bayer/Monsanto/Cargill) and supports anti-trust action against agricultural cartels',
            'Candidate supports raw-milk freedom, small-farm protections, and opposes USDA / EPA overreach against family farms',
            'Candidate supports defense-contractor accountability, completion of Pentagon audits, and ending revolving-door appointments',
        ],
    },
]

# ────────────────────────────────────────────────────────────────────────────
# DATA MIGRATION MAP — old category id → new category id (where carryable)
# ────────────────────────────────────────────────────────────────────────────
CARRY_OVER = {
    'life':         'sanctity_of_life',     # 5 questions, near-identical domain
    'marriage':     'biblical_marriage',    # 5 questions, identical domain
    'self_defense': 'self_defense',         # 5 questions, identical domain
    'immigration':  'border_immigration',   # 5 questions, identical domain
}
# The remaining old categories (america_first, education, christian_heritage) get null'd —
# their questions changed too much to carry forward honestly. Two specific Qs survive:
#   america_first[3] (AIPAC) → foreign_policy_restraint[3]
#   america_first[4] (election integrity) → election_integrity[0]
SPECIFIC_CARRY = [
    ('america_first', 3, 'foreign_policy_restraint', 3),
    ('america_first', 4, 'election_integrity', 0),
]

def migrate_candidate_scores(old_scores: dict) -> dict:
    """Build a new scores dict for v2, carrying data where the domain matches."""
    new_scores = {}
    for cat in V2_CATEGORIES:
        new_scores[cat['id']] = [None, None, None, None, None]

    # Bulk carry-overs (whole arrays)
    for old_id, new_id in CARRY_OVER.items():
        old_arr = old_scores.get(old_id)
        if isinstance(old_arr, list) and len(old_arr) == 5:
            new_scores[new_id] = list(old_arr)

    # Specific question carry-overs
    for old_id, old_idx, new_id, new_idx in SPECIFIC_CARRY:
        old_arr = old_scores.get(old_id)
        if isinstance(old_arr, list) and len(old_arr) > old_idx:
            new_scores[new_id][new_idx] = old_arr[old_idx]

    return new_scores

def update_index(index_data: dict) -> dict:
    """Replace the categories array + bump meta to v2."""
    index_data['categories'] = V2_CATEGORIES
    index_data['meta']['version'] = '4.0.0'
    index_data['meta']['rubric_version'] = 'v2-god-first-america-first-100pt'
    index_data['meta']['methodology'] = (
        '10 categories × 5 true/false questions each. Each True = +2 points, '
        'each False or "no evidence found" = +0. Max per category = 10. '
        '6 God First categories (60 pts) + 4 America First categories (40 pts) = 100 pts max. '
        'The 60/40 weighting encodes the loyalty hierarchy structurally: '
        'God first, country second. Only primary sources: official campaign websites, '
        'state/federal legislature voting records, sponsored bills, official statements, '
        'and candidate X (Twitter) accounts.'
    )
    index_data['meta']['scoring_rules'] = (
        'Rejection of Neutrality: If a candidate frames the state as "neutral," "multi-faith," '
        'or "inclusive," it is a confession of refusal to acknowledge Christ\'s Lordship — '
        'ranked as failure. Evidence-First: If a candidate\'s position is purely performative '
        '(e.g., using "Judeo-Christian" rhetoric to avoid naming Christ Jesus) — ranked as failure. '
        'Subtotals: God First (60 pts max) and America First (40 pts max) are displayed separately '
        'alongside the total so readers can see whether a candidate scores by sovereignty alone '
        'or by Christian conviction alone — both gaps matter.'
    )
    return index_data

def main():
    apply = '--apply' in sys.argv
    if not apply:
        print('DRY RUN — pass --apply to write changes.\n')

    # 1. Migrate index.json
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    print('=== INDEX.JSON ===')
    print(f'Before: {len(idx["categories"])} categories (v1, 70 pts)')
    new_idx = update_index(json.loads(json.dumps(idx)))  # deep copy
    print(f'After:  {len(new_idx["categories"])} categories (v2, 100 pts)')
    print(f'  God First categories:    {sum(1 for c in new_idx["categories"] if c["tier"]=="god_first")} (60 pts)')
    print(f'  America First categories: {sum(1 for c in new_idx["categories"] if c["tier"]=="america_first")} (40 pts)')

    if apply:
        with open(INDEX_PATH, 'w') as f:
            json.dump(new_idx, f, ensure_ascii=False, indent=2)
        print(f'  → wrote {INDEX_PATH}')

    # 2. Migrate every state JSON
    print('\n=== STATE FILES ===')
    state_files = sorted(f for f in os.listdir(STATES_DIR) if f.endswith('.json'))
    tally = Counter()
    for fn in state_files:
        fp = os.path.join(STATES_DIR, fn)
        with open(fp) as f:
            sd = json.load(f)
        candidates = sd.get('candidates', [])
        for c in candidates:
            old_scores = c.get('scores', {})
            new_scores = migrate_candidate_scores(old_scores)
            c['scores'] = new_scores
            tally['candidates_migrated'] += 1
            # Count carryover quality
            answered = sum(1 for cat in new_scores.values() for v in cat if v is not None)
            if answered == 0: tally['result_all_null'] += 1
            elif answered < 25: tally['result_partial'] += 1
            else: tally['result_mostly_filled'] += 1
        if apply:
            with open(fp, 'w') as f:
                json.dump(sd, f, ensure_ascii=False, separators=(',', ':'))

    print(f'Files processed: {len(state_files)}')
    print(f'Candidates migrated: {tally["candidates_migrated"]}')
    print(f'  All-null after migration:   {tally["result_all_null"]}')
    print(f'  Partial (some data carry):  {tally["result_partial"]}')
    print(f'  Mostly filled:              {tally["result_mostly_filled"]}')

    # 3. ALSO migrate the master scorecard.json (build-data.py regenerates
    # state files FROM this; if it's not migrated too, state files revert
    # on next build).
    if os.path.exists(SCORECARD_PATH):
        print('\n=== SCORECARD.JSON (MASTER) ===')
        with open(SCORECARD_PATH) as f:
            sc = json.load(f)
        old_cat_ids = [c['id'] for c in sc.get('categories', [])]
        sc = update_index(sc)  # same meta + categories swap
        sc_migrated = 0
        for c in sc.get('candidates', []):
            old_scores = c.get('scores', {})
            new_scores = migrate_candidate_scores(old_scores)
            c['scores'] = new_scores
            sc_migrated += 1
        print(f'Migrated {sc_migrated} candidates in scorecard.json')
        print(f'Old categories: {old_cat_ids}')
        print(f'New categories: {[c["id"] for c in sc["categories"]]}')
        if apply:
            with open(SCORECARD_PATH, 'w') as f:
                json.dump(sc, f, ensure_ascii=False, separators=(',', ':'))
            print(f'  → wrote {SCORECARD_PATH}')

    if apply:
        print('\n✓ Migration applied. Run build-data.py next to verify state files match scorecard.json.')
    else:
        print('\nDry-run complete. Re-run with --apply to write.')

if __name__ == '__main__':
    main()
