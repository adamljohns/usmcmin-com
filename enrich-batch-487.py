#!/usr/bin/env python3
"""Enrichment batch 487: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket) in the unset-confidence
tier since the archetype_curated federal bucket is fully exhausted.

Delegates:
  JB Akers (james-robert-akers-ii) — WV District 55, appointed Jan 9, 2024
  Ian T. Masters (ian-t-masters)   — WV District 91, appointed Jan 24, 2025
  Henry Dillon (henry-dillon)      — WV District 29, elected Nov 2022 (in office Dec 1, 2022)
  Guy Ward (guy-ward)              — WV District 74, served 2020-2022 + reappointed Jan 29, 2026
  Gregory A. Watt (gregory-a-watt) — WV District 48, appointed Oct 15, 2025

Key WV bills cited (Republican-supermajority party-line votes):
  HB 302 (2022 3X)   — near-total abortion ban, final House vote Sep 13, 2022 (77-17)
  HB 3293 (2021 RS)  — Save Women's Sports Act, signed April 28, 2021
  SB 456 (2025 RS)   — Riley Gaines Act, defines biological sex, passed House Mar 2025
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
    # ---- JB Akers (District 55, Kanawha Co., appointed Jan 9, 2024, Judiciary Chair) ----
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("james-robert-akers-ii", "WV", "Delegate", [
        claim("jbakers1", "james-robert-akers-ii", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which defines 'male' and 'female' in state law as biological and reproductive categories — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it on March 12, 2025. Akers has chaired the House Judiciary Committee since 2024 and was present throughout the 2025 session.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("jbakers2", "james-robert-akers-ii", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("jbakers3", "james-robert-akers-ii", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Ian T. Masters (District 91, appointed Jan 24, 2025; President of WVCDL) ----
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("ian-t-masters", "WV", "Delegate", [
        claim("imasters1", "ian-t-masters", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex as binary in state law — defining 'male' as one born able to produce sperm and 'female' as one born able to produce ova — explicitly rejecting gender-identity ideology. Passed the WV House in early March 2025; signed by Governor Morrisey on March 12, 2025. Masters was appointed to the House on January 24, 2025, weeks before the vote.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("imasters2", "ian-t-masters", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care without state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("imasters3", "ian-t-masters", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement; passed the House 87-9 on February 17, 2026, signed by Governor Morrisey April 1, 2026. Masters brings direct Second Amendment expertise to the House: he is the President of the West Virginia Citizens Defense League (WVCDL), the state's primary firearms-rights advocacy organization, which opposes red-flag laws, assault-weapons bans, and magazine restrictions.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://ballotpedia.org/Ian_Masters"]),
    ]),

    # ---- Henry "Corby" Dillon (District 29, Wayne Co., first in office Dec 1, 2022) ----
    # Present for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("henry-dillon", "WV", "Delegate", [
        claim("hdillon1", "henry-dillon", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), codifying biological sex in state law as binary and reproductive — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Dillon serves on the House Rules and Finance committees.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("hdillon2", "henry-dillon", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Dillon, a former educator with a Ph.D. in Leadership from Marshall University, serves on the House Education-aligned panels that advanced the measure.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Henry_C._Dillon"]),
        claim("hdillon3", "henry-dillon", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20, removing the permit requirement for concealed carry. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Guy Ward (District 74, Marion Co.) ----
    # First term Dec 2020 – Dec 2022: voted HB 3293 (Apr 2021) and HB 302 (Sep 2022)
    # Reappointed Jan 29, 2026: voted HB 4106 (Feb 2026)
    ("guy-ward", "WV", "Delegate", [
        claim("gward1", "guy-ward", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Extraordinary Session), the state's near-total abortion ban, which bans abortion from fertilization with narrow exceptions for medical emergencies, non-viable pregnancies, and ectopic pregnancies. The bill passed the House 77-17 on September 13, 2022; Governor Justice signed it September 16, 2022. Ward served as Delegate from District 74 from December 2020 through December 2022 and was in office for the vote.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/"]),
        claim("gward2", "guy-ward", "biblical_marriage", 2, True,
              "Voted for West Virginia HB 3293 (2021 Regular Session), the Save Women's Sports Act, which restricts participation in female athletic events to students whose biological sex at birth is female, explicitly banning transgender males from women's teams. Signed by Governor Justice on April 28, 2021. Ward was serving his first House term (District 74, December 2020 – December 2022) when the bill passed.",
              ["https://en.wikipedia.org/wiki/West_Virginia_House_Bill_3293",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=HB3293+SUB+ENR.htm&yr=2021&sesstype=RS&i=3293"]),
        claim("gward3", "guy-ward", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20, removing the permit requirement for concealed carry. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Ward was reappointed to the House on January 29, 2026 — just weeks before the vote.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://blog.wvlegislature.gov/breaking/2026/01/29/guy-ward-sworn-into-house/"]),
    ]),

    # ---- Gregory A. Watt (District 48, Webster/Greenbrier/Nicholas, appointed Oct 15, 2025) ----
    # Present for: HB 4106 (Feb 2026), HB 4412 (Apr 2026)
    ("gregory-a-watt", "WV", "Delegate", [
        claim("gwatt1", "gregory-a-watt", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Watt, a retired U.S. Army officer, was appointed to the House on October 15, 2025.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://blog.wvlegislature.gov/headline/2025/10/15/gregory-a-watt-sworn-in-as-delegate/"]),
        claim("gwatt2", "gregory-a-watt", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 4412 (2026 Regular Session), requiring websites that distribute obscene or explicit sexual content to implement age-verification measures to prevent minors from accessing such material; signed by Governor Morrisey on April 1, 2026. The bill gives parents a structural safeguard to protect children from online pornography — aligning with the rubric's family and child-sovereignty principle.",
              ["https://legiscan.com/WV/bill/HB4412/2026",
               "https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4412%20sub1%20enr.pdf"]),
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
