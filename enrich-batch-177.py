#!/usr/bin/env python3
"""Enrichment batch 177: 4 sitting House members from CA (bottom-of-alpha pool).

evidence_federal bucket, bottom-of-alphabet states (CA sitting members):
- Scott Peters (CA-50, D — sitting since 2013, New Democrat Coalition co-chair)
- Sara Jacobs (CA-51, D — sitting since 2021, Equality Caucus VP, Trans Task Force co-chair)
- Lou Correa (CA-46, D — sitting since 2017, Blue Dog, HS Border Subcommittee Ranking Member)
- Salud Carbajal (CA-24, D — sitting since 2017, USMC veteran)

Sources: reproductivefreedomforall.org, sbaprolife.org, ballotpedia.org,
sarajacobs.house.gov, govtrack.us, en.wikipedia.org.
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
    # -------- Scott Peters (CA-50, D — sitting since 2013, New Dem Coalition) ----------
    ("scott-peters", "CA", "Representative", [
        claim("sp1", "scott-peters", "sanctity_of_life", 4, False,
              "Carries a 100% lifetime score from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and an 'F' grade from Susan B. Anthony Pro-Life America — placing him fully inside the abortion-advocacy endorsement network and never meeting the rubric's standard of taking no PP/NARAL/EMILY money.",
              ["https://reproductivefreedomforall.org/lawmaker/scott-peters/",
               "https://sbaprolife.org/representative/scott-peters"]),
        claim("sp2", "scott-peters", "biblical_marriage", 1, False,
              "Voted yes on H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022, passing 267–157), which repealed the Defense of Marriage Act and federally directed recognition of same-sex marriages — directly opposing the rubric's definition of marriage as between one man and one woman.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
    ]),

    # -------- Sara Jacobs (CA-51, D — sitting since 2021, Equality Caucus VP) ----------
    ("sara-jacobs", "CA", "Representative", [
        claim("sj1", "sara-jacobs", "sanctity_of_life", 4, False,
              "Holds a 100% lifetime rating from Planned Parenthood and was arrested outside the U.S. Supreme Court building on July 19, 2022, during a demonstration demanding abortion rights — representing maximum engagement with the abortion-advocacy network, contrary to the rubric's standard of taking no PP/NARAL/EMILY money or endorsement.",
              ["https://sarajacobs.house.gov/about/accomplishments",
               "https://ballotpedia.org/Sara_Jacobs"]),
        claim("sj2", "sara-jacobs", "biblical_marriage", 2, False,
              "Earned a 100% lifetime rating from the Human Rights Campaign; serves as Vice Chair of the Congressional Equality Caucus and Co-Chair of the Transgender Equality Task Force; introduced the Ensuring Military Readiness Not Discrimination Act to prohibit discrimination against transgender service members and protect trans integration into the military — directly opposing the rubric's rejection of transgender ideology.",
              ["https://sarajacobs.house.gov/about/accomplishments",
               "https://www.govtrack.us/congress/members/sara_jacobs/456804"]),
        claim("sj3", "sara-jacobs", "self_defense", 1, False,
              "Voted for both the Assault Weapons Ban of 2022 (H.R. 1808) and the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022) — celebrating the gun-safety package in a House floor speech — enacting expanded background checks, red-flag law incentives, and new criminal penalties, contrary to the rubric's defense of Second Amendment rights against new bans and restrictions.",
              ["https://sarajacobs.house.gov/news/documentsingle.aspx?DocumentID=119",
               "https://www.govtrack.us/congress/votes/117-2022/h299"]),
    ]),

    # -------- Lou Correa (CA-46, D — sitting since 2017, HS Border Subcomte Ranking Member) ----------
    ("lou-correa", "CA", "Representative", [
        claim("lc1", "lou-correa", "sanctity_of_life", 4, False,
              "Carries a 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and an 'F' grade from Susan B. Anthony Pro-Life America across his congressional tenure — placing him inside the abortion-advocacy endorsement network and never meeting the rubric's standard of taking no PP/NARAL/EMILY money.",
              ["https://ballotpedia.org/Lou_Correa",
               "https://justfacts.votesmart.org/candidate/evaluations/9732/lou-correa"]),
        claim("lc2", "lou-correa", "border_immigration", 1, False,
              "Publicly championed H.R. 6, the Dream and Promise Act, declaring DREAMers 'have earned the right to the American Dream' and calling for a legislative pathway to citizenship for DACA recipients — directly opposing the rubric's mandatory-deportation standard for those present illegally.",
              ["https://ballotpedia.org/Lou_Correa",
               "https://en.wikipedia.org/wiki/Lou_Correa"]),
        claim("lc3", "lou-correa", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022) — the first major federal gun legislation in nearly three decades — which enacted expanded background checks for buyers under 21, red-flag law incentives, and tightened straw-purchase rules, contrary to the rubric's standard of defending Second Amendment rights against new restrictions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Bipartisan_Safer_Communities_Act_of_2022"]),
    ]),

    # -------- Salud Carbajal (CA-24, D — sitting since 2017, USMC veteran) ----------
    ("salud-carbajal", "CA", "Representative", [
        claim("sc1", "salud-carbajal", "sanctity_of_life", 0, False,
              "Called the Supreme Court's June 2022 Dobbs v. Jackson Women's Health Organization decision a 'betrayal to our Constitution' and publicly opposed it, rejecting any restriction on abortion access — incompatible with the rubric's standard of protecting life from conception.",
              ["https://en.wikipedia.org/wiki/Salud_Carbajal",
               "https://ballotpedia.org/Salud_Carbajal"]),
        claim("sc2", "salud-carbajal", "biblical_marriage", 1, False,
              "Voted for H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022, passing 267–157), which repealed the Defense of Marriage Act and directed federal recognition of same-sex marriages — directly opposing the rubric's definition of marriage as between one man and one woman.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
        claim("sc3", "salud-carbajal", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022) — backed by all 220 House Democrats — which enacted expanded background checks for buyers under 21, red-flag law incentives, and tightened straw-purchase rules, contrary to the rubric's standard of defending Second Amendment rights against new restrictions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Bipartisan_Safer_Communities_Act_of_2022"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
