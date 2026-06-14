#!/usr/bin/env python3
"""Enrichment batch 208: 4 sitting U.S. Representatives with 0 claims.

Targets archetype_party_default federal representatives from the bottom of
the alphabet: Julia Letlow (LA-R), Laura Gillen (NY-D), Cleo Fields (LA-D),
Frank Mrvan (IN-D).  Sources: official congress.gov/govtrack.us/Wikipedia
and advocacy-org scorecards (NRL, SBA, NARAL/RFFA).
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
    # ---------------- Julia Letlow (LA-05, R — US Rep running for Senate) ----------------
    ("julia-letlow", "LA", "Representative", [
        claim("jl1", "julia-letlow", "sanctity_of_life", 0, True,
              "Letlow compiled a 100% pro-life voting record across all 29 votes scored by National Right to Life during her House career (2021-2026). She states: 'I'm unabashedly pro-life and I believe that every soul is precious in the sight of God.' On the House Appropriations Committee she fought to preserve the Hyde Amendment blocking federal funding of abortions.",
              ["https://prolifelouisiana.org/laws-elections/federal-legislation/federal-elected-officials/5th-congressional/",
               "https://sbaprolife.org/representative/julia-letlow",
               "https://en.wikipedia.org/wiki/Julia_Letlow"]),
        claim("jl2", "julia-letlow", "election_integrity", 0, True,
              "Letlow publicly backed the SAVE America Act, which requires photo identification to register to vote and explicitly prohibits noncitizens from casting ballots — directly matching the rubric's voter-ID and election-security standard.",
              ["https://www.nola.com/news/politics/julia-letlow-john-fleming-jamie-davis-gary-crockett-louisiana-senate/article_cf8aed7b-16fe-4e9d-9539-3aa2510b2b5c.html",
               "https://en.wikipedia.org/wiki/Julia_Letlow"]),
        claim("jl3", "julia-letlow", "border_immigration", 0, True,
              "Letlow welcomed the opening of Louisiana's migrant detention center as a needed 'immigration crackdown' and joined Louisiana colleagues in demanding accountability from the Biden administration after it released immigration detainees in the state — aligning with the rubric's border-security and enforcement standard.",
              ["https://en.wikipedia.org/wiki/Julia_Letlow",
               "https://www.nola.com/news/politics/julia-letlow-john-fleming-jamie-davis-gary-crockett-louisiana-senate/article_cf8aed7b-16fe-4e9d-9539-3aa2510b2b5c.html"]),
    ]),

    # ---------------- Laura Gillen (NY-04, D — US Representative) ----------------
    ("laura-gillen", "NY", "Representative", [
        claim("lg1", "laura-gillen", "sanctity_of_life", 0, False,
              "Gillen called the Dobbs decision 'disastrous' and 'a shocking and potentially devastating setback,' has consistently described herself as an advocate for reproductive rights, and argues the government must not dictate medical decisions to women — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Laura_Gillen",
               "https://justfacts.votesmart.org/candidate/208621/laura-gillen"]),
        claim("lg2", "laura-gillen", "self_defense", 1, False,
              "Gillen supports extreme risk protection orders (red-flag laws) enabling pre-crime firearm confiscation without a conviction, and advocates for broader 'common sense gun legislation' restricting firearm access — directly opposing the rubric's position against red-flag laws, assault-weapon bans, and magazine limits.",
              ["https://en.wikipedia.org/wiki/Laura_Gillen",
               "https://ballotpedia.org/Laura_Gillen"]),
        claim("lg3", "laura-gillen", "biblical_marriage", 4, True,
              "In May 2026, Gillen was one of only eight House Democrats to vote for the Stopping Indoctrination and Protecting Kids Act, which bans teaching of transgender ideology in K-12 schools and prohibits schools from allowing students to use preferred pronouns or opposite-sex facilities without parental consent — aligning with the rubric's opposition to LGBTQ promotion in schools.",
              ["https://en.wikipedia.org/wiki/Laura_Gillen"]),
    ]),

    # ---------------- Cleo Fields (LA-06, D — US Representative) ----------------
    ("cleo-fields", "LA", "Representative", [
        claim("cf1", "cleo-fields", "sanctity_of_life", 0, False,
              "Fields received a 100% rating from the National Abortion Rights Action League (now Reproductive Freedom for All) across his congressional service and holds a consistent pro-choice position, supporting abortion access as a medical right and rejecting any personhood-from-conception framework.",
              ["https://en.wikipedia.org/wiki/Cleo_Fields",
               "https://govtrack.us/congress/members/cleo_fields/404067"]),
        claim("cf2", "cleo-fields", "self_defense", 1, False,
              "Fields has been an outspoken gun-control advocate throughout his congressional career, supporting restrictions on firearm access in direct opposition to the rubric's defense of unrestricted Second Amendment rights and against red-flag laws, assault-weapon bans, and magazine-limit restrictions.",
              ["https://en.wikipedia.org/wiki/Cleo_Fields"]),
        claim("cf3", "cleo-fields", "biblical_marriage", 4, True,
              "In 2026, Fields was one of only eight House Democrats to vote for the Stopping Indoctrination and Protecting Kids Act, which bans transgender content in K-12 schools and mandates parental notification when a student seeks to change their gender identification — aligning with the rubric's opposition to LGBTQ promotion in schools and public policy.",
              ["https://en.wikipedia.org/wiki/Cleo_Fields"]),
    ]),

    # ---------------- Frank Mrvan (IN-01, D — US Representative) ----------------
    ("frank-mrvan", "IN", "Representative", [
        claim("fm1", "frank-mrvan", "sanctity_of_life", 0, False,
              "Mrvan cosponsored the Women's Health Protection Act in both the 118th (2023) and 119th (2025) Congresses to codify federal abortion access and eliminate state restrictions. He describes himself as 'a staunch supporter of women's rights' including 'autonomy over their own bodies' — explicitly opposing any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Frank_J._Mrvan",
               "https://www.congress.gov/bill/118th-congress/house-bill/12/cosponsors",
               "https://govtrack.us/congress/members/frank_mrvan/456821"]),
        claim("fm2", "frank-mrvan", "border_immigration", 1, False,
              "Mrvan declined to vote on the Laken Riley Act (January 2025), which would have required mandatory ICE detention of illegal immigrants who commit crimes, choosing to abstain rather than support enforcement — a record the NRCC highlighted as inconsistent with border-security and mandatory-deportation priorities.",
              ["https://www.nrcc.org/2026/02/23/as-president-trump-touts-laken-riley-act-remember-frank-mrvan-sat-on-the-sidelines/",
               "https://govtrack.us/congress/members/frank_mrvan/456821"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
