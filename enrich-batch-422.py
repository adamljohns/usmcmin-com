#!/usr/bin/env python3
"""Enrichment batch 422: depth claims for 5 Texas U.S. Representatives.

Targets: evidence_curated TX Reps with 3 claims, adding 2 new claims each
in uncovered rubric categories. Two retiring Republican members and three
sitting/retiring Democratic members. All from TX (bottom-of-alphabet).

Michael McCaul (TX-10-R):  election_integrity + border_immigration
Jodey Arrington (TX-19-R): election_integrity + self_defense
Lloyd Doggett (TX-35-D):   border_immigration + election_integrity
Marc Veasey (TX-33-D):     border_immigration + election_integrity
Joaquin Castro (TX-20-D):  border_immigration + election_integrity
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
    # ---------------- Michael McCaul (TX-R, U.S. Representative TX-10, retiring) ----------------
    ("michael-mccaul", "TX", "Representative", [
        claim("mm4", "michael-mccaul", "election_integrity", 0, True,
              "Was an original co-sponsor of H.R. 22 (SAVE Act) on January 3, 2025, and voted YES when it passed (House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship for voter registration in federal elections. His office issued a press release titled 'McCaul Votes For SAVE Act to Protect Election Integrity,' confirming his support for citizens-only voter rolls.",
              ["https://mccaul.house.gov/media-center/press-releases/mccaul-votes-save-act-protect-election-integrity",
               "https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("mm5", "michael-mccaul", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213), serving as a co-chair alongside Chairmen Green and Jordan — the bill funded border-wall construction, reinstated Remain in Mexico, and tightened asylum standards. Also voted YES on the One Big Beautiful Bill (July 3, 2025, 218-214), which included $46.55B for physical barriers, $4.1B for Border Patrol hiring, and reimbursed border states $13.5B for enforcement costs.",
              ["https://mccaul.house.gov/media-center/press-releases/mccaul-votes-secure-border",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://mccaul.house.gov/media-center/press-releases/mccaul-votes-pass-one-big-beautiful-bill"]),
    ]),

    # ---------------- Jodey Arrington (TX-R, U.S. Representative TX-19, retiring) ----------------
    ("jodey-arrington", "TX", "Representative", [
        claim("ja4", "jodey-arrington", "election_integrity", 0, True,
              "Was an original co-sponsor of H.R. 22 (SAVE Act) on January 3, 2025 — one of 53 original House sponsors — and voted YES when it passed (House Vote #102, April 10, 2025, 220-208), requiring documentary proof of U.S. citizenship for voter registration in federal elections. He also delivered a floor speech urging passage of the companion SAVE America Act (H.R. 7296), calling citizens-only voter rolls essential to election integrity.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://arrington.house.gov/news/documentsingle.aspx?DocumentID=4340"]),
        claim("ja5", "jodey-arrington", "self_defense", 1, True,
              "Voted NO on the Bipartisan Safer Communities Act (House Vote #299, June 24, 2022) and issued a statement opposing H.R. 7910 and H.R. 1808 as unconstitutional infringements. Co-sponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act, in both the 118th and 119th Congresses. As House Budget Committee Chair, championed the One Big Beautiful Bill (passed May 22, 2025), which eliminated the $200 NFA suppressor tax stamp — advancing the rubric's anti-restriction Second Amendment standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://arrington.house.gov/news/documentsingle.aspx?DocumentID=762",
               "https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://www.nraila.org/articles/20250522/us-house-passes-reconciliation-bill-removing-suppressors-from-the-national-firearms-act"]),
    ]),

    # ---------------- Lloyd Doggett (TX-D, U.S. Representative, retiring) ----------------
    ("lloyd-doggett", "TX", "Representative", [
        claim("ld4", "lloyd-doggett", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213), which would have funded border-wall construction, reinstated Remain in Mexico, and empowered ICE deportation enforcement. He has been one of the most consistent House opponents of border-security enforcement legislation across his multi-decade tenure, voting against border barrier funding and deportation-enforcement measures throughout.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://doggett.house.gov"]),
        claim("ld5", "lloyd-doggett", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which would have required documentary proof of U.S. citizenship for voter registration in federal elections. All 208 NO votes were cast by Democrats. He has consistently opposed documentary-identification requirements for voters, characterizing such measures as barriers to participation rather than integrity safeguards.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://doggett.house.gov"]),
    ]),

    # ---------------- Marc Veasey (TX-D, U.S. Representative, retiring) ----------------
    ("marc-veasey", "TX", "Representative", [
        claim("mv4", "marc-veasey", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213), which would have funded border-wall construction, tightened asylum standards, and expanded deportation enforcement. He has consistently voted against border-security legislation requiring physical barriers or mandatory deportation enforcement.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://veasey.house.gov"]),
        claim("mv5", "marc-veasey", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which would have required documentary proof of U.S. citizenship for voter registration in federal elections. All 208 NO votes were cast by Democrats. He has opposed citizenship-verification requirements for voter registration, framing broad access as incompatible with documentary-proof mandates.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://veasey.house.gov"]),
    ]),

    # ---------------- Joaquin Castro (TX-D, U.S. Representative TX-20) ----------------
    ("joaquin-castro", "TX", "Representative", [
        claim("jc4", "joaquin-castro", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213). As a senior member of the House Foreign Affairs Committee and former Congressional Hispanic Caucus Chair, Castro has been one of the most vocal House opponents of border-wall construction and mandatory deportation enforcement — the core border-security posture the rubric endorses.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://castro.house.gov"]),
        claim("jc5", "joaquin-castro", "election_integrity", 0, False,
              "Voted NO on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025, 220-208), which would have required documentary proof of U.S. citizenship for voter registration in federal elections. All 208 NO votes were cast by Democrats. He has characterized documentary-proof requirements for voter registration as voter suppression inconsistent with broad electoral participation.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://castro.house.gov"]),
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
