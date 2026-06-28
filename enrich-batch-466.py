#!/usr/bin/env python3
"""Enrichment batch 466: hand-curated claims for 5 WA state senators.

Targets archetype_party_default Washington State Senators with 0 claims,
taken from the bottom of the alphabet (WA). Covers two 2025 party-line
votes — HB 1163 (gun permit-to-purchase) and ESHB 1296 (weakened
parental bill of rights) — plus sponsor/position claims for each.

Mix: 1 R (Chris Gildon) / 4 D (Robinson, Salomon, Stanford, Wilson).

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
    # ---------------- Chris Gildon (WA-R, State Senator District 25) ----------------
    ("chris-gildon", "WA", "State Senator", [
        claim("cg1", "chris-gildon", "sanctity_of_life", 0, True,
              "Publicly supports the Born Alive Abortion Survivors Protection Act, requiring health-care providers to render life-saving medical care to infants born alive after an attempted abortion — a concrete expression of his stated view that he will 'always err on the side of life.'",
              ["https://ivoterguide.com/candidate/41831/race/20738/election/1247",
               "https://ballotpedia.org/Chris_Gildon"]),
        claim("cg2", "chris-gildon", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), which requires a government-issued permit — plus a certified firearms-safety course — before purchasing any firearm. The bill passed 29-19 along strict party lines with all Republicans opposed; Gildon is the Senate Republican Caucus deputy leader.",
              ["https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate",
               "https://www.opb.org/article/2025/05/21/washington-gun-law-permit-safety-course-house-bill-1163-firearms/"]),
        claim("cg3", "chris-gildon", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), which rewrote Initiative 2081 (the voter-approved parental bill of rights) to remove parents' access to school-based medical records, allow schools to delay records responses, and mandate alignment with state transgender policies — the Senate passed it 30-19 along party lines.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # ---------------- June Robinson (WA-D, State Senator District 38) ----------------
    ("june-robinson", "WA", "State Senator", [
        claim("jr1", "june-robinson", "self_defense", 1, False,
              "Voted Yes on WA HB 1163 (2025), requiring all firearm purchasers to obtain a government-issued permit and complete a certified safety course before buying a gun; the bill passed 29-19 on a strict party-line vote. Robinson serves as Senate Ways and Means Committee Chair.",
              ["https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate",
               "https://www.axios.com/local/seattle/2025/04/23/washington-gun-permit-bill"]),
        claim("jr2", "june-robinson", "family_child_sovereignty", 0, False,
              "Voted Yes on WA ESHB 1296 (2025), which rewrote the voter-approved Initiative 2081 parental bill of rights, stripping parents' access to children's school-based medical records and requiring schools to adopt state transgender-identity policies; the Senate passed it 30-19 along party lines.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
    ]),

    # ---------------- Jesse Salomon (WA-D, State Senator District 32) ----------------
    ("jesse-salomon", "WA", "State Senator", [
        claim("js1", "jesse-salomon", "self_defense", 1, False,
              "Voted Yes on WA HB 1163 (2025), which mandates a government permit and certified firearms-safety course before purchasing any firearm in Washington; passed 29-19 on a party-line Senate vote.",
              ["https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate",
               "https://publichealth.jhu.edu/center-for-gun-violence-solutions/2025/washington-passes-permit-to-purchase-law"]),
        claim("js2", "jesse-salomon", "family_child_sovereignty", 0, False,
              "Voted Yes on WA ESHB 1296 (2025), the Democratic rewrite of Initiative 2081 that removed parents' right to access children's school medical records and mandated schools to adopt state-prescribed transgender identity policies; the bill cleared the Senate 30-19 on a party-line vote.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # ---------------- Derek Stanford (WA-D, State Senator District 1) ----------------
    ("derek-stanford", "WA", "State Senator", [
        claim("ds1", "derek-stanford", "self_defense", 1, False,
              "Voted Yes on WA HB 1163 (2025), requiring a state-issued permit and completed firearms-safety training before any gun purchase; the measure passed 29-19 along party lines. Stanford previously served on the WA House Business & Financial Services Committee before joining the Senate.",
              ["https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate",
               "https://ballotpedia.org/Derek_Stanford"]),
        claim("ds2", "derek-stanford", "family_child_sovereignty", 0, False,
              "Voted Yes on WA ESHB 1296 (2025), which gutted voter-approved parental rights by removing parents' access to school medical records and directing schools to follow state transgender-policy mandates; passed the Senate 30-19 on a party-line vote.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.thecentersquare.com/washington/article_07324883-0cbe-4c5a-b4d2-fc6e1f97c846.html"]),
    ]),

    # ---------------- Claire Wilson (WA-D, State Senator District 30) ----------------
    ("claire-wilson", "WA", "State Senator", [
        claim("cw1", "claire-wilson", "self_defense", 1, False,
              "Voted Yes on WA HB 1163 (2025), establishing a state permit-to-purchase regime that requires fingerprinting and a certified firearms-safety course before buying a gun; passed 29-19 on a party-line Senate vote.",
              ["https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate",
               "https://www.axios.com/local/seattle/2025/04/23/washington-gun-permit-bill"]),
        claim("cw2", "claire-wilson", "biblical_marriage", 4, False,
              "Sponsored and passed WA SB 5395 (2020), which mandated LGBTQ-inclusive comprehensive sexual health education in all public schools statewide — requiring age-appropriate instruction on gender identity and sexual orientation. The bill passed the Senate 28-21.",
              ["https://www.claireforsenate.com/senate-passes-wilson-bill-for-comprehensive-sexuality-health-education/",
               "https://auburnexaminer.com/sen-wilson-nationally-recognized-for-sexual-health-education-legislation/"]),
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
