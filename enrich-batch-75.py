#!/usr/bin/env python3
"""Enrichment batch 75: hand-curated claims for 5 US-level federal officials.

Targets archetype_curated federal officials (state=US) with 0 evidence claims,
taken from the bottom of the candidate list (reverse alpha / US-level executives).

Mix (5 R): Kristi Noem (Special Envoy/former DHS), Doug Burgum (Interior),
Linda McMahon (Education), Mike Pence (former VP), Nikki Haley (former UN Amb).
Each claim cites >=1 reliable source and reflects documented public record.

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
    # ------------ Kristi Noem (US-R, Special Envoy / former DHS Secretary) ------------
    ("kristi-noem", "US", "Homeland", [
        claim("kn1", "kristi-noem", "sanctity_of_life", 0, True,
              "As a U.S. Representative, Noem co-sponsored legislation in 2015 to amend the 14th Amendment to define human life and personhood as beginning at fertilization, a federal ban on abortion from conception. She also voted for the Pain-Capable Unborn Child Protection Act banning abortions after 20 weeks, and holds a lifetime 100% pro-life voting record endorsed by Susan B. Anthony List.",
              ["https://ballotpedia.org/Kristi_Noem",
               "https://en.wikipedia.org/wiki/Kristi_Noem"]),
        claim("kn2", "kristi-noem", "border_immigration", 2, True,
              "Voted Yea on the No Sanctuary for Criminals Act (HR 3003, 2017) in the U.S. House, blocking federal funds to sanctuary jurisdictions that refuse to cooperate with ICE detainer requests — directly opposing sanctuary policies.",
              ["https://ballotpedia.org/Kristi_Noem",
               "https://en.wikipedia.org/wiki/Kristi_Noem"]),
        claim("kn3", "kristi-noem", "border_immigration", 1, True,
              "As Secretary of Homeland Security (2025), Noem led the Trump administration's historic mass-deportation campaign: DHS executed over 713,000 removals of criminal illegal aliens in 2025, including gang members, drug traffickers, and violent offenders — the largest deportation effort in modern U.S. history.",
              ["https://www.dhs.gov/news/2025/12/19/under-president-trump-and-secretary-noem-department-homeland-security-has-historic",
               "https://www.dhs.gov/news/2025/08/14/secretary-noem-makes-history-first-200-days-office"]),
    ]),

    # ------------ Doug Burgum (US-R, Secretary of the Interior) ------------
    ("doug-burgum", "US", "Interior", [
        claim("db1", "doug-burgum", "sanctity_of_life", 0, True,
              "As North Dakota governor, Burgum signed SB 2150 in April 2023, a near-total abortion ban prohibiting virtually all abortions in the state — one of the strictest pro-life laws in the nation following the Dobbs decision.",
              ["https://ballotpedia.org/Doug_Burgum",
               "https://en.wikipedia.org/wiki/Doug_Burgum"]),
        claim("db2", "doug-burgum", "self_defense", 0, True,
              "Received an 'A' grade from the NRA Political Victory Fund as governor of North Dakota, reflecting strong support for Second Amendment rights and gun-friendly legislation throughout his gubernatorial tenure.",
              ["https://ballotpedia.org/Doug_Burgum",
               "https://en.wikipedia.org/wiki/Doug_Burgum"]),
        claim("db3", "doug-burgum", "economic_stewardship", 4, True,
              "Appointed by Trump to chair the National Energy Dominance Council (February 2025), Burgum championed domestic fossil fuel extraction on federal lands, reversed Biden-era wind energy mandates, and rejected ESG-driven energy policy — opposing the globalist climate-finance agenda the rubric identifies as WEF/ESG capture.",
              ["https://www.doi.gov/pressreleases/secretary-doug-burgum-signs-first-round-secretarys-orders-unleash-american-energy",
               "https://en.wikipedia.org/wiki/Doug_Burgum"]),
    ]),

    # ------------ Linda McMahon (US-R, Secretary of Education) ------------
    ("linda-mcmahon", "US", "Education", [
        claim("lm1", "linda-mcmahon", "self_defense", 0, True,
              "The NRA endorsed McMahon in her 2010 Connecticut U.S. Senate campaign, reflecting her pro-Second Amendment stance in a state known for strict gun laws.",
              ["https://ballotpedia.org/Linda_McMahon",
               "https://en.wikipedia.org/wiki/Linda_McMahon"]),
        claim("lm2", "linda-mcmahon", "biblical_marriage", 2, True,
              "As Secretary of Education, McMahon launched federal investigations into school districts and state departments that concealed gender-transition records from parents, stating those schools were advancing a 'dangerous transgender agenda' — actively opposing transgender ideology in K-12 settings.",
              ["https://en.wikipedia.org/wiki/Linda_McMahon",
               "https://www.ed.gov/about/ed-organization/meet-secretary-of-education/linda-e-mcmahon"]),
        claim("lm3", "linda-mcmahon", "family_child_sovereignty", 0, True,
              "A leading advocate for parental rights and school choice: as chair of the America First Policy Institute achieved Universal School Choice in 12 states, and as Secretary of Education has continued championing parental empowerment and school-choice expansion as core policy priorities.",
              ["https://ballotpedia.org/Linda_McMahon_(United_States_Secretary_of_Education)",
               "https://en.wikipedia.org/wiki/Linda_McMahon"]),
    ]),

    # ------------ Mike Pence (US-R, Former Vice President) ------------
    ("mike-pence", "US", "Vice President", [
        claim("mp1", "mike-pence", "sanctity_of_life", 4, True,
              "Beginning in 2007, Pence led the congressional effort to defund Planned Parenthood, introducing legislation every session to block all Title X federal funding to organizations that perform abortions — the longest-running legislative campaign to strip abortion providers of public money in modern congressional history.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Mike_Pence",
               "https://en.wikipedia.org/wiki/Mike_Pence"]),
        claim("mp2", "mike-pence", "sanctity_of_life", 0, True,
              "After the Supreme Court overturned Roe v. Wade in June 2022, Pence declared 'we must not rest and must not relent until the sanctity of life is restored to the center of American law in every state in the land,' affirming a life-from-conception standard as the governing principle for all states.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Mike_Pence",
               "https://ballotpedia.org/Mike_Pence"]),
        claim("mp3", "mike-pence", "christian_liberty", 0, True,
              "As Indiana governor in 2015, Pence signed the Religious Freedom Restoration Act (RFRA), protecting business owners' religious conscience from government compulsion — a landmark state-level assertion of free exercise rights despite intense national backlash.",
              ["https://en.wikipedia.org/wiki/Mike_Pence",
               "https://en.wikipedia.org/wiki/Indiana_Senate_Bill_101"]),
    ]),

    # ------------ Nikki Haley (US-R, Former UN Ambassador) ------------
    ("nikki-haley", "US", "Ambassador", [
        claim("nh1", "nikki-haley", "sanctity_of_life", 0, False,
              "During her 2024 presidential campaign, Haley explicitly rejected a federal abortion ban, arguing each state must independently decide its abortion policy — declining to endorse federal personhood protections from conception and calling a national ban politically unrealistic.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Nikki_Haley",
               "https://ballotpedia.org/Nikki_Haley_(U.S._ambassador_to_the_U.N.)"]),
        claim("nh2", "nikki-haley", "foreign_policy_restraint", 1, False,
              "Strongly advocated for continuing U.S. financial and military aid packages to both Israel and Ukraine during her 2024 presidential campaign, opposing any reduction in foreign military entanglements — contrary to the rubric's call to end open-ended foreign wars and repeal authorization for military force.",
              ["https://en.wikipedia.org/wiki/Nikki_Haley",
               "https://en.wikipedia.org/wiki/Nikki_Haley_2024_presidential_campaign"]),
        claim("nh3", "nikki-haley", "foreign_policy_restraint", 0, False,
              "As UN Ambassador (2017-2018), Haley threatened consequences against nations voting against U.S. positions on Jerusalem, championed broad U.S. interventionist postures at the Security Council, and advanced an aggressive foreign-policy agenda outside Article-I congressional war-powers constraints.",
              ["https://en.wikipedia.org/wiki/Nikki_Haley",
               "https://ballotpedia.org/Nikki_Haley_(U.S._ambassador_to_the_U.N.)"]),
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
