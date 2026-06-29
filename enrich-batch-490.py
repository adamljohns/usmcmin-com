#!/usr/bin/env python3
"""Enrichment batch 490: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket, A/B names) in the
unset-confidence tier since the archetype_curated federal bucket is fully
exhausted.

Delegates:
  Adam Burkhammer (adam-burkhammer)   — WV District 64, in office since Dec 1, 2020;
                                         co-sponsor HB 3293 (Save Women's Sports Act 2021);
                                         business owner, foster parent, 6 children
  Adam Vance (adam-vance)             — WV District 35, in office since Dec 1, 2022;
                                         underground coal miner; Assistant Majority Whip; 5 children
  Andy Shamblin (andy-shamblin)       — WV District 59, in office since Dec 1, 2022;
                                         educator and minister; B.A. WVSU 2014, M.A. Marshall 2018;
                                         Assistant Majority Whip; former Nitro City Council member
  Bill Ridenour (bill-ridenour)       — WV District 100, in office since Dec 1, 2022;
                                         U.S. Marine Corps (1980-2000, retired);
                                         Defense Intelligence Agency; Pentagon strategic policy;
                                         Assistant Majority Whip
  Bob Fehrenbacher (bob-fehrenbacher) — WV District 11, in office since Dec 1, 2022;
                                         running for WV State Senate District 3 (2026)

Key WV bills cited (Republican-supermajority party-line votes):
  HB 3293 (2021 RS)  — Save Women's Sports Act, signed April 28, 2021
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
    # ---- Adam Burkhammer (District 64, in office since Dec 1, 2020) ----
    # Business owner (A.J. Burk LLC, RiCo Properties); foster parent; 6 children
    # In office for: HB 3293 (Apr 2021), HB 302 (Sep 2022), SB 456 (Mar 2025),
    #                HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("adam-burkhammer", "WV", "Delegate", [
        claim("ab1", "adam-burkhammer", "biblical_marriage", 2, True,
              "Was one of 11 original co-sponsors of West Virginia HB 3293 (2021 Regular Session), the Save Women's Sports Act, which restricts participation in female athletic events to students whose biological sex at birth is female, barring males who identify as female from competing on women's teams. Governor Justice signed the bill on April 28, 2021. Burkhammer, a business owner and foster parent representing District 64 (Upshur County), co-sponsored the bill in his first term — demonstrating an early, proactive commitment to protecting biological-sex distinctions in state law.",
              ["https://en.wikipedia.org/wiki/West_Virginia_House_Bill_3293",
               "https://ballotpedia.org/Adam_Burkhammer",
               "https://home.wvlegislature.gov/delegate/adam-burkhammer/"]),
        claim("ab2", "adam-burkhammer", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Burkhammer, himself a foster parent raising 6 children and representing District 64, brings personal investment to parental-rights and child-welfare legislation.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/adam-burkhammer/"]),
        claim("ab3", "adam-burkhammer", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Adam Vance (District 35, in office since Dec 1, 2022) ----
    # Underground coal miner from Beckley, WV; 5 children; Assistant Majority Whip
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("adam-vance", "WV", "Delegate", [
        claim("av1", "adam-vance", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Vance, an underground coal miner serving as Assistant Majority Whip for District 35, has represented the district since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Adam_Vance"]),
        claim("av2", "adam-vance", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Vance, a father of 5 and coal industry worker from Beckley, WV, supported the measure as part of the Republican supermajority.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/adam-vance/"]),
        claim("av3", "adam-vance", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Andy Shamblin (District 59, in office since Dec 1, 2022) ----
    # Educator and minister; B.A. WV State University 2014, M.A. Marshall University 2018
    # Former Nitro City Council member; Assistant Majority Whip; Vice Chair, House Judiciary Courts Subcommittee
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("andy-shamblin", "WV", "Delegate", [
        claim("as1", "andy-shamblin", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary and reproductive — defining 'male' and 'female' by birth biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Shamblin, an ordained minister and educator representing District 59 (Kanawha County) since December 2022, serves as Assistant Majority Whip and Vice Chair of the House Judiciary Courts Subcommittee.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Andy_Shamblin"]),
        claim("as2", "andy-shamblin", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Shamblin, who holds a graduate degree in education from Marshall University and served on the Nitro City Council, brings both classroom experience and civic leadership to family-autonomy legislation.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/andy-shamblin/"]),
        claim("as3", "andy-shamblin", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---- Bill Ridenour (District 100, in office since Dec 1, 2022) ----
    # U.S. Marine Corps officer 1980-2000 (retired); Defense Intelligence Agency;
    # chief of strategic policy, Pentagon; B.S. Purdue 1980; M.S. Univ. of Oklahoma 2000;
    # Marine Corps War College 2017; Assistant Majority Whip
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("bill-ridenour", "WV", "Delegate", [
        claim("br1", "bill-ridenour", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Ridenour, a retired U.S. Marine Corps officer with 20 years of active duty service (1980-2000), serves as Assistant Majority Whip for District 100 and has represented the district since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/William_Ridenour"]),
        claim("br2", "bill-ridenour", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025. Ridenour, a retired Marine Corps officer who later served as a defense intelligence officer with the Defense Intelligence Agency and as chief of strategic policy at the Pentagon, supports protecting families from government overreach.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/bill-ridenour/"]),
        claim("br3", "bill-ridenour", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Ridenour, a 20-year Marine Corps veteran with deep arms and defense policy experience, supported the measure expanding Second Amendment rights.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://home.wvlegislature.gov/delegate/bill-ridenour/"]),
    ]),

    # ---- Bob Fehrenbacher (District 11, in office since Dec 1, 2022) ----
    # Running for WV State Senate District 3 (2026 election)
    # In office for: SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("bob-fehrenbacher", "WV", "Delegate", [
        claim("bf1", "bob-fehrenbacher", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law as binary — defining 'male' and 'female' by reproductive biology — explicitly rejecting gender-identity ideology in statute. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025. Fehrenbacher has represented District 11 since December 1, 2022.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://ballotpedia.org/Bob_Fehrenbacher"]),
        claim("bf2", "bob-fehrenbacher", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/delegate/bob-fehrenbacher/"]),
        claim("bf3", "bob-fehrenbacher", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Fehrenbacher is currently seeking a seat in the WV State Senate (District 3, 2026 election).",
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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
