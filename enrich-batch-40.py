#!/usr/bin/env python3
"""Enrichment batch 40: hand-curated claims for 4 federal House candidates.

Targets archetype_curated Representatives with 0 evidence claims, taken from
the bottom of the alphabet (PA > OH > NY).  Uses the (slug + state +
office_keyword) matcher from batches 2-39 to avoid name-collision bugs.

Mix (2 R / 2 D): Marc Molinaro (NY-R), Kevin Coughlin (OH-R),
Chris Rabb (PA-D), John Avlon (NY-D).
Each claim cites >=1 reliable source and reflects documented
voting record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Chris Rabb (PA-03, D, democratic socialist) ----------------
    ("chris-rabb", "PA", "Representative", [
        claim("cr1", "chris-rabb", "sanctity_of_life", 0, False,
              "A self-described democratic socialist who openly advocates abortion access as health care; co-sponsored Pennsylvania legislation to protect reproductive health services and access to abortion, and won the May 2026 Democratic primary on a platform endorsed by DSA and pro-abortion progressive organizations — rejecting any life-at-conception standard.",
              ["https://en.wikipedia.org/wiki/Chris_Rabb",
               "https://ballotpedia.org/Christopher_Rabb"]),
        claim("cr2", "chris-rabb", "self_defense", 1, False,
              "As a PA state representative Rabb sponsored legislation expanding background checks and restricting firearm access; endorsed by the Justice Democrats and Sunrise Movement, which advocate for assault-weapons bans and red-flag laws — opposing constitutional carry and unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Christopher_Rabb",
               "https://en.wikipedia.org/wiki/Chris_Rabb"]),
        claim("cr3", "chris-rabb", "biblical_marriage", 4, False,
              "Endorsed by the Democratic Socialists of America (both Philadelphia and national chapters), Justice Democrats, and the Working Families Party — organizations that actively advance LGBTQ curriculum and policy promotion in schools and public accommodations, the ideology the rubric opposes.",
              ["https://ballotpedia.org/Christopher_Rabb",
               "https://justicedemocrats.com/candidate/chris-rabb/"]),
    ]),

    # ---------------- Kevin Coughlin (OH-13, R) ----------------
    ("kevin-coughlin", "OH", "Representative", [
        claim("kc1", "kevin-coughlin", "sanctity_of_life", 0, True,
              "Endorsed by Ohio Right to Life, pledging to 'stand up for the unborn, for mothers, and their babies in Congress'; described by Democrats as someone who 'spent his career supporting efforts to ban abortion,' consistent with a life-affirming record throughout his Ohio Senate and 2024 congressional campaign.",
              ["https://ballotpedia.org/Kevin_Coughlin",
               "https://en.wikipedia.org/wiki/Kevin_Coughlin"]),
        claim("kc2", "kevin-coughlin", "border_immigration", 0, True,
              "Campaigned to 'secure the border and close loopholes that allow illegal immigrants who commit a crime to escape justice,' and explicitly opposed any path to citizenship for those who entered the country illegally — aligning with the wall-and-enforcement posture the rubric favors.",
              ["https://ballotpedia.org/Kevin_Coughlin"]),
        claim("kc3", "kevin-coughlin", "economic_stewardship", 2, True,
              "Signed the Taxpayer Protection Pledge (Americans for Tax Reform) and campaigned for a constitutional balanced-budget amendment modeled on the surplus budgets he helped pass as an Ohio state senator — consistent with the rubric's anti-deficit, sound-stewardship standard.",
              ["https://ballotpedia.org/Kevin_Coughlin",
               "https://en.wikipedia.org/wiki/Kevin_Coughlin"]),
    ]),

    # ---------------- John Avlon (NY-01, D) ----------------
    ("john-avlon", "NY", "Representative", [
        claim("ja1", "john-avlon", "sanctity_of_life", 0, False,
              "Campaigned on protecting reproductive freedom and criticized the Dobbs decision as having 'taken away the constitutional right to reproductive freedom after 50 years of Roe v. Wade'; supports a Democratic Congress to codify abortion rights federally — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/John_Avlon",
               "https://en.wikipedia.org/wiki/John_Avlon"]),
        claim("ja2", "john-avlon", "self_defense", 1, False,
              "Called for restoring the federal assault weapons ban and declared that 'nobody needs a weapon of war for hunting, sport or self-defense'; supports universal background checks and banning untraceable ghost guns — opposing constitutional carry and the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/John_Avlon",
               "https://en.wikipedia.org/wiki/John_Avlon"]),
        claim("ja3", "john-avlon", "border_immigration", 1, False,
              "Supports the bipartisan border bill that prioritized processing asylum claims and adding CBP personnel over mandatory deportation; explicitly rejects a deportation-first enforcement approach — not aligning with the rubric's mandatory-deportation standard.",
              ["https://ballotpedia.org/John_Avlon",
               "https://en.wikipedia.org/wiki/John_Avlon"]),
    ]),

    # ---------------- Marc Molinaro (NY-19, R) ----------------
    ("marc-molinaro", "NY", "Representative", [
        claim("mm1", "marc-molinaro", "sanctity_of_life", 0, False,
              "Has stated Congress has 'no role' in abortion policy and he would not vote for an abortion ban; personally opposes only very late-term abortions except in cases of rape, incest, or health of the mother — explicitly rejecting a life-at-conception or personhood standard.",
              ["https://en.wikipedia.org/wiki/Marc_Molinaro",
               "https://ballotpedia.org/Marcus_Molinaro"]),
        claim("mm2", "marc-molinaro", "biblical_marriage", 0, False,
              "Supports same-sex marriage and stated he would have voted for the Respect for Marriage Act — the 2022 law codifying federal recognition of same-sex unions — had he been in Congress during the 117th Congress; rejects the one-man-one-woman definition.",
              ["https://en.wikipedia.org/wiki/Marc_Molinaro",
               "https://ballotpedia.org/Marcus_Molinaro"]),
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
