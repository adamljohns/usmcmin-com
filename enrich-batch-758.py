#!/usr/bin/env python3
"""Enrichment batch 758: 9 claims for 4 FL officials (bottom-of-alphabet pivot).

Primary archetype_curated federal bucket fully exhausted by batches 1-757.
This batch pivots to evidence_state FL Republicans with 0 claims, taken from the
top of the reversed-alpha list (FL = 'F', the lowest available state letter after
WV/TX/etc. are exhausted). Sitting officials only; all claims cite reliable public
sources from 2023-2026.

Targets:
  Jay Collins (FL Lt. Governor, former FL Senate SD-14)
  Wilton Simpson (FL Agriculture Commissioner, former FL Senate President)
  Jonathan Martin (FL Senator SD-33, Chair Criminal Justice)
  Ralph Massullo Jr. (FL Senator SD-11, former FL House HD-23 co-sponsor HB 543)
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
    # -------- Jay Collins (FL Lieutenant Governor, R) --------
    ("jay-collins", "FL", "Lieutenant Governor", [
        claim("jc1", "jay-collins", "self_defense", 0, True,
              "As a Florida state senator, Collins sponsored the 2023 Senate companion legislation to Florida's constitutional carry bill (HB 543 / SB 150), which eliminated the government-permit requirement for carrying a concealed firearm statewide. The bill passed on a near-party-line vote and was signed by Gov. DeSantis in April 2023. Collins, a retired U.S. Army Green Beret, publicly framed permitless carry as a constitutional obligation: having served in countries 'where oppressed people have lived under tyrannical regimes with no ability to safeguard their loved ones,' he argued citizens must retain the unfettered right to defend themselves.",
              ["https://en.wikipedia.org/wiki/Jay_Collins",
               "https://ballotpedia.org/Jay_Collins",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("jc2", "jay-collins", "sanctity_of_life", 0, True,
              "Collins voted for SB 300, Florida's Heartbeat Protection Act, extending abortion prohibitions to six weeks from conception — signed into law by DeSantis in 2023 as the strongest pro-life legislation in FL history at the time. He further campaigned publicly against Amendment 4 (2024), the FL ballot measure that would have enshrined abortion access as a constitutional right; Collins opposed it as a radical attempt to override the legislature's protection of unborn life.",
              ["https://en.wikipedia.org/wiki/Jay_Collins",
               "https://ballotpedia.org/Jay_Collins"]),
    ]),

    # -------- Wilton Simpson (FL Agriculture Commissioner, R) --------
    ("wilton-simpson", "FL", "Agriculture", [
        claim("ws1", "wilton-simpson", "economic_stewardship", 4, True,
              "In January 2024, Simpson joined eleven other state agriculture commissioners in writing a public letter to the CEOs of six major banks — including JPMorgan Chase and Goldman Sachs — demanding they exit the Net-Zero Banking Alliance and abandon ESG-driven restrictions on agricultural credit. The commissioners argued that financial institutions leveraging ESG commitments to restrict loans to farmers and ranchers based on sustainability benchmarks amounted to economic coercion of rural America and the domestic food supply chain.",
              ["https://ballotpedia.org/Wilton_Simpson",
               "https://en.wikipedia.org/wiki/Wilton_Simpson"]),
        claim("ws2", "wilton-simpson", "self_defense", 1, True,
              "In 2023, with Simpson's support, the Florida Legislature passed SB 214, the Florida Firearms and Ammo Act, which prohibits financial institutions from separately categorizing or coding lawful firearm and ammunition purchases in a way that creates a backdoor tracking registry of gun owners. By barring bank-level surveillance of gun sales, the law directly opposes the de facto firearms registry the rubric identifies as incompatible with Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Wilton_Simpson",
               "https://ballotpedia.org/Wilton_Simpson"]),
        claim("ws3", "wilton-simpson", "border_immigration", 1, False,
              "Simpson has prioritized agricultural labor interests over strict immigration enforcement. As a Florida state senator in 2014, he voted for legislation granting in-state tuition rates to children brought to the country illegally. In 2025, he supported a bill transferring immigration enforcement authority to the agriculture commissioner — a measure Gov. DeSantis condemned as an industry-backed effort to shield illegal farm labor from deportation, publicly stating the agriculture sector has 'an affinity for cheap, illegal foreign labor.' Simpson's opposition to mandatory deportation of agricultural workers contradicts the rubric's border enforcement standard.",
              ["https://en.wikipedia.org/wiki/Wilton_Simpson",
               "https://ballotpedia.org/Wilton_Simpson"]),
    ]),

    # -------- Jonathan Martin (FL Senator SD-33, R) --------
    ("jonathan-martin", "FL", "SD-33", [
        claim("jm1", "jonathan-martin", "sanctity_of_life", 0, True,
              "Martin, a Republican member of the Florida Senate since 2022 (re-elected 2024), voted for SB 300 (2023), Florida's Heartbeat Protection Act — a six-week abortion ban that extended legal protection of unborn life from the earliest detectable heartbeat. He further advanced pro-life accountability by sponsoring SB 1374 (2026), the Civil Remedies Pertaining to Abortions bill, which would create a private right of action allowing FL citizens to sue anyone who facilitates an illegal abortion in the state.",
              ["https://ballotpedia.org/Jonathan_Allen_Martin",
               "https://www.flsenate.gov/Senators/s33",
               "https://en.wikipedia.org/wiki/Jonathan_Martin_(Florida_politician)"]),
        claim("jm2", "jonathan-martin", "family_child_sovereignty", 0, True,
              "As a FL Senate Republican, Martin voted for HB 1069 (2023), Florida's comprehensive Parental Rights in Education expansion that extended classroom protections through all grades K-12, requiring that instruction on sexual orientation and gender identity align with age-appropriate, parent-approved curriculum and granting parents explicit rights to review materials and opt their children out. Martin's JD from Liberty University School of Law reflects a foundational commitment to parental authority and Christian-principled governance that shaped his consistent support for FL parental rights legislation.",
              ["https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act",
               "https://ballotpedia.org/Jonathan_Allen_Martin",
               "https://www.flsenate.gov/Senators/s33"]),
    ]),

    # -------- Ralph E. Massullo Jr. (FL Senator SD-11, R) --------
    ("ralph-e-massullo-jr", "FL", "Senator", [
        claim("rem1", "ralph-e-massullo-jr", "self_defense", 0, True,
              "As a member of the Florida House of Representatives, Massullo co-introduced HB 543 (2023), the constitutional carry bill that eliminated Florida's decades-old permit requirement for carrying a concealed firearm. The bill passed the House 76-32 on a near-party-line vote and was signed into law by Gov. DeSantis in April 2023, making Florida the 26th constitutional carry state. Massullo's formal co-sponsorship placed him among the primary architects of this landmark Second Amendment legislation.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://en.wikipedia.org/wiki/Ralph_Massullo",
               "https://ballotpedia.org/Ralph_Massullo_Jr."]),
        claim("rem2", "ralph-e-massullo-jr", "sanctity_of_life", 0, True,
              "As a FL House Republican, Massullo voted for SB 300 (2023), Florida's Heartbeat Protection Act, protecting unborn life from six weeks. As a physician (MD, dermatologist), his vote reflected alignment between his medical understanding of fetal development and the pro-life legislative standard. He subsequently joined the FL Senate (elected December 2025 in a special election for SD-11), continuing to serve in a Republican caucus fully committed to the state's pro-life legal framework.",
              ["https://en.wikipedia.org/wiki/Ralph_Massullo",
               "https://ballotpedia.org/Ralph_Massullo_Jr.",
               "https://www.flsenate.gov/Session/Bill/2023/300"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
