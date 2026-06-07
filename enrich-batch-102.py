#!/usr/bin/env python3
"""Enrichment batch 102: hand-curated claims for 4 federal candidates.

Targets archetype_party_default U.S. Representatives running for Senate (2026),
taken from the bottom of the alphabet (WY, KY, OK, IA). All are sitting
members of Congress with documented voting records from reliable public sources.

Mix (4 R): Harriet Hageman (WY), Andy Barr (KY), Kevin Hern (OK),
Ashley Hinson (IA). Each claim cites >=1 reliable source and reflects
2024-2026 voting record / public positions.

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
    # ----------- Harriet Hageman (WY-AL Rep, 2026 Senate candidate) -----------
    ("harriet-hageman", "WY", "Representative", [
        claim("hh1", "harriet-hageman", "sanctity_of_life", 0, True,
              "A consistent pro-life voter who has voted for the Born Alive Survivors Protection Act and against any taxpayer funding of abortion; in January 2026 she sponsored legislation to revoke the tax-exempt status of organizations that provide or fund abortions — affirming that unborn life deserves legal protection from conception.",
              ["https://hageman.house.gov/media/press-releases",
               "https://sbaprolife.org/representative/harriet-hageman"]),
        claim("hh2", "harriet-hageman", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023, which mandates border-wall completion, tightens asylum standards, and adds enforcement personnel. Also cosponsored the SAVE Act (H.R. 8281) requiring in-person proof of citizenship for federal-election voter registration, and opposed every continuing resolution that did not include border-security concessions.",
              ["https://hageman.house.gov/media/press-releases/hageman-votes-end-invasion-americas-southern-border",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281"]),
        claim("hh3", "harriet-hageman", "economic_stewardship", 2, True,
              "A Freedom Caucus member who has repeatedly voted NO on continuing resolutions that fail to rein in government spending, objecting to deficit-funded status-quo budgets; supports hard spending caps and structural budget balance before signing off on government funding.",
              ["https://hageman.house.gov/media/press-releases/hageman-votes-no-continuing-resolution-fails-rein-government-spending-or",
               "https://en.wikipedia.org/wiki/Harriet_Hageman"]),
    ]),

    # --------------- Andy Barr (KY-06 Rep, 2026 R Senate nominee) ---------------
    ("andy-barr", "KY", "Representative", [
        claim("ab1", "andy-barr", "sanctity_of_life", 0, True,
              "Holds a consistent anti-abortion record, stating that abortion should be illegal in all circumstances except to save the mother's life; opposes all federal funding for organizations that perform abortions and has voted to defund Planned Parenthood.",
              ["https://en.wikipedia.org/wiki/Andy_Barr",
               "https://sbaprolife.org/representative/andy-barr"]),
        claim("ab2", "andy-barr", "economic_stewardship", 2, True,
              "A longtime cosponsor of a Balanced Budget Amendment to the Constitution; voted for the largest mandatory-spending cuts ever proposed in Congress and reintroduced the bipartisan Fiscal State of the Nation Act to require annual public reporting on the nation's fiscal health as the national debt approached $40 trillion.",
              ["https://barr.house.gov/spending-and-debt",
               "https://barr.house.gov/2026/1/barr-reintroduces-bipartisan-bill-to-strengthen-oversight-of-government-spending"]),
        claim("ab3", "andy-barr", "border_immigration", 1, True,
              "Publicly states that all illegal immigrants must be deported and that U.S. resources should not be spent housing them in 'luxury hotels'; supports mandatory deportation and a fully closed border as non-negotiable policy positions.",
              ["https://ballotpedia.org/Andy_Barr",
               "https://barr.house.gov/"]),
    ]),

    # ------------ Kevin Hern (OK-01 Rep, former RSC Chair, Senate candidate) ------------
    ("kevin-hern", "OK", "Representative", [
        claim("kh1", "kevin-hern", "sanctity_of_life", 0, True,
              "Introduced H.R. 384, the Protecting Life from Chemical Abortions Act, to roll back the FDA's loosened dispensing rules for the abortion drug mifepristone; has consistently voted to block taxpayer funding of abortion domestically and internationally and to protect conscience rights for pro-life healthcare workers.",
              ["https://hern.house.gov/",
               "https://sbaprolife.org/representative/kevin-hern"]),
        claim("kh2", "kevin-hern", "economic_stewardship", 2, True,
              "As Republican Study Committee Chair (2023-24), authored the FY2024 RSC budget that would balance the federal budget in seven years through $16.3 trillion in spending cuts over 10 years — one of the most aggressive deficit-reduction plans ever released by a House caucus; has said the first step on the debt is simply to 'stop adding to it.'",
              ["https://hern.house.gov/news/documentsingle.aspx?DocumentID=849",
               "https://en.wikipedia.org/wiki/Kevin_Hern"]),
        claim("kh3", "kevin-hern", "border_immigration", 0, True,
              "Voted for H.R. 2 (Secure the Border Act of 2023) mandating border-wall construction and military support for enforcement; the RSC budget he authored included dedicated border-security appropriations, E-Verify mandates, and a framework for deploying military resources to stop illegal crossings.",
              ["https://hern.house.gov/",
               "https://govtrack.us/congress/members/kevin_hern/412748"]),
    ]),

    # ------------ Ashley Hinson (IA-02 Rep, 2026 R Senate nominee, Ernst seat) ------------
    ("ashley-hinson", "IA", "Representative", [
        claim("ah1", "ashley-hinson", "sanctity_of_life", 0, True,
              "Received an A+ on SBA Pro-Life America's National Pro-Life Scorecard; states she is 'pro-life and pro-family,' opposes all taxpayer funding of abortion providers, and affirms that life must be protected from conception — opposing any federal legislation that would codify abortion on demand.",
              ["https://hinson.house.gov/media/press-releases/hinson-receives-sba-pro-life-scorecard",
               "https://sbaprolife.org/representative/ashley-hinson"]),
        claim("ah2", "ashley-hinson", "self_defense", 1, True,
              "Named to the National Shooting Sports Foundation's Dean's List for her work protecting Second Amendment rights; publicly opposed Biden-era gun-control measures as unconstitutional, calling the right to keep and bear arms foundational while the left 'continues to twist and undermine the Second Amendment.'",
              ["https://hinson.house.gov/media/press-releases/hinson-recognized-protecting-second-amendment-rights",
               "https://en.wikipedia.org/wiki/Ashley_Hinson"]),
        claim("ah3", "ashley-hinson", "border_immigration", 1, True,
              "Voted against the 2024 bipartisan mass-amnesty bill; advocated for stronger border security and immigration enforcement during House Appropriations Committee markups; and voted for the One Big Beautiful Bill Act (OBBBA) with its sweeping immigration enforcement provisions.",
              ["https://hinson.house.gov/media/press-releases/hinson-votes-against-mass-amnesty-illegal-immigrants-urges-focus-fixing-border",
               "https://en.wikipedia.org/wiki/Ashley_Hinson"]),
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
