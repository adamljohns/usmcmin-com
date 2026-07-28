#!/usr/bin/env python3
"""Enrichment batch 868: 5 Washington State Representatives (archetype_party_default, 0 claims).

Federal and archetype_curated buckets fully exhausted; continuing with
archetype_party_default WA State Representatives from the bottom of the alphabet.
All five are Democratic members of the Washington House — Brandy Donaghy (D-44),
Beth Doglio (D-22), April Berg (D-44), Amy Walen (D-48), Brianna Thomas (D-34).

Sources: en.wikipedia.org, ballotpedia.org, progressivevotersguide.com,
plannedparenthoodaction.org, seattletimes.com, washingtonstatestandard.com,
app.leg.wa.gov (HB 1240 / HB 1163 bill pages), housedemocrats.wa.gov.

Key votes:
  HB 1240 (2023): WA assault-weapons ban, passed House 55-42 party-line 3/8/2023.
  HB 1163 (2025): WA permit-to-purchase firearms, passed House 58-38, signed 5/20/2025.
2 claims each, 10 total — spanning self_defense, sanctity_of_life, and biblical_marriage.
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
    # ---- Brandy Donaghy (WA-44, D, State Representative) ----
    ("brandy-donaghy", "WA", "Representative", [
        claim("bd1", "brandy-donaghy", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice Washington and Planned Parenthood Alliance "
              "Advocates during her December 2021 appointment campaign, and again endorsed "
              "by Planned Parenthood Alliance Advocates in 2024 — placing her squarely "
              "inside the abortion-industry political network whose funding the rubric's "
              "sanctity-of-life question on 'never took PP/NARAL/EMILY money' is designed "
              "to flag.",
              ["https://progressivevotersguide.com/washington/2021/general/brandy-donaghy",
               "https://ballotpedia.org/Brandy_Donaghy"]),
        claim("bd2", "brandy-donaghy", "self_defense", 1, False,
              "Endorsed by Alliance for Gun Responsibility in her 2021 campaign and sits "
              "in the WA House Democratic caucus majority that passed Washington's landmark "
              "HB 1240 (March 8, 2023, 55-42 party-line) banning future sales of AR-15s, "
              "AK-47s, and semi-automatic rifles with detachable or high-capacity magazines "
              "— a sweeping assault-weapons restriction the rubric opposes.",
              ["https://progressivevotersguide.com/washington/2021/general/brandy-donaghy",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
    ]),

    # ---- Beth Doglio (WA-22, D, State Representative) ----
    ("beth-doglio", "WA", "Representative", [
        claim("bdg1", "beth-doglio", "self_defense", 1, False,
              "A sponsor of Washington's HB 1240 (passed March 8, 2023, 55-42), the "
              "landmark assault-weapons ban banning future sales of AR-15s, AK-47s, M-16s, "
              "and semi-automatic firearms with detachable or high-capacity magazines — "
              "among the most sweeping state-level firearm restrictions in the country, "
              "directly opposing the rubric's defense of unrestricted Second Amendment "
              "rights.",
              ["https://ballotpedia.org/Beth_Doglio",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
        claim("bdg2", "beth-doglio", "sanctity_of_life", 4, False,
              "Before entering electoral politics, volunteered as a field organizer for the "
              "National Abortion and Reproductive Rights Action League (NARAL), placing her "
              "inside the organized pro-abortion advocacy network the rubric's sanctity-of-life "
              "question specifically names — identifying her as a legislative ally of the "
              "abortion industry from the outset of her public career.",
              ["https://en.wikipedia.org/wiki/Beth_Doglio",
               "https://ballotpedia.org/Beth_Doglio"]),
    ]),

    # ---- April Berg (WA-44, D, State Representative) ----
    ("april-berg", "WA", "Representative", [
        claim("ab1", "april-berg", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates for her 2020 election and "
              "subsequent races for Washington's 44th District House seat — placing her "
              "inside the abortion-industry political network the rubric targets with the "
              "question about legislators who 'never took PP/NARAL/EMILY money.'",
              ["https://ballotpedia.org/April_Berg",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements"]),
        claim("ab2", "april-berg", "self_defense", 1, False,
              "A member of the WA House Democratic majority caucus that passed Washington's "
              "HB 1240 on a strict 55-42 party-line vote (March 8, 2023), banning future "
              "sales of AR-15s, AK-47s, and semi-automatic rifles accepting detachable or "
              "fixed high-capacity magazines — the assault-weapons ban governor Jay Inslee "
              "signed April 25, 2023, making Washington the 10th state to prohibit such "
              "sales.",
              ["https://www.seattletimes.com/seattle-news/politics/wa-house-votes-to-ban-assault-weapons/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
    ]),

    # ---- Amy Walen (WA-48, D, State Representative) ----
    ("amy-walen", "WA", "Representative", [
        claim("aw1", "amy-walen", "self_defense", 1, False,
              "A sponsor of Washington's HB 1240 (passed April 25, 2023), the assault-weapons "
              "ban prohibiting future sales of AR-15s, AK-47s, and semi-automatic rifles "
              "that accept detachable magazines or have fixed magazines exceeding ten rounds "
              "— a direct government restriction on the firearms the rubric defends as an "
              "unrestricted constitutional right.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false",
               "https://en.wikipedia.org/wiki/Amy_Walen"]),
        claim("aw2", "amy-walen", "sanctity_of_life", 4, False,
              "Received Planned Parenthood Alliance Advocates' endorsement in the 2022 "
              "primary elections for Washington House District 48-Position 2 — placing "
              "her inside the abortion-industry political network the rubric's "
              "sanctity-of-life question specifically targets.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/press-releases/planned-parenthood-announces-first-round-of-2022-endorsements-in-wa",
               "https://ballotpedia.org/Amy_Walen"]),
    ]),

    # ---- Brianna Thomas (WA-34, D, State Representative) ----
    ("brianna-thomas", "WA", "Representative", [
        claim("bt1", "brianna-thomas", "self_defense", 1, False,
              "Voted YES on Washington's HB 1163 (passed House 58-38, signed into law "
              "May 20, 2025, effective May 1, 2027), the permit-to-purchase bill requiring "
              "all firearms buyers to obtain a state-issued permit and complete mandatory "
              "safety training before any purchase — a government-approval requirement "
              "directly opposing the rubric's defense of unrestricted firearms acquisition.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("bt2", "brianna-thomas", "biblical_marriage", 2, False,
              "As newly-appointed 34th District State Representative and Assistant Majority "
              "Whip (WA House Democrats, 2025), publicly committed to 'LGBTQ+ equality' as "
              "a core governing position — explicitly embracing the gender-identity and "
              "transgender policy agenda the rubric's biblical-marriage question on 'rejects "
              "transgender ideology' is designed to identify.",
              ["https://housedemocrats.wa.gov/thomas/",
               "https://en.wikipedia.org/wiki/Brianna_Thomas_(politician)"]),
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
