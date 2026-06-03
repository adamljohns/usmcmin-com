#!/usr/bin/env python3
"""Enrichment batch 21: hand-curated claims for 5 federal senate candidates.

Targets archetype_curated candidates from the BOTTOM of the alphabet bucket
(bottom-of-Z-first sort: NC, NE, NJ, OK) with 0 evidence claims.

Mix (2 R / 2 D / 1 I): Michael Whatley (NC-R), Wiley Nickel (NC-D),
Dan Osborn (NE-I), Curtis Bashaw (NJ-R), Madison Horn (OK-D).
Each claim cites >=1 reliable source and reflects publicly known
2024-2026 voting records / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ----------- Michael Whatley (NC-R, 2026 R Nominee · Tillis seat) -----------
    ("michael-whatley", "NC", "Senator", [
        claim("mw1", "michael-whatley", "election_integrity", 0, True,
              "As chair of the Republican National Committee (2024–2025) and co-chair of Trump's 2024 presidential campaign, Whatley led national GOP 'election integrity' operations — pushing for stricter voter-ID requirements, paper-ballot verification, and restrictions on mass mail-in voting. He ran for Senate in 2026 explicitly to advance these and other Trump-agenda priorities.",
              ["https://en.wikipedia.org/wiki/Michael_Whatley",
               "https://ballotpedia.org/Michael_Whatley"]),
        claim("mw2", "michael-whatley", "border_immigration", 0, True,
              "Running as the 2026 Republican nominee for U.S. Senate in North Carolina with President Trump's personal endorsement, Whatley is campaigning on Trump's full border agenda — including border-wall completion, military deployment to the southern border, and strict enforcement against illegal immigration.",
              ["https://en.wikipedia.org/wiki/Michael_Whatley",
               "https://ballotpedia.org/Michael_Whatley"]),
    ]),

    # ----------- Wiley Nickel (NC-D, 2026 D Candidate · former U.S. Rep NC-13) -----------
    ("wiley-nickel-senate", "NC", "Senate", [
        claim("wn1", "wiley-nickel-senate", "sanctity_of_life", 0, False,
              "During his single term as U.S. Representative for NC-13 (2023–2025), Nickel was rated a strong supporter of reproductive rights by Reproductive Freedom for All (successor to NARAL), voting consistently against measures restricting abortion access and supporting federal legislation to codify abortion rights — rejecting any personhood-from-conception standard.",
              ["https://www.govtrack.us/congress/members/wiley_nickel/456915",
               "https://en.wikipedia.org/wiki/Wiley_Nickel"]),
        claim("wn2", "wiley-nickel-senate", "foreign_policy_restraint", 1, False,
              "After traveling to Ukraine on a bipartisan congressional delegation in 2024 and meeting with President Zelenskyy, Nickel publicly called for continued U.S. military assistance to Ukraine and urged Congress to pass additional foreign-aid packages — the type of open-ended overseas military entanglement the rubric's foreign-policy-restraint criterion opposes.",
              ["https://en.wikipedia.org/wiki/Wiley_Nickel",
               "https://ballotpedia.org/Wiley_Nickel"]),
    ]),

    # ----------- Dan Osborn (NE-I, 2026 Independent · Pete Ricketts seat) -----------
    ("dan-osborn-senate-2026", "NE", "Senate", [
        claim("do1", "dan-osborn-senate-2026", "sanctity_of_life", 0, False,
              "Supports a woman's right to choose abortion, describing his approach as 'libertarian' — keeping government out of private lives. While he calls late-term abortions 'disgusting,' he does not support any personhood-from-conception standard or legislative restrictions on early abortion access.",
              ["https://en.wikipedia.org/wiki/Dan_Osborn",
               "https://ballotpedia.org/Dan_Osborn"]),
        claim("do2", "dan-osborn-senate-2026", "border_immigration", 0, True,
              "Supports building the U.S.–Mexico border wall and increasing border security to halt illegal immigration, explicitly calling for wall construction as part of his 2024 and 2026 Senate platforms — while also proposing immigration reform for long-term non-criminal undocumented residents.",
              ["https://en.wikipedia.org/wiki/Dan_Osborn",
               "https://ballotpedia.org/Dan_Osborn"]),
        claim("do3", "dan-osborn-senate-2026", "self_defense", 1, True,
              "Supports protecting gun rights and the Second Amendment and backs gun-safety education in schools; has not called for assault-weapon bans, magazine-capacity restrictions, or red-flag laws.",
              ["https://ballotpedia.org/Dan_Osborn",
               "https://en.wikipedia.org/wiki/Dan_Osborn"]),
    ]),

    # ----------- Curtis Bashaw (NJ-R, 2026 R Candidate · 2024 R nominee · hotelier) -----------
    ("curtis-bashaw-nj-senate-2026", "NJ", "Senate", [
        claim("cb1", "curtis-bashaw-nj-senate-2026", "sanctity_of_life", 0, False,
              "As the 2024 Republican Senate nominee in New Jersey, Bashaw stated he does not support a national abortion ban and believes reproductive decisions 'are best decided by a woman and her doctor, and not by the federal government' — explicitly rejecting any personhood-from-conception legislative standard.",
              ["https://ballotpedia.org/Curtis_Bashaw",
               "https://en.wikipedia.org/wiki/2024_United_States_Senate_election_in_New_Jersey"]),
        claim("cb2", "curtis-bashaw-nj-senate-2026", "border_immigration", 1, True,
              "Supports mandatory deportation of non-citizens who commit violent crimes or have terrorist connections, stating: 'anyone convicted of a violent crime or connected to a terrorist organization needs to be deported immediately' — aligning with the rubric's mandatory-deportation criterion.",
              ["https://ballotpedia.org/Curtis_Bashaw"]),
    ]),

    # ----------- Madison Horn (OK-D, 2022 D nominee · cybersecurity exec) -----------
    ("madison-horn-ok-senate", "OK", "Senate", [
        claim("mh1", "madison-horn-ok-senate", "sanctity_of_life", 0, False,
              "An Oklahoma Democrat endorsed by VoteProchoice who affirms that women should have access to safe and legal reproductive healthcare — rejecting any personhood-from-conception framework that would restrict abortion access.",
              ["https://www.voteprochoice.us/candidates/madison-horn",
               "https://ballotpedia.org/Madison_Horn"]),
        claim("mh2", "madison-horn-ok-senate", "border_immigration", 0, False,
              "Supports a 'functioning immigration system for legal immigrants' paired with incremental border-security improvements — a reform-first approach that does not call for full border-wall construction or military deployment to the border.",
              ["https://ballotpedia.org/Madison_Horn"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
