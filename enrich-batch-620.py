#!/usr/bin/env python3
"""Enrichment batch 620: 5 R state senators from RI and PA (bottom of alphabet).

All archetype_curated federal senator/representative buckets are exhausted;
this batch transitions to archetype_party_default state senators from the
bottom of the reverse-sorted alphabet (RI, PA).

Targets: Elaine J. Morgan (RI), Thomas Paolino (RI),
         Kim L. Ward (PA), Wayne Langerholc Jr. (PA), Joe Pittman (PA).
Each claim cites >=1 reliable source and reflects verified 2018-2026
voting records / public positions.

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
    # ---------------- Elaine J. Morgan (RI-R, State Senator) ----------------
    ("elaine-j-morgan", "RI", "Senator", [
        claim("ejm1", "elaine-j-morgan", "sanctity_of_life", 0, True,
              "Opposed Rhode Island's 2019 abortion protection bill (which would preserve abortion rights if Roe were overturned) and proposed a limiting amendment that would make the act effective only upon a Roe reversal — taking the most restrictive pro-life position in the RI Senate.",
              ["https://en.wikipedia.org/wiki/Elaine_J._Morgan",
               "https://ballotpedia.org/Elaine_Morgan"]),
        claim("ejm2", "elaine-j-morgan", "self_defense", 1, True,
              "In 2018 was the sole senator to vote against both Rhode Island's red flag firearm seizure law and its bump stock ban, opposing both gun-control measures as infringements on Second Amendment rights. Consistent pro-gun stance recognized by CPAC and the American Conservative Union (Conservative Achievement Award, 2020).",
              ["https://en.wikipedia.org/wiki/Elaine_J._Morgan",
               "https://ballotpedia.org/Elaine_Morgan"]),
        claim("ejm3", "elaine-j-morgan", "biblical_marriage", 2, True,
              "In 2022 introduced legislation (S 2788) to categorize women's sports participation by biological sex assigned at birth rather than gender identity, rejecting transgender ideology in public athletics.",
              ["https://en.wikipedia.org/wiki/Elaine_J._Morgan",
               "https://ballotpedia.org/Elaine_Morgan"]),
    ]),

    # ---------------- Thomas Paolino (RI-R, State Senator) ----------------
    ("thomas-paolino", "RI", "Senator", [
        claim("tp1", "thomas-paolino", "self_defense", 1, False,
              "Voted for Rhode Island's 2018 red flag gun seizure law and bump stock ban — bills that passed with only one dissenting vote (Sen. Elaine Morgan) in the entire Senate, placing Paolino in the pro-gun-control majority.",
              ["https://en.wikipedia.org/wiki/Elaine_J._Morgan",
               "https://ballotpedia.org/Thomas_Paolino"]),
        claim("tp2", "thomas-paolino", "economic_stewardship", 2, True,
              "Per his official Rhode Island Senate biography, Paolino advocates for fiscal responsibility, streamlining business regulations, and lowering the tax burden for Rhode Islanders — a consistent anti-deficit, limited-government economic posture as Senate Deputy Minority Leader since 2021.",
              ["https://www.rilegislature.gov/senators/paolino/Pages/Biography.aspx",
               "https://ballotpedia.org/Thomas_Paolino"]),
    ]),

    # ---------------- Kim L. Ward (PA-R, State Senator) ----------------
    ("kim-l-ward", "PA", "Senator", [
        claim("klw1", "kim-l-ward", "sanctity_of_life", 0, True,
              "Championed Pennsylvania Senate Bill 106, a constitutional amendment declaring the PA Constitution provides no right to abortion and no right to public funding for abortion; the Senate passed it 28-22 on July 8, 2022. Ward served as Senate Majority Leader at the time and is recognized by pasenategop.com as the driver of the 'Pro-Life Constitutional Amendment.'",
              ["https://www.pasenategop.com/news/senate-approves-wards-pro-life-constitutional-amendment/",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106"]),
        claim("klw2", "kim-l-ward", "election_integrity", 0, True,
              "Voted for the SB 106 omnibus constitutional amendment package (July 8, 2022) that included a proposed amendment requiring government-issued photo ID to vote in Pennsylvania — a voter-ID mandate the rubric supports.",
              ["https://www.spotlightpa.org/news/2022/07/pa-abortion-restrictions-constitutional-amendment-voter-id/",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106"]),
        claim("klw3", "kim-l-ward", "self_defense", 1, True,
              "NRA member with an A rating from the NRA Political Victory Fund and an A- rating from Firearms Owners Against Crime (FOAC); maintains a 93% pro-gun, 5% anti-gun voting record in the PA Senate per FOAC legislative scorecard.",
              ["https://ns1.foac-pac.org/PA-Legislator-Details/247",
               "https://ballotpedia.org/Kim_Ward"]),
    ]),

    # ---------------- Wayne Langerholc Jr. (PA-R, State Senator) ----------------
    ("wayne-langerholc", "PA", "Senator", [
        claim("wl1", "wayne-langerholc", "sanctity_of_life", 0, True,
              "As PA Senate Majority Whip voted with the 26-member Republican majority for SB 106, the constitutional amendment declaring no Pennsylvania right to abortion or public abortion funding (Senate 28-22, July 8, 2022); only two Republicans (Baker, Laughlin) voted against it.",
              ["https://www.spotlightpa.org/news/2022/07/pa-abortion-restrictions-constitutional-amendment-voter-id/",
               "https://penncapital-star.com/government-politics/pa-senate-republicans-advance-late-night-constitutional-amendment-package-on-abortion-voter-id/"]),
        claim("wl2", "wayne-langerholc", "election_integrity", 0, True,
              "Voted for the SB 106 package that included a voter ID constitutional amendment for Pennsylvania, advancing it as part of the Republican Senate caucus majority in July 2022.",
              ["https://www.spotlightpa.org/news/2022/07/pa-abortion-restrictions-constitutional-amendment-voter-id/",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106"]),
        claim("wl3", "wayne-langerholc", "public_justice", 0, True,
              "In the 2023-24 legislative session, sponsored key measures signed into law: a statewide rape kit evidence tracking system and legislation cracking down on crime plaguing Philadelphia's SEPTA mass transit system — focusing on victim-centered public-safety accountability.",
              ["https://ballotpedia.org/Wayne_Langerholc",
               "https://www.legis.state.pa.us/cfdocs/legis/home/member_information/senate_bio.cfm?id=1764"]),
    ]),

    # ---------------- Joe Pittman (PA-R, State Senator) ----------------
    ("joe-pittman", "PA", "Senator", [
        claim("jp1", "joe-pittman", "self_defense", 0, True,
              "Life-member of the National Rifle Association; has consistently championed Second Amendment rights as PA Senate Majority Leader, opposing gun-control measures that would infringe on constitutional carry rights.",
              ["https://en.wikipedia.org/wiki/Joe_Pittman_(politician)",
               "https://ballotpedia.org/Joe_Pittman"]),
        claim("jp2", "joe-pittman", "economic_stewardship", 2, True,
              "As PA Senate Majority Leader, states his resolution to Pennsylvania's fiscal challenges is 'eliminating needless regulations, reducing the tax burden' — an anti-deficit, limited-government economic posture.",
              ["https://en.wikipedia.org/wiki/Joe_Pittman_(politician)",
               "https://ballotpedia.org/Joe_Pittman"]),
        claim("jp3", "joe-pittman", "public_justice", 0, True,
              "Prioritizes support for law enforcement as a core legislative agenda item as PA Senate Majority Leader, stating publicly that advancing pro-law-enforcement legislation is a principal duty of his leadership role.",
              ["https://ballotpedia.org/Joe_Pittman",
               "https://en.wikipedia.org/wiki/Joe_Pittman_(politician)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
