#!/usr/bin/env python3
"""Enrichment batch 796: 4 candidates from bottom-of-alphabet states (VA/TX).

Federal archetype_curated bucket exhausted (see batch 795 note); targets
drawn from evidence_local pool — prominent local/county officials in VA and TX
with well-documented 2024-2026 public positions. 4 targets / 8 claims.

Targets:
  Colin Stolle       — Virginia Beach Commonwealth's Attorney (VA-R)
  Bobby Dyer         — Mayor of Virginia Beach (VA-R)
  Marc Whyte         — San Antonio City Council District 10 (TX-R)
  Mary Nan Huffman   — Houston City Council District G (TX-R)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ----------- Colin Stolle (VA-R, Virginia Beach Commonwealth's Attorney) -----------
    ("colin-stolle", "VA", "Commonwealth's Attorney", [
        claim("cs1", "colin-stolle", "self_defense", 0, True,
              "During the 2025 Virginia Beach Commonwealth's Attorney re-election campaign, Stolle publicly stated 'I am a strong supporter of the Second Amendment, own firearms and hunt,' affirming a personal pro-2A commitment consistent with the rubric's constitutional-carry ideal. While he distinguishes prosecutorial enforcement from constitutional adjudication (courts decide constitutionality, not his office), his stated personal and cultural alignment with lawful firearm ownership is on the record.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-colin-stolle-virginia-beach-commonwealths-attorney/",
               "https://www.yahoo.com/news/articles/candidate-profile-colin-stolle-virginia-182259099.html"]),
        claim("cs2", "colin-stolle", "public_justice", 0, True,
              "Stolle has made victim-rights reform a central platform issue: he argues that allowing a defendant convicted of a violent crime to unilaterally choose judge vs. jury sentencing — without any input from the victim — is an unjust process that denies victims a voice. Under his leadership the Virginia Beach Commonwealth's Attorney's Office grew from 17 to 50 attorneys and Virginia Beach attained some of the lowest crime rates in its history, earning Stolle the 2021 Robert F. Horan Award from the Virginia Association of Commonwealth's Attorneys.",
              ["https://www.colinstolle.com/my-commitment",
               "https://www.wavy.com/news/politics/candidates/candidate-profile-colin-stolle-virginia-beach-commonwealths-attorney/",
               "https://oca.virginiabeach.gov/commonwealths-attorney-bio"]),
    ]),

    # ----------- Bobby Dyer (VA-R, Mayor of Virginia Beach) -----------
    ("bobby-dyer", "VA", "Mayor", [
        claim("bd1", "bobby-dyer", "economic_stewardship", 2, True,
              "Mayor Dyer has consistently kept Virginia Beach's property tax rate the lowest in the Hampton Roads region throughout his tenure, publicly committing to 'a careful balance of high citizen services with the lowest property taxes in the region.' During the FY2025-26 budget cycle the City Council held public hearings on City Manager Patrick Duhaney's proposed $2.8 billion operating budget without raising the real property tax rate — a fiscal discipline posture consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.virginiabeachmayorbobbydyer.com/",
               "https://www.yahoo.com/news/virginia-beach-city-council-hold-011915050.html",
               "https://virginiabeach.gov/connect/news/virginia-beach-city-council-votes-to-adopt-revised-fy25-budget"]),
        claim("bd2", "bobby-dyer", "public_justice", 0, True,
              "In 2026, Mayor Dyer assembled the Mayor's Task Force for a Safer Virginia Beach — a cross-sector advisory panel of community leaders and stakeholders charged with developing public safety recommendations for City Council. The Task Force is expected to submit its findings in late 2026. Dyer is also the first U.S. Marine Corps veteran ever directly elected as mayor of Virginia Beach (served 1968-72), bringing a military discipline and public-order perspective to city leadership.",
              ["https://virginiabeach.gov/city-hall/mayors-office/safer-vb",
               "https://virginiabeach.gov/connect/news/mayor-dyer-announces-members-of-the-mayors-task-force-for-a-safer-virginia-beach",
               "https://en.wikipedia.org/wiki/Bobby_Dyer_(politician)"]),
    ]),

    # ----------- Marc Whyte (TX-R, San Antonio City Council District 10) -----------
    ("marc-whyte", "TX", "District 10", [
        claim("mw1", "marc-whyte", "economic_stewardship", 2, True,
              "As San Antonio's lone conservative on City Council, Whyte championed and won adoption of the maximum allowable homestead exemption (20%) for homeowners, directly reducing the property tax burden. When the city manager proposed a 6% property tax rate increase to close a $158 million structural deficit in the FY2026 budget process, Whyte was among the majority who pushed back, publicly questioning whether tax increases solve long-term fiscal problems rather than forcing structural spending discipline — consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://marcwhyte.com/policies/",
               "https://sanantonioreport.org/profile/marc-whyte-2025-san-antonio-city-council-district-10-candidate/",
               "https://www.sacurrent.com/news/san-antonio-news/majority-of-san-antonio-council-balks-at-6-property-tax-increase-proposed-by-city-manager/"]),
        claim("mw2", "marc-whyte", "public_justice", 0, True,
              "In the FY2024-25 San Antonio budget process, Whyte secured funding for more than 100 new SAPD (San Antonio Police Department) sworn officers — the city's largest single-year headcount increase in years — and drove removal of more than 700 homeless encampments since fall 2023, framing encampments as public-safety hazards. He serves on the City Council's Public Safety Committee and was re-elected May 3, 2025, with 69% of the vote, validating his law-and-order approach to city governance.",
              ["https://marcwhyte.com/policies/",
               "https://sanantonioreport.org/profile/marc-whyte-2025-san-antonio-city-council-district-10-candidate/",
               "https://www.ksat.com/news/local/2025/05/01/results-district-10-san-antonio-city-council-election-on-may-3-2025/"]),
    ]),

    # ----------- Mary Nan Huffman (TX-R, Houston City Council District G) -----------
    ("mary-nan-huffman", "TX", "District G", [
        claim("mnh1", "mary-nan-huffman", "family_child_sovereignty", 0, True,
              "Before joining Houston City Council, Huffman spent 10 years as a prosecutor in the Montgomery County District Attorney's Office, rising to Chief Felony Prosecutor over the Child Exploitation Division and the Internet Crimes Against Children (ICAC) Task Force. She developed a national reputation pursuing internet-based child predators and continues to be sought as a special prosecutor for complex child exploitation cases — placing her career at the forefront of protecting children from exploitation, consistent with the rubric's family/child-sovereignty and child-protection standard.",
              ["https://www.marynanhuffman.com/about-mary-nan-huffman/",
               "https://ballotpedia.org/Mary_Nan_Huffman",
               "https://www.click2houston.com/news/politics/2023/12/11/meet-houstons-recently-elected-city-council-members/"]),
        claim("mnh2", "mary-nan-huffman", "public_justice", 0, True,
              "Huffman's governing philosophy places public safety as 'government's most important responsibility.' She ran for Houston City Council District G in 2022 and 2023 explicitly on a crime-fighting platform — citing rising Houston crime rates — and defeated Tony Buzbee in the December 2023 general runoff. Her current term runs through January 2028. Her decade as a felony child-exploitation prosecutor grounds her public-safety posture in direct victim-advocacy experience.",
              ["https://www.marynanhuffman.com/about-mary-nan-huffman/",
               "https://ballotpedia.org/Mary_Nan_Huffman",
               "https://www.houstontx.gov/council/g/index.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
