#!/usr/bin/env python3
"""Enrichment batch 693: evidence_state Republicans with 0 claims (bottom-of-alphabet).

Primary archetype_curated federal buckets are fully exhausted; pivoting to
evidence_state Republican state executives and state legislators.

Targets (4): Mike Causey (NC-R, Commissioner of Insurance),
Luke Farley (NC-R, Commissioner of Labor), Billy Nungesser (LA-R, Lt. Governor),
April Rose (MD-R, State Delegate, HD-5).

Sources: NC DOI press releases, NC Values Coalition, NC Political News,
iVoterGuide (2023 Nungesser survey), Wikipedia, Baltimore Banner.
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
    # ---------------- Mike Causey (NC-R, Commissioner of Insurance) ----------------
    ("mike-causey", "NC", "Insurance", [
        claim("mc1", "mike-causey", "industry_capture", 0, True,
              "In February 2024 formally rejected the NC Rate Bureau's request for a 42.2% average homeowners insurance rate increase (some areas sought up to 99.4%), negotiating the final settlement to 7.5%/year for 2025-26, saving NC consumers an estimated $777 million. Also recovered a record $144 million for North Carolinians in 2024 through fraud enforcement and $130 million in 2023, with hundreds of fraud arrests annually — actively countering insurance-industry capture.",
              ["https://www.ncdoi.gov/news/press-releases/2024/02/06/insurance-commissioner-mike-causey-rejects-insurance-companies-average-422-rate-hike-request",
               "https://www.ncdoi.gov/news/press-releases/2025/01/10/commissioner-causey-announces-record-144-million-saved-or-recovered-north-carolinians-2024"]),
        claim("mc2", "mike-causey", "refuse_federal_overreach", 0, True,
              "His campaign platform explicitly opposes 'efforts to impose more government mandates and control over your healthcare insurance' and supports Association Health Plans — a market-based vehicle allowing small businesses to purchase coverage outside ACA-mandated requirements, reducing compulsory federal insurance mandates.",
              ["https://mikecauseync.com/",
               "https://ballotpedia.org/Mike_Causey"]),
        claim("mc3", "mike-causey", "economic_stewardship", 2, True,
              "Demonstrated fiscal discipline as Insurance Commissioner: rejected a massive rate-hike request saving consumers $777 million, returned $130 million to policyholders in 2023 and a record $144 million in 2024 through fraud enforcement, and in 2025 fined two insurers $113K and ordered $2.6 million in refunds — holding the line against predatory insurance costs.",
              ["https://www.ncdoi.gov/news/press-releases/2024/01/16/commissioner-causey-announces-record-130-million-saved-or-recovered-north-carolinians-2023",
               "https://hoodline.com/2025/05/nc-insurance-commissioner-fines-two-firms-113k-for-violations-orders-2-6m-refund-to-policyholders/"]),
    ]),

    # ---------------- Luke Farley (NC-R, Commissioner of Labor) ----------------
    ("luke-farley", "NC", "Labor", [
        claim("lf1", "luke-farley", "christian_liberty", 0, True,
              "Endorsed by the NC Values Coalition specifically because he 'believes in religious freedom in the workplace, and that proprietors should have the freedom to conduct their businesses based on conscience and religious beliefs.' Pledged to enforce NC's Retaliatory Employment Discrimination Act (REDA) on behalf of workers who faced employer retaliation for declining the COVID-19 vaccine on religious or personal grounds.",
              ["https://ncvalues.org/pr-nc-values-endorses-luke-farley-for-north-carolina-labor-commissioner/",
               "https://www.ncpoliticalnews.com/news/gop-labor-commissioner-candidate-luke-farley-opposes-proposed-new-covid-workplace-mandates"]),
        claim("lf2", "luke-farley", "refuse_federal_overreach", 0, True,
              "Publicly opposed proposed new COVID-19 workplace mandates from the previous NC DOL administration, stating 'The last time we had mandates and lockdowns, it was a disaster for our economy and students.' Defends NC's right-to-work law: 'North Carolina workers deserve the freedom to choose for themselves whether to join a union or pay union dues' — resisting federal union-organizing pressure.",
              ["https://www.ncpoliticalnews.com/news/gop-labor-commissioner-candidate-luke-farley-opposes-proposed-new-covid-workplace-mandates",
               "https://www.luke4labor.com/"]),
        claim("lf3", "luke-farley", "economic_stewardship", 2, True,
              "In his first year as Labor Commissioner (2025), recovered $2.5 million in unpaid wages for NC workers. In April 2026 submitted a formal comment letter to the U.S. DOL supporting higher prevailing wages in H-1B/H-1B1/E-3 visa programs, stating 'our workers are being hurt by foreign visa programs that depress wages.' Championed the Worker Safety Act of 2026 (H.B. 258), which passed NC House 108-5 and Senate 46-0.",
              ["https://www.labor.nc.gov/news/press-releases/2026/01/07/promises-made-promises-kept-labor-commissioner-luke-farley-delivers-results-and-sets-stage-whats",
               "https://www.labor.nc.gov/news/press-releases/2026/04/27/labor-commissioner-farley-issues-statement-support-proposed-federal-rule-protect-wages-american"]),
    ]),

    # ---------------- Billy Nungesser (LA-R, Lieutenant Governor) ----------------
    ("billy-nungesser", "LA", "Lieutenant", [
        claim("bn1", "billy-nungesser", "sanctity_of_life", 0, True,
              "In his 2023 re-election iVoterGuide survey, agreed with the statement: 'Human life begins at conception and deserves legal protection at every stage until natural death.' Also stated that abortion providers including Planned Parenthood should not receive funds from federal, state, or local governments, including Title X grants.",
              ["https://ivoterguide.com/candidate/46496/race/8169/election/1038",
               "https://ballotpedia.org/Billy_Nungesser"]),
        claim("bn2", "billy-nungesser", "christian_liberty", 0, True,
              "In his 2023 iVoterGuide survey stated: 'Judeo-Christian values established a framework of morality which is necessary for our system of limited government,' and affirmed that 'Religious liberty is at risk in the United States and deserves the highest level of protection in the law.'",
              ["https://ivoterguide.com/candidate/46496/race/8169/election/1038",
               "https://ballotpedia.org/Billy_Nungesser"]),
        claim("bn3", "billy-nungesser", "economic_stewardship", 2, True,
              "Self-described fiscal conservative who supports a balanced budget amendment to the U.S. Constitution. As Plaquemines Parish President, held the line on taxes and controlled spending, producing annual taxpayer savings and multi-million-dollar budget surpluses — applying the same small-government fiscal discipline the rubric calls for.",
              ["https://ivoterguide.com/candidate/46496/race/8169/election/664",
               "https://ballotpedia.org/Billy_Nungesser"]),
    ]),

    # ---------------- April Rose (MD-R, State Delegate HD-5) ----------------
    ("april-rose", "MD", "Delegate", [
        claim("ar1", "april-rose", "sanctity_of_life", 0, True,
              "Self-identifies as pro-life and called Maryland Gov. Wes Moore's 2023 bill codifying abortion access in the state constitution 'radical,' stating the legislation reflects a state that 'views abortion as the only possible response to an unplanned pregnancy.' In March 2022 introduced an amendment to reappropriate $3.5 million in Abortion Care Access Act clinical training funding away from abortion providers.",
              ["https://en.wikipedia.org/wiki/April_Rose_(politician)",
               "https://ballotpedia.org/April_Rose"]),
        claim("ar2", "april-rose", "self_defense", 1, True,
              "Supports the Second Amendment and publicly argues that gun control laws 'increase crime and make people less safe.' Advocates making Maryland a shall-issue concealed-carry state. In July 2022, following NYSRPA v. Bruen, co-signed a letter to Maryland's Attorney General seeking compliance with the Supreme Court's landmark carry ruling — opposing Maryland's restrictive licensing regime.",
              ["https://en.wikipedia.org/wiki/April_Rose_(politician)",
               "https://ballotpedia.org/April_Rose"]),
        claim("ar3", "april-rose", "family_child_sovereignty", 0, True,
              "In February 2025, during House debate on a bill mandating age-appropriate LGBTQ sex education in public schools, introduced an amendment to allow parents to opt their children out of those lessons — a direct defense of parental authority over children's education. The amendment was rejected 38-92 by the Democratic majority.",
              ["https://en.wikipedia.org/wiki/April_Rose_(politician)",
               "https://www.thebaltimorebanner.com/politics-power/state-government/maryland-health-sex-education-57GPZTBKXVGHBO6CEALGZXGSO4/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
