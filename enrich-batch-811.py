#!/usr/bin/env python3
"""Enrichment batch 811: 5 West Virginia State Delegates (Democratic caucus).

Federal archetype_curated bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets: Kayla Young (D-56, Minority Leader Pro Tempore),
John Williams (D-80), Hollis Lewis (D-57), Evan Hansen (D-79),
Anitra Hamilton (D-81).

All claims drawn from 2022-2025 official legislative records, roll-call
reporting, and documented public statements. WV SB 456 (Riley Gaines Act,
2025) passed House 87-9 with every Democrat voting no — confirmed by
West Virginia Watch and Wikipedia. MINIFIED write preserved (no indent=2).
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
    # ---------------- Kayla Young (WV-56, Minority Leader Pro Tempore, D) ----------------
    ("kayla-young", "WV", "Delegate", [
        claim("ky1", "kayla-young", "sanctity_of_life", 0, False,
              "As Minority Leader Pro Tempore, Young led a group of eight Democratic delegates in February 2024 and again in March 2025 to introduce legislation asking voters to enshrine a state constitutional right to 'make and carry out one's own reproductive decisions,' including abortion, contraception, and fertility treatment — explicitly opposing any life-at-conception or personhood standard and seeking to entrench abortion access in the WV Constitution.",
              ["https://mountainstatespotlight.org/2024/02/15/wv-abortion-reproductive-rights-redo/",
               "https://westvirginiawatch.com/2025/03/04/democrat-lawmakers-want-wv-voters-to-decide-on-abortion-fertility-rights/"],
              kind="statement"),
        claim("ky2", "kayla-young", "biblical_marriage", 2, False,
              "Voted against West Virginia SB 456 (Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in state code based on biological sex and strips state-level protections for transgender and gender non-conforming persons. The bill passed the House 87–9; all nine House Democrats cast no votes, including Young.",
              ["https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
    ]),

    # ---------------- John Williams (WV-80, State Delegate, D) ----------------
    ("john-williams", "WV", "Delegate", [
        claim("jw1", "john-williams", "sanctity_of_life", 0, False,
              "Publicly stated 'I do not support restricting access to abortion,' affirming opposition to the legislature's near-total abortion ban (HB 302, signed Sept 2022) and subsequent efforts to tighten restrictions — rejecting any legislative protection of life from conception.",
              ["https://www.acluwv.org/john-williams-district-51/",
               "https://ballotpedia.org/John_Williams_(West_Virginia)"]),
        claim("jw2", "john-williams", "self_defense", 0, False,
              "Voted against West Virginia SB 10 (Campus Self-Defense Act, signed March 2023), which extended concealed-carry rights to university campuses statewide. The bill passed the House 84–13 with Democrats in near-unanimous opposition; Williams, representing the Morgantown/WVU district, was among the opposing minority.",
              ["https://wvmetronews.com/2023/03/01/justice-signs-campus-carry-legislation-into-law/",
               "https://en.wikipedia.org/wiki/John_Williams_(West_Virginia_politician)"]),
    ]),

    # ---------------- Hollis Lewis (WV-57, State Delegate, D) ----------------
    ("hollis-lewis", "WV", "Delegate", [
        claim("hl1", "hollis-lewis", "self_defense", 0, False,
              "Voted against West Virginia HB 4299 (School Protection Officer Act, Feb 2024), which permitted trained K-12 school staff to carry concealed firearms as school protection officers. The bill passed 89–11 with Democrats providing nearly all no votes; Lewis, a magistrate and criminal-justice instructor, voted with the Democratic minority against expanding lawful carry into public schools.",
              ["https://wvpublic.org/story/government/tempers-flare-in-house-debate-over-arming-teachers/",
               "https://mountainstatespotlight.org/2024/02/21/teachers-concealed-carry-bill-house-passage/"]),
        claim("hl2", "hollis-lewis", "biblical_marriage", 2, False,
              "Voted against West Virginia SB 456 (Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in state code based on biological sex and strips state-level protections for transgender and gender non-conforming persons. The bill passed the House 87–9; West Virginia Watch confirmed every Democrat in the chamber — including Lewis — voted no.",
              ["https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
    ]),

    # ---------------- Evan Hansen (WV-79, State Delegate, D) ----------------
    ("evan-hansen", "WV", "Delegate", [
        claim("eh1", "evan-hansen", "election_integrity", 0, False,
              "Directly and publicly opposed West Virginia HB 3016 (2025 Regular Session), the stricter photo voter ID law signed by Gov. Morrisey, stating on record that 'the bill would result in fewer legal West Virginians voting in-person on Election Day or during early in-person voting' — opposing the rubric's voter-ID election-integrity standard.",
              ["https://www.herald-dispatch.com/_zapp/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://ballotpedia.org/2025_West_Virginia_legislative_session"],
              kind="statement"),
        claim("eh2", "evan-hansen", "self_defense", 0, False,
              "Voted against West Virginia HB 4299 (School Protection Officer Act, Feb 2024, passed 89–11), which permitted K-12 school staff to carry concealed firearms; Hansen was specifically quoted on the House floor opposing an amendment to the bill, making him one of the most vocal Democratic opponents of the measure.",
              ["https://wvpublic.org/story/government/tempers-flare-in-house-debate-over-arming-teachers/",
               "https://mountainstatespotlight.org/2024/02/21/teachers-concealed-carry-bill-house-passage/"]),
        claim("eh3", "evan-hansen", "economic_stewardship", 4, False,
              "As WV House Minority Chair of both the Energy & Manufacturing and Natural Resources committees, Hansen advocates for a renewable energy transition aligned with ESG/net-zero frameworks: he sponsored HB 2419 (community solar program), HB 4770 (Energy Efficiency Jobs Creation Act), and helped pass SB 583 enabling utility-grade solar development — at direct odds with the rubric's opposition to WEF/ESG/Davos-aligned energy mandates.",
              ["https://mountainstatespotlight.org/2024/01/22/energy-efficiency-job-creation-wv-hansen/",
               "https://www.hansenforwv.com/about"]),
    ]),

    # ---------------- Anitra Hamilton (WV-81, State Delegate, D) ----------------
    ("anitra-hamilton", "WV", "Delegate", [
        claim("ah1", "anitra-hamilton", "sanctity_of_life", 0, False,
              "Publicly advocates that 'reproductive healthcare should be at the discretion and protection of a woman and her physician to maintain and enhance the health of all women,' and supports putting abortion access on the ballot as a constitutional right — rejecting any life-at-conception or personhood standard and opposing the legislature's existing near-total abortion ban.",
              ["https://ballotpedia.org/Anitra_Hamilton",
               "https://www.acluwv.org/en/anitra-hamilton"],
              kind="statement"),
        claim("ah2", "anitra-hamilton", "biblical_marriage", 2, False,
              "Voted against West Virginia SB 456 (Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in state code based on biological sex and strips state-level protections for transgender and gender non-conforming persons. The bill passed the House 87–9; as one of only nine House Democrats, Hamilton cast one of the nine no votes.",
              ["https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
