#!/usr/bin/env python3
"""submit-scorecard-update.py — PSA correction intake with a MECHANICAL verification gate.

Lets an agent (Sheriff Roy et al.) PROPOSE scorecard updates without ever being trusted to
write them: every proposed cell must carry an exact quote + source URL, and this validator
re-fetches each source and verbatim-verifies the quote before anything becomes a dossier.
Grok/Gemma/whoever proposes; the machine decides. Unverified cells are DROPPED and reported.

Proposal file shape (author with `write`, then run this):
{
  "author": "sheriff-roy",
  "note": "why these corrections",
  "records": {
    "<slug>@<ST>": {
      "evidence": { "<category_id>": { "<q_idx>": {
          "v": true|false,
          "quote": "sentence copied EXACTLY from the source page",
          "src": "https://..." } } },
      "set": { "candidacy_status": "...", "status": "..." },   # optional currency fixes
      "set_src": "https://...",     # REQUIRED if "set" present: page naming the candidate
      "note": "one-line reason"
    }
  }
}

Rules enforced here (mirror the grind's):
  - evidence cell verifies only if quote appears VERBATIM in the fetched src page;
  - one quote may back at most 2 cells (MAX_CELLS_PER_QUOTE);
  - "set" (status) changes verify only if set_src fetches AND contains the candidate's surname;
  - confidence: evidence_<tier> ONLY when >=1 cell verified; otherwise the record's existing
    confidence is re-stated verbatim (banking/status-fixes are NOT evidence — the 7-16 lesson).

Usage:
  submit-scorecard-update.py PROPOSAL.json                # validate -> write dossier + report (dry)
  submit-scorecard-update.py PROPOSAL.json --apply        # ...then apply+build+push via commit_refinement
"""
import json, os, re, subprocess, sys, time

sys.path.insert(0, ".")
import importlib.util
_spec = importlib.util.spec_from_file_location("lpe", "local-politician-extract.py")
lpe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lpe)   # fetch/to_text/norm + MAX_CELLS_PER_QUOTE — one implementation

CONF = {"federal": "evidence_federal", "state": "evidence_state", "local": "evidence_local"}


def main():
    prop_path = sys.argv[1]
    apply_now = "--apply" in sys.argv
    prop = json.load(open(prop_path))
    author = re.sub(r"[^a-z0-9-]", "", str(prop.get("author") or "psa").lower()) or "psa"
    today = time.strftime("%Y-%m-%d")

    sc = json.load(open("data/scorecard.json"))
    by = {}
    for c in sc["candidates"]:
        by.setdefault(c.get("slug"), []).append(c)

    def resolve(key):
        slug, _, st = key.partition("@")
        m = by.get(slug, [])
        if len(m) == 1 and not st:
            return m[0]
        want = (st or "").upper()
        nar = [c for c in m if (c.get("state") or "").upper() == want]
        return nar[0] if len(nar) == 1 else None

    records, report = {}, {"verified_cells": 0, "dropped": [], "status_fixes": 0, "skipped_records": []}
    page_cache = {}

    def get_page(url):
        if url not in page_cache:
            try:
                page_cache[url] = lpe.norm(lpe.to_text(lpe.fetch(url)))
            except Exception:
                page_cache[url] = None
        return page_cache[url]

    for key, entry in (prop.get("records") or {}).items():
        cand = resolve(key)
        if not cand:
            report["skipped_records"].append({"key": key, "reason": "slug not resolved (use slug@ST)"})
            continue
        tier = cand.get("level") or "state"
        quote_uses, evidence, srcs = {}, {}, []

        for cat, qs in (entry.get("evidence") or {}).items():
            for qi, cell in (qs or {}).items():
                quote, src, v = str(cell.get("quote") or ""), cell.get("src"), cell.get("v")
                where = f"{key}:{cat}[{qi}]"
                if v not in (True, False) or not quote or not src:
                    report["dropped"].append({"cell": where, "reason": "needs v + quote + src"})
                    continue
                nq = lpe.norm(quote)
                if quote_uses.get(nq, 0) >= lpe.MAX_CELLS_PER_QUOTE:
                    report["dropped"].append({"cell": where, "reason": "quote_overused (max 2 cells/quote)"})
                    continue
                page = get_page(src)
                if page is None:
                    report["dropped"].append({"cell": where, "reason": f"source unreachable: {src}"})
                    continue
                if nq not in page:
                    report["dropped"].append({"cell": where, "reason": "quote NOT verbatim on source page"})
                    continue
                quote_uses[nq] = quote_uses.get(nq, 0) + 1
                evidence.setdefault(cat, {})[str(qi)] = {
                    "v": bool(v), "src": [src],
                    "note": (entry.get("note") or quote)[:400],
                }
                srcs.append(src)
                report["verified_cells"] += 1

        rec_out = {}
        set_block = entry.get("set") or {}
        if set_block:
            ssrc = entry.get("set_src")
            surname = (cand.get("name") or "").split()[-1].lower()
            page = get_page(ssrc) if ssrc else None
            if not ssrc or page is None or (surname and surname not in page):
                report["skipped_records"].append(
                    {"key": key, "reason": "status fix rejected: set_src missing/unreachable/doesn't name candidate"})
            else:
                rec_out["set"] = set_block
                srcs.append(ssrc)
                report["status_fixes"] += 1

        if evidence:
            rec_out["evidence"] = evidence
            rec_out["profile"] = {"confidence": CONF.get(tier, "evidence_state"),
                                  "confidence_note": f"PSA-submitted, verbatim-verified intake ({author}) {today}",
                                  "last_refined": today}
        elif rec_out:
            # status-only fix: NOT evidence — re-state existing confidence so the engine
            # default can't promote the record (the 2026-07-16 lesson).
            rec_out["profile"] = {"confidence": (cand.get("profile") or {}).get("confidence")}

        if rec_out:
            if srcs:
                rec_out["sources_add"] = sorted(set(srcs))
            rec_out["notes_append"] = f"{author} correction {today}: {entry.get('note') or 'verified intake'}"
            records[key] = rec_out

    if not records:
        print("NOTHING VERIFIED — no dossier written. Dropped/skipped detail:")
        print(json.dumps(report, indent=1))
        return 1

    os.makedirs("refinements", exist_ok=True)
    dpath = f"refinements/psa-{author}-{time.strftime('%Y-%m-%d-%H%M')}.json"
    json.dump({"_meta": {"author": author, "date": today,
                         "note": f"PSA intake ({author}) — mechanically verbatim-verified"},
               "reset_unspecified": False, "records": records}, open(dpath, "w"), indent=1)
    print(f"VERIFIED: {report['verified_cells']} cell(s) + {report['status_fixes']} status fix(es) "
          f"across {len(records)} record(s) -> {dpath}")
    if report["dropped"] or report["skipped_records"]:
        print("DROPPED (not applied — fix or discard):")
        for d in report["dropped"] + report["skipped_records"]:
            print(f"  - {d}")

    if apply_now:
        subj = f"psa({author}): {report['verified_cells']} verified cell(s), {report['status_fixes']} status fix(es) (verbatim-gated intake)"
        rc = subprocess.call(["/opt/homebrew/bin/python3", "commit_refinement.py", dpath, subj])
        return rc
    print("\nDry validation only. Review the dossier, then apply with:")
    print(f"  /opt/homebrew/bin/python3 commit_refinement.py {dpath} \"psa({author}): verified intake\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
