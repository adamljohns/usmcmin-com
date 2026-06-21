#!/usr/bin/env python3
"""Enrichment batch 344: 4 bottom-of-alphabet U.S. Senate candidates.

Targets (WY/VA/SD/SC/PA bottom-of-alphabet sweep):
  John Fetterman  (PA-D, sitting U.S. Senator)            — 3 new claims
  Hung Cao        (VA-R, 2024 nominee / now Acting SecNav) — 2 new claims
  Brian Bengs     (SD-I, 2026 candidate)                   — 1 new claim
  Annie Andrews   (SC-D, 2026 candidate / pediatrician)    — 1 new claim

Categories: biblical_marriage, self_defense, economic_stewardship, christian_liberty.

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep the master
under GitHub's 50 MB limit.
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
    # ---------- John Fetterman (PA-D, U.S. Senator) ----------
    # Existing: foreign_policy_restraint[2]F, border_immigration[0]F, sanctity_of_life[0]F
    ("john-fetterman", "PA", "Senator", [
        claim("jf4", "john-fetterman", "biblical_marriage", 0, False,
              "In 2013, as Mayor of Braddock, PA, Fetterman officiated the first same-sex marriages "
              "in Allegheny County in open defiance of the state's same-sex marriage ban — an act of "
              "civil disobedience for marriage equality. He pledged as a Senate candidate to 'proudly "
              "and swiftly vote to pass a bill guaranteeing the right to same-sex marriage,' was "
              "endorsed by the Human Rights Campaign, and voted for the Respect for Marriage Act (2022) "
              "which codified federal recognition of same-sex unions and repealed the Defense of "
              "Marriage Act — categorically rejecting the one-man-one-woman definition of marriage.",
              ["https://www.hrc.org/press-releases/human-rights-campaign-endorses-john-fetterman-for-senate",
               "https://en.wikipedia.org/wiki/John_Fetterman"]),
        claim("jf5", "john-fetterman", "self_defense", 1, False,
              "In his first week as U.S. Senator (January 2023), Fetterman co-sponsored a federal "
              "assault-weapons ban — legislation to prohibit the sale of military-style semi-automatic "
              "rifles and high-capacity magazines. Co-sponsoring an assault-weapons ban directly "
              "contradicts the rubric's standard of opposing AWBs and magazine-capacity restrictions.",
              ["https://www.fetterman.senate.gov/fetterman-co-sponsors-four-bills-in-first-week-in-senate/",
               "https://en.wikipedia.org/wiki/John_Fetterman"]),
        claim("jf6", "john-fetterman", "economic_stewardship", 2, False,
              "Fetterman's economic platform centers on protecting and expanding federal safety-net "
              "spending — he voted against a 2023 debt-ceiling deal he said pushes 'people into "
              "poverty' and has opposed reconciliation legislation that cuts Medicaid, Medicare, or "
              "SNAP. His opposition is to spending cuts, not to deficits; he supports increased "
              "federal expenditures on social programs rather than deficit reduction, contrary to "
              "the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.fetterman.senate.gov/fetterman-statement-i-cannot-in-good-conscience-support-a-debt-ceiling-proposal-that-pushes-people-into-poverty/",
               "https://en.wikipedia.org/wiki/John_Fetterman"]),
    ]),

    # ---------- Hung Cao (VA-R, 2024 Senate nominee / now Acting SecNav) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, border_immigration[0]T
    ("hung-cao-senate-2026", "VA", "Senate", [
        claim("hc4", "hung-cao-senate-2026", "economic_stewardship", 2, True,
              "During his 2024 Virginia Senate campaign, Cao stated 'our economy is hurting because "
              "of reckless spending' and highlighted his experience reviewing and overseeing the Navy's "
              "$140 billion budget. He expressed a desire to serve on the Appropriations Committee, "
              "citing his ability to 'review line items and eliminate unnecessary spending' — consistent "
              "with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.vpm.org/elections/2024-10-08/wamu-guide-2024-us-senate-race-virginia-hung-cao-tim-kaine",
               "https://guides.vote/guide/2024-virginia-us-senate-voters-guide"]),
        claim("hc5", "hung-cao-senate-2026", "christian_liberty", 0, True,
              "Following Kennedy v. Bremerton School District (2022) — which protected a public school "
              "football coach's right to pray in view of students after games — Cao stated: 'The right "
              "to express one's faith is a cornerstone of this country. I'm glad to see religious "
              "freedom being protected by the Court.' His support for the ruling reflects his commitment "
              "to robust free exercise of religion in the public square.",
              ["https://localcandidates.org/candidates/hung-cao/",
               "https://en.wikipedia.org/wiki/Hung_Cao"]),
    ]),

    # ---------- Brian Bengs (SD-I, 2026 U.S. Senate candidate) ----------
    # Existing: sanctity_of_life[0]F, self_defense[1]F, border_immigration[0]F
    ("brian-bengs-sd-senate", "SD", "Senate", [
        claim("bb4", "brian-bengs-sd-senate", "economic_stewardship", 2, True,
              "Bengs explicitly campaigns on 'Balance The Budget & Pay Down The Debt,' warning that "
              "'just 25 years ago, we had a federal budget surplus & talked about potentially paying "
              "off the debt' and noting the national debt has grown to 20% above total U.S. annual "
              "GDP. His anti-deficit fiscal platform aligns with the rubric's anti-deficit/balanced-"
              "budget standard — even as his broader social and regulatory positions diverge from "
              "the rubric's God-First framework.",
              ["https://ballotpedia.org/Brian_Bengs",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_South_Dakota"]),
    ]),

    # ---------- Annie Andrews (SC-D, 2026 U.S. Senate candidate / pediatrician) ----------
    # Existing: sanctity_of_life[0]F, self_defense[1]F, industry_capture[0]F
    ("annie-andrews-senate", "SC", "Senate", [
        claim("aa4", "annie-andrews-senate", "economic_stewardship", 2, False,
              "Andrews campaigns on raising wages for South Carolina workers, expanding Medicaid and "
              "Medicare access, and opposing any cuts to social programs, while proposing to fund "
              "these expansions by cutting 'tax breaks for billionaires' rather than reducing overall "
              "government expenditure. Her spending-expansion and redistribution-first platform "
              "is contrary to the rubric's anti-deficit/balanced-budget standard.",
              ["https://womencount.org/candidate/dr-annie-andrews-sc-us-senate/",
               "https://ballotpedia.org/Annie_Andrews"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state same-slug collisions."""
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

    # Minified write — preserve no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
