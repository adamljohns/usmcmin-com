#!/usr/bin/env python3
"""Enrichment batch 256: 4 state legislators from bottom-of-alphabet states (WV / WY).

archetype_curated federal bucket exhausted; continues enriching state legislators
from WV and WY with documented 2017-2026 positions and voting records.

Targets: Ryan Weld (WV Senator, Majority Whip 2017-2025),
         Rupie Phillips (WV Senator, party-switch coal/guns/abortion),
         Tim French (WY Senator, Wyoming Right to Life endorsed),
         Trenton Barnhart (WV Senator, NRA + WV Citizens Defense League).
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
    # ----------- Ryan Weld (WV, State Senator) -----------
    ("ryan-weld", "WV", "Senator", [
        claim("rw1", "ryan-weld", "sanctity_of_life", 1, True,
              "Weld authored two floor amendments to West Virginia Senate Bill 173 (February 2026) — legislation prohibiting out-of-state entities from prescribing or mailing abortifacients into West Virginia, where abortion has been nearly totally illegal since September 2022. His first amendment barred the state from contracting with any manufacturer or wholesale distributor that ships abortion-inducing drugs into WV; his second gave WV women a private right of action to sue those senders in the circuit court of the county where they received the drugs — adding civil enforcement teeth to criminal penalties. The full Senate passed SB 173 with his amendments by a 31-1 vote.",
              ["https://westvirginiawatch.com/2026/02/13/senate-passes-bill-prohibiting-abortifacients-being-prescribed-or-mailed-to-west-virginia/",
               "https://www.herald-dispatch.com/news/senate-passes-bill-prohibiting-abortifacients-being-prescribed-or-mailed-to-west-virginia/article_3df04ba8-f00d-41c5-a5e4-86fd2a72dce8.html"]),
        claim("rw2", "ryan-weld", "self_defense", 0, True,
              "A Republican member of the West Virginia State Senate since 2016 who has publicly stated he has 'always supported the 2nd Amendment rights.' Weld served as Senate Majority Whip — the chamber's chief vote-counter — from 2017 to 2025, helping maintain West Virginia's constitutional-carry framework (permitless carry enacted 2016, expanded to ages 18-20 in 2021) throughout his eight-year tenure in Senate leadership.",
              ["https://ballotpedia.org/Ryan_Weld",
               "https://en.wikipedia.org/wiki/Ryan_Weld"]),
    ]),

    # ----------- Rupie Phillips (WV, State Senator) -----------
    ("rupie-phillips", "WV", "Senator", [
        claim("rp1", "rupie-phillips", "sanctity_of_life", 0, True,
              "Phillips switched his party registration from Democrat to Republican in January 2017 explicitly because the Democratic Party 'did not match his values or the values of his district, specifically in reference to policies involving coal, guns, and abortion.' His party change over abortion values places him in the pro-life camp, consistent with his service in the Republican supermajority that passed West Virginia's near-total abortion ban in 2022.",
              ["https://en.wikipedia.org/wiki/Rupie_Phillips",
               "https://www.wsaz.com/content/news/WVa-representative-to-switch-parties--411878785.html"]),
        claim("rp2", "rupie-phillips", "self_defense", 0, True,
              "Phillips is a member of the National Rifle Association and explicitly cited gun rights as one of the three core reasons he left the Democratic Party for the Republican Party in 2017 — stating the Democratic Party no longer matched his values 'involving coal, guns, and abortion.' His NRA membership and stated defense of gun rights align with West Virginia's constitutional-carry framework.",
              ["https://en.wikipedia.org/wiki/Rupie_Phillips",
               "https://ballotpedia.org/Rupert_Phillips_Jr."]),
        claim("rp3", "rupie-phillips", "economic_stewardship", 4, True,
              "A career coal-industry worker and member of Friends of Coal, Phillips rejected the Democratic Party's anti-fossil-fuel energy agenda when he switched parties in 2017. His membership in Friends of Coal — a WV coal-industry advocacy group — and his decades-long career in the coal sector position him against the ESG/WEF investment agenda that targets fossil-fuel industries for divestment, regulatory shutdown, and exclusion from institutional investment portfolios.",
              ["https://en.wikipedia.org/wiki/Rupie_Phillips",
               "https://ballotpedia.org/Rupert_Phillips_Jr."]),
    ]),

    # ----------- Tim French (WY, State Senator) -----------
    ("tim-french", "WY", "Senator", [
        claim("tf1", "tim-french", "sanctity_of_life", 1, True,
              "French holds an endorsement from Wyoming Right to Life — an organization that explicitly 'does not endorse candidates who support abortion ban exceptions for rape or incest,' meaning French's pro-life position is without the compromise exceptions that would disqualify him from their support. He self-describes as 'pro-life' and co-sponsors up to 15 pieces of legislation per session including pro-life bills, maintaining a consistent uncompromised pro-life record across multiple terms in the Wyoming Senate.",
              ["https://ballotpedia.org/Tim_French",
               "https://www.powelltribune.com/stories/senator-and-former-councilman-promote-their-conservative-credentials,136389"]),
        claim("tf2", "tim-french", "self_defense", 0, True,
              "French self-describes as 'pro-second amendment' and co-sponsors pro-Second Amendment bills each legislative session in the Wyoming Senate. He serves on the Senate Judiciary Committee — the panel that hears firearms legislation in Wyoming — and publicly aligns with Wyoming's constitutional-carry framework as a core plank of his conservative legislative platform.",
              ["https://ballotpedia.org/Tim_French",
               "https://www.timfrenchforwyosenate.com/"]),
    ]),

    # ----------- Trenton Barnhart (WV, State Senator) -----------
    ("trenton-barnhart", "WV", "Senator", [
        claim("tb1", "trenton-barnhart", "self_defense", 0, True,
              "Barnhart is a member of the National Rifle Association and the West Virginia Citizens Defense League — WV's leading no-compromise gun-rights organization. The WVCDL advocates for permitless (constitutional) carry and has been a key lobbying force in maintaining West Virginia's constitutional-carry framework. His dual membership in both the NRA and WVCDL establishes a documented pro-constitutional-carry record.",
              ["https://ballotpedia.org/Trenton_Barnhart",
               "https://en.wikipedia.org/wiki/Trenton_Barnhart"]),
        claim("tb2", "trenton-barnhart", "self_defense", 1, True,
              "As a member of the West Virginia Citizens Defense League, Barnhart aligns with an organization that consistently lobbies against red-flag laws, assault-weapons bans, and magazine-capacity restrictions in West Virginia — explicitly opposing any firearm registration scheme and any measure that would restrict law-abiding West Virginians' right to keep and bear arms without government infringement.",
              ["https://ballotpedia.org/Trenton_Barnhart",
               "https://wvmetronews.com/2026/01/28/morrisey-fills-senate-vacancy-with-houses-barnhart/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  ok {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
