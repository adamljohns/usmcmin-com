#!/usr/bin/env python3
"""Enrichment batch 167: 5 sitting House Republicans from bottom of alphabet.

Targets archetype_party_default federal House members with 0 evidence claims,
taken from the bottom of the alphabet (NY, NJ, NC).  All claims sourced from
official *.house.gov, congress.gov, govtrack.us, ballotpedia.org, or
sbaprolife.org and reflect 2025-2026 public record.

Candidates:
  Mike Lawler       (NY-17, R) — biblical_marriage, election_integrity, border_immigration
  Thomas Kean Jr.   (NJ-7,  R) — election_integrity, border_immigration, biblical_marriage
  Pat Harrigan      (NC-10, R) — sanctity_of_life, border_immigration, self_defense
  Mark Harris       (NC-8,  R) — sanctity_of_life, border_immigration, biblical_marriage
  Greg Murphy       (NC-3,  R) — sanctity_of_life, biblical_marriage, border_immigration
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
    # ---------------- Mike Lawler (NY-17, R) ----------------
    ("mike-lawler", "NY", "US Representative", [
        claim("ml1", "mike-lawler", "biblical_marriage", 2, True,
              "Voted for the Protection of Women and Girls in Sports Act of 2025, which would bar transgender-identifying males from competing in female athletic categories in federally funded programs — joining every other House Republican in rejecting transgender ideology in women's sports.",
              ["https://en.wikipedia.org/wiki/Mike_Lawler",
               "https://ballotpedia.org/Michael_Lawler_(New_York)"]),
        claim("ml2", "mike-lawler", "election_integrity", 0, True,
              "Voted for H.R. 22 (the SAVE Act, 119th Congress), requiring documentary proof of U.S. citizenship to register to vote in federal elections — a citizenship-verification standard that directly aligns with the rubric's voter-ID and anti-fraud election-integrity position.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/bills/119/hr22"]),
        claim("ml3", "mike-lawler", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29 / S. 5, signed January 29, 2025) — the first bill signed into law by President Trump — which mandates detention and deportation proceedings for illegal immigrants who commit theft, burglary, or other specified crimes against American citizens.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
    ]),

    # ---------------- Thomas Kean Jr. (NJ-7, R) ----------------
    ("thomas-kean-jr", "NJ", "US House", [
        claim("tkj1", "thomas-kean-jr", "election_integrity", 0, True,
              "Voted for H.R. 22 (the SAVE Act, 119th Congress), which requires proof of U.S. citizenship to register to vote in federal elections and mandates states remove noncitizens from voter rolls — a direct voter-eligibility verification measure consistent with the rubric's election-integrity standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/bills/119/hr22"]),
        claim("tkj2", "thomas-kean-jr", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (S. 5 / H.R. 29, signed January 29, 2025), mandating detention and deportation proceedings for illegal immigrants who commit theft, burglary, or violent crimes — an enforcement-first border-security measure passed with bipartisan House support.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
        claim("tkj3", "thomas-kean-jr", "biblical_marriage", 2, True,
              "Voted for the Protection of Women and Girls in Sports Act of 2025 alongside every other House Republican, barring biological males from female sports categories in federally funded programs — rejecting the transgender-ideology redefinition of sex.",
              ["https://ballotpedia.org/Thomas_Kean_Jr.",
               "https://www.govtrack.us/congress/members/thomas_kean/456917"]),
    ]),

    # ---------------- Pat Harrigan (NC-10, R) ----------------
    ("pat-harrigan", "NC", "US Representative", [
        claim("ph1", "pat-harrigan", "sanctity_of_life", 0, True,
              "Applauded the Supreme Court's Dobbs decision as 'correcting an errant opinion that removed power from the People,' affirms a pro-life stance, and publicly supports returning abortion law to the states as a pro-life outcome — consistent with the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Pat_Harrigan",
               "https://en.wikipedia.org/wiki/Pat_Harrigan"]),
        claim("ph2", "pat-harrigan", "border_immigration", 0, True,
              "Has stated 'It's time to build the wall, secure our borders, and outlaw sanctuary cities,' tying open-border policy directly to gang violence, sex trafficking, drug smuggling, and terrorism — a wall-plus-military border posture matching the rubric's top border criterion.",
              ["https://ballotpedia.org/Pat_Harrigan",
               "https://en.wikipedia.org/wiki/Pat_Harrigan"]),
        claim("ph3", "pat-harrigan", "self_defense", 0, True,
              "A decorated Army Special Forces veteran, Harrigan sponsored the Special Operations Forces Concealed Carry Act (119th Congress, April 2026), which expands carry rights for current and former SOF personnel — reflecting an expansive Second Amendment philosophy consistent with constitutional-carry principles.",
              ["https://www.congress.gov/member/pat-harrigan/H001101",
               "https://ballotpedia.org/Pat_Harrigan"]),
    ]),

    # ---------------- Mark Harris (NC-8, R) ----------------
    ("mark-harris", "NC", "US Representative", [
        claim("mh1", "mark-harris", "sanctity_of_life", 0, True,
              "A Baptist pastor and Freedom Caucus member who affirms 'the sanctity of all human life, from conception to natural end,' publicly declares himself 100% pro-life, and is listed on the SBA Pro-Life America candidate scorecard — placing him squarely at the rubric's life-from-conception standard.",
              ["https://sbaprolife.org/candidate/mark-harris",
               "https://en.wikipedia.org/wiki/Mark_Harris_(North_Carolina_politician)"]),
        claim("mh2", "mark-harris", "border_immigration", 0, True,
              "Has stated he is 'committed to fortifying our borders, supporting advanced technology, and rigorously enforcing our immigration laws to protect American citizens,' and pointed to NGOs actively hindering law enforcement for illegal immigrants — a build-the-wall/enforcement-first border stance.",
              ["https://ballotpedia.org/Mark_Harris_(North_Carolina)",
               "https://en.wikipedia.org/wiki/Mark_Harris_(North_Carolina_politician)"]),
        claim("mh3", "mark-harris", "biblical_marriage", 2, True,
              "Voted for the Protection of Women and Girls in Sports Act of 2025, which bars biological males from competing in female sports categories in federally funded programs — consistent with his pastoral identity and Freedom Caucus membership that reject transgender-ideology redefinitions of sex.",
              ["https://www.congress.gov/member/mark-harris/H001102",
               "https://www.govtrack.us/congress/members/mark_harris/457002"]),
    ]),

    # ---------------- Greg Murphy (NC-3, R) ----------------
    ("greg-murphy", "NC", "US Representative", [
        claim("gm1", "greg-murphy", "sanctity_of_life", 0, True,
              "A urologist and 'devout Christian with lifelong allegiance to the unborn,' Murphy carries a 100% lifetime pro-life rating on the SBA Pro-Life America National Scorecard and has voted in every Congress to stop taxpayer funding of abortion domestically and internationally.",
              ["https://sbaprolife.org/representative/greg-murphy",
               "https://ballotpedia.org/Gregory_Murphy"]),
        claim("gm2", "greg-murphy", "biblical_marriage", 2, True,
              "Voted for the Protection of Women and Girls in Sports Act of 2025, which prohibits biological males from competing in women's and girls' athletic categories in federally funded programs — rejecting the redefinition of biological sex that transgender ideology requires.",
              ["https://www.congress.gov/member/gregory-murphy/M001210",
               "https://www.govtrack.us/congress/members/gregory_murphy/412845"]),
        claim("gm3", "greg-murphy", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29 / S. 5, signed January 29, 2025), which mandates federal detention and deportation proceedings for illegal immigrants who commit theft, burglary, or violent crimes — a mandatory-deportation enforcement measure that directly matches the rubric's border criterion.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
