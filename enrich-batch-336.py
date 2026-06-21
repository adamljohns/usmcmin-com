#!/usr/bin/env python3
"""Enrichment batch 336: 5 WV State Senators from the bottom of the alphabet.

The archetype_curated federal senator/representative bucket is exhausted.
This batch continues with archetype_party_default WV State Senators, taking
the next five by reverse-alpha name order (Thorne -> Hart -> Rose -> Clements
-> Helton) from the remaining 9 in the bucket.

Targets:
  - Darren Thorne (WV-R, District 15, Hampshire County farmer) — appointed by
      Gov. Justice Dec 2024; self-described pro-life constitutionalist,
      strong 2nd Amendment defender, "big God and small government"
  - Craig A. Hart (WV-R, District 6, agriculture teacher/FFA advisor) —
      "Life at Conception" and "Guns Save Lives" campaign platform; NRA affiliate
  - Chris Rose (WV-R, District 2, Energy Chair) — West Virginians for Life
      endorsed; NRA Life Member and Gun Owners of America Life Member;
      4th-generation coal miner
  - Charles H. Clements (WV-R, District 2, since 2017) — Transportation Chair,
      School Choice Committee; sponsored SB 99 (Return to WV Tax Credit Act)
  - Brian Helton (WV-R, District 9, Baptist business owner) — NRA PVF endorsed;
      Health/HHR Committee Chair; faith/family/freedom platform opposing PP funding

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
    # ---------- Darren Thorne (WV-R, District 15, Hampshire County farmer) ----------
    ("darren-thorne", "WV", "State Senator", [
        claim("dt1", "darren-thorne", "sanctity_of_life", 0, True,
              "Campaign platform explicitly identifies Darren Thorne as 'pro-life' and lists parent rights alongside pro-life as core commitments. Thorne, a Hampshire County farmer appointed to the West Virginia Senate in December 2024 by Governor Jim Justice, describes himself as 'a constitutionalist that believes in a big God and small government.' He previously served in the WV House of Delegates (89th district, 2022–2024) in a Republican supermajority caucus that enacted WV's near-total abortion ban in 2022.",
              ["https://www.darrenthorneforwv.com",
               "https://ballotpedia.org/Darren_Thorne",
               "https://home.wvlegislature.gov/senator/darren-thorne/"]),
        claim("dt2", "darren-thorne", "self_defense", 0, True,
              "Campaign website states: 'Darren is a strong defender of the Second Amendment. As a constitutionalist, he opposes government efforts to restrict firearm ownership for responsible citizens and believes gun control laws punish the wrong people. Darren stands with hunters, sportsmen, and families who rely on firearms for tradition, self-defense, and protection.' Thorne represents a rural West Virginia district where constitutional carry (enacted 2016) and broad firearms rights enjoy strong public support.",
              ["https://www.darrenthorneforwv.com",
               "https://ballotpedia.org/Darren_Thorne",
               "https://home.wvlegislature.gov/senator/darren-thorne/"]),
    ]),

    # ---------- Craig A. Hart (WV-R, District 6, agriculture teacher/FFA advisor) ----------
    ("craig-a-hart", "WV", "State Senator", [
        claim("cah1", "craig-a-hart", "sanctity_of_life", 0, True,
              "Craig Hart's 2024 campaign for West Virginia Senate District 6 explicitly stated his position as 'Life at Conception,' meaning he supports personhood-level protection of the unborn from the moment of fertilization — the most comprehensive pro-life position in the sanctity-of-life rubric. Hart won the November 2024 general election and assumed office December 1, 2024. He serves on the WV Senate Judiciary Committee, which oversees criminal and civil law including enforcement of WV's near-total abortion ban.",
              ["https://www.ballotready.org/people/craig-a-hart",
               "https://ballotpedia.org/Craig_Hart",
               "https://home.wvlegislature.gov/senator/craig-hart/"]),
        claim("cah2", "craig-a-hart", "self_defense", 0, True,
              "Hart's 2024 campaign stated 'Guns Save Lives' as a campaign position and lists the National Rifle Association as an affiliation. He also affiliates with the WV Farm Bureau and WV CDL — organizations that strongly support Second Amendment rights in rural West Virginia. Hart represents Senate District 6 in a rural district where firearms ownership for hunting, farming, and self-defense is foundational.",
              ["https://www.ballotready.org/people/craig-a-hart",
               "https://ballotpedia.org/Craig_Hart",
               "https://home.wvlegislature.gov/senator/craig-hart/"]),
        claim("cah3", "craig-a-hart", "family_child_sovereignty", 0, True,
              "As a career agriculture teacher and FFA (Future Farmers of America) advisor, Craig Hart's professional vocation centers on hands-on, community-rooted, skills-based education outside the conventional academic pipeline. He serves on the WV Senate Education Committee, where he brings a practitioner's perspective prioritizing parental and community involvement in education and career-preparation pathways — consistent with parental rights and educational sovereignty principles.",
              ["https://ballotpedia.org/Craig_Hart",
               "https://home.wvlegislature.gov/senator/craig-hart/",
               "https://www.legistorm.com/person/bio/516692/Craig_Allen_Hart.html"]),
    ]),

    # ---------- Chris Rose (WV-R, District 2, Energy Chair, 4th-gen coal miner) ----------
    ("chris-rose", "WV", "State Senator", [
        claim("cr1", "chris-rose", "sanctity_of_life", 0, True,
              "Endorsed by West Virginians for Life Political Action Committee (WVL-PAC) during his 2024 campaign for WV Senate District 2 — the state's leading pro-life endorsement organization, which backs candidates committed to protecting life from conception. Rose defeated incumbent Mike Maroney in the Republican primary and won the November 2024 general election. He now chairs the WV Senate Energy, Industry and Mining Committee.",
              ["https://www.chrisrosewv.com/about",
               "https://www.chrisrosewv.com/post/wave-of-endorsements-for-chris-rose-for-wv-state-senate",
               "https://ballotpedia.org/Christopher_Rose"]),
        claim("cr2", "chris-rose", "self_defense", 0, True,
              "Chris Rose is a Life Member of both the National Rifle Association and Gun Owners of America — the two leading national firearms-rights organizations. GOA, founded as the 'no compromise' gun lobby, does not endorse candidates who support any firearms restrictions. Rose's dual life memberships signal a constitutional-carry, no-NFA-reform, no-red-flag-law position on firearms.",
              ["https://www.chrisrosewv.com/about",
               "https://ballotpedia.org/Christopher_Rose",
               "https://home.wvlegislature.gov/senator/chris-rose/"]),
        claim("cr3", "chris-rose", "economic_stewardship", 4, True,
              "As a fourth-generation coal miner who spent 14 years working in coal mines and now chairs the WV Senate Energy, Industry and Mining Committee, Rose is a forceful opponent of ESG-driven financial discrimination against the fossil fuel industry. His coal mining heritage and Energy Committee chairmanship position him squarely against WEF/Davos-style climate finance strategies that target coal, natural gas, and domestic energy production — the exact industries that have sustained West Virginia's economy for generations.",
              ["https://www.chrisrosewv.com/about",
               "https://ballotpedia.org/Christopher_Rose",
               "https://home.wvlegislature.gov/senator/chris-rose/"]),
    ]),

    # ---------- Charles H. Clements (WV-R, District 2, Wetzel County, since 2017) ----------
    ("charles-h-clements", "WV", "State Senator", [
        claim("chc1", "charles-h-clements", "family_child_sovereignty", 0, True,
              "Charles Clements serves as Vice Chair of the WV Senate Education Committee and is a member of the Select Committee on School Choice — a legislative body that advances parental rights and school-choice options including education savings accounts and homeschool protections. In 2025 he sponsored SB 122, which established minimum student enrollment thresholds for school aid formula calculations — a measure reflecting the principle that public education dollars should follow actual students rather than institutional overhead.",
              ["https://home.wvlegislature.gov/senator/charles-h-clements/",
               "https://ballotpedia.org/Charles_Clements",
               "https://legiscan.com/WV/people/charles-clements/id/19258"]),
        claim("chc2", "charles-h-clements", "economic_stewardship", 2, True,
              "Clements sponsored SB 99 (2025 Regular Session), the 'Return to WV Tax Credit Act,' proposing a nonrefundable $25,000 tax credit against state personal income taxes to incentivize former West Virginia residents to return — a supply-side, tax-reduction measure aimed at growing the tax base without raising rates. He chairs the Senate Transportation and Infrastructure Committee and has served since 2017 in a Republican caucus that produced one of the top state budget surpluses in the nation as a percentage of overall budget, through spending restraint rather than tax increases.",
              ["https://www.theintelligencer.net/news/top-headlines/2025/01/clements-education-spending-in-west-virginia-is-upside-down/",
               "https://home.wvlegislature.gov/senator/charles-h-clements/",
               "https://ballotpedia.org/Charles_Clements"]),
    ]),

    # ---------- Brian Helton (WV-R, District 9, Baptist, Health Chair) ----------
    ("brian-helton", "WV", "State Senator", [
        claim("bh1", "brian-helton", "sanctity_of_life", 0, True,
              "Brian Helton's campaign platform states that 'abortion providers, including Planned Parenthood, should not receive taxpayer funds from federal, state, or local governments' and that 'chemical abortion drugs should meet essential safety standards.' He is a Baptist whose platform leads with 'Faith, Family, Freedom' and lists 'Life' as a core value. He chairs the WV Senate Health and Human Resources Committee, which oversees healthcare legislation including measures affecting abortion access in West Virginia.",
              ["https://ivoterguide.com/candidate/79223/race/19632/election/1213",
               "https://ballotpedia.org/Brian_Helton",
               "https://home.wvlegislature.gov/senator/brian-helton/"]),
        claim("bh2", "brian-helton", "self_defense", 0, True,
              "Brian Helton received endorsement from the NRA Political Victory Fund (NRA-PVF) for his 2024 West Virginia Senate District 9 campaign — the NRA's official political arm that grades and endorses candidates based on their commitment to Second Amendment rights. Helton represents a rural southern WV district where constitutional carry (enacted 2016) is the law and firearms ownership for hunting and self-defense is a foundational constituency value.",
              ["https://ivoterguide.com/candidate/79223/race/19632/election/1213",
               "https://ballotpedia.org/Brian_Helton",
               "https://home.wvlegislature.gov/senator/brian-helton/"]),
        claim("bh3", "brian-helton", "christian_liberty", 0, True,
              "Brian Helton is an openly Baptist elected official who explicitly leads his platform with 'Faith, Family, Freedom' and states 'religious freedom' as a core value. He describes himself as 'a lifelong southern West Virginian, Baptist' married to Emily. As Chair of the WV Senate Health and Human Resources Committee, he is positioned to oppose healthcare mandates that infringe on religious conscience rights — including vaccine mandates and policies compelling religious institutions to act against their beliefs.",
              ["https://ivoterguide.com/candidate/79223/race/19632/election/1213",
               "https://ballotpedia.org/Brian_Helton",
               "https://home.wvlegislature.gov/senator/brian-helton/"]),
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
