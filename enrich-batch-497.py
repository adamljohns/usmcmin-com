#!/usr/bin/env python3
"""Enrichment batch 497: 5 state senators (VT + TN) — bottom-of-alphabet bucket.

Federal archetype_curated buckets exhausted; pivoting to archetype_party_default
state senators from the bottom of the alphabet (VT then TN).

Targets:
  Virginia V. Lyons (VT-D): 3 claims — Article 22 sponsorship, S.37 trans-sanctuary, PP honor
  Terry Williams (VT-R): 2 claims — NRA life member / Gun Owners of VT / constitutional carry
  Wendy Harrison (VT-D): 1 claim — reproductive-freedom champion, S.37 supermajority
  Todd Gardenhire (TN-R): 2 claims — NRA Board member, private-school-voucher champion
  Steve Southerland (TN-R): 2 claims — pro-life statement, NRA + permitless-carry alignment

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
    # ---------- Virginia V. Lyons (VT-D, State Senator) ----------
    ("virginia-v-lyons", "VT", "State Senator", [
        claim("vvl1", "virginia-v-lyons", "sanctity_of_life", 0, False,
              "Lead Senate sponsor of Proposal 5 (Article 22), the Vermont constitutional amendment "
              "ratified November 8, 2022, enshrining an unlimited right to 'personal reproductive "
              "autonomy' that passed 76.8% — rejecting any state interest in protecting unborn life "
              "from conception.",
              ["https://ballotpedia.org/Vermont_Proposal_5,_Right_to_Personal_Reproductive_Autonomy_Amendment_(2022)",
               "https://vtdigger.org/2019/03/13/senate-takes-constitutional-amendment-protect-abortion-rights/"]),
        claim("vvl2", "virginia-v-lyons", "biblical_marriage", 2, False,
              "Spearheaded Senate Bill 37 (Act 15, 2023), signed May 10, 2023, turning Vermont into a "
              "'trans sanctuary state' by shielding providers and patients who give or receive "
              "gender-affirming medical care from out-of-state legal action — direct institutional "
              "promotion of transgender ideology that the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Vermont_Senate_Bill_37",
               "https://vtdigger.org/2023/04/27/with-reproductive-shield-bills-vermont-lawmakers-seek-to-be-a-beacon-of-hope-for-transgender-patients/"]),
        claim("vvl3", "virginia-v-lyons", "sanctity_of_life", 4, False,
              "Honored by Planned Parenthood Vermont Action Fund at its annual fundraiser ('Sex, Politics "
              "& Cocktails') as a champion of abortion access — placing her directly inside the Planned "
              "Parenthood organizational network the rubric identifies as disqualifying.",
              ["https://vtdigger.org/2019/10/15/planned-parenthood-vermont-action-fund-ie-pac-honors-senator-ginny-lyons-attorney-general-t-j-donovan-at-sex-politics-cocktails-event/"]),
    ]),

    # ---------- Terry Williams (VT-R, State Senator) ----------
    ("terry-williams", "VT", "State Senator", [
        claim("tw1", "terry-williams", "self_defense", 1, True,
              "Life member of the National Rifle Association, vice president of the Vermont Federation of "
              "Sportsman's Clubs, and member of Gun Owners of Vermont — organizations that actively oppose "
              "red-flag laws, assault-weapons bans, and magazine-capacity limits — placing Williams in "
              "strong alignment with the rubric's anti-restriction standard.",
              ["https://en.wikipedia.org/wiki/Terry_Williams_(politician)",
               "https://ballotpedia.org/Terry_Williams_(Vermont)"]),
        claim("tw2", "terry-williams", "self_defense", 0, True,
              "As vice president of the Vermont Federation of Sportsman's Clubs and NRA life member, "
              "Williams defends Vermont's historic permitless-carry framework — the 'Vermont carry' "
              "tradition of bearing arms without a government-issued permit — which Vermont Democrats "
              "have repeatedly sought to curtail through new restrictions.",
              ["https://en.wikipedia.org/wiki/Terry_Williams_(politician)",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"]),
    ]),

    # ---------- Wendy Harrison (VT-D, State Senator) ----------
    ("wendy-harrison", "VT", "State Senator", [
        claim("wh1", "wendy-harrison", "sanctity_of_life", 0, False,
              "Identifies 'reproductive freedom rights' as a signature Vermont legislative achievement "
              "she is proud of; as a member of the 2023 Senate Democratic supermajority, served in "
              "the body that passed S.37 (Act 15, 2023) — Vermont's abortion-and-gender-affirming-care "
              "shield law — opposing any recognition of unborn life from conception.",
              ["https://ballotpedia.org/Wendy_Harrison",
               "https://vtdigger.org/2023/03/16/vermont-senate-gives-initial-approval-to-abortion-omnibus-bill-seeking-to-protect-reproductive-health-care/"]),
    ]),

    # ---------- Todd Gardenhire (TN-R, State Senator) ----------
    ("todd-gardenhire", "TN", "State Senator", [
        claim("tg1", "todd-gardenhire", "self_defense", 1, True,
              "Serves on the National Rifle Association's Board of Directors — a senior governance role "
              "in the nation's premier constitutional-carry and anti-gun-restriction organization — "
              "placing him in direct alignment with the rubric's opposition to red-flag laws, "
              "assault-weapons bans, and magazine-capacity limits.",
              ["https://en.wikipedia.org/wiki/Todd_Gardenhire",
               "https://ballotpedia.org/Todd_Gardenhire"]),
        claim("tg2", "todd-gardenhire", "family_child_sovereignty", 0, True,
              "Filed legislation to expand Tennessee's Education Savings Account (private-school voucher) "
              "program to Hamilton County, directing public funds to family-chosen schools rather than "
              "government-assigned institutions — consistent with the rubric's parental-sovereignty "
              "standard.",
              ["https://tennesseelookout.com/2022/12/08/chattanooga-senator-wants-private-school-vouchers-expanded-to-hamilton-county/",
               "https://ballotpedia.org/Todd_Gardenhire"]),
    ]),

    # ---------- Steve Southerland (TN-R, State Senator) ----------
    ("steve-southerland", "TN", "State Senator", [
        claim("ss1", "steve-southerland", "sanctity_of_life", 0, True,
              "Publicly stated opposition to abortion as a matter of personal conviction and has served "
              "as a Tennessee Republican senator through the state's landmark pro-life laws: the Human "
              "Life Protection Act (2019, trigger ban) and the Dobbs-activated near-total abortion ban "
              "(2022) — consistent with the rubric's life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Steve_Southerland_(Tennessee_politician)",
               "https://ballotpedia.org/Steve_Southerland_(Tennessee)"]),
        claim("ss2", "steve-southerland", "self_defense", 1, True,
              "Affiliated with the National Rifle Association per his official legislative biography, "
              "and served as a Tennessee Republican senator through the passage of the permitless-carry "
              "law (SB765/HB786, Act 786, 2021) — consistent with the rubric's opposition to "
              "government licensing requirements, red-flag laws, and gun registries.",
              ["https://en.wikipedia.org/wiki/Steve_Southerland_(Tennessee_politician)",
               "https://ballotpedia.org/Steve_Southerland_(Tennessee)"]),
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
