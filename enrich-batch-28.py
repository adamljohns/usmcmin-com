#!/usr/bin/env python3
"""Enrichment batch 28: hand-curated claims for 5 bottom-of-alphabet U.S. House candidates.

Targets archetype_curated representatives/candidates that had 0 evidence claims.
Taken from the bottom of the alphabet (WA + WI), reverse-sorted per instructions.

Mix: Joe Kent (WA-R), Rebecca Cooke (WI-D), Peter Barca (WI-D),
Carmen Goers (WA-R), Leslie Lewallen (WA-R).
Each claim cites >=1 reliable source and reflects public positions / voting record.

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
    # ---------------- Joe Kent (WA-R, WA-03) ----------------
    ("joe-kent", "WA", "Representative", [
        claim("jk1", "joe-kent", "self_defense", 2, True,
              "Has called for abolishing the ATF and repealing the National Firearms Act: 'I want to get rid of all the federal gun laws — like the ATF, the National Firearms Act,' affirming that 'gun laws are infringements' — an explicit demand to repeal the GCA/NFA consistent with the rubric.",
              ["https://en.wikipedia.org/wiki/Joe_Kent",
               "https://ballotpedia.org/Joe_Kent_(Washington)"]),
        claim("jk2", "joe-kent", "border_immigration", 0, True,
              "Campaigned on sealing the southern border with wall construction and military assets, and backed halting all legal immigration for 20 years — one of the most restrictive border-enforcement platforms of the 2022 and 2024 cycles.",
              ["https://en.wikipedia.org/wiki/Joe_Kent",
               "https://ballotpedia.org/Joe_Kent_(Washington)"]),
        claim("jk3", "joe-kent", "foreign_policy_restraint", 1, True,
              "Resigned as director of the National Counterterrorism Center in March 2026 specifically over U.S. involvement in the Iran war and the influence of foreign-linked lobbying in domestic policy — a concrete act of foreign-policy restraint consistent with the rubric's end-forever-wars criterion.",
              ["https://en.wikipedia.org/wiki/Joe_Kent",
               "https://fortune.com/2026/03/17/who-is-joe-kent-green-beret-maga-loyalist-former-political-candidate-who-quit-over-iran/"]),
    ]),

    # ---------------- Rebecca Cooke (WI-D, WI-03) ----------------
    ("rebecca-cooke", "WI", "Representative", [
        claim("rc1", "rebecca-cooke", "sanctity_of_life", 0, False,
              "Describes herself as firmly pro-choice and has pledged to vote to codify Roe v. Wade protections into federal law, rejecting any personhood-from-conception standard: 'I am a firm believer that every person should have the right to make the best decision for themselves about if, when, and how to start or grow a family.'",
              ["https://ballotpedia.org/Rebecca_Cooke",
               "https://emilyslist.org/candidate/rebecca-cooke-2/"]),
        claim("rc2", "rebecca-cooke", "sanctity_of_life", 4, False,
              "Endorsed and supported by EMILY's List — the nation's largest pro-abortion-rights fundraising network — which requires all endorsees to be pro-choice, placing Cooke squarely within the abortion-industry endorsement and funding network the rubric opposes.",
              ["https://emilyslist.org/news/emilys-list-endorses-rebecca-cooke-for-wisconsins-3rd-congressional-district/",
               "https://ballotpedia.org/EMILY's_List"]),
    ]),

    # ---------------- Peter Barca (WI-D, WI-01) ----------------
    ("peter-barca", "WI", "Representative", [
        claim("pb1", "peter-barca", "sanctity_of_life", 0, False,
              "Has pledged to 'always protect women's right to make their own health care decisions' and frames access to reproductive care as a campaign centerpiece, rejecting any personhood-from-conception protection for the unborn.",
              ["https://ballotpedia.org/Peter_Barca",
               "https://wisdems.org/wisdems-news/icymi-peter-barca-send-me-to-congress-again-to-fight-for-wisconsin-families/"]),
        claim("pb2", "peter-barca", "self_defense", 1, False,
              "Supports universal background-check legislation and 'common sense gun safety measures,' aligning with the gun-control agenda the rubric's self-defense category opposes (background-check mandates extend the federal firearms registry).",
              ["https://ballotpedia.org/Peter_Barca",
               "https://govtrack.us/congress/members/peter_barca/401134"]),
    ]),

    # ---------------- Carmen Goers (WA-R, WA-08) ----------------
    ("carmen-goers", "WA", "Representative", [
        claim("cg1", "carmen-goers", "sanctity_of_life", 0, False,
              "Describes elective abortion as 'highly personal decisions that should be made between the parents and their medical professional team' and considers federal abortion restrictions unconstitutional, leaving it to states — she does not affirm personhood or life-at-conception protection.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/207474/carmen-goers",
               "https://ballotpedia.org/Carmen_Goers"]),
        claim("cg2", "carmen-goers", "border_immigration", 0, True,
              "Supports physically securing the southern border and called for change to prioritize national security at the border: 'I am concerned about the impact of the open border on national security' — consistent with the rubric's wall-plus-military border criterion.",
              ["https://www.carmenforwashington.com/issues/",
               "https://ballotpedia.org/Carmen_Goers"]),
    ]),

    # ---------------- Leslie Lewallen (WA-R, WA-03) ----------------
    ("leslie-lewallen", "WA", "Representative", [
        claim("ll1", "leslie-lewallen", "border_immigration", 0, True,
              "Names closing the southern border as her top priority and specifically argues that funding border-patrol agents and building a wall would prevent drugs from entering Washington state — consistent with the rubric's wall-plus-military border-security standard.",
              ["https://ballotpedia.org/Leslie_Lewallen",
               "https://www.thereflector.com/stories/congressional-candidate-leslie-lewallen-aims-to-reduce-drug-overdoses,342533"]),
        claim("ll2", "leslie-lewallen", "family_child_sovereignty", 0, True,
              "On the Camas City Council she has consistently 'fought for parental rights,' citing parental rights as a pillar of her platform alongside fiscal responsibility and public safety — aligning with the rubric's family and child-sovereignty criterion.",
              ["https://ballotpedia.org/Leslie_Lewallen",
               "https://www.koin.com/nwpolitics/leslie-lewallen-on-the-race-for-washingtons-3rd-district/"]),
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
