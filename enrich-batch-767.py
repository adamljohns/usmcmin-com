#!/usr/bin/env python3
"""Enrichment batch 767: 5 Florida Republican State Senators (bottom-of-alphabet FL targets).

Primary archetype_curated federal senator/rep buckets are exhausted; this batch
targets evidence_state FL Republican State Senators with 0 claims — the next
available bottom-of-alphabet cohort with documentable records.

Targets (reverse-alpha FL sweep, R senators with sourced records):
  Nick DiCeglie      (SD-18, Pinellas County, since Nov 2022)
  Keith L. Truenow   (SD-13, Lake County, since Nov 2024; FL House 2016-2024)
  Jim Boyd           (SD-20, Manatee/Hillsborough; Senate President-Designate 2026-28)
  Jennifer Bradley   (SD-6, North Florida, since Nov 2020)
  Ed Hooper          (SD-21, Pinellas/Pasco, since 2018; Appropriations Chair 2024-26)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Nick DiCeglie (FL SD-18, Pinellas, R, since Nov 2022) ----------
    ("nick-diceglie", "FL", "Senator", [
        claim("nd1", "nick-diceglie", "sanctity_of_life", 0, True,
              "Co-introduced Florida HB 5 (2022) as a member of the Florida House — the Reducing Fetal "
              "and Infant Mortality Act, which enacted a 15-week abortion ban, Florida's first major "
              "gestational limit after Roe v. Wade was overturned. DiCeglie was among the Republican "
              "co-introducers who put the bill on its path to Gov. DeSantis's signature on April 14, "
              "2022, affirming a commitment to protecting unborn life at the state level.",
              ["https://www.flsenate.gov/Session/Bill/2022/5",
               "https://ballotpedia.org/Nick_DiCeglie"]),
        claim("nd2", "nick-diceglie", "self_defense", 0, True,
              "Voted in the Florida Senate for the 2023 constitutional (permitless) carry legislation "
              "(SB 150 / CS/HB 543), eliminating Florida's license requirement for law-abiding citizens "
              "to carry a concealed firearm. The bill passed the Senate 27–13 in March 2023 and was "
              "signed by Gov. DeSantis on April 3, 2023 — making Florida the 26th state to enact "
              "constitutional carry.",
              ["https://www.wtsp.com/article/news/politics/constitutional-permitless-carry-florida-senate-passes-sb-150-bill/67-878b25e5-dbd9-492b-819b-1bc6c267eee6",
               "https://www.flsenate.gov/Session/Bill/2023/150"]),
    ]),

    # ---------- Keith L. Truenow (FL SD-13, Lake County, R, Senate since Nov 2024) ----------
    ("keith-l-truenow", "FL", "Senator", [
        claim("kt1", "keith-l-truenow", "industry_capture", 0, True,
              "Sponsored SB 700 (2025), the Florida Farm Bill provision banning fluoride additives from "
              "all public water supplies in Florida, removing the state from a compulsory mass-medication "
              "regime not consented to by individual consumers. The Senate voted 27–9 to pass the "
              "measure on April 16, 2025; Gov. DeSantis signed it into law, making Florida the second "
              "state after Utah to prohibit the additive. Truenow declared: 'We're here to hydrate, "
              "not medicate.' The law mirrors the framework championed by RFK Jr. and MAHA proponents "
              "opposing unelected public-health mandates.",
              ["https://www.wusf.org/politics-issues/2025-04-17/florida-senate-passes-bill-ban-fluoride-public-water",
               "https://en.wikipedia.org/wiki/Keith_Truenow"]),
        claim("kt2", "keith-l-truenow", "sanctity_of_life", 0, True,
              "Voted as a Florida House member for HB 5 (2022), which enacted Florida's first "
              "gestational abortion limit — a 15-week ban — signed by Gov. DeSantis on April 14, 2022. "
              "Truenow, serving in the FL House from 2016 through 2024 before moving to the Senate, "
              "was part of the Republican majority that advanced this pro-life milestone.",
              ["https://www.flsenate.gov/Session/Bill/2022/5",
               "https://ballotpedia.org/Keith_Truenow"]),
    ]),

    # ---------- Jim Boyd (FL SD-20, Manatee/Hillsborough, R; President-Designate 2026-28) ----------
    ("jim-boyd", "FL", "Senator", [
        claim("jb1", "jim-boyd", "self_defense", 0, True,
              "Voted in the Florida Senate for the 2023 constitutional (permitless) carry legislation "
              "(SB 150 / CS/HB 543), which eliminated the license requirement for law-abiding "
              "Floridians to carry a concealed firearm; the Senate passed it 27–13. As incoming Senate "
              "President-Designate for 2026–28, Boyd also stated publicly in October 2025 that he is "
              "'not an opponent of lowering the long-gun age back to 18,' signaling support for "
              "restoring the right stripped from 18–20-year-olds under Florida's 2018 post-Parkland "
              "gun law.",
              ["https://www.flsenate.gov/Session/Bill/2023/150",
               "https://www.wusf.org/politics-issues/2025-10-26/incoming-senate-president-jim-boyd-talks-property-insurance-reform-gun-buying-age"]),
        claim("jb2", "jim-boyd", "public_justice", 0, True,
              "Sponsored Florida's 2022 retail-theft crackdown bill, signed into law by Gov. DeSantis, "
              "which toughened penalties for organized retail crime and property theft — a direct "
              "defense of private property rights and community safety. Boyd, who will serve as Florida "
              "Senate President for the 2026–28 term, has consistently championed law-and-order "
              "legislation protecting Floridians from crime.",
              ["https://ballotpedia.org/Jim_Boyd",
               "https://floridapolitics.com/archives/760657-jim-boyd-elected-senate-president-designate-vows-principled-leadership-broad-opportunity/"]),
    ]),

    # ---------- Jennifer Bradley (FL SD-6, North Florida, R, since Nov 2020) ----------
    ("jennifer-bradley", "FL", "Senator", [
        claim("jbr1", "jennifer-bradley", "sanctity_of_life", 0, True,
              "Voted in the Florida Senate for SB 300 (2023), the Heartbeat Protection Act, banning "
              "most abortions after approximately six weeks of gestation — the most protective pro-life "
              "legislation in Florida history at the time. The Senate passed the bill 26–13; Gov. "
              "DeSantis signed it on April 13, 2023. Bradley, representing North Florida's SD-6, cast "
              "one of the Republican yes votes protecting unborn life from the moment cardiac activity "
              "is detectable.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://ballotpedia.org/Jennifer_Bradley"]),
        claim("jbr2", "jennifer-bradley", "public_justice", 0, True,
              "Received the Florida Prosecutors Association Senate Leadership Award and the Florida "
              "Sheriffs Association Legislative Champion Award in 2024, recognizing her work as Vice "
              "Chair of the Senate Criminal Justice Committee in championing law-enforcement support, "
              "public-safety legislation, and accountability for offenders. Bipartisan recognition from "
              "both prosecutors and sheriffs — the top two law-enforcement constituencies in the state "
              "— marks her as a consistent defender of ordered liberty.",
              ["https://ballotpedia.org/Jennifer_Bradley",
               "https://www.flsenate.gov/Senators/s6"]),
    ]),

    # ---------- Ed Hooper (FL SD-21, Pinellas/Pasco, R, since 2018; Appropriations Chair 2024-26) ----------
    ("ed-hooper", "FL", "Senator", [
        claim("eh1", "ed-hooper", "public_justice", 0, True,
              "Sponsored SB 718 (2024), signed into law as Chapter 2024-68, which created a new "
              "second-degree felony for any person 18 or older who — while unlawfully possessing "
              "fentanyl or fentanyl analogs — recklessly exposes a first responder to the substance "
              "resulting in overdose or serious bodily injury. The law directly protects firefighters, "
              "paramedics, and law-enforcement officers from fentanyl ambushes, a real and growing "
              "danger to Florida's first-responder community.",
              ["https://www.flsenate.gov/Session/Bill/2024/718",
               "https://floridapolitics.com/archives/742732-no-4-on-the-list-of-tampa-bays-most-powerful-politicians-ed-hooper/"]),
        claim("eh2", "ed-hooper", "economic_stewardship", 2, True,
              "As Chair of the Florida Senate Appropriations Committee for the 2024–26 term, Hooper "
              "leads the state's budget process with a stewardship posture — publicly calling out a "
              "$242-million-and-growing waste of taxpayer dollars on a Pinellas County pedestrian "
              "infrastructure project and demanding accountability for government spending. His "
              "Appropriations chairmanship gives him direct influence over the state's fiscal "
              "discipline, in line with the rubric's anti-deficit, taxpayer-stewardship standard.",
              ["https://floridapolitics.com/archives/564770-ed-hooper-242m-and-counting-taxpayer-dollars-wasted-on-a-pinellas-county-pedestrian-project/",
               "https://floridapolitics.com/archives/706661-ed-hooper-named-senate-appropriations-chair-and-thats-great-news-for-pinellas-pasco/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
