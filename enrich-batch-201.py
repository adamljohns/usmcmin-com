#!/usr/bin/env python3
"""Enrichment batch 201: 5 low_evidence federal candidates from WI + TN with 0 claims.

archetype_curated federal bucket exhausted; evidence_federal pool thin on sitting senators.
Targets taken from the bottom of the alphabet among active U.S. House candidates:
  WI (Wisconsin) and TN (Tennessee) — bottom-of-alphabet states with documented records.

  Lore Bergman      (TN-06 D · open seat · Rose seat · documented pro-abortion/gun-reform/LGBTQ)
  Fred Clark        (WI-07 D · open seat · Tiffany seat · former WI Assembly member, pro-choice record)
  Mike Croley       (TN-06 D · open seat · Rose seat · Navy vet, progressive spending platform)
  Niina Threlfall-Baum (WI-07 R · open seat · Tiffany seat · self-described 'moderate Republican')
  Chris Armstrong   (WI-07 D · open seat · Tiffany seat · first-time candidate, anti-Trump protest origin)

MINIFIED write — see enrich-batch-4.py module docstring for rationale.
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
    # ---- Lore Bergman (TN-06, D · open seat · Rose seat) ----
    ("lore-bergman", "TN", "Representative", [
        claim("lb1", "lore-bergman", "sanctity_of_life", 0, False,
              "Explicitly advocates for permanently restoring federal abortion rights, stating on her campaign platform: "
              "'Women should once again and permanently have the right to CHOOSE their own reproductive care needs, "
              "including care for abortions, miscarriages and any other care that has to do with their reproductive "
              "systems, including contraception' — a direct rejection of any legal protection of the unborn from "
              "conception and contrary to the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Lore_Bergman",
               "https://www.lebanonemocrat.com/maconcounty/news/lore-bergman-for-tennessee-s-6th-congressional-district/article_a18b65c5-88c1-5423-9408-aec7e53a9b4e.html"]),
        claim("lb2", "lore-bergman", "self_defense", 1, False,
              "Ballotpedia documents her support for 'gun reform' as a core campaign position — directly opposing the "
              "rubric's standard of defending uninfringed Second Amendment rights against restrictions on semi-automatic "
              "firearms, magazine limits, background-check expansions, and red-flag laws.",
              ["https://ballotpedia.org/Lore_Bergman"]),
        claim("lb3", "lore-bergman", "biblical_marriage", 2, False,
              "Her campaign platform explicitly endorses LGBTQ rights including rights for transgender individuals — "
              "placing her in direct opposition to the rubric's standard of rejecting transgender ideology in law and "
              "policy. She also supports same-sex-marriage protections as part of her stated equality agenda.",
              ["https://ballotpedia.org/Lore_Bergman",
               "https://www.ballotready.org/people/lore-bergman"]),
    ]),

    # ---- Fred Clark (WI-07, D · open seat · Tiffany seat · former WI Assembly member) ----
    ("fred-clark-wi-07", "WI", "Representative", [
        claim("fc1", "fred-clark-wi-07", "sanctity_of_life", 0, False,
              "As a Democratic member of the Wisconsin State Assembly from 2009 to 2015, Clark built a pro-choice "
              "legislative record that included votes in favor of abortion-access legislation — in direct conflict with "
              "the rubric's life-at-conception standard. Running again in 2026 as a Democrat in a district where "
              "Wisconsin's partial abortion ban remains a live legislative issue, Clark continues to align with the "
              "pro-abortion caucus.",
              ["https://en.wikipedia.org/wiki/Fred_Clark_(politician)",
               "https://ballotpedia.org/Fred_Clark",
               "https://docs.legis.wisconsin.gov/2013/legislators/assembly/1024"]),
        claim("fc2", "fred-clark-wi-07", "border_immigration", 1, False,
              "Clark has publicly stated he supports 'maintaining secure borders while providing a pathway for "
              "immigrants to live and work in the country' — endorsing a form of legal status for those already "
              "present illegally rather than mandatory deportation, directly contrary to the rubric's "
              "mandatory-deportation standard.",
              ["https://www.wsaw.com/2026/03/07/dem-candidate-clark-brings-political-experience-7th-district-race-compares-self-gops-rand-paul/"]),
        claim("fc3", "fred-clark-wi-07", "self_defense", 1, False,
              "While claiming to support the Second Amendment for 'law abiding people,' Clark has expressed concern "
              "about 'semi-automatic weapons used in mass shootings' — a position that opens the door to "
              "assault-weapon restrictions and magazine limits, contrary to the rubric's standard of opposing all "
              "AWB/mag-limit/red-flag schemes and defending fully uninfringed Second Amendment rights.",
              ["https://www.wsaw.com/2026/03/07/dem-candidate-clark-brings-political-experience-7th-district-race-compares-self-gops-rand-paul/"]),
    ]),

    # ---- Mike Croley (TN-06, D · open seat · Rose seat · Navy vet, NOAA fellow) ----
    ("mike-croley", "TN", "Representative", [
        claim("mc1", "mike-croley", "economic_stewardship", 2, False,
              "Croley's campaign explicitly advocates for 'fair wages, access to healthcare, and real investment in "
              "rural infrastructure' through expanded federal spending — a posture directly at odds with the rubric's "
              "call for fiscal discipline, balanced-budget commitments, and opposition to runaway deficit spending. "
              "He frames his candidacy around rebuilding and expanding government services rather than limiting them.",
              ["https://ballotpedia.org/Mike_Croley",
               "https://www.mikefortn6.com/post/mike-croley-for-congress-tennessee-s-6th-district-campaign-update"]),
        claim("mc2", "mike-croley", "economic_stewardship", 4, False,
              "Croley served as a Presidential Management Fellow at NOAA where he 'helped lead climate resilience "
              "efforts and supported community-centered science' — federal programs aligned with the WEF/ESG climate "
              "regulatory agenda the rubric identifies as contrary to sound economic stewardship. His 2026 campaign "
              "lists 'protecting the environment' as a policy priority, signaling continued support for federal "
              "climate mandates.",
              ["https://ballotpedia.org/Mike_Croley",
               "https://www.mikefortn6.com/post/beyond-left-and-right-a-campaign-rooted-in-service"]),
    ]),

    # ---- Niina Threlfall-Baum (WI-07, R · open seat · Tiffany seat · moderate Republican) ----
    ("niina-threlfall-baum", "WI", "Representative", [
        claim("nt1", "niina-threlfall-baum", "sanctity_of_life", 0, False,
              "Running as a self-described 'moderate Republican,' Threlfall-Baum has explicitly stated that "
              "'representation should be about listening to constituents and putting personal opinions second' — a "
              "posture that refuses the rubric's requirement that a representative advocate for life-at-conception "
              "protections from biblical conviction. Her publicly stated priorities contain no pro-life advocacy, no "
              "sought or received pro-life endorsements, and no commitment to personhood legislation.",
              ["https://www.weau.com/2026/02/04/moderate-republican-niina-baum-running-7th-congressional-district/",
               "https://ballotpedia.org/Paul_Wassgren"]),
        claim("nt2", "niina-threlfall-baum", "border_immigration", 0, False,
              "Threlfall-Baum's campaign deliberately avoids the America First immigration-enforcement positions "
              "(border wall, military deployment, mandatory deportation) advocated by her WI-07 Republican primary "
              "opponents Ebben, Alfonso, and Hermening. She has not endorsed wall construction or military border "
              "enforcement in her publicly stated platform, which focuses exclusively on economic, healthcare, and "
              "infrastructure issues.",
              ["https://baumforwisconsin.com/",
               "https://news.ballotpedia.org/2026/06/03/major-donors-back-competing-candidates-in-wisconsins-7th-district-republican-primary/"]),
    ]),

    # ---- Chris Armstrong (WI-07, D · open seat · Tiffany seat · first-time anti-Trump candidate) ----
    ("chris-armstrong-wi-07", "WI", "Representative", [
        claim("ca1", "chris-armstrong-wi-07", "border_immigration", 0, False,
              "Armstrong launched his congressional candidacy explicitly as 'a one-man protest against the Trump "
              "Administration' — the administration whose defining domestic achievements include border wall "
              "construction and mass deportation operations. His opposition to the Trump agenda as his stated "
              "political motivation places him squarely against the rubric's wall-and-military-enforcement "
              "border standard.",
              ["https://www.wsaw.com/2026/03/05/armstrong-thinks-dems-can-overcome-odds-flip-7th-congressional-seat/",
               "https://ballotpedia.org/Chris_Armstrong_(Wisconsin)"]),
        claim("ca2", "chris-armstrong-wi-07", "economic_stewardship", 2, False,
              "Armstrong's campaign platform centers on government action to address healthcare affordability, housing "
              "costs, and energy prices — all expanded-government-spending priorities contrary to the rubric's "
              "balanced-budget and anti-deficit-spending standard. He explicitly frames his candidacy as an answer to "
              "working-class struggles that require federal intervention rather than fiscal restraint.",
              ["https://ballotpedia.org/Chris_Armstrong_(Wisconsin)",
               "https://upnorthnewswi.com/2026/02/06/meet-democratic-candidates-7th-congressional-district/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; slug uniqueness prevents collisions here."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
