#!/usr/bin/env python3
"""Enrichment batch 112: hand-curated claims for bottom-of-alphabet bucket.

Bucket had 4 archetype_curated candidates with 0 claims (reverse-alpha).
Joe Mazzola (MA), Drew Wilson (FL-02), and Bernadette Sanchez (NM) returned
no verifiable sourced positions after extensive research — all three appear to
be placeholder / non-filing entries with no public candidate record. Only
Chris Jones (AR) has a documented 2024-2026 position record from reliable
sources. This batch enriches Chris Jones only.

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---- Chris Jones (AR-D, 2026 congressional candidate / 2022 Gov nominee) ----
    ("chris-jones-ar-gov-2026", "AR", "Governor", [
        claim("cj1", "chris-jones-ar-gov-2026", "sanctity_of_life", 0, False,
              "Stated 'I certainly support Roe v. Wade' during his 2022 Arkansas gubernatorial campaign and described abortion as 'a healthcare issue that needs to be left with families' — explicitly rejecting legal personhood from conception and affirming open access to abortion.",
              ["https://ontheissues.org/Governor/Chris_Jones_Abortion.htm",
               "https://www.democracydocket.com/analysis/candidate-qa-chris-jones-on-his-run-for-governor-of-arkansas/"]),
        claim("cj2", "chris-jones-ar-gov-2026", "self_defense", 1, False,
              "While a gun owner, Jones openly called for new firearm regulations including mandatory training and accountability for owners, and specifically sought to address untraceable 'ghost guns' — opposing the rubric's constitutional-carry / no-new-restrictions standard.",
              ["https://www.chrisforgovernor.com/promises/the-promise-for-a-balanced-conversation-on-gun-violence-and-safety",
               "https://www.5newsonline.com/article/news/politics/arkansas-candidate-social-issues-healthcare-crime/91-a5334ef4-0b13-46ab-920e-8927284723bc"]),
        claim("cj3", "chris-jones-ar-gov-2026", "christian_liberty", 0, False,
              "OnTheIssues VoteMatch analysis rates Jones as 'strongly opposing keeping God in the public sphere,' running counter to the rubric's standard for full public religious free exercise.",
              ["https://ontheissues.org/Chris_Jones.htm",
               "https://en.wikipedia.org/wiki/Chris_Jones_(Arkansas_politician)"]),
    ]),
]


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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
