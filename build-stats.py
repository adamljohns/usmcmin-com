#!/usr/bin/env python3
"""
build-stats.py — compute aggregate coverage metrics across every data
source in the repo and emit data/stats.json.

The /stats.html page fetches this JSON and renders. Run this any time
data shifts materially (after scorecard edits, new photos, new
claims, new bias entries); it's cheap — single-digit seconds on the
full corpus.

Sections:
  totals            — candidates, states, distinct offices, claims,
                      verified claims, sources, unique domains.
  photos            — photo coverage (on disk + referenced in data).
  federal_contact   — DC phone, contact form, bioguide, twitter,
                      facebook, youtube, district offices.
  notes_coverage    — non-empty notes, org ratings detected, election
                      countdown populated.
  states            — per-state candidate count + photo pct + claim
                      count + notes pct.
  source_diversity  — aggregate tone breakdown across every cited URL.
  bias_coverage     — domains in source_bias.json, citation coverage pct.
  data_files        — file sizes and last-modified for the major JSONs.
  last_updated      — ISO timestamp.
"""
from __future__ import annotations

import collections
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(REPO, 'data')

# Reuse the helper for bias resolution.
sys.path.insert(0, REPO)
import source_bias as sb  # noqa: E402


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def fsize(path):
    try:
        st = os.stat(path)
        return {'bytes': st.st_size, 'mtime': datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat()}
    except FileNotFoundError:
        return None


def compute():
    sc = load(os.path.join(DATA, 'scorecard.json'))
    bias = load(os.path.join(DATA, 'source_bias.json'))

    try:
        proposed = load(os.path.join(DATA, 'proposed_claims.json'))
    except FileNotFoundError:
        proposed = None

    candidates = sc.get('candidates') or []
    n_cands = len(candidates)
    states = sorted({c.get('state') for c in candidates if c.get('state')})

    # Photo coverage — count references that point at a file that exists.
    photos_on_disk = 0
    photos_dir = os.path.join(REPO, 'assets', 'photos')
    if os.path.isdir(photos_dir):
        for root, _, files in os.walk(photos_dir):
            photos_on_disk += sum(1 for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')))

    with_photo_ref = 0
    with_photo_actual = 0
    for c in candidates:
        p = c.get('photo')
        if p:
            with_photo_ref += 1
            # relative to repo root
            full = os.path.join(REPO, p)
            if os.path.isfile(full):
                with_photo_actual += 1

    # Federal contact enrichment applies only to level=federal
    # (U.S. Senate + U.S. House members; excludes state Senate etc.).
    fed = [c for c in candidates if c.get('level') == 'federal']
    with_phone = sum(1 for c in fed if (c.get('profile') or {}).get('phone'))
    with_contact_form = sum(1 for c in fed if (c.get('profile') or {}).get('contact_form'))
    with_bioguide = sum(1 for c in fed if (c.get('profile') or {}).get('bioguide'))
    with_twitter = sum(1 for c in fed if (c.get('profile') or {}).get('twitter'))
    with_facebook = sum(1 for c in fed if (c.get('profile') or {}).get('facebook'))
    with_youtube = sum(1 for c in fed if (c.get('profile') or {}).get('youtube'))
    with_district_office = sum(1 for c in fed if (c.get('profile') or {}).get('district_offices'))

    # Notes + election enrichment.
    with_notes = 0
    for c in candidates:
        n = c.get('notes')
        if isinstance(n, str) and n.strip():
            with_notes += 1
        elif isinstance(n, (dict, list)) and n:
            with_notes += 1
    with_next_election = sum(1 for c in candidates if (c.get('profile') or {}).get('next_election_date'))
    with_twitter_any = sum(1 for c in candidates if (c.get('profile') or {}).get('twitter'))
    # Org ratings: candidate has a source URL in a known ratings domain.
    RATING_DOMS = {'heritageaction.com', 'plannedparenthoodaction.org',
                   'nrapvf.org', 'aclu.org', 'reportcard.familyfoundation.org',
                   'freedomindex.us', 'thefreedomindex.org', 'index.idahofreedom.org',
                   'txvaluesaction.org', 'texasrighttolife.com', 'vcdl.org',
                   'tsrapac.com'}
    with_org_rating = 0
    for c in candidates:
        for u in c.get('sources') or []:
            host = u.split('://')[-1].split('/')[0].lower().removeprefix('www.')
            if host in RATING_DOMS or any(host.endswith('.' + d) for d in RATING_DOMS):
                with_org_rating += 1
                break

    # Claims aggregate.
    total_claims = 0
    verified_claims = 0
    disputed_claims = 0
    candidates_with_claims = 0
    claims_by_category = collections.Counter()
    claims_by_kind = collections.Counter()
    for c in candidates:
        cls = c.get('claims') or []
        if cls:
            candidates_with_claims += 1
            total_claims += len(cls)
            for cl in cls:
                if cl.get('verified'):
                    verified_claims += 1
                if cl.get('disputed'):
                    disputed_claims += 1
                claims_by_category[cl.get('category') or 'unknown'] += 1
                claims_by_kind[cl.get('kind') or 'statement'] += 1

    # Scoring-confidence distribution. The three tiers are:
    #   evidence_reviewed — the candidate has at least one verified claim,
    #                       OR profile.confidence is explicitly not
    #                       "party_default" (e.g., unset means the record
    #                       predates the confidence-tagging era).
    #   party_default     — profile.confidence == "party_default" and the
    #                       record has no verified claims yet. These
    #                       render the amber banner in the profile UI.
    #   unreviewed        — no claims, no explicit confidence, and the
    #                       entire scores matrix is all-null (i.e., a
    #                       true placeholder awaiting data).
    confidence_counts = collections.Counter()
    for c in candidates:
        cls = c.get('claims') or []
        conf = (c.get('profile') or {}).get('confidence') or ''
        has_verified = any(cl.get('verified') for cl in cls)
        # Detect all-null scores
        scores = c.get('scores') or {}
        all_null = all(
            all(x is None for x in (scores.get(cat) or [None]))
            for cat in scores
        ) if scores else True
        if has_verified:
            confidence_counts['evidence_reviewed'] += 1
        elif conf == 'party_default':
            confidence_counts['party_default'] += 1
        elif all_null:
            confidence_counts['unreviewed'] += 1
        else:
            confidence_counts['legacy_reviewed'] += 1

    # Source diversity aggregate. Track two different classification
    # metrics so the UI can report both:
    #   * bias_citation_coverage_pct — citations whose domain has an
    #     exact or parent match in source_bias.json. Misses rule-
    #     based *.gov fallbacks.
    #   * tone_classification_pct — citations that get a meaningful
    #     chip at all (including *.gov/*.house.gov rule fallbacks
    #     which render as "Official"). This is the number that
    #     matches what a visitor actually sees on a profile page.
    tone_counts = collections.Counter()
    all_sources_total = 0
    unique_sources = set()
    unique_domains = collections.Counter()
    rule_classified_citations = 0
    unclassified_citations = 0
    for c in candidates:
        for u in c.get('sources') or []:
            all_sources_total += 1
            unique_sources.add(u)
            host = u.split('://')[-1].split('/')[0].lower().removeprefix('www.')
            unique_domains[host] += 1
            entry = sb.resolve(u)
            tone_counts[sb.badge_tone(entry)] += 1
            match = entry.get('_match', 'none')
            if match.startswith('rule:'):
                rule_classified_citations += 1
            elif match == 'none':
                unclassified_citations += 1

    # Bias coverage.
    bias_domains = set(bias.get('domains', {}).keys())
    cited_domains_covered = sum(1 for d in unique_domains if d in bias_domains)

    # Per-state stats.
    per_state = []
    for st in states:
        st_cands = [c for c in candidates if c.get('state') == st]
        st_photos = sum(1 for c in st_cands
                        if c.get('photo') and os.path.isfile(os.path.join(REPO, c['photo'])))
        st_notes = sum(1 for c in st_cands if (isinstance(c.get('notes'), str) and c['notes'].strip())
                       or (isinstance(c.get('notes'), (dict, list)) and c.get('notes')))
        st_claims = sum(len(c.get('claims') or []) for c in st_cands)
        per_state.append({
            'state': st,
            'candidates': len(st_cands),
            'with_photo': st_photos,
            'with_notes': st_notes,
            'claims': st_claims,
            'photo_pct': round(100.0 * st_photos / max(1, len(st_cands)), 1),
            'notes_pct': round(100.0 * st_notes / max(1, len(st_cands)), 1),
        })
    per_state.sort(key=lambda x: -x['candidates'])

    # Data-file footprint.
    data_files = {}
    for fn in ['scorecard.json', 'source_bias.json', 'proposed_claims.json',
               'zips.json', 'places.json', 'elections.json', 'index.json', 'issues.json']:
        info = fsize(os.path.join(DATA, fn))
        if info:
            data_files[fn] = info

    # Proposed-claim status breakdown (if file present).
    proposed_summary = None
    if proposed:
        pending = approved = rejected = 0
        for ce in proposed.get('candidates') or []:
            for p in ce.get('proposed_claims') or []:
                s = (p.get('reviewer_status') or 'pending').lower()
                if s == 'pending':
                    pending += 1
                elif s == 'approved':
                    approved += 1
                elif s == 'rejected':
                    rejected += 1
        proposed_summary = {
            'total': pending + approved + rejected,
            'pending': pending,
            'approved_waiting_apply': approved,
            'rejected_waiting_apply': rejected,
            'candidates': len(proposed.get('candidates') or []),
        }

    return {
        '_meta': {
            'generated': datetime.now(timezone.utc).isoformat(),
            'script': 'build-stats.py',
            'scorecard_md5': hashlib.md5(json.dumps(sc, sort_keys=True).encode('utf-8')).hexdigest(),
            'scorecard_version': (sc.get('meta') or {}).get('version'),
        },
        'totals': {
            'candidates': n_cands,
            'states_covered': len(states),
            'distinct_offices': len({c.get('office') for c in candidates if c.get('office')}),
            'candidates_with_claims': candidates_with_claims,
            'total_claims': total_claims,
            'verified_claims': verified_claims,
            'disputed_claims': disputed_claims,
            'all_sources_total': all_sources_total,
            'unique_source_urls': len(unique_sources),
            'unique_cited_domains': len(unique_domains),
            'bias_entries': len(bias_domains),
            'bias_citation_coverage_pct': round(100.0 * sum(n for d, n in unique_domains.items() if d in bias_domains) / max(1, all_sources_total), 1),
            'bias_domain_coverage_pct': round(100.0 * cited_domains_covered / max(1, len(unique_domains)), 1),
            'tone_classification_pct': round(100.0 * (all_sources_total - unclassified_citations) / max(1, all_sources_total), 1),
            'rule_classified_citations': rule_classified_citations,
            'unclassified_citations': unclassified_citations,
        },
        'photos': {
            'files_on_disk': photos_on_disk,
            'candidates_with_reference': with_photo_ref,
            'candidates_with_actual_file': with_photo_actual,
            'coverage_pct': round(100.0 * with_photo_actual / max(1, n_cands), 1),
        },
        'federal_contact': {
            'federal_candidates_scanned': len(fed),
            'with_direct_phone': with_phone,
            'with_contact_form': with_contact_form,
            'with_bioguide_id': with_bioguide,
            'with_twitter': with_twitter,
            'with_facebook': with_facebook,
            'with_youtube': with_youtube,
            'with_district_offices': with_district_office,
        },
        'notes_coverage': {
            'with_notes': with_notes,
            'with_next_election_date': with_next_election,
            'with_twitter_anywhere': with_twitter_any,
            'with_org_rating_source': with_org_rating,
            'notes_pct': round(100.0 * with_notes / max(1, n_cands), 1),
        },
        'source_diversity': dict(tone_counts),
        'claims_by_category': dict(claims_by_category),
        'claims_by_kind': dict(claims_by_kind),
        'scoring_confidence': dict(confidence_counts),
        'per_state': per_state,
        'proposed_claims': proposed_summary,
        'data_files': data_files,
    }


def main():
    doc = compute()
    out_path = os.path.join(DATA, 'stats.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    t = doc['totals']
    print(
        f"Wrote {out_path}: "
        f"{t['candidates']} candidates, {t['states_covered']} states, "
        f"{t['total_claims']} claims, "
        f"bias coverage {t['bias_citation_coverage_pct']}% of citations."
    )


if __name__ == '__main__':
    main()
