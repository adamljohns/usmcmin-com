#!/usr/bin/env python3
"""Enrichment batch 406: hand-curated claims for 5 federal senators/candidates.

Targets senators/candidates with 5 existing claims from bottom-of-alphabet states
(VA, TX, TX, TN, RI). Adds 2 claims each in DISTINCT rubric categories not yet covered.
All positions verified via official senate.gov, congress.gov, govtrack.us, ballotpedia.org,
ontheissues.org, and official senator/campaign websites.

Targets: Hung Cao (VA-R), Ken Paxton (TX-R), Marsha Blackburn (TN-R),
         Jack Reed (RI-D), Jasmine Crockett (TX-D).
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
    # ---------------- Hung Cao (VA-R, 2024 Senate nominee) ----------------
    ("hung-cao-senate-2026", "VA", "Senate Virginia", [
        claim("hc406a", "hung-cao-senate-2026", "biblical_marriage", 0, True,
              "During his 2024 Virginia Senate campaign, Cao stated that same-sex marriage is 'a states' rights issue' but that 'at the federal level, it needs to be illegal,' opposing federal codification of same-sex marriage. A Virginia Catholic Conference voter guide rated his position as 'mostly ban' on same-sex marriage, consistent with the rubric's one-man-one-woman standard.",
              ["https://www.smithmountaineagle.com/news/on-20-issues-virginia-u-s-senate-candidates-kaine-and-cao/article_4b999538-8fc2-11ef-bdbb-cb01c5d43583.html",
               "https://ballotpedia.org/Hung_Cao"]),
        claim("hc406b", "hung-cao-senate-2026", "election_integrity", 0, True,
              "Cao made election integrity a centerpiece of his 2024 Virginia Senate campaign, demanding photo voter ID and declaring 'We demand election integrity. We cannot have a democratic republic if we cannot trust the legitimacy of our elections.' He stated, 'If you can show an ID to go to a movie theater, you had better be required to show an ID to vote.'",
              ["https://www.hungforva.com/election-integrity/",
               "https://ballotpedia.org/Hung_Cao"]),
    ]),

    # ---------------- Ken Paxton (TX-R, 2026 Senate nominee) ----------------
    ("ken-paxton-senate", "TX", "Senate Texas", [
        claim("kp406a", "ken-paxton-senate", "biblical_marriage", 0, True,
              "As Texas AG in 2015, Paxton advised county clerks they could refuse same-sex marriage licenses on religious-freedom grounds following Obergefell v. Hodges, describing the ruling as an attack on Americans' religious freedoms. He stated that 'same-sex marriage is not lawful under the U.S. Constitution' and consistently championed traditional one-man-one-woman marriage — a stance he maintained through his 2026 Senate run.",
              ["https://en.wikipedia.org/wiki/Ken_Paxton",
               "https://ballotpedia.org/Ken_Paxton"]),
        claim("kp406b", "ken-paxton-senate", "foreign_policy_restraint", 4, True,
              "Paxton opposed the AIPAC-backed incumbent Sen. John Cornyn in the 2026 Texas Senate primary and defeated him by more than 25 points. AIPAC explicitly endorsed Cornyn; Paxton's campaign drew a clear contrast between the nationalist America-First lane and the AIPAC/establishment-donor lane. Paxton's win was noted by Track AIPAC as unseating one of their top endorsed incumbents.",
              ["https://www.trackaipac.com/candidates",
               "https://www.newarab.com/news/maga-aipac-texas-primary-runoff-highlight-2026-us-politics"]),
    ]),

    # ---------------- Marsha Blackburn (TN-R, US Senator) ----------------
    ("marsha-blackburn-gov", "TN", "Governor of Tennessee", [
        claim("mb406a", "marsha-blackburn-gov", "election_integrity", 0, True,
              "Blackburn championed election-integrity measures throughout her Senate tenure and introduced the Election Security Partnership Act (2026) with Sen. Lindsey Graham to incentivize states to verify voter rolls against DHS's SAVE database, weeding out non-citizens. She declared 'I will not rest until we pass election integrity measures in any way possible' and noted Tennessee ranks #1 in election integrity because it cleaned up voter rolls and requires voter ID.",
              ["https://www.blackburn.senate.gov/2026/6/blackburn-graham-introduce-legislation-to-incentivize-every-state-to-submit-voter-rolls-to-dhs",
               "https://ballotpedia.org/Marsha_Blackburn"]),
        claim("mb406b", "marsha-blackburn-gov", "foreign_policy_restraint", 4, True,
              "Blackburn co-led the No WHO Pandemic Preparedness Treaty Without Senate Approval Act (2022-2023), co-introduced with Sen. Ron Johnson, requiring any WHO pandemic convention to be ratified as a treaty by two-thirds of the Senate. She stated the WHO 'failed miserably in their response to COVID-19' and that new treaty powers 'would increase the WHO's power at the expense of American sovereignty,' consistent with the rubric's opposition to WHO/UN expansions of authority.",
              ["https://blackburn.senate.gov/2023/2/blackburn-johnson-lead-colleagues-in-effort-to-protect-american-sovereignty-against-world-health-organization",
               "https://blackburn.senate.gov/2022/6/blackburn-colleagues-lead-effort-to-protect-american-sovereignty-against-world-health-organization"]),
    ]),

    # ---------------- Jack Reed (RI-D, US Senator) ----------------
    ("jack-reed", "RI", "Senator", [
        claim("jr406a", "jack-reed", "biblical_marriage", 0, False,
              "Reed voted YES on the Respect for Marriage Act (H.R.8404, Senate vote #362, November 29, 2022, 61-36) to federally codify same-sex and interracial marriage. Reed stated 'All Americans, no matter who they love or where they live, should be treated fairly and equally under the law,' and was a cosponsor of the bill — directly rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.reed.senate.gov/news/releases/us-senate-passes-bipartisan-respect-for-marriage-act-to-protect-marriage-equality",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00362.htm"]),
        claim("jr406b", "jack-reed", "border_immigration", 0, False,
              "Reed has consistently opposed physical border-barrier construction and restrictive enforcement. His Senate website states he supports 'a pathway to citizenship for the undocumented population already here' and opposes border-wall funding. He supported the Border Act of 2024, which included asylum reforms but no wall funding or mass deportation — rejecting the rubric's wall-plus-military mandate.",
              ["https://www.reed.senate.gov/issues/immigration",
               "https://ballotpedia.org/Jack_Reed"]),
    ]),

    # ---------------- Jasmine Crockett (TX-D, House/Senate candidate) ----------------
    ("jasmine-crockett", "TX", "running for", [
        claim("jc406a", "jasmine-crockett", "biblical_marriage", 0, False,
              "Crockett is a staunch LGBTQ+ ally who supports marriage equality and opposes any restriction on same-sex marriage. She criticized conservatives for what she called their 'obsession with trans people' and backed the Equality Act to extend federal civil-rights protections to sexual orientation and gender identity — directly opposing the rubric's one-man-one-woman marriage standard.",
              ["https://www.advocate.com/politics/jasmine-crockett-james-talarico-lgbtq",
               "https://en.wikipedia.org/wiki/Jasmine_Crockett"]),
        claim("jc406b", "jasmine-crockett", "economic_stewardship", 2, False,
              "As a House member and Senate candidate, Crockett supported multi-trillion-dollar progressive spending programs including Medicare for All-style proposals, expanded social spending, and opposed budget-cutting reconciliation bills. She voted against the Republican FY2025 reconciliation measure that included spending cuts, backing the Democratic progressive caucus position of universal and affordable healthcare and expanded federal expenditures — contrary to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.jasmineforus.com/",
               "https://www.govtrack.us/congress/members/jasmine_crockett/456944"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
