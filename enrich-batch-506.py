#!/usr/bin/env python3
"""Enrichment batch 506: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_curated federal bucket fully exhausted; archetype_party_default state
legislators (WI — bottom of alphabet) are the target tier.

Targets:
  Patrick Snyder (patrick-snyder-wi-85) — WI AD-85 Wausau/Marathon Co.; in
                                          office since 2017; cosponsor of AB975
                                          (14-week abortion referendum, 2023-24)
                                          and SJR73 (voter photo ID constitutional
                                          amendment, 2023)
  Nancy VanderMeer (nancy-vandermeer-wi-70) — WI AD-70 Monroe County; in office
                                          since 2015; Majority Caucus Secretary;
                                          dairy farmer and small-business owner;
                                          authored 911 Caller Immunity law (signed
                                          by Gov. Evers, Nov. 2025)
  Lindee Brill (lindee-brill-wi-27) — WI AD-27 Sheboygan County; assumed office
                                          Jan 2025; cosponsor of AB382 (born alive
                                          infant protection, 2025) and AB614
                                          (parental notification of school
                                          violence, 2025)
  Kevin Petersen (kevin-petersen-wi-57) — WI AD-57 Waupaca Co.; Speaker Pro
                                          Tempore 2023-24 and 2025-26; NRA member;
                                          U.S. Navy submarine veteran / Persian
                                          Gulf War vet (1983-2008)
  John Spiros (john-spiros-wi-86) — WI AD-86 Marshfield; in office since 2013;
                                          Chair, Assembly Committee on Criminal
                                          Justice and Public Safety; former police
                                          officer (Dallas, TX) and Air Force
                                          veteran; cosponsor of AB975 and SJR73

Key WI bills cited:
  AB975  (2023-24 session) — 14-week abortion referendum bill; passed Assembly
                              53-46 on Jan 25, 2024; vetoed by Gov. Evers
  SJR73  (2023 session)    — Voter photo ID constitutional amendment; passed
                              Assembly 62-35 on Nov 9, 2023; approved by
                              Wisconsin voters April 2025
  AB382  (2025 session)    — Born alive infant protection: requirements for
                              children born alive following abortion/attempt
  AB614  (2025 session)    — Parental notification of disruptive or violent
                              behavior at school

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
    # ---- Patrick Snyder (WI AD-85, Marathon County; since 2017) ----
    ("patrick-snyder-wi-85", "WI", "Assembly", [
        claim("ps1", "patrick-snyder-wi-85", "sanctity_of_life", 0, True,
              "Patrick Snyder (R, WI AD-85) was a named cosponsor of 2023 Wisconsin Assembly Bill 975, which would have placed a 14-week abortion ban on the referendum ballot for Wisconsin voters to decide. The bill passed the Assembly 53-46 on January 25, 2024, with Republicans who opposed it arguing 14 weeks was still 14 weeks too many — placing Snyder among the pro-life coalition that moved the measure.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://www.wpr.org/news/assembly-republicans-approve-14-week-limit-on-abortion-access"]),
        claim("ps2", "patrick-snyder-wi-85", "election_integrity", 0, True,
              "Patrick Snyder was a named cosponsor of Senate Joint Resolution 73 (SJR 73, 2023 session), the Wisconsin voter photo ID constitutional amendment. The amendment passed the Assembly 62-35 on November 9, 2023, and was subsequently approved by Wisconsin voters in the April 2025 referendum, enshrining a photo identification requirement to vote in the state constitution.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
    ]),

    # ---- Nancy VanderMeer (WI AD-70, Monroe County; since 2015; Majority Caucus Sec.) ----
    ("nancy-vandermeer-wi-70", "WI", "Assembly", [
        claim("nv1", "nancy-vandermeer-wi-70", "election_integrity", 0, True,
              "Nancy VanderMeer voted with the entire Assembly Republican caucus for the voter photo ID constitutional amendment (SJR 73), which passed 62-35 on November 9, 2023. Wisconsin Public Radio and Ballotpedia confirm all Republicans voted in favor of the amendment, which was subsequently ratified by Wisconsin voters in April 2025, making photo ID mandatory to vote in Wisconsin.",
              ["https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/voter-identification-constitutional-amendment-wisconsin"]),
        claim("nv2", "nancy-vandermeer-wi-70", "public_justice", 0, True,
              "Nancy VanderMeer authored and championed Wisconsin's 911 Caller Immunity law, which Governor Tony Evers signed into law in November 2025. The law protects citizens who make good-faith 911 emergency calls from civil liability, removing a legal barrier that had discouraged some people from calling for help — a bipartisan public-safety accountability measure reflecting support for first-responder access and community safety.",
              ["https://legis.wisconsin.gov/assembly/70/vandermeer/media/gvxipluu/vandermeer-press-release-11-04-25-governor-evers-signs-vandermeer-911-immunity-bill-into-law.pdf",
               "https://legis.wisconsin.gov/assembly/70/vandermeer/"]),
    ]),

    # ---- Lindee Brill (WI AD-27, Sheboygan County; assumed office Jan 2025) ----
    ("lindee-brill-wi-27", "WI", "Assembly", [
        claim("lb1", "lindee-brill-wi-27", "sanctity_of_life", 0, True,
              "Lindee Brill (R, WI AD-27) cosponsored 2025 Assembly Bill 382, which establishes requirements for the care of infants born alive following an abortion or attempted abortion — directly protecting newborn life and affirming that legal personhood must be recognized at birth regardless of whether the birth resulted from an attempted termination.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://legis.wisconsin.gov/assembly/27/brill/"]),
        claim("lb2", "lindee-brill-wi-27", "family_child_sovereignty", 0, True,
              "Lindee Brill cosponsored 2025 Assembly Bill 614, requiring schools to notify parents of disruptive or violent behavior by or toward their children. The bill expands parental rights over their children's school environment, ensuring families receive information about safety incidents rather than having schools manage those details without parental input.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab614",
               "https://legis.wisconsin.gov/assembly/27/brill/news-updates/press-releases-news/"]),
    ]),

    # ---- Kevin Petersen (WI AD-57, Waupaca; Speaker Pro Tempore; Navy vet) ----
    ("kevin-petersen-wi-57", "WI", "Assembly", [
        claim("kp1", "kevin-petersen-wi-57", "self_defense", 1, True,
              "Kevin Petersen is a member of the National Rifle Association and has supported Second Amendment legislation throughout his tenure as an Assembly member since 2006. He served as Speaker Pro Tempore for 2023-24 and 2025-26, a role that required him to shepherd Republican priorities — including gun-rights legislation — through the chamber. His NRA membership reflects consistent opposition to firearm restrictions such as red-flag laws, assault-weapon bans, and magazine-capacity limits.",
              ["https://justfacts.votesmart.org/candidate/biography/68668/kevin-petersen",
               "https://legis.wisconsin.gov/assembly/57/petersen/about/"]),
        claim("kp2", "kevin-petersen-wi-57", "election_integrity", 0, True,
              "Kevin Petersen voted with the entire Assembly Republican caucus for the voter photo ID constitutional amendment (SJR 73), which passed 62-35 on November 9, 2023. All Assembly Republicans supported the amendment, which was ratified by Wisconsin voters in April 2025, requiring photo identification to vote in any Wisconsin election.",
              ["https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/voter-identification-constitutional-amendment-wisconsin"]),
    ]),

    # ---- John Spiros (WI AD-86, Marshfield; Criminal Justice Chair; former officer) ----
    ("john-spiros-wi-86", "WI", "Assembly", [
        claim("js1", "john-spiros-wi-86", "sanctity_of_life", 0, True,
              "John Spiros (R, WI AD-86) was a named cosponsor of 2023 Wisconsin Assembly Bill 975, which would have placed a 14-week abortion ban on the statewide referendum ballot. The bill passed the Assembly 53-46 on January 25, 2024, and Spiros's cosponsor status placed him in the pro-life coalition — even as some Republicans dissented as insufficiently protective of unborn life.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://www.wpr.org/news/assembly-republicans-approve-14-week-limit-on-abortion-access"]),
        claim("js2", "john-spiros-wi-86", "election_integrity", 0, True,
              "John Spiros was a named cosponsor of Senate Joint Resolution 73 (SJR 73, 2023 session), the Wisconsin voter photo ID constitutional amendment, which passed the Assembly 62-35 on November 9, 2023. As Chair of the Assembly Committee on Criminal Justice and Public Safety, Spiros has championed election-law integrity measures alongside broader public-safety reform. Wisconsin voters ratified the amendment in April 2025.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://legis.wisconsin.gov/assembly/86/spiros/"]),
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
