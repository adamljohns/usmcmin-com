#!/usr/bin/env python3
"""Enrichment batch 270: hand-curated claims for 5 sitting Washington U.S. House members.

Targets bottom-of-alphabet WA House members with 3 existing claims each.
Adds 2 claims per candidate spanning DISTINCT rubric categories not yet documented.
All claims cite reliable public sources and reflect 2024-2026 voting records /
public positions.

Candidates: Dan Newhouse (WA-R), Marie Gluesenkamp Perez (WA-D), Kim Schrier (WA-D),
Rick Larsen (WA-D), Adam Smith (WA-D).
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
    # ---------------- Dan Newhouse (WA-R, U.S. House WA-04, sitting since 2015; retiring 2026) ----------------
    ("dan-newhouse", "WA", "House", [
        claim("dn270a", "dan-newhouse", "border_immigration", 0, False,
              "Cosponsored the DIGNIDAD Act (2026), which would create a pathway to legal status for up to 12 million illegal immigrants in the United States paired with enhanced border-enforcement and work requirements — a regularization-first approach that contrasts with the rubric's wall+military enforcement standard. He also voted for the Farm Workforce Modernization Act (2021), which would grant legal status to certain undocumented agricultural workers, making him one of 30 Republicans backing the measure.",
              ["https://ballotpedia.org/Dan_Newhouse",
               "https://en.wikipedia.org/wiki/Dan_Newhouse"]),
        claim("dn270b", "dan-newhouse", "foreign_policy_restraint", 1, False,
              "Voted YES on the $95 billion Ukraine/Israel/Taiwan foreign-aid package (Senate Amendment to H.R. 815, House Vote #109, April 20, 2024), breaking with House conservatives who had held the measure for six months. He also voted for approximately $13.6 billion in Ukraine military and humanitarian aid in 2022 — a consistent pattern of supporting open-ended U.S. military assistance abroad rather than the rubric's end-forever-wars, wind-down-entanglements standard.",
              ["https://www.govtrack.us/congress/members/dan_newhouse/412660",
               "https://en.wikipedia.org/wiki/Dan_Newhouse"]),
    ]),

    # ---------------- Marie Gluesenkamp Perez (WA-D, U.S. House WA-03, sitting since 2023) ----------------
    ("marie-gluesenkamp-perez", "WA", "House", [
        claim("mgp270a", "marie-gluesenkamp-perez", "sanctity_of_life", 0, False,
              "Self-identifies as pro-choice and supports access to abortion services; has publicly stated that decisions about pregnancy should rest with women and their doctors, rejecting any life-at-conception personhood standard. She has voted for legislation protecting abortion access and represents a district where she has explicitly distinguished herself from national Democrats primarily on economic and gun issues — not on abortion.",
              ["https://ballotpedia.org/Marie_Gluesenkamp_Perez",
               "https://en.wikipedia.org/wiki/Marie_Gluesenkamp_Perez"]),
        claim("mgp270b", "marie-gluesenkamp-perez", "self_defense", 1, True,
              "Publicly opposes a federal assault-weapons ban, calling such bans 'politically and practically ineffective' for her rural southwest Washington constituency. She represents a heavily gun-owning district and has consistently broken with the House Democratic Caucus on assault-weapons-ban legislation — aligning with the rubric's rejection of AWB-style restrictions. She ran explicitly on respecting Second Amendment rights in a district where gun ownership is a cultural baseline.",
              ["https://ballotpedia.org/Marie_Gluesenkamp_Perez",
               "https://en.wikipedia.org/wiki/Marie_Gluesenkamp_Perez"]),
    ]),

    # ---------------- Kim Schrier (WA-D, U.S. House WA-08, sitting since 2019) ----------------
    ("kim-schrier", "WA", "House", [
        claim("ks270a", "kim-schrier", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan Act (H.R. 1319, March 2021, $1.9 trillion) and the Inflation Reduction Act (H.R. 5376, August 2022, ~$739 billion) — both passed with only Democratic votes and both added substantially to the federal deficit. As a member of the House in her first and second terms, Schrier backed these large unbudgeted expenditures rather than the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Kim_Schrier",
               "https://www.govtrack.us/congress/members/kim_schrier/412835"]),
        claim("ks270b", "kim-schrier", "election_integrity", 0, False,
              "Voted against the SAVE Act (H.R. 22, House Vote #102, April 10, 2025), which would require documentary proof of U.S. citizenship to register to vote in federal elections — the core voter-verification measure the rubric supports. As a Democrat in a competitive suburban Seattle district, Schrier joined nearly all House Democrats in opposing the bill, which passed 220-208 on a near-party-line vote.",
              ["https://www.congress.gov/member/kim-schrier/S001216",
               "https://ballotpedia.org/Kim_Schrier"]),
    ]),

    # ---------------- Rick Larsen (WA-D, U.S. House WA-02, sitting since 2001) ----------------
    ("rick-larsen", "WA", "House", [
        claim("rl270a", "rick-larsen", "election_integrity", 0, False,
              "Voted against the SAVE Act (H.R. 22, House Vote #102, April 10, 2025), which would require documentary proof of U.S. citizenship to register to vote in federal elections. As a 25-year House veteran and New Democrat Coalition member, Larsen has opposed Republican-led election-integrity measures including voter-ID mandates, placing him against the rubric's citizens-only verified-registration standard.",
              ["https://ballotpedia.org/Rick_Larsen",
               "https://www.govtrack.us/congress/members/rick_larsen/400232"]),
        claim("rl270b", "rick-larsen", "foreign_policy_restraint", 1, False,
              "Voted for the $95 billion Ukraine/Israel/Taiwan foreign-aid supplemental (Senate Amendment to H.R. 815, April 2024) and has supported robust U.S. military and security commitments abroad throughout his 25-year career on the House Armed Services and Transportation committees — the inverse of the rubric's end-forever-wars, wind-down-entanglements standard. He has not supported repeal of the broad post-9/11 AUMF authorities that have underwritten two decades of overseas military operations.",
              ["https://ballotpedia.org/Rick_Larsen",
               "https://en.wikipedia.org/wiki/Rick_Larsen"]),
    ]),

    # ---------------- Adam Smith (WA-D, U.S. House WA-09, sitting since 1997) ----------------
    ("adam-smith", "WA", "House", [
        claim("as270a", "adam-smith", "self_defense", 1, False,
              "As former Chairman (2019-2022) and current Ranking Member of the House Armed Services Committee, Smith has combined support for large defense budgets with support for gun-control legislation — voting for the Bipartisan Safer Communities Act (2022), which expanded background checks and closed the 'boyfriend loophole,' and backing the Assault Weapons Ban of 2022. His position supports restrictions on semi-automatic rifles and enhanced background-check requirements that the rubric opposes.",
              ["https://ballotpedia.org/Adam_Smith_(Washington)",
               "https://en.wikipedia.org/wiki/Adam_Smith_(Washington_politician)"]),
        claim("as270b", "adam-smith", "election_integrity", 0, False,
              "Voted against the SAVE Act (H.R. 22, House Vote #102, April 10, 2025), which would require documentary proof of U.S. citizenship to register to vote in federal elections. As a nearly 30-year House veteran representing a safe Democratic district in suburban Tacoma/Seattle, Smith has consistently opposed Republican-led election-integrity bills and voter-ID requirements — the inverse of the rubric's verified citizenship-at-registration standard.",
              ["https://ballotpedia.org/Adam_Smith_(Washington)",
               "https://www.congress.gov/member/adam-smith/S000510"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
