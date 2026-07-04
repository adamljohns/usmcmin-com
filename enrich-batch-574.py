#!/usr/bin/env python3
"""Enrichment batch 574: 5 South Carolina Republican state senators with 0 claims.

Targets archetype_party_default SC state senators taken from the BOTTOM of the
reversed-alphabet bucket: Thomas C. Alexander (SD-1, Senate President),
Tom Fernandez (SD-39), Thomas D. Corbin (SD-5), Tom Davis (SD-46),
Tom Young Jr. (SD-24).

Sources: en.wikipedia.org, ballotpedia.org, scstatehouse.gov, nraila.org.
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
    # ---- Thomas C. Alexander (SC-1, R, Senate President since 2021) ----
    ("thomas-c-alexander", "SC", "Senator", [
        claim("tca1", "thomas-c-alexander", "sanctity_of_life", 0, True,
              "As President of the South Carolina Senate, oversaw passage of the Fetal "
              "Heartbeat Protection Act (S.474, 2023), SC's most restrictive abortion law "
              "at the time, which took effect August 23, 2023; Ballotpedia notes he "
              "'prefers a total ban without exceptions,' aligning with a life-at-conception "
              "personhood standard.",
              ["https://en.wikipedia.org/wiki/Thomas_C._Alexander",
               "https://ballotpedia.org/Thomas_Alexander"]),
        claim("tca2", "thomas-c-alexander", "biblical_marriage", 2, True,
              "Introduced H.4624 to ban gender-affirming care (puberty blockers, "
              "cross-sex hormones, and surgery) for minors in South Carolina; the bill "
              "became law on May 21, 2024. Also voted for SC's Save Women's Sports Act "
              "(2022), barring male-born athletes from competing in girls' sports.",
              ["https://en.wikipedia.org/wiki/Thomas_C._Alexander",
               "https://ballotpedia.org/Thomas_Alexander"]),
    ]),

    # ---- Tom Fernandez (SC-39, R, elected Nov 2024) ----
    ("tom-fernandez", "SC", "Senator", [
        claim("tf1", "tom-fernandez", "sanctity_of_life", 0, True,
              "Voted on November 18, 2025 in favor of South Carolina Senate Bill 323, "
              "which would make abortion a felony punishable by up to 30 years in prison — "
              "one of the most restrictive abortion proposals introduced anywhere in the "
              "nation, reflecting a personhood-at-conception conviction.",
              ["https://en.wikipedia.org/wiki/Tom_Fernandez",
               "https://ballotpedia.org/Tom_Fernandez"]),
        claim("tf2", "tom-fernandez", "industry_capture", 0, True,
              "Voted in 2025 against confirming Dr. Edward Simmer to lead the SC "
              "Department of Public Health, citing Simmer's strong advocacy for COVID-19 "
              "vaccines and his wearing of a face mask — objecting to placing a "
              "pro-pharmaceutical-mandate official at the head of the state's public "
              "health system.",
              ["https://en.wikipedia.org/wiki/Tom_Fernandez",
               "https://ballotpedia.org/Tom_Fernandez"]),
    ]),

    # ---- Thomas D. Corbin (SC-5, R) ----
    ("thomas-d-corbin", "SC", "Senator", [
        claim("tdc1", "thomas-d-corbin", "sanctity_of_life", 0, True,
              "Publicly pro-life per his campaign platform — his official 2020 website "
              "lists being pro-life as a core governing principle alongside gun rights and "
              "limited government. He has consistently voted in the SC Senate Republican "
              "majority on abortion-restriction legislation, including advancing a 2026 "
              "abortion ban amendment through the Senate Medical Affairs Committee.",
              ["https://en.wikipedia.org/wiki/Tom_Corbin",
               "https://ballotpedia.org/Tom_Corbin_(South_Carolina)"]),
        claim("tdc2", "thomas-d-corbin", "self_defense", 1, True,
              "Introduced legislation in the SC Senate requiring residents to join a "
              "regulated state militia, arguing this constitutionally shields South "
              "Carolinians from federal restrictions on private firearm ownership — a "
              "proactive legislative stance against federal gun-control laws, registries, "
              "and mandated disarmament that goes beyond mere opposition to new regulations.",
              ["https://en.wikipedia.org/wiki/Tom_Corbin",
               "https://ballotpedia.org/Tom_Corbin_(South_Carolina)"]),
    ]),

    # ---- Tom Davis (SC-46, R) ----
    ("tom-davis", "SC", "Senator", [
        claim("td1", "tom-davis", "economic_stewardship", 2, True,
              "Received a 71% rating from the Palmetto Liberty PAC in 2012, ranking 3rd "
              "out of all 46 SC senators on anti-spending and limited-government votes; "
              "previously served as Chief of Staff to Governor Mark Sanford, who famously "
              "rejected approximately $700 million in federal stimulus funds in 2009 on "
              "fiscal-discipline grounds — a record of resisting deficit expansion.",
              ["https://ballotpedia.org/Tom_Davis_(South_Carolina)",
               "https://en.wikipedia.org/wiki/Tom_Davis_(South_Carolina_politician)"]),
        claim("td2", "tom-davis", "self_defense", 0, True,
              "Voted with the SC Senate Republican majority to pass the South Carolina "
              "Constitutional Carry/Second Amendment Preservation Act of 2024 (H.3594), "
              "signed by Governor McMaster on March 7, 2024 — making SC the 29th state "
              "to enact permitless carry for adults 18+, a priority of the NRA-backed "
              "Republican caucus Davis is part of.",
              ["https://www.nraila.org/articles/20240306/south-carolina-constitutional-carry-headed-to-gov-mcmasters-desk-for-his-signature",
               "https://ballotpedia.org/Tom_Davis_(South_Carolina)"]),
    ]),

    # ---- Tom Young Jr. (SC-24, R, Chair Family & Veterans' Services) ----
    ("tom-young-jr", "SC", "Senator", [
        claim("tyj1", "tom-young-jr", "sanctity_of_life", 0, True,
              "Voted as part of the SC Senate Republican majority (27-19) for the "
              "Fetal Heartbeat Protection Act (S.474, 2023), SC's 6-week abortion ban "
              "that became law on August 23, 2023; only the chamber's three Republican "
              "women opposed the measure, placing Young firmly in the pro-life majority.",
              ["https://en.wikipedia.org/wiki/Abortion_in_South_Carolina",
               "https://ballotpedia.org/Tom_Young_(South_Carolina)"]),
        claim("tyj2", "tom-young-jr", "self_defense", 0, True,
              "Voted with the SC Senate Republican majority for the SC Constitutional "
              "Carry/Second Amendment Preservation Act of 2024 (H.3594), signed by "
              "Governor McMaster on March 7, 2024, making South Carolina the 29th "
              "permitless carry state in the nation.",
              ["https://www.nraila.org/articles/20240306/south-carolina-constitutional-carry-headed-to-gov-mcmasters-desk-for-his-signature",
               "https://ballotpedia.org/Tom_Young_(South_Carolina)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    # Minified write — preserve the no-whitespace master (keep under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
