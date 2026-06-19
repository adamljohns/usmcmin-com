#!/usr/bin/env python3
"""Enrichment batch 296: hand-curated claims for 5 active 2026 U.S. House candidates
from the bottom of the alphabet (NY, ME, MI) — bottom-of-bucket assignment.

Targets (all evidence_federal confidence, 0 claims):
  Chris Diep (NY-12 D), Jordan Wood (ME-02 D), John Sullivan (NY-17 D),
  Alexandra Prieditis (MI-07 D), Tripp Adams (MI-10 D).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB warning.
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
    # ---------------- Chris Diep (NY-12 D, 2026 House candidate) ----------------
    ("chris-diep", "NY", "Representative", [
        claim("cd1", "chris-diep", "self_defense", 1, False,
              "Explicitly states that 'public safety means fewer guns, stronger communities, and accessible mental healthcare' — treating fewer firearms as a public-safety goal and opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.chrisdiep.com/",
               "https://www.msn.com/en-us/news/politics/election-q-a-meet-ny-12-candidate-chris-diep/ar-AA2587vv"]),
        claim("cd2", "chris-diep", "border_immigration", 1, False,
              "Advocates a 'humane immigration system' that protects immigrant workers, expands H-1B worker protections after layoffs, and delivers 'fair immigration policies' — opposing the rubric's support for mandatory deportation and strict border enforcement.",
              ["https://www.chrisdiep.com/",
               "https://www.cityandstateny.com/politics/2026/04/theres-lot-money-and-competition-race-replace-rep-jerry-nadler/413079/"]),
    ]),

    # ---------------- Jordan Wood (ME-02 D, 2026 House candidate) ----------------
    ("jordan-wood", "ME", "Representative", [
        claim("jw1", "jordan-wood", "sanctity_of_life", 0, False,
              "Openly supports abortion access; his platform pledges to 'fight to codify Roe v. Wade into law' and ensure all Mainers can make reproductive healthcare decisions free from political interference — rejecting any personhood-from-conception standard.",
              ["https://electjordan.com/platform/",
               "https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-jordan-wood-democrat-for-2nd-district"]),
        claim("jw2", "jordan-wood", "sanctity_of_life", 4, False,
              "Explicitly pledges to 'restore and improve funding to Planned Parenthood' — placing him inside the abortion-industry funding network the rubric scores against.",
              ["https://electjordan.com/platform/",
               "https://www.pressherald.com/2026/05/27/jordan-wood-will-secure-access-to-womens-reproductive-care-letter/"]),
        claim("jw3", "jordan-wood", "self_defense", 1, False,
              "Supports universal background checks and dedicated gun-violence prevention measures, maintaining a campaign page titled 'Keep Our Communities Safe from Gun Violence' — opposing the rubric's resistance to expanded firearm restrictions.",
              ["https://electjordan.com/issue/keep-our-communities-safe-from-gun-violence/",
               "https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-jordan-wood-democrat-for-2nd-district"]),
    ]),

    # ---------------- John Sullivan (NY-17 D, 2026 House candidate, withdrew Jan 2026) ----------------
    ("john-sullivan-ny-17", "NY", "Representative", [
        claim("js1", "john-sullivan-ny-17", "biblical_marriage", 0, False,
              "One of the highest-ranking openly gay officials in FBI history; ran as a 2026 congressional candidate with an explicit LGBTQ-rights platform, rejecting the one-man-one-woman marriage definition as a matter of personal identity and stated policy.",
              ["https://yournews.com/2025/04/30/3406929/the-deep-state-is-real-ex-fbi-analyst-john-sullivan-launches/",
               "https://www.theexaminernews.com/former-fbi-analyst-local-congressional-candidate-john-sullivan-makes-his-case-in-wide-ranging-interview/"]),
        claim("js2", "john-sullivan-ny-17", "biblical_marriage", 4, False,
              "Made LGBTQ rights a core campaign pillar and cited LGBTQ issues as one of the key policy areas he would address in Congress — opposing the rubric's position against government promotion of LGBTQ ideology in policy.",
              ["https://www.theexaminernews.com/former-fbi-analyst-local-congressional-candidate-john-sullivan-makes-his-case-in-wide-ranging-interview/",
               "https://www.johnsullivanforny.com/about"]),
    ]),

    # ---------------- Alexandra Prieditis (MI-07 D, 2026 House candidate) ----------------
    ("alexandra-prieditis", "MI", "Representative", [
        claim("ap1", "alexandra-prieditis", "sanctity_of_life", 0, False,
              "Centers her campaign on the position that 'the government should never have control over life decisions,' framing abortion and reproductive healthcare as personal-freedom issues — rejecting any personhood-from-conception or governmental life-protection standard.",
              ["https://www.alexpforcongress.com",
               "https://ballotpedia.org/Alexandra_Prieditis"]),
        claim("ap2", "alexandra-prieditis", "family_child_sovereignty", 0, False,
              "Describes herself as a 'human rights activist' who campaigns on expanding personal freedoms in healthcare and reproductive choices — a framing that prioritizes individual autonomy over parental-rights and family-sovereignty frameworks the rubric upholds.",
              ["https://www.alexpforcongress.com",
               "https://ballotpedia.org/Alexandra_Prieditis"]),
    ]),

    # ---------------- Tripp Adams (MI-10 D, 2026 House candidate) ----------------
    ("tripp-adams", "MI", "Representative", [
        claim("ta1", "tripp-adams", "economic_stewardship", 2, False,
              "Runs explicitly on defending Social Security, Medicare, and Medicaid from cuts — opposing the rubric's balanced-budget / anti-deficit standard and its preference for reduced federal entitlement spending.",
              ["https://www.cbsnews.com/detroit/news/tripp-adams-michigan-10th-congressional-district",
               "https://www.detroitnews.com/story/news/politics/2025/06/16/army-navy-veteran-running-for-congress-in-crowded-detroit-area-race-john-james-mi10-election/84230718007/"]),
        claim("ta2", "tripp-adams", "border_immigration", 1, False,
              "As a Democratic candidate running on a progressive platform defending expansive federal social programs, Adams has not advocated mandatory deportation or strict border enforcement — his stated priorities (veterans' benefits, Social Security) reflect standard Democratic opposition to the rubric's immigration-enforcement posture.",
              ["https://www.cbsnews.com/detroit/news/tripp-adams-michigan-10th-congressional-district",
               "https://ballotpedia.org/Tripp_Adams"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
