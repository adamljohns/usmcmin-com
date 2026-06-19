#!/usr/bin/env python3
"""Enrichment batch 305: 3rd claims for 5 sitting U.S. Representatives.

Archetype_curated federal bucket fully exhausted (see batch 303 note).
Targets evidence_curated sitting federal representatives with exactly 2 claims —
taken from the bottom of the alphabet (FL ×2, CO, GA ×2) spanning
distinct rubric categories not yet covered in each candidate's profile.

Targets:
  Laurel Lee      (FL-15, R) — voted YES H.R.2 Secure the Border Act 2023 → border_immigration
  Jimmy Patronis  (FL-1,  R) — voted YES H.R.1 One Big Beautiful Bill (PP defunding) → sanctity_of_life
  Jeff Hurd       (CO-3,  R) — voted YES SAVE Act H.R.22 2025 → election_integrity
  Nikema Williams (GA-5,  D) — voted NO  H.R.2 Secure the Border Act 2023 → border_immigration
  Lucy McBath     (GA-7,  D) — voted YES Inflation Reduction Act 2022 → economic_stewardship

Each claim cites >=1 reliable source and reflects documented 2022-2025 public record.

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
    # ---- Laurel Lee (FL-15, R — US Representative) ----
    ("laurel-lee", "FL", "Representative", [
        claim("ll3", "laurel-lee", "border_immigration", 0, True,
              "Voted YES on H.R.2 (Secure the Border Act of 2023, 118th Congress, House Vote #209, May 11, 2023), which passed 219-213 with no Democratic support. H.R.2 would have funded border-wall construction, restricted asylum eligibility to official ports of entry only, ended catch-and-release, mandated E-Verify for employers, and imposed safe-third-country bars — the comprehensive wall-and-enforcement posture the rubric identifies as border-security alignment. Lee (R-FL15) voted YES along with every other House Republican present.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Laurel_Lee"]),
    ]),

    # ---- Jimmy Patronis (FL-1, R — US Representative) ----
    ("jimmy-patronis", "FL", "Representative", [
        claim("jp3", "jimmy-patronis", "sanctity_of_life", 0, True,
              "Voted YES on H.R.1 (One Big Beautiful Bill, July 2025), the first federal law to defund Planned Parenthood of Medicaid dollars — an outcome Patronis publicly praised as 'a Big, Beautiful Victory for America,' releasing a press statement hailing the bill's passage. H.R.1's Medicaid provider-exclusion provision cut approximately $880 million in annual Planned Parenthood Medicaid reimbursements for one year, the largest federal pro-life legislative win since the Hyde Amendment, directly aligning with the rubric's personhood-and-life standard.",
              ["https://patronis.house.gov/media/press-releases/congressman-patronis-congress-delivered-a-big-beautiful-victory-for-america",
               "https://floridapolitics.com/archives/739429-florida-congressional-delegation-touts-condemns-house-passage-of-big-beautiful-bill/"]),
    ]),

    # ---- Jeff Hurd (CO-3, R — US Representative) ----
    ("jeff-hurd", "CO", "Representative", [
        claim("jh3", "jeff-hurd", "election_integrity", 0, True,
              "Voted YES on H.R.22 (SAVE Act — Safeguard American Voter Eligibility Act, 119th Congress, House Vote #102, April 10, 2025), which passed 220-208 on a near-party-line vote. The SAVE Act amends the National Voter Registration Act to require applicants to present documentary proof of U.S. citizenship (e.g., passport, birth certificate, or naturalization certificate) when registering to vote in federal elections — a citizenship-verification requirement that aligns with the rubric's voter-ID and election-integrity standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://annelandmanblog.com/2026/02/rep-jeff-hurd-votes-in-favor-of-the-trump-backed-save-america-act/"]),
    ]),

    # ---- Nikema Williams (GA-5, D — U.S. Representative) ----
    ("nikema-williams", "GA", "Representative", [
        claim("nw3", "nikema-williams", "border_immigration", 0, False,
              "Voted NO on H.R.2 (Secure the Border Act of 2023, 118th Congress, House Vote #209, May 11, 2023), which passed 219-213 with no Democratic votes. H.R.2 would have funded border-wall construction, limited asylum to ports of entry, ended catch-and-release, and mandated E-Verify — the wall-and-enforcement measures the rubric identifies as border-security alignment. Williams (D-GA5), a member of the Congressional Progressive Caucus representing Atlanta, voted NO along with all other House Democrats present.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Nikema_Williams"]),
    ]),

    # ---- Lucy McBath (GA-7, D — U.S. Representative) ----
    ("lucy-mcbath", "GA", "Representative", [
        claim("lm3", "lucy-mcbath", "economic_stewardship", 2, False,
              "Voted YES on H.R.5376 (Inflation Reduction Act of 2022, 117th Congress, House Vote #420, August 12, 2022), which passed 220-207 with every House Democrat — including McBath (then D-GA6) — voting in favor. The IRA authorized approximately $369 billion in new federal spending on climate programs and ACA subsidy extensions, financed partly by a corporate alternative minimum tax; fiscal conservatives and balanced-budget advocates widely criticized it as a net expansion of federal outlays and deficit spending, placing McBath outside the anti-deficit stewardship posture the rubric calls for.",
              ["https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://ballotpedia.org/Inflation_Reduction_Act_of_2022",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; prevents wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
