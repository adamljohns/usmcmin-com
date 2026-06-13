#!/usr/bin/env python3
"""Enrichment batch 172: hand-curated claims for 5 sitting U.S. House members.

Targets evidence_federal candidates with 0 claims from the bottom of the
available alphabet pool (CA/AZ after WY–VA states were exhausted).

Targets (all R): Eli Crane (AZ-02), Juan Ciscomani (AZ-06),
Ken Calvert (CA-40/41), Young Kim (CA-40), David Valadao (CA-22).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Eli Crane (AZ-02, R) ----------------
    ("eli-crane", "AZ", "Representative", [
        claim("ec1", "eli-crane", "sanctity_of_life", 0, True,
              "Rated 83% by the National Right to Life Committee and describes himself as 'proudly and unflinchingly pro-life.' Publicly stated 'Roe v. Wade was a mistake that cost millions of innocent lives, and our Constitution never authorizes the right to terminate human life' — affirming the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Eli_Crane",
               "https://en.wikipedia.org/wiki/Eli_Crane"]),
        claim("ec2", "eli-crane", "border_immigration", 0, True,
              "Voted YES on HR 2, the Secure the Border Act of 2023, which mandates resumption of southern-border wall construction, deploys military assets to the border, and tightens asylum — consistent with the wall-and-military enforcement standard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Eli_Crane"]),
        claim("ec3", "eli-crane", "self_defense", 1, True,
              "A U.S. Navy SEAL combat veteran and Freedom Caucus member who consistently opposes new gun-control measures. GovTrack's 2024 report card noted Crane joined bipartisan legislation the least of any House freshman, reflecting refusal to compromise on constitutional rights including Second Amendment protections against red-flag laws, assault-weapons bans, and registries.",
              ["https://www.govtrack.us/congress/members/eli_crane/456879/report-card/2024",
               "https://en.wikipedia.org/wiki/Eli_Crane"]),
    ]),

    # ---------------- Juan Ciscomani (AZ-06, R) ----------------
    ("juan-ciscomani", "AZ", "Representative", [
        claim("jc1", "juan-ciscomani", "self_defense", 0, True,
              "Cosponsor of HR 38, the Constitutional Concealed Carry Reciprocity Act of 2025, which would require states to recognize lawful carry permits issued by other states — advancing constitutional carry principles nationwide.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://ballotpedia.org/Juan_Ciscomani"]),
        claim("jc2", "juan-ciscomani", "sanctity_of_life", 0, True,
              "Praised the Supreme Court's overturning of Roe v. Wade; per SBA Pro-Life America has 'voted consistently to defend the lives of the unborn and infants, including stopping hard-earned tax dollars from paying for abortion.'",
              ["https://sbaprolife.org/representative/juan-ciscomani",
               "https://ballotpedia.org/Juan_Ciscomani"]),
        claim("jc3", "juan-ciscomani", "border_immigration", 1, False,
              "Has stated he would be open to 'immigration reform and legal protections for young immigrants who came to the U.S. as children' (DACA recipients) — rejecting the mandatory-deportation standard and instead supporting a legal pathway for those who entered illegally.",
              ["https://ballotpedia.org/Juan_Ciscomani",
               "https://en.wikipedia.org/wiki/Juan_Ciscomani"]),
    ]),

    # ---------------- Ken Calvert (CA-40/41, R) ----------------
    ("ken-calvert", "CA", "Representative", [
        claim("kc1", "ken-calvert", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee; supported the overturning of Roe v. Wade, stating it 'shifts the power to set abortion policies to Congress and to the States' — consistent with the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Ken_Calvert",
               "https://en.wikipedia.org/wiki/Ken_Calvert"]),
        claim("kc2", "ken-calvert", "border_immigration", 0, True,
              "Voted YES on HR 2, the Secure the Border Act of 2023; stated 'The worst step we can take is to grant amnesty to people who entered our country illegally — it sends a horrible message to those who entered our country legally' — aligning with wall-and-enforcement priorities.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Ken_Calvert"]),
        claim("kc3", "ken-calvert", "economic_stewardship", 2, True,
              "Has stated 'I continue to have serious concerns about our federal debt. As this graph shows, the leading driver of debt is our mandatory spending' — a sustained anti-deficit position consistent with the rubric's balanced-budget standard.",
              ["https://ballotpedia.org/Ken_Calvert",
               "https://en.wikipedia.org/wiki/Ken_Calvert"]),
    ]),

    # ---------------- Young Kim (CA-40, R) ----------------
    ("young-kim", "CA", "Representative", [
        claim("yk1", "young-kim", "border_immigration", 1, False,
              "Cosponsor of the DIGNIDAD Act (HR 4393, 119th Congress), which would create a pathway to legal permanent resident status for up to 12 million illegal immigrants — directly opposing the mandatory-deportation standard. The bill, led by Rep. Maria Elvira Salazar, drew 20 Republican cosponsors including Kim.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/4393",
               "https://en.wikipedia.org/wiki/DIGNIDAD_Act"]),
        claim("yk2", "young-kim", "sanctity_of_life", 0, True,
              "Voted YES on HR 1 (One Big Beautiful Bill Act) on May 22, 2025, which included a one-year defunding of Planned Parenthood of Medicaid dollars — a pro-life budget provision tracked by SBA Pro-Life America.",
              ["https://en.wikipedia.org/wiki/Young_Kim",
               "https://sbaprolife.org/representative/young-kim"]),
    ]),

    # ---------------- David Valadao (CA-22, R) ----------------
    ("david-valadao", "CA", "Representative", [
        claim("dv1", "david-valadao", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and stated 'I am proud to receive an A+ rating from @SBAList for my pro-life voting record.' Voted YES on HR 1 (One Big Beautiful Bill Act) which defunded Planned Parenthood of Medicaid dollars for one year.",
              ["https://sbaprolife.org/representative/david-valadao",
               "https://en.wikipedia.org/wiki/David_Valadao"]),
        claim("dv2", "david-valadao", "border_immigration", 0, True,
              "Voted YES on HR 2, the Secure the Border Act of 2023, and HR 5525, the Continuing Appropriations and Border Security Enhancement Act of 2024 — a consistent record of backing border-wall and enforcement legislation.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/David_Valadao"]),
        claim("dv3", "david-valadao", "border_immigration", 1, False,
              "Supports a legislative path for Dreamers/DACA recipients to remain in the United States: 'These young people make significant contributions to our communities each and every day… Congress must provide a legislative solution so these individuals may continue to live in America — the only home they know.' This rejects the mandatory-deportation standard.",
              ["https://ballotpedia.org/David_Valadao",
               "https://en.wikipedia.org/wiki/David_Valadao"]),
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
