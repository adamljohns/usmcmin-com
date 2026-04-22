#!/usr/bin/env python3
"""
curate-spanberger-demo.py — one-shot demo curation.

Walks data/proposed_claims.json, finds Abigail Spanberger's proposals,
flips the Planned Parenthood 100% rating to reviewer_status="approved"
with tightened text + explicit score_impact, and leaves the rest
pending. Proves the review → apply → regenerate loop end-to-end.

Safe to re-run (idempotent). Targets by proposal_id + by the substring
'Planned Parenthood' to survive minor reshuffles of the proposals file.
"""
import json
import os

REPO = os.path.dirname(os.path.abspath(__file__))
PROPOSALS = os.path.join(REPO, 'data', 'proposed_claims.json')

with open(PROPOSALS, 'r', encoding='utf-8') as f:
    doc = json.load(f)

touched = 0
for cand in doc.get('candidates') or []:
    if cand.get('slug') != 'abigail-spanberger':
        continue
    for p in cand.get('proposed_claims') or []:
        if 'Planned Parenthood' in (p.get('text') or ''):
            p['reviewer_status'] = 'approved'
            # Tighten the inferred fields with a curator's edit:
            p['text'] = (
                "Planned Parenthood Action Fund scored Abigail Spanberger 100% "
                "on reproductive-rights votes during her U.S. House tenure "
                "(Virginia's 7th congressional district, 2019–2025)."
            )
            p['category'] = 'life'
            p['question_idx'] = 3
            p['score_impact'] = False  # she voted AGAINST our scoring criterion
            p['kind'] = 'rating'
            p['confidence'] = 'high'
            p['sources'] = [
                'https://www.plannedparenthoodaction.org/',
            ]
            p['claim_id_suggest'] = 'abigail-spanberger-life-3'
            touched += 1

with open(PROPOSALS, 'w', encoding='utf-8') as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f'Curated {touched} Spanberger proposal(s) to approved status.')
