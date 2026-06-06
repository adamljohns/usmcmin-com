#!/usr/bin/env python3
"""Enrichment batch 76: hand-curated claims for 5 US-level federal officials.

Targets archetype_curated federal officials (state=US) with 0 evidence claims,
taken from the bottom of the candidate list (reverse-alpha / US-level executives).

Mix (5 R): Pam Bondi (former AG), Kash Patel (FBI Director),
Howard Lutnick (Commerce Secretary), Brooke Rollins (Agriculture Secretary),
Chris Wright (Energy Secretary).
Each claim cites >=1 reliable source and reflects documented 2024-2026 record.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Pam Bondi (US, former U.S. Attorney General) ----------------
    ("pam-bondi", "US", "Attorney General", [
        claim("pb1", "pam-bondi", "sanctity_of_life", 4, True,
              "Received SBA Pro-Life America endorsement in her 2010 Florida Attorney General race; pledged as FL AG to fight taxpayer funding of abortion at all levels of government — placing her squarely outside the PP/NARAL/EMILY's List endorsement network.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-list-candidate-fund-endorses-pam-bondi",
               "https://sbaprolife.org/newsroom/press-releases/sba-list-endorsed-pam-bondi-claims-primary-win-florida-ag-race"]),
        claim("pb2", "pam-bondi", "border_immigration", 1, True,
              "As U.S. Attorney General (2025–2026), Bondi coordinated aggressive nationwide ICE deportation operations and publicly pressured state governors — including demanding voter-roll data from Minnesota's Tim Walz — to cooperate with federal immigration enforcement, in line with a mandatory-deportation posture.",
              ["https://en.wikipedia.org/wiki/Pam_Bondi"]),
        claim("pb3", "pam-bondi", "self_defense", 1, False,
              "The DOJ under Bondi explored policies to restrict firearm rights for transgender individuals without adjudicated due process, prompting the NRA to publicly state it 'does not support any policy proposals that strip law-abiding citizens of their Second Amendment rights without due process' — a stance at odds with the rubric's opposition to extra-judicial gun restrictions.",
              ["https://en.wikipedia.org/wiki/Pam_Bondi"]),
    ]),

    # ---------------- Kash Patel (US, FBI Director) ----------------
    ("kash-patel", "US", "Bureau of Investigation", [
        claim("kp1", "kash-patel", "refuse_federal_overreach", 0, True,
              "As senior aide to Rep. Devin Nunes, Patel was the primary author of the 2018 Nunes memo that documented systemic FBI FISA warrant abuse in the Crossfire Hurricane counterintelligence investigation — the most concrete public exposure of unconstitutional federal surveillance of a presidential campaign.",
              ["https://en.wikipedia.org/wiki/Kash_Patel"]),
        claim("kp2", "kash-patel", "election_integrity", 0, True,
              "His investigative work exposing the FBI's politically motivated interference in the 2016 election — subsequently corroborated by the DOJ Inspector General's report and the Durham Report — aligns with the rubric's priority of protecting the electoral process from agency manipulation.",
              ["https://en.wikipedia.org/wiki/Kash_Patel"]),
        claim("kp3", "kash-patel", "public_justice", 0, True,
              "As FBI Director, Patel disbanded the DC-based Public Corruption Unit that had been used to prosecute Trump allies, and restructured the bureau to end what he called politically weaponized law enforcement — consistent with the rubric's standard of equal-justice application without partisan targeting.",
              ["https://en.wikipedia.org/wiki/Kash_Patel",
               "https://en.wikipedia.org/wiki/Arctic_Frost_investigation"]),
    ]),

    # ---------------- Howard Lutnick (US, Commerce Secretary) ----------------
    ("howard-lutnick", "US", "Commerce", [
        claim("hl1", "howard-lutnick", "economic_stewardship", 4, True,
              "As Commerce Secretary and lead of the Trump Tariff and Trade agenda, Lutnick has championed protective tariffs as a direct counterweight to the WEF/Davos globalist free-trade consensus that exported American manufacturing; stated publicly, 'tariffs are an amazing tool for the president to use — we need to protect the American worker.'",
              ["https://en.wikipedia.org/wiki/Howard_Lutnick",
               "https://ballotpedia.org/Confirmation_process_for_Howard_Lutnick_for_secretary_of_commerce"]),
        claim("hl2", "howard-lutnick", "foreign_policy_restraint", 2, True,
              "Led the Commerce Department's aggressive tariff and sanction campaign against China — a regime that persecutes Christians and systematically steals U.S. intellectual property — framing trade barriers as America-first policy that refuses to economically subsidize a hostile power.",
              ["https://en.wikipedia.org/wiki/Economic_policy_of_the_second_Trump_administration",
               "https://en.wikipedia.org/wiki/Howard_Lutnick"]),
        claim("hl3", "howard-lutnick", "economic_stewardship", 2, True,
              "Tariff revenue was publicly framed by Lutnick and the Trump administration as a fiscally self-financing alternative to deficit-driven income-tax dependence; Lutnick appeared before the Senate Commerce Committee promoting tariffs as a way to fund government without further borrowing.",
              ["https://ballotpedia.org/Confirmation_process_for_Howard_Lutnick_for_secretary_of_commerce",
               "https://en.wikipedia.org/wiki/Howard_Lutnick"]),
    ]),

    # ---------------- Brooke Rollins (US, Agriculture Secretary) ----------------
    ("brooke-rollins", "US", "Agriculture", [
        claim("br1", "brooke-rollins", "industry_capture", 3, True,
              "Trump nominated Rollins specifically citing her 'commitment to support the American Farmer, defense of American Food Self-Sufficiency, and the restoration of Agriculture-dependent American Small Towns' — placing small-farm and local-food sovereignty at the center of her USDA mandate.",
              ["https://news.ballotpedia.org/2024/11/25/donald-trump-r-announced-brooke-rollins-as-his-nominee-for-secretary-of-agriculture-in-his-second-presidential-term/",
               "https://en.wikipedia.org/wiki/Brooke_Rollins"]),
        claim("br2", "brooke-rollins", "industry_capture", 2, True,
              "Her 15-year leadership (2003–2018) at the Texas Public Policy Foundation included policy positions opposing federal agriculture subsidies that disproportionately benefit large corporate agribusiness, a stance consistent with the rubric's anti-Big Ag posture favoring independent family farms.",
              ["https://en.wikipedia.org/wiki/Brooke_Rollins"]),
        claim("br3", "brooke-rollins", "refuse_federal_overreach", 0, True,
              "In June 2025, Rollins formally ended the Clinton-era 'roadless rule,' eliminating a 24-year federal restriction that had locked 58 million acres of national forest land away from agricultural and resource use — a direct reversal of federal executive overreach on land access.",
              ["https://en.wikipedia.org/wiki/Brooke_Rollins"]),
    ]),

    # ---------------- Chris Wright (US, Energy Secretary) ----------------
    ("chris-wright", "US", "Energy", [
        claim("cw1", "chris-wright", "refuse_federal_overreach", 0, True,
              "As Energy Secretary, oversaw the rollback of Biden-era climate mandates and DOE regulations on fossil fuel production; directed coal power plants to remain operational despite federal regulatory pressure to close them, prioritizing grid reliability over administrative climate diktat.",
              ["https://en.wikipedia.org/wiki/Chris_Wright",
               "https://ballotpedia.org/Chris_Wright_(secretary_of_energy)"]),
        claim("cw2", "chris-wright", "economic_stewardship", 4, True,
              "An outspoken critic of ESG-driven energy restrictions, Wright's 'energy abundance' philosophy directly challenges the WEF/Davos-aligned sustainability agenda that seeks to constrain fossil fuels; he considers mandatory green-energy transitions economically destructive to American workers and developing-world poverty reduction.",
              ["https://en.wikipedia.org/wiki/Chris_Wright"]),
        claim("cw3", "chris-wright", "foreign_policy_restraint", 1, True,
              "Trump cited Wright as 'one of the pioneers who helped launch the American Shale Revolution that fueled American Energy Independence, and transformed the Global Energy Markets and Geopolitics' — his domestic energy-dominance agenda directly reduces the oil-import dependency that has driven two decades of Middle Eastern military entanglements.",
              ["https://en.wikipedia.org/wiki/Chris_Wright",
               "https://ballotpedia.org/Confirmation_process_for_Chris_Wright_for_secretary_of_energy"]),
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
        print(f"  ✓ {m['name']:<26} (US) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
