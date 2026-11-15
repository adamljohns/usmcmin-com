#!/usr/bin/env python3
"""Commerce full review, stage 4: APPLY a review patch. Default is a dry run.

NOT RUN LIVE until Adam's GO after the dry-run results (ticket 2026-11-09).

  apply-full-review-patch.py PATCH.json                       # dry run: prints what would change, writes nothing
  apply-full-review-patch.py PATCH.json --data /tmp/copy.json # dry run against a copy (writes the copy only)
  apply-full-review-patch.py PATCH.json --live [--approved HOLD_IDS.txt] [--push]

What applies:
  * gate=auto changes (hours, phone fills, social links from the business's own site);
  * HOLD rows only when their hold_id is listed in --approved (Roy/Adam QA sign-off file);
  * approved duplicate flags merge through the EXISTING pattern (duplicate_of + publish=false
    + notes_internal with a restore line); approved closure flags retire through the existing
    pattern (closed=true + closed_evidence + publish=false + notes_internal). Nothing is deleted.
Every applied change is re-checked: the field's current value must still equal the patch's
`old` (the grind may have moved it); a mismatch is skipped and reported.

Live run: takes the commerce grind lock (/tmp/commerce-enrichment-round.lock.d) so the grind
cannot overlap, writes data/businesses.json, regenerates the touched profile pages, categories,
stats and full-review counts, runs the integrity checks, commits only those paths, and with
--push does the same pull --rebase / push HEAD:main the grind uses. Deploy doctrine unchanged.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import full_review_common as fr  # noqa: E402

TODAY = date.today().isoformat()
SCRIPTS = Path(__file__).resolve().parent
REPO = fr.ROOT.parents[1]


def get_field(b: dict, field: str):
    if field.startswith("scores."):
        return (b.get("scores") or {}).get(field.split(".", 1)[1], "gray")
    return b.get(field)


def set_field(b: dict, field: str, value) -> None:
    if field.startswith("scores."):
        b.setdefault("scores", {})[field.split(".", 1)[1]] = value
    else:
        b[field] = value


def apply_change(b: dict, c: dict, round_id: str) -> str:
    f, op = c["field"], c["op"]
    if op == "research":
        return "skip: research rows are information for QA, not values"
    if f == "sources" and op == "append":
        srcs = b.setdefault("sources", [])
        if any(str(s.get("url") or "").rstrip("/").lower() == c["new"]["url"].rstrip("/").lower() for s in srcs):
            return "skip: already present"
        srcs.append(dict(c["new"]))
        return "applied"
    cur = get_field(b, f)
    old = c["old"]
    if f == "hours":
        cur = cur or []
        old = old or []
    elif cur in (None,) and old == "":
        cur = ""
    if cur != old:
        return f"skip: stale (current {json.dumps(cur)[:60]} != patch old {json.dumps(old)[:60]})"
    set_field(b, f, c["new"])
    for k, v in (c.get("also_sets") or {}).items():
        if k.startswith("scores."):
            meta = dict((b.get("scores") or {}).get(k.split(".", 1)[1]) or {})
            meta.update(v)
            meta["source_count"] = max(int(meta.get("source_count") or 0), 1)
            meta["concern_count"] = int(meta.get("concern_count") or 0)
            meta["quote"] = c["evidence"]["quote"][:400]
            meta["full_review"] = round_id
            b["scores"][k.split(".", 1)[1]] = meta
        else:
            b[k] = v
    if c["evidence"].get("url") and f != "sources":
        srcs = b.setdefault("sources", [])
        u = c["evidence"]["url"]
        if c["evidence"].get("evidence_type") in ("html_text", "html_link") and not any(str(s.get("url") or "").rstrip("/") == u.rstrip("/") for s in srcs):
            srcs.insert(0, {"url": u, "label": f"Official site — full review {TODAY}"})
    return "applied"


def apply_flag(b: dict, row: dict, round_id: str) -> str:
    kind = row.get("kind", "")          # the flag's own kind (duplicate-candidate, possibly-closed, ...)
    title = row.get("title", "")
    if kind == "duplicate-candidate" and title.startswith("possible duplicate of "):
        target = title.split("possible duplicate of ", 1)[1].split(" ", 1)[0]
        b["duplicate_of"] = target
        b["publish"] = False
        b["notes_internal"] = (str(b.get("notes_internal") or "") + f" FULL-REVIEW {round_id} {TODAY}: folded as duplicate of {target} "
                               f"({title}). Restore: set publish true, drop duplicate_of.").strip()
        return "applied (merged via duplicate_of)"
    if kind in ("possibly-closed", "possibly-closed-or-moved") and "moved" not in title:
        ev = row["evidence"]
        b["closed"] = True
        b.setdefault("closed_evidence", []).append({"label": f"Own site, checked {TODAY}: \"{ev['quote'][:200]}\"", "url": ev["url"]})
        b["publish"] = False
        b["notes_internal"] = (str(b.get("notes_internal") or "") + f" FULL-REVIEW {round_id} {TODAY}: reported closed (see closed_evidence). "
                               "Hidden (publish=false, closed=true). Restore: publish true, drop closed.").strip()
        return "applied (retired via closed)"
    return "skip: flag kind has no automatic apply path; handle by hand"


def checks(before: dict, after: dict) -> list[str]:
    errs = []
    sb = [b["slug"] for b in before["businesses"]]
    sa = [b["slug"] for b in after["businesses"]]
    if sb != sa:
        errs.append("slug list changed (a listing was added, removed or reordered)")
    json.loads(json.dumps(after))
    for b in after["businesses"]:
        if b.get("hours") is not None and not isinstance(b["hours"], list):
            errs.append(f"{b['slug']}: hours not a list")
    return errs


def write_data(path: Path, data: dict, template: str) -> None:
    compact = "\n" not in template.strip()
    ascii_ = "\\u" in template[:200000]
    txt = json.dumps(data, ensure_ascii=ascii_, separators=(",", ":")) if compact else json.dumps(data, ensure_ascii=ascii_, indent=2) + "\n"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(txt)
    tmp.replace(path)


def main():
    args = sys.argv[1:]
    patch_path = Path(args[0])
    live = "--live" in args
    push = "--push" in args
    data_path = Path(args[args.index("--data") + 1]) if "--data" in args else fr.DATA
    approved = set()
    if "--approved" in args:
        approved = {l.strip() for l in Path(args[args.index("--approved") + 1]).read_text().splitlines() if l.strip() and not l.startswith("#")}
    if live and data_path != fr.DATA:
        sys.exit("--live writes the canonical data file only")
    if not live and data_path == fr.DATA and "--data" in args:
        sys.exit("refusing: a dry run never writes the canonical data file")
    patch = json.load(open(patch_path))
    round_id = patch["round_id"]
    holds = {r["hold_id"]: r for r in json.load(open(patch_path.parent / "hold.json"))["rows"]}

    lock_taken = False
    if live:
        try:
            fr.GRIND_LOCK.mkdir()
            lock_taken = True
        except FileExistsError:
            sys.exit("GRIND_RUNNING: commerce grind holds its lock; try again after the round")
    try:
        raw = data_path.read_text()
        before = json.loads(raw)
        data = copy.deepcopy(before)
        idx = {b["slug"]: b for b in data["businesses"]}
        sha_now = fr.sha256_file(data_path)
        report = {"round_id": round_id, "mode": "live" if live else "dry-run", "data_sha256_before": sha_now,
                  "patch_built_on_sha": patch["data_sha256_at_build"], "results": []}
        touched = set()
        for e in patch["businesses"]:
            b = idx.get(e["slug"])
            if not b:
                continue
            for c in e["changes"]:
                if c["gate"] == "auto" or c["change_id"] in approved:
                    r = apply_change(b, c, round_id)
                    report["results"].append({"id": c["change_id"], "slug": b["slug"], "field": c["field"], "result": r})
                    if r == "applied":
                        touched.add(b["slug"])
            for f in e["flags"]:
                if f["flag_id"] in approved:
                    r = apply_flag(b, f, round_id)
                    report["results"].append({"id": f["flag_id"], "slug": b["slug"], "field": f["kind"], "result": r})
                    if r.startswith("applied"):
                        touched.add(b["slug"])
            b["full_review"] = {"verified_at": TODAY, "round": round_id}
        errs = checks(before, data)
        report["checks"] = errs or ["ok: slugs unchanged, nothing deleted, hours lists valid, JSON round-trips"]
        report["applied"] = sum(1 for r in report["results"] if r["result"].startswith("applied"))
        report["touched"] = sorted(touched)
        if errs:
            print(json.dumps(report, indent=1))
            sys.exit("CHECKS FAILED: nothing written")
        if not live and "--data" not in args:
            print(json.dumps(report, indent=1))
            print(f"DRY RUN: {report['applied']} change(s) would apply to {len(touched)} listing(s). Nothing written.")
            return
        write_data(data_path, data, raw)
        if not live:
            print(json.dumps(report, indent=1))
            print(f"DRY RUN on copy {data_path}: {report['applied']} applied there. Canonical file untouched.")
            return
        # live: regenerate + ledger + path-scoped commit
        py = sys.executable
        for s in sorted(touched):
            subprocess.run([py, str(SCRIPTS / "render-profile.py"), s], cwd=fr.ROOT, check=True)
        subprocess.run([py, str(SCRIPTS / "build-categories.py")], cwd=fr.ROOT, check=True)
        subprocess.run([py, str(SCRIPTS / "build-stats.py")], cwd=fr.ROOT, check=True, stdout=subprocess.DEVNULL)
        led_path = fr.FR_HOME / "applied-ledger.json"
        led = json.load(open(led_path)) if led_path.exists() else {"applied": []}
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        led["applied"] += [dict(r, round=round_id, at=stamp) for r in report["results"] if r["result"].startswith("applied")]
        fr.dump(led, led_path)
        subprocess.run([py, str(SCRIPTS / "build-full-review-stats.py")], cwd=fr.ROOT, check=True)
        paths = ["fxbg/commerce/data/businesses.json", "fxbg/commerce/data/stats.json", "fxbg/commerce/data/full-review-stats.json",
                 "fxbg/commerce/data/directory-index.json", "fxbg/commerce/categories"] + [f"fxbg/commerce/business/{s}.html" for s in sorted(touched)]
        subprocess.run(["git", "add", "--"] + paths, cwd=REPO, check=True)
        msg = (f"commerce full review {round_id}: apply {report['applied']} change(s) to {len(touched)} listing(s)\n\n"
               f"Auto-gated factual fills from each business's own site plus QA-approved HOLD rows. Patch: {patch_path}")
        subprocess.run(["git", "commit", "-m", msg], cwd=REPO, check=True)
        if push:
            for i in range(4):
                if subprocess.run(["git", "pull", "-q", "--rebase", "--autostash", "origin", "main"], cwd=REPO).returncode == 0 and \
                   subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=REPO).returncode == 0:
                    break
            else:
                sys.exit("FAILED: push rejected 4x — commit left local")
        print(json.dumps(report, indent=1))
    finally:
        if lock_taken:
            fr.GRIND_LOCK.rmdir()


if __name__ == "__main__":
    main()
