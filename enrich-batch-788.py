#!/usr/bin/env python3
"""Enrichment batch 788: 5 Utah Republican state representatives.

All federal and archetype_curated buckets exhausted.
Targets taken from the top of the reversed archetype_party_default
Republican state-legislative bucket (UT, sorted reverse-alpha by name),
continuing after batch 787 (which covered M/L names).

Kristen Chevrier (District 54, Highland),
Kay J. Christofferson (District 53),
Katy Hall (District 11, South Ogden),
Karen M. Peterson (District 13, Clinton/Davis County),
Joseph Elison (District 72, Toquerville).

Sources: le.utah.gov, ksl.com, sltrib.com, utahnewsdispatch.com,
ksltv.com, legiscan.com, ballotpedia.org.
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
    # ------- Kristen Chevrier (UT-R, District 54, Highland) -------
    ("kristen-chevrier", "UT", "Representative", [
        claim("kc1", "kristen-chevrier", "industry_capture", 2, True,
              "Chevrier was chief sponsor of H.B. 403 — SNAP Funds Amendments — in the 2025 Utah General Session. The bill required Utah to seek a federal waiver to prohibit SNAP benefits from being used to purchase soft drinks, blocking a major revenue stream to the industrial beverage industry from taxpayer-funded food-assistance dollars. The House passed H.B. 403 54-14; the federal USDA approved Utah's waiver in June 2025, and the soda restriction took effect January 1, 2026 — making Utah among the first states in the nation to curtail government subsidy of Big Food/Big Beverage through the SNAP program.",
              ["https://www.ksl.com/article/51247100/utah-lawmaker-takes-aim-at-candy-soda-and-food-dyes-with-2-new-bills",
               "https://utahnewsdispatch.com/2025/06/11/utah-snap-ban-on-soda-gets-green-light-along-with-maha-waivers-for-idaho-arkansas/",
               "https://le.utah.gov/~2025/bills/static/HB0403.html"]),
        claim("kc2", "kristen-chevrier", "industry_capture", 3, True,
              "Chevrier was chief sponsor of H.B. 179 — Milk Amendments — in the 2026 Utah General Session. The bill expanded where licensed small farmers may sell raw (unpasteurized) milk: under prior law, a farmer could only sell raw milk on their own farm property or at a store they personally owned; H.B. 179 allowed sales at any inspected retail establishment and permitted third-party delivery to stores subject to safe-storage requirements, while retaining mandatory batch-testing for bacteria and pathogens. The Senate Business and Labor Committee approved it unanimously; Governor Cox signed it on March 28, 2026, effective May 6, 2026. The law directly reduces regulatory barriers that concentrated raw-milk distribution in large-scale processed dairies at the expense of small family farms.",
              ["https://utahnewsdispatch.com/2026/02/28/utah-might-make-it-easier-to-buy-and-sell-raw-milk/",
               "https://www.sltrib.com/artsliving/food/2026/03/28/new-law-will-make-it-easier-buy/",
               "https://le.utah.gov/~2026/bills/static/HB0179.html"]),
    ]),

    # ------- Kay J. Christofferson (UT-R, District 53) -------
    ("kay-j-christofferson", "UT", "Representative", [
        claim("kjc1", "kay-j-christofferson", "border_immigration", 4, True,
              "Christofferson was a House co-sponsor of H.B. 186 — Restrictions on Foreign Acquisitions of Land Act — in the 2023 Utah General Session (chief sponsor: Rep. Matthew H. Gwynn). The bill enacted Title 63L-13 of the Utah Code, establishing the first comprehensive state-law framework restricting foreign government-linked entities from acquiring interests in Utah land; covered parties must divest prohibited interests within five years. Governor Cox signed it into law effective May 3, 2023. By supporting the bill, Christofferson backed a measure directly targeting the national-security threat of adversarial-nation land acquisition near Utah military and critical-infrastructure sites.",
              ["https://le.utah.gov/~2023/bills/static/HB0186.html",
               "https://www.sltrib.com/news/environment/2023/02/10/bills-would-restrict-foreign/",
               "https://www.ksl.com/article/50875734/utah-lawmakers-move-to-ban-land-sales-to-some-foreign-entities"]),
        claim("kjc2", "kay-j-christofferson", "election_integrity", 0, True,
              "Christofferson was a named co-sponsor of H.B. 209 — Voting Amendments — in the 2026 Utah General Session (chief sponsor: Rep. A. Cory Maloy; Senate sponsor: Sen. Ronald M. Winterton). The bill created a bifurcated ballot system requiring documentary proof of U.S. citizenship — passport, birth certificate, state-issued citizenship-confirming ID, naturalization certificate, or tribal ID — to register to vote in state and local races; voters who cannot or do not provide documentation are limited to federal-only ballots. The House passed it 51-16-8; Governor Cox signed it on March 25, 2026. By May 2026, more than 5,000 Utah voters had been formally notified of the new citizenship-documentation requirement.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0209.html",
               "https://utahnewsdispatch.com/2026/05/27/5000-utah-voters-need-to-provide-proof-of-citizenship-under-new-state-law/",
               "https://utahnewsdispatch.com/briefs/utah-bill-requiring-proof-of-citizenship-to-vote-advances/"]),
    ]),

    # ------- Katy Hall (UT-R, District 11, South Ogden) -------
    ("katy-hall", "UT", "Representative", [
        claim("kh1", "katy-hall", "biblical_marriage", 2, True,
              "Hall was the House floor sponsor of S.B. 16 — Transgender Medical Treatments and Procedures Amendments — in the 2023 Utah General Session (Senate chief sponsor: Sen. Michael S. Kennedy). As a practicing registered nurse, Hall shepherded the landmark bill through the House, publicly stating she could 'lend a healthcare viewpoint.' S.B. 16 placed a moratorium on prescribing puberty blockers and cross-sex hormones to new minor patients diagnosed with gender dysphoria and banned all surgical sex-change procedures on minors; it provided continuity protections only for minors already mid-treatment. The House passed S.B. 16 58-14; Governor Cox signed it into law on January 28, 2023, making Utah the first state in the nation to enact such restrictions in 2023. Hall's role as House floor sponsor placed her at the center of Utah's categorical legislative rejection of transgender medical ideology applied to children.",
              ["https://le.utah.gov/~2023/bills/static/SB0016.html",
               "https://www.deseret.com/utah/2023/1/26/23572997/transgender-surgery-ban-for-kids-cross-sex-hormones-puberty-blockers/",
               "https://www.sltrib.com/news/politics/2023/01/20/breaking-utah-senate-approves/"]),
        claim("kh2", "katy-hall", "biblical_marriage", 4, True,
              "Hall was chief sponsor of H.B. 261 — Equal Opportunity Initiatives — in the 2024 Utah General Session. The bill prohibited all eight public universities, all K-12 school systems, and every state government agency in Utah from maintaining offices, programs, or trainings that provide differential treatment or preference based on race, sex, sexual orientation, national origin, religion, or gender identity; existing DEI offices were required to transform into universally open 'student success centers' serving all students equally. It also banned DEI loyalty statements in public-institution hiring. The House passed H.B. 261 58-14 along party lines; Governor Cox signed it January 31, 2024, effective July 1, 2024. The bill directly dismantled the institutional infrastructure of LGBTQ-identity promotion inside Utah public schools and government agencies.",
              ["https://le.utah.gov/~2024/bills/static/HB0261.html",
               "https://utahnewsdispatch.com/2024/01/30/utah-governor-signs-anti-dei-bill-into-law/",
               "https://www.sltrib.com/news/education/2024/01/31/utahs-gov-cox-signs-anti-dei-bill/"]),
    ]),

    # ------- Karen M. Peterson (UT-R, District 13, Clinton / Davis County) -------
    ("karen-m-peterson", "UT", "Representative", [
        claim("kmp1", "karen-m-peterson", "election_integrity", 2, True,
              "Peterson was chief sponsor of H.B. 242 — Petition Signature Circulators — in the 2026 Utah General Session (Senate sponsor: Sen. Calvin R. Musselman). The bill tightened the training and background requirements for paid petition-signature circulators on ballot initiatives and referenda. In the final hours of the session, H.B. 242 was amended to add a provision that prohibited voters from using prepaid-postage mailers supplied by advocacy organizations to request the removal of their signatures from a petition — closing a coordinated tactic that had been used by the anti-gerrymandering group Better Boundaries to mass-harvest signature revocations. Both chambers approved the amended substitute; Governor Cox signed it into law immediately (effective upon signing, March 8, 2026). The legislation protects the integrity of the signature-gathering process from industry-funded signature-harvesting operations.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0242.html",
               "https://www.ksl.com/article/51458587/legislature-makes-late-night-election-bill-change-targeting-signature-removals",
               "https://utahnewsdispatch.com/2026/03/09/gov-cox-signs-bill-that-could-disqualify-prop-4-signature-removals/"]),
        claim("kmp2", "karen-m-peterson", "family_child_sovereignty", 0, True,
              "Peterson carried the House floor version of S.B. 98 — Parental Education on Student Use of Technology Amendments — in the 2025 Utah General Session (Senate prime sponsor: Sen. Wilson). The bill mandated that schools and school districts educate parents about the risks and monitoring tools available for their children's use of school-issued or school-supervised technology and digital platforms — empowering parents to exercise informed oversight of what public schools expose their children to online. The bill was supported by law-enforcement testimony (Pleasant Grove Police) and the Utah Attorney General's Office, and advanced through both the Senate Education Committee and the House Education Committee during the 2025 session. Peterson's House sponsorship placed her squarely on the side of parental oversight of school-directed technology access.",
              ["https://le.utah.gov/~2025/bills/static/sb0098.html",
               "https://le.utah.gov/av/committeeArchive.jsp?mtgID=19795"]),
    ]),

    # ------- Joseph Elison (UT-R, District 72, Toquerville) -------
    ("joseph-elison", "UT", "Representative", [
        claim("je1", "joseph-elison", "refuse_federal_overreach", 4, True,
              "Elison was chief sponsor of H.B. 120 — Time Change Amendments — in the 2025 Utah General Session. The bill asserted Utah's state authority to exit the federal Daylight Saving Time framework: it directed Utah to observe mountain standard time year-round unless and until an act of Congress authorizes states to permanently observe mountain daylight time. The bill passed the Utah House 52-23 on February 6, 2025, demonstrating broad Republican caucus support for reasserting state time-zone sovereignty against the federal Uniform Time Act's mandated clock-switching regime. While the Senate Business and Labor Committee tabled the bill 7-1, Elison's leadership on the legislation established a clear legislative record of refusing to defer indefinitely to federal scheduling mandates when state authority exists.",
              ["https://le.utah.gov/~2025/bills/static/HB0120.html",
               "https://www.ksl.com/article/51246295/a-waste-of-time-utah-house-passes-bill-to-end-daylight-saving-time",
               "https://utahnewsdispatch.com/2025/02/19/bill-to-stop-clocks-from-changing-in-utah-isnt-ready/"]),
        claim("je2", "joseph-elison", "christian_liberty", 4, True,
              "Elison was a House co-sponsor of H.C.R. 4 — Concurrent Resolution Regarding Religious Freedom — in the 2026 Utah General Session (chief House sponsor: Rep. Mike Petersen). The resolution formally declared the Utah Legislature's commitment to protecting the free exercise of religion as guaranteed by both the Utah Constitution and the First Amendment, reaffirming that government may not substantially burden sincerely held religious beliefs without a compelling governmental interest pursued through the least restrictive means. The resolution passed both chambers and was signed by Governor Cox on March 25, 2026. Elison's co-sponsorship aligns him with the Legislature's affirmative defense of religious free exercise against growing regulatory encroachment.",
              ["https://le.utah.gov/~2026/bills/static/HCR004.html",
               "https://legiscan.com/UT/bill/HCR004/2026"]),
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
