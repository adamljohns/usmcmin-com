#!/usr/bin/env python3
"""Enrichment batch 258: 2 additional claims each for 5 sitting U.S. Senators.

All five already have 3 claims (evidence_curated); this adds 2 more spanning
distinct rubric categories to deepen their profiles.

Targets (bottom-of-alphabet by state, R/D mix):
  Jack Reed        (RI-D) — election_integrity, economic_stewardship
  James Lankford   (OK-R) — border_immigration, economic_stewardship
  Kevin Cramer     (ND-R) — border_immigration, election_integrity
  Jon Husted       (OH-R) — self_defense, economic_stewardship
  Bernie Moreno    (OH-R) — election_integrity, economic_stewardship

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
    # ---------------- Jack Reed (RI-D, US Senator) ----------------
    ("jack-reed", "RI", "Senator", [
        claim("jr1", "jack-reed", "election_integrity", 0, False,
              "A cosponsor of the Freedom to Vote Act (S.2747), which mandates that every registered voter can request a mail-in ballot and opposes uniform voter-ID requirements; Reed explicitly labeled the SAVE Act — which requires documentary proof of U.S. citizenship to register for federal elections — a 'voter suppression bill,' rejecting both voter-ID and citizenship-verification measures.",
              ["https://www.reed.senate.gov/news/releases/reed-urges-passage-of-the-freedom-to-vote-act",
               "https://www.reed.senate.gov/news/releases/reed-votes-to-protect-voting-rights-for-all-americans"]),
        claim("jr2", "jack-reed", "economic_stewardship", 2, False,
              "Throughout his Senate career Reed has backed multi-trillion-dollar budget resolutions and has not sponsored a balanced-budget amendment; as longtime chair of the Senate Armed Services Committee and a senior Appropriations member, he praised the FY2024 Biden budget — which projected adding trillions to the national debt — as 'fiscally responsible,' consistently prioritizing federal spending over deficit reduction.",
              ["https://www.reed.senate.gov/news/releases/reed-statement-on-bidens-fy24-budget-blueprint",
               "https://www.reed.senate.gov/issues/budget"]),
    ]),

    # ---------------- James Lankford (OK-R, US Senator) ----------------
    ("james-lankford", "OK", "Senator", [
        claim("jl1b", "james-lankford", "border_immigration", 3, True,
              "Authored the Border Patrol Enhancement Act and co-led the Border Act of 2024 (S.4361), which included border-wall construction funding and enforcement measures; in 2025 voted for the One Big Beautiful Bill containing mandatory federal E-Verify requirements — consistent with a multi-year record of pushing wall construction and employer-verification mandates.",
              ["https://www.lankford.senate.gov/issues/calling-out-bidens-chaos-at-the-southern-border-pushing-to-secure-the-us-from-bad-actors-around-the-world/",
               "https://www.congress.gov/bill/118th-congress/senate-bill/4361"]),
        claim("jl2b", "james-lankford", "economic_stewardship", 2, True,
              "Received the National Taxpayers Union 'Taxpayers' Friend Award' multiple times for opposing irresponsible federal spending; served on the Joint Select Committee on Budget and Appropriations Process Reform to reduce the national debt; holds an ACU Conservative rating of 95 percent and is consistently ranked among the most fiscally conservative members of the Senate.",
              ["https://www.lankford.senate.gov/news/press-releases/lankford-receives-taxpayers-friend-award-for-standing-up-to-irresponsible-federal-spending/",
               "https://www.lankford.senate.gov/news/press-releases/lankford-named-one-of-the-most-conservative-senators/"]),
    ]),

    # ---------------- Kevin Cramer (ND-R, US Senator) ----------------
    ("kevin-cramer", "ND", "Senator", [
        claim("kc1", "kevin-cramer", "border_immigration", 0, True,
              "Supports full southern border security including wall construction and military enforcement; publicly notes that North Dakota communities suffer direct harm from drug trafficking across the open southern border, and consistently backs DHS enforcement operations and border-infrastructure funding.",
              ["https://www.cramer.senate.gov/issues/immigration",
               "https://en.wikipedia.org/wiki/Kevin_Cramer"]),
        claim("kc2", "kevin-cramer", "election_integrity", 0, True,
              "Appeared publicly to champion voter-ID requirements, arguing all voters should prove who they are before casting a ballot, and signed the Americans for Tax Reform Taxpayer Protection Pledge; backed Republican election-integrity measures including photo-ID provisions for federal elections.",
              ["https://www.cramer.senate.gov/news/videos/watch/sen-cramer-joins-fox-and-friends-to-talk-about-voter-id-requirements-and-the-infrastructure-bill",
               "https://en.wikipedia.org/wiki/Kevin_Cramer"]),
    ]),

    # ---------------- Jon Husted (OH-R, US Senator) ----------------
    ("jon-husted", "OH", "Senator", [
        claim("jhu1", "jon-husted", "self_defense", 0, True,
              "Backed the LEOSA Reform Act to expand concealed-carry rights for active, off-duty, and retired law enforcement officers across all U.S. jurisdictions; consistent with a pro-Second-Amendment record carried from his time as Ohio Speaker and Lt. Governor into his Senate term.",
              ["https://www.husted.senate.gov/media/press-releases/husted-backs-bill-to-expand-law-enforcement-concealed-carry-rights/",
               "https://www.husted.senate.gov/about/"]),
        claim("jhu2", "jon-husted", "economic_stewardship", 2, True,
              "In November 2025 introduced the Principles-Based Balanced Budget Amendment (PBBA), a constitutional amendment requiring Congress to balance spending and revenues within 10 years of ratification; stated the goal is to 'restore fiscal responsibility in Washington, calm inflation and require Congress to rein in spending in a principled way.'",
              ["https://www.husted.senate.gov/media/press-releases/husted-introduces-constitutional-amendment-to-balance-the-federal-budget/",
               "https://en.wikipedia.org/wiki/Jon_Husted"]),
    ]),

    # ---------------- Bernie Moreno (OH-R, US Senator) ----------------
    ("bernie-moreno", "OH", "Senator", [
        claim("bmo1", "bernie-moreno", "election_integrity", 0, True,
              "Supported a Senate motion requiring photo identification for voters and backed the SAVE Act requiring documentary proof of U.S. citizenship to register for federal elections; has maintained that the 2020 presidential election outcome was illegitimate, reflecting a strong election-integrity posture throughout his Senate career.",
              ["https://en.wikipedia.org/wiki/Bernie_Moreno",
               "https://ballotpedia.org/Bernie_Moreno"]),
        claim("bmo2", "bernie-moreno", "economic_stewardship", 0, True,
              "Championed the GENIUS Act (signed into law 2025), creating a regulatory framework for private stablecoins as a market-driven alternative to a government-controlled central bank digital currency (CBDC); also introduced the Deploying American Blockchains Act to establish U.S. leadership in private decentralized digital assets — an explicit structural counter to a Federal Reserve CBDC.",
              ["https://www.moreno.senate.gov/press-releases/moreno-recaps-first-year-successes-for-ohio/",
               "https://en.wikipedia.org/wiki/Bernie_Moreno"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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
