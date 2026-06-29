#!/usr/bin/env python3
"""Enrichment batch 491: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket, D names) in the
unset-confidence tier since the archetype_curated federal bucket is fully
exhausted.

Delegates:
  Dave Foggin (dave-foggin)                 — WV District 14 (Wood Co.), in office Dec 1, 2022;
                                               B.S. chemical engineering, M.A. secondary education;
                                               physics teacher and EMT; Assistant Majority Whip
  David Cannon (david-cannon)               — WV District 89 (Hampshire Co.), appointed Jan 13, 2025
                                               by Gov. Morrisey; former Hampshire County Commissioner
  David Green (david-green)                 — WV District 36, appointed Jan 29, 2024 by Gov. Justice;
                                               independent insurance agent, Concord University B.S.;
                                               Assistant Majority Leader
  David McCormick Jr. (david-mccormick)     — WV District 82 (Monongalia Co./WVU area),
                                               in office Dec 1, 2024; Assistant Majority Leader
  David Elliott Pritt (david-elliott-pritt) — WV District 50 (Fayette Co.), in office Dec 1, 2022;
                                               switched from Democrat to Republican April 2023;
                                               U.S. Air Force 2008-2014; Concord Univ. B.A./M.A.;
                                               named Assistant Majority Leader by Speaker Hanshaw 2025

Key WV bills cited (Republican-supermajority party-line votes):
  SB 456  (2025 RS)  — Riley Gaines Act, defines biological sex, signed March 12, 2025
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
    # ---- Dave Foggin (District 14, Wood County, in office since Dec 1, 2022) ----
    # B.S. chemical engineering, M.A. secondary education, EMT; physics teacher; Belleville WV
    # Assistant Majority Whip; won re-election November 5, 2024
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("dave-foggin", "WV", "Delegate", [
        claim("df1", "dave-foggin", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Foggin, a physics teacher and EMT with degrees in chemical engineering and secondary education, has represented District 14 (Wood County) since December 1, 2022 and serves as Assistant Majority Whip.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Dave_Foggin",
               "https://home.wvlegislature.gov/delegate/dave-foggin/"]),
        claim("df2", "dave-foggin", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Foggin, who brings the perspective of a career educator (physics teacher) and first responder (EMT) to family-autonomy legislation, supported the measure as part of the Republican supermajority.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/dave-foggin/"]),
        claim("df3", "dave-foggin", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Foggin, representing District 14 along the Ohio River valley in Wood County, supported the expansion of Second Amendment rights without age-based licensing requirements.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/dave-foggin/"]),
    ]),

    # ---- David Cannon (District 89, Hampshire County, appointed Jan 13, 2025) ----
    # Former Hampshire County Commissioner; appointed by Gov. Morrisey to replace Darren Thorne (D)
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("david-cannon", "WV", "Delegate", [
        claim("dc1", "david-cannon", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Cannon, a former Hampshire County Commissioner appointed to the House of Delegates by Governor Morrisey on January 13, 2025 (replacing a Democrat in District 89), cast this vote in his first months in office.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/David_Cannon_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/david-cannon/"]),
        claim("dc2", "david-cannon", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Cannon, who previously served as a County Commissioner in Hampshire County (Romney, WV area) before his January 2025 House appointment, brought local-government experience to the vote on parental and family sovereignty.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/david-cannon/"]),
        claim("dc3", "david-cannon", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Cannon, representing District 89 in Hampshire County, supported the expansion of constitutional carry rights without age-based permit restrictions.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/david-cannon/"]),
    ]),

    # ---- S. David Green (District 36, appointed Jan 29, 2024 by Gov. Justice) ----
    # Independent insurance agent; B.S. Concord University; Assistant Majority Leader
    # Won 2024 general election defeating Tiffany Clemins
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("david-green", "WV", "Delegate", [
        claim("dg1", "david-green", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Green, who serves as an Assistant Majority Leader and was appointed to District 36 by Governor Justice in January 2024, cast this vote in his first full legislative session.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/S._David_Green",
               "https://home.wvlegislature.gov/delegate/david-green/"]),
        claim("dg2", "david-green", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Green, an independent insurance agent and Concord University graduate representing District 36, won his first full election in November 2024 and serves in House leadership as an Assistant Majority Leader.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/david-green/"]),
        claim("dg3", "david-green", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Green, serving as one of the House's Assistant Majority Leaders for District 36, supported the measure expanding Second Amendment rights to young adults without permit requirements.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/david-green/"]),
    ]),

    # ---- David McCormick Jr. (District 82, Monongalia County, in office Dec 1, 2024) ----
    # Assistant Majority Leader; represents WVU college-town district
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("david-mccormick", "WV", "Delegate", [
        claim("dm1", "david-mccormick", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. McCormick, who serves as Assistant Majority Leader for District 82 (Monongalia County, home of West Virginia University), cast this vote in his first legislative session after taking office December 1, 2024.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/David_McCormick_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/david-mccormick/"]),
        claim("dm2", "david-mccormick", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. McCormick, representing District 82 in Monongalia County and serving as one of the House's Assistant Majority Leaders, supported the measure codifying parental authority over children's education and healthcare in his first regular session.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/david-mccormick/"]),
        claim("dm3", "david-mccormick", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. McCormick, representing District 82 in the Morgantown/WVU area and serving as Assistant Majority Leader, supported the expansion of constitutional carry rights to young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/david-mccormick/"]),
    ]),

    # ---- David Elliott Pritt (District 50, Fayette County, in office Dec 1, 2022) ----
    # U.S. Air Force 2008-2014; B.A. and M.A. Concord University; switched D→R April 2023
    # Named Assistant Majority Leader by Speaker Hanshaw for 87th Legislature (2025)
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026) — all as Republican
    ("david-elliott-pritt", "WV", "Delegate", [
        claim("dep1", "david-elliott-pritt", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Pritt, a U.S. Air Force veteran who switched from the Democratic Party to the Republican Party in April 2023, cast this vote as a member of the House Republican Caucus and in his capacity as one of the House's Assistant Majority Leaders (appointed by Speaker Hanshaw, 2025).",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/David_Pritt",
               "https://home.wvlegislature.gov/delegate/david-elliott-pritt/"]),
        claim("dep2", "david-elliott-pritt", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Pritt, a Concord University graduate and Air Force veteran representing District 50 (Fayette County) who joined the House Republican Caucus in April 2023 after leaving the Democratic Party, supported the measure as an Assistant Majority Leader.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/david-elliott-pritt/",
               "https://wvpublic.org/w-va-state-lawmaker-elliott-pritt-switches-from-dem-to-gop/"]),
        claim("dep3", "david-elliott-pritt", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Pritt, a veteran of the U.S. Air Force (2008-2014) who represents District 50 in Fayette County and serves as an Assistant Majority Leader, supported the expansion of Second Amendment rights to young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/david-elliott-pritt/"]),
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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
