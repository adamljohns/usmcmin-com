#!/usr/bin/env python3
"""Enrichment batch 14: hand-curated claims for 5 federal Senate candidates.

Targets from the BOTTOM of the alphabet (VA/TX/OR/NH/NM) that were
archetype_curated with 0 evidence claims. Uses the
(slug + state + office_keyword) matcher from earlier batches.

Targets: Hung Cao (VA-R), Ken Paxton (TX-R), Jo Rae Perkins (OR-R),
Scott Brown (NH-R), Mark Ronchetti (NM-R).
Each claim cites >=1 reliable source and reflects 2024-2026 public
positions / legal actions.

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
    # ---------------- Hung Cao (VA-R, 2026 U.S. Senate candidate) ----------------
    ("hung-cao-senate-2026", "VA", "Senate", [
        claim("hc1", "hung-cao-senate-2026", "sanctity_of_life", 0, True,
              "During his 2024 Virginia Senate campaign, stated 'Life begins at conception' and expressed being 'thrilled' by the Supreme Court's Dobbs ruling overturning Roe v. Wade — affirming a life-from-conception standard.",
              ["https://wset.com/news/local/us-senate-election-candidates-virginia-tim-kaine-hung-cao-election-day-2024",
               "https://ballotpedia.org/Hung_Cao"]),
        claim("hc2", "hung-cao-senate-2026", "self_defense", 1, True,
              "Campaign platform stated 'The Constitution is clear regarding the Second Amendment. I will always protect the right to self defense' and Cao strictly opposes new legislation he considers an infringement on Second Amendment rights.",
              ["https://ballotpedia.org/Hung_Cao"]),
        claim("hc3", "hung-cao-senate-2026", "border_immigration", 0, True,
              "Listed 'Securing our borders' as a core federal priority during his 2024 Senate campaign, calling border defense part of 'providing for the common defense' — the federal government's primary duty.",
              ["https://ballotpedia.org/Hung_Cao"]),
    ]),

    # ---------------- Ken Paxton (TX-R, 2026 U.S. Senate candidate / sitting TX AG) ----------------
    ("ken-paxton-senate", "TX", "Senate", [
        claim("kp1", "ken-paxton-senate", "sanctity_of_life", 0, True,
              "As TX Attorney General, secured a unanimous Texas Supreme Court ruling upholding the Human Life Protection Act (near-total abortion ban) and won at the U.S. Supreme Court protecting Texas pro-life laws; consistently defends life from conception in court.",
              ["https://texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-win-texas-pro-life-laws-supreme-court-united-states",
               "https://www.texasattorneygeneral.gov/news/releases/texas-supreme-court-unanimously-upholds-pro-life-law"]),
        claim("kp2", "ken-paxton-senate", "self_defense", 1, True,
              "As TX AG, successfully sued the Biden ATF and blocked the rule reclassifying pistols with stabilizing braces as short-barreled rifles — stopping a regulation that would have criminalized millions of law-abiding gun owners.",
              ["https://ballotpedia.org/Ken_Paxton"]),
        claim("kp3", "ken-paxton-senate", "border_immigration", 1, True,
              "As TX AG, won the federal-court ruling vacating DACA and halted Biden's unlawful freeze on deportations, enforcing mandatory removal of unlawfully present aliens and building the nation's strongest state-level border-enforcement record.",
              ["https://ballotpedia.org/Ken_Paxton",
               "https://www.texasattorneygeneral.gov/news/releases/ag-paxton-leads-11-state-coalition-brief-defend-federal-immigration-laws-and-protect-unborn-children"]),
    ]),

    # ---------------- Jo Rae Perkins (OR-R, 2026 U.S. Senate candidate) ----------------
    ("jo-rae-perkins-2026", "OR", "Senate", [
        claim("jrp1", "jo-rae-perkins-2026", "sanctity_of_life", 0, True,
              "Self-described 'Pro life' candidate who has listed 'Protect the lives of the pre-born, end infanticide' as a top priority across her 2020, 2022, and 2026 Oregon Senate campaigns.",
              ["https://ballotpedia.org/Jo_Rae_Perkins",
               "https://justfacts.votesmart.org/candidate/146001/jo-rae-perkins"]),
        claim("jrp2", "jo-rae-perkins-2026", "self_defense", 0, True,
              "Self-described 'Pro 2nd Amendment' candidate who opposes gun-control restrictions and supports the constitutional right to keep and bear arms, a consistent position across all her Senate campaigns.",
              ["https://ballotpedia.org/Jo_Rae_Perkins",
               "https://justfacts.votesmart.org/candidate/146001/jo-rae-perkins"]),
        claim("jrp3", "jo-rae-perkins-2026", "border_immigration", 0, True,
              "States all immigration must proceed 'via proper channels' and lists 'Secure our borders' as a top campaign priority, consistently across her 2020, 2022, and 2026 Senate races.",
              ["https://ballotpedia.org/Jo_Rae_Perkins"]),
    ]),

    # ---------------- Scott Brown (NH-R, 2026 U.S. Senate candidate / former MA Senator) ----------------
    ("scott-brown-nh-senate", "NH", "Senate", [
        claim("sb1", "scott-brown-nh-senate", "biblical_marriage", 0, True,
              "Stated in his 2011 VoteSmart Political Courage Test: 'I believe marriage is between a man and a woman. States should be free to make their own laws in this area, so long as they reflect the people's will.'",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/18919/scott-brown/",
               "https://ballotpedia.org/Scott_Brown_(Massachusetts)"]),
        claim("sb2", "scott-brown-nh-senate", "sanctity_of_life", 0, False,
              "Stated in his 2011 VoteSmart Political Courage Test that the abortion decision 'should ultimately be made by the woman in consultation with her doctor' — explicitly rejecting a life-from-conception personhood standard.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/18919/scott-brown/",
               "https://ballotpedia.org/Scott_Brown_(Massachusetts)"]),
    ]),

    # ---------------- Mark Ronchetti (NM-R, 2026 U.S. Senate candidate) ----------------
    ("mark-ronchetti-senate-2026", "NM", "Senate", [
        claim("mr1", "mark-ronchetti-senate-2026", "sanctity_of_life", 0, True,
              "Endorsed by National Right to Life in his 2020 Senate run; supported the Hyde Amendment, opposed taxpayer funding of abortion, and called for a constitutional amendment protecting unborn life in New Mexico.",
              ["https://ballotpedia.org/Mark_Ronchetti",
               "https://www.ontheissues.org/Social/Mark_Ronchetti_Abortion.htm"]),
        claim("mr2", "mark-ronchetti-senate-2026", "self_defense", 0, True,
              "States 'I support the second amendment and oppose these bans and gun confiscation' — opposing assault-weapons bans and confiscation schemes in both his 2020 and 2026 Senate campaigns.",
              ["https://ballotpedia.org/Mark_Ronchetti"]),
        claim("mr3", "mark-ronchetti-senate-2026", "border_immigration", 0, True,
              "States he will 'secure our southern border' as a top federal priority, a consistent campaign position across his 2020 and 2026 New Mexico Senate races.",
              ["https://ballotpedia.org/Mark_Ronchetti"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
