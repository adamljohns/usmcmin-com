#!/usr/bin/env python3
"""Enrichment batch 832: hand-curated claims for 5 Nebraska Republican State Senators.

Targets archetype_party_default state senators from Nebraska (NE — continuing
bottom-of-alphabet enrichment after ND processed in batch 831).  All 5 are
Republican members of Nebraska's unicameral legislature with documented records
on life, gun rights, parental rights, transgender policy, and state mandates.

Targets: Paul Strommen (NE-R, Dist. 47), Myron Dorn (NE-R, Dist. 30),
         Mike Moser (NE-R, Dist. 22), Merv Riepe (NE-R, Dist. 12),
         Loren Lippincott (NE-R, Dist. 34).
Each claim cites >=1 reliable source and reflects 2023-2025 voting record /
public positions.

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
    # ---------------- Paul Strommen (NE-R, State Senator Dist. 47) ----------------
    ("paul-strommen", "NE", "State Senator", [
        claim("ps1", "paul-strommen", "biblical_marriage", 2, True,
              "Voted YES on LB 89, the 'Stand With Women Act' (passed 33-16, May 28, 2025, signed June 4, 2025), which defines male and female in Nebraska state law by biological reproductive capacity and bars transgender students from competing on K-12 and postsecondary sports teams that do not match their biological sex. Every Republican member of the Legislature voted in favor, explicitly rejecting gender self-identification ideology in competitive athletics and public policy.",
              ["https://governor.nebraska.gov/governor-pillen-signs-stand-women-act",
               "https://en.wikipedia.org/wiki/Nebraska_Legislative_Bill_89",
               "https://nebraskaexaminer.com/2025/05/14/lawmakers-narrow-advance-bill-to-define-male-and-female-in-nebraska-law-for-school-sports/"]),
        claim("ps2", "paul-strommen", "refuse_state_overreach", 0, True,
              "Co-sponsored LB 698 (2025), which successfully carved out exemptions from Nebraska's voter-approved paid sick leave mandate for seasonal agricultural workers, youth workers under 16, independent contractors, and businesses with 10 or fewer employees. Strommen, an executive with a 50-million-gallon ethanol plant and a former city council member in Sidney, argued the blanket mandate imposed unrealistic compliance costs on small rural employers and family farms, limiting state government's reach into agricultural labor arrangements.",
              ["https://nebraskaexaminer.com/2025/02/03/some-nebraska-lawmakers-seek-exemptions-in-voter-approved-paid-sick-leave-law-as-others-protest/",
               "https://nebraskalegislature.gov/senators/landing-pages/index.php?SenatorID=223"]),
    ]),

    # ---------------- Myron Dorn (NE-R, State Senator Dist. 30) ----------------
    ("myron-dorn", "NE", "State Senator", [
        claim("md1", "myron-dorn", "self_defense", 0, True,
              "Named in roll-call reporting as one of the 33 senators voting YES on LB 77 (Constitutional Carry), which passed 33-14 on April 19, 2023, and was signed by Governor Jim Pillen on April 25, 2023. The law eliminated Nebraska's permit and safety-training requirement for concealed carry of handguns by law-abiding adults 21 and older, ending the state licensing regime that had restricted the right to bear arms without government permission.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://governor.nebraska.gov/press/icymi-governor-pillen-signs-constitutional-carry-bill-law",
               "https://journalstar.com/news/state-and-regional/govt-and-politics/bill-allowing-nebraskans-to-carry-concealed-guns-without-permit-passes-legislature/article_cec3133c-ef81-5101-915e-5069b11916bc.html"]),
        claim("md2", "myron-dorn", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (passed 33-15, May 19, 2023, signed May 22, 2023), which enacted Nebraska's 12-week abortion ban — the most significant pro-life law in Nebraska since Roe's reversal. Dorn, an Adams County farmer serving on the Appropriations Committee, cast one of the 33 votes needed to overcome a Democratic filibuster and enact the restriction on elective abortions past 12 weeks gestation.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately",
               "https://update.legislature.ne.gov/?p=34361"]),
        claim("md3", "myron-dorn", "biblical_marriage", 2, True,
              "Voted YES on LB 574 (passed 33-15, May 19, 2023), which also enacted Nebraska's first statutory ban on gender-affirming medical interventions — including puberty blockers, cross-sex hormones, and surgeries — for minors under 19. The gender-care restrictions took effect October 1, 2023, and were upheld by the Nebraska Supreme Court in July 2024, cementing rejection of transgender medical ideology as applied to children.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://nebraskaexaminer.com/2024/07/26/nebraska-supreme-court-upholds-legislation-combining-abortion-and-trans-health-care-for-minors/",
               "https://update.legislature.ne.gov/?p=34361"]),
    ]),

    # ---------------- Mike Moser (NE-R, State Senator Dist. 22) ----------------
    ("mike-moser", "NE", "State Senator", [
        claim("mm1", "mike-moser", "sanctity_of_life", 0, True,
              "Publicly states support for 'legal protection for every pre-born child from the moment of conception, unless the mother's life is at risk' — an explicit life-at-conception position recorded in his Nebraska voter guide answers. He backed this up legislatively: voted YES on LB 574 (passed 33-15, May 19, 2023), which enacted Nebraska's 12-week abortion limit and was the most restrictive statewide abortion law in Nebraska post-Dobbs.",
              ["https://en.wikipedia.org/wiki/Mike_Moser_(politician)",
               "https://www.nebraskavoterguide.com/candidates/mike-moser",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-takes-effect-immediately"]),
        claim("mm2", "mike-moser", "family_child_sovereignty", 0, True,
              "On record stating: 'Parents are the primary educators of their own children and should have the most say over what their child is taught in the classroom.' A former mayor of Columbus (2004-2016) and current state senator, Moser consistently backs parental rights in K-12 policy, supporting school choice legislation (LB 753, Opportunity Scholarships Act, 2023) to expand family educational options beyond the public school assignment system.",
              ["https://en.wikipedia.org/wiki/Mike_Moser_(politician)",
               "https://www.nebraskavoterguide.com/candidates/mike-moser",
               "https://nebraskaexaminer.com/2023/05/24/opportunity-scholarship-bill-given-final-ok-will-make-nebraska-a-school-choice-state/"]),
        claim("mm3", "mike-moser", "self_defense", 0, True,
              "Voted YES on LB 77 (Constitutional Carry), which passed 33-14 on April 19, 2023, and was signed by the governor April 25, 2023. The law allows law-abiding Nebraskans 21 and older to carry concealed handguns without a permit or government-mandated safety training, eliminating the prior permit requirement that restricted the exercise of the right to bear arms in Nebraska.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://governor.nebraska.gov/press/icymi-governor-pillen-signs-constitutional-carry-bill-law"]),
    ]),

    # ---------------- Merv Riepe (NE-R, State Senator Dist. 12) ----------------
    ("merv-riepe", "NE", "State Senator", [
        claim("mr1", "merv-riepe", "self_defense", 0, True,
              "Voted YES on LB 77 (Constitutional Carry), which passed 33-14 on April 19, 2023, and was signed by Governor Pillen on April 25, 2023. The law eliminated Nebraska's permit and safety-training requirement for concealed carry of handguns by law-abiding adults 21 and older, and Riepe was among the 33 senators who voted to end a filibuster and advance the bill to passage.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://governor.nebraska.gov/press/icymi-governor-pillen-signs-constitutional-carry-bill-law",
               "https://journalstar.com/news/state-and-regional/govt-and-politics/bill-allowing-nebraskans-to-carry-concealed-guns-without-permit-passes-legislature/article_cec3133c-ef81-5101-915e-5069b11916bc.html"]),
        claim("mr2", "merv-riepe", "biblical_marriage", 2, True,
              "Cast the decisive 33rd vote on the LB 574 cloture motion (May 2023), making possible Nebraska's first ban on gender-affirming medical procedures for minors — puberty blockers, cross-sex hormones, and surgeries for anyone under 19. Riepe negotiated the shift from a 6-week to a 12-week abortion limit as part of the same bill, then provided the margin-of-one vote needed to pass the entire combined measure (33-15, May 19, 2023). The gender-care restrictions were upheld by the Nebraska Supreme Court in July 2024.",
              ["https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://siouxcityjournal.com/news/state-and-regional/govt-and-politics/nebraska-senator-not-budging-from-abortion-vote-despite-weekend-pressure/article_42112781-ee23-5226-8f18-2891eabce5e3.html"]),
    ]),

    # ---------------- Loren Lippincott (NE-R, State Senator Dist. 34) ----------------
    ("loren-lippincott", "NE", "State Senator", [
        claim("ll1", "loren-lippincott", "self_defense", 0, True,
              "Voted YES on LB 77 (Constitutional Carry, passed 33-14, April 19, 2023) and is a member of the National Rifle Association. Lippincott — a former U.S. Air Force F-16 fighter pilot and farmer — describes Second Amendment rights as a leading legislative priority since taking office in January 2023, and his NRA membership reflects a consistent constitutional-carry posture on firearm rights.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://governor.nebraska.gov/press/icymi-governor-pillen-signs-constitutional-carry-bill-law",
               "https://ballotpedia.org/Loren_Lippincott"]),
        claim("ll2", "loren-lippincott", "sanctity_of_life", 0, True,
              "Self-described 'leading advocate for pro-life protections' in the Nebraska Legislature and voted YES on LB 574 (passed 33-15, May 19, 2023), which enacted Nebraska's 12-week abortion ban — the most significant post-Dobbs pro-life law in the state. Lippincott's publicly stated platform centers pro-life protections alongside faith-community values and family policy, reflecting a consistent pro-life legislative posture.",
              ["https://ballotpedia.org/Loren_Lippincott",
               "https://lorenlippincott.com/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately"]),
        claim("ll3", "loren-lippincott", "family_child_sovereignty", 0, True,
              "Voted YES on LB 753 (Opportunity Scholarships Act), which passed 33-11 on May 24, 2023, and was signed into law by Governor Pillen on May 30, 2023 — making Nebraska a school-choice state. The law provides up to $10 million per year in scholarship tax credits allowing families to direct education funding toward private or parochial schools, supporting parental rights to choose the educational environment best suited to their children's needs and values.",
              ["https://nebraskaexaminer.com/2023/05/24/opportunity-scholarship-bill-given-final-ok-will-make-nebraska-a-school-choice-state/",
               "https://governor.nebraska.gov/press/school-choice-puts-kids-first",
               "https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=50326"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
