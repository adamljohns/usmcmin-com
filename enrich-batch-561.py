#!/usr/bin/env python3
"""Enrichment batch 561: 4 WA State Representatives, 10 claims.

Targets archetype_party_default state legislators from Washington (WA) — the
next bottom-of-alphabet state after WY/WV/WI. All federal archetype_curated
slots are exhausted; this batch continues with WA state-level officials.

Candidates (all WA, D, 'State Representative'):
  Shelley Kloba (WA-01, Kirkland)
  Sharon Wylie (WA-49, Clark County)
  Sharon Tomiko Santos (WA-37, South Seattle)
  Roger Goodman (WA-45, Kirkland/Sammamish)
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
    # -------- Shelley Kloba (WA-01, D, State Representative) --------
    ("shelley-kloba", "WA", "State Representative", [
        claim("sk1", "shelley-kloba", "self_defense", 1, False,
              "A named co-sponsor of HB 1240 (2023), which banned the manufacture, importation, distribution, and sale of assault weapons in Washington State, prohibiting more than 50 specific firearm models including AR-15s and AK-47s. The House passed the bill 55-42 on March 8, 2023; Gov. Inslee signed it April 25, 2023, making Washington the 10th state to enact such a ban.",
              ["https://wa-law.org/bill/2023-24/hb/1240/",
               "https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://gunresponsibility.org/media-center/washington-state-legislature-passes-hb-1240-to-prohibit-the-sale-of-assault-rifles/"]),
        claim("sk2", "shelley-kloba", "sanctity_of_life", 4, False,
              "Received a 2024 endorsement from Planned Parenthood Alliance Advocates, which explicitly requires endorsed candidates to affirm support for abortion access and reproductive health care including abortion. Listed among Washington's officially endorsed candidates.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements",
               "https://prochoicewashington.org/elections-legislation/endorsed-candidates/"]),
        claim("sk3", "shelley-kloba", "border_immigration", 2, False,
              "Co-sponsored HB 2173 (2025-26 session) requiring law enforcement — including federal ICE agents — to remain visibly identifiable during operations, a bill explicitly motivated by ICE enforcement activities. In February 2026 she published a public statement calling federal immigration enforcement 'dangerous, aggressive, and illegal' and advocated Washington protect undocumented immigrants from federal enforcement action.",
              ["https://app.leg.wa.gov/BillSummary/?BillNumber=2173&Chamber=House&Year=2025",
               "https://housedemocrats.wa.gov/kloba/2026/02/20/standing-up-against-fear-and-division/"]),
    ]),

    # -------- Sharon Wylie (WA-49, D, State Representative) --------
    ("sharon-wylie", "WA", "State Representative", [
        claim("sw1", "sharon-wylie", "family_child_sovereignty", 0, False,
              "Voted yes on ESSB 5599 (April 2023), which allows licensed youth shelters to notify the state DCYF instead of parents when a runaway minor seeks gender-affirming care or reproductive health services, effectively removing parental notification rights over a child's location and medical decisions. The bill passed the House 57-39 entirely on party lines — every Democrat yes, every Republican no.",
              ["https://open.pluralpolicy.com/vote/d8d944c8-ea87-469d-b442-390d8d8a53f2/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023&Initiative=false",
               "https://komonews.com/news/local/senate-bill-5599-washington-state-transgender-trans-at-risk-youth-gender-affirming-reproductive-care-without-parental-consent-governor-jay-inslee-family-foster-homeless-children-families-minors-law-legislation"]),
        claim("sw2", "sharon-wylie", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), which requires Washington residents to obtain a government-issued permit before purchasing any firearm, establishing a mandatory live-fire training requirement and creating a government database of firearm purchasers. The NRA described it as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false",
               "https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://www.nrahlf.org/articles/2025/4/18/nra-alerts-gun-owners-as-washington-state-senate-passes-permit-to-purchase-bill/"]),
        claim("sw3", "sharon-wylie", "biblical_marriage", 4, False,
              "Voted yes on HB 1296 (2025), the Democratic overhaul of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), stripping parental notification rights over transgender-related student health decisions and removing parental access to student medical records. The bill passed 56-37 along party lines; Gov. Ferguson signed it May 20, 2025. Wylie recorded a public video statement supporting the bill.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://m.youtube.com/watch?v=ufmADhgBtPo"]),
    ]),

    # -------- Sharon Tomiko Santos (WA-37, D, State Representative) --------
    ("sharon-tomiko-santos", "WA", "State Representative", [
        claim("sts1", "sharon-tomiko-santos", "family_child_sovereignty", 0, False,
              "As House Education Committee Chair, Santos was the floor manager for HB 1296 (2025), which Democrats used to gut Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), removing parental notification rights over children's medical services in schools including transgender-related health decisions. She personally asked representatives to 'concur on the Senate amendments' in the final passage push. The bill passed 59-39 along party lines; signed May 2025. A conservative legal group subsequently filed suit to block the law.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://washingtonstatestandard.com/2025/10/24/conservative-group-sues-to-overturn-rewrite-of-wa-parental-rights-law/"]),
        claim("sts2", "sharon-tomiko-santos", "sanctity_of_life", 0, False,
              "A co-sponsor of HB 1469 (2023), which shielded abortion providers and gender-affirming care practitioners from medical licensing board accountability, including for services rendered to out-of-state patients seeking care in Washington. The bill became Chapter 193, 2023 Laws; effective April 27, 2023.",
              ["https://legiscan.com/WA/bill/HB1469/2023",
               "https://wa-law.org/bill/2023-24/hb/1469/",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1469&Chamber=House&Year=2023"]),
    ]),

    # -------- Roger Goodman (WA-45, D, State Representative) --------
    ("roger-goodman", "WA", "State Representative", [
        claim("rg1", "roger-goodman", "self_defense", 1, False,
              "Signed the House Civil Rights & Judiciary Committee majority report advancing HB 1240 (2023), the assault-weapons ban that outlawed the manufacture, importation, distribution, and sale of semi-automatic 'assault weapons' in Washington State, banning more than 50 specific models. Also listed as a co-sponsor. Gov. Inslee signed it April 25, 2023.",
              ["https://wa-law.org/bill/2023-24/hb/1240/1/",
               "https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://gunresponsibility.org/media-center/washington-state-legislature-passes-hb-1240-to-prohibit-the-sale-of-assault-rifles/"]),
        claim("rg2", "roger-goodman", "sanctity_of_life", 0, False,
              "A listed co-sponsor of HB 1469 (2023), shielding abortion providers and gender-affirming care practitioners from medical licensing board accountability for services rendered in Washington, including to patients crossing state lines seeking care. The bill became Chapter 193, 2023 Laws; effective April 27, 2023.",
              ["https://legiscan.com/WA/bill/HB1469/2023",
               "https://wa-law.org/bill/2023-24/hb/1469/"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
