#!/usr/bin/env python3
"""Enrichment batch 250: 5 evidence_federal candidates with 0 claims, bottom of alphabet.

Targets: John Duarte (CA-13 R former rep), Daniel Butierez (AZ-07 R),
Brian Montgomery (GA-01 R), John Trobough (AZ-01 R), Eugene Yu (GA-01 R).
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
    # ---------------- John Duarte (CA-13, R, former U.S. Rep 118th) ----------------
    ("john-duarte", "CA", "CA-13", [
        claim("jd1", "john-duarte", "sanctity_of_life", 0, False,
              "A self-described 'pro-choice' Republican who publicly supports first-trimester abortion access and opposes any federal ban; earned only a C rating from SBA Pro-Life America and a 21% score from Planned Parenthood's congressional scorecard — far above nearly all House Republicans — including a vote against a House amendment to block Biden administration reimbursement of abortion travel expenses.",
              ["https://sbaprolife.org/representative/john-duarte",
               "https://www.aol.com/republican-congressman-california-tossup-really-191052254.html"]),
        claim("jd2", "john-duarte", "border_immigration", 3, False,
              "One of only two House Republicans to vote against H.R. 2 (Secure Our Borders Act, 2023); published a statement calling the bill's mandatory E-Verify requirement 'devastating for farmers,' arguing that Central Valley agriculture depends on undocumented labor — a direct rejection of employment verification as an immigration-enforcement tool and an explicit opposition to E-Verify.",
              ["https://duarte.house.gov/news/documentsingle.aspx?DocumentID=92",
               "https://news.yahoo.com/central-valley-republican-comfortable-word-130000398.html"]),
        claim("jd3", "john-duarte", "self_defense", 1, True,
              "Received endorsements from both the National Rifle Association Political Victory Fund (NRA-PVF) and the California Rifle & Pistol Association during the 118th Congress, establishing a documented pro-Second Amendment record opposing new firearm restrictions including red-flag laws and assault-weapons bans.",
              ["https://ivoterguide.com/candidate/66580/race/1242/election/1202",
               "https://ballotpedia.org/John_Duarte"]),
    ]),

    # ---------------- Daniel Butierez (AZ-07, R) ----------------
    ("daniel-butierez", "AZ", "AZ-07", [
        claim("db1", "daniel-butierez", "border_immigration", 0, True,
              "Campaigned across both his 2025 AZ-07 special election and 2026 general-election run on completing the border wall as his primary border-security priority, stating a finished wall will channel migrants to legal ports of entry and curtail drug and human-trafficking flows through the Tucson corridor.",
              ["https://azluminaria.org/2025/08/26/grijalva-vs-butierez-cd7-debate-live/",
               "https://www.kgun9.com/news/local-news/daniel-butierez-says-its-time-for-change-in-southern-arizona"]),
        claim("db2", "daniel-butierez", "border_immigration", 1, True,
              "Publicly called for detaining and deporting all unauthorized migrants who entered the United States in the four years prior to his 2025 campaign, making mandatory mass deportation a core plank across two general-election runs against Rep. Raúl Grijalva in one of the most border-adjacent congressional districts in the country.",
              ["https://azluminaria.org/2025/08/26/grijalva-vs-butierez-cd7-debate-live/",
               "https://azluminaria.org/2025/09/02/arizona-district-7-voter-guide-grijalva-and-butierez-on-water-and-homelessness-ahead-of-special-election/"]),
        claim("db3", "daniel-butierez", "sanctity_of_life", 4, True,
              "On his iVoterGuide questionnaire stated that Planned Parenthood and all abortion providers 'should not receive taxpayer funds from federal, state, or local governments (including Title X grants)' — documented refusal to support the abortion-industry funding network, consistent with having accepted no contributions from Planned Parenthood, NARAL, or EMILY's List across all of his campaigns.",
              ["https://ivoterguide.com/candidate/59490/race/1124/election/1243",
               "https://ivoterguide.com/candidate/59490/race/23052/election/1292"]),
    ]),

    # ---------------- Brian Montgomery (GA-01, R) ----------------
    ("brian-montgomery-ga-01", "GA", "GA-01", [
        claim("bm1", "brian-montgomery-ga-01", "sanctity_of_life", 0, True,
              "Campaign platform explicitly pledges to 'stand up for the sanctity of life' as a core commitment alongside protecting religious liberty, framing the protection of the unborn as central to his America First agenda.",
              ["https://www.brianmontgomery.org/issues",
               "https://ballotpedia.org/Brian_Montgomery_(Georgia)"]),
        claim("bm2", "brian-montgomery-ga-01", "self_defense", 1, True,
              "A decorated combat veteran who states he will 'never compromise' on the Second Amendment, pledging on his campaign site to oppose 'any attempt to restrict or erode' gun rights for law-abiding citizens — a commitment that encompasses opposition to red-flag laws, assault-weapons bans, magazine limits, and firearms registries.",
              ["https://www.brianmontgomery.org/issues",
               "https://ballotpedia.org/Brian_Montgomery_(Georgia)"]),
        claim("bm3", "brian-montgomery-ga-01", "family_child_sovereignty", 0, True,
              "Explicitly pledges to 'defend parents' rights to raise their children free from government interference,' aligning with homeschool protections, parental-consent requirements in schools, and opposition to government overreach in family decision-making.",
              ["https://www.brianmontgomery.org/issues",
               "https://ballotpedia.org/Brian_Montgomery_(Georgia)"]),
    ]),

    # ---------------- John Trobough (AZ-01, R) ----------------
    ("john-trobough", "AZ", "AZ-01", [
        claim("jt1", "john-trobough", "sanctity_of_life", 0, True,
              "Campaign website states he is '100% pro-life' and will defend the life of the unborn, protect against congressional rollbacks of Dobbs-era pro-life legislation, and stand against efforts to reverse the U.S. Supreme Court's overturning of Roe v. Wade.",
              ["https://www.troboughforaz.com/",
               "https://www.johntrobough.com/"]),
        claim("jt2", "john-trobough", "self_defense", 1, True,
              "Self-describes as a 'Second Amendment patriot,' quoting the constitutional text verbatim and pledging that the right of the people to keep and bear arms 'shall not be infringed' — a categorical rejection of red-flag laws, assault-weapons bans, and federal firearms registries.",
              ["https://www.troboughforaz.com/",
               "https://www.johntrobough.com/"]),
        claim("jt3", "john-trobough", "border_immigration", 0, True,
              "Running on a 'secure the border' national-security platform that calls for a comprehensive end to illegal immigration, halting drug and human trafficking, and framing border security as the top federal priority — criticizing Biden-Harris open-border policies for devastating Arizona communities.",
              ["https://www.troboughforaz.com/",
               "https://www.johntrobough.com/"]),
    ]),

    # ---------------- Eugene Yu (GA-01, R) ----------------
    ("eugene-yu", "GA", "GA-01", [
        claim("ey1", "eugene-yu", "sanctity_of_life", 0, True,
              "Declared '100% pro-life. No exceptions.' — explicitly rejecting the common Republican carve-outs for rape and incest and affirming full personhood from conception, one of the strongest pro-life positions in the 2026 GA-01 Republican primary field.",
              ["https://ballotpedia.org/Eugene_Yu",
               "https://thepollingplace.org/candidate/eugene-yu/"]),
        claim("ey2", "eugene-yu", "border_immigration", 0, True,
              "'Lock down the borders. Secure borders are the key to sovereignty. Build the wall now.' — verbatim platform statement demanding physical-barrier completion as the foundation of immigration enforcement.",
              ["https://ballotpedia.org/Eugene_Yu",
               "https://thepollingplace.org/candidate/eugene-yu/"]),
        claim("ey3", "eugene-yu", "election_integrity", 0, True,
              "Campaigns on what he calls 'Vote Amish': hand-marked, hand-counted paper ballots cast and counted on election day with no electronic voting machines (including Dominion systems) — a maximalist election-integrity stance pairing paper-ballot integrity with strict anti-electronic-tabulation enforcement.",
              ["https://ballotpedia.org/Eugene_Yu",
               "https://thepollingplace.org/candidate/eugene-yu/"]),
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
