#!/usr/bin/env python3
"""Enrichment batch 598: 4 state senators from bottom-of-alphabet states.

All archetype_curated federal senator/rep buckets are fully depleted.
This batch shifts to archetype_party_default state senators starting from
the bottom of the alphabet (SC, OK) — collision-avoidance zone for the
cloud enrichment agent.

Targets (4 R): A. Shane Massey (SC), Todd Gollihare (OK),
Roland Pederson (OK), Randy Grellner (OK).
Claims span distinct rubric categories with 2024-2026 sourced positions
plus verified older votes (Pederson 2019 constitutional-carry YES).
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
    # -------------- A. Shane Massey (SC-R, State Senator) ---------------
    ("a-shane-massey", "SC", "Senator", [
        claim("sm1", "a-shane-massey", "sanctity_of_life", 0, True,
              "Served as lead co-sponsor of South Carolina's Fetal Heartbeat and Protection from Abortion Act (SB 474), banning most abortions once fetal cardiac activity is detected (~6 weeks), signed into law by Governor McMaster on May 25, 2023. Massey declared: 'Twenty-nine Republican Senators have voted twice to pass a heartbeat bill, and I look forward to returning with these members to continue the fight for life in South Carolina.'",
              ["https://www.fitsnews.com/2021/01/28/shane-massey-touts-his-leadership-on-gop-heartbeat-bill/",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm"]),
        claim("sm2", "a-shane-massey", "self_defense", 0, True,
              "Brokered passage of South Carolina's Constitutional Carry (permitless carry) law (S3594) through the Senate, which passed 28-15 on February 1, 2024, and was signed by Governor McMaster on March 7, 2024 — allowing law-abiding adults to carry a handgun without a government permit or mandatory training requirement.",
              ["https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.live5news.com/2024/03/07/mcmaster-signs-constitutional-carry-bill/"]),
        claim("sm3", "a-shane-massey", "biblical_marriage", 2, True,
              "Championed South Carolina's Student Physical Privacy Act (HB 4756), signed into law in 2024, requiring K-12 public schools and state colleges to assign bathrooms, changing rooms, and dormitory housing strictly by biological sex — with institutions risking loss of 25% of state funding for violations. At the signing Massey declared: 'If it falls on South Carolina to educate the rest of the country about what a woman is, we are happy to.'",
              ["https://www.wrdw.com/2024/04/28/sc-measure-would-ban-transgender-students-restroom-choices/",
               "https://abcnews4.com/news/state/gov-mcmaster-signs-law-mandating-sex-based-school-bathrooms-public-k-12-biological-gender-opposite-public"]),
    ]),

    # -------------- Todd Gollihare (OK-R, State Senator) ----------------
    ("todd-gollihare", "OK", "Senator", [
        claim("tg1", "todd-gollihare", "christian_liberty", 0, True,
              "Authored Oklahoma SB 743, protecting worship services from intentional disruption — the first bill signed by Governor Kevin Stitt in the 2026 legislative session. The measure passed the Senate 31-15 and imposes misdemeanor penalties (rising to felony status for repeat offenders) on those who unlawfully disrupt religious assemblies. Gollihare introduced the bill after his own church (Blue Bell Freewill Baptist, Creek County) was targeted.",
              ["https://oksenate.gov/press-releases/gollihare-champions-bill-shield-worship-services-disruption",
               "https://oklahomavoice.com/briefs/bill-to-protect-oklahoma-worship-services-becomes-law/",
               "https://www.kosu.org/religion/2026-02-05/bill-protecting-places-of-worship-from-disruptors-heads-to-oklahoma-governor"]),
        claim("tg2", "todd-gollihare", "sanctity_of_life", 0, True,
              "A retired U.S. Marine Corps Lieutenant Colonel with 24 years of service, Gollihare has publicly committed to 'always protect the Right to Life,' placing Oklahoma's existing near-total abortion protections among his core legislative priorities and consistently opposing any effort to restore abortion access.",
              ["https://gollihare.com/",
               "https://oksenate.gov/senators/todd-gollihare"]),
        claim("tg3", "todd-gollihare", "self_defense", 0, True,
              "A combat veteran and 24-year Marine who pledged to 'stand strong for the American flag and the Second Amendment,' Gollihare represents District 12 (Creek and Tulsa Counties) in a constitutional-carry state and has actively opposed new restrictions on firearm ownership and carry rights.",
              ["https://gollihare.com/",
               "https://oksenate.gov/senators/todd-gollihare"]),
    ]),

    # -------------- Roland Pederson (OK-R, State Senator) ---------------
    ("roland-pederson", "OK", "Senator", [
        claim("rp1", "roland-pederson", "self_defense", 0, True,
              "Voted YES on HB 2597, Oklahoma's landmark Constitutional Carry bill, which passed the Senate 40-6 on February 20, 2019, and was the very first bill signed by then-new Governor Kevin Stitt (Feb. 27, 2019). The law allows any qualified adult 21+ (or 18+ active-duty military) to carry a firearm without a government-issued permit.",
              ["http://webserver1.lsb.state.ok.us/cf/2019-20%20SUPPORT%20DOCUMENTS/votes/Senate/HB2597_VOTES.HTM",
               "https://oklahoma.gov/governor/newsroom/newsroom/2019/february/governor-kevin-stitt-signs-legislation-to-establish-constitution.html"]),
        claim("rp2", "roland-pederson", "sanctity_of_life", 0, True,
              "Describes himself as 'pro-life' and has consistently aligned with Oklahoma's pro-life legislative majority since taking office in 2016 — a majority that enacted one of the nation's most protective abortion regimes, including HB 4327 (signed April 26, 2022), prohibiting nearly all abortions with narrow exceptions for the mother's life.",
              ["https://en.wikipedia.org/wiki/Roland_Pederson",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=HB4327&Session=2200"]),
    ]),

    # -------------- Randy Grellner (OK-R, State Senator) ----------------
    ("randy-grellner", "OK", "Senator", [
        claim("rg1", "randy-grellner", "industry_capture", 0, True,
              "As a rural osteopathic physician with 25 years of practice, Grellner publicly opposed COVID-19 vaccine mandates and mask mandates, prescribed ivermectin to patients during the pandemic, and has characterized the mRNA COVID-19 vaccine as 'gene therapy' and 'not a vaccine' — a consistent record of challenging pharmaceutical-government consensus and opposing mandated medical interventions.",
              ["https://en.wikipedia.org/wiki/Randy_Grellner",
               "https://www.drgrellnerforsenate.com/"]),
        claim("rg2", "randy-grellner", "sanctity_of_life", 0, True,
              "Affirms the protection of life at conception and opposes taxpayer funding for abortion providers including Planned Parenthood. Supports requiring chemical abortion drugs to meet all FDA safety standards and reporting requirements — among the most protective pro-life positions in Oklahoma's conservative caucus.",
              ["https://ivoterguide.com/candidate/67467/race/21194/election/1231",
               "https://www.drgrellnerforsenate.com/"]),
        claim("rg3", "randy-grellner", "self_defense", 1, True,
              "Rated 'A' by the Oklahoma 2nd Amendment Association (OK2A), affirming his opposition to red-flag laws, assault-weapons bans, magazine restrictions, and other gun-control measures. Describes himself as '100% pro Second Amendment and pro states' rights.'",
              ["https://www.ok2a.org/2024-voting-scorecard/",
               "https://ivoterguide.com/candidate/67467/race/21194/election/1231"]),
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36MB, under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
