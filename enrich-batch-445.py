#!/usr/bin/env python3
"""Enrichment batch 445: 5 Washington state House Republicans (archetype_party_default, 0 claims).

Federal and evidence_state pools exhausted; continuing bottom-of-alphabet WA State
Representatives (the next unworked state in reverse-alphabetical order after WV batches).
All 5 are sitting 2025-session members with verified 2023-2026 votes and public statements.

Targets (all R):
  Tom Dent        (WA HD-13, District 13, since 2015)
  Peter Abbarno   (WA HD-20, District 20, since 2021 — House Republican Caucus Chair)
  Mike Volz       (WA HD-06, District 6, since 2017)
  Mary Dye        (WA HD-09, District 9, since 2015)
  Suzanne Schmidt (WA HD-04, District 4, since Jan 2023)

Key bills / measures used:
  - HB 1240 (2023 RS): WA state assault-weapons ban; final passage 56-42 (all Rs NAY, Apr 2023)
  - ESSB 5599 (2023 RS): Allowed shelters to house runaway minors seeking gender-affirming care
    without parental notification; passed 57-39 party-line (all Rs NAY, Apr 2023)
  - Initiative 2081 (passed legislature Mar 2024): Parents' Bill of Rights
  - IL26-638 / IL-26-001 (2026 citizen initiatives): Girls-sports + parental-rights restoration

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ---------------- Tom Dent (WA-13, R, State Representative, since 2015) ----------------
    ("tom-dent", "WA", "state representative", [
        claim("td1", "tom-dent", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, April 2023), Washington state's assault-weapons ban "
              "prohibiting the sale and import of semi-automatic rifles. Published a legislative newsletter "
              "titled 'Constitutional rights being threatened with gun bills, not too late to testify in the "
              "Senate,' urging his constituents to oppose the legislation before it reached the Senate — a "
              "direct defense of Second Amendment rights against the assault-weapons ban.",
              ["https://tomdent.houserepublicans.wa.gov/2023/03/22/rep-dents-legislative-update-constitutional-rights-being-threatened-with-gun-bills-not-too-late-to-testify-in-the-senate/",
               "https://legiscan.com/WA/votes/HB1240/2023"]),
        claim("td2", "tom-dent", "biblical_marriage", 2, True,
              "Voted against ESSB 5599 (passed 57-39 on a strict party-line vote, April 2023), the bill that "
              "authorized licensed youth shelters to house runaway minors seeking gender-affirming care — "
              "including hormone treatments — for an indefinite period without notifying their parents. All 39 "
              "NAY votes were cast by House Republicans. Dent, representing rural Central Washington (Grant, "
              "Kittitas, Adams, Douglas Counties), opposed the legislature's endorsement of gender-transition "
              "procedures for minors outside of parental authority.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023",
               "https://ballotpedia.org/Washington_Parental_Notification_Requirements_for_Homeless_and_Runaway_Youth_Seeking_Gender-Related_or_Reproductive_Health_Services_Referendum_(2023)"]),
    ]),

    # ---------------- Peter Abbarno (WA-20, R, State Representative, since 2021) ----------------
    ("peter-abbarno", "WA", "state representative", [
        claim("pa1", "peter-abbarno", "family_child_sovereignty", 0, True,
              "Publicly called for a NO vote on ESSB 5599 (April 2023), which allowed licensed youth shelters "
              "to house runaway minors seeking gender-affirming care indefinitely without parental notification. "
              "Proposed a parental-affirmation amendment on the House floor — requiring shelters to notify "
              "parents — which House Democrats voted down. In 2025, as House Republican Caucus Chair, issued a "
              "formal statement condemning Democrats for 'silencing debate' on Initiative 2081 (Parents' Bill "
              "of Rights) as Democrats dismantled it via HB 1296, removing parents' guaranteed right to access "
              "student medical records.",
              ["https://peterabbarno.houserepublicans.wa.gov/2023/04/20/rep-peter-abbarno-stands-up-for-parental-rights-urges-a-no-vote-on-senate-bill-5599/",
               "https://peterabbarno.houserepublicans.wa.gov/2025/04/14/rep-peter-abbarno-issues-statement-on-house-democrats-silencing-debate-on-parental-bill-of-rights-legislation/"]),
        claim("pa2", "peter-abbarno", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, April 2023), Washington's assault-weapons ban. "
              "In his March 2023 legislative update Abbarno stated 'Our state must prioritize victims over "
              "criminals and allow law-abiding citizens to protect themselves and their families from the rise "
              "in violent crime,' and in February 2024 published a statement defending 'the rights of "
              "law-abiding gun owners to protect themselves from criminals.'",
              ["https://peterabbarno.houserepublicans.wa.gov/2023/03/10/email-update-from-rep-peter-abbarno-prioritizing-criminals-over-victims-zoom-town-hall-meeting/",
               "https://peterabbarno.houserepublicans.wa.gov/2024/02/28/rep-peter-abbarno-defends-rights-of-law-abiding-gun-owners/",
               "https://legiscan.com/WA/votes/HB1240/2023"]),
        claim("pa3", "peter-abbarno", "biblical_marriage", 4, True,
              "As House Republican Caucus Chair, challenged House Democrats in April 2025 for silencing debate "
              "on Initiative 2081 amendments that would protect parents' rights to know what is taught in "
              "public schools. Opposed the Democrat majority's removal of the guarantee allowing parents to "
              "access student medical records and opt out of instruction conflicting with their values — "
              "framing the move as enabling ideological agendas, including LGBTQ content, in schools without "
              "parental knowledge or consent.",
              ["https://peterabbarno.houserepublicans.wa.gov/2025/04/14/rep-peter-abbarno-issues-statement-on-house-democrats-silencing-debate-on-parental-bill-of-rights-legislation/",
               "https://washingtonstatestandard.com/2025/09/08/new-wa-initiatives-seek-to-undo-rewrite-of-parental-rights-law-block-trans-girls-in-sports/"]),
    ]),

    # ---------------- Mike Volz (WA-06, R, State Representative, since 2017) ----------------
    ("mike-volz", "WA", "state representative", [
        claim("mv1", "mike-volz", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, April 2023), Washington's assault-weapons ban "
              "prohibiting the sale and import of semi-automatic rifles. Named in news coverage as one of the "
              "Spokane-area Republican representatives who unanimously opposed the ban; published a March 2023 "
              "alert titled 'Your opportunity to weigh in on gun bills' encouraging constituents to contact "
              "their Senators to oppose HB 1240 and HB 1143 (firearms safety training mandate).",
              ["https://www.spokesman.com/stories/2023/apr/19/assault-weapon-ban-on-sales-and-import-in-washington-heads-to-inslee-for-final-approval/",
               "https://mikevolz.houserepublicans.wa.gov/2023/03/22/your-opportunity-to-weigh-in-on-gun-bills-rep-mike-volz/"]),
        claim("mv2", "mike-volz", "family_child_sovereignty", 0, True,
              "Strongly supported Initiative 2081 (Parents' Bill of Rights), which passed the legislature in "
              "March 2024, stating 'No one is more important in a child's life than his or her parents' and "
              "emphasizing the initiative gives parents 'a stronger voice and presence in their children's "
              "education,' including rights to review instructional materials, inspect records, receive school "
              "notifications, and opt out of sexual-health instruction. In 2025 Volz offered an amendment to "
              "SSB 5181 to block Democrat attempts to weaken the initiative.",
              ["https://mikevolz.houserepublicans.wa.gov/2024/03/05/rep-volz-expresses-satisfaction-as-three-statewide-initiatives-pass-the-legislature/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5181&Year=2025"]),
    ]),

    # ---------------- Mary Dye (WA-09, R, State Representative, since 2015) ----------------
    ("mary-dye", "WA", "state representative", [
        claim("md1", "mary-dye", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, April 2023), Washington state's assault-weapons ban. "
              "Named in regional news coverage as one of the Eastern Washington Republican representatives who "
              "unanimously opposed the legislation. Dye has represented rural District 9 (Pomeroy area, "
              "Garfield and Asotin Counties) since 2015, consistently opposing state gun-control mandates.",
              ["https://www.spokesman.com/stories/2023/apr/19/assault-weapon-ban-on-sales-and-import-in-washington-heads-to-inslee-for-final-approval/",
               "https://legiscan.com/WA/votes/HB1240/2023"]),
        claim("md2", "mary-dye", "biblical_marriage", 2, True,
              "Supports IL26-638, the 2026 citizen initiative backed by Let's Go Washington (445,187 petition "
              "signatures) to block transgender girls from competing in girls' sports in Washington state, "
              "preserving biological-sex-based athletic competition. This initiative is in direct response to "
              "Democrat legislative action authorizing transgender participation in girls' sports — a policy "
              "Dye opposes as a rejection of biological sex distinctions.",
              ["https://marydye.houserepublicans.wa.gov/2026/03/23/rep-mary-dye-back-home-after-a-difficult-session-and-focused-on-what-comes-next/",
               "https://washingtonstatestandard.com/2026/01/03/signatures-filed-for-initiatives-on-parental-rights-blocking-trans-athletes-from-girls-sports/"]),
        claim("md3", "mary-dye", "family_child_sovereignty", 0, True,
              "Supports IL-26-001, the 2026 parental-rights restoration initiative (416,201 signatures) that "
              "would roll back HB 1296 — the 2025 Democrat bill that removed parents' guaranteed right to "
              "access their children's school medical records and gutted the voter-approved Initiative 2081 "
              "(Parents' Bill of Rights). Dye has framed the 2025 Democrat rollback as a direct attack on "
              "parental authority over their children's education and healthcare.",
              ["https://marydye.houserepublicans.wa.gov/2026/03/23/rep-mary-dye-back-home-after-a-difficult-session-and-focused-on-what-comes-next/",
               "https://washingtonstatestandard.com/2025/09/08/new-wa-initiatives-seek-to-undo-rewrite-of-parental-rights-law-block-trans-girls-in-sports/"]),
    ]),

    # ---------------- Suzanne Schmidt (WA-04, R, State Representative, since Jan 2023) ----------------
    ("suzanne-schmidt", "WA", "state representative", [
        claim("ss1", "suzanne-schmidt", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, April 2023), Washington's assault-weapons ban. "
              "Named in regional news coverage as one of the Spokane-area Republican representatives who "
              "unanimously opposed the legislation. Her campaign platform explicitly includes protecting First "
              "and Second Amendment rights, and she has opposed new gun-control mandates since taking office "
              "in January 2023.",
              ["https://www.spokesman.com/stories/2023/apr/19/assault-weapon-ban-on-sales-and-import-in-washington-heads-to-inslee-for-final-approval/",
               "https://ballotpedia.org/Suzanne_Schmidt"]),
        claim("ss2", "suzanne-schmidt", "family_child_sovereignty", 0, True,
              "Voted against ESSB 5599 (57-39 party-line, April 2023) and publicly objected to the bill, "
              "which allowed licensed youth shelters to house runaway minors seeking gender-affirming medical "
              "care indefinitely without notifying their parents. Described this work as 'fighting for parental "
              "rights' in her April 2023 legislative update, and in February 2025 raised alarm that Democrats "
              "were again 'threatening' Initiative 2081 (Parents' Bill of Rights) through procedural "
              "maneuvers.",
              ["https://suzanneschmidt.houserepublicans.wa.gov/2023/04/18/rep-suzanne-schmidts-legislative-update-my-first-bill-signed-into-law-governor-also-signs-senate-legislation-related-to-my-journey-level-electricians-house-bill-and-fighting-for-parental-rights/",
               "https://suzanneschmidt.houserepublicans.wa.gov/2025/02/14/rep-suzanne-schmidt-debate-rules-changed-parental-rights-initiative-threatened-bills-moving-through-the-process/"]),
        claim("ss3", "suzanne-schmidt", "biblical_marriage", 2, True,
              "Voted against ESSB 5599 (April 2023), the bill that formally authorized Washington state "
              "shelters to provide runaway minors with gender-affirming care — including hormone treatments — "
              "without parental knowledge or consent, embedding transgender-ideology medical practices into "
              "state youth-shelter policy. Opposed the 2025 Democrat effort to weaken Initiative 2081 "
              "guardrails that protect parents from school-based gender-ideology instruction without their "
              "consent.",
              ["https://suzanneschmidt.houserepublicans.wa.gov/2023/04/18/rep-suzanne-schmidts-legislative-update-my-first-bill-signed-into-law-governor-also-signs-senate-legislation-related-to-my-journey-level-electricians-house-bill-and-fighting-for-parental-rights/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
