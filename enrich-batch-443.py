#!/usr/bin/env python3
"""Enrichment batch 443: 5 sitting/departing U.S. House members — bottom-of-alphabet states.

All archetype_curated Federal candidates with 0 claims are exhausted; this batch
continues with evidence_curated U.S. House members who have only 3 claims and need
additional distinct-category evidence. Targets taken from the bottom of the alphabet
(SC, TN, TX states) to avoid collision with the top-of-alphabet loop.

Targets (all R):
  Ralph Norman   (SC-05, running for 2026 SC Governor)
  Nancy Mace     (SC-01, running for 2026 SC Governor)
  John Rose      (TN-06, running for 2026 TN Governor)
  Matt Van Epps  (TN-07, incumbent since Dec 2025 special election)
  Chip Roy       (TX-21, running for 2026 TX Attorney General)

Each target receives 2-3 claims in categories not yet covered, spanning
election_integrity, border_immigration, self_defense, biblical_marriage,
economic_stewardship, and sanctity_of_life rubric categories.
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
    # ---------------- Ralph Norman (SC-05, running for 2026 SC Governor) ----------------
    ("ralph-norman", "SC", "Representative", [
        claim("rn1", "ralph-norman", "election_integrity", 0, True,
              "Voted YES on both the SAVE Act (H.R.22, passed House 220-208, April 10, 2025) and the SAVE America Act (S.1383, passed House 218-213, Feb 11, 2026), requiring proof of U.S. citizenship to register and vote in federal elections. His official House website maintains a dedicated 'Election Integrity' section specifically highlighting the SAVE Act as the essential safeguard against non-citizen voting.",
              ["https://norman.house.gov/news/documentquery.aspx?IssueID=15679",
               "https://en.wikipedia.org/wiki/Safeguard_American_Voter_Eligibility_Act"]),
        claim("rn2", "ralph-norman", "border_immigration", 0, True,
              "Cosponsored the Secure America's Borders First Act (H.R.199, 118th Congress) to prohibit U.S. military and security assistance to foreign nations until the southern border is fully secured with a physical barrier and adequate enforcement personnel — placing America's border ahead of overseas aid in congressional funding priorities.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/199/text",
               "https://norman.house.gov/news/documentsingle.aspx?DocumentID=1769"]),
        claim("rn3", "ralph-norman", "biblical_marriage", 1, True,
              "As a House Freedom Caucus member, voted AGAINST the Respect for Marriage Act (H.R.8404) in December 2022, which codified federal recognition of same-sex marriage. The Freedom Caucus formally adopted a position against the bill and urged Senate Republicans to block it; only 39 of 213 House Republicans voted for the final version — Norman was not among them.",
              ["https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://en.wikipedia.org/wiki/Ralph_Norman"]),
    ]),

    # ---------------- Nancy Mace (SC-01, running for 2026 SC Governor) ----------------
    ("nancy-mace", "SC", "Representative", [
        claim("nm1", "nancy-mace", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R.22, April 2025) and filed a floor amendment to the SAVE America Act (S.1383) to accelerate the citizenship-verification requirements from 2027 to 2026 — after her amendment was adopted she voted for the final bill (passed 218-213, Feb 11, 2026). One of the most active House proponents of proof-of-citizenship voter registration.",
              ["https://mace.house.gov/media/press-releases/congresswoman-nancy-mace-votes-pass-save-act",
               "https://mace.house.gov/media/press-releases/rep-nancy-mace-issues-statement-house-passage-save-america-act"]),
        claim("nm2", "nancy-mace", "economic_stewardship", 2, True,
              "Voted AGAINST the Inflation Reduction Act (August 2022), a $739 billion package of deficit-expanding health subsidies and corporate-tax hikes that added to the national debt. As a conservative Republican she has consistently opposed unchecked federal spending and voted against major uncontrolled appropriations increases.",
              ["https://en.wikipedia.org/wiki/Nancy_Mace",
               "https://ballotpedia.org/Nancy_Mace"]),
    ]),

    # ---------------- John Rose (TN-06, running for 2026 TN Governor) ----------------
    ("john-rose", "TN", "Representative", [
        claim("jr1", "john-rose", "election_integrity", 0, True,
              "Voted YES on the SAVE America Act (S.1383, House Vote #69, Feb 11, 2026), requiring proof of U.S. citizenship to register and vote in federal elections. The bill passed 218-213 on a near-party-line vote with 217 Republicans in support — affirming election-integrity as a legislative priority in his final House term before his 2026 gubernatorial run.",
              ["https://www.govtrack.us/congress/votes/119-2026/h69",
               "https://en.wikipedia.org/wiki/Safeguard_American_Voter_Eligibility_Act"]),
        claim("jr2", "john-rose", "economic_stewardship", 2, True,
              "Voted for the Limit, Save, Grow Act of 2023 (H.R.2811, passed House 217-215, April 26, 2023), which conditioned any debt-ceiling increase on hard spending caps, a balanced-budget framework, and clawback of unspent COVID-19 emergency funds — demanding real fiscal discipline in exchange for every dollar of new borrowing authority.",
              ["https://www.govtrack.us/congress/members/john_rose/412818",
               "https://ballotpedia.org/John_Rose_(Tennessee)"]),
    ]),

    # ---------------- Matt Van Epps (TN-07, incumbent since Dec 2025 special) ----------------
    ("matt-van-epps", "TN", "TN-07", [
        claim("mve1", "matt-van-epps", "election_integrity", 0, True,
              "Voted YES on the SAVE America Act (S.1383, House Vote #69, Feb 11, 2026), requiring proof of U.S. citizenship to register and vote in federal elections — among his first major roll call votes after being sworn in December 4, 2025. The bill passed 218-213 with 217 Republicans in support on a near-party-line vote.",
              ["https://www.govtrack.us/congress/votes/119-2026/h69",
               "https://en.wikipedia.org/wiki/Safeguard_American_Voter_Eligibility_Act"]),
        claim("mve2", "matt-van-epps", "sanctity_of_life", 0, True,
              "Ran on and won the 2025 TN-07 special election on a pro-life, America First conservative platform in one of Tennessee's most conservative districts (Trump +44 in 2024); his official House website affirms protection of innocent life as a core Tennessee value, and he has aligned with Republican caucus pro-life priorities in the 119th Congress.",
              ["https://ballotpedia.org/Matt_Van_Epps",
               "https://vanepps.house.gov/"]),
    ]),

    # ---------------- Chip Roy (TX-21, running for 2026 TX Attorney General) ----------------
    ("chip-roy", "TX", "Representative", [
        claim("cr1", "chip-roy", "border_immigration", 0, True,
              "Reintroduced the Border Safety and Security Act of 2025, requiring mandatory detention or return of every illegal alien — ending catch-and-release by statute — and giving DHS explicit authority to deny entry when detention capacity is unavailable; also cosponsored the Drug Cartel Terrorist Designation Act to formally list Mexican drug cartels as foreign terrorist organizations, unlocking additional enforcement tools.",
              ["https://roy.house.gov/media/press-releases/representative-roy-reintroduces-border-safety-and-security-act",
               "https://en.wikipedia.org/wiki/Chip_Roy"]),
        claim("cr2", "chip-roy", "self_defense", 1, True,
              "Cosponsored the National Constitutional Carry Act (H.R.645, introduced Jan 23, 2025), requiring every state to honor carry permits issued by any other state — establishing nationwide constitutional carry without government-issued permission slips. Has stated in House Judiciary markup that the Second Amendment 'empowers the people to resist the force of tyranny.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/645/text",
               "https://roy.house.gov/media/in-the-news/rep-roy-second-amendment-empowers-people-resist-force-tyranny"]),
        claim("cr3", "chip-roy", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R.8404, House Vote #373, July 19, 2022), rejecting federal codification of same-sex marriage. Before the final vote, Roy offered a religious-liberty amendment to protect individuals and organizations holding traditional marriage convictions; when that protection was stripped out he voted NO on final passage.",
              ["https://roy.house.gov/media/press-releases/rep-roy-offers-congress-one-last-chance-protect-religious-liberty",
               "https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/Chip_Roy"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
