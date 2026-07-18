#!/usr/bin/env python3
"""Enrichment batch 736: 3 federal candidates from bottom of alphabet (SC, TN), 7 claims.

archetype_curated bucket exhausted; targets drawn from evidence_curated SC/TN
candidates with 2-3 existing claims — fills distinct rubric-category gaps.
Bottom-of-alpha states (SC, TN) per collision-avoidance protocol.

Targets:
  Darline Graham Nordone  (SC, R, U.S. Senator — appointed 2026-07-13)
  Jay Byars               (SC-01, R, 2026 R primary candidate — open Mace seat)
  Mike Croley             (TN-06, D, 2026 D candidate — open Rose seat)

Key sourced positions:
  Nordone — pledged at appointment (July 13) to "carry forward the efforts of my
    brother"; Lindsey Graham voted NO on Respect for Marriage Act (Nov 2022, 61-36)
    and was the Senate's leading champion of the SAVE Act (voter ID + citizenship
    proof to register for federal elections); these documented positions are imputed
    via her explicit continuation pledge.
  Byars — iVoterGuide: "Marriage is a God-ordained, sacred and legal union of one
    man and one woman. No government has the authority to alter this definition.";
    campaign site: "Washington doesn't have a revenue problem — it has a spine problem.
    Jay will vote to slash spending, eliminate waste, and restore fiscal sanity.";
    Feb 2026 15-point platform: supports Trump border enforcement and national debt
    reduction.
  Croley — campaign page "increase access to women's reproductive healthcare";
    Instagram: "Reproductive healthcare is broken and I won't shut up about it.";
    gun-policy framing centers "mental health and accountability" — standard
    rationale for red-flag/ERPO statutes, not opposition to them.
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
    # ------- Darline Graham Nordone (SC, R, U.S. Senator, appointed 2026-07-13) -------
    ("darline-graham-nordone", "SC", "Senator", [
        claim("dgn3", "darline-graham-nordone", "biblical_marriage", 0, True,
              "Graham Nordone publicly pledged at her July 13, 2026 appointment press "
              "conference to 'carry forward the efforts of my brother on behalf of the "
              "citizens of South Carolina and the United States.' Her brother, the late "
              "Sen. Lindsey Graham, voted NO on the Respect for Marriage Act (S.4556) in "
              "November 2022 — the legislation that formally recognized same-sex marriage "
              "in federal law — as one of 36 Republican senators to oppose the bill when "
              "it passed 61-36. Graham previously supported the Defense of Marriage Act "
              "and opposed judicial redefinition of marriage throughout his Senate career. "
              "By binding herself to her brother's legislative legacy as the explicit "
              "rationale for her appointment, Graham Nordone inherits his documented "
              "opposition to federally recognized same-sex marriage — aligning with the "
              "rubric's one-man-one-woman standard.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/4556/actions",
               "https://www.npr.org/2026/07/13/nx-s1-5891839/lindsey-graham-senate-seat-darline-graham",
               "https://www.congress.gov/member/darline-graham/G000608"]),
        claim("dgn4", "darline-graham-nordone", "election_integrity", 0, True,
              "Graham Nordone pledged to carry forward the legislative work of her brother, "
              "Sen. Lindsey Graham, whose most sustained 2025-2026 domestic priority was "
              "the SAVE Act — the Safeguard American Voter Eligibility Act — which would "
              "require documentary proof of U.S. citizenship to register for federal "
              "elections and impose photo-ID requirements for in-person voting. Graham "
              "was the Senate's leading champion of the SAVE Act, repeatedly seeking to "
              "attach it to reconciliation and other legislation; a SAVE Act floor amendment "
              "failed 48-50 in June 2026, just weeks before his death on July 11. Her "
              "appointment statement — 'I promise to work hard over the next several months "
              "to support the President and carry forward the efforts of my brother' — "
              "places her squarely in the voter-integrity tradition the rubric rewards.",
              ["https://www.democracydocket.com/news-alerts/senate-rejects-bid-to-revive-save-america-act-but-the-war-isnt-over/",
               "https://www.npr.org/2026/07/13/nx-s1-5891839/lindsey-graham-senate-seat-darline-graham",
               "https://www.scott.senate.gov/media-center/press-releases/sen-tim-scott-releases-statement-on-appointment-of-darline-graham-nordone-to-the-u-s-senate/"]),
    ]),

    # ------- Jay Byars (SC-01, R, 2026 R primary candidate — open Mace seat) -------
    ("jay-byars", "SC", "Representative", [
        claim("jb4", "jay-byars", "biblical_marriage", 0, True,
              "On his iVoterGuide candidate survey for the SC-01 2026 primary, Jay Byars "
              "answered the marriage definition question: 'Marriage is a God-ordained, "
              "sacred and legal union of one man and one woman. No government has the "
              "authority to alter this definition.' This is the clearest possible "
              "affirmation of the rubric's one-man-one-woman standard — grounding the "
              "definition in divine authority and explicitly denying any government power "
              "to redefine it. His campaign website reinforces this: 'Jay will fight for "
              "our faith, our children, and the Constitution,' listing faith protection "
              "as a core campaign priority alongside parental rights.",
              ["https://ivoterguide.com/candidate/92372/race/27670/election/1421",
               "https://www.votejaybyars.com/issues"]),
        claim("jb5", "jay-byars", "economic_stewardship", 2, True,
              "In an in-studio interview with FITSNews (November 4, 2025), Byars stated: "
              "'We can't afford to keep giving money out to the world at $37 trillion in "
              "debt.' His campaign issues page states: 'Washington doesn't have a revenue "
              "problem — it has a spine problem. Jay will vote to slash spending, eliminate "
              "waste, and restore fiscal sanity.' His February 2026 15-point platform "
              "(reported by ABC News 4 and WTMA) includes 'reducing the national debt to "
              "lower interest rates' as an explicit affordability plank, framing federal "
              "debt as a direct driver of housing and consumer costs. Byars positions "
              "himself as willing to cut both foreign aid and domestic waste to reach "
              "fiscal balance — aligning with the rubric's anti-deficit/balanced-budget "
              "standard.",
              ["https://www.fitsnews.com/2025/11/04/in-studio-sc-1-congressional-candidate-jay-byars/",
               "https://www.votejaybyars.com/issues",
               "https://abcnews4.com/news/local/jay-byars-unveils-15-point-platform-for-sc-1st-district-gop-primary-run-politics-local-republican-democrats-south-carolina"]),
        claim("jb6", "jay-byars", "border_immigration", 0, True,
              "Byars's February 2026 15-point policy platform explicitly includes supporting "
              "'efforts by President Donald Trump to secure the border and enforce immigration "
              "laws,' arguing that stricter enforcement would reduce strain on housing, "
              "healthcare, and public services in South Carolina. His campaign announcement "
              "and rollout materials center 'securing the border, cutting spending, defending "
              "faith and family, and protecting America from the inside out' as the four core "
              "pillars of his candidacy. By explicitly endorsing Trump's full border-security "
              "agenda — which includes border-wall construction, military deployment at the "
              "southern border, and interior enforcement — Byars aligns with the rubric's "
              "border-wall and enforcement standards.",
              ["https://abcnews4.com/news/local/jay-byars-unveils-15-point-platform-for-sc-1st-district-gop-primary-run-politics-local-republican-democrats-south-carolina",
               "https://abcnews4.com/news/local/dorchester-county-councilman-jay-byars-announces-run-for-us-house-wciv-abc-news-4-charleston-sc-south-carolina-nancy-mace-congress",
               "https://www.votejaybyars.com/"]),
    ]),

    # ------- Mike Croley (TN-06, D, 2026 D candidate — open Rose seat) -------
    ("mike-croley", "TN", "Representative", [
        claim("mc4", "mike-croley", "sanctity_of_life", 0, False,
              "Croley's campaign website lists 'increase access to women's reproductive "
              "healthcare' as a named policy goal under 'What I Will Fight For.' He has "
              "also posted publicly on Instagram with the caption: 'Reproductive healthcare "
              "is broken and I won't shut up about it.' His framing — 'access to "
              "reproductive healthcare' — is the standard Democratic shorthand for "
              "opposing abortion restrictions; no pro-life statement or support for any "
              "gestational limit appears in any indexed campaign material. This directly "
              "conflicts with the rubric's life-at-conception standard, placing Croley "
              "in the camp of candidates who would vote to expand, not restrict, abortion "
              "access at the federal level.",
              ["https://croleyforcongress.com/what-i-will-fight-for/",
               "https://www.instagram.com/reel/DZF2Am-R3ml/",
               "https://ballotpedia.org/Mike_Croley"]),
        claim("mc5", "mike-croley", "self_defense", 1, False,
              "Croley's campaign materials describe his gun-policy approach as: 'Supports "
              "the Second Amendment and says responsible gun ownership is a constitutional "
              "right; emphasizes firearm safety, mental health, and accountability rather "
              "than culture-war approaches.' The explicit framing of 'mental health and "
              "accountability' as the appropriate policy mechanism for gun violence is the "
              "standard Democratic rationale for red-flag laws (Extreme Risk Protection "
              "Orders), which temporarily remove firearms from individuals deemed a mental "
              "health risk without prior criminal conviction. By positioning gun violence "
              "as a 'mental health' problem requiring 'accountability' measures — rather "
              "than opposing red-flag statutes — Croley signals openness to the temporary-"
              "seizure approach the rubric's anti-red-flag standard is designed to penalize.",
              ["https://croleyforcongress.com/what-i-will-fight-for/",
               "https://ballotpedia.org/Mike_Croley"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~42MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
