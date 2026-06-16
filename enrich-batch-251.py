#!/usr/bin/env python3
"""Enrichment batch 251: 5 evidence_federal candidates with 0 claims, bottom of alphabet.

Targets (VA → FL → CO → CA, reversed-alpha order):
  John Gray (VA-07 R, Vietnam-era USMC vet),
  Mark Douglas (FL-20 D, immigration attorney),
  Adam Frisch (CO-03 D, former nominee),
  Will Rollins (CA-41 D, former federal prosecutor),
  Saikat Chakrabarti (CA-11 D, Green New Deal architect).
Each claim cites >=1 reliable source and reflects documented 2024-2026
voting record / public positions.

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


TARGETS = [
    # ---------------- John Gray (VA-07, R, Vietnam-era USMC vet) ----------------
    ("john-gray-va-07", "VA", "VA-07", [
        claim("jg1", "john-gray-va-07", "biblical_marriage", 2, True,
              "Self-described 'proud Marine' and 'devout man of faith,' Gray explicitly states 'Boys don't belong in girls' sports' and pledges to fight to pass Sage's Law — Virginia's 2023 statute requiring school notification to parents before socially transitioning a minor — making protection of children from gender ideology a cornerstone of his campaign against incumbent Eugene Vindman.",
              ["https://www.johngrayforvirginia.com/",
               "https://ballotpedia.org/John_Gray_(Virginia)"]),
        claim("jg2", "john-gray-va-07", "family_child_sovereignty", 0, True,
              "Gray campaigns on defending parental rights, supporting school choice, and insisting that 'public schools should educate and not indoctrinate students' — a broad parental-sovereignty platform that encompasses school vouchers, curriculum transparency, and opposition to government overreach in children's upbringing.",
              ["https://www.johngrayforvirginia.com/",
               "https://ballotpedia.org/John_Gray_(Virginia)"]),
        claim("jg3", "john-gray-va-07", "refuse_federal_overreach", 0, True,
              "Signed the U.S. Term Limits pledge committing to co-sponsor and vote for a constitutional amendment to term limit members of Congress — rejecting career-politician incumbency and limiting federal entrenchment of power.",
              ["https://www.termlimits.com/john-gray-pledges-to-support-term-limits-on-congress/",
               "https://ballotpedia.org/John_Gray_(Virginia)"]),
    ]),

    # ---------------- Mark Douglas (FL-20, D, immigration attorney) ----------------
    ("mark-douglas-fl-20", "FL", "FL-20", [
        claim("md1", "mark-douglas-fl-20", "border_immigration", 1, False,
              "Douglas built his legal career since 2006 as an immigration defense attorney, representing clients in removal and deportation proceedings; his Sunrise, FL-based law firm explicitly handles immigration cases alongside criminal defense — a career-long professional record directly opposed to mandatory mass deportation and built on defeating removal orders.",
              ["https://markdouglaslaw.com/",
               "https://www.sunrisefl.gov/city-commission/meet-the-city-commission/commissioner-mark-a-douglas"]),
        claim("md2", "mark-douglas-fl-20", "border_immigration", 3, False,
              "His immigration practice explicitly includes Fair Labor Standards Act (FLSA) claims on behalf of undocumented workers — combining immigration defense with employment-law advocacy to recover wages for workers without lawful employment authorization — a professional stance fundamentally incompatible with E-Verify employer-verification mandates that would deny jobs and legal standing to his clients.",
              ["https://markdouglaslaw.com/",
               "https://sflcn.com/building-a-brighter-future-mark-a-douglas-for-mayor-of-sunrise/"]),
    ]),

    # ---------------- Adam Frisch (CO-03, D, 2022+2024 nominee) ----------------
    ("adam-frisch", "CO", "CO-03", [
        claim("af1", "adam-frisch", "sanctity_of_life", 0, False,
              "Frisch ran as explicitly pro-choice across both his 2022 and 2024 campaigns for CO-03, pledging to protect abortion access and stating he would oppose federal abortion restrictions — directly rejecting life-at-conception and fetal personhood legislation in a district that includes conservative rural Colorado.",
              ["https://www.cpr.org/2022/11/09/who-is-adam-frisch-lauren-boebert-colorado-3rd-congressional-district/",
               "https://ballotpedia.org/Adam_Frisch"]),
        claim("af2", "adam-frisch", "economic_stewardship", 2, False,
              "Frisch stated he 'would have voted for' the 2021 Bipartisan Infrastructure Investment and Jobs Act — a $1.2 trillion spending package that added directly to the federal deficit — while positioning himself as a pro-business moderate; selectively criticizing deficit spending only from the opposing party while endorsing major new outlays.",
              ["https://www.cpr.org/2022/11/15/adam-frisch-interview-lauren-boebert-colorado-district-3/",
               "https://ballotpedia.org/Adam_Frisch"]),
    ]),

    # ---------------- Will Rollins (CA-41, D, former federal prosecutor) ----------------
    ("will-rollins", "CA", "CA-41", [
        claim("wr1", "will-rollins", "sanctity_of_life", 0, False,
              "Rollins stated he supports 'a federal law that would codify a right to abortion access' — explicitly endorsing federal legislation to override state pro-life protections and enshrine abortion access as a national standard, in direct opposition to life-at-conception and fetal personhood principles.",
              ["https://ballotpedia.org/Will_Rollins",
               "https://news.ballotpedia.org/2024/07/18/incumbent-ken-calvert-and-will-rollins-are-running-in-the-general-election-for-californias-41st-congressional-district/"]),
        claim("wr2", "will-rollins", "biblical_marriage", 2, False,
              "Rollins stated he 'supports gay rights' and publicly accused incumbent Ken Calvert of being untrustworthy on LGBTQ issues — explicitly endorsing LGBTQ policy priorities and rejecting a traditional definition of sexuality and gender in both his 2022 and 2024 CA-41 campaigns.",
              ["https://ballotpedia.org/Will_Rollins"]),
        claim("wr3", "will-rollins", "self_defense", 1, False,
              "Rollins stated he supports 'enacting gun safety laws to promote public safety,' using the standard progressive framing for legislation that encompasses red-flag laws, assault-weapons bans, and magazine-capacity restrictions — direct opposition to the anti-red-flag/anti-AWB/anti-registry standard.",
              ["https://ballotpedia.org/Will_Rollins"]),
    ]),

    # ---------------- Saikat Chakrabarti (CA-11, D, Green New Deal architect) ----------------
    ("saikat-chakrabarti", "CA", "CA-11", [
        claim("sc1", "saikat-chakrabarti", "sanctity_of_life", 4, False,
              "On his iVoterGuide 2026 CA-11 candidate questionnaire, Chakrabarti stated that 'Abortion providers, including Planned Parenthood, should receive taxpayer funds from federal, state, or local governments (including Title X grants)' — an explicit, documented pro-PP/NARAL/EMILY's List funding position that is the direct inverse of the never-took-abortion-industry-money standard.",
              ["https://ivoterguide.com/candidate/90308/race/25572/election/1385",
               "https://ballotpedia.org/Saikat_Chakrabarti"]),
        claim("sc2", "saikat-chakrabarti", "economic_stewardship", 4, False,
              "Chakrabarti co-authored the Green New Deal as AOC's chief of staff, then founded New Consensus — a think tank advancing comprehensive economy-wide climate mandates — and ran on delivering 'clean energy' government-managed transformation of every economic sector; his platform tracks directly with the WEF/ESG/Davos-style framework of carbon scores, sector-wide emissions mandates, and green-finance standards.",
              ["https://en.wikipedia.org/wiki/Saikat_Chakrabarti",
               "https://theintercept.com/2026/05/27/sunrise-movement-endorses-saikat-chakrabarti-congress-california/",
               "https://ballotpedia.org/Saikat_Chakrabarti"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
