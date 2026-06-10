#!/usr/bin/env python3
"""Enrichment batch 118: hand-curated claims for 4 sitting U.S. Senators.

Targets archetype_curated senators at the bottom of the reverse-alpha bucket
(Graham/SC, Cassidy/LA, Scott/FL, Murkowski/AK) — all had exactly 1 claim.
The strict 0-claim federal-senator bucket was exhausted (1 perennial candidate
with no public voting record); these 4 sitting senators are the next-closest
targets at the bottom of reverse-alpha order.

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Lindsey Graham (SC-R, US Senator) ----------------
    ("lindsey-graham", "SC", "Senator", [
        claim("lg1", "lindsey-graham", "sanctity_of_life", 1, False,
              "Approaches abortion through a federal-restrictions strategy, not abolition: his signature Protecting Pain-Capable Unborn Children from Late-Term Abortions Act (reintroduced 2023-2025) bans abortion after 15 weeks with explicit exceptions for rape, incest, and life of the mother — the 'restrictions' model the rubric contrasts with full abolition. In April 2024 Graham criticized Trump for not supporting a federal abortion ban but did not advance a conception-personhood standard.",
              ["https://sbaprolife.org/senator/lindsey-graham",
               "https://www.lgraham.senate.gov/public/index.cfm/2025/1/graham-earns-a-rating-for-protecting-life",
               "https://en.wikipedia.org/wiki/Lindsey_Graham"]),
        claim("lg2", "lindsey-graham", "foreign_policy_restraint", 1, False,
              "The Senate's most prominent hawk on Ukraine: in 2024-2025 Graham declared cutting off Ukraine 'would be worse than Afghanistan,' co-introduced the Sanctioning Russia Act of 2025 to impose 500% tariffs on countries buying Russian exports, and publicly called for sending Tomahawk missiles to Ukraine to strike drone and missile factories inside Russia — directly opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.nbcnews.com/politics/congress/sen-lindsey-graham-pause-us-help-ukraine-worse-afghanistan-rcna195540",
               "https://kyivindependent.com/us-senator-graham-says-tomahawks-should-go-to-ukraine-if-putin-rejects-peace-deal/",
               "https://www.lgraham.senate.gov/public/index.cfm/press-releases?ID=B907D728-63B2-48AC-82DD-0EB1C33EBBC5"]),
    ]),

    # ---------------- Bill Cassidy (LA-R, US Senator) ----------------
    ("bill-cassidy", "LA", "Senator", [
        claim("bc1", "bill-cassidy", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America; as HELP Committee chairman convened a January 2025 hearing on the dangers of chemical abortion drugs alongside Louisiana AG Liz Murrill; voted with the majority to defund Planned Parenthood of Medicaid dollars through the 2025 H.R.1 reconciliation bill — a consistent pro-life record aligned with protecting the unborn.",
              ["https://sbaprolife.org/senator/bill-cassidy",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-leads-entire-louisiana-republican-delegation-in-protecting-women-babies-from-dangerous-abortion-drugs-upholding-louisiana-values/",
               "https://en.wikipedia.org/wiki/Bill_Cassidy"]),
        claim("bc2", "bill-cassidy", "economic_stewardship", 2, True,
              "Named a 2024 Fiscal Hero by Fix the Debt for sustained anti-deficit advocacy; introduced the Fiscal Commission Act to establish a commission targeting debt-to-GDP stabilization below 100% by 2039; delivered a Senate floor speech warning that runaway debt is destroying the American Dream — aligning with the rubric's call for balanced-budget discipline.",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-named-2024-fiscal-hero-by-fix-the-debt/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidydelivers-floor-speech-on-the-national-debt-saving-the-american-dream/",
               "https://www.crfb.org/blogs/cassidy-criticizes-process-and-results-budget-deal"]),
    ]),

    # ---------------- Rick Scott (FL-R, US Senator) ----------------
    ("rick-scott", "FL", "Senator", [
        claim("rs1", "rick-scott", "economic_stewardship", 0, True,
              "Co-introduced the CBDC Anti-Surveillance State Act (2024) with Sen. Ted Cruz to prohibit the Federal Reserve from issuing a central bank digital currency directly or indirectly to individuals, calling a CBDC 'a massive overreach' and 'non-starter.' In May 2026 reintroduced the Chinese CBDC Prohibition Act barring money services businesses and the U.S. Postal Service from using any China-issued digital currency — opposing government financial surveillance on both fronts.",
              ["https://www.rickscott.senate.gov/2024/2/sens-rick-scott-ted-cruz-introduce-legislation-to-ban-central-bank-digital-currencies",
               "https://www.rickscott.senate.gov/2026/5/sen-rick-scott-reintroduces-bill-to-ban-use-of-chinese-cbdc-in-u-s-markets"]),
        claim("rs2", "rick-scott", "economic_stewardship", 1, True,
              "In May 2025 reintroduced a Federal Reserve accountability legislative package to end the Fed's 'out-of-control monetary policies' and restore sound money discipline; separately backed a Principles-Based Balanced Budget Constitutional Amendment (December 2025) requiring the federal government to balance its budget — consistent with the rubric's sound-money and anti-deficit standards.",
              ["https://www.rickscott.senate.gov/2025/5/sen-rick-scott-reintroduces-bills-to-hold-the-federal-reserve-accountable",
               "https://www.rickscott.senate.gov/2025/12/sen-rick-scott-backs-bill-for-balanced-budget-constitutional-amendment"]),
    ]),

    # ---------------- Lisa Murkowski (AK-R, US Senator) ----------------
    ("lisa-murkowski", "AK", "Senator", [
        claim("lm1", "lisa-murkowski", "sanctity_of_life", 0, False,
              "A consistent pro-choice Republican who introduced the Reproductive Choice Act to codify Roe v. Wade into federal law, repeatedly called for congressional action to restore the Roe standard after the 2022 Dobbs ruling, and in 2025 was one of only two Republicans (with Sen. Collins) to vote against the H.R.1 reconciliation provision defunding Planned Parenthood — directly opposing the rubric's life-at-conception standard.",
              ["https://www.murkowski.senate.gov/press/release/-murkowski-reiterates-strong-support-for-codification-of-roe-v-wade-",
               "https://en.wikipedia.org/wiki/Political_positions_of_Lisa_Murkowski",
               "https://alaskawatchman.com/2025/05/29/alaska-prolife-youth-to-urge-sens-murkowski-and-sullivan-to-defund-planned-parenthood/"]),
        claim("lm2", "lisa-murkowski", "biblical_marriage", 1, False,
              "Publicly endorsed marriage equality via the Human Rights Campaign, stating she supports 'the right of all Americans to marry the person they love'; voted for the Respect for Marriage Act (2022) codifying federal recognition of same-sex unions — rejecting the rubric's standard of opposing same-sex marriage at the legislative level.",
              ["https://www.hrc.org/press-releases/senator-lisa-murkowski-endorses-marriage-equality",
               "https://www.murkowski.senate.gov/press/op-ed/op-ed-murkowski-shares-thoughts-on-marriage-equality-with-alaskans",
               "https://en.wikipedia.org/wiki/Political_positions_of_Lisa_Murkowski"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
