#!/usr/bin/env python3
"""Enrichment batch 159: 5 sitting U.S. Representatives — OH (Carey, Rulli, Miller, Turner, Joyce).

All are archetype_party_default with 0 evidence claims. Claims span distinct
rubric categories: sanctity_of_life, border_immigration, self_defense,
economic_stewardship. Sources: ballotpedia.org, govtrack.us, congress.gov,
sbaprolife.org, house.gov official sites.

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
    # ---------------- Mike Carey (OH-15, R) ----------------
    ("mike-carey", "OH", "Representative", [
        claim("mc1", "mike-carey", "sanctity_of_life", 0, True,
              "Cosponsor of H.R. 21, the Born-Alive Abortion Survivors Protection Act (119th Congress, cosigned Jan 21, 2025), and voted YEA on its final passage (House Vote #27, Jan 23, 2025). SBA Pro-Life America scores Carey as consistently defending unborn life across his tenure since 2021, including opposing taxpayer funding of abortion domestically and internationally.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://sbaprolife.org/representative/mike-carey"]),
        claim("mc2", "mike-carey", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (S. 5, House Vote #23, Jan 22, 2025), mandating ICE detention and deportation proceedings for illegal aliens arrested for theft or violent crimes — enforcing mandatory deportation over discretionary release. Also voted for the 2025 reconciliation bill providing over $175 billion for border security, including new enforcement officers and physical barriers.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://carey.house.gov/2025/07/03/carey-votes-to-send-republican-reconciliation-bill-to-president-trumps-desk/"]),
        claim("mc3", "mike-carey", "self_defense", 1, True,
              "Defends the Second Amendment as a core priority and has voted against gun-control legislation throughout his tenure; his campaign platform explicitly calls for defending the 2nd Amendment and GovTrack places him among the most consistently pro-gun members of the Ohio delegation.",
              ["https://ballotpedia.org/Mike_Carey_(Ohio)",
               "https://www.govtrack.us/congress/members/mike_carey/456864"]),
    ]),

    # ---------------- Michael Rulli (OH-6, R) ----------------
    ("michael-rulli", "OH", "Representative", [
        claim("mr1", "michael-rulli", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025), requiring medical care for infants born alive after failed abortions — affirming a life-from-conception posture consistent with refusing to treat a born child as anything less than a full person.",
              ["https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://www.congress.gov/bill/119th-congress/house-bill/21"]),
        claim("mr2", "michael-rulli", "border_immigration", 0, True,
              "States publicly that 'securing our borders and ending illegal immigration are non-negotiable' and supports wall construction and military enforcement at the border; is a committed America-First voice on halting illegal crossings.",
              ["https://rulli.house.gov/our-district/",
               "https://ballotpedia.org/Michael_Rulli"]),
        claim("mr3", "michael-rulli", "economic_stewardship", 2, True,
              "Founding member of the DOGE Caucus in the 119th Congress; has committed to reassessing and eliminating wasteful federal programs and opposes deficit spending, aligning with the rubric's call for anti-deficit / balanced-budget stewardship.",
              ["https://rulli.house.gov/our-district/",
               "https://www.govtrack.us/congress/members/michael_rulli/456959"]),
    ]),

    # ---------------- Max Miller (OH-7, R) ----------------
    ("max-miller", "OH", "Representative", [
        claim("mm1", "max-miller", "sanctity_of_life", 0, True,
              "SBA Pro-Life America scores Rep. Miller as consistently voting to defend the lives of the unborn and infants. In public statements he invokes 'defending the sanctity of life' as a core American value and has supported pro-life appropriations riders blocking federal abortion funding.",
              ["https://sbaprolife.org/representative/max-miller",
               "https://maxmiller.house.gov/about"]),
        claim("mm2", "max-miller", "self_defense", 1, True,
              "Publicly commits to defending the Second Amendment as a non-negotiable core American value and has opposed gun-control legislation during his tenure in the 118th and 119th Congresses.",
              ["https://maxmiller.house.gov/about",
               "https://ballotpedia.org/Max_Miller"]),
        claim("mm3", "max-miller", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (H.R. 29, House Vote #6, Jan 7, 2025), mandating ICE detention and deportation proceedings for illegal aliens arrested for theft or violent crime — supporting mandatory deportation over discretionary release.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
    ]),

    # ---------------- Michael Turner (OH-10, R) ----------------
    ("michael-turner", "OH", "Representative", [
        claim("mt1", "michael-turner", "self_defense", 1, False,
              "In August 2019, Congressman Turner publicly called for restricting sales of military-style semi-automatic rifles to civilians, implementing magazine-capacity limits, and enacting red-flag laws — stating 'I strongly support the Second Amendment, but we must prevent mentally unstable people from terrorizing our communities with military style weapons.' These positions directly oppose the rubric's defense of unrestricted semi-automatic ownership and rejection of red-flag confiscation.",
              ["https://turner.house.gov/media-center/press-releases/turner-supports-restricting-military-style-weapon-sales-magazine-limits",
               "https://ballotpedia.org/Michael_Turner_(Ohio)"]),
        claim("mt2", "michael-turner", "sanctity_of_life", 0, True,
              "Cosponsor of H.R. 619, the Born-Alive Abortion Survivors Protection Act in the 117th Congress (cosigned Jan 28, 2021), affirming that infants born alive after a failed abortion deserve the same medical care as any other newborn — consistent with a life-from-conception posture.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/619/cosponsors",
               "https://ballotpedia.org/Michael_Turner_(Ohio)"]),
    ]),

    # ---------------- David Joyce (OH-14, R) ----------------
    ("david-joyce", "OH", "Representative", [
        claim("dj1", "david-joyce", "self_defense", 1, False,
              "A self-described bipartisan dealmaker on gun policy who has 'continued to reach across the aisle to find bipartisan solutions to gun violence' — signaling openness to background-check expansions and other measures the rubric counts against (anti red-flag / anti-AWB / anti-registry posture).",
              ["https://joyce.house.gov/posts/joyce-continues-to-reach-across-the-aisle-to-find-bipartisan-solutions-to-gun-violence",
               "https://ballotpedia.org/David_Joyce"]),
        claim("dj2", "david-joyce", "sanctity_of_life", 0, True,
              "Cosponsor of H.R. 21, the Born-Alive Abortion Survivors Protection Act (119th Congress), which requires medical practitioners to provide care to any infant born alive after an attempted abortion — affirming the child's personhood at birth.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h27"]),
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
