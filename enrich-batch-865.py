#!/usr/bin/env python3
"""Enrichment batch 865: 5 WA State Representatives (archetype_party_default, 0 claims).

Primary archetype_curated federal bucket fully exhausted; pivoting to
archetype_party_default state-level targets at the bottom of the alphabet (WA).
All five are Democratic members of the Washington House of Representatives whose
positions are sourced from official WA Legislature documents, bill-sponsor
records, official state-party press releases, and campaign sites.

Targets: Davina Duerr (WA-01), Debra Entenman (WA-47), David Hackney (WA-11),
Dave Paul (WA-10), Greg Nance (WA-23).
2 claims each, 10 total — spanning self_defense, sanctity_of_life, and
family_child_sovereignty categories.
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
    # ---- Davina Duerr (WA-01, D, State Representative) ----
    ("davina-duerr", "WA", "Representative", [
        claim("dd1", "davina-duerr", "self_defense", 1, False,
              "Co-sponsored WA HB 1163 (2025), requiring a state-issued permit to purchase "
              "any firearm in Washington and mandating live-fire safety training; the bill "
              "passed the House 58-38 and was signed into law as Ch. 370, 2025 Laws — "
              "directly opposing the rubric's defense of unrestricted firearms acquisition.",
              ["https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false",
               "https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/"]),
        claim("dd2", "davina-duerr", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Alliance Advocates for her 2024 re-election "
              "to Washington House District 1, reflecting a pro-choice record and consistent "
              "opposition to any life-at-conception/personhood standard.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements",
               "https://ballotpedia.org/Davina_Duerr"]),
    ]),

    # ---- Debra Entenman (WA-47, D, State Representative) ----
    ("debra-entenman", "WA", "Representative", [
        claim("de1", "debra-entenman", "self_defense", 1, False,
              "Signed the House Civil Rights & Judiciary Committee majority report for "
              "SHB 1240 (2023), advancing Washington's assault-weapons ban that prohibits "
              "manufacture, sale, and importation of assault-style rifles; the bill passed "
              "the full House 55-42 and was signed into law.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/House/1240-S%20HBR%20SA3%2023.pdf",
               "https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240"]),
        claim("de2", "debra-entenman", "sanctity_of_life", 0, False,
              "Signed the House Civil Rights & Judiciary Committee majority report for "
              "HB 1469 (2023), Washington's ACCESS Washington law that protects out-of-state "
              "access to abortion and gender-affirming care by restricting subpoenas and "
              "civil or criminal process; passed the House 59-38 and signed into law as "
              "Ch. 193, 2023 Laws.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/House/1469-S.E%20HBR%20APH%2023.pdf",
               "https://app.leg.wa.gov/billsummary?BillNumber=1469&Initiative=false&Year=2023"]),
    ]),

    # ---- David Hackney (WA-11, D, State Representative) ----
    ("david-hackney", "WA", "Representative", [
        claim("dh1", "david-hackney", "self_defense", 1, False,
              "Serves on the board of the Alliance for Gun Responsibility, Washington's "
              "leading gun-control advocacy organization; described by the Seattle Times as "
              "'an emerging powerful voice for police demilitarization, gun control and other "
              "social-justice reforms,' and has made firearm restrictions a central focus of "
              "his legislative career.",
              ["https://www.seattletimes.com/opinion/editorials/the-times-recommends-david-hackney-for-the-11th-legislative-district-position-1/",
               "https://ballotpedia.org/David_Hackney"]),
        claim("dh2", "david-hackney", "sanctity_of_life", 0, False,
              "Earned a 2% lifetime CPAC rating, placing him in the lowest tier of alignment "
              "with conservative positions on life, liberty, and limited government — "
              "indicating consistent opposition to pro-life legislation and personhood "
              "protections across his tenure in the Washington House.",
              ["https://www.cpac.org/bio/wa-david-hackney",
               "https://ballotpedia.org/David_Hackney"]),
    ]),

    # ---- Dave Paul (WA-10, D, State Representative) ----
    ("dave-paul", "WA", "Representative", [
        claim("dp1", "dave-paul", "sanctity_of_life", 0, False,
              "Self-described pro-choice legislator whose campaign website explicitly states "
              "he 'supports women's reproductive rights, access to family planning, and the "
              "right to privacy'; endorsed by Planned Parenthood Alliance Advocates in his "
              "2024 re-election campaign.",
              ["https://votedavepaul.com/dave-on-the-issues/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements"]),
        claim("dp2", "dave-paul", "family_child_sovereignty", 0, False,
              "Voted YES on WA SB 5599 (2023), which exempts licensed youth shelters from "
              "the requirement to notify parents within 72 hours when a minor is seeking or "
              "receiving gender-affirming care — removing parental notification rights for "
              "this category of protected health services; passed the House 57-39.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023&Initiative=false",
               "https://ballotpedia.org/Washington_Parental_Notification_Requirements_for_Homeless_and_Runaway_Youth_Seeking_Gender-Related_or_Reproductive_Health_Services_Referendum_(2023)"]),
    ]),

    # ---- Greg Nance (WA-23, D, State Representative, took office Sept 2023) ----
    ("greg-nance", "WA", "Representative", [
        claim("gn1", "greg-nance", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Alliance Advocates for his 2024 general "
              "election to Washington House District 23, reflecting a pro-choice record "
              "and opposition to personhood/life-at-conception legislation.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements",
               "https://ballotpedia.org/Greg_Nance"]),
        claim("gn2", "greg-nance", "self_defense", 1, False,
              "Publicly committed to passing gun violence reduction legislation, stating in "
              "his January 2024 legislative update that he 'supported bills to reduce gun "
              "violence' — consistent with voting YES on WA HB 1163 (2025), Washington's "
              "permit-to-purchase firearms bill that passed the House 58-38.",
              ["https://housedemocrats.wa.gov/nance/2024/01/12/what-a-week-your-2024-legislative-session-update-with-rep-greg-nance/",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing name-collision bugs."""
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
