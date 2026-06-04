#!/usr/bin/env python3
"""Enrichment batch 33: hand-curated claims for 4 candidates.

Targets archetype_curated candidates (bottom-of-alphabet bucket) with 0 claims.
Mix (2 R / 2 D): Rodney Glassman (AZ-R, AG candidate), Mike Waltz (US-R, UN Ambassador),
Mike McGuire (CA-D, CA-01), Troy Jackson (ME-D, Governor candidate).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions / voting record.

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
    # ---------------- Rodney Glassman (AZ-R, AG Candidate) ----------------
    ("rodney-glassman-ag", "AZ", "Attorney", [
        claim("rg1", "rodney-glassman-ag", "border_immigration", 0, True,
              "Advocates an immediate increase of National Guard presence at the U.S.-Mexico border in Arizona, expansion of the Arizona Rangers, and prosecution of cartel members 'to the fullest extent of the law' — aligning with the rubric's wall-and-military border posture.",
              ["https://azpbs.org/azvotes/2026/05/arizona-attorney-general-republican-candidate-rodney-glassman/",
               "https://ballotpedia.org/Rodney_Glassman"]),
        claim("rg2", "rodney-glassman-ag", "border_immigration", 1, True,
              "Proposes establishing 'a new legal mechanism to expeditiously adjudicate' massive immigration caseloads, blaming inherited backlogs on the Biden administration — consistent with a mandatory-removal, fast-track-deportation posture.",
              ["https://azpbs.org/azvotes/2026/05/arizona-attorney-general-republican-candidate-rodney-glassman/",
               "https://rodneyglassman.com/"]),
        claim("rg3", "rodney-glassman-ag", "sanctity_of_life", 4, True,
              "States publicly that abortion providers, including Planned Parenthood, should not receive funds from federal, state, or local governments (including Title X grants), and as a Republican candidate has accepted no funds from Planned Parenthood, NARAL, or EMILY's List.",
              ["https://ivoterguide.com/candidate/67568/race/17895/election/904",
               "https://ballotpedia.org/Rodney_Glassman"]),
    ]),

    # ---------------- Mike Waltz (US-R, UN Ambassador) ----------------
    ("mike-waltz", "US", "Ambassador", [
        claim("mw1", "mike-waltz", "sanctity_of_life", 0, True,
              "Earned a 100% rating from the National Right to Life Committee (2023-24) and voted for HR 26, the Born-Alive Abortion Survivors Protection Act, in 2023. Stated publicly that Roe v. Wade was 'overreaching and unconstitutional legislating from the Supreme Court,' affirming the pro-life position that life deserves protection before birth.",
              ["https://en.wikipedia.org/wiki/Mike_Waltz",
               "https://www.congress.gov/bill/118th-congress/house-bill/26"]),
        claim("mw2", "mike-waltz", "self_defense", 1, True,
              "NRA-endorsed since his first election in 2018; the NRA called him 'a staunch supporter of the Second Amendment' who would 'work hard to protect our constitutional freedoms.' Consistent pro-gun voting record throughout six years in the House (FL-06, 2019-2025).",
              ["https://www.nrapvf.org/articles/20181107/nra-congratulates-waltz-in-floridas-6th-congressional-district-race",
               "https://ballotpedia.org/Michael_Waltz"]),
        claim("mw3", "mike-waltz", "foreign_policy_restraint", 4, True,
              "As U.S. Ambassador to the United Nations (confirmed September 2025), Waltz declared he would seek fundamental reform of the United Nations, stating the body had 'drifted from its core mission of peacemaking' — a posture aligned with the rubric's opposition to UN institutional expansion and entanglement.",
              ["https://usun.usmission.gov/ambassador-michael-waltz/",
               "https://ballotpedia.org/Confirmation_process_for_Michael_Waltz_for_ambassador_to_the_United_Nations"]),
    ]),

    # ---------------- Mike McGuire (CA-D, CA-01) ----------------
    ("mike-mcguire-ca-01", "CA", "Representative", [
        claim("mm1", "mike-mcguire-ca-01", "sanctity_of_life", 0, False,
              "Supports unrestricted abortion access; as California Senate President pro Tempore championed state investment to keep Planned Parenthood health centers open and reacted to the draft Dobbs decision as 'horrifying,' rejecting any personhood-from-conception standard. His 2026 House campaign platform explicitly includes keeping Planned Parenthood open.",
              ["https://www.votemikemcguire.com/",
               "https://ballotpedia.org/Mike_McGuire",
               "https://www.plannedparenthoodaction.org/planned-parenthood-affiliates-california/media/planned-parenthood-congratulates-new-senate-pro-tem-mike-mcguire"]),
        claim("mm2", "mike-mcguire-ca-01", "sanctity_of_life", 4, False,
              "Endorsed and celebrated by Planned Parenthood Affiliates of California upon his swearing-in as Senate President pro Tempore, and actively steered state funds to Planned Parenthood health centers as pro tem — a recipient of deep institutional support from the abortion-industry network the rubric opposes.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-affiliates-california/media/planned-parenthood-congratulates-new-senate-pro-tem-mike-mcguire"]),
        claim("mm3", "mike-mcguire-ca-01", "biblical_marriage", 4, False,
              "Endorsed by Equality California — the state's leading LGBTQ-advocacy organization — for his 2026 U.S. House race, reflecting his consistent support for LGBTQ policy promotion in schools and public life throughout his legislative career.",
              ["https://www.progressivevotersguide.com/california/2026/primary/mike-mcguire",
               "https://ballotpedia.org/Mike_McGuire"]),
    ]),

    # ---------------- Troy Jackson (ME-D, Governor Candidate) ----------------
    ("troy-jackson-gov", "ME", "Governor", [
        claim("tj1", "troy-jackson-gov", "sanctity_of_life", 0, False,
              "Principal sponsor of Maine LD 1619 (2023), widely described as one of the most expansive abortion-rights laws in the U.S., which removed the state's ban on late-term abortions and stripped criminal penalties from abortion providers — explicitly rejecting protection of the unborn from conception.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-maine-action-fund/press-releases/patient-advocates-reproductive-rights-groups-faith-leaders-praise-maine-senate-vote-to-enact-ld-1619",
               "https://www.ontheissues.org/governor/Troy_Jackson_Abortion.htm"]),
        claim("tj2", "troy-jackson-gov", "sanctity_of_life", 4, False,
              "Received a 100% score from Planned Parenthood for at least seven consecutive years (2018-2024), having voted in support of reproductive care on every bill that came before the Maine legislature, placing him squarely inside the abortion-industry endorsement network.",
              ["https://www.ontheissues.org/governor/Troy_Jackson_Abortion.htm",
               "https://www.penbaypilot.com/article/reproductive-rights-will-have-champion-troy-jackson-governor/269499"]),
        claim("tj3", "troy-jackson-gov", "self_defense", 1, False,
              "Supports a suite of gun-control measures — red-flag laws, expanded background checks, and mandatory waiting periods — as part of his 2026 gubernatorial platform, directly opposing the rubric's defense of unrestricted Second Amendment rights against red-flag laws and new restrictions.",
              ["https://www.mainepublic.org/politics/2026-04-17/your-vote-2026-profile-troy-jackson-democrat-for-governor"]),
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
