#!/usr/bin/env python3
"""Enrichment batch 754: 4 FL state officials with 0 evidence claims.

Targets evidence_state FL candidates (archetype_curated federal bucket now
exhausted). Bottom-of-name-alphabet FL pool: Wilton Simpson (Agriculture
Commissioner), Webster Barnaby (HD-29), Wyman Duggan (HD-12/15),
Toby Overdorf (HD-85). 9 claims spanning self_defense, sanctity_of_life,
biblical_marriage, economic_stewardship, family_child_sovereignty, and
public_justice categories.

All claims cite reliable 2019-2025 sources (floridapolitics.com,
flsenate.gov, en.wikipedia.org). Minified write preserves ~35-36 MB master.
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
    # ----------- Wilton Simpson (FL, Agriculture Commissioner, R) -----------
    ("wilton-simpson", "FL", "Agriculture Commissioner", [
        claim("ws1", "wilton-simpson", "sanctity_of_life", 0, True,
              "As Florida Senate President, stood alongside Gov. DeSantis at the April 2022 signing of HB 5 — Florida's 15-week abortion ban — applauding the legislation and declaring 'I think it's a great day,' while highlighting protections for the unborn. His Senate majority delivered the bill on a near party-line 23-15 vote.",
              ["https://floridapolitics.com/archives/516821-gov-desantis-signs-15-week-abortion-ban/",
               "https://floridapolitics.com/archives/506785-after-senate-agrees-to-restrict-abortions-president-wilton-simpson-puts-birth-control-funding-in-budget/"]),
        claim("ws2", "wilton-simpson", "self_defense", 0, True,
              "NRA-endorsed Agriculture Commissioner who oversees Florida's concealed-weapons licensing program; as a state senator stated publicly he would vote for constitutional carry; and as Commissioner advanced the Florida Firearms and Ammo Act (SB 214, 2023) — the first-in-the-nation law shielding Floridians' firearm and ammunition purchase records from corporate financial tracking.",
              ["https://floridapolitics.com/archives/510795-nra-endorses-wilton-simpson-for-agriculture-commissioner/",
               "https://floridapolitics.com/archives/488221-wilton-simpson-says-hed-vote-for-constitutional-carry-bill/",
               "https://floridapolitics.com/archives/580248-wilton-simpson-wants-to-shield-gun-and-ammo-sale-data/"]),
        claim("ws3", "wilton-simpson", "economic_stewardship", 4, True,
              "Led a coalition of 12 state agriculture commissioners demanding the largest U.S. banks fully disclose their ESG investment policies, publicly stating he was 'proud to stand' against the UN's Net-Zero Banking Alliance and its 'left-wing, anti-agriculture, ESG-driven, and anti-consumer climate policies.' The 2025 Florida Farm Bill he backed also included provisions barring ESG-based lending discrimination against farmers.",
              ["https://floridapolitics.com/archives/659806-wilton-simpson-hammers-u-n-climate-alliance-of-investors-after-jpmorgan-chase-blackrock-drop-out/",
               "https://floridapolitics.com/archives/738289-desantis-fluoride-fake-milk-meat-shrooms/"]),
    ]),

    # ----------- Webster Barnaby (FL, State Representative HD-29, R) -----------
    ("webster-barnaby", "FL", "State Representative", [
        claim("wb1", "webster-barnaby", "biblical_marriage", 2, True,
              "Voted for HB 1521 (Facility Requirements Based on Sex Act, 2023) — Florida's bathroom bill that passed on an 80-37 party-line vote — and during the April 2023 House floor debate openly rejected transgender ideology, calling those who identify as transgender 'demons and imps' pretending to be part of this world.",
              ["https://floridapolitics.com/archives/604915-bathroom-bill-passes-on-party-lines-in-house/",
               "https://en.wikipedia.org/wiki/Webster_Barnaby",
               "https://www.flsenate.gov/Session/Bill/2023/1521"]),
        claim("wb2", "webster-barnaby", "self_defense", 0, True,
              "Co-introduced HB 543 (2023), the Florida constitutional carry / permitless carry bill signed by Gov. DeSantis on April 3, 2023, making Florida the 26th state to allow concealed carry of a firearm without a government-issued permit.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
    ]),

    # ----------- Wyman Duggan (FL, State Representative HD-12/15, R) -----------
    ("wyman-duggan", "FL", "State Representative", [
        claim("wd1", "wyman-duggan", "self_defense", 0, True,
              "Co-introduced HB 543 (2023), Florida's permitless concealed carry law signed by Gov. DeSantis on April 3, 2023 — eliminating the prior requirement for a government-issued concealed weapons license and making Florida the 26th constitutional-carry state.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
        claim("wd2", "wyman-duggan", "family_child_sovereignty", 0, True,
              "As Speaker Pro Tempore, introduced and shepherded 'Brooke's Law' (HB 1161 / SB 700, 2025) through the Florida House — legislation requiring internet platforms to remove non-consensual AI-generated deepfake sexual imagery of victims within 48 hours upon request, protecting Floridians (including minors) from digital sexual exploitation. The bill passed both chambers unanimously.",
              ["https://floridapolitics.com/archives/732378-house-passes-brookes-law/",
               "https://floridapolitics.com/archives/723350-wyman-duggan-bills-tackle-fake-sex-pics-crimes-against-children/"]),
    ]),

    # ----------- Toby Overdorf (FL, State Representative HD-85, R) -----------
    ("toby-overdorf", "FL", "State Representative", [
        claim("to1", "toby-overdorf", "self_defense", 0, True,
              "Co-introduced HB 543 (2023), Florida's constitutional carry / permitless carry bill, which eliminated the state's prior concealed-weapons licensing requirement and was signed into law by Gov. DeSantis on April 3, 2023.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
        claim("to2", "toby-overdorf", "public_justice", 0, True,
              "Twice championed anti-human-trafficking legislation in the Florida House: HB 219 (2019) expanded the legal definition of adult theaters to include strip clubs for age-documentation enforcement and set mandatory minimums for solicitation convictions; and HB 615 (2023) required the Statewide Council on Human Trafficking to assess social-media platforms' role in facilitating trafficking and created training for fire-safety inspectors to identify trafficking victims.",
              ["https://floridapolitics.com/archives/295040-house-approves-bill-human-trafficking/",
               "https://floridapolitics.com/archives/609164-legislature-passes-bill-adding-safe-house-protections-against-human-trafficking-closing-hotels-loophole/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
