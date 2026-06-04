#!/usr/bin/env python3
"""Enrichment batch 38: 4 bottom-of-alphabet PA U.S. House candidates (all D).

Targets archetype_curated U.S. Representative candidates with 0 claims,
taken from the bottom of the reverse-alphabetical bucket (PA block).

Candidates: Morgan Cephas (PA-03), Ashley Ehasz (PA-01),
Janelle Stelson (PA-10), Ala Stanford (PA-03).

All claims cite 2024-2026 sourced positions; score_impact reflects
alignment with the God-First/America-First rubric (True = aligns).
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
    # ---------------- Morgan Cephas (PA-03, D) ----------------
    ("morgan-cephas", "PA", "Representative", [
        claim("mc1", "morgan-cephas", "sanctity_of_life", 0, False,
              "As a PA state rep, voted against HB 2459 (2022) that would have amended the Pennsylvania Constitution to exclude abortion from constitutional protection, and against HB 1888 (2022) banning D&E procedures and post-20-week abortions — consistently rejecting personhood and any gestational-limit framework.",
              ["https://choicetracker.org/legislator/h192cephas",
               "https://www.palegis.us/house/members/bio/1759/rep-morgan-cephas"]),
        claim("mc2", "morgan-cephas", "self_defense", 1, False,
              "Sponsored PA HB 1099 (2025) banning all-plastic 'ghost' firearms and co-sponsored the 2024 ghost-gun bill that passed the PA House 104–97; earned a 'Gun Safety Champion' designation from CeaseFirePA in 2024 — opposing the rubric's protection of unrestricted gun rights.",
              ["https://www.ceasefirepa.org/general-interest/ceasefirepa-action-endorses-81-gun-safety-champions-for-2024-election/",
               "https://www.cityandstatepa.com/policy/2025/09/gun-control-bills-receive-mixed-response-tight-pa-house-votes/408508/"]),
        claim("mc3", "morgan-cephas", "biblical_marriage", 2, False,
              "Serves on the PA House LGBTQ+ Equality Caucus and has co-issued official House statements supporting LGBTQ+ nondiscrimination protections and transgender rights — rejecting the rubric's standard of opposing transgender ideology in policy.",
              ["https://www.pahouse.com/Cephas/InTheNews/NewsRelease/?id=133093",
               "https://www.pahouse.com/LGBTQ/inthenews/newsrelease"]),
    ]),

    # ---------------- Ashley Ehasz (PA-01, D) ----------------
    ("ashley-ehasz", "PA", "Representative", [
        claim("ae1", "ashley-ehasz", "sanctity_of_life", 0, False,
              "Favors H.R. 3755 (Women's Health Protection Act), which would bar any government restriction on abortion throughout an entire pregnancy, and stated abortion decisions 'should be between her and her doctor' — explicitly rejecting personhood from conception.",
              ["https://penncapital-star.com/election-2024/ehasz-talks-issues-in-pa-01-forum-as-fitzpatrick-declines-to-participate-in-debate/",
               "https://whyy.org/articles/brian-fitzpatrick-ashley-ehasz-congressional-race-pennsylvania-elections-2024/"]),
        claim("ae2", "ashley-ehasz", "self_defense", 1, False,
              "Labeled gun violence a 'public health crisis' and explicitly supports a federal assault-weapons ban and universal background checks — positions directly opposed to the rubric's defense of unrestricted Second Amendment rights.",
              ["https://penncapital-star.com/election-2024/ehasz-talks-issues-in-pa-01-forum-as-fitzpatrick-declines-to-participate-in-debate/",
               "https://levittownnow.com/2024/10/23/democratic-candidate-ehasz-talks-issues-at-forum-as-rep-fitzpatrick-declines-to-participate/"]),
        claim("ae3", "ashley-ehasz", "border_immigration", 1, False,
              "Supports DACA protections for 'Dreamers' and believes the U.S. must make it easier for immigrants to become citizens legally — rejecting the rubric's mandatory-deportation standard for those present without authorization.",
              ["https://whyy.org/articles/brian-fitzpatrick-ashley-ehasz-congressional-race-pennsylvania-elections-2024/"]),
    ]),

    # ---------------- Janelle Stelson (PA-10, D) ----------------
    ("janelle-stelson", "PA", "Representative", [
        claim("js1", "janelle-stelson", "sanctity_of_life", 0, False,
              "EMILY's List-endorsed 'pro-choice champion'; ran on codifying Roe v. Wade into federal law and stated reproductive freedom is 'not something that is negotiable' — rejecting any personhood-from-conception standard.",
              ["https://emilyslist.org/news/emilys-list-endorses-janelle-stelson-for-election-to-pennsylvanias-10th-congressional-district/",
               "https://keystonenewsroom.com/2024/04/24/stelson-wins-pa-10-primary/"]),
        claim("js2", "janelle-stelson", "self_defense", 1, False,
              "Supports implementing red-flag laws, expanded background checks, and removal of untraceable 'ghost guns' from civilian hands — positions that directly oppose the rubric's protection of the Second Amendment from such restrictions.",
              ["https://www.witf.org/2024/10/09/in-10th-district-debate-gop-incumbent-perry-and-democrat-stelson-agree-on-immigration-differ-on-abortion/",
               "https://www.fox43.com/article/news/politics/elections/scott-perry-janelle-stelson-abortion-foreign-aid-border-control-pennsylvania-election-vote/521-53dcbc36-e8da-42e1-93dc-ceaed4cfa34f"]),
        claim("js3", "janelle-stelson", "border_immigration", 1, True,
              "In an October 2024 candidate forum, agreed with GOP incumbent Scott Perry that undocumented immigrants already in the U.S. 'need to be sent home,' stating 'The ones who are here, we need to find out where they are and they need to be sent home' — aligning with the rubric's mandatory-deportation position on this specific point.",
              ["https://www.witf.org/2024/10/09/in-10th-district-debate-gop-incumbent-perry-and-democrat-stelson-agree-on-immigration-differ-on-abortion/"]),
    ]),

    # ---------------- Ala Stanford (PA-03, D) ----------------
    ("ala-stanford", "PA", "Representative", [
        claim("as1", "ala-stanford", "sanctity_of_life", 0, False,
              "EMILY's List-endorsed 2026 congressional candidate who supports abortion access and opposes restrictions on reproductive healthcare; her campaign explicitly highlights the need to protect abortion rights — rejecting any personhood-from-conception standard.",
              ["https://visibletogether.com/%E3%80%902026-pennsylvania-election%E3%80%91who-is-ala-stanford/",
               "https://www.inquirer.com/politics/philadelphia/ala-stanford-philadelphia-congress-healthcare-medicare-20260318.html"]),
        claim("as2", "ala-stanford", "border_immigration", 2, False,
              "Her 2026 congressional platform calls for abolishing ICE — directly opposing the rubric's anti-sanctuary-city and interior enforcement standard.",
              ["https://visibletogether.com/%E3%80%902026-pennsylvania-election%E3%80%91who-is-ala-stanford/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
