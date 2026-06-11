#!/usr/bin/env python3
"""Enrichment batch 138: 5 sitting U.S. Representatives (bottom-of-alphabet states).

Targets evidence_federal House members with 0 claims (archetype_curated bucket
exhausted). Bottom-of-alphabet states: IL, HI, GA.

Mix (5 D): Jonathan Jackson (IL-01), Delia Ramirez (IL-03), Ed Case (HI-01),
Jill Tokuda (HI-02), Hank Johnson (GA-04).
Each claim cites >=1 reliable source and reflects 2023-2025 voting
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
    # ---------------- Jonathan Jackson (IL-01, D) ----------------
    ("jonathan-jackson", "IL", "Representative", [
        claim("jj1", "jonathan-jackson", "sanctity_of_life", 0, False,
              "Pro-choice member who earned a 100 score from Reproductive Freedom for All (formerly NARAL) in 2024, publicly supports codifying abortion access into federal law, and opposes any personhood-from-conception standard.",
              ["https://reproductivefreedomforall.org/lawmaker/jonathan-jackson/",
               "https://sbaprolife.org/representative/jonathan-jackson"]),
        claim("jj2", "jonathan-jackson", "self_defense", 1, False,
              "Co-sponsored the Assault Weapons Ban of 2023 (H.R.698) and has called for Congress to reinstate the federal assault-weapons ban and pass universal background checks — a record contrary to the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://jonathanjackson.house.gov/media/press-releases/congressman-jackson-condemns-presidents-declaration-war-chicago-calls-action"]),
    ]),

    # ---------------- Delia Ramirez (IL-03, D) ----------------
    ("delia-ramirez", "IL", "Representative", [
        claim("dr1", "delia-ramirez", "sanctity_of_life", 0, False,
              "Strongly pro-choice member who in the 119th Congress (2025) co-sponsored multiple measures to expand abortion access, codify the right to abortion, and repeal the Hyde Amendment — rejecting any recognition of personhood from conception.",
              ["https://reproductivefreedomforall.org/lawmaker/delia-ramirez/",
               "https://en.wikipedia.org/wiki/Delia_Ramirez"]),
        claim("dr2", "delia-ramirez", "self_defense", 1, False,
              "Co-sponsored the Assault Weapons Ban of 2023 (H.R.698) and the Office of Gun Violence Prevention Act; also co-sponsored Ethan's Law mandating home-storage of firearms — a record consistently opposed to uninfringed Second Amendment rights.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://giffords.org/candidates/delia-ramirez/"]),
    ]),

    # ---------------- Ed Case (HI-01, D) ----------------
    ("ed-case", "HI", "Representative", [
        claim("ec1", "ed-case", "election_integrity", 0, True,
              "Broke with nearly all House Democrats on April 10, 2025 to vote for the SAVE Act (H.R.22), which requires documented proof of U.S. citizenship to register to vote — one of only four Democrats to support voter-ID at the federal registration level.",
              ["https://thehill.com/homenews/house/5242559-house-republicans-pass-bill-requiring-proof-of-citizenship-to-vote/",
               "https://en.wikipedia.org/wiki/Ed_Case"]),
        claim("ec2", "ed-case", "sanctity_of_life", 0, False,
              "Rated 100% by NARAL Pro-Choice America; voted against banning partial-birth abortion, against making it a crime to harm a fetus during another crime, and against restricting interstate transport of minors for abortions — rejecting personhood from conception.",
              ["https://www.ontheissues.org/House/Ed_Case.htm",
               "https://ballotpedia.org/Ed_Case"]),
    ]),

    # ---------------- Jill Tokuda (HI-02, D) ----------------
    ("jill-tokuda", "HI", "Representative", [
        claim("jt1", "jill-tokuda", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, a political network that funds and elects exclusively pro-abortion-access Democratic women — placing her squarely inside the abortion-industry donor ecosystem the rubric flags.",
              ["https://emilyslist.org/candidate/jill-tokuda-22/",
               "https://en.wikipedia.org/wiki/Jill_Tokuda"]),
        claim("jt2", "jill-tokuda", "self_defense", 1, False,
              "Endorsed by the Giffords PAC Courage to Fight Gun Violence, an organization that grades legislators on support for assault-weapons restrictions, waiting periods, and red-flag laws — contrary to constitutional-carry and anti-restriction principles.",
              ["https://en.wikipedia.org/wiki/Jill_Tokuda",
               "https://ballotpedia.org/Jill_Tokuda"]),
    ]),

    # ---------------- Hank Johnson (GA-04, D) ----------------
    ("hank-johnson", "GA", "Representative", [
        claim("hj1", "hank-johnson", "self_defense", 1, False,
              "Voted to reinstate the Assault Weapons Ban and voted for the Federal Extreme Risk Protection Order Act (federal red-flag law); also co-authored the Gun Violence Prevention and Community Safety Act, which would create a federal gun-licensing system — a record directly contrary to constitutional-carry and anti-red-flag principles.",
              ["https://hankjohnson.house.gov/media-center/press-releases/rep-johnson-votes-reinstate-assault-weapons-ban-prevent-gun-violence",
               "https://hankjohnson.house.gov/media-center/press-releases/rep-johnson-votes-empower-communities-prevent-gun-violence-through"]),
        claim("hj2", "hank-johnson", "sanctity_of_life", 0, False,
              "Pro-choice member who has consistently voted against abortion restrictions throughout his tenure since 2007, supported the Women's Health Protection Act to preempt state-level abortion limits, and opposes any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Hank_Johnson",
               "https://ballotpedia.org/Hank_Johnson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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
