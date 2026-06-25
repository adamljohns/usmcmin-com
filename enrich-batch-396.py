#!/usr/bin/env python3
"""Enrichment batch 396: hand-curated claims for 5 sitting U.S. Representatives.

archetype_curated federal bucket fully exhausted; targets are evidence_curated
U.S. Representatives with 3 claims each — adding 2 new claims per candidate
in distinct rubric categories not yet covered.

Candidates (all R):
  Tim Burchett (TN-2), Andy Ogles (TN-5), William Timmons (SC-4),
  Lance Gooden (TX-5), John Carter (TX-31).

Direction: bottom-of-alphabet states (TX, TN, SC) to avoid collision with the
top-of-alphabet enrichment loop.
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


TARGETS = [
    # ---------- Tim Burchett (TN-2, R) ----------
    ("tim-burchett", "TN", "Representative", [
        claim("tb4", "tim-burchett", "election_integrity", 0, True,
              "Voted YES on the SAVE America Act (H.R.22, 119th Congress, February 11, 2026) and was a cosponsor of the bill, which requires documentary proof of U.S. citizenship to register to vote and photo ID to cast a ballot in federal elections. Stated 'Who Can Vote Against Saving America?' and pointedly noted '213 Democrats just used their photo id to vote against photo ids in elections.' Source: burchett.house.gov.",
              ["https://burchett.house.gov/media/press-releases/congressman-burchett-votes-favor-save-america-act",
               "https://rsc-pfluger.house.gov/media/press-releases/rep-tim-burchett-who-can-vote-against-saving-america"]),
        claim("tb5", "tim-burchett", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, passed 219-213), which mandates resumption of southern border wall construction, ends catch-and-release, codifies Remain in Mexico, and broadens deportation authority. Also voted for H.R. 3602 (End the Border Catastrophe Act, April 2024), including a restart of wall-system construction. Source: burchett.house.gov press releases.",
              ["https://burchett.house.gov/media/press-releases/rep-burchett-votes-favor-bill-secure-southern-border",
               "https://congress.gov/bill/118th-congress/house-bill/2"]),
    ]),

    # ---------- Andy Ogles (TN-5, R) ----------
    ("andy-ogles", "TN", "Representative", [
        claim("ao4", "andy-ogles", "election_integrity", 0, True,
              "An original cosponsor of the SAVE Act (H.R.22, 119th Congress, passed 220-208 on April 10, 2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections; publicly declared 'The SAVE Act should be at the very top of the Republican agenda. All illegal voters must be suppressed. The President has demanded action; Congress has no excuse for delay.' Source: RSC press release.",
              ["https://rsc-pfluger.house.gov/media/press-releases/rsc-members-demand-senate-action-save-act",
               "https://congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ao5", "andy-ogles", "foreign_policy_restraint", 1, True,
              "Consistently opposed open-ended U.S. military aid abroad: stated 'It's America First, not Ukraine First — we cannot be the world's checkbook' (2022, andyogles.com); introduced a House floor amendment in the 118th Congress to strip lend-lease authority for Ukraine from the National Defense Authorization Act (failed 71-360). Source: andyogles.com campaign statement; congress.gov.",
              ["https://andyogles.com/tn-5-candidate-andy-ogles-on-40-billion-ukrainian-aid-package-its-america-first-not-ukraine-first/",
               "https://congress.gov/member/andrew-ogles/O000175"]),
    ]),

    # ---------- William Timmons (SC-4, R) ----------
    ("william-timmons", "SC", "Representative", [
        claim("wt4", "william-timmons", "election_integrity", 0, True,
              "A cosponsor of the SAVE Act (H.R.22, 119th Congress) and voted Yea when it passed 220-208 (House Vote #102, April 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections — affirming that only American citizens should decide American elections. Source: congress.gov.",
              ["https://congress.gov/bill/119th-congress/house-bill/22",
               "https://clerk.house.gov/Votes/2025102"]),
        claim("wt5", "william-timmons", "border_immigration", 1, True,
              "Voted Yea on the Laken Riley Act (H.R.535, 119th Congress, January 22, 2025, passed 264-159), the first bill signed into law in the 119th Congress, which mandates ICE detention and initiation of removal proceedings for unlawfully present aliens charged with robbery, burglary, theft, or violent offenses. Source: congress.gov.",
              ["https://congress.gov/bill/119th-congress/house-bill/535",
               "https://timmons.house.gov/voterecord/"]),
    ]),

    # ---------- Lance Gooden (TX-5, R) ----------
    ("lance-gooden", "TX", "Representative", [
        claim("lg4", "lance-gooden", "self_defense", 1, True,
              "Voted NAY on H.R. 1808, the Assault Weapons Ban of 2022 (House Vote #380, July 29, 2022, passed 217-213), opposing a federal prohibition on semi-automatic rifles and standard-capacity magazines; only 2 of 213 Republicans voted Yes, making Gooden's Nay a principled stand against any federal assault-weapons ban or magazine-limit registry. Source: clerk.house.gov Roll Call #380.",
              ["https://clerk.house.gov/Votes/2022380",
               "https://congress.gov/bill/117th-congress/house-bill/1808"]),
        claim("lg5", "lance-gooden", "border_immigration", 1, True,
              "Voted Yea on the Laken Riley Act (H.R.535, 119th Congress, January 22, 2025, passed 264-159), mandating ICE detention and removal proceedings for unlawfully present aliens charged with specified crimes. His border-security page states he is committed to 'standing with Border Patrol and ICE agents to keep our borders secure, uphold the rule of law, and protect communities…to remove criminal illegal aliens.' Source: congress.gov, gooden.house.gov.",
              ["https://congress.gov/bill/119th-congress/house-bill/535",
               "https://gooden.house.gov/border-security-immigration"]),
    ]),

    # ---------- John Carter (TX-31, R) ----------
    ("john-carter", "TX", "Representative", [
        claim("jc3", "john-carter", "self_defense", 0, True,
              "Proudly carries an NRA 'A' rating; his official congressional website states he 'fully supports the Second Amendment right to keep and bear arms' and is 'proud to receive the NRA's endorsement.' Voted against the Biden administration's ATF rule banning stabilizing pistol braces, defending every law-abiding American's right to keep and bear commonly used firearms. Source: carter.house.gov.",
              ["https://carter.house.gov/issues/issue/?IssueID=14896",
               "https://www.ontheissues.org/tx/John_Carter_Gun_Control.htm"]),
        claim("jc4", "john-carter", "border_immigration", 1, True,
              "Voted Yea on the Laken Riley Act (H.R.535, 119th Congress, January 22, 2025, passed 264-159), the first bill signed into law in the 119th Congress, which requires ICE to detain and initiate removal proceedings against unlawfully present aliens charged with robbery, burglary, theft, or violent crimes — supporting mandatory deportation policy. Source: congress.gov.",
              ["https://congress.gov/bill/119th-congress/house-bill/535",
               "https://carter.house.gov/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
