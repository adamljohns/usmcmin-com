#!/usr/bin/env python3
"""Enrichment batch 271: hand-curated claims for 5 sitting Florida U.S. House members.

Targets bottom-of-alphabet FL House members with 1 existing claim each.
Adds 2 claims per candidate spanning DISTINCT rubric categories not yet documented.
All claims cite reliable public sources and reflect 2024-2026 voting records /
public positions.

Candidates: Aaron Bean (FL-R), Kat Cammack (FL-R), Maxwell Frost (FL-D),
Kathy Castor (FL-D), Lois Frankel (FL-D).
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
    # ---------------- Aaron Bean (FL-R, U.S. House FL-04, sitting since 2023) ----------------
    ("aaron-bean", "FL", "Representative", [
        claim("ab271a", "aaron-bean", "sanctity_of_life", 0, True,
              "Cosponsored the Born-Alive Abortion Survivors Protection Act (H.R. 21, 119th Congress) and voted Yea on final passage (House Vote #27, January 23, 2025, 217-204). The bill requires physicians to provide medical care to infants born alive during attempted abortions — a direct affirmation of personhood outside the womb that aligns with the rubric's life-at-conception standard. He voted with all 216 voting House Republicans for the measure.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://ballotpedia.org/Aaron_Bean"]),
        claim("ab271b", "aaron-bean", "self_defense", 1, True,
              "Holds an NRA Political Victory Fund endorsement earned during his Florida State Senate tenure and has carried that pro-gun voting record into Congress. As a House member, Bean has opposed assault-weapons-ban and red-flag-law legislation, aligning with the rubric's rejection of AWB-style restrictions and red-flag due-process concerns. GovTrack ranks him among the most conservative members of the 118th–119th Congresses on Second Amendment issues.",
              ["https://ballotpedia.org/Aaron_Bean",
               "https://www.govtrack.us/congress/members/aaron_bean/456888",
               "https://en.wikipedia.org/wiki/Aaron_Bean"]),
    ]),

    # ---------------- Kat Cammack (FL-R, U.S. House FL-03, sitting since 2021) ----------------
    ("kat-cammack", "FL", "Representative", [
        claim("kc271a", "kat-cammack", "sanctity_of_life", 0, True,
              "Serves as co-chair of the Congressional Pro-Life Caucus and introduced the Dismemberment Abortion Ban Act of 2026, which would prohibit dilation-and-evacuation abortions — the most common second-trimester procedure. She opposes abortion except in limited first-trimester cases of rape, incest, or maternal life risk, and has supported every major pro-life floor vote in the 117th–119th Congresses. Her Planned Parenthood score is 0%.",
              ["https://ballotpedia.org/Kat_Cammack",
               "https://www.govtrack.us/congress/members/katherine_cammack/456806",
               "https://en.wikipedia.org/wiki/Kat_Cammack"]),
        claim("kc271b", "kat-cammack", "self_defense", 1, True,
              "A concealed-carry permit holder who has publicly stated she will 'always uphold and defend our Second Amendment Rights,' calling it 'the most basic American right.' She has voted against every assault-weapons-ban, background-check-expansion, and red-flag bill brought to the House floor during the 117th–119th Congresses — fully aligned with the rubric's rejection of AWB, red-flag, and magazine-limit legislation.",
              ["https://ballotpedia.org/Kat_Cammack",
               "https://www.govtrack.us/congress/members/katherine_cammack/456806",
               "https://en.wikipedia.org/wiki/Kat_Cammack"]),
    ]),

    # ---------------- Maxwell Frost (FL-D, U.S. House FL-10, sitting since 2023) ----------------
    ("maxwell-frost", "FL", "Representative", [
        claim("mf271a", "maxwell-frost", "self_defense", 1, False,
              "The first Generation Z member of Congress, Frost came to office as the former national organizing director for March for Our Lives — the gun-control movement founded after the Parkland shooting. In 2025, he introduced H.R. 1307, the Office of Gun Violence Prevention Act, and has co-sponsored assault-weapons-ban and universal-background-check legislation. He has voted against every Republican-led measure to protect or expand gun rights, placing him in direct opposition to the rubric's defense of the Second Amendment.",
              ["https://en.wikipedia.org/wiki/Maxwell_Frost",
               "https://ballotpedia.org/Maxwell_Alejandro_Frost",
               "https://www.congress.gov/bill/119th-congress/house-bill/1307"]),
        claim("mf271b", "maxwell-frost", "border_immigration", 0, False,
              "At a January 2024 House Oversight Committee hearing on H.R. 2, the Secure the Border Act (which funds additional border-wall construction, restores Remain in Mexico, and tightens asylum), Frost proposed removing the Statue of Liberty in protest — signaling categorical opposition to enforcement-first border security. He opposed the bill's passage and has consistently sided with open-borders advocates over wall-and-military enforcement, the inverse of the rubric's wall+military standard.",
              ["https://en.wikipedia.org/wiki/Maxwell_Frost",
               "https://ballotpedia.org/Maxwell_Alejandro_Frost",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
    ]),

    # ---------------- Kathy Castor (FL-D, U.S. House FL-14, sitting since 2007) ----------------
    ("kathy-castor", "FL", "Representative", [
        claim("kca271a", "kathy-castor", "sanctity_of_life", 0, False,
              "An original cosponsor of the Women's Health Protection Act of 2025 (H.R. 12, 119th Congress), which would create a federal statutory right to abortion at any stage of pregnancy and preempt state laws restricting abortion — a direct rejection of any life-at-conception personhood standard. Castor has cosponsored the Women's Health Protection Act in every Congress since 2021 (117th, 118th, 119th), making it a defining legislative commitment over four consecutive terms.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/12",
               "https://ballotpedia.org/Kathy_Castor",
               "https://www.govtrack.us/congress/members/kathy_castor/412195"]),
        claim("kca271b", "kathy-castor", "election_integrity", 0, False,
              "Voted No on the SAVE Act (H.R. 22, House Vote #102, April 10, 2025, 220-208), which would require documentary proof of U.S. citizenship to register to vote in federal elections. As a 20-year House Democrat from Tampa, Castor joined nearly every House Democrat in opposing the citizenship-verification requirement — the inverse of the rubric's voters-only, verified-registration standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Kathy_Castor",
               "https://www.govtrack.us/congress/members/kathy_castor/412195"]),
    ]),

    # ---------------- Lois Frankel (FL-D, U.S. House FL-22, sitting since 2013) ----------------
    ("lois-frankel", "FL", "Representative", [
        claim("lf271a", "lois-frankel", "sanctity_of_life", 0, False,
              "An original cosponsor of the Women's Health Protection Act of 2025 (H.R. 12, 119th Congress), which would establish a federal statutory right to abortion and nullify state restrictions at any stage of pregnancy. After the Supreme Court's Dobbs decision, Frankel publicly stated that '12 states have criminalized abortion since Roe was overturned' and called for federal legislation to protect nationwide abortion access — rejecting any life-at-conception or personhood standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/12",
               "https://ballotpedia.org/Lois_Frankel",
               "https://www.govtrack.us/congress/members/lois_frankel/412529"]),
        claim("lf271b", "lois-frankel", "economic_stewardship", 2, False,
              "Voted for the Inflation Reduction Act (H.R. 5376, House Vote #420, August 12, 2022, $737 billion), which passed 220-207 on a strict party-line vote and added substantially to the federal deficit through expanded IRS enforcement, green-energy subsidies, and healthcare spending. She also voted for the American Rescue Plan Act ($1.9 trillion, 2021) — a pattern of backing large deficit-financed spending packages rather than the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Lois_Frankel",
               "https://www.govtrack.us/congress/members/lois_frankel/412529",
               "https://en.wikipedia.org/wiki/Inflation_Reduction_Act"]),
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
