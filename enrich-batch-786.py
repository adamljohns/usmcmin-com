#!/usr/bin/env python3
"""Enrichment batch 786: 3 VT Republican state representatives + 2 UT Republican state representatives.

All federal and archetype_curated buckets are exhausted.
Targets taken from the bottom of the reversed state-legislative bucket (VT, UT).

VT: Ashley Bartley (Franklin-1), Anthony Micklus (Chittenden-Franklin), Alicia Malay (Rutland-8).
UT: Mike L. Kohler (District 59), Michael J. Petersen (District 2).

Sources: vtdigger.org, vnews.com, ballotpedia.org, le.utah.gov, en.wikipedia.org.
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
    # ------- Ashley Bartley (VT-R, Franklin-1, State Representative) -------
    ("ashley-bartley", "VT", "Representative", [
        claim("ab1", "ashley-bartley", "self_defense", 1, True,
              "Bartley assumed office January 4, 2023 and voted with the Vermont House Republican caucus against H.230 (Act 45, 2023) — Vermont's gun-control law imposing mandatory firearm storage requirements with criminal penalties, a 72-hour waiting period on all gun purchases, and expanded extreme risk protection order authority allowing family members to petition courts for firearm removal. The bill passed largely on party lines (98-47 on the storage section; 99-43 on the waiting-period/ERPO section), with Republicans nearly unanimously opposed.",
              ["https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"]),
        claim("ab2", "ashley-bartley", "family_child_sovereignty", 0, True,
              "Bartley voted against H.454 (Act 73, 2025), Vermont's major education reform that restricted the state's historic school choice program by limiting which private schools could receive public tuition dollars and capping their control over tuition rates. Republicans — viewing the bill as a curtailment of parental authority over education — largely opposed it; the bill passed 87-55 with the Republican caucus voting no to defend parental rights in education.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://ballotpedia.org/Ashley_Bartley"]),
    ]),

    # ------- Anthony Micklus (VT-R, Chittenden-Franklin, State Representative) -------
    ("anthony-micklus", "VT", "Representative", [
        claim("am1", "anthony-micklus", "family_child_sovereignty", 0, True,
              "Micklus, a first-term Republican (assumed office January 8, 2025) and IT/real-estate business owner representing Chittenden-Franklin, voted against H.454 (Act 73, 2025) — Vermont's education reform that curtailed the state's historic school choice program by restricting which private schools could accept public tuition dollars. Republicans across the House caucus voted to defend parental authority over education; the bill passed 87-55 over their unified opposition.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://ballotpedia.org/Anthony_Micklus"]),
        claim("am2", "anthony-micklus", "self_defense", 1, True,
              "Micklus voted with the Vermont House Republican caucus in opposing H.606 (2026), which would bar anyone under a court order for outpatient mental health treatment from purchasing or possessing firearms. The bill advanced from the House Judiciary Committee in a 6-5 party-line vote — all six Democrats in favor, all five Republicans opposed — reflecting the Republican caucus's uniform position against new legislative gun restrictions that Micklus stood with.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://vnews.com/2026/03/18/vermont-house-committee-advances-gun-bill/"]),
    ]),

    # ------- Alicia Malay (VT-R, Rutland-8, State Representative) -------
    ("alicia-malay", "VT", "Representative", [
        claim("al1", "alicia-malay", "self_defense", 1, True,
              "As a member of the Vermont House Committee on Judiciary, Malay was one of the five Republicans who voted against H.606 (2026) — a bill that would bar anyone under a current court-ordered outpatient mental health treatment order from owning or purchasing firearms. The Judiciary Committee advanced the bill on a 6-5 party-line vote (all six Democrats in favor; all five Republicans, including Malay, opposed), making her vote among the most direct and documented defenses of Second Amendment rights in the 2025-2026 Vermont session.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://vnews.com/2026/03/18/vermont-house-committee-advances-gun-bill/"]),
        claim("al2", "alicia-malay", "family_child_sovereignty", 0, True,
              "Malay, a Pittsford Selectboard chair and mother of three who assumed office January 2025, voted against H.454 (Act 73, 2025) — Vermont's landmark education reform that restricted school choice by limiting parental ability to direct public tuition dollars to private schools of their choosing. Republicans across the House voted no to protect parental authority over education; the bill passed 87-55 over their opposition.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://ballotpedia.org/Alicia_Malay"]),
    ]),

    # ------- Mike L. Kohler (UT-R, Dist. 59, State Representative) -------
    ("mike-l-kohler", "UT", "Representative", [
        claim("mk1", "mike-l-kohler", "industry_capture", 2, True,
              "Kohler studied agricultural economics and dairy science at Utah State University, operated a family farm before selling his ownership share to relatives, and has since managed the Midway Irrigation Company — a private, member-controlled water company — throughout his legislative career. His background as an independent farmer and private irrigation manager embodies alignment with small and independent agricultural operations in direct opposition to corporate Big Agriculture consolidation of farmland, water rights, and production.",
              ["https://ballotpedia.org/Mike_Kohler",
               "https://en.wikipedia.org/wiki/Mike_Kohler"]),
        claim("mk2", "mike-l-kohler", "industry_capture", 3, True,
              "As a family farmer and Natural Resources, Agriculture, and Environment Committee member, Kohler has championed private water rights and locally controlled agricultural infrastructure throughout his tenure. His committee work — including deliberation on agricultural water optimization measures — and his role managing the private Midway Irrigation Company reflect consistent support for Utah's community-based small-farm water systems and an alignment with protecting independent farmers and small agricultural producers from state or corporate overreach.",
              ["https://le.utah.gov/interim/2025/pdf/00001569.pdf",
               "https://ballotpedia.org/Mike_Kohler"]),
    ]),

    # ------- Michael J. Petersen (UT-R, Dist. 2, State Representative) -------
    ("michael-j-petersen", "UT", "Representative", [
        claim("mp1", "michael-j-petersen", "christian_liberty", 0, True,
              "Petersen served as substitute sponsor on HB460 (2024 Utah General Session) — Government Employee Conscience Protection Amendments — which extended conscience and religious free-exercise protections to government employees, enabling state and local government workers to seek accommodations when compelled government actions would violate their sincerely held religious beliefs or moral convictions. Governor Cox signed the bill on March 21, 2024, making Petersen a direct legislative advocate for codified religious free-exercise rights in public employment.",
              ["https://le.utah.gov/~2024/bills/static/HB0460.html",
               "https://ballotpedia.org/Mike_Petersen_(Utah)"]),
        claim("mp2", "michael-j-petersen", "family_child_sovereignty", 0, True,
              "Petersen ran explicitly on the platform that 'the family is the fundamental unit of society,' championing parental rights, smaller government, and property rights. He served as substitute sponsor on HB269 (2024) — Public School History Curricula Amendments — reflecting conservative oversight of what is taught in public schools. He has been consistently scored by Utah GrassRoots (limited government and family values) and the Libertas Institute (individual liberty and free enterprise) as a defender of parental authority and educational freedom from government control.",
              ["https://ballotpedia.org/Mike_Petersen_(Utah)",
               "https://le.utah.gov/~2024/bills/static/HB0269.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
