#!/usr/bin/env python3
"""Enrichment batch 68: hand-curated claims for 5 state-level candidates (bottom of alphabet).

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the reverse-sorted bucket to avoid collision with the concurrent
top-of-alphabet agent.

Mix (4 R / 1 D): Frank LaRose (OH SoS), Steve Hobbs (WA SoS, D),
Blaise Ingoglia (FL CFO), Darren Bailey (IL Gov R nominee),
Mike Mazzei (OK Gov R candidate).

Each claim cites >=1 reliable source and reflects 2024-2026 record/positions.

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
    # ---------------- Frank LaRose (OH-R, Secretary of State) ----------------
    ("frank-larose-sos-2026", "OH", "Secretary of State", [
        claim("fl1", "frank-larose-sos-2026", "election_integrity", 0, True,
              "In November 2025 LaRose endorsed legislation requiring documentary proof of U.S. citizenship to register to vote in Ohio, and in December 2025 formalized a historic 20-year agreement with the federal government giving Ohio access to the SAVE System to verify citizenship for all registered voters — directly backing the rubric's demand for citizenship-based voter qualification.",
              ["https://www.ohiosos.gov/media-center/press-releases/2025/2025-12-01/",
               "https://en.wikipedia.org/wiki/Frank_LaRose"]),
        claim("fl2", "frank-larose-sos-2026", "election_integrity", 1, True,
              "In 2024, LaRose's office completed Ohio's annual voter-roll maintenance, removing 154,995 inactive and out-of-date registrations; in June 2025 he issued Ohio's sixth statewide election security directive — the most aggressive election infrastructure standards in the nation — and created Ohio's first Public Integrity Division to investigate election-law violations.",
              ["https://www.ohiosos.gov/media-center/press-releases/2024/2024-08-02/",
               "https://www.ohiosos.gov/media-center/press-releases/2025/2025-06-02/"]),
        claim("fl3", "frank-larose-sos-2026", "sanctity_of_life", 0, True,
              "As an Ohio state senator in 2017, LaRose sponsored legislation to prevent abortions after a fetal Down syndrome diagnosis — a targeted pro-life intervention against selective abortion that affirms the dignity of the unborn regardless of disability, consistent with the rubric's personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Frank_LaRose"]),
    ]),

    # ---------------- Steve Hobbs (WA-D, Secretary of State) ----------------
    ("steve-hobbs-sos-2026", "WA", "Secretary of State", [
        claim("sh1", "steve-hobbs-sos-2026", "election_integrity", 2, False,
              "As Washington Secretary of State, Hobbs administers and defends the state's universal vote-by-mail system — every registered voter automatically receives a mail ballot for every election under state law — the mass mail-in infrastructure the rubric opposes as undermining election security and in-person accountability.",
              ["https://www.sos.wa.gov/elections",
               "https://en.wikipedia.org/wiki/Steve_Hobbs_(Washington_politician)"]),
        claim("sh2", "steve-hobbs-sos-2026", "sanctity_of_life", 0, False,
              "A Democrat who served 15 years in the Washington State Senate Democratic caucus and won his 2024 Secretary of State reelection with Washington State Democrats' endorsement; he has made no public statement supporting any restriction on abortion, consistent with the Democratic Party's defense of Washington's broad abortion access laws.",
              ["https://en.wikipedia.org/wiki/Steve_Hobbs_(Washington_politician)",
               "https://ballotpedia.org/Steve_Hobbs_(Washington)"]),
    ]),

    # ---------------- Blaise Ingoglia (FL-R, Chief Financial Officer) ----------------
    ("blaise-ingoglia-cfo", "FL", "Chief Financial Officer", [
        claim("bi1", "blaise-ingoglia-cfo", "sanctity_of_life", 0, True,
              "As a Florida state senator, Ingoglia voted with the Republican supermajority for Florida's Heartbeat Protection Act (SB 300, 2023), signed by Governor DeSantis, which bans abortion once a fetal heartbeat is detectable at approximately six weeks — one of the nation's most protective abortion limits at the time of passage.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://en.wikipedia.org/wiki/Blaise_Ingoglia"]),
        claim("bi2", "blaise-ingoglia-cfo", "economic_stewardship", 4, True,
              "As Florida's Chief Financial Officer since July 2025, Ingoglia administers Florida's investment policy under SB 7014 (2022) which bars fund managers from using ESG criteria when investing state assets — legislation he supported as a sitting state senator under DeSantis's anti-ESG agenda that made Florida the national leader in divesting from ESG-screened funds.",
              ["https://en.wikipedia.org/wiki/Blaise_Ingoglia",
               "https://ballotpedia.org/Blaise_Ingoglia"]),
        claim("bi3", "blaise-ingoglia-cfo", "family_child_sovereignty", 0, True,
              "As a Florida state senator (2022-2025), Ingoglia voted with the Republican supermajority for HB 1069 (2023) — Florida's expanded Parental Rights in Education law — extending classroom restrictions on LGBTQ and gender-ideology instruction through 12th grade and reinforcing parents' authority over their children's education, consistent with the rubric's parental sovereignty standard.",
              ["https://en.wikipedia.org/wiki/Blaise_Ingoglia",
               "https://ballotpedia.org/Blaise_Ingoglia"]),
    ]),

    # ---------------- Darren Bailey (IL-R, 2026 Governor nominee) ----------------
    ("darren-bailey-gov-2026", "IL", "Governor", [
        claim("db1", "darren-bailey-gov-2026", "sanctity_of_life", 0, True,
              "Bailey vocally opposes abortion and praised the Supreme Court's 2022 Dobbs decision overturning Roe v. Wade. He supports a near-total abortion ban in Illinois, allowing an exception only when the mother's life is directly at risk and rejecting exceptions for rape or incest — consistent with the rubric's life-at-conception personhood standard.",
              ["https://en.wikipedia.org/wiki/Darren_Bailey",
               "https://ontheissues.org/Governor/Darren_Bailey_Abortion.htm"]),
        claim("db2", "darren-bailey-gov-2026", "self_defense", 1, True,
              "A strong Second Amendment advocate throughout his state legislative career, Bailey opposed Illinois' 2023 Protect Illinois Communities Act (PICA) — the state's sweeping assault-weapons and high-capacity-magazine ban — and has consistently opposed new firearms restrictions, aligning with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Darren_Bailey",
               "https://ballotpedia.org/Darren_Bailey"]),
        claim("db3", "darren-bailey-gov-2026", "family_child_sovereignty", 0, True,
              "Bailey's 2026 governor platform explicitly centers parental authority in education, pledging to 'empower parents to make choices for their children' and opposing ideologically driven school curricula — consistent with the rubric's parental rights, homeschool protection, and anti-CPS-overreach standards.",
              ["https://ballotpedia.org/Darren_Bailey",
               "https://en.wikipedia.org/wiki/Darren_Bailey"]),
    ]),

    # ---------------- Mike Mazzei (OK-R, 2026 Governor candidate) ----------------
    ("mike-mazzei-gov", "OK", "Governor", [
        claim("mm1", "mike-mazzei-gov", "economic_stewardship", 2, True,
              "As Chairman of the Oklahoma Senate Finance Committee during his 12 years in the state senate (2004-2016) and as Governor Stitt's Secretary of Budget (2019-2020), Mazzei built a career around controlling state expenditures, preventing deficit spending, and enforcing fiscal discipline — directly aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Mike_Mazzei",
               "https://ballotpedia.org/Mike_Mazzei"]),
        claim("mm2", "mike-mazzei-gov", "sanctity_of_life", 0, True,
              "Mazzei is running in Oklahoma's 2026 Republican gubernatorial primary with the endorsement of U.S. Representative Josh Brecheen (OK-02), a leading House pro-life conservative. As an Oklahoma Republican state senator for 12 years, Mazzei served in the Republican caucus that consistently advanced Oklahoma's increasingly restrictive pro-life legislation throughout the 2004-2016 era.",
              ["https://en.wikipedia.org/wiki/Mike_Mazzei",
               "https://ballotpedia.org/Mike_Mazzei"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
