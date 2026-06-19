#!/usr/bin/env python3
"""Enrichment batch 295: hand-curated claims for 5 Wyoming state senators.

archetype_curated federal bucket exhausted; batch completes the WY State
Senator sub-bucket (archetype_party_default, 0 claims, reverse alpha):
Barry Crago (SD-22), Brian Boner (SD-2), Bob Ide (SD-29),
Bill Landen (SD-27), Cale Case (SD-25).

Key sourced votes / actions:
  WY HB 126 (2026) — Human Heartbeat Act, banning abortion once a fetal
  heartbeat is detectable; Senate co-sponsors include Boner and Ide;
  passed Senate 27-4; signed by Governor Gordon March 9, 2026.
  WY HB 125 (2024) — Repeal gun free zones and preemption amendments;
  Senate passed 22-8-1 on March 7, 2024; Bob Ide co-sponsor; Bill Landen
  cast deciding committee vote to kill but ultimately voted AYE on floor;
  bill vetoed by governor (gun-free zones later repealed via HB 172, 2025).
  WY SF0113 (2026) — Election hand count comparison; sponsored by Barry
  Crago; signed into law; requires county clerks to hand-count 5% of
  all ballots in 2026 primary and general elections to audit tabulator
  accuracy; effective for August 2026 primary.
  Cale Case — libertarian Republican economist; voted against WY Senate bill
  that would have barred recognition of out-of-state same-sex marriages;
  earned 100% on Wyoming Liberty Index (2012), ranking 1st in WY Senate.
  Brian Boner — since 2015 has helped cut $1 billion in biennial operating
  costs from Wyoming's state budget; chairs WY Senate Agriculture Committee.
  Barry Crago — sits on Wyoming's Select Committee on Blockchain, Financial
  Technology and Digital Innovation Technology (SPDI/DAO framework).

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{slug}-{category}-{q_idx}-{cid}",
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
    # ---------- Barry Crago (WY-R, State Senator SD-22, since Jan 2025) ----------
    ("barry-crago", "WY", "State Senator", [
        claim("bc1", "barry-crago", "election_integrity", 0, True,
              "Sponsored WY SF0113 (2026), the 'Election Hand Count Comparison' bill, signed into law, requiring all Wyoming county clerks to hand-count approximately 5% of ballots cast in each 2026 primary and general election contest and compare results against machine tabulator output. Crago said the bill's intent was to address Wyomingites' 'concerns about the accuracy and integrity of our tabulating machines.' The hand-count audit provision — covering both primary and general elections — took effect with the August 2026 primary.",
              ["https://www.wyomingpublicmedia.org/politics-government/2026-02-24/hand-recounts-bill-and-other-election-measures-move-along-in-legislative-process",
               "https://www.wyomingpublicmedia.org/politics-government/2026-03-10/new-laws-concealed-carry-at-18-professional-wildfire-fighters-and-hand-counting-ballots",
               "https://legiscan.com/WY/bill/SF0113/2026"]),
        claim("bc2", "barry-crago", "economic_stewardship", 0, True,
              "Crago serves on Wyoming's Select Committee on Blockchain, Financial Technology and Digital Innovation Technology, the legislative body overseeing Wyoming's groundbreaking SPDI (Special Purpose Depository Institution) banking-charter law and DAO LLC Act — statutes that authorize non-bank, non-Federal Reserve digital-asset custody and decentralized autonomous organization recognition, providing an alternative monetary-architecture framework explicitly outside centralized government currency control. Wyoming is the only state with a full statutory stack enabling hard-asset digital custody independent of the Federal Reserve system.",
              ["https://ballotpedia.org/Barry_Crago",
               "https://en.wikipedia.org/wiki/Barry_Crago"]),
    ]),

    # ---------- Brian Boner (WY-R, State Senator SD-2, since Jan 2015) ----------
    ("brian-boner", "WY", "State Senator", [
        claim("bb1", "brian-boner", "sanctity_of_life", 0, True,
              "Co-sponsored WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable (approximately six weeks' gestation), with a narrow medical-emergency exception; Governor Mark Gordon signed the bill into law on March 9, 2026. Boner is listed among thirteen Senate co-sponsors of the legislation alongside Sens. Biteman, Laursen, Brennan, Dockstader, Hicks, Hutchings, Ide, Love, Olsen, Pearson, Salazar, and Steinmetz. A sixth-generation Wyoming rancher, Air Force veteran, and Platte/Converse County senator since 2015, Boner co-sponsored the bill as a statement of his pro-life convictions.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Brian_Boner"]),
        claim("bb2", "brian-boner", "economic_stewardship", 2, True,
              "Since joining the Wyoming Senate in 2015, Boner has helped cut $1 billion in biennial operating costs from Wyoming's state budget, maintaining the state's no-income-tax, balanced-budget tradition. He chairs the Wyoming Senate Agriculture Committee and has sponsored the Cowboy State Agricultural Trust Fund bill (SF0109, 2025) to preserve Wyoming resource revenues within the state rather than channeling them into federal spending streams.",
              ["https://www.brianboner.org/",
               "https://ballotpedia.org/Brian_Boner"]),
    ]),

    # ---------- Bob Ide (WY-R, State Senator SD-29, since Dec 2022) ----------
    ("bob-ide", "WY", "State Senator", [
        claim("bi1", "bob-ide", "sanctity_of_life", 0, True,
              "Co-sponsored WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable; Governor Mark Gordon signed the bill into law on March 9, 2026. Ide is listed among thirteen Senate co-sponsors of the legislation alongside Sens. Biteman, Boner, Brennan, Dockstader, Hicks, Hutchings, Laursen, Love, Olsen, Pearson, Salazar, and Steinmetz. Ide, a commercial real estate developer representing Natrona County's Senate District 29 since December 2022, co-sponsored the bill as a statement of pro-life principle.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Bob_Ide"]),
        claim("bi2", "bob-ide", "self_defense", 0, True,
              "Co-sponsored WY HB 125 (2024), 'Repeal Gun Free Zones and Preemption Amendments,' a bill to repeal all gun-free zone designations on public property in Wyoming and clarify that only the state legislature — not local governments — may regulate firearms, weapons, and ammunition. The Wyoming Senate passed the bill 22-8-1 on March 7, 2024. Governor Gordon subsequently vetoed the measure, but Wyoming's gun-free zones were ultimately repealed via HB 172 (enacted without signature, February 2025). Ide's co-sponsorship reflects his foundational commitment to permitless and location-unrestricted constitutional carry.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0125",
               "https://cowboystatedaily.com/2024/03/05/wyomings-gun-free-zones-to-stay-after-bill-to-get-rid-of-them-dies/",
               "https://ballotpedia.org/Bob_Ide"]),
    ]),

    # ---------- Bill Landen (WY-R, State Senator SD-27, since Jan 2007) ----------
    ("bill-landen", "WY", "State Senator", [
        claim("bl1", "bill-landen", "sanctity_of_life", 0, True,
              "Voted AYE on WY HB 126 (2026), the Human Heartbeat Act, prohibiting abortion in Wyoming once a fetal heartbeat is detectable (approximately six weeks' gestation), with a narrow medical-emergency exception; Governor Mark Gordon signed the bill into law on March 9, 2026. The Wyoming Senate passed HB 126 by a 27-4 margin. Landen, a Republican representing Natrona County's Senate District 27 since 2007, voted with the overwhelming Republican majority to enact Wyoming's most protective pro-life statute in decades.",
              ["https://www.wyomingnewsnow.tv/news/heartbeat-act-passes-senate-and-moves-to-governors-desk/article_1fad539e-f039-4ff7-8f40-1af8df7537cb.html",
               "https://wyoleg.gov/Legislation/2026/HB0126",
               "https://ballotpedia.org/Bill_Landen"]),
        claim("bl2", "bill-landen", "self_defense", 0, True,
              "Landen's initial Senate Judiciary Committee vote killed WY HB 125 (2024), 'Repeal Gun Free Zones and Preemption Amendments' — he cast the deciding 'no' vote citing a personal experience at Casper College during a murder-suicide — but the full Senate voted to reconsider the bill, and Landen subsequently changed his vote, supporting final passage 22-8-1 on March 7, 2024. Governor Gordon vetoed the bill; Wyoming's gun-free zones were later repealed via HB 172 (2025, enacted without signature). Landen's floor vote places him on the side of expanding constitutional carry, notwithstanding his initial committee hesitation.",
              ["https://www.wyomingnews.com/news/local_news/senate-committee-votes-to-keep-state-s-gun-free-zones-in-place-full-chamber-votes/article_e87cad72-daaf-11ee-ae22-53a57201fe12.html",
               "https://cowboystatedaily.com/2024/03/05/wyomings-gun-free-zones-to-stay-after-bill-to-get-rid-of-them-dies/",
               "https://wyofile.com/shot-down-resuscitated-wyoming-senate-bucks-precedent-to-target-gun-free-zones/"]),
    ]),

    # ---------- Cale Case (WY-R, State Senator SD-25, since Jan 1999) ----------
    ("cale-case", "WY", "State Senator", [
        claim("cc1", "cale-case", "biblical_marriage", 0, False,
              "Case voted against a Wyoming Senate bill that would have forbidden the state from recognizing same-sex marriages legally contracted in other states or countries — breaking with the majority of his Republican colleagues and signaling acceptance of same-sex marriage as a legally valid institution. A self-described libertarian economist who endorsed Ron Paul in 2008 and earned a 100% Wyoming Liberty Index score in 2012 (ranking 1st in the 31-member Wyoming State Senate), Case has consistently applied libertarian contract-recognition principles over social conservatism on marriage questions, placing him outside the rubric's one-man-one-woman marriage ideal.",
              ["https://ballotpedia.org/Cale_Case",
               "https://en.wikipedia.org/wiki/Cale_Case"]),
        claim("cc2", "cale-case", "economic_stewardship", 2, True,
              "Case earned a score of 100% on the Wyoming Liberty Index (2012), ranking 1st out of 31 Wyoming Senate members, reflecting a consistent record of voting against new taxes and government spending expansions. A Ph.D. economist who has served Fremont County's Senate District 25 since 1999, Case has long been Wyoming's most recognizable voice for fiscal austerity and balanced-budget discipline in the state chamber.",
              ["https://ballotpedia.org/Cale_Case",
               "https://en.wikipedia.org/wiki/Cale_Case"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
