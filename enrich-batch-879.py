#!/usr/bin/env python3
"""Enrichment batch 879: hand-curated claims for 5 Nebraska Republican state senators.

Targets archetype_party_default State Senators (NE) with 0 evidence claims, picked
from the bottom of the remaining enrichable pool after the archetype_curated federal
bucket was fully exhausted. All 5 voted YES on LB77 (permitless concealed carry,
April 2023) and on LB574 (gender-affirming care ban for minors + 12-week abortion
limit, May 2023).

Targets: Loren Lippincott, Mike Moser, Myron Dorn, Merv Riepe, Brad von Gillern
(all NE-R, State Senator).

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
    # ---- Loren Lippincott (NE-R, District 34, State Senator) ----
    ("loren-lippincott", "NE", "Senator", [
        claim("ll1", "loren-lippincott", "self_defense", 0, True,
              "Voted YES on LB77 (signed April 25, 2023), Nebraska's permitless-concealed-carry law, in a 33-14 vote that made Nebraska a constitutional-carry state — allowing any law-abiding adult 21+ to carry a concealed handgun without a permit or government training requirement. Lippincott is a lifelong NRA member who has described himself as a consistent defender of Second Amendment rights.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49710",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
        claim("ll2", "loren-lippincott", "biblical_marriage", 2, True,
              "Voted YES on LB574 (Adopt the Let Them Grow Act / Preborn Child Protection Act, signed May 22, 2023), which prohibited gender-affirming medical interventions — puberty blockers, cross-sex hormones, and surgeries — for minors under 19, directly rejecting transgender ideology in state medical policy.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49961",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
        claim("ll3", "loren-lippincott", "christian_liberty", 0, True,
              "Dismissed the principle of church-state separation as 'total hogwash' after questions arose about a religious group using a state Capitol hearing room, arguing the nation was founded on Christian principles and that religious exercise belongs in public life. Also sponsored LB550 to allow students to leave school for off-campus religious instruction during the school day.",
              ["https://nebraskaexaminer.com/2024/03/13/more-scrutiny-coming-over-use-of-state-legislative-space-after-bible-study-held-in-hearing-room/",
               "https://ballotpedia.org/Loren_Lippincott"]),
    ]),

    # ---- Mike Moser (NE-R, District 22, State Senator / Transportation Committee Chair) ----
    ("mike-moser", "NE", "Senator", [
        claim("mm1", "mike-moser", "self_defense", 0, True,
              "Voted YES on LB77 (signed April 25, 2023), Nebraska's constitutional-carry law permitting law-abiding adults 21+ to carry concealed handguns without a permit, in a 33-14 vote.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49710",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
        claim("mm2", "mike-moser", "biblical_marriage", 2, True,
              "Voted YES on LB574 (signed May 22, 2023), which banned gender-affirming medical interventions for minors under 19 and restricted elective abortions after 12 weeks — directly rejecting transgender ideology in state health policy.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49961",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
    ]),

    # ---- Myron Dorn (NE-R, District 30, State Senator) ----
    ("myron-dorn", "NE", "Senator", [
        claim("md1", "myron-dorn", "self_defense", 0, True,
              "Voted YES on LB77 (signed April 25, 2023) in a 33-14 vote making Nebraska a constitutional-carry state; law-abiding adults may carry concealed handguns without a government permit.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49710",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
        claim("md2", "myron-dorn", "biblical_marriage", 2, True,
              "Voted YES on LB574 (May 2023), which banned gender-affirming medical interventions for minors and limited elective abortions to 12 weeks. Dorn was one of four senators who had initially raised concerns but ultimately provided a yes vote on the combined bill to overcome the filibuster.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49961",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
    ]),

    # ---- Merv Riepe (NE-R, District 12, State Senator) ----
    ("merv-riepe", "NE", "Senator", [
        claim("mr1", "merv-riepe", "sanctity_of_life", 0, False,
              "Voted 'present, not voting' on LB626 (Nebraska Heartbeat Act, April 2023), denying the bill the 33rd vote it needed to break a filibuster and advance to final passage. The bill would have banned most abortions when cardiac activity is detected (approximately 6 weeks), a near-total ban aligned with a life-at-conception standard. Riepe's abstention single-handedly killed the measure; Nebraska Right to Life subsequently rescinded his endorsement.",
              ["https://nebraskaexaminer.com/2023/04/27/nebraska-abortion-ban-tied-to-cardiac-activity-falls-one-vote-short-20-week-limit-remains-intact/",
               "https://nebraskaexaminer.com/briefs/nebraska-right-to-life-rescinds-endorsement-of-state-sen-merv-riepe/"]),
        claim("mr2", "merv-riepe", "self_defense", 0, True,
              "Voted YES on LB77 (April 2023) constitutional-carry law, 33-14, allowing law-abiding adults 21+ to carry concealed firearms without a permit.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49710",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
        claim("mr3", "merv-riepe", "biblical_marriage", 2, True,
              "Provided the decisive 33rd yes vote for LB574 (May 2023), breaking the filibuster on a bill that banned gender-affirming medical interventions for minors and limited abortions to 12 weeks. His vote was the key swing that overcame the filibuster, and he acknowledged his earlier LB626 abstention as a mistake.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://nebraskaexaminer.com/2024/02/22/i-made-a-mistake-lawmaker-who-sank-nebraskas-near-total-abortion-ban-seeks-changes/"]),
    ]),

    # ---- Brad von Gillern (NE-R, District 4, State Senator) ----
    ("brad-von-gillern", "NE", "Senator", [
        claim("bvg1", "brad-von-gillern", "self_defense", 0, True,
              "Voted YES on LB77 (April 2023), Nebraska's constitutional-carry law, in a 33-14 vote. Von Gillern articulated the core Second Amendment argument in support: 'Criminals don't care what the law says,' framing permit requirements as burdens on law-abiding citizens rather than deterrents to crime.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49710",
               "https://journalstar.com/news/state-and-regional/govt-and-politics/bill-allowing-nebraskans-to-carry-concealed-guns-without-a-permit-passes-legislature/article_cec3133c-ef81-5101-915e-5069b11916bc.html"]),
        claim("bvg2", "brad-von-gillern", "biblical_marriage", 2, True,
              "Voted YES on LB574 (May 2023), which banned gender-affirming medical interventions for minors under 19 and restricted elective abortions after 12 weeks, in a 33-15 final vote.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=49961",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
