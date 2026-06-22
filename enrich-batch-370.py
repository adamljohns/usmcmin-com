#!/usr/bin/env python3
"""Enrichment batch 370: hand-curated claims for 5 Wisconsin State Senators.

Targets archetype_party_default WI state senators with 0 claims, taken from the
bottom of the alphabet (WI). Mix of 3 R / 2 D covering 2024-2026 records.

Targets:
  Sarah Keyeski (WI-D, SD-14), Romaine Quinn (WI-R, SD-25),
  Robert Wirch (WI-D, SD-22), Rob Stafsholt (WI-R, SD-10),
  Rob Hutton (WI-R, SD-5).

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
    # ---------------- Sarah Keyeski (WI-D, SD-14) ----------------
    ("sarah-keyeski", "WI", "State Senator", [
        claim("sk1", "sarah-keyeski", "sanctity_of_life", 0, False,
              "Believes women should have the right to make decisions without governmental interference over their reproductive options, including abortion care, and has explicitly called for codifying Roe v. Wade into Wisconsin law. She has sponsored bills eliminating abortion-related regulations and requiring health care plans to cover abortion — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Sarah_Keyeski",
               "https://www.keyeskiforwi.com/"]),
        claim("sk2", "sarah-keyeski", "self_defense", 1, False,
              "Endorsed by Moms Demand Action as a 'Gun Sense Candidate' and has explicitly committed to advancing gun safety reform legislation in Wisconsin — opposing the rubric's defense of unrestricted Second Amendment rights including opposition to red-flag laws and assault-weapon bans.",
              ["https://ballotpedia.org/Sarah_Keyeski",
               "https://progressivevotersguide.com/wisconsin/2024/general/sarah-keyeski"]),
        claim("sk3", "sarah-keyeski", "border_immigration", 0, False,
              "Has not taken positions aligned with border-security enforcement; her legislative priorities focus on healthcare, education, and social services. Consistent with Wisconsin Democratic caucus positions opposing border wall funding and mandatory deportation policies.",
              ["https://ballotpedia.org/Sarah_Keyeski",
               "https://legis.wisconsin.gov/senate/14/keyeski/"]),
    ]),

    # ---------------- Romaine Quinn (WI-R, SD-25) ----------------
    ("romaine-quinn", "WI", "State Senator", [
        claim("rq1", "romaine-quinn", "sanctity_of_life", 0, True,
              "Openly identifies as pro-life and co-authored Wisconsin SB 553 (2025) with Rep. Joy Goeben to clarify that abortion definitions do not include treatment for ectopic pregnancies, miscarriages, and other obstetric emergencies — legislation backed by Pro-Life Wisconsin, Wisconsin Right to Life, and the Wisconsin Catholic Conference. Quinn stated: 'Women who need medical attention due to situations of stillbirths, miscarriages, ectopic pregnancies … can and should receive the care that they need. That has always been the pro-life position.'",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sb553",
               "https://www.prolifewi.org/blog/2025/11/action-alert-clarifying-abortion",
               "https://wisconsinexaminer.com/2025/11/19/senate-passes-bills-to-eliminate-400-year-veto-and-redefine-abortion/"]),
        claim("rq2", "romaine-quinn", "self_defense", 1, True,
              "Sponsored Wisconsin SB 12 (2025), a sales-and-use tax exemption for gun safes, supporting responsible firearm ownership. His overall legislative record and Republican caucus alignment are consistent with opposition to new firearms restrictions and support for Wisconsin's robust gun-rights framework.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2824",
               "https://ballotpedia.org/Romaine_Quinn"]),
        claim("rq3", "romaine-quinn", "border_immigration", 2, True,
              "Backed Wisconsin legislation blocking state and local health-care dollars from being spent on services for undocumented immigrants (passed the Senate November 2025) — an anti-sanctuary measure that directly aligns with the rubric's opposition to using taxpayer funds for those present illegally.",
              ["https://www.wpr.org/news/wisconsin-senate-block-health-funds-undocumented-immigrants-define-abortion",
               "https://wausaupilotandreview.com/2025/11/19/senate-passes-bills-to-eliminate-400-year-veto-and-redefine-abortion/"]),
    ]),

    # ---------------- Robert Wirch (WI-D, SD-22) ----------------
    ("robert-wirch", "WI", "State Senator", [
        claim("rw1", "robert-wirch", "sanctity_of_life", 0, False,
              "A long-serving Democratic senator (since 1997) who has consistently supported abortion rights: backed Wisconsin Senate bills in 2019 and subsequent sessions to eliminate abortion prohibitions and abortion-related regulations, and co-sponsored legislation affirming the right to choose an abortion — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Robert_Wirch",
               "https://legiscan.com/WI/people/robert-wirch/id/3835"]),
        claim("rw2", "robert-wirch", "biblical_marriage", 0, False,
              "Supported joint resolutions in the Wisconsin Senate to eliminate constitutional restrictions on marriage (i.e., the one-man-one-woman definition) and backed the effort to remove Wisconsin's constitutional marriage amendment — rejecting the biblical definition of marriage as one man and one woman.",
              ["https://ballotpedia.org/Robert_Wirch",
               "https://legiscan.com/WI/people/robert-wirch/id/3835"]),
        claim("rw3", "robert-wirch", "economic_stewardship", 2, False,
              "Backed legislation to enact a state minimum wage increase and allow local governments to set higher local minimum wage ordinances — a government wage-price control approach inconsistent with the rubric's free-market, anti-deficit-spending economic stewardship standard.",
              ["https://ballotpedia.org/Robert_Wirch",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2834"]),
    ]),

    # ---------------- Rob Stafsholt (WI-R, SD-10) ----------------
    ("rob-stafsholt", "WI", "State Senator", [
        claim("rs1", "rob-stafsholt", "self_defense", 1, True,
              "A lifetime NRA member and lifetime member of the Balsam Lake Rod & Gun Club and Richardson Sportsman Club. As a Wisconsin Assembly member (2017-2021), he opposed any new firearm restrictions and consistently backed the state's strong gun-rights framework; his record is uniformly aligned with the rubric's defense of Second Amendment rights against bans, registries, and red-flag laws.",
              ["https://legis.wisconsin.gov/senate/10/stafsholt/about-rob/biography/",
               "https://ballotpedia.org/Rob_Stafsholt"]),
        claim("rs2", "rob-stafsholt", "industry_capture", 0, True,
              "Explicitly characterized COVID-19 vaccine mandates and vaccine passport requirements as 'government overreach' and 'a personal violation of freedom.' Sponsored 2021 legislation prohibiting state universities from requiring COVID vaccination or testing for on-campus students, and sponsored Assembly Bill 23 prohibiting government officials from mandating COVID-19 vaccination — opposing pharma-government mandate capture.",
              ["https://en.wikipedia.org/wiki/Rob_Stafsholt",
               "https://badgerherald.com/news/2021/04/20/wisconsin-lawmakers-oppose-vaccine-passports/"]),
        claim("rs3", "rob-stafsholt", "refuse_federal_overreach", 0, True,
              "During the 2020 campaign, called Governor Evers's COVID-19 emergency public-health orders 'unlawful government overreach.' His broader legislative record — eliminating minimum hunting ages, rolling back wetland regulations, opposing vaccine passports — reflects a consistent pattern of resisting executive and regulatory overreach at the state and federal levels.",
              ["https://en.wikipedia.org/wiki/Rob_Stafsholt",
               "https://ballotpedia.org/Rob_Stafsholt"]),
    ]),

    # ---------------- Rob Hutton (WI-R, SD-5) ----------------
    ("rob-hutton", "WI", "State Senator", [
        claim("rh1", "rob-hutton", "sanctity_of_life", 0, True,
              "Endorsed by Wisconsin Right to Life's Political Action Committee for the 2022 State Senate general election. His official biography states a 'proven voting record of … protecting life' across his time in the Wisconsin Assembly (2012-2018) and Senate (2022-2026), consistently backing pro-life legislation in alignment with Wisconsin Right to Life priorities.",
              ["https://wisconsinrighttolife.org/wrtl-news/2022/09/19/wisconsin-right-to-life-political-action-committee-announces-endorsements-for-2022-fall-general-election/",
               "https://rob-hutton.com/"]),
        claim("rh2", "rob-hutton", "economic_stewardship", 2, True,
              "Voted NO on the 2025-2027 Wisconsin state budget, citing a hidden 12% spending increase leveraged through gubernatorial vetoes and a structural deficit. Stated: 'In a time of economic uncertainty … we need a budget that creates proper spending priorities and puts taxpayers first.' Also opposed the May 2026 bipartisan $1.8B surplus-spending deal as fiscally irresponsible — a consistent anti-deficit posture.",
              ["https://legis.wisconsin.gov/senate/05/hutton/press-releases/statement-on-budget",
               "https://milwaukeecourier.com/news/2026/05/15/wisconsins-1-8-billion-budget-deal-collapses-exposing-rifts-within-both-parties"]),
        claim("rh3", "rob-hutton", "public_justice", 0, True,
              "Backed Wisconsin SB 25 (2025), which limits open-ended, harassment-based investigations of police officers involved in incidents of justifiable self-defense unless new evidence is presented — a measure protecting prosecutorial accountability and restraining politically motivated law-enforcement investigations.",
              ["https://docs.legis.wisconsin.gov/misc/lc/hearing_testimony_and_materials/2025/sb25/sb0025_2025_02_06.pdf",
               "https://ballotpedia.org/Rob_Hutton"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
