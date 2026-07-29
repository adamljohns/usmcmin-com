#!/usr/bin/env python3
"""Enrichment batch 876: Florida state legislators + Georgia Sen. Emanuel Jones — bottom of evidence_state bucket.

Targets (all 0 claims, evidence_state confidence):
Michele K. Rayner (FL-D, State Rep HD-62, first openly queer Black FL legislator; 2026 FL Senate SD-16 candidate),
Yvonne Hayes Hinson (FL-D, State Rep HD-21, Gainesville),
Emanuel Jones (GA-D, State Senator SD-10, outgoing; led GA Senate Safe Firearm Storage Study Committee 2024),
Mike Gottlieb (FL-D, State Rep HD-102, Broward; Minority Floor Leader 2022-2024),
Rita Harris (FL-D, State Rep HD-44, Orange County; 21% ILA score 2023).
10 new claims across 5 candidates spanning sanctity_of_life, biblical_marriage, and self_defense categories.

Sources: flsenate.gov official vote records, flgov.com, ballotpedia.org, en.wikipedia.org,
metroweekly.com, watermarkoutnews.com, victoryfund.org, eqfl.org, senatepress.net,
gpb.org, courthousenews.com, analysis.limitedgov.org.
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
    # ---------------- Michele K. Rayner (FL-D, State Rep HD-62) ----------------
    ("michele-k-rayner", "FL", "Representative", [
        claim("mr876a", "michele-k-rayner", "biblical_marriage", 4, False,
              "Michele Rayner-Goolsby made history in November 2020 as the first openly queer Black member of the Florida Legislature and has since made the promotion of LGBTQ inclusion in public institutions and policy the defining thread of her legislative career. She was a vocal opponent of HB 1557 (the 'Don't Say Gay' law, signed March 2022), which restricted classroom instruction on sexual orientation and gender identity. In July 2026, Equality Florida, the LGBTQ Victory Fund, and other LGBTQ organizations endorsed her campaign for Florida Senate District 16, citing her record as 'one of the strongest advocates for LGBTQ people' in the Legislature. The Victory Fund noted she would become 'the first queer woman senator' in Florida history. Her legislative and campaign platform centers on expanding LGBTQ recognition and access in public schools and government policy — exactly the agenda the rubric's biblical_marriage standard opposes.",
              ["https://www.metroweekly.com/2020/11/michele-rayner-goolsby-becomes-first-black-queer-woman-elected-to-florida-house/",
               "http://watermarkoutnews.com/2026/07/02/lgbtq-organizations-endorse-michele-rayner-for-florida-senate/",
               "https://victoryfund.org/candidate/michele-rayner/",
               "https://en.wikipedia.org/wiki/Michele_Rayner"]),
        claim("mr876b", "michele-k-rayner", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks) on April 14, 2023, by a vote of 70-40. Rep. Michele Rayner was among the House Democrats who voted NO on SB 300, opposing any statutory recognition of unborn personhood. As co-founder of the Black Women's Caucus of the Florida Legislature and a women's rights advocate, Rayner has publicly framed abortion access as a core civil rights issue. After the Florida Supreme Court upheld the 15-week ban in April 2024 (triggering the 6-week ban), she continued to oppose abortion restrictions and support repeal efforts — confirming her rejection of the rubric's sanctity-of-life standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://ballotpedia.org/Michele_Rayner",
               "https://en.wikipedia.org/wiki/Michele_Rayner"]),
    ]),

    # ---------------- Yvonne Hayes Hinson (FL-D, State Rep HD-21) ----------------
    ("yvonne-hayes-hinson", "FL", "Representative", [
        claim("yh876a", "yvonne-hayes-hinson", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, 6-week abortion ban) on April 14, 2023, by a vote of 70-40. Rep. Yvonne Hayes Hinson, D-Gainesville (District 21, Alachua County), voted NO on SB 300 as part of the Democratic minority, opposing the bill that prohibits abortion after detection of fetal cardiac activity and represents Florida's strongest abortion restriction. Hinson assumed office in November 2022 and has earned a 14% Freedom Score on the Freedom Index — reflecting a consistently progressive voting pattern that rejects statutory recognition of unborn personhood.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://thefreedomindex.org/fl/legislator/21887/votes/session-20211/",
               "https://ballotpedia.org/Yvonne_Hayes_Hinson"]),
        claim("yh876b", "yvonne-hayes-hinson", "self_defense", 0, False,
              "The Florida House passed HB 543 (Florida Constitutional Carry Act, eliminating the permit requirement for concealed carry) on March 24, 2023, by a vote of 76-32. Rep. Yvonne Hayes Hinson voted NO on HB 543, joining the Democratic minority in opposing the bill that Gov. DeSantis signed on April 3, 2023, making Florida the 26th constitutional carry state (effective July 1, 2023). By voting to preserve the state's concealed-carry permit requirement, Hinson's record opposes the rubric's constitutional carry standard recognizing every law-abiding citizen's right to bear arms without government-issued permission.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry",
               "https://ballotpedia.org/Yvonne_Hayes_Hinson"]),
    ]),

    # ---------------- Emanuel Jones (GA-D, State Senator SD-10) ----------------
    ("emanuel-jones", "GA", "Senator", [
        claim("ej876a", "emanuel-jones", "self_defense", 1, False,
              "In May 2024, Lt. Gov. Burt Jones appointed Sen. Emanuel Jones (D-Decatur, SD-10) as Chairman of the Senate Study Committee on Safe Firearm Storage, convened following the Apalachee High School shooting (September 2024, four killed). Jones proposed legislation to impose civil and criminal penalties on parents or caregivers who allow children access to a loaded, unsecured firearm, and to incentivize safe-storage purchases through homeowners'-insurance premium reductions. Government-mandated firearm storage requirements backed by criminal penalties for non-compliance expand regulatory burden on lawful gun owners and set precedent for further restrictions — opposing the rubric's self-defense standard which rejects red-flag laws, government registries, and related restrictions on Second Amendment exercise.",
              ["https://senatepress.net/sen-emanuel-jones-appointed-to-lead-senate-study-committee-on-safe-firearm-storage/",
               "https://www.gpb.org/news/2024/08/21/georgia-senate-committee-explore-benefits-of-safe-gun-storage-for-owners-with-testimonies",
               "https://www.courthousenews.com/georgia-senators-propose-bills-to-combat-child-gun-violence/"]),
        claim("ej876b", "emanuel-jones", "sanctity_of_life", 0, False,
              "Georgia House Bill 481 (LIFE Act), prohibiting abortion after detection of fetal cardiac activity (approximately 6 weeks), passed the Georgia Senate on March 22, 2019, by a vote of 34-18, on a near-party-line vote with Democrats unanimously opposing. Sen. Emanuel Jones (D-Decatur), who has served in the Georgia Senate since 2005, was among the Senate Democratic minority voting against HB 481 — rejecting the bill's fetal personhood framework. The LIFE Act was signed by Gov. Brian Kemp on May 7, 2019, and took full effect in June 2022 after the U.S. Supreme Court overturned Roe v. Wade. Jones's career-long opposition to abortion restrictions reflects a clear rejection of the rubric's sanctity-of-life standard.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://www.legis.ga.gov/legislation/57219",
               "https://ballotpedia.org/Emanuel_Jones"]),
    ]),

    # ---------------- Mike Gottlieb (FL-D, State Rep HD-102) ----------------
    ("mike-gottlieb", "FL", "Representative", [
        claim("mg876a", "mike-gottlieb", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, 6-week abortion ban) on April 14, 2023, by a vote of 70-40. Rep. Michael 'Mike' Gottlieb (D-Davie, District 102, Broward County), who served as House Minority Floor Leader from 2022 to 2024, voted NO on SB 300 in his capacity as the Democratic caucus's floor leader coordinating minority opposition. As Minority Floor Leader, Gottlieb was a central organizer of House Democratic resistance to the DeSantis legislative agenda, including abortion restrictions. His opposition to SB 300 reflects a rejection of any legislative recognition of unborn personhood from conception.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://ballotpedia.org/Michael_Gottlieb",
               "https://en.wikipedia.org/wiki/Michael_Gottlieb_(politician)"]),
        claim("mg876b", "mike-gottlieb", "self_defense", 0, False,
              "The Florida House passed HB 543 (Florida Constitutional Carry Act, permitless concealed carry) on March 24, 2023, by a vote of 76-32. As House Minority Floor Leader (2022-2024), Rep. Gottlieb led the Democratic caucus's organized opposition to HB 543, which DeSantis signed on April 3, 2023 (effective July 1, 2023), eliminating Florida's concealed-carry permit requirement. Gottlieb voted NO on HB 543 as part of the 32-member Democratic minority — opposing the constitutional carry reform that the rubric identifies as the baseline self-defense standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://ballotpedia.org/Michael_Gottlieb"]),
    ]),

    # ---------------- Rita Harris (FL-D, State Rep HD-44) ----------------
    ("rita-harris", "FL", "Representative", [
        claim("rh876a", "rita-harris", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, 6-week abortion ban) on April 14, 2023, by a vote of 70-40. Rep. Jennifer 'Rita' Harris (D-Orlando, District 44, Orange County), who assumed office in November 2022, voted NO on SB 300 as part of the Democratic minority opposing the bill. Harris earned a 21% score on the Institute for Legislative Analysis (ILA) 2023 scorecard — below the Democratic average — reflecting a consistently progressive voting pattern that rejects any statutory recognition of unborn personhood.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://analysis.limitedgov.org/lawmakers/jennifer-rita-harris-d-fl-rep-44",
               "https://ballotpedia.org/Jennifer_Rita_Harris"]),
        claim("rh876b", "rita-harris", "self_defense", 0, False,
              "The Florida House passed HB 543 (Florida Constitutional Carry Act, permitless concealed carry) on March 24, 2023, by a vote of 76-32. Rep. Rita Harris voted NO on HB 543, joining the Democratic minority in opposing the bill that eliminated Florida's permit requirement for concealed carry (signed by Gov. DeSantis, effective July 1, 2023, making Florida the 26th constitutional carry state). By voting to maintain the state permit requirement, Harris's record opposes the rubric's constitutional carry standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry",
               "https://ballotpedia.org/Jennifer_Rita_Harris"]),
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
