#!/usr/bin/env python3
"""Enrichment batch 790: 5 Florida Republican state representatives.

All archetype_curated and archetype_party_default federal buckets exhausted.
Targets taken from the evidence_state bucket (0 claims), bottom of alphabet
(FL, sorted reverse-alpha by last name, W/V/T names first).

Wyman Duggan (District 12, Duval County / Jacksonville),
Will Robinson Jr. (District 71, Manatee/Sarasota — term-limited 2026),
Webster Barnaby (HD-29, Deltona / Volusia County),
Vanessa Oliver (District 76, Charlotte County / Punta Gorda),
Traci Koster (District 66, Hillsborough/Pinellas County).

Sources: flsenate.gov, myfloridahouse.gov, wusf.org, wsvn.com,
wuft.org, revolt.tv, nbcnews.com, cfpublic.org, news.wfsu.org,
floridapolitics.com, news.wgcu.org, ballotpedia.org,
freedomindex.us.
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
    # ------- Wyman Duggan (FL-R, District 12, Duval County) -------
    ("wyman-duggan", "FL", "Representative", [
        claim("wd1", "wyman-duggan", "self_defense", 0, True,
              "Duggan was a co-introducer of HB 543 (2023 Florida General Session), the legislation that enacted constitutional carry in Florida — permitting any law-abiding adult 21 or older who may lawfully possess a firearm to carry a concealed weapon without first obtaining a government-issued permit. Governor DeSantis signed HB 543 in April 2023, making Florida the 26th constitutional-carry state in the nation. As co-introducer, Duggan formally co-sponsored and advanced the bill through the Florida House. His prior service in the U.S. Marine Corps Reserve (1993–1995) underscores a personal commitment to firearms rights alongside his legislative record.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.wuft.org/public-safety/2023-04-10/florida-passes-permitless-carry-law"]),
        claim("wd2", "wyman-duggan", "public_justice", 0, True,
              "Duggan was the primary House sponsor of HB 601 (2024), which Governor DeSantis signed into law on April 12, 2024. The law bars Florida's civilian police review boards from independently investigating specific complaints about individual officers or correctional officers — removing civilian boards' power to receive, process, and investigate individual misconduct complaints while allowing them to continue discussing systemic policy and training issues. Duggan argued the boards had become 'vehicles to persecute law enforcement officers' and that the goal was to make Florida 'the most law enforcement-friendly state.' The measure passed the Florida House with broad Republican support.",
              ["https://www.flsenate.gov/Session/Bill/2024/601",
               "https://news.wfsu.org/state-news/2024-04-12/its-official-desantis-has-signed-bills-into-law-that-bans-citizen-police-review-boards-in-florida",
               "https://floridapolitics.com/archives/669329-gov-desantis-signs-bills-restricting-harassment-civilian-oversight-of-cops"]),
    ]),

    # ------- Will Robinson Jr. (FL-R, District 71, Manatee/Sarasota) -------
    ("will-robinson-jr", "FL", "Representative", [
        claim("wrj1", "will-robinson-jr", "sanctity_of_life", 0, True,
              "Robinson voted for and vocally supported HB 5 (2022), Florida's 15-week abortion ban (titled 'Reducing Fetal and Infant Mortality Act'). During the bill's debate in the House Health and Human Services Committee, Robinson stated 'It's an important pro-life legislation that we're seeing in this bill' and expressed his desire for Florida to follow Mississippi's lead ahead of the Supreme Court's Dobbs decision. The House passed HB 5 78–39 on February 17, 2022; Governor DeSantis signed it in April 2022. Robinson served four terms as a pro-life Republican representing southwest Florida's Manatee and Sarasota counties.",
              ["https://www.flsenate.gov/Session/Bill/2022/5",
               "https://wsvn.com/news/politics/floridas-controversial-anti-abortion-bill-passes-state-house-health-and-human-services-committee/"]),
        claim("wrj2", "will-robinson-jr", "self_defense", 0, True,
              "Robinson was a leading Florida House proponent of HB 543 (2023), constitutional carry legislation, calling it 'the most pro-Second Amendment bill I've seen in my four years' during the House Judiciary Committee hearing. The bill eliminated the requirement for law-abiding Floridians 21 and older to obtain a concealed-weapons permit before carrying a firearm — making Florida the 26th constitutional-carry state when DeSantis signed HB 543 in April 2023. As a four-term legislator serving on key committees, Robinson's vocal endorsement of the bill reflected his consistent pro-Second Amendment record.",
              ["https://www.wusf.org/politics-issues/2023-02-24/permitless-carry-is-likely-to-pass-in-florida-despite-broad-pushback",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
    ]),

    # ------- Webster Barnaby (FL-R, HD-29, Deltona / Volusia County) -------
    ("webster-barnaby", "FL", "Representative", [
        claim("wb1", "webster-barnaby", "biblical_marriage", 2, True,
              "During a Florida House Commerce Committee hearing on April 10, 2023, Barnaby delivered a high-profile speech opposing transgender ideology while debating the Safety in Private Spaces Act — a bill restricting bathroom access to biological sex. Barnaby declared 'This is the planet Earth, where God created men, male and women, female,' called transgender activists 'mutants not of this world,' and referred to them as 'demons' and 'imps.' He stated: 'It's like I'm watching an X-Men movie...it's like we have mutants living among us on planet Earth.' Though Barnaby subsequently apologized for the language ('I would like to apologize to the trans community for referring to you as demons'), he stood by his support for the underlying legislation and his view that biological sex is fixed at creation. His speech reflects an unambiguous rejection of transgender ideology as incompatible with God's design for male and female.",
              ["https://www.revolt.tv/article/2023-04-11/294828/florida-republican-calls-transgenders-mutants/",
               "https://mynews13.com/fl/orlando/news/2023/04/11/florida-republican-calls-transgender-people--mutants--and--demons-",
               "https://www.nbcnews.com/politics/politics-news/florida-legislator-apologizes-calling-transgender-people-mutants-demon-rcna79063"]),
        claim("wb2", "webster-barnaby", "sanctity_of_life", 0, True,
              "Barnaby has filed multiple anti-abortion bills in the Florida House and is a consistent supporter of Florida's pro-life legislative agenda. Prior to the enactment of Florida's six-week heartbeat protection law, Barnaby filed several anti-abortion bills — none advanced from the legislature at that time, but they signaled his position. After the six-week ban was enacted, Barnaby publicly stated he supports the law as 'a step in the right direction' but believes 'more can be done by the legislature to discourage abortions,' indicating he supports legislation restricting abortion beyond the current statutory framework.",
              ["https://www.cfpublic.org/health/2024-10-17/residents-work-against-abortion-amendment-are-in-search-of-a-true-political-champion",
               "https://ballotpedia.org/Webster_Barnaby"]),
    ]),

    # ------- Vanessa Oliver (FL-R, District 76, Charlotte County) -------
    ("vanessa-oliver", "FL", "Representative", [
        claim("vo1", "vanessa-oliver", "sanctity_of_life", 0, True,
              "Oliver publicly identified herself as pro-life throughout her successful 2024 campaign for Florida House District 76 (Charlotte County) and stated she would 'vote no on Amendment 4' — Florida's November 2024 ballot initiative that would have embedded abortion rights in the state constitution before fetal viability. Amendment 4 required a 60-percent supermajority but fell short at approximately 57 percent in November 2024, preserving Florida's existing six-week heartbeat protection law. Oliver entered the Florida House in January 2025 as a committed pro-life Republican from Punta Gorda.",
              ["https://news.wgcu.org/elections/2024-09-30/sharp-differences-emerge-between-candidates-in-florida-house-district-76-election",
               "https://ballotpedia.org/Vanessa_Oliver"]),
        claim("vo2", "vanessa-oliver", "family_child_sovereignty", 0, True,
              "Oliver sponsored HB 1261 (2026 Florida Legislative Session), which would require Florida Medicaid managed care plans to reimburse licensed home health agencies for private-duty nursing services provided to children requiring continuing care in community residential group homes at a 'prevailing hourly rate' — ensuring adequate Medicaid payment rates for private-sector nurses serving medically complex children in home-like settings rather than forcing institutional placement. Oliver's healthcare legislative agenda draws on her background as a Florida Bar Board-Certified Health Law Attorney and CEO of Ambitrans Ambulance, an ambulance provider employing more than 250 people across five southwest Florida counties.",
              ["https://www.flsenate.gov/Session/Bill/2026/1261",
               "https://ballotpedia.org/Vanessa_Oliver"]),
    ]),

    # ------- Traci Koster (FL-R, District 66, Hillsborough/Pinellas) -------
    ("traci-koster", "FL", "Representative", [
        claim("tk1", "traci-koster", "family_child_sovereignty", 0, True,
              "Koster voted for HB 1 (2023 Florida General Session), the landmark legislation that made Florida's school-choice program universal — extending eligibility for the Family Empowerment Scholarship and Florida Tax Credit Scholarship to any K-12 student in Florida regardless of family income or disability status. The House passed HB 1 by 83–27 on March 17, 2023, and Governor DeSantis signed it; the law made Florida one of the most expansive school-choice states in the nation by giving every family the option to redirect their child's education funding to the school of their choice. As a family law attorney representing District 66 in Hillsborough and Pinellas counties, Koster backed an historic expansion of parental educational freedom.",
              ["https://www.flsenate.gov/Session/Bill/2023/1",
               "https://freedomindex.us/legislator/3307"]),
        claim("tk2", "traci-koster", "border_immigration", 2, True,
              "Koster voted for CS/SB 1808 (2022 Florida General Session), the Florida Immigration Enforcement Act. The law revised the definition of 'sanctuary policy' to include any local directive that prevents law enforcement agencies from sharing immigration-status information with state or federal authorities, and required all Florida law enforcement agencies to honor federal ICE detainers — making sanctuary practices a legal violation. The bill passed the Florida House 77–42 on March 9, 2022. The Florida Freedom Index tracked Koster's vote on SB 1808 as part of her overall legislative record.",
              ["https://www.flsenate.gov/Session/Bill/2022/1808",
               "https://freedomindex.us/legislator/3307"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
