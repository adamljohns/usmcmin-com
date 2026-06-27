#!/usr/bin/env python3
"""Enrichment batch 451: 10 claims across 5 active 2026 U.S. Senate candidates.

Bottom-of-alphabet targets (reverse-sorted by state):
  - Karishma Manzur (NH-D, Shaheen seat)
  - Don Tracy (IL-R, 2026 R Nominee, Durbin seat)
  - Kurt Alme (MT-R, 2026 R Nominee, Daines seat)
  - Elizabeth Temple (NC-R, 2026 R Primary Candidate, Tillis seat)
  - Christopher Campbell (KY-I, 2026 Independent General Candidate)

Primary rubric categories added: election_integrity, self_defense, sanctity_of_life,
border_immigration, economic_stewardship.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Karishma Manzur (NH-D, 2026 D Candidate, Shaheen seat) ----------------
    ("karishma-manzur", "NH", "Senator", [
        claim("km1", "karishma-manzur", "border_immigration", 2, False,
              "Her official campaign press release calls for abolishing ICE (Immigration and Customs Enforcement) entirely and replacing it with a 'humane immigration enforcement system' under the Department of Justice — directly opposing the rubric's standard of enforcing immigration law through existing federal enforcement structures and eliminating sanctuary-style policies.",
              ["https://www.karishmaforsenate.com/press-release/abolish-ice-and-build-a-humane-immigration-system",
               "https://ballotpedia.org/Karishma_Manzur"]),
        claim("km2", "karishma-manzur", "economic_stewardship", 2, False,
              "Champions Medicare for All as a core campaign plank, arguing the federal government has a constitutional duty under the General Welfare clause to provide medical care for all citizens — a massive expansion of federal spending that would add trillions to the national debt and is antithetical to the rubric's balanced-budget and anti-deficit standard.",
              ["https://www.thedartmouth.com/article/2026/02/menna-democratic-senate-candidate-karishma-manzur-says-housing-universal-health-care-are-top-policy-priorities",
               "https://www.nhpr.org/nh-news/2025-08-20/nh-senate-race-democratic-primary-2026-karishma-manzur-chris-pappas"]),
    ]),

    # ---------------- Don Tracy (IL-R, 2026 R Nominee, Durbin seat) ----------------
    ("don-tracy", "IL", "Senator", [
        claim("dt1", "don-tracy", "sanctity_of_life", 0, False,
              "Stated in the 2026 primary that he would not support a national abortion ban and believes abortion is a state issue following Dobbs — declining to affirm a federal personhood-from-conception standard. He also opposed criminal penalties for abortion providers when asked during the 2026 Illinois Republican primary debate, and welcomed the endorsement of pro-choice former Senator Mark Kirk.",
              ["https://capitolfax.com/2026/02/20/bailey-only-gop-gov-candidate-to-denounce-sen-andersons-abortion-bill-heidner-calls-to-end-infighting-us-senate-candidate-don-tracy-cardinal-cupich-oppose-penalties/",
               "https://www.illinoisreview.com/illinoisreview/2026/03/anti-trump-pro-choice-mark-kirk-endorses-don-tracy-in-illinois-gop-senate-race.html"]),
        claim("dt2", "don-tracy", "border_immigration", 4, False,
              "Stated in a April 2026 WTTW interview that he finds the U.S.'s 'pure birthright citizenship' policy 'odd,' questioning whether children born to tourists or undocumented immigrants should automatically receive citizenship — aligning with calls to restrict birthright citizenship, consistent with rubric opposition to automatic birthright for illegal-entrant children.",
              ["https://news.wttw.com/2026/04/01/gop-candidate-don-tracy-running-us-senate-future-birthright-citizenship",
               "https://www.pbs.org/video/us-senate-candidate-don-tracy-on-birthright-citizenship-war-in-iran-umwqmm/"]),
    ]),

    # ---------------- Kurt Alme (MT-R, 2026 R Nominee, Daines seat) ----------------
    ("kurt-alme", "MT", "Senator", [
        claim("ka1", "kurt-alme", "election_integrity", 0, True,
              "Explicitly supports requiring voter identification and proof of citizenship for federal elections, stating: 'As America celebrates its 250th anniversary, we must ensure that the fate of our country for the next 250 years is decided by Americans — and only Americans — in secure elections.' Alme's position aligns squarely with the rubric's voter-ID and anti-non-citizen-voting standard.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/kurt-alme/",
               "https://ballotpedia.org/Kurt_Alme"]),
        claim("ka2", "kurt-alme", "self_defense", 1, True,
              "Endorsed by President Trump, who stated Alme will 'Protect our always under siege Second Amendment.' As U.S. Attorney for Montana (2025-2026 and 2017-2020 under Trump), Alme built a record of standing up for the firearm industry and prosecuting cartel-linked gun traffickers rather than targeting lawful gun owners — opposing federal gun restrictions and defending Second Amendment rights consistent with the rubric.",
              ["https://thehill.com/homenews/campaign/5768566-steve-daines-kurt-alme-montana-senate-trump-endorsement/",
               "https://www.msuexponent.com/news/state/vote-kurt-alme-affordability-safer-communities-and-montana-values-kurt-alme/article_59708ca5-3fd4-5358-a88c-7db7d26fcc0e.html"]),
    ]),

    # ---------------- Elizabeth Temple (NC-R, 2026 R Primary Candidate, Tillis seat) ----------------
    ("elizabeth-temple", "NC", "Senator", [
        claim("et1", "elizabeth-temple", "sanctity_of_life", 0, True,
              "Holds a pro-life position: states that elective abortion should only be permitted to protect the life of the mother, opposes taxpayer funding of abortion providers including Planned Parenthood at federal, state, and local levels, and supports safety-standard requirements for chemical abortion drugs — consistent with the rubric's protection of unborn life.",
              ["https://ivoterguide.com/candidate/77962/race/8446/election/1090",
               "https://ballotpedia.org/Elizabeth_Anne_Temple"]),
        claim("et2", "elizabeth-temple", "border_immigration", 0, True,
              "Has proposed requiring all elected officials — including U.S. House and Senate members and mayors — to pledge promoting legal immigration and closed borders 'in order to preserve the history and culture of the United States,' signaling strong alignment with the rubric's call for military-backed border enforcement and an end to open-border policies.",
              ["https://wcti12.com/news/local/meet-elizabeth-temple-candidate-for-us-senate",
               "https://ballotpedia.org/Elizabeth_Anne_Temple"]),
    ]),

    # ---------------- Christopher Campbell (KY-I, 2026 Independent General Candidate) ----------------
    ("christopher-campbell-ky-senate", "KY", "Senator", [
        claim("cc1", "christopher-campbell-ky-senate", "economic_stewardship", 2, False,
              "Champions Medicare for All as a core policy, arguing it is 'the U.S. government's sworn duty' under the General Welfare clause to provide medical care for all citizens and that the program 'will save U.S. taxpayers several trillions of dollars' — a single-payer expansion of federal spending that would dramatically increase federal outlays and add to the national debt, contrary to the rubric's balanced-budget and anti-deficit standard.",
              ["https://candidates.goodparty.org/campbell4congress2026",
               "https://linknky.com/press-releases/2025/11/05/press-release-campbell-declares-intent-to-run-for-senate/"]),
        claim("cc2", "christopher-campbell-ky-senate", "refuse_federal_overreach", 0, False,
              "Campaigns on a Constitutional 'Green Amendment' that would establish a federal constitutional duty to ensure a 'safe, healthy environment' for all citizens — a vehicle for expansive federal environmental regulation and litigation that would significantly grow federal power over state and local land, energy, and economic decisions, inconsistent with the rubric's rejection of unaccountable federal overreach.",
              ["https://candidates.goodparty.org/campbell4congress2026",
               "https://linknky.com/press-releases/2025/11/05/press-release-campbell-declares-intent-to-run-for-senate/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
