#!/usr/bin/env python3
"""Enrichment batch 81: hand-curated claims for 4 federal/national-level candidates.

Targets archetype_curated federal-level candidates with 0 evidence claims taken from
the bottom of the alphabet (US, CA, TX). Mix: Mac Warner (US-R, Acting AAG),
Donald J. Trump (US-R, President), Katie Porter (CA-D, former US Rep / Gov candidate),
Eric Johnson (TX-R, Dallas Mayor who switched from D).

Each claim cites >= 1 reliable source and reflects 2024-2026 voting record /
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
    # ---------------- Mac Warner (US-R, Acting AAG / former WV Secretary of State) ----------------
    ("mac-warner", "US", "Secretary of State", [
        claim("mw1", "mac-warner", "election_integrity", 0, True,
              "As West Virginia Secretary of State (2017-2025), Warner consistently opposed automatic voter registration, same-day voter registration, and mail-in voting expansion. In March 2023 he withdrew West Virginia from the ERIC interstate voter-registration database, citing data-sharing and accuracy concerns — a firm voter-ID and anti-mass-mail-in posture matching the rubric standard.",
              ["https://en.wikipedia.org/wiki/Mac_Warner",
               "https://ballotpedia.org/Mac_Warner"]),
        claim("mw2", "mac-warner", "refuse_federal_overreach", 0, True,
              "Warner sided with Ohio's Secretary of State in the 2018 U.S. Supreme Court case Husted v. A. Philip Randolph Institute, defending states' sovereign authority to purge inactive voters from rolls — upholding state control over elections against expansive federal mandates.",
              ["https://en.wikipedia.org/wiki/Mac_Warner",
               "https://ballotpedia.org/Mac_Warner"]),
    ]),

    # ---------------- Donald J. Trump (US-R, President) ----------------
    ("donald-j-trump", "US", "President", [
        claim("djt1", "donald-j-trump", "economic_stewardship", 0, True,
              "On January 23, 2025, President Trump signed the executive order 'Strengthening American Leadership in Digital Financial Technology,' which explicitly prohibits federal agencies from establishing, issuing, or promoting a central bank digital currency (CBDC) within the United States or abroad — directly fulfilling the rubric's anti-CBDC standard.",
              ["https://www.whitehouse.gov/presidential-actions/2025/01/strengthening-american-leadership-in-digital-financial-technology/",
               "https://www.cfodive.com/news/trump-crypto-executiveorder-bars-agencies-cbdcs-federalreserve-stablecoins/738292/"]),
        claim("djt2", "donald-j-trump", "border_immigration", 0, True,
              "On Day 1 (January 20, 2025), Trump signed the 'Securing Our Borders' executive order directing military resources and physical border wall construction. The One Big Beautiful Bill Act (signed July 4, 2025) then allocated $46.5 billion specifically for border wall construction, fulfilling the rubric's wall-plus-military enforcement standard.",
              ["https://www.whitehouse.gov/presidential-actions/2025/01/securing-our-borders/",
               "https://www.idga.org/federal/articles/trumps-2025-executive-orders-reshaping-the-southern-border"]),
        claim("djt3", "donald-j-trump", "self_defense", 1, True,
              "On February 7, 2025, Trump signed Executive Order 14206 'Protecting Second Amendment Rights,' directing the Attorney General to review all Biden-era firearm regulations and deliver a plan to eliminate any infringements on Second Amendment rights — opposing red-flag law frameworks, assault-weapon restrictions, and registry schemes the rubric flags.",
              ["https://www.whitehouse.gov/fact-sheets/2025/02/fact-sheet-president-donald-j-trump-is-protecting-americans-second-amendment-rights/",
               "https://www.nraila.org/articles/20250207/nra-statement-on-president-trump-s-executive-order-protecting-second-amendment-rights"]),
    ]),

    # ---------------- Katie Porter (CA-D, former US Rep / 2026 CA Gov candidate) ----------------
    ("katie-porter-gov", "CA", "Governor", [
        claim("kp1", "katie-porter-gov", "sanctity_of_life", 4, False,
              "Porter earned a 100 percent rating on the 2024 congressional scorecard from Reproductive Freedom for All (the renamed NARAL Pro-Choice America) and received NARAL's endorsement — placing her squarely inside the abortion-industry endorsement network the rubric's question 4 opposes.",
              ["https://reproductivefreedomforall.org/lawmaker/katie-porter/",
               "https://reproductivefreedomforall.org/news/naral-pro-choice-america-celebrates-katie-porters-victory-in-californias-47th-congressional-district/"]),
        claim("kp2", "katie-porter-gov", "sanctity_of_life", 0, False,
              "Throughout her congressional career (CA-45 and CA-47, 2019-2025) and her 2026 California gubernatorial campaign, Porter has opposed any personhood-from-conception standard, supported codifying Roe v. Wade into federal law, and opposed the Supreme Court's Dobbs ruling overturning Roe.",
              ["https://en.wikipedia.org/wiki/Katie_Porter",
               "https://ballotpedia.org/Katie_Porter"]),
        claim("kp3", "katie-porter-gov", "biblical_marriage", 4, False,
              "Porter cosponsored and voted for the Equality Act (H.R. 5) in both 2019 and 2021, legislation that would enshrine sexual orientation and gender identity as federal civil-rights protected classes, extending those protections into public schools and workplaces — the promotion of LGBTQ ideology in schools and policy that the rubric's question 4 opposes.",
              ["https://en.wikipedia.org/wiki/Katie_Porter",
               "https://ballotpedia.org/Katie_Porter"]),
    ]),

    # ---------------- Eric Johnson (TX-R, Mayor of Dallas) ----------------
    ("eric-johnson-mayor", "TX", "Mayor", [
        claim("ej1", "eric-johnson-mayor", "public_justice", 0, True,
              "In September 2023 Johnson publicly switched from Democrat to Republican, explicitly citing support for police funding as a primary motivation: progressive protesters outside his home called for defunding the police while Republican officials were the ones who offered solidarity. As Dallas mayor he made public safety and policing a top priority, opposing the 'defund the police' movement.",
              ["https://en.wikipedia.org/wiki/Eric_Johnson_(Texas_politician)",
               "https://news.ballotpedia.org/2023/09/27/dallas-mayor-is-third-big-city-mayor-to-switch-parties-since-2016/"]),
        claim("ej2", "eric-johnson-mayor", "economic_stewardship", 2, True,
              "Johnson cited low property taxes as a core reason for his September 2023 party switch to Republican, signaling a fiscal-restraint and anti-tax-increase orientation consistent with the rubric's balanced-budget and anti-deficit standard.",
              ["https://en.wikipedia.org/wiki/Eric_Johnson_(Texas_politician)",
               "https://ballotpedia.org/Eric_Johnson_(Texas)"]),
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
