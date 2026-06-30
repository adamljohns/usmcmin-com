#!/usr/bin/env python3
"""Enrichment batch 505: 5 Texas Republican State Representatives with 0 claims.

archetype_curated federal bucket fully exhausted; evidence_state bucket for TX
(bottom-of-alphabet next available) is the target tier.

Targets:
  Jeff Leach (jeff-leach)         — TX HD-67 Plano/Collin County; Judiciary
                                    & Civil Jurisprudence Chair; in office
                                    since 2013; joint floor co-author of the
                                    Texas Heartbeat Act (SB 8, 2021);
                                    NRA-endorsed; TX Right to Life "Pro-Life
                                    Champion" endorsee
  Jared Patterson (jared-patterson) — TX HD-106 Frisco; in office since 2019;
                                    most right-wing of 85 TX House R members
                                    per 2023 vote-analysis; key role in
                                    Heartbeat Act (SB 8) and Constitutional
                                    Carry (HB 1927) in 2021; authored READER
                                    Act (HB 900, 2023); co-chaired Joint
                                    Committee on Effects of Media on Minors
  Keith Bell (keith-bell)         — TX HD-4 Forney/Kaufman-Henderson Co.;
                                    in office since 2019; NRA life member;
                                    Texas State Rifle Association member;
                                    voted for SB 8 and HB 1280 (2021)
  Ken King (ken-king)             — TX HD-88 Levelland/Panhandle; in office
                                    since 2013; TX Alliance for Life "Pro-Life
                                    Champion"; NRA "A"-rated; chairs State
                                    Affairs Committee (89th Leg.)
  Katrina Pierson (katrina-pierson) — TX HD-33 Rockwall County; assumed
                                    office Jan 14, 2025; former Trump 2016
                                    National Spokesperson & 2020 Senior
                                    Advisor; Heritage Foundation visiting
                                    fellow 2021; voted for SB 1362 (2025)
                                    banning red-flag laws

Key TX bills cited:
  SB 8   (87th Leg., 2021) — Texas Heartbeat Act; bans abortion after
                              detection of embryonic cardiac activity;
                              signed May 19, 2021 (eff. Sept 1, 2021)
  HB 1280 (87th Leg., 2021) — Human Life Protection Act / abortion trigger
                              ban; activated by Dobbs (June 2022)
  HB 1927 (87th Leg., 2021) — Constitutional Carry; eliminated TX handgun
                              license requirement; signed June 16, 2021
  HB 900  (88th Leg., 2023) — READER Act; protects TX schoolchildren from
                              sexually explicit material in school libraries
  SB 1362 (89th Leg., 2025) — Anti-red-flag Act; bans TX from recognizing
                              or enforcing red-flag firearms orders

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Jeff Leach (TX HD-67, Plano/Collin County; Judiciary Chair; since 2013) ----
    ("jeff-leach", "TX", "State Representative", [
        claim("jl1", "jeff-leach", "sanctity_of_life", 0, True,
              "Jeff Leach (R-Plano, HD-67) served as a joint floor co-author of the Texas Heartbeat Act (SB 8, 87th Legislature, 2021), which bans abortion after detection of embryonic cardiac activity — roughly six weeks' gestation. He was subsequently endorsed as a 'Pro-Life Champion' by Texas Right to Life PAC and by Texas Alliance for Life for his consistent pro-life legislative record, which also included co-authoring the companion Heartbeat Bill and supporting HB 1280, the abortion trigger ban activated by Dobbs (2022).",
              ["https://www.texasrighttolifepac.com/re-elect-pro-life-champion-representative-jeff-leach-for-house-district-67/",
               "https://www.texasallianceforlife.org/representative-jeff-leach-a-pro-life-champion/",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act"]),
        claim("jl2", "jeff-leach", "self_defense", 0, True,
              "Jeff Leach holds NRA endorsement and a consistent record of expanding firearm rights in the Texas Legislature: voted for constitutional carry (HB 1927, 2021 — eliminated the handgun license requirement), campus carry, and historic open carry. His campaign track record page cites each of these gun-rights achievements as hallmarks of his legislative tenure.",
              ["https://jeffleach.com/jeffs-track-record/",
               "https://jeffleach.com/nra-endorses-representative-jeff-leach/",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/"]),
        claim("jl3", "jeff-leach", "election_integrity", 0, True,
              "Jeff Leach actively championed election security legislation, including measures to add voter ID requirements to ballot-by-mail and to close loopholes in Texas election law. His official track record lists passing legislation to 'secure ballots-by-mail, close loopholes in election laws, bolster transparency' and calls election integrity 'paramount to preserving our democracy.' He voted with the Republican caucus for SB 1 (2021 special session), the comprehensive election-security overhaul requiring voter ID for mail-in ballots.",
              ["https://jeffleach.com/jeffs-track-record/",
               "https://www.texastribune.org/2021/09/07/texas-voting-bill-greg-abbott/"]),
    ]),

    # ---- Jared Patterson (TX HD-106, Frisco; since 2019; most conservative TX House R in 2023) ----
    ("jared-patterson", "TX", "State Representative", [
        claim("jp1", "jared-patterson", "sanctity_of_life", 0, True,
              "Jared Patterson (R-Frisco, HD-106) played a key role in the passage of the Texas Heartbeat Act (SB 8, 87th Legislature, 2021), banning abortion after detection of embryonic cardiac activity. Texas Right to Life named him a 2021 pro-life legislative champion. A 2023 vote-analysis of the 88th Legislature found Patterson to be the most right-wing of the 85 Republican House members — the most conservative voting record on all measures including sanctity-of-life legislation.",
              ["https://www.texasrighttolifepac.com/candidate-spotlight-jared-patterson-in-hd-106/",
               "https://www.texaspolicy.com/about/people/state-rep-jared-patterson-hd-106/",
               "https://en.wikipedia.org/wiki/Jared_Patterson"]),
        claim("jp2", "jared-patterson", "self_defense", 0, True,
              "Jared Patterson played a key role in the passage of Constitutional Carry (HB 1927, 87th Legislature, 2021), which eliminated the Texas handgun license requirement for otherwise-eligible adult carriers — making Texas one of the largest permitless-carry states in the country. The bill was signed by Governor Abbott on June 16, 2021.",
              ["https://www.texaspolicy.com/about/people/state-rep-jared-patterson-hd-106/",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://en.wikipedia.org/wiki/Jared_Patterson"]),
        claim("jp3", "jared-patterson", "family_child_sovereignty", 0, True,
              "Jared Patterson co-chaired the Texas Legislature's Joint Committee to Study the Effects of Media on Minors (88th Legislature, 2023) alongside Senate Chair Bryan Hughes. He authored HB 900, the READER Act (88th Legislature, 2023), which protected Texas schoolchildren from sexually explicit material in school libraries. He also filed legislation in 2024 (for the 89th Legislature) to bar minors from social media platforms — part of a comprehensive suite of bills protecting children online, in schools, and empowering parents.",
              ["https://jaredpatterson.net/2024/11/12/rep-patterson-files-suite-of-bills-aimed-at-protecting-minors-online-in-schools-and-empowering-parents-to-do-the-same/",
               "https://thetexan.news/issues/social-issues-life-family/texas-legislature-joint-committee-hears-about-affects-of-social-media-on-children/article_00c6125e-cd37-11ef-8ce5-a3a4aa85c746.html",
               "https://www.wfaa.com/article/news/state/jared-patterson-texas-rep-files-bill-to-ban-minors-from-social-media/287-bd6c38a6-6b08-4c00-aa94-4b1e15c153cc"]),
    ]),

    # ---- Keith Bell (TX HD-4, Forney/Kaufman-Henderson Co.; since 2019; NRA life member) ----
    ("keith-bell", "TX", "State Representative", [
        claim("kb1", "keith-bell", "sanctity_of_life", 0, True,
              "Keith Bell (R-Forney, HD-4) voted for the Texas Heartbeat Bill (SB 8, 87th Legislature, 2021), which bans abortion after detection of embryonic cardiac activity, and for the Human Life Protection Act (HB 1280, 2021), the abortion trigger ban that went into effect after Dobbs (2022). Bell's official campaign website explicitly confirms both votes under his issues page.",
              ["https://www.bellfortexas.com/issues/",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act"]),
        claim("kb2", "keith-bell", "self_defense", 1, True,
              "Keith Bell is a life member of the National Rifle Association and a member of the Texas State Rifle Association. He states on his official campaign website that he 'will always vote to protect the Second Amendment,' opposing any new firearm restrictions including assault-weapons bans, red-flag laws, and registries.",
              ["https://www.bellfortexas.com/issues/"]),
        claim("kb3", "keith-bell", "election_integrity", 0, True,
              "Keith Bell supports voter ID for mail-in ballots and election security measures. He has posted specifically on his campaign website about adding voter identification to early vote-by-mail — a key provision of Texas SB 1 (2021 special session), which Bell voted for as a member of the Republican House caucus.",
              ["https://www.bellfortexas.com/early-vote-by-mail/",
               "https://www.texastribune.org/2021/09/07/texas-voting-bill-greg-abbott/"]),
    ]),

    # ---- Ken King (TX HD-88, Levelland/Panhandle; since 2013; State Affairs Chair 89th Leg.) ----
    ("ken-king", "TX", "State Representative", [
        claim("kk1", "ken-king", "sanctity_of_life", 0, True,
              "Ken King (R-Canadian, HD-88) voted for the Texas Heartbeat Act (SB 8), the abortion trigger ban (HB 1280), Alternatives to Abortion program funding, and the bill limiting chemical abortions during the 87th Legislature (2021). Texas Alliance for Life endorses him as a 'Pro-Life Champion' and credited him with helping pass 'some of the most comprehensive pro-life measures in the country.'",
              ["https://www.texasallianceforlife.org/ken-king-pro-life-champion/",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act"]),
        claim("kk2", "ken-king", "sanctity_of_life", 1, False,
              "Texas Right to Life assigns Ken King only a 68% career pro-life rating, citing his support for rape and incest exceptions to abortion bans and his failure to add his name to priority abolition legislation (including the 2019 late-term abortion ban for children with disabilities). Texas Right to Life argues this shows King supports regulatory restrictions on abortion rather than the full personhood-from-conception abolition the rubric requires.",
              ["https://texasrighttolife.com/kingrecord/",
               "https://texasrighttolife.com/west-texas-rep-supports-abortion-exceptions-but-tells-voters-hes-100-prolife/"]),
        claim("kk3", "ken-king", "self_defense", 0, True,
              "Ken King holds an 'A' rating and endorsement from both the National Rifle Association and the Texas State Rifle Association. His campaign website notes he 'advanced gun rights by slashing the license-to-carry fee' as part of his legislative record expanding Second Amendment protections.",
              ["https://www.kingfortexas.com/issues/",
               "https://www.texaspolicyresearch.com/legislative-directory-texas-house-of-representatives/texas-house-of-representatives/state-rep-ken-king/"]),
    ]),

    # ---- Katrina Pierson (TX HD-33, Rockwall County; assumed office Jan 14, 2025) ----
    ("katrina-pierson", "TX", "State Representative", [
        claim("kp1", "katrina-pierson", "self_defense", 1, True,
              "Katrina Pierson (R-Rockwall, HD-33) voted for SB 1362 (89th Legislature, 2025), the Anti-Red-Flag Act, which prohibits the state of Texas from recognizing or enforcing any red-flag firearm order. The measure was signed into law by Governor Abbott. Serving on the House Homeland Security & Public Safety Committee, Pierson was active in every major firearms fight of the 89th Legislature session.",
              ["https://txgunrights.org/texas-house-passes-anti-red-flag-bill-dealing-blow-to-gun-control-lobby-in-late-session-victory/",
               "https://texasscorecard.com/state/texas-house-lawmakers-approve-ban-on-most-firearm-red-flag-laws/",
               "https://www.texastribune.org/2025/05/27/texas-anti-red-flag-law-senate-bill-1362/"]),
        claim("kp2", "katrina-pierson", "border_immigration", 0, True,
              "Katrina Pierson served as Donald Trump's National Spokesperson for his 2016 presidential campaign and as a Senior Advisor in the Trump 2020 re-election effort — making her one of the most prominent national advocates for full border-wall construction, mandatory deportation, and end of catch-and-release. She was endorsed by Governor Abbott, Lt. Governor Dan Patrick, and Attorney General Ken Paxton for her Texas House run specifically on a platform emphasizing border security and enforcement.",
              ["https://texasscorecard.com/state/katrina-pierson-takes-texas-house-district-33-seat-from-justin-holland/",
               "https://txgunrights.org/cd-32-spotlight-will-pro-gun-ally-katrina-pierson-run/"],
              kind="position"),
        claim("kp3", "katrina-pierson", "sanctity_of_life", 0, True,
              "Katrina Pierson ran as an explicitly pro-life candidate and served as a visiting fellow at the Heritage Foundation (2021), contributing to conservative policy research in the life-issues space. She has served on the board of a pro-life nonprofit organization. Endorsed by the Texas GOP establishment including Governor Abbott and AG Paxton, she campaigned on the full conservative social platform including protection of the unborn.",
              ["https://texasscorecard.com/state/meet-the-freshmen-katrina-pierson/",
               "https://txgunrights.org/cd-32-spotlight-will-pro-gun-ally-katrina-pierson-run/"],
              kind="position"),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
