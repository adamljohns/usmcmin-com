#!/usr/bin/env python3
"""Enrichment batch 51: 4 federal House candidates (4R) from the bottom
of the archetype_curated bucket with 0 claims.

Targets (bottom-of-alphabet pick — avoiding AK/AL/AR collision-window):
  Paul Hudson      (MI-03  R) — attorney, 2024 R nominee; pro-life/2A/border hawk
  Madison Cawthorn (FL-19  R) — former US Rep NC-11; NRA A-rating; pro-life champion
  Tricia Pridemore (GA-11  R) — GA PSC commissioner; life-at-conception; wall supporter
  Houston Gaines   (GA-10  R) — GA state rep; won R primary 5/19/26; Comstock enforcer

Each claim cites >=1 reliable public source and reflects 2024-2026
voting record / public positions. Minified write preserves the ~35-36 MB
master (no indent=2 — see enrich-batch-4.py docstring).
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


TARGETS = [
    # ---------- Paul Hudson (MI-03 R) ----------
    ("paul-hudson", "MI", "Representative", [
        claim("ph1", "paul-hudson", "sanctity_of_life", 0, True,
              "Describes himself as 'strongly Pro Life' (iVoterGuide questionnaire); his 2024 campaign was flagged by the DCCC as 'backed by extreme anti-abortion groups'; explicitly opposes taxpayer funding for abortion providers including Planned Parenthood and Title X grants, and supports requiring in-person medical oversight for chemical abortion drugs — a consistent pro-life record affirming protection of the unborn.",
              ["https://ivoterguide.com/candidate/74682/race/835/election/1244",
               "https://ballotpedia.org/Paul_Hudson"]),
        claim("ph2", "paul-hudson", "self_defense", 1, True,
              "Is a member of the NRA and describes himself as 'Pro Second Amendment'; iVoterGuide records him as believing 'strongly in the Second Amendment as written and supports the NRA positions on gun ownership' — opposing new restrictions, bans, and registries and aligning with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ivoterguide.com/candidate/74682/race/835/election/1244",
               "https://ballotpedia.org/Paul_Hudson"]),
        claim("ph3", "paul-hudson", "border_immigration", 0, True,
              "States the U.S. must 'secure our borders, enforce the rule of law in our cities and communities'; attacked his 2024 opponent for an 'open-borders record'; said 'we have immigration laws for a reason, and we need to enforce them' — supporting border-security infrastructure and enforcement consistent with the rubric's wall-and-military standard.",
              ["https://ballotpedia.org/Paul_Hudson",
               "https://bridgemi.com/michigan-government/republican-congressional-candidates-fight-reclaim-west-michigan-former-stronghold"]),
    ]),

    # ---------- Madison Cawthorn (FL-19 R) ----------
    ("madison-cawthorn-fl-19", "FL", "Representative", [
        claim("mc1", "madison-cawthorn-fl-19", "sanctity_of_life", 0, True,
              "As U.S. Representative (NC-11, 2021-2023), hosted a dedicated 'Pro-Life' page on his official congressional website and was named a 'Pro-Life Generation Champion' by Students for Life Action; receives a 0% rating from Reproductive Freedom for All — affirming life from conception and fully rejecting any legal right to abortion.",
              ["https://cawthorn.house.gov/issues/pro-life",
               "https://reproductivefreedomforall.org/lawmaker/madison-cawthorn/",
               "https://en.wikipedia.org/wiki/Madison_Cawthorn"]),
        claim("mc2", "madison-cawthorn-fl-19", "self_defense", 1, True,
              "Holds an NRA 'A' rating earned during his time in Congress; stated there was 'no stronger advocate for the Second Amendment than Madison Cawthorn' and pledges to 'not give an inch when it comes to our Second Amendment Rights' — opposing all new restrictions, bans, and registries consistent with the rubric.",
              ["https://en.wikipedia.org/wiki/Madison_Cawthorn",
               "https://ivoterguide.com/candidate?elecK=718&raceK=5299&primarypartyk=R&canK=52405"]),
        claim("mc3", "madison-cawthorn-fl-19", "border_immigration", 1, True,
              "Has called for defending borders and 'removing anti-American illegal immigrants'; his 2026 Florida campaign platform centers in part on combating illegal immigration, promising to fight insurance costs, crime, and illegal immigration — supporting mandatory removal and enforcement consistent with the rubric.",
              ["https://en.wikipedia.org/wiki/Madison_Cawthorn",
               "https://floridapolitics.com/archives/758786-madison-cawthorn-officially-enters-race-for-byron-donalds-house-seat/"]),
    ]),

    # ---------- Tricia Pridemore (GA-11 R) ----------
    ("tricia-pridemore", "GA", "Representative", [
        claim("tp1", "tricia-pridemore", "sanctity_of_life", 0, True,
              "States 'every innocent human life deserves legal protection from conception until natural death' and pledges to fight to defund Planned Parenthood and defend the unborn in Congress — a personhood-from-conception standard that directly matches the rubric's most demanding pro-life criterion.",
              ["https://ballotpedia.org/Tricia_Pridemore",
               "https://en.wikipedia.org/wiki/Tricia_Pridemore"]),
        claim("tp2", "tricia-pridemore", "self_defense", 1, True,
              "States 'The Second Amendment is not up for debate' and pledges to 'oppose every gun control measure that comes before her in Congress' — a blanket anti-restriction posture fully consistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Tricia_Pridemore"]),
        claim("tp3", "tricia-pridemore", "border_immigration", 0, True,
              "Supports full funding for the border wall, end to catch-and-release, and deportation of criminal illegal aliens; states 'America is a nation of laws, and if you broke them to get here, you do not get to stay. Our sovereignty is not negotiable.' — directly matching the rubric's wall-plus-military enforcement standard.",
              ["https://ballotpedia.org/Tricia_Pridemore"]),
    ]),

    # ---------- Houston Gaines (GA-10 R) ----------
    ("houston-gaines", "GA", "Representative", [
        claim("hg1", "houston-gaines", "sanctity_of_life", 0, True,
              "States 'Human life deserves legal protection from conception until natural death' — a personhood-from-conception standard matching the rubric's most demanding pro-life criterion; won the Republican primary for Georgia's 10th Congressional District on May 19, 2026.",
              ["https://ivoterguide.com/candidate/46845/race/26940/election/1409",
               "https://ballotpedia.org/Houston_Gaines"]),
        claim("hg2", "houston-gaines", "sanctity_of_life", 1, True,
              "Advocates enforcement of the Comstock Act to block interstate transportation of abortion-inducing drugs — a maximalist pro-life position that moves beyond incremental restrictions toward abolition of chemical abortion access, consistent with the rubric's 'abolition-not-restrictions' standard.",
              ["https://ivoterguide.com/candidate/46845/race/26940/election/1409",
               "https://houstongaines.com/"]),
        claim("hg3", "houston-gaines", "border_immigration", 1, True,
              "As a Georgia state representative, supported hard-line state immigration enforcement legislation including measures passed in the wake of the Laken Riley killing that enabled prosecution of illegal immigrants who commit crimes in Georgia — consistent with the rubric's mandatory-deportation and enforcement standard.",
              ["https://ballotpedia.org/Houston_Gaines",
               "https://houstongaines.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
