#!/usr/bin/env python3
"""Enrichment batch 123: hand-curated claims for 4 U.S. Representatives.

Targets archetype_party_default federal representatives from bottom-of-alphabet
states (TX, UT) with 0 evidence claims. Uses the (slug + state + office_keyword)
matcher from prior batches.

Mix (3 R aligned / 1 R non-aligned): Troy Nehls (TX-R), Celeste Maloy (UT-R),
Mike Kennedy (UT-R), Blake Moore (UT-R moderate).

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
    # ---------------- Troy Nehls (TX-22, R, retiring) ----------------
    ("troy-nehls", "TX", "Representative", [
        claim("tn1", "troy-nehls", "sanctity_of_life", 0, True,
              "SBA Pro-Life America records Nehls as voting consistently to defend the lives of the unborn: blocking taxpayer-funded abortion domestically and internationally, and protecting conscience rights of health care providers who refuse to perform abortions.",
              ["https://sbaprolife.org/representative/troy-nehls",
               "https://en.wikipedia.org/wiki/Troy_Nehls"]),
        claim("tn2", "troy-nehls", "self_defense", 1, True,
              "Nehls voted to keep extreme-risk-protection-order ('red flag') provisions out of the National Defense Authorization Act, publicly declaring that gun-control legislators 'tried and FAILED' to insert such language — opposing red-flag laws and new firearm restrictions.",
              ["https://en.wikipedia.org/wiki/Troy_Nehls",
               "https://nehls.house.gov/about/about"]),
        claim("tn3", "troy-nehls", "border_immigration", 0, True,
              "A former Fort Bend County, Texas sheriff and hard-line border-enforcement advocate, Nehls rejected the 2024 bipartisan Senate border bill as far too weak, demanding full military-backed enforcement of the southern border rather than incremental legislative compromise.",
              ["https://en.wikipedia.org/wiki/Troy_Nehls",
               "https://ballotpedia.org/Troy_Nehls"]),
    ]),

    # ---------------- Celeste Maloy (UT-2, R) ----------------
    ("celeste-maloy", "UT", "Representative", [
        claim("cml1", "celeste-maloy", "sanctity_of_life", 0, True,
              "SBA Pro-Life America records Maloy as consistently pro-life: blocking taxpayer-funded abortion including abortion travel reimbursements, and pushing back on Biden administration executive actions expanding abortion access.",
              ["https://sbaprolife.org/representative/celeste-maloy",
               "https://en.wikipedia.org/wiki/Celeste_Maloy"]),
        claim("cml2", "celeste-maloy", "border_immigration", 0, True,
              "Campaigned on a commitment to 'finish the wall, fully fund our border patrol, and keep dangerous drugs like fentanyl out of our communities' — placing her within the wall-and-enforcement standard the rubric requires.",
              ["https://ballotpedia.org/Celeste_Maloy",
               "https://maloy.house.gov/voterecord/"]),
    ]),

    # ---------------- Mike Kennedy (UT-3, R) ----------------
    ("mike-kennedy", "UT", "Representative", [
        claim("mkut1", "mike-kennedy", "economic_stewardship", 2, True,
              "As a Utah state legislator before entering Congress, Kennedy spearheaded efforts to cut taxes and balance the state budget while making government more efficient; he explicitly campaigns on applying that same fiscal discipline at the federal level.",
              ["https://en.wikipedia.org/wiki/Mike_Kennedy",
               "https://ballotpedia.org/Mike_Kennedy_(Utah)"]),
        claim("mkut2", "mike-kennedy", "self_defense", 1, True,
              "Kennedy emerged as a vocal Second Amendment advocate during his state legislative tenure and 2024 congressional campaign, actively meeting with Utah Gun Exchange to demonstrate opposition to new firearm restrictions.",
              ["https://en.wikipedia.org/wiki/Mike_Kennedy",
               "https://www.govtrack.us/congress/members/mike_kennedy/457025"]),
        claim("mkut3", "mike-kennedy", "border_immigration", 1, True,
              "In April 2025 Kennedy traveled to El Salvador and received a tour of the CECOT maximum-security prison, publicly supporting the Trump administration's aggressive deportation posture — signaling alignment with mandatory deportation enforcement.",
              ["https://www.govtrack.us/congress/members/mike_kennedy/457025",
               "https://en.wikipedia.org/wiki/Mike_Kennedy"]),
    ]),

    # ---------------- Blake Moore (UT-1, R, moderate) ----------------
    ("blake-moore", "UT", "Representative", [
        claim("bm1", "blake-moore", "biblical_marriage", 1, False,
              "On July 19, 2022, Moore was one of 47 House Republicans who voted for the Respect for Marriage Act (H.R.8404), which codified federal recognition of same-sex marriages — directly rejecting the one-man-one-woman standard and the opposition to same-sex marriage the rubric holds.",
              ["https://en.wikipedia.org/wiki/Blake_Moore",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("bm2", "blake-moore", "economic_stewardship", 2, False,
              "While Moore publicly claims to vote for 'budgets that get as close to a balanced budget as possible,' his 2024 primary opponents cited his repeated votes for non-balanced, deficit-spending budgets as a key failure — a record that falls short of the rubric's anti-deficit standard.",
              ["https://ballotpedia.org/Blake_Moore",
               "https://en.wikipedia.org/wiki/Blake_Moore"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
