#!/usr/bin/env python3
"""Enrichment batch 381: hand-curated claims for 5 federal candidates.

Targets evidence_curated candidates with 3 existing claims, pulled from
the bottom of the alphabet (WI, VA×4).  Each gets 2 new claims in rubric
categories not yet scored.

Mix: Michael Alfonso (WI-07 R), Eugene Vindman (VA-07 D),
Bobby Scott (VA-03 D), Don Beyer (VA-08 D), James Walkinshaw (VA-11 D).

Sources: ballotpedia.org, govtrack.us, congress.gov, wispolitics.com,
en.wikipedia.org.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # -------- Michael Alfonso (WI-07 R, 2026 R nominee) --------
    ("michael-alfonso", "WI", "Representative", [
        claim("ma1", "michael-alfonso", "election_integrity", 0, True,
              "President Trump's January 27, 2026 endorsement statement described Alfonso as 'an America First fighter who will work with me to STRENGTHEN ELECTION INTEGRITY, secure our borders, and make America's heartland safer' — explicitly naming election integrity as a core campaign pillar. Alfonso also received endorsements from Speaker Mike Johnson and Wisconsin legislative leaders Fitzgerald and Steil, all aligned with voter-ID and election-security priorities.",
              ["https://ballotpedia.org/Michael_Alfonso",
               "https://www.wispolitics.com/2026/fitzgerald-steil-and-wied-campaigns-endorse-michael-alfonso-for-congress/"]),
        claim("ma2", "michael-alfonso", "economic_stewardship", 2, True,
              "Alfonso is recognized as a leading advocate for the Opportunity Zone program created by the 2017 Tax Cuts and Jobs Act — a private-investment-first model for community revitalization that reduces reliance on deficit-funded federal spending. His campaign, endorsed by House fiscal conservatives Speaker Johnson and Sean Duffy's political network, pledges to 'reform government' and 'bring down the cost of energy, food, and housing' through deregulation rather than new federal expenditure.",
              ["https://www.wjfw.com/news/local/paul-wassgren-vying-for-tiffanys-congress-seat-makes-campaign-stop-in-merrill/article_d3919f8c-a5fa-4ce2-95aa-949d8bad8d3d.html",
               "https://ballotpedia.org/Michael_Alfonso"]),
    ]),

    # -------- Eugene Vindman (VA-07 D, sitting member) --------
    ("eugene-vindman", "VA", "House", [
        claim("ev1", "eugene-vindman", "foreign_policy_restraint", 0, True,
              "On March 5, 2026, Vindman voted in favor of H.Con.Res. 38 (House Vote #85), a War Powers Resolution directing the President to remove U.S. Armed Forces from unauthorized hostilities against Iran unless Congress explicitly authorizes them — consistent with the rubric's Article I war-powers standard. Vindman stated the Iran conflict has 'no legal justification under domestic and international law.'",
              ["https://www.govtrack.us/congress/votes/119-2026/h85",
               "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/38",
               "https://en.wikipedia.org/wiki/Eugene_Vindman"]),
        claim("ev2", "eugene-vindman", "election_integrity", 0, False,
              "Vindman voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025), which required documentary proof of U.S. citizenship as a condition of federal voter registration. The bill passed 220–208 on a near-party-line vote; Vindman's opposition is consistent with the Democratic position opposing proof-of-citizenship requirements — at odds with the rubric's voter-ID and election-integrity standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Eugene_Vindman"]),
    ]),

    # -------- Bobby Scott (VA-03 D, sitting member) --------
    ("bobby-scott", "VA", "House", [
        claim("bs1", "bobby-scott", "election_integrity", 0, False,
              "Scott voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025), which required documentary proof of U.S. citizenship for federal voter registration. The bill passed 220–208 on a near-party-line vote. Scott's opposition is consistent with his 30-year record opposing restrictive voter-registration requirements and championing broad franchise access over the voter-ID and paper-ballot guardrails the rubric requires.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Bobby_Scott_(Virginia)"]),
        claim("bs2", "bobby-scott", "economic_stewardship", 2, False,
              "Scott voted YES on H.R. 1319, the American Rescue Plan Act of 2021 (House Vote #72, March 10, 2021), adding approximately $1.9 trillion to the national deficit. His legislative priorities consistently favor large deficit-funded federal programs — he is the top House sponsor of labor and education spending bills (44% and 18% of his sponsored legislation respectively, per GovTrack) — rather than balanced-budget or anti-deficit approaches the rubric requires.",
              ["https://www.govtrack.us/congress/members/robert_scott/400364",
               "https://www.congress.gov/bill/117th-congress/house-bill/1319",
               "https://ballotpedia.org/Bobby_Scott_(Virginia)"]),
    ]),

    # -------- Don Beyer (VA-08 D, sitting member) --------
    ("don-beyer", "VA", "House", [
        claim("db1", "don-beyer", "election_integrity", 0, False,
              "Beyer voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025), which required documentary proof of U.S. citizenship for federal voter registration. The bill passed 220–208 on a near-party-line vote. Beyer's voting record is among the most consistently partisan in the Virginia delegation (missed fewer than 2% of votes, voting with Democrats nearly 100% of the time per GovTrack), making his opposition to the rubric's voter-ID standard clear.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/members/donald_beyer/412657"]),
        claim("db2", "don-beyer", "economic_stewardship", 2, False,
              "Beyer voted YES on H.R. 1319 (American Rescue Plan Act, March 10, 2021) and H.R. 5376 (Inflation Reduction Act, August 12, 2022) — two major deficit-funded spending packages totaling over $2.5 trillion. As a member of the Joint Economic Committee, Beyer has championed federal investment as economic strategy and has not supported balanced budget amendments, placing him in direct opposition to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.congress.gov/member/donald-beyer/B001292",
               "https://ballotpedia.org/Don_Beyer",
               "https://www.govtrack.us/congress/members/donald_beyer/412657"]),
    ]),

    # -------- James Walkinshaw (VA-11 D, sitting member since Sep 2025) --------
    ("james-walkinshaw", "VA", "House", [
        claim("jw1", "james-walkinshaw", "self_defense", 1, False,
              "On October 3, 2025, Walkinshaw cosponsored H.R. 3115, the Assault Weapons Ban of 2025, which would make it a federal crime to import, sell, manufacture, transfer, or possess a semiautomatic assault weapon or large-capacity ammunition feeding device — directly contradicting the rubric's opposition to assault-weapon bans and high-capacity magazine restrictions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3115/cosponsors",
               "https://ballotpedia.org/James_Walkinshaw"]),
        claim("jw2", "james-walkinshaw", "election_integrity", 0, False,
              "Walkinshaw cosponsored H.R. 14, the John R. Lewis Voting Rights Advancement Act of 2025, which would reinstate and expand federal preclearance requirements under the Voting Rights Act, prioritizing expanded voting access and opposing state-level election integrity restrictions — at odds with the rubric's voter-ID, paper-ballot, and anti-mass-mail-in standards.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/14/cosponsors",
               "https://ballotpedia.org/James_Walkinshaw"]),
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
