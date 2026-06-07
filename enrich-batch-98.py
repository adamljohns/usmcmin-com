#!/usr/bin/env python3
"""Enrichment batch 98: hand-curated claims for 4 candidates (GA/CA).

Targets archetype_curated candidates with 0 evidence claims, taken from the
bottom of the remaining alphabet bucket (MA/GA/FL/CA).  Federal bucket is
exhausted (2 candidates remain with no findable public record); batch falls
back to well-documented state executives per protocol.

Mix (4 R): Brian Kemp (GA-Gov-R), Brad Raffensperger (GA-SoS-R),
Chris Carr (GA-AG-R), Steve Hilton (CA-Gov-R).
Each claim cites >=1 reliable source and reflects 2024-2026 record/positions.

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{slug}-{category}-{q_idx}-{cid}",
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


TARGETS = [
    # -------- Brian Kemp (GA, Governor, R) --------
    ("brian-kemp", "GA", "Governor", [
        claim("bk1", "brian-kemp", "self_defense", 0, True,
              "Signed the Georgia Constitutional Carry Act in April 2022, making Georgia the 25th state to allow most adults to carry a handgun in public without a government-issued license or training requirement — direct fulfillment of the constitutional-carry standard the rubric upholds.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://en.wikipedia.org/wiki/Brian_Kemp"]),
        claim("bk2", "brian-kemp", "sanctity_of_life", 0, True,
              "In 2019 signed the Living Infants Fairness and Equality (LIFE) Act, one of the nation's most protective fetal-heartbeat laws, prohibiting most abortions after a heartbeat is detectable at roughly six weeks; upon Dobbs (2022) the law immediately took effect, placing Georgia among the most protective states for unborn life.",
              ["https://en.wikipedia.org/wiki/Brian_Kemp",
               "https://www.foxnews.com/politics/georgia-gov-brian-kemp-signs-controversial-heartbeat-bill-into-law"]),
        claim("bk3", "brian-kemp", "border_immigration", 2, True,
              "In 2024 signed HB 1105 (Georgia Criminal Alien Track and Report Act), mandating all local law-enforcement agencies cooperate with ICE under the 287(g) program and forbidding sanctuary policies statewide; simultaneously deployed the Georgia National Guard to the southern border, sustaining the longest continuous state border presence of any state.",
              ["https://georgiarecorder.com/2024/05/01/kemp-signs-bill-into-law-forcing-sheriffs-to-enforce-federal-immigration-law/",
               "https://gov.georgia.gov/press-releases/2024-02-13/gov-kemp-directs-georgia-guard-reinforcements-southern-border"]),
    ]),

    # -------- Brad Raffensperger (GA, SoS → Gov candidate, R) --------
    ("brad-raffensperger-running-higher", "GA", "Secretary of State", [
        claim("br1", "brad-raffensperger-running-higher", "election_integrity", 0, True,
              "Publicly called for Georgia's General Assembly to mandate REAL ID for all forms of voting in state elections, arguing the same federal-ID standard required to board an airplane or enter a federal building should apply at the ballot box — a voter-ID posture that aligns with the rubric's election-integrity plank.",
              ["https://www.thecentersquare.com/georgia/article_501d3680-397d-4463-992b-eb326fffaf00.html",
               "https://sos.ga.gov/news/groundhog-day-returns-highlighting-raffenspergers-five-point-plan-election-reform"]),
        claim("br2", "brad-raffensperger-running-higher", "sanctity_of_life", 0, True,
              "Affirmed his anti-abortion stance throughout the 2025-2026 gubernatorial campaign — including at a Faith & Freedom Coalition event — and pledged that his 'bold conservative agenda' would include protecting unborn life; previously opposed abortion as a Georgia state legislator.",
              ["https://www.gpb.org/news/2025/09/17/secretary-of-state-brad-raffensperger-joins-the-republican-race-for-governor",
               "https://www.thecentersquare.com/georgia/article_501d3680-397d-4463-992b-eb326fffaf00.html"]),
        claim("br3", "brad-raffensperger-running-higher", "biblical_marriage", 2, True,
              "Pledged as part of his 2026 gubernatorial platform to ban drugs that block puberty for gender-affirming care in minors — a direct application of the rubric's call to reject transgender ideology in public policy and protect children from irreversible medical interventions.",
              ["https://www.thecentersquare.com/georgia/article_501d3680-397d-4463-992b-eb326fffaf00.html"]),
    ]),

    # -------- Chris Carr (GA, AG → Gov candidate, R) --------
    ("chris-carr-ag-running-higher", "GA", "Attorney General", [
        claim("cc1", "chris-carr-ag-running-higher", "sanctity_of_life", 0, True,
              "As Georgia AG, Carr served as the state's primary legal defender of the Living Infants Fairness and Equality Act (six-week heartbeat law), filing briefs with the Georgia Supreme Court to reinstate the law amid ongoing court challenges, and made 'keeping Georgia's abortion law' a top plank of his 2026 gubernatorial campaign.",
              ["https://www.wabe.org/their-voice-your-vote-chris-carr-emphasizes-economic-growth-public-safety-keeping-state-abortion-law/",
               "https://www.gpb.org/news/2022/10/14/abortion-fight-highlights-georgia-attorney-general-election"]),
        claim("cc2", "chris-carr-ag-running-higher", "public_justice", 0, True,
              "Made public safety the top pillar of his 2026 gubernatorial campaign, emphasizing prosecution of violent crime, human trafficking, and drug enforcement as the state's chief law officer — consistent with the rubric's call for public justice that protects innocent life.",
              ["https://www.wabe.org/their-voice-your-vote-chris-carr-emphasizes-economic-growth-public-safety-keeping-state-abortion-law/",
               "https://en.wikipedia.org/wiki/Christopher_M._Carr"]),
    ]),

    # -------- Steve Hilton (CA, Gov candidate, R) --------
    ("steve-hilton-gov", "CA", "Governor", [
        claim("sh1", "steve-hilton-gov", "sanctity_of_life", 0, True,
              "Holds that human life deserves legal protection from conception until natural death; on the 2026 campaign trail stated he would allow California to honor out-of-state extradition requests for abortion providers who perform procedures illegal in other states — placing him among the most pro-life Republican gubernatorial candidates in the country.",
              ["https://www.kqed.org/news/12071206/gop-candidate-steve-hilton-would-extradite-california-abortion-doctor-to-louisiana",
               "https://ivoterguide.com/candidate/90812/race/25614/election/1385"]),
        claim("sh2", "steve-hilton-gov", "self_defense", 0, True,
              "Pledged that as California governor he would 'do everything in my power to restore 2nd Amendment rights' that Democrat supermajorities have eroded, partnering with a Second Amendment-focused attorney general candidate to reverse California's near-total ban on lawful carry — directly opposing the state's anti-constitutional-carry posture.",
              ["https://stevehiltonforgovernor.com/",
               "https://sdcitytimes.com/news/2026/05/25/primary-26-hilton-introduction/"]),
        claim("sh3", "steve-hilton-gov", "border_immigration", 0, True,
              "As a legal immigrant himself, Hilton has been a vocal critic of Biden-era open-border policies and supports closing the southern border and enforcing immigration law; his campaign platform opposes California's sanctuary-state posture and calls for mandatory enforcement of federal immigration law at the state level.",
              ["https://sdcitytimes.com/news/2026/05/25/primary-26-hilton-introduction/",
               "https://en.wikipedia.org/wiki/Steve_Hilton"]),
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
