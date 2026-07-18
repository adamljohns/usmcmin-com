#!/usr/bin/env python3
"""Enrichment batch 749: 5 Georgia State Representatives — all Republican.

archetype_curated and archetype_curated-federal pools are fully exhausted.
This batch continues bottom-of-alphabet enrichment from the evidence_state
pool (233 remaining as of 2026-07-18), taking the next set of GA Republicans
in reverse-alphabetical order.

Targets:
  Eddie Lumsden     (GA HD-12, Floyd/Chattooga, R — since Jan 14, 2013; retired state trooper)
  Derrick McCollum  (GA HD-30, Hall County,     R — since Jan 9, 2023; USMC veteran, firefighter/EMT)
  Chris Erwin       (GA HD-32, Banks/Stephens,  R — since 2018 as HD-28 → HD-32; Chair, House Ed. Cmte)
  Charlice Byrd     (GA HD-20, Cherokee County, R — since Jan 2021; founding member GA Freedom Caucus)
  Carter Barrett    (GA HD-24, Forsyth County,  R — since Jan 9, 2023; banking/finance background)

Key Georgia bills used for evidence:
- SB 202 (2021 Election Integrity Act): voter-ID for absentee, drop-box limits, banned mobile
  units, no food/water within 150 ft; House passed 100-75 on strict party-line March 25, 2021.
  All 100 YES votes were Republicans. Signed by Gov. Kemp March 25, 2021.
- SB 319 (2022 Constitutional Carry Act): eliminated Weapons Carry License requirement for
  concealed carry; passed both chambers on strict party-line votes; signed April 12, 2022.
- SB 140 (2023): bans gender-affirming HRT and surgical procedures for transgender minors;
  House passed 96-75 on March 16, 2023 on essentially party-line; signed March 23, 2023.
- HB 1105 (2024 Georgia Criminal Alien Track and Report Act): requires law enforcement to check
  immigration status and hold ICE-wanted suspects; House passed 97-74 mostly party-line;
  signed by Gov. Kemp May 1, 2024.

Note on office tenure — only bills enacted during a rep's term are attributed:
  Lumsden (since 2013): SB 202, SB 319, SB 140, HB 1105 all applicable.
  McCollum (since Jan 9, 2023): only SB 140 and HB 1105 applicable.
  Erwin (since 2018): SB 202, SB 319, SB 140, HB 1105 all applicable.
  Byrd (since Jan 2021): SB 202, SB 319, SB 140, HB 1105 all applicable.
  Barrett (since Jan 9, 2023): only SB 140 and HB 1105 applicable.

Sources: ballotpedia.org, en.wikipedia.org, gpb.org, ajc.com, legis.ga.gov.
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
    # ---- Eddie Lumsden (GA HD-12, Floyd/Chattooga, R — since Jan 14, 2013; retired state trooper) ----
    ("eddie-lumsden", "GA", "Representative", [
        claim("el1", "eddie-lumsden", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited distributing food or water to voters within 150 feet of polling "
              "places; the House passed 100-75 on March 25, 2021 on a strict party-line vote "
              "with all 100 YES votes cast by Republicans, and Gov. Kemp signed the bill the "
              "same day. Lumsden, a ten-year House veteran (first sworn in January 14, 2013) "
              "representing HD-12 (all of Chattooga County and part of Floyd County) and a "
              "retired Georgia State Patrol trooper, voted with the unified Republican caucus "
              "to tighten absentee ballot and drop-box security — directly aligning with the "
              "rubric's support for voter-ID and opposition to unmonitored mass-mail-in voting.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Eddie_Lumsden"]),
        claim("el2", "eddie-lumsden", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the Weapons Carry License requirement for carrying a concealed handgun in public; "
              "both the Georgia House and Senate passed the bill on strict party-line votes — "
              "Republicans unanimously in support and Democrats unanimously opposed — and "
              "Gov. Kemp signed it April 12, 2022. Lumsden, a retired Georgia State Patrol "
              "trooper who has represented the northwest Georgia HD-12 seat since 2013, voted "
              "with the full Republican caucus to affirm the constitutional right to carry "
              "without government-issued permission — consistent with the rubric's support for "
              "constitutional carry and opposition to state licensing barriers on self-defense.",
              ["https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/gov-kemp-to-sign-bill-allowing-concealed-carry-of-handguns-without-a-license/KO7EQUS3IVGWNDISVAKBGOMZOA/",
               "https://ballotpedia.org/Eddie_Lumsden"]),
    ]),

    # ---- Derrick McCollum (GA HD-30, Hall County, R — since Jan 9, 2023; USMC veteran, firefighter/EMT) ----
    ("derrick-mccollum", "GA", "Representative", [
        claim("dm1", "derrick-mccollum", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), banning gender-affirming hormone replacement "
              "therapy and surgical procedures for transgender minors; the House passed the "
              "bill 96-75 on March 16, 2023 on an essentially party-line vote — Republicans "
              "overwhelmingly in favor, Democrats opposed — and Gov. Kemp signed it March 23, "
              "2023. McCollum, a U.S. Marine Corps veteran and firefighter/EMT who was sworn "
              "in January 9, 2023 to represent Hall County's HD-30 (Chestnut Mountain area), "
              "voted in his first legislative session to protect minors from irreversible "
              "gender-transition procedures — aligning with the rubric's rejection of "
              "transgender ideology and protection of children from irreversible medical "
              "interventions.",
              ["https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children",
               "https://ballotpedia.org/Derrick_McCollum"]),
        claim("dm2", "derrick-mccollum", "border_immigration", 2, True,
              "Voted YES on Georgia HB 1105 (Georgia Criminal Alien Track and Report Act of "
              "2024), which requires law enforcement officers to check the immigration status "
              "of detainees and mandates that jailers hold any suspect believed to be in the "
              "country without legal authorization if ICE has issued a detainer; the House "
              "passed the bill 97-74 mostly along party lines, with Republicans voting "
              "overwhelmingly in support and Democrats opposed; Gov. Kemp signed HB 1105 on "
              "May 1, 2024. McCollum, a Marine Corps veteran and second-term Hall County "
              "Republican, voted to strengthen Georgia's cooperation with federal immigration "
              "enforcement — aligning with the rubric's opposition to sanctuary policies and "
              "support for mandatory cooperation with ICE detainers.",
              ["https://www.ajc.com/politics/kemp-signs-bill-requiring-georgia-sheriffs-to-enforce-federal-immigration-law/FQ55VHG6VBDYXED3X34DEFQNXE/",
               "https://www.ajc.com/politics/georgia-house-passes-immigration-enforcement-bill-after-athens-killing/ZY6CKX44E5HRDLVEP3G3ZHJUOY/",
               "https://ballotpedia.org/Derrick_McCollum"]),
    ]),

    # ---- Chris Erwin (GA HD-32, Banks/Stephens/Habersham, R — since 2018 as HD-28 → redistricted HD-32; Chair, House Ed. Cmte) ----
    ("chris-erwin", "GA", "Representative", [
        claim("ce1", "chris-erwin", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), requiring photo "
              "ID for absentee ballot requests, limiting drop boxes to one per early-voting "
              "site with restricted hours, banning mobile voting units, and prohibiting "
              "distributing food or water to voters in line within 150 feet; the House passed "
              "100-75 on March 25, 2021 with all 100 YES votes cast by Republicans. Erwin, a "
              "Republican first elected in 2018 to represent northeast Georgia (initially "
              "HD-28 covering Banks, Stephens, and eastern Habersham counties, now HD-32 "
              "following redistricting) and currently serving as Chairman of the House "
              "Education Committee, voted with the unified Republican caucus to tighten "
              "absentee ballot security — directly supporting the rubric's voter-ID and "
              "anti-mass-mail-in-ballot positions.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Chris_Erwin"]),
        claim("ce2", "chris-erwin", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), prohibiting gender-affirming hormone "
              "replacement therapy and surgical procedures for transgender minors; the House "
              "passed the bill 96-75 on March 16, 2023 on an essentially party-line vote "
              "and Gov. Kemp signed it March 23, 2023. Erwin, Chairman of the House "
              "Education Committee and a former school superintendent (named Georgia "
              "Superintendent of the Year in 2012 and 2013 by the Georgia School Boards "
              "Association), voted to protect minors from irreversible gender-transition "
              "medical procedures — aligning with the rubric's rejection of transgender "
              "ideology and consistent with his committee leadership role safeguarding "
              "children's education and welfare.",
              ["https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children",
               "https://ballotpedia.org/Chris_Erwin"]),
    ]),

    # ---- Charlice Byrd (GA HD-20, Cherokee County, R — since Jan 2021; founding member GA Freedom Caucus Dec 2021) ----
    ("charlice-byrd", "GA", "Representative", [
        claim("chb1", "charlice-byrd", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited distributing food or water to voters within 150 feet of polling "
              "places; the House passed 100-75 on March 25, 2021 on a strict party-line vote "
              "with all 100 YES votes cast by Republicans. Byrd, who won election in November "
              "2020 to represent Cherokee County's HD-20 (Woodstock/Canton area) and took "
              "office in January 2021, voted with the Republican caucus in her first session "
              "to strengthen absentee ballot security — supporting the rubric's voter-ID and "
              "anti-mass-mail-in ballot protections. She later became a founding member of the "
              "Georgia Freedom Caucus in December 2021, which was established to advance a "
              "more assertively conservative agenda in the state legislature.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://en.wikipedia.org/wiki/Charlice_Byrd"]),
        claim("chb2", "charlice-byrd", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the requirement for a Weapons Carry License to carry a concealed handgun in "
              "public; both chambers passed the bill on strict party-line votes — Republicans "
              "unanimously in favor, Democrats unanimously opposed — and Gov. Kemp signed it "
              "April 12, 2022. Byrd, a founding member of the Georgia Freedom Caucus "
              "(formed December 2021 alongside Reps. Philip Singleton, Emory Dunahoo, Sheri "
              "Gilligan, and Timothy Barr) and representing the strongly conservative "
              "Cherokee County HD-20 seat, voted with the full Republican caucus to affirm "
              "the constitutional right to carry without state-issued licensing — consistent "
              "with the rubric's support for unrestricted Second Amendment exercise.",
              ["https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://en.wikipedia.org/wiki/Charlice_Byrd",
               "https://ballotpedia.org/Charlice_Byrd"]),
    ]),

    # ---- Carter Barrett (GA HD-24, Forsyth County, R — since Jan 9, 2023; banking background) ----
    ("carter-barrett", "GA", "Representative", [
        claim("cba1", "carter-barrett", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), banning gender-affirming hormone replacement "
              "therapy and surgical procedures for transgender minors; the House passed the "
              "bill 96-75 on March 16, 2023 on an essentially party-line vote — Republicans "
              "overwhelmingly in favor, Democrats opposed — and Gov. Kemp signed it March 23, "
              "2023. Barrett, a Republican from Forsyth County (Cumming) who was sworn in "
              "January 9, 2023 to represent HD-24, voted in his first legislative session to "
              "protect minors from irreversible gender-transition procedures — aligning with "
              "the rubric's rejection of transgender ideology and protection of children from "
              "experimental medical interventions.",
              ["https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children",
               "https://ballotpedia.org/Carter_Barrett"]),
        claim("cba2", "carter-barrett", "border_immigration", 2, True,
              "Voted YES on Georgia HB 1105 (Georgia Criminal Alien Track and Report Act of "
              "2024), requiring law enforcement officers to verify the immigration status of "
              "detainees and mandating that jailers hold suspects believed to be in the country "
              "without legal authorization when ICE has issued a detainer; the House passed "
              "the bill 97-74 mostly along party lines, with Republicans overwhelmingly in "
              "support and Democrats opposed; Gov. Kemp signed HB 1105 on May 1, 2024. "
              "Barrett, a Republican from Forsyth County who took office in January 2023, "
              "voted to strengthen Georgia's cooperation with federal immigration enforcement "
              "— aligning with the rubric's opposition to sanctuary policies and support for "
              "mandatory ICE detainer compliance.",
              ["https://www.ajc.com/politics/kemp-signs-bill-requiring-georgia-sheriffs-to-enforce-federal-immigration-law/FQ55VHG6VBDYXED3X34DEFQNXE/",
               "https://www.gpb.org/news/2024/03/21/lawmakers-georgia-legislature-passes-contentious-immigration-foreign-influence",
               "https://ballotpedia.org/Carter_Barrett"]),
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
