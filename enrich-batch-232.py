#!/usr/bin/env python3
"""Enrichment batch 232: third-claim enrichment for 5 federal Senate candidates.

Targets evidence_curated U.S. Senate candidates (2 claims each) from the
bottom of the alphabet: NH, MN, MI, KY (R), KY (D).  Each claim adds a
distinct rubric category not already covered by the candidate's prior two
claims.

Candidates: Chris Pappas (NH-D), Angie Craig (MN-D), Haley Stevens (MI-D),
Mike Faris (KY-R), Amy McGrath (KY-D).
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


TARGETS = [
    # ---------- Chris Pappas (NH-D, U.S. Senate 2026) ----------
    ("chris-pappas", "NH", "Senate", [
        claim("cp3", "chris-pappas", "biblical_marriage", 0, False,
              "New Hampshire's first openly gay member of Congress who personally led the Respect for Marriage Act through the House — the 2022 law that repealed DOMA and codified federal recognition of same-sex marriage — and re-introduced the Equality Act to extend LGBTQ anti-discrimination protections into schools and public accommodations; co-chairs the Congressional LGBTQ+ Equality Caucus, making marriage-equality advocacy a defining feature of his legislative identity and rejecting the one-man-one-woman standard the rubric requires.",
              ["https://pappas.house.gov/media/press-releases/pappas-leads-house-in-passing-respect-for-marriage-act",
               "https://pappas.house.gov/media/press-releases/pappas-helps-re-introduce-landmark-equality-act-1"]),
    ]),

    # ---------- Angie Craig (MN-D, U.S. Senate 2026) ----------
    ("angie-craig", "MN", "Senate", [
        claim("ac3", "angie-craig", "biblical_marriage", 4, False,
              "First openly lesbian mother to serve in Congress and co-chair of the Congressional LGBTQ+ Equality Caucus; voted for the Equality Act — which writes sexual-orientation and gender-identity protections into federal civil-rights law extending to schools, public accommodations, and federal programs — and declared 'no government, and certainly no politician, should be able to dictate what my marriage or family looks like' upon voting for the Respect for Marriage Act, making LGBTQ promotion in schools and policy a core legislative priority and directly opposing the rubric's standard.",
              ["https://craig.house.gov/media/press-releases/representative-angie-craig-statement-house-passage-equality-act",
               "https://craig.house.gov/media/press-releases/representative-angie-craig-votes-pass-respect-marriage-act"]),
    ]),

    # ---------- Haley Stevens (MI-D, U.S. Senate 2026) ----------
    ("haley-stevens", "MI", "Senate", [
        claim("hs3", "haley-stevens", "economic_stewardship", 2, False,
              "Voted for three of the largest deficit-funded spending packages in modern U.S. history: the $1.9T American Rescue Plan (2021), the $1.2T Infrastructure Investment and Jobs Act (2021), and led House passage of key provisions of the $280B CHIPS and Science Act (2022) as Chair of the House Research and Technology Subcommittee — a consistent pattern of supporting large-scale new federal outlays financed by deficit borrowing, contrary to the rubric's balanced-budget standard.",
              ["https://stevens.house.gov/media/press-releases/rep-stevens-secures-wins-chips-and-science-act-votes-historic-investments",
               "https://en.wikipedia.org/wiki/CHIPS_and_Science_Act"]),
    ]),

    # ---------- Mike Faris (KY-R, LOST 5/19 Republican primary) ----------
    ("mike-faris", "KY", "Senator", [
        claim("mf3", "mike-faris", "self_defense", 0, True,
              "Campaigns as a firm supporter of Kentucky's constitutional carry law, calling mandatory licensing requirements 'a violation of the Second Amendment rights of honest, accountable Kentuckians'; is an active NRA member who obtained his own concealed carry permit voluntarily — affirming the rubric's constitutional-carry standard without mandatory government permitting.",
              ["https://ivoterguide.com/candidate?canK=52693&elecK=720&path=%2Fall-in-state%2FKentucky&primarypartyk=R&raceK=11605",
               "https://ballotpedia.org/Mike_Faris"]),
    ]),

    # ---------- Amy McGrath (KY-D, LOST 5/19 Democratic primary) ----------
    ("amy-mcgrath", "KY", "Senator", [
        claim("am3", "amy-mcgrath", "border_immigration", 0, False,
              "Explicitly opposes construction of a physical border wall, calling it 'very expensive' and 'not effective' and arguing it can be defeated 'with a ladder' — rejecting the wall-and-military-enforcement standard the rubric requires; calls instead for 'comprehensive immigration reform' while maintaining ICE.",
              ["https://en.wikipedia.org/wiki/Amy_McGrath",
               "https://ballotpedia.org/Amy_McGrath"]),
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
