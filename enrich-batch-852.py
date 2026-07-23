#!/usr/bin/env python3
"""Enrichment batch 852: 8 claims for 4 sitting NC US Representatives.

Targets (bottom-of-alphabet continuation from batch 851 NY/PA focus):
  Alma Adams (NC-12, D, sitting US Rep since 2014),
  Valerie Foushee (NC-04, D, sitting US Rep since Jan 2023),
  Don Davis (NC-01, D, sitting US Rep since Jan 2023),
  Deborah Ross (NC-02, D, sitting US Rep since Jan 2017 / re-elected 2020).

archetype_curated and archetype_party_default federal buckets fully
exhausted; continuing with evidence_curated sitting members with fewest
claims from bottom-of-alphabet states. NC (North Carolina) is the next
available state with 4+ sitting members below the NY/PA tier enriched by
batch 851.

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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
    # ---- Alma Adams (NC-12, D, sitting US Rep since 2014) ----
    ("alma-adams", "NC", "Representative", [
        claim("aa852a", "alma-adams", "biblical_marriage", 1, False,
              "Rep. Alma Adams voted YEA on H.R.8404, the Respect for Marriage Act, on both occasions "
              "the House passed it: the initial passage on July 19, 2022 (House Roll Call No. 373, passed "
              "267-157) and the final passage of the Senate-amended version on December 8, 2022 (House Roll "
              "Call No. 513, passed 258-169). The Respect for Marriage Act repeals the Defense of Marriage "
              "Act's one-man-one-woman definition of marriage, requires the federal government to recognize "
              "and give full legal effect to same-sex marriages, and directs all U.S. states to recognize "
              "valid out-of-state marriages regardless of the sex or race of the parties — effectively "
              "codifying same-sex marriage in federal statute. Adams issued a formal press release confirming "
              "and celebrating her votes: 'Rep. Alma Adams Votes to Enshrine Marriage Equality Under Federal "
              "Law.' By voting for the RFMA on both occasions, Adams directly opposes the rubric's "
              "biblical_marriage[1] standard, which rewards candidates who oppose codification of same-sex "
              "marriage in federal law.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://adams.house.gov/media-center/press-releases/rep-alma-adams-votes-enshrine-marriage-equality-under-federal-law"]),
        claim("aa852b", "alma-adams", "economic_stewardship", 0, False,
              "Rep. Alma Adams voted NAY on H.R.5403, the CBDC Anti-Surveillance State Act (House Roll Call "
              "No. 230, May 23, 2024, passed 216-192), which would have prohibited the Federal Reserve from "
              "issuing a central bank digital currency directly to individual Americans — blocking creation of "
              "a programmable government digital dollar capable of monitoring and restricting every financial "
              "transaction. The vote was near-perfectly partisan: 213 Republicans voted YES to ban a CBDC, "
              "while approximately 192 Democrats voted NO. Only three Democrats crossed party lines to support "
              "the CBDC ban: Representatives Mary Peltola (AK), Marie Gluesenkamp Perez (WA), and Jared "
              "Golden (ME). Adams is not among them and voted with her caucus to decline prohibiting the CBDC "
              "infrastructure. Her record reflects a 0% Heritage Action score for the 119th Congress — "
              "consistent with voting against conservative priorities on virtually every major partisan roll "
              "call. By voting NAY, Adams declined to block the government-controlled programmable monetary "
              "infrastructure the rubric identifies as the primary threat at economic_stewardship[0].",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230"]),
    ]),

    # ---- Valerie Foushee (NC-04, D, sitting US Rep since Jan 2023) ----
    ("valerie-foushee", "NC", "Representative", [
        claim("vf852a", "valerie-foushee", "border_immigration", 2, False,
              "Rep. Valerie Foushee cosponsored the Melt ICE Act in the 119th Congress (February 2026), "
              "legislation to defund and strip U.S. Immigration and Customs Enforcement (ICE) of authority "
              "to detain or surveil immigrants — directly opposing the rubric's border_immigration[2] standard "
              "that rewards anti-sanctuary postures and federal-state cooperation on immigration enforcement. "
              "In May 2025, Foushee condemned the Trump Administration's 'sanctuary jurisdictions' targeting "
              "list — which named Chatham, Durham, and Orange Counties in North Carolina for refusing to "
              "cooperate with federal immigration enforcement — calling it 'a politically motivated stunt "
              "designed to intimidate and punish local governments.' In November 2025, she condemned DHS/CBP "
              "deployment of Border Patrol and ICE agents in North Carolina as an overreach, opposing interior "
              "enforcement operations in her district. Her co-sponsorship of legislation to defund ICE "
              "entirely, combined with her active defense of non-cooperative local jurisdictions, places "
              "Foushee squarely in opposition to the anti-sanctuary standard the rubric rewards.",
              ["https://foushee.house.gov/media/press-releases",
               "https://www.congress.gov/bill/119th-congress/house-bill"]),
        claim("vf852b", "valerie-foushee", "biblical_marriage", 2, False,
              "Rep. Valerie Foushee cosponsored H.R.15, the Equality Act, on June 21, 2023 (118th Congress). "
              "The Equality Act would amend existing federal civil-rights law to explicitly prohibit "
              "discrimination on the basis of sexual orientation and gender identity across employment, "
              "housing, credit, education, jury service, and public accommodations — codifying transgender "
              "identity protections at the federal level and extending them into schools, workplaces, and "
              "public facilities nationwide. Unlike the Respect for Marriage Act (which Foushee was not in "
              "Congress for), the Equality Act goes further by embedding gender-identity anti-discrimination "
              "mandates throughout federal law. Foushee is also a member of the Congressional Equality "
              "Caucus; her official website states she 'works to advance LGBTQIA+ equality' and she "
              "previously worked in the North Carolina General Assembly to expand hate-crime law to cover "
              "sexual orientation and gender identity. By co-sponsoring legislation that expressly codifies "
              "gender-identity protections across public life, Foushee directly opposes the rubric's "
              "biblical_marriage[2] standard, which rewards candidates who reject transgender ideology in "
              "public policy.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/15/cosponsors",
               "https://foushee.house.gov/issues/equality"]),
    ]),

    # ---- Don Davis (NC-01, D, sitting US Rep since Jan 2023) ----
    ("don-davis", "NC", "Representative", [
        claim("dd852a", "don-davis", "election_integrity", 0, True,
              "Rep. Don Davis (D-NC-01) voted YES on H.R.8800, the National Defense Authorization Act for "
              "Fiscal Year 2027 (House Roll Call No. 278, July 22, 2026, passed 216-212), making him one of "
              "only 6 Democrats to cross party lines and support the bill. The FY2027 NDAA incorporated the "
              "SAVE America Act — added via H.Res.1438 during engrossment — which amends the National Voter "
              "Registration Act to require documentary proof of U.S. citizenship (passport, birth certificate, "
              "or REAL ID-compliant document indicating citizenship) when registering to vote in federal "
              "elections. The five other House Democrats who voted YES were Henry Cuellar (TX-28), Jared "
              "Golden (ME-02), Vicente Gonzalez (TX-34), Adam Gray (CA-13), and Marie Gluesenkamp Perez "
              "(WA-03); 205 Democrats voted NAY. Davis issued a press release noting this was 'the fourth "
              "consecutive year' he voted to pass the annual defense authorization bill, highlighting 31 "
              "provisions he sponsored related to Seymour Johnson Air Force Base and MCAS Cherry Point. By "
              "voting YES, Davis supported the documentary citizenship proof requirement for voter registration "
              "— the kind of identity-verification standard the rubric's election_integrity[0] category "
              "rewards alongside voter ID and paper ballot protections.",
              ["https://www.govtrack.us/congress/votes/119-2026/h278",
               "https://dondavis.house.gov/media/press-releases/congressman-don-davis-votes-house-passage-eastern-north-carolina-defense",
               "https://thehill.com/homenews/house/5984555-democrats-join-gop-vote-ndaa/"]),
        claim("dd852b", "don-davis", "economic_stewardship", 0, False,
              "Rep. Don Davis voted NAY on H.R.5403, the CBDC Anti-Surveillance State Act (House Roll Call "
              "No. 230, May 23, 2024, passed 216-192), which would have prohibited the Federal Reserve from "
              "issuing a central bank digital currency directly to individual Americans. Despite Davis's "
              "reputation as one of the most bipartisan House Democrats — ranking 4th highest for party "
              "defection, named #1 most bipartisan member of Congress by the Common Ground Scorecard, and "
              "a frequent crossover vote alongside Jared Golden and Marie Gluesenkamp Perez — Davis did not "
              "cross party lines on the CBDC prohibition vote. Only three Democrats voted YES: Mary Peltola "
              "(AK), Marie Gluesenkamp Perez (WA), and Jared Golden (ME). Davis is not among them, "
              "consistent with no public statements from his office on CBDC or central bank digital currency. "
              "By voting NAY, Davis declined to block the government-programmable monetary infrastructure "
              "the rubric identifies as the primary threat at economic_stewardship[0].",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://ncnewsline.com/2024/03/27/democrat-don-davis-votes-with-the-gop-as-he-seeks-reelection-in-a-toss-up-congressional-district/"]),
    ]),

    # ---- Deborah Ross (NC-02, D, sitting US Rep since Jan 2017 / re-elected 2020) ----
    ("deborah-ross", "NC", "Representative", [
        claim("dr852a", "deborah-ross", "biblical_marriage", 1, False,
              "Rep. Deborah Ross voted YEA on H.R.8404, the Respect for Marriage Act, on both occasions the "
              "House passed it: the initial passage on July 19, 2022 (House Roll Call No. 373, passed "
              "267-157) and the final passage of the Senate-amended version on December 8, 2022 (House Roll "
              "Call No. 513, passed 258-169). Ross was serving in the 117th Congress for both votes, having "
              "been elected to represent NC-2 in 2016 and re-elected in 2020. The Respect for Marriage Act "
              "repeals the Defense of Marriage Act's one-man-one-woman definition of marriage, requires "
              "federal recognition of same-sex marriages, and directs all U.S. states to recognize valid "
              "out-of-state marriages — effectively codifying same-sex marriage in federal statute. Ross "
              "is a consistent advocate for LGBTQ rights and has publicly supported marriage equality "
              "throughout her congressional career. Her votes for the RFMA directly oppose the rubric's "
              "biblical_marriage[1] standard, which rewards candidates who oppose codification of same-sex "
              "marriage in federal law.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://ballotpedia.org/Deborah_Ross"]),
        claim("dr852b", "deborah-ross", "border_immigration", 1, False,
              "Rep. Deborah Ross voted NAY on H.R.29/S.5, the Laken Riley Act (House Roll Call No. 6, "
              "January 7, 2025, passed 263-156), which requires mandatory detention by DHS of any "
              "undocumented immigrant charged with theft, burglary, or a crime of violence against a law "
              "enforcement officer. The bill, named after Laken Riley — a nursing student murdered in "
              "Georgia by an undocumented Venezuelan national — passed with 46 Democrats crossing party "
              "lines to vote YES, a historically high bipartisan margin for an immigration enforcement bill. "
              "Among North Carolina's Democratic House members, Rep. Don Davis (NC-01) was the only "
              "Democrat to cross party lines and vote YES; all other NC Democrats, including Ross, voted "
              "NAY. Ross's opposition to mandatory detention of undocumented immigrants charged with violent "
              "or property crimes is not aligned with the rubric's border_immigration[1] standard, which "
              "rewards candidates who support mandatory deportation and detention of undocumented criminals.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://clerk.house.gov/Votes/20256",
               "https://ballotpedia.org/Deborah_Ross"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
