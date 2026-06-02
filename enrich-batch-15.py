#!/usr/bin/env python3
"""Enrichment batch 15: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators from the bottom of the alphabet (MI, ME, MD, KS)
that had 0 evidence claims. Uses the (slug + state + office_keyword) matcher.

Mix (2 R / 3 D): Jerry Moran (KS-R), Susan Collins (ME-R),
Gary Peters (MI-D), Elissa Slotkin (MI-D), Chris Van Hollen (MD-D).
Each claim cites >=1 reliable source and reflects 2022-2026 voting
record / public positions.

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
    # ---------------- Jerry Moran (KS-R, US Senator) ----------------
    ("jerry-moran", "KS", "Senator", [
        claim("jm1", "jerry-moran", "sanctity_of_life", 0, True,
              "States on his Senate website that 'science demonstrates that each human life begins at conception' and that 'the right to life guaranteed by the U.S. Constitution is vested in each human being'; supports legislation protecting life at its earliest stages.",
              ["https://www.moran.senate.gov/public/index.cfm/life",
               "https://ballotpedia.org/Jerry_Moran"]),
        claim("jm2", "jerry-moran", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (2022), stating 'I am a strong defender of the Constitution and the Second Amendment'; opposed background-check expansions and red-flag-law funding that the bill contained.",
              ["https://www.moran.senate.gov/public/index.cfm/news-releases?ID=2BB952E9-865B-4291-9A8A-32C6D33A9D5C",
               "https://ballotpedia.org/Jerry_Moran"]),
        claim("jm3", "jerry-moran", "border_immigration", 0, True,
              "Traveled to El Paso to witness the southern border crisis and stated 'securing our borders is the first step'; supported the Secure the Border Act as 'a first step in addressing the humanitarian and national security crisis at our southern border.'",
              ["https://www.moran.senate.gov/public/index.cfm/immigration",
               "https://www.moran.senate.gov/public/index.cfm/news-releases?id=EF9EA023-C82A-4FBF-AF7E-7505377DFCCE"]),
    ]),

    # ---------------- Susan Collins (ME-R, US Senator) ----------------
    ("susan-collins", "ME", "Senator", [
        claim("sc1", "susan-collins", "sanctity_of_life", 0, False,
              "The most pro-choice Republican in the Senate; consistently opposes federal abortion restrictions lacking health exceptions, supports Planned Parenthood funding, and has never held a life-at-conception or personhood position — voting against bills that restrict abortion access.",
              ["https://ballotpedia.org/Susan_Collins_(Maine)",
               "https://www.govtrack.us/congress/members/susan_collins/300025"]),
        claim("sc2", "susan-collins", "biblical_marriage", 1, False,
              "Co-authored and co-led the Respect for Marriage Act (2022) with Sen. Tammy Baldwin, codifying federal recognition of same-sex marriage into U.S. law; attended the White House signing ceremony as a lead sponsor.",
              ["https://www.collins.senate.gov/newsroom/senate-passes-baldwin-collins-marriage-equality-bill",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
        claim("sc3", "susan-collins", "self_defense", 1, False,
              "Helped negotiate and co-led the Bipartisan Safer Communities Act (2022), which expands background checks for under-21 gun buyers, funds state red-flag laws, and tightens straw-purchase rules — directly advancing gun restrictions the rubric opposes.",
              ["https://www.collins.senate.gov/newsroom/senate-passes-bipartisan-gun-safety-legislation-negotiated-by-senator-collins-and-11-colleagues",
               "https://www.govtrack.us/congress/members/susan_collins/300025"]),
    ]),

    # ---------------- Gary Peters (MI-D, US Senator) ----------------
    ("gary-peters", "MI", "Senator", [
        claim("gp1", "gary-peters", "sanctity_of_life", 0, False,
              "Cosponsored and championed the Women's Health Protection Act to codify federal abortion access nationwide; took to the Senate floor to share his family's personal abortion story urging its passage, and in 2025 rejoined colleagues reintroducing the bill post-Dobbs.",
              ["https://www.peters.senate.gov/newsroom/press-releases/video-on-senate-floor-peters-urges-passage-of-womens-health-protection-act-and-shares-family-abortion-story",
               "https://ballotpedia.org/Gary_Peters"]),
        claim("gp2", "gary-peters", "self_defense", 1, False,
              "Delivered floor remarks calling for passage of the Bipartisan Safer Communities Act and celebrated it as 'the most significant legislation to address gun violence in nearly 30 years'; a consistent supporter of expanded background checks and red-flag laws.",
              ["https://www.peters.senate.gov/newsroom/press-releases/video-on-senate-floor-peters-calls-for-passage-of-bipartisan-safer-communities-act",
               "https://ballotpedia.org/Gary_Peters"]),
    ]),

    # ---------------- Elissa Slotkin (MI-D, US Senator) ----------------
    ("elissa-slotkin", "MI", "Senator", [
        claim("es1", "elissa-slotkin", "sanctity_of_life", 0, False,
              "Rated 100% by NARAL Pro-Choice America and Planned Parenthood Action Fund; cosponsored a Senate resolution to ensure equitable access to medication abortion — rejecting any personhood-from-conception standard.",
              ["https://justfacts.votesmart.org/candidate/key-votes/181080/elissa-slotkin/2/abortion",
               "https://ballotpedia.org/Elissa_Slotkin"]),
        claim("es2", "elissa-slotkin", "self_defense", 1, False,
              "Rated 0% by both the NRA and Gun Owners of America; supports an assault-weapons ban, universal background checks, red-flag laws, and safe-storage requirements — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://justfacts.votesmart.org/candidate/key-votes/181080/elissa-slotkin",
               "https://ballotpedia.org/Elissa_Slotkin"]),
        claim("es3", "elissa-slotkin", "border_immigration", 0, False,
              "Voted against the Secure the Border Act of 2023 (H.R. 2), which would have reinstated remain-in-Mexico policy, funded border-wall construction, and tightened asylum restrictions.",
              ["https://ballotpedia.org/Elissa_Slotkin",
               "https://www.govtrack.us/congress/members/elissa_slotkin/412784"]),
    ]),

    # ---------------- Chris Van Hollen (MD-D, US Senator) ----------------
    ("chris-van-hollen", "MD", "Senator", [
        claim("cvh1", "chris-van-hollen", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act and stated: 'We need to pass the Women's Health Protection Act to codify Roe and guarantee a woman's right to choose as a matter of law nationwide' — rejecting any personhood-from-conception standard.",
              ["https://www.vanhollen.senate.gov/news/press-releases/van-hollen-statement-on-womens-health-protection-act",
               "https://ballotpedia.org/Chris_Van_Hollen"]),
        claim("cvh2", "chris-van-hollen", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), stating 'The Bipartisan Safer Communities Act will help save lives, and I was proud to vote for it tonight'; supports expanded background checks and red-flag-law funding.",
              ["https://www.vanhollen.senate.gov/news/press-releases/van-hollen-statement-on-the-bipartisan-safer-communities-act",
               "https://ballotpedia.org/Chris_Van_Hollen"]),
        claim("cvh3", "chris-van-hollen", "biblical_marriage", 2, False,
              "Joined colleagues in pushing to strip anti-LGBTQ+ and anti-abortion provisions from critical government funding bills, opposing any legislative restriction on LGBTQ+ promotion in public policy.",
              ["https://www.vanhollen.senate.gov/news/press-releases/van-hollen-joins-merkley-baldwin-booker-colleagues-in-pushing-to-keep-anti-lgbtq-and-anti-abortion-provisions-out-of-critical-government-funding-bills",
               "https://ballotpedia.org/Chris_Van_Hollen"]),
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
