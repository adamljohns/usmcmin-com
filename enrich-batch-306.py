#!/usr/bin/env python3
"""Enrichment batch 306: 3rd claims for 5 sitting U.S. Representatives / Commissioners.

Archetype_curated federal bucket fully exhausted (see batch 303 note).
Continues the batch-305 pattern: targets evidence_curated sitting federal
representatives with exactly 2 claims — taken from the bottom of the
alphabet (PR, DE, CO ×2, CA) spanning distinct rubric categories not yet
covered in each candidate's profile.

Targets:
  Pablo José Hernández Rivera (PR, PPD) — economic_stewardship / anti-deficit
  Sarah McBride             (DE, D)  — self_defense / AWB & gun-control co-sponsorships
  Jason Crow                (CO, D)  — self_defense / Assault Weapons Ban 2023 co-sponsor
  Brittany Pettersen        (CO, D)  — border_immigration / voted NO HR2 2023
  Young Kim                 (CA, R)  — self_defense / opposed mag-bans; NRA 92%, GOA 100%

Each claim cites >=1 reliable source and reflects documented 2023-2026 public record.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---- Pablo José Hernández Rivera (PR, Resident Commissioner, PPD) ----
    ("pablo-jose-hernandez-rivera", "PR", "Resident", [
        claim("pjhr3", "pablo-jose-hernandez-rivera", "economic_stewardship", 2, False,
              "Consistently advocates for expanded federal program spending in Puerto Rico rather than deficit reduction: introduced the Medicare Advantage Integrity Act of 2025 to increase Medicare Advantage payments to Puerto Rico, testified before Congress demanding full Medicaid parity for Puerto Rico's 1.6 million Medicaid enrollees, and pushed for expanded SNAP and Social Security access. When President Trump signed a 2025 executive order restricting federal funds, Hernández Rivera publicly denounced the action as unconstitutional and demanded full restoration of federal assistance to the island — a posture at odds with the rubric's anti-deficit/balanced-budget alignment.",
              ["https://hernandez.house.gov/media/press-releases/puerto-rico-resident-commissioner-statement-president-trumps-order-regarding",
               "https://www.elnuevodia.com/english/news/story/resident-commissioner-pablo-jose-hernandez-advocates-for-parity-in-the-medicaid-program/",
               "https://hernandez.house.gov/media/press-releases/hernandez-rivera-announces-achievements-his-first-100-days-washington"]),
    ]),

    # ---- Sarah McBride (DE, US Representative) ----
    ("sarah-mcbride", "DE", "Representative", [
        claim("smb3", "sarah-mcbride", "self_defense", 1, False,
              "In the 119th Congress (2025-2026) co-sponsored the Federal Firearm Licensing Act — which would require a federal license and background check for every gun purchase — and the Office of Gun Violence Prevention Act; also co-sponsored legislation cracking down on automatic gun conversion devices. Publicly supports reinstating the federal Assault Weapons Ban. In spring 2025, hosted a gun-safety roundtable in Wilmington with former Rep. Gabby Giffords and Delaware public-safety officials to press for further firearm restrictions — the inverse of the rubric's anti-AWB/registry/red-flag standard.",
              ["https://mcbride.house.gov/media/press-releases/photo-release-rep-sarah-mcbride-hosts-gun-safety-roundtable-former-rep-gabby-giffords",
               "https://giffords.org/candidates/sarah-mcbride/",
               "https://www.govtrack.us/congress/members/sarah_mcbride/456985"]),
    ]),

    # ---- Jason Crow (CO, US Representative) ----
    ("jason-crow", "CO", "Representative", [
        claim("jcrow3", "jason-crow", "self_defense", 1, False,
              "Co-sponsored H.R. 698 (Assault Weapons Ban of 2023, 118th Congress), which would make it a federal crime to import, sell, manufacture, transfer, or possess semiautomatic assault weapons and large-capacity ammunition feeding devices (magazines over 10 rounds). Crow, who serves as Vice Chair of the House Gun Violence Prevention Task Force, joined over 200 House Democrats as a cosponsor when the bill was introduced in February 2023. He has also introduced legislation to close the 'Colorado Loophole' on long-gun background checks and previously voted YES on H.R. 8 (Bipartisan Background Checks Act) — a consistent legislative pattern supporting the AWB, magazine limits, and expanded registry infrastructure that the rubric opposes.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/all-info",
               "https://crow.house.gov/issues/gun-violence-prevention",
               "https://ballotpedia.org/Jason_Crow"]),
    ]),

    # ---- Brittany Pettersen (CO, US Representative) ----
    ("brittany-pettersen", "CO", "Representative", [
        claim("bp3", "brittany-pettersen", "border_immigration", 0, False,
              "Voted NO on H.R. 2 (Secure the Border Act of 2023, 118th Congress, House Vote #209, May 11, 2023), which would have funded border-wall construction, restricted asylum eligibility to official ports of entry only, ended catch-and-release, mandated E-Verify for employers, and imposed safe-third-country bars. The bill passed 219-213 with no Democratic support — Pettersen voted with every House Democrat against the comprehensive wall-and-enforcement package the rubric identifies as the border-security alignment standard.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2/summary/00",
               "https://ballotpedia.org/Brittany_Pettersen"]),
    ]),

    # ---- Young Kim (CA-40, US Representative) ----
    ("young-kim", "CA", "Representative", [
        claim("yk3", "young-kim", "self_defense", 1, True,
              "Consistently voted against magazine bans, background-check expansions on ammunition, and other firearms restrictions in the 118th-119th Congresses; VoteSmart documents her opposition to prohibiting high-capacity magazines and mandatory background checks for ammo purchases. Stated publicly that she opposes restrictions on the Right to Keep and Bear Arms (Christian Coalition survey response). Gun-rights groups rewarded this record with an NRA rating of 92% in 2024 and a Gun Owners of America rating of 100% in 2024 — reflecting rubric-aligned opposition to AWB, magazine limits, and registry expansions.",
              ["https://justfacts.votesmart.org/candidate/key-votes/151787/young-kim/37/guns",
               "https://justfacts.votesmart.org/candidate/evaluations/151787/young-kim",
               "https://ontheissues.org/CA/Young_Kim_Gun_Control.htm"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
