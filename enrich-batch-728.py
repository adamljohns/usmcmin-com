#!/usr/bin/env python3
"""Enrichment batch 728: 5 New Mexico Republican State Senators with 0 claims.

Continuing the NM state-senator pivot from batch 727. Targets the next 5 from
the reverse-alpha bucket: Rex Wilson (SD-33), Pat Boone (SD-27), Nicole Tobiassen
(SD-21), Larry R. Scott (SD-42), Joshua A. Sanchez (SD-29).

Key sourced votes/positions:
  SB 57 (2025) — shielded abortion-provider records at public institutions from
    IPRA requests; passed 26-16 on strict party line, all 16 Republicans NO.
    (Boone, Tobiassen, L. Scott, Sanchez all in office; Wilson was not yet seated.)
  SB 17 (2026) — "Stop the Illegal Gun Trade and Extremely Dangerous Weapons Act";
    banned gas-operated semi-auto rifles and 10-round+ magazines; passed 21-17
    with all Republicans present voting NO. All 5 targets confirmed by the NM
    Senate GOP press release and NRA-ILA reporting.
  HB 9 (2026) — "Immigrant Safety Act"; banned NM public bodies from contracting
    with ICE for detention facilities; passed 24-15 with all 15 Republicans voting
    NO. Three border-adjacent Democrats joined them. (Wilson, Boone, L. Scott targets.)
  HB 7 (2023) — "Reproductive & Gender-Affirming Health Care Act"; passed NM Senate
    23-15 with all 15 Republicans voting NO, including Sanchez (in Senate since 2021).
  Tobiassen Public Safety Day (Dec 2025) — Organized statewide law enforcement
    coalition for 2026 session; called for bail reform, felony firearm penalties,
    juvenile code reform.
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
    # ------- Rex Wilson (SD-33, Lincoln/Chaves/Otero, appointed Jan 8 2026 by MLG) -------
    ("rex-wilson", "NM", "State Senator", [
        claim("rw1", "rex-wilson", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), the 'Stop the Illegal Gun Trade and Extremely "
              "Dangerous Weapons Act,' which banned the sale of gas-operated semi-automatic "
              "rifles and magazines holding more than 10 rounds. Wilson, appointed to SD-33 "
              "on January 8, 2026, was present for the entire 30-day session and joined "
              "every Republican colleague in opposing the bill on the Senate floor. The "
              "Senate passed SB 17 by a 21-17 vote, with all Republicans present voting NO "
              "— a result the NM Senate GOP formally condemned as a 'radical gun control "
              "measure' and an unconstitutional infringement on Second Amendment rights.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://www.abqjournal.com/news/governor-appoints-former-lincoln-county-commissioner-rex-wilson-to-vacant-state-senate-seat/2956766"]),
        claim("rw2", "rex-wilson", "border_immigration", 2, True,
              "As a New Mexico state senator representing a rural district spanning parts of "
              "Lincoln, Chaves, and Otero counties — including areas near the New Mexico–Texas "
              "border corridor — Wilson voted NO on HB 9 (2026), the 'Immigrant Safety Act,' "
              "which prohibited NM public bodies from entering ICE detention contracts and "
              "blocked law enforcement from serving federal immigration warrants at local "
              "jails. The bill passed 24-15 with all 15 Republicans voting NO. Republicans "
              "argued the sanctuary-style restrictions would harm border-region economies "
              "and obstruct enforcement cooperation with federal immigration authorities.",
              ["https://www.abqjournal.com/news/new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities/2973634",
               "https://sourcenm.com/briefs/new-mexico-immigrant-safety-act-heads-to-governor/"]),
    ]),

    # ------- Pat Boone (SD-27, Chaves/Curry/De Baca/Lea/Roosevelt, rancher, since Jan 2025) -------
    ("pat-boone", "NM", "State Senator", [
        claim("pb1", "pat-boone", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), a Democrat-sponsored bill that would exempt the "
              "personal records of abortion providers at state-funded public institutions "
              "from New Mexico's Inspection of Public Records Act. The bill passed on a "
              "strict party-line vote of 26-16, with all 16 Republican senators — including "
              "first-term Sen. Boone — voting to preserve public accountability for abortion "
              "practices at state institutions rather than grant providers special legal "
              "secrecy.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://fastdemocracy.com/bill-search/nm/2025/bills/NMB00010994/",
               "https://ballotpedia.org/Patrick_Boone_IV"]),
        claim("pb2", "pat-boone", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), the sweeping 'Stop the Illegal Gun Trade and "
              "Extremely Dangerous Weapons Act,' which would have banned the sale of "
              "gas-operated semi-automatic rifles and magazines holding more than 10 rounds "
              "in New Mexico. Boone joined the unanimous Republican bloc in opposing the "
              "21-17 Senate floor vote. His rural district — covering the ranching and "
              "agricultural counties of Chaves, Curry, De Baca, Lea, and Roosevelt — has "
              "a strong culture of firearm ownership and self-reliance that makes "
              "Second Amendment protections a core constituent priority.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://ballotpedia.org/Patrick_Boone_IV"]),
        claim("pb3", "pat-boone", "border_immigration", 2, True,
              "Voted NO on HB 9 (2026), New Mexico's 'Immigrant Safety Act,' which banned "
              "public bodies statewide from entering contracts with ICE for immigration "
              "detention facilities and blocked local law enforcement from serving federal "
              "immigration warrants at county jails. The bill passed 24-15 with all 15 "
              "Republican senators voting NO. Boone's southeastern New Mexico district — "
              "including counties in the broader border-region corridor — is directly "
              "impacted by cross-border drug and human trafficking flows, making "
              "anti-sanctuary measures a priority for his constituents.",
              ["https://www.abqjournal.com/news/new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities/2973634",
               "https://sourcenm.com/briefs/new-mexico-immigrant-safety-act-heads-to-governor/"]),
    ]),

    # ------- Nicole Tobiassen (SD-21, Albuquerque area, first term since Jan 2025) -------
    ("nicole-tobiassen", "NM", "State Senator", [
        claim("nt1", "nicole-tobiassen", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), which would have shielded the personal records "
              "of abortion providers at New Mexico public institutions from the state's "
              "Inspection of Public Records Act. The bill passed 26-16 on a strict party-"
              "line vote, with all 16 Republican senators — including Tobiassen in her "
              "first term — rejecting special legal protections for abortion practices at "
              "state-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://fastdemocracy.com/bill-search/nm/2025/bills/NMB00010994/",
               "https://ballotpedia.org/Nicole_Tobiassen"]),
        claim("nt2", "nicole-tobiassen", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), New Mexico's sweeping 'assault weapon' ban that "
              "prohibited gas-operated semi-automatic rifles and magazines holding more than "
              "10 rounds. Tobiassen joined the unanimous Republican caucus in opposing the "
              "21-17 Senate floor vote. As a member of the Republican public safety task "
              "force that advocated for stiffer penalties for felons in possession of "
              "firearms, she has consistently distinguished between lawful gun owners — "
              "who she supports — and violent criminals, whose access to firearms she seeks "
              "to curtail through existing enforcement rather than civilian bans.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://www.santafenewmexican.com/news/local_news/we-lock-up-our-deodorant-but-not-our-criminals-state-sen-nicole-tobiassen-speaks-on/article_3375a17d-37c3-44b4-b4a4-0bcba0342714.html"]),
        claim("nt3", "nicole-tobiassen", "public_justice", 0, True,
              "In December 2025, organized a statewide 'Public Safety Day' coordinating "
              "every law enforcement entity in New Mexico — including federal agencies — "
              "to advocate at the 2026 Regular Legislative Session in Santa Fe, alongside "
              "victim advocacy groups and business owners. As a member of the Republican "
              "public safety task force, she championed bail reform to keep violent "
              "offenders detained, increased penalties for felons possessing firearms, "
              "and juvenile code reform — stating 'Public safety is not a partisan issue — "
              "it is a fundamental responsibility of government.' She also quipped about "
              "broken enforcement priorities: 'We lock up our deodorant but not our "
              "criminals.'",
              ["https://nmsenategop.com/2025/12/02/senator-nicole-tobiassen-calls-law-enforcement-across-nm-to-advocate-for-public-safety-ahead-of-2026-legislative-session/",
               "https://www.santafenewmexican.com/news/local_news/we-lock-up-our-deodorant-but-not-our-criminals-state-sen-nicole-tobiassen-speaks-on/article_3375a17d-37c3-44b4-b4a4-0bcba0342714.html"],
              kind="position"),
    ]),

    # ------- Larry R. Scott (SD-42, R, NM House 2015-2024; Senate since Jan 2025) -------
    ("larry-r-scott", "NM", "State Senator", [
        claim("ls1", "larry-r-scott", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), which would have exempted abortion provider "
              "identity records at state-funded public institutions from New Mexico's "
              "Inspection of Public Records Act. The bill passed on a strict party-line "
              "vote of 26-16, with all 16 Republicans — including Scott in his first "
              "Senate term after nine years in the House — voting against granting special "
              "secrecy protections for abortion practices at taxpayer-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://fastdemocracy.com/bill-search/nm/2025/bills/NMB00010994/",
               "https://ballotpedia.org/Larry_Scott"]),
        claim("ls2", "larry-r-scott", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), the 'Stop the Illegal Gun Trade and Extremely "
              "Dangerous Weapons Act,' which banned gas-operated semi-automatic rifles "
              "and magazines holding more than 10 rounds in New Mexico. Scott, a nine-year "
              "veteran of the NM House before moving to the Senate in 2025, joined the "
              "unanimous Republican caucus in opposing the 21-17 Senate floor vote. The "
              "NM Senate GOP condemned SB 17 as a 'radical gun control measure' that "
              "infringes constitutionally protected Second Amendment rights.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://ballotpedia.org/Larry_Scott"]),
        claim("ls3", "larry-r-scott", "border_immigration", 2, True,
              "Voted NO on HB 9 (2026), the 'Immigrant Safety Act,' which prohibited New "
              "Mexico public bodies from contracting with ICE for immigration detention "
              "facilities and barred local law enforcement from serving federal immigration "
              "warrants at county jails. The bill passed 24-15 with all 15 Republican "
              "senators voting NO. Republicans argued the anti-enforcement bill would "
              "undermine border security and harm rural counties — including Torrance and "
              "Otero, which host detention facilities — by cutting off detention-related "
              "economic activity and blocking cooperation with federal immigration "
              "authorities.",
              ["https://www.abqjournal.com/news/new-mexico-senate-passes-bill-seeking-to-close-immigration-detention-facilities/2973634",
               "https://sourcenm.com/briefs/new-mexico-immigrant-safety-act-heads-to-governor/"]),
    ]),

    # ------- Joshua A. Sanchez (SD-29, R, rancher/contractor, in Senate since 2021) -------
    ("joshua-a-sanchez", "NM", "State Senator", [
        claim("jas1", "joshua-a-sanchez", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), a Democrat-sponsored bill that would have shielded "
              "the personal records of abortion providers at state-funded public institutions "
              "from New Mexico's Inspection of Public Records Act. The bill passed on a "
              "strict party-line 26-16 vote, with all 16 Republican senators — including "
              "Sanchez, who has served in the NM Senate since 2021 — opposing special "
              "secrecy protections for abortion practices at taxpayer-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://fastdemocracy.com/bill-search/nm/2025/bills/NMB00010994/",
               "https://ballotpedia.org/Joshua_A._Sanchez"]),
        claim("jas2", "joshua-a-sanchez", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), the 'Stop the Illegal Gun Trade and Extremely "
              "Dangerous Weapons Act,' which banned gas-operated semi-automatic rifles "
              "and magazines holding more than 10 rounds in New Mexico. Sanchez, a rancher "
              "and owner of a demolition and construction contracting business in Veguita, "
              "joined the unanimous Republican caucus in opposing the 21-17 Senate floor "
              "vote. The NM Senate GOP called SB 17 a 'radical gun control measure' that "
              "unconstitutionally infringes on Second Amendment rights.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://ballotpedia.org/Joshua_A._Sanchez"]),
        claim("jas3", "joshua-a-sanchez", "biblical_marriage", 2, True,
              "Voted NO on HB 7 (2023), the 'Reproductive and Gender-Affirming Health Care "
              "Act,' which created state-level protections for abortion access and "
              "gender-transition services, prohibited local governments from restricting "
              "these procedures, and blocked any interference with providers performing "
              "gender-affirming care. The New Mexico Senate passed HB 7 on a 23-15 vote, "
              "with all 15 Republican senators — including Sanchez — opposing a bill that "
              "embedded both abortion access and transgender health mandates into state law. "
              "Gov. Lujan Grisham signed HB 7 on March 16, 2023.",
              ["https://www.ksfr.org/2023-legislature/2023-03-08/reproductive-and-gender-affirming-health-care-bill-clears-state-senate",
               "https://nmpoliticalreport.com/2023/03/08/reproductive-and-gender-affirming-healthcare-bill-close-to-passing-legislature/",
               "https://www.governor.state.nm.us/2023/03/16/governor-signs-house-bill-7-reproductive-and-gender-affirming-health-care-act/"]),
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
