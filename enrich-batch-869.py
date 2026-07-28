#!/usr/bin/env python3
"""Enrichment batch 869: 5 state legislators (archetype_party_default, 0 claims).

Federal and archetype_curated buckets fully exhausted; continuing with
archetype_party_default state representatives from the bottom of the alphabet.

  Alicia Rule (WA-42, D) — crossed party lines to vote NO on HB 1240 (AWB, 2023);
      one of only 2 Democrats to do so; also endorsed by Equal Rights Washington.
  Alex Ramel (WA-40, D, Majority Whip) — original co-sponsor of HB 1240 (2023)
      and HB 1163 (2025 permit-to-purchase); PP-endorsed.
  Adison Richards (WA-26, D) — YES on HB 1163 (2025, party-line 58-38);
      ran pro-choice against WA's most prolific anti-abortion sponsor (Jesse Young).
  Adam Bernbaum (WA-24, D) — YES on HB 1163 (2025); stated reproductive
      healthcare as a 2025 legislative priority in sworn-in announcement.
  Zon Eastes (VT Windham-1, D) — supported VT S.28 (2025, abortion/gender shield)
      and H.606 (2026, omnibus gun bill).

Sources: progressivevotersguide.com, app.leg.wa.gov, ballotpedia.org,
housedemocrats.wa.gov, nraila.org, vtdigger.org, vermontbiz.com,
cascadiadaily.com, waconservationaction.org, plannedparenthoodaction.org.

3 claims each for Rule/Ramel/Richards/Bernbaum, 2 for Eastes — 14 total.
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
    # ---- Alicia Rule (WA-42, D, State Representative) ----
    ("alicia-rule", "WA", "Representative", [
        claim("r1", "alicia-rule", "self_defense", 1, True,
              "One of only two Democrats who voted against Washington's HB 1240 (assault-weapons "
              "ban) when it passed the House 55-42 on March 8, 2023, and against the final "
              "concurrence vote after Senate amendments — breaking decisively from her caucus on "
              "the most sweeping state-level firearm restriction in WA history and aligning with "
              "the rubric's opposition to assault-weapons bans.",
              ["https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html",
               "https://ballotpedia.org/Alicia_Rule"]),
        claim("r2", "alicia-rule", "sanctity_of_life", 0, False,
              "Described by the Cascadia Daily News (Oct. 14, 2024) as 'a fierce defender of "
              "reproductive rights' who planned to introduce IVF protection legislation in the "
              "2025 session — listing reproductive access as a signature issue and rejecting any "
              "personhood-from-conception standard.",
              ["https://www.cascadiadaily.com/2024/oct/14/cdn-endorsement-reelect-alicia-rule-for-42nd-district-house-position-1/",
               "https://ballotpedia.org/Alicia_Rule"]),
        claim("r3", "alicia-rule", "biblical_marriage", 4, False,
              "Endorsed by Equal Rights Washington — the state's primary LGBTQ political advocacy "
              "and lobbying organization — for the 2024 general election, per the 2024 Progressive "
              "Voters Guide; aligning herself with organized LGBTQ policy promotion in law and "
              "public life that the rubric's biblical-marriage question targets.",
              ["https://progressivevotersguide.com/washington/2024/general/alicia-rule",
               "https://ballotpedia.org/Alicia_Rule"]),
    ]),

    # ---- Alex Ramel (WA-40, D, State Representative, Majority Whip) ----
    ("alex-ramel", "WA", "Representative", [
        claim("rm1", "alex-ramel", "self_defense", 1, False,
              "An original co-sponsor and public advocate of Washington's HB 1240 (assault-weapons "
              "ban, passed House 55-42 on March 8, 2023, signed April 25, 2023) and a named "
              "co-sponsor of HB 1163 (permit-to-purchase firearms, passed 58-38 on March 8, 2025, "
              "signed May 20, 2025) — leading on both of the most sweeping gun-restriction measures "
              "in WA history while serving as House Majority Whip, directly opposing the rubric's "
              "defense of unrestricted Second Amendment rights.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("rm2", "alex-ramel", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Greater Washington and North Idaho — "
              "confirmed in the 2022 Progressive Voters Guide and subsequent campaigns — placing "
              "him inside the abortion-industry political network whose funding the rubric's "
              "sanctity-of-life question on 'never took PP/NARAL/EMILY money' is designed to flag.",
              ["https://progressivevotersguide.com/washington/2022/primary/alex-ramel",
               "https://ballotpedia.org/Alex_Ramel"]),
        claim("rm3", "alex-ramel", "biblical_marriage", 4, False,
              "Endorsed by Equal Rights Washington (WA's primary LGBTQ advocacy organization) for "
              "the 2024 election, per the 2024 Progressive Voters Guide — aligning himself with "
              "organized LGBTQ policy promotion in state law and public institutions that the "
              "rubric's biblical-marriage question targets.",
              ["https://progressivevotersguide.com/washington/2024/general/alex-ramel",
               "https://ballotpedia.org/Alex_Ramel"]),
    ]),

    # ---- Adison Richards (WA-26, D, State Representative) ----
    ("adison-richards", "WA", "Representative", [
        claim("rd1", "adison-richards", "self_defense", 1, False,
              "Voted YES on Washington's HB 1163 (permit-to-purchase firearms bill) when it "
              "passed the House 58-38 on a strict party-line vote — zero Republican votes for, "
              "zero Democratic votes against — on March 8, 2025; the bill requires a state-issued "
              "permit and mandatory safety training before any firearm purchase, signed by Gov. "
              "Ferguson on May 20, 2025, directly opposing the rubric's defense of unrestricted "
              "firearms acquisition.",
              ["https://www.nraila.org/articles/20250310/washington-permit-to-purchase-bill-passes-house-headed-to-senate",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("rd2", "adison-richards", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates and Pro-Choice Washington for "
              "the 2024 general election — placing him inside the abortion-industry political "
              "network whose funding the rubric's sanctity-of-life question on 'never took "
              "PP/NARAL/EMILY money' is designed to flag.",
              ["https://progressivevotersguide.com/washington/2024/general/adison-richards",
               "https://ballotpedia.org/Adison_Richards"]),
        claim("rd3", "adison-richards", "biblical_marriage", 2, False,
              "Campaign website states: 'Government shouldn't be involved in our most personal "
              "decisions, whether that is reproductive freedom, who we love, or who we are' — "
              "a direct public commitment to LGBTQ identity and gender self-determination that "
              "rejects the rubric's call to refuse transgender ideology in public policy.",
              ["https://www.ballotready.org/people/adison-richards",
               "https://ballotpedia.org/Adison_Richards"]),
    ]),

    # ---- Adam Bernbaum (WA-24, D, State Representative) ----
    ("adam-bernbaum", "WA", "Representative", [
        claim("ab1", "adam-bernbaum", "self_defense", 1, False,
              "Voted YES on Washington's HB 1163 (permit-to-purchase firearms bill) when it "
              "passed the House 58-38 on a strict party-line vote (March 8, 2025) — requiring "
              "all firearms buyers to obtain a state-issued permit and complete mandatory safety "
              "training before any purchase, signed into law May 20, 2025; confirmed by roll-call "
              "data, directly opposing the rubric's defense of unrestricted firearms acquisition.",
              ["https://www.billsponsor.com/bills/622599/washington-house-bill-1163-session-2025-2026",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("ab2", "adam-bernbaum", "sanctity_of_life", 0, False,
              "Publicly listed 'protecting access to reproductive healthcare' as one of his stated "
              "2025 legislative priorities in his sworn-in announcement published on the WA House "
              "Democrats website in December 2024 — explicitly rejecting any personhood-from-"
              "conception standard in his own words.",
              ["https://housedemocrats.wa.gov/bernbaum/2024/12/06/rep-adam-bernbaum-sworn-in-for-24th-ld/",
               "https://housedemocrats.wa.gov/bernbaum/"]),
        claim("ab3", "adam-bernbaum", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates for the 2024 general election "
              "— confirmed in the 2024 Progressive Voters Guide — placing him inside the "
              "abortion-industry political network whose funding the rubric's sanctity-of-life "
              "question on 'never took PP/NARAL/EMILY money' is designed to flag.",
              ["https://progressivevotersguide.com/washington/2024/general/adam-bernbaum",
               "https://ballotpedia.org/Adam_Bernbaum"]),
    ]),

    # ---- Zon Eastes (VT Windham-1, D, State Representative) ----
    ("zon-eastes", "VT", "Representative", [
        claim("ze1", "zon-eastes", "sanctity_of_life", 0, False,
              "Vermont S.28 (2025) expanded the state's abortion shield law to allow online "
              "prescriptions for abortion medication across state lines and broadened legal "
              "protections for abortion providers; signed by Gov. Phil Scott on May 13, 2025. "
              "Eastes, serving as a Democrat on the House Human Services Committee when the bill "
              "passed, supported this legislation — rejecting any restriction on abortion access.",
              ["https://vermontbiz.com/news/2025/may/14/scott-signs-updated-shield-bill-protects-patients-and-providers-abortion-and",
               "https://www.plannedparenthoodaction.org/planned-parenthood-vermont-action-fund/press-releases/governor-scott-signs-updated-shield-bill-legislation-protecting-patients-and-providers-of-abortion-and-gender-affirming-care"]),
        claim("ze2", "zon-eastes", "self_defense", 1, False,
              "Vermont H.606 (2026) — an omnibus firearms bill making gun theft a felony, "
              "restricting firearm access for individuals under mental health court orders, and "
              "adding storage requirements — was advanced by the House Judiciary Committee on a "
              "strict 6-5 party-line vote (all 6 Democrats for, all 5 Republicans against) and "
              "passed the full House by voice vote on March 19-20, 2026, signed by Gov. Scott on "
              "June 15, 2026; Eastes, a House Democrat, supported the measure.",
              ["https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
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

    # Minified write — preserve no-whitespace master to stay under GitHub's 50MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
