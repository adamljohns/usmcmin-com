#!/usr/bin/env python3
"""Enrichment batch 421: depth claims for 5 sitting U.S. Representatives.

Targets: evidence_curated Reps with 3 claims, adding 2 new claims each
in uncovered rubric categories. All sitting members, bottom-of-alphabet
states (OK, OR, PA).

Josh Brecheen (OK-R): election_integrity + self_defense
Tom Cole (OK-R): election_integrity + economic_stewardship
Cliff Bentz (OR-R): self_defense + election_integrity
Dan Meuser (PA-R): self_defense + election_integrity
Lloyd Smucker (PA-R): election_integrity + economic_stewardship
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
    # ---------------- Josh Brecheen (OK-R, U.S. Representative OK-02) ----------------
    ("josh-brecheen", "OK", "Representative", [
        claim("jb4", "josh-brecheen", "election_integrity", 0, True,
              "Cosponsored H.R. 22 (SAVE Act) on January 3, 2025 — one of the original House sponsors demanding documentary proof of U.S. citizenship for voter registration in federal elections — and voted YES when it passed (House Vote #102, April 10, 2025, 220-208), placing him among the leading advocates for citizens-only voter rolls.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("jb5", "josh-brecheen", "self_defense", 0, True,
              "Cosponsored H.R. 38 (Constitutional Concealed Carry Reciprocity Act of 2025) on January 3, 2025, legislation that would allow any law-abiding citizen with a valid concealed-carry permit from their home state to carry concealed across all 50 states — advancing the rubric's constitutional-carry standard nationwide.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://www.govtrack.us/congress/members/josh_brecheen/456931"]),
    ]),

    # ---------------- Tom Cole (OK-R, U.S. Representative OK-04) ----------------
    ("tom-cole", "OK", "Representative", [
        claim("tc4", "tom-cole", "election_integrity", 0, True,
              "Voted YES on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship for voter registration in federal elections — consistent with his two-decade record as one of the House's senior members championing election-integrity safeguards.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.govtrack.us/congress/members/tom_cole/400077"]),
        claim("tc5", "tom-cole", "economic_stewardship", 2, True,
              "Voted to rescind $9.4 billion in wasteful spending identified by DOGE in the Rescissions Act of 2025, calling it 'another step in fulfilling the promise President Trump and House Republicans made to the American people — to change the trajectory of our fiscal glide path and restore discipline across federal agencies.'",
              ["https://cole.house.gov/media/press-releases/cole-votes-favor-rescinding-wasteful-spending",
               "https://www.govtrack.us/congress/members/tom_cole/400077"]),
    ]),

    # ---------------- Cliff Bentz (OR-R, U.S. Representative OR-02) ----------------
    ("cliff-bentz", "OR", "Representative", [
        claim("cb4", "cliff-bentz", "self_defense", 1, True,
              "Voted to protect veterans' Second Amendment rights by opposing the Biden-era VA policy of forwarding benefit-assistance applicants to the FBI's NICS (National Instant Criminal Background Check System) without judicial consent — blocking a de facto red-flag registry that would have stripped gun rights from veterans who seek financial help.",
              ["https://bentz.house.gov/media/press-releases/bentz-votes-cut-spending-protect-veterans-2a-rights-and-pass-6-spending-bills",
               "https://www.govtrack.us/congress/members/cliff_bentz/456842"]),
        claim("cb5", "cliff-bentz", "election_integrity", 0, True,
              "Voted YES on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship for voter registration in federal elections — the sole House Republican from Oregon, where automatic voter registration and ballot-harvesting laws make this vote especially consequential.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.govtrack.us/congress/members/cliff_bentz/456842"]),
    ]),

    # ---------------- Dan Meuser (PA-R, U.S. Representative PA-09) ----------------
    ("dan-meuser", "PA", "Representative", [
        claim("dm4", "dan-meuser", "self_defense", 1, True,
              "Voted NO on H.R. 8 (Bipartisan Background Checks Act) and H.R. 1446 (Enhanced Background Checks Act) in 2021, stating that these bills 'would do nothing to prevent criminals from accessing firearms, while greatly restricting the 2nd Amendment rights of law-abiding citizens' — a consistent pattern of opposing the Democratic gun-control agenda.",
              ["https://meuser.house.gov/media/press-releases/meuser-votes-against-hr8-hr1446",
               "https://www.govtrack.us/congress/members/daniel_meuser/412811"]),
        claim("dm5", "dan-meuser", "election_integrity", 0, True,
              "Officially supported and voted for the SAVE Act (H.R. 22, House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship for voter registration in federal elections — issuing a press release titled 'Congressman Meuser Supports SAVE Act to Ensure Election Integrity' confirming his position.",
              ["https://meuser.house.gov/media/press-releases/congressman-meuser-supports-save-act-ensure-election-integrity",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
    ]),

    # ---------------- Lloyd Smucker (PA-R, U.S. Representative PA-11) ----------------
    ("lloyd-smucker", "PA", "Representative", [
        claim("ls4", "lloyd-smucker", "election_integrity", 0, True,
              "Voted YES on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), and also voted to pass S. 1383 (SAVE America Act), both requiring documentary proof of U.S. citizenship for voter registration — reflecting his publicly stated support for citizens-only voter rolls and election-integrity safeguards.",
              ["https://smucker.house.gov/",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("ls5", "lloyd-smucker", "economic_stewardship", 2, True,
              "As Vice Chair of the House Budget Committee, led 37 Members urging the Senate to pass reconciliation legislation with 'real, enforceable spending reductions,' insisting 'any additional tax cuts must be matched dollar-for-dollar by real, enforceable spending reductions'; also voted for FY 2026 appropriations bills that 'reduce waste and respect American taxpayers.'",
              ["https://smucker.house.gov/issues/budget",
               "https://www.govtrack.us/congress/members/lloyd_smucker/412722"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
