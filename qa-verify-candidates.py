#!/usr/bin/env python3
"""qa-verify-candidates.py — PSA-runnable QA pass over grind-scored candidates. ZERO CLOUD.

Sheriff Roy's (or any exec-granted agent's) verification tool: samples the most recently
LOCAL-GRIND-scored candidates and mechanically re-audits each scored cell —
  1. re-fetches the cell's cited source URL (dead source = FAIL),
  2. asks the LOCAL Gemma (:1234, fallback :1235) whether the fetched page still supports
     the stored claim for that rubric question (NO = MISMATCH -> HOLD for review).
The agent QUOTES this report — it never vouches from memory. Exit 0 = all sampled cells
verified; exit 1 = at least one FAIL/MISMATCH (report says exactly which).

Usage:
  qa-verify-candidates.py [N]                  # sample the N most recent (default 3)
  qa-verify-candidates.py --slugs a,b,c        # audit specific slugs
  qa-verify-candidates.py 3 --out /tmp/qa.json # also write the full JSON report
"""
import json, re, sys, time, urllib.request

sys.path.insert(0, ".")
import importlib.util
_spec = importlib.util.spec_from_file_location("lpe", "local-politician-extract.py")
lpe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lpe)   # reuse fetch/to_text/norm/model_at/chat — ONE implementation

JUDGE_SYS = (
    "You are a neutral fact-checker. Given a scorecard POSITION (an affirmative policy statement), "
    "a stored CLAIM about a candidate, the VERDICT recorded (SUPPORT or OPPOSE the position), and "
    "TEXT fetched from the claim's cited source page: answer YES if the page text genuinely backs "
    "the stored claim/verdict, NO if it does not (off-topic, contradicts, or no longer present). "
    "Answer only YES or NO."
)


def main():
    args = sys.argv[1:]
    out_path = None
    if "--out" in args:
        out_path = args[args.index("--out") + 1]
    want_slugs = None
    if "--slugs" in args:
        want_slugs = [s.strip() for s in args[args.index("--slugs") + 1].split(",") if s.strip()]
    n = next((int(a) for a in args if a.isdigit()), 3)

    sc = json.load(open("data/scorecard.json"))
    cats = {c["id"]: c for c in sc["categories"]}
    pool = [c for c in sc["candidates"]
            if "Local-grind" in str((c.get("profile") or {}).get("confidence_note") or "")]
    if want_slugs:
        pool = [c for c in pool if c["slug"] in want_slugs]
    pool.sort(key=lambda c: str((c.get("profile") or {}).get("last_refined") or ""), reverse=True)
    sample = pool[:n] if not want_slugs else pool
    if not sample:
        print("QA: no local-grind-scored candidates found to audit.")
        return 0

    base = "http://127.0.0.1:1234/v1"
    model = lpe.model_at(base, prefer=["gemma-4-31b", "gemma"])
    if not model:
        base = "http://127.0.0.1:1235/v1"
        model = lpe.model_at(base)
    if not model:
        print("QA ABORT: no local model on :1234/:1235 — cannot judge. (Do not vouch without this.)")
        return 1
    print(f"QA judge: {model} @ {base}  |  auditing {len(sample)} candidate(s)")

    report, any_bad = [], False
    for c in sample:
        slug = c["slug"]
        foot = c.get("footnotes") or {}
        af = c.get("answer_footnotes") or {}
        scores = c.get("scores") or {}
        entry = {"slug": slug, "state": c.get("state"), "cells": [], "verified": 0, "failed": 0}
        page_cache = {}
        for cat_id, refs_per_q in af.items():
            qs = (cats.get(cat_id) or {}).get(
                {"federal": "questions", "state": "questions_state", "local": "questions_local"}
                .get(c.get("level") or "state", "questions")) or (cats.get(cat_id) or {}).get("questions") or []
            arr = scores.get(cat_id) or []
            for qi, refs in enumerate(refs_per_q or []):
                if not refs:
                    continue
                v = arr[qi] if qi < len(arr) else None
                if v is not True and v is not False:
                    continue
                # note text for this cell lives in the footnote excerpt/title; src url in footnotes
                for ref in refs:
                    fn = foot.get(ref) or foot.get(f"src-{ref}") or {}
                    url = fn.get("url")
                    note = fn.get("excerpt") or fn.get("title") or ""
                    if not url:
                        continue
                    cell = {"cat": cat_id, "q": qi, "v": v, "url": url, "status": None}
                    if url not in page_cache:
                        try:
                            page_cache[url] = lpe.to_text(lpe.fetch(url))[:9000]
                        except Exception as e:
                            page_cache[url] = None
                    txt = page_cache[url]
                    if txt is None:
                        cell["status"] = "FAIL_dead_source"
                        entry["failed"] += 1; any_bad = True
                    else:
                        pos = qs[qi] if qi < len(qs) else cat_id
                        verdict = "SUPPORT" if v else "OPPOSE"
                        try:
                            ans = lpe.chat(base, model, JUDGE_SYS,
                                           f"POSITION: {pos}\nCLAIM: {note[:300]}\nVERDICT: {verdict}\n"
                                           f"SOURCE PAGE TEXT:\n{txt}", max_tokens=6).strip().upper()
                        except Exception:
                            ans = "ERROR"
                        if ans.startswith("YES"):
                            cell["status"] = "VERIFIED"; entry["verified"] += 1
                        elif ans.startswith("NO"):
                            cell["status"] = "MISMATCH_hold"; entry["failed"] += 1; any_bad = True
                        else:
                            cell["status"] = "JUDGE_ERROR"; entry["failed"] += 1; any_bad = True
                    entry["cells"].append(cell)
                    break   # one footnote per cell is enough for the audit
        report.append(entry)
        print(f"  {slug:26} {entry['verified']} verified / {entry['failed']} flagged"
              + ("" if not entry["cells"] else ""))
        for cell in entry["cells"]:
            if cell["status"] != "VERIFIED":
                print(f"      !! {cell['cat']}[{cell['q']}]={cell['v']} {cell['status']} {cell['url'][:60]}")

    tot_v = sum(e["verified"] for e in report); tot_f = sum(e["failed"] for e in report)
    print(f"\nQA RESULT: {tot_v} cell(s) verified, {tot_f} flagged across {len(report)} candidate(s)"
          f" -> {'PASS' if not any_bad else 'ATTENTION NEEDED'}")
    if out_path:
        json.dump({"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "judge": model,
                   "candidates": report}, open(out_path, "w"), indent=1)
        print(f"report: {out_path}")
    return 1 if any_bad else 0


if __name__ == "__main__":
    sys.exit(main())
