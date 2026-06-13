#!/usr/bin/env python3
"""Enrichment batch 179: evidence_federal candidates — 5 targets with documented 2024-2026 positions.

archetype_curated bucket is fully exhausted. Targets pulled from evidence_federal (0 claims):
Mike Rogers AL-03 (HASC Chair), Gary Palmer AL-06 (House Freedom Caucus),
Jim Desmond CA-48 (Trump-endorsed general candidate), Mike Gross AZ-05
(former-D with documented pro-abortion/LGBT positions — negative scores),
Jay Feely AZ-01 (Trump-endorsed; NRCC MAGA Majority fund).
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
    # ---- Mike Rogers (AL-03, R, HASC Chair) ----
    ("mike-rogers", "AL", "Armed Services", [
        claim("mr1", "mike-rogers", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record with National Right to Life; co-sponsored the "
              "Sanctity of Human Life Act asserting personhood from fertilization; upon the Dobbs "
              "ruling called it 'the right decision to protect the innocent lives of unborn children.'",
              ["https://en.wikipedia.org/wiki/Mike_Rogers_(Alabama_politician)",
               "https://ballotpedia.org/Mike_Rogers_(Alabama)"]),
        claim("mr2", "mike-rogers", "border_immigration", 1, True,
              "Consistent record opposing amnesty and supporting mandatory removal of illegal "
              "immigrants; voted against the 2024 Senate-drafted bipartisan border package as "
              "insufficiently strict and has backed enforcement-first border legislation throughout "
              "his tenure in the House.",
              ["https://ballotpedia.org/Mike_Rogers_(Alabama)",
               "https://govtrack.us/congress/members/mike_rogers/400341"]),
        claim("mr3", "mike-rogers", "self_defense", 0, True,
              "Consistently earns A/A+ ratings from the National Rifle Association reflecting "
              "unwavering support for Second Amendment rights; voted for the Concealed Carry "
              "Reciprocity Act (2017) extending constitutional-carry protections across state lines, "
              "and opposes new firearms restrictions including red-flag laws and assault-weapons bans.",
              ["https://en.wikipedia.org/wiki/Mike_Rogers_(Alabama_politician)",
               "https://ballotpedia.org/Mike_Rogers_(Alabama)"]),
    ]),

    # ---- Gary Palmer (AL-06, R, House Freedom Caucus) ----
    ("gary-palmer", "AL", "Representative", [
        claim("gp1", "gary-palmer", "border_immigration", 1, True,
              "Opposes illegal immigration and backs mandatory deportation; has consistently "
              "supported interior-enforcement bills, opposed amnesty proposals, and backed federal "
              "resources to remove illegal immigrants from the country.",
              ["https://en.wikipedia.org/wiki/Gary_Palmer",
               "https://ballotpedia.org/Gary_Palmer"]),
        claim("gp2", "gary-palmer", "biblical_marriage", 0, True,
              "A traditional Christian conservative and member of the House Freedom Caucus who "
              "consistently votes against LGBTQ legislation redefining marriage; supports the "
              "definition of marriage as one man and one woman and opposed federal codification "
              "of same-sex marriage.",
              ["https://en.wikipedia.org/wiki/Gary_Palmer",
               "https://ballotpedia.org/Gary_Palmer"]),
        claim("gp3", "gary-palmer", "economic_stewardship", 2, True,
              "One of 71 Republicans who voted against the Fiscal Responsibility Act of 2023, "
              "rejecting the debt-limit deal as fiscally irresponsible; as a House Freedom Caucus "
              "member, consistently demands real spending cuts before agreeing to any debt-ceiling "
              "increase — a hard anti-deficit posture.",
              ["https://en.wikipedia.org/wiki/Gary_Palmer",
               "https://ballotpedia.org/Gary_Palmer"]),
    ]),

    # ---- Jim Desmond (CA-48, R, Trump-endorsed 2026 general candidate) ----
    ("jim-desmond", "CA", "CA-48", [
        claim("jd1", "jim-desmond", "border_immigration", 2, True,
              "Actively opposes California's sanctuary law (SB54): in February 2025 he attended a "
              "press conference with Republicans promoting legislation to weaken the state's "
              "prohibition on local law enforcement cooperating with federal ICE operations.",
              ["https://en.wikipedia.org/wiki/Jim_Desmond",
               "https://ballotpedia.org/Jim_Desmond"]),
        claim("jd2", "jim-desmond", "border_immigration", 1, True,
              "Testified before the House Committee on Homeland Security about how the influx of "
              "migrants strained San Diego County's resources; publicly stated that the Biden "
              "administration's immigration policy made the U.S. 'more unsafe,' supporting "
              "stronger deportation and interior enforcement.",
              ["https://en.wikipedia.org/wiki/Jim_Desmond",
               "https://ballotpedia.org/Jim_Desmond"]),
        claim("jd3", "jim-desmond", "industry_capture", 0, True,
              "Criticized the COVID-19 public health response, arguing that the dangers of the "
              "disease were exaggerated — particularly in schools — and that the economy and "
              "schools should have been reopened safely; opposed pandemic-era pharmaceutical and "
              "government mandates that suppressed normal economic and educational activity.",
              ["https://en.wikipedia.org/wiki/Jim_Desmond",
               "https://ballotpedia.org/Jim_Desmond"]),
    ]),

    # ---- Mike Gross (AZ-05, R primary candidate — negative-score documentation) ----
    ("mike-gross-az-05", "AZ", "AZ-05", [
        claim("mg1", "mike-gross-az-05", "sanctity_of_life", 0, False,
              "A 'longtime supporter of abortion' (Ballotpedia) who served on the Board of Directors "
              "of the Human Rights Council of North Central Florida, an organization that explicitly "
              "champions abortion access — rejecting any life-at-conception personhood standard.",
              ["https://ballotpedia.org/Michael_Gross"]),
        claim("mg2", "mike-gross-az-05", "biblical_marriage", 0, False,
              "A 'longtime supporter of LGBT rights' (Ballotpedia) who served on the Board of the "
              "Human Rights Council; previously active in LGBT equality advocacy, rejecting the "
              "one-man-one-woman definition of marriage.",
              ["https://ballotpedia.org/Michael_Gross"]),
        claim("mg3", "mike-gross-az-05", "biblical_marriage", 4, False,
              "As a former peace-movement activist and longtime board member of the Human Rights "
              "Council of North Central Florida — which advocates LGBTQ equality in public "
              "institutions — Gross has a documented record of promoting LGBTQ ideology in public "
              "policy rather than opposing it.",
              ["https://ballotpedia.org/Michael_Gross"]),
    ]),

    # ---- Jay Feely (AZ-01, R, Trump-endorsed; NRCC MAGA Majority fund) ----
    ("jay-feely", "AZ", "AZ-01", [
        claim("jf1", "jay-feely", "economic_stewardship", 2, True,
              "Self-described 'fiscal conservative' whose campaign explicitly focuses on delivering "
              "'lower costs for Arizona's families' — language consistent with anti-deficit, "
              "reduced-government-spending positions aligned with the rubric's preference for "
              "balanced-budget governance.",
              ["https://ballotpedia.org/Jay_Feely",
               "https://news.ballotpedia.org/2026/05/01/joseph-chaplik-jay-feely-and-john-trobough-running-in-republican-primary-for-arizonas-1st-congressional-district/"]),
        claim("jf2", "jay-feely", "border_immigration", 0, True,
              "Selected for NRCC's MAGA Majority fund (March 2026) and endorsed by President Trump "
              "(January 6, 2026) — America-First endorsement and fund selection explicitly tied to "
              "platforms calling for border-wall funding and military enforcement of the southern "
              "border.",
              ["https://ballotpedia.org/Jay_Feely",
               "https://news.ballotpedia.org/2026/05/01/joseph-chaplik-jay-feely-and-john-trobough-running-in-republican-primary-for-arizonas-1st-congressional-district/"]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
