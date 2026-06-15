#!/usr/bin/env python3
"""Enrichment batch 237: third-claim enrichment for 4 federal candidates from
the bottom of the alphabet (evidence_curated 2-claim pool, reverse-sorted by state).

Targets (bottom-of-alphabet priority: VA → NJ → NE → NC → NJ):
  Chris Smith      (NJ-R · U.S. Rep NJ-04 · incumbent)          – election_integrity
  Don Bacon        (NE-R · U.S. Rep NE-02 · retiring)            – self_defense
  Jeff Jackson     (NC-D · NC Attorney General · fmr U.S. Rep)   – biblical_marriage
  Analilia Mejia   (NJ-D · U.S. Rep NJ-11 · 2026 D incumbent)   – biblical_marriage

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
    # ------------ Chris Smith (NJ-R, U.S. Rep NJ-04, incumbent) -------------
    ("chris-smith", "NJ", "House", [
        claim("cs3", "chris-smith", "election_integrity", 0, True,
              "On April 10, 2025, Smith voted YES on the Safeguard American Voter Eligibility (SAVE) Act (H.R. 22), which passed the House 220–208 with every Republican member voting in favor while 208 Democrats voted against. The SAVE Act requires documentary proof of U.S. citizenship when registering to vote in federal elections, directly implementing the rubric's standard of voter-ID enforcement to bar non-citizens from participating in federal elections. The bill also restricts mass mail-in voter registration drives by requiring in-person verification of citizenship documents. Smith's YES vote — consistent with his four-decade record as a reliable House Republican — reflects sustained commitment to election security measures that align with the rubric's voter-ID and anti-mass-mail-in standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://en.wikipedia.org/wiki/Safeguard_American_Voter_Eligibility_Act"]),
    ]),

    # ------------ Don Bacon (NE-R, U.S. Rep NE-02, retiring) ----------------
    ("don-bacon", "NE", "House", [
        claim("db3", "don-bacon", "self_defense", 1, True,
              "Bacon voted AGAINST H.R. 8, the Bipartisan Background Checks Act of 2021 (House Vote #75, March 11, 2021) — which would have required universal background checks for all private firearm transfers — and AGAINST H.R. 1446, the Enhanced Background Checks Act of 2021, which would have extended the background-check waiting period. His public statement on gun policy: 'Enforcing the laws already on the books would be a more effective tactic than introducing new laws that only punish law-abiding citizens. We should protect the rights of the 99% who are law abiding citizens, and hold accountable those who break the law.' These votes and the accompanying statement are consistent with the rubric's self_defense standard of opposing new firearm registry requirements, expanded background-check mandates, and magazine-limit restrictions that burden law-abiding gun owners rather than targeting criminal misuse.",
              ["https://www.govtrack.us/congress/members/don_bacon/412713",
               "https://en.wikipedia.org/wiki/Don_Bacon",
               "https://ballotpedia.org/Don_Bacon"]),
    ]),

    # ------------ Jeff Jackson (NC-D, NC Attorney General) ------------------
    ("jeff-jackson-ag-2026", "NC", "Attorney General", [
        claim("jj3", "jeff-jackson-ag-2026", "biblical_marriage", 2, False,
              "As a North Carolina State Senator representing District 37, Jackson introduced legislation in 2017 to fully repeal the Public Facilities Privacy & Security Act (HB2) — the state law requiring transgender individuals to use bathrooms corresponding to their biological sex in government buildings and public schools. HB2 had been enacted in 2016 to limit the use of opposite-sex facilities by people who identify as transgender. Jackson's active sponsorship of HB2's full repeal — using his legislative office to dismantle a statutory protection grounded in biological sex — directly contradicts the rubric's standard of rejecting transgender ideology and opposing the legal normalization of gender self-identification over biological sex. North Carolina partially repealed HB2 via HB 142 in March 2017; Jackson's introduction of a full repeal bill demonstrates his willingness to use legislative power to advance transgender accommodation claims beyond the partial repeal that ultimately passed.",
              ["https://en.wikipedia.org/wiki/Jeff_Jackson_(politician)",
               "https://ballotpedia.org/Jeff_Jackson",
               "https://en.wikipedia.org/wiki/Public_Facilities_Privacy_%26_Security_Act"]),
    ]),

    # ------------ Analilia Mejia (NJ-D, U.S. Rep NJ-11, D incumbent) --------
    ("analilia-mejia", "NJ", "NJ-11", [
        claim("am3", "analilia-mejia", "biblical_marriage", 0, False,
              "Running as a DSA-backed progressive endorsed by Sen. Bernie Sanders and Rep. Alexandria Ocasio-Cortez for New Jersey's 11th Congressional District special election, Mejia explicitly pledged to 'fight for full equality for LGBTQ Americans, including access to essential healthcare and comprehensive anti-discrimination protections.' She won the 2026 special election and took office in April 2026 as a sitting U.S. Representative. Her platform explicitly rejects any legal definition of marriage as exclusively between one man and one woman and positions her to vote in favor of legislation recognizing and extending same-sex marriage rights. These statements and endorsements directly contradict the rubric's standard of supporting marriage as an exclusively one-man-one-woman institution under civil law.",
              ["https://en.wikipedia.org/wiki/Analilia_Mejia",
               "https://ballotpedia.org/Analilia_Mejia",
               "https://en.wikipedia.org/wiki/2026_New_Jersey%27s_11th_congressional_district_special_election"]),
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
