#!/usr/bin/env python3
"""Enrichment batch 206: 5 federal House candidates/members with 0 claims.

archetype_curated bucket exhausted; pulling from archetype_party_default sitting
House members (IL, KY) and low_evidence House candidates (MT, SC).

  Robin Kelly        (IL-02 D, sitting rep · gun-control author · lost Senate primary)
  Raja Krishnamoorthi (IL-08 D, sitting rep · Intelligence Cmte · lost Senate primary)
  Morgan McGarvey    (KY-03 D, sitting rep · only KY Dem in delegation)
  Matt Rains         (MT-01 D, open-seat candidate · West Point / Army pilot / rancher)
  Sam McCown         (SC-01 R, open-seat candidate · physician · lost June 9 primary)

Mix: 4 D / 1 R. Sources: sbaprolife.org, govtrack.us, congress.gov, ballotpedia.org,
robinkelly.house.gov, en.wikipedia.org, mtpr.org.

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
    # ------------ Robin Kelly (IL-02, D, sitting US Rep) ------------
    ("robin-kelly", "IL", "Representative", [
        claim("rk1", "robin-kelly", "self_defense", 1, False,
              "A leading House gun-control advocate who co-chairs the Gun Violence Prevention "
              "Task Force and releases an annual 'Kelly Report' on gun violence — a blueprint "
              "for restricting semi-automatic weapons, closing background-check loopholes, and "
              "expanding red-flag laws — directly opposing the rubric's defense of unrestricted "
              "Second Amendment rights.",
              ["https://robinkelly.house.gov/media-center/press-releases/rep-robin-kelly-releases-2024-kelly-report-gun-violence",
               "https://en.wikipedia.org/wiki/Robin_Kelly"]),
        claim("rk2", "robin-kelly", "sanctity_of_life", 0, False,
              "Holds a 0% lifetime rating from SBA Pro-Life America, having consistently voted "
              "to eliminate or prevent protections for the unborn and for children born alive "
              "after failed abortions — rejecting any life-at-conception or personhood standard.",
              ["https://sbaprolife.org/representative/robin-kelly",
               "https://en.wikipedia.org/wiki/Robin_Kelly"]),
        claim("rk3", "robin-kelly", "sanctity_of_life", 4, False,
              "Voted repeatedly to eliminate prohibitions on taxpayer funding for abortion "
              "domestically and internationally, including votes to allow federal funds to cover "
              "abortion travel expenses — placing her squarely inside the abortion-industry "
              "funding network the rubric opposes.",
              ["https://sbaprolife.org/representative/robin-kelly",
               "https://robinkelly.house.gov/about"]),
    ]),

    # ------------ Raja Krishnamoorthi (IL-08, D, sitting US Rep) ------------
    ("raja-krishnamoorthi", "IL", "Representative", [
        claim("rk1", "raja-krishnamoorthi", "sanctity_of_life", 0, False,
              "Holds a 0% rating from SBA Pro-Life America, having consistently voted to "
              "eliminate or prevent protections for the unborn and against prohibitions on "
              "taxpayer-funded abortion travel — rejecting any life-at-conception standard "
              "across his full House tenure (2017–2026).",
              ["https://sbaprolife.org/representative/raja-krishnamoorthi",
               "https://en.wikipedia.org/wiki/Raja_Krishnamoorthi"]),
        claim("rk2", "raja-krishnamoorthi", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (Dec 2022), which federally codifies "
              "recognition of same-sex marriages and requires all states to honor them — "
              "directly rejecting the one-man-one-woman definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Raja_Krishnamoorthi",
               "https://ballotpedia.org/Raja_Krishnamoorthi"]),
        claim("rk3", "raja-krishnamoorthi", "biblical_marriage", 2, False,
              "Publicly opposed Attorney General Sessions' religious-freedom guidelines as "
              "unlawful discrimination against LGBTQ people, and declared in his 2026 Senate "
              "campaign he 'won't stand by when Trump targets LGBTQ kids' — affirming "
              "transgender ideology and rejecting the rubric's defense of biological-sex norms.",
              ["https://krishnamoorthi.house.gov/media/press-releases/congressman-raja-krishnamoorthi-speaks-out-against-weakening-civil-rights",
               "https://en.wikipedia.org/wiki/Raja_Krishnamoorthi"]),
    ]),

    # ------------ Morgan McGarvey (KY-03, D, sitting US Rep) ------------
    ("morgan-mcgarvey", "KY", "Representative", [
        claim("mm1", "morgan-mcgarvey", "sanctity_of_life", 0, False,
              "Holds a 0% rating from SBA Pro-Life America, having consistently voted to "
              "eliminate or prevent protections for the unborn and against prohibitions on "
              "taxpayer abortion funding — framing his stance as fighting for 'reproductive "
              "rights' as the only Democrat in Kentucky's congressional delegation.",
              ["https://sbaprolife.org/representative/morgan-mcgarvey",
               "https://en.wikipedia.org/wiki/Morgan_McGarvey"]),
        claim("mm2", "morgan-mcgarvey", "self_defense", 1, False,
              "Serves on the Gun Violence Prevention Task Force and supports gun-reform "
              "legislation including universal background checks and other new firearm "
              "restrictions — opposing the rubric's defense of unrestricted Second Amendment "
              "rights.",
              ["https://mcgarvey.house.gov/about",
               "https://ballotpedia.org/Morgan_McGarvey"]),
        claim("mm3", "morgan-mcgarvey", "economic_stewardship", 2, False,
              "Voted against the 2025 'One Big Beautiful Bill' reconciliation package that "
              "included significant deficit-reduction provisions, instead advocating for "
              "maintaining government spending levels — a posture at odds with the rubric's "
              "demand for a balanced budget and anti-deficit fiscal discipline.",
              ["https://en.wikipedia.org/wiki/Morgan_McGarvey",
               "https://govtrack.us/congress/members/morgan_mcgarvey/456904"]),
    ]),

    # ------------ Matt Rains (MT-01, D, open-seat candidate) ------------
    ("matt-rains-mt-01", "MT", "Representative", [
        claim("mr1", "matt-rains-mt-01", "sanctity_of_life", 0, False,
              "Publicly stated he supports access to abortion — rejecting any life-at-conception "
              "or personhood standard — as part of his 2026 Democratic primary campaign for "
              "Montana's western congressional district (MT-01, open Zinke seat).",
              ["https://www.mtpr.org/montana-news/2026-05-04/q-a-matt-rains-democratic-western-district-u-s-house-candidate",
               "https://ballotpedia.org/Matt_Rains"]),
        claim("mr2", "matt-rains-mt-01", "refuse_federal_overreach", 0, False,
              "Opposed federal Medicaid budget cuts, arguing that reductions to Medicaid funding "
              "would damage rural hospitals and healthcare access across Montana — defending "
              "continued federal program expansion rather than returning healthcare decisions to "
              "states and individuals.",
              ["https://www.mtpr.org/montana-news/2026-05-04/q-a-matt-rains-democratic-western-district-u-s-house-candidate",
               "https://www.mtpr.org/montana-news/2026-03-11/montanas-democratic-house-candidates-are-largely-aligned-on-key-issues"]),
    ]),

    # ------------ Sam McCown (SC-01, R, open-seat candidate) ------------
    ("sam-mccown", "SC", "Representative", [
        claim("sm1", "sam-mccown", "economic_stewardship", 2, True,
              "Made the national debt a signature campaign issue, warning that unchecked deficit "
              "spending would cause hyperinflation and calling for fiscal responsibility — "
              "consistent with the rubric's demand for anti-deficit and balanced-budget "
              "discipline.",
              ["https://www.postandcourier.com/politics/sam-mccown-gop-sc-race-congress/article_51a3d698-2210-481a-9896-dcf1c5b9d515.html",
               "https://ballotpedia.org/Sam_McCown"]),
        claim("sm2", "sam-mccown", "industry_capture", 0, True,
              "A physician and medical administrator who ran on cutting government healthcare "
              "bureaucracy and reducing costly regulations, citing the death of his 14-year-old "
              "sister when a hospital ICU was delayed by regulatory approvals — positioning "
              "against pharma-government entanglement even as he championed Trump's agenda for "
              "SC-01 (lost June 9 primary with 17%, seat formerly held by Nancy Mace).",
              ["https://www.postandcourier.com/politics/sam-mccown-gop-sc-race-congress/article_51a3d698-2210-481a-9896-dcf1c5b9d515.html",
               "https://ballotpedia.org/Sam_McCown"]),
        claim("sm3", "sam-mccown", "family_child_sovereignty", 0, True,
              "Specifically opposed diversity, equity, and inclusion (DEI) policies in schools, "
              "running against federal imposition of identity ideology in education — aligning "
              "with the rubric's defense of parental rights and local control over schooling.",
              ["https://www.postandcourier.com/politics/sam-mccown-gop-sc-race-congress/article_51a3d698-2210-481a-9896-dcf1c5b9d515.html",
               "https://news.ballotpedia.org/2026/05/07/jay-byars-r-jenny-honeycutt-r-sam-mccown-r-alex-pelbath-r-mark-smith-r-and-six-other-candidates-are-running-in-the-republican-primary-for-south-carolinas-1st-congressional-district-on/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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
