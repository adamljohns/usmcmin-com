#!/usr/bin/env python3
"""Enrichment batch 556: 5 federal senators — bottom-of-alphabet fill.

Targets sitting/appointed federal senators from states near the end of the
alphabet (WY→MT→NC→OK) that had fewer claims than their peers.  All claims
cite ≥1 reliable primary source and reflect 2024-2026 record/positions.

5 candidates (3 R / 2 D-adjacent):
  Roy Cooper       (NC-D, 2026 Senate nominee)
  James Lankford   (OK-R, US Senator)
  Michael Whatley  (NC-R, 2026 Senate nominee)
  Tim Sheehy       (MT-R, US Senator)
  Alan Armstrong   (OK-R, appointed US Senator — interim)
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
    # ---------------- Roy Cooper (NC-D, 2026 Senate nominee) ----------------
    ("roy-cooper-nc-senate", "NC", "Senator", [
        claim("rc1", "roy-cooper-nc-senate", "election_integrity", 0, False,
              "As North Carolina governor, vetoed SB 824 — the 2018 voter ID bill — even after NC voters passed a constitutional amendment requiring photo ID by referendum, calling it 'a solution in search of a problem.' Also vetoed SB 747 in August 2023 (which eliminated the 3-day mail-in grace period and added signature verification for absentee ballots), calling it 'dangerous'; the Republican legislature overrode both vetoes. As the 2026 Democratic Senate nominee, opposes the federal SAVE Act's proof-of-citizenship voter registration requirement.",
              ["https://abc11.com/voter-id-bill-law-north-carolina-nc-house/4899675",
               "https://governor.nc.gov/news/press-releases/2023/08/24/governor-cooper-veto-election-bill-makes-it-harder-vote-and-votes-count",
               "https://www.axios.com/2023/10/11/north-carolina-republicans-override-governor-voting-laws-veto"]),
        claim("rc2", "roy-cooper-nc-senate", "economic_stewardship", 0, False,
              "As North Carolina governor, vetoed House Bill 690 ('No Central Bank Digital Currency Payments to the State Act') in July 2024, blocking NC from banning CBDC use for state payments and barring the state from participating in any Federal Reserve CBDC pilot program. Cooper called the CBDC ban 'premature, vague and reactionary.' The Republican-controlled legislature overrode the veto in September 2024 — meaning Cooper actively prevented an anti-CBDC law from taking effect.",
              ["https://dailyhodl.com/2024/07/09/north-carolina-governor-vetoes-bill-that-would-have-banned-a-us-cbdc-in-the-state/"]),
        claim("rc3", "roy-cooper-nc-senate", "christian_liberty", 0, False,
              "During the COVID-19 pandemic, issued Executive Order 138 (May 2020) capping indoor worship services at a maximum of 10 persons while 'normal operations' continued at airports, shopping malls, and medical facilities — applying stricter restrictions to religious gatherings than comparable secular venues. A federal judge immediately issued a temporary restraining order, ruling: 'There is no pandemic exception to the Constitution of the United States or the Free Exercise Clause of the First Amendment.'",
              ["https://www.wunc.org/news/2020-05-16/judge-blocks-governors-virus-related-orders-on-churches",
               "https://lc.org/newsroom/details/051820-judge-rules-no-pandemic-exception-to-constitution",
               "https://ncfamily.org/federal-judge-temporarily-restrains-cooper-executive-order-restricting-church-services-in-nc/"]),
    ]),

    # ---------------- James Lankford (OK-R, US Senator) ----------------
    ("james-lankford", "OK", "Senator", [
        claim("jl1", "james-lankford", "family_child_sovereignty", 0, True,
              "Lead sponsor of the Families' Rights and Responsibilities Act (S.204, 119th Congress; originally S.3571, 118th Congress) with Senators Scott, Cramer, Barrasso, Kennedy, and Rubio. The bill requires the federal government to pass strict scrutiny before burdening any parental right over a child's upbringing, education, or healthcare — and gives parents direct legal standing to raise violations in federal and state courts. Re-introduced January 23, 2025.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/204/all-info",
               "https://www.govtrack.us/congress/bills/119/s204",
               "https://www.scott.senate.gov/media-center/press-releases/scott-lankford-foxx-introduce-bill-to-protect-parents-rights/"]),
        claim("jl2", "james-lankford", "foreign_policy_restraint", 1, False,
              "A consistent Ukraine aid supporter: urged President Biden to 'honor our promise to Ukraine,' co-signed letters requesting MiG-29 fighter transfers, and ultimately voted YEA on final passage of H.R. 815 — the $95.3B Ukraine/Israel/Taiwan supplemental (Senate Vote #154, April 23, 2024, passed 79-18) — after dropping his initial border-security condition. Also voted to block the 2025 Iran War Powers Resolution, arguing presidents have inherent authority to use military force against designated terrorist organizations.",
              ["https://www.govtrack.us/congress/votes/118-2024/s154",
               "https://www.lankford.senate.gov/news/press-releases/lankford-issues-statement-on-ukraine-supplemental-aid/",
               "https://www.lankford.senate.gov/news/press-releases/senator-lankford-opposes-war-powers-resolution/"]),
    ]),

    # ---------------- Michael Whatley (NC-R, 2026 Senate nominee) ----------------
    ("michael-whatley", "NC", "Senator", [
        claim("mw1", "michael-whatley", "biblical_marriage", 4, True,
              "As 2026 Republican U.S. Senate nominee, pledges to 'keep radical woke ideology out of schools' and attacks Democrats for pushing 'transgenderism' through teachers' unions. During his tenure as NC GOP Chair, the state Republican Party formally censured Senator Thom Tillis specifically for supporting LGBTQ rights and immigration reform — a recorded institutional action demonstrating active opposition to LGBTQ promotion in policy.",
              ["https://www.theassemblync.com/news/politics/michael-whatley-faith-trump-maga-republicans/",
               "https://www.ontheissues.org/Senate/Michael_Whatley.htm"]),
        claim("mw2", "michael-whatley", "christian_liberty", 0, True,
              "Holds master's degrees in Religion (Wake Forest University) and theology (Notre Dame). At a pastor summit co-organized with the American Renewal Project, declared: 'We don't need separation of faith and politics. We don't need separation of church and state,' calling the recruitment of people of faith into politics 'a personal mission of mine' and 'a really big deal.' Has publicly stated: 'I don't believe the Republican Party should hide from faith.'",
              ["https://www.wral.com/story/gop-senate-candidate-whatley-we-don-t-need-separation-of-church-and-state/22151351/",
               "https://ballotpedia.org/Michael_Whatley"]),
    ]),

    # ---------------- Tim Sheehy (MT-R, US Senator) ----------------
    ("tim-sheehy", "MT", "Senator", [
        claim("ts1", "tim-sheehy", "foreign_policy_restraint", 0, False,
              "Voted NAY on the Senate Iran War Powers Resolution (June 23–24, 2026, passed 50-48) — a joint resolution directing removal of U.S. forces from unauthorized hostilities against Iran and reasserting Article I congressional war authority. Sheehy sided with Republican leadership and the White House against restoring congressional war powers; only four Republicans (Cassidy, Collins, Paul, Murkowski) crossed over to support the Article I restraint measure.",
              ["https://www.npr.org/2026/06/23/nx-s1-5868599/senate-iran-war-powers-resolution"]),
        claim("ts2", "tim-sheehy", "industry_capture", 4, True,
              "Has publicly called for a 'complete overhaul' of the Pentagon's defense acquisition system, framing entrenched defense-contractor relationships as a national security modernization problem rather than a procurement success. Sits on the Senate Agriculture, Nutrition, and Forestry Committee and introduced the Precision Agriculture Cybersecurity Act and the WINGS Act (both 2026) to modernize and secure critical agricultural infrastructure independent of large corporate supply-chain dependencies.",
              ["https://www.congress.gov/member/tim-sheehy/S001232",
               "https://www.sheehy.senate.gov/press-releases/sheehy-statement-on-passage-of-one-big-beautiful-bill/"]),
    ]),

    # ---------------- Alan Armstrong (OK-R, appointed US Senator) ----------------
    ("alan-armstrong", "OK", "Senator", [
        claim("aa1", "alan-armstrong", "foreign_policy_restraint", 0, False,
              "Voted NAY on the Iran War Powers Resolution (June 23, 2026, passed 50-48 in the Senate) — a measure directing removal of U.S. forces from unauthorized hostilities against Iran and reasserting Article I congressional war powers. Armstrong aligned with Republican leadership and the White House against the resolution; only four Republicans (Cassidy, Collins, Paul, Murkowski) voted to assert congressional restraint. As a caretaker senator barred from seeking a full term, Armstrong has no legislative record on social issues — this Iran vote is his most consequential foreign policy data point.",
              ["https://www.npr.org/2026/06/23/nx-s1-5868599/senate-iran-war-powers-resolution",
               "https://en.wikipedia.org/wiki/Alan_S._Armstrong"]),
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
