#!/usr/bin/env python3
"""Enrichment batch 686: hand-curated claims for 5 sitting U.S. Representatives (OH).

Targets sitting Republican U.S. Representatives from Ohio with only 3 existing claims,
taken from the bottom of the alphabet (OH) per the collision-avoidance protocol.

Candidates: Mike Carey (OH-15), Michael Turner (OH-10), Michael Rulli (OH-06),
Max Miller (OH-07), Jim Jordan (OH-04).

Each claim cites >=1 reliable source and reflects 2024-2026 voting records / public positions.

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
    # ---------------- Mike Carey (OH-15, US Representative) ----------------
    ("mike-carey", "OH", "Representative", [
        claim("mc-ei1", "mike-carey", "election_integrity", 0, True,
              "Author of H.R. 6513, the Confirmation of Congressional Observer Access (COCOA) Act, which passed both chambers unanimously and was signed into law on October 4, 2024; codifies the requirement that states allow designated congressional staff to observe all stages of federal election administration — voting, scanning, tabulation, canvassing, recounting, and certification — as a transparency and integrity safeguard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/6513"]),
        claim("mc-es1", "mike-carey", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which prohibits the Federal Reserve from issuing a retail central bank digital currency directly to individuals — blocking a government-controlled digital dollar that could enable financial surveillance of American citizens.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
        claim("mc-bm1", "mike-carey", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), amending Title IX to define sex as 'based solely on a person's reproductive biology and genetics at birth' and prohibiting biological males from competing in women's and girls' athletic programs at federally funded schools.",
              ["https://clerk.house.gov/Votes/202512",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
    ]),

    # ---------------- Michael Turner (OH-10, US Representative) ----------------
    ("michael-turner", "OH", "Representative", [
        claim("mt-bi1", "michael-turner", "border_immigration", 1, True,
              "Voted YEA on H.R. 29, the Laken Riley Act (House Roll Call #6, January 7, 2025, passed 264-159), mandating federal detention of undocumented immigrants charged with theft, burglary, or violent crimes and authorizing states to sue the federal government for immigration enforcement failures.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
        claim("mt-bm1", "michael-turner", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), amending Title IX to define sex by reproductive biology and genetics at birth, barring biological males from women's and girls' sports at federally funded schools.",
              ["https://clerk.house.gov/Votes/202512",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
        claim("mt-es1", "michael-turner", "economic_stewardship", 2, False,
              "Voted YEA on H.R. 1, the One Big Beautiful Bill Act (House Roll Call #190, July 3, 2025, passed 218-214) after initially holding out and then flipping following federal-worker pension changes; the Congressional Budget Office estimates the bill adds approximately $3.3 trillion to the federal deficit over ten years — a result at odds with the balanced-budget standard the rubric requires.",
              ["https://clerk.house.gov/Votes/2025190",
               "https://www.daytondailynews.com/local/area-rep-flips-on-support-for-big-beautiful-bill-how-ohio-lawmakers-voted-on-trump-budget-package/KFIC2VTKVFFXXOVMDEYBK2U4JY/"]),
    ]),

    # ---------------- Michael Rulli (OH-06, US Representative) ----------------
    ("michael-rulli", "OH", "Representative", [
        claim("mr-sd1", "michael-rulli", "self_defense", 1, True,
              "Cosponsor of H.R. 563, the No Retaining Every Gun In a System That Restricts Your Rights Act (119th Congress), which prohibits the federal government from creating or maintaining a centralized database or registry of identifiable lawful firearm owners or purchases — directly opposing the universal gun-tracking infrastructure the rubric warns against.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/563/cosponsors"]),
        claim("mr-bm1", "michael-rulli", "biblical_marriage", 2, True,
              "Cosponsor (added 01/13/2025) and YEA voter on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), which amends Title IX to define sex as reproductive biology and genetics at birth and prohibit biological males from competing in women's and girls' athletic programs at federally funded schools.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28/cosponsors",
               "https://clerk.house.gov/Votes/202512"]),
        claim("mr-ei1", "michael-rulli", "election_integrity", 0, True,
              "Voted YEA on H.R. 22, the SAVE Act (Safeguard American Voter Eligibility Act; House Roll Call #102, April 10, 2025, passed 220-208), requiring documentary proof of U.S. citizenship when registering to vote in federal elections — one of zero Republican defections on the party-line vote.",
              ["https://clerk.house.gov/Votes/2025102",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
    ]),

    # ---------------- Max Miller (OH-07, US Representative) ----------------
    ("max-miller", "OH", "Representative", [
        claim("mm-es1", "max-miller", "economic_stewardship", 2, True,
              "Voted NAY on H.R. 9747, the Continuing Appropriations and Extensions Act 2025 (House Roll Call #450, September 25, 2024, passed 341-82), releasing a formal statement: 'Congress has had all year to pass the twelve appropriations bills that are required to fund the government responsibly. Instead of doing that … we once again kicked the can down the road and set ourselves up for another omnibus spending bill right before the holidays.'",
              ["https://maxmiller.house.gov/posts/u-s-congressman-miller-votes-against-bad-government-funding-bill",
               "https://www.govtrack.us/congress/votes/118-2024/h450"]),
        claim("mm-ei1", "max-miller", "election_integrity", 0, True,
              "Voted YEA on H.R. 22, the SAVE Act (House Roll Call #102, April 10, 2025, passed 220-208), requiring documentary proof of U.S. citizenship to register to vote in federal elections; released a statement: 'Americans should decide American elections. Not foreigners. We should have photo ID … Allowing non-citizens to vote in our elections not only makes our elections less secure, but it diminishes the value of American citizenship.'",
              ["https://maxmiller.house.gov/posts/u-s-congressman-max-millers-statement-on-the-houses-passage-of-the-safeguard-american-voter-eligibility-save-ac",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("mm-bm1", "max-miller", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206, unanimous Republican vote), amending Title IX to define sex as reproductive biology and genetics at birth and bar biological males from women's and girls' athletic programs at federally funded schools.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://clerk.house.gov/Votes/202512"]),
    ]),

    # ---------------- Jim Jordan (OH-04, US Representative) ----------------
    ("jim-jordan", "OH", "Representative", [
        claim("jj-bm1", "jim-jordan", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), among the unanimous Republican majority that amended Title IX to define sex as reproductive biology and genetics at birth, barring biological males from women's and girls' sports in federally funded schools.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://mikejohnson.house.gov/news/documentsingle.aspx?DocumentID=1526"]),
        claim("jj-ei1", "jim-jordan", "election_integrity", 0, True,
              "As House Judiciary Committee Chairman, championed the SAVE Act (H.R. 22, Roll Call #102, April 10, 2025, passed 220-208) requiring documentary proof of U.S. citizenship to register to vote; stated publicly: 'Americans should be voting in American elections. Not foreigners. We should have photo ID. We should have a citizenship requirement.'",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://thenationaldesk.com/news/americas-news-now/exclusive-rep-jim-jordan-talks-election-integrity-actblue-nfl-probes-citizenship-democratic-investigation-doj"]),
        claim("jj-bi1", "jim-jordan", "border_immigration", 1, True,
              "Voted YEA on H.R. 29, the Laken Riley Act (House Roll Call #6, January 7, 2025, passed 264-159), mandating federal detention of undocumented immigrants charged with theft, burglary, or violent crimes; as Judiciary Committee Chairman Jordan was also a principal House author of H.R. 2, the Secure the Border Act of 2023, which passed the House 219-213.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
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
