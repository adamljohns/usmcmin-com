#!/usr/bin/env python3
"""Full-review applier. NOT RUN LIVE until Adam's go.

Turns a review patch into a refine-records.py dossier and (only with --live) applies it through the
EXISTING compile path: refine-records.py consistency checks + build + commit_refinement.py's
path-scoped, conflict-safe push. Deploy doctrine is unchanged: the push is the deploy.

What it takes from the patch:
  * every change with gate == "auto" (high-confidence factual fills of empty fields: official website,
    term dates, office phone — never a score, never a Fredericksburg/Virginia official);
  * HOLD changes ONLY if their change_id is listed as approved in --approved FILE
    (a JSON list or {"approved": [...]} written by Roy QA / Adam). Flags, dedupe, needs-ruling and
    re-check rows are never applied by this tool.

Before anything is written, each change's quote is re-verified against a FRESH fetch of its URL
(XML/link evidence against the raw page). A change whose quote is gone is skipped and reported.

Modes:
  apply.py PATCH.json                       dry: print the dossier it would apply (default)
  apply.py PATCH.json --check               dry + run `refine-records.py --dry-run` on the dossier
                                            (reads scorecard.json, writes nothing)
  apply.py PATCH.json --live                refused unless FULL_REVIEW_APPLY_GO=<round id> is set;
                                            then: shared grind lock -> isolated worktree off
                                            origin/main -> commit_refinement.py (push = deploy)
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fr_lib as L  # noqa: E402

LOCK = "/tmp/scorecard-refine-local.lock"
OWNER = LOCK + ".owner"


def load_approved(path):
    if not path:
        return set()
    j = json.load(open(path))
    return set(j.get("approved", []) if isinstance(j, dict) else j)


def reverify(F, ch):
    ev = ch.get("evidence") or {}
    url, q = ev.get("url"), ev.get("quote")
    if not url or not q:
        return False, "no url/quote"
    rec = F.get(url, allow_archive=False) if "web.archive.org" not in url else F.get(url, allow_archive=False)
    if not rec.get("ok"):
        return False, f"fetch failed: {rec.get('status') or rec.get('error')}"
    if ev.get("evidence_type") in ("xml_record", "html_link", "site-config"):
        return (q in F.raw(rec)), "raw match"
    return bool(L.find_literal(q, F.text(rec))), "text match"


def to_dossier(patch, approved, F=None):
    sc = json.load(open(L.SCORECARD))
    by = {f"{c['slug']}@{(c.get('state') or '').upper()}": c for c in sc["candidates"]}
    records, report = {}, []
    for P in patch["politicians"]:
        c = by.get(P["key"])
        if not c:
            continue
        entry = {"profile": {}, "set": {}, "evidence": {}, "sources_add": []}
        for ch in P.get("changes", []):
            take = ch.get("gate") == "auto" or ch["change_id"] in approved
            if not take:
                continue
            if F is not None:
                ok, why = reverify(F, ch)
                if not ok:
                    report.append((ch["change_id"], "SKIP", f"quote not re-verified ({why})"))
                    continue
            f = ch["field"]
            m = re.match(r"scores\.(\w+)\[(\d)\]$", f)
            if m:
                entry["evidence"].setdefault(m.group(1), {})[m.group(2)] = {
                    "v": ch["new"], "src": [ch["evidence"]["url"]],
                    "note": (ch["evidence"]["quote"] or "")[:400]}
                entry["sources_add"].append(ch["evidence"]["url"])
            elif f.startswith("profile."):
                entry["profile"][f.split(".", 1)[1]] = ch["new"]
            elif f in ("website", "party", "district", "status"):
                entry["set"][f] = ch["new"]
            else:
                report.append((ch["change_id"], "SKIP", f"unsupported field {f}"))
                continue
            report.append((ch["change_id"], "TAKE", f"{f}: {ch['old']!r} -> {ch['new']!r}"))
        if not (entry["profile"] or entry["set"] or entry["evidence"]):
            continue
        # refine-records stamps evidence_<tier> on a profile written without confidence: re-state it
        entry["profile"]["confidence"] = (c.get("profile") or {}).get("confidence")
        entry["profile"]["full_review"] = patch["_meta"]["round"]
        for k in ("set", "evidence", "sources_add"):
            if not entry[k]:
                del entry[k]
        records[P["key"]] = entry
    dossier = {"_meta": {"author": "full-review", "date": time.strftime("%Y-%m-%d"),
                         "note": f"full-review {patch['_meta']['round']} (auto fills + approved HOLD items)"},
               "reset_unspecified": False, "records": records}
    return dossier, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("patch")
    ap.add_argument("--approved")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    patch = json.load(open(a.patch))
    rid = patch["_meta"]["round"]
    approved = load_approved(a.approved)

    if a.live:
        go = os.environ.get("FULL_REVIEW_APPLY_GO", "")
        if go != rid:
            sys.exit(f"REFUSED: live apply needs Adam's go for this round (FULL_REVIEW_APPLY_GO={rid}).")
        if patch["_meta"].get("dry_run") is not True:
            sys.exit("REFUSED: unexpected patch shape")

    F = L.Fetcher(tempfile.mkdtemp(prefix="fr-apply-pages-")) if (a.live or a.check) else None
    dossier, report = to_dossier(patch, approved, F)
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.patch)), "apply-dossier.json")
    L.dump_json(out, dossier)
    for r in report:
        print("  ", *r)
    print(f"dossier: {len(dossier['records'])} record(s) -> {out}")
    if not dossier["records"]:
        return
    if a.check and not a.live:
        # existing consistency checks, read-only
        subprocess.run([sys.executable, os.path.join(L.REPO, "refine-records.py"), out, "--dry-run"], cwd=L.REPO)
        return
    if not a.live:
        print("[dry] nothing written. Use --check to run refine-records.py --dry-run on it.")
        return

    # ---------------- live path (only after Adam's go) ----------------
    waited = 0
    while True:
        try:
            os.mkdir(LOCK)
            break
        except FileExistsError:
            if waited > 1500:
                sys.exit("grind lock held — retry later")
            time.sleep(30); waited += 30
    open(OWNER, "w").write(f"full-review-apply {os.getpid()} {time.strftime('%F %T')}\n")
    iso = f"/tmp/scorecard-full-review-apply-{os.getpid()}"
    try:
        main_repo = os.path.expanduser("~/.openclaw/workspace/usmcmin-com")
        subprocess.run(["git", "-C", main_repo, "fetch", "-q", "origin", "main"], check=True)
        subprocess.run(["git", "-C", main_repo, "worktree", "add", "--detach", iso, "origin/main"], check=True)
        os.makedirs(os.path.join(iso, "refinements"), exist_ok=True)
        rel = f"refinements/full-review-{rid}.json"
        shutil.copy2(out, os.path.join(iso, rel))
        r = subprocess.run(["/opt/homebrew/bin/python3", "commit_refinement.py", rel,
                            f"scorecard full-review {rid}: {len(dossier['records'])} record(s), auto fills + approved HOLD"],
                           cwd=iso)
        if r.returncode != 0:
            sys.exit("commit_refinement failed — nothing pushed beyond what it reports")
        stats = L.load_json(L.PUBLIC_STATS, {}) or {}
        print("applied; update data/full-review-stats.json 'applied' from this run's TAKE count:",
              sum(1 for x in report if x[1] == "TAKE"), stats.get("totals"))
    finally:
        subprocess.run(["git", "-C", os.path.expanduser("~/.openclaw/workspace/usmcmin-com"), "worktree", "remove",
                        "--force", iso], stderr=subprocess.DEVNULL)
        try:
            os.remove(OWNER)
        except OSError:
            pass
        os.rmdir(LOCK)


if __name__ == "__main__":
    main()
