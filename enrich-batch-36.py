#!/usr/bin/env python3
"""Enrichment batch 36: hand-curated claims for 4 candidates (2 TX Representatives,
1 TN Representative candidate, 1 PA Representative candidate).

Targets archetype_curated Representatives with 0 evidence claims. Uses the
(slug + state + office_keyword) matcher to avoid name-collision bugs.

Mix (4 D): Colin Allred (TX), Marquette Greene-Scott (TX),
Justin Pearson (TN-09), Sharif Street (PA-03).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Colin Allred (TX-D, US Representative TX-33) ----------------
    ("colin-allred", "TX", "Representative", [
        claim("ca1", "colin-allred", "sanctity_of_life", 0, False,
              "Earned a 100% Reproductive Freedom for All congressional scorecard during his tenure as U.S. Representative for Texas's 32nd district (2019–2025); cosponsored the Women's Health Protection Act to codify federal abortion access before viability and was formally endorsed by Reproductive Freedom for All for his 2024 U.S. Senate run — rejecting any personhood-from-conception standard.",
              ["https://reproductivefreedomforall.org/lawmaker/colin-allred/",
               "https://en.wikipedia.org/wiki/Colin_Allred"]),
        claim("ca2", "colin-allred", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), which creates federal incentives for states to enact red-flag laws enabling firearm seizure without conviction; also on record supporting a federal assault-weapons ban — both directly contrary to the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Colin_Allred",
               "https://justfacts.votesmart.org/candidate/key-votes/177357/colin-allred"]),
        claim("ca3", "colin-allred", "border_immigration", 1, False,
              "Calls to 'abolish' U.S. Immigration and Customs Enforcement and redistribute its functions to other agencies, citing lost faith in the agency after the Trump administration's deportation surge — directly opposing the rubric's mandatory-deportation enforcement standard.",
              ["https://www.texastribune.org/2026/05/06/texas-33rd-congressional-district-democratic-runoff-colin-allred-julie-johnson/",
               "https://www.nbcnews.com/politics/2026-election/tx-33-texas-runoff-house-winner-allred-defeats-johnson-rcna346550"]),
    ]),

    # ---------------- Marquette Greene-Scott (TX-D, US Representative TX-22) ----------------
    ("marquette-greene-scott", "TX", "Representative", [
        claim("mgs1", "marquette-greene-scott", "sanctity_of_life", 0, False,
              "Supports abortion access in cases of non-viable pregnancy, risk to the mother's life, and rape or incest; would only endorse federal limits if the fetus can survive outside the womb — explicitly rejecting personhood or legal protection from the moment of conception.",
              ["https://ivoterguide.com/candidate/82299/race/6580/election/1214",
               "https://www.branch.vote/races/2024-texas-general-election-tx-state-us-representative-tx-congressional-22/candidates/marquette-greene-scott"]),
        claim("mgs2", "marquette-greene-scott", "border_immigration", 1, False,
              "Supports creating legal pathways for immigration and a path to citizenship for those currently in the country — rejecting the rubric's mandatory-deportation enforcement standard in favor of legalization.",
              ["https://ivoterguide.com/candidate/82299/race/6580/election/1214",
               "https://thefacts.com/opinion/candidate-introduction-marquette-greene-scott-democrat-u-s-house-district-22/article_d0514119-0dc1-4839-a8ab-b024503d285b.html"]),
        claim("mgs3", "marquette-greene-scott", "election_integrity", 0, False,
              "Endorsed the John Lewis Voting Rights Advancement Act, which would restore federal pre-clearance over state election laws and restrict state voter-ID and election-security measures — opposing the rubric's voter-ID and anti-mass-mail-in standards.",
              ["https://ivoterguide.com/candidate/82299/race/6580/election/1214",
               "https://marquettegreenescott.com/"]),
    ]),

    # ---------------- Justin Pearson (TN-D, US Representative TN-09 candidate) ----------------
    ("justin-pearson-tn-09", "TN", "Representative", [
        claim("jp1", "justin-pearson-tn-09", "self_defense", 1, False,
              "Introduced HB 1390 in the Tennessee legislature to create extreme-risk protection orders (red-flag laws) authorizing courts to seize firearms without a criminal conviction; was also expelled from the Tennessee House in April 2023 for participating in a gun-control demonstration on the chamber floor — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Justin_J._Pearson",
               "https://tennesseelookout.com/2025/10/08/memphis-state-rep-justin-pearson-to-challenge-u-s-rep-steve-cohen-in-2026-democratic/"]),
        claim("jp2", "justin-pearson-tn-09", "biblical_marriage", 0, False,
              "Publicly opposed 2024 Tennessee legislation that would have allowed government officials to decline to solemnize same-sex marriages, calling such bills 'harmful' and criticizing them for 'not caring for inclusion' — standing squarely against the rubric's one-man-one-woman marriage definition.",
              ["https://wpln.org/post/tennessee-is-one-signature-away-from-a-new-attempt-to-restrict-same-sex-marriages/",
               "https://www.wsmv.com/2026/02/19/tennessee-house-passes-bill-allowing-private-citizens-refuse-recognition-same-sex-marriages/"]),
    ]),

    # ---------------- Sharif Street (PA-D, US Representative PA-03 candidate) ----------------
    ("sharif-street", "PA", "Representative", [
        claim("ss1", "sharif-street", "sanctity_of_life", 0, False,
              "Pro-choice Pennsylvania state senator who voted against a bill to amend the Pennsylvania Constitution to exclude any right to abortion, cosponsored legislation requiring crisis pregnancy centers to meet the same medical-facility standards as licensed providers, and supports codifying Roe v. Wade into federal law — rejecting personhood from conception.",
              ["https://pa.choicetracker.org/people/sharif-street/31522816",
               "https://ballotpedia.org/Sharif_Street"]),
        claim("ss2", "sharif-street", "self_defense", 1, False,
              "Supports stronger gun-safety laws and has publicly criticized Pennsylvania's state preemption law that blocks cities from enacting their own stricter firearm regulations — favoring expanded restrictions rather than the constitutional-carry and anti-red-flag position the rubric requires.",
              ["https://www.politicspa.com/elections/candidates/sharif-street",
               "https://ballotpedia.org/Sharif_Street"]),
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
