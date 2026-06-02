#!/usr/bin/env python3
"""Enrichment batch 11: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators with 0 evidence claims from the BOTTOM
of the alphabet (NE, ND, NC, MT) to avoid collision with the top-of-alphabet
loop.  All R incumbents; sources 2023-2026.

Mix: Pete Ricketts (NE-R), Kevin Cramer (ND-R), John Hoeven (ND-R),
Ted Budd (NC-R), Tim Sheehy (MT-R).

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
    # ---------------- Pete Ricketts (NE-R, US Senator) ----------------
    ("pete-ricketts", "NE", "Senator", [
        claim("pr1", "pete-ricketts", "sanctity_of_life", 0, True,
              "Supports a total abortion ban with no exceptions for rape or incest. Following the 2023 Nebraska March for Life, co-sponsored the No Taxpayer Funding for Abortion Act, the Child Interstate Abortion Notification Act, and the SAVE Moms and Babies Act. In 2024 personally donated $500,000 to defeat a pro-abortion constitutional amendment in Nebraska — affirming that life must be protected from conception.",
              ["https://www.ricketts.senate.gov/news/press-releases/ricketts-announces-co-sponsorships-of-three-pro-life-bills-following-nebraska-march-for-life/",
               "https://en.wikipedia.org/wiki/Pete_Ricketts"]),
        claim("pr2", "pete-ricketts", "self_defense", 1, True,
              "As governor, declared Nebraska a Second Amendment 'sanctuary state,' pledging that state resources would not enforce unconstitutional federal gun restrictions. As senator, co-signed a 2024 amicus curiae brief urging the U.S. Supreme Court to reject Biden administration firearm regulations and protect gun owners' rights — opposing new bans, registries, and magazine restrictions.",
              ["https://www.ricketts.senate.gov/news/press-releases/ricketts-signs-brief-to-defend-gun-owners-and-second-amendment/",
               "https://en.wikipedia.org/wiki/Pete_Ricketts"]),
        claim("pr3", "pete-ricketts", "border_immigration", 1, True,
              "Voted against the bipartisan 2024 Senate border supplemental, publicly declaring it 'doesn't get the job done.' Demanded a 1,000-encounter-per-day enforcement threshold (versus the bill's 5,000), mandatory detention of illegal aliens instead of catch-and-release, and organized Republican senators to require a 72-hour public review period before any vote — insisting on hard enforcement over status quo.",
              ["https://www.ricketts.senate.gov/news/press-releases/ricketts-border-bill-doesnt-get-the-job-done/",
               "https://www.ricketts.senate.gov/news/press-releases/ricketts-colleagues-call-for-72-hour-review-period-before-vote-on-border-supplemental/"]),
    ]),

    # ---------------- Kevin Cramer (ND-R, US Senator) ----------------
    ("kevin-cramer", "ND", "Senator", [
        claim("kc1", "kevin-cramer", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record with SBA Pro-Life America and voted for H.R.1 (the 2025 reconciliation bill) that defunded Planned Parenthood of Medicaid dollars for one year — described as the largest pro-life legislative victory in two decades. Also introduced the Unborn Child Support Act enabling pregnant women to receive child support payments, consistent with recognizing unborn life as legally protected.",
              ["https://sbaprolife.org/senator/kevin-cramer",
               "https://www.cramer.senate.gov/issues/second-amendment"]),
        claim("kc2", "kevin-cramer", "self_defense", 1, True,
              "Received an A+ rating on the 2024 NSSF Congressional Dean's List for a perfect voting and co-sponsorship record on Second Amendment issues. Introduced the Fair Access to Banking Act (reintroduced 2023 with over a third of the Senate as co-sponsors) to bar financial institutions from discriminating against firearms manufacturers and retailers. Formally issued a statement of opposition to the 2022 Bipartisan Safer Communities Act gun-control package.",
              ["https://www.cramer.senate.gov/news/press-releases/cramer-receives-a-rating-in-2024-nssf-congressional-report-card",
               "https://www.cramer.senate.gov/news/press-releases/sen-cramer-statement-of-opposition-to-senate-gun-control-legislation"]),
        claim("kc3", "kevin-cramer", "economic_stewardship", 2, True,
              "Describes himself as a fiscal conservative with a 'proven record of cutting and balancing budgets' through limited government and private-sector growth. In 2025, publicly defended the Trump administration's DOGE-led spending cuts — including proposed reductions at the VA — as necessary reductions of federal waste, consistent with an anti-deficit, balanced-budget philosophy.",
              ["https://www.cramer.senate.gov/biography",
               "https://ballotpedia.org/Kevin_Cramer"]),
    ]),

    # ---------------- John Hoeven (ND-R, US Senator) ----------------
    ("john-hoeven", "ND", "Senator", [
        claim("jh1", "john-hoeven", "sanctity_of_life", 0, True,
              "In the 119th Congress, co-sponsored and voted to advance both the Pain-Capable Unborn Child Protection Act (protecting babies at 20 weeks' development) and the Born-Alive Abortion Survivors Protection Act. Also voted for H.R.1 (2025 reconciliation) that defunded Planned Parenthood of Medicaid dollars — a consistent record of voting to protect unborn and newborn human life.",
              ["https://www.hoeven.senate.gov/news/news-releases/hoeven-votes-to-advance-two-pro-life-bills-he-cosponsored1",
               "https://sbaprolife.org/senator/john-hoeven"]),
        claim("jh2", "john-hoeven", "self_defense", 1, True,
              "Holds an A+ lifetime rating from the NRA Political Victory Fund, reflecting consistent Senate votes against firearms restrictions — including opposition to universal background check mandates and terrorism-watchlist firearm purchase bans. Issued a formal statement opposing federal gun-control legislation when the Senate considered expanded firearm regulations in 2022.",
              ["https://en.wikipedia.org/wiki/John_Hoeven",
               "https://www.hoeven.senate.gov/news/news-releases/hoeven-statement-on-senate-gun-control-legislation"]),
    ]),

    # ---------------- Ted Budd (NC-R, US Senator) ----------------
    ("ted-budd", "NC", "Senator", [
        claim("tb1", "ted-budd", "sanctity_of_life", 0, True,
              "Earned an A+ rating on the SBA Pro-Life America National Pro-Life Scorecard. As senator, co-sponsored the SAVE Moms and Babies Act, the No Taxpayer Funding for Abortion and Abortion Insurance Full Disclosure Act, and the Pain-Capable Unborn Child Protection Act — a consistent record of defending unborn life at every stage of development.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-pro-life-americas-candidate-fund-endorses-pro-life-champion-ted-budd-for-u-s-senate",
               "https://sbaprolife.org/candidate/ted-budd"]),
        claim("tb2", "ted-budd", "self_defense", 1, True,
              "Owner of a gun range and firearms retailer in Rural Hall, NC — bringing direct industry standing to the Senate. In January 2024, filed an amicus curiae brief in NRA v. Vullo urging the Supreme Court to stop New York's financial blacklisting of the NRA and gun-rights groups. Voted in 2023 to disapprove the ATF's rule restricting pistol stabilizing braces, opposing ATF regulatory overreach targeting lawful gun owners.",
              ["https://www.budd.senate.gov/priority-issues/defending-second-amendment-rights/",
               "https://www.budd.senate.gov/2024/01/16/budd-hudson-defend-first-amendment-rights-of-gun-groups/"]),
        claim("tb3", "ted-budd", "border_immigration", 0, True,
              "An early and consistent advocate for building a physical wall on the southern border to stop illegal immigration, drug trafficking, and human trafficking — specifically backing a border wall combined with enforcement measures as a core security priority since his time in the House.",
              ["https://www.budd.senate.gov/about-senator-ted-budd/",
               "https://ballotpedia.org/Ted_Budd"]),
    ]),

    # ---------------- Tim Sheehy (MT-R, US Senator) ----------------
    ("tim-sheehy", "MT", "Senator", [
        claim("ts1", "tim-sheehy", "sanctity_of_life", 0, True,
              "Ran for Senate in 2024 as 'strongly pro-life' and earned the SBA Pro-Life America Candidate Fund endorsement. Publicly opposed Montana Initiative 128, which sought to embed a broad abortion right (through fetal viability) in the Montana constitution — affirming state-level protection of the unborn and a life-from-conception standard.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-pro-life-americas-candidate-fund-endorses-tim-sheehy-u-s-senate",
               "https://en.wikipedia.org/wiki/Tim_Sheehy"]),
        claim("ts2", "tim-sheehy", "border_immigration", 1, True,
              "Identifies securing the border as a core Senate priority — 'fighting for a strong economy, a secure border, American strength' — and ran explicitly against Biden-era open-border policies. As a former Navy SEAL who trained for high-stakes security operations, Sheehy frames illegal immigration as a national security threat demanding mandatory enforcement.",
              ["https://www.sheehy.senate.gov/about/",
               "https://en.wikipedia.org/wiki/Tim_Sheehy"]),
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
