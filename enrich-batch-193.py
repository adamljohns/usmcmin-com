#!/usr/bin/env python3
"""Enrichment batch 193: hand-curated claims for 5 U.S. House Representatives.

Targets (bottom-of-alphabet protocol, archetype_party_default, 0 claims):
  Greg Landsman (OH-D), Emilia Sykes (OH-D), Yvette Clarke (NY-D),
  Tom Suozzi (NY-D), Tim Kennedy (NY-D).

Sources: govtrack.us, sbaprolife.org, ballotpedia.org, official house.gov
press releases, reproductivefreedomforall.org.

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
    # ---------------- Greg Landsman (OH-D, US Representative OH-1) ----------------
    ("greg-landsman", "OH", "Representative", [
        claim("gl1", "greg-landsman", "sanctity_of_life", 0, False,
              "SBA Pro-Life America documents Landsman as consistently voting to eliminate or prevent protections for the unborn and for children born alive after failed abortions throughout his congressional career; Reproductive Freedom for All gives him a 100% pro-choice rating.",
              ["https://sbaprolife.org/representative/greg-landsman",
               "https://reproductivefreedomforall.org/lawmaker/greg-landsman/"]),
        claim("gl2", "greg-landsman", "self_defense", 1, False,
              "Landsman joined the House Gun Violence Prevention Task Force and publicly declared that 'comprehensive background checks and banning weapons of war will save lives and make us more free' — a direct embrace of assault-weapons bans and expanded background-check legislation.",
              ["https://landsman.house.gov/posts/landsman-joins-house-gun-violence-prevention-task-force",
               "https://www.govtrack.us/congress/members/greg_landsman/456928"]),
        claim("gl3", "greg-landsman", "sanctity_of_life", 4, False,
              "Reproductive Freedom for All (formerly NARAL Pro-Choice America) rates Landsman at 100% — placing him squarely inside the abortion-industry endorsement network that the rubric requires candidates to avoid.",
              ["https://reproductivefreedomforall.org/lawmaker/greg-landsman/",
               "https://ballotpedia.org/Greg_Landsman"]),
    ]),

    # ---------------- Emilia Sykes (OH-D, US Representative OH-13) ----------------
    ("emilia-sykes", "OH", "Representative", [
        claim("es1", "emilia-sykes", "sanctity_of_life", 0, False,
              "Sykes led House Democrats' push to protect access to emergency abortions and has repeatedly stated that abortion restrictions are unconstitutional; SBA Pro-Life documents her as voting consistently against protections for the unborn and for children born alive after failed abortions.",
              ["https://sykes.house.gov/media/in-the-news/sykes-leads-democratic-push-to-protect-emergency-abortion-access",
               "https://sbaprolife.org/representative/emilia-sykes"]),
        claim("es2", "emilia-sykes", "biblical_marriage", 2, False,
              "Sykes is an original co-sponsor of the Equality Act, which would expand federal non-discrimination law to include gender identity and sexual orientation across housing, employment, and public accommodations — directly enshrining transgender ideology in federal civil-rights law.",
              ["https://sykes.house.gov/media/press-releases/rep-sykes-co-leads-equality-act",
               "https://ballotpedia.org/Emilia_Sykes"]),
        claim("es3", "emilia-sykes", "self_defense", 1, False,
              "Sykes co-sponsored H.R. 698 (Assault Weapons Ban) and joined House Democrats in forcing floor consideration of three gun-control bills including the Bipartisan Background Checks Act and Enhanced Background Checks Act — a comprehensive record in favor of federal firearms restrictions.",
              ["https://sykes.house.gov/media/press-releases/rep-sykes-co-sponsors-legislation-ban-assault-weapons",
               "https://sykes.house.gov/media/press-releases/rep-sykes-joins-house-democrats-push-advance-gun-safety-legislation-during-gun"]),
    ]),

    # ---------------- Yvette Clarke (NY-D, US Representative NY-9) ----------------
    ("yvette-clarke", "NY", "Representative", [
        claim("yc1", "yvette-clarke", "sanctity_of_life", 0, False,
              "SBA Pro-Life America documents Clarke as consistently voting to eliminate or prevent protections for the unborn and for children born alive after failed abortions, and to eliminate prohibitions on taxpayer funding of abortion — a record spanning her entire tenure in Congress since 2007.",
              ["https://sbaprolife.org/representative/yvette-clarke",
               "https://reproductivefreedomforall.org/lawmaker/yvette-clarke/"]),
        claim("yc2", "yvette-clarke", "biblical_marriage", 1, False,
              "Clarke issued a formal statement celebrating passage of the Respect for Marriage Act (Dec. 2022), declaring that it 'preserves the right for gay and interracial couples to marry' — confirming her vote for the bill that repealed the federal Defense of Marriage Act's one-man-one-woman definition.",
              ["https://clarke.house.gov/congresswoman-clarke-issues-statement-on-the-passage-of-the-respect-for-marriage-act/",
               "https://www.govtrack.us/congress/votes/117-2022/h513"]),
    ]),

    # ---------------- Tom Suozzi (NY-D, US Representative NY-3) ----------------
    ("tom-suozzi", "NY", "Representative", [
        claim("ts1", "tom-suozzi", "sanctity_of_life", 4, False,
              "Reproductive Freedom for All (formerly NARAL Pro-Choice America) endorsed Suozzi in his February 2024 special-election campaign and celebrated his victory, documenting a 100% pro-choice lifetime congressional rating — placing him fully within the abortion-industry endorsement network the rubric disqualifies.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-tom-suozzi-in-ny-03-special-election/",
               "https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-tom-suozzis-victory-in-ny-03/"]),
        claim("ts2", "tom-suozzi", "self_defense", 1, False,
              "Suozzi lists 'common-sense gun safety' as a signature accomplishment of his bipartisan record, promoting expanded background checks and assault-weapons restrictions as core legislative priorities throughout his congressional service.",
              ["https://suozzi.house.gov/media/in-the-news/new-york-times-tom-suozzi-returns-congress-2-words-house-wake",
               "https://ballotpedia.org/Tom_Suozzi"]),
        claim("ts3", "tom-suozzi", "sanctity_of_life", 0, False,
              "Suozzi has consistently promoted 'full access to reproductive health care' as a core platform plank and built his special-election campaign around defending abortion rights — rejecting any life-at-conception or personhood standard.",
              ["https://suozzi.house.gov/about/votes-and-legislation",
               "https://ballotpedia.org/Tom_Suozzi"]),
    ]),

    # ---------------- Tim Kennedy (NY-D, US Representative NY-26) ----------------
    ("tim-kennedy", "NY", "Representative", [
        claim("tk1", "tim-kennedy", "sanctity_of_life", 0, False,
              "Kennedy ran explicitly on protecting abortion access at the federal level, having previously codified Roe v. Wade in the New York State Senate; his congressional biography commits him to 'leading that fight' nationally — rejecting any federal life-at-conception or personhood standard.",
              ["https://kennedy.house.gov/about/",
               "https://ballotpedia.org/Tim_Kennedy_(New_York)"]),
        claim("tk2", "tim-kennedy", "self_defense", 1, False,
              "Kennedy maintains a dedicated Gun Violence Prevention legislative issue page and led 47 House colleagues in urging the Trump administration's ATF director to reverse DOGE-driven efforts to weaken ATF enforcement capacity — opposing any rollback of federal firearms regulations.",
              ["https://kennedy.house.gov/news/documentquery.aspx?IssueID=15077",
               "https://www.govtrack.us/congress/members/timothy_kennedy/456957"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
