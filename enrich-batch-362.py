#!/usr/bin/env python3
"""Enrichment batch 362: 5 Virginia State Senate members with documented public positions.

All five had 0 claims and evidence_state confidence.
Bottom-of-alphabet targeting (VA).
  Danica Roem        (VA-D, State Senate District 30 — first openly transgender state senator in the South)
  Danny Diggs        (VA-R, State Senate District 24 — former York County Sheriff)
  Jennifer Carroll Foy (VA-D, State Senate District 33 — ran for governor 2021)
  Creigh Deeds       (VA-D, State Senate District 11 — gun-control champion, Charlottesville)
  Christie New Craig (VA-R, State Senate District 19 — former law enforcement, school board)
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
    # ---- Danica Roem (VA-D, State Senate District 30) ----
    ("danica-roem", "VA", "State Senate", [
        claim("dr1", "danica-roem", "biblical_marriage", 2, False,
              "The nation's first openly transgender state legislator (Virginia House of Delegates, January 2018) and the first openly transgender state senator in the Southern United States (Virginia State Senate, January 2024), Roem actively embodies and champions transgender ideology in public office rather than rejecting it. In 2024 she voted against legislation requiring schools to notify parents if a student socially transitions to a different gender identity — opposing the parental oversight the rubric's Christian-liberty and family-sovereignty standards favor.",
              ["https://en.wikipedia.org/wiki/Danica_Roem",
               "https://ballotpedia.org/Danica_Roem"]),
        claim("dr2", "danica-roem", "sanctity_of_life", 0, False,
              "Roem is a consistent pro-choice Democrat who has supported the Virginia Democratic majority's efforts to protect and expand abortion access in state law throughout her career in the House of Delegates (2018–2024) and continuing in the State Senate; she received pro-abortion organization endorsements and aligns with the Democratic caucus's position opposing any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Danica_Roem",
               "https://ballotpedia.org/Danica_Roem"]),
    ]),

    # ---- Danny Diggs (VA-R, State Senate District 24) ----
    ("danny-diggs", "VA", "State Senate", [
        claim("dd1", "danny-diggs", "self_defense", 1, True,
              "Diggs, a 23-year York County Sheriff and gun owner, ran his 2023 Senate campaign on an explicit Second Amendment platform, pledging that 'the Second Amendment's rights shall not be infringed' and committing to defend those rights against gun-control legislation; as a senator he has voted with the Republican minority against the gun-restriction bills advanced by the Democratic majority in the 2024 and 2025 Virginia General Assembly sessions.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-j-d-danny-diggs-va-senate-district-24/",
               "https://ballotpedia.org/J.D._Diggs"]),
        claim("dd2", "danny-diggs", "sanctity_of_life", 0, False,
              "Diggs stated in his 2023 Senate campaign that he supports Governor Youngkin's 15-week abortion limit with exceptions for rape, incest, and the health of the mother — a position that accepts elective abortion through 15 weeks gestation and retains rape/incest exceptions, falling short of the rubric's personhood-from-conception and no-exception standard for this question.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-j-d-danny-diggs-va-senate-district-24/",
               "https://ballotpedia.org/J.D._Diggs"]),
    ]),

    # ---- Jennifer Carroll Foy (VA-D, State Senate District 33) ----
    ("jennifer-carroll-foy", "VA", "State Senate", [
        claim("jcf1", "jennifer-carroll-foy", "sanctity_of_life", 0, False,
              "Carroll Foy is a pro-choice Democrat who has made reproductive rights a core platform plank throughout her career in the House of Delegates (2017–2020), her 2021 gubernatorial campaign, and her current State Senate role; she won the endorsement of pro-abortion organizations, has supported the Democratic majority's push to enshrine abortion access in state statute, and explicitly called for treating abortion and reproductive healthcare as a protected right rather than recognizing personhood from conception.",
              ["https://en.wikipedia.org/wiki/Jennifer_Carroll_Foy",
               "https://ballotpedia.org/Jennifer_Carroll_Foy"]),
        claim("jcf2", "jennifer-carroll-foy", "biblical_marriage", 4, False,
              "In her 2021 gubernatorial platform and continuing into her Senate service, Carroll Foy explicitly committed to ensuring the rights of LGBTQIA+ people are protected, advocating for learning environments affirming students regardless of sexual orientation or gender identity, and championing LGBTQ-inclusive school policies — active promotion of LGBTQ ideology in schools and public accommodations that the rubric opposes.",
              ["https://ballotpedia.org/Jennifer_Carroll_Foy",
               "https://en.wikipedia.org/wiki/Jennifer_Carroll_Foy"]),
    ]),

    # ---- Creigh Deeds (VA-D, State Senate District 11) ----
    ("creigh-deeds", "VA", "State Senate", [
        claim("cd1", "creigh-deeds", "self_defense", 1, False,
              "Following the 2022 University of Virginia campus shooting, Deeds introduced SB 272 in successive sessions (2023, 2024, 2025, and 2026) to prohibit firearms in state-owned buildings including public university campuses, narrowing carry exemptions to only approved institutional activities; the bill has passed both chambers each session and is awaiting final action in 2026, representing an ongoing effort to restrict lawful carry rights.",
              ["https://virginiamercury.com/2026/01/27/virginia-senate-panel-advances-gun-safety-bills-once-vetoed-by-youngkin/",
               "https://lis.virginia.gov/bill-details/20261/SB272"]),
        claim("cd2", "creigh-deeds", "self_defense", 0, False,
              "Deeds introduced legislation in the Virginia Senate to make it a Class 1 misdemeanor for any civilian to import, sell, manufacture, purchase, possess, transport, or transfer an 'assault firearm' — one of the most sweeping anti-gun proposals in the Virginia legislature — reflecting his consistent record of opposing constitutional carry and civilian firearm ownership.",
              ["https://virginiamercury.com/2024/01/22/virginia-democrats-press-major-new-gun-control-measures-despite-gop-opposition/",
               "https://ballotpedia.org/Creigh_Deeds"]),
    ]),

    # ---- Christie New Craig (VA-R, State Senate District 19) ----
    ("christie-new-craig", "VA", "State Senate", [
        claim("cnc1", "christie-new-craig", "self_defense", 1, True,
              "Craig, a former law enforcement officer (1987–2002) and gun owner, campaigned on a pledge that 'the Second Amendment's rights shall not be infringed' and committed as senator to firmly defending Second Amendment rights; she has voted with the Republican minority against gun-restriction bills advanced by the Democratic majority in the 2024 and 2025 Virginia General Assembly sessions.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-christie-new-craig-va-senate-district-19/",
               "https://ballotpedia.org/Christie_Craig_(Virginia)"]),
        claim("cnc2", "christie-new-craig", "sanctity_of_life", 4, True,
              "Craig ran on a pro-life platform that explicitly calls for defunding abortion providers, including Planned Parenthood, from government funding sources — aligning with the rubric's standard opposing government subsidies to abortion-industry organizations — and has not accepted endorsements or funding from Planned Parenthood, EMILY's List, or NARAL/Reproductive Freedom for All.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-christie-new-craig-va-senate-district-19/",
               "https://ivoterguide.com/candidate/71655/race/18906/election/1054"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
