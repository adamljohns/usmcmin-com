#!/usr/bin/env python3
"""Enrichment batch 666: hand-curated claims for 5 Wisconsin State Assembly Democrats.

Targets from the bottom of the archetype_party_default / 0-claims bucket
(sorted descending by state then name): all five represent WI Assembly seats
held by Democrats. Claims span the 2025 Abortion Rights Restoration Act
(AB355), sanctuary legislation (AB57), voter-ID constitutional amendment
NO votes (AJR1), conversion-therapy ban (AB359), LGBTQ school-training
grants (AB316), and gay-panic-defense elimination (AB361), covering
January–July 2025.

Assembly Members (WI / D):
  Lee Snodgrass   — AD-52, Appleton
  Karen Kirsch    — AD-7, Edgerton
  Karen DeSanto   — AD-40, Brookfield
  Kalan Haywood   — AD-16, Milwaukee
  Joe Sheehan     — AD-26, Shullsburg

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50 MB warning.
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
    # ── Lee Snodgrass (WI AD-52, D) ─────────────────────────────────────────
    ("lee-snodgrass-wi-52", "WI", "Assembly Member", [
        claim("ls1", "lee-snodgrass-wi-52", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which asserts a fundamental right to bodily autonomy including the right to "
              "obtain an abortion, repeals Wisconsin's existing abortion restrictions, and "
              "mandates that health plans covering maternity care also cover abortion with "
              "no gestational limit — explicitly rejecting any personhood-from-conception "
              "legal standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("ls2", "lee-snodgrass-wi-52", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), which prohibits all "
              "Wisconsin state and local officials — including law enforcement officers — "
              "from assisting in the detention of any individual on the sole basis that "
              "the person is or is alleged to be unlawfully present in the United States, "
              "and bars state agencies from expending funds toward such assistance — a "
              "de facto sanctuary-state bill opposing mandatory immigration-enforcement "
              "cooperation.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
        claim("ls3", "lee-snodgrass-wi-52", "biblical_marriage", 2, False,
              "Co-introduced AB359 (July 17, 2025), which prohibits licensed mental-health "
              "providers from engaging in conversion therapy with a minor — banning "
              "therapeutic approaches that seek to change a person's sexual orientation or "
              "gender identity and criminalizing practices that affirm a traditional or "
              "biblical understanding of sexuality and gender.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab359",
               "https://legiscan.com/WI/bill/AB359/2025"]),
    ]),

    # ── Karen Kirsch (WI AD-7, D) ────────────────────────────────────────────
    ("karen-kirsch-wi-7", "WI", "Assembly Member", [
        claim("kk1", "karen-kirsch-wi-7", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which establishes a statutory right to bodily autonomy including the right "
              "to access abortion, repeals Wisconsin's existing abortion regulations, and "
              "requires health plans that cover maternity care to cover abortion — opposing "
              "any recognition of the unborn as persons in law.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("kk2", "karen-kirsch-wi-7", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), a sanctuary measure "
              "prohibiting Wisconsin state and local officials — including law enforcement — "
              "from aiding in the detention of individuals on the sole basis that they are "
              "or are alleged to be unlawfully present in the United States, and barring "
              "state funds from being spent on such assistance — opposing the rubric's "
              "anti-sanctuary-city position.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
        claim("kk3", "karen-kirsch-wi-7", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025), the Wisconsin Assembly resolution to "
              "enshrine a voter-ID requirement in the state constitution; the measure passed "
              "54-45 on a strict party-line vote, with all 45 Assembly Democrats — including "
              "Kirsch — voting against embedding voter-ID in the Wisconsin constitution.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
    ]),

    # ── Karen DeSanto (WI AD-40, D) ──────────────────────────────────────────
    ("karen-desanto-wi-40", "WI", "Assembly Member", [
        claim("kd1", "karen-desanto-wi-40", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which declares a fundamental right to bodily autonomy encompassing abortion, "
              "repeals Wisconsin's abortion restrictions, and mandates abortion coverage "
              "under health plans that include maternity benefits — rejecting life-at-conception "
              "legal standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("kd2", "karen-desanto-wi-40", "biblical_marriage", 4, False,
              "Co-sponsored AB316 (2025), which creates a state grant program for LGBTQIA+ "
              "rights training provided specifically to public school counselors and school "
              "social workers — state-funded promotion of LGBTQ ideology within the K-12 "
              "school system, opposing the rubric's standard against LGBTQ promotion in "
              "schools and policy.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab316",
               "https://legiscan.com/WI/text/AB316/id/3260988"]),
        claim("kd3", "karen-desanto-wi-40", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025), the Assembly joint resolution to send "
              "a voter-ID constitutional amendment to Wisconsin voters; AJR1 passed 54-45 "
              "on a strict party-line vote with all Assembly Democrats — including DeSanto — "
              "opposing the measure.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
    ]),

    # ── Kalan Haywood (WI AD-16, D) ──────────────────────────────────────────
    ("kalan-haywood-wi-16", "WI", "Assembly Member", [
        claim("kh1", "kalan-haywood-wi-16", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which establishes a statutory right to bodily autonomy including the right "
              "to obtain an abortion, repeals Wisconsin's existing abortion laws, and "
              "mandates coverage of abortion in health plans — rejecting any legal "
              "protection of the unborn from conception.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("kh2", "kalan-haywood-wi-16", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), a Wisconsin sanctuary "
              "bill barring all state and local officials — including law enforcement — "
              "from assisting in the detention of individuals on the sole basis that they "
              "are or are alleged to be unlawfully present in the United States, and "
              "prohibiting state agencies from expending funds for such assistance — "
              "directly opposing mandatory immigration-enforcement cooperation.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
        claim("kh3", "kalan-haywood-wi-16", "biblical_marriage", 2, False,
              "Co-sponsored AB361 (introduced July 17, 2025), which eliminates the criminal "
              "defenses of adequate provocation, self-defense, and not guilty by reason of "
              "mental disease or defect when the defendant's claim is based on the victim's "
              "gender identity or sexual orientation — embedding gender identity as a "
              "legally protected category in Wisconsin criminal law and opposing a "
              "biblical understanding of sex and gender.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab361"]),
    ]),

    # ── Joe Sheehan (WI AD-26, D) ────────────────────────────────────────────
    ("joe-sheehan-wi-26", "WI", "Assembly Member", [
        claim("js1", "joe-sheehan-wi-26", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which asserts a fundamental right to bodily autonomy encompassing abortion, "
              "repeals Wisconsin's existing abortion restrictions, and mandates abortion "
              "coverage in health plans offering maternity benefits — explicitly opposing "
              "life-at-conception legal standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("js2", "joe-sheehan-wi-26", "biblical_marriage", 2, False,
              "Co-introduced AB359 (introduced July 17, 2025), which prohibits licensed "
              "mental-health providers from practicing conversion therapy with a minor — "
              "banning therapeutic approaches that seek to change a person's sexual "
              "orientation or gender identity; the bill criminalizes practices that affirm "
              "a traditional or biblical understanding of human sexuality.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab359",
               "https://legiscan.com/WI/bill/AB359/2025"]),
        claim("js3", "joe-sheehan-wi-26", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025), the Wisconsin Assembly joint resolution "
              "to enshrine voter-ID requirements in the state constitution; the measure "
              "passed 54-45 on a strict party-line vote with all 45 Assembly Democrats — "
              "including Sheehan — opposing the constitutional amendment.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher. Returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
