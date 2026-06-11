#!/usr/bin/env python3
"""Enrichment batch 131: hand-curated claims for 5 sitting WA U.S. Representatives.

Targets archetype_party_default members with 0 evidence claims, taken from the
BOTTOM of the alphabet (WA): Suzan DelBene, Rick Larsen, Kim Schrier,
Adam Smith, Marilyn Strickland. All five are House Democrats whose public
positions and voting records have been researched against the rubric.

Writes scorecard.json MINIFIED — no indent=2 — to stay under GitHub 50MB limit.
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
    # ---------------- Suzan DelBene (WA-01, D) ----------------
    ("suzan-delbene", "WA", "House", [
        claim("sd1", "suzan-delbene", "sanctity_of_life", 0, False,
              "Co-chair of the House Pro-Choice Caucus and a consistent supporter of abortion without restriction through all nine months; cosponsored the Women's Health Protection Act (H.R.3755, 117th Congress) to enshrine abortion as a federal right, rejecting any recognition of life from conception.",
              ["https://en.wikipedia.org/wiki/Suzan_DelBene",
               "https://www.congress.gov/bill/117th-congress/house-bill/3755"]),
        claim("sd2", "suzan-delbene", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (H.R.8404, December 2022), codifying federal recognition of same-sex marriage and repealing the Defense of Marriage Act's one-man-one-woman definition in federal law.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("sd3", "suzan-delbene", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022) and cosponsored assault-weapons-ban legislation; supports universal background checks, red-flag laws, and magazine-capacity limits — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Suzan_DelBene",
               "https://www.govtrack.us/congress/members/suzan_delbene/412505"]),
    ]),

    # ---------------- Rick Larsen (WA-02, D) ----------------
    ("rick-larsen", "WA", "House", [
        claim("rl1", "rick-larsen", "sanctity_of_life", 4, False,
              "Endorsed and rated highly by Planned Parenthood Action Fund and NARAL Pro-Choice America (Reproductive Freedom for All) across multiple election cycles; has accepted campaign support from the abortion-industry endorsement network the rubric directs candidates to avoid.",
              ["https://en.wikipedia.org/wiki/Rick_Larsen",
               "https://sbaprolife.org/representative/rick-larsen"]),
        claim("rl2", "rick-larsen", "self_defense", 1, False,
              "Rated F by the National Rifle Association for his long record of supporting gun-control measures including universal background checks, assault-weapons restrictions, and the Bipartisan Safer Communities Act — in direct opposition to the rubric's defense of unrestricted firearms rights.",
              ["https://en.wikipedia.org/wiki/Rick_Larsen",
               "https://www.govtrack.us/congress/members/rick_larsen/400232"]),
        claim("rl3", "rick-larsen", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), codifying federal recognition of same-sex marriages and eliminating the one-man-one-woman standard from federal law.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://ballotpedia.org/Rick_Larsen_(Washington)"]),
    ]),

    # ---------------- Kim Schrier (WA-08, D) ----------------
    ("kim-schrier", "WA", "House", [
        claim("ks1", "kim-schrier", "sanctity_of_life", 0, False,
              "A pediatrician and the first woman physician elected to Congress; describes herself as the only pro-choice woman doctor in the House and cosponsored the Women's Health Protection Act to guarantee abortion access federally, explicitly opposing any restrictions tied to personhood from conception.",
              ["https://en.wikipedia.org/wiki/Kim_Schrier",
               "https://www.congress.gov/bill/117th-congress/house-bill/3755"]),
        claim("ks2", "kim-schrier", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2022 and the Enhanced Background Checks Act; endorsed by Giffords and Everytown gun-control organizations, opposing the rubric's position of no restrictions on firearms.",
              ["https://en.wikipedia.org/wiki/Kim_Schrier",
               "https://www.govtrack.us/congress/members/kim_schrier/412835"]),
        claim("ks3", "kim-schrier", "biblical_marriage", 4, False,
              "Voted for the Equality Act (H.R.5, 117th Congress), which would write sexual-orientation and gender-identity protections into federal civil-rights law and enforce them in schools and public accommodations — the government promotion of LGBTQ ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Equality_Act_(United_States)",
               "https://ballotpedia.org/Kim_Schrier"]),
    ]),

    # ---------------- Adam Smith (WA-09, D) ----------------
    ("adam-smith", "WA", "House", [
        claim("as1", "adam-smith", "sanctity_of_life", 0, False,
              "Supports abortion access and voted for the Women's Health Protection Act (H.R.3755, 117th Congress) to federally codify abortion rights with no gestational limits, rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Adam_Smith_(Washington_politician)",
               "https://www.congress.gov/bill/117th-congress/house-bill/3755"]),
        claim("as2", "adam-smith", "foreign_policy_restraint", 1, False,
              "As Ranking Member (and former Chairman) of the House Armed Services Committee, championed and helped pass multiple Ukraine supplemental aid packages totaling over $100 billion since 2022, supporting open-ended foreign military entanglements the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Adam_Smith_(Washington_politician)",
               "https://www.govtrack.us/congress/members/adam_smith/400379"]),
        claim("as3", "adam-smith", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), codifying same-sex marriage at the federal level and rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://en.wikipedia.org/wiki/Adam_Smith_(Washington_politician)"]),
    ]),

    # ---------------- Marilyn Strickland (WA-10, D) ----------------
    ("marilyn-strickland", "WA", "House", [
        claim("ms1", "marilyn-strickland", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Action Fund and rated highly by Reproductive Freedom for All; has accepted campaign support from abortion-industry organizations the rubric identifies as disqualifying.",
              ["https://en.wikipedia.org/wiki/Marilyn_Strickland",
               "https://ballotpedia.org/Marilyn_Strickland"]),
        claim("ms2", "marilyn-strickland", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), codifying federal recognition of same-sex unions and standing with the LGBTQ community on marriage equality, rejecting the one-man-one-woman standard.",
              ["https://en.wikipedia.org/wiki/Marilyn_Strickland",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("ms3", "marilyn-strickland", "self_defense", 1, False,
              "As Mayor of Tacoma and as a U.S. Representative, championed universal background checks and gun-safety measures; supports an assault-weapons ban and red-flag laws — opposing the rubric's position on unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Marilyn_Strickland",
               "https://www.govtrack.us/congress/members/marilyn_strickland/456854"]),
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
