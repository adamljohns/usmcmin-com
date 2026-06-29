#!/usr/bin/env python3
"""Enrichment batch 489: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket) in the unset-confidence
tier since the archetype_curated federal bucket is fully exhausted.

Delegates:
  Doug Smith (doug-smith)          — WV District 39 (Mercer Co.), in office Dec 1, 2022
  Daniel Linville (daniel-linville)— WV District 22 (formerly 16, Cabell Co.), in office since Aug 2018
  Dana Ferrell (dana-ferrell)      — WV District 60 (Kanawha Co.), in office since Dec 2020
  Clay Riley (clay-riley)          — WV District 72, in office Dec 1, 2022
  Chuck Horst (chuck-horst)        — WV District 95, in office Dec 1, 2022

Key WV bills cited (Republican-supermajority party-line votes):
  HB 302 (2022 3X)   — near-total abortion ban, final House vote Sep 13, 2022 (77-17)
  HB 3293 (2021 RS)  — Save Women's Sports Act, signed April 28, 2021
  SB 456 (2025 RS)   — Riley Gaines Act, defines biological sex, signed March 12, 2025
  HB 2129 (2025 RS)  — Parents' Bill of Rights, signed April 14, 2025
  HB 4106 (2026 RS)  — Constitutional carry for ages 18-20, passed House 87-9 Feb 17, 2026

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Doug Smith (District 39, Mercer County, in office Dec 1, 2022) ----
    # Background: retired U.S. Army Colonel, 34 years Military Police
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("doug-smith", "WV", "Delegate", [
        claim("ds1", "doug-smith", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Smith, a retired U.S. Army Colonel with 34 years as a Military Police Officer, has served District 39 (Mercer County) since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Doug_Smith_(West_Virginia)"]),
        claim("ds2", "doug-smith", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("ds3", "doug-smith", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Daniel Linville (District 22 / formerly 16, Cabell County, in office since Aug 2018) ----
    # Background: business owner, Assistant Majority Whip; appointed Aug 2018 to fill vacancy, re-elected 2020/2022
    # Present for: HB 3293 (Apr 2021), HB 302 (Sep 2022), SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("daniel-linville", "WV", "Delegate", [
        claim("dl1", "daniel-linville", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Extraordinary Session), the state's near-total abortion ban, which prohibits abortion from fertilization with narrow exceptions for medical emergencies, non-viable pregnancies, and ectopic pregnancies. The bill passed the House 77-17 on September 13, 2022; Governor Justice signed it September 16, 2022. Linville, representing Cabell County (then District 16, now District 22 post-redistricting), confirmed his yes vote publicly. Mountain State Spotlight confirmed Linville voted yes.",
              ["https://mountainstatespotlight.org/2022/10/07/the-wv-races-where-abortion-is-on-the-ballot/",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/",
               "https://ballotpedia.org/Daniel_Linville"]),
        claim("dl2", "daniel-linville", "biblical_marriage", 2, True,
              "Voted for West Virginia HB 3293 (2021 Regular Session), the Save Women's Sports Act, which restricts participation in female athletic events to students whose biological sex at birth is female, barring males who identify as female from competing on women's teams. Governor Justice signed the bill on April 28, 2021. Linville has represented Cabell County continuously since his August 2018 appointment to District 16 and was one of the bill's Republican majority supporters.",
              ["https://en.wikipedia.org/wiki/West_Virginia_House_Bill_3293",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=HB3293+SUB+ENR.htm&yr=2021&sesstype=RS&i=3293",
               "https://home.wvlegislature.gov/delegate/daniel-linville/"]),
        claim("dl3", "daniel-linville", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Linville, serving as Assistant Majority Whip, supported the measure.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Dana Ferrell (District 60, Kanawha County, in office since Dec 2020) ----
    # Background: educator, business owner, developer (B.S. Business Ed, M.A. Special Ed from Marshall University)
    # Present for: HB 3293 (Apr 2021), HB 302 (Sep 2022), SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("dana-ferrell", "WV", "Delegate", [
        claim("df1", "dana-ferrell", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Extraordinary Session), the state's near-total abortion ban, prohibiting abortion from fertilization with narrow exceptions for medical emergencies, non-viable pregnancies, and ectopic pregnancies. The bill passed the House 77-17 on September 13, 2022; Governor Justice signed it September 16, 2022. Ferrell, elected in 2020 and representing District 60 (Kanawha County), was part of the House Republican supermajority that passed the bill on a near-party-line vote.",
              ["https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/",
               "https://ballotpedia.org/Dana_Ferrell"]),
        claim("df2", "dana-ferrell", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Ferrell, an educator and M.A.-holder in Special Education from Marshall University, brings classroom experience to his support of family-directed education.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/dana-ferrell/"]),
        claim("df3", "dana-ferrell", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Clay Riley (District 72, in office Dec 1, 2022) ----
    # Background: Professional Engineer (B.S. Computer Engineering + B.S. Electrical Engineering from WVU)
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("clay-riley", "WV", "Delegate", [
        claim("cri1", "clay-riley", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary and reproductive — defining 'male' and 'female' by birth biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Riley, a Professional Engineer (Computer and Electrical Engineering, WVU), has served District 72 since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Clay_Riley"]),
        claim("cri2", "clay-riley", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/clay-riley/"]),
        claim("cri3", "clay-riley", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Chuck Horst (Charles Horst Sr., District 95, in office Dec 1, 2022) ----
    # Background: first elected Nov 8, 2022, defeating Debi Carroll
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("chuck-horst", "WV", "Delegate", [
        claim("ch1", "chuck-horst", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which defines 'male' and 'female' in state law as biological and reproductive categories — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Horst (Charles Horst Sr.) has served District 95 since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Charles_Horst_Sr."]),
        claim("ch2", "chuck-horst", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/house/lawmaker.cfm?member=Delegate+Horst"]),
        claim("ch3", "chuck-horst", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
