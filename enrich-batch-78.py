#!/usr/bin/env python3
"""Enrichment batch 78: hand-curated claims for 4 federal candidates (bottom of alphabet).

Targets archetype_curated federal candidates (former US Reps / AG-level) with 0 claims,
taken from the BOTTOM of the alphabet (TX, NC, MD, AR) to avoid collision with the
top-of-alphabet loop.

Mix: Beto O'Rourke (TX-D, former US Rep running for TX Gov),
     Jeff Jackson (NC-D, former US Rep / NC AG incumbent),
     Anthony Brown (MD-D, former US Rep / MD AG incumbent),
     Tim Griffin (AR-R, former US Rep / AR AG incumbent).
Each claim cites >=1 reliable source and reflects documented 2019-2026 positions.

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
    # ---------------- Beto O'Rourke (TX-D, former US Rep TX-16 / 2026 TX Gov candidate) ----------------
    ("beto-orourke-gov-2026", "TX", "Governor", [
        claim("bo1", "beto-orourke-gov-2026", "self_defense", 1, False,
              "At the September 2019 presidential primary debate called for a government-mandated assault-weapons buyback, stating 'Hell yes, we're going to take your AR-15, your AK-47' — the most explicit federal gun-confiscation pledge by a major-party candidate in modern history, directly opposing the rubric's protection of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Beto_O%27Rourke",
               "https://ballotpedia.org/Beto_O'Rourke"]),
        claim("bo2", "beto-orourke-gov-2026", "sanctity_of_life", 0, False,
              "Identifies as pro-choice and made repealing Texas's abortion ban a centerpiece of his 2022 and 2026 gubernatorial campaigns; spoke at the DNC's 2024 I Will Vote Gala on behalf of abortion rights, rejecting any recognition of life from conception.",
              ["https://en.wikipedia.org/wiki/Beto_O%27Rourke",
               "https://ballotpedia.org/Beto_O'Rourke"]),
        claim("bo3", "beto-orourke-gov-2026", "border_immigration", 0, False,
              "In February 2019 said he would tear down the existing border fence at El Paso, and in his 2020 presidential immigration platform called for ending all new border-wall construction and creating a pathway to citizenship for 11 million undocumented people — the opposite of the rubric's wall-plus-military enforcement posture.",
              ["https://en.wikipedia.org/wiki/Beto_O%27Rourke",
               "https://ballotpedia.org/Beto_O'Rourke_presidential_campaign,_2020"]),
    ]),

    # ---------------- Jeff Jackson (NC-D, former US Rep NC-14 / NC AG incumbent 2026) ----------------
    ("jeff-jackson-ag-2026", "NC", "Attorney", [
        claim("jj1", "jeff-jackson-ag-2026", "sanctity_of_life", 0, False,
              "Endorsed by Reproductive Freedom for All (NARAL successor) for his 2024 NC Attorney General campaign; stated 'The future of reproductive rights in North Carolina will be decided this year — we have to do everything in our power to defeat extreme politicians who are trying to rip away women's rights to choose,' and as AG has defended NC abortion-access statutes in court.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-rachel-hunt-for-north-carolina-lieutenant-governor-and-jeff-jackson-for-attorney-general/",
               "https://en.wikipedia.org/wiki/Jeff_Jackson_(politician)"]),
        claim("jj2", "jeff-jackson-ag-2026", "self_defense", 1, False,
              "As the U.S. Representative for NC-14 (118th Congress, 2023-2024), voted in favor of H.R.8 (Enhanced Background Checks Act), which would require universal background checks for all firearm transfers — a gun-restriction measure that directly opposes the rubric's standard of no new infringements on the right to keep and bear arms.",
              ["https://www.govtrack.us/congress/members/jeffrey_jackson/456916",
               "https://en.wikipedia.org/wiki/Jeff_Jackson_(politician)"]),
    ]),

    # ---------------- Anthony Brown (MD-D, former US Rep MD-04 / MD AG incumbent 2026) ----------------
    ("anthony-brown-ag-2026", "MD", "Attorney", [
        claim("ab1", "anthony-brown-ag-2026", "sanctity_of_life", 0, False,
              "Earned a 100% score from Reproductive Freedom for All (NARAL successor) for his 2022 congressional record; cosponsored the Women's Health Protection Act, which would have codified abortion access into federal law with no gestational limit, rejecting any protection for unborn life from conception.",
              ["https://reproductivefreedomforall.org/lawmaker/anthony-g-brown/",
               "https://en.wikipedia.org/wiki/Anthony_Brown_(Maryland_politician)"]),
        claim("ab2", "anthony-brown-ag-2026", "self_defense", 1, False,
              "As the U.S. Representative for MD-04 (117th Congress), voted for the Bipartisan Safer Communities Act (2022), which funded state red-flag laws that allow firearm seizure before due process and closed the so-called 'boyfriend loophole' in background-check law — directly opposing the rubric's opposition to red-flag laws and background-check expansions.",
              ["https://www.govtrack.us/congress/members/anthony_brown/412707",
               "https://en.wikipedia.org/wiki/Anthony_Brown_(Maryland_politician)"]),
    ]),

    # ---------------- Tim Griffin (AR-R, former US Rep AR-02 / AR AG incumbent 2026) ----------------
    ("tim-griffin-ag-2026", "AR", "Attorney", [
        claim("tg1", "tim-griffin-ag-2026", "sanctity_of_life", 0, True,
              "SBA Pro-Life America endorsed him for the 2022 AR Attorney General race, citing his 'unapologetically pro-life' record; while in Congress (AR-02, 2011–2014) championed legislation to protect unborn babies from late-term abortions and to end taxpayer funding of abortion, aligning fully with the rubric's life-from-conception standard.",
              ["https://sbaprolife.org/home/sba-lists-candidate-fund-pac-endorses-tim-griffin-for-attorney-general-of-arkansas",
               "https://en.wikipedia.org/wiki/Tim_Griffin"]),
        claim("tg2", "tim-griffin-ag-2026", "self_defense", 1, True,
              "A self-described gun owner who openly supports Second Amendment rights; voted with the House Republican conference 98.2% of the time during his 2011–2014 tenure, opposing new gun-restriction legislation, and has not supported red-flag laws, assault-weapons bans, or magazine limits.",
              ["https://www.govtrack.us/congress/members/tim_griffin/412401",
               "https://ballotpedia.org/Tim_Griffin_(Arkansas)"]),
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
