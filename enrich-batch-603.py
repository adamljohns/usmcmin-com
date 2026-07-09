#!/usr/bin/env python3
"""Enrichment batch 603: 4 state R executives — 11 claims.

All archetype_curated federal senator/rep buckets remain depleted.
Continues bottom-of-alphabet evidence_state enrichment pivot, targeting
statewide R officials with 0 claims in the IA/GA/ID/NC range.

Targets:
  Kim Reynolds    (IA) — Governor
  Burt Jones      (GA) — Lieutenant Governor
  Scott Bedke     (ID) — Lieutenant Governor
  Steve Troxler   (NC) — Commissioner of Agriculture
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
    # ---------- Kim Reynolds (IA, Governor) ----------
    ("kim-reynolds", "IA", "Governor", [
        claim("kr1", "kim-reynolds", "sanctity_of_life", 0, True,
              "Signed HF 732 (Iowa's 'Heartbeat Bill') on July 14, 2023, prohibiting abortion after detection of fetal cardiac activity at approximately six weeks of pregnancy. After the Iowa Supreme Court lifted a temporary injunction on June 28, 2024, the law took effect July 29, 2024. Reynolds stated: 'Life and death are determined by a person's heartbeat, and I believe that includes our unborn children. As long as I'm Governor, I will stand up for the sanctity of life.' Received endorsement and 'pro-life champion' designation from SBA Pro-Life America.",
              ["https://governor.iowa.gov/press-release/2023-07-14/gov-reynolds-signs-heartbeat-bill-law",
               "https://governor.iowa.gov/press-release/2024-06-28/gov-reynolds-republican-leaders-release-statements-iowa-supreme-court-fetal-heartbeat-ruling",
               "https://sbaprolife.org/newsroom/press-releases/pro-life-groups-announce-six-figure-campaign-re-elect-iowa-gov-reynolds-expose-hubbell-extremism-2"]),
        claim("kr2", "kim-reynolds", "biblical_marriage", 4, True,
              "Signed SF 418 (February 2025) eliminating gender identity as a protected class from the Iowa Civil Rights Act — making Iowa the first state in the nation to remove such protections — and signed legislation (May 2023) banning sexual-orientation and gender-identity instruction in public schools through grade 6. Also signed laws (March 2023) banning puberty blockers, cross-sex hormones, and gender-affirming surgery for minors, and prohibiting students from using school restrooms that do not correspond to their biological sex.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_Iowa",
               "https://governor.iowa.gov/press-release/2025-06-06/gov-reynolds-signs-list-bills-law"]),
        claim("kr3", "kim-reynolds", "border_immigration", 0, True,
              "Signed Senate File 2340 (April 10, 2024), making it a state crime for individuals previously deported or denied U.S. entry to be present in Iowa. Deployed 109 Iowa National Guard soldiers and 31 DPS officers to Texas's Operation Lone Star in 2023. In 2025 directed the Iowa National Guard to provide logistical support to ICE officials statewide, stating: 'Iowa will continue to assist in the enforcement of federal immigration laws — this time, by working with the Trump Administration to support U.S. Immigration and Customs Enforcement officials in our state.'",
              ["https://governor.iowa.gov/press-release/2024-04-10/gov-reynolds-signs-several-bills-law",
               "https://governor.iowa.gov/press-release/2025-08-12/gov-reynolds-directs-iowa-national-guard-support-federal-immigration-enforcement-mission",
               "https://governor.iowa.gov/press-release/2023-10-25/gov-reynolds-provides-results-on-operation-lone-star-deployment-us-southern"]),
    ]),

    # ---------- Burt Jones (GA, Lieutenant Governor) ----------
    ("burt-jones", "GA", "Lieutenant Governor", [
        claim("bj1", "burt-jones", "sanctity_of_life", 0, True,
              "As a Georgia State Senator, voted for the Living Infants Fairness and Equality (LIFE) Act (HB 481) in 2019, Georgia's heartbeat bill banning most abortions after fetal cardiac activity is detected at approximately six weeks. As Lt. Governor established a Senate committee focused on pregnancy resource centers, adoption reform, and foster care improvements, and has stated he is 'proud of the work that was done in 2019.'",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://www.gpb.org/news/2023/02/02/new-lieutenant-governor-outlines-goals",
               "https://ballotpedia.org/Burt_Jones"]),
        claim("bj2", "burt-jones", "self_defense", 1, True,
              "Co-sponsored Senate Bill 319, the Georgia Constitutional Carry Act of 2021, signed into law by Governor Kemp on April 13, 2022, making Georgia the 25th state to allow law-abiding adults to carry a firearm without a permit. Has backed a proposal to pay public school teachers a $10,000 annual stipend to take voluntary firearms training and carry guns in school. Received NRA endorsement.",
              ["https://legiscan.com/GA/bill/SB319/2021",
               "https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://www.ajc.com/politics/burt-jones-backs-paying-teachers-to-carry-guns-as-he-preps-for-2024-and-beyond/LUJ7KYIXKBFNJECCCECLHGOGOI/"]),
        claim("bj3", "burt-jones", "election_integrity", 0, True,
              "Voted for Georgia's Election Integrity Act of 2021 (SB 202), which replaced signature-matching on absentee ballots with photo/ID verification requirements, restricted unsolicited absentee ballot mailings, and limited drop boxes. As Lt. Governor made election transparency a stated 2026 legislative priority, issuing a formal priority statement on Georgia election accountability and continuing Senate oversight of election administration.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://ltgov.georgia.gov/press-releases/2026-01-14/lt-governor-burt-jones-prioritizes-georgia-election-transparency-and",
               "https://ballotpedia.org/Burt_Jones"]),
    ]),

    # ---------- Scott Bedke (ID, Lieutenant Governor) ----------
    ("scott-bedke", "ID", "Lieutenant Governor", [
        claim("sb1", "scott-bedke", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting rating from Idaho Chooses Life. As Idaho House Speaker, voted in favor of SB 1385 (Idaho's 2020 trigger law banning nearly all abortions after Dobbs) and SB 1309 (the 2022 law enabling family members to sue abortion providers). States his position plainly: 'On abortion my track record is clear. I am pro-life.'",
              ["https://idahocapitalsun.com/2022/10/28/pickens-manweiler-and-bedke-spar-over-abortion-rights-in-idaho-lt-gov-debate/",
               "https://ballotpedia.org/Scott_Bedke"]),
        claim("sb2", "scott-bedke", "self_defense", 1, True,
              "Holds an NRA A+ rating and was endorsed for Lt. Governor by the NRA in April 2022, with the NRA Idaho State Director citing his 'steadfast devotion to protecting the Second Amendment rights of all law-abiding Idahoans.' Supported legislation ensuring Idahoans retain access to firearms, ammunition, and shooting ranges during declared states of emergency.",
              ["https://www.ktvb.com/article/news/politics/national-rifle-association-endorses-scott-bedke-as-idahos-next-lt-governor/277-0e7e4791-29ba-4a10-af84-200ac595e667",
               "https://bedkeforidaho.com/2022/04/national-rifle-association-endorses-scott-bedke-to-be-idahos-next-lieutenant-governor/"]),
        claim("sb3", "scott-bedke", "refuse_federal_overreach", 0, True,
              "Co-signed two official letters opposing Biden administration overreach: a 2021 letter (with Gov. Little, AG Wasden, and Senate Pro Tem Winder) threatening legal action against Biden's federal vaccine mandate on private businesses, stating Idaho 'will have no choice but to take the necessary legal actions to uphold its sovereignty, check the overreach of power by federal bureaucracy'; and a 2024 letter opposing the Biden-Harris administration's 'groundwater grab' and attempts to increase federal oversight of Idaho groundwater.",
              ["https://gov.idaho.gov/pressrelease/idaho-leaders-detail-legal-issues-with-federal-vaccine-mandate-threaten-biden-with-legal-action/",
               "https://gov.idaho.gov/pressrelease/little-bedke-oppose-biden-harris-groundwater-grab/"]),
    ]),

    # ---------- Steve Troxler (NC, Commissioner of Agriculture) ----------
    ("steve-troxler", "NC", "Commissioner", [
        claim("st1", "steve-troxler", "industry_capture", 3, False,
              "Personally requested the raw-milk ban provision in North Carolina's 2025 Farm Act (SB 639), which as introduced would have repealed all legal protections for raw-milk sales and herd-share agreements — the primary mechanism small farmers use to sell unpasteurized milk directly to consumers — aligning with the NC Farm Bureau and NC Dairy Association against food-freedom advocates. Stated: 'Raw milk presents a significant public health risk as there is absolutely no way to ensure its safety.' After bipartisan legislative pushback, the total ban was narrowed in June 2025, but Troxler's opposition to raw-milk food freedom is on the record.",
              ["https://myfox8.com/news/politics/nc/north-carolina-agriculture-commissioner-speaks-out-against-raw-milk-consumption-puts-human-health-at-risk/",
               "https://www.wunc.org/politics/2025-05-05/amid-bird-flu-concerns-nc-farm-act-aims-to-ban-raw-milk-sales-in-the-state",
               "https://www.wral.com/story/raw-milk-back-nc-lawmakers-reverse-course-on-proposed-ban-after-bipartisan-outcry/21994779/",
               "https://www.neusenews.com/index/2025/6/1/op-ed-agriculture-commissioner-steve-troxler-on-raw-milk"]),
        claim("st2", "steve-troxler", "self_defense", 0, False,
              "Posted the NC State Fair as a gun-free zone in 2014, prohibiting even lawful concealed-carry permit holders from carrying at the fairgrounds — contrary to the spirit of North Carolina's 2013 law expanding venues where permitted carriers could carry. Stated: 'I believe that the mix of kids, guns, rides and large crowds is a bad idea.' Grass Roots North Carolina filed a court injunction; the legislature subsequently had to pass a separate bill to lift the fair's gun ban. No NRA rating is on record for Troxler.",
              ["https://www.grnc.org/grnc-alerts-archive/688-grnc-alert-09-29-14-troxler-to-post-nc-state-fair-in-violation-of-law",
               "https://www.wral.com/judge-upholds-ban-on-concealed-weapons-at-state-fair/14074420/",
               "https://en.wikipedia.org/wiki/Steve_Troxler"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
