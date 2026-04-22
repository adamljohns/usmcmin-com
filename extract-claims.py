#!/usr/bin/env python3
"""
extract-claims.py — propose atomic claims for every candidate whose
`notes` field is non-empty, and dump them to data/proposed_claims.json
for Adam's review.

Does NOT write to scorecard.json. By design. The output is a review
file. A follow-up step (apply-claims.py or a manual pass) promotes
approved proposals into the canonical claims[] array on each
candidate.

Pipeline per candidate:
  1. Normalize notes (str or dict → list[str]).
  2. Split on sentence boundaries, respecting common abbreviations.
  3. For each sentence, apply pattern detectors to extract:
       - organization ratings (Heritage Action, Planned Parenthood,
         NRA PVF, ACLU, Family Foundation, Freedom Index) → claim
       - bill actions (voted YES/NO on X, signed X, vetoed X) → claim
       - explicit policy statements (supports X, opposes X) → claim
       - endorsement statements → claim (kind=endorsement)
       - generic residual sentences → claim (kind=statement, low conf)
  4. Infer (category, question_idx) from keywords in the claim text.
  5. Match candidate's existing `sources` URLs to the claim by topic.

The emitted schema matches what Ship 4 added to scorecard.json. A
reviewer can:
  - copy a proposed claim block into scorecard.json verbatim, OR
  - delete a false positive,
  - edit text / sources / inferences in place
then run the (not-yet-built) apply step.

Run:
    python3 extract-claims.py             # scans all 899 noted candidates
    python3 extract-claims.py --only VA   # restrict to one state
    python3 extract-claims.py --limit 50  # cap for quick iteration
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Optional

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
OUTPUT = os.path.join(REPO, 'data', 'proposed_claims.json')

CATEGORY_KEYWORDS = {
    'life': [
        ('abortion', 2),
        ('abortion rights', 2),
        ('pro-choice', 3),
        ('pro-life', 2),
        ('planned parenthood', 3),
        ('heartbeat', 2),
        ('15-week', 2),
        ('6-week', 2),
        ('fetal', 2),
        ('dobbs', 2),
        ('roe', 2),
    ],
    'self_defense': [
        ('second amendment', 1),
        ('2nd amendment', 1),
        ('2a', 1),
        ('gun control', 3),
        ('gun rights', 0),
        ('constitutional carry', 3),
        ('concealed carry', 3),
        ('red flag', 3),
        ('assault weapons ban', 3),
        ('nra', 1),
        ('castle doctrine', 2),
        ('stand-your-ground', 2),
        ('stand your ground', 2),
        ('firearm', 1),
    ],
    'marriage': [
        ('same-sex marriage', 0),
        ('homosexual', 1),
        ('transgender', 2),
        ('gender ideology', 2),
        ('gender-affirming', 2),
        ('trans kid', 2),
        ('biological sex', 2),
        ('parental rights', 3),
        ('sodomy', 4),
        ('sexual orientation', 3),
        ('drag show', 3),
        ('pride month', 3),
    ],
    'immigration': [
        ('illegal immigration', 1),
        ('illegal aliens', 1),
        ('illegal immigrants', 1),
        ('border wall', 0),
        ('ice cooperation', 1),
        ('ice ', 1),
        ('e-verify', 1),
        ('deport', 1),
        ('sanctuary', 1),
        ('asylum', 0),
        ('daca', 1),
        ('anchor baby', 2),
        ('h-1b', 4),
        ('immigrat', 0),
    ],
    'education': [
        ('school choice', 0),
        ('voucher', 0),
        ('homeschool', 0),
        ('private school', 0),
        ('crt', 2),
        ('critical race theory', 2),
        ('dei ', 2),
        ('diversity equity', 2),
        ('stop woke', 2),
        ('school prayer', 3),
        ('sex education', 4),
        ('sex-ed', 4),
        ('bible in school', 3),
        ('library book', 1),
        ('book ban', 1),
    ],
    'america_first': [
        ('america first', None),
        ('heritage action', None),
        ('foreign aid', 1),
        ('aipac', 3),
        ('foreign donation', 3),
        ('paper ballot', 4),
        ('voter id', 4),
        ('election integrity', 4),
        ('voting machine', 4),
        ('mail-in ballot', 4),
        ('absentee ballot', 4),
    ],
    'christian_heritage': [
        ('christian nation', 0),
        ('christian nationalism', 0),
        ('ten commandments', 1),
        ('blasphemy', 3),
        ('biblical law', 4),
        ('christian magistrate', 0),
        ('kingdom of christ', 0),
    ],
}

# Source-matching keywords: if a claim's text contains one of these
# substrings and the candidate has a source URL whose host contains
# the matching domain fragment, auto-attach that URL to the claim.
SOURCE_MATCH = [
    ('heritage action', 'heritageaction.com'),
    ('planned parenthood', 'plannedparenthoodaction.org'),
    ('nra', 'nrapvf.org'),
    ('aclu', 'aclu.org'),
    ('family foundation', 'familyfoundation.org'),
    ('freedom index', 'freedomindex.us'),
    ('vcdl', 'vcdl.org'),
    ('texas right to life', 'texasrighttolife.com'),
    ('texas values', 'txvaluesaction.org'),
    ('idaho freedom', 'idahofreedom.org'),
    ('tsra', 'tsrapac.com'),
    ('choice tracker', 'choicetracker.org'),
    ('ballotpedia', 'ballotpedia.org'),
    ('vote smart', 'votesmart.org'),
]

# Patterns that lift a single atomic fact from a sentence and label it.
# Each rule: (name, regex, kind, confidence). Only the first match per
# sentence is recorded; residuals fall through to the "statement" rule.
RULES = [
    (
        'org_rating',
        re.compile(r'\b(Heritage Action|Planned Parenthood( Action)?|NRA( PVF)?|ACLU|Family Foundation|Freedom Index|Texas Values|Texas Right to Life|VCDL|Idaho Freedom|TSRA)\s+(score\s+)?(\d+)\s*%', re.IGNORECASE),
        'rating', 'high',
    ),
    (
        'bill_signed',
        re.compile(r'\b(signed|vetoed|co-sponsored|introduced|sponsored|supported passage of|opposed)\s+(HB|SB|HR|S\.|H\.)\s*[\dA-Z\.\-/ ]+\b', re.IGNORECASE),
        'vote', 'high',
    ),
    (
        'voted',
        re.compile(r'\bvoted\s+(YES|NO|aye|nay|against|for)\b[^.]*', re.IGNORECASE),
        'vote', 'high',
    ),
    (
        'endorsement',
        re.compile(r'\b(endorsed|endorsement|endorses)\b[^.]*', re.IGNORECASE),
        'endorsement', 'medium',
    ),
    (
        'policy_support',
        re.compile(r'\b(supports|opposes|advocates|favors|backs|rejects)\b[^.]*', re.IGNORECASE),
        'policy', 'medium',
    ),
]

ABBREV = [
    'Sen.', 'Rep.', 'Gov.', 'Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.',
    'Jr.', 'Sr.', 'U.S.', 'D.C.', 'vs.', 'Inc.', 'Co.', 'No.',
    'H.R.', 'S.', 'H.J. Res.', 'S.J. Res.', 'p.m.', 'a.m.',
    'i.e.', 'e.g.', 'etc.',
]
# Pre-mask abbreviations so sentence split on ". " doesn't chop them.
_ABBREV_TABLE = [(a, a.replace('.', '§')) for a in ABBREV]
SENTENCE_BOUNDARY = re.compile(r'(?<=[.!?])\s+(?=[A-Z("0-9])')


def split_sentences(text: str) -> list:
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return []
    masked = text
    for orig, masked_form in _ABBREV_TABLE:
        masked = masked.replace(orig, masked_form)
    parts = SENTENCE_BOUNDARY.split(masked)
    out = []
    for p in parts:
        # Restore abbreviations
        for orig, masked_form in _ABBREV_TABLE:
            p = p.replace(masked_form, orig)
        p = p.strip()
        if p:
            out.append(p)
    return out


def infer_category_and_question(text: str) -> tuple:
    low = text.lower()
    best = (None, None, 0)
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw, qidx in keywords:
            if kw in low:
                weight = len(kw)
                if weight > best[2]:
                    best = (cat, qidx, weight)
    return best[0], best[1]


def match_sources(text: str, candidate_sources: list) -> list:
    low = text.lower()
    attached = []
    for keyword, domain_frag in SOURCE_MATCH:
        if keyword in low:
            for s in candidate_sources or []:
                if domain_frag in s and s not in attached:
                    attached.append(s)
    return attached


def normalize_notes(notes) -> list:
    if notes is None:
        return []
    if isinstance(notes, str):
        return [notes.strip()] if notes.strip() else []
    if isinstance(notes, dict):
        out = []
        for v in notes.values():
            if isinstance(v, str) and v.strip():
                out.append(v.strip())
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, str) and item.strip():
                        out.append(item.strip())
        return out
    if isinstance(notes, list):
        return [str(x).strip() for x in notes if str(x).strip()]
    return []


def propose_for_candidate(c: dict) -> list:
    notes_blobs = normalize_notes(c.get('notes'))
    if not notes_blobs:
        return []
    sources = c.get('sources') or []
    proposals = []
    proposal_idx = 0

    for blob in notes_blobs:
        for sent in split_sentences(blob):
            rule_name = 'statement'
            kind = 'statement'
            confidence = 'low'
            match_text = None
            for (rname, regex, rkind, rconf) in RULES:
                m = regex.search(sent)
                if m:
                    rule_name = rname
                    kind = rkind
                    confidence = rconf
                    match_text = m.group(0)
                    break

            cat, qidx = infer_category_and_question(sent)
            attached_sources = match_sources(sent, sources)

            proposal_idx += 1
            pid = f"{c.get('slug','unknown')}-p{proposal_idx}"
            proposal = {
                'proposal_id': pid,
                'claim_id_suggest': f"{c.get('slug','unknown')}-{cat}-{qidx}" if (cat and qidx is not None) else pid,
                'text': sent,
                'matched_phrase': match_text,
                'rule': rule_name,
                'kind': kind,
                'confidence': confidence,
                'inferred_category': cat,
                'inferred_question_idx': qidx,
                'inferred_sources': attached_sources,
                'score_impact': None,
                'verified': False,
                'verified_date': None,
                'disputed': False,
                'reviewer_status': 'pending',
            }
            proposals.append(proposal)

    return proposals


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--only', help='Restrict to candidates from this state code (e.g. VA)')
    ap.add_argument('--limit', type=int, help='Cap number of candidates processed')
    ap.add_argument('--output', default=OUTPUT, help='Override output path')
    args = ap.parse_args()

    with open(SCORECARD, 'r', encoding='utf-8') as f:
        raw = f.read()
    sc = json.loads(raw)
    md5 = hashlib.md5(raw.encode('utf-8')).hexdigest()

    candidates = sc.get('candidates') or []
    if args.only:
        candidates = [c for c in candidates if c.get('state') == args.only]
    if args.limit:
        candidates = candidates[:args.limit]

    out_candidates = []
    total_proposals = 0
    for c in candidates:
        # Skip candidates that already have curated claims — don't
        # second-guess human work.
        if c.get('claims'):
            continue
        proposals = propose_for_candidate(c)
        if not proposals:
            continue
        out_candidates.append({
            'slug': c.get('slug'),
            'state': c.get('state'),
            'name': c.get('name'),
            'office': c.get('office'),
            'party': c.get('party'),
            'existing_notes': c.get('notes'),
            'existing_sources': c.get('sources') or [],
            'proposed_claims': proposals,
        })
        total_proposals += len(proposals)

    output_doc = {
        '_meta': {
            'generated': datetime.now(timezone.utc).isoformat(),
            'script_version': '1.0.0',
            'scorecard_md5': md5,
            'candidates_scanned': len(candidates),
            'candidates_with_proposals': len(out_candidates),
            'total_proposals': total_proposals,
            'flags': vars(args),
            'how_to_review': (
                'Open this file and walk the candidates list. For each proposed_claim, '
                'set reviewer_status to "approved" or "rejected"; tighten text, '
                'category, question_idx, sources if needed. Future apply-claims.py '
                'will pick up reviewer_status="approved" items and merge them into '
                'scorecard.json under each candidate\'s claims[] array with '
                'verified_date=today and confidence copied forward. Items you '
                'do not touch stay pending; they are re-proposed on the next run.'
            ),
            'categories_available': list(CATEGORY_KEYWORDS.keys()),
        },
        'candidates': out_candidates,
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output_doc, f, indent=2, ensure_ascii=False)

    print(
        f'Scanned {len(candidates)} candidate(s); proposed '
        f'{total_proposals} claim(s) across {len(out_candidates)} candidate(s). '
        f'Wrote {args.output}.',
        file=sys.stderr,
    )


if __name__ == '__main__':
    main()
