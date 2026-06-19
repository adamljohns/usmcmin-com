#!/usr/bin/env python3
"""Enrichment batch 302: 3rd claims for 4 active 2026 federal candidates.

Archetype_curated federal-senator bucket fully exhausted (also confirmed by
batch 301). Batch targets evidence_curated federal candidates at the bottom of
the alphabet (SC, NY, IA) that carry exactly 2 claims and need a 3rd to span
a third rubric category.

Targets (1 D/SC + 1 D/IA + 2 D/NY):
  Mac Deford    (SC-01, D) — June 23 runoff, open Mace seat
  Josh Turek    (IA Senate, D) — June 2 nominee, faces Hinson Nov 3
  George Conway (NY-12, D) — Nadler-seat open, June 23 primary
  Antonio Reynoso (NY-07, D) — Velazquez-seat open, June 23 primary

Each claim cites >=1 reliable source and reflects 2024-2026 positions.

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
    # ---- Mac Deford (SC-01, D — June 23 runoff, open Mace seat) ----
    ("mac-deford", "SC", "Representative", [
        claim("md1", "mac-deford", "border_immigration", 1, False,
              "At an August 2025 'WE THE PALMETTO' candidate interview, stated 'I do not agree with how this administration is going about immigration enforcement' and called for 'a fair, efficient, transparent immigration process' that includes a pathway to citizenship for undocumented people — explicitly rejecting the mandatory-deportation and mass-deportation enforcement posture the rubric requires.",
              ["https://www.live5news.com/2025/08/22/we-palmetto-meet-candidate-mac-deford-sc01/",
               "https://ballotpedia.org/Mac_Deford"]),
    ]),

    # ---- Josh Turek (IA Senate D nominee, won June 2 primary) ----
    ("josh-turek", "IA", "Senate", [
        claim("jt1", "josh-turek", "self_defense", 1, False,
              "During his 2026 Iowa Democratic Senate primary campaign, publicly called for reinstating the 1990s federal assault-weapons ban, stating 'I would like to see us return to a 1990s… assault-weapons ban' — a position highlighted by the NRSC as opposing Second Amendment rights and directly contradicting the rubric's defense of the right to keep semiautomatic firearms.",
              ["https://www.nrsc.org/press-releases/nrsc-slams-liberal-josh-turek-in-new-ad-2026-06-03/",
               "https://en.wikipedia.org/wiki/Josh_Turek"]),
    ]),

    # ---- George Conway (NY-12, D — Nadler-seat open, June 23 primary) ----
    ("george-conway-ny-12", "NY", "NY-12", [
        claim("gc1", "george-conway-ny-12", "self_defense", 1, False,
              "In his 2026 NY-12 congressional campaign, explicitly endorsed regulation of AR-15-style semiautomatic rifles and expanded universal background checks, describing these as 'commonsense' gun measures — opposing the rubric's protection of the unrestricted right to keep and bear semiautomatic arms.",
              ["https://www.amny.com/sponsored/your-vote-2026-district-12-meet-george-conway/",
               "https://www.georgeconwayforcongress.com/campaign-updates/press-releases/george-conway-launches-campaign-for-congress-in-ny-12/"]),
    ]),

    # ---- Antonio Reynoso (NY-07, D — Velazquez-seat open, June 23 primary) ----
    ("antonio-reynoso", "NY", "NY-07", [
        claim("ar1", "antonio-reynoso", "sanctity_of_life", 0, False,
              "As Brooklyn Borough President, launched a 'Historic Maternal Health Agenda' that frames abortion access as essential reproductive healthcare; and per his 2025 Jim Owles Liberal Democratic Club candidate questionnaire, committed to protecting unrestricted access to reproductive care and abortion — rejecting any life-at-conception or personhood standard.",
              ["https://www.brooklynbp.nyc.gov/maternal-health-agenda/",
               "https://jimowles.org/news/antonio-reynoso-for-brooklyn-borough-president-2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; prevents wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
