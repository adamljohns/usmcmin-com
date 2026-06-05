#!/usr/bin/env python3
"""Enrichment batch 49: hand-curated claims for 5 federal House candidates.

Targets archetype_curated House candidates that had 0 evidence claims, taken
from the bottom of the alphabet (NY > NJ > MN > MD > MA), consistent with
the bottom-of-alphabet assignment for this agent.

Mix (5 D): Micah Lasher (NY-12), Sue Altman (NJ-12), Ilhan Omar (MN-05),
Harry Dunn (MD-05), Ayanna Pressley (MA-07).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Micah Lasher (NY-12, D) ----------------
    ("micah-lasher", "NY", "Representative", [
        claim("ml1", "micah-lasher", "self_defense", 1, False,
              "Served on the board of Everytown for Gun Safety, the nation's leading gun-control organization, and immediately after the 2022 Buffalo and Uvalde mass shootings played a leading role in writing and enacting sweeping New York gun safety legislation — a record that directly opposes constitutional carry and resistance to assault-weapons restrictions.",
              ["https://ny1.com/nyc/all-boroughs/inside-city-hall/2026/03/13/micah-lasher-vies-for-jerrold-nadler-s-manhattan-congressional-seat",
               "https://micahlasher.com/meet-micah-lasher/"]),
        claim("ml2", "micah-lasher", "sanctity_of_life", 4, False,
              "Earned the endorsement of Planned Parenthood of Greater New York Votes during his 2024 State Assembly campaign, placing him squarely within the abortion-industry endorsement network.",
              ["https://ny1.com/nyc/all-boroughs/inside-city-hall/2026/03/13/micah-lasher-vies-for-jerrold-nadler-s-manhattan-congressional-seat"]),
        claim("ml3", "micah-lasher", "biblical_marriage", 2, False,
              "Supports the Equality Act and codifying Biden-era executive orders protecting transgender and gender-nonconforming individuals from discrimination and ensuring access to gender-affirming care — explicitly a legislative priority in his 2026 congressional campaign.",
              ["https://micahlasher.com/platform-and-policies/",
               "https://voterguide.abundanceny.org/questionnaires/micah-lasher-questionnaire"]),
    ]),

    # ---------------- Sue Altman (NJ-12, D) ----------------
    ("sue-altman", "NJ", "Representative", [
        claim("sa1", "sue-altman", "sanctity_of_life", 4, False,
              "A pro-abortion-rights champion who attacked her 2024 congressional opponent Rep. Tom Kean Jr. for '23 years of votes against Planned Parenthood' and for opposing codifying Roe v. Wade — making abortion access and Planned Parenthood funding central to her campaign platform.",
              ["https://www.cbsnews.com/newyork/news/tom-kean-sue-altman-new-jersey-district-7/"]),
        claim("sa2", "sue-altman", "border_immigration", 1, False,
              "Protested outside Delaney Hall immigration detention center in New Jersey on Memorial Day 2026, standing in solidarity with detained immigrants on a work and hunger strike; decried the facility as 'not what we should be as Americans,' opposing immigration enforcement and detention.",
              ["https://www.insidernj.com/cd-12-flashpoint-sue-altman-outside-delaney-hall-this-is-not-what-we-should-be-as-americans/"]),
    ]),

    # ---------------- Ilhan Omar (MN-05, D) ----------------
    ("ilhan-omar", "MN", "House", [
        claim("io1", "ilhan-omar", "border_immigration", 1, False,
              "Has repeatedly called to abolish ICE, calling current immigration detention and deportation enforcement 'un-American,' and fights for a pathway to citizenship for all 11 million undocumented immigrants in the United States — directly opposing mandatory deportation and border security enforcement.",
              ["https://omar.house.gov/issues/immigration",
               "https://foxnews.com/politics/ilhan-omar-unamerican-ice-detain-immigrants"]),
        claim("io2", "ilhan-omar", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2023 (H.R. 698 in the 118th Congress), which would have banned semi-automatic firearms with military-style features; also supports banning high-capacity magazines and requiring universal background checks for every firearm sale.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors"]),
        claim("io3", "ilhan-omar", "sanctity_of_life", 4, False,
              "Receives 0% from SBA Pro-Life America and is endorsed by Planned Parenthood Action Fund with a 100% pro-choice score; has never cast a pro-life vote in Congress, placing her squarely within the abortion-industry endorsement network.",
              ["https://sbaprolife.org/representative/ilhan-omar",
               "https://reproductivefreedomforall.org/lawmaker/ilhan-omar/"]),
    ]),

    # ---------------- Harry Dunn (MD-05, D) ----------------
    ("harry-dunn-md-05", "MD", "Representative", [
        claim("hd1", "harry-dunn-md-05", "border_immigration", 1, False,
              "Publicly stated that ICE should be 'abolished' because 'I don't think there is a logical way to train your way out of this' — directly opposing the rubric's call for mandatory deportation enforcement and secure borders.",
              ["https://www.nbcnews.com/politics/2026-election/former-capitol-police-officer-harry-dunn-launches-another-run-congress-rcna257319"]),
        claim("hd2", "harry-dunn-md-05", "self_defense", 1, False,
              "Campaigns on gun reform and gun violence prevention as a central issue alongside abortion and healthcare, drawing on his experience as a Capitol Police officer who defended the Capitol on January 6, 2021 — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.nbcnews.com/politics/2026-election/former-capitol-police-officer-harry-dunn-launches-another-run-congress-rcna257319",
               "https://rollcall.com/2026/02/04/harry-dunn-house-election-maryland-democrat/"]),
    ]),

    # ---------------- Ayanna Pressley (MA-07, D) ----------------
    ("ayanna-pressley", "MA", "Representative", [
        claim("ap1", "ayanna-pressley", "sanctity_of_life", 4, False,
              "Holds a 100% score from Reproductive Freedom for All (NARAL's successor) and was endorsed by Planned Parenthood Action Fund; in January 2025 she was named Co-Chair of the House Reproductive Freedom Caucus for the 119th Congress and introduced a resolution recognizing Abortion Provider Appreciation Day.",
              ["https://reproductivefreedomforall.org/lawmaker/ayanna-pressley/",
               "https://pressley.house.gov/2025/01/09/pressley-to-serve-as-co-chair-of-reproductive-freedom-caucus-for-119th-congress/"]),
        claim("ap2", "ayanna-pressley", "self_defense", 1, False,
              "A vocal gun-control advocate who calls for an assault-weapons ban, universal background checks, comprehensive red-flag laws, and raising the federal firearms purchase age to 21; praised House passage of the Bipartisan Safer Communities Act (2022), saying 'failure is not an option' on gun legislation.",
              ["https://pressley.house.gov/2022/06/09/pressley-statement-on-house-passage-of-gun-violence-prevention-legislation/",
               "https://www.wgbh.org/news/politics/2022-06-01/failure-is-not-an-option-rep-pressley-calls-for-stricter-gun-control"]),
        claim("ap3", "ayanna-pressley", "biblical_marriage", 4, False,
              "Spoke in support of H.R. 5, the Equality Act, providing sweeping federal non-discrimination protections for LGBTQ Americans in schools and public accommodations; introduced the Equality in Our Laws Act to make the federal U.S. Code more inclusive of gender-nonconforming, nonbinary, and intersex individuals.",
              ["https://pressley.house.gov/media/press-releases/rep-pressley-speaks-support-hr-5-equality-act",
               "https://pressley.house.gov/2023/07/25/pressley-lee-garcia-introduce-equality-in-our-laws-act/"]),
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
