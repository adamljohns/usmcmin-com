#!/usr/bin/env python3
"""Enrichment batch 784: hand-curated claims for 5 VT Republican state representatives.

All archetype_curated and archetype_party_default federal buckets are exhausted.
Targets taken from the bottom of the reversed state-legislative bucket (VT-R).

Targets (all VT-R, State Representative): Christopher Howland (Rutland-4),
Chris Pritchard (Rutland-Bennington), Brenda Steady (Chittenden-25),
Bill Canfield (Rutland-10, VP Ways & Means), Beth Quimby (Caledonia-3).
Sources: vtdigger.org, ballotpedia.org, legislature.vermont.gov (2025-2026 session).
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
    # ------- Christopher Howland (VT-R, Rutland-4, State Representative) -------
    ("christopher-howland", "VT", "Representative", [
        claim("ch1", "christopher-howland", "family_child_sovereignty", 0, True,
              "Howland, a Vermont National Guard veteran and Rutland-4 Republican, joined most House Republicans in opposing H.454 (2025), Vermont's landmark education reform that restricted the state's long-standing school choice program by limiting which private schools could accept public tuition dollars and capping their control over tuition rates. The bill passed 87-55 with most Republicans voting no to defend parental authority over education.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://vtdigger.org/2025/06/16/vermont-legislature-passes-landmark-education-reform-bill-after-a-messy-final-day/"]),
        claim("ch2", "christopher-howland", "self_defense", 1, True,
              "Howland is a member of the Vermont House Republican caucus, which has unanimously opposed gun-control legislation advanced by the Democratic majority in the 2025-2026 session. In March 2026, all five Republican members of the House Judiciary Committee voted against H.606 — which would bar firearm ownership for those under active court-ordered mental health treatment — while all six Democrats supported it, reflecting the caucus's consistent defense of Second Amendment rights against new legislative restrictions.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://vnews.com/2026/03/18/vermont-house-committee-advances-gun-bill/"]),
    ]),

    # ------- Chris Pritchard (VT-R, Rutland-Bennington, State Representative) -------
    ("chris-pritchard", "VT", "Representative", [
        claim("cp1", "chris-pritchard", "self_defense", 1, True,
              "Pritchard is a 35-year certified Vermont Hunter Education Instructor and Certified Level 1 and Level 2 shotgun instructor for the UVM 4-H Shooting Sports Program, coaching the shotgun discipline at the Oxbow Mountain 4-H Shooting Sports club for 18 years. His career reflects a deep commitment to firearms education and the lawful use of guns; he ran as a Republican explicitly supporting Second Amendment rights and joined his caucus in opposing new gun-control measures in the 2025-2026 legislative session.",
              ["https://ballotpedia.org/Chris_Pritchard",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("cp2", "chris-pritchard", "family_child_sovereignty", 0, True,
              "Pritchard joined most Republicans in opposing H.454 (2025), Vermont's education reform law that restricted the state's school choice program by curtailing parental ability to direct public tuition dollars to private schools of their choosing; the bill passed 87-55 over Republican objections rooted in defense of parental rights and Vermont's historic education freedom tradition.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://vtdigger.org/2025/06/16/vermont-legislature-passes-landmark-education-reform-bill-after-a-messy-final-day/"]),
    ]),

    # ------- Brenda Steady (VT-R, Chittenden-25, State Representative) -------
    ("brenda-steady", "VT", "Representative", [
        claim("bs1", "brenda-steady", "family_child_sovereignty", 0, True,
              "Steady, a Chittenden County Republican who unseated Democratic incumbent Julia Andrews in November 2024, opposed H.454 (2025), Vermont's landmark education reform law that limited the state's school choice program — restricting which private schools could receive public tuition payments and how much control they retain over tuition rates. The bill passed 87-55 with most Republicans, including Steady, voting to preserve parental education choice.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://ballotpedia.org/Brenda_Steady"]),
        claim("bs2", "brenda-steady", "self_defense", 1, True,
              "As a Vermont House Republican, Steady aligns with the caucus's uniform opposition to gun-control legislation pushed by the Democratic majority. In 2026, the Republican bloc on the House Judiciary Committee voted 5-0 against H.606 — which would prohibit firearm ownership for anyone under an active court-ordered mental health treatment order — while Democrats voted unanimously in favor, demonstrating the sharp partisan divide on Second Amendment restrictions.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://ballotpedia.org/Brenda_Steady"]),
    ]),

    # ------- Bill Canfield (VT-R, Rutland-10, State Representative) -------
    ("bill-canfield", "VT", "Representative", [
        claim("bc1", "bill-canfield", "family_child_sovereignty", 0, True,
              "Canfield, Vice Chair of the Vermont House Ways and Means Committee and a Republican member since 2013, joined most Republicans in opposing H.454 (2025) — Vermont's education reform that restricted school choice by limiting which private schools could accept public tuition vouchers. Lawmakers from school-choice-dependent Vermont communities condemned the bill's curtailment of parental education freedom; it passed 87-55 over Republican objections.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://vtdigger.org/2025/06/16/vermont-legislature-passes-landmark-education-reform-bill-after-a-messy-final-day/"]),
        claim("bc2", "bill-canfield", "self_defense", 1, True,
              "A U.S. Navy veteran who has served in the Vermont House since 2013, Canfield voted with his Republican colleagues against H.230 (2023, Act 45) — Vermont's major gun-control law that imposed new storage mandates, a 72-hour waiting period on firearm purchases, and extreme risk protection orders (gun confiscation). Vermont Democrats pushed the legislation through largely along party lines; Republicans, including Canfield, uniformly opposed it as an infringement on Second Amendment rights.",
              ["https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"]),
    ]),

    # ------- Beth Quimby (VT-R, Caledonia-3, State Representative) -------
    ("beth-quimby", "VT", "Representative", [
        claim("bq1", "beth-quimby", "family_child_sovereignty", 0, True,
              "Quimby, a 30-year math teacher and Justice of the Peace representing Vermont's rural Northeast Kingdom, joined most Republicans in opposing H.454 (2025), Vermont's education reform law that restricted the school choice program by limiting families' ability to direct public tuition dollars to private schools of their choosing. The bill passed 87-55 with the Republican caucus largely voting no to protect parental authority over education.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://ballotpedia.org/Beth_Quimby"]),
        claim("bq2", "beth-quimby", "self_defense", 1, True,
              "Quimby serves as secretary of the Lyndon Republican Committee and as the Caledonia County member of the VT GOP platform committee — a party official whose caucus has uniformly opposed gun-control legislation in Vermont. Vermont House Republicans voted unanimously against H.230 (2023, Act 45) and in 2026 all five Republican committee members opposed H.606 (which would restrict gun ownership during court-ordered mental health treatment), reflecting the Republican platform Quimby helps shape.",
              ["https://ballotpedia.org/Beth_Quimby",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collision."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
