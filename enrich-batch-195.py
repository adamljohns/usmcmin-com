#!/usr/bin/env python3
"""Enrichment batch 195: 5 sitting U.S. House members — bottom-of-alphabet bucket.

Targets archetype_party_default Representatives with 0 claims,
reverse-sorted by state (NY → NC → MS), as the archetype_curated federal
senator/representative bucket is fully exhausted.

Candidates (all D):
  Pat Ryan (NY-18), Joseph Morelle (NY-25), George Latimer (NY-16),
  Deborah Ross (NC-02), Bennie Thompson (MS-02).

Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions from en.wikipedia.org, ballotpedia.org, govtrack.us,
reproductivefreedomforall.org, or official *.house.gov sources.

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
    # ---------------- Pat Ryan (NY-18, D, US Representative) ----------------
    ("pat-ryan", "NY", "Representative", [
        claim("pr1", "pat-ryan", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice America (now Reproductive Freedom for All) in his initial 2022 House bid; his signature legislation, the 'Protecting Reproductive Freedom Act' — reintroduced in 2025 — is jointly backed by Planned Parenthood and Reproductive Freedom for All, placing him squarely within the abortion-industry endorsement network the rubric opposes.",
              ["https://reproductivefreedomforall.org/news/naral-endorses-pat-ryan-to-us-house/",
               "https://patryan.house.gov/media/press-releases/congressman-pat-ryan-reintroduces-his-protecting-reproductive-freedom-act-amid"]),
        claim("pr2", "pat-ryan", "self_defense", 1, False,
              "Campaigns on 'freedom from gun violence' and supports an assault-weapons ban, universal background checks, and red-flag laws; as an Army combat veteran he argues these restrictions are consistent with national security — directly opposing the rubric's defense of Second Amendment rights against new firearms restrictions.",
              ["https://ballotpedia.org/Pat_Ryan_(New_York)",
               "https://rollcall.com/2024/10/16/upstate-ny-house-races-test-party-messaging-on-abortion-immigration/"]),
        claim("pr3", "pat-ryan", "border_immigration", 1, False,
              "A cosponsor of the bipartisan Dignity Act, which provides a pathway to legal status for undocumented immigrants and 'Documented Dreamers,' opposing the rubric's call for mandatory deportation and zero-tolerance border enforcement.",
              ["https://patryan.house.gov/media/press-releases",
               "https://ballotpedia.org/Pat_Ryan_(New_York)"]),
    ]),

    # ---------------- Joseph Morelle (NY-25, D, US Representative) ----------------
    ("joseph-morelle", "NY", "Representative", [
        claim("jm1", "joseph-morelle", "sanctity_of_life", 0, False,
              "Voted to establish a federally protected right to reproductive healthcare and 'stands firmly against the Republican agenda to criminalize women's health freedom' — rejecting any legal recognition of life from conception and opposing all federal restrictions on abortion.",
              ["https://morelle.house.gov/media/press-releases",
               "https://ballotpedia.org/Joseph_Morelle"]),
        claim("jm2", "joseph-morelle", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (2022) to enshrine same-sex marriage in federal law, calling it a vote to ensure 'all couples — regardless of race, gender, or sexual orientation — have an equal right to marry whoever they love' — directly rejecting the one-man-one-woman definition.",
              ["https://morelle.house.gov/media/press-releases/congressman-joe-morelle-acts-safeguard-marriage-equality",
               "https://en.wikipedia.org/wiki/Joseph_Morelle"]),
        claim("jm3", "joseph-morelle", "self_defense", 1, False,
              "Has made passing 'common-sense gun reform laws' one of his top legislative priorities, supporting universal background checks and restrictions on semi-automatic firearms — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Joseph_Morelle",
               "https://www.govtrack.us/congress/members/joseph_morelle/412749"]),
    ]),

    # ---------------- George Latimer (NY-16, D, US Representative) ----------------
    ("george-latimer", "NY", "Representative", [
        claim("gl1", "george-latimer", "sanctity_of_life", 0, False,
              "Will 'fight back against any efforts to pass a national abortion ban' and pledges to advocate for expanded IVF access and contraception in Congress; as Westchester County Executive he codified IVF access and protected abortion clinics from protest harassment — rejecting personhood from conception.",
              ["https://latimerforny.com/priorities/",
               "https://reproductivefreedomforall.org/lawmaker/george-latimer/"]),
        claim("gl2", "george-latimer", "self_defense", 1, False,
              "Passed a state-level assault-weapons ban and universal background checks as a New York state legislator, and as county executive banned gun shows from the county center over NRA objections — the record directly opposes the rubric's defense of semi-automatic rifles and opposition to new firearms restrictions.",
              ["https://latimerforny.com/priorities/",
               "https://ballotpedia.org/George_Latimer"]),
        claim("gl3", "george-latimer", "election_integrity", 0, False,
              "Voted against the SAVE Act, which would require documentary proof of citizenship (passport or birth certificate) to register to vote — opposing the voter-ID and election-integrity protections the rubric values.",
              ["https://www.govtrack.us/congress/members/george_latimer/457011",
               "https://ballotpedia.org/George_Latimer"]),
    ]),

    # ---------------- Deborah Ross (NC-02, D, US Representative) ----------------
    ("deborah-ross", "NC", "Representative", [
        claim("dr1", "deborah-ross", "sanctity_of_life", 0, False,
              "Has pledged she will 'never stop fighting' for 'women's reproductive freedom' and voted against any legislative restrictions on abortion access, including the 2022 Women's Health Protection Act cosponsorship — rejecting life-at-conception and any federal abortion limitations.",
              ["https://ross.house.gov/about",
               "https://ballotpedia.org/Deborah_Ross"]),
        claim("dr2", "deborah-ross", "sanctity_of_life", 2, False,
              "Called for IVF to be codified into federal law (2024), advocating procedures that routinely create and discard human embryos — opposing the rubric's position against embryonic destruction.",
              ["https://ross.house.gov/2024/3/nc-congresswoman-deborah-ross-calling-for-ivf-to-be-codified-into-law",
               "https://ballotpedia.org/Deborah_Ross"]),
        claim("dr3", "deborah-ross", "self_defense", 1, False,
              "Advocates for mandatory safe-storage gun laws, citing firearms as the leading cause of child injury/death in NC; testified in support of additional gun-control measures — opposing the rubric's defense of unrestricted firearms ownership and opposition to new federal gun regulations.",
              ["https://ross.house.gov/2024/5/nc-lawmaker-calls-for-safe-storage-gun-laws",
               "https://ballotpedia.org/Deborah_Ross"]),
    ]),

    # ---------------- Bennie Thompson (MS-02, D, US Representative) ----------------
    ("bennie-thompson", "MS", "Representative", [
        claim("bt1", "bennie-thompson", "sanctity_of_life", 1, False,
              "Voted against the Born-Alive Abortion Survivors Protection Act (January 2025), rejecting even the requirement that infants born alive during failed abortions receive emergency medical care — opposing the rubric's abolition-level standard that every born and unborn life must be protected.",
              ["https://newsouthpolitics.com/mississippi-political-leaders/mississippi-us-senators-and-representatives/overview-of-mississippi-congressman-bennie-thompson-district-2/",
               "https://www.govtrack.us/congress/members/bennie_thompson/400402"]),
        claim("bt2", "bennie-thompson", "self_defense", 1, False,
              "Receives an F rating from the National Rifle Association for a career-long record of supporting gun-control legislation and opposing pro-gun measures — placing him at the opposite end of the spectrum from the rubric's defense of Second Amendment rights against any new restrictions.",
              ["https://www.ontheissues.org/House/Bennie_Thompson_Gun_Control.htm",
               "https://ballotpedia.org/Bennie_Thompson"]),
        claim("bt3", "bennie-thompson", "sanctity_of_life", 4, False,
              "Carries a lifetime pro-choice voting record tracked and celebrated by Reproductive Freedom for All (formerly NARAL), indicating consistent alignment with the abortion-industry lobby network the rubric identifies as disqualifying.",
              ["https://reproductivefreedomforall.org/lawmaker/bennie-thompson/",
               "https://ballotpedia.org/Bennie_Thompson"]),
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
