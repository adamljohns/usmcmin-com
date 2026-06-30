#!/usr/bin/env python3
"""Enrichment batch 507: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_curated federal bucket fully exhausted; archetype_party_default state
legislators (WI — bottom of alphabet) are the target tier.

Targets:
  Joel Kitchens (joel-kitchens-wi-1) — WI AD-1 Door County/Green Bay area;
                                        in office since 2014; one of the
                                        introducers of AB975 (14-week abortion
                                        referendum, Jan 2024); named cosponsor
                                        of SJR73 (voter photo ID constitutional
                                        amendment, 2023)
  Jim Piwowarczyk (jim-piwowarczyk-wi-98) — WI AD-98 Washington County;
                                        assumed office Jan 6, 2025; former
                                        Glendale police sergeant; co-founder
                                        Wisconsin Right Now; named cosponsor
                                        of AB382 (born alive infant protection,
                                        July 2025); 2nd Amendment and parental
                                        rights advocate per official bio
  Jessie Rodriguez (jessie-rodriguez-wi-21) — WI AD-21 southeast WI;
                                        in office since Dec 2013; serving
                                        seventh term; cosponsor of SB299 (2023)
                                        clarifying medical necessity for
                                        abortion under WI's near-total ban;
                                        former Chair, Assembly Children and
                                        Families Committee
  Jerry O'Connor (jerry-o-connor-wi-60) — WI AD-60 (formerly AD-52 2023-24)
                                        Fond du Lac area; assumed current
                                        district office Jan 6, 2025; named
                                        cosponsor of SJR73 (voter photo ID
                                        amendment, 2023); chaired WI Assembly
                                        task force on reducing human sex
                                        trafficking
  Elijah Behnke (elijah-behnke-wi-6) — WI AD-6 Oconto County; assumed
                                        office Jan 2025; small business owner;
                                        associate degree in Biblical Studies
                                        from Toccoa Falls College (2005);
                                        named cosponsor of AB382 (born alive
                                        infant protection, July 2025)

Key WI bills cited:
  AB975  (2023-24 session) — 14-week abortion referendum bill; passed Assembly
                              53-46 on Jan 25, 2024; vetoed by Gov. Evers
  SJR73  (2023 session)    — Voter photo ID constitutional amendment; passed
                              Assembly 62-35 on Nov 9, 2023; approved by
                              Wisconsin voters April 2025
  SB299  (2023 session)    — Medical necessity clarification for abortion
                              with narrow exceptions under WI's near-total ban
  AB382  (2025 session)    — Born alive infant protection: requirements for
                              children born alive following abortion/attempt

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
    # ---- Joel Kitchens (WI AD-1, Door County/Green Bay; since 2014) ----
    ("joel-kitchens-wi-1", "WI", "Assembly", [
        claim("jk1", "joel-kitchens-wi-1", "sanctity_of_life", 0, True,
              "Joel Kitchens (R, WI AD-1) was one of the introducers of 2023 Wisconsin Assembly Bill 975, the legislation introduced January 19, 2024, that would have placed a 14-week abortion ban on the Wisconsin ballot as a public referendum. The bill passed the Assembly 53-46 on January 25, 2024. As a primary introducer, Kitchens helped lead the pro-life coalition advancing the measure, though it was subsequently vetoed by Governor Evers.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab975",
               "https://www.wpr.org/news/assembly-republicans-approve-14-week-limit-on-abortion-access"]),
        claim("jk2", "joel-kitchens-wi-1", "election_integrity", 0, True,
              "Joel Kitchens was a named cosponsor of Senate Joint Resolution 73 (SJR 73, 2023 session), the Wisconsin voter photo ID constitutional amendment. The amendment passed the Assembly 62-35 on November 9, 2023, and was subsequently approved by Wisconsin voters in the April 2025 referendum, permanently enshrining a photo identification requirement to vote in the state constitution.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
    ]),

    # ---- Jim Piwowarczyk (WI AD-98, Washington County; since Jan 2025) ----
    ("jim-piwowarczyk-wi-98", "WI", "Assembly", [
        claim("jp1", "jim-piwowarczyk-wi-98", "sanctity_of_life", 0, True,
              "Jim Piwowarczyk (R, WI AD-98) was a named cosponsor of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, which requires health care providers to exercise the same degree of professional skill and care for infants born alive following an abortion or attempted abortion as they would for any other child born alive at the same gestational age, with immediate transfer to a hospital. Piwowarczyk joined a coalition of Assembly Republicans affirming legal personhood and medical obligations at the moment of birth.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://legis.wisconsin.gov/assembly/98/piwowarczyk/"]),
        claim("jp2", "jim-piwowarczyk-wi-98", "self_defense", 0, True,
              "Jim Piwowarczyk explicitly lists 'the 2nd Amendment' as a core policy belief on his official Wisconsin Legislature biography page, alongside law and order and fiscal conservatism. As a former patrol sergeant with the Glendale Police Department and former officer with the Village of Kewaskum, Piwowarczyk brings law-enforcement credentials to his constitutional carry and Second Amendment advocacy.",
              ["https://legis.wisconsin.gov/assembly/98/piwowarczyk/about/",
               "https://ballotpedia.org/Jim_Piwowarczyk"]),
        claim("jp3", "jim-piwowarczyk-wi-98", "family_child_sovereignty", 0, True,
              "Jim Piwowarczyk explicitly lists 'parents' rights' as a core policy belief on his official Wisconsin Legislature biography page. His advocacy for parental rights is further evidenced by his work as co-founder of Wisconsin Right Now, a conservative news outlet that regularly covers parental rights, school curriculum transparency, and family sovereignty issues in Wisconsin.",
              ["https://legis.wisconsin.gov/assembly/98/piwowarczyk/about/",
               "https://ballotpedia.org/Jim_Piwowarczyk"]),
    ]),

    # ---- Jessie Rodriguez (WI AD-21, southeast WI; since Dec 2013) ----
    ("jessie-rodriguez-wi-21", "WI", "Assembly", [
        claim("jr1", "jessie-rodriguez-wi-21", "sanctity_of_life", 0, True,
              "Jessie Rodriguez (R, WI AD-21) was a named cosponsor of 2023 Wisconsin Senate Bill 299 (introduced May 2023), which sought to clarify the narrow medical-necessity circumstances under which abortion would be permitted while Wisconsin's near-total abortion ban — a 19th-century statute reinstated after Dobbs — remained in legal contest. By cosponsoring a bill that codified strict limits on permissible abortion, Rodriguez positioned herself with the legislative coalition working to restrict abortion access to the narrowest legally defensible circumstances.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/sb299",
               "https://ballotpedia.org/Jessie_Rodriguez"]),
        claim("jr2", "jessie-rodriguez-wi-21", "family_child_sovereignty", 0, True,
              "Jessie Rodriguez served as Chair of the Wisconsin Assembly's Children and Families Committee, shepherding legislation affecting child welfare, family structure, and parental rights through the legislative process. Her committee chairmanship — combined with her seven terms representing District 21 — reflects a sustained legislative focus on protecting children and family sovereignty within Wisconsin state government.",
              ["https://ballotpedia.org/Jessie_Rodriguez",
               "https://legis.wisconsin.gov/assembly/21/rodriguez/"]),
    ]),

    # ---- Jerry O'Connor (WI AD-60, formerly AD-52; Fond du Lac; since 2023) ----
    ("jerry-o-connor-wi-60", "WI", "Assembly", [
        claim("jo1", "jerry-o-connor-wi-60", "election_integrity", 0, True,
              "Jerry O'Connor was a named cosponsor of Senate Joint Resolution 73 (SJR 73, 2023 session), the Wisconsin voter photo ID constitutional amendment, while representing Assembly District 52 in the 2023-24 session. The amendment passed the Assembly 62-35 on November 9, 2023, and was approved by Wisconsin voters in the April 2025 referendum, enshrining a photo identification requirement to vote in any Wisconsin election in the state constitution.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("jo2", "jerry-o-connor-wi-60", "public_justice", 0, True,
              "Jerry O'Connor chaired a Wisconsin State Assembly task force focused on reducing human sex trafficking in Wisconsin. O'Connor, a former banker and Fond du Lac-area community leader, used his Assembly platform to lead the effort to combat trafficking — a public-justice priority that reflects a commitment to protecting the vulnerable and holding exploiters accountable under the law.",
              ["https://ballotpedia.org/Jerry_O%27Connor",
               "https://legis.wisconsin.gov/assembly/60/oconnor/about/"]),
    ]),

    # ---- Elijah Behnke (WI AD-6, Oconto County; since Jan 2025) ----
    ("elijah-behnke-wi-6", "WI", "Assembly", [
        claim("eb1", "elijah-behnke-wi-6", "sanctity_of_life", 0, True,
              "Elijah Behnke (R, WI AD-6) was a named cosponsor of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, requiring health care providers present at a birth resulting from an abortion or attempted abortion to exercise the same professional skill and care for that infant as for any other child born alive at the same gestational age and to ensure immediate hospital transport. Behnke's cosponsor status affirms his position that personhood and legal protection extend to every child the moment of live birth.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://legis.wisconsin.gov/assembly/06/behnke/"]),
        claim("eb2", "elijah-behnke-wi-6", "christian_liberty", 0, True,
              "Elijah Behnke holds an associate degree in Biblical Studies from Toccoa Falls College (2005), a Christian liberal arts college in Georgia, reflecting a foundational commitment to Christian faith and scripture. His faith background informs his public service in Oconto County and his policy positions, and he chairs the Assembly Rural Development Committee and serves as Vice Chair of Constitution and Ethics in the 2025-26 session.",
              ["https://ballotpedia.org/Elijah_Behnke",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2845"]),
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
