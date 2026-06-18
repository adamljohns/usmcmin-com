#!/usr/bin/env python3
"""Enrichment batch 279: hand-curated claims for 5 state officials (WV/VA).

archetype_curated federal bucket exhausted; evidence_state bucket continues
bottom-of-alphabet. Targets drawn from WV then VA (reverse state-alpha):
  Mark Hunt (WV State Auditor-R), Larry Pack (WV State Treasurer-R),
  Kent Leonhardt (WV Commissioner of Agriculture-R),
  Travis Hackworth (VA State Senate D5-R),
  Tammy Brankley Mulchi (VA State Senate D9-R).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # -------------- Mark Hunt (WV-R, State Auditor) --------------
    ("mark-hunt", "WV", "Auditor", [
        claim("mh1", "mark-hunt", "economic_stewardship", 2, True,
              "Upon taking office in January 2025, Hunt announced an 'aggressive agenda to keep an eye on the budget, transparency and accountability for every tax dollar that is spent' — a zero-tolerance posture toward waste and deficit spending from the Auditor's constitutional oversight seat.",
              ["https://www.wvsao.gov/about",
               "https://therealwv.com/2025/01/16/state-auditor-mark-hunt-announces-leadership-team/"]),
        claim("mh2", "mark-hunt", "public_justice", 0, True,
              "Hunt's State Auditor's Public Integrity and Fraud Unit investigation led directly to an embezzlement conviction in December 2025 — using the Auditor's constitutional authority to hold government actors criminally accountable for misappropriating taxpayer funds.",
              ["https://therealwv.com/2025/12/19/auditors-public-integrity-and-fraud-unit-investigation-leads-to-embezzlement-conviction/",
               "https://www.wvsao.gov/about"]),
    ]),

    # -------------- Larry Pack (WV-R, State Treasurer) --------------
    ("larry-pack", "WV", "Treasurer", [
        claim("lp1", "larry-pack", "economic_stewardship", 4, True,
              "Campaigned explicitly on defeating 'liberal ESG investment strategies' that cause the state to 'lose money, reduce pensions, and hurt the job market and economy,' pledging to prevent Wall Street from using West Virginia's pension dollars to advance political agendas over working families — a direct posture against WEF/ESG influence on public finance.",
              ["https://ballotpedia.org/Larry_Pack_(West_Virginia)",
               "https://larrypackforwv.com/"]),
        claim("lp2", "larry-pack", "refuse_federal_overreach", 0, True,
              "Continues the West Virginia Treasurer's office policy — initiated under predecessor Riley Moore — of flagging and restricting financial institutions that comply with federal ESG mandates hostile to West Virginia's coal, gas, and manufacturing economy, asserting the state's sovereign right to choose investment partners free from politically driven federal pressure.",
              ["https://www.pionline.com/esg/west-virginia-warns-6-financial-institutions-not-boycott-fossil-fuel-companies/",
               "https://ballotpedia.org/Larry_Pack_(West_Virginia)"]),
    ]),

    # -------------- Kent Leonhardt (WV-R, Commissioner of Agriculture) --------------
    ("kent-leonhardt", "WV", "Agriculture", [
        claim("kl1", "kent-leonhardt", "industry_capture", 3, True,
              "Implemented the West Virginia Exempt Dairy Farm and Milk Products Rule, creating a regulatory pathway for small dairy farmers to process and sell their own milk and dairy products locally — reducing regulatory capture by large commercial agriculture interests and expanding food-sovereignty options for small family farms.",
              ["https://agriculture.wv.gov/divisions/regulatory-and-environmental-affairs/west-virginia-exempt-dairy-farm-and-milk-products-rule/",
               "https://ballotpedia.org/Kent_Leonhardt"]),
        claim("kl2", "kent-leonhardt", "sanctity_of_life", 0, True,
              "Earned an endorsement from West Virginians for Life — the state's leading pro-life organization — in his successful 2024 re-election campaign, a vetting and endorsement not granted to candidates who reject life-from-conception principles.",
              ["https://ballotpedia.org/West_Virginia_Agriculture_Commissioner_election,_2024",
               "https://www.kentforwv.com/accomplishments"]),
    ]),

    # -------------- Travis Hackworth (VA-R, State Senate District 5) --------------
    ("travis-hackworth", "VA", "Senate", [
        claim("th1", "travis-hackworth", "sanctity_of_life", 0, True,
              "Introduced SB1284 in the Virginia Senate (2023 session), a near-total abortion prohibition explicitly providing that 'life begins at conception' and making an unlawful abortion a Class 4 felony — a personhood-level bill, not a gestational-limit restriction.",
              ["https://lis.virginia.gov/cgi-bin/legp604.exe?231+sum+SB1284",
               "https://www.richmondsunlight.com/legislator/tthackworth/"]),
        claim("th2", "travis-hackworth", "self_defense", 1, True,
              "Campaign platform explicitly commits to standing firm on 'guns,' representing rural Appalachian districts (Bland, Giles, Pulaski, Smyth, Tazewell, Wythe, Radford, Montgomery) where Second Amendment rights are foundational — opposing anti-gun legislation advanced by Virginia's Democratic majority.",
              ["https://ballotpedia.org/Travis_Hackworth",
               "https://justfacts.votesmart.org/candidate/key-votes/195752/travis-hackworth"]),
        claim("th3", "travis-hackworth", "christian_liberty", 0, True,
              "Campaign platform explicitly commits to standing firm on 'religious liberty,' positioning Hackworth as a defender of Christians' right to live and operate according to their convictions against government compulsion — the free exercise of religion the rubric prioritizes.",
              ["https://ballotpedia.org/Travis_Hackworth",
               "https://www.richmondsunlight.com/legislator/tthackworth/"]),
    ]),

    # -------------- Tammy Brankley Mulchi (VA-R, State Senate District 9) --------------
    ("tammy-brankley-mulchi", "VA", "Senate", [
        claim("tbm1", "tammy-brankley-mulchi", "sanctity_of_life", 0, True,
              "Voted against HJR1/SJ1, the Virginia constitutional amendment to enshrine unrestricted abortion access through the third trimester in the state constitution — joining the unanimous Republican caucus in opposing the measure, which passed 21-18 along strict party lines in January 2026.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("tbm2", "tammy-brankley-mulchi", "biblical_marriage", 1, True,
              "Voted against the Virginia constitutional amendment to enshrine same-sex marriage in the state constitution (January 2026 session), joining the Republican caucus in opposing the Democratic majority's effort to redefine marriage in Virginia's founding law.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Tammy_Mulchi"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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
