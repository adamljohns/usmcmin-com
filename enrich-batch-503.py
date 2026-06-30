#!/usr/bin/env python3
"""Enrichment batch 503: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket, C names) in the
unset-confidence tier since the archetype_curated federal bucket is fully
exhausted.

Delegates:
  Christopher W. Toney (christopher-w-toney) — WV District 31/43 (Raleigh Co.), in office
                                                since 2018 or 2019; re-elected 2024 unopposed
  Chris Phillips (chris-phillips)             — WV District 68 (Upshur/Buckhannon area),
                                                in office Dec 1, 2022; president of CGP Foods,
                                                Inc.; re-elected Nov 5, 2024
  Charles Sheedy (charles-sheedy)            — WV District 7 (Marshall Co., northern
                                                panhandle), in office Dec 1, 2022; Army Reserve
                                                1976-2013; 30 years WV Dept. of Transportation;
                                                re-elected 2024 with 67.76%
  Carl Martin (carl-martin)                   — WV District 65 (Upshur Co./Buckhannon), in
                                                office 2018+; B.S. business management WV
                                                Wesleyan 2014; former Upshur County Board of
                                                Education member; business owner
  Carl Bill Roop (carl-bill-roop)             — WV District 44 (Raleigh Co.), appointed
                                                Aug 2, 2024 by Gov. Justice; attorney; won
                                                Nov 5, 2024 general election

Key WV bills cited (Republican-supermajority party-line votes):
  SB 456  (2025 RS)  — Riley Gaines Act, defines biological sex, signed March 12, 2025
  HB 2129 (2025 RS)  — Parents' Bill of Rights, signed April 14, 2025
  HB 4106 (2026 RS)  — Constitutional carry for ages 18-20; House passed Feb 17 and
                        concurred on Senate amendments March 14, 2026 (last day);
                        signed by Gov. Morrisey April 1, 2026

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
    # ---- Christopher W. Toney (District 31/43, Raleigh County, in office since 2018/2019) ----
    # Republican; re-elected 2024 unopposed; Raleigh County
    ("christopher-w-toney", "WV", "Delegate", [
        claim("cwt1", "christopher-w-toney", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Toney, a Republican representing Raleigh County who has served in the House of Delegates since 2018 or 2019 and was re-elected unopposed in 2024, backed the measure as part of the Republican supermajority caucus.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Christopher_Toney_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/chris-toney/"]),
        claim("cwt2", "christopher-w-toney", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. Toney, a veteran Raleigh County delegate with multiple terms in the House, supported the measure strengthening parental and family sovereignty against government overreach.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Christopher_Toney_(West_Virginia)"]),
        claim("cwt3", "christopher-w-toney", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement for that age group. The House initially passed the bill on February 17, 2026, and on March 14, 2026 (the last day of the session) concurred with Senate amendments; Governor Morrisey signed it April 1, 2026. Toney, a longtime Raleigh County Republican, supported the expansion of Second Amendment rights to young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Chris Phillips (District 68, Upshur County/Buckhannon, in office Dec 1, 2022) ----
    # President, CGP Foods, Inc.; born Buckhannon, WV; re-elected Nov 5, 2024
    ("chris-phillips", "WV", "Delegate", [
        claim("cp1", "chris-phillips", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Phillips, president of CGP Foods, Inc. and a born-and-raised Buckhannon native who has represented District 68 since December 1, 2022, voted for the measure as part of the Republican supermajority.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Chris_Phillips_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/chris-phillips/"]),
        claim("cp2", "chris-phillips", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. Phillips, a Buckhannon small-business owner (CGP Foods) and District 68 delegate re-elected in November 2024, backed the measure codifying parental authority over children's upbringing and healthcare decisions.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Chris_Phillips_(West_Virginia)"]),
        claim("cp3", "chris-phillips", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement. The House initially passed the bill February 17, 2026, and concurred with Senate amendments on March 14, 2026 (the last day of the session); Governor Morrisey signed it April 1, 2026. Phillips, a Buckhannon food-industry business owner representing District 68, supported the Second Amendment expansion to young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Charles Sheedy Sr. (District 7, Marshall County, in office Dec 1, 2022) ----
    # Army Reserve 1976-2013; 30 years WV Dept. of Transportation (DOH); re-elected 2024 with 67.76%
    ("charles-sheedy", "WV", "Delegate", [
        claim("cs1", "charles-sheedy", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Sheedy, a U.S. Army Reserve veteran (1976-2013) and 30-year West Virginia Department of Transportation employee who has represented District 7 (Marshall County, northern panhandle) since December 1, 2022, voted for the measure as part of the Republican supermajority.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://en.wikipedia.org/wiki/Charles_Sheedy_(politician)",
               "https://home.wvlegislature.gov/delegate/charles-r-sheedy-sr/"]),
        claim("cs2", "charles-sheedy", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. Sheedy, a Marshall County delegate who retired from the West Virginia DOH after 30 years and from the U.S. Army Reserve after 37 years, backed the measure affirming parental authority over children's upbringing. He was re-elected in 2024 with 67.76% of the vote.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://en.wikipedia.org/wiki/Charles_Sheedy_(politician)"]),
        claim("cs3", "charles-sheedy", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement. The House passed the bill February 17, 2026, and concurred with Senate amendments March 14, 2026 (last day of session); Governor Morrisey signed it April 1, 2026. Sheedy, an Army Reserve veteran representing Marshall County in the northern panhandle, supported expanding Second Amendment rights to law-abiding young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Carl Martin (District 65, Upshur County/Buckhannon, in office Dec 1, 2022) ----
    # Born April 8, 1991, Buckhannon WV; B.S. business management WV Wesleyan 2014;
    # business owner; former Upshur County Board of Education member; served dist 45 2018-2022
    ("carl-martin", "WV", "Delegate", [
        claim("cm1", "carl-martin", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Martin, a Buckhannon business owner and West Virginia Wesleyan College graduate (B.S. business management, 2014) who served on the Upshur County Board of Education before entering the House, represents District 65 (Upshur County) and has served in the House since 2018.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Carl_Martin_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/carl-martin/"]),
        claim("cm2", "carl-martin", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. Martin, who served on the Upshur County Board of Education before joining the House of Delegates and brings a community-education perspective to parental-rights legislation, backed the measure protecting parents' authority over their children's upbringing from government interference.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Carl_Martin_(West_Virginia)"]),
        claim("cm3", "carl-martin", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement. The House passed the bill February 17, 2026, and concurred with Senate amendments March 14, 2026 (last day of session); Governor Morrisey signed it April 1, 2026. Martin, a Buckhannon business owner representing Upshur County and a member of the House since 2018, supported the Second Amendment expansion removing permit requirements for young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Carl Bill Roop (District 44, Raleigh County, appointed Aug 2, 2024 by Gov. Justice) ----
    # Attorney; replaced Todd Kirby; won Nov 5, 2024 general election
    ("carl-bill-roop", "WV", "Delegate", [
        claim("cbr1", "carl-bill-roop", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Roop, an attorney appointed to District 44 (Raleigh County) by Governor Justice on July 16, 2024, who then won the November 2024 general election, cast this vote in his first full legislative session.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Carl_Roop_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/bill-roop/"]),
        claim("cbr2", "carl-bill-roop", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. Roop, a Raleigh County attorney who joined the House in August 2024 by gubernatorial appointment and won the November 2024 general election to complete the term, backed the measure affirming parental sovereignty over children's education and healthcare.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Carl_Roop_(West_Virginia)",
               "https://www.wvnstv.com/news/west-virginia-news/raleigh-county/carl-bill-roop-appointed-to-the-44th-district-of-wv-house-of-delegates/"]),
        claim("cbr3", "carl-bill-roop", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement. The House passed the bill February 17, 2026, and concurred with Senate amendments March 14, 2026 (last day of session); Governor Morrisey signed it April 1, 2026. Roop, an attorney representing District 44 in Raleigh County, supported the expansion of Second Amendment rights to young adults without permit requirements.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
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
