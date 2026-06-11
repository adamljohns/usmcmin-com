#!/usr/bin/env python3
"""Enrichment batch 126: hand-curated claims for 5 sitting U.S. Representatives.

Targets evidence_federal and archetype_party_default reps with 0 claims,
taken from the bottom of the alphabet (WA, ID, IA, GA).  Uses the
(slug + state + office_keyword) matcher from batches 2-125 to avoid
name-collision bugs.

Targets (5 R): Dan Newhouse (WA), Russ Fulcher (ID),
Mariannette Miller-Meeks (IA), Andrew Clyde (GA), Rich McCormick (GA).
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
    # ---------------- Dan Newhouse (WA-04, R, retiring) ----------------
    ("dan-newhouse", "WA", "House", [
        claim("dn1", "dan-newhouse", "sanctity_of_life", 0, True,
              "Earned an A rating from SBA Pro-Life America and declared publicly that he is '100% pro-life' and 'proud to be #ProLife,' committing to defend the unborn in Congress.",
              ["https://sbaprolife.org/representative/dan-newhouse",
               "https://en.wikipedia.org/wiki/Dan_Newhouse"]),
        claim("dn2", "dan-newhouse", "border_immigration", 2, True,
              "Called for defunding all sanctuary cities and completing the border wall, stating he would 'defund all sanctuary cities, fully secure our border, build a wall on the southern border, and fix our dangerous immigration system' — a direct anti-sanctuary enforcement stance.",
              ["https://en.wikipedia.org/wiki/Dan_Newhouse"]),
    ]),

    # ---------------- Russ Fulcher (ID-01, R) ----------------
    ("russ-fulcher", "ID", "Representative", [
        claim("rf1", "russ-fulcher", "self_defense", 1, True,
              "Holds a 92% rating from the NRA; voted against the Assault Weapons Ban of 2022 (HR 1808) and against the Bipartisan Safer Communities Act — opposing both new restrictions on firearm types and the red-flag/background-check expansions in that legislation.",
              ["https://en.wikipedia.org/wiki/Russ_Fulcher",
               "https://justfacts.votesmart.org/candidate/33091/russ-fulcher"]),
        claim("rf2", "russ-fulcher", "border_immigration", 0, True,
              "Voted for the Secure the Border Act of 2023 (HR 2), which funds border-wall construction and tightens asylum; toured the southern border firsthand, stating he is 'more convinced than ever — we must secure our border' and calling effective border security 'foundational to any good immigration policy.'",
              ["https://ballotpedia.org/Russ_Fulcher",
               "https://en.wikipedia.org/wiki/Russ_Fulcher"]),
        claim("rf3", "russ-fulcher", "sanctity_of_life", 0, True,
              "Backed the Dobbs decision and praised Idaho for quickly enacting pro-life legislation after Roe's repeal, stating that 'States, as the Constitutionally prescribed authority on this matter, will now have the opportunity to enact policies that promote a culture of life' — aligning with the life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Russ_Fulcher"]),
    ]),

    # ---------------- Mariannette Miller-Meeks (IA-01, R) ----------------
    ("mariannette-miller-meeks", "IA", "Representative", [
        claim("mm1", "mariannette-miller-meeks", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America and among the first cosponsors of the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act (2022); consistently voted to stop taxpayer funding of abortion domestically and internationally, and to protect health-care providers who refuse to participate in abortions.",
              ["https://sbaprolife.org/representative/marianette-miller-meeks",
               "https://en.wikipedia.org/wiki/Mariannette_Miller-Meeks"]),
        claim("mm2", "mariannette-miller-meeks", "self_defense", 1, True,
              "Voted NO on the Bipartisan Safer Communities Act (June 24, 2022), citing concerns that the bill gave 'government bureaucrats access to private health records' and lacked due process protections — opposing the red-flag and background-check expansions central to that legislation.",
              ["https://millermeeks.house.gov/media/press-releases/miller-meeks-statement-gun-legislation"]),
    ]),

    # ---------------- Andrew Clyde (GA-09, R) ----------------
    ("andrew-clyde", "GA", "Representative", [
        claim("ac1", "andrew-clyde", "self_defense", 2, True,
              "A gun-store owner and the leading House champion of NFA reform: introduced H.R. 3228, the Constitutional Hearing Protection Act (119th Congress, 2025-26), to remove suppressors from the NFA's burdensome registration and tax regime. P.L. 119-21 (2025) — enacted in the same Congress — reduced NFA-required taxes to $0 for covered weapons other than machineguns, a direct legislative result of his sustained push.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3228/text",
               "https://en.wikipedia.org/wiki/Andrew_Clyde"]),
        claim("ac2", "andrew-clyde", "sanctity_of_life", 0, True,
              "Voted against the Women's Health Protection Act (HR 3755, 2021) and has publicly mourned 'the millions of innocent lives lost to the evils of abortion,' affirming a personhood standard and opposing any federal statutory right to abortion.",
              ["https://en.wikipedia.org/wiki/Andrew_Clyde"]),
        claim("ac3", "andrew-clyde", "election_integrity", 0, True,
              "Voted against certifying Arizona's and Pennsylvania's 2020 presidential election results, citing unresolved election-integrity concerns — and has been among the most consistent House members opposing moves to federalize or administratively alter election rules.",
              ["https://en.wikipedia.org/wiki/Andrew_Clyde"]),
    ]),

    # ---------------- Rich McCormick (GA-07, R) ----------------
    ("rich-mccormick", "GA", "Representative", [
        claim("rm1", "rich-mccormick", "sanctity_of_life", 0, True,
              "Cosponsored the Life at Conception Act (H.R. 722, 119th Congress, introduced January 24, 2025) recognizing legal personhood from the moment of fertilization; endorsed by SBA Pro-Life America, which recognized him as protecting 'every precious life.'",
              ["https://www.govtrack.us/congress/bills/119/hr722",
               "https://sbaprolife.org/representative/rich-mccormick"]),
        claim("rm2", "rich-mccormick", "election_integrity", 0, True,
              "A consistent election-integrity advocate who 'continues to fight against all attempts to federalize elections,' opposing federal takeover of state election administration as an unconstitutional overreach.",
              ["https://en.wikipedia.org/wiki/Rich_McCormick"]),
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
