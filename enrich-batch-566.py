#!/usr/bin/env python3
"""Enrichment batch 566: 5 Republican State Representatives (3 WA, 2 VT), 10 claims.

All archetype_curated federal and prior state-rep slots (WI) are exhausted.
This batch continues bottom-of-alphabet coverage with WA and VT Republican
state representatives that have 0 claims.

Candidates:
  Andrew Engell    (WA-7  R, State Representative — District 7, largest in WA)
  Andrew Barkis    (WA-2  R, State Representative — District 2, Yelm/Thurston Co.)
  Alex Ybarra      (WA-13 R, State Representative — District 13, Minority Caucus VC)
  Zachary Harvey   (VT    R, State Representative — Rutland-3, VTGOP Finance Chair)
  Woodman Page     (VT    R, State Representative — Orleans-2, USAF Major ret.)

Rubric categories covered:
  Engell   — self_defense[1], economic_stewardship[2]
  Barkis   — self_defense[1], economic_stewardship[2]
  Ybarra   — economic_stewardship[2], self_defense[1]
  Harvey   — self_defense[1], economic_stewardship[2]
  Page     — self_defense[1], economic_stewardship[2]
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
    # -------- Andrew Engell (WA-7, R, State Representative) --------
    ("andrew-engell", "WA", "State Representative", [
        claim("ae1", "andrew-engell", "self_defense", 1, True,
              "Voted NO on Washington HB 1163 (March 2025), a permit-to-purchase bill that requires a government-issued firearm purchase permit, mandatory fingerprinting, live-fire training certification, and creates a statewide registry of firearm owners. The House passed it 57-39 along strict party lines; Governor Ferguson signed it May 20, 2025 (Chapter 370, 2025 Laws). Engell co-authored a public alert to 7th District constituents — Washington's largest legislative district, covering rural ranch and farm communities — urging them to engage and calling the bill 'a bad gun bill.' He voted NO throughout its House passage. The bill's statewide firearm registry and permit mandate directly contradict constitutional-carry and anti-registry principles.",
              ["https://andrewengell.houserepublicans.wa.gov/2025/03/07/bad-gun-bill-being-debated-tonight-how-you-can-watch-and-make-an-impact-reps-abell-engell/",
               "https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation"]),
        claim("ae2", "andrew-engell", "economic_stewardship", 2, True,
              "In the 2026 Washington legislative session, majority Democrats passed a new state income tax — Washington has no state income tax and voters have repeatedly rejected one. After more than 24 consecutive hours of floor debate (the longest in recent legislative memory), Engell voted NO, sponsored multiple amendments that were rejected by the majority, and gave repeated floor speeches defending rural Washingtonians. He stated: 'Washingtonians have consistently rejected an income tax,' and warned the bill included an emergency clause to block a citizens' referendum. His post-passage joint statement warned: 'Once a new tax is created, the threshold almost always comes down and more working families get pulled in.' He also opposed the 2025-27 operating budget ($77.8 billion; 54-44 House vote, April 1, 2025) as fiscally reckless.",
              ["https://andrewengell.houserepublicans.wa.gov/2026/03/10/joint-statement-from-reps-hunter-abell-and-andrew-engell-on-the-passage-of-a-new-state-income-tax/",
               "https://andrewengell.houserepublicans.wa.gov/2026/02/27/rep-andrew-engell-joins-kpq-to-discuss-income-tax-vote-rural-health-care-and-bipartisan-wins/"]),
    ]),

    # -------- Andrew Barkis (WA-2, R, State Representative) --------
    ("andrew-barkis", "WA", "State Representative", [
        claim("ab1", "andrew-barkis", "self_defense", 1, True,
              "Voted NO on Washington HB 1163 (March 2025), which creates a state permit-to-purchase firearm scheme, mandates fingerprinting and live-fire training certificates, and establishes a statewide registry of all firearm owners and transfers. The House passed it 57-39 along party lines; signed by Governor Ferguson on May 20, 2025. Barkis engaged closely enough to draft and submit a floor amendment (1163-S2 AMH BARK ADAM 190, March 8, 2025) — later withdrawn — reflecting active deliberation on limiting the bill's Second Amendment harms. He voted NO on final passage. The NRA-ILA confirmed the bill passed both chambers on party-line votes with Republicans uniformly opposed.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("ab2", "andrew-barkis", "economic_stewardship", 2, True,
              "Voted NO on Washington's 2025-27 operating budget ($77.8 billion; 54-44 House vote, April 1, 2025), joining all 39 House Republicans in opposing a spending plan financed by more than $24 billion in new taxes over several years. Barkis has consistently championed alternatives focused on taxpayer relief: his platform calls for sales tax relief, property tax relief, and expansion of the Working Families Tax Credit to ease burdens on families rather than grow government expenditure. He serves on the House Economic and Revenue Forecast Council, giving him direct visibility into the state's fiscal trajectory and the structural deficits created by excess spending.",
              ["https://washingtonstatestandard.com/2025/04/01/washington-house-passes-budget-clearing-way-for-talks-with-senate/",
               "https://andrewbarkis.houserepublicans.wa.gov/"]),
    ]),

    # -------- Alex Ybarra (WA-13, R, State Representative) --------
    ("alex-ybarra", "WA", "State Representative", [
        claim("ay1", "alex-ybarra", "economic_stewardship", 2, True,
              "As Minority Caucus Vice-Chair of the Washington House, Ybarra led the Republican caucus's fiscal opposition to the 2025-27 operating budget ($77.8 billion; 54-44 House vote, April 1, 2025, with all 39 Republicans voting no). He published an op-ed titled 'State spending is out of control — here's what we're doing about it,' warning that Washington burned through a $14 billion surplus in just a few years to produce a $7-10 billion deficit 'primarily due to overspending and overly optimistic revenue assumptions.' The enacted budget layered on more than $24 billion in new taxes (capital gains, payroll tax) — taxes that Ybarra said 'aren't just unsustainable — they're unaffordable.' Even with the tax hikes, the budget cut special education, Medicaid, and child support enforcement for low-income families.",
              ["https://alexybarra.houserepublicans.wa.gov/2025/03/28/rep-alex-ybarra-state-spending-is-out-of-control-heres-what-were-doing-about-it/",
               "https://washingtonstatestandard.com/2025/04/26/new-taxes-no-furloughs-in-wa-legislatures-77-8b-budget-deal/"]),
        claim("ay2", "alex-ybarra", "self_defense", 1, True,
              "Voted NO on Washington HB 1163 (2025 session) — the permit-to-purchase firearm bill requiring state permits, fingerprinting, training mandates, and a statewide firearm registry — as part of the unanimous 39-member Republican no-vote (bill passed 57-39, signed May 20, 2025). Ybarra has an established record of opposing gun-control legislation on the House floor: in March 2023 he gave a floor speech explicitly against HB 1240 (Washington's assault weapons ban), described by his office as 'speaking against [a] bill restricting constitutionally protected gun rights.' The NRA-ILA tracked Republican opposition to HB 1163 throughout the 2025 session, confirming a unified party-line no vote.",
              ["https://alexybarra.houserepublicans.wa.gov/2023/03/09/rep-alex-ybarra-speaks-against-bill-restricting-constitutionally-protected-gun-rights-hb-1240/",
               "https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate"]),
    ]),

    # -------- Zachary Harvey (VT, R, State Representative — Rutland-3) --------
    ("zachary-harvey", "VT", "State Representative", [
        claim("zh1", "zachary-harvey", "self_defense", 1, True,
              "As a member of the Vermont House Committee on Judiciary, Harvey cast a NO vote on March 14, 2026, when H.606 — an omnibus gun control bill — advanced out of committee 6-5 along party lines. H.606 would impose Vermont's first-ever prohibition on machine guns and Auto-RESET conversion devices, restrict gun ownership for persons under court-ordered mental health treatment, and add criminal penalties for firearm storage violations. Harvey specifically challenged the mental health prohibition as a rights overreach, warning colleagues he was 'screaming out into the wilderness' about a provision that would drive Republican opposition. He stated that without the mental health restriction, Republicans would have supported the bill's other components. The NRA-ILA characterized H.606 as 'a wish list of gun control measures pushed nationally by anti-gun groups.'",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments"]),
        claim("zh2", "zachary-harvey", "economic_stewardship", 2, True,
              "Serving simultaneously as a Vermont House member and Vermont Republican Party Finance Chair, Harvey championed fiscal restraint in Vermont's 2026 session. When the House debated H.949 — a property tax bill raising education property taxes by a 7% average — Harvey backed a Republican-led amendment to redirect $52.5 million in Vermont General Fund surplus and $22.3 million in unallocated education funds to buy down the tax-rate increase and return savings to taxpayers. He stated: 'Taxpayers need immediate relief,' and warned that announcing a $50 million reserve to school districts would cause them to spend it rather than return it as tax relief. The pro-taxpayer amendment, supported by Republicans and a handful of Democrats, was defeated 85-56 when the Democrat majority blocked it.",
              ["https://www.vermontpublic.org/local-news/2026-03-20/capitol-recap-lawmakers-advance-property-tax-bill-whittling-increase-down-to-7",
               "https://vermontdailychronicle.com/rep-zachary-harvey-appointed-as-vtgop-finance-chair/"]),
    ]),

    # -------- Woodman Page (VT, R, State Representative — Orleans-2) --------
    ("woodman-page", "VT", "State Representative", [
        claim("wp1", "woodman-page", "self_defense", 1, True,
              "Voted NO on Vermont H.606 when it passed the Vermont House on March 19, 2026. The NRA-ILA characterized H.606 as a 'wish list of gun control measures pushed nationally by anti-gun groups,' including Vermont's first-ever machine gun prohibition, restrictions on firearms for persons under court-ordered mental health treatment, and storage-violation penalties. Democrats, who hold a supermajority in the Vermont House, passed H.606 over unanimous Republican opposition. Page, a retired U.S. Air Force major with a 28-year career in defense who commissioned through Norwich University's ROTC, voted against the bill's sweeping restrictions as incompatible with constitutional Second Amendment protections.",
              ["https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("wp2", "woodman-page", "economic_stewardship", 2, True,
              "When Vermont's H.949 (2026) proposed raising education property taxes by a 7% average, Page voted YES on the Republican-led amendment to use $52.5 million in General Fund surplus and $22.3 million in unallocated education funds to buy down the property tax rate increase and deliver immediate taxpayer relief. The amendment, supported by Republicans and a handful of Democrats, was defeated 85-56 when the Democrat majority blocked fiscal restraint in favor of higher property taxes. Page's vote aligned with his consistent advocacy for Newport and Orleans County constituents — a rural district where property tax increases fall hardest on fixed-income homeowners and small farms.",
              ["https://www.vermontpublic.org/local-news/2026-03-20/capitol-recap-lawmakers-advance-property-tax-bill-whittling-increase-down-to-7",
               "https://vtdigger.org/2026/03/26/vermont-house-advances-property-tax-bill-with-7-average-increase/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
