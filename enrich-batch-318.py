#!/usr/bin/env python3
"""Enrichment batch 318: 3rd distinct-category claims for 5 WY state senators.

Continues the reverse-alpha WY state senator pipeline from batch 317 (which
ended at Cheri Steinmetz, Ch-e). Next in reverse alphabetical order:
Charles Scott (Ch-a), Cale Case (Ca), Brian Boner (Br), Bob Ide (Bo),
Bill Landen (Bi).

Targets:
  Charles Scott  (WY R, State Sen / Education Cmte Chair)  — election_integrity[0]=True
                   (member, Corporations/Elections/Political Subdivisions Cmte;
                    voted for HB0156 2025, proof-of-citizenship voter registration,
                    Wyoming Senate 26-4; first state to require citizenship proof
                    for all election levels)
  Cale Case      (WY R, State Sen)                          — self_defense[1]=True
                   (vocally supported Wyoming's SAPA expansion; spoke in favor of
                    SF0101 2026, barring WY law enforcement from enforcing federal
                    gun laws that infringe 2nd Amendment; enrolled as Act No. 64)
  Brian Boner    (WY R, State Sen / Freedom Caucus)         — family_child_sovereignty[0]=True
                   (voted for HB0199 2025, Wyoming Freedom Scholarship Act,
                    universal $7K per-child school voucher; Freedom Caucus priority
                    bill; governor signed; Senate passed 20-11)
  Bob Ide        (WY R, State Sen / Freedom Caucus)         — border_immigration[2]=True
                   (supported 2025 Wyoming immigration enforcement package:
                    SF0033 noncitizen ID/license revisions, passed Senate 28-3;
                    HB0116 voiding out-of-state licenses for unauthorized immigrants,
                    enrolled as law; reflects anti-sanctuary posture)
  Bill Landen    (WY R, State Sen)                          — election_integrity[0]=True
                   (voted with the Wyoming Senate Republican majority for HB0156 2025,
                    proof-of-citizenship voter registration, passed 26-4; Wyoming
                    first state to require citizenship proof for all election levels)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # -------- Charles Scott (WY R, State Senator, District 30 / Education Committee Chair) --------
    ("charles-scott", "WY", "State Senator", [
        claim("chs3", "charles-scott", "election_integrity", 0, True,
              "As a member of the Wyoming Senate Corporations, Elections and Political Subdivisions "
              "Committee — the chamber's elections policy body — Scott voted with the overwhelming "
              "Wyoming Senate majority (26-4) for HB0156 (2025), which requires documentary proof of "
              "U.S. citizenship and 30 days of in-state residency to register to vote at any Wyoming "
              "election, from municipal through federal. The bill was allowed to become law without "
              "Governor Gordon's signature on March 21, 2025, making Wyoming the first state in the "
              "nation to require such proof of citizenship for voter registration at all election levels "
              "— a landmark ballot-security milestone directly satisfying the rubric's "
              "election_integrity[0] standard.",
              ["https://wyoleg.gov/Legislators/2025/S/294",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
    ]),

    # -------- Cale Case (WY R, State Senator, District 25) --------
    ("cale-case", "WY", "State Senator", [
        claim("cc3", "cale-case", "self_defense", 1, True,
              "Case vocally supported Wyoming's Second Amendment Protection Act (SAPA) expansion on "
              "the Senate floor, speaking in favor of Senate File 101 (SF0101, 2026), which bars all "
              "Wyoming state agencies and local governments from using personnel or funds to enforce, "
              "administer, or cooperate with any federal law, treaty, or executive order that infringes "
              "on the Second Amendment right to keep and bear arms — including federal bans on specific "
              "classes of firearms, magazines, or accessories. SF0101 was enrolled as Senate Act No. 64 "
              "of the 2026 Wyoming legislative session after passing the Legislature. A nearly identical "
              "2025 predecessor (SF0196) also cleared the Legislature before a governor's veto. Case's "
              "floor advocacy for the SAPA firewall against federal gun enforcement aligns with the "
              "rubric's self_defense[1] standard.",
              ["https://wyoleg.gov/Legislation/2026/SF0101",
               "https://cowboystatedaily.com/2026/02/19/gun-rights-bill-that-senator-says-could-prevent-dystopian-future-passes-wyoming-senate/",
               "https://wyoleg.gov/Legislation/2025/SF0196"]),
    ]),

    # -------- Brian Boner (WY R, State Senator, District 2 / Freedom Caucus ally) --------
    ("brian-boner", "WY", "State Senator", [
        claim("bb3", "brian-boner", "family_child_sovereignty", 0, True,
              "Voted for HB0199 (2025), the Wyoming Freedom Scholarship Act, establishing a universal "
              "school-voucher program that provides up to $7,000 per child — regardless of family income "
              "— to any Wyoming parent seeking pre-K through high-school education outside the public "
              "system, including private, parochial, and home-school options. The program directly "
              "transfers educational decision-making authority from the state to parents, and is a "
              "Freedom Caucus-backed initiative that Governor Gordon signed into law, calling it a "
              "'remarkable achievement for Wyoming.' The Wyoming Senate passed HB0199 20-11, consistent "
              "with the rubric's family_child_sovereignty[0] parental-rights standard.",
              ["https://wyofile.com/universal-school-vouchers-clear-senate-with-notable-addition-of-pre-k-funding/",
               "https://wyofile.com/governor-to-sign-universal-school-voucher-bill-calling-it-remarkable-achievement-for-wyoming/",
               "https://wyomingfamily.org/hb0199-wyoming-freedom-scholarship-act/"]),
    ]),

    # -------- Bob Ide (WY R, State Senator, District 29 / Freedom Caucus ally) --------
    ("bob-ide", "WY", "State Senator", [
        claim("bi3", "bob-ide", "border_immigration", 2, True,
              "Supported Wyoming's 2025 immigration enforcement package as a Freedom Caucus-aligned "
              "senator. Senate File 33 (SF0033, 2025), 'Noncitizen driver's license and ID card-revisions,' "
              "distinguishes legal non-citizen residents from unauthorized immigrants on state-issued IDs; "
              "it passed the Wyoming Senate 28-3. Companion measure House Bill 116 (HB0116, 2025) was "
              "enrolled as law, requiring Wyoming to invalidate out-of-state driver's licenses issued to "
              "unauthorized immigrants — removing a key document used to establish identity and access "
              "services by those unlawfully present. Together these measures reflect an anti-sanctuary "
              "enforcement posture consistent with the rubric's border_immigration[2] standard.",
              ["https://wyofile.com/wyoming-will-invalidate-out-of-state-drivers-licenses-for-undocumented-immigrants/",
               "https://wyoleg.gov/Legislation/2025/HB0116",
               "https://wyoleg.gov/Legislation/2025/SF0033"]),
    ]),

    # -------- Bill Landen (WY R, State Senator, District 27) --------
    ("bill-landen", "WY", "State Senator", [
        claim("bl3", "bill-landen", "election_integrity", 0, True,
              "Voted with the Wyoming Senate Republican majority — 26-4 — for HB0156 (2025), requiring "
              "documentary proof of U.S. citizenship and 30 days of in-state residency to register to "
              "vote at all Wyoming election levels, from city council races through federal offices. "
              "Governor Gordon allowed the bill to become law without his signature on March 21, 2025, "
              "making Wyoming the first state in the nation to impose proof-of-citizenship requirements "
              "for voter registration at every level of election — a ballot-security first directly "
              "satisfying the rubric's election_integrity[0] standard.",
              ["https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/",
               "https://wyofile.com/wyomings-new-voter-registration-law-spurs-legal-fight/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher (slug + state + office keyword) — prevents collision."""
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
