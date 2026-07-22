#!/usr/bin/env python3
"""Enrichment batch 818: 5 Utah Republican State Representatives (archetype_party_default → evidence_curated).

Targets from the remaining archetype_party_default UT pool (bottom of alphabet; batch 817
completed 5 UT Rs — this batch continues with the next 5 reverse-alphabetical Republicans):
Casey Snider (UT-05, House Majority Leader), Carl R. Albrecht (UT-70),
Calvin Roberts (UT-46), Bridger Bolinder (UT-29, HHS Committee Chair),
Ariel Defay (UT-15).
All are Utah House Republicans with 0 prior claims.
Research covers 2023-2026 legislative sessions with verifiable votes and sponsorships.
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
    # ---------- Casey Snider (UT-05, R, Cache County; House Majority Leader 2025) ----------
    ("casey-snider", "UT", "Representative", [
        claim("cs1", "casey-snider", "refuse_federal_overreach", 0, True,
              "Chief sponsor of HB 371 (2023 General Session) — Working Farm and Ranch Protection Fund — establishing a dedicated state fund to acquire conservation interests in Utah working farms and ranches threatened by conversion or federal regulatory pressure. Snider, a Cache County farmer and agricultural advocate, designed the fund to shield family agricultural operations from federal land-management and environmental mandates. Signed by Governor Cox on March 14, 2023.",
              ["https://le.utah.gov/~2023/bills/static/HB0371.html",
               "https://house.utleg.gov/firefighting-farming-and-public-service-meet-utahs-new-house-majority-leader-rep-casey-snider/"]),
        claim("cs2", "casey-snider", "self_defense", 0, True,
              "Voted YES on HB 219 (2023 General Session) — Federal Firearm Enforcement Limitation Act — establishing Utah as a Second Amendment Sanctuary state, prohibiting state and local agencies from spending public funds to assist federal gun regulations not mirrored in state law. Passed 60–3; signed into law. Snider has publicly identified himself as a defender of the Second Amendment and has been elected House Majority Leader by the Republican caucus.",
              ["https://www.stgeorgeutah.com/news/government-news/declaring-utah-a-2nd-amendment-sanctuary-state-among-these-gun-related-bills-moving-through-legislature/article_e1230bd4-74a1-5e38-bdc6-c739c72d5baf.html",
               "https://ballotpedia.org/Casey_Snider"]),
        claim("cs3", "casey-snider", "election_integrity", 0, True,
              "Voted YES on HB 300 (2025 General Session) — Amendments to Election Law — requiring voters to include the last four digits of a government-issued ID on mail-in ballot return envelopes, phasing out Utah's automatic vote-by-mail system by 2029 (voters must opt in), and mandating ballots be received by 8 p.m. on election night. Passed the House 56–15 mostly along party lines; signed by Governor Cox on March 26, 2025.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/",
               "https://le.utah.gov/~2025/bills/static/HB0300.html"]),
    ]),

    # ---------- Carl R. Albrecht (UT-70, R, Millard/Juab/Piute; serving since 2017) ----------
    ("carl-r-albrecht", "UT", "Representative", [
        claim("ca1", "carl-r-albrecht", "refuse_federal_overreach", 0, True,
              "Chief sponsor of HB 363 (2024 General Session) — Livestock Grazing Amendments — codifying in Utah law that a grazing allotment constitutes a legally recognized vested right, directly countering federal BLM and Forest Service attempts to reduce or revoke grazing permits. Albrecht represents heavily agricultural Millard, Juab, and Piute County districts and has made protecting ranching operations from federal land-management overreach a signature legislative priority.",
              ["https://le.utah.gov/~2024/bills/static/HB0363.html",
               "https://fastdemocracy.com/bill-search/ut/legislators/UTL000149/"]),
        claim("ca2", "carl-r-albrecht", "self_defense", 0, True,
              "Publicly stated: 'I am a strong proponent of the 2nd Amendment constitutional rights.' Votes consistently with the pro-gun majority in the Utah House on Second Amendment legislation.",
              ["https://sengov.com/states/utah/carl-albrecht/",
               "https://ballotpedia.org/Carl_R._Albrecht"],
              kind="statement"),
        claim("ca3", "carl-r-albrecht", "industry_capture", 3, True,
              "Chief sponsor of HB 047 (2025 General Session) — Public Lands Watering Rights Amendments — establishing that when the federal government reduces a rancher's Animal Unit Months (AUMs) on a grazing allotment, causing water to go unused, the federal government cannot then claim that water for other purposes (e.g., wildlife enhancement). The bill protects small ranchers and family grazing operations from federal double-taking of their water rights. Signed into law in 2025.",
              ["https://www.usu.edu/ilwa/resources/2025-legislative-updates/agriculture.php",
               "https://ironcountytoday.com/2025/02/28/representative-albrechts-sixth-week-of-session/"]),
    ]),

    # ---------- Calvin Roberts (UT-46, R, Draper; first term Jan 2025, finance background) ----------
    ("calvin-roberts", "UT", "Representative", [
        claim("cr1", "calvin-roberts", "election_integrity", 0, True,
              "Voted YES on HB 300 (2025 General Session) — Amendments to Election Law — requiring voters to include the last four digits of a government-issued ID on mail-in ballot return envelopes, phasing out Utah's automatic vote-by-mail system by 2029 (voters must opt in), and mandating ballots be received by 8 p.m. on election night. Passed the House 56–15 mostly along party lines; signed by Governor Cox on March 26, 2025.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/",
               "https://le.utah.gov/~2025/bills/static/HB0300.html"]),
        claim("cr2", "calvin-roberts", "biblical_marriage", 2, True,
              "Voted YES on HB 174 (2026 General Session) — Sex Characteristic Change Treatment Amendments — permanently banning puberty blockers and cross-sex hormones for transgender minors in Utah, converting the prior moratorium into a permanent prohibition. Passed the House 54–15 on Feb. 5, 2026; signed by Governor Cox on March 18, 2026.",
              ["https://utahnewsdispatch.com/2026/01/28/utah-bill-would-ban-transgender-care-for-minors/",
               "https://utahnewsdispatch.com/2026/02/05/utah-house-passes-ban-transgender-treatments-for-minors/"]),
        claim("cr3", "calvin-roberts", "refuse_federal_overreach", 0, True,
              "Ran for Utah House District 46 on an explicit platform of local control and land use autonomy, arguing that communities — not the state or federal government — should direct zoning and development decisions. A former Wall Street finance professional (Credit Suisse; Moelis & Company) and Draper City Council member 2020–2024, Roberts won the Republican primary by defeating the incumbent in the convention, running on fiscal restraint and rolling back federal influence over local development.",
              ["https://www.votecalroberts.com/",
               "https://ballotpedia.org/Cal_Roberts"],
              kind="statement"),
    ]),

    # ---------- Bridger Bolinder (UT-29, R, Ogden-area; HHS Committee Chair; not seeking re-election 2026) ----------
    ("bridger-bolinder", "UT", "Representative", [
        claim("bb1", "bridger-bolinder", "election_integrity", 0, True,
              "Voted YES on HB 300 (2025 General Session) — Amendments to Election Law — requiring voters to include the last four digits of a government-issued ID on mail-in ballot return envelopes, phasing out Utah's automatic vote-by-mail system by 2029 (voters must opt in), and mandating ballots be received by 8 p.m. on election night. Passed the House 56–15 mostly along party lines; signed by Governor Cox on March 26, 2025.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/",
               "https://le.utah.gov/~2025/bills/static/HB0300.html"]),
        claim("bb2", "bridger-bolinder", "biblical_marriage", 2, True,
              "Voted YES on HB 174 (2026 General Session) — Sex Characteristic Change Treatment Amendments — permanently banning puberty blockers and cross-sex hormones for transgender minors in Utah, converting the prior moratorium into a permanent prohibition. As Chair of the House Health and Human Services Committee, Bolinder was directly involved in advancing health-related protective legislation. Passed the House 54–15; signed by Governor Cox on March 18, 2026.",
              ["https://utahnewsdispatch.com/2026/01/28/utah-bill-would-ban-transgender-care-for-minors/",
               "https://ballotpedia.org/Bridger_Bolinder"]),
        claim("bb3", "bridger-bolinder", "refuse_federal_overreach", 0, True,
              "Publicly committed to the Constitution, limited government, and maintaining local control over state and federal bureaucratic mandates. Serves as Assistant Majority Whip (2025) and Chair of the House Health and Human Services Committee, consistently voting with the Utah House Republican caucus to resist federal regulatory overreach in health, land, and economic policy.",
              ["https://www.votebolinder.com/home",
               "https://ballotpedia.org/Bridger_Bolinder"],
              kind="statement"),
    ]),

    # ---------- Ariel Defay (UT-15, R, Kaysville; Education Committee; appointed Nov 2023, re-elected 2024) ----------
    ("ariel-defay", "UT", "Representative", [
        claim("ad1", "ariel-defay", "family_child_sovereignty", 0, True,
              "House floor sponsor of SB 76 (2025 General Session) — Minor Marriage Restrictions — banning minors from marrying a person four or more years their senior and requiring a 72-hour cooling-off period between marriage application and court-issued permission, specifically to protect minors from coercive and exploitative arrangements. Defay stated: 'I think four years is a reasonable measure. Really, we're talking about a 17 year old.' Approved by the Utah Legislature and signed into law in 2025.",
              ["https://utahnewsdispatch.com/briefs/utah-legislature-approves-bill-forbidding-minors-from-marrying-someone-four-years-older/",
               "https://le.utah.gov/~2025/bills/static/SB0076.html"]),
        claim("ad2", "ariel-defay", "public_justice", 0, True,
              "Primary sponsor of HB 137 (2025 General Session) — Human Trafficking Expungement Amendments — modifying Utah's expungement statutes to make it easier for survivors of human trafficking to clear criminal records incurred as a direct result of being trafficked. The bill reflects a conviction that the justice system should protect and restore victims rather than perpetuate their exploitation.",
              ["https://le.utah.gov/~2025/bills/static/HB0137.html",
               "https://legiscan.com/UT/people/ariel-defay/id/24964"]),
        claim("ad3", "ariel-defay", "election_integrity", 0, True,
              "Voted YES on HB 300 (2025 General Session) — Amendments to Election Law — requiring voters to include the last four digits of a government-issued ID on mail-in ballot return envelopes, phasing out Utah's automatic vote-by-mail system by 2029 (voters must opt in), and mandating ballots be received by 8 p.m. on election night. Passed the House 56–15 mostly along party lines; signed by Governor Cox on March 26, 2025.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/",
               "https://le.utah.gov/~2025/bills/static/HB0300.html"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
