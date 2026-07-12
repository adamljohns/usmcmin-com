#!/usr/bin/env python3
"""Enrichment batch 690: 3 cited claims each for 5 sitting TX U.S. Representatives.

Targets sitting members with 5 existing claims from bottom-of-alphabet states (TX).
Adds claims in distinct categories not yet covered: biblical_marriage,
christian_liberty, foreign_policy_restraint, economic_stewardship, industry_capture.

Targets (5 R): Ronny Jackson (TX-13), Randy Weber (TX-14), Pat Fallon (TX-04),
Nathaniel Moran (TX-01), Monica De La Cruz (TX-15).
Each claim cites >=1 reliable source and reflects 2022-2026 voting record /
public positions.

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
    # -------------- Ronny Jackson (TX-13, R) --------------
    ("ronny-jackson", "TX", "Representative", [
        claim("rj-bm2", "ronny-jackson", "biblical_marriage", 2, True,
              "A vocal opponent of transgender ideology who introduced the 'Male or Female Only Act' "
              "(H.R. 6144, 119th Congress, Nov 2025), which prohibits any U.S. government form or "
              "document from offering gender identity options beyond 'male' or 'female.' He also "
              "voted for the FY2025 NDAA provision banning TRICARE coverage of gender-transition "
              "procedures for military dependents, and stated on Newsmax that transgender ideology "
              "is 'a cancer that's spreading across this country.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/6144",
               "https://jackson.house.gov/news/documentsingle.aspx?DocumentID=2462"]),
        claim("rj-cl0", "ronny-jackson", "christian_liberty", 0, True,
              "Cosponsored the Religious Freedom Over Mandates Act (H.R. 6502, 117th Congress), "
              "which barred use of federal funds for any federal records system tracking religious "
              "accommodation requests to COVID-19 vaccine requirements. He also introduced "
              "legislation requiring an Inspector General investigation into the Biden Pentagon's "
              "denial of religious exemption requests from servicemembers under the military "
              "COVID vaccine mandate — explicitly framing mandate resistance as a First Amendment "
              "Free Exercise right.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/6502/all-info",
               "https://jackson.house.gov/news/documentsingle.aspx?DocumentID=2352"]),
        claim("rj-fp1", "ronny-jackson", "foreign_policy_restraint", 1, True,
              "Voted against both major Ukraine supplemental aid packages: NAY on H.R. 7691 "
              "($40.1B, Roll Call #145, May 2022) — one of only 57 House members to oppose "
              "it — and NAY on H.R. 8035 ($60.84B, Roll Call #151, April 2024). He also "
              "voted for three NDAA amendments that would have curtailed or eliminated U.S. "
              "security assistance to Ukraine entirely, reflecting a consistent America-first, "
              "border-before-foreign-aid posture on military entanglements abroad.",
              ["https://www.govtrack.us/congress/votes/117-2022/h145",
               "https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://gopforukraine.com/legislator/ronny-jackson/"]),
    ]),

    # -------------- Randy Weber (TX-14, R) --------------
    ("randy-weber", "TX", "Representative", [
        claim("rw-bm0", "randy-weber", "biblical_marriage", 0, True,
              "Voted NAY on both House roll calls on the Respect for Marriage Act (H.R. 8404): "
              "Roll Call #373 (July 19, 2022, passed 267–157) and Roll Call #513 (December 8, "
              "2022, final passage 258–169). The bill federally codified same-sex marriage and "
              "repealed the Defense of Marriage Act; Weber was among the 169 Republicans "
              "defending the traditional one-man-one-woman definition. GovTrack ranked Weber "
              "the most conservative House member for the 118th Congress.",
              ["https://clerk.house.gov/Votes/2022513",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("rw-cl0", "randy-weber", "christian_liberty", 0, True,
              "Describes himself as 'first and foremost a Christian, a Conservative and then a "
              "Republican in that order' and publicly identifies July 2, 1973 as his conversion "
              "date. He advocates returning 'the Bible, prayer and the pledge back in schools' "
              "and cosponsored the GRACE Act (H.R. 5075, 119th Congress), which prohibits "
              "federal education funding to institutions that deny religious exemptions to "
              "vaccination requirements — directly protecting faith-based religious free "
              "exercise against government mandate pressure.",
              ["https://thepostnewspaper.net/2022/08/20/christian-values-foundation-for-weber-at-home-congress/",
               "https://www.congress.gov/bill/119th-congress/house-bill/5075/text"]),
        claim("rw-fp1", "randy-weber", "foreign_policy_restraint", 1, True,
              "Shifted from supporting early Ukraine aid to consistently opposing open-ended "
              "military entanglement: voted NAY on H.R. 5692 ($24B Ukraine Security "
              "Supplemental, House Vote #503, Sep 2023) and NAY on H.R. 8035 ($60.84B "
              "Ukraine Security Supplemental, Roll Call #151, Apr 2024). He also voted for "
              "three 2023 NDAA amendments that would have cut or prohibited all U.S. security "
              "assistance to Ukraine. Republicans for Ukraine awarded Weber an 'F' (Very Poor) "
              "grade on their congressional report card.",
              ["https://www.govtrack.us/congress/votes/118-2023/h503",
               "https://clerk.house.gov/Votes/2024151",
               "https://gopforukraine.com/legislator/randy-weber/"]),
    ]),

    # -------------- Pat Fallon (TX-04, R) --------------
    ("pat-fallon", "TX", "Representative", [
        claim("pf-bm0", "pat-fallon", "biblical_marriage", 0, True,
              "Voted NAY on the Respect for Marriage Act (H.R. 8404) on both House votes: "
              "Roll Call #373 (July 19, 2022) and the final Roll Call #513 (December 8, 2022, "
              "passed 258–169), which federally codified same-sex marriage. CatholicVote "
              "confirms his NAY alongside other key social-conservative votes including YEA "
              "on the Born-Alive Abortion Survivors Protection Act and YEA on a resolution "
              "condemning attacks on pro-life organizations.",
              ["https://clerk.house.gov/Votes/2022513",
               "https://catholicvote.org/scorer/pat-fallon/"]),
        claim("pf-bm2", "pat-fallon", "biblical_marriage", 2, True,
              "Cosponsored the Protection of Women and Girls in Sports Act in both the 117th "
              "Congress (H.R. 426, cosponsor Apr 2022) and the 118th Congress (H.R. 734, "
              "which passed the House 219–203 on April 20, 2023), amending Title IX to "
              "define sex by reproductive biology at birth and bar biological males from "
              "federally funded female athletic programs. He also voted for the FY2025 NDAA, "
              "which included a ban on TRICARE coverage of gender-transition procedures for "
              "military dependents.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/426/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/734/all-info",
               "https://www.govtrack.us/congress/votes/118-2023/h192"]),
        claim("pf-ic0", "pat-fallon", "industry_capture", 0, True,
              "Sponsored H.R. 5009 (117th Congress, Aug 2021) to prohibit the District of "
              "Columbia government from requiring individuals to present COVID-19 vaccination "
              "documentation as a condition of entering any building or venue — one of the "
              "earliest federal anti-mandate bills. He also signed a letter to President Biden "
              "in September 2021 opposing all federal vaccine mandates, and publicly backed "
              "the Vaccine Mandate Reenlistment Act to restore servicemembers discharged for "
              "vaccine refusal to their prior rank and pay.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/5009/all-info",
               "https://fallon.house.gov/news/documentsingle.aspx?DocumentID=80"]),
    ]),

    # -------------- Nathaniel Moran (TX-01, R) --------------
    ("nathaniel-moran", "TX", "Representative", [
        claim("nm-es2", "nathaniel-moran", "economic_stewardship", 2, True,
              "Sponsored the Principles-Based Balanced Budget Amendment as H.J.Res. 80 "
              "(118th Congress) and reintroduced it as H.J.Res. 110 (119th Congress), "
              "constitutionally requiring Congress to balance the budget. He backed this "
              "with votes: voted NO on the Fiscal Responsibility Act of 2023 (H.R. 3746, "
              "Roll Call #243) as 'not going far enough,' and in December 2024 voted against "
              "the Trump-backed CR with a two-year debt ceiling increase, stating 'I cannot "
              "support a blank check for spending in the form of a two-year debt limit "
              "increase.'",
              ["https://www.govtrack.us/congress/bills/118/hjres80/text",
               "https://www.congress.gov/bill/119th-congress/house-joint-resolution/110/text",
               "https://www.govtrack.us/congress/votes/118-2023/h243"]),
        claim("nm-bm2", "nathaniel-moran", "biblical_marriage", 2, True,
              "Voted YES on H.R. 28, the Protection of Women and Girls in Sports Act "
              "(House Roll Call #12, January 14, 2025, passed 218–206), issuing a statement: "
              "'I was proud to vote for this critical' legislation barring biological males "
              "from competing in federally funded female athletic programs. He had also voted "
              "for the equivalent H.R. 734 in the 118th Congress (passed 219–203, April 2023).",
              ["https://moran.house.gov/news/documentsingle.aspx?DocumentID=930",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("nm-cl0", "nathaniel-moran", "christian_liberty", 0, True,
              "Cosponsored the Fair Treatment of Religious Organizations Act (H.R. 8117, "
              "119th Congress, introduced Mar 2026), which amends IRC §501 to bar the IRS "
              "from revoking a religious organization's tax-exempt status based on its beliefs "
              "or practices regarding marriage, sexuality, or gender identity. Personally "
              "states: 'My political worldview is entirely informed by my Judeo-Christian "
              "worldview through the lens of Holy Scripture through the Bible,' and spoke at "
              "the 2024 Christians Engaged Conference about his faith-driven call to office.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/8117",
               "https://stream.org/faith-family-and-public-service-the-call-of-congressman-nathaniel-moran/"]),
    ]),

    # -------------- Monica De La Cruz (TX-15, R) --------------
    ("monica-de-la-cruz", "TX", "Representative", [
        claim("mdlc-bm0", "monica-de-la-cruz", "biblical_marriage", 0, True,
              "Has publicly stated: 'Marriage is a God-ordained, sacred and legal union of "
              "one man and one woman. No government has the authority to alter this "
              "definition.' She was not in Congress for the 2022 Respect for Marriage Act "
              "vote but has affirmed the traditional biblical definition of marriage as the "
              "proper legal standard, in direct opposition to the federal codification of "
              "same-sex marriage.",
              ["https://ivoterguide.com/candidate/51859/race/6572/election/1214"]),
        claim("mdlc-bm2", "monica-de-la-cruz", "biblical_marriage", 2, True,
              "Cosponsored and voted for the Protection of Women and Girls in Sports Act "
              "(H.R. 734, 118th Congress, passed 219–203, House Roll Call #192, April 20, "
              "2023), amending Title IX to bar transgender women from federally funded "
              "female sports programs. Her public statement: 'Biological males should not be "
              "allowed to participate in women's sports or occupy biological women's spaces "
              "whether it be bathrooms, locker rooms, sorority houses, women's shelters, or "
              "prison.'",
              ["https://www.congress.gov/bill/118th-congress/house-bill/734/all-info",
               "https://clerk.house.gov/Votes/2023192"]),
        claim("mdlc-fp1", "monica-de-la-cruz", "foreign_policy_restraint", 1, True,
              "Voted NAY on H.R. 8035, the Ukraine Security Supplemental Appropriations Act "
              "(Roll Call #151, April 20, 2024, passed 311–112), the $60.84 billion Ukraine "
              "military and humanitarian aid package. She was among approximately 15 Texas "
              "Republicans voting against, with opposition tied to demands for border-security "
              "legislation before committing further U.S. resources to foreign military "
              "entanglements.",
              ["https://clerk.house.gov/Votes/2024151",
               "https://www.texastribune.org/2024/04/20/texas-congress-ukraine-israel-tik-tok/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
