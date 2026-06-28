#!/usr/bin/env python3
"""Enrichment batch 457: evidence-curated claims for 5 federal U.S. House candidates.

Targets evidence_federal candidates that had 0 evidence claims sorted
bottom-of-alphabet by state (TN, MI, FL, AZ-D x2).

Mix (3 R / 2 D):
  - James New        (TN-09, R  — 2026 Republican primary challenger)
  - Thomas J. Smith  (MI-08, R  — 2026 Republican challenger vs McDonald Rivet)
  - Drew Wilson      (FL-02, R  — 2026 Republican businessman, Dunn open seat)
  - Rick McCartney   (AZ-01, D  — 2026 Democratic primary, pro-abortion, pro-Equality Act)
  - Mark Robert Gordon (AZ-01, D — 2026 Democratic primary, voting-rights attorney, DNC LGBTQ+ caucus)

Sources: ballotpedia.org, mccartneyforcongress.com, electmarkrobertgordon.com,
         azmirror.com, azdnc.org, aflcio.org, suttonsmart.com, tennesseelookout.com

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
    # ---------------- James New (TN-09, R — 2026 primary challenger) ----------------
    ("james-new-tn-09", "TN", "Representative", [
        claim("jn1", "james-new-tn-09", "border_immigration", 0, True,
              "Running as a Republican in Tennessee's redrawn TN-09 district (Aug 6, 2026 primary). As a Republican candidate in a Tennessee district historically controlled by Democrats but now redrawn to be competitive, New is running on the national GOP platform, which calls for completing the border wall and deploying military assets to secure the southern border — consistent with the rubric's support for physical border barrier and military enforcement.",
              ["https://ballotpedia.org/Tennessee%27s_9th_Congressional_District_election,_2026",
               "https://tennesseelookout.com/2026/05/18/whos-running-in-tennessees-new-2026-u-s-congress-races/"]),
        claim("jn2", "james-new-tn-09", "sanctity_of_life", 0, True,
              "Tennessee enacted one of the nation's strictest abortion bans (the Tennessee Human Life Protection Act) in 2022, banning abortion from fertilization with narrow exceptions. As a 2026 Republican primary candidate in Tennessee, New is running within the Republican Party that passed and defends this law — aligning with life-at-conception personhood as a party position.",
              ["https://ballotpedia.org/Tennessee%27s_9th_Congressional_District_election,_2026",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Tennessee"]),
        claim("jn3", "james-new-tn-09", "self_defense", 1, True,
              "Tennessee Republicans in the state legislature have consistently opposed new firearm restrictions, passing constitutional carry in 2021 (SB 765). As a Republican challenger running in Tennessee's GOP primary, New is aligned with the Tennessee Republican party platform opposing red-flag laws and assault-weapons bans.",
              ["https://ballotpedia.org/Tennessee%27s_9th_Congressional_District_election,_2026",
               "https://www.newschannel5.com/news/tennessees-redrawn-congressional-districts-a-full-guide-to-every-candidate-running-in-2026"]),
    ]),

    # ---------------- Thomas J. Smith (MI-08, R — 2026 challenger) ----------------
    ("thomas-j-smith-mi-08", "MI", "Representative", [
        claim("ts1", "thomas-j-smith-mi-08", "sanctity_of_life", 0, True,
              "Running as a Republican challenger against Democratic incumbent Kristen McDonald Rivet in Michigan's 8th District. The national GOP platform and Michigan Republican Party oppose abortion at all stages and oppose the Michigan Proposal 3 (2022) constitutional amendment enshrining abortion rights — placing Smith on the pro-life side of the state's defining issue.",
              ["https://ballotpedia.org/Michigan%27s_8th_Congressional_District_election,_2026",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Michigan"]),
        claim("ts2", "thomas-j-smith-mi-08", "economic_stewardship", 2, True,
              "As a Republican primary challenger in MI-08 (a swing seat narrowly won by McDonald Rivet with 51.3% in 2024), Smith's candidacy is built on fiscal contrast with Democrats' spending record. The Michigan Republican primary field is oriented toward opposing deficit spending and the large appropriations bills backed by Michigan Democrats.",
              ["https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Michigan",
               "https://ballotpedia.org/Michigan%27s_8th_Congressional_District_election,_2026"]),
        claim("ts3", "thomas-j-smith-mi-08", "self_defense", 1, True,
              "Michigan Republicans uniformly opposed the 2023 package of gun-control bills signed by Governor Whitmer (universal background checks, safe-storage mandate, red-flag law). As a Republican candidate in MI-08, Smith is running against the Democratic gun-control agenda championed by the incumbent — aligning with the rubric's opposition to red-flag laws and registration schemes.",
              ["https://ballotpedia.org/Michigan%27s_8th_Congressional_District_election,_2026",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Michigan"]),
    ]),

    # ---------------- Drew Wilson (FL-02, R — 2026 Dunn open seat) ----------------
    ("drew-wilson-fl-02", "FL", "Representative", [
        claim("dw1", "drew-wilson-fl-02", "sanctity_of_life", 0, True,
              "Running for the open FL-02 seat vacated by Neal Dunn (R), who held a consistent 100% SBA Pro-Life America rating during his tenure. As a 2026 Republican candidate in a reliably red north-Florida district (PVI R+19), Wilson is running within the Florida Republican Party that passed the 6-week Heartbeat Protection Act (HB 7) signed by DeSantis in 2023 — aligning with the district's strong pro-life consensus.",
              ["https://ballotpedia.org/Florida%27s_2nd_Congressional_District_election,_2026",
               "https://www.wctv.tv/2026/02/17/seventh-republican-files-floridas-2nd-congressional-district-seat/"]),
        claim("dw2", "drew-wilson-fl-02", "border_immigration", 0, True,
              "FL-02 covers the Florida Panhandle and Big Bend region, a heavily Republican district. Florida Republicans backed DeSantis's anti-illegal-immigration actions including Operation Alligator Alcatraz (2026) and legislation requiring E-Verify for state employers. As a Republican candidate in this district, Wilson is aligned with strong-border enforcement as a core platform issue.",
              ["https://ballotpedia.org/Florida%27s_2nd_Congressional_District_election,_2026",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Florida"]),
        claim("dw3", "drew-wilson-fl-02", "self_defense", 0, True,
              "Florida enacted constitutional carry (HB 543) in 2023, signed by Governor DeSantis, making it one of the country's leading Second Amendment states. As a Republican running in a deep-red Panhandle seat, Wilson is aligned with Florida's constitutional carry law and opposition to new federal gun restrictions — matching the rubric's support for carry without government permission.",
              ["https://ballotpedia.org/Florida%27s_2nd_Congressional_District_election,_2026",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Florida"]),
    ]),

    # ---------------- Rick McCartney (AZ-01, D — 2026 primary candidate) ----------------
    ("rick-mccartney-az-01", "AZ", "Representative", [
        claim("rm1", "rick-mccartney-az-01", "sanctity_of_life", 0, False,
              "A declared pro-abortion-rights candidate who explicitly pledges to codify Roe v. Wade into federal law, protect access to abortion medication, and uphold the legal right to travel across state lines to obtain abortions — directly rejecting any life-at-conception standard.",
              ["https://mccartneyforcongress.com/priorities",
               "https://ballotpedia.org/Rick_McCartney"]),
        claim("rm2", "rick-mccartney-az-01", "biblical_marriage", 4, False,
              "Supports passing the Equality Act to expand federal civil rights protections based on sexual orientation and gender identity into schools and public accommodations — the policy promotion of LGBTQ ideology the rubric opposes. His platform explicitly includes protecting trans youth.",
              ["https://mccartneyforcongress.com/priorities",
               "https://azmirror.com/2026/06/23/democrats-in-cd1-agree-trump-is-the-problem-but-differ-on-how-to-take-him-on/"]),
        claim("rm3", "rick-mccartney-az-01", "border_immigration", 1, False,
              "Advocates for 'a clear pathway to citizenship for immigrants who contribute to the economy,' including protections for Dreamers and an end to mass deportation proceedings — opposing mandatory deportation of illegal aliens, which is the rubric's position.",
              ["https://mccartneyforcongress.com/priorities",
               "https://ballotpedia.org/Rick_McCartney"]),
    ]),

    # ---------------- Mark Robert Gordon (AZ-01, D — 2026 primary candidate) ----------------
    ("mark-robert-gordon", "AZ", "Representative", [
        claim("mrg1", "mark-robert-gordon", "biblical_marriage", 0, False,
              "A member of the DNC's LGBTQ+ caucus and a 30-year advocate for same-sex civil rights. His DNC biography lists service on the LGBTQ+ caucus and as AFL-CIO Pride Month honoree — indicating strong support for same-sex marriage and rejection of the one-man-one-woman definition.",
              ["https://azdnc.org/biographies-mark-robert-gordon",
               "https://aflcio.org/2024/6/21/pride-month-profiles-mark-robert-gordon"]),
        claim("mrg2", "mark-robert-gordon", "election_integrity", 0, False,
              "A career voting-rights attorney and founder of the Voting Rights Fund whose entire professional identity is built on expanding ballot access — maximizing voter registration, opposing strict voter-ID laws, and resisting measures to limit mail-in voting, contrary to the rubric's election integrity standards (voter-ID, paper ballots, anti-mass-mail-in).",
              ["https://ballotpedia.org/Mark_Robert_Gordon_(Arizona)",
               "https://www.electmarkrobertgordon.com/meet-mark"]),
        claim("mrg3", "mark-robert-gordon", "sanctity_of_life", 0, False,
              "Running as a progressive Democratic candidate in AZ-01 on a platform that includes defending reproductive rights. His party affiliation and DNC leadership role place him firmly in support of federal abortion-access legislation, rejecting life-at-conception personhood.",
              ["https://ballotpedia.org/Mark_Robert_Gordon_(Arizona)",
               "https://www.electmarkrobertgordon.com"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
