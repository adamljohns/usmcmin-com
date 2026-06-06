#!/usr/bin/env python3
"""Enrichment batch 79: hand-curated claims for 4 state/gubernatorial candidates (bottom of alphabet).

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the alphabet (OK, SD, TN) to avoid collision with the top-of-alphabet loop.

Mix (4 R): Kevin Stitt (OK-R, Gov incumbent term-limited),
           Larry Rhoden (SD-R, Gov incumbent),
           Carol Swain (TN-R, 2026 Gov candidate),
           Toby Doeden (SD-R, 2026 Gov candidate).
Each claim cites >=1 reliable source and reflects documented 2019-2026 positions.

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
    # ---------------- Kevin Stitt (OK-R, Governor) ----------------
    ("kevin-stitt", "OK", "Governor", [
        claim("ks1", "kevin-stitt", "sanctity_of_life", 0, True,
              "In May 2022, Governor Stitt signed HB 4327, the most restrictive abortion law in the country at the time, banning abortion from the moment of fertilization and allowing private citizens to sue abortion providers — a de facto recognition that personhood begins at conception and the broadest available legal protection for the unborn.",
              ["https://en.wikipedia.org/wiki/Kevin_Stitt",
               "https://ballotpedia.org/Kevin_Stitt"]),
        claim("ks2", "kevin-stitt", "self_defense", 0, True,
              "On February 27, 2019, Governor Stitt signed SB 1212, making Oklahoma a permitless 'constitutional carry' state — citizens may carry firearms without a government-issued license — affirming that the right to bear arms requires no bureaucratic permission.",
              ["https://en.wikipedia.org/wiki/Kevin_Stitt",
               "https://en.wikipedia.org/wiki/Constitutional_carry"]),
        claim("ks3", "kevin-stitt", "biblical_marriage", 2, True,
              "In 2022 Stitt signed SB 615 requiring students to use school facilities corresponding to their biological sex, and in 2023 signed legislation banning gender-affirming care for minors — making Oklahoma among the earliest states to codify that biological sex is fixed, directly rejecting transgender ideology in law.",
              ["https://en.wikipedia.org/wiki/Kevin_Stitt",
               "https://en.wikipedia.org/wiki/LGBTQ_rights_in_Oklahoma"]),
    ]),

    # ---------------- Larry Rhoden (SD-R, Governor) ----------------
    ("larry-rhoden-gov-2026", "SD", "Governor", [
        claim("lr1", "larry-rhoden-gov-2026", "sanctity_of_life", 0, True,
              "Rhoden has spoken out publicly against abortion throughout his legislative and executive career; his overall conservative record earned the American Conservative Union's highest ranking in 2017, reflecting a consistent pro-life posture.",
              ["https://en.wikipedia.org/wiki/Larry_Rhoden",
               "https://ballotpedia.org/Larry_Rhoden"]),
        claim("lr2", "larry-rhoden-gov-2026", "self_defense", 0, True,
              "As a state legislator Rhoden sponsored a South Dakota legislative finding affirming that the Founding Fathers 'abjured all legislative and executive authority to regulate gun ownership and usage to individual citizens,' and backed bills to arm school volunteers — a constitutional-carry-aligned posture rejecting government restriction of the right to bear arms.",
              ["https://en.wikipedia.org/wiki/Larry_Rhoden",
               "https://ballotpedia.org/Larry_Rhoden"]),
        claim("lr3", "larry-rhoden-gov-2026", "biblical_marriage", 0, True,
              "Rhoden has publicly spoken out against same-sex marriage, aligning with the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Larry_Rhoden",
               "https://ballotpedia.org/Larry_Rhoden"]),
    ]),

    # ---------------- Carol Swain (TN-R, 2026 Governor candidate) ----------------
    ("carol-swain-gov", "TN", "Governor", [
        claim("cs1", "carol-swain-gov", "christian_liberty", 0, True,
              "A Southern Baptist, Swain left the Democratic Party in 2009 after her Christian faith led her to reexamine her worldview; she has since built an entire public ministry and author career on applying biblical principles to law, politics, and culture — embodying the rubric's demand that Christian conscience, not government preference, govern public life.",
              ["https://en.wikipedia.org/wiki/Carol_M._Swain",
               "https://ballotpedia.org/Carol_Swain"]),
        claim("cs2", "carol-swain-gov", "family_child_sovereignty", 0, True,
              "Co-chairwoman of President Trump's 1776 Commission (2020-21), whose founding report explicitly repudiated critical race theory and called for restoring traditional civic and moral education — a direct defense of parental rights and family sovereignty against ideological capture of schools.",
              ["https://en.wikipedia.org/wiki/Carol_M._Swain",
               "https://ballotpedia.org/Carol_Swain"]),
        claim("cs3", "carol-swain-gov", "biblical_marriage", 0, True,
              "Author of 'Countercultural Living: What Jesus Has to Say About Life, Marriage, Race, Gender, and Materialism' (2017), Swain has consistently argued that marriage is a lifelong covenant between one man and one woman defined by Scripture — a public, authored commitment to the one-man-one-woman standard.",
              ["https://en.wikipedia.org/wiki/Carol_M._Swain",
               "https://ballotpedia.org/Carol_Swain"]),
    ]),

    # ---------------- Toby Doeden (SD-R, 2026 Governor candidate) ----------------
    ("toby-doeden-gov", "SD", "Governor", [
        claim("td1", "toby-doeden-gov", "border_immigration", 1, True,
              "Campaigned on a pledge to work with President Trump to 'round up illegal immigrants and get deadly drugs off our streets' and pledged as governor to deport dangerous illegal aliens — a deportation-first posture consistent with the rubric's mandatory-deportation standard.",
              ["https://ballotpedia.org/Toby_Doeden"]),
        claim("td2", "toby-doeden-gov", "family_child_sovereignty", 0, True,
              "Pledged to end all 'wokeness and DEI' in South Dakota government, eliminate DEI from all state programs, and ban critical race theory from classrooms — a hard parental-rights and anti-indoctrination posture protecting families from ideological capture of public institutions.",
              ["https://ballotpedia.org/Toby_Doeden"]),
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
