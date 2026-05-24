#!/usr/bin/env python3
"""
migrate-v5-rubric-structure.py — v5.0 STAGE 1: scorecard.json rubric structure.

Adds a per-category `pillars` map encoding all three tier-specific rubrics in
one field, appends the 3 new categories, and bumps meta to v5.0. Does NOT
re-score any record — shared category scores are reused; new categories start
null. Idempotent.

Rulings (Adam delegated, 2026-05-21):
  - Federal 60/40 (unchanged) · State + Local 70/30
  - Self-Defense & 2A → Government pillar (State/Local First)
  - Election Integrity → God First in all tiers
  - Industry Capture + Foreign Policy → federal-only (dropped at state/local)
  - New: Public Justice (God First, state+local), Refuse Federal Overreach
    (State First), Refuse State Overreach (Local First)
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# Per-category pillar assignment by tier. Absence of a tier key = category is
# NOT part of that tier's rubric.
PILLARS = {
    'sanctity_of_life':          {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'biblical_marriage':         {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'family_child_sovereignty':  {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'christian_liberty':         {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'economic_stewardship':      {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'election_integrity':        {'federal': 'god_first', 'state': 'god_first', 'local': 'god_first'},
    'border_immigration':        {'federal': 'america_first', 'state': 'state_first', 'local': 'local_first'},
    'self_defense':              {'federal': 'america_first', 'state': 'state_first', 'local': 'local_first'},
    'foreign_policy_restraint':  {'federal': 'america_first'},
    'industry_capture':          {'federal': 'america_first'},
    # NEW categories
    'public_justice':            {'state': 'god_first', 'local': 'god_first'},
    'refuse_federal_overreach':  {'state': 'state_first'},
    'refuse_state_overreach':    {'local': 'local_first'},
}

NEW_CATEGORIES = [
    {
        'id': 'public_justice',
        'tier': 'god_first',  # legacy field; primary pillar
        'label': 'Public Justice & Law/Order',
        'icon': 'shield-chain-sword-48.png',
        'description': ("Does this candidate uphold the magistrate's God-ordained duty to punish "
                        "evildoers and protect the innocent (Romans 13)? Backs lawful order, "
                        "opposes soft-on-crime and rogue-prosecutor agendas, supports victim restitution."),
        'questions': [
            'Candidate has publicly backed law enforcement and opposed defunding/dismantling police',
            'Candidate opposes cashless-bail, soft-on-crime, and rogue-prosecutor (e.g. Soros-DA) policy',
            'Candidate supports victim restitution and proportional punishment of evildoers',
            'Candidate refuses to treat violent crime as a "public health" excuse to avoid punishment',
            'Candidate affirms the magistrate\'s God-ordained duty to bear the sword (Rom. 13:4)',
        ],
        'applicable_at': [['state', 'local']] * 5,
        'questions_state': [None] * 5,
        'questions_local': [None] * 5,
        'pillars': PILLARS['public_justice'],
    },
    {
        'id': 'refuse_federal_overreach',
        'tier': 'state_first',
        'label': 'Refuse Federal Overreach',
        'icon': 'shield-star.png',
        'description': ("Does this state official defend state sovereignty against unconstitutional "
                        "federal action — 10th-Amendment nullification, anti-commandeering, refusing "
                        "federal strings that compel ungodly or unconstitutional policy?"),
        'questions': [
            'Official has voted for or sponsored 10th-Amendment nullification or anti-commandeering measures',
            'Official has declined unconstitutional federal mandates or federal strings on the state',
            'Official has resisted federal overreach on guns, life, education, or religious liberty',
            'Official affirms state sovereignty against unconstitutional federal action',
            'Official has opposed federal capture of state elections, data, or land',
        ],
        'applicable_at': [['state']] * 5,
        'questions_state': [None] * 5,
        'questions_local': [None] * 5,
        'pillars': PILLARS['refuse_federal_overreach'],
    },
    {
        'id': 'refuse_state_overreach',
        'tier': 'local_first',
        'label': 'Refuse State Overreach',
        'icon': 'shield-star.png',
        'description': ("Does this local official assert lawful local control against unconstitutional "
                        "state mandates, affirm subsidiarity (decisions at the lowest competent level), "
                        "and protect citizens from state overreach?"),
        'questions': [
            'Official has asserted local control against unconstitutional state mandates',
            'Official has declined state strings that compel ungodly or unconstitutional local policy',
            'Official has protected local citizens from state overreach (lockdowns, mandates, ESG)',
            'Official affirms subsidiarity — decisions made at the lowest competent level',
            'Official has refused to enforce unconstitutional state directives',
        ],
        'applicable_at': [['local']] * 5,
        'questions_state': [None] * 5,
        'questions_local': [None] * 5,
        'pillars': PILLARS['refuse_state_overreach'],
    },
]

# meta.rubrics — documentation + machine-readable tier rubric summary
RUBRICS_META = {
    'federal': {
        'split': [60, 40], 'pillar_a_label': 'God First', 'pillar_b_label': 'America First',
        'pillar_a': ['sanctity_of_life', 'biblical_marriage', 'family_child_sovereignty',
                     'christian_liberty', 'economic_stewardship', 'election_integrity'],
        'pillar_b': ['border_immigration', 'self_defense', 'foreign_policy_restraint', 'industry_capture'],
    },
    'state': {
        'split': [70, 30], 'pillar_a_label': 'God First', 'pillar_b_label': 'State First',
        'pillar_a': ['sanctity_of_life', 'biblical_marriage', 'family_child_sovereignty',
                     'christian_liberty', 'economic_stewardship', 'election_integrity', 'public_justice'],
        'pillar_b': ['refuse_federal_overreach', 'border_immigration', 'self_defense'],
    },
    'local': {
        'split': [70, 30], 'pillar_a_label': 'God First', 'pillar_b_label': 'Local First',
        'pillar_a': ['sanctity_of_life', 'biblical_marriage', 'family_child_sovereignty',
                     'christian_liberty', 'economic_stewardship', 'election_integrity', 'public_justice'],
        'pillar_b': ['refuse_state_overreach', 'border_immigration', 'self_defense'],
    },
}


def main():
    data = json.loads(SCORECARD.read_text())
    cats = data['categories']
    existing_ids = {c['id'] for c in cats}

    # 1. Add pillars to existing categories
    added_pillars = 0
    for c in cats:
        if c['id'] in PILLARS:
            c['pillars'] = PILLARS[c['id']]
            added_pillars += 1

    # 2. Append new categories (idempotent)
    inserted = 0
    for nc in NEW_CATEGORIES:
        if nc['id'] not in existing_ids:
            cats.append(nc)
            inserted += 1

    # 3. Bump meta
    m = data['meta']
    m['version'] = '5.0.0'
    m['rubric_version'] = 'v3-tiered-rubrics'
    m['rubrics'] = RUBRICS_META
    m['methodology'] = (
        'v5.0 — THREE tier-specific rubrics, each 0-100. Federal: 10 categories, '
        '60 God First / 40 America First (6+4). State & Local: 10 categories, '
        '70 God First / 30 State|Local First (7+3). Each category = 5 T/F questions '
        '× 2 pts. True = +2, False/"no evidence" = +0, null = unscored (shrinks '
        'dynamic max, no penalty). The God First pillar weight rises from 60% '
        '(federal) to 70% (state/local) because lower offices have narrower '
        'national-issue scope, so faithfulness to Christ is proportionally more '
        'of the record. Subsidiarity is structural: Refuse Federal Overreach '
        '(state) and Refuse State Overreach (local) measure officials on authority '
        'they actually hold. Self-Defense & 2A sits in the Government pillar '
        '(citizen-vs-state sovereignty); Election Integrity stays God First (honest '
        'weights, Prov 11:1). Foreign Policy Restraint + Industry Capture are '
        'federal-only.'
    )

    SCORECARD.write_text(json.dumps(data, indent=2) + '\n')
    print(f'v5.0 structure migration complete:')
    print(f'  pillars added to {added_pillars} existing categories')
    print(f'  {inserted} new categories appended ({", ".join(n["id"] for n in NEW_CATEGORIES)})')
    print(f'  meta.version → {m["version"]}, rubric_version → {m["rubric_version"]}')
    print(f'  categories now: {len(cats)}')


if __name__ == '__main__':
    main()
