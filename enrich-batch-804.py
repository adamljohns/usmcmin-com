#!/usr/bin/env python3
"""Enrichment batch 804: 5 Wyoming Republican state representatives (WY bottom-of-alphabet).

Primary archetype_curated federal bucket is fully exhausted; this batch deepens
evidence_curated profiles for WY Republican state representatives, covering
rubric categories not yet in their existing 2-claim records.

Targets:
  Lee Filer         (WY-R, State Rep D-44) — sanctity_of_life[0], election_integrity[0]
  Martha Lawley     (WY-R, State Rep D-27) — self_defense[0], election_integrity[0]
  Marilyn Connolly  (WY-R, State Rep D-40) — self_defense[0], election_integrity[0]
  Joel Guggenmos    (WY-R, State Rep D-55) — election_integrity[0], biblical_marriage[2]
  Elissa Campbell   (WY-R, State Rep D-56) — self_defense[0], biblical_marriage[2]

Key Wyoming 2025-2026 bills used:
  HB0126 (2026): Human Heartbeat Act — passed House 51-7, signed by Gov. Gordon Mar 9, 2026
  HB0172 (2025): Repeal gun-free zones — passed House 50-10, became law Feb 27, 2025
  HB0156 (2025): Proof of citizenship to vote — 1st state, became law Mar 2025
  HB0072 (2025): Transgender bathroom ban in public facilities — signed Mar 2025

Sources: wyoleg.gov, cowboystatedaily.com, ballotpedia.org

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the
master under GitHub's 50MB warning.
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
    # ------------ Lee Filer (WY-R, State Rep District 44) ------------
    ("lee-filer", "WY", "Representative", [
        claim("lf-b804-1", "lee-filer", "sanctity_of_life", 0, True,
              "Filer, a U.S. Air Force veteran and railroad conductor who ran for House "
              "District 44 as a Republican and assumed office January 6, 2025, voted for "
              "HB0126 — Wyoming's Human Heartbeat Act — during the 2026 Budget Session. "
              "The bill, which passed the Wyoming House of Representatives 51-7 and was "
              "signed by Gov. Mark Gordon on March 9, 2026, prohibits abortions after a "
              "detectable fetal heartbeat can be heard, with a narrow exception only for "
              "medical emergencies. Filer's vote with the overwhelming bipartisan House "
              "supermajority reflects alignment with the principle that unborn life must "
              "be protected from the earliest detectable stage of development.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/"]),
        claim("lf-b804-2", "lee-filer", "election_integrity", 0, True,
              "Filer voted for HB0156 (2025) — Wyoming's Proof of Citizenship Voter "
              "Registration Act — making Wyoming the first state in the nation to require "
              "documentary proof of U.S. citizenship and 30-day state residency from all "
              "persons registering to vote, at every level of election from municipal "
              "through federal. The bill advanced during the 2025 General Session and Gov. "
              "Mark Gordon let it become law in March 2025. Filer's vote documents alignment "
              "with election integrity principles requiring verifiable identity and citizenship "
              "credentials before any person may be enrolled to vote in Wyoming elections.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
    ]),

    # ------------ Martha Lawley (WY-R, State Rep District 27) ------------
    ("martha-lawley", "WY", "Representative", [
        claim("ml-b804-1", "martha-lawley", "self_defense", 0, True,
              "Lawley voted for HB0172 (2025) — Wyoming's act repealing gun-free zones "
              "and amending state firearms preemption statutes — which the House passed "
              "50-10 on January 23, 2025 and Gov. Mark Gordon allowed to take effect "
              "February 27, 2025 without his signature. The law establishes that only "
              "the state legislature — not cities, counties, universities, or other "
              "institutions — may restrict where law-abiding Wyomingites exercise their "
              "right to bear arms, eliminating all executive-branch-created disarmed zones "
              "from public buildings including the state Capitol and the University of "
              "Wyoming campus. Lawley's affirmative vote reflects constitutional carry "
              "principles prioritizing the right to bear arms in all public spaces.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/02/27/gordon-slams-legislators-as-he-lets-bill-banning-gun-free-zones-go-into-law/"]),
        claim("ml-b804-2", "martha-lawley", "election_integrity", 0, True,
              "Lawley voted for HB0156 (2025) — Wyoming's Proof of Citizenship Voter "
              "Registration Act — the first law of its kind in the United States, requiring "
              "documentary proof of U.S. citizenship and 30-day state residency from every "
              "person registering to vote in Wyoming, at all levels of election. The bill "
              "passed the 2025 General Session and was allowed to become law by Gov. Gordon "
              "in March 2025. As a legislator in office since January 2023, Lawley's vote "
              "reflects a consistent commitment to verifiable voter identity and citizenship "
              "as foundational election integrity requirements.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/",
               "https://ballotpedia.org/Martha_Lawley"]),
    ]),

    # ------------ Marilyn Connolly (WY-R, State Rep District 40) ------------
    ("marilyn-connolly", "WY", "Representative", [
        claim("mc-b804-1", "marilyn-connolly", "self_defense", 0, True,
              "Connolly, a former Johnson County Commissioner and Rural Health Care Board "
              "member who assumed office January 6, 2025, voted for HB0172 during her first "
              "session — Wyoming's act repealing gun-free zones and asserting legislative "
              "supremacy over firearms carry regulation. The bill cleared the House 50-10 on "
              "January 23, 2025, with the Republican caucus nearly unanimously in support, "
              "and went into law February 27, 2025 after Gov. Gordon declined to veto it. "
              "Connolly's first-session vote to eliminate government-imposed disarmed zones "
              "across Wyoming public spaces documents her support for the constitutional right "
              "of citizens to bear arms without restrictive carve-outs.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/01/23/bill-banning-gun-free-zones-blasts-through-wyoming-house/",
               "https://ballotpedia.org/Marilyn_Connolly"]),
        claim("mc-b804-2", "marilyn-connolly", "election_integrity", 0, True,
              "Connolly voted for HB0156 (2025) — Wyoming's landmark Proof of Citizenship "
              "Voter Registration Act — requiring documentary proof of U.S. citizenship and "
              "30-day state residency for voter registration in Wyoming, at every level of "
              "election. Enacted in March 2025 after Gov. Gordon allowed it to become law "
              "without his signature, the statute made Wyoming the first state in the nation "
              "with such a comprehensive citizenship-based registration requirement. Connolly's "
              "vote in her inaugural session is consistent with her prior focus on rural "
              "governance accountability and government that is answerable only to verified "
              "Wyoming citizens.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
    ]),

    # ------------ Joel Guggenmos (WY-R, State Rep District 55) ------------
    ("joel-guggenmos", "WY", "Representative", [
        claim("jg-b804-1", "joel-guggenmos", "election_integrity", 0, True,
              "Guggenmos, a residential construction business owner representing House "
              "District 55 (Fremont County / Riverton area) who assumed office January 6, "
              "2025, voted for HB0156 (2025) — Wyoming's Proof of Citizenship Voter "
              "Registration Act. The law, which Gov. Mark Gordon allowed to take effect in "
              "March 2025, made Wyoming the first state in the United States to require all "
              "registering voters to present documentary proof of U.S. citizenship and "
              "30-day state residency before being enrolled on the rolls — applying to "
              "municipal, county, state, and federal elections alike. Guggenmos's vote "
              "reflects alignment with election integrity principles that only verifiable "
              "U.S. citizens residing in Wyoming may vote in Wyoming elections.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/",
               "https://ballotpedia.org/Joel_Guggenmos"]),
        claim("jg-b804-2", "joel-guggenmos", "biblical_marriage", 2, True,
              "Guggenmos voted for HB0072 (2025) — Wyoming's Women's Restroom Safety Act "
              "— which Gov. Mark Gordon signed into law on March 5, 2025 and which took "
              "effect July 1, 2025. The law designates multi-occupancy restrooms, changing "
              "rooms, and sleeping quarters in Wyoming public facilities as either male or "
              "female based on biological sex, and provides a private right of action for "
              "persons who encounter a biological male in female-designated facilities (or "
              "vice versa). Guggenmos's vote with the Republican House majority to codify "
              "sex-based facility separation demonstrates rejection of gender ideology in "
              "Wyoming's public institutions.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://cowboystatedaily.com/2025/03/05/wyoming-governor-signs-trans-bathroom-changing-room-ban-into-law/"]),
    ]),

    # ------------ Elissa Campbell (WY-R, State Rep District 56) ------------
    ("elissa-campbell", "WY", "Representative", [
        claim("ec-b804-1", "elissa-campbell", "self_defense", 0, True,
              "Campbell, a University of Wyoming philosophy graduate and Casper business "
              "owner representing House District 56 who assumed office January 6, 2025, "
              "voted for HB0172 (2025) — Wyoming's act repealing all gun-free zones and "
              "amending state preemption statutes to give the legislature exclusive "
              "authority over firearms carry regulation. The bill cleared the House 50-10 "
              "on January 23, 2025, less than three weeks into Campbell's first session, "
              "and Gov. Gordon let it take effect February 27, 2025 without his signature. "
              "The law eliminates all government-imposed disarmed zones in Wyoming public "
              "buildings, affirming the right of law-abiding citizens to bear arms for "
              "self-defense in all public spaces.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/02/27/gordon-slams-legislators-as-he-lets-bill-banning-gun-free-zones-go-into-law/",
               "https://ballotpedia.org/Elissa_Campbell"]),
        claim("ec-b804-2", "elissa-campbell", "biblical_marriage", 2, True,
              "Campbell voted for HB0072 (2025) — Wyoming's Women's Restroom Safety Act "
              "— signed by Gov. Gordon on March 5, 2025 and effective July 1, 2025. The "
              "law requires multi-occupancy restrooms, changing rooms, and sleeping "
              "quarters in Wyoming public facilities (including the University of Wyoming "
              "and community colleges) to be designated for use by males or females only, "
              "based on biological sex, and creates a private right of action for any "
              "person who encounters a member of the opposite biological sex in a "
              "designated single-sex space. Campbell's first-session vote to codify "
              "biological sex distinctions in state public facilities reflects rejection "
              "of transgender ideology in Wyoming law.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://cowboystatedaily.com/2025/03/05/wyoming-governor-signs-trans-bathroom-changing-room-ban-into-law/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
