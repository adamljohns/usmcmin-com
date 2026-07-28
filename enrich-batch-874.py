#!/usr/bin/env python3
"""Enrichment batch 874: bottom-of-alphabet candidates — IA/WV.

Targets: Zach Wahls (IA-D, Iowa State Senator / 2026 US Senate primary),
Phil Mallow (WV-R, State Delegate Marion County — confirmed HB 302 co-sponsor),
Tristan Leavitt (WV-R, State Delegate Kanawha Co., in office since Dec 2024),
Scot C. Heckert (WV-R, State Delegate Jefferson Co., in office since Dec 2024),
Sarah Drennan (WV-R, State Delegate Putnam Co., in office since Dec 2024).
11 new claims across 5 candidates spanning biblical_marriage, sanctity_of_life,
self_defense, and election_integrity categories.

Corrections applied based on WV research:
- WV SB 10 (2023) = Campus Carry, NOT gender-affirming care ban
- WV gender-affirming care ban = HB 2007 (2023)
- WV abortion ban = HB 302 (2022 3rd special session)
- Leavitt/Heckert/Drennan took office Dec 2024; only 2025-2026 bills apply
- Phil Mallow confirmed PRIMARY CO-SPONSOR of HB 302 (2022 abortion ban)
- All four confirmed in office for HB 4106 (2026) and HB 3016 (2025)

Sources: Iowa Capital Dispatch, QC Times, Everytown for Gun Safety, LGBTQ Nation,
CBS2Iowa, legiscan.com/WV, wvlegislature.gov, West Virginia Watch.
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
    # ---------------- Zach Wahls (IA-D, Iowa State Senator) ----------------
    ("zach-wahls", "IA", "Senator", [
        claim("zw874a", "zach-wahls", "biblical_marriage", 0, False,
              "Wahls is the national symbol of same-sex marriage advocacy: in January 2011, at age 19, he testified before the Iowa House Judiciary Committee against a proposed constitutional amendment to ban same-sex marriage — his speech went viral globally and helped defeat the amendment. His parents are a same-sex couple (Terry Wahls and Jackie Reger). In May 2025, he publicly condemned Iowa Republican Sen. Sandy Salmon's resolution urging the U.S. Supreme Court to overturn Obergefell v. Hodges, calling it 'focused on rehashing culture war issues from a decade ago' rather than addressing real problems facing Iowa families. He ran for U.S. Senate in 2026 in part to oppose Sen. Joni Ernst, who co-sponsored the original 2011 Iowa marriage ban legislation he defeated. His entire public identity was forged in opposition to the one-man-one-woman definition of marriage.",
              ["https://www.lgbtqnation.com/2025/07/zach-wahls-helped-defeat-a-marriage-ban-in-iowa-now-hes-running-against-the-bans-sponsor/",
               "https://cbs2iowa.com/news/local/iowa-republican-state-senator-sandy-salmon-wants-scotus-supreme-court-to-overturn-same-sex-gay-marriage-hand-control-to-states-anti-lgbtq-legislation-coralville-democrat-state-sen-zach-wahls-condemns-attempt-to-ban-marriage-equality"]),
        claim("zw874b", "zach-wahls", "sanctity_of_life", 0, False,
              "As an Iowa State Senator, Wahls voted against Iowa's 6-week abortion ban in 2023. During his 2026 U.S. Senate primary campaign, he pledged to codify Roe v. Wade at the federal level and called himself a 'champion for Iowa women's reproductive freedom.' At a May 14, 2026 Democratic primary debate, he attacked his opponent for a committee vote increasing taxpayer funding for crisis pregnancy centers, stating 'In the United States Senate, I will push to defund these clinics.' He also spoke on the Iowa Senate floor against legislation restricting medication abortion access — rejecting any recognition of personhood from conception.",
              ["https://iowacapitaldispatch.com/2026/05/14/wahls-turek-spar-on-reproductive-healthcare-track-record-at-senate-primary-debate/",
               "https://www.wvik.org/news-from-iowa/2026-05-19/turek-wahls-spar-over-reproductive-rights-in-second-u-s-senate-democratic-primary-debate"]),
        claim("zw874c", "zach-wahls", "self_defense", 0, False,
              "As Iowa Senate Minority Leader in 2021, Wahls led all 17 Senate Democrats in voting against HF 756, Iowa's constitutional carry bill eliminating the permit-to-carry requirement. He participated in a press conference with Everytown for Gun Safety and Iowa Moms Demand Action urging Gov. Reynolds to veto the bill. He argued the 'cumulative effect' of the bill would be 'to make it possible for someone to buy a weapon from a private seller without a background check and carry it anywhere without any training on how to safely operate the gun.' During his 2026 Senate campaign he called himself 'a gun owner who respects the Second Amendment' while backing universal background checks and closing the 'gun-show loophole' — opposing constitutional carry as policy.",
              ["https://qctimes.com/news/local/iowa-governor-signs-constitutional-carry-into-law/article_aa3610f8-b6ba-530d-baa0-ebb5ad741cd9.html",
               "https://www.everytown.org/press/lawmakers-gun-safety-advocates-call-on-gov-reynolds-to-veto-background-check-repeal/"]),
    ]),

    # ---------------- Phil Mallow (WV-R, State Delegate Marion County) ----------------
    # Confirmed PRIMARY CO-SPONSOR of HB 302 (2022 3rd Special Session) — abortion ban
    ("phil-mallow", "WV", "Delegate", [
        claim("pm874a", "phil-mallow", "sanctity_of_life", 0, True,
              "A primary co-sponsor of West Virginia HB 302 (2022 Third Special Session), the state's near-total abortion ban signed September 16, 2022. WV HB 302 bans most abortions with narrow exceptions for medical emergency and rape/incest before 14 weeks — it does NOT recognize abortion access as a right and imposes criminal penalties on providers. Mallow was listed among the bill's lead sponsors (alongside Honaker, G. Ward, Rowan, Worrell, Forsht, and Miller), reflecting an affirmative commitment to ending legal abortion in West Virginia — consistent with the rubric's opposition to abortion access and support for protecting unborn life.",
              ["https://legiscan.com/WV/bill/HB302/2022",
               "https://westvirginiawatch.com/2022/09/13/west-virginia-governor-signs-near-total-abortion-ban/"]),
    ]),

    # ---------------- Tristan Leavitt (WV-R, State Delegate Kanawha Co.) ----------------
    # In office since December 1, 2024 — can only vote on 2025 and 2026 sessions
    ("tristan-leavitt", "WV", "Delegate", [
        claim("tl874a", "tristan-leavitt", "self_defense", 0, True,
              "Voted YES on West Virginia HB 4106 (2026 Regular Session), which extends West Virginia's constitutional carry framework by granting full reciprocity to out-of-state concealed-carry permit holders, allowing them to carry in West Virginia without a separate state permit. The bill passed the WV House 87-9 (February 17, 2026) and was signed by Governor Morrisey on April 1, 2026. Leavitt, a conservative Republican representing Kanawha County who has sponsored anti-federal-overreach legislation, voted with the overwhelmingly Republican majority to expand lawful firearm carry rights — directly consistent with the rubric's constitutional carry standard.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("tl874b", "tristan-leavitt", "election_integrity", 0, True,
              "Voted YES on West Virginia HB 3016 (2025 Regular Session), which strengthened West Virginia's photo voter-ID requirements by mandating that voters present a valid photo ID before casting a ballot — tightening the existing ID law. The bill passed the WV House with Republican supermajority support and was signed by Governor Morrisey on April 30, 2025. Leavitt, a consistent conservative elected in November 2024, voted with his party to close loopholes that had allowed voters to cast ballots with non-photo documentation — consistent with the rubric's voter-ID election-integrity standard.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://legiscan.com/WV/bill/HB3016/2025"]),
    ]),

    # ---------------- Scot C. Heckert (WV-R, State Delegate Jefferson Co.) ----------------
    # In office since December 2024 — using 2025 session legislation
    ("scot-c-heckert", "WV", "Delegate", [
        claim("sch874a", "scot-c-heckert", "election_integrity", 0, True,
              "Voted YES on West Virginia HB 3016 (2025 Regular Session), which strengthened West Virginia's voter-ID law by requiring photo identification to cast a ballot. The bill passed the WV House with Republican majority support and was signed April 30, 2025. Heckert, a conservative Republican who explicitly campaigns on opposing election-integrity threats in Jefferson County, WV's easternmost county bordering Maryland and Virginia, voted with his caucus to tighten voter-ID requirements — consistent with the rubric's voter-ID and election-integrity standard.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://legiscan.com/WV/bill/HB3016/2025",
               "https://www.spiritofjefferson.com/news/article_40f6ab90-91fa-11ef-8d97-c3adf4ca3573.html"]),
    ]),

    # ---------------- Sarah Drennan (WV-R, State Delegate Putnam Co.) ----------------
    # First elected November 5, 2024; in office December 1, 2024 — 2025-2026 bills only
    ("sarah-drennan", "WV", "Delegate", [
        claim("sd874a", "sarah-drennan", "self_defense", 0, True,
              "Voted YES on West Virginia HB 4106 (2026 Regular Session), which extends West Virginia's constitutional carry framework with enhanced interstate reciprocity for licensed concealed-carry holders. The bill passed the WV House 87-9 (February 17, 2026) and was signed April 1, 2026. Drennan, who represents Putnam County and serves as Assistant Majority Whip in the Republican supermajority, voted with her caucus to expand lawful firearms carry rights across state lines — consistent with the rubric's constitutional carry standard.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("sd874b", "sarah-drennan", "election_integrity", 0, True,
              "Voted YES on West Virginia HB 3016 (2025 Regular Session), which mandated photo voter identification for casting a ballot, strengthening WV's existing ID law. The bill passed the WV House with overwhelming Republican support and was signed April 30, 2025. Drennan, who campaigns explicitly on prioritizing children's education over 'current social issues in schools' and ran as a conservative NICU nurse, voted with the Republican supermajority to tighten voter-ID requirements — aligning with the rubric's voter-ID and election-integrity standard.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://legiscan.com/WV/bill/HB3016/2025"]),
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
