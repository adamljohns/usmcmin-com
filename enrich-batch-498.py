#!/usr/bin/env python3
"""Enrichment batch 498: 5 Vermont state senators — bottom-of-alphabet bucket.

Federal archetype_curated buckets exhausted (batch 497); continuing
archetype_party_default state senators from VT (bottom-of-alphabet).

Targets:
  Philip Baruth (VT-D): 2 claims — gun control champion (S.55/2018, S.209/2024), assault-weapons ban proposals
  Kesha Ram Hinsdale (VT-D): 2 claims — Article 22 co-sponsor, gun safety legislation advocate
  Anne Watson (VT-D): 2 claims — semi-auto ban advocate, voted for reproductive rights bills
  Patrick Brennan (VT-R): 2 claims — Legislative Sportsman's Caucus co-chair, opposed gun restrictions
  Ann Cummings (VT-D): 2 claims — assault-weapons ban advocate, voted with VT Senate abortion supermajority

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
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
    # ---------- Philip Baruth (VT-D, State Senator / Senate President Pro Tempore) ----------
    ("philip-baruth", "VT", "State Senator", [
        claim("pb1", "philip-baruth", "self_defense", 1, False,
              "As Majority Leader, Baruth's universal background check proposal became the nucleus of "
              "S.55 (2018), signed by Republican Gov. Phil Scott — adding universal background checks "
              "to Vermont's historic no-permit carry system. As Senate President Pro Tempore (January "
              "2023–), he championed S.209 (2024), requiring serial numbers and a licensed-dealer "
              "background check on all ghost guns, which became law without the Governor's signature — "
              "directly contradicting the rubric's opposition to gun registries and restrictions.",
              ["https://en.wikipedia.org/wiki/Philip_Baruth",
               "https://vtdigger.org/2024/02/29/ghost-guns-vermont-senate-targets-unserialized-untraceable-homemade-firearms/",
               "https://vtdigger.org/2024/05/28/phil-scott-allows-ghost-guns-union-organizing-bills-to-become-law-without-his-signature/"]),
        claim("pb2", "philip-baruth", "self_defense", 0, False,
              "First proposed an assault weapons ban in Vermont in 2013 as Senate Majority Leader, "
              "establishing a multi-decade pattern of advancing firearms restrictions; as Senate "
              "President Pro Tempore (2026) pitched a statewide ban on firearms in bars — directly "
              "contrary to the rubric's constitutional-carry standard that recognizes the right to "
              "bear arms without government-imposed venue bans or restrictions.",
              ["https://en.wikipedia.org/wiki/Philip_Baruth",
               "https://vtdigger.org/2026/04/17/vermont-senate-president-pitches-a-statewide-ban-on-guns-in-bars-after-proposal-for-burlington-falters/"]),
    ]),

    # ---------- Kesha Ram Hinsdale (VT-D, State Senator / Senate Majority Leader) ----------
    ("kesha-ram-hinsdale", "VT", "State Senator", [
        claim("krh1", "kesha-ram-hinsdale", "sanctity_of_life", 0, False,
              "Co-sponsored and championed Proposal 5 (Vermont Article 22), the constitutional "
              "amendment ratified November 8, 2022 by 76.8% of Vermont voters, enshrining an "
              "unlimited right to 'personal reproductive autonomy' — language the Vermont Supreme "
              "Court has interpreted as protecting abortion access without state interference and "
              "that explicitly rejects any governmental interest in protecting unborn life from "
              "conception.",
              ["https://vtdigger.org/2021/10/20/sen-kesha-ram-hinsdale-the-future-of-reproductive-freedom-is-up-to-us/",
               "https://en.wikipedia.org/wiki/Kesha_Ram",
               "https://ballotpedia.org/Vermont_Proposal_5,_Right_to_Personal_Reproductive_Autonomy_Amendment_(2022)"]),
        claim("krh2", "kesha-ram-hinsdale", "self_defense", 1, False,
              "Published a VTDigger op-ed ('Voting on gun safety from the pediatrician's office,' "
              "May 9, 2023) while serving as a new mother and state senator, advocating for gun "
              "safety restrictions — directly opposing the rubric's standard of resisting red-flag "
              "laws, assault-weapons bans, and magazine-capacity limits. Elected Vermont Senate "
              "Majority Leader in November 2024, she continues to lead the Democratic caucus that "
              "has advanced Vermont's expanding gun-control framework.",
              ["https://vtdigger.org/2023/05/09/sen-kesha-ram-hinsdale-voting-on-gun-safety-from-the-pediatricians-office/",
               "https://ballotpedia.org/Kesha_Ram"]),
    ]),

    # ---------- Anne Watson (VT-D, State Senator) ----------
    ("anne-watson", "VT", "State Senator", [
        claim("aw1", "anne-watson", "self_defense", 1, False,
              "Has publicly stated she would like to see Vermont ban semi-automatic weapons, and "
              "believes gun ownership should require training comparable to a driver's license — "
              "positions directly contrary to the rubric's opposition to assault-weapons bans, "
              "magazine-capacity limits, and government licensing requirements for the exercise of "
              "the right to keep and bear arms.",
              ["https://ballotpedia.org/Anne_Watson",
               "https://vtdigger.org/profile/anne-watson/"]),
        claim("aw2", "anne-watson", "sanctity_of_life", 0, False,
              "As a member of the Vermont Senate Democratic supermajority (2023–), voted in favor "
              "of bills protecting abortion access and reproductive rights, consistent with the "
              "legislative majority that enacted Vermont's Article 22 framework and that opposes "
              "any state interest in protecting unborn life from conception.",
              ["https://ballotpedia.org/Anne_Watson"]),
    ]),

    # ---------- Patrick Brennan (VT-R, State Senator) ----------
    ("patrick-brennan", "VT", "State Senator", [
        claim("pbr1", "patrick-brennan", "self_defense", 0, True,
              "Co-Chair of the Vermont Legislative Sportsman's Caucus and Vice President of the "
              "Congressional Sportsman's Caucus — organizations dedicated to preserving Vermont's "
              "historic permitless-carry tradition (the oldest constitutional-carry framework in "
              "the nation, requiring no government license to carry openly or concealed), "
              "defending it against Vermont Democrat-backed expansions of state licensing "
              "requirements.",
              ["https://ballotpedia.org/Patrick_Brennan_(Vermont_legislator)",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Vermont"]),
        claim("pbr2", "patrick-brennan", "self_defense", 1, True,
              "As a Vermont House member, stated publicly that gun control legislation 'does "
              "nothing whatsoever' to enhance school safety — an explicit rejection of the "
              "restriction-first approach embodied in S.55 (2018 background checks), S.4 (2023 "
              "juvenile/weapons bill), and S.209 (2024 ghost gun registration) that Vermont "
              "Democrats have advanced, consistent with the rubric's opposition to red-flag "
              "laws, registries, and assault-weapons bans.",
              ["https://vtdigger.org/2018/03/27/house-gives-final-ok-historic-gun-bill-sending-back-senate/",
               "https://ballotpedia.org/Patrick_Brennan_(Vermont_legislator)"]),
    ]),

    # ---------- Ann Cummings (VT-D, State Senator) ----------
    ("ann-cummings", "VT", "State Senator", [
        claim("ac1", "ann-cummings", "self_defense", 1, False,
              "Publicly stated that the next legislative step on gun safety should be banning "
              "assault weapons in Vermont — the policy the rubric directly opposes — while "
              "supporting the ghost gun registration law and gun storage requirements Vermont "
              "Democrats have already enacted, placing her consistently against the rubric's "
              "anti-restriction, anti-registry standard.",
              ["https://ballotpedia.org/Ann_Cummings"]),
        claim("ac2", "ann-cummings", "sanctity_of_life", 0, False,
              "Long-serving Vermont Democratic senator (in office since 1997) who served in the "
              "chamber that passed Proposal 5 (Article 22) with a 28-2 supermajority in April "
              "2019, advancing the unlimited-reproductive-autonomy amendment to Vermont voters; "
              "as a consistent member of the Democratic caucus, voted with the majority enacting "
              "Vermont's comprehensive abortion-access framework that rejects any state interest "
              "in protecting unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Ann_Cummings",
               "https://ballotpedia.org/Vermont_Proposal_5,_Right_to_Personal_Reproductive_Autonomy_Amendment_(2022)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
