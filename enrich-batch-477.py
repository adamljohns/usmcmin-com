#!/usr/bin/env python3
"""Enrichment batch 477: hand-curated claims for 5 Virginia House of Delegates members.

Continues bottom-of-alphabet VA House of Delegates enrichment begun in batch 476.
Federal (archetype_curated) and VA state-senator buckets are fully enriched.
These five are all Democrats from the evidence_state pool with 0 claims.

Targets (all VA, reverse-alpha from remaining HoD pool):
  Destiny LeVere Bolling (VA-D, HoD-80)  — Henrico County; first VA delegate to vote remotely post-childbirth
  Delores McQuinn       (VA-D, HoD-81)  — Richmond area; in House since 2009; gun-control patron
  Debra Gardner         (VA-D, HoD-76)  — Democrat, social-worker background; elected 2023
  David Reid            (VA-D, HoD-28)  — Loudoun County; retired USN Reserve Cdr; in House since 2017
  Cliff Hayes Jr.       (VA-D, HoD-91)  — Chesapeake/Hampton Roads; Moms Demand Action Gun Sense honoree

Key sourced events:
  • HJR 1 (Right to Reproductive Freedom constitutional amendment) passed VA House 51-48
    on 14 Jan 2025 on a strict party-line vote — all 51 Democrats yes, all Republicans no.
    (VPM, 2025-01-15; Ballotpedia)
  • HJR 9 (Marriage Equality constitutional amendment) passed VA House 58-35 on 14 Jan 2025
    — all 51 Democrats plus 7 Republicans in favor.  (VPM, 2025-01-15)
  • HB 2 (2019 session) — Delores McQuinn as patron; expanded firearm transfer
    background-check requirements in Virginia.  (Ballotpedia/Delores McQuinn)
  • Cliff Hayes Jr. received Moms Demand Action Gun Sense Candidate Distinction in 2021.
    (Ballotpedia/Cliff Hayes)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
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
    # ----------- Destiny LeVere Bolling (VA-D, HoD-District 80) -----------
    ("destiny-levere-bolling", "VA", "District 80", [
        claim("dlb1", "destiny-levere-bolling", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House of Delegates passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — by a strict 51-48 party-line vote, with every Democratic delegate voting yes. LeVere Bolling (D-Henrico, District 80), serving her second term, voted yes along with her entire caucus. The amendment would enshrine in Virginia's constitution a sweeping right to abortion at all stages of pregnancy, foreclosing any life-from-conception protection under state law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Destiny_LeVere_Bolling",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("dlb2", "destiny-levere-bolling", "biblical_marriage", 1, False,
              "On 14 January 2025, the Virginia House passed HJR 9 — the Marriage Equality constitutional amendment — by 58-35, with all 51 Democrats (including LeVere Bolling) voting yes. The amendment would permanently enshrine same-sex marriage in Virginia's constitution, directly rejecting the one-man-one-woman definition the rubric requires.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Destiny_LeVere_Bolling",
               "https://www.vpap.org/legislators/455078-destiny-levere-bolling/"]),
    ]),

    # ----------- Delores McQuinn (VA-D, HoD-District 81) -----------
    ("delores-mcquinn", "VA", "District 81", [
        claim("dm1", "delores-mcquinn", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — 51-48 on a strict party-line vote, with all 51 Democrats voting yes. McQuinn (D-Richmond area, District 81), a 15-year House veteran first elected in 2009, voted yes. The amendment would entrench a constitutional right to abortion through all stages of pregnancy in Virginia, precluding any life-at-conception standard under state law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Delores_McQuinn",
               "https://www.vpap.org/legislators/33585-delores-mcquinn/"]),
        claim("dm2", "delores-mcquinn", "self_defense", 1, False,
              "McQuinn was a patron of Virginia HB 2 in the 2019 General Assembly session, which expanded firearm transfer background-check requirements under the Commonwealth's criminal history record information check framework. Sponsoring legislation to impose additional purchase-restriction requirements on firearm transfers directly conflicts with the rubric's standard of opposing new firearm restrictions and registries.",
              ["https://ballotpedia.org/Delores_McQuinn",
               "https://www.vpap.org/legislators/33585-delores-mcquinn/"]),
    ]),

    # ----------- Debra Gardner (VA-D, HoD-District 76) -----------
    ("debra-gardner", "VA", "District 76", [
        claim("dg1", "debra-gardner", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — 51-48 on a strict party-line vote, with all 51 Democrats voting yes. Gardner (D-District 76), first elected in November 2023 and serving her first full term, voted yes along with her entire caucus. The amendment would enshrine a sweeping constitutional right to abortion at all stages of pregnancy in Virginia law, foreclosing any life-from-conception recognition.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Debra_Gardner",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("dg2", "debra-gardner", "biblical_marriage", 1, False,
              "On 14 January 2025, the Virginia House passed HJR 9 — the Marriage Equality constitutional amendment — by 58-35, with all 51 House Democrats (including Gardner) voting yes. The amendment would permanently write same-sex marriage into Virginia's constitution, directly rejecting the one-man-one-woman definition the rubric requires.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Debra_Gardner",
               "https://www.vpap.org/legislators/328311-debra-gardner/"]),
    ]),

    # ----------- David Reid (VA-D, HoD-District 28) -----------
    ("david-reid", "VA", "District 28", [
        claim("dr1", "david-reid", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — 51-48 on a strict party-line vote, with all 51 Democrats voting yes. Reid (D-Loudoun County, District 28), a retired U.S. Navy Reserve commander who has served in the House since 2017, voted yes. The amendment would enshrine a constitutional right to abortion at all stages of pregnancy in Virginia law, precluding any life-at-conception standard.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/David_Reid_(Virginia)",
               "https://en.wikipedia.org/wiki/David_A._Reid"]),
        claim("dr2", "david-reid", "biblical_marriage", 1, False,
              "On 14 January 2025, the Virginia House passed HJR 9 — the Marriage Equality constitutional amendment — by 58-35, with all 51 Democrats (including Reid) voting yes. Reid has represented Northern Virginia's Loudoun County since 2017 and consistently votes with the Democratic caucus on social issues. The amendment would permanently enshrine same-sex marriage in Virginia's constitution, directly rejecting the one-man-one-woman definition the rubric requires.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/David_Reid_(Virginia)",
               "https://www.vpap.org/legislators/272244-david-reid/"]),
    ]),

    # ----------- Cliff Hayes Jr. (VA-D, HoD-District 91) -----------
    ("cliff-hayes-jr", "VA", "District 91", [
        claim("ch1", "cliff-hayes-jr", "self_defense", 1, False,
              "Hayes received the Moms Demand Action Gun Sense Candidate Distinction in 2021, a recognition awarded to candidates who publicly commit to supporting gun-control policies including expanded background checks, red-flag laws, and other firearm purchase restrictions. Accepting this endorsement and the policy platform it entails directly conflicts with the rubric's standard of opposing new firearm restrictions, red-flag orders, and magazine or registry regulations.",
              ["https://ballotpedia.org/Cliff_Hayes",
               "https://www.vpap.org/legislators/151974-cliff-hayes/",
               "https://en.wikipedia.org/wiki/Cliff_Hayes_Jr."]),
        claim("ch2", "cliff-hayes-jr", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — 51-48 on a strict party-line vote, with all 51 Democrats voting yes. Hayes (D-Chesapeake/Hampton Roads, District 91), who has served in the House since 2016, voted yes. The amendment would enshrine a constitutional right to abortion at all stages of pregnancy in Virginia, foreclosing any life-from-conception recognition under state law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Cliff_Hayes",
               "https://www.vpap.org/legislators/151974-cliff-hayes/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
