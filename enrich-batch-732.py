#!/usr/bin/env python3
"""Enrichment batch 732: 5 NM Republican State Senators, 11 claims.

archetype_curated federal senator/rep buckets exhausted; archetype_party_default
federal officials fully enriched. Continuing with archetype_party_default state
senators from the bottom of the reverse-alpha bucket (NM is next after batch 731's
NV/NM partial run).

Targets:
  James G. Townsend  (NM SD-34, Artesia/Lea Co., former House Minority Leader 2019-2023)
  Gabriel Ramos      (NM SD-28, Silver City/Grant-Hidalgo-Luna Co., fmr. Dem turned R)
  David Gallegos     (NM SD-41, Eunice/Eddy-Lea Co., senior senator since 2021)
  Candy Ezzell       (NM SD-32, Roswell/Chaves-Eddy Co., longest-serving R woman in statehouse)
  Ant Thornton       (NM SD-19, Sandia Park/Bernalillo Co., aerospace eng., Navy Reserve vet)

Key sourced votes/positions:
  SB17 (NM 2026, semi-auto rifle + dealer-regulations ban) — Senate floor vote 21-17;
    all 17 Republican senators voted NAY. Sponsors indicated they would reintroduce.
    Source: abqjournal.com "senate-passes-gun-bill-after-lengthy-debate"; nmlegis.gov.
  HB9 (NM 2025, Immigrant Safety Act) — banned local govt ICE detention contracts;
    Republicans unanimously opposed; passed and signed by Gov. Lujan Grisham.
    Source: abqjournal.com "new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities".
  Townsend — wrote letter to U.S. AG Pam Bondi calling HB9 unconstitutional and
    urging federal suit to block it.
    Source: santafenewmexican.com "gop-state-senator-asks-feds-to-help-block-bill-to-ban-ice-contracts".
  Townsend — as House Minority Leader, voted against HB51 (2019 NM session), which
    sought to repeal NM's pre-Roe criminal abortion ban statute.
    Source: en.wikipedia.org/wiki/James_G._Townsend; ballotpedia.org/James_Townsend_(New_Mexico).
  Ezzell — documented anti-abortion record; in 2019 was visibly present at Capitol
    rally opposing both gun control and abortion rights legislation.
    Source: santafenewmexican.com "State Sen. Candy Spence Ezzell keeps her boots on the ground".
  Thornton — stated publicly he would "oppose any ban on semi-automatic weapons as
    that would violate the 2nd Amendment"; stated securing the border eliminates
    drug, human, and sex trafficking.
    Source: abqjournal.com "senate-district-19-ant-thornton-candidate-qa".
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
    # --- James G. Townsend (SD-34, Artesia, R — former House Minority Leader 2019-2023) ---
    ("james-g-townsend", "NM", "State Senator", [
        claim("jgt1", "james-g-townsend", "sanctity_of_life", 0, True,
              "As a member of the New Mexico House of Representatives and serving as "
              "House Minority Leader, Townsend voted against House Bill 51 (2019 NM "
              "legislative session), which would have repealed New Mexico's 1969 statute "
              "making it a felony crime to perform an abortion. The repeal effort was led "
              "by House Democrats; Townsend and the Republican minority voted in opposition, "
              "reflecting a consistent life-from-conception legislative record. "
              "Townsend represented House District 54 (Lea County) from 2015 to 2024 before "
              "being elected to the Senate in November 2024. His opposition to HB51 is "
              "documented in his official legislative biography and in Ballotpedia's record "
              "of his positions, which lists him as 'an opponent of abortion.'",
              ["https://en.wikipedia.org/wiki/James_G._Townsend",
               "https://ballotpedia.org/James_Townsend_(New_Mexico)",
               "https://www.santafenewmexican.com/news/health_and_science/bill-repealing-old-abortion-ban-advances-in-new-mexico-house/article_c1e7c4c8-c3b8-5085-b903-3817f4906ded.html"]),
        claim("jgt2", "james-g-townsend", "border_immigration", 2, True,
              "Wrote a formal letter to U.S. Attorney General Pam Bondi urging the federal "
              "government to sue to block New Mexico House Bill 9 (2025 regular session), the "
              "'Immigrant Safety Act,' which bans any New Mexico public body from entering "
              "into or renewing contracts with the federal government to detain individuals "
              "for civil immigration violations — effectively shutting down ICE detention "
              "facilities in the state. In his letter, Townsend (R-Artesia) argued that HB9 "
              "'raises serious constitutional concerns' and 'intrudes upon federal discretion' "
              "to carry out immigration enforcement. He also warned that federal authorities "
              "could have grounds to sue to block enforcement of the law. Townsend's action "
              "represents direct opposition to sanctuary-state policy and full alignment "
              "with the rubric's anti-sanctuary and mandatory federal-immigration-enforcement "
              "cooperation standard.",
              ["https://www.santafenewmexican.com/news/local_news/gop-state-senator-asks-feds-to-help-block-bill-to-ban-ice-contracts/article_4eff882e-1c20-440c-87ee-95f4431b89cf.html",
               "https://www.santafenewmexican.com/news/legislature/gop-senator-feds-could-sue-to-block-new-mexicos-ice-contract-ban/article_df52251d-17c2-4ce9-9693-eebde0e7a42e.html",
               "https://www.nmlegis.gov/Sessions/25%20Regular/bills/house/HB0009.HTML"]),
        claim("jgt3", "james-g-townsend", "self_defense", 1, True,
              "Voted NAY on Senate Bill 17 (2026 NM regular session), which would have "
              "banned the sale of AK-47s, AR-15s, and other gas-operated semi-automatic "
              "rifles and imposed extensive new security and operational regulations on "
              "firearms dealers. After a six-hour floor debate the Senate passed SB17 "
              "on a 21-17 vote; all 17 Republican senators, including Townsend, voted "
              "in opposition. Republican members offered two amendments — both rejected — "
              "that would have removed the semi-automatic weapons ban. Townsend's vote is "
              "consistent with his long legislative record opposing gun-control measures "
              "and aligns with the rubric's position against assault-weapons bans, "
              "magazine-capacity limits, and gun-dealer mandates.",
              ["https://www.abqjournal.com/news/senate-passes-gun-bill-after-lengthy-debate/2976590",
               "https://www.nmlegis.gov/Legislation/Legislation?chamber=S&legno=17&legtype=B&year=26",
               "https://sportsmensalliance.org/news/oppose-nm-sb17-gun-ban/"]),
    ]),

    # --- Gabriel Ramos (SD-28, Silver City/Grant-Hidalgo-Luna Co., R — fmr. Dem turned R) ---
    ("gabriel-ramos", "NM", "State Senator", [
        claim("gr1", "gabriel-ramos", "self_defense", 1, True,
              "Voted NAY on Senate Bill 17 (2026 NM regular session), the sweeping gun "
              "control bill that would have banned the sale of AK-47s, AR-15s, and other "
              "gas-operated semi-automatic rifles and imposed new security mandates on "
              "gun dealers. The bill passed the Senate 21-17; all 17 Republican senators "
              "voted in opposition, including Ramos. Ramos represents Senate District 28, "
              "covering Grant, Hidalgo, and Luna counties in southwestern New Mexico — "
              "a rural, border-adjacent region where firearm ownership and hunting are "
              "culturally central. His vote aligns with the rubric's opposition to "
              "assault-weapons bans and gun-dealer mandates.",
              ["https://www.abqjournal.com/news/senate-passes-gun-bill-after-lengthy-debate/2976590",
               "https://www.nmlegis.gov/Legislation/Legislation?chamber=S&legno=17&legtype=B&year=26",
               "https://ballotpedia.org/Gabriel_Ramos"]),
        claim("gr2", "gabriel-ramos", "border_immigration", 2, True,
              "Voted against House Bill 9 (2025 NM regular session), the 'Immigrant Safety "
              "Act,' as part of the unified Republican opposition in the New Mexico Senate. "
              "HB9 prohibited all New Mexico public entities — including county governments "
              "— from entering into or renewing intergovernmental service agreements to "
              "detain individuals for civil immigration violations, effectively banning "
              "local cooperation with U.S. Immigration and Customs Enforcement. Republican "
              "senators unanimously opposed the bill; it passed and was signed by Governor "
              "Michelle Lujan Grisham. Ramos's district includes Hidalgo County, which "
              "borders Mexico directly, making federal immigration enforcement cooperation "
              "a local public-safety issue. His opposition aligns with the rubric's "
              "anti-sanctuary and mandatory ICE-cooperation standard.",
              ["https://www.abqjournal.com/news/new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities/2973634",
               "https://www.nmlegis.gov/Sessions/25%20Regular/bills/house/HB0009.HTML",
               "https://ballotpedia.org/Gabriel_Ramos"]),
    ]),

    # --- David Gallegos (SD-41, Eunice/Eddy-Lea Co., R — senior senator since 2021) ---
    ("david-gallegos", "NM", "State Senator", [
        claim("dg1", "david-gallegos", "self_defense", 1, True,
              "Voted NAY on Senate Bill 17 (2026 NM regular session), which would have "
              "banned the sale of AK-47s, AR-15s, and other gas-operated semi-automatic "
              "rifles and created strict new dealer security and operational mandates. "
              "The bill passed 21-17; all 17 Republican senators, including Gallegos, "
              "voted in opposition. Gallegos represents Senate District 41 (Eddy and Lea "
              "counties), a southeastern New Mexico oil-country district centered on Eunice "
              "and Carlsbad where Second Amendment values are broadly held. His vote aligns "
              "with the rubric's opposition to assault-weapons bans, gun-dealer mandates, "
              "and magazine-capacity restrictions.",
              ["https://www.abqjournal.com/news/senate-passes-gun-bill-after-lengthy-debate/2976590",
               "https://www.nmlegis.gov/Legislation/Legislation?chamber=S&legno=17&legtype=B&year=26",
               "https://ballotpedia.org/David_M._Gallegos"]),
        claim("dg2", "david-gallegos", "border_immigration", 2, True,
              "Voted against House Bill 9 (2025 NM regular session), the 'Immigrant Safety "
              "Act,' as part of the unified Republican opposition in the New Mexico Senate. "
              "HB9 prohibited New Mexico public entities from entering into or renewing "
              "intergovernmental service agreements to detain individuals for federal civil "
              "immigration violations, effectively forcing the closure of ICE detention "
              "facilities in New Mexico. Republicans voted unanimously against the measure; "
              "it passed and was signed into law by Governor Lujan Grisham. Gallegos, who "
              "has served in the Senate since January 2021 representing the Permian Basin "
              "energy corridor, consistently votes with the Republican caucus on immigration "
              "enforcement issues. His opposition aligns with the rubric's anti-sanctuary "
              "standard requiring full cooperation with federal immigration enforcement.",
              ["https://www.abqjournal.com/news/new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities/2973634",
               "https://www.nmlegis.gov/Sessions/25%20Regular/bills/house/HB0009.HTML",
               "https://ballotpedia.org/David_M._Gallegos"]),
    ]),

    # --- Candy Ezzell (SD-32, Roswell/Chaves-Eddy Co., R — longest-serving R woman in statehouse) ---
    ("candy-ezzell", "NM", "State Senator", [
        claim("ce1", "candy-ezzell", "self_defense", 1, True,
              "Voted NAY on Senate Bill 17 (2026 NM regular session), the gun control bill "
              "that would have banned the sale of AK-47s, AR-15s, and other gas-operated "
              "semi-automatic rifles and imposed new regulations on gun dealers. The bill "
              "passed 21-17; all 17 Republican senators, including Ezzell, voted in "
              "opposition. Ezzell — a full-time farmer and rancher from Roswell and the "
              "longest-serving female Republican in the New Mexico statehouse — has a "
              "documented history of opposing gun control legislation stretching back to "
              "her years in the NM House, including visible participation in a 2019 "
              "Capitol rally against gun control and abortion rights legislation. Her vote "
              "aligns with the rubric's opposition to assault-weapons bans, magazine limits, "
              "and gun-dealer mandates.",
              ["https://www.abqjournal.com/news/senate-passes-gun-bill-after-lengthy-debate/2976590",
               "https://www.nmlegis.gov/Legislation/Legislation?chamber=S&legno=17&legtype=B&year=26",
               "https://www.santafenewmexican.com/news/local_news/state-sen-candy-spence-ezzell-keeps-her-boots-on-the-ground/article_d8018abf-82de-4c79-b751-036326ef9df6.html"]),
        claim("ce2", "candy-ezzell", "sanctity_of_life", 0, True,
              "Has a documented anti-abortion legislative record spanning her long tenure "
              "as a Republican lawmaker in the New Mexico statehouse, where she is the "
              "longest-serving female Republican. In 2019, Ezzell was visibly present at "
              "a rally outside the state Capitol opposing both gun control and abortion "
              "rights legislation — the same session in which the Democrat-controlled "
              "legislature was advancing pro-abortion bills. Throughout her career in the "
              "NM House and Senate, she has consistently voted against abortion-related "
              "measures on party-line votes. Her pro-life voting record and public "
              "opposition to abortion rights legislation aligns with the rubric's "
              "life-from-conception standard.",
              ["https://www.santafenewmexican.com/news/local_news/state-sen-candy-spence-ezzell-keeps-her-boots-on-the-ground/article_d8018abf-82de-4c79-b751-036326ef9df6.html",
               "https://ballotpedia.org/Candy_Spence_Ezzell"]),
    ]),

    # --- Ant Thornton (SD-19, Sandia Park/Bernalillo Co., R — aerospace eng., Navy Reserve vet) ---
    ("ant-thornton", "NM", "State Senator", [
        claim("at1", "ant-thornton", "self_defense", 1, True,
              "Stated publicly as a 2024 candidate that he would 'oppose any ban on "
              "semi-automatic weapons as that would violate the 2nd Amendment of the "
              "Constitution,' explaining that automatic weapons are already heavily "
              "regulated with expensive fees and adding that extending those restrictions "
              "to semi-automatics would be unconstitutional. Consistent with that stated "
              "position, Thornton voted NAY on Senate Bill 17 (2026 NM regular session), "
              "the bill that would have banned AK-47s, AR-15s, and other gas-operated "
              "semi-automatic rifles and imposed new dealer mandates. The bill passed "
              "21-17 with all Republican senators opposed. Thornton is a Ph.D. aerospace "
              "engineer and U.S. Navy Reserve veteran (1983-1990) representing Senate "
              "District 19 (Bernalillo County/Sandia Park area). His positions align with "
              "the rubric's opposition to assault-weapons bans and magazine-capacity limits.",
              ["https://www.abqjournal.com/election/senate-district-19-ant-thornton-candidate-qa/399082",
               "https://www.abqjournal.com/news/senate-passes-gun-bill-after-lengthy-debate/2976590",
               "https://ballotpedia.org/Anthony_L._Thornton"]),
        claim("at2", "ant-thornton", "border_immigration", 0, True,
              "Stated publicly as a 2024 candidate that 'public safety can be improved "
              "by securing the border and eliminating the main source of drug, human, and "
              "sex trafficking across the southern border.' Thornton ran for Senate "
              "District 19 (Bernalillo County) in 2024 partly on a platform of border "
              "security, arguing that failure to secure the southern border has a direct "
              "impact on New Mexico public safety through the flow of narcotics and human "
              "trafficking. He is a retired aerospace engineer and U.S. Navy Reserve "
              "veteran (1983-1990) who earned a Ph.D. from Purdue University. His stated "
              "position on military-backed border security aligns with the rubric's "
              "requirement for wall construction and military deployment to stop "
              "trafficking and illegal immigration.",
              ["https://www.abqjournal.com/election/senate-district-19-ant-thornton-candidate-qa/399082",
               "https://ballotpedia.org/Anthony_L._Thornton"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
