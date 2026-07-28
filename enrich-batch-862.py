#!/usr/bin/env python3
"""Enrichment batch 862: hand-curated claims for 3 Virginia federal candidates.

Targets from the bottom of the alphabet (VA state) with 0-2 existing claims.
Mix: David Williams (VA Senate R, 0 claims), Shannon Taylor (VA-01 D, +3 new),
Rob Tracinski (VA-05 D, +2 new). All claims sourced from reliable public sources.

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
    # ---------------- David Williams (VA-R, US Senate 2026 candidate) ----------------
    ("david-williams", "VA", "Senate", [
        claim("dw862a", "david-williams", "border_immigration", 0, True,
              "Explicitly prioritizes border security and military-level enforcement: campaign platform calls for stopping \"the flow of deadly drugs like fentanyl, crack down on cartel networks, and reverse policies that encourage lawlessness,\" and states that illegal immigration \"undercuts American workers and drives down wages.\" Backed as a partner to Trump on border policy.",
              ["https://www.washingtonexaminer.com/news/campaigns/congressional/3886732/navy-marine-veteran-david-williams-virginia-senate-campaign-oust-mark-warner/",
               "https://www.cvilletomorrow.org/qa-with-virginias-three-republican-primary-candidates-for-u-s-senate/"]),
        claim("dw862b", "david-williams", "christian_liberty", 0, True,
              "OnTheIssues records Williams as \"Strongly Favors\" the position that America was founded on Christian values. His campaign consistently uses \"faith, family, freedom, and the flag\" as its thematic core, stating \"his faith continues to guide his life and leadership today.\" Opened at least one campaign event with prayer.",
              ["https://www.ontheissues.org/Senate/David_Williams.htm",
               "https://www.prismnews.com/local/goochland-va/combat-veteran-david-williams-brings-senate-campaign"]),
        claim("dw862c", "david-williams", "economic_stewardship", 2, True,
              "Platforms explicitly on \"limited government\" and \"a smaller, more accountable federal government,\" criticizing rising taxes as harmful to Virginians and aligning with fiscal-restraint priorities over deficit spending.",
              ["https://cardinalnews.org/2026/06/19/three-republicans-seek-u-s-senate-nomination-to-face-warner-all-cite-ties-to-trump/",
               "https://www.davidwilliamsforva.com/"]),
    ]),

    # ---------------- Shannon Taylor (VA-01 D, US Representative 2026 candidate) ----------------
    ("shannon-taylor", "VA", "Representative VA-01", [
        claim("st862a", "shannon-taylor", "self_defense", 1, False,
              "Endorsed by the Giffords gun-safety organization; publicly supports universal background checks, a ban on ghost guns, and safe-storage laws (championed a safe-storage ordinance in Henrico after a teen used an unsecured firearm to shoot a 13-year-old) — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://giffords.org/candidates/shannon-taylor/",
               "https://ballotpedia.org/Shannon_Taylor_(Virginia)/"]),
        claim("st862b", "shannon-taylor", "biblical_marriage", 0, False,
              "Explicitly supports removing Virginia's same-sex marriage ban from the state constitution, stating she backs \"removing the egregious and illegal ban on same-sex marriage from the Virginia Constitution\" in her 2025 attorney-general-race questionnaire — rejecting the one-man-one-woman definition.",
              ["https://virginiamercury.com/2025/06/16/virginia-attorney-general-race-questionnaire-shannon-taylor/",
               "https://emilyslist.org/candidate/shannon-taylor/"]),
        claim("st862c", "shannon-taylor", "biblical_marriage", 2, False,
              "Directly attacked Governor Youngkin's transgender student policies (pronoun/name rules) as \"following Donald Trump's playbook to target our children for his own extreme political agenda\" and labeled the attorney general's opposition to Biden-era Title IX transgender rules a \"bigoted action against LGBTQ+ Virginians\" — rejecting the rubric's opposition to transgender ideology in schools.",
              ["https://www.13newsnow.com/article/news/politics/elections/henrico-county-commonwealths-attorney-shannon-taylor-2025-virginia-attorney-general-race/291-65d69450-b4a0-4966-b74d-15e05e64b0c1",
               "https://virginiamercury.com/2025/06/16/virginia-attorney-general-race-questionnaire-shannon-taylor/"]),
    ]),

    # ---------------- Mo Seifeldein (VA-08 D, US Representative 2026 candidate) ----------------
    ("mo-seifeldein", "VA", "Representative VA-08", [
        claim("ms862a", "mo-seifeldein", "sanctity_of_life", 0, False,
              "Supports codifying reproductive rights into federal law and has called for repealing the Comstock Act (an 1873 anti-obscenity law being used to restrict abortion medication), framing abortion access as a civil right rather than recognizing any personhood standard from conception.",
              ["https://moforcongress.com/issues/",
               "https://virginiamercury.com/voter-guides/contests/general-election-8th-district/",
               "https://patch.com/virginia/oldtownalexandria/mo-seifeldein-running-democratic-va-8-primary-candidate-questionnaire"]),
        claim("ms862b", "mo-seifeldein", "self_defense", 1, False,
              "As an Alexandria City Council member, participated in the council's unanimous June 2020 vote to ban guns, ammunition, and related items from all city buildings, parks, recreation centers, and streets during permitted public events — making Alexandria the first Virginia city to use a new state law to prohibit firearms on city property.",
              ["https://www.washingtonpost.com/local/virginia-politics/alexandria-bans-guns-ammunition-in-city-buildings-parks-and-recreation-centers/2020/06/20/0a17658e-b30a-11ea-856d-5054296735e5_story.html",
               "https://alextimes.com/2020/06/council-prohibits-guns-on-city-property/"]),
    ]),

    # ---------------- Rob Tracinski (VA-05 D, US Representative 2026 candidate) ----------------
    ("rob-tracinski", "VA", "Representative VA-05", [
        claim("rt862a", "rob-tracinski", "sanctity_of_life", 0, False,
              "Opposes any state prohibition on abortion, arguing in published writings that a first-trimester fetus \"is not an independent being with rights\" and that post-Dobbs state bans would cause \"national chaos\" analogous to the slavery crisis — framing abortion restriction as a violation of individual rights and resisting any state control over the decision.",
              ["https://tracinskiletter.substack.com/p/the-substance-of-due-process",
               "https://discoursemagazine.com/ideas/2022/06/24/federalism-has-its-limits-and-abortion-will-soon-test-them"]),
        claim("rt862b", "rob-tracinski", "biblical_marriage", 0, False,
              "Explicitly supported same-sex marriage in his published writings as a matter of equal individual rights, arguing against any legal framework that withholds recognition from same-sex couples — directly rejecting the one-man-one-woman definition.",
              ["https://thefederalist.com/2014/10/27/gay-marriage-and-the-right-to-be-wrong/",
               "https://ballotpedia.org/Robert_Tracinski"]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
