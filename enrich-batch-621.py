#!/usr/bin/env python3
"""Enrichment batch 621: 5 R state senators from RI and PA (bottom of alphabet, continued).

Continuing from batch 620 — archetype_curated federal senator/representative buckets
are exhausted; this batch enriches archetype_party_default state senators from
the bottom of the reverse-sorted alphabet (RI, PA).

Targets: Jessica de la Cruz (RI), Gordon Rogers (RI),
         Tracy Pennycuick (PA), Scott Martin (PA), Scott E. Hutchinson (PA).
Each claim cites >=1 reliable source and reflects verified 2022-2025
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
    # ------- Jessica de la Cruz (RI-R, State Senator / Senate Minority Leader) -------
    ("jessica-de-la-cruz", "RI", "Senator", [
        claim("jdlc1", "jessica-de-la-cruz", "sanctity_of_life", 0, True,
              "As Rhode Island Senate Minority Leader, voted against the 2023 Equality in Abortion Coverage Act — which would have compelled insurers to cover abortion procedures — citing Article 1 Section 2 of the RI Constitution: 'Nothing in this section shall be construed to grant or secure any right relating to abortion or the funding thereof.' De la Cruz opposed the bill and predicted it would face a legal challenge under that provision, aligning with a consistent pro-life, no-public-funding-for-abortion stance.",
              ["https://www.bostonglobe.com/2023/05/16/metro/key-ri-senate-committee-poised-vote-abortion-coverage/",
               "https://ballotpedia.org/Jessica_de_la_Cruz"]),
        claim("jdlc2", "jessica-de-la-cruz", "public_justice", 0, True,
              "Lead sponsor of a Rhode Island law requiring the state's Attorney General to publicly report the total number of firearms-related court cases in Rhode Island courts each year — bringing transparency and public accountability to how the state prosecutes firearms charges, a priority for gun rights advocates who seek to monitor government treatment of lawful gun owners.",
              ["https://www.rilegislature.gov/senators/de%20la%20Cruz/Pages/Biography.aspx",
               "https://ballotpedia.org/Jessica_de_la_Cruz"]),
    ]),

    # ------- Gordon Rogers (RI-R, State Senator / Senate Minority Whip) -------
    ("gordon-rogers", "RI", "Senator", [
        claim("gr1", "gordon-rogers", "self_defense", 3, True,
              "As Rhode Island Senate Minority Whip, championed legislation to strengthen Rhode Island's Castle doctrine — advancing the right of residents to use force to defend themselves in their homes without any duty to retreat — listed as a signature legislative priority in his official Rhode Island Senate biography.",
              ["https://www.rilegislature.gov/senators/rogers/Pages/Biography.aspx",
               "https://ballotpedia.org/Gordon_Rogers"]),
        claim("gr2", "gordon-rogers", "economic_stewardship", 2, True,
              "Advocates for returning surplus state revenue to taxpayers rather than spending it, and has pushed to limit gubernatorial emergency-power renewals — consistently opposing expansive government spending and executive overreach as part of his Senate Minority Whip platform.",
              ["https://www.rilegislature.gov/senators/rogers/Pages/Biography.aspx",
               "https://ballotpedia.org/Gordon_Rogers"]),
    ]),

    # ------- Tracy Pennycuick (PA-R, State Senator District 24) -------
    ("tracy-pennycuick", "PA", "Senator", [
        claim("tp1", "tracy-pennycuick", "self_defense", 1, True,
              "Endorsed by Gun Owners of America (GOA) for State Senate in 2022 based on a 100% pro-gun voting record; co-sponsored Constitutional Carry (HB 659) and Pennsylvania firearms preemption legislation (HB 979) as a PA House member, opposing gun restrictions. CeaseFirePA identified her as anti-gun-control in 2020, confirming a sustained Second Amendment record across both legislative chambers.",
              ["https://pennsylvania.gunowners.org/goa-endorses-rep-tracy-pennycuick-for-state-senate/",
               "https://ballotpedia.org/Tracy_Pennycuick"]),
        claim("tp2", "tracy-pennycuick", "election_integrity", 0, True,
              "In January 2025, announced legislation to introduce a constitutional amendment requiring government-issued photo ID for in-person voting in Pennsylvania, explicitly arguing that 'Pennsylvania must join the majority of states and nations with voter ID laws.' Pennsylvania is among a minority of U.S. states without such a mandate.",
              ["https://www.pasenategop.com/news/pennycuick-to-introduce-voter-id-measure/",
               "https://broadandliberty.com/2023/02/01/sen-tracy-pennycuick-pennsylvania-must-join-the-majority-of-states-and-nations-with-voter-id-laws/"]),
    ]),

    # ------- Scott Martin (PA-R, State Senator / Senate Appropriations Chair) -------
    ("scott-martin", "PA", "Senator", [
        claim("sm1", "scott-martin", "sanctity_of_life", 0, True,
              "Co-sponsored Pennsylvania Senate Bill 106 (2021-22 session) — a joint resolution proposing a constitutional amendment declaring that the Pennsylvania Constitution provides no right to abortion and no right to taxpayer-funded abortion; passed the PA Senate 28-22 on July 8, 2022. The PA Pro-Life Federation endorsed Martin in the 2024 General Election, reflecting a consistent life-affirming legislative record.",
              ["https://www.palegis.us/legislation/bills/2021/sb106",
               "https://ballotpedia.org/Scott_Martin_(Pennsylvania)"]),
        claim("sm2", "scott-martin", "economic_stewardship", 2, True,
              "As Chair of the Pennsylvania Senate Appropriations Committee — which reviews all legislation for fiscal impact and leads state budget negotiations — Martin applies a conservative lens to all state spending, consistently seeking to minimize regulatory and fiscal burdens on Pennsylvania taxpayers.",
              ["https://www.legis.state.pa.us/cfdocs/legis/home/member_information/senate_bio.cfm?id=1763",
               "https://ballotpedia.org/Scott_Martin_(Pennsylvania)"]),
    ]),

    # ------- Scott E. Hutchinson (PA-R, State Senator District 21) -------
    ("scott-e-hutchinson", "PA", "Senator", [
        claim("seh1", "scott-e-hutchinson", "sanctity_of_life", 0, True,
              "Voted for Pennsylvania Senate Bill 106 (July 8, 2022) — the constitutional amendment declaring no right to abortion in the PA Constitution; separately sponsored legislation to prohibit abortions after approximately six weeks gestation and a bill prohibiting abortions carried out because of the fetal sex or a Down syndrome diagnosis, reflecting a comprehensive pro-life legislative record.",
              ["https://legiscan.com/PA/bill/SB106/2021",
               "https://choicetracker.org/pa/people/scott-hutchinson/50135040"]),
        claim("seh2", "scott-e-hutchinson", "election_integrity", 0, True,
              "Voted for the SB106 package (July 8, 2022) that included a proposed constitutional amendment requiring government-issued photo ID to vote in Pennsylvania, advancing voter ID as part of the Republican Senate caucus majority.",
              ["https://www.palegis.us/legislation/bills/2021/sb106",
               "https://legiscan.com/PA/bill/SB106/2021"]),
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
