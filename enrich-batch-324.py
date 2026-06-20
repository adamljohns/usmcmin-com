#!/usr/bin/env python3
"""Enrichment batch 324: hand-curated claims for 5 federal 2026 candidates.

Bottom-of-alphabet selection from the evidence_federal tier (archetype_curated
bucket exhausted). All positions sourced from iVoterGuide questionnaires,
WHYY candidate forums, campaign websites, and credible news coverage.

Targets: Joshua Sales (TN-07 D), Pablo McConnie-Saad (PA-03 D),
Kishla Askins (NE-02 D), Omed Hamid (CA-11 D), Brandon Riker (CA-48 D).

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
    # ---------------- Joshua Sales (TN-07, D) ----------------
    ("joshua-sales", "TN", "TN-07", [
        claim("js1", "joshua-sales", "industry_capture", 4, True,
              "Army-veteran challenger for TN-07 who backs the bipartisan Sanders-Grassley Audit the Pentagon Act — legislation requiring a full, independent financial audit of the Defense Department to expose wasteful defense-contractor spending — aligning with the rubric's demand for Pentagon accountability.",
              ["https://sales4congress.com/",
               "https://www.sanders.senate.gov/press-releases/news-sanders-grassley-and-colleagues-make-bipartisan-push-to-audit-the-pentagon-and-end-wasteful-spending/"]),
        claim("js2", "joshua-sales", "border_immigration", 1, False,
              "Campaigns on a 'Welcoming the Stranger Act' that would expand humanitarian pathways and create legal residency options for undocumented immigrants — directly opposing the rubric's mandatory-deportation standard for illegal-alien enforcement.",
              ["https://sales4congress.com/",
               "https://ballotpedia.org/Tennessee's_7th_Congressional_District_election,_2026"]),
        claim("js3", "joshua-sales", "foreign_policy_restraint", 1, True,
              "Runs on an anti-interventionist platform calling for reduced overseas military spending and an end to open-ended foreign wars, redirecting those resources to domestic priorities — consistent with the rubric's call to end forever wars and repeal AUMFs.",
              ["https://sales4congress.com/",
               "https://kaburbank.substack.com/p/candidates-on-the-revolution-joshua"]),
    ]),

    # ---------------- Pablo McConnie-Saad (PA-03, D) ----------------
    ("pablo-mcconnie-saad", "PA", "PA-03", [
        claim("pm1", "pablo-mcconnie-saad", "border_immigration", 1, False,
              "At a February 2026 WHYY candidate forum for Pennsylvania's 3rd Congressional District, McConnie-Saad called for abolishing ICE outright, arguing the agency was 'created for part of the weaponization of the federal government' — the opposite of the rubric's mandatory-deportation and interior-enforcement standard.",
              ["https://whyy.org/articles/pennsylvania-3rd-congressional-district-forum/",
               "https://ballotpedia.org/Pablo_McConnie-Saad"]),
        claim("pm2", "pablo-mcconnie-saad", "foreign_policy_restraint", 3, True,
              "Explicitly pledged to reject AIPAC and all corporate-PAC money, with his campaign stating the race is 'entirely people-powered — no corporate PAC money, no AIPAC, just everyday people' — satisfying the rubric's 'never took AIPAC/foreign-linked PAC' criterion.",
              ["https://www.inquirer.com/politics/philadelphia/congressional-race-fundraising-sharif-street-ala-stanford-20260202.html",
               "https://pabloforcongress.com/"]),
    ]),

    # ---------------- Kishla Askins (NE-02, D) ----------------
    ("kishla-askins", "NE", "NE-02", [
        claim("ka1", "kishla-askins", "biblical_marriage", 0, False,
              "A gay woman who has been married to her wife since 2015 and survived two DADT (Don't Ask, Don't Tell) investigations during her 30-year Navy career — her personal life and advocacy reject the one-man-one-woman marriage definition the rubric upholds.",
              ["https://www.advocate.com/politics/kishla-askins-congress-nebraska",
               "https://nebraskaexaminer.com/2025/07/15/retired-navy-veteran-kishla-askins-joins-nebraska-2nd-district-u-s-house-race/"]),
        claim("ka2", "kishla-askins", "biblical_marriage", 2, False,
              "Publicly opposes the Trump-era transgender military service ban, arguing as a clinician that 'if you are medically ready, then you should be able to serve' and that it is 'a medical diagnosis for politicians not to weigh in on' — directly rejecting the rubric's rejection-of-transgender-ideology standard.",
              ["https://nebraskaexaminer.com/2025/07/15/retired-navy-veteran-kishla-askins-joins-nebraska-2nd-district-u-s-house-race/",
               "https://www.yahoo.com/news/articles/30-years-uniform-veteran-nebraska-120003591.html"]),
    ]),

    # ---------------- Omed Hamid (CA-11, D) ----------------
    ("omed-hamid", "CA", "CA-11", [
        claim("oh1", "omed-hamid", "sanctity_of_life", 0, False,
              "On his iVoterGuide questionnaire for the 2026 CA-11 primary, Hamid stated 'abortion should remain a legal and protected healthcare option' and emphasized that 'the right of individuals to make deeply personal healthcare decisions' must not face 'government interference' — rejecting any life-at-conception or personhood standard.",
              ["https://ivoterguide.com/candidate/90310/race/25572/election/1385",
               "https://ballotpedia.org/Omed_Hamid"]),
        claim("oh2", "omed-hamid", "biblical_marriage", 0, False,
              "Stated in his 2026 iVoterGuide questionnaire that 'marriage is a legal institution that should be available to all consenting adults, regardless of gender' and that 'the government must ensure equal rights and protections under the law' — directly contradicting the one-man-one-woman definition the rubric requires.",
              ["https://ivoterguide.com/candidate/90310/race/25572/election/1385"]),
        claim("oh3", "omed-hamid", "border_immigration", 2, False,
              "Defended sanctuary-city policies in his 2026 iVoterGuide questionnaire, writing that 'sanctuary policies help build trust between local communities and law enforcement, making everyone safer' and that 'cities should be able to focus on public safety without forcing local resources into federal immigration enforcement' — opposing the anti-sanctuary standard the rubric demands.",
              ["https://ivoterguide.com/candidate/90310/race/25572/election/1385"]),
    ]),

    # ---------------- Brandon Riker (CA-48, D) ----------------
    ("brandon-riker", "CA", "CA-48", [
        claim("br1", "brandon-riker", "sanctity_of_life", 0, False,
              "Palm Springs businessman running for CA-48 who has pledged to codify Roe v. Wade into federal law, eliminating state-level protections for the unborn and rejecting the personhood-from-conception standard the rubric requires.",
              ["https://www.msn.com/en-us/news/other/q-a-meet-brandon-riker-candidate-for-california-s-48th-congressional-district/ar-AA22EdhM",
               "https://ballotpedia.org/Brandon_Riker_(California)"]),
        claim("br2", "brandon-riker", "biblical_marriage", 2, False,
              "Has declared 'I will always stand with the trans community,' called gender-affirming care 'medically necessary,' and pledged to pass the federal Equality Act extending gender-identity protections into employment, housing, and public accommodations — directly opposing the rubric's standard of rejecting transgender ideology.",
              ["https://www.msn.com/en-us/news/other/q-a-meet-brandon-riker-candidate-for-california-s-48th-congressional-district/ar-AA22EdhM",
               "https://rikerforcongress.com/news/"]),
        claim("br3", "brandon-riker", "self_defense", 1, False,
              "Received an endorsement from Gun Sense Voters, a gun-control PAC that backs candidates supporting universal background checks, red-flag laws, and magazine-capacity restrictions — the direct opposite of the rubric's anti-red-flag, anti-AWB, anti-registry standard.",
              ["https://ballotpedia.org/Brandon_Riker_(California)",
               "https://www.msn.com/en-us/news/other/q-a-meet-brandon-riker-candidate-for-california-s-48th-congressional-district/ar-AA22EdhM"]),
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
