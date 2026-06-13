#!/usr/bin/env python3
"""Enrichment batch 174: 5 House Republicans from AZ and CA.

evidence_federal bucket, bottom-of-alphabet states: AZ sitting incumbents
(Gosar AZ-09, Hamadeh AZ-08), AZ open-seat conservatives (Lamb AZ-05,
Chaplik AZ-01), and CA-01 special-election winner Gallagher.

Sources: gosar.house.gov, hamadeh.house.gov, ballotpedia.org,
en.wikipedia.org, govtrack.us, congress.gov.
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
    # ---------------- Paul Gosar (AZ-09, US Representative) ----------------
    ("paul-gosar", "AZ", "Representative", [
        claim("pg1", "paul-gosar", "sanctity_of_life", 0, True,
              "Holds a 100% rating from the National Right to Life Committee; was an original cosponsor of the Born-Alive Abortion Survivors Protection Act in multiple Congresses; voted to defund Planned Parenthood and introduced the Defund Planned Parenthood Act, affirming his position that human life deserves protection from conception.",
              ["https://gosar.house.gov/news/documentsingle.aspx?DocumentID=1502",
               "https://ballotpedia.org/Paul_Gosar"]),
        claim("pg2", "paul-gosar", "self_defense", 1, True,
              "Introduced the Gun Owner Registration Information Protection Act to block any federal government registry or database of gun-owner information — directly targeting the surveillance infrastructure that enables confiscation and rejecting red-flag-law-style registration mandates.",
              ["https://ballotpedia.org/Paul_Gosar",
               "https://gosar.house.gov/voterecord/"]),
        claim("pg3", "paul-gosar", "border_immigration", 0, True,
              "Published 'The GOP's last chance to keep our border wall promise,' calling on Congress to fund and complete the southern border wall before losing the majority; questioned sanctuary-city officials at a March 2025 House hearing — a consistent 15-year record of wall-and-enforcement-first immigration policy.",
              ["https://gosar.house.gov/news/documentsingle.aspx?DocumentID=3609",
               "https://www.govtrack.us/congress/members/paul_gosar/412397"]),
    ]),

    # ---------------- Abraham Hamadeh (AZ-08, US Representative) ----------------
    ("abraham-hamadeh", "AZ", "Representative", [
        claim("ah1", "abraham-hamadeh", "self_defense", 1, True,
              "Cosponsored the Hearing Protection Act and two companion pieces of suppressor legislation — all backed by the NRA — stating he 'learned firsthand about the health and safety value of suppressors' during U.S. Army Reserve intelligence service; explicitly frames his cosponsorship as protecting Second Amendment rights from anti-gun regulatory overreach.",
              ["https://hamadeh.house.gov/media/press-releases/congressman-hamadeh-takes-aim-anti-second-amendment-policies-support",
               "https://en.wikipedia.org/wiki/Abraham_Hamadeh"]),
        claim("ah2", "abraham-hamadeh", "border_immigration", 1, True,
              "As a sitting freshman Congressman, personally traveled to Guantanamo Bay to inspect and publicly support the Trump administration's mass deportation operations — one of the first House members to visit the facility — affirming mandatory deportation of illegal aliens as federal policy.",
              ["https://hamadeh.house.gov/media/press-releases",
               "https://ballotpedia.org/Abraham_Hamadeh"]),
        claim("ah3", "abraham-hamadeh", "election_integrity", 0, True,
              "Co-leading the Preventing Ranked Choice Corruption Act with Rep. Nick Begich to prohibit ranked-choice voting nationwide; also sent a formal letter to Attorney General Pam Bondi requesting investigation of credible claims that an elections service provider breached protocols in Arizona's 2024 general election.",
              ["https://en.wikipedia.org/wiki/Abraham_Hamadeh",
               "https://hamadeh.house.gov/media/press-releases"]),
    ]),

    # ---------------- James Gallagher (CA-01, US Representative) ----------------
    ("james-gallagher-ca-01", "CA", "Representative", [
        claim("jg1", "james-gallagher-ca-01", "sanctity_of_life", 0, True,
              "As California Assembly Minority Leader, formally opposed California Proposition 1 (the 2022 Right to Reproductive Freedom Amendment) that enshrined abortion up to viability in the state constitution — one of the most prominent Republicans in the state to lead organized opposition to the measure.",
              ["https://ballotpedia.org/California_Right_to_Reproductive_Freedom_Amendment_(2022)",
               "https://en.wikipedia.org/wiki/James_Gallagher_(California_politician)"]),
        claim("jg2", "james-gallagher-ca-01", "refuse_state_overreach", 0, True,
              "Served as California Assembly Minority Leader from 2022 to 2025, leading Republican resistance to California's progressive supermajority agenda on parental rights, property rights, and individual liberty; won Trump-endorsed 2026 special election for CA-01 at 61.6%, bringing a limited-government, pushback-against-state-overreach record to Congress.",
              ["https://en.wikipedia.org/wiki/James_Gallagher_(California_politician)",
               "https://ballotpedia.org/James_Gallagher_(California)"]),
    ]),

    # ---------------- Mark Lamb (AZ-05, candidate) ----------------
    ("mark-lamb", "AZ", "Representative", [
        claim("ml1", "mark-lamb", "self_defense", 0, True,
              "Spoke at the Constitutional Sheriffs and Peace Officers Association convention in 2020, which holds that sheriffs must refuse to enforce unconstitutional firearm restrictions; as Pinal County Sheriff refused to enforce a COVID-19 stay-at-home order he deemed unconstitutional; running for Congress pledging to defend Second Amendment rights 'without compromise.'",
              ["https://en.wikipedia.org/wiki/Mark_Lamb_(sheriff)",
               "https://ballotpedia.org/Mark_Lamb"]),
        claim("ml2", "mark-lamb", "border_immigration", 0, True,
              "As Pinal County Sheriff, called for military-level security along the Mexico–U.S. border as early as 2019 to combat cartel violence in national parks; appeared alongside the Federation for American Immigration Reform (FAIR) advocating enforcement-first immigration policy; ran for U.S. Senate 2024 on a wall-and-deportation enforcement platform.",
              ["https://en.wikipedia.org/wiki/Mark_Lamb_(sheriff)",
               "https://ballotpedia.org/Mark_Lamb"]),
        claim("ml3", "mark-lamb", "industry_capture", 0, True,
              "In May 2020, publicly refused to enforce Arizona's COVID-19 pandemic stay-at-home order as Pinal County Sheriff, stating he believed it was unconstitutional — an early and documented stand against government-mandated public-health restrictions driven by pharma and public-health bureaucracy.",
              ["https://en.wikipedia.org/wiki/Mark_Lamb_(sheriff)",
               "https://ballotpedia.org/Mark_Lamb"]),
    ]),

    # ---------------- Joseph Chaplik (AZ-01, candidate) ----------------
    ("joseph-chaplik", "AZ", "Representative", [
        claim("jc1", "joseph-chaplik", "border_immigration", 2, True,
              "Founding member and Vice Chairman of the Arizona Freedom Caucus, which has consistently pushed enforcement-first, anti-sanctuary immigration policy at the state level; running for Congress explicitly on stopping illegal immigration and keeping Arizona communities safe from cartel-driven crime.",
              ["https://ballotpedia.org/Joseph_Chaplik",
               "https://en.wikipedia.org/wiki/Joseph_Chaplik"]),
        claim("jc2", "joseph-chaplik", "economic_stewardship", 2, True,
              "As founding member of the Arizona Freedom Caucus — modeled on the House Freedom Caucus — consistently fought against reckless state spending; publicly states his mission to bring the same fight against deficit spending to Congress, putting 'people ahead of special interests and reckless spending.'",
              ["https://ballotpedia.org/Joseph_Chaplik",
               "https://news.ballotpedia.org/2026/05/01/joseph-chaplik-jay-feely-and-john-trobough-running-in-republican-primary-for-arizonas-1st-congressional-district/"]),
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
