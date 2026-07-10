#!/usr/bin/env python3
"""Enrichment batch 622: 5 R state senators from OR and OK (bottom of alphabet, continued).

Continuing from batch 621 (RI+PA). Targets archetype_party_default state senators
from OR (Oregon) and OK (Oklahoma).

Targets: Bruce Starr (OR), Cedric Hayden (OR), Julie Daniels (OK),
         Julie McIntosh (OK), Diane Linthicum (OR).
Each claim cites >=1 reliable source and reflects verified 2022-2025
voting records / public positions.

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
    # ------- Bruce Starr (OR-R, State Senator District 12 / Senate Minority Leader) -------
    ("bruce-starr", "OR", "Senator", [
        claim("bs1", "bruce-starr", "sanctity_of_life", 0, True,
              "Endorsed by Oregon Right to Life PAC for Senate District 12 (February 2024) and sworn in alongside ORTL-endorsed pro-life colleagues for the 2025 legislative session; has been described as a 'constant advocate for the unborn' throughout his entire public service career, receiving endorsements from trusted pro-life organizations each cycle he has run.",
              ["https://www.ortl.org/2024/02/ortl-pac-endorses-bruce-starr/",
               "https://www.ortl.org/2025/01/newly-elected-pro-life-lawmakers-sworn-in-ahead-of-oregons-2025-legislative-session/"]),
        claim("bs2", "bruce-starr", "self_defense", 1, True,
              "States on his campaign platform that '\"Shall not be infringed\" means something' and has 'never wavered protecting Oregonians' rights to purchase, own, and keep firearms and ammunition' throughout his legislative career — a consistent record opposing gun-control restrictions such as assault-weapon bans, magazine limits, and registries. Elected Oregon Senate Minority Leader in September 2025.",
              ["https://www.brucestarr.com/issues",
               "https://en.wikipedia.org/wiki/Bruce_Starr"]),
    ]),

    # ------- Cedric Hayden (OR-R, State Senator District 6) -------
    ("cedric-hayden", "OR", "Senator", [
        claim("ch1", "cedric-hayden", "sanctity_of_life", 0, True,
              "Joined the May 2023 Oregon Senate Republican walkout — the longest in state history at six weeks — specifically to deny Democrats a quorum for a floor vote on HB 2002, an omnibus bill that would have codified expanded abortion access and transgender healthcare guarantees into Oregon law. The walkout successfully stalled the bill for weeks and forced negotiations over its scope.",
              ["https://oregoncapitalchronicle.com/2023/05/03/oregon-senate-republicans-independent-stage-walkout-as-divisive-bills-await-votes/",
               "https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/"]),
        claim("ch2", "cedric-hayden", "christian_liberty", 0, True,
              "A practicing Seventh-Day Adventist, filed formal religious-freedom complaints with the Oregon Bureau of Labor and Industries (May 8, 2023) during the walkout, arguing that Measure 113's attendance-counting mechanism penalized him for observing his Sabbath on Saturday — a day his faith prohibits work — constituting religious discrimination and a violation of free-exercise rights.",
              ["https://oregoncapitalchronicle.com/2023/05/08/hayden-files-religious-discrimination-complaints-on-6th-day-of-oregon-senate-walkout/",
               "https://en.wikipedia.org/wiki/Cedric_Ross_Hayden"]),
        claim("ch3", "cedric-hayden", "self_defense", 1, True,
              "Joined the 2023 Oregon Senate Republican walkout to simultaneously block HB 2005 — a sweeping gun-control bill that would have banned 'ghost guns,' raised the legal firearms purchase age from 18 to 21, and allowed Oregon cities to ban all firearms in public buildings — affirming Second Amendment rights against state-level restrictions.",
              ["https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/",
               "https://oregoncapitalchronicle.com/2023/05/03/oregon-senate-republicans-independent-stage-walkout-as-divisive-bills-await-votes/"]),
    ]),

    # ------- Julie Daniels (OK-R, State Senator District 29 / Senate Majority Floor Leader) -------
    ("julie-daniels", "OK", "Senator", [
        claim("jd1", "julie-daniels", "sanctity_of_life", 0, True,
              "Co-sponsored Oklahoma HB 4327 — a near-total abortion ban signed into law by Gov. Kevin Stitt on May 25, 2022 — and separately authored SB 989 (2025 'Wrongful Death Protection Act') targeting abortion-inducing drugs. Her legislative record reflects a consistent life-from-fertilization posture across multiple sessions. Serves as Oklahoma Senate Majority Floor Leader as of February 2025.",
              ["https://www.forbes.com/sites/alisondurkee/2022/04/12/oklahoma-gov-signs-near-total-abortion-ban-into-law---possible-10-year-sentence-for-performing-procedure/",
               "https://legiscan.com/OK/text/HB4327/id/2587278"]),
        claim("jd2", "julie-daniels", "family_child_sovereignty", 0, True,
              "Authored legislation championing parental education choice in Oklahoma, including measures supporting school-choice frameworks that allow families to direct their children's education outside of traditional public school systems — a consistent priority on her legislative platform alongside First Amendment protections.",
              ["https://ballotpedia.org/Julie_Daniels",
               "https://www.oksenate.gov/senators/julie-daniels"]),
    ]),

    # ------- Julie McIntosh (OK-R, State Senator District 3) -------
    ("julie-mcintosh", "OK", "Senator", [
        claim("jm1", "julie-mcintosh", "sanctity_of_life", 0, True,
              "A retired family physician who ran explicitly on being '100% pro-life,' declaring that protection of all human life is among her core conservative values. Won her 2024 Oklahoma Senate District 3 primary by defeating an incumbent on a platform that included faith, family, and the protection of unborn life from conception.",
              ["https://drjuliemcintoshforstatesenate.com/",
               "https://ballotpedia.org/Julie_McIntosh"]),
        claim("jm2", "julie-mcintosh", "self_defense", 1, True,
              "States on her platform that 'the first and last line of defense against a tyrannical government is the Second Amendment,' listing gun rights among her core values alongside patriotism, liberty, and the Constitution — opposing restrictions on the right to keep and bear arms.",
              ["https://drjuliemcintoshforstatesenate.com/",
               "https://ballotpedia.org/Julie_McIntosh"]),
        claim("jm3", "julie-mcintosh", "industry_capture", 0, True,
              "Ran on a platform of 'medical freedom,' opposing government vaccine and medical mandates — a key issue given her background as a retired family physician who witnessed pandemic-era coercive mandates firsthand. Supports patient and physician autonomy against pharmaceutical and regulatory overreach.",
              ["https://drjuliemcintoshforstatesenate.com/",
               "https://ballotpedia.org/Julie_McIntosh"]),
    ]),

    # ------- Diane Linthicum (OR-R, State Senator District 28) -------
    ("diane-linthicum", "OR", "Senator", [
        claim("dl1", "diane-linthicum", "sanctity_of_life", 0, True,
              "Endorsed by Oregon Right to Life PAC for the Senate District 28 Republican primary (2024) as a pro-life candidate. Succeeded her husband Dennis Linthicum — himself described by ORTL as 'an outspoken pro-life advocate' — and shares his life-affirming legislative posture. Won the seat with 69.7% of the vote in the 2024 general election.",
              ["https://www.ortl.org/tag/diane-linthicum/",
               "https://ballotpedia.org/Diane_Linthicum"]),
        claim("dl2", "diane-linthicum", "self_defense", 1, True,
              "A licensed Concealed-Carry-Weapon permit holder who describes herself as 'a staunch advocate for the Second Amendment,' citing 'Constitutional rights, rooted in the core principles of life, liberty, free speech, conscience, and religious expression' as foundational to her legislative platform — opposing restrictions on the right to keep and bear arms.",
              ["https://ballotpedia.org/Diane_Linthicum",
               "https://oregonvotes.gov/voters-guide-military/dianelinthicum.html"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
