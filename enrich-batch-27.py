#!/usr/bin/env python3
"""Enrichment batch 27: 4 bottom-of-alphabet federal candidates (DE, AR, AK, CA).

Targets: Eric Hansen (DE-R), Marcus Jones (AR-D), Mary Peltola (AK-D),
Monique Limón (CA-D). All archetype_curated with 0 evidence claims.
Sources: Delaware Public Media, WDEL, THV11, Alaska Public Radio,
Anchorage Daily News, Must Read Alaska, CalMatters, marcusjonesforcongress.com.
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
    # ---------------- Eric Hansen (DE-R, 2026 U.S. Senate candidate) ----------------
    ("eric-hansen-de-senate", "DE", "Delaware", [
        claim("eh1", "eric-hansen-de-senate", "sanctity_of_life", 0, False,
              "Explicitly stated 'I, as a U.S. Senator, will not vote for a federal abortion ban, full stop'; supports only late-term abortion limits with exceptions for rape, incest, and life of the mother — rejecting personhood-from-conception and federal restrictions on abortion.",
              ["https://www.delawarepublic.org/show/the-green/2024-09-03/candidate-conversations-republican-candidate-for-u-s-senate-eric-hansen",
               "https://www.wdel.com/news/wdel-electionwatch-candidate-forum---eric-hansen-for-us-senate/article_2a4dd90e-197d-11ef-85ea-bbe07b3eaed7.html"]),
        claim("eh2", "eric-hansen-de-senate", "border_immigration", 0, False,
              "Backed the failed 2024 bipartisan border reform bill over a wall-construction or mass-deportation framework; characterized illegal immigration as a vetting problem requiring stricter legal screening rather than military enforcement at the border.",
              ["https://www.wdel.com/news/wdel-electionwatch-candidate-forum---eric-hansen-for-us-senate/article_2a4dd90e-197d-11ef-85ea-bbe07b3eaed7.html",
               "https://ballotpedia.org/Eric_Hansen_(Delaware)"]),
        claim("eh3", "eric-hansen-de-senate", "family_child_sovereignty", 0, True,
              "Proposes a national school choice program giving families the ability to direct education funds to the school of their choosing, expanding parental authority over children's schooling.",
              ["https://www.delawarepublic.org/show/the-green/2024-09-03/candidate-conversations-republican-candidate-for-u-s-senate-eric-hansen"]),
    ]),

    # ---------------- Marcus Jones (AR-D, 2026 U.S. Senate candidate) ----------------
    ("marcus-jones-ar-senate", "AR", "Arkansas", [
        claim("mj1", "marcus-jones-ar-senate", "sanctity_of_life", 0, False,
              "Opposes any national abortion restriction; stated in the 2024 AR-02 congressional debate 'a strong nation protects women's rights. It does not invade their exam room' — rejecting personhood from conception and any federal limit on abortion access.",
              ["https://arkansasadvocate.com/2024/10/07/health-care-topics-lead-debate-between-arkansas-2nd-congressional-district-candidates/",
               "https://www.thv11.com/article/news/politics/elections/marcus-jones-french-hill-arkansas-debate/91-fb7f2d3e-ed88-4947-8940-815a47b32799"]),
        claim("mj2", "marcus-jones-ar-senate", "border_immigration", 0, False,
              "Advocated for the bipartisan border reform bill over wall construction or mass deportation; described the border as a 'national security and humanitarian crisis' requiring a legislative negotiated solution rather than military force.",
              ["https://www.thv11.com/article/news/politics/elections/marcus-jones-french-hill-arkansas-debate/91-fb7f2d3e-ed88-4947-8940-815a47b32799",
               "https://arkansasadvocate.com/2024/10/07/health-care-topics-lead-debate-between-arkansas-2nd-congressional-district-candidates/"]),
        claim("mj3", "marcus-jones-ar-senate", "economic_stewardship", 2, False,
              "Prioritizes expanding and permanently codifying the federal Child Tax Credit — an entitlement that increases deficit spending — as a top economic policy, opposing a balanced-budget or spending-restraint posture.",
              ["https://marcusjonesforcongress.com/priorities/",
               "https://arkansasadvocate.com/briefs/arkansas-democrats-elect-retired-army-colonel-marcus-jones-as-party-chair/"]),
    ]),

    # ---------------- Mary Peltola (AK-D, 2026 U.S. Senate candidate) ----------------
    ("mary-peltola-senate", "AK", "Alaska", [
        claim("mp1", "mary-peltola-senate", "sanctity_of_life", 0, False,
              "Consistently supported abortion rights throughout her 2022–2024 congressional service; earned the endorsement of EMILY's List and stated support for federal abortion access — rejecting any personhood-from-conception standard.",
              ["https://rollcall.com/2026/01/12/mary-peltola-alaska-senate-election-sullivan/",
               "https://ballotpedia.org/Mary_Peltola"]),
        claim("mp2", "mary-peltola-senate", "self_defense", 1, False,
              "Received an NRA rating of 'D' for supporting universal background checks, mandatory waiting periods for firearm purchases, and raising the minimum purchase age for certain firearms to 21 — positions opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://mustreadalaska.com/on-second-amendment-peltola-now-representing-alaska-in-congress-supports-gun-control-gets-a-d-from-nra/",
               "https://www.adn.com/politics/2023/04/09/in-the-wake-of-shootings-alaska-rep-peltola-finds-herself-in-a-tough-position-on-guns/"]),
        claim("mp3", "mary-peltola-senate", "border_immigration", 0, True,
              "Broke with the Democratic Party in 2024 by voting for border enforcement measures, one of 78 party-line-defying votes during her congressional service; her aisle-crossing votes were concentrated in border and energy policy.",
              ["https://alaskapublic.org/2024/05/17/peltola-defies-party-with-votes-on-border-enforcement-and-arms-for-israel/",
               "https://alaskapublic.org/2024/03/28/peltolas-votes-show-shes-one-of-the-least-loyal-democrats-in-the-u-s-house/"]),
    ]),

    # ---------------- Monique Limón (CA-D, 2026 U.S. House CA-26 candidate) ----------------
    ("monique-limon-ca-26", "CA", "CA-26", [
        claim("ml1", "monique-limon-ca-26", "election_integrity", 0, False,
              "Authored SB 299 (2024) to convert California's voter registration system to automatic 'opt-out' enrollment at state agencies, expanding voter rolls without traditional verification at the point of registration — opposing the rubric's voter-ID and anti-automatic-registration standard.",
              ["https://sd21.senate.ca.gov/2024-legislation",
               "https://ballotpedia.org/S._Monique_Lim%C3%B3n"]),
        claim("ml2", "monique-limon-ca-26", "sanctity_of_life", 0, False,
              "As California Senate president pro tempore since January 2026, leads a caucus that has continuously expanded state abortion-access guarantees post-Dobbs and has framed reproductive healthcare as a core legislative priority — opposing personhood-from-conception standards at every level.",
              ["https://calmatters.org/politics/2026/01/monique-limon-senate-president/",
               "https://women.ca.gov/monique-limon/"]),
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
