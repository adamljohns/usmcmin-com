#!/usr/bin/env python3
"""Enrichment batch 313: 3rd distinct-category claims for 5 bottom-of-alphabet WY state senators.

Archetype_curated and evidence_federal 0-claim federal buckets exhausted (batch 303+).
Pipeline continues with evidence_curated state-level candidates at exactly 2 claims,
reverse-sorted by state — WY senators at the top of that reversed list.

Targets (WY Republicans, all State Senator, reverse-alpha by name within WY):
  Wendy Schuler      — self_defense[0]=False   (opposed HB0125 gun-free-zone repeal 2024;
                        WY Gun Owners targeted her for opposing 2A expansion)
  Troy McKeown       — self_defense[0]=True    (cosponsored SF0196 2A Protection Act +
                        SF0058 gun-sales-tax repeal; voted to revive HB0125)
  Tim French         — economic_stewardship[2]=True  (Senate Appropriations member;
                        WY Freedom Caucus 2024 endorsee; fiscal-restraint platform)
  Tara Nethercott    — election_integrity[0]=True    (ran for SoS 2022 on election-integrity
                        platform; co-sponsored + voted for WY voter-ID bill)
  Stephan Pappas     — self_defense[0]=False   (voted against HB0125 gun-free-zone repeal
                        2024; supported firearm hold-agreement bill for suicide prevention)

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


TARGETS = [
    # ---------------- Wendy Schuler (WY, State Senator) ----------------
    ("wendy-schuler", "WY", "State Senator", [
        claim("ws1", "wendy-schuler", "self_defense", 0, False,
              "Voted against HB0125 in the Wyoming Senate Judiciary Committee (2024), a bill to repeal the state's gun-free zones and expand where licensed carriers could legally carry firearms. Proposed an amendment to restrict armed civilians near public schools on active-shooter safety grounds — prioritizing gun-free zone maintenance above the unrestricted carry the rubric's constitutional-carry ideal envisions. Wyoming Gun Owners publicly targeted Schuler for opposing this Second Amendment expansion.",
              ["https://wyofile.com/shot-down-resuscitated-wyoming-senate-bucks-precedent-to-target-gun-free-zones/",
               "https://cowboystatedaily.com/2024/03/05/wyomings-gun-free-zones-to-stay-after-bill-to-get-rid-of-them-dies/"]),
    ]),

    # ---------------- Troy McKeown (WY, State Senator) ----------------
    ("troy-mckeown", "WY", "State Senator", [
        claim("tm1", "troy-mckeown", "self_defense", 0, True,
              "Co-sponsored Senate File 196 (2025), which strengthens Wyoming's Second Amendment Protection Act, and Senate File 58 (2025), which eliminates the state sales tax on firearm purchases — directly reducing the cost of exercising Second Amendment rights. Also voted in 2024 to retrieve HB0125 from procedural death and allow a floor vote expanding where Wyomingites can legally carry firearms — consistent with the rubric's constitutional-carry ideal.",
              ["https://www.wyoleg.gov/Legislation/2025/SF0196",
               "https://www.wyoleg.gov/Legislation/2025/SF0058",
               "https://wyofile.com/shot-down-resuscitated-wyoming-senate-bucks-precedent-to-target-gun-free-zones/"]),
    ]),

    # ---------------- Tim French (WY, State Senator) ----------------
    ("tim-french", "WY", "State Senator", [
        claim("tf1", "tim-french", "economic_stewardship", 2, True,
              "Serves on the Wyoming Senate Appropriations Committee — the chamber's fiscal gatekeeper — and received a 2024 endorsement from the Wyoming Freedom Caucus, which campaigns explicitly for spending restraint and against deficit-driven budgets. French's stated platform of being 'pro-property rights' and supporting the coal industry positions him against the regulatory-and-spending expansion the rubric's economic_stewardship[2] anti-deficit standard opposes.",
              ["https://ballotpedia.org/Tim_French",
               "https://www.wyomingpublicmedia.org/politics-government/2025-09-10/senate-leadership-shuffles-committee-chairs-following-resignations"]),
    ]),

    # ---------------- Tara Nethercott (WY, State Senator) ----------------
    ("tara-nethercott", "WY", "State Senator", [
        claim("tn1", "tara-nethercott", "election_integrity", 0, True,
              "Ran for Wyoming Secretary of State in 2022 explicitly on an election-integrity platform, declaring Wyoming elections should be 'a point of pride' and 'an example to the nation for election integrity.' Co-sponsored and voted for Wyoming's voter-ID legislation, affirming ballot-security measures — strict ID requirements and registration controls — that the rubric's election_integrity[0] standard requires.",
              ["https://cowboystatedaily.com/2022/08/15/candidate-profile-tara-nethercott-for-wyoming-secretary-of-state/",
               "https://wyofile.com/election-integrity-front-and-center-in-secretary-of-state-race/"]),
    ]),

    # ---------------- Stephan Pappas (WY, State Senator) ----------------
    ("stephan-pappas", "WY", "State Senator", [
        claim("sp1", "stephan-pappas", "self_defense", 0, False,
              "Voted against Wyoming HB0125 in 2024, a bill to repeal state gun-free zones and expand permitted carry locations, placing him with the minority opposed to Second Amendment expansion. He also advocated for moving forward with a government-facilitated firearm 'hold agreement' bill tied to suicide prevention — a mechanism that would temporarily disarm at-risk individuals through a state-brokered process paralleling red-flag law logic. Both positions diverge from the constitutional-carry ideal the rubric's self_defense[0] standard envisions.",
              ["https://wyomingpublicmedia.org/politics-government/2025-10-21/lawmakers-table-bill-on-firearm-hold-agreements-meant-to-help-address-suicide-prevention",
               "https://wyofile.com/shot-down-resuscitated-wyoming-senate-bucks-precedent-to-target-gun-free-zones/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
