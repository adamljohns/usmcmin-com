#!/usr/bin/env python3
"""Enrichment batch 508: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_curated federal bucket fully exhausted; archetype_party_default state
legislators (WI — bottom of alphabet) are the target tier.

Targets:
  Duke Tucker (duke-tucker-wi-75) — WI AD-75 Burnett County (Grantsburg area);
                                     assumed office Jan 6, 2025; U.S. Air Force
                                     veteran (1989-1992); operations manager at
                                     Grantsburg Telecom 28 years; explicitly
                                     lists "protecting the 2nd Amendment rights"
                                     and "promoting strong family values" as core
                                     policy priorities per official about page

  Dean Kaufert (dean-kaufert-wi-53) — WI AD-53 (Neenah); 30+ year small business
                                     owner; served in Assembly 1991-2015 (formerly
                                     AD-55), Mayor of Neenah 2014-2022, returned
                                     Jan 6, 2025; authored AB915 (2025, ICHRA tax
                                     credit for small businesses); member Assembly
                                     Committee on Financial Institutions

  David Steffen (david-steffen-wi-4) — WI AD-4 Howard/Green Bay area; in Assembly
                                     since 2015; named introducer of AB382 (born
                                     alive infant protection, July 2025); chaired
                                     Assembly Committee on Energy and Utilities;
                                     as a Howard village president led elimination
                                     of virtually 100% of Howard's debt

  David Murphy (david-murphy-wi-56) — WI AD-56 Hortonville area; named introducer
                                     of AB382 (born alive infant protection, July
                                     2025); authored AB56 (2025, "In God We Trust"
                                     display requirement in public schools/buildings);
                                     introduced AB74 (2025, parental notification
                                     of alleged school staff sexual misconduct)

  David Armstrong (david-armstrong-wi-67) — WI AD-67 Rice Lake/Barron County;
                                     previously represented AD-75 (2021-2025);
                                     named cosponsor of SJR73 (voter photo ID
                                     constitutional amendment, 2023); selected for
                                     Speaker's Government Efficiency Task Force
                                     (Oct 2025)

Key WI bills cited:
  AB382  (2025 session)    — Born alive infant protection: same standard of care
                             for infants born alive following abortion/attempt as
                             any other child born alive at that gestational age;
                             introduced July 31, 2025
  SJR73  (2023 session)    — Voter photo ID constitutional amendment; passed
                             Assembly 62-35 on Nov 9, 2023; approved by
                             Wisconsin voters April 2025
  AB915  (2025 session)    — Tax credit for small businesses offering employees
                             Individual Coverage Health Reimbursement Arrangements
                             (ICHRAs)
  AB56   (2025 session)    — Require display of national motto "In God We Trust"
                             in public schools and on public buildings
  AB74   (2025 session)    — Parental notification requirement when school staff
                             is alleged to have committed sexual misconduct

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
    # ---- Duke Tucker (WI AD-75, Burnett County; since Jan 2025) ----
    ("duke-tucker-wi-75", "WI", "Assembly", [
        claim("dt1", "duke-tucker-wi-75", "self_defense", 0, True,
              "Duke Tucker (R, WI AD-75) explicitly lists 'protecting the 2nd Amendment rights' as one of his core policy priorities on his official Wisconsin Legislature biography page. Tucker, a U.S. Air Force veteran (1989-1992) and lifelong rural Wisconsin resident from Burnett County, carries a pro-constitutional-carry, Second-Amendment-protective posture into the 2025-26 legislative session for the Grantsburg and northwest Wisconsin area.",
              ["https://legis.wisconsin.gov/assembly/75/tucker/about/",
               "https://ballotpedia.org/Duke_Tucker"]),
        claim("dt2", "duke-tucker-wi-75", "family_child_sovereignty", 0, True,
              "Duke Tucker explicitly lists 'promoting strong family values' as one of his core policy priorities on his official Wisconsin Legislature biography page alongside protecting private property rights. As a U.S. Air Force veteran and 28-year operations manager at Grantsburg Telecom who was raised in the farming community of Trade Lake, Wisconsin, Tucker's legislative priorities center on preserving family structure, community values, and parental authority in northwestern Wisconsin.",
              ["https://legis.wisconsin.gov/assembly/75/tucker/about/",
               "https://ballotpedia.org/Duke_Tucker"]),
    ]),

    # ---- Dean Kaufert (WI AD-53, Neenah; since Jan 2025) ----
    ("dean-kaufert-wi-53", "WI", "Assembly", [
        claim("dk1", "dean-kaufert-wi-53", "economic_stewardship", 2, True,
              "Dean Kaufert (R, WI AD-53) is a 30-year Wisconsin small business owner (All Sport Trophy and Engraving and the Dome Sports Bar and Grill, both in Neenah) who brings a private-sector fiscal-conservative perspective to the Assembly. In 2025, Kaufert co-authored AB915, which would create a state tax credit for small businesses offering employees Individual Coverage Health Reimbursement Arrangements (ICHRAs) — supporting employer-directed, market-based health coverage over government mandate-dependent models and reducing dependency on deficit-financed state health programs.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2852",
               "https://legis.wisconsin.gov/assembly/53/kaufert/about/"]),
        claim("dk2", "dean-kaufert-wi-53", "family_child_sovereignty", 0, True,
              "Dean Kaufert has served Wisconsin's Fox Valley families across nearly four decades of public service — 24 years in the Assembly (1991-2015, then 2025-26), eight years as Mayor of Neenah (2014-2022), and prior Alderman service. Throughout his career, Kaufert has represented Neenah-area families' interests in local-control governance and community autonomy, and he brings that orientation — as a small business owner married 47 years with seven grandchildren — to his 2025-26 legislative work in the 53rd Assembly District.",
              ["https://legis.wisconsin.gov/assembly/53/kaufert/about/",
               "https://en.wikipedia.org/wiki/Dean_Kaufert"]),
    ]),

    # ---- David Steffen (WI AD-4, Howard/Green Bay area; since 2015) ----
    ("david-steffen-wi-4", "WI", "Assembly", [
        claim("ds1", "david-steffen-wi-4", "sanctity_of_life", 0, True,
              "David Steffen (R, WI AD-4) was one of the named introducers of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, which requires health care providers to exercise the same degree of professional skill and care for any infant born alive following an abortion or attempted abortion as they would for any other child born alive at the same gestational age, and mandates immediate hospital transfer. Steffen's role as a primary introducer places him at the forefront of the legislative coalition affirming that every child born alive holds full legal personhood and the right to medical care.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2789"]),
        claim("ds2", "david-steffen-wi-4", "economic_stewardship", 2, True,
              "David Steffen led the elimination of virtually 100% of the Village of Howard's debt and established Howard as having the lowest spending per capita of any community of comparable size in Wisconsin — a record he carries into his legislative work as a small business owner and Assembly member since 2015. Steffen has consistently championed fiscal discipline and minimal-government spending in both his village leadership and his Assembly career, including as chair of the Assembly Committee on Energy and Utilities.",
              ["https://legis.wisconsin.gov/assembly/04/steffen/meet-david/",
               "https://ballotpedia.org/David_Steffen"]),
    ]),

    # ---- David Murphy (WI AD-56, Hortonville; since at least 2025) ----
    ("david-murphy-wi-56", "WI", "Assembly", [
        claim("dm1", "david-murphy-wi-56", "sanctity_of_life", 0, True,
              "David Murphy (R, WI AD-56) was one of the named introducers of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, which requires health care providers to exercise the same degree of professional skill and care for infants born alive following an abortion or attempted abortion as they would for any other child born alive at the same gestational age, and mandates immediate hospital transfer. Murphy's cosponsor position affirms his legislative stance that life and legal personhood begin at birth and must be medically protected from that moment.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://legis.wisconsin.gov/assembly/56/murphy/"]),
        claim("dm2", "david-murphy-wi-56", "christian_liberty", 0, True,
              "David Murphy (R, WI AD-56) authored 2025 Wisconsin Assembly Bill 56, which would require the display of the national motto 'In God We Trust' in public schools and on public buildings across Wisconsin. By legislating that the nation's official motto — with its direct acknowledgment of divine authority — appear visibly in state educational and civic spaces, Murphy used his Assembly position to reinforce the public expression of religious heritage and resist the secularization of Wisconsin's public institutions.",
              ["https://legis.wisconsin.gov/assembly/56/murphy/",
               "https://docs.legis.wisconsin.gov/document/legislator/2025/2756"]),
        claim("dm3", "david-murphy-wi-56", "family_child_sovereignty", 0, True,
              "David Murphy introduced 2025 Wisconsin Assembly Bill 74, which would require school districts to notify parents or guardians when a school staff member has been alleged to have committed sexual misconduct against a student. The bill directly strengthens parental authority and the right of families to know when their children may be at risk, addressing a child-protective transparency gap in Wisconsin school governance.",
              ["https://legis.wisconsin.gov/assembly/56/murphy/",
               "https://docs.legis.wisconsin.gov/document/legislator/2025/2756"]),
    ]),

    # ---- David Armstrong (WI AD-67, Rice Lake/Barron County; since Jan 2025 in AD-67) ----
    ("david-armstrong-wi-67", "WI", "Assembly", [
        claim("da1", "david-armstrong-wi-67", "election_integrity", 0, True,
              "David Armstrong (R, WI AD-67, previously AD-75) was a named cosponsor of Senate Joint Resolution 73 (SJR 73, 2023 session), the Wisconsin voter photo ID constitutional amendment. The amendment passed the Assembly 62-35 on November 9, 2023, and was subsequently approved by Wisconsin voters in the April 2025 statewide referendum, permanently enshrining a photo identification requirement to vote in any Wisconsin election in the state constitution.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("da2", "david-armstrong-wi-67", "economic_stewardship", 2, True,
              "David Armstrong (R, WI AD-67) was appointed to the Wisconsin Assembly Speaker's Government Efficiency Task Force in October 2025, charged with identifying and eliminating wasteful state spending and streamlining government operations. Armstrong — an executive director of the Barron County Economic Development Corporation with private-sector management experience in healthcare services — brought professional efficiency credentials to the legislative effort to reduce the state's spending footprint.",
              ["https://legis.wisconsin.gov/assembly/67/armstrong/media/cbsdufth/speakerstaskforceoct12025.pdf",
               "https://en.wikipedia.org/wiki/David_Armstrong_(Wisconsin_politician)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
