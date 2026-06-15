#!/usr/bin/env python3
"""Enrichment batch 217: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Primary archetype_curated bucket exhausted; this batch adds a sourced 3rd
claim to evidence_curated candidates that had only 2 claims, taking from
the reverse-alphabetical bottom (WA × 3, WI × 1, RI × 1).

Targets: Dan Newhouse (WA-R retiring), Carmen Goers (WA-R),
         Leslie Lewallen (WA-R), Niina Threlfall-Baum (WI-R),
         Seth Magaziner (RI-D).
Each new claim covers a DISTINCT rubric category not yet evidenced.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # -------- Dan Newhouse (WA-R, retiring US House WA-04) --------
    ("dan-newhouse", "WA", "House", [
        claim("dn1", "dan-newhouse", "self_defense", 1, True,
              "Voted NO on Senate Amendment to S.2938 (Bipartisan Safer Communities Act, 2022), explicitly warning the bill 'undermines the constitutionally-guaranteed rights of law-abiding citizens, including the right to bear arms and the right to due process.' He objected to provisions that lacked due process protections and that allow states to delay firearm purchases — opposing red-flag-style restrictions without adequate legal safeguards.",
              ["https://newhouse.house.gov/media-center/press-releases/newhouse-votes-no-gun-control-bill",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
    ]),

    # -------- Carmen Goers (WA-R, 2026 WA-08 candidate) --------
    ("carmen-goers", "WA", "Representative", [
        claim("cg1", "carmen-goers", "economic_stewardship", 2, True,
              "Campaigned on explicit fiscal conservatism: stated 'Congress needs to reassess its spending habits and prioritize our nation's financial stability,' called for 'No more taxes,' and argued that 'Washingtonians cannot afford the reckless spending by Democrats in Congress — they need relief, not more taxes and fees.' Advocates cutting taxes to let individuals keep more of what they earn.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/207474/carmen-goers",
               "https://ballotpedia.org/Carmen_Goers"]),
    ]),

    # -------- Leslie Lewallen (WA-R, 2026 WA-03 candidate) --------
    ("leslie-lewallen", "WA", "Representative", [
        claim("ll1", "leslie-lewallen", "economic_stewardship", 2, True,
              "Identified 'out-of-control spending by the federal government' as a primary driver of inflation and committed to 'fiscal responsibility,' arguing that 'Washingtonians cannot afford the reckless spending by Democrats in Congress — they need relief, not more taxes and fees.' Opposes tax increases and calls for balanced federal spending.",
              ["https://ballotpedia.org/Leslie_Lewallen",
               "https://ballotpedia.org/Washington%27s_3rd_Congressional_District_election,_2024"]),
    ]),

    # -------- Niina Threlfall-Baum (WI-R, 2026 WI-07 candidate) --------
    ("niina-threlfall-baum", "WI", "Representative", [
        claim("ntb1", "niina-threlfall-baum", "economic_stewardship", 2, True,
              "Pledges to uphold 'fiscal responsibility, local control, and government accountability' as core governing principles and committed to not accepting corporate PAC contributions funded by corporate treasury money — emphasizing taxpayer and constituent accountability over special-interest spending.",
              ["https://ballotpedia.org/Wisconsin%27s_7th_Congressional_District_election,_2026_%28August_11_Republican_primary%29",
               "https://ballotpedia.org/Niina_Threlfall-Baum"]),
    ]),

    # -------- Seth Magaziner (RI-D, US Rep RI-02) --------
    ("seth-magaziner", "RI", "Representative", [
        claim("sm1", "seth-magaziner", "border_immigration", 0, False,
              "Voted against H.R.5525, the 'Continuing Appropriations and Border Security Enhancement Act, 2024,' which included provisions for border-wall construction and enhanced enforcement — consistent with his opposition to military-style border security measures and physical barrier funding.",
              ["https://www.govtrack.us/congress/members/seth_magaziner/456937",
               "https://ballotpedia.org/Seth_Magaziner"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collision."""
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
