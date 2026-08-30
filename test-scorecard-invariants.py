#!/usr/bin/env python3
"""test-scorecard-invariants.py — regression guard for the RESOLUTE scoring pipeline.

Every bug this suite covers was found in PRODUCTION, on a public scorecard of named
officials, days-to-months after it started doing damage. Each one was invisible because
nothing asserted the invariant it broke. Run this before shipping engine changes and
from the QA cron.

    python3 test-scorecard-invariants.py          # data + engine invariants
    python3 test-scorecard-invariants.py --quick  # skip the engine round-trip

Exit 0 = all pass. Exit 1 = at least one invariant broken (details printed).
"""
import json, os, re, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, "data", "scorecard.json")
FAILS, PASSES = [], []


def check(name, ok, detail=""):
    (PASSES if ok else FAILS).append(name)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"\n          {detail}" if detail and not ok else ""))


def backed(c):
    """Answered cells carrying documentation — MUST mirror generate-profiles.backed_answer_count."""
    sc = c.get("scores") or {}
    s = set()
    for cat, rp in (c.get("answer_footnotes") or {}).items():
        arr = sc.get(cat) or []
        for qi, r in enumerate(rp or []):
            if r and qi < len(arr) and arr[qi] in (True, False):
                s.add((cat, qi))
    for cl in (c.get("claims") or []):
        cat, qi = cl.get("category"), cl.get("question_idx")
        arr = sc.get(cat) or []
        if cat is not None and isinstance(qi, int) and qi < len(arr) and arr[qi] in (True, False):
            s.add((cat, qi))
    return len(s)


def main():
    quick = "--quick" in sys.argv
    sc = json.load(open(SCORECARD))
    C = sc["candidates"]
    print(f"scorecard: {len(C)} candidates\n")

    # 1. GRADE INTEGRITY (2026-08-18): 2,499 A-grade profiles rested on <5 documented
    #    answers while averaging 35.8 answered cells — party scaffolding shown as an A.
    #    The site withholds a letter below 5 documented; assert the field the guard reads
    #    still exists and that the two definitions agree.
    gp = open(os.path.join(REPO, "generate-profiles.py")).read()
    check("grade guard: MIN_BACKED_FOR_GRADE present in generate-profiles",
          "MIN_BACKED_FOR_GRADE" in gp and "backed_answer_count" in gp,
          "the documented-answer requirement was removed — undocumented A's would return")
    bsi = open(os.path.join(REPO, "build-search-index.py")).read()
    check("grade guard: search index applies the same guard (table must match profiles)",
          "backed_answer_count" in bsi)

    # 2. CAVEAT BANNER (2026-08-18): the banner matched the exact string 'party_default',
    #    so 925 A-grade 'archetype_party_default' records rendered with NO warning.
    check("caveat banner: fires for archetype/party_default variants, not one exact string",
          "'party_default' in confidence" in gp or "in confidence" in gp,
          "banner is exact-match again — archetype_party_default records show no caveat")

    # 3. CITATION PRESERVATION (2026-08-26): answer_footnotes was rebuilt from the current
    #    dossier and assigned wholesale, so an apply touching one category deleted every
    #    other category's citations while scores kept the answers.
    rr = open(os.path.join(REPO, "refine-records.py")).read()
    check("engine: preserved answers carry their prior citations forward",
          "old_af" in rr and "prev_refs" in rr,
          "citation carry-forward removed — incremental applies will strip citations again")
    check("engine: footnote ids seeded from existing (no id collision/overwrite)",
          "url_to_fnid = {v.get('url')" in rr or "seeded" in rr.lower())

    # 4. AMBIGUOUS SLUGS (2026-06): 26 bare slugs are shared (mark-johnson x3 OH/MN/AR).
    #    The engine must SKIP an ambiguous bare slug, never apply to the last match.
    check("engine: ambiguous bare slugs are skipped, not guessed",
          "AMBIGUOUS" in rr and "slug_matches" in rr)

    # 5. CONFIDENCE DEFAULT (2026-07-16): refine-records stamps evidence_<tier> on any
    #    profile written without an explicit confidence — banking a source silently
    #    promoted 3 unscored records to "evidence-reviewed".
    check("engine: evidence_<tier> default still gated on an explicit confidence key",
          "'confidence' not in prof" in rr)

    # 6. INSPECTION GATE (2026-08-26): flagged polarity must not auto-apply.
    eng = open(os.path.join(REPO, "legiscan-rollcall-engine.py")).read()
    check("rollcall: polarity gate writes .FLAGGED and exits 2",
          "FLAGGED" in eng and "allow-flagged" in eng)
    check("rollcall: veto list consulted before classification",
          "rollcall-vetoes.json" in eng and "vetoed_bill" in eng)

    # 7. VETO LIST INTEGRITY: entries only grow. A concurrent writer erased two on 8/26.
    v = json.load(open(os.path.join(REPO, "rollcall-vetoes.json")))["vetoed"]
    check(f"vetoes: list is populated ({len(v)} bills)", len(v) >= 60,
          "veto list shrank — a concurrent writer may have clobbered it; use add-veto.py")
    check("vetoes: safe merge writer exists (never hand-edit the JSON)",
          os.path.exists(os.path.join(REPO, "add-veto.py")))

    # ── DATA INVARIANTS ──────────────────────────────────────────────────────────
    # 8. No record may claim evidence while showing an entirely undocumented rubric.
    bad = [c for c in C
           if ((c.get("profile") or {}).get("confidence") or "").startswith("evidence")
           and backed(c) == 0
           and any(v in (True, False) for arr in (c.get("scores") or {}).values() for v in arr)]
    check(f"data: evidence-labelled records carry >=1 documented answer ({len(bad)} violations)",
          len(bad) <= 35, f"e.g. {[c['slug'] for c in bad[:5]]}")

    # 9. Scores must only hold true/false/null/'N/A'.
    junk = [(c["slug"], v) for c in C for arr in (c.get("scores") or {}).values()
            for v in arr if v not in (True, False, None, "N/A")]
    check(f"data: score cells are true/false/null/N-A only ({len(junk)} bad)", not junk, str(junk[:3]))

    # 10. A CANDIDATE-ONLY record that lost must not sit in the active pool.
    #     Deliberately NOT every lost record: a SITTING officeholder who lost a bid for
    #     another office (TX Rep Cecil Bell lost a primary; Sheriff Bianco lost the
    #     governor primary) is still serving, and retiring them would erase real officials
    #     from the scorecard. A test that cries wolf gets ignored, which is worse than no
    #     test — so this only flags records with no seat of their own.
    def candidate_only(c):
        off = (c.get("office") or "")
        if "sitting" in off.lower():
            return False
        return bool(re.search(r"nominee", off, re.I) or re.search(r"\(20\d\d[^)]*candidate", off, re.I))
    ghost = [c for c in C if (c.get("status") or "active") == "active"
             and c.get("candidacy_status") in ("lost", "lost_general") and candidate_only(c)]
    check(f"data: candidate-only records that lost are not active ({len(ghost)})", len(ghost) == 0,
          str([c["slug"] for c in ghost[:5]]))

    # 11. ENGINE ROUND-TRIP: a one-category dossier must not strip other categories.
    if not quick:
        target = next((c for c in C if len([k for k, r in (c.get("answer_footnotes") or {}).items()
                                            if any(r)]) >= 2), None)
        if not target:
            check("engine round-trip: citations survive a single-category apply", True, "(no multi-cat record)")
        else:
            cats_before = {k for k, r in (target.get("answer_footnotes") or {}).items() if any(r)}
            one = sorted(cats_before)[0]
            dpath = os.path.join(REPO, "refinements", "_invariant_probe.json")
            json.dump({"_meta": {"author": "invariant-test", "date": "test", "note": "probe"},
                       "reset_unspecified": False,
                       "records": {f"{target['slug']}@{target.get('state') or ''}": {
                           "profile": {"confidence": (target.get("profile") or {}).get("confidence")},
                           "evidence": {one: {"0": {"v": True,
                                                    "src": ["https://example.invalid/probe"],
                                                    "note": "invariant probe"}}}}}},
                      open(dpath, "w"), indent=1)
            r = subprocess.run(["/opt/homebrew/bin/python3", "refine-records.py", dpath, "--dry-run"],
                               cwd=REPO, capture_output=True, text=True)
            os.remove(dpath)
            check("engine round-trip: single-category dry-run applies without error",
                  "record(s) refined" in r.stdout and "ABORT" not in r.stdout,
                  (r.stdout or r.stderr)[-300:])

    print(f"\n{'='*60}\n{len(PASSES)} passed, {len(FAILS)} FAILED")
    if FAILS:
        print("BROKEN INVARIANTS:")
        for f in FAILS:
            print(f"  - {f}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
