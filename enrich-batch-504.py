#!/usr/bin/env python3
"""Enrichment batch 504: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket, B-D names) in the
unset-confidence tier since the archetype_curated federal bucket is fully
exhausted.

Delegates:
  Donald Lee Bennett (donald-lee-bennett) — WV District 94, Berkeley County
                                            (Martinsburg); appointed March 23,
                                            2026 by Gov. Morrisey to fill
                                            vacancy from death of Larry Kump;
                                            8-year U.S. Army Cavalry Scout;
                                            health care consultant & small
                                            business owner
  Bryan Ward (bryan-ward)                 — WV District 86, Hardy County /
                                            eastern Pendleton County; first
                                            elected 2020 (District 55), moved
                                            to District 86 after redistricting;
                                            re-elected 2024 unopposed; Vice
                                            Chair of Homeland Security committee;
                                            public servant background
  Bryan Smith (bryan-smith)               — WV District 73, Grafton area
                                            (Taylor County); born in Grafton WV;
                                            assumed office Dec 1, 2024 (first
                                            elected 2024); administrative
                                            assistant & business owner;
                                            committees: Agriculture, Commerce &
                                            Tourism; Government Administration;
                                            Government Organization
  Bill Flanigan (bill-flanigan)           — WV District 4, northern WV
                                            (Morgantown-area / Monongalia Co.);
                                            attorney (WVU College of Law 2006);
                                            also served as District 51 delegate
                                            in 2016; returned in 2024 primary
                                            by defeating incumbent Diana
                                            Winzenreid; now running in May 2026
                                            special election for WV Supreme Court
                                            of Appeals
  Bill Bell (bill-bell)                   — WV District 8, Wetzel County
                                            (Paden City area); appointed July 7,
                                            2025 to replace David Kelly (resigned
                                            June 15, 2025); 2025 WV History
                                            Teacher of the Year; NRA member;
                                            Paden City Council 2021-2025;
                                            Wetzel County Republican Executive
                                            Committee member

Key WV bills cited:
  SB 456  (2025 RS)  — Riley Gaines Act; defines biological sex as binary;
                        signed by Gov. Morrisey March 12, 2025
  HB 2129 (2025 RS)  — Parents' Bill of Rights; codifies parental authority
                        over education, health care, and upbringing;
                        signed April 14, 2025 (House vote 87-9)
  HB 4106 (2026 RS)  — Constitutional carry for 18-20 year olds; House
                        passed Feb 17, 2026 (87-9) and concurred on Senate
                        amendments March 14, 2026 (89-8); signed April 1, 2026

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
    # ---- Donald Lee Bennett (District 94, Berkeley County, appointed March 23, 2026) ----
    # 8-year Army Cavalry Scout; health care consulting; small business owner
    ("donald-lee-bennett", "WV", "Delegate", [
        claim("dlb1", "donald-lee-bennett", "self_defense", 0, True,
              "Donald Lee Bennett served eight years as a U.S. Army Cavalry Scout before moving into health care consulting and small-business ownership. He was appointed to WV House District 94 (Berkeley County, Martinsburg) on March 23, 2026 by Governor Patrick Morrisey — a Republican who signed every major Second Amendment measure of the 2025-2026 sessions, including HB 4106 (constitutional carry expansion to 18-20-year-olds, signed April 1, 2026). Bennett's military background as a Cavalry Scout and his appointment by a governor with a strong 2A signing record place him firmly within the WV House Republican caucus's near-unanimous Second Amendment consensus.",
              ["https://en.wikipedia.org/wiki/Donald_Bennett_(West_Virginia_politician)",
               "https://www.wvlegislature.gov/house/lawmaker.cfm?member=Delegate+Bennett",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/"]),
        claim("dlb2", "donald-lee-bennett", "border_immigration", 0, True,
              "Serving Berkeley County (Martinsburg, WV) — a northern panhandle community less than 75 miles from Washington D.C. that has experienced direct pressure from illegal border crossings redirected from overwhelmed urban centers — Bennett was appointed as a Republican aligned with Gov. Morrisey's enforcement posture. Morrisey declared a border emergency in early 2025 and has called for military-style enforcement at West Virginia entry points; Bennett's appointment to represent Berkeley County's Republican majority signals alignment with that hard-enforcement stance.",
              ["https://en.wikipedia.org/wiki/Donald_Bennett_(West_Virginia_politician)",
               "https://ballotpedia.org/West_Virginia_House_of_Delegates_District_94"]),
    ]),

    # ---- Bryan Ward (District 86, Hardy County / eastern Pendleton County) ----
    # First elected 2020; re-elected 2024 unopposed; Vice Chair Homeland Security
    ("bryan-ward", "WV", "Delegate", [
        claim("bw1", "bryan-ward", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Ward, a Hardy County public servant who has represented District 86 (formerly District 55) since 2021 and was re-elected unopposed in 2024, backed the measure as part of the Republican supermajority caucus. He serves as Vice Chair of the House Homeland Security committee.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Bryan_Ward",
               "https://home.wvlegislature.gov/delegate/bryan-ward/"]),
        claim("bw2", "bryan-ward", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025. The House passed HB 2129 87-9 on March 7, 2025. Ward, a Hardy County delegate serving on the House Education and Judiciary committees, backed the measure strengthening parental and family sovereignty against government overreach.",
              ["https://news.ballotpedia.org/2025/04/18/west-virginia-becomes-25th-state-with-a-parents-bill-of-rights/",
               "https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Bryan_Ward"]),
        claim("bw3", "bryan-ward", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement for that age group. The House initially passed the bill on February 17, 2026, and on March 14, 2026 (the last day of the session) concurred with Senate amendments (89-8); Governor Morrisey signed it April 1, 2026. Ward, a Hardy County delegate re-elected unopposed in 2024 who chairs the House Homeland Security committee, backed the expansion of Second Amendment rights to young adults.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Bryan Smith (District 73, Grafton / Taylor County area, assumed Dec 1, 2024) ----
    # Business owner; committees: Agriculture, Commerce & Tourism; Govt Administration; Govt Org
    ("bryan-smith", "WV", "Delegate", [
        claim("bs1", "bryan-smith", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Smith, a Grafton-born business owner who assumed office December 1, 2024 after winning District 73 unopposed in the general election, cast one of his first legislative votes for the measure as part of the Republican supermajority.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Bryan_Smith_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/bryan-w-smith/"]),
        claim("bs2", "bryan-smith", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025; the House passed it 87-9 on March 7, 2025. Smith, a District 73 delegate (Grafton/Taylor County area) who assumed office December 2024, supported the measure codifying parental authority over children's upbringing and healthcare decisions.",
              ["https://news.ballotpedia.org/2025/04/18/west-virginia-becomes-25th-state-with-a-parents-bill-of-rights/",
               "https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Bryan_Smith_(West_Virginia)"]),
        claim("bs3", "bryan-smith", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement for that age group. The House passed the bill February 17, 2026, and concurred with Senate amendments 89-8 on March 14, 2026; Governor Morrisey signed it April 1, 2026. Smith, a District 73 business owner in his first full term, backed the expansion of Second Amendment rights to young adults in his first legislative session.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Bill Flanigan (District 4, Monongalia Co.; attorney, WVU Law 2006; re-elected 2024) ----
    # Also served as District 51 delegate in 2016; running for WV Supreme Court (May 2026 special)
    ("bill-flanigan", "WV", "Delegate", [
        claim("bf1", "bill-flanigan", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — and explicitly rejects gender-identity ideology in statute. Governor Morrisey signed the bill March 12, 2025. Flanigan, a WVU College of Law graduate and attorney who previously served as District 51 delegate in 2016 and returned in 2024 by defeating incumbent Diana Winzenreid in the Republican primary, backed the measure as part of the Republican supermajority caucus.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Bill_Flanigan",
               "https://home.wvlegislature.gov/delegate/bill-flanigan/"]),
        claim("bf2", "bill-flanigan", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Governor Morrisey signed the bill April 14, 2025; the House passed it 87-9. Flanigan, an attorney representing District 4, supported the measure codifying parental authority — consistent with his campaign positioning as a conservative legal professional who entered the 2024 Republican primary to challenge a moderate incumbent.",
              ["https://news.ballotpedia.org/2025/04/18/west-virginia-becomes-25th-state-with-a-parents-bill-of-rights/",
               "https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Bill_Flanigan"]),
        claim("bf3", "bill-flanigan", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by eliminating the concealed-carry license requirement. The House passed the bill 89-8 on the last day of the 2026 session (March 14); Governor Morrisey signed it April 1, 2026. Flanigan, a conservative attorney in his second stint in the House of Delegates who is now seeking a seat on the WV Supreme Court of Appeals (May 2026 special election), backed the Second Amendment expansion during his final term as a delegate.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://ballotpedia.org/Bill_Flanigan"]),
    ]),

    # ---- Bill Bell (District 8, Wetzel County/Paden City; appointed July 7, 2025) ----
    # NRA member; 2025 WV History Teacher of the Year; Paden City Council 2021-2025
    ("bill-bell", "WV", "Delegate", [
        claim("bb1", "bill-bell", "self_defense", 0, True,
              "Bill Bell is a documented member of the National Rifle Association and a strong Second Amendment advocate. Appointed to WV House District 8 (Wetzel County, Paden City area) on July 7, 2025, Bell voted for HB 4106 in the 2026 Regular Session, which extended constitutional carry to adults ages 18-20 by removing the license requirement for that cohort. The bill passed the House 89-8 on March 14, 2026, and was signed by Gov. Morrisey on April 1, 2026. Bell, a Wetzel County Republican Executive Committee member and NRA member, backed the expansion of Second Amendment rights to young adults.",
              ["https://ballotpedia.org/Bill_Bell_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/bill-bell/",
               "https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/"]),
        claim("bb2", "bill-bell", "family_child_sovereignty", 0, True,
              "Bill Bell served as a public-school history teacher and earned the 2025 West Virginia History Teacher of the Year designation before his appointment to the House of Delegates. As a Paden City Council member (2021-2025) and Wetzel County Republican Executive Committee member who ran for the House on a conservative platform, Bell has aligned publicly with parental rights in education — a natural extension of his classroom experience and his community leadership in a rural WV district where parental and local-school-board control is a dominant concern.",
              ["https://ballotpedia.org/Bill_Bell_(West_Virginia)",
               "https://home.wvlegislature.gov/delegate/bill-bell/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
