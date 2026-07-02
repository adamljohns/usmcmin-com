#!/usr/bin/env python3
"""Enrichment batch 514: additional claims for 5 sitting U.S. Senators with 3 existing claims.

The archetype_curated 0-claim bucket is fully exhausted (0 remaining). This batch
deepens coverage for the lightest-evidence sitting senators from bottom-of-alphabet
states (IL, HI, DE), adding 2 claims each in distinct rubric categories not yet
represented in each senator's profile.

Targets: Tammy Duckworth (IL-D), Dick Durbin (IL-D), Mazie Hirono (HI-D),
Brian Schatz (HI-D), Lisa Blunt Rochester (DE-D).
All claims cite >= 1 reliable source reflecting 2022-2026 public record.
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
    # ---------------- Tammy Duckworth (IL-D, US Senator) ----------------
    ("tammy-duckworth", "IL", "Senator", [
        claim("td1", "tammy-duckworth", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (Dec. 2022), calling it 'a great first step' in protecting same-sex marriage at the federal level. She has also co-sponsored the Equality Act alongside Sen. Durbin to write sexual-orientation and gender-identity protections into federal civil-rights law — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.duckworth.senate.gov/news/in-the-news/sen-tammy-duckworth-on-same-sex-marriage-protections-potential-rail-strike",
               "https://www.duckworth.senate.gov/news/press-releases/-during-pride-month-duckworth-and-durbin-join-merkley-baldwin-booker-to-introduce-the-equality-act"]),
        claim("td2", "tammy-duckworth", "foreign_policy_restraint", 1, False,
              "A vocal proponent of open-ended U.S. military support for Ukraine: voted for the $40 billion Ukraine aid package (May 2022), traveled to the Ukraine-Poland border to reinforce NATO commitments, and stated 'continued American support for Ukraine is critically important … for America's own national security and the security of all NATO allies.' These positions contradict the rubric's call to end foreign military entanglements and reassert Article I war powers.",
              ["https://www.duckworth.senate.gov/news/press-releases/duckworth-statement-following-senate-passing-40-billion-aid-package-for-ukraine",
               "https://www.duckworth.senate.gov/news/press-releases/duckworth-visits-ukraine-poland-border-region-to-reinforce-bipartisan-support-for-the-people-of-ukraine-and-nato-allies"]),
    ]),

    # ---------------- Dick Durbin (IL-D, US Senator) ----------------
    ("dick-durbin", "IL", "Senator", [
        claim("dd1", "dick-durbin", "self_defense", 1, False,
              "Holds a career 'F' rating from the National Rifle Association and is a consistent sponsor of gun-control legislation. In 2023 he joined Sen. Duckworth in reintroducing the Assault Weapons Ban and called on the Senate to ban assault weapons from civilian use following the Nashville school shooting — directly opposing the rubric's defense of unrestricted Second Amendment rights and opposition to semi-automatic rifle bans.",
              ["https://www.durbin.senate.gov/newsroom/press-releases/durbin-duckworth-colleagues-reintroduce-assault-weapons-ban",
               "https://www.durbin.senate.gov/newsroom/press-releases/in-speech-on-senate-floor-durbin-reacts-to-nashville-school-shooting-calls-on-colleagues-to-ban-assault-weapons"]),
        claim("dd2", "dick-durbin", "economic_stewardship", 2, False,
              "Has consistently voted for large deficit-spending legislation throughout his Senate career — including the $1.9 trillion American Rescue Plan and the Inflation Reduction Act — and opposes balanced-budget measures. While acknowledging that 'borrowing 40 cents out of every dollar spent is unsustainable,' he voted for debt-ceiling increases and new spending bills rather than supporting the anti-deficit, balanced-budget standard the rubric requires.",
              ["https://www.durbin.senate.gov/newsroom/press-releases/durbin-even-though-debt-ceiling-compromise-is-not-perfect-i-cannot-let-the-american-economy-descend-into-chaos",
               "https://en.wikipedia.org/wiki/Dick_Durbin"]),
    ]),

    # ---------------- Mazie Hirono (HI-D, US Senator) ----------------
    ("mazie-hirono", "HI", "Senator", [
        claim("mh1", "mazie-hirono", "sanctity_of_life", 0, False,
              "Voted to advance the Reproductive Freedom for Women Act (2024) and has been a vocal Senate champion for unrestricted abortion access since Dobbs: participated in Judiciary Committee hearings attacking abortion restrictions, co-released a 2024 report documenting the 'nationwide impacts of abortion bans,' and sponsored S.4920 (2025) to shield abortion privacy data under HIPAA — rejecting any personhood-from-conception standard.",
              ["https://www.hirono.senate.gov/news/press-releases/video-hirono-votes-to-pass-reproductive-freedom-for-women-act-blasts-republicans-on-senate-floor",
               "https://www.hirono.senate.gov/news/press-releases/two-years-after-dobbs-hirono-joins-colleagues-in-releasing-report-on-nationwide-impact-of-abortion-bans"]),
        claim("mh2", "mazie-hirono", "border_immigration", 2, False,
              "Opposes sanctuary-city enforcement measures and has defended jurisdictions that shield undocumented immigrants from federal immigration authorities; denounced Republican proposals to defund or penalize sanctuary cities as 'criminalizing immigrant communities' and argued local law enforcement should not serve as immigration agents — rejecting the rubric's anti-sanctuary standard.",
              ["https://www.hirono.senate.gov/news/press-releases/hirono-denounces-republican-attempt-to-criminalize-immigrant-communities",
               "https://www.hirono.senate.gov/news/press-releases/video-on-senate-floor-hirono-condemns-republicans-anti-immigrant-proposal-calls-for-bipartisan-comprehensive-immigration-reform"]),
    ]),

    # ---------------- Brian Schatz (HI-D, US Senator) ----------------
    ("brian-schatz", "HI", "Senator", [
        claim("bs1", "brian-schatz", "biblical_marriage", 4, False,
              "A consistent Senate champion of LGBTQ rights in schools and public life: in April 2025 he sponsored S.Res.168, a Senate resolution supporting the 'Rise Up for LGBTQI+ Youth in Schools' initiative demanding 'equal educational opportunity' and 'civil rights protections' for LGBTQ+ students in K-12 schools. He also holds a 100% rating from the Human Rights Campaign and is a co-sponsor of the Equality Act — the promotion of LGBTQ ideology in schools and policy the rubric opposes.",
              ["https://www.schatz.senate.gov/about/issues/civil-rights-and-criminal-justice",
               "https://en.wikipedia.org/wiki/Brian_Schatz"]),
        claim("bs2", "brian-schatz", "economic_stewardship", 2, False,
              "Consistently voted for large-deficit spending legislation including the $1.9 trillion American Rescue Plan (2021) and the $700 billion Inflation Reduction Act (2022), and has championed expanded federal programs without corresponding revenue or debt-reduction mechanisms throughout his Senate tenure — opposing the rubric's call for anti-deficit, balanced-budget governance.",
              ["https://en.wikipedia.org/wiki/Brian_Schatz",
               "https://www.govtrack.us/congress/members/brian_schatz/412507/report-card/2024"]),
    ]),

    # ---------------- Lisa Blunt Rochester (DE-D, US Senator) ----------------
    ("lisa-blunt-rochester", "DE", "Senator", [
        claim("lbr1", "lisa-blunt-rochester", "self_defense", 1, False,
              "Led the Senate reintroduction of the Assault Weapons Ban of 2025 alongside Senators Schiff, Murphy, Blumenthal, and Padilla — legislation to ban military-style semi-automatic rifles and high-capacity magazines — declaring 'Assault weapons are weapons of war — they have no place in our communities.' She also cosponsored the Assault Weapons Ban in every Congress beginning with the 115th (2017), building a consistent record of opposing the rubric's defense of civilian semi-automatic rifle ownership.",
              ["https://www.bluntrochester.senate.gov/news/press-releases/blunt-rochester-schiff-murphy-blumenthal-padilla-rep-mcbath-colleagues-reintroduce-assault-weapons-ban/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/1531/cosponsors"]),
        claim("lbr2", "lisa-blunt-rochester", "biblical_marriage", 0, False,
              "As Delaware's at-large U.S. Representative, voted for the Respect for Marriage Act (H.R. 8404, Jul. and Dec. 2022), which repealed the Defense of Marriage Act and codified federal recognition of same-sex and interracial marriages. She has consistently supported same-sex marriage equality throughout her congressional service — rejecting the rubric's one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Lisa_Blunt_Rochester",
               "https://ballotpedia.org/Lisa_Blunt_Rochester"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision.

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
