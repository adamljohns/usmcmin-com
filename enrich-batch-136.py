#!/usr/bin/env python3
"""Enrichment batch 136: hand-curated claims for 5 low-evidence U.S. House candidates.

Targets low_evidence federal Representatives with 0 claims, taken from the
bottom of the alphabet (WA, SC, TN states).

Candidates (all R, bottom-of-alphabet): Jerrod Sessler (WA-04),
Tyler Dykes (SC-01), Natisha Brooks (TN-06),
Amanda McKinney (WA-04), Jay Reedy (TN-07).

Each claim cites >=1 reliable source and reflects 2024-2026 public
positions from ballotpedia.org, official campaign sites, yakimaherald.com,
postandcourier.com, and tennesseelookout.com.

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
    # ---------- Jerrod Sessler (WA-04, R) ----------
    ("jerrod-sessler", "WA", "Representative", [
        claim("js1", "jerrod-sessler", "sanctity_of_life", 0, True,
              "As a Christian conservative, affirms life begins at conception and believes Roe v. Wade was a constitutional error that should have been left to the states; publicly stated pro-life conviction aligns with a personhood-from-conception position.",
              ["https://www.yakimaherald.com/news/local/q-a-district-4-candidates-share-views-on-abortion-policy/article_36fe85d7-132d-5bf2-ba5c-57d3c53a56d3.html",
               "https://ivoterguide.com/candidate/59654/race/2691/election/899"]),
        claim("js2", "jerrod-sessler", "self_defense", 1, True,
              "States the Second Amendment 'shall not be infringed' and opposes all new firearm restrictions, comparing liability for firearms dealers to holding matchbox manufacturers responsible for arsonists — a strict-constructionist, anti-AWB/anti-registry stance.",
              ["https://www.jerrodforcongress.com/",
               "https://ivoterguide.com/candidate/59654/race/2691/election/899"]),
        claim("js3", "jerrod-sessler", "border_immigration", 2, True,
              "Calls for finishing the border wall, empowering ICE to deport illegal entrants immediately, and cutting state and federal funds to any sanctuary city or entity that defies immigration enforcement — a direct anti-sanctuary policy.",
              ["https://www.jerrodforcongress.com/",
               "https://washingtonstatestandard.com/tag/jerrod-sessler/"]),
    ]),

    # ---------- Tyler Dykes (SC-01, R) ----------
    ("tyler-dykes", "SC", "Representative", [
        claim("td1", "tyler-dykes", "border_immigration", 0, True,
              "Built his congressional platform on ending mass immigration, calling for a secure border wall and blaming federal open-borders policy for displacing workers, suppressing wages, and disrupting housing markets — consistent with the wall-and-military enforcement position.",
              ["https://www.postandcourier.com/beaufort-county/politics/tyler-dykes-campaign-sc1-congress/article_c255115c-45cf-430e-b4a4-160a322631e1.html",
               "https://www.live5news.com/2026/03/01/we-palmetto-meet-candidate-tyler-dykes-sc-01/"]),
        claim("td2", "tyler-dykes", "foreign_policy_restraint", 1, True,
              "Advocates non-interventionist foreign policy: 'America needs to mind our own business and stay out of the business of the whole rest of the world,' explicitly opposing overseas military entanglements — aligning with the rubric's call to end forever wars.",
              ["https://www.postandcourier.com/beaufort-county/politics/tyler-dykes-campaign-sc1-congress/article_c255115c-45cf-430e-b4a4-160a322631e1.html"]),
        claim("td3", "tyler-dykes", "economic_stewardship", 2, True,
              "Cites $40 trillion in national debt as a primary driver of his candidacy, framing deficit spending as a generational burden making it harder for young Americans to get ahead — consistent with the rubric's anti-deficit/balanced-budget position.",
              ["https://www.postandcourier.com/beaufort-county/politics/tyler-dykes-campaign-sc1-congress/article_c255115c-45cf-430e-b4a4-160a322631e1.html"]),
    ]),

    # ---------- Natisha Brooks (TN-06, R) ----------
    ("natisha-brooks", "TN", "Representative", [
        claim("nb1", "natisha-brooks", "sanctity_of_life", 3, True,
              "Supports the Born Alive Abortion Survivors Protection Act, requiring medical care for infants born alive during attempted abortions — directly opposing infanticide-by-neglect and aligning with the rubric's anti-euthanasia of the newborn position.",
              ["https://ballotpedia.org/Natisha_Brooks",
               "https://ivoterguide.com/candidate/53817/race/6830/election/704"]),
        claim("nb2", "natisha-brooks", "family_child_sovereignty", 0, True,
              "Owner-Director of The Brooks Academy, a homeschool institution serving grade-school through collegiate students; frames parental authority over education as a core value — directly embodying the rubric's parental rights and homeschool-support position.",
              ["https://ballotpedia.org/Natisha_Brooks",
               "https://mainstreetmediatn.com/articles/thewilsonpost/candidate-announcement-natisha-brooks-for-congress/"]),
        claim("nb3", "natisha-brooks", "refuse_federal_overreach", 0, True,
              "A self-described Christian conservative constitutionalist who consistently opposes federal control over local education and curricula, arguing that education policy belongs to parents and states — directly rejecting federal overreach in schools.",
              ["https://ballotpedia.org/Natisha_Brooks",
               "https://tennesseeconservativenews.com/natisha-brooks-running-for-congress-in-5th-district/"]),
    ]),

    # ---------- Amanda McKinney (WA-04, R) ----------
    ("amanda-mckinney", "WA", "Representative", [
        claim("am1", "amanda-mckinney", "self_defense", 1, True,
              "A staunch Second Amendment advocate who testified against gun restrictions, arguing that fees and mandated-training requirements function as 'taxes on constitutional rights' that disproportionately harm working families and domestic-violence victims — opposing red-flag-style or AWB-style restrictions.",
              ["https://www.mckinneyforwashington.com/",
               "https://ballotpedia.org/Amanda_McKinney_(Washington)"]),
        claim("am2", "amanda-mckinney", "border_immigration", 0, True,
              "Running as an America First Republican with firm border-security and immigration-enforcement positions; endorsed by President Trump and House Speaker Mike Johnson on a platform including barrier construction and deportation operations.",
              ["https://www.yakimaherald.com/news/local/government/elections/trump-endorses-yakimas-amanda-mckinney-for-wa-congressional-campaign/article_8f63ffb3-ab67-49a3-bff1-93b43d0a2a95.html",
               "https://ballotpedia.org/Amanda_McKinney_(Washington)"]),
        claim("am3", "amanda-mckinney", "refuse_federal_overreach", 0, True,
              "Signed the U.S. Term Limits pledge to impose constitutional term limits on Congress, committing to restrict the tenure of career politicians — a structural limit on federal legislative entrenchment consistent with the rubric's anti-federal-overreach principle.",
              ["https://termlimits.com/amanda-mckinney-pledges-to-support-congressional-term-limits/"]),
    ]),

    # ---------- Jay Reedy (TN-07, R) ----------
    ("jay-reedy", "TN", "Representative", [
        claim("jr1", "jay-reedy", "border_immigration", 2, True,
              "As a Tennessee state representative, advocated banning sanctuary cities and backed federal immigration enforcement — carrying that firm anti-sanctuary position into his 2026 congressional campaign.",
              ["https://tennesseelookout.com/2025/07/01/tennessee-republican-lawmaker-entering-congressional-race/"]),
        claim("jr2", "jay-reedy", "border_immigration", 4, True,
              "Supports blocking foreign adversaries, including China, from purchasing Tennessee farmland — an anti-foreign-adversary land-ownership stance consistent with the rubric's opposition to foreign-adversary farmland acquisition.",
              ["https://tennesseelookout.com/2025/07/01/tennessee-republican-lawmaker-entering-congressional-race/"]),
        claim("jr3", "jay-reedy", "refuse_federal_overreach", 0, True,
              "Calls for eliminating the U.S. Department of Education, stating 'The federal government needs to stay out of Tennessee's business,' and signed numerous lawsuits against federal overreach under the Obama and Biden administrations.",
              ["https://tennesseelookout.com/2025/07/01/tennessee-republican-lawmaker-entering-congressional-race/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
