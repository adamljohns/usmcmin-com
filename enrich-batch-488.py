#!/usr/bin/env python3
"""Enrichment batch 488: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket) in the unset-confidence
tier since the archetype_curated federal bucket is fully exhausted.

Delegates:
  George Street (george-street)           — WV District 83, in office Dec 1, 2022
  Geno Chiarelli (geno-chiarelli)         — WV District 78, in office Dec 1, 2022
  Gary G. Howell (gary-g-howell)          — WV District 87 (formerly 56), in office since 2016
  Erica Moore (erica-moore)               — WV District 15, appointed Nov 6, 2023
  Elias Coop-Gonzalez (elias-coop-gonzalez) — WV District 67, in office Dec 1, 2022

Key WV bills cited (Republican-supermajority party-line votes):
  HB 302 (2022 3X)   — near-total abortion ban, final House vote Sep 13, 2022 (77-17)
  HB 3293 (2021 RS)  — Save Women's Sports Act, signed April 28, 2021
  SB 456 (2025 RS)   — Riley Gaines Act, defines biological sex, signed March 12, 2025
  HB 2129 (2025 RS)  — Parents' Bill of Rights, signed April 14, 2025
  HB 4106 (2026 RS)  — Constitutional carry for ages 18-20, passed House 87-9 Feb 17, 2026
  HB 4412 (2026 RS)  — Age verification for minors on obscene-content sites, signed Apr 1, 2026

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
    # ---- George Street (District 83, in office Dec 1, 2022) ----
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("george-street", "WV", "Delegate", [
        claim("gs1", "george-street", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which defines 'male' and 'female' in state law as biological and reproductive categories — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it on March 12, 2025. Street has served District 83 since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/George_Street"]),
        claim("gs2", "george-street", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("gs3", "george-street", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Geno Chiarelli (District 78, Marion Co., in office Dec 1, 2022) ----
    # Background: substance abuse counselor, child protective services — familiar with family breakdown
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4412 (Apr 2026), HB 4106 (Feb 2026)
    ("geno-chiarelli", "WV", "Delegate", [
        claim("gch1", "geno-chiarelli", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex as binary in state law — defining 'male' as one born able to produce sperm and 'female' as one born able to produce ova — explicitly rejecting gender-identity ideology. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Chiarelli has served District 78 (Marion County) since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Eugene_Chiarelli"]),
        claim("gch2", "geno-chiarelli", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care without state interference. Signed by Governor Morrisey on April 14, 2025. Chiarelli's background as a substance abuse counselor and former child protective services worker in Marion County informs his commitment to protecting family integrity.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/geno-chiarelli/"]),
        claim("gch3", "geno-chiarelli", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Gary G. Howell (District 87 / formerly District 56, Mineral Co., in office since 2016) ----
    # Long-serving delegate: present for HB 3293 (2021), HB 302 (Sep 2022), SB 456 (2025), HB 4106 (2026)
    ("gary-g-howell", "WV", "Delegate", [
        claim("ggh1", "gary-g-howell", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Extraordinary Session), the state's near-total abortion ban, which bans abortion from fertilization with narrow exceptions for medical emergencies, non-viable pregnancies, and ectopic pregnancies. The bill passed the House 77-17 on September 13, 2022; Governor Justice signed it September 16, 2022. Howell has continuously served in the House since 2016, representing Mineral County (District 56 until redistricting, then District 87).",
              ["https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/",
               "https://ballotpedia.org/Gary_Howell_(West_Virginia)"]),
        claim("ggh2", "gary-g-howell", "biblical_marriage", 2, True,
              "Voted for West Virginia HB 3293 (2021 Regular Session), the Save Women's Sports Act, which restricts participation in female athletic events to students whose biological sex at birth is female, explicitly barring males who identify as female from women's teams. Signed by Governor Justice on April 28, 2021. Howell was serving in District 56 (Mineral County) when the bill passed.",
              ["https://en.wikipedia.org/wiki/West_Virginia_House_Bill_3293",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=HB3293+SUB+ENR.htm&yr=2021&sesstype=RS&i=3293"]),
        claim("ggh3", "gary-g-howell", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Erica Moore (District 15, appointed Nov 6, 2023 by Gov. Justice) ----
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026), HB 4412 (Apr 2026)
    ("erica-moore", "WV", "Delegate", [
        claim("em1", "erica-moore", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary and reproductive — defining 'male' as one born able to produce sperm and 'female' as one born able to produce ova — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Moore was appointed to District 15 by Governor Justice on November 6, 2023, replacing Riley Keaton, and won the seat outright in November 2024.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Erica_Moore_(West_Virginia)"]),
        claim("em2", "erica-moore", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("em3", "erica-moore", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Elias Coop-Gonzalez (District 67, in office Dec 1, 2022) ----
    # Background: Leadership Institute, interned at U.S. House — ideologically conservative
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026), HB 4412 (Apr 2026)
    ("elias-coop-gonzalez", "WV", "Delegate", [
        claim("ecg1", "elias-coop-gonzalez", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which defines 'male' and 'female' in state law as biological and reproductive categories — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Coop-Gonzalez has served District 67 since December 1, 2022 and previously worked at The Leadership Institute, a conservative political training organization in Arlington, Virginia.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Elias_Coop-Gonzalez"]),
        claim("ecg2", "elias-coop-gonzalez", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("ecg3", "elias-coop-gonzalez", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
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
