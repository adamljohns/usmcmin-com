#!/usr/bin/env python3
"""Enrichment batch 866: 5 WA State Representatives (archetype_party_default, 0 claims).

Primary archetype_curated federal bucket fully exhausted; continuing pivot to
archetype_party_default state-level targets at the bottom of the alphabet (WA).
All five are Democratic members of the Washington House of Representatives whose
positions are sourced from official WA Legislature documents, bill-sponsor
records, WA House Democrats press releases, Planned Parenthood Alliance Advocates
endorsements, and Ballotpedia profiles.

Targets: Darya Farivar (WA-46), Dan Bronoske (WA-28), Clyde Shavers (WA-10),
Chris Stearns (WA-47), Chipalo Street (WA-37).
2 claims each, 10 total — spanning self_defense and sanctity_of_life categories.

Key vote note: Clyde Shavers was one of only two House Democrats to vote NO on
HB 1240 (2023 assault weapons ban); he did vote YES on HB 1163 (2025).
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
    # ---- Darya Farivar (WA-46, D, State Representative) ----
    ("darya-farivar", "WA", "Representative", [
        claim("df1", "darya-farivar", "self_defense", 1, False,
              "Served as Vice Chair of the House Civil Rights & Judiciary Committee that "
              "reported HB 1163 (2025) and championed the permit-to-purchase firearms bill "
              "on the House floor, stating it would ensure 'everyone who decides to purchase "
              "a firearm, understands the capability of the machinery they hold in their "
              "hands'; the bill passed 58-38 on a strict party-line vote and was signed "
              "into law in May 2025 — directly opposing the rubric's defense of "
              "unrestricted firearms acquisition.",
              ["https://mynorthwest.com/mynorthwest-politics/bill-requiring-permits-for-gun-purchases-passes-house-on-party-line-vote/4059942",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("df2", "darya-farivar", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates for her 2024 reelection "
              "to Washington House District 46-Position 2, placing her inside the "
              "abortion-industry political network that opposes any life-at-conception "
              "or personhood standard.",
              ["https://ballotpedia.org/Darya_Farivar",
               "https://daryaforhouse.com/endorsements/"]),
    ]),

    # ---- Dan Bronoske (WA-28, D, State Representative) ----
    ("dan-bronoske", "WA", "Representative", [
        claim("db1", "dan-bronoske", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates for his Washington House "
              "District 28 campaigns, indicating alignment with the abortion-advocacy "
              "network and opposition to any pro-life/personhood standard.",
              ["https://ballotpedia.org/Dan_Bronoske",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements"]),
        claim("db2", "dan-bronoske", "self_defense", 1, False,
              "Voted YES on WA HB 1240 (2023), Washington's ban on the manufacture, "
              "import, distribution, and sale of assault-style rifles — the bill passed "
              "the House 55-42 and was signed into law by Gov. Inslee on April 25, 2023; "
              "opposing the rubric's defense of unrestricted access to commonly owned "
              "semi-automatic firearms.",
              ["https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html"]),
    ]),

    # ---- Clyde Shavers (WA-10, D, State Representative) ----
    ("clyde-shavers", "WA", "Representative", [
        claim("cs1", "clyde-shavers", "self_defense", 1, False,
              "Voted YES on WA HB 1163 (2025), Washington's permit-to-purchase firearms "
              "law requiring a state-issued permit, fingerprinting, and live-fire safety "
              "training before any firearm purchase; the bill passed 58-38 on a strict "
              "party-line vote and was signed into law in May 2025 — opposing the rubric's "
              "defense of unrestricted Second Amendment rights.",
              ["https://legiscan.com/WA/votes/HB1163/2025",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("cs2", "clyde-shavers", "sanctity_of_life", 0, False,
              "Self-described '100 percent pro-choice' legislator who pledges to 'fight to "
              "protect every woman's freedom to choose by ensuring access to abortions and "
              "preventative and prenatal care' — explicitly rejecting any life-at-conception "
              "or personhood standard.",
              ["https://ballotpedia.org/Clyde_Shavers",
               "https://housedemocrats.wa.gov/shavers/"]),
    ]),

    # ---- Chris Stearns (WA-47, D, State Representative) ----
    ("chris-stearns", "WA", "Representative", [
        claim("cst1", "chris-stearns", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates for his Washington House "
              "District 47 campaigns; his legislative work has been recognized by "
              "Pro-Choice Washington for advocacy on abortion rights and reproductive care "
              "— opposing any life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Chris_Stearns",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements"]),
        claim("cst2", "chris-stearns", "self_defense", 1, False,
              "Voted YES on WA HB 1240 (2023), Washington's ban on the manufacture, "
              "import, distribution, and sale of assault-style rifles; the bill passed the "
              "House 55-42 and was signed by Gov. Inslee on April 25, 2023 — opposing the "
              "rubric's defense of unrestricted access to commonly owned semi-automatic "
              "firearms.",
              ["https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://www.king5.com/article/news/politics/state-politics/assault-weapon-ban-passes-senate-to-house-concurrence/281-4400321f-2822-4685-9fae-05a0f1cb1ef8"]),
    ]),

    # ---- Chipalo Street (WA-37, D, State Representative) ----
    ("chipalo-street", "WA", "Representative", [
        claim("chip1", "chipalo-street", "self_defense", 1, False,
              "Cosponsor of WA HB 1163 (2025), the permit-to-purchase firearms law "
              "requiring a state permit, fingerprinting, and live-fire training before "
              "any firearm purchase; the law was signed on May 20, 2025 and passed both "
              "chambers on a strict party-line vote (58-38 in the House) — directly "
              "opposing the rubric's defense of unrestricted firearms acquisition.",
              ["https://www.billsponsor.com/politicians/9862/chipalo-street",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("chip2", "chipalo-street", "sanctity_of_life", 0, False,
              "Voted YES on WA HB 1469 (2023), the ACCESS Washington law protecting "
              "out-of-state access to abortion and gender-affirming care by barring "
              "civil or criminal subpoenas targeting those who seek or provide such "
              "services; passed the House 59-38 and signed into law as Ch. 193, 2023 "
              "Laws — opposing any life-at-conception or personhood standard.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1469&Initiative=false&Year=2023",
               "https://ballotpedia.org/Chipalo_Street",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing name-collision bugs."""
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
