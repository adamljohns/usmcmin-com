#!/usr/bin/env python3
"""Enrichment batch 134: 4 federal Senate candidates (low_evidence, bottom of alphabet).

Targets: Nick Hankins (OK-R), William Sean Buckner (OK-R),
Gary Ty England (OK-R), Brian Ragain (OK-R).
All are 2026 U.S. Senate Republican primary candidates (Mullin seat, OK) with 0 prior claims.
Primary scheduled June 16, 2026.

Sources: candidate campaign sites (oksaysno.com, auditthesenate.com,
garytyenglandforsenate.com, ragainforsenate.com), ivoterguide.com,
ballotpedia.org, nondoc.com, kosu.org, natlawreview.com.

MINIFIED write: separators=(',',':') — keeps scorecard.json ~35-36MB under GitHub 50MB limit.
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
    # ---------------- Nick Hankins (OK-R, 2026 Senate candidate, Mullin seat) ----------------
    ("nick-hankins", "OK", "Senator", [
        claim("nh1", "nick-hankins", "sanctity_of_life", 0, True,
              "States that 'Human life deserves legal protection from conception until natural death' and supports enforcing the Comstock Act to ban interstate transportation of abortion-inducing drugs — affirming a life-at-conception personhood posture.",
              ["https://www.oksaysno.com/positions",
               "https://ivoterguide.com/candidate/80985/race/27978/election/1425"]),
        claim("nh2", "nick-hankins", "self_defense", 1, True,
              "Pledges to 'vote NO on any bill that attempts to restrict the second amendment rights of law abiding citizens' and explicitly supports abolishing the ATF — the strongest anti-regulatory Second Amendment posture.",
              ["https://www.oksaysno.com/positions",
               "https://ballotpedia.org/Nick_Hankins"]),
        claim("nh3", "nick-hankins", "border_immigration", 1, True,
              "Runs on deporting all illegal aliens, ending asylum abuse, and sealing the border, citing Senator Mullin's vote for '$5 Billion dollars for illegal aliens' as the kind of betrayal he will not repeat.",
              ["https://www.oksaysno.com/",
               "https://nondoc.com/2026/05/26/cheat-sheet-5-gop-candidates-seek-oklahoma-u-s-senate-seat/"]),
    ]),

    # ---------------- William Sean Buckner (OK-R, 2026 Senate candidate, Mullin seat) ----------------
    ("william-sean-buckner", "OK", "Senator", [
        claim("wsb1", "william-sean-buckner", "self_defense", 1, True,
              "Opposes federal red flag laws, universal background checks, and magazine restrictions; pledges to 'defend the Second Amendment' and recruit arms and ammunition manufacturers to Oklahoma.",
              ["https://auditthesenate.com/issues/",
               "https://ballotpedia.org/United_States_Senate_election_in_Oklahoma,_2026_(June_16_Republican_primary)"]),
        claim("wsb2", "william-sean-buckner", "border_immigration", 0, True,
              "Supports fully funding and completing the southern border wall, designating Mexican drug cartels as Foreign Terrorist Organizations, and treating cartel fentanyl networks as a direct act of war against Americans.",
              ["https://auditthesenate.com/issues/",
               "https://nondoc.com/2026/05/26/cheat-sheet-5-gop-candidates-seek-oklahoma-u-s-senate-seat/"]),
        claim("wsb3", "william-sean-buckner", "sanctity_of_life", 4, True,
              "Opposes any federal taxpayer funding for abortion providers; his platform explicitly rejects channeling public funds to Planned Parenthood or any abortion-industry entity.",
              ["https://auditthesenate.com/issues/",
               "https://tulsabeacon.com/u-s-senate-hopefuls-in-june-primary/"]),
    ]),

    # ---------------- Gary Ty England (OK-R, 2026 Senate candidate, Mullin seat) ----------------
    ("gary-ty-england", "OK", "Senator", [
        claim("gte1", "gary-ty-england", "sanctity_of_life", 0, True,
              "Describes himself as a 'Reagan conservative' committed to protecting the unborn, pledging to advance pro-life legislation as a core priority in the U.S. Senate.",
              ["https://www.garytyenglandforsenate.com/platform",
               "https://www.kosu.org/ty-england-senate-campaign"]),
        claim("gte2", "gary-ty-england", "self_defense", 0, True,
              "Pledges to defend the Second Amendment as a constitutional conservative, opposing federal infringement on the right to keep and bear arms.",
              ["https://www.garytyenglandforsenate.com/platform",
               "https://www.kosu.org/ty-england-senate-campaign"]),
        claim("gte3", "gary-ty-england", "border_immigration", 0, True,
              "Runs on 'strong borders' as a central campaign pillar, calling for secure southern border enforcement to protect Oklahoma families and American sovereignty.",
              ["https://www.garytyenglandforsenate.com/platform",
               "https://www.citynewsokc.com/government/gary-ty-england-says-oklahoma-needs-an-ambassador-not-another-politician-in-u-s-senate/article_4209b699-f822-4e9c-9de3-2e68348b869e.html"]),
    ]),

    # ---------------- Brian Ragain (OK-R, 2026 Senate candidate, Mullin seat) ----------------
    ("brian-ragain", "OK", "Senator", [
        claim("br1", "brian-ragain", "sanctity_of_life", 0, True,
              "Affirms that 'human life deserves legal protection from conception until natural death' — a life-at-conception personhood position held as a core conviction.",
              ["https://ragainforsenate.com/",
               "https://ivoterguide.com/candidate/92459/race/27978/election/1425"]),
        claim("br2", "brian-ragain", "foreign_policy_restraint", 1, True,
              "Calls for removing 'American service members from the pointless foreign conflicts that fuel the trauma,' opposing open-ended overseas military entanglements and prioritizing troop welfare over foreign nation-building.",
              ["https://ragainforsenate.com/",
               "https://natlawreview.com/press-releases/retired-firefighter-nurse-and-paramedic-enters-oklahoma-us-senate-race"]),
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
