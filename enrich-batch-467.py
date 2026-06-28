#!/usr/bin/env python3
"""Enrichment batch 467: hand-curated claims for 5 WA state representatives.

Targets archetype_party_default Washington State Representatives with 0 claims,
taken from the bottom of the alphabet (WA). Covers two 2025 party-line
votes — HB 1163 (gun permit-to-purchase, House 58-38) and ESHB 1296 (parental
rights rewrite, House 56-37) — for five Republican members of the 69th Legislature.

Mix: 5 R (Marshall, Klicker, Steele, Keaton, Valdez).

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
    # --- Matt Marshall (WA-R, State Representative District 2-Position 2, Eatonville) ---
    ("matt-marshall", "WA", "State Representative", [
        claim("mm1", "matt-marshall", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), which requires all firearm purchasers to obtain a government-issued permit and complete a certified firearms-safety course before buying any gun; signed the minority report urging 'do not pass' and argued on the floor that 'passing legislation that further impedes our constitutionally protected rights is irresponsible.' The bill passed the House 58-38 on a strict party-line vote.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://www.thecentersquare.com/washington/article_a955165e-f61d-11ef-bdf1-8749bbf8574f.html"]),
        claim("mm2", "matt-marshall", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), which rewrote voter-approved Initiative 2081 (the parental bill of rights) to remove parents' access to children's school-based medical records, allow schools to delay records responses, and mandate alignment with state transgender-identity policies; the House passed it 56-37 on a party-line vote.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- Mark Klicker (WA-R, State Representative District 16-Position 1, Walla Walla) ---
    ("mark-klicker", "WA", "State Representative", [
        claim("mk1", "mark-klicker", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), which creates a new government permit-to-purchase scheme requiring fingerprinting and a certified firearms-safety course before any firearm purchase; submitted a floor amendment in opposition during House debate. The bill passed 58-38 on a strict party-line House vote with all Republicans opposed.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://www.nraila.org/articles/20250304/washington-several-gun-control-bills-primed-for-house-floor"]),
        claim("mk2", "mark-klicker", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), which gutted voter-approved Initiative 2081 by stripping parents' access to school medical records and requiring schools to follow state-mandated transgender-identity policies; the House passed the bill 56-37 on a party-line vote with Republicans unified in opposition.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- Mike Steele (WA-R, State Representative District 12-Position 2) ---
    ("mike-steele", "WA", "State Representative", [
        claim("ms1", "mike-steele", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), the Democratic-backed permit-to-purchase bill requiring a state-issued permit and completed firearms-safety training before any gun purchase; the measure passed the House 58-38 on a strict party-line vote with all Republicans including Steele opposed.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://www.nraila.org/articles/20250304/washington-several-gun-control-bills-primed-for-house-floor"]),
        claim("ms2", "mike-steele", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), which rewrote voter-enacted Initiative 2081, eliminating parents' right to access their children's school medical records and directing schools to adopt state transgender-identity mandates; the House passed it 56-37 on a party-line vote with Republicans unanimously opposed.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- Michael Keaton (WA-R, State Representative District 25-Position 1) ---
    ("michael-keaton", "WA", "State Representative", [
        claim("mke1", "michael-keaton", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), which mandates a state-issued permit and certified firearms-safety course before purchasing any firearm — a new pre-purchase government approval regime. The bill passed the House 58-38 on a party-line vote with all Republicans opposed. Keaton, a 20-year Air Force F-16 combat pilot, took office January 13, 2025.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://ballotpedia.org/Michael_Keaton"]),
        claim("mke2", "michael-keaton", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), a Democratic rewrite of voter-approved Initiative 2081 that stripped parents' access to school-based medical records and required schools to adopt state-mandated transgender-identity policies; the House passed it 56-37 on a party-line vote with Republicans unified in opposition.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- Michelle Valdez (formerly Caldier; WA-R, State Representative District 26-Position 2, Gig Harbor) ---
    ("michelle-valdez", "WA", "State Representative", [
        claim("mv1", "michelle-valdez", "self_defense", 1, True,
              "Voted No on WA HB 1163 (2025), which establishes a permit-to-purchase regime requiring fingerprinting and a government-certified firearms-safety course before any firearm purchase; the House passed it 58-38 on a party-line vote with all Republicans opposed. Valdez (formerly Caldier) is a six-term Republican serving Gig Harbor and parts of Pierce and Kitsap counties.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://washingtonstatestandard.com/briefs/six-term-gop-lawmaker-wont-seek-reelection-to-wa-house/"]),
        claim("mv2", "michelle-valdez", "family_child_sovereignty", 0, True,
              "Voted No on WA ESHB 1296 (2025), which rewrote voter-approved Initiative 2081 by removing parents' access to children's school medical records and mandating schools follow state transgender-identity policies; the House passed it 56-37 on a party-line vote with Republicans unified in opposition.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
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
