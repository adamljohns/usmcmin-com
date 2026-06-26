#!/usr/bin/env python3
"""Enrichment batch 433: 5 Wisconsin State Assembly Republicans (archetype_party_default, 0 claims).

Federal senator/rep archetype_curated and archetype_party_default buckets exhausted;
continuing with WI state-level officials from the bottom-of-alphabet queue:
William Penterman (WI-38), Treig Pronschinske (WI-29), Travis Tranel (WI-49),
Tony Kurtz (WI-41), Todd Novak (WI-51).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = "2026-06-26"


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
    # ---------- William Penterman (WI Assembly-38, R) ----------
    ("william-penterman-wi-38", "WI", "Assembly", [
        claim("wp1", "william-penterman-wi-38", "sanctity_of_life", 0, True,
              "Co-sponsored 2023 Assembly Bill 63 (Born Alive Infant Protection Act), requiring health care providers to give life-saving treatment to infants surviving abortion. On iVoterGuide, stated 'Life is sacred and should be protected. To make exceptions is a slippery slope' — affirming personhood from conception.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://ivoterguide.com/candidate?canK=58626&elecK=838&path=%2Fall-in-state%2Fwi&primarypartyk=R&raceK=12888"]),
        claim("wp2", "william-penterman-wi-38", "sanctity_of_life", 4, True,
              "Endorsed by both Pro-Life Wisconsin Victory Fund and Wisconsin Right to Life PAC in the 2022 general election; states that 'abortion providers, including Planned Parenthood, should not receive taxpayer funds or grants from federal, state, or local governments.'",
              ["https://www.prolifewi.org/fall-2022-general-election-endorsements",
               "https://wisconsinrighttolife.org/wrtl-news/2022/09/19/wisconsin-right-to-life-political-action-committee-announces-endorsements-for-2022-fall-general-election/"]),
        claim("wp3", "william-penterman-wi-38", "border_immigration", 2, True,
              "Co-sponsored 2025 Assembly Bill 24, requiring county sheriffs to verify immigration status of felony detainees, comply with ICE detainers and administrative warrants, and penalizing non-compliance with a 15% shared-revenue reduction — an anti-sanctuary enforcement measure. Passed Assembly 51-43 on party-line vote.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab24",
               "https://legiscan.com/WI/bill/AB24/2025"]),
    ]),

    # ---------- Treig Pronschinske (WI Assembly-29, R) ----------
    ("treig-pronschinske-wi-29", "WI", "Assembly", [
        claim("tp1", "treig-pronschinske-wi-29", "self_defense", 1, True,
              "Lead author of 2023 Assembly Bill 801, allowing concealed-carry licensees to carry in a place of worship on private school grounds when the governing body has a written policy permitting it; also co-authored 2023 AB1160 (sales and use tax exemption for firearms and ammunition) — a direct opponent of new restrictions on the right to keep and bear arms.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab801",
               "https://docs.legis.wisconsin.gov/2023/proposals/reg/asm/bill/ab1160"]),
        claim("tp2", "treig-pronschinske-wi-29", "sanctity_of_life", 0, True,
              "Voted yes on 2023 Assembly Bill 975 (14-week abortion ban via statewide referendum), which passed the Assembly 53-46 on January 25, 2024. The 11 Republicans who voted no did so because they found the restriction insufficiently strict — not because they supported broader abortion access.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://legiscan.com/WI/rollcall/AB975/id/1369064"]),
        claim("tp3", "treig-pronschinske-wi-29", "border_immigration", 2, True,
              "Voted yes on 2025 Assembly Bill 24 (passed 51-43 on a party-line vote, March 18, 2025), requiring Wisconsin sheriffs to honor ICE detainers and administrative warrants for felony detainees and penalizing non-compliance with a 15% shared-revenue cut — opposing sanctuary county policies.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab24",
               "https://www.wpr.org/news/assembly-republicans-sheriffs-ice-cooperation-federal-immigration-authorities"]),
    ]),

    # ---------- Travis Tranel (WI Assembly-49, R) ----------
    ("travis-tranel-wi-49", "WI", "Assembly", [
        claim("tt1", "travis-tranel-wi-49", "sanctity_of_life", 0, True,
              "Co-authored 2021 Assembly Bill 6 (Born Alive Infant Protection Act reintroduction) requiring emergency medical care for infants surviving abortion; previously co-authored 2019 AB179 (same subject); and voted YES on 2023 AB975 (14-week abortion ban, 53-46, January 25, 2024). Campaign materials state belief in 'the value of life and the sanctity of marriage.'",
              ["https://docs.legis.wisconsin.gov/2021/proposals/ab6",
               "https://docs.legis.wisconsin.gov/2019/related/proposals/ab179",
               "https://legiscan.com/WI/rollcall/AB975/id/1369064"]),
        claim("tt2", "travis-tranel-wi-49", "self_defense", 1, True,
              "NRA member; authored 2019 Assembly Bill 366 (sales and use tax exemption for gun safe purchases), demonstrating legislative commitment to protecting lawful gun ownership without new restrictions.",
              ["https://docs.legis.wisconsin.gov/2019/proposals/reg/asm/bill/ab366",
               "https://en.wikipedia.org/wiki/Travis_Tranel"]),
        claim("tt3", "travis-tranel-wi-49", "border_immigration", 4, True,
              "As Agriculture Committee Chair, publicly championed a 2025 bill banning citizens of foreign adversary nations from owning Wisconsin farmland, stating 'It's a really good idea' and noting: 'In China not even the Chinese are allowed to buy farmland. And I think that really just shows how we in this country take private property rights almost for granted.' — directly aligning with the rubric's anti-foreign-farmland position.",
              ["https://www.midwestfarmreport.com/2025/11/08/heres-whats-circling-the-assembly-ag-committee/",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2795"]),
    ]),

    # ---------- Tony Kurtz (WI Assembly-41, R) ----------
    ("tony-kurtz-wi-41", "WI", "Assembly", [
        claim("ak1", "tony-kurtz-wi-41", "sanctity_of_life", 0, True,
              "Named co-sponsor of 2023 Assembly Bill 975, a 14-week abortion ban via statewide referendum; the Assembly passed it 53–46 on January 25, 2024. Twenty-year Army veteran who has consistently supported pro-life legislation as a Republican member of the Assembly since 2019.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://spectrumnews1.com/wi/milwaukee/news/2024/01/25/wisconsin--republicans--abortion-ban-bill"]),
        claim("ak2", "tony-kurtz-wi-41", "economic_stewardship", 2, True,
              "Issued a formal press release calling 2023 Assembly Bill 386 'one of the largest tax cuts in Wisconsin history,' supporting the $2.9 billion income-tax reduction that cut the third bracket from 5.3% to 4.4%; serves on the Joint Committee on Finance overseeing the state budget.",
              ["https://legis.wisconsin.gov/assembly/41/kurtz/press-releases/rep-tony-kurtz-s-statement-on-tax-cut/",
               "https://docs.legis.wisconsin.gov/2023/proposals/ab386"]),
        claim("ak3", "tony-kurtz-wi-41", "family_child_sovereignty", 0, True,
              "Voted yes on 2023 Assembly Bill 510 (Wisconsin Parental Bill of Rights), which passed 62-35 on a strict party-line vote in January 2024, establishing enforceable parental authority over children's education, religious upbringing, medical decisions, and school pronoun policies.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab510",
               "https://www.wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-childrens-education/"]),
    ]),

    # ---------- Todd Novak (WI Assembly-51, R) ----------
    ("todd-novak-wi-51", "WI", "Assembly", [
        claim("tn1", "todd-novak-wi-51", "sanctity_of_life", 0, True,
              "Named co-sponsor of 2023 Assembly Bill 975 (14-week abortion ban via statewide referendum), which passed the Assembly 53-46 on January 25, 2024; also co-sponsored AB175 (2023), clarifying the medical-necessity exception to Wisconsin's existing abortion prohibition — reinforcing the underlying ban's framework.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://docs.legis.wisconsin.gov/2023/proposals/ab175",
               "https://legiscan.com/WI/rollcall/AB975/id/1369066"]),
        claim("tn2", "todd-novak-wi-51", "self_defense", 1, True,
              "Voted yes on SB466 (Gun Owner Credit Card Data Privacy Act), which passed the Assembly 62-35 on January 18, 2024, prohibiting financial institutions from using firearms-specific merchant codes to track gun purchases — an NRA-ILA endorsed measure. NRA member.",
              ["https://www.nraila.org/articles/20240118/wisconsin-gun-owner-credit-card-data-privacy-bill-headed-to-governor-s-desk",
               "https://legiscan.com/WI/text/SB466/2023"]),
        claim("tn3", "todd-novak-wi-51", "biblical_marriage", 4, False,
              "Co-sponsored 2020 Assembly Joint Resolution 152 formally recognizing June 2020 as LGBT Pride Month in Wisconsin — government promotion of LGBTQ ideology in policy that the rubric opposes.",
              ["https://docs.legis.wisconsin.gov/2019/related/proposals/ajr152",
               "https://docs.legis.wisconsin.gov/2019/legislators/assembly/1845"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
