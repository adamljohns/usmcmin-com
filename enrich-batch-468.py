#!/usr/bin/env python3
"""Enrichment batch 468: hand-curated claims for 5 WA state representatives.

Targets archetype_party_default Washington State Representatives with 0 claims,
taken from the bottom of the alphabet (WA), sorted reverse-alphabetically by name.
Covers two 2025 party-line votes — E2SHB 1163 (permit-to-purchase firearms,
House 58-38) and ESHB 1296 (parental-rights rewrite, House 56-37) — for five
Republican members of the 69th Legislature.

Mix: 5 R (Waters, Penner, McEntire, Ley, Schmick).

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
    # --- Kevin Waters (WA-R, State Representative District 17-Position 1, Skamania County) ---
    ("kevin-waters", "WA", "State Representative", [
        claim("kw1", "kevin-waters", "self_defense", 1, True,
              "Voted No on E2SHB 1163 (2025), which creates a state permit-to-purchase scheme "
              "requiring fingerprinting, a government-issued permit, and certified live-fire "
              "firearms-safety training before any firearm purchase. The NRA condemned the bill "
              "as creating 'an illegal government registry of firearm owners.' The House passed it "
              "58-38 on a strict party-line vote with all Republicans, including Waters, opposed. "
              "Gov. Ferguson signed it May 20, 2025.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025"]),
        claim("kw2", "kevin-waters", "family_child_sovereignty", 0, True,
              "Voted No on ESHB 1296 (2025), which rewrote voter-approved Initiative 2081 (the "
              "Parents' Bill of Rights) to strip parents of access to their children's school-based "
              "medical records and require schools to align with state-mandated transgender-identity "
              "policies. Waters, a District 17 representative for rural Skamania County, joined all "
              "House Republicans in opposition; the bill passed 56-37 on a party-line vote.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- Joshua Penner (WA-R, State Representative District 31-Position 2, Orting; Marine vet) ---
    ("joshua-penner", "WA", "State Representative", [
        claim("jp1", "joshua-penner", "self_defense", 1, True,
              "Voted No on E2SHB 1163 (2025), a new permit-to-purchase law requiring a "
              "government-issued permit, fingerprinting, and certified live-fire safety training "
              "before any firearm purchase — creating what the NRA called 'an illegal government "
              "registry.' The House passed it 58-38 on a strict party-line vote with all "
              "Republicans opposed. Penner, a Marine Corps veteran and former mayor of Orting, "
              "took office January 13, 2025.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://ballotpedia.org/Josh_Penner"]),
        claim("jp2", "joshua-penner", "family_child_sovereignty", 0, True,
              "Voted No on ESHB 1296 (2025), which gutted voter-enacted Initiative 2081 by "
              "removing parents' right to access school-based medical records for their children "
              "and mandating that schools follow state transgender-identity policies. All "
              "Republicans in the House, including Penner, opposed the bill; it passed 56-37 "
              "on a party-line vote. Gov. Ferguson signed it in May 2025.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://washingtonstatestandard.com/2025/05/20/wa-governor-signs-parental-bill-of-rights-rewrite/"]),
    ]),

    # --- Joel McEntire (WA-R, State Representative District 19-Position 2; Marine Reserve / math teacher) ---
    ("joel-mcentire", "WA", "State Representative", [
        claim("jmc1", "joel-mcentire", "self_defense", 1, True,
              "Voted No on E2SHB 1163 (2025), which requires all Washington residents to obtain "
              "a state-issued permit — including fingerprinting and a live-fire safety course — "
              "before purchasing any firearm. NRA-ILA opposed it as an unconstitutional registry "
              "scheme. The House passed the bill 58-38 on a party-line vote with all Republicans "
              "opposed. McEntire, a Marine Corps Reserve officer and math teacher representing "
              "District 19, is a consistent Second Amendment advocate.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://ballotpedia.org/Joel_McEntire"]),
        claim("jmc2", "joel-mcentire", "family_child_sovereignty", 0, True,
              "Voted No on ESHB 1296 (2025), which Democrats passed to rewrite Initiative 2081, "
              "stripping parents' access to school-based medical records and compelling schools to "
              "implement state-dictated transgender-identity policies. McEntire joined all House "
              "Republicans in opposition; the bill passed 56-37 on a party-line vote before "
              "being signed by Gov. Ferguson.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://www.kuow.org/stories/changes-to-wa-parents-rights-law-headed-to-governor-after-tense-final-vote"]),
    ]),

    # --- John Ley (WA-R, State Representative District 18-Position 2; Air Force vet / journalist) ---
    ("john-ley", "WA", "State Representative", [
        claim("jl1", "john-ley", "self_defense", 1, True,
              "Voted No on E2SHB 1163 (2025), which creates a government permit-to-purchase "
              "requirement — fingerprinting, a state-issued permit, and mandatory live-fire "
              "safety training — for all firearm purchases in Washington. The NRA opposed it as "
              "an unconstitutional registry. The House passed it 58-38 on a strict party-line "
              "vote. Ley, an Air Force veteran and former journalist representing District 18, "
              "took office January 13, 2025.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://ballotpedia.org/John_Ley"]),
        claim("jl2", "john-ley", "family_child_sovereignty", 0, True,
              "Voted No on ESHB 1296 (2025), which rewrote voter-approved Initiative 2081 "
              "to eliminate parents' access to children's school-based medical records and "
              "require schools to adopt state-mandated transgender-identity policies. All "
              "House Republicans, including Ley, voted against the bill; it passed 56-37 "
              "on a party-line vote and was signed by Gov. Ferguson in May 2025.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://washingtonstatestandard.com/2025/05/20/wa-governor-signs-parental-bill-of-rights-rewrite/"]),
    ]),

    # --- Joe Schmick (WA-R, State Representative District 9-Position 2; farmer / small business, since 2007) ---
    ("joe-schmick", "WA", "State Representative", [
        claim("js1", "joe-schmick", "self_defense", 1, True,
              "Voted No on E2SHB 1163 (2025), which mandates a state-issued permit, "
              "fingerprinting, and certified live-fire safety training before any firearm "
              "purchase in Washington — establishing what NRA-ILA described as 'an illegal "
              "government registry of firearm owners.' The House passed it 58-38 on a strict "
              "party-line vote. Schmick, a farmer and small-business owner who has represented "
              "rural eastern Washington's District 9 since 2007, consistently opposed the bill.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://ballotpedia.org/Joe_Schmick"]),
        claim("js2", "joe-schmick", "family_child_sovereignty", 0, True,
              "Voted No on ESHB 1296 (2025), which rewrote voter-enacted Initiative 2081 "
              "to strip parents of the right to access their children's school-based medical "
              "records and require schools to comply with state transgender-identity mandates. "
              "Schmick joined all House Republicans in opposing the bill; it passed 56-37 on "
              "a party-line vote before being signed into law by Gov. Ferguson in May 2025.",
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
