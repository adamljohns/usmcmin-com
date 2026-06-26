#!/usr/bin/env python3
"""Enrichment batch 423: depth claims for 5 FL/CA U.S. Representatives.

Targets: evidence_curated FL/CA Reps with 1-2 claims, adding 2 new claims each
in uncovered rubric categories. All active members / 2026 nominees.

Frederica Wilson   (FL-24-D): election_integrity + self_defense
Jared Moskowitz    (FL-23-D): border_immigration + election_integrity
Debbie Wasserman Schultz (FL-D): election_integrity + economic_stewardship
Darren Soto        (FL-9-D):  self_defense + election_integrity
Sam Liccardo       (CA-16-D): election_integrity + border_immigration
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
    # ---------------- Frederica Wilson (FL-24-D, retiring 2026) ----------------
    ("frederica-wilson", "FL", "Representative", [
        claim("fw1", "frederica-wilson", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which required documentary proof of U.S. citizenship to register for federal elections. All 208 NO votes were cast by Democrats. Wilson, representing Miami-area FL-24 since 2011, has consistently characterized documentary-proof requirements as voter suppression and opposed citizenship-verification mandates for voter registration.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://en.wikipedia.org/wiki/Frederica_Wilson"]),
        claim("fw2", "frederica-wilson", "self_defense", 0, False,
              "Voted YES on H.R. 1808, the Assault Weapons Ban of 2022 (House Vote #399, July 29, 2022, 217-213), banning the manufacture and sale of semi-automatic assault weapons, and has consistently backed gun-control legislation throughout her tenure. Wilson has opposed constitutional-carry reciprocity and expansions of carry rights, directly contradicting the rubric's constitutional-carry standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h399",
               "https://en.wikipedia.org/wiki/Frederica_Wilson"]),
    ]),

    # ---------------- Jared Moskowitz (FL-23-D, running 2026 in FL-25) ----------------
    ("jared-moskowitz", "FL", "Representative", [
        claim("jm3", "jared-moskowitz", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213), which would have funded border-wall construction, reinstated the Remain-in-Mexico policy, and tightened asylum standards. Moskowitz, representing FL-23 since January 2023, has consistently opposed physical-barrier border enforcement and mandatory deportation legislation.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://en.wikipedia.org/wiki/Jared_Moskowitz"]),
        claim("jm4", "jared-moskowitz", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship to register for federal elections. All 208 NO votes came from House Democrats. As a South Florida Democrat, Moskowitz opposed citizenship-verification requirements as barriers to broad voter participation.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://en.wikipedia.org/wiki/Jared_Moskowitz"]),
    ]),

    # ---------------- Debbie Wasserman Schultz (FL-25-D) ----------------
    ("debbie-wasserman-schultz", "FL", "Representative", [
        claim("dws3", "debbie-wasserman-schultz", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which required documentary proof of U.S. citizenship to register in federal elections. All 208 NO votes were cast by Democrats. As former DNC chair (2011-2016) and a senior Florida Democrat, Wasserman Schultz has consistently opposed voter-ID and citizenship-verification requirements, characterizing them as voter suppression inconsistent with broad electoral access.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://en.wikipedia.org/wiki/Debbie_Wasserman_Schultz"]),
        claim("dws4", "debbie-wasserman-schultz", "economic_stewardship", 2, False,
              "Voted YES on the $1.9-trillion American Rescue Plan (House Vote #72, March 10, 2021, 220-211) and the $740-billion Inflation Reduction Act (House Vote #417, August 12, 2022, 220-207), both of which added substantially to the federal deficit without offsetting budget cuts or a balanced-budget framework. As former DNC chair, Wasserman Schultz consistently backed large-expenditure packages over fiscal restraint — the opposite of the rubric's anti-deficit standard.",
              ["https://www.govtrack.us/congress/votes/117-2021/h72",
               "https://www.govtrack.us/congress/votes/117-2022/h417",
               "https://en.wikipedia.org/wiki/Debbie_Wasserman_Schultz"]),
    ]),

    # ---------------- Darren Soto (FL-9-D, running 2026 in redrawn district) ----------------
    ("darren-soto", "FL", "Representative", [
        claim("ds3", "darren-soto", "self_defense", 0, False,
              "Co-sponsored H.R. 698, the Assault Weapons Ban of 2023 (118th Congress), which would ban the manufacture, sale, and importation of semi-automatic assault weapons and large-capacity magazines. Soto has also consistently opposed constitutional-carry reciprocity legislation, voting NO on H.R. 38 (the Constitutional Concealed Carry Reciprocity Act) when it advanced in the 115th Congress — directly contradicting the rubric's constitutional-carry standard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://en.wikipedia.org/wiki/Darren_Soto"]),
        claim("ds4", "darren-soto", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), requiring proof of U.S. citizenship to register for federal elections. All 208 NO votes were cast by Democrats. Soto, representing FL-9 (Orlando corridor) since 2017, has consistently opposed documentary-identification requirements for voter registration, framing them as barriers to electoral participation.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://en.wikipedia.org/wiki/Darren_Soto"]),
    ]),

    # ---------------- Sam Liccardo (CA-16-D, sworn in Jan 2025) ----------------
    ("sam-liccardo", "CA", "Representative", [
        claim("sl3", "sam-liccardo", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which required documentary proof of U.S. citizenship to register for federal elections. All 208 NO votes came from House Democrats. Liccardo, elected to represent CA-16 in November 2024 and sworn in January 2025, cast one of his first election-related House votes against citizenship-verification requirements for voter registration.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://en.wikipedia.org/wiki/Sam_Liccardo"]),
        claim("sl4", "sam-liccardo", "border_immigration", 0, False,
              "Voted NO on H.R. 1, the One Big Beautiful Bill (House Vote #232, May 22, 2025, 215-214), which included $46.55 billion for new border barriers, $4.1 billion for Border Patrol and ICE hiring, and rapid-deportation procedures for recent illegal entrants. As a Democrat representing the San Jose area — where he maintained sanctuary policies as mayor — Liccardo joined all House Democrats in opposing the border-security and enforcement provisions the rubric endorses.",
              ["https://www.govtrack.us/congress/votes/119-2025/h232",
               "https://en.wikipedia.org/wiki/Sam_Liccardo"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
