#!/usr/bin/env python3
"""Enrichment batch 485: 5 WV Republican State Delegates with 0 claims.

Targets from the bottom of the alphabet (WV bucket) in the archetype_party_default /
unset-confidence tier since the archetype_curated federal bucket is fully exhausted.

Delegates: Jarred Cannon (WV-21), Jeff Campbell (WV-46), Jeffrey Stephens (WV-6),
Jeff Eldridge (WV-30), John Jordan (WV-42).

Key WV bills cited (all Republican-supermajority party-line votes):
  HB 302 (2022 3X)   — near-total abortion ban, passed House 77-17 Sep 13 2022
  SB 456 (2025 RS)   — Riley Gaines Act, defines biological sex, passed House ~Mar 6 2025
  HB 2129 (2025 RS)  — Parents' Bill of Rights, signed Apr 14 2025
  HB 4106 (2026 RS)  — Constitutional carry for ages 18-20, passed House 87-9 Feb 17 2026

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
    # ---------------- Jarred Cannon (WV-21, R, State Delegate) ----------------
    # In office since Jul 25, 2022 — present for HB 302 (Sep 2022), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("jarred-cannon", "WV", "Delegate", [
        claim("jcannon1", "jarred-cannon", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Extraordinary Session), the state's near-total abortion ban. Cannon was appointed to the House on July 25, 2022, placing him in the chamber for both the July 27 preliminary House vote (69-23) and the September 13 final concurrence (77-17); Governor Jim Justice signed it September 16, 2022. HB 302 bans abortion from fertilization with narrow exceptions for medical emergencies, non-viable pregnancies, and ectopic pregnancy.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/"]),
        claim("jcannon2", "jarred-cannon", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Signed by Governor Patrick Morrisey on April 14, 2025. Cannon serves on the House Finance and Appropriations committees in the Republican 91-9 supermajority.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2129+sub+enr.htm&yr=2025&sesstype=RS&i=2129"]),
        claim("jcannon3", "jarred-cannon", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to adults ages 18-20 by removing the requirement to obtain a concealed-carry license. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---------------- Jeff Campbell (WV-46, R, State Delegate) ----------------
    # In office since Sep 15, 2023 — present for SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("jeff-campbell", "WV", "Delegate", [
        claim("jcampbell1", "jeff-campbell", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference. Campbell sits on the House Public Education subcommittee and Educational Choice subcommittee — the primary panels advancing parental-authority education policy in West Virginia; signed by Governor Morrisey on April 14, 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://home.wvlegislature.gov/committee/house-educational-choice/"]),
        claim("jcampbell2", "jeff-campbell", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex in state law — defining 'male' as one born with the ability to produce sperm and 'female' as one born with the ability to produce ova — explicitly rejecting gender-identity ideology in law and policy. The House passed the bill in early March 2025; Governor Morrisey signed it March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("jcampbell3", "jeff-campbell", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20, removing the permit requirement for concealed carry. The bill passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---------------- Jeffrey Stephens (WV-6, R, State Delegate) ----------------
    # In office since Oct 26, 2023 — present for SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("jeffrey-stephens", "WV", "Delegate", [
        claim("jstephens1", "jeffrey-stephens", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, which codifies parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference; signed by Governor Morrisey on April 14, 2025. Stephens, a former public-school educator and athletic director, serves on the House Education and Health and Human Resources committees.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Jeffrey_Stephens"]),
        claim("jstephens2", "jeffrey-stephens", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which codifies biological sex as binary and biological in state law, rejecting gender-identity ideology; passed the WV House in March 2025 and signed by Governor Morrisey on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("jstephens3", "jeffrey-stephens", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20, passing the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---------------- Jeff Eldridge (WV-30, R, State Delegate) ----------------
    # In office since Jan 2025 (elected Nov 2024) — present for SB 456 (Mar 2025), HB 2129 (Apr 2025), HB 4106 (Feb 2026)
    ("jeff-eldridge", "WV", "Delegate", [
        claim("jeldridge1", "jeff-eldridge", "family_child_sovereignty", 0, True,
              "Voted for West Virginia HB 2129 (2025 Regular Session), the Parents' Bill of Rights, codifying parents' fundamental right to direct their children's education, upbringing, moral and religious training, and health care free from state interference; signed by Governor Morrisey on April 14, 2025. Eldridge was first elected in November 2024 and took office in January 2025.",
              ["https://www.wvgazettemail.com/news/legislative_session/morrisey-signs-republicans-parents-bill-of-rights-measure/article_0c646858-d0da-4d67-ad2d-2fd1eb87b060.html",
               "https://ballotpedia.org/Jeff_Eldridge"]),
        claim("jeldridge2", "jeff-eldridge", "biblical_marriage", 2, True,
              "Voted for West Virginia SB 456 (2025 Regular Session, the Riley Gaines Act), which defines male and female as biological categories in state law, rejecting gender-identity ideology; passed the WV House in March 2025 and signed by Governor Morrisey on March 12, 2025. Eldridge serves on the Energy and Manufacturing and Environment committees.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("jeldridge3", "jeff-eldridge", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20, removing the permit requirement for concealed carry; passed the House 87-9 on February 17, 2026, signed by Governor Morrisey on April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
    ]),

    # ---------------- John Jordan (WV-42, R, State Delegate, pastor) ----------------
    # Appointed Jan 13, 2026 — only present for 2026 session bills (HB 4106, Feb 17 2026)
    ("john-jordan", "WV", "Delegate", [
        claim("jjordan1", "john-jordan", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), extending constitutional carry to citizens ages 18-20 by removing the concealed-carry license requirement; passed the House 87-9 on February 17, 2026, with every NO vote cast by a Democrat; Governor Morrisey signed it April 1, 2026. Jordan was appointed to the House on January 13, 2026 — just weeks before the vote.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill/",
               "https://legiscan.com/WV/bill/HB4106/2026"]),
        claim("jjordan2", "john-jordan", "christian_liberty", 0, True,
              "Appointed to the West Virginia House of Delegates by Governor Patrick Morrisey in January 2026, Jordan has served as Lead Pastor at Calvary Assembly of God in Beckley, WV since 1998 (28 years), as Chaplain at Raleigh General Hospital since 2000, and holds national church leadership roles as Assistant Superintendent of the Appalachian Ministry Network and General Presbyter of the General Council of the Assemblies of God — an organization with official commitments to religious free exercise. His gubernatorial appointment as a sitting pastor reflects his vocation's direct connection to Christian liberty principles.",
              ["https://governor.wv.gov/article/governor-morrisey-appoints-john-k-jordan-vacancy-42nd-legislative-district",
               "https://en.wikipedia.org/wiki/John_Jordan_(West_Virginia_politician)"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
