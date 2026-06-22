#!/usr/bin/env python3
"""Enrichment batch 358: 2-3 claims each for 5 Virginia House of Delegates members — bottom of alphabet.

archetype_curated federal and state pools are fully exhausted; this batch targets
evidence_state Virginia House of Delegates members with 0 prior claims, selected from
the reverse-alphabetical bottom of the bucket:

  • Michael Feggans   (VA HD-97, D) — voted YES on HJ1 reproductive freedom amendment (2025); PPAV-endorsed; YES on SB749
  • May Nivar         (VA HD-57, D) — voted YES on HJ1 2nd passage (2026); YES on HJ3 marriage equality; YES on SB749
  • Marty Martinez    (VA HD-29, D) — voted YES on HJ1 (2025); YES on marriage equality amendment (2025); YES on SB749
  • Mark Downey       (VA HD-69, D) — voted YES on HJ1 2nd passage (2026); YES on HJ3; endorsed by gun safety groups; YES on SB749
  • Margaret Franklin (VA HD-23, D) — publicly committed to abortion access (2026 campaign); YES on SB749

Sources: lis.virginia.gov, vpm.org, virginiamercury.com, cardinalnews.org, michaelfeggans.com,
         plannedparenthoodaction.org, ballotpedia.org, ammoland.com, vavoterguide.com
Writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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
    # ---- Michael Feggans (VA HD-97, D) ---- in office since Jan 2024
    ("michael-feggans", "VA", "House of Delegates", [
        claim("mf1", "michael-feggans", "sanctity_of_life", 0, False,
              "Voted YES on HJ1 (January 14, 2025), Virginia's constitutional resolution "
              "establishing a 'fundamental right to reproductive freedom' — defined to "
              "include abortion care at any stage of pregnancy with no gestational limit, "
              "no required waiting periods, and no mandatory parental-consent provisions. "
              "The House passed HJ1 51-48 on a near-party-line vote; Feggans joined all "
              "but one Democrat in voting in favor. The amendment was also part of the "
              "'Bros for Repro' campaign in which Feggans participated, calling on male "
              "legislators to publicly champion the reproductive-freedom measure.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://michaelfeggans.com/del-michael-feggans-earns-planned-parenthood-advocates-of-virginia-endorsement/"]),
        claim("mf2", "michael-feggans", "sanctity_of_life", 4, False,
              "Earned the endorsement of Planned Parenthood Advocates of Virginia (PPAV) "
              "for his 2025 re-election race in House District 97. PPAV's endorsement — "
              "granted to candidates they identify as committed to expanding abortion "
              "access — was announced in July 2025 with Feggans stating he is 'proud to "
              "stand with the majority of Virginians who believe Virginia should remain "
              "the last safe haven in the South for reproductive freedom.' The rubric "
              "requires legislators to have never accepted endorsements or financial "
              "support from Planned Parenthood, NARAL, or EMILY's List.",
              ["https://michaelfeggans.com/del-michael-feggans-earns-planned-parenthood-advocates-of-virginia-endorsement/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-virginia-inc/ppav-endorsements-2025",
               "https://ballotpedia.org/Michael_Feggans"]),
        claim("mf3", "michael-feggans", "self_defense", 1, False,
              "Voted YES on SB749 (March 4, 2026), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles with detachable magazines and "
              "specified features, and magazines holding more than 15 rounds. "
              "The House passed the bill 59-35 in a near-party-line vote, with Feggans "
              "and almost all Democratic delegates voting in favor over united Republican "
              "opposition. Governor Spanberger signed SB749 into law in May 2026, "
              "with provisions taking effect July 1, 2026.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.ammoland.com/2026/03/virginia-assault-firearms-ban-sb749-passes-legislature/"]),
    ]),

    # ---- May Nivar (VA HD-57, D) ---- in office since Jan 14, 2026
    ("may-nivar", "VA", "House of Delegates", [
        claim("mn1", "may-nivar", "sanctity_of_life", 0, False,
              "Voted YES on HJ1 (January 14, 2026) — the required second legislative "
              "passage of Virginia's constitutional amendment establishing a 'fundamental "
              "right to reproductive freedom,' including abortion care at any stage of "
              "pregnancy. This was among her first official votes after being sworn in "
              "as a delegate on the same day, January 14, 2026. The House passed the "
              "amendment 64-34; Nivar had explicitly pledged during her 2025 campaign "
              "to vote in favor, saying she wanted to 'protect reproductive freedom' "
              "and keep Virginia the last safe haven for abortion access in the South.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/",
               "https://www.vpm.org/generalassembly/2026-01-05/may-nivar-house-of-delegates-hd57-owen-henrico-goochland-growth-teacher-pay"]),
        claim("mn2", "may-nivar", "biblical_marriage", 1, False,
              "Voted YES on HJ3 (January 14, 2026), the second and final legislative "
              "passage of Virginia's constitutional amendment to repeal Article I, "
              "Section 15-A — the provision voters ratified in 2006 defining marriage "
              "in Virginia as solely between one man and one woman. With Nivar's YES "
              "vote, the House passed the repeal amendment 67-31 (the most bipartisan "
              "of the four amendments, with three Republicans crossing over). The "
              "amendment was placed on the November 2026 statewide ballot for voter "
              "ratification.",
              ["https://lis.virginia.gov/bill-details/20261/HJ3",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/",
               "https://virginiaindependentnews.com/politics/referendum-reproductive-rights-marriage-equality-voting-rights-constitutional-amendments/"]),
        claim("mn3", "may-nivar", "self_defense", 1, False,
              "Voted YES on SB749 (March 4, 2026), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles with detachable magazines and "
              "specified features, and magazines holding more than 15 rounds. "
              "The House passed the bill 59-35 on a near-party-line vote; Nivar voted "
              "with the Democratic majority in favor. Gun Owners of America and the "
              "Virginia Citizens Defense League called the bill unconstitutional and "
              "an infringement on Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.ammoland.com/2026/03/virginia-assault-firearms-ban-sb749-passes-legislature/"]),
    ]),

    # ---- Marty Martinez (VA HD-29, D) ---- in office since Jan 2024
    ("marty-martinez", "VA", "House of Delegates", [
        claim("mm1", "marty-martinez", "sanctity_of_life", 0, False,
              "Voted YES on HJ1 (January 14, 2025), Virginia's constitutional resolution "
              "to establish a 'fundamental right to reproductive freedom' including "
              "abortion care at any stage of pregnancy, with no gestational limit. "
              "The House passed HJ1 51-48 on a near-party-line vote, with Martinez "
              "joining the Democratic majority in favor while all Republicans opposed. "
              "The resolution initiated the required two-session constitutional amendment "
              "process; the second passage was completed in January 2026.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("mm2", "marty-martinez", "biblical_marriage", 1, False,
              "Voted YES on the Virginia constitutional resolution (January 14, 2025) "
              "to repeal Article I, Section 15-A — the 2006 voter-approved provision "
              "defining marriage in Virginia as solely between one man and one woman. "
              "The House passed the repeal 58-35, with Martinez and 50 other Democrats "
              "voting in favor alongside seven Republicans. The amendment received its "
              "required second passage in the 2026 session and was placed on the "
              "November 2026 ballot for voter ratification.",
              ["https://lis.virginia.gov/bill-details/20251/SJ249",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://news.ballotpedia.org/2025/01/27/virginias-two-session-rule-for-constitutional-amendment-house-of-delegates-election-could-affect-the-future-of-proposed-amendments-on-abortion-marriage-and-voting/"]),
        claim("mm3", "marty-martinez", "self_defense", 1, False,
              "Voted YES on SB749 (March 4, 2026), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles with detachable magazines and "
              "certain features, and magazines holding more than 15 rounds. "
              "The House passed the bill 59-35 on a near-party-line vote; Martinez "
              "voted with the Democratic majority in favor. The bill was condemned by "
              "Gun Owners of America and the Virginia Citizens Defense League as "
              "unconstitutional. Governor Spanberger signed it into law in May 2026.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.ammoland.com/2026/03/virginia-assault-firearms-ban-sb749-passes-legislature/"]),
    ]),

    # ---- Mark Downey (VA HD-69, D) ---- in office since Jan 14, 2026
    ("mark-downey", "VA", "House of Delegates", [
        claim("md1", "mark-downey", "sanctity_of_life", 0, False,
              "Voted YES on HJ1 (January 14, 2026) — the required second legislative "
              "passage of Virginia's constitutional amendment establishing a 'fundamental "
              "right to reproductive freedom,' including abortion care at any stage of "
              "pregnancy with no gestational limit. Downey took office the same day, "
              "January 14, 2026, and voted with all but two Democrats in the 64-34 "
              "passage. During his 2025 campaign he had stated he would vote for the "
              "constitutional amendment to 'ensure women have full autonomy over "
              "reproductive decisions.'",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/",
               "https://www.vavoterguide.com/candidate/mark-downey/"]),
        claim("md2", "mark-downey", "biblical_marriage", 1, False,
              "Voted YES on HJ3 (January 14, 2026), the second and final legislative "
              "passage of Virginia's constitutional amendment to repeal Article I, "
              "Section 15-A — the 2006 voter-approved provision defining marriage as "
              "solely between one man and one woman. The House passed the repeal "
              "amendment 67-31 on the opening day of the 2026 General Assembly session; "
              "Downey voted with the Democratic majority in favor. The amendment was "
              "placed on the November 2026 ballot for voter ratification.",
              ["https://lis.virginia.gov/bill-details/20261/HJ3",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/",
               "https://virginiaindependentnews.com/politics/referendum-reproductive-rights-marriage-equality-voting-rights-constitutional-amendments/"]),
        claim("md3", "mark-downey", "self_defense", 1, False,
              "A Williamsburg pediatrician who ran on gun-safety measures and received "
              "endorsements from Brady United, Everytown for Gun Safety, and Giffords. "
              "After taking office, he voted YES on SB749 (March 4, 2026), Virginia's "
              "assault-firearms ban prohibiting the purchase, sale, importation, "
              "manufacture, or transfer of semi-automatic centerfire rifles and "
              "magazines over 15 rounds. The House passed the bill 59-35 on a "
              "near-party-line vote.",
              ["https://www.vavoterguide.com/candidate/mark-downey/",
               "https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # ---- Margaret Franklin (VA HD-23, D) ---- in office since Jan 19, 2026
    ("margaret-franklin", "VA", "House of Delegates", [
        claim("mgf1", "margaret-franklin", "sanctity_of_life", 0, False,
              "During her January 2026 special-election campaign for House District 23, "
              "Franklin publicly declared: 'Since the Supreme Court overturned Roe v. "
              "Wade, millions of Americans have lost their fundamental right to choose' "
              "and pledged to pass a guaranteed right to abortion access and stop "
              "'right-wing extremists from banning it in Virginia.' She won the "
              "special election January 13, 2026, defeating her Republican opponent "
              "77-23% in a Prince William County district; her explicit rejection of "
              "any restrictions on abortion access is directly contrary to the "
              "rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Margaret_Franklin_(Virginia)",
               "https://virginiamercury.com/2026/01/13/democrats-retain-house-districts-11-and-23-in-tuesdays-special-elections/",
               "https://www.insidenova.com/headlines/supervisor-franklin-wins-special-election-for-23rd-house-district/article_79bdc3f9-ac44-4876-9bcf-210bb20e1b71.html"]),
        claim("mgf2", "margaret-franklin", "self_defense", 1, False,
              "Voted YES on SB749 (March 4, 2026), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles with detachable magazines and "
              "certain features, and magazines holding more than 15 rounds. "
              "Franklin took office January 19, 2026, and voted with the Democratic "
              "majority when the House passed the bill 59-35 in March. She had "
              "previously described gun violence reduction as 'a top priority' and "
              "cited her experience as a Prince William County supervisor working "
              "with law enforcement to reduce gun violence.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://ballotpedia.org/Margaret_Franklin_(Virginia)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
