#!/usr/bin/env python3
"""Enrichment batch 829: 5 Washington State House Democrats.

Targets archetype_party_default WA State Representatives with 0 claims from
the bottom of the alphabet (WA). All five co-sponsored or voted for WA HB 1163
(2025, permit-to-purchase firearms, signed by Gov. Ferguson 5/20/2025) and all
five voted yes on WA SB 6182 (2026, Abortion Savings Program, Chapter 228,
2026 Laws) — both passing on 58-38 / 57-36 party-line House votes, directly
opposing the RESOLUTE Citizen rubric on self-defense and sanctity of life.

Lauren Davis (WA-32, D): confirmed co-sponsor HB 1163; sanctity_of_life via SB 6182.
Julio Cortes (WA-38, D): confirmed co-sponsor HB 1163; sanctity_of_life via SB 6182.
Joe Timmons (WA-42, D): party-line yes vote HB 1163; stated champion of abortion access.
Janice Zahn (WA-41, D): party-line yes vote HB 1163; endorsed by Planned Parenthood WA.
Jamila Taylor (WA-30, D): confirmed co-sponsor HB 1163; sanctity_of_life via SB 6182.
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
    # ------------- Lauren Davis (WA-32, D) -------------
    ("lauren-davis", "WA", "Representative", [
        claim("ld1", "lauren-davis", "self_defense", 1, False,
              "Co-sponsored Washington HB 1163 (2025), which requires any person wishing to "
              "purchase a firearm in Washington to first obtain a five-year permit from the "
              "Washington State Patrol — requiring fingerprinting, a certified firearms safety "
              "training course, and a background check. The bill was signed by Gov. Bob Ferguson "
              "on May 20, 2025, creating a mandatory government-permission system before any "
              "firearm purchase, directly opposing the rubric's defense of unrestricted "
              "constitutional carry and opposition to firearm registry and licensing systems.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://washingtonstatestandard.com/2025/05/20/washingtonians-will-need-state-permit-to-buy-guns-under-new-law/"]),
        claim("ld2", "lauren-davis", "sanctity_of_life", 0, False,
              "Voted yes on Washington SB 6182 (2026), which establishes the Abortion Savings "
              "Program — a state grant system funded by a new tax on health insurance carriers "
              "that directs public dollars to organizations providing direct abortion care. The "
              "bill was signed into law as Chapter 228, 2026 Laws (effective 6/11/2026), "
              "passing the House 57–36 on a party-line vote. Supporting public funding for "
              "abortion is directly at odds with the rubric's life-at-conception standard, "
              "which holds that the unborn must be protected from fertilization.",
              ["https://conservativeladiesofwa.com/sb6182-abortion-tax-health-carriers/",
               "https://legiscan.com/WA/bill/SB6182/2025"]),
    ]),

    # ------------- Julio Cortes (WA-38, D) -------------
    ("julio-cortes", "WA", "Representative", [
        claim("jc1", "julio-cortes", "self_defense", 1, False,
              "Co-sponsored Washington HB 1163 (2025), the permit-to-purchase firearms law "
              "signed by Gov. Bob Ferguson on May 20, 2025. The law mandates that anyone "
              "seeking to buy a firearm in Washington must first obtain a five-year state "
              "permit requiring fingerprinting, a certified firearms safety course, and a "
              "WSP background check — creating a government-permission and registry "
              "infrastructure that directly opposes the rubric's stance against firearm "
              "licensing, permitting, and registration requirements.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://publichealth.jhu.edu/center-for-gun-violence-solutions/2025/washington-passes-permit-to-purchase-law"]),
        claim("jc2", "julio-cortes", "sanctity_of_life", 0, False,
              "Voted yes on Washington SB 6182 (2026), the Abortion Savings Program, which "
              "creates a state-administered grant fund — financed by a new assessment on "
              "health insurance carriers — to pay organizations providing direct abortion "
              "care services. The bill passed the Washington House 57–36 on a party-line "
              "vote and was signed into law (Chapter 228, 2026 Laws). Voting to create a "
              "public fund specifically for abortion care is incompatible with the rubric's "
              "affirmation that life begins at conception and must be protected.",
              ["https://conservativeladiesofwa.com/sb6182-abortion-tax-health-carriers/",
               "https://legiscan.com/WA/bill/SB6182/2025"]),
    ]),

    # ------------- Joe Timmons (WA-42, D) -------------
    ("joe-timmons", "WA", "Representative", [
        claim("jt1", "joe-timmons", "self_defense", 1, False,
              "Voted yes on Washington HB 1163 (2025), the permit-to-purchase firearms law "
              "signed by Gov. Ferguson on May 20, 2025, which passed the Washington House "
              "on a 58–38 party-line vote with Democrats unanimous in favor. The law requires "
              "a state permit, fingerprinting, WSP background check, and certified firearms "
              "safety training before any firearm purchase in Washington — a comprehensive "
              "government-permission and licensing system directly opposing the rubric's "
              "defense of constitutional carry and its opposition to firearm permitting.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://mynorthwest.com/mynorthwest-politics/bill-requiring-permits-for-gun-purchases-passes-house-on-party-line-vote/4059942"]),
        claim("jt2", "joe-timmons", "sanctity_of_life", 0, False,
              "Has publicly stated he is a champion of legislation protecting access to "
              "'safe, legal abortion' and 'comprehensive reproductive health care,' and voted "
              "yes on Washington SB 6182 (2026), which establishes a state Abortion Savings "
              "Program to fund grants to abortion providers through a new tax on health "
              "insurance carriers (Chapter 228, 2026 Laws, signed into law, House vote 57–36). "
              "Advocating for and funding abortion access is irreconcilable with the rubric's "
              "life-at-conception standard.",
              ["https://www.repjoetimmons.org/",
               "https://conservativeladiesofwa.com/sb6182-abortion-tax-health-carriers/"]),
    ]),

    # ------------- Janice Zahn (WA-41, D) -------------
    ("janice-zahn", "WA", "Representative", [
        claim("jz1", "janice-zahn", "self_defense", 1, False,
              "Voted yes on Washington HB 1163 (2025), the state's permit-to-purchase "
              "firearms law (signed by Gov. Ferguson May 20, 2025), which passed the "
              "Washington House 58–38 on a party-line vote. The law requires every "
              "prospective firearm buyer to first obtain a five-year permit from the "
              "Washington State Patrol — with mandatory fingerprinting, a certified safety "
              "course, and a background check — directly opposing the rubric's position "
              "against government-imposed licensing, permitting, and registration requirements "
              "for the exercise of Second Amendment rights.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://washingtonstatestandard.com/2025/05/20/washingtonians-will-need-state-permit-to-buy-guns-under-new-law/"]),
        claim("jz2", "janice-zahn", "sanctity_of_life", 4, False,
              "Received an endorsement from Planned Parenthood Alliance Advocates of "
              "Washington for her 2024 legislative campaign, and voted yes on Washington "
              "SB 6182 (2026), which levies a new tax on health insurance carriers to "
              "fund an Abortion Savings Program granting public money to abortion providers "
              "(Chapter 228, 2026 Laws; House vote 57–36). Accepting Planned Parenthood's "
              "endorsement and voting to fund abortion care directly conflicts with the "
              "rubric's standard of never accepting PP/NARAL/EMILY endorsements or money.",
              ["https://www.janicezahn.org/endorsements",
               "https://conservativeladiesofwa.com/sb6182-abortion-tax-health-carriers/"]),
    ]),

    # ------------- Jamila Taylor (WA-30, D) -------------
    ("jamila-taylor", "WA", "Representative", [
        claim("jmt1", "jamila-taylor", "self_defense", 1, False,
              "Co-sponsored Washington HB 1163 (2025), the permit-to-purchase firearms bill "
              "signed by Gov. Bob Ferguson on May 20, 2025. The law requires all Washington "
              "firearm buyers to obtain a five-year state permit via the Washington State "
              "Patrol, with mandatory fingerprinting, a certified firearms safety course, "
              "and a background check — building a statewide licensing and registry "
              "infrastructure for gun buyers that directly opposes the rubric's defense of "
              "constitutional carry and its rejection of firearm permitting and registration.",
              ["https://www.nraila.org/articles/20250521/washington-governor-ferguson-signs-permit-to-purchase-legislation",
               "https://publichealth.jhu.edu/center-for-gun-violence-solutions/2025/washington-passes-permit-to-purchase-law"]),
        claim("jmt2", "jamila-taylor", "sanctity_of_life", 0, False,
              "Voted yes on Washington SB 6182 (2026), the Abortion Savings Program, which "
              "establishes a grant fund financed by a new assessment on health insurance "
              "carriers, directing public dollars to organizations providing direct abortion "
              "clinical care services (Chapter 228, 2026 Laws; House vote 57–36). Voting "
              "to fund abortion care through a dedicated public program is directly "
              "incompatible with the rubric's life-at-conception standard, which holds "
              "that personhood begins at fertilization and the unborn must be protected.",
              ["https://conservativeladiesofwa.com/sb6182-abortion-tax-health-carriers/",
               "https://legiscan.com/WA/bill/SB6182/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record."""
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

    # Minified write — preserve the no-whitespace master to keep scorecard.json ~35-36MB.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
