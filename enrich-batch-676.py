#!/usr/bin/env python3
"""Enrichment batch 676: hand-curated claims for 5 RI state senators.

archetype_curated federal bucket exhausted; archetype_party_default state
senators from bottom of alphabet (RI). Targets chosen from the top of the
reverse-alpha list to avoid collision with the top-of-alphabet loop.

Targets: Leonidas Raptakis (RI), Frank Ciccone (RI), Dawn Euer (RI),
Hanna Gallo (RI), Jonathon Acosta (RI).
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
    # ---------- Leonidas Raptakis (RI SD33, Coventry/West Greenwich — conservative Democrat) ----------
    ("leonidas-raptakis", "RI", "State Senator", [
        claim("lr1", "leonidas-raptakis", "sanctity_of_life", 0, True,
              "Voted NO on the Reproductive Privacy Act (RI S0152, 2019) — the bill that codified abortion access in Rhode Island state law — both in Senate Judiciary Committee (where a 5-4 vote initially killed it) and on the final floor vote (passed 21-17). Citizens for Life RI publicly praised his 'courageous efforts' opposing the legislation.",
              ["https://upriseri.com/2019-06-20-repro/",
               "https://www.citizensforliferi.com/media_release_citizens_for_life_ri_reaction_on_reproductive_privacy_act_passage"]),
        claim("lr2", "leonidas-raptakis", "self_defense", 1, True,
              "One of only two Senate Democrats who voted against the 2024 mandatory safe-storage firearms bill (final vote 28-7), and opposed the 2022 high-capacity magazine ban. At the 2025 Senate Judiciary hearing on Rhode Island's assault-weapons ban, Raptakis stated publicly: 'No form of a firearms ban is acceptable under the guise of making us safer — it's ridiculous' — among the most explicit pro-Second-Amendment positions of any Democrat in the chamber.",
              ["https://rhodeislandcurrent.com/2024/03/19/safe-weapons-bill-passes-through-rhode-island-senate/",
               "https://rhodeislandcurrent.com/2025/06/18/vote-first-ask-questions-later-senate-panel-quickly-advances-reworked-assault-weapons-ban/",
               "https://www.oceanstatemedia.org/politics/gun-bills-draw-a-crowd-to-rhode-island-state-house-for-seven-and-a-half-hours-of-testimony"]),
    ]),

    # ---------- Frank Ciccone (RI SD7, Providence/Johnston — Senate Majority Leader, licensed FFL dealer) ----------
    ("frank-ciccone", "RI", "State Senator", [
        claim("fc1", "frank-ciccone", "sanctity_of_life", 0, True,
              "A Democrat who has co-sponsored anti-abortion legislation every session for over a decade. Primary co-sponsor of the Born-Alive Infant Protection Act (2018) — AUL model legislation requiring life-saving care for infants surviving abortion. Voted against the Reproductive Privacy Act (2019, 21-17) and against the 2023 Equality in Abortion Coverage Act expanding Medicaid funding for abortion.",
              ["https://perfectunion.us/rhode-islands-corporate-anti-choice-democrats-are-facing-challenges-from-the-left/",
               "https://rhodeislandcurrent.com/2025/04/29/madame-president-r-i-senate-picks-lawson-to-lead-with-ciccone-as-her-no-2/"]),
        claim("fc2", "frank-ciccone", "biblical_marriage", 1, True,
              "Described in multiple news accounts as 'a same-sex marriage opponent.' When the Rhode Island General Assembly moved to legalize same-sex marriage in 2013, Ciccone introduced a compromise bill that would have placed the question on the 2014 ballot rather than passing it directly — a blocking tactic that sought to delay and potentially defeat marriage equality legislation.",
              ["https://en.wikipedia.org/wiki/Same-sex_marriage_in_Rhode_Island",
               "https://www.browndailyherald.com/article/2013/05/after-16-years-r-i-legalizes-same-sex-marriage/"]),
        claim("fc3", "frank-ciccone", "self_defense", 1, True,
              "A licensed federal firearms dealer (FFL) who sells guns from his home — a posture that drew press scrutiny when he became Senate Majority Leader in April 2025. One of only two Democrats to vote against the 2024 mandatory safe-storage bill (28-7). Opposed the 2022 magazine ban, offering a grandfather-clause amendment. Publicly stated he would oppose the 2025 assault-weapons ban 'as currently drafted,' reflecting a consistent pro-Second-Amendment record that 'rankled progressive lawmakers.'",
              ["https://rhodeislandcurrent.com/2025/05/16/ciccone-has-been-a-licensed-firearms-dealer-for-decades-should-he-recuse-himself-from-gun-debate/",
               "https://rhodeislandcurrent.com/2024/03/19/safe-weapons-bill-passes-through-rhode-island-senate/"]),
    ]),

    # ---------- Dawn Euer (RI SD13, Newport/Jamestown — Senate President, progressive) ----------
    ("dawn-euer", "RI", "State Senator", [
        claim("de1", "dawn-euer", "sanctity_of_life", 0, False,
              "As Senate Judiciary Chair, introduced the Healthcare Provider Shield Act (2024), which passed 29-7. The law shields physicians who perform abortions or provide gender-affirming care from prosecution or civil liability by other states — explicitly protecting both the abortion industry and cross-sex medical interventions from accountability.",
              ["https://www.advocate.com/news/rhode-island-shield-law-abortion-transgender",
               "https://www.bostonglobe.com/2024/05/03/metro/ri-bill-would-shield-doctors-who-provide-abortion-transgender-care/"]),
        claim("de2", "dawn-euer", "biblical_marriage", 1, False,
              "Before her 2017 election to the Senate, Euer served as Deputy Campaign Director for Rhode Islanders United for Marriage — the campaign that successfully legalized same-sex marriage in Rhode Island in 2013. She has since described herself as a champion of marriage equality, making her a core architect of the policy the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Dawn_Euer",
               "https://ballotpedia.org/Dawn_Euer"]),
        claim("de3", "dawn-euer", "election_integrity", 2, False,
              "Senate sponsor of the 'Let RI Vote Act' (2022-S 2007A), which eliminated the excuse requirement for mail-in ballots, dropped the two-witness or notary signature requirement, created online mail-ballot applications, and made permanent early in-person voting — expanding no-excuse absentee and mass mail-in voting in Rhode Island. Honored by Common Cause RI for the legislation.",
              ["https://governor.ri.gov/press-releases/governor-mckee-signs-let-ri-vote-act",
               "https://www.reportertoday.com/stories/whip-kazarian-and-chairwoman-euer-honored-by-common-cause-ri-for-let-ri-vote-act,43203"]),
    ]),

    # ---------- Hanna Gallo (RI SD27, Cranston/West Warwick — Senate President Pro Tempore, Planned Parenthood champion) ----------
    ("hanna-gallo", "RI", "State Senator", [
        claim("hg1", "hanna-gallo", "sanctity_of_life", 0, False,
              "Named by Planned Parenthood Votes! Rhode Island as one of 17 'champions who were crucial in passing the Reproductive Privacy Act of 2019' (Senate 21-17), which codified the right to abortion in RI state law and removed criminal penalties on providers — a landmark pro-abortion vote. Received the Planned Parenthood PAC endorsement in the 2020 election cycle.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-votes-rhode-island/news-room/with-national-election-results-unclear-voters-in-rhode-island-prove-sexual-and-reproductive-health-and-rights-are-winning-issues",
               "https://upriseri.com/2019-06-20-repro/"]),
        claim("hg2", "hanna-gallo", "self_defense", 1, False,
              "Co-sponsor of S0359, the Rhode Island Assault Weapons Ban Act of 2025, which bans the manufacture, sale, and transfer of semi-automatic rifles and shotguns defined as 'military-style weapons' statewide. The Senate passed it 25-11 on June 20, 2025; Governor McKee signed it into law with an effective date of July 1, 2026.",
              ["https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-bill-banning-sale-assault-weapons",
               "https://www.billtrack50.com/billdetail/1842237"]),
    ]),

    # ---------- Jonathon Acosta (RI SD16, Central Falls/Pawtucket — progressive, first elected 2020) ----------
    ("jonathon-acosta", "RI", "State Senator", [
        claim("ja1", "jonathon-acosta", "self_defense", 1, False,
              "Endorsed by the Rhode Island Coalition Against Gun Violence (RICAGV), which maintains a dedicated endorsement page for him and whose platform includes magazine bans, red-flag laws, and assault-weapons restrictions. Acosta self-describes as an 'advocate for common sense gun control.'",
              ["https://ricagv.org/politics/jonathan-acosta/",
               "https://ricagv.org/endorsed-candidates/"]),
        claim("ja2", "jonathon-acosta", "economic_stewardship", 2, False,
              "Signed the Green New Deal pledge as a condition of endorsement by the RI Political Cooperative, requiring members to support Green New Deal policies. His platform calls for rolling back early-2000s tax cuts on Rhode Island's top 5% of earners to fund 'critical social programs' and an expanded state budget line for affordable housing — opposing fiscal restraint and balanced-budget principles.",
              ["https://www.jonacosta.com/",
               "https://ecori.org/social-justice-archive/2021/1/18/progressive-act-addresses-environmental-social-justice/"]),
        claim("ja3", "jonathon-acosta", "public_justice", 0, False,
              "Introduced the Rishod K. Gore Justice in Policing Act of 2021 (with Rep. José Batista), which would eliminate qualified immunity for officers who engage in willful misconduct, ban chokeholds and neck restraints, prohibit officers from striking suspects or using vehicles as weapons, mandate officer intervention on witnessed misconduct, and require statewide body cameras. He also sponsored legislation to bar private prisons in Rhode Island.",
              ["https://patch.com/rhode-island/pawtucket/sen-acosta-rep-batista-file-ri-police-reform-bill",
               "https://turnto10.com/i-team/ri-lawmakers-push-for-statewide-body-cameras-and-other-police-reforms"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
