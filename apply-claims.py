#!/usr/bin/env python3
"""
apply-claims.py — promote approved proposals from data/proposed_claims.json
into the canonical claims[] array on each candidate in data/scorecard.json.

Companion to extract-claims.py. That script emits proposals with
reviewer_status="pending". A human reviewer walks the file, flips
reviewer_status to "approved" for claims they want to publish or
"rejected" for ones they want to discard, and optionally tightens
the inferred fields (category, question_idx, sources, score_impact,
text).

This script:
  1. Loads scorecard.json + proposed_claims.json.
  2. For each candidate in the proposed file, collects the
     reviewer_status="approved" proposals.
  3. Converts each approved proposal into the claim-schema shape
     used by Ship 4 and appends it to the candidate's claims[]
     array (replacing any existing entry with the same id).
  4. Merges each claim's sources into the candidate's top-level
     sources array (so they surface on the profile's Sources &
     Evidence block with bias chips).
  5. Removes approved AND rejected proposals from
     proposed_claims.json — they've either been published or
     discarded, so they shouldn't re-appear on the next run.
  6. Calls build-data.py to refresh per-state files + index.json.
  7. Prints a one-line-per-candidate summary.

Safe defaults:
  - Dry-run by default (prints what WOULD happen). Pass --apply
    to actually write.
  - Refuses to run if proposed_claims.json's _meta.scorecard_md5
    doesn't match the current scorecard.json. The reviewer's work
    assumed a specific version of the notes field; a silent drift
    could misattribute a claim. Override with --force.
  - Keeps a backup of scorecard.json at
    data/scorecard.json.pre-apply so a botched review is one
    `cp` away from rescue.

Run:
    python3 apply-claims.py                       # dry-run
    python3 apply-claims.py --apply               # actually write
    python3 apply-claims.py --apply --only VA     # restrict to one state
    python3 apply-claims.py --apply --force       # ignore md5 mismatch
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
PROPOSALS = os.path.join(REPO, 'data', 'proposed_claims.json')
BACKUP    = os.path.join(REPO, 'data', 'scorecard.json.pre-apply')

# Fields that can flow from a proposal into a claim. Anything else the
# reviewer adds to the proposal JSON is ignored on purpose — keeps the
# published claim schema tight.
CLAIM_FIELDS_FROM_PROPOSAL = (
    'text', 'kind', 'category', 'question_idx', 'score_impact',
    'sources', 'confidence', 'disputed',
)


def promote(proposal: dict, today: str) -> dict:
    """Return a published-shape claim dict derived from the proposal."""
    cat = proposal.get('category') or proposal.get('inferred_category')
    qidx = proposal.get('question_idx', proposal.get('inferred_question_idx'))
    sources = proposal.get('sources') or proposal.get('inferred_sources') or []
    claim_id = proposal.get('claim_id_suggest') or proposal.get('proposal_id')
    return {
        'id': claim_id,
        'category': cat,
        'question_idx': qidx,
        'score_impact': proposal.get('score_impact'),
        'kind': proposal.get('kind') or 'statement',
        'text': (proposal.get('text') or '').strip(),
        'sources': list(sources),
        'verified': True,
        'verified_date': today,
        'disputed': bool(proposal.get('disputed')),
        'confidence': proposal.get('confidence') or 'medium',
    }


def merge_claim(cand: dict, new_claim: dict):
    """Append or replace (by id) the claim on the candidate."""
    existing = cand.get('claims') or []
    kept = [c for c in existing if c.get('id') != new_claim['id']]
    kept.append(new_claim)
    cand['claims'] = kept
    # Also surface source URLs at the top level so the diversity strip
    # and per-link chips pick them up on the profile page.
    src = list(cand.get('sources') or [])
    for u in new_claim.get('sources') or []:
        if u and u not in src:
            src.append(u)
    cand['sources'] = src


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--apply', action='store_true',
                    help='Actually write to scorecard.json + proposed_claims.json. Default is dry-run.')
    ap.add_argument('--force', action='store_true',
                    help='Ignore the scorecard_md5 mismatch check.')
    ap.add_argument('--only', help='Restrict to candidates in this state code (e.g. VA)')
    args = ap.parse_args()

    if not os.path.exists(PROPOSALS):
        print(f'ERROR: {PROPOSALS} not found. Run extract-claims.py first.', file=sys.stderr)
        sys.exit(1)

    with open(SCORECARD, 'rb') as f:
        sc_raw = f.read()
    current_md5 = hashlib.md5(sc_raw).hexdigest()
    sc = json.loads(sc_raw.decode('utf-8'))

    with open(PROPOSALS, 'r', encoding='utf-8') as f:
        proposals_doc = json.load(f)

    expected_md5 = (proposals_doc.get('_meta') or {}).get('scorecard_md5')
    if expected_md5 and expected_md5 != current_md5:
        msg = (
            f'scorecard_md5 mismatch.\n'
            f'  proposed_claims.json was generated against {expected_md5}\n'
            f'  scorecard.json is currently           {current_md5}\n'
            'The notes field may have drifted since the proposals were made.\n'
            'Re-run extract-claims.py, re-review, and try again — or pass --force.'
        )
        if not args.force:
            print('ERROR: ' + msg, file=sys.stderr)
            sys.exit(2)
        print('WARNING: ' + msg, file=sys.stderr)

    # Index candidates by (slug, state) for quick lookup.
    cand_idx = {}
    for c in sc.get('candidates') or []:
        key = (c.get('slug'), c.get('state'))
        cand_idx[key] = c

    today = date.today().isoformat()
    per_candidate_summary = []
    approved_count = 0
    rejected_count = 0
    pending_count = 0
    remaining_candidates = []

    for cand_entry in proposals_doc.get('candidates') or []:
        slug = cand_entry.get('slug')
        state = cand_entry.get('state')
        if args.only and state != args.only:
            remaining_candidates.append(cand_entry)
            continue

        approved = []
        rejected = []
        pending = []
        for p in cand_entry.get('proposed_claims') or []:
            status = (p.get('reviewer_status') or 'pending').lower()
            if status == 'approved':
                approved.append(p)
            elif status == 'rejected':
                rejected.append(p)
            else:
                pending.append(p)

        approved_count += len(approved)
        rejected_count += len(rejected)
        pending_count += len(pending)

        if approved:
            cand = cand_idx.get((slug, state))
            if cand is None:
                print(f'WARN: approved claims for {slug}/{state} but candidate not found; skipping', file=sys.stderr)
            else:
                for p in approved:
                    claim = promote(p, today)
                    if args.apply:
                        merge_claim(cand, claim)
                per_candidate_summary.append(
                    f'{state}/{slug}: +{len(approved)} approved'
                    + (f', -{len(rejected)} rejected' if rejected else '')
                )

        # Retain only still-pending items for the next review pass; if
        # there are none left, drop the candidate from the proposals
        # file entirely.
        if pending:
            new_entry = dict(cand_entry)
            new_entry['proposed_claims'] = pending
            remaining_candidates.append(new_entry)

    print('\n=== Summary ===')
    print(f'  Approved:  {approved_count}')
    print(f'  Rejected:  {rejected_count}')
    print(f'  Pending:   {pending_count}')
    for line in per_candidate_summary:
        print(f'  • {line}')

    if not args.apply:
        print('\n(dry-run) Re-run with --apply to write changes.')
        return

    if approved_count == 0 and rejected_count == 0:
        print('\nNothing to apply; scorecard untouched.')
        return

    # Backup and write scorecard + updated proposals.
    shutil.copyfile(SCORECARD, BACKUP)
    print(f'\nBackup: {BACKUP}')

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'Wrote  {SCORECARD}')

    new_meta = dict(proposals_doc.get('_meta') or {})
    new_meta['last_applied'] = datetime.now(timezone.utc).isoformat()
    new_meta['last_applied_summary'] = {
        'approved': approved_count,
        'rejected': rejected_count,
        'pending_retained': pending_count,
    }
    proposals_doc['_meta'] = new_meta
    proposals_doc['candidates'] = remaining_candidates
    with open(PROPOSALS, 'w', encoding='utf-8') as f:
        json.dump(proposals_doc, f, indent=2, ensure_ascii=False)
    print(f'Wrote  {PROPOSALS}')

    # Regenerate per-state files + index.json so the UI stays in sync.
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)
    print('\nDone. Run generate-profiles.py to rebuild candidate HTMLs.')


if __name__ == '__main__':
    main()
