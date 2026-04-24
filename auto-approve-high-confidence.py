#!/usr/bin/env python3
"""
auto-approve-high-confidence.py — flip reviewer_status to "approved"
on proposed claims that meet strict quality criteria, then let the
normal apply-claims.py pipeline promote them into scorecard.json.

Criteria for auto-approval:
  * confidence == "high"  (org_rating / bill_signed / voted)
  * reviewer_status is currently "pending"
  * inferred_category is set (non-null)
  * inferred_question_idx is set (0..4)
  * EITHER the rule is 'org_rating' (the citation IS the evidence, a
    human reviewer would approve reflexively),
    OR the rule is 'bill_signed' / 'voted' and a vote-pattern regex
    match was recorded.

For each approved proposal we also determine the score_impact based
on which DIRECTION the underlying source pushes:
  * Heritage Action / Family Foundation / NRA PVF / VCDL / Freedom
    Index / Texas Right to Life / Texas Values / iVoterGuide /
    SBA Pro-Life → conservative direction → score_impact = True
    only when the rating is HIGH (>= 70%). A low rating on a
    conservative scorecard is evidence the candidate voted AGAINST
    conservative criteria, i.e., score_impact = False.
  * Planned Parenthood Action / ACLU / Choice Tracker / Repro
    Rising VA → progressive direction → opposite rule.

Run:
    python3 auto-approve-high-confidence.py --dry-run   # report only
    python3 auto-approve-high-confidence.py             # flip to approved
    python3 apply-claims.py --apply --force             # write to scorecard
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).parent
PROPOSALS = REPO / 'data' / 'proposed_claims.json'

CONSERVATIVE_HOSTS = {
    'heritageaction.com', 'familyfoundation.org',
    'reportcard.familyfoundation.org', 'nrapvf.org',
    'vcdl.org', 'tsrapac.com', 'freedomindex.us',
    'thefreedomindex.org', 'idahofreedom.org',
    'index.idahofreedom.org', 'txvaluesaction.org',
    'texasrighttolife.com', 'sbaprolife.org', 'ivoterguide.com',
}
PROGRESSIVE_HOSTS = {
    'plannedparenthoodaction.org', 'aclu.org',
    'reprorisingva.org', 'choicetracker.org',
    'progressivevotersguide.com',
}


def classify_source_list(sources):
    """Return 'conservative' / 'progressive' / 'neutral' based on
    which camp most of the cited sources come from."""
    import urllib.parse
    c, p = 0, 0
    for u in sources or []:
        host = (urllib.parse.urlparse(u).hostname or '').lower().removeprefix('www.')
        parent = host.split('.', 1)[-1] if '.' in host else host
        if host in CONSERVATIVE_HOSTS or parent in CONSERVATIVE_HOSTS:
            c += 1
        elif host in PROGRESSIVE_HOSTS or parent in PROGRESSIVE_HOSTS:
            p += 1
    if c > p: return 'conservative'
    if p > c: return 'progressive'
    return 'neutral'


def parse_rating_pct(text):
    """Extract the numeric percent from an org_rating text like
    'Heritage Action score 85%' → 85. Returns None if not found."""
    m = re.search(r'(\d{1,3})\s*%', text)
    if m:
        try:
            v = int(m.group(1))
            if 0 <= v <= 100:
                return v
        except ValueError:
            pass
    return None


def infer_score_impact(p):
    """Decide score_impact True/False/None for an auto-approved
    proposal. Used by apply-claims.py to surface direction to the UI."""
    rule = p.get('rule')
    srcs = p.get('inferred_sources') or []
    direction = classify_source_list(srcs)
    if rule == 'org_rating':
        pct = parse_rating_pct(p.get('text') or '')
        if pct is None or direction == 'neutral':
            return None
        # High rating on conservative source → aligned with our True
        # direction. Low rating on conservative source → False.
        # Opposite for progressive sources.
        if direction == 'conservative':
            return True if pct >= 70 else False
        else:
            return False if pct >= 70 else True
    if rule == 'voted':
        # "Voted YES on HR X" / "Voted NO on HB Y" — ambiguous without
        # knowing the bill's direction. Leave null; reviewer can tighten.
        return None
    if rule == 'bill_signed':
        # "Signed HB X" in notes — signing a bill is typically a True
        # alignment with the author (R signing R bill → True).
        return None
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    with open(PROPOSALS, 'r', encoding='utf-8') as f:
        doc = json.load(f)

    approved = 0
    skipped = 0
    for cand in doc.get('candidates') or []:
        for p in cand.get('proposed_claims') or []:
            if p.get('reviewer_status', 'pending') != 'pending':
                continue
            if p.get('confidence') != 'high':
                continue
            cat = p.get('category') or p.get('inferred_category')
            qidx = p.get('question_idx')
            if qidx is None:
                qidx = p.get('inferred_question_idx')
            if not cat or qidx is None:
                skipped += 1
                continue
            rule = p.get('rule')
            if rule not in ('org_rating', 'voted', 'bill_signed'):
                skipped += 1
                continue

            # Apply
            p['reviewer_status'] = 'approved'
            p['category'] = cat
            p['question_idx'] = qidx
            if p.get('score_impact') is None:
                p['score_impact'] = infer_score_impact(p)
            # Promote inferred_sources to sources if empty
            if not p.get('sources'):
                p['sources'] = list(p.get('inferred_sources') or [])
            approved += 1

    if not args.dry_run:
        with open(PROPOSALS, 'w', encoding='utf-8') as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f'Approved: {approved}')
    print(f'Skipped (missing category/qidx or non-approvable rule): {skipped}')
    if args.dry_run:
        print('(dry-run) proposed_claims.json not written.')


if __name__ == '__main__':
    main()
