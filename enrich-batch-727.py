#!/usr/bin/env python3
"""Enrichment batch 727: 5 New Mexico Republican State Senators with 0 claims.

Bottom-of-alphabet pivot: WY/WV/WI/WA all exhausted; taking from the next
deepest range — NM Republican state senators, reverse-alpha sorted.

Targets: William Sharer (NM-1, Minority Floor Leader), Pat Woods (NM-7,
Minority Whip), Craig Brandt (NM-40), Crystal Brantley (NM-35, Caucus
Chair), Steve D. Lanier (NM-2, new senator 2024).

Key sourced votes/positions:
  SB 57 (2025) — bill shielding abortion provider records at public institutions
    from IPRA requests; passed 26-16 on strict party line (all 16 Republicans
    voted NO). Pat Woods specifically quoted opposing it.
  SB 17 (2026) — "Stop the Illegal Gun Trade and Extremely Dangerous Weapons
    Act"; banned semi-auto gas-operated rifles and 10-round+ magazines; passed
    21-17 with all Republicans present voting NO. Sharer led floor opposition.
    Brantley specifically named in reporting as voting NO.
  PFML committee (2025) — Senate Finance Committee voted 8-3 to table the
    Paid Family & Medical Leave Act; Lanier was among the majority.
  Sharer flat-tax proposal (2025) — Senate Minority Leader proposed replacing
    NM's complex gross receipts tax with a flat 2% rate, a recurring fiscal
    restraint initiative.
  Crystal Brantley CYFD reform — sponsored/enacted legislation creating the
    Office of the Child Advocate and phone-free school legislation.
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
    # ----------- William Sharer (NM-1, Farmington, Minority Floor Leader since Jan 2025) -----------
    ("william-sharer", "NM", "State Senator", [
        claim("ws1", "william-sharer", "self_defense", 1, True,
              "As Senate Minority Leader, personally led Republican floor opposition to SB 17 (2026), "
              "the 'Stop the Illegal Gun Trade and Extremely Dangerous Weapons Act,' which banned "
              "the sale of gas-operated semi-automatic rifles and magazines holding more than 10 "
              "rounds. Sharer called the bill an infringement 'on a constitutional right he sees as "
              "a safeguard against tyranny.' He and his Republican colleagues debated against the "
              "bill for more than four hours. The Senate passed it 21-17, with all Republicans "
              "present voting NO.",
              ["https://www.santafenewmexican.com/news/legislature/senators-public-square-off-on-safety-versus-freedom-in-gun-debate/article_09b63a1d-ebfe-453c-bed5-c1cbd064c452.html",
               "https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate"]),
        claim("ws2", "william-sharer", "economic_stewardship", 2, True,
              "Repeatedly proposed replacing New Mexico's complex, loophole-laden gross receipts "
              "tax system with a simple flat 2% rate, with no exemptions — a fiscal-restraint "
              "and simplification initiative designed to reduce government complexity and level the "
              "playing field for all businesses. The Santa Fe New Mexican reported this as a "
              "'longshot' reform Sharer keeps advancing as Senate Minority Leader, reflecting a "
              "sustained commitment to reducing tax burdens and closing cronyist exemptions.",
              ["https://www.santafenewmexican.com/news/local_news/new-mexico-state-senate-minority-leader-again-proposes-longshot-tax-system-overhaul/article_36006cc0-0662-42bb-afce-5a3a761c6a63.html",
               "https://www.rdrnews.com/news/local/nm-senate-gop-taps-sharer-for-minority-leader/article_0cc0a47c-9e1e-11ef-a376-e732388b0dc8.html"],
              kind="position"),
        claim("ws3", "william-sharer", "border_immigration", 0, True,
              "As Senate Minority Leader, Sharer led New Mexico Senate Republicans in declaring "
              "the border crisis 'the number one issue' facing the state and demanding enforcement "
              "reforms modeled on Texas's approach — including military and law-enforcement "
              "deployment to address the flow of drugs and crime across the southern border. "
              "Sharer's caucus has consistently opposed Democrat-led policies that limit "
              "cooperation with federal immigration enforcement.",
              ["https://nmsenategop.com/member/william-sharer/",
               "https://www.santafenewmexican.com/news/elections/sharer-named-new-senate-minority-leader/article_b46e442e-9d59-11ef-8304-03159004e5ea.html"],
              kind="position"),
    ]),

    # ----------- Pat Woods (NM-7, Broadview, Minority Whip, rancher since 2012) -----------
    ("pat-woods", "NM", "State Senator", [
        claim("pw1", "pat-woods", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), a Democrat-sponsored bill that would shield records of "
              "abortion providers at public institutions from New Mexico's Inspection of Public "
              "Records Act. The bill passed 26-16 on a strict party-line vote, with all 16 "
              "Republican senators voting NO. Woods specifically challenged the need for special "
              "secrecy, stating on the floor: 'There are already exemptions for sensitive and "
              "personal information an IPRA request cannot reveal to the public, so what exactly "
              "is this bill trying to hide?' — opposing a legislative shield for abortion "
              "practices at state-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://ballotpedia.org/Pat_Woods"]),
        claim("pw2", "pat-woods", "self_defense", 1, True,
              "As New Mexico Senate Minority Whip, Pat Woods is a member of the Republican "
              "caucus that delivered unanimous opposition to SB 17 (2026), the sweeping gun "
              "control package banning gas-operated semi-automatic rifles and 10-round-plus "
              "magazines. All Republicans present voted NO on the 21-17 Senate floor vote. "
              "The NM Senate Republican caucus described the legislation as a 'radical gun "
              "control measure' and a 'relentless' unconstitutional infringement on Second "
              "Amendment rights.",
              ["https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate",
               "https://ballotpedia.org/Pat_Woods"]),
    ]),

    # ----------- Craig Brandt (NM-40, Rio Rancho, 7-yr Air Force vet, since 2013) -----------
    ("craig-brandt", "NM", "State Senator", [
        claim("cb1", "craig-brandt", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), a party-line 26-16 vote in which all 16 New Mexico "
              "Senate Republicans rejected a Democrat bill that would exempt abortion provider "
              "records at public institutions from the state's open-records law. Brandt, who "
              "holds a bachelor's degree in pastoral ministries from Oklahoma Baptist University "
              "and has consistently championed traditional values in the legislature, voted to "
              "maintain public accountability for abortion practices at state-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://ballotpedia.org/Craig_Brandt"]),
        claim("cb2", "craig-brandt", "self_defense", 1, True,
              "As a member of the New Mexico Senate Republican caucus and as ranking member of "
              "the Senate Public Affairs Committee — where he has 'championed Constitutional "
              "rights and limited government intrusion' — Brandt joined the unanimous Republican "
              "bloc opposing SB 17 (2026), the semi-automatic rifle and magazine ban that passed "
              "21-17 over relentless Republican opposition. The NM Senate GOP formally condemned "
              "SB 17 as a 'radical gun control measure' and an unconstitutional infringement.",
              ["https://nmsenategop.com/member/craig-brandt/",
               "https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/",
               "https://www.nraila.org/articles/20260208/new-mexico-sweeping-gun-control-bill-passes-senate"]),
    ]),

    # ----------- Crystal Brantley (NM-35, Elephant Butte, Caucus Chair, border district) -----------
    ("crystal-brantley", "NM", "State Senator", [
        claim("cbr1", "crystal-brantley", "self_defense", 1, True,
              "Voted NO on SB 17 (2026), specifically named in news coverage as one of the "
              "Republican senators opposing the 'Stop the Illegal Gun Trade and Extremely "
              "Dangerous Weapons Act,' which would have banned semi-automatic gas-operated "
              "rifles and 10-round-plus magazines. Senate Minority Leader Bill Sharer, who "
              "elected Brantley as caucus chair, highlighted her work to 'defeat damaging and "
              "unconstitutional policies such as radical gun-grabs.' The bill passed 21-17 "
              "with all Republicans present voting NO.",
              ["https://sourcenm.com/2026/02/09/weekend-wrap-new-mexico-senate-advances-bill-limiting-gun-sales-produced-water-proposal-fails/",
               "https://www.santafenewmexican.com/news/local_news/crystal-brantley-to-lead-new-mexico-senate-gop-caucus/article_3f34e74c-d7c2-448f-a8ca-7ff0d05df550.html",
               "https://nmsenategop.com/2026/02/08/radical-gun-control-measure-sb-17-passes-final-senate-vote-despite-relentless-republican-opposition/"]),
        claim("cbr2", "crystal-brantley", "family_child_sovereignty", 0, True,
              "Has driven child welfare and parental-rights reform every legislative session "
              "since taking office, resulting in enacted legislation creating the Office of "
              "the Child Advocate — an independent watchdog to protect children from CYFD "
              "(child welfare agency) overreach and ensure family accountability. She also "
              "sponsored and passed phone-free school legislation, protecting children from "
              "smartphone-driven harms during the school day. Senate Minority Leader Sharer "
              "cited these reforms as hallmarks of her 'fierce advocacy for the people of "
              "New Mexico.'",
              ["https://www.santafenewmexican.com/news/local_news/crystal-brantley-to-lead-new-mexico-senate-gop-caucus/article_3f34e74c-d7c2-448f-a8ca-7ff0d05df550.html",
               "https://newmexicosun.com/stories/670497418-fighting-for-reform-senator-crystal-brantley-s-push-for-change-in-new-mexico"]),
        claim("cbr3", "crystal-brantley", "border_immigration", 0, True,
              "In 2020 became the first Republican and first woman elected to New Mexico Senate "
              "District 35, which covers seven counties along the New Mexico–Mexico border — "
              "the state's largest district by area. She credits her victory to voter "
              "dissatisfaction with the state's approach to border security. Her stated policy "
              "passions include Public Safety & Border Security, and she has opposed Democrat "
              "policies that limit immigration enforcement in her border-region district.",
              ["https://ballotpedia.org/Crystal_Diamond_Brantley",
               "https://www.legistorm.com/person/bio/387490/Crystal_Diamond_Brantley.html",
               "https://www.santafenewmexican.com/news/local_news/crystal-brantley-to-lead-new-mexico-senate-gop-caucus/article_3f34e74c-d7c2-448f-a8ca-7ff0d05df550.html"],
              kind="position"),
    ]),

    # ----------- Steve D. Lanier (NM-2, Aztec, teacher/coach, took office Jan 2025) -----------
    ("steve-d-lanier", "NM", "State Senator", [
        claim("sl1", "steve-d-lanier", "economic_stewardship", 2, True,
              "In the 2025 legislative session, Lanier was part of the 8-3 Senate Finance "
              "Committee majority that voted to table New Mexico's Paid Family & Medical Leave "
              "Act — blocking a new government-mandated employer-payroll insurance fund that "
              "would have imposed significant new costs on businesses and created a state-run "
              "benefit program. Opposing the bill reflected a commitment to limiting government "
              "spending mandates and protecting employers from new fiscal obligations.",
              ["https://ballotpedia.org/Steve_Lanier",
               "https://www.abqjournal.com/news/article_f54f0478-3282-4e3d-887f-22416d600000.html"]),
        claim("sl2", "steve-d-lanier", "sanctity_of_life", 0, True,
              "Voted NO on SB 57 (2025), a party-line 26-16 vote in which all 16 New Mexico "
              "Senate Republicans rejected a Democrat bill exempting abortion provider records "
              "at public institutions from the state's Inspection of Public Records Act. "
              "Lanier, a first-term senator who ran as a 'common-sense' conservative, joined "
              "his caucus in opposing special legal shields for abortion practices at "
              "state-funded facilities.",
              ["https://sourcenm.com/2025/03/20/nm-legislative-recap-march-20-a-picture-tells-1000-words/",
               "https://ballotpedia.org/Steve_Lanier"]),
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
