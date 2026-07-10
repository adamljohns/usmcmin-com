#!/usr/bin/env python3
"""Enrichment batch 612: 2 additional claims each for 5 active 2026 federal House candidates.

archetype_curated bucket fully exhausted; targets evidence_curated candidates at 3 prior
claims, adding 2 new claims each in DISTINCT rubric categories. Bottom-of-alphabet states:
TN, SC, MT.

Candidates (all R):
  Jason Knight          (TN-07) — Montgomery County Commissioner, 2026 R candidate open seat
  Mark Smith            (SC-01) — SC state rep (Dist. 99), 2026 R candidate, lost runoff
  Jenny Costa Honeycutt (SC-01) — county councilmember, 2026 R nominee (won June 23 runoff)
  Al Olszewski          (MT-01) — physician/former MT state senator, 2026 R candidate
  Aaron Flint           (MT-01) — conservative radio host, 2026 R nominee (won June 2 primary)

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ----------- Jason Knight (TN-07, R) -----------
    ("jason-knight-tn-07", "TN", "TN-07", [
        claim("jk4", "jason-knight-tn-07", "sanctity_of_life", 0, True,
              "Self-describes as 'very pro-life' and campaigns in Tennessee, which enacted one of the nation's strictest abortion bans (the Human Life Protection Act, effective 2022, protecting life from fertilization) — reflecting a life-from-conception philosophical alignment while holding that states rather than Congress should be the venue for codifying it.",
              ["https://nashvillebanner.com/2025/09/10/jason-knight-district-7-special-election/",
               "https://ballotpedia.org/Jason_Knight_(Tennessee)"]),
        claim("jk5", "jason-knight-tn-07", "border_immigration", 1, True,
              "In his candidacy declaration called it 'imperative' that local, state, and federal law enforcement 'work together to deport illegal immigrants, especially those who have been previously convicted of crimes or pose a national security risk,' and praised the One Big Beautiful Bill's border-security funding as a measure he would support — a deportation-first enforcement posture.",
              ["https://www.ksgazette.com/jason-knight-declares-candidacy-for-7th-congressional-district/",
               "https://ballotpedia.org/Jason_Knight_(Tennessee)"]),
    ]),

    # ----------- Mark Smith (SC-01, R) -----------
    ("mark-smith-sc-01", "SC", "SC-01", [
        claim("ms4", "mark-smith-sc-01", "border_immigration", 1, True,
              "At the SC-01 GOP runoff debate (June 2026) pledged to send back 'every single one of those illegal aliens that came into our country' and answered 'no' on iVoterGuide when asked whether he would support a pathway for undocumented immigrants with no criminal record — a no-amnesty, mandatory-deportation posture.",
              ["https://www.live5news.com/2026/06/18/councilwoman-jenny-costa-honeycutt-state-rep-mark-smith-face-off-gop-1st-district-runoff-debate/",
               "https://ivoterguide.com/candidate/53464/race/27670/election/1421"]),
        claim("ms5", "mark-smith-sc-01", "biblical_marriage", 2, True,
              "Stated on iVoterGuide 'Biological males should not be allowed to participate in women's sports or occupy biological women's spaces whether it be bathrooms, locker rooms, sorority houses, women's shelters, or prison'; as a SC state legislator cosponsored both the Save Women's Sports Act (2022, signed into law) and the Student Physical Privacy Act (2026, ratified May 14), barring transgender students from using opposite-sex facilities in K-12 and public universities.",
              ["https://ivoterguide.com/candidate/53464/race/27670/election/1421",
               "https://www.scstatehouse.gov/member.php?code=1724999793"]),
    ]),

    # ----------- Jenny Costa Honeycutt (SC-01, R) -----------
    ("jenny-costa-honeycutt", "SC", "SC-01", [
        claim("jcn4", "jenny-costa-honeycutt", "self_defense", 1, True,
              "Brands herself 'a proven free speech advocate and defender of the Second Amendment' and declares 'The Bill of Rights is not negotiable — and she will ensure it remains fully protected' — an explicit constitutional-originalist posture that opposes any legislative erosion of Second Amendment rights including red-flag laws, assault-weapon bans, and magazine restrictions.",
              ["https://www.jennycostahoneycutt.com/platform",
               "https://www.nrcc.org/2026/06/23/nrcc-statement-on-sc-01/"]),
        claim("jcn5", "jenny-costa-honeycutt", "border_immigration", 1, True,
              "Explicitly opposes amnesty ('I do not support amnesty'), campaigns on 'stopping the flow of deadly drugs like fentanyl and criminal illegal aliens from harming our families,' and called Trump's border enforcement record 'one of the most successful things that Trump has done in this administration' — a no-amnesty, enforcement-first immigration posture.",
              ["https://www.live5news.com/2026/06/18/councilwoman-jenny-costa-honeycutt-state-rep-mark-smith-face-off-gop-1st-district-runoff-debate/",
               "https://www.jennycostahoneycutt.com/platform"]),
    ]),

    # ----------- Al Olszewski (MT-01, R) -----------
    ("al-olszewski", "MT", "MT-01", [
        claim("ao4", "al-olszewski", "economic_stewardship", 2, True,
              "Campaigns on mandatory fiscal restraint: 'The federal government must stop deficit spending that devalues the dollar through inflation,' endorses a balanced-budget amendment, and pledges to 'cut government spending, reduce the national debt and pass legislation to finally require a balanced budget' — a structural anti-deficit commitment aligned with the rubric's balanced-budget standard.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/al-doc-olszewski/",
               "https://alformontana.com/"]),
        claim("ao5", "al-olszewski", "border_immigration", 0, True,
              "Pledges to 'fight to secure our southern border by finishing Trump's wall to stop the influx of illegal immigrants who are entering the United States' and opposes amnesty, citizenship, or work visas for those who entered illegally — a wall-first, no-amnesty border posture matching the rubric's wall-and-military standard.",
              ["https://alformontana.com/",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/al-doc-olszewski/"]),
    ]),

    # ----------- Aaron Flint (MT-01, R) — 2026 R nominee -----------
    ("aaron-flint", "MT", "MT-01", [
        claim("af4", "aaron-flint", "sanctity_of_life", 0, True,
              "Declared 'I am pro-life' at the May 2026 Glacier Country Pachyderm Forum; on iVoterGuide supports enforcing the Comstock Act (banning interstate transport of abortion-inducing drugs) and states abortion providers including Planned Parenthood should receive no taxpayer funds from any level of government — a firm pro-life policy floor across executive enforcement and funding levers.",
              ["https://dailyinterlake.com/news/2026/may/10/republicans-jockey-for-chance-to-represent-western-montana/",
               "https://ivoterguide.com/candidate/91396/race/27492/election/1419"]),
        claim("af5", "aaron-flint", "economic_stewardship", 2, True,
              "Told iVoterGuide 'The government should cut spending in order to reduce the national debt' and at the April 2026 Bozeman debate argued for single-subject appropriations bills through regular order ('If they can't get a budget done, they shouldn't get paid') and criticized overseas foreign-aid spending as going 'directly against American interests' — a government-downsizing, fiscal-accountability posture.",
              ["https://ivoterguide.com/candidate/91396/race/27492/election/1419",
               "https://montanafreepress.org/2026/04/21/gop-congressional-candidates-aaron-flint-and-al-olszewski-face-off-in-bozeman/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
