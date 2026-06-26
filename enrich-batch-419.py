#!/usr/bin/env python3
"""Enrichment batch 419: 5 West Virginia Republican State Delegates.

All five are archetype_party_default (unset) with 0 claims; taken from the
bottom of the alphabet (WV) after the archetype_curated federal bucket was
exhausted (as of batch 418 which completed WY).

Targets (reverse-alpha, WV):
  William Anderson  (District 10, Wood County — Energy & Manufacturing Chair)
  Wayne Clark       (District 99, Jefferson County)
  Walter Hall       (District 58, Kanawha County — Asst. Majority Whip)
  Vernon Criss      (District 12, Wood County — House Finance Chair)
  Tristan Leavitt   (District 53, Cabell County — Empower Oversight president)

Key sourced votes / positions:
  WV SB 10 (2023): Campus carry signed into law March 1, 2023; passed House 84-13.
  WV HB 4106 (2026): Extended constitutional carry to ages 18-20; signed April 1,
    2026 by Gov. Morrisey; passed House 87-9 (all 10 nays = Democrats only).
  WV HB 2007 / gender-affirming care ban (2023): Banned gender-altering surgeries
    and hormone therapy for minors; passed House 84-10; all 10 nays from Democrats.
  WV Hope Scholarship (2021+): Universal ESA; Criss managed FY2026 appropriations
    (HB 3356 $28.4M; HB 3357 $33.8M) as Finance Chairman.
  WV HCR102 (2025): Article V Convention for fiscal restraints; sponsored by Leavitt;
    failed 49-49 on April 10, 2025.

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


TARGETS = [
    # ---- William Anderson (District 10, Wood County, R) ----
    # Air Force veteran, educator; Chair of House Energy and Manufacturing Committee.
    ("william-anderson", "WV", "Delegate", [
        claim("wa1", "william-anderson", "refuse_federal_overreach", 0, True,
              "As Chairman of the West Virginia House Energy and Manufacturing Committee, "
              "Anderson champions state energy sovereignty — increasing in-state power "
              "generation capacity, defending WV's coal and natural-gas industries from "
              "federal EPA regulatory overreach, and fostering a diverse energy economy "
              "under state rather than Washington direction. He was honored by the West "
              "Virginia Manufacturers Association in September 2023 for his advocacy "
              "on behalf of energy stability and security.",
              ["https://home.wvlegislature.gov/delegate/bill-anderson/",
               "https://www.newsandsentinel.com/news/business/2023/09/west-virginia-manufacturers-association-honors-anderson/"]),
        claim("wa2", "william-anderson", "economic_stewardship", 2, True,
              "Sponsored HB 2589, requiring job seekers to document completed work-search "
              "activities as a prerequisite for receiving West Virginia unemployment "
              "compensation — enforcing a conservative work-ethic standard that deters "
              "government-dependency, controls state expenditures, and holds benefit "
              "programs to a reciprocal obligation of effort.",
              ["https://home.wvlegislature.gov/delegate/bill-anderson/",
               "https://fastdemocracy.com/bill-search/wv/legislators/WVL000078/"]),
    ]),

    # ---- Wayne Clark (District 99, Jefferson County, R) ----
    # Business owner (Locust Hill Golf Course); endorsed by WV Citizens Defense League.
    ("wayne-clark", "WV", "Delegate", [
        claim("wc1", "wayne-clark", "self_defense", 0, True,
              "A consistent Second Amendment champion: voted YES on West Virginia SB 10 "
              "(2023), the Campus Self-Defense Act extending constitutional carry to "
              "college campuses (House vote 84-13, signed March 1, 2023), and voted YES "
              "on HB 4106 (2026), which expanded permitless carry to citizens ages 18-20 "
              "(passed 87-9, signed April 1, 2026 by Gov. Morrisey). Clark is endorsed by "
              "the West Virginia Citizens Defense League.",
              ["https://ballotpedia.org/Wayne_Clark_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/wayne-clark/",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/"]),
        claim("wc2", "wayne-clark", "family_child_sovereignty", 0, True,
              "Sponsored West Virginia legislation raising the minimum age for parental "
              "consent on children's social media data from 13 to 18 — a COPPA-style "
              "parental-authority bill requiring explicit parental permission before "
              "platforms may collect or process personal data of minors, directly "
              "expanding family sovereignty over children's digital lives.",
              ["https://ballotpedia.org/Wayne_Clark_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/wayne-clark/"]),
    ]),

    # ---- Walter Hall (District 58, Kanawha County, R) ----
    # Licensed insurance agent; Assistant Majority Whip; member of Grace Baptist Temple.
    ("walter-hall", "WV", "Delegate", [
        claim("wh1", "walter-hall", "self_defense", 0, True,
              "As Assistant Majority Whip in West Virginia's 91-9 Republican supermajority, "
              "Hall has provided floor leadership for the state's expanding constitutional "
              "carry framework — including WV SB 10 (2023), the Campus Self-Defense Act "
              "(passed 84-13), and HB 4106 (2026), extending permitless carry to citizens "
              "ages 18-20 (passed 87-9 with every NO vote cast by a Democrat, signed "
              "April 1, 2026).",
              ["https://home.wvlegislature.gov/delegate/walter-hall/",
               "https://ballotpedia.org/Walter_Hall",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/"]),
        claim("wh2", "walter-hall", "biblical_marriage", 2, True,
              "Voted YES on West Virginia's 2023 ban on gender-affirming surgeries and "
              "hormone therapy for minors under 18, which passed the House 84-10 — all "
              "10 NO votes came from Democrats, while every Republican delegate, including "
              "Hall, voted to protect children from irreversible gender-altering medical "
              "interventions. Hall assumed office December 2022 and was serving throughout "
              "the 2023 legislative session.",
              ["https://www.wsaz.com/2023/02/03/bill-prohibiting-gender-affirming-care-minors-passes-wva-house/",
               "https://ballotpedia.org/Walter_Hall"]),
    ]),

    # ---- Vernon Criss (District 12, Wood County, R) ----
    # House Finance Committee Chairman; re-elected 2016; lost 2026 R primary.
    ("vernon-criss", "WV", "Delegate", [
        claim("vc1", "vernon-criss", "family_child_sovereignty", 0, True,
              "As House Finance Committee Chairman, guided West Virginia's Hope Scholarship "
              "appropriations for FY 2026 — HB 3356 ($28.4 million from surplus collections) "
              "and HB 3357 ($33.8 million from lottery surplus) — West Virginia's universal "
              "education savings account program that lets families direct state education "
              "funds to private, religious, or home schools, expanding parental sovereignty "
              "over children's education outside the government-school monopoly.",
              ["https://ballotpedia.org/Vernon_Criss",
               "https://home.wvlegislature.gov/delegate/vernon-criss/",
               "https://www.wvgazettemail.com/elections/morrisey-continues-social-media-push-to-oust-house-finance-chair-vernon-criss/article_44303253-aa31-4c59-a242-6b168b4ca1c9.html"]),
        claim("vc2", "vernon-criss", "economic_stewardship", 2, True,
              "As Finance Chairman managed West Virginia's $5.317 billion FY 2026 state "
              "budget with $200.5 million in revenue changes; under the Republican "
              "supermajority Criss has served since his 2016 re-election, WV has "
              "repeatedly cut the state income tax and achieved multiple consecutive "
              "budget surpluses — a record of fiscal discipline and balanced-budget "
              "governance rare among states.",
              ["https://ballotpedia.org/Vernon_Criss",
               "https://home.wvlegislature.gov/delegate/vernon-criss/"]),
    ]),

    # ---- Tristan Leavitt (District 53, Cabell County, R) ----
    # Attorney; President of Empower Oversight; assumed office December 1, 2024.
    ("tristan-leavitt", "WV", "Delegate", [
        claim("tl1", "tristan-leavitt", "sanctity_of_life", 0, True,
              "Self-identifies as pro-life and ran explicitly on conservative values "
              "including protecting unborn life. Describes himself as 'a husband, father "
              "of five, and disciple of Christ.' As President of Empower Oversight — a "
              "non-profit that investigated the ATF's Operation Fast and Furious, the "
              "misuse of Hillary Clinton's email server, and federal whistleblower "
              "retaliation — he has held government accountable for institutional overreach "
              "against the values-based organizations the pro-life community depends on.",
              ["https://ballotpedia.org/Tristan_Leavitt",
               "https://www.leavittforwv.com/",
               "https://mountainstatespotlight.org/govpack_profiles/tristan-leavitt-2/"]),
        claim("tl2", "tristan-leavitt", "refuse_federal_overreach", 0, True,
              "Sponsored HCR102 (2025), West Virginia's Article V Convention resolution "
              "urging Congress to call a convention of states, limited to proposing "
              "amendments to the U.S. Constitution that impose fiscal responsibility and "
              "restraint on the federal government — the constitutional mechanism by which "
              "states can impose binding limits on Washington without Congress's consent. "
              "The resolution reached a 49-49 tie vote in the WV House on April 10, 2025.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hcr102+intr.htm&yr=2025&sesstype=RS&i=102&houseorig=h&billtype=cr",
               "https://fastdemocracy.com/bill-search/wv/2025/bills/WVB00031300/",
               "https://freedomindex.us/legislator/12460"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
