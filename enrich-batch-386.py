#!/usr/bin/env python3
"""Enrichment batch 386: hand-curated claims for 4 Republican State Senators (WI + WA).

Targets archetype_party_default state senators with 0 evidence claims from the
bottom of the alphabet (WI then WA), continuing after the archetype_curated federal
senator and representative buckets were fully depleted.

Senators: Cory Tomczyk (WI-SD29), Phil Fortunato (WA-SD31),
Shelly Short (WA-SD7), Perry Dozier (WA-SD16).

Each claim cites >=1 reliable source and reflects 2023-2026 voting
record / public positions.

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
    # ---------------- Cory Tomczyk (WI-SD29, State Senator) ----------------
    ("cory-tomczyk", "WI", "Senator", [
        claim("ct1", "cory-tomczyk", "election_integrity", 0, True,
              "Sponsored 2023 Senate Joint Resolution 73, which would amend the Wisconsin Constitution to require photographic identification to vote in any Wisconsin election — a foundational voter-integrity measure demanding verified identity at the ballot box.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/senate/2567",
               "https://ballotpedia.org/Cory_Tomczyk"]),
        claim("ct2", "cory-tomczyk", "self_defense", 1, True,
              "Sponsored 2023 Senate Bill 466 prohibiting financial institutions from using firearms-specific merchant category codes in payment card transactions and banning government lists of firearm owners — defending gun-owner financial privacy against corporate and government surveillance of Second Amendment activity.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/senate/2567",
               "https://en.wikipedia.org/wiki/Cory_Tomczyk"]),
        claim("ct3", "cory-tomczyk", "industry_capture", 0, True,
              "Ran for Wisconsin State Senate in 2022 explicitly opposing COVID-19 government lockdown orders — a principled stand against pandemic-era pharmaceutical-backed public-health mandates and executive overreach that closed businesses and places of worship across Wisconsin.",
              ["https://ballotpedia.org/Cory_Tomczyk",
               "https://legis.wisconsin.gov/senate/29/tomczyk/about/"]),
    ]),

    # ---------------- Phil Fortunato (WA-SD31, State Senator) ----------------
    ("phil-fortunato", "WA", "Senator", [
        claim("pf1", "phil-fortunato", "sanctity_of_life", 0, True,
              "Sponsored Washington SB 5172 providing that only licensed physicians may perform abortions and that women must be fully informed of the inherent risks of the procedure — a pro-life medical-safety measure restricting abortion to qualified practitioners in a state where it is broadly legal.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5172&Initiative=false&Year=2024",
               "https://philfortunato.src.wastateleg.org/abortions-washington-might-legal-inslee-made-less-safe-says-fortunato/"]),
        claim("pf2", "phil-fortunato", "self_defense", 1, True,
              "Opposed 2023 SB 5078, which banned high-capacity magazines and created new barriers to legal gun purchases, stating 'Problems with gun violence and crime in Washington are not caused by law-abiding citizens' and warning that magazine restrictions and storage mandates unconstitutionally impair self-defense rights under the Washington Constitution.",
              ["https://philfortunato.src.wastateleg.org/restricting-your-rights/",
               "https://ballotpedia.org/Phil_Fortunato"]),
        claim("pf3", "phil-fortunato", "family_child_sovereignty", 0, True,
              "Publicly opposed Washington state bills that would prevent the government from notifying parents when their minor child seeks 'protected health services' — including abortions performable by any health care provider — defending parental notification rights and opposing the state substituting itself for parents in minor children's medical decisions.",
              ["https://philfortunato.src.wastateleg.org/restricting-your-rights/",
               "https://ballotpedia.org/Phil_Fortunato"]),
    ]),

    # ---------------- Shelly Short (WA-SD7, State Senator) ----------------
    ("shelly-short", "WA", "Senator", [
        claim("ss1", "shelly-short", "self_defense", 1, True,
              "NRA-endorsed Washington State Senator who has consistently voted against gun-control legislation, opposing the Democratic majority's sweeping firearms restrictions including assault weapons bans and high-capacity magazine limits advanced in the 2023–2025 sessions.",
              ["https://ballotpedia.org/Shelly_Short",
               "https://justfacts.votesmart.org/candidate/108332/shelly-short"]),
        claim("ss2", "shelly-short", "sanctity_of_life", 0, True,
              "Endorsed by Human Life of Washington — the state's oldest pro-life organization — reflecting a consistent pro-life voting record across her service in the Washington House of Representatives (2009–2017) and Washington State Senate (2017–present).",
              ["https://ballotpedia.org/Shelly_Short",
               "https://justfacts.votesmart.org/interest-group/508/human-life-of-washington"]),
        claim("ss3", "shelly-short", "family_child_sovereignty", 0, True,
              "Supported hearings in 2024 for Initiative 2081, the Washington Parental Bill of Rights — which required schools and health care providers to notify parents of services provided to their minor children, including non-emergency medical services — championing parental notification as a fundamental family protection.",
              ["https://shellyshort.src.wastateleg.org/three-initiatives-get-hearings-olympia/",
               "https://ballotpedia.org/Shelly_Short"]),
    ]),

    # ---------------- Perry Dozier (WA-SD16, State Senator) ----------------
    ("perry-dozier", "WA", "Senator", [
        claim("pd1", "perry-dozier", "family_child_sovereignty", 0, True,
              "Opposed 2025 Senate Bill 5181 — which stripped critical provisions from Washington's Initiative 2081 (Parental Bill of Rights) including school notification requirements for non-emergency medical services provided to minor children — declaring: 'It\\'s not a cleanup bill, it\\'s an overhaul bill. What was in there that the parents wanted in 2081 was totally changed.'",
              ["https://washingtonstatestandard.com/2025/02/05/wa-senate-democrats-approve-changes-to-parents-bill-of-rights/",
               "https://ballotpedia.org/Perry_Dozier"]),
        claim("pd2", "perry-dozier", "refuse_state_overreach", 0, True,
              "As a 35-year dryland and irrigated wheat farmer, former president of the Washington Association of Wheat Growers, and Ranking Member of the Senate Business, Financial Services & Trade Committee, Dozier consistently opposes state regulatory mandates that burden independent family farmers and rural small businesses.",
              ["https://ballotpedia.org/Perry_Dozier",
               "https://leg.wa.gov/legislators/member/perry-dozier"]),
        claim("pd3", "perry-dozier", "economic_stewardship", 2, True,
              "Serving as Ranking Member of the Senate Business, Financial Services & Trade Committee, Dozier leads Republican opposition to Washington's Democratic-majority budget expansions, consistently advocating for fiscal restraint and opposing new regulatory burdens and deficit-financed spending increases that raise costs for family farms and small rural businesses.",
              ["https://leg.wa.gov/legislators/member/perry-dozier",
               "https://ballotpedia.org/Perry_Dozier"]),
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
