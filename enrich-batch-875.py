#!/usr/bin/env python3
"""Enrichment batch 875: Florida state legislators — bottom of remaining evidence_state bucket.

Targets: Lori Berman (FL-D, State Senator SD-26, Senate Minority Leader since Apr 2025),
Shevrin Jones (FL-D, State Senator SD-34, FL's first openly gay Black lawmaker),
Carlos Guillermo Smith (FL-D, State Senator SD-17, first openly LGBTQ Latino in FL Legislature),
Fentrice Driskell (FL-D, State Rep HD-67, FL House Minority Leader, EMILY's List Giffords Star),
Rosalind Osgood (FL-D, State Senator SD-32, seeking reelection 2026).
10 new claims across 5 candidates spanning sanctity_of_life, biblical_marriage,
and self_defense categories.

NOTE on Smith/Driskell legislative timeline:
  - Carlos Guillermo Smith was NOT in the FL legislature in 2023 (left House 2022,
    joined Senate Nov 2024). Claims drawn from 2022 House record and 2024-26 Senate.
  - Fentrice Driskell was in the FL House for all 2023 votes (SB 300, HB 543, SB 254).

Sources: Tampa Bay Times, Florida Politics, flsenate.gov, en.wikipedia.org,
loriberman.com, cbsnews.com/miami, eqfl.org, ballotpedia.org.
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
    # ---------------- Lori Berman (FL-D, State Senator SD-26, Senate Minority Leader) ----------------
    ("lori-berman", "FL", "Senator", [
        claim("lb875a", "lori-berman", "sanctity_of_life", 0, False,
              "During the Florida Senate's floor debate and committee vote on SB 300 (April 2023), Sen. Lori Berman, D-Boca Raton, characterized the legislation as 'a ban' on abortion, joining all 12 Senate Democrats in opposing Florida's Heartbeat Protection Act. SB 300 criminalizes abortion after 6 weeks of gestation (before most women know they are pregnant) and took effect May 1, 2024. As Senate Minority Leader since April 2025, Berman names protecting abortion access her top priority and has repeatedly characterized abortion restrictions as government overreach into private medical decisions — rejecting any recognition of personhood from conception.",
              ["https://www.tampabay.com/news/florida-politics/2023/04/03/abortion-ban-pregnant-senate-debate-protest/",
               "https://www.flsenate.gov/Session/Bill/2023/300/Vote/SenateVote_s00300e1018.PDF",
               "https://en.wikipedia.org/wiki/Lori_Berman"]),
        claim("lb875b", "lori-berman", "self_defense", 1, False,
              "Berman has filed legislation to allow family and household members to petition courts to have firearms removed from a dangerous person — a red-flag-law mechanism. Her campaign platform explicitly includes fighting for 'commonsense gun violence prevention measures,' including support for bills restricting firearms in certain areas. This directly opposes the rubric's rejection of red-flag laws, assault-weapons bans, magazine limits, and related firearm restrictions.",
              ["https://loriberman.com/meet-lori/",
               "https://cbsnews.com/miami/news/new-bill-seeks-to-ban-guns-in-some-areas"]),
    ]),

    # ---------------- Shevrin Jones (FL-D, State Senator SD-34) ----------------
    ("shevrin-jones", "FL", "Senator", [
        claim("sj875a", "shevrin-jones", "sanctity_of_life", 0, False,
              "During the Florida Senate Fiscal Policy Committee hearing on SB 300 (March 28, 2023), Sen. Shevrin Jones, D-Miami Gardens, stated: 'Whatever we do here today, abortions are still going to happen. Whether legally or illegally and dangerous, abortions will still happen.' He voted with all 12 Senate Democrats against SB 300 (the Heartbeat Protection Act, 6-week abortion ban) on final Senate passage. He later co-sponsored SB 1404 to repeal the ban and restore abortion access through the second trimester — directly rejecting personhood-from-conception.",
              ["https://www.tampabay.com/news/florida-politics/2023/03/28/ban-abortion-after-6-weeks-pregnancy-headed-full-florida-senate/",
               "https://www.flsenate.gov/Session/Bill/2023/300"]),
        claim("sj875b", "shevrin-jones", "biblical_marriage", 4, False,
              "Florida's first openly LGBTQ Black lawmaker (came out as gay in 2018 while serving in the FL House), Jones was 'the loudest voice raising concerns' against the 'Don't Say Gay' law (HB 1557, signed March 2022) and the Stop WOKE Act. He also voted against SB 254 (2023 gender-affirming care ban) in the FL Senate, moving a floor amendment to create a medical exception. The LGBTQ+ Victory Fund endorsed his 2026 congressional bid, citing his 'record of leadership delivering for LGBTQ people.' His career has been defined by the active promotion of LGBTQ visibility and policy in public institutions — the agenda the rubric opposes.",
              ["https://floridapolitics.com/archives/682194-shevrin-jones-knows-value-of-lgbtq-representation-within-the-florida-senate/",
               "https://floridapolitics.com/archives/805688-shev-has-never-backed-down-lgbtq-victory-fund-endorses-shevrin-jones-for-congress/",
               "https://en.wikipedia.org/wiki/Shevrin_Jones"]),
    ]),

    # ---------------- Carlos Guillermo Smith (FL-D, State Senator SD-17) ----------------
    # NOTE: Smith was NOT in the FL legislature in 2023 (left House 2022, joined Senate Nov 2024).
    ("carlos-guillermo-smith", "FL", "Senator", [
        claim("cgs875a", "carlos-guillermo-smith", "biblical_marriage", 4, False,
              "The first openly LGBTQ Latino elected to the Florida Legislature, Smith was among the most vocal opponents of HB 1557 (the 'Don't Say Gay' law, signed March 2022) while in the FL House. He co-authored public analysis with Rep. Anna Eskamani arguing HB 1557 'will endanger teens,' and when it was signed stated: 'By signing #DontSayGay into law, DeSantis is attempting to censor and exclude an entire community of people from our public schools for his own political gain.' Equality Florida credited him as one who 'showed up for us every step of the way.' Elected to the FL Senate in November 2024 — the second openly LGBTQ member of that chamber in Florida history — he chairs the Senate LGBTQ Caucus and continues to lead legislative efforts promoting LGBTQ identity in education and public policy, precisely the agenda the rubric opposes.",
              ["https://floridapolitics.com/archives/510993-carlos-guillermo-smith-anna-eskamani-say-hb-1557-will-endanger-teens/",
               "https://floridapolitics.com/archives/511972-gov-desantis-failed-the-people-of-florida-lawmakers-react-as-hb-1557-becomes-law/",
               "https://eqfl.org/2024/Carlos-Wins-SD17-Election"]),
        claim("cgs875b", "carlos-guillermo-smith", "self_defense", 1, False,
              "As a Florida state senator, Smith filed SB 346 (2025 and 2026 sessions) to ban assault weapons and large-capacity magazines statewide — continuing a pattern begun in the FL House where he co-introduced similar legislation. Filing an assault-weapons ban in the FL Senate directly opposes the rubric's rejection of assault-weapon restrictions, magazine-capacity limits, and new firearms registries.",
              ["https://www.flsenate.gov/Session/Bill/2026/346",
               "https://floridapolitics.com/archives/229821-linda-stewart-carlos-guillermo-smith-introduce-bill-to-ban-assault-weapons-florida/"]),
    ]),

    # ---------------- Fentrice Driskell (FL-D, State Rep HD-67, House Minority Leader) ----------------
    ("fentrice-driskell", "FL", "Representative", [
        claim("fd875a", "fentrice-driskell", "sanctity_of_life", 0, False,
              "As FL House Minority Leader, Driskell led House Democratic opposition to SB 300 (April 2023 6-week abortion ban), issuing a statement: 'This incredibly personal decision regarding heart and home should be between a woman and her doctor, family and faith. She does not need Tallahassee politicians invading her right to privacy and taking that right away.' She voted NO on SB 300, which passed the House 70-40. When the FL Supreme Court subsequently upheld the 15-week ban (April 2024), triggering the 6-week ban, Driskell called Florida 'the land of government interference,' charging that GOP leaders were 'deciding what's best for pregnant women and girls' — rejecting any recognition of unborn personhood.",
              ["https://floridapolitics.com/archives/603032-six-week-abortion-ban-house/",
               "https://en.wikipedia.org/wiki/Fentrice_Driskell",
               "https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF"]),
        claim("fd875b", "fentrice-driskell", "self_defense", 0, False,
              "Before the 2023 Florida House floor vote on HB 543 (Constitutional Carry / permitless concealed carry), Driskell held a press conference on February 21, 2023 with Democratic lawmakers and gun-safety advocates opposing the bill, stating it would 'make Florida less safe' and invoking Parkland: 'It seems to me that we're breaking our promise to the parents and the students of Parkland.' Named the 2023 Gabrielle Giffords Rising Star by EMILY's List for 'fighting for common sense gun reform,' Driskell voted NO on HB 543 (passed 76-32 in the House, 27-13 in the Senate). This opposition to permitless constitutional carry directly conflicts with the rubric's self-defense standard.",
              ["https://www.tampabay.com/news/florida-politics/2023/02/21/permitless-carry-gun-parkland-desantis-constitutional/",
               "https://floridapolitics.com/archives/602727-fentrice-driskell-named-emilys-list-2023-gabrielle-giffords-rising-star/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
    ]),

    # ---------------- Rosalind Osgood (FL-D, State Senator SD-32) ----------------
    ("rosalind-osgood", "FL", "Senator", [
        claim("ro875a", "rosalind-osgood", "sanctity_of_life", 0, False,
              "In April 2023, the Florida Senate passed SB 300 (the Heartbeat Protection Act 6-week abortion ban) on a nearly straight party-line vote, with all 12 Senate Democrats voting against — including Sen. Rosalind Osgood, who has served in the FL Senate since November 2022. Osgood was among 16 Democratic women endorsed by Ruth's List Florida specifically for supporting abortion rights, placing her squarely in opposition to any recognition of fetal personhood from conception and against the rubric's sanctity-of-life standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/SenateVote_s00300e1018.PDF",
               "https://ballotpedia.org/Rosalind_Osgood"]),
        claim("ro875b", "rosalind-osgood", "self_defense", 0, False,
              "In March 2023 the Florida Senate passed HB 543 (Florida's Constitutional Carry Act, eliminating the permit requirement for concealed carry) 27-13, with all 12 Senate Democrats voting against — including Sen. Osgood. Only Republican Sen. Ileana Garcia joined all 12 Democrats in opposition. By voting against HB 543 (signed by Gov. DeSantis, effective July 1, 2023), Osgood voted to maintain the permit requirement for concealed carry — opposing the rubric's constitutional carry standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision on same-name candidates."""
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

    # Minified write — preserve the no-whitespace master to keep under GitHub's 50MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
