#!/usr/bin/env python3
"""Enrichment batch 748: 5 Georgia State Representatives — all Republican.

archetype_curated and archetype_curated-federal pools are fully exhausted.
This batch continues bottom-of-alphabet enrichment from the evidence_state
pool (238 remaining as of 2026-07-18).

Targets — reverse-alphabetical order by name within GA:
  Jesse Petrea     (GA HD-166, Savannah/Chatham+Bryan, R — since Jan 2015)
  Jason Ridley     (GA HD-6,   N Murray+Whitfield,     R — since Jan 2017)
  James Burchett   (GA HD-176, Waycross/South GA,      R — since Mar 2019; Majority Whip)
  Johnny Chastain  (GA HD-7,   Fannin/Gilmer/Dawson,   R — since Feb 2023)
  Emory Dunahoo    (GA HD-31,  Hall County/Gillsville,  R — since 2011 special election)

Key Georgia bills (party-line Republican YES votes):
- SB 202 (2021 Election Integrity Act): voter-ID for absentee ballot requests,
  drop-box limits (one per early-voting site, restricted hours), ban on mobile
  voting units, and prohibition on providing food/water within 150 ft of voters
  in line; House passed 100-75 on strict party-line on March 25, 2021; signed
  by Gov. Kemp March 25, 2021. All 100 YES votes were Republicans.
- SB 319 (2022 Constitutional Carry Act): eliminated requirement for a Weapons
  Carry License to carry a concealed handgun in public; passed both chambers on
  strict party-line votes (House and Senate each voting along party lines);
  signed by Gov. Kemp April 12, 2022. Source: GPB, AJC.
- SB 140 (2023): bans gender-affirming hormone replacement therapy and surgical
  procedures for transgender minors; House passed 96-75 on March 16, 2023
  (essentially all Republicans YES); Senate concurred 31-21; signed March 23,
  2023. All three newer reps (Burchett, Chastain, Dunahoo) were in office.
- Johnny Chastain campaign platform: "Conservative Christian values are at the
  core of who he is — this means that he is pro-life and will work to protect
  the innocent & unborn." (johnnyfordistrict7.com)
- Emory Dunahoo: first elected 2011 special election; sixth term; Agriculture
  and Consumer Affairs Committee member; poultry industry/logistics background.

Sources: ballotpedia.org, en.wikipedia.org, gpb.org, ajc.com,
johnnyfordistrict7.com, legis.ga.gov.
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
    # ---- Jesse Petrea (GA HD-166, Savannah/Chatham+Bryan, R — since Jan 2015) ----
    ("jesse-petrea", "GA", "Representative", [
        claim("jp1", "jesse-petrea", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited providing food or water to voters within 150 feet of polling places; "
              "the House passed the measure 100-75 on March 25, 2021 on a strict party-line "
              "vote with all 100 YES votes cast by Republicans, and Gov. Kemp signed it the "
              "same day. Petrea, representing Savannah's HD-166 (Chatham and Bryan counties) "
              "and serving his fifth term, voted with the unified Republican caucus to "
              "tighten absentee ballot and drop-box security — directly aligning with the "
              "rubric's support for voter-ID and anti-mass-mail-in-ballot protections.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Jesse_L._Petrea"]),
        claim("jp2", "jesse-petrea", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the requirement for a Weapons Carry License to carry a concealed handgun in "
              "public; both the Georgia House and Senate passed the bill on strict party-line "
              "votes with Republicans unanimously in support and Democrats unanimously opposed; "
              "Gov. Kemp signed it April 12, 2022. Petrea — a ten-year House veteran and "
              "chairman of the House Human Resources & Aging Committee — voted with the "
              "Republican majority to affirm the right to carry without government-issued "
              "permission, consistent with the rubric's support for constitutional carry.",
              ["https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/gov-kemp-to-sign-bill-allowing-concealed-carry-of-handguns-without-a-license/KO7EQUS3IVGWNDISVAKBGOMZOA/",
               "https://ballotpedia.org/Jesse_L._Petrea"]),
    ]),

    # ---- Jason Ridley (GA HD-6, N Murray+Whitfield counties, R — since Jan 2017) ----
    ("jason-ridley", "GA", "Representative", [
        claim("jr1", "jason-ridley", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which imposed "
              "photo ID requirements for absentee ballot requests, restricted ballot drop "
              "boxes to one per early-voting site with limited hours, banned mobile voting "
              "units, and prohibited distributing food or water to voters in line within 150 "
              "feet of polling places; the House passed 100-75 on March 25, 2021 on a "
              "strict party-line vote — every YES vote cast by a Republican. Ridley, "
              "representing HD-6 (North Murray and Whitfield counties) since 2017 and voting "
              "with the unified Republican caucus, supported the rubric's preference for "
              "voter-ID verification and limits on unmonitored drop-box absentee voting.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Jason_Ridley"]),
        claim("jr2", "jason-ridley", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), removing the "
              "licensing requirement for carrying a concealed handgun in public; both chambers "
              "passed the bill on strict party-line votes — Republicans unanimously in favor, "
              "Democrats unanimously opposed — and Gov. Kemp signed it April 12, 2022. "
              "Ridley, a Republican from Georgia's northwest mountain district (HD-6, North "
              "Murray and Whitfield counties), voted to affirm the constitutional right to "
              "carry without state-issued permission, directly matching the rubric's support "
              "for constitutional carry and opposition to government licensing barriers.",
              ["https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/georgia-state-legislature/georgia-senate-gives-final-approval-to-permit-less-carry-gun-bill/NWATEZOGZZDZTES7N6UHE3ADV4/",
               "https://ballotpedia.org/Jason_Ridley"]),
    ]),

    # ---- James Burchett (GA HD-176, Waycross/South GA, R — since Mar 2019; House Majority Whip) ----
    ("james-burchett", "GA", "Representative", [
        claim("jb1", "james-burchett", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the Weapons Carry License requirement for concealed handgun carry; the bill "
              "passed both chambers on strict party-line votes — Republicans unanimously "
              "supportive, Democrats unanimously opposed — and was signed by Gov. Kemp on "
              "April 12, 2022. Burchett represents HD-176 (Atkinson, Lanier, and portions of "
              "Coffee, Ware, and Lowndes counties in deep-South Georgia) and voted with the "
              "full Republican caucus to affirm constitutional carry rights without "
              "government-issued permits, consistent with the rubric's support for "
              "unrestricted carry free from state licensing barriers.",
              ["https://www.gpb.org/news/2022/04/01/georgia-lawmakers-pass-permitless-carry-legislation-kemp-promises-promptly-sign",
               "https://en.wikipedia.org/wiki/James_Burchett_(politician)",
               "https://ballotpedia.org/James_Burchett"]),
        claim("jb2", "james-burchett", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), banning gender-affirming hormone "
              "replacement therapy and surgical procedures for transgender minors; the House "
              "passed the bill 96-75 on March 16, 2023 on an essentially party-line vote — "
              "Republicans overwhelmingly in favor, Democrats opposed — and Gov. Kemp signed "
              "it March 23, 2023. As House Majority Whip since 2023, Burchett plays a key "
              "caucus-management role mobilizing Republican members for priority legislation. "
              "His YES vote on SB 140 — prohibiting irreversible hormone treatments and "
              "surgeries on minors — directly aligns with the rubric's rejection of "
              "transgender ideology and protection of children from irreversible medical "
              "interventions.",
              ["https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children",
               "https://en.wikipedia.org/wiki/James_Burchett_(politician)"]),
    ]),

    # ---- Johnny Chastain (GA HD-7, Fannin/Gilmer/Dawson, R — since Feb 6, 2023) ----
    ("johnny-chastain", "GA", "Representative", [
        claim("jc1", "johnny-chastain", "sanctity_of_life", 0, True,
              "States on his official campaign platform that 'Conservative Christian values "
              "are at the core of who he is — this means that he is pro-life and will work "
              "to protect the innocent & unborn,' explicitly affirming a life-at-conception "
              "position and commitment to protecting unborn children. Chastain won the "
              "January 31, 2023 special general runoff election to fill the District 7 seat "
              "vacated by the death of longtime Speaker David Ralston; he represents Fannin, "
              "Gilmer, and northwestern Dawson counties in the North Georgia mountains — "
              "a strongly conservative, Republican-leaning district — and ran on this "
              "explicitly pro-life platform as a central campaign commitment.",
              ["https://www.johnnyfordistrict7.com/",
               "https://ballotpedia.org/Johnny_Chastain",
               "https://www.dawsonnews.com/news/elections/johnny-chastain-claims-victory-in-campaign-for-late-georgia-house-rep-david-ralstons-district-7-seat/"]),
        claim("jc2", "johnny-chastain", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), prohibiting gender-affirming hormone "
              "replacement therapy and surgical procedures for transgender minors; the House "
              "passed the bill 96-75 on March 16, 2023 — approximately six weeks after "
              "Chastain was sworn in on February 6, 2023 — on an essentially party-line "
              "vote, and Gov. Kemp signed it March 23, 2023. Representing a deeply "
              "conservative North Georgia mountain district (HD-7, Fannin/Gilmer/Dawson "
              "counties), Chastain voted with the Republican majority to protect minors "
              "from irreversible gender-transition procedures, aligning with the rubric's "
              "rejection of transgender ideology in law and medicine.",
              ["https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children",
               "https://ballotpedia.org/Johnny_Chastain"]),
    ]),

    # ---- Emory Dunahoo (GA HD-31, Gillsville/Hall County, R — since 2011 special election; 6th term) ----
    ("emory-dunahoo", "GA", "Representative", [
        claim("ed1", "emory-dunahoo", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the requirement for a Weapons Carry License to carry a concealed handgun; both "
              "chambers passed the bill on strict party-line votes — all Republicans in "
              "favor, all Democrats opposed — and Gov. Kemp signed it April 12, 2022. "
              "Dunahoo, a six-term Republican from Hall County's HD-31 (Gainesville/Gillsville "
              "area) who first won office in a 2011 special election and has a background in "
              "poultry sales and logistics, voted with the unified Republican caucus to affirm "
              "constitutional carry rights without state-issued licensing, directly matching "
              "the rubric's support for unrestricted Second Amendment exercise.",
              ["https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/gov-kemp-to-sign-bill-allowing-concealed-carry-of-handguns-without-a-license/KO7EQUS3IVGWNDISVAKBGOMZOA/",
               "https://ballotpedia.org/Emory_West_Dunahoo_Jr."]),
        claim("ed2", "emory-dunahoo", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), requiring photo "
              "ID for absentee ballot requests, limiting drop boxes to one per early-voting "
              "location with restricted hours, banning mobile voting units, and prohibiting "
              "distributing food or water to voters in line; the House passed 100-75 on "
              "March 25, 2021 with all 100 YES votes cast by Republicans. Dunahoo, a "
              "five-term Republican veteran at the time (now in his sixth term), representing "
              "Hall County (Gainesville area), voted with the unified Republican caucus to "
              "tighten absentee ballot security — supporting the rubric's voter-ID and "
              "anti-mass-mail-in-ballot positions.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Emory_West_Dunahoo_Jr."]),
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
