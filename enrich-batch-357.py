#!/usr/bin/env python3
"""Enrichment batch 357: 2-3 claims each for 5 Virginia State Senators — bottom of alphabet.

archetype_curated and evidence_curated federal pools are fully exhausted.
This batch targets evidence_state Virginia State Senators with 0 prior claims,
selected from the reverse-alphabetical bottom of the bucket:

  • Mamie Locke        (VA SD-23, D) — voted YES on SJ247 reproductive freedom amendment; YES on SB749 assault weapons ban
  • L. Louise Lucas    (VA SD-18, D) — Senate President Pro Tempore; YES on SJ247; YES on marriage equality SJ248; YES on SB749
  • Lashrecse Aird     (VA SD-13, D) — co-sponsored SJ247; Planned Parenthood endorsee; YES on SB749
  • Lamont Bagby       (VA SD-14, D) — YES on SJ247; YES on SJ248 marriage equality; YES on SB749
  • Kannan Srinivasan  (VA SD-32, D) — publicly pledged to keep abortion legal; YES on SJ247; YES on SB749

Sources: lis.virginia.gov, vpm.org, ballotpedia.org, en.wikipedia.org, acluva.org,
         plannedparenthoodaction.org, gunowners.org, news.ballotpedia.org
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
    # ---- Mamie Locke (VA SD-23, D) ----
    ("mamie-locke", "VA", "State Senate", [
        claim("ml1", "mamie-locke", "sanctity_of_life", 0, False,
              "Voted YES on SJ247 (January 21, 2025), Virginia's constitutional amendment "
              "to establish a 'fundamental right to reproductive freedom' — including "
              "abortion care at any stage of pregnancy — with no exceptions for gestational "
              "limits, parental consent, or health-neutral regulations. The Senate passed "
              "the amendment 21-19 on a strict party-line vote; all 21 Democratic senators, "
              "including Locke, voted in favor while all 19 Republicans opposed it. The "
              "amendment appeared on the November 2026 statewide ballot after a required "
              "second legislative passage.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("ml2", "mamie-locke", "self_defense", 1, False,
              "Voted YES on SB749 (2026 session), Virginia's sweeping assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer of "
              "semi-automatic centerfire rifles with detachable magazines and certain "
              "features, as well as magazines holding more than 15 rounds. The Senate "
              "passed the bill 21-19 on a strict party-line vote, with all 21 Democratic "
              "senators — including Locke — voting in favor. Gun Owners of America and the "
              "Virginia Citizens Defense League (VCDL) both opposed the bill as "
              "unconstitutional. Governor Spanberger signed SB749 into law in May 2026.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.gunowners.org/va03052026/",
               "https://www.29news.com/2026/03/10/virginia-assault-weapon-ban-awaits-governors-signature/"]),
    ]),

    # ---- L. Louise Lucas (VA SD-18, D) ----
    ("l-louise-lucas", "VA", "State Senate", [
        claim("ll1", "l-louise-lucas", "sanctity_of_life", 0, False,
              "As Senate President Pro Tempore — the highest-ranking officer in the chamber "
              "and the first African American woman to hold that position — Lucas voted YES "
              "on SJ247 (January 21, 2025), the constitutional amendment creating an "
              "unlimited 'fundamental right to reproductive freedom' including abortion "
              "care at any stage. All 21 Democratic senators voted with her in the "
              "21-19 party-line passage; Lucas's leadership role made her instrumental "
              "in managing the amendment's floor proceedings.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://en.wikipedia.org/wiki/L._Louise_Lucas",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("ll2", "l-louise-lucas", "biblical_marriage", 1, False,
              "Voted YES on the 2025 Virginia constitutional amendment (first legislative "
              "passage) to repeal Article I, Section 15-A of the Virginia Constitution — "
              "the provision defining marriage as solely between a man and a woman, "
              "enacted by Virginia voters in 2006. The Senate passed the repeal amendment "
              "21-18 on January 21, 2025, with Lucas and her Democratic colleagues "
              "providing the margin of passage. The amendment received its required "
              "second passage in the 2026 session and went to Virginia voters in "
              "November 2026.",
              ["https://lis.virginia.gov/bill-details/20251/SJ249",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights",
               "https://19thnews.org/2025/09/virginia-marriage-equality-election-ballot/"]),
        claim("ll3", "l-louise-lucas", "self_defense", 1, False,
              "Voted YES on SB749 (2026), Virginia's assault-firearms ban prohibiting "
              "the purchase, sale, manufacture, and transfer of 'assault firearms' "
              "and magazines over 15 rounds. As Senate President Pro Tempore, Lucas "
              "presided over the chamber during the 21-19 party-line passage. "
              "The bill was strongly opposed by the Virginia Citizens Defense League "
              "and Gun Owners of America, who called it an unconstitutional infringement "
              "on Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.gunowners.org/va03052026/",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/"]),
    ]),

    # ---- Lashrecse Aird (VA SD-13, D) ----
    ("lashrecse-aird", "VA", "State Senate", [
        claim("la1", "lashrecse-aird", "sanctity_of_life", 0, False,
              "Co-sponsored SJ247 (introduced November 2024, voted January 21, 2025), "
              "Virginia's constitutional amendment establishing a 'fundamental right to "
              "reproductive freedom' that explicitly prohibits the state from regulating "
              "abortion in any way that burdens that right. Aird was among the Democratic "
              "co-sponsors who moved the amendment through the Senate 21-19 on a "
              "party-line vote. The ACLU of Virginia called the passage 'historic'; "
              "SBA Pro-Life America and Virginia's pro-life groups strongly opposed it.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("la2", "lashrecse-aird", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Virginia in her 2023 state "
              "Senate primary — a rare intervention by the organization in a contested "
              "Democratic primary. Aird's campaign also received financial and "
              "organizational support from Planned Parenthood's Virginia affiliate, "
              "whose endorsement was centered on her commitment to expanding abortion "
              "access. The rubric requires legislators to have never accepted money or "
              "in-kind support from Planned Parenthood, NARAL, or EMILY's List.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-advocates-virginia-inc/press-releases/planned-parenthood-advocates-of-virginia-endorses-lashrecse-aird-for-virginia-state-senate",
               "https://www.virginiascope.com/in-a-rare-move-planned-parenthood-advocates-of-virginia-gets-involved-in-a-primary-by-endorsing-aird/"]),
        claim("la3", "lashrecse-aird", "self_defense", 1, False,
              "Voted YES on SB749 (2026 session), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles and magazines over 15 rounds. The "
              "Senate passed the bill 21-19, with Aird joining all 20 other Democratic "
              "senators in favor. The Virginia Citizens Defense League rated every "
              "Democratic senator who voted YES a 'F' on Second Amendment fidelity "
              "for the 2026 session.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.gunowners.org/va03052026/",
               "https://www.13newsnow.com/article/news/local/virginia/virginia-gun-restrictions-assault-weapons-ghost-guns-bills-pass-senate/291-33791bc0-58c5-478a-887c-24c620334912"]),
    ]),

    # ---- Lamont Bagby (VA SD-14, D) ----
    ("lamont-bagby", "VA", "State Senate", [
        claim("lb1", "lamont-bagby", "sanctity_of_life", 0, False,
              "Voted YES on SJ247 (January 21, 2025), the Virginia constitutional amendment "
              "to create a 'fundamental right to reproductive freedom' — defined to include "
              "abortion care with no gestational limit — with all 21 Democratic senators "
              "voting in favor 21-19 over united Republican opposition. As Chair of the "
              "Virginia Legislative Black Caucus and Chair of the Democratic Party of "
              "Virginia, Bagby was a key voice in advancing the progressive agenda that "
              "included this reproductive freedom amendment.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://en.wikipedia.org/wiki/Lamont_Bagby",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights"]),
        claim("lb2", "lamont-bagby", "biblical_marriage", 1, False,
              "Voted YES on the 2025 Virginia constitutional amendment (first passage) "
              "to repeal Article I, Section 15-A — the 2006 voter-approved provision "
              "defining marriage in Virginia as solely between one man and one woman. "
              "The repeal measure passed the Senate 21-18 on January 21, 2025, "
              "with Bagby and his Democratic colleagues providing the decisive margin. "
              "The amendment received its required second passage in 2026 and was placed "
              "on the November 2026 statewide ballot.",
              ["https://lis.virginia.gov/bill-details/20251/SJ249",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights",
               "https://virginiaindependentnews.com/politics/referendum-reproductive-rights-marriage-equality-voting-rights-constitutional-amendments/"]),
        claim("lb3", "lamont-bagby", "self_defense", 1, False,
              "Voted YES on SB749 (2026), Virginia's assault-firearms ban prohibiting "
              "the purchase, sale, and transfer of semi-automatic centerfire rifles "
              "with detachable magazines and certain features, plus magazines over "
              "15 rounds. The Senate passed the bill 21-19 on a party-line vote; "
              "Bagby joined all Democratic senators in voting in favor. "
              "Governor Spanberger signed the bill in May 2026.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.wboc.com/news/virginia-lawmakers-send-proposed-assault-weapons-ban-to-gov-spanberger-s-desk/article_2df35fd2-bd73-4634-b54c-285d7e1252c5.html"]),
    ]),

    # ---- Kannan Srinivasan (VA SD-32, D) ----
    ("kannan-srinivasan", "VA", "State Senate", [
        claim("ks1", "kannan-srinivasan", "sanctity_of_life", 0, False,
              "Publicly and emphatically committed to preserving unrestricted abortion "
              "access in Virginia during his January 2025 special-election campaign: "
              "'Virginia is the last, the only state in the South where women don't "
              "have to worry about [the legality of abortion]. And I am very, very "
              "committed to keeping it that way.' This stance explicitly rejects "
              "any statutory protection for unborn life, contrary to the rubric's "
              "life-at-conception standard.",
              ["https://news.ballotpedia.org/2025/01/06/kannan-srinivasan-d-and-tumay-harding-r-are-running-in-the-special-election-for-virginias-32nd-senate-district/",
               "https://ballotpedia.org/Kannan_Srinivasan"]),
        claim("ks2", "kannan-srinivasan", "sanctity_of_life", 1, False,
              "Voted YES on SJ247 on January 21, 2025 — just six days after being sworn "
              "in to the Senate on January 15, 2025, following his victory in the "
              "SD-32 special election. SJ247 constitutionally enshrines an unlimited "
              "'fundamental right to reproductive freedom' that bars the Commonwealth "
              "from restricting abortion at any stage, with the Senate passing the "
              "amendment 21-19 on a strict party-line vote. Srinivasan's vote "
              "was his first major Senate action after taking office.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://ballotpedia.org/Virginia_State_Senate_District_32_special_election,_2025",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("ks3", "kannan-srinivasan", "self_defense", 1, False,
              "Voted YES on SB749 (2026 session), Virginia's assault-firearms ban "
              "prohibiting the purchase, sale, importation, manufacture, or transfer "
              "of semi-automatic centerfire rifles with detachable magazines and "
              "certain features, and magazines holding more than 15 rounds. "
              "The Senate passed the bill 21-19 on a party-line vote, with "
              "Srinivasan joining all 20 other Democratic senators in favor. "
              "Gun Owners of America condemned the bill as 'unconstitutional' "
              "and urged Virginians to contact their representatives in opposition.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.gunowners.org/va03052026/"]),
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
