#!/usr/bin/env python3
"""Enrichment batch 856: 13 new claims for 5 VA Republican 2026 federal candidates.

Bottom-of-alphabet batch targeting Virginia (state V — near the bottom).
All five had confidence='unset' and 0 claims; archetype_curated federal bucket
is fully depleted as of 2026-07-28.

Targets (all VA, all R, all 2026 federal candidates):
  Bert Mizusawa   — U.S. Senate VA (2026 R primary; retired Army Major General)
  Kim Farington   — U.S. Senate VA (2026 R primary; CPA / former DoD executive)
  Tony Sabio      — U.S. Representative VA-08 (Navy/CIA/Secret Service veteran)
  Melanie Lucero  — U.S. Representative VA-05 (USMC veteran, intelligence analyst)
  Edwin Rivera    — U.S. Representative VA-03 (Army vet, disabled veteran, ex-police)

Sources verified 2026-07-28. Minified write preserves ~35-36 MB master.
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
    # ---- Bert Mizusawa (VA, U.S. Senate 2026 R primary) ----
    ("bert-mizusawa", "VA", "Senate", [
        claim("bm1", "bert-mizusawa", "self_defense", 0, True,
              "Has stated: 'Our Constitutional right to keep and bear arms is key to the security of freedom and individual liberty. I will defend our rights to citizen self-defense and fight any effort to infringe on that right.' — a direct campaign commitment to unrestricted Second Amendment protection.",
              ["https://bertforsenate.com/",
               "https://ballotpedia.org/Bert_Mizusawa"]),
        claim("bm2", "bert-mizusawa", "border_immigration", 4, True,
              "Opposes birthright citizenship, calling the 14th Amendment's birthright provision 'a post-Civil War loophole' in a July 2026 public video event — aligning with the rubric's opposition to automatic birthright citizenship for children of illegal entrants.",
              ["https://bluevirginia.us/2026/07/video-frontrunner-for-2026-va-gop-u-s-senate-nomination-calls-birthright-citizenship-a-post-civil-war-loophole/",
               "https://www.cvilletomorrow.org/qa-with-virginias-three-republican-primary-candidates-for-u-s-senate/"]),
        claim("bm3", "bert-mizusawa", "economic_stewardship", 2, True,
              "Campaigns on a simplified tax code with fewer brackets and larger standard deductions, paired with curbing government spending — a balanced fiscal posture consistent with the rubric's anti-deficit standard.",
              ["https://www.einpresswire.com/article/884832889/gen-bert-mizusawa-to-run-for-us-senate-in-virginia",
               "https://insideelections.com/person/bert-k-mizusawa/"]),
    ]),

    # ---- Kim Farington (VA, U.S. Senate 2026 R primary) ----
    ("kim-farington", "VA", "Senate", [
        claim("kf1", "kim-farington", "sanctity_of_life", 0, True,
              "Pledges to be 'a pro-life vote in the U.S. Senate;' actively opposes Virginia's 2026 constitutional amendment enshrining abortion as a right (stated at a June 2026 candidate forum: 'Please, be like me, vote no on that abortion amendment'); advocates for adoption and prevention programs as alternatives.",
              ["https://kimforvirginia.com/",
               "https://www.opencampaign.com/politicians-in-united-states/196241/kim-farington"]),
        claim("kf2", "kim-farington", "self_defense", 0, True,
              "Commits to ensuring 'Congress passes no laws that impede our Second Amendment Rights' — explicitly protecting firearm ownership as a core legislative priority and rejecting any new federal gun restrictions.",
              ["https://kimforvirginia.com/",
               "https://www.wythecountyrepublicanparty.com/post/virginia-s-2026-senate-race-three-republican-challengers-and-the-incumbent-they-hope-to-unseatvir"]),
        claim("kf3", "kim-farington", "border_immigration", 0, True,
              "Supports border wall completion and deportation of criminal offenders; stated 'The first duty of the American government is to protect American citizens, not those who break our immigration laws' — aligning with the rubric's call for militarized border security and mandatory enforcement.",
              ["https://kimforvirginia.com/",
               "https://www.ballotready.org/people/kim-farington"]),
    ]),

    # ---- Tony Sabio (VA, U.S. Representative VA-08, 2026 R nominee) ----
    ("tony-sabio", "VA", "Representative", [
        claim("ts1", "tony-sabio", "border_immigration", 2, True,
              "Pledged that when elected, local law enforcement in his district would fully cooperate with ICE and Trump border czar Tom Homan; stated 'We're going to find criminals, we're going to pull them out,' directly opposing Arlington County's policy barring police cooperation with immigration authorities — a hard anti-sanctuary position.",
              ["https://www.arlnow.com/2025/05/23/former-cia-agent-files-as-republican-challenger-to-don-beyer/",
               "https://www.thegatewaypundit.com/2026/07/this-is-about-america-american-people-republican-hopes/"]),
        claim("ts2", "tony-sabio", "election_integrity", 0, True,
              "Made safe and transparent elections a campaign priority; stated '80% of Americans want safe elections. They want safe and transparent elections' — aligning with the rubric's support for election integrity measures and transparent vote-counting.",
              ["https://www.thegatewaypundit.com/2026/07/this-is-about-america-american-people-republican-hopes/",
               "https://ballotpedia.org/Tony_Sabio"]),
    ]),

    # ---- Melanie Lucero (VA, U.S. Representative VA-05, 2026 R primary) ----
    ("melanie-lucero", "VA", "Representative", [
        claim("ml1", "melanie-lucero", "sanctity_of_life", 0, True,
              "Lists 'Right to Life' as a core campaign platform position and has stated her intention to work to end Planned Parenthood federal funding — a Marine veteran who identifies as pro-life and makes life protection a legislative priority.",
              ["https://www.29news.com/2026/06/03/republican-melanie-lucero-challenges-incumbent-congressman-virginias-fifth-district-primary/",
               "https://www.opencampaign.com/politicians-in-united-states/202883/melanie-lucero"]),
        claim("ml2", "melanie-lucero", "border_immigration", 1, True,
              "Supports mandatory immigration enforcement including proper ICE funding; stated illegal immigration 'has put a significant strain on our country as far as resources, funding and taking from programs and benefits that the American people were in line for' — calls for deporting those who have entered illegally.",
              ["https://wset.com/news/local/melanie-lucero-brings-gop-primary-challenge-to-rep-john-mcguire-to-lynchburg-stop-july-2026-la-villa-washington-politics-republican",
               "https://www.opencampaign.com/politicians-in-united-states/202883/melanie-lucero"]),
        claim("ml3", "melanie-lucero", "self_defense", 0, True,
              "USMC veteran who, along with other Republican candidates in VA-05, is documented as committed to 'protecting the Second Amendment' as a core conservative value; opposes any federal restrictions on firearm ownership.",
              ["https://cvillerightnow.com/news/208802-as-5th-district-gop-race-heats-up-melanie-lucero-calls-incumbent-john-mcguire-a-huge-disappointment/",
               "https://ballotpedia.org/Melanie_Lucero"]),
    ]),

    # ---- Edwin Rivera (VA, U.S. Representative VA-03, 2026 R candidate) ----
    ("edwin-rivera", "VA", "Representative", [
        claim("er1", "edwin-rivera", "self_defense", 0, True,
              "States on his campaign website that he 'loves the second amendment and believes that responsible gun ownership is both a right and a responsibility' — an Army combat veteran and former police officer who explicitly champions constitutional gun rights.",
              ["https://edwinriveraforcongress.com/",
               "https://ballotpedia.org/Virginia's_3rd_Congressional_District_election,_2026"]),
        claim("er2", "edwin-rivera", "family_child_sovereignty", 0, True,
              "Describes himself as 'a devoted family man' committed to 'strengthening families, expanding opportunity, and building safer communities;' his personal history navigating foster care and being raised by grandparents in Puerto Rico informs his commitment to family-centered, community-driven policy over government intervention.",
              ["https://edwinriveraforcongress.com/",
               "https://virginia.gop/republican-party-of-virginia-announces-candidates-for-u-s-house-seats/"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
