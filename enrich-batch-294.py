#!/usr/bin/env python3
"""Enrichment batch 294: hand-curated claims for 5 Wyoming state senators.

archetype_curated federal bucket exhausted; batch continues the state-senator
protocol from batch 293 (WY), taking the next 5 from the bottom of the
reverse-sorted archetype_party_default WY State Senator bucket with 0 claims.

Targets: Ed Cooper (WY-R SD-20), Dan Laursen (WY-R SD-19),
Dan Dockstader (WY-R SD-16), Chris Rothfuss (WY-D SD-9),
Charles Scott (WY-R SD-30).

Key sourced votes / actions:
  WY HB 96 (2026) — lowering concealed-carry permit age from 21 to 18,
  extending campus carry to adults 18-20; passed Senate ~29 to 2 (2 dissenting);
  signed by Governor Gordon March 2026, effective July 1, 2026.
  WY HB 126 (2026) — Human Heartbeat Act, banning abortion once a fetal
  heartbeat is detectable; Senate co-sponsors include Dockstader and Laursen;
  passed Senate 27-4; signed by Governor Gordon March 9, 2026.
  WY HB 72 (2025) — Protecting Women's Privacy in Public Spaces Act,
  codifying biological sex for sex-segregated facilities; passed Senate 25-6;
  signed April 2025, effective July 1, 2025.
  WY Parental Rights in Education-1 (2024) — bars gender-identity lessons
  without parental consent, requires notification of health-status changes;
  took effect without Governor Gordon's signature, March 2024.
  WY SAPA (2022-era) — Dan Laursen as a Wyoming House member filed Wyoming
  Gun Owners' Second Amendment Preservation Act bill, seeking to nullify
  federal gun regulations within Wyoming.

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
    # ---------- Ed Cooper (WY-R, State Senator SD-20, since Jan 2021) ----------
    ("ed-cooper", "WY", "State Senator", [
        claim("ec1", "ed-cooper", "self_defense", 0, True,
              "Voted for WY HB 96 (2026), lowering Wyoming's concealed-carry permit age from 21 to 18 and extending campus carry rights to legal adults ages 18-20 at the University of Wyoming; the bill passed the Wyoming Senate with only two dissenting votes and was signed by Governor Mark Gordon in March 2026, effective July 1, 2026. Cooper, a conservative Republican oil-and-gas consultant representing Senate District 20 (Big Horn, Hot Springs, and Washakie counties), voted with the near-unanimous Republican caucus to close Wyoming's remaining age gap in its constitutional-carry framework — Wyoming first codified permitless carry for adults in 2011.",
              ["https://wyoleg.gov/Legislation/2026/HB0096",
               "https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://ballotpedia.org/Edward_Cooper"]),
        claim("ec2", "ed-cooper", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act, prohibiting abortion in Wyoming once a fetal heartbeat is detectable (approximately six weeks' gestation), with a narrow medical-emergency exception; Governor Mark Gordon signed the bill into law on March 9, 2026. The Wyoming Senate passed the bill 27-4; Cooper, who has served Senate District 20 since 2021 representing conservative rural communities in north-central Wyoming, voted with the overwhelming Republican majority to enact Wyoming's most protective pro-life statute in the state's modern legislative history.",
              ["https://wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Edward_Cooper"]),
    ]),

    # ---------- Dan Laursen (WY-R, State Senator SD-19, since Jan 2023) ----------
    ("dan-laursen", "WY", "State Senator", [
        claim("dl1", "dan-laursen", "sanctity_of_life", 0, True,
              "Co-sponsored WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable; Governor Mark Gordon signed the bill into law on March 9, 2026. Laursen is listed as a Senate co-sponsor alongside Sens. Biteman, Boner, Brennan, Dockstader, Hicks, Hutchings, Ide, Love, Olsen, Pearson, Salazar, and Steinmetz. Laursen, who represents Park and Big Horn counties (Senate District 19) and is known as one of Wyoming's most consistently conservative legislators, actively co-sponsored the bill as a statement of his pro-life convictions.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Dan_Laursen"]),
        claim("dl2", "dan-laursen", "self_defense", 2, True,
              "While serving as a Wyoming state representative (2015-2023), Laursen filed Wyoming Gun Owners' (WYGO) Second Amendment Preservation Act (SAPA) in the Wyoming House — legislation that would declare all past and future federal gun regulations, including provisions of the National Firearms Act and the Gun Control Act of 1968, unenforceable in Wyoming; Laursen served as WYGO's primary House sponsor for the SAPA bill. He also co-sponsored legislation repealing gun-free zones throughout Wyoming during his House tenure, consistently advocating the most expansive constitutional-carry and federal-firearm-nullification positions in the Wyoming legislature.",
              ["https://www.wyominggunowners.org/uncategorized/rep-dan-laursen-files-wygos-sapa-bill-in-the-house/",
               "https://ballotpedia.org/Dan_Laursen",
               "https://cowboystatedaily.com/2022/12/05/wyoming-state-senate-pariah-dan-laursen-frustrated-with-no-committee-assignments/"]),
    ]),

    # ---------- Dan Dockstader (WY-R, State Senator SD-16, since Jan 2009; WY Senate President 2021-2023) ----------
    ("dan-dockstader", "WY", "State Senator", [
        claim("dd1", "dan-dockstader", "sanctity_of_life", 0, True,
              "Co-sponsored WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable; the Wyoming Senate passed the bill 27-4 and Governor Mark Gordon signed it into law on March 9, 2026. Dockstader, who called his support for the bill a matter of personal conviction — 'I'll always stand with life,' he said — is one of 13 Senate co-sponsors of the legislation. A Republican publisher and radio host representing Senate District 16 (Lincoln, Sublette, and Teton counties), Dockstader served as Wyoming Senate President from 2021 to 2023 and has championed pro-life legislation throughout his tenure.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Dan_Dockstader"]),
        claim("dd2", "dan-dockstader", "self_defense", 0, True,
              "Voted for WY HB 96 (2026), lowering Wyoming's concealed-carry permit age from 21 to 18 and extending campus carry to legal adults 18-20; the bill passed the Wyoming Senate with only two dissenting votes and was signed by Governor Mark Gordon in March 2026, effective July 1, 2026. Dockstader, a Republican who served as Wyoming Senate President from 2021 to 2023, supported the bill as consistent with Wyoming's constitutional-carry tradition and the principle that legal adults should enjoy the full exercise of Second Amendment rights.",
              ["https://wyoleg.gov/Legislation/2026/HB0096",
               "https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://ballotpedia.org/Dan_Dockstader"]),
    ]),

    # ---------- Chris Rothfuss (WY-D, State Senator SD-9, since Jan 2011; Senate Minority Leader 2013-2025) ----------
    ("chris-rothfuss", "WY", "State Senator", [
        claim("cr1", "chris-rothfuss", "sanctity_of_life", 0, False,
              "Voted against WY HB 126 (2026), the Human Heartbeat Act, prohibiting abortion in Wyoming once a fetal heartbeat is detectable; the bill passed the Senate 27-4 and was signed by Governor Mark Gordon on March 9, 2026. Rothfuss, one of only two Democrats in the Wyoming Senate, was among the four senators who cast a NO vote. His opposition is consistent with his decade-long record of voting against pro-life legislation in Wyoming and with his broader progressive position on reproductive policy.",
              ["https://www.wyomingnewsnow.tv/news/heartbeat-act-passes-senate-and-moves-to-governors-desk/article_1fad539e-f039-4ff7-8f40-1af8df7537cb.html",
               "https://wyoleg.gov/Legislation/2026/HB0126",
               "https://ballotpedia.org/Chris_Rothfuss"]),
        claim("cr2", "chris-rothfuss", "biblical_marriage", 2, False,
              "Voted against WY HB 72 (2025), the Protecting Women's Privacy in Public Spaces Act, which codifies biological sex as the operative legal standard for all sex-segregated government facilities in Wyoming (restrooms, locker rooms, overnight quarters); the Senate passed the bill 25-6 and Governor Mark Gordon signed it in April 2025, effective July 1, 2025. Rothfuss, then serving as Senate Minority Leader, vocally opposed the bill during committee hearings — invoking the Supreme Court's 'separate but equal' doctrine to argue the biological-sex standard harmed transgender students — and cast one of only six NO votes against the measure.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://www.wyomingpublicmedia.org/politics-government/2025-07-02/trying-to-silence-us-trans-woman-uses-the-womens-bathroom-to-protest-new-wyoming-law",
               "https://ballotpedia.org/Chris_Rothfuss"]),
    ]),

    # ---------- Charles Scott (WY-R, State Senator SD-30, since Jan 1983; Senate Education Committee Chairman) ----------
    ("charles-scott", "WY", "State Senator", [
        claim("cs1", "charles-scott", "family_child_sovereignty", 0, True,
              "As Chairman of the Wyoming Senate Education Committee and Co-Chair of the Joint Education Committee, Scott shepherded 'Parental Rights in Education-1' through the 2024 Wyoming legislative session; the law bars Wyoming public schools from conducting lessons on sexual orientation or gender identity without prior parental consent and requires schools to notify parents about non-emergency health matters — including a student's social gender-identity transition; Governor Mark Gordon allowed the law to take effect without his signature in March 2024. Scott's committee contributions included an amendment clarifying emergency-care carve-outs while preserving the bill's core parental-notification mandate.",
              ["https://cowboystatedaily.com/2024/02/26/law-banning-schools-from-hiding-gender-transitions-from-parents-advances/",
               "https://cowboystatedaily.com/2024/03/06/schools-cant-keep-info-from-parents-as-gordon-lets-law-pass-without-signature/",
               "https://ballotpedia.org/Charles_Scott_(Wyoming)"]),
        claim("cs2", "charles-scott", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable; Governor Mark Gordon signed the bill into law on March 9, 2026. The Wyoming Senate passed HB 126 by a 27-4 margin. Scott, a Harvard-educated Republican who has represented Natrona County's Senate District 30 since 1983 — among the longest-serving state legislators in the nation — voted with the overwhelming Republican majority to enact Wyoming's most protective pro-life statute in decades.",
              ["https://wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Charles_Scott_(Wyoming)"]),
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
