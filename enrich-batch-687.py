#!/usr/bin/env python3
"""Enrichment batch 687: hand-curated claims for 5 sitting NY Republican U.S. Representatives.

Targets NY Republican House members with 3 existing claims, adding 2-3 new claims each
spanning distinct rubric categories (election_integrity, economic_stewardship, biblical_marriage,
sanctity_of_life). All votes sourced from congress.gov, govtrack.us, clerk.house.gov, and
official representative press releases.

Candidates: Nicole Malliotakis (NY-11), Nick Langworthy (NY-23), Nick LaLota (NY-01),
Mike Lawler (NY-17), Claudia Tenney (NY-24).

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
    # ------------ Nicole Malliotakis (NY-11, US Representative) ------------
    ("nicole-malliotakis", "NY", "Representative", [
        claim("nm4", "nicole-malliotakis", "election_integrity", 0, True,
              "Original cosponsor of H.R. 22, the SAVE Act (Safeguard American Voter Eligibility Act; added January 3, 2025), and voted YEA on passage (House Roll Call #102, April 10, 2025, passed 220–208), requiring documentary proof of U.S. citizenship when registering to vote in federal elections. Malliotakis applauded the bill in an official press release: 'The passage of the SAVE Act today reaffirms our commitment to creating more trust in our elections.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://malliotakis.house.gov/media/press-releases/malliotakis-applauds-house-passage-bill-prevent-noncitizen-voting-us-elections",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("nm5", "nicole-malliotakis", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219–210), prohibiting the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that would enable financial surveillance of American citizens.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201"]),
    ]),

    # ------------ Nick Langworthy (NY-23, US Representative) ------------
    ("nick-langworthy", "NY", "Representative", [
        claim("nl4", "nick-langworthy", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218–206), amending Title IX to define sex as 'based solely on a person's reproductive biology and genetics at birth' and prohibiting biological males from competing in women's and girls' athletic programs at federally funded schools.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://clerk.house.gov/Votes/202512"]),
        claim("nl5", "nick-langworthy", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219–210), prohibiting the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that would enable financial surveillance of Americans.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201"]),
    ]),

    # ------------ Nick LaLota (NY-01, US Representative) ------------
    ("nick-lalota", "NY", "Representative", [
        claim("nll4", "nick-lalota", "election_integrity", 0, True,
              "Voted YEA on H.R. 22, the SAVE Act (House Roll Call #102, April 10, 2025, passed 220–208), requiring documentary proof of U.S. citizenship when registering to vote in federal elections; issued a press release confirming his support: 'The SAVE Act, which passed the House today with my support … ensures that only American citizens are participating in our elections.'",
              ["https://lalota.house.gov/media/press-releases/lalota-backs-save-act-strengthen-election-integrity-and-prevent-voter-fraud",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("nll5", "nick-lalota", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218–206), amending Title IX to define sex as reproductive biology and genetics at birth and bar biological males from competing in women's and girls' athletic programs at federally funded schools; issued a press release: 'LaLota Votes to Uphold Title IX and Protect Women and Girls in Sports.'",
              ["https://lalota.house.gov/media/press-releases/lalota-votes-uphold-title-ix-and-protect-women-and-girls-sports",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
        claim("nll6", "nick-lalota", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219–210), prohibiting the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that would enable financial surveillance of Americans.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201"]),
    ]),

    # ------------ Mike Lawler (NY-17, US Representative) ------------
    ("mike-lawler", "NY", "Representative", [
        claim("ml4", "mike-lawler", "sanctity_of_life", 0, True,
              "Voted YEA on H.R. 26, the Born-Alive Abortion Survivors Protection Act (House Roll Call #29, January 11, 2023, passed 220–210–1 Present), requiring physicians to provide medical care to any infant born alive after an attempted abortion and imposing criminal penalties for failure to do so. The 220 YES votes came unanimously from Republicans with zero GOP defections.",
              ["https://www.govtrack.us/congress/votes/118-2023/h29",
               "https://clerk.house.gov/Votes/202329"]),
        claim("ml5", "mike-lawler", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219–210), prohibiting the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that would enable financial surveillance of Americans.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201"]),
    ]),

    # ------------ Claudia Tenney (NY-24, US Representative) ------------
    ("claudia-tenney", "NY", "Representative", [
        claim("ct4", "claudia-tenney", "election_integrity", 0, True,
              "Original cosponsor of H.R. 22, the SAVE Act (added January 3, 2025), and voted YEA on passage (House Roll Call #102, April 10, 2025, passed 220–208), requiring documentary proof of U.S. citizenship to register to vote in federal elections. As co-chair of the House Election Integrity Caucus, Tenney issued a statement titled 'Congresswoman Tenney Votes to Ban Illegal Immigrants From Voting in US Elections.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://tenney.house.gov/media/press-releases/congresswoman-tenney-votes-ban-illegal-immigrants-voting-us-elections",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("ct5", "claudia-tenney", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218–206), amending Title IX to define sex as 'based solely on a person's reproductive biology and genetics at birth' and prohibiting biological males from competing in women's and girls' athletic programs at federally funded schools.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://clerk.house.gov/Votes/202512"]),
        claim("ct6", "claudia-tenney", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219–210), prohibiting the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that would enable financial surveillance of Americans.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
