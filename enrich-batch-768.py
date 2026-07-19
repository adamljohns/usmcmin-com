#!/usr/bin/env python3
"""Enrichment batch 768: 5 Florida Republican state officials (bottom-of-alphabet FL targets).

Primary archetype_curated federal senator/rep buckets are exhausted; this batch
continues the evidence_state FL Republican sweep with the 4 remaining FL R State
Senators (Passidomo, Garcia, Harrell, Gaetz) plus the top reverse-alpha FL R State
Representative (Benarroch) with 0 claims.

Targets:
  Kathleen Passidomo  (SD-28, Naples; FL Senate President 2022-2024; term-limited)
  Ileana Garcia       (SD-36, Miami-Dade; term 2024-2026)
  Gayle Harrell       (SD-31, Stuart; re-elected 2024)
  Don Gaetz           (SD-1, Northwest FL; former Senate President 2012-14; re-elected 2024)
  Yvette Benarroch    (HD-81, Collier County; sworn Nov 2024; Air Force veteran)

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
    # ---------- Kathleen Passidomo (FL SD-28, Naples, Senate President 2022-24) ----------
    ("kathleen-passidomo", "FL", "Senator", [
        claim("kp1", "kathleen-passidomo", "sanctity_of_life", 0, True,
              "As Florida Senate President, championed SB 300 (the 'Heartbeat Protection Act'), "
              "signed April 14, 2023, which bans abortion after approximately 6 weeks of gestation "
              "— Florida's most restrictive limit at the time. In her own legislative priorities "
              "statement, Passidomo declared the session 'recognized the value of all life by "
              "prohibiting abortions after six weeks,' and she shepherded the bill through the "
              "chamber as presiding officer.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://en.wikipedia.org/wiki/Kathleen_Passidomo"]),
        claim("kp2", "kathleen-passidomo", "family_child_sovereignty", 0, True,
              "As Senate President, Passidomo was the leading legislative champion of Florida's "
              "universal school-choice law (HB 1, 2023), stating: 'This visionary bill makes school "
              "choice a reality for every child in every family across our great state by providing "
              "parents the chance to guide how and where the funding for their children's education "
              "is spent.' The law — effective July 1, 2023 — extended education savings accounts to "
              "ALL Florida families regardless of income, the broadest expansion of parental school "
              "choice in state history.",
              ["https://www.flsenate.gov/Media/PressReleases/Show/4426",
               "https://www.flsenate.gov/Session/Bill/2023/1/ByVersion"]),
    ]),

    # ---------- Ileana Garcia (FL SD-36, Miami-Dade, 2022-2026) ----------
    ("ileana-garcia", "FL", "Senator", [
        claim("ig1", "ileana-garcia", "biblical_marriage", 4, True,
              "Voted for Florida's Parental Rights in Education Act (HB 1557, March 2022) and "
              "gave a floor speech in support, asserting 'Gay is not a permanent thing' — explicitly "
              "opposing the normalization of LGBTQ identity among young students. The law bans "
              "classroom instruction on sexual orientation or gender identity in kindergarten "
              "through grade 3 and in any manner not age-appropriate in higher grades, directly "
              "matching the rubric's opposition to LGBTQ promotion in schools.",
              ["https://en.wikipedia.org/wiki/Ileana_Garcia",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act"]),
        claim("ig2", "ileana-garcia", "family_child_sovereignty", 0, True,
              "Has served as Chair and Vice Chair of the Florida Senate Children, Families, and "
              "Elder Affairs Committee; her support for HB 1557 (2022) includes the provision "
              "requiring schools to notify parents of any mental-health or counseling services "
              "provided to their children — a parental-rights guardrail against school overreach "
              "into family affairs. She was also named Chair of the Appropriations Committee on "
              "Criminal and Civil Justice for 2025.",
              ["https://ballotpedia.org/Ileana_Garcia",
               "https://en.wikipedia.org/wiki/Ileana_Garcia"]),
    ]),

    # ---------- Gayle Harrell (FL SD-31, Stuart/Martin County, re-elected 2024) ----------
    ("gayle-harrell", "FL", "Senator", [
        claim("gh1", "gayle-harrell", "sanctity_of_life", 0, True,
              "Endorsed by Florida Right to Life; voted yes on both Florida's 15-week abortion ban "
              "(HB 5, 2022) and the 6-week 'Heartbeat Protection Act' (SB 300, 2023) — two "
              "consecutive votes making Florida one of the nation's most protective states for the "
              "unborn. Her record spans decades in the Florida House (2000–2008, 2010–2018) and "
              "the Florida Senate (2018–present).",
              ["https://ballotpedia.org/Gayle_Harrell",
               "https://choicetracker.org/fl/people/gayle-harrell/191889408"]),
        claim("gh2", "gayle-harrell", "self_defense", 1, True,
              "Earned the endorsement of the National Rifle Association of America during her "
              "congressional campaign; has maintained a consistent pro-gun voting record across "
              "decades in the Florida House and Senate, opposing additional restrictions on "
              "firearm ownership and use — in alignment with the rubric's defense of the Second "
              "Amendment against red-flag laws, assault-weapon bans, and magazine limits.",
              ["https://ballotpedia.org/Gayle_Harrell",
               "https://en.wikipedia.org/wiki/Gayle_Harrell"]),
    ]),

    # ---------- Don Gaetz (FL SD-1, Niceville/Northwest FL; Senate Pres. 2012-14; re-elected 2024) ----------
    ("don-gaetz", "FL", "Senator", [
        claim("dg1", "don-gaetz", "family_child_sovereignty", 0, True,
              "As Florida Senate Education Committee Chairman and Senate President (2012–2014), "
              "Gaetz sponsored legislation raising academic standards, expanding what Florida "
              "students are tested on, mandating honors diplomas for high achievers, and "
              "introducing world-language instruction in elementary schools — an excellence-first "
              "posture that lifts expectations and community accountability over bureaucratic "
              "compliance. He is known as one of the architects of Florida's education-reform era.",
              ["https://en.wikipedia.org/wiki/Don_Gaetz",
               "https://ballotpedia.org/Don_Gaetz"]),
        claim("dg2", "don-gaetz", "industry_capture", 0, True,
              "In January 2026, Gaetz filed legislation with Rep. Snyder to improve access and "
              "accountability in Florida's Medicaid managed-care program, requiring managed-care "
              "plans to meet basic benefit standards, ensuring able-bodied adults on Medicaid are "
              "on a path to self-sufficiency, and enhancing oversight and transparency for Florida "
              "taxpayers — a direct check on opaque managed-care and pharmaceutical intermediaries "
              "that profit from government health programs without adequate public accountability.",
              ["https://www.flsenate.gov/PublishedContent/Offices/Senator/"
               "Senator_Gaetz_and_Representative_Snyder_to_File_Key_Legislation_to_Improve_"
               "Access_and_Accountability_in_Floridas_Medicaid_Program.pdf",
               "https://en.wikipedia.org/wiki/Don_Gaetz"]),
    ]),

    # ---------- Yvette Benarroch (FL HD-81, Collier County; sworn Nov 2024; USAF veteran) ----------
    ("yvette-benarroch", "FL", "Representative", [
        claim("yb1", "yvette-benarroch", "border_immigration", 2, True,
              "As a member of the Florida House Republican majority in January 2025, voted as part "
              "of the unanimous R bloc for the TRUMP Act (SB 2B / HB 1B, special session Jan 2025) "
              "— which created a new state Office of Immigration Enforcement, required all Florida "
              "law enforcement agencies to comply with federal immigration detainers, and dedicated "
              "approximately $515 million to immigration enforcement cooperation, establishing an "
              "explicit anti-sanctuary mandate statewide.",
              ["https://www.flsenate.gov/Session/Bill/2025B/1B",
               "https://ballotpedia.org/Yvette_Benarroch"]),
        claim("yb2", "yvette-benarroch", "sanctity_of_life", 0, True,
              "Rated 'Anti-Choice' by the Florida Choice Tracker, reflecting her legislative "
              "votes against abortion access in the 2025 Florida House session. An Air Force "
              "Desert Storm veteran (1990–1992) and self-described 'proud conservative,' "
              "Benarroch campaigns on 'strong family values' and is in alignment with Florida's "
              "existing 6-week heartbeat law and the rubric's protection of life from conception.",
              ["https://choicetracker.org/fl/people/yvette-benarroch/290652160",
               "https://ballotpedia.org/Yvette_Benarroch"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
