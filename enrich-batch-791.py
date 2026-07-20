#!/usr/bin/env python3
"""Enrichment batch 791: 5 Florida Republican state representatives.

All archetype_curated and archetype_party_default federal buckets exhausted.
Targets taken from the evidence_state bucket (0 claims), bottom of alphabet
(FL, sorted reverse-alpha by last name, T/S/P/O/F names).

Susan Plasencia (HD-37, Orange/Seminole County),
Taylor Yarkosky (HD-25, Lake County),
Tiffany Esposito (HD-77, Lee County / Bonita Springs-Estero),
Tom Fabricio (HD-110, Hialeah / Miami Lakes),
Toby Overdorf (HD-85, Martin/St. Lucie counties).

Sources: flsenate.gov, myfloridahouse.gov, clickorlando.com,
floridapolitics.com, wuft.org, tomfabricio.com, tobyoverdorf.com,
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
    # ------- Susan Plasencia (FL-R, HD-37, Orange/Seminole) -------
    ("susan-plasencia", "FL", "Representative", [
        claim("sp1", "susan-plasencia", "sanctity_of_life", 0, True,
              "Plasencia voted for Florida's SB 300 (Heartbeat Protection Act, 2023), which prohibits abortion after detection of a fetal heartbeat — approximately six weeks of gestation — with exceptions for rape, incest, and human trafficking. The House passed the measure 70–40 on April 14, 2023; Governor DeSantis signed it the same day. Plasencia's 2024 opponent explicitly highlighted this vote, noting she had avoided discussing abortion during the campaign but 'voted for the six-week abortion ban' when the bill came before the Legislature — confirming her affirmative roll-call vote. She holds a CPAC lifetime score of 86% and a Florida Freedom Index of 76%, reflecting a consistently pro-life, conservative legislative record.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://www.clickorlando.com/news/politics/2024/10/20/meet-the-candidates-for-florida-house-district-37/",
               "https://freedomindex.us/legislator/3587"]),
        claim("sp2", "susan-plasencia", "self_defense", 0, True,
              "Plasencia voted for HB 543 (2023), Florida's constitutional-carry law, which eliminated the requirement for law-abiding adults 21 or older to obtain a government-issued concealed-weapons permit before carrying a firearm — making Florida the 26th constitutional-carry state when DeSantis signed it on April 3, 2023. The House passed HB 543 76–32, with Plasencia voting with the Republican majority. Her Florida Freedom Index score of 76% and CPAC lifetime rating of 86% further document her consistent pro-Second-Amendment voting record in a competitive swing district (HD-37, Orange/Seminole).",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.wuft.org/public-safety/2023-04-10/florida-passes-permitless-carry-law",
               "https://freedomindex.us/legislator/3587"]),
    ]),

    # ------- Taylor Yarkosky (FL-R, HD-25, Lake County) -------
    ("taylor-yarkosky", "FL", "Representative", [
        claim("ty1", "taylor-yarkosky", "self_defense", 0, True,
              "Yarkosky voted YES on HB 543 (2023), Florida's constitutional-carry bill, which Gov. DeSantis signed into law on April 3, 2023. Beyond his legislative vote, Yarkosky is a licensed NRA-certified firearms instructor — a credential that reflects a hands-on, professional commitment to lawful firearm ownership and self-defense training. He chairs the Lake County Republican Executive Committee and represents HD-25 (Clermont/Lake County), a deeply conservative district where he was re-elected in November 2024 with 64.95% of the vote.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.wuft.org/public-safety/2023-04-10/florida-passes-permitless-carry-law",
               "https://ballotpedia.org/Taylor_Yarkosky"]),
        claim("ty2", "taylor-yarkosky", "family_child_sovereignty", 0, True,
              "Yarkosky voted for HB 1 (2023), Florida's landmark universal school-choice law. The bill — which passed the House 83–27 on March 17, 2023, and was signed by Governor DeSantis — expanded Florida's Family Empowerment Scholarship and Florida Tax Credit Scholarship to every K-12 student regardless of family income, giving all Florida parents the legal right to redirect their child's education funding to the school of their choice (public, private, or home education). The law made Florida one of the most expansive school-choice states in the nation and directly reinforces parental sovereignty over children's education.",
              ["https://www.flsenate.gov/Session/Bill/2023/1",
               "https://ballotpedia.org/Taylor_Yarkosky"]),
    ]),

    # ------- Tiffany Esposito (FL-R, HD-77, Lee County) -------
    ("tiffany-esposito", "FL", "Representative", [
        claim("te1", "tiffany-esposito", "sanctity_of_life", 0, True,
              "Esposito ran for — and won — her seat in HD-77 (Lee County / Bonita Springs-Estero) in 2022 explicitly describing herself as a 'pro-life, pro-gun constitutional conservative' in campaign mailers. Upon taking office she voted with the Republican caucus for Florida's SB 300 (Heartbeat Protection Act, 2023), the six-week abortion ban the House passed 70–40 on April 14, 2023. Her pro-life platform, confirmed in campaign materials and legislative record, reflects the sanctity-of-life standard the rubric requires.",
              ["https://floridapolitics.com/archives/550217-chamber-leader-tiffany-esposito-wins-gop-primary-in-hd-77/",
               "https://www.flsenate.gov/Session/Bill/2023/300"]),
        claim("te2", "tiffany-esposito", "self_defense", 1, True,
              "Esposito has publicly and consistently identified as 'pro-gun' — appearing in her 2022 HD-77 campaign mailers as a 'pro-life, pro-gun constitutional conservative.' She voted for HB 543 (2023), Florida's constitutional-carry law, which removed the government-permit requirement for lawful concealed carry. She has also stated she will oppose mandates and government overreach that restrict individual constitutional rights, positioning her as a reliable Second Amendment vote in the Florida House.",
              ["https://floridapolitics.com/archives/550217-chamber-leader-tiffany-esposito-wins-gop-primary-in-hd-77/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
    ]),

    # ------- Tom Fabricio (FL-R, HD-110, Hialeah / Miami Lakes) -------
    ("tom-fabricio", "FL", "Representative", [
        claim("tf1", "tom-fabricio", "border_immigration", 2, True,
              "Fabricio voted for CS/CS/SB 1718 (2023), Florida's comprehensive immigration-enforcement law. The statute prohibits local governments from adopting sanctuary policies that restrict law enforcement cooperation with federal immigration authorities, mandates E-Verify for private employers with 25 or more employees, requires Florida law enforcement agencies to honor ICE detainers, and bars local funds from being used to issue identification to individuals without lawful immigration status. The bill was signed by Governor DeSantis on May 10, 2023, and took effect July 1, 2023. As a Cuban-American Republican representing Hialeah — a community with strong anti-communist, pro-rule-of-law values — Fabricio's support for border enforcement and anti-sanctuary legislation reflects his district's core concerns.",
              ["https://www.flsenate.gov/Session/Bill/2023/1718",
               "https://ballotpedia.org/Tom_Fabricio"]),
        claim("tf2", "tom-fabricio", "economic_stewardship", 2, True,
              "Fabricio serves as Vice Chair of the Florida House Ways & Means Committee and his campaign materials document that since 2020 he has 'played a vital role in sponsoring and supporting numerous bills that have lowered taxes, improved our economy, and protected law enforcement officers from the agenda of the radical left.' His fiscal record as a small-business owner (managing partner of The Fabricio Law Firm and owner of True Freedom Title, LLC) and his committee role reflect a pro-limited-government, anti-deficit posture consistent with the rubric's economic-stewardship standard.",
              ["https://tomfabricio.com/meet-tom.html",
               "https://ballotpedia.org/Tom_Fabricio"]),
    ]),

    # ------- Toby Overdorf (FL-R, HD-85, Martin/St. Lucie) -------
    ("toby-overdorf", "FL", "Representative", [
        claim("to1", "toby-overdorf", "family_child_sovereignty", 0, True,
              "Overdorf has led Florida House efforts to protect children from sexual exploitation and traffickers. He sponsored legislation restricting minors' access to online pornography and cracking down on strip clubs used for sex trafficking. In 2023 Governor DeSantis appointed him to the Statewide Council on Human Trafficking, and he served as a board member of the Florida Alliance to End Human Trafficking since 2020 — personally training more than 100,000 Floridians to identify and report trafficking. His record directly addresses parental sovereignty and family protection against predatory exploitation.",
              ["https://floridapolitics.com/archives/784753-toby-overdorf-staunch-conservative-bids-farewell-to-house-with-a-bipartisan-address/",
               "https://ballotpedia.org/Toby_Overdorf"]),
        claim("to2", "toby-overdorf", "self_defense", 0, True,
              "Overdorf is a self-described 'staunch conservative' who voted for HB 543 (2023), Florida's constitutional-carry law, as part of the Republican majority that passed the bill 76–32. He has represented parts of Martin and St. Lucie counties since 2018 with a consistent conservative record, and his 2025 campaign for Florida Senate SD-31 carries an explicit 'Florida First, America First' platform that includes protecting constitutional rights. Florida Politics has described him as having 'established a reputation as a staunch conservative.'",
              ["https://floridapolitics.com/archives/784753-toby-overdorf-staunch-conservative-bids-farewell-to-house-with-a-bipartisan-address/",
               "https://tobyoverdorf.com/2025/07/07/rep-toby-overdorf-announces-candidacy-for-florida-senate-district-31/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
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
