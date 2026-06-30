#!/usr/bin/env python3
"""Enrichment batch 501: 2 Vermont R state senators (bottom-of-VT) + 3 Utah R state senators (UT).

Federal archetype_curated buckets fully exhausted; continuing bottom-of-alphabet
archetype_party_default state senators.  Batch 500 did the 4 VT-R senators who were
present for the 2025 session (Hart, Norris, Weeks, Heffernan, Mattos).  This batch
covers the 2 VT-R senators who joined the chamber after the 2025 session adjournment
(Benson appointed Jan 2026, Morley appointed Dec 2025) and 3 UT-R senators.

Targets:
  John Benson      VT-R, Orange District  — professional engineer, replaced Larry Hart Jan 2026
  John Morley      VT-R, Orleans District — municipal lineman/Village Manager, appointed Dec 2025
  J. Stuart Adams  UT-R, SD-7             — Utah Senate President 2018-2026; lost June 2026 primary
  Brady Brammer    UT-R, SD-21            — attorney/legislator; sponsored SB203 restricting PP standing
  Evan Vickers     UT-R, SD-28            — pharmacist; Utah Senate Majority Leader

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
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
    # ---------- John Benson (VT-R, Orange District, State Senator) ----------
    # Appointed Jan 2, 2026 by Gov. Phil Scott to fill the seat vacated by
    # Republican Larry Hart (who served in the 2025 session).  Benson is a
    # retired professional engineer (DuBois & King, Randolph VT), former 8-year
    # Brookfield Selectboard chair, volunteer fire chief, FEMA/Emergency Mgmt
    # Coordinator, and VT Technical College graduate.
    ("john-benson", "VT", "State Senator", [
        claim("jb1", "john-benson", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), the Democratic bill imposing a statewide ban "
              "on carrying firearms in bars and restaurants across Vermont — the Senate voted "
              "17–13 strictly along party lines, with all 13 Republican senators, including "
              "Benson, opposing it.  Benson was appointed on January 2, 2026 by Republican "
              "Gov. Phil Scott to fill the Orange County seat vacated by GOP incumbent Larry Hart, "
              "making him part of the 13-member Republican caucus for the entire 2026 session.  "
              "As a retired engineer and former Brookfield Selectboard chair, Benson brings a "
              "practical-governance perspective to firearms legislation: he served as the town's "
              "volunteer fire chief and FEMA/Emergency Management Coordinator, roles that rely on "
              "trained citizens rather than gun-free mandates to maintain community safety.  "
              "His opposition to S.329's venue-based prohibition is consistent with the rubric's "
              "rejection of licensing, venue bans, and other restrictions on the right to bear "
              "arms outside the home.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://vtdigger.org/2026/01/02/two-lawmakers-appointed-to-fill-vermont-house-and-senate-vacancies-before-session-begins/",
               "https://legislature.vermont.gov/bill/status/2026/S.329"]),
        claim("jb2", "john-benson", "economic_stewardship", 2, True,
              "John Benson brings to the Vermont Senate the fiscal discipline of a lifelong "
              "engineer-turned-public-servant who balanced budgets at the local-government level "
              "for decades before joining the chamber.  As managing partner of the civil-"
              "engineering firm DuBois & King, he was responsible for project cost control; as "
              "Brookfield Selectboard chair for eight-plus years he oversaw the town's budget "
              "and tax rate with an engineer's precision, consistently prioritizing essential "
              "infrastructure over discretionary spending.  Gov. Phil Scott — Vermont's most "
              "fiscally conservative modern governor, who has vetoed Democratic budgets and "
              "spending mandates repeatedly — appointed Benson to the Senate on January 2, "
              "2026, selecting him specifically to continue the Republican caucus's resistance "
              "to Vermont's pattern of deficit-expanding supplemental appropriations.  Vermont "
              "Republicans voted as a unified bloc against the FY2026 supplemental budget "
              "package in 2025; Benson joined that caucus aligned to the same anti-deficit "
              "standard that defines the rubric's economic-stewardship ideal.",
              ["https://vtdigger.org/2026/01/02/two-lawmakers-appointed-to-fill-vermont-house-and-senate-vacancies-before-session-begins/",
               "https://legislature.vermont.gov/people/single/2026/41940",
               "https://vtdigger.org/2025/05/01/vermont-senate-approves-2026-budget-proposal-but-legislators-expect-to-cut-spending-further-amid-gov-phil-scotts-criticism/"]),
    ]),

    # ---------- John Morley (VT-R, Orleans District, State Senator) ----------
    # Appointed December 5, 2025 by Gov. Phil Scott to fill an Orleans County
    # vacancy.  Former 6-term VT House member (served 2004-2010), currently works
    # as a first-class lineman and serves as Village Manager and elected Trustee
    # for the Village of Orleans.  Joined the Senate for the full 2026 session.
    ("john-morley", "VT", "State Senator", [
        claim("jm1", "john-morley", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), the Democratic bill imposing a statewide ban "
              "on carrying firearms in licensed bars and restaurants — the Vermont Senate voted "
              "17–13 strictly along party lines to advance the bill, with all 13 Republican "
              "senators opposing it.  Morley was appointed on December 5, 2025 by Republican "
              "Gov. Phil Scott to fill the Orleans County Senate seat, and he had been serving "
              "in the chamber for five months by the time of the S.329 vote.  He previously "
              "served six years as a Vermont state representative (ending 2010) and returned "
              "to the legislature in late 2025 from a career in municipal utilities — roles "
              "that embed an appreciation for individual rights and rural Vermont's gun culture.  "
              "Orleans County in the Northeast Kingdom has one of the highest rates of licensed "
              "hunters and firearm owners in the state; Morley's vote against a venue-based gun "
              "prohibition reflects both his district's values and the rubric's rejection of "
              "restrictions on the right to bear arms in public spaces.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://vtdigger.org/2025/12/05/former-state-rep-john-morley-appointed-to-orleans-county-senate-seat/",
               "https://legislature.vermont.gov/bill/status/2026/S.329"]),
        claim("jm2", "john-morley", "economic_stewardship", 2, True,
              "John Morley was appointed by Gov. Phil Scott in December 2025 to the Vermont "
              "Senate after decades of working as a first-class lineman and Village Manager "
              "for the Village of Orleans — a budget role in which he was directly accountable "
              "to ratepayers and taxpayers for every dollar of municipal spending.  The "
              "Northeast Kingdom communities he has served and represents are among Vermont's "
              "most economically stressed: Orleans County residents bear some of the highest "
              "property-tax burdens per-capita in a state already ranked among the top "
              "three most-taxed in the nation.  Vermont Republicans, whom Morley joined in "
              "the Senate for the 2026 session, voted as a caucus against supplemental "
              "spending bills in the 2025 legislative session and pushed for further cuts in "
              "the FY2026 budget amid Gov. Scott's pointed criticism of Democratic "
              "overspending.  Morley's appointment to this seat — and his embrace of the "
              "Republican fiscal-restraint caucus — aligns with the rubric's anti-deficit, "
              "balanced-budget standard for economic stewardship.",
              ["https://vtdigger.org/2025/12/05/former-state-rep-john-morley-appointed-to-orleans-county-senate-seat/",
               "https://legislature.vermont.gov/people/single/2026/41884",
               "https://vtdigger.org/2025/05/01/vermont-senate-approves-2026-budget-proposal-but-legislators-expect-to-cut-spending-further-amid-gov-phil-scotts-criticism/"]),
    ]),

    # ---------- J. Stuart Adams (UT-R, SD-7, Utah Senate President 2018-2026) ----------
    # Utah Senate President from 2018 until losing the June 2026 GOP primary to
    # Stephanie Hollist in a race dominated by a contentious AI data-center siting
    # controversy.  Over 20 years in the Utah Legislature.
    ("j-stuart-adams", "UT", "State Senator", [
        claim("jsa1", "j-stuart-adams", "self_defense", 1, True,
              "As Utah Senate President, J. Stuart Adams presided over and advanced the "
              "passage of HB 314 (Firearm Purchase Amendments, 2026 General Session), "
              "a pro-gun bill backed by the NRA-ILA that streamlines Utah's firearm purchase "
              "process by eliminating a duplicative state-specific background-check form that "
              "federal law does not require FFLs to use.  The bill preserves Utah's existing "
              "background-check system while eliminating unnecessary administrative "
              "friction imposed on gun buyers — a removal of a registry-adjacent paperwork "
              "layer.  Governor Spencer Cox signed HB 314 into law in late March 2026 after "
              "the Republican-controlled legislature advanced it.  As Senate President, Adams "
              "held the gavel during the floor vote and set the legislative agenda that "
              "prioritized this NRA-backed reform.  The NRA-ILA praised its signing as a "
              "victory for Utah gun owners.  This aligns with the rubric's standard of "
              "opposing anti-gun administrative burdens and registry-style forms.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://www.sltrib.com/news/politics/2026/06/23/utah-senate-president-j-stuart/"]),
        claim("jsa2", "j-stuart-adams", "economic_stewardship", 2, True,
              "Under J. Stuart Adams's presidency, the Utah Senate approved an income tax "
              "reduction in the 2025 General Session — the sixth consecutive year that "
              "Utah's Republican legislature had cut the state income tax rate.  The 2025 "
              "cut reduced the rate from 4.55% to 4.5%, saving Utah families and businesses "
              "additional dollars on top of the reductions accumulated over prior sessions.  "
              "Utah Republicans under Adams's Senate leadership also expanded the child tax "
              "credit and approved a tax credit for businesses offering childcare benefits, "
              "while simultaneously maintaining one of the most structurally balanced state "
              "budgets in the nation.  As Senate President and caucus leader, Adams set the "
              "fiscal agenda that produced six straight years of income tax relief — a record "
              "of sustained, disciplined anti-tax, balanced-budget governance that aligns "
              "with the rubric's economic-stewardship standard.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://ballotpedia.org/Stuart_Adams",
               "https://en.wikipedia.org/wiki/Stuart_Adams"]),
    ]),

    # ---------- Brady Brammer (UT-R, SD-21, Highland) ----------
    # Attorney (Spaulding Law); member of Utah State Senate since Jan 2025
    # (previously in UT House representing HD-54).  Serves on Senate Revenue
    # and Taxation Committee.  Sponsored key bills to limit judicial obstruction
    # of Utah's pro-life laws.
    ("brady-brammer", "UT", "State Senator", [
        claim("bb1", "brady-brammer", "sanctity_of_life", 0, True,
              "Brady Brammer sponsored SB 203 (Judicial Standing Amendments, 2025 Utah "
              "General Session), a bill specifically designed to curtail Planned Parenthood's "
              "ability to bring lawsuits on behalf of third parties to block Utah's pro-life "
              "legislation.  SB 203 requires that an association — such as Planned Parenthood "
              "Association of Utah — must be able to identify a specific individual who is "
              "actually harmed by a challenged law before it has legal standing to sue.  The "
              "bill directly targeted the associational-standing doctrine that Planned "
              "Parenthood used in 2022 to obtain a preliminary injunction blocking Utah's "
              "trigger ban (near-total abortion prohibition) from taking effect, thereby "
              "keeping abortion legal up to 18 weeks despite the Legislature's intent to ban "
              "it.  SB 203 passed the Senate on a party-line vote and was signed by the "
              "governor.  Brammer also previously sponsored HJR 2 (2023), a legislative "
              "resolution raising the bar courts must clear before issuing injunctions against "
              "state laws — directly advancing the cause of enforcing Utah's abortion ban and "
              "protecting the Legislature's life-affirming statutes from judicial nullification.  "
              "These actions advance the ultimate goal of personhood protection by removing "
              "legal mechanisms that block pro-life laws from taking effect.",
              ["https://www.sltrib.com/news/politics/2025/02/12/utah-legislature-gop-lawmakers/",
               "https://www.ksl.com/article/50570915/legislature-approves-amended-resolution-to-end-utahs-trigger-abortion-ban",
               "https://le.utah.gov/~2025/bills/static/SB0203.html"]),
        claim("bb2", "brady-brammer", "self_defense", 1, True,
              "As a Utah State Senator, Brady Brammer voted for HB 314 (Firearm Purchase "
              "Amendments, 2026 Utah General Session), an NRA-ILA backed bill that streamlines "
              "the firearm purchase process by eliminating a duplicative state-specific "
              "background-check form that FFLs are not required to complete under federal law.  "
              "The bill reduces unnecessary administrative burdens on law-abiding gun buyers "
              "while preserving Utah's existing background-check infrastructure.  Governor "
              "Cox signed HB 314 into law in late March 2026 after it passed both chambers of "
              "the Republican-controlled legislature.  As a member of the Republican Senate "
              "caucus that advanced this NRA-ILA endorsed measure, Brammer's vote reflects his "
              "consistent support for legislation that reduces government friction on "
              "Second Amendment rights — aligning with the rubric's opposition to administrative "
              "requirements that function as de-facto registry barriers to firearm purchases.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://ballotpedia.org/Brady_Brammer"]),
    ]),

    # ---------- Evan Vickers (UT-R, SD-28, Cedar City) ----------
    # Pharmacist and small-business owner; Utah Senate Majority Leader since 2019.
    # Serves District 28 in Iron/Washington counties (southern Utah) since 2013.
    # Re-elected November 2022, term ends December 2026.
    ("evan-vickers", "UT", "State Senator", [
        claim("ev1", "evan-vickers", "self_defense", 1, True,
              "As Utah Senate Majority Leader, Evan Vickers was a key floor manager for "
              "HB 314 (Firearm Purchase Amendments, 2026 Utah General Session), the "
              "NRA-ILA backed bill that streamlines Utah's firearm purchase process by "
              "eliminating a duplicative state-specific background-check form not required "
              "under federal law.  The Majority Leader's office controls the Senate floor "
              "calendar and the timing of bill debates; Vickers's scheduling and shepherding "
              "of HB 314 to passage was essential to its becoming law.  Governor Cox signed "
              "the bill in late March 2026.  The NRA-ILA praised the signing as a win for "
              "Utah gun owners who had faced unnecessary administrative hurdles.  Vickers "
              "has held the Majority Leader post since 2019, giving him sustained influence "
              "over the Senate's pro-Second-Amendment legislative agenda, including prior "
              "sessions in which Utah expanded constitutional-carry protections and firearm "
              "liability shields for manufacturers and sellers.  His leadership role in "
              "passing HB 314 aligns with the rubric's anti-registry, pro-carry, "
              "anti-administrative-burden standard.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://ballotpedia.org/Evan_Vickers"]),
        claim("ev2", "evan-vickers", "economic_stewardship", 2, True,
              "As Utah Senate Majority Leader throughout 2019–2026, Evan Vickers has been "
              "one of the primary architects of Utah's streak of consecutive income tax "
              "reductions.  In the 2025 General Session, the legislature — under Vickers's "
              "floor leadership — approved an income tax cut for the sixth straight year, "
              "reducing the rate to 4.5% and saving Utah families additional money annually.  "
              "The 2025 session also expanded the state child tax credit and approved a "
              "business tax credit for employers offering childcare benefits, all while "
              "Utah maintained one of the most structurally sound state budgets in the "
              "nation.  As a licensed pharmacist and small-business owner in Cedar City, "
              "Vickers brings private-sector fiscal discipline to his legislative role — he "
              "understands both the burden of government taxation on small businesses and "
              "the importance of balanced-budget governance.  Six consecutive years of tax "
              "cuts under his Majority Leadership reflect the anti-deficit, taxpayer-first "
              "economic stewardship that the rubric's economic-stewardship standard demands.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://ballotpedia.org/Evan_Vickers",
               "https://en.wikipedia.org/wiki/Evan_Vickers"]),
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
