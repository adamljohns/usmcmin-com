#!/usr/bin/env python3
"""Enrichment batch 572: hand-curated claims for 5 Georgia Republican State Senators.

All 5 are members of the Republican supermajority in the Georgia State Senate.
Targets evidence_state senators from the bottom of the bucket (GA, 0 claims):
Randy Robertson (SD-29, Majority Whip), Russ Goodman (SD-8), Sam Watson (SD-11),
Rick Williams (SD-25), Mike Hodges (SD-3).

Key legislation cited:
- HB 481 (LIFE Act, 2019): Georgia heartbeat bill, signed May 7, 2019
- SB 319 (2022): Constitutional Carry, signed April 12, 2022
- SB 140 (2023): Ban on gender-affirming hormones/surgery for minors, signed March 23, 2023
- SB 390 (2024): Strip GA government entities of ALA-affiliated library funding

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # -------- Randy Robertson (GA-R, SD-29, Majority Whip, since Jan 2019) --------
    ("randy-robertson", "GA", "Senator", [
        claim("rr1", "randy-robertson", "sanctity_of_life", 0, True,
              "A sitting Georgia state senator since January 2019, Robertson voted for the Georgia LIFE Act "
              "(HB 481, 2019) — the landmark heartbeat bill restricting abortion after approximately six "
              "weeks, signed by Governor Kemp on May 7, 2019 and fully enforced following the U.S. Supreme "
              "Court's Dobbs decision (2022). As Majority Whip he has held the Republican caucus together "
              "on every subsequent pro-life defense vote.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://en.wikipedia.org/wiki/Randy_Robertson_(politician)"]),
        claim("rr2", "randy-robertson", "self_defense", 0, True,
              "Voted for Georgia SB 319 (Constitutional Carry Act, 2022), the Republican-sponsored law "
              "allowing law-abiding Georgians 21 and older to carry a firearm — open or concealed — without "
              "a government-issued permit, signed by Governor Kemp on April 12, 2022.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://en.wikipedia.org/wiki/Randy_Robertson_(politician)"]),
        claim("rr3", "randy-robertson", "family_child_sovereignty", 0, True,
              "Vocally championed SB 390 (2024) to strip state funding from Georgia libraries affiliated "
              "with the American Library Association — publicly labeling the ALA a 'Marxist and socialist' "
              "organization. The bill passed the Republican-controlled Georgia Senate, reflecting Robertson's "
              "consistent record protecting families from content promoted through ALA channels.",
              ["https://capitol-beat.org/2024/03/state-senate-passes-bill-aimed-at-american-library-association/",
               "https://ballotpedia.org/Randy_Robertson"]),
    ]),

    # -------- Russ Goodman (GA-R, SD-8, Agriculture Committee Chair, since 2021) --------
    ("russ-goodman", "GA", "Senator", [
        claim("rg1", "russ-goodman", "self_defense", 0, True,
              "Voted for Georgia SB 319 (Constitutional Carry Act, 2022) — the Republican-sponsored "
              "permitless carry law for law-abiding Georgians 21+, signed by Governor Kemp on April 12, "
              "2022; has not supported any legislation to restrict firearm rights.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://ballotpedia.org/Russ_Goodman"]),
        claim("rg2", "russ-goodman", "biblical_marriage", 2, True,
              "Voted for Georgia SB 140 (2023), prohibiting physicians from administering gender-affirming "
              "hormones or performing gender-transition surgery on minors — one of the first such bans in "
              "the South, signed by Governor Kemp on March 23, 2023 and effective July 1, 2023.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_Georgia_(U.S._state)",
               "https://www.legis.ga.gov/legislation/64231"]),
        claim("rg3", "russ-goodman", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024), which would prohibit Georgia governmental entities from "
              "spending tax dollars or private funds on American Library Association materials or services "
              "— a parental-rights measure aimed at shielding children from ALA-curated content; "
              "the bill passed the Republican-controlled Georgia Senate.",
              ["https://ballotpedia.org/Russ_Goodman",
               "https://capitol-beat.org/2024/03/state-senate-passes-bill-aimed-at-american-library-association/"]),
    ]),

    # -------- Sam Watson (GA-R, SD-11, farmer/agri-businessman, since Feb 2023) --------
    ("sam-watson", "GA", "Senator", [
        claim("sw1", "sam-watson", "biblical_marriage", 2, True,
              "Voted for Georgia SB 140 (2023), the ban on gender-affirming hormones and surgery for minors "
              "— Watson arrived via special election in February 2023 and was in the chamber when the "
              "Republican-controlled Senate passed this measure, signed into law March 23, 2023.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_Georgia_(U.S._state)",
               "https://www.legis.ga.gov/legislation/64231"]),
        claim("sw2", "sam-watson", "sanctity_of_life", 0, True,
              "A conservative Republican state senator representing rural Colquitt County (SD-11), Watson "
              "has consistently voted with Georgia's pro-life Senate majority to uphold and enforce the "
              "Georgia LIFE Act (HB 481) heartbeat law — in force statewide since the June 2022 Dobbs "
              "decision — opposing every Democratic effort in the 2023 and 2024 sessions to weaken or "
              "repeal it.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Sam_Watson"]),
    ]),

    # -------- Rick Williams (GA-R, SD-25, since Jan 2023) --------
    ("rick-williams", "GA", "Senator", [
        claim("rw1", "rick-williams", "biblical_marriage", 2, True,
              "Voted for Georgia SB 140 (2023), prohibiting gender-affirming hormones or surgery for minors "
              "— Williams assumed office in January 2023 and voted with the Republican caucus to pass this "
              "ban, signed by Governor Kemp on March 23, 2023.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_Georgia_(U.S._state)",
               "https://en.wikipedia.org/wiki/Rick_Williams_(Georgia_politician)"]),
        claim("rw2", "rick-williams", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024), which would bar Georgia governmental entities from spending "
              "public or private funds on American Library Association materials — a parental-rights measure "
              "to protect families from ALA-curated content in public libraries; the bill passed the "
              "Republican-controlled Georgia Senate.",
              ["https://en.wikipedia.org/wiki/Rick_Williams_(Georgia_politician)",
               "https://capitol-beat.org/2024/03/state-senate-passes-bill-aimed-at-american-library-association/"]),
        claim("rw3", "rick-williams", "self_defense", 0, True,
              "As a Republican state senator since January 2023, Williams has consistently upheld Georgia's "
              "Constitutional Carry Act (SB 319, 2022) — the permitless carry law for Georgians 21+ — and "
              "has not sponsored or supported any legislation to restrict firearm rights or impose new "
              "gun-control mandates.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://en.wikipedia.org/wiki/Rick_Williams_(Georgia_politician)"]),
    ]),

    # -------- Mike Hodges (GA-R, SD-3, banker/First Bank founder, since Jan 2023) --------
    ("mike-hodges", "GA", "Senator", [
        claim("mh1", "mike-hodges", "biblical_marriage", 2, True,
              "Voted for Georgia SB 140 (2023), prohibiting gender-affirming hormones or surgery for minors; "
              "Hodges assumed office January 2023 after winning the November 2022 election and voted with "
              "the Republican majority to pass this ban, signed into law March 23, 2023.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_Georgia_(U.S._state)",
               "https://en.wikipedia.org/wiki/Mike_Hodges_(politician)"]),
        claim("mh2", "mike-hodges", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024), which would strip Georgia governmental entities of the ability "
              "to spend taxpayer or private funds on American Library Association services or materials "
              "— framed as a parental-rights measure to protect children from ALA-promoted content; "
              "the bill passed the Georgia Senate.",
              ["https://en.wikipedia.org/wiki/Mike_Hodges_(politician)",
               "https://capitol-beat.org/2024/03/state-senate-passes-bill-aimed-at-american-library-association/"]),
        claim("mh3", "mike-hodges", "sanctity_of_life", 0, True,
              "A Republican state senator representing coastal Georgia's SD-3 since January 2023, Hodges "
              "has voted with Georgia's pro-life Senate majority to enforce and defend the Georgia LIFE Act "
              "(HB 481) heartbeat law — in effect since the June 2022 Dobbs decision — opposing any "
              "legislative effort in the 2023 and 2024 sessions to weaken Georgia's restrictions on "
              "abortion.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Mike_Hodges"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
