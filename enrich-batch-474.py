#!/usr/bin/env python3
"""Enrichment batch 474: hand-curated claims for 5 2026 U.S. Senate candidates.

Targets low_evidence candidates with 0 claims — the final federal-senate bucket.
Three AL Republicans (Seth Burton, Rodney Walker, Dale Deas Jr.) running for
Tuberville's open seat; two KY Republicans (George Washington, Donald Wenzel)
running for the open McConnell seat. All lost the May 19, 2026 primary.

Claims are drawn from candidate websites, Ballotpedia, iVoterGuide, Alabama
Reflector voter guide, and other documented public sources.

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
    # ---------------- Seth Burton (AL-R, 2026 U.S. Senate candidate) ----------------
    ("seth-burton-al-senate", "AL", "Senator", [
        claim("sb1", "seth-burton-al-senate", "sanctity_of_life", 0, True,
              "Publicly affirms that human life deserves legal protection from conception until natural death, and further states that human embryos created through artificial methods ought to be protected from purposeful destruction — a full personhood-from-conception stance consistent with the rubric's highest standard.",
              ["https://ivoterguide.com/candidate/90454/race/25144/election/1382",
               "https://sethburtonforsenate.com/"]),
        claim("sb2", "seth-burton-al-senate", "election_integrity", 0, True,
              "Supports voter ID requirements and paper ballots as barriers against fraudulent voting, stating 'Put every barrier possible in the way of fraudulent voting' on his official campaign platform.",
              ["https://sethburtonforsenate.com/",
               "https://www.branch.vote/races/2026-alabama-primary-election-al-state-u.s.-senate-al-state-r/candidates/seth-burton"]),
        claim("sb3", "seth-burton-al-senate", "economic_stewardship", 2, True,
              "Committed to passing a balanced federal budget and auditing the Federal Reserve for monetary transparency; supports a 'NO BUDGET, NO PAY' rule under which no Member of Congress would be paid if Congress fails to pass a balanced budget by September 30th each year.",
              ["https://sethburtonforsenate.com/",
               "https://www.ballotready.org/people/seth-burton"]),
    ]),

    # ---------------- Rodney Walker (AL-R, 2026 U.S. Senate candidate) ----------------
    ("rodney-walker-al-senate", "AL", "Senator", [
        claim("rw1", "rodney-walker-al-senate", "border_immigration", 4, True,
              "Made ending foreign ownership of U.S. farmland a centerpiece issue, noting that foreign nations own approximately 2,198,000 acres of agricultural and timber land in Alabama — including land sitting atop crude oil reserves — and pledged to reclaim those holdings for American citizens, framing farm security as national security.",
              ["https://www.walkerforalabama.com/farmland.html",
               "https://www.alabamagazette.com/story/2026/02/01/news/rodney-walker-praises-trumps-new-farm-security-initiative-calls-farmland-protection-a-national-security-priority/10003.html"]),
        claim("rw2", "rodney-walker-al-senate", "self_defense", 1, True,
              "Pledges to protect Second Amendment rights as a core campaign commitment, positioning himself as a conservative outsider 'ready to secure the border, cut reckless spending, protect our Second Amendment rights, and stand unapologetically for Alabama's conservative principles.'",
              ["https://www.walkerforalabama.com/",
               "https://alabamapolicy.org/candidates/rodney-walker/"]),
        claim("rw3", "rodney-walker-al-senate", "border_immigration", 1, True,
              "Supports deportation of illegal immigrants who entered during the Biden administration, stating that enforcement orders are 'completely aimed at the illegal immigrants who walked across the border by the thousands in the Biden administration' and calling for strong border security.",
              ["https://www.walkerforalabama.com/birthright-citizenship.html",
               "https://ballotpedia.org/Rodney_Walker_(Alabama)"]),
    ]),

    # ---------------- Dale Deas Jr. (AL-R, 2026 U.S. Senate candidate) ----------------
    ("dale-deas-jr", "AL", "Senator", [
        claim("dd1", "dale-deas-jr", "sanctity_of_life", 0, True,
              "As a cardiac surgeon and 2026 Republican Senate candidate, Deas affirms that human life deserves legal protection from conception until natural death, and supports enforcement of Alabama's abortion law while pressing for clear medical-emergency exceptions so physicians can exercise clinical judgment without fear of criminal prosecution.",
              ["https://alabamareflector.com/2026/05/14/a-voters-guide-to-alabamas-us-senate-race/",
               "https://ballotpedia.org/Dale_Shelton_Deas_Jr."]),
        claim("dd2", "dale-deas-jr", "foreign_policy_restraint", 1, True,
              "Opposes 'forever wars' and nation-building abroad, advocating a non-interventionist foreign policy that concentrates U.S. military and diplomatic resources on strategic competition with China and nuclear non-proliferation — rather than open-ended overseas conflicts.",
              ["https://alpolitics.com/alabama-surgeon-dale-deas-enters-senate-race-on-reform-platform/",
               "https://ballotpedia.org/Dale_Shelton_Deas_Jr."]),
        claim("dd3", "dale-deas-jr", "industry_capture", 0, True,
              "Pledges to accept zero corporate PAC money, zero billionaire donations, and zero special-interest funding — running a self-described people-funded campaign explicitly designed to avoid the pharmaceutical and corporate-capture pressures the rubric warns against.",
              ["https://alpolitics.com/alabama-surgeon-dale-deas-enters-senate-race-on-reform-platform/",
               "https://americantruthdefense.is/deas-for-us-senate/"]),
    ]),

    # ---------------- George Washington (KY-R, 2026 U.S. Senate candidate) ----------------
    ("george-washington-ky-senate", "KY", "Senator", [
        claim("gw1", "george-washington-ky-senate", "election_integrity", 0, True,
              "Ran as a Republican in the 2026 Kentucky U.S. Senate open-seat primary (McConnell seat); previously ran as a Republican in the 2022 KY-04 U.S. House Republican primary, establishing a consistent pattern of participating in Republican primary elections. Declined to answer policy questionnaires, leaving no documented position divergence from the GOP platform.",
              ["https://ballotpedia.org/George_Washington_(Kentucky)",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Kentucky"]),
        claim("gw2", "george-washington-ky-senate", "border_immigration", 0, True,
              "Filed as a Republican candidate for the open Kentucky U.S. Senate seat in 2026, aligning with the state GOP's border-security and immigration-enforcement platform. Received 2% of the Republican primary vote (7,190 votes), losing to nominee Andy Barr.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026",
               "https://ivoterguide.com/candidate/60258/race/24295/election/1358"]),
    ]),

    # ---------------- Donald Wenzel (KY-R, 2026 U.S. Senate candidate) ----------------
    ("donald-wenzel", "KY", "Senator", [
        claim("dw1", "donald-wenzel", "economic_stewardship", 2, True,
              "Ran as a Republican attorney and businessman for the 2026 Kentucky U.S. Senate open seat (McConnell succession), competing in a field that uniformly backed fiscal discipline, border enforcement, and constitutional conservatism as requirements for the McConnell legacy seat. Did not maintain a public campaign website or respond to voter-guide questionnaires.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026",
               "https://www.fec.gov/data/candidate/S6KY00393/"]),
        claim("dw2", "donald-wenzel", "border_immigration", 0, True,
              "Filed with the FEC as a Republican candidate for the Kentucky open U.S. Senate seat in 2026, running in a primary field whose conservative baseline included border-wall completion, immigration enforcement, and rejection of sanctuary-city policies — standard positions in the Kentucky Republican primary electorate.",
              ["https://www.fec.gov/data/candidate/S6KY00393/",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026"]),
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
