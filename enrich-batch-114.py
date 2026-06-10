#!/usr/bin/env python3
"""Enrichment batch 114: no-op — archetype_curated federal bucket exhausted.

Confirmed again on 2026-06-10. The three remaining archetype_curated
0-claims entries are all unenrichable:

  • Joe Mazzola (MA, R, joe-mazzola-ma-senate) — does not appear in the
    official 2026 MA U.S. Senate Republican primary candidate lists (only
    Nathan Bech and John Deaton are tracked by Ballotpedia/Wikipedia); no
    policy positions findable via WebSearch.

  • Drew Wilson (FL, R, drew-wilson-fl-02) — not among the officially-filed
    FL-02 Republican primary candidates (Evan Power, Nick Lewis, Keith Gross,
    Austin Rogers, Audie Rowell, Luke Murphy, Jim Norton per WCTV/Ballotpedia);
    no verifiable public record or policy positions found.

  • Bernadette Sanchez (NM, D, bernadette-sanchez-sos) — did not appear in
    the June 2, 2026 NM Secretary of State Democratic primary (field was
    Katharine Clark, Sonya Lee Smith, Amanda Lopez Askin); was a NM state
    senator 2001-2013 but specific sourced votes could not be retrieved via
    approved sources (Ballotpedia/Wikipedia returning 403, VoteSmart 403).

All three have been documented as unenrichable in batches 112 and 113.
No new sourced positions emerged in this session's research.

TARGETS is intentionally empty. This batch preserves the sequential record.
Future runs should expand the bucket to lower-confidence or state-level
candidates with verifiable records.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


TARGETS = []


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
