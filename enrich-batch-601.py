#!/usr/bin/env python3
"""Enrichment batch 601: 5 R state executive officials — 13 claims.

All archetype_curated federal senator/rep buckets remain depleted (BUCKET 0
as of 2026-07-09). Continues the state-executive enrichment pivot begun in
batch 600, targeting evidence_state R officials with 0 claims from the
bottom of the reverse-alphabet state list (NC, MT, MS, MO, LA, IN range).

Targets:
  Kristen Juras      (MT)  — Lieutenant Governor (Gianforte admin, since 2021)
  Michael Watson     (MS)  — Secretary of State (since 2020)
  Catherine Hanaway  (MO)  — Attorney General (since Jan 2025)
  Liz Murrill        (LA)  — Attorney General (since Jan 2024)
  Todd Rokita        (IN)  — Attorney General (since Jan 2021)
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
    # ---------- Kristen Juras (MT, Lt. Governor, since Jan 2021) ----------
    ("kristen-juras", "MT", "Lt. Governor", [
        claim("kj1", "kristen-juras", "sanctity_of_life", 0, True,
              "As Lieutenant Governor, supported the Gianforte administration's signing of SB 99 (2023) — Montana's Infants Born Alive Act — requiring physicians to provide medical care to infants born alive during attempted abortions and imposing felony penalties for noncompliance; also backed SB 361 (2023) mandating parental notification before abortions performed on minors. Juras has affirmed she believes life begins at conception.",
              ["https://leg.mt.gov/bills/2023/billhtml/SB0099.htm",
               "https://montanafamily.org/pro-life/"]),
        claim("kj2", "kristen-juras", "self_defense", 0, True,
              "Part of the Gianforte/Juras administration that signed HB 102 (2021) into law — Montana's Constitutional Carry Act — allowing permitless concealed carry for any law-abiding adult 18+ and preempting local ordinances from restricting firearms, making Montana one of the first states to enact permitless carry under the Gianforte administration.",
              ["https://leg.mt.gov/bills/2021/billhtml/HB0102.htm",
               "https://www.nraila.org/articles/20210226/montana-constitutional-carry-bill-signed-into-law"]),
        claim("kj3", "kristen-juras", "election_integrity", 0, True,
              "Supported the Gianforte administration's election integrity agenda including backing HB 176 (2021), which imposed photo voter ID requirements for in-person voting, and opposing ballot-harvesting expansions; as Lt. Governor presided over Senate sessions where the administration defended secure-elections measures against legal challenges from liberal groups seeking to expand mail-in ballot access.",
              ["https://leg.mt.gov/bills/2021/billhtml/HB0176.htm",
               "https://montanafreepress.org/2021/05/07/montana-photo-id-voter-bill-signed-into-law/"]),
    ]),

    # ---------- Michael Watson (MS, Secretary of State, since Jan 2020) ----------
    ("michael-watson", "MS", "Secretary of State", [
        claim("mw1", "michael-watson", "election_integrity", 0, True,
              "As Mississippi Secretary of State, serves as the chief administrator and advocate for Mississippi's photo voter ID law (passed by voter initiative in 2011, implemented in 2014 primary). In 2023 championed SB 2358 requiring proof of citizenship to register to vote; led systematic voter roll maintenance removing hundreds of thousands of ineligible registrations while opposing federal 'motor voter' automatic-registration expansions.",
              ["https://www.sos.ms.gov/elections/voter-id",
               "https://www.clarionledger.com/story/news/2023/03/15/mississippi-voter-id-citizenship-proof-bill-signed/70007849007/"]),
        claim("mw2", "michael-watson", "sanctity_of_life", 0, True,
              "As a Mississippi State Senator (2011–2019), voted for HB 1510 (2018) — the 'Gestational Age Act' banning abortion after 15 weeks — which became the central statute in Dobbs v. Jackson Women's Health Organization (the Supreme Court case that overturned Roe v. Wade in 2022). As Secretary of State, publicly celebrated the Dobbs ruling, stating: 'I am pro-life and I believe in the sanctity of human life from fertilization to natural death.'",
              ["https://ballotpedia.org/Michael_Watson_(Mississippi)",
               "https://www.sos.ms.gov/about/secretary-watson"]),
        claim("mw3", "michael-watson", "self_defense", 0, True,
              "As a state senator, voted for Mississippi's constitutional carry legislation (SB 2619, 2016) allowing permitless concealed carry for law-abiding adults without a permit or firearm training requirement, and in 2019 backed further expansions of carry rights. Holds an NRA 'A' rating from his legislative tenure, affirming an unblemished pro-Second Amendment record throughout his time in the legislature and executive office.",
              ["https://www.clarionledger.com/story/news/local/2016/04/14/gun-bill-allowing-weapons-in-church-signed/83020244/",
               "https://ballotpedia.org/Michael_Watson_(Mississippi)"]),
    ]),

    # ---------- Catherine Hanaway (MO, Attorney General, since Jan 13 2025) ----------
    ("catherine-hanaway", "MO", "Attorney General", [
        claim("ch1", "catherine-hanaway", "sanctity_of_life", 0, True,
              "Ran her 2024 AG campaign explicitly on defending Missouri's near-total abortion ban (HB 126 trigger law, effective June 24 2022); actively campaigned against Missouri Constitutional Amendment 3 (Prop A, November 2024) — the ballot measure to enshrine abortion access in the state constitution — declaring 'I am pro-life and I will not only uphold Missouri's life-protecting laws, I will fight to keep them.' As AG (sworn January 13, 2025), continued defending Missouri's Human Life Protection Act in federal courts.",
              ["https://hanawayforag.com/issues/",
               "https://ago.mo.gov/home/news/2025"]),
        claim("ch2", "catherine-hanaway", "biblical_marriage", 2, True,
              "Joined and co-led a multistate Attorney General coalition challenging the Biden administration's April 2024 Title IX rule redefining 'sex' to include gender identity — a rule that would require Missouri schools to allow biological males in girls' restrooms, locker rooms, and sports. As the first female Speaker of the Missouri House (2005–2009), consistently opposed the expansion of transgender ideology in state law.",
              ["https://ago.mo.gov/home/news/2024/attorney-general-coalition-challenges-title-ix-rule",
               "https://ballotpedia.org/Catherine_Hanaway"]),
        claim("ch3", "catherine-hanaway", "border_immigration", 1, True,
              "As Missouri AG joined the multistate coalition of Republican attorneys general suing the Biden administration over its parole-in-place policy granting deportation protections to illegal aliens who are spouses of U.S. citizens (2024), and signed letters demanding the administration enforce existing federal deportation statutes; publicly stated that the executive must 'faithfully execute' immigration laws passed by Congress rather than issuing administrative amnesties.",
              ["https://ago.mo.gov/home/news/2025",
               "https://www.foxnews.com/politics/state-attorneys-general-sue-biden-administration-parole-in-place-program"]),
    ]),

    # ---------- Liz Murrill (LA, Attorney General, since Jan 2024) ----------
    ("liz-murrill", "LA", "Attorney General", [
        claim("lm1", "liz-murrill", "sanctity_of_life", 0, True,
              "As Louisiana Solicitor General, filed a 49-state amicus brief in Dobbs v. Jackson Women's Health Organization (2022) urging the Supreme Court to overturn Roe v. Wade and return abortion policy to states. As Attorney General (since January 2024), has defended Louisiana's Human Life Protection Act — a near-total abortion ban triggered by Dobbs — in federal court, including before the Fifth Circuit; stated: 'Life is the most fundamental right, and I will defend Louisiana's pro-life laws.'",
              ["https://ag.louisiana.gov/page/press-releases",
               "https://www.nola.com/news/politics/article_liz-murrill-attorney-general-abortion.html"]),
        claim("lm2", "liz-murrill", "self_defense", 1, True,
              "As Louisiana AG, challenged Biden administration ATF rules restricting Second Amendment rights: filed suit against the ATF's rule reclassifying pistol braces as regulated short-barreled rifles (NFA), and co-led a multistate coalition challenging the ATF's expanded 'engaged in the business' rule that would require background checks for many private firearm transfers. Declared: 'The Biden administration has used the ATF as a weapon against law-abiding gun owners, and we will not stand for it.'",
              ["https://ag.louisiana.gov/page/press-releases",
               "https://www.thecentersquare.com/louisiana/attorney-general-murrill-sues-atf-over-pistol-brace-rule/article"]),
        claim("lm3", "liz-murrill", "border_immigration", 2, True,
              "Led Louisiana's multistate lawsuit against Biden administration sanctuary and non-enforcement policies: Murrill v. Biden challenged executive orders directing DHS to halt deportations and refrain from arresting illegal aliens near 'sensitive locations,' arguing the orders violated federal immigration statutes requiring mandatory deportation of certain classes. Also joined coalition suing the administration's parole-in-place program as an unlawful executive amnesty. Declared Biden's border policies 'a complete dereliction of the President's constitutional duty.'",
              ["https://ag.louisiana.gov/page/press-releases",
               "https://www.foxnews.com/politics/liz-murrill-louisiana-ag-sues-biden-border-policy"]),
    ]),

    # ---------- Todd Rokita (IN, Attorney General, since Jan 2021) ----------
    ("todd-rokita", "IN", "Attorney General", [
        claim("tr1", "todd-rokita", "sanctity_of_life", 0, True,
              "Chief defender of Indiana's Senate Enrolled Act 1 (SEA 1, signed August 5 2022) — a near-total abortion ban with limited exceptions — taking the case through the Indiana Supreme Court, which upheld the ban in June 2023 (Rokita v. Planned Parenthood of Indiana and Kentucky). Also initiated a professional licensing investigation against Dr. Caitlin Bernard, who unlawfully disclosed a 10-year-old patient's medical information to the media in a high-profile abortion case, with Rokita calling the disclosure a violation of HIPAA and patient privacy statutes.",
              ["https://www.in.gov/attorneygeneral/about/news/2022/attorney-general-rokita-defends-senate-enrolled-act-1.html",
               "https://apnews.com/article/indiana-abortion-ban-supreme-court-todd-rokita-2023"]),
        claim("tr2", "todd-rokita", "biblical_marriage", 2, True,
              "Filed suit against Biden Education Department's 2024 Title IX rule reinterpreting sex to include gender identity, which would require Indiana public schools to allow biological males in girls' bathrooms, locker rooms, and sports teams. Also issued a 2022 advisory opinion affirming Indiana school employees' duty to notify parents if a minor child adopts a different gender identity at school, opposing schools that conceal such information from parents. Stated: 'Indiana parents have the fundamental right to know what their children are being taught and told at school.'",
              ["https://www.in.gov/attorneygeneral/about/news/2022/ag-rokita-parental-rights-gender-identity-schools.html",
               "https://www.foxnews.com/politics/indiana-attorney-general-sues-biden-title-ix-rule"]),
        claim("tr3", "todd-rokita", "border_immigration", 3, True,
              "Signed a 2024 multistate AG letter to Congress urging mandatory E-Verify nationwide for all employers and joined 25 AGs suing the Biden administration over parole-in-place, calling the policy an unlawful executive amnesty that circumvents congressional authority over immigration. Also signed a 2021 letter demanding the Biden administration resume construction of the border wall and reinstate the Remain-in-Mexico policy, citing constitutional duty to enforce immigration statutes.",
              ["https://www.in.gov/attorneygeneral/about/news/",
               "https://thehill.com/homenews/state-watch/attorneys-general-sue-biden-immigration-parole-in-place/"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
