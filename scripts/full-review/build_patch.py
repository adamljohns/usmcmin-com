#!/usr/bin/env python3
"""Full-review patch builder. Deterministic: no model calls, no network beyond the round's page cache.

Turns <round>/obs/*.json into
  <round>/review-patch.json   every proposed change, per politician, with per-field evidence
  <round>/hold.json           every HOLD item (changes that wait for Roy QA + needs-ruling + flags + rechecks)
  <STATE>/hold-queue.json     cumulative queue, latest round per politician
  <STATE>/ledger.json         selection rotation state
  data/full-review-stats.json PUBLIC counts only (no names, no evidence)

Gates (all must pass or the item is dropped / held — never scored):
  * evidence quote literally on the cited page (case/whitespace/curly quotes normalized only)
  * score: published rule text found on usmcmin.com for that cell, quoted with the change
  * score: on-topic word gate + second-model cross-check (on topic, direction, about this official)
  * scope: page names the official; third-party passages must name them; joint statements HOLD
  * slogans / fragments stay blank; one quote backs at most 2 cells
  * news/aggregator evidence (rank 5) is never a score: HOLD needs-ruling
  * PAC / foreign-lobby cells are never filled from page text (hit / no-hit / not-run report only)
Gate auto (would apply on a live run) only for high-confidence factual fills of an EMPTY field
(official website, term dates, office phone) from an official structured or official page, and never
for a Fredericksburg / Virginia official. Everything else is HOLD.

Usage: build_patch.py ROUND_DIR [--dry-run]
"""
import argparse
import glob
import json
import os
import re
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fr_lib as L  # noqa: E402

AUTO_FIELDS = {"website", "profile.term_start", "profile.term_end", "profile.phone"}
LETTERS = "FDCBA"
SOCIAL_FIELD = {"twitter.com": "profile.twitter", "x.com": "profile.twitter", "facebook.com": "profile.facebook",
                "youtube.com": "profile.youtube", "instagram.com": "profile.instagram"}
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], 1)}


def iso(d):
    m = re.match(r"(\w+)\s+(\d{1,2}),\s+(\d{4})", d or "")
    if not m or m.group(1).lower() not in MONTHS:
        return None
    return f"{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"


def digits(s):
    return re.sub(r"\D", "", s or "")[-10:]


def handle_of(field, v):
    v = (v or "").strip().lower().lstrip("@").rstrip("/")
    return v.split("/")[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("round_dir")
    ap.add_argument("--dry-run", action="store_true", default=True)
    a = ap.parse_args()
    rd = a.round_dir
    rid = os.path.basename(rd.rstrip("/"))
    sc = json.load(open(L.SCORECARD))
    cats, rubrics = sc["categories"], sc["meta"]["rubrics"]
    by = {f"{c['slug']}@{(c.get('state') or '').upper()}": c for c in sc["candidates"]}
    name_index = Counter((L.norm(c.get("name")), (c.get("state") or "").upper()) for c in sc["candidates"]
                         if c.get("status") in ("active", "lame_duck", None))
    F = L.Fetcher(os.path.join(rd, "pages"))
    rules = L.Rules(F)
    rules.load()
    batch = json.load(open(os.path.join(rd, "batch.json")))
    pols, hold_rows = [], []

    for b in batch:
        fp = os.path.join(rd, "obs", b["key"].replace("/", "_") + ".json")
        c = by.get(b["key"])
        if not os.path.exists(fp) or not c:
            pols.append({"key": b["key"], "name": b.get("name"), "status": "pending" if c else "missing"})
            continue
        obs = json.load(open(fp))
        # The official site found on the official roster this round counts as the person's own site
        # for scope and ranking (e.g. a House member whose record has no website yet).
        c_orig = c
        ro = obs.get("roster", {})
        disc = (ro.get("house_dir") or {}).get("url") or ((ro.get("senate") or {}).get("row") or {}).get("website") \
            or ((ro.get("va_house") or {}).get("row") or {}).get("url") \
            or ((ro.get("va_senate") or {}).get("row") or {}).get("url")
        if disc and not c.get("website"):
            c = dict(c, website=disc)
        tier = L.tier_of(c)
        prof = c.get("profile") or {}
        P = {"key": b["key"], "slug": c["slug"], "state": c.get("state"), "name": c.get("name"),
             "office": c.get("office"), "party": c.get("party"), "tier": tier,
             "selection_tier": b.get("selection_tier"), "fxbg": L.is_fxbg(c), "virginia": L.is_fxbg_or_va(c),
             "record_status": c.get("status"), "candidacy_status": c.get("candidacy_status"),
             "profile_url": f"https://usmcmin.com/candidates/{(c.get('state') or '').lower()}/{c['slug']}.html",
             "headline_before": L.headline(c, cats), "changes": [], "confirms": [], "dropped": [],
             "flags": [], "rechecks": [], "pac": {}, "pages_read": [
                 {k: p.get(k) for k in ("url", "role", "ok", "status", "error", "fetched_url", "archive_of",
                                        "text_file", "raw_file")} for p in obs.get("pages", [])],
             "errors": obs.get("errors", [])}
        n = [0]

        def cid():
            n[0] += 1
            return f"{rid}:{b['key']}:{n[0]}"

        def page_text(url):
            return F.text(F.index.get(url) or {})

        def page_raw(url):
            return F.raw(F.index.get(url) or {})

        def verified(quote, url, raw=False):
            src = page_raw(url) if raw else page_text(url)
            if raw:
                return quote if quote and quote in src else None
            return L.exact_quote(quote, src)

        # ---------------------------------------------------------------- roster (federal XML)
        for src_key in ("house_clerk", "senate"):
            r = obs.get("roster", {}).get(src_key)
            if not r:
                continue
            url = r["source"]
            if not r.get("matched"):
                if F.index.get(url, {}).get("ok"):
                    P["flags"].append({"change_id": cid(), "kind": "flag", "field": "status",
                                       "title": "not found on the official roster — possible out of office or wrong record",
                                       "evidence": {"url": url, "quote": None, "evidence_type": "absence",
                                                    "note": f"no {src_key} row matched {c.get('name')} ({c.get('state')})"},
                                       "gate": "hold", "hold_reasons": ["out-of-office flag (Roy QA)"]})
                continue
            row, blk = r["row"], r.get("raw_block") or ""
            namefrag = (f"<official-name>{row.get('official_name')}</official-name>" if src_key == "house_clerk"
                        else f"<last_name>{row.get('last')}</last_name>")

            def xml_ev(tagfrag):
                """Smallest contiguous slice of this member's XML block holding the name and the field."""
                a_ = blk.find(namefrag); b_ = blk.find(tagfrag)
                if a_ < 0 or b_ < 0:
                    return None
                lo, hi = min(a_, b_), max(a_ + len(namefrag), b_ + len(tagfrag))
                if hi - lo > 900:
                    return None
                return blk[lo:hi]

            # party
            xp = row.get("party")
            rp = (c.get("party") or "").strip()
            if xp and rp[:1].upper() != xp[:1].upper():
                tag = f"<party>{xp}</party>"
                q = xml_ev(tag)
                if q and verified(q, url, raw=True):
                    P["changes"].append({"change_id": cid(), "field": "party", "op": "replace", "old": c.get("party"),
                                         "new": xp, "kind": "roster", "evidence": {"quote": q, "url": url,
                                         "evidence_type": "xml_record", "source_rank": 1}, "confidence": "high"})
            # district (House)
            if src_key == "house_clerk":
                xd = row.get("district")
                rdist = str(c.get("district") or "").lstrip("0")
                if xd and rdist and xd != rdist and not (xd == "AL" and rdist in ("0", "AL", "At-Large")):
                    # the block starts right after <statedistrict>; quote from it through the name
                    full = L.Fetcher.raw(F, F.index.get(url) or {})
                    k = full.find(blk)
                    sdtag = f"<statedistrict>{row['statedistrict']}</statedistrict>"
                    q = None
                    if k >= 0:
                        lo = full.rfind(sdtag, 0, k + 40)
                        hi = full.find("</namelist>", lo)
                        if lo >= 0 and 0 < hi - lo < 300:
                            q = full[lo:hi + len("</namelist>")]
                    if q and verified(q, url, raw=True):
                        P["changes"].append({"change_id": cid(), "field": "district", "op": "replace",
                                             "old": c.get("district"), "new": xd, "kind": "roster",
                                             "evidence": {"quote": q, "url": url, "evidence_type": "xml_record",
                                                          "source_rank": 1}, "confidence": "high"})
                if row.get("sworn"):
                    s = row["sworn"]
                    tag = re.search(r"<sworn-date[^>]*>[^<]*</sworn-date>", blk)
                    q = xml_ev(tag.group(0)) if tag else None
                    new = f"{s[:4]}-{s[4:6]}-{s[6:]}"
                    if q and verified(q, url, raw=True) and prof.get("term_start") != new:
                        P["changes"].append({"change_id": cid(), "field": "profile.term_start",
                                             "op": "fill" if not prof.get("term_start") else "replace",
                                             "old": prof.get("term_start"), "new": new, "kind": "fact",
                                             "evidence": {"quote": q, "url": url, "evidence_type": "xml_record",
                                                          "source_rank": 1,
                                                          "note": "Clerk of the House sworn-in date for the current term"},
                                             "confidence": "high"})
            # phone
            xph = row.get("phone")
            if xph and digits(xph) != digits(prof.get("phone")):
                q = xml_ev(f"<phone>{xph}</phone>")
                if q and verified(q, url, raw=True):
                    P["changes"].append({"change_id": cid(), "field": "profile.phone",
                                         "op": "fill" if not prof.get("phone") else "replace",
                                         "old": prof.get("phone"), "new": xph, "kind": "contact",
                                         "evidence": {"quote": q, "url": url, "evidence_type": "xml_record",
                                                      "source_rank": 1}, "confidence": "high"})
            # senate website
            if src_key == "senate" and row.get("website"):
                w = row["website"]
                if L.domain(w) != L.domain(c_orig.get("website")):
                    q = xml_ev(f"<website>{w}</website>")
                    if q and verified(q, url, raw=True):
                        P["changes"].append({"change_id": cid(), "field": "website",
                                             "op": "fill" if not c_orig.get("website") else "replace",
                                             "old": c_orig.get("website"), "new": w, "kind": "contact",
                                             "evidence": {"quote": q, "url": url, "evidence_type": "xml_record",
                                                          "source_rank": 1}, "confidence": "high"})
        # ---------------------------------------------------------------- roster (Virginia General Assembly)
        for src_key in ("va_house", "va_senate"):
            r = obs.get("roster", {}).get(src_key)
            if not r:
                continue
            url = r["source"]
            if not r.get("matched"):
                if F.index.get(url, {}).get("ok"):
                    P["flags"].append({"change_id": cid(), "kind": "flag", "field": "status",
                                       "title": "not found on the official General Assembly member list — possible "
                                                "out of office or wrong record",
                                       "evidence": {"url": url, "quote": None, "evidence_type": "absence"},
                                       "gate": "hold", "hold_reasons": ["out-of-office flag (Roy QA)"]})
                continue
            row = r["row"]
            q = row.get("snippet")
            if not (q and verified(q, url, raw=True)):
                continue
            ev = {"quote": q, "url": url, "evidence_type": "html_record", "source_rank": 1,
                  "note": "official member list card (name link + district" +
                          (" + party" if src_key == "va_senate" else "") + ")"}
            rdist = str(c.get("district") or "").lstrip("0")
            if row.get("district") and rdist and row["district"] != rdist:
                P["changes"].append({"change_id": cid(), "field": "district", "op": "replace", "old": c.get("district"),
                                     "new": row["district"], "kind": "roster", "evidence": ev, "confidence": "high"})
            if row.get("party") in ("D", "R") and (c.get("party") or "")[:1].upper() != row["party"]:
                P["changes"].append({"change_id": cid(), "field": "party", "op": "replace", "old": c.get("party"),
                                     "new": row["party"], "kind": "roster", "evidence": ev, "confidence": "high"})
            if L.domain(row["url"]) != L.domain(c_orig.get("website")) or not c_orig.get("website"):
                if (c_orig.get("website") or "").rstrip("/") != row["url"]:
                    P["changes"].append({"change_id": cid(), "field": "website",
                                         "op": "fill" if not c_orig.get("website") else "replace",
                                         "old": c_orig.get("website"), "new": row["url"], "kind": "contact",
                                         "evidence": ev, "confidence": "high"})

        hd = obs.get("roster", {}).get("house_dir")
        if hd and hd.get("url") and L.domain(hd["url"]) != L.domain(c_orig.get("website")):
            q = hd.get("snippet")
            if q and verified(q, hd["source"], raw=True):
                P["changes"].append({"change_id": cid(), "field": "website",
                                     "op": "fill" if not c_orig.get("website") else "replace", "old": c_orig.get("website"),
                                     "new": hd["url"].rstrip("/"), "kind": "contact",
                                     "evidence": {"quote": q, "url": hd["source"], "evidence_type": "html_link",
                                                  "source_rank": 1, "note": "house.gov member directory"},
                                     "confidence": "high"})

        # ---------------------------------------------------------------- printed term dates
        term = obs.get("roster", {}).get("term")
        if term:
            q = verified(term["quote"], term["url"])
            if q:
                arch = "web.archive.org" in term["url"]
                for fld, val in (("profile.term_start", iso(term["start"])), ("profile.term_end", iso(term["end"]))):
                    old = prof.get(fld.split(".")[1])
                    if val and old != val:
                        P["changes"].append({"change_id": cid(), "field": fld, "op": "fill" if not old else "replace",
                                             "old": old, "new": val, "kind": "fact",
                                             "evidence": {"quote": q, "url": term["url"], "evidence_type":
                                                          "archive_copy" if arch else "page_text",
                                                          "source_rank": 2, "note": ("Wayback copy of the official page "
                                                          "(live page blocks automated reads)") if arch else None},
                                             "confidence": "medium" if arch else "high"})

        # ---------------------------------------------------------------- social links
        first, last = L.name_parts(c.get("name"))
        for s in obs.get("socials", []):
            host = L.domain(s["url"])
            fld = SOCIAL_FIELD.get(host)
            if not fld:
                continue
            if not (s.get("own_site") or s.get("handle_names_person")):
                P["dropped"].append({"field": fld, "new": s["url"], "reason": "shared site link that does not name "
                                     "this official (e.g. the city's own account)", "url": s.get("page")})
                continue
            old = prof.get(fld.split(".")[1])
            if old and handle_of(fld, old) == handle_of(fld, s["url"]):
                continue
            q = s["quote"] if s["quote"] in page_raw(s["page"]) else None
            if not q:
                continue
            # keep only one proposal per field (first own-site html_link wins)
            if any(ch["field"] == fld for ch in P["changes"]):
                continue
            # store in the profile's own convention: twitter "@handle", facebook/instagram "handle",
            # youtube channel id (the profile template builds the link from it)
            h = s["url"].rstrip("/").split("/")[-1]
            fmt_note = None
            if fld == "profile.twitter":
                newv = "@" + h.lstrip("@")
            elif fld == "profile.youtube":
                if "/channel/" in s["url"]:
                    newv = h
                elif old:
                    P["dropped"].append({"field": fld, "new": s["url"], "url": s.get("page"),
                                         "reason": "stored value is a channel id, page link is a handle: cannot tell if they differ"})
                    continue
                else:
                    newv, fmt_note = s["url"], "youtube value is not a channel id; template link may need review"
            else:
                newv = h
            P["changes"].append({"change_id": cid(), "field": fld, "op": "fill" if not old else "replace", "old": old,
                                 "new": newv, "new_url": s["url"], "format_note": fmt_note, "kind": "contact",
                                 "evidence": {"quote": q, "url": s["page"], "evidence_type": s["evidence_type"],
                                              "source_rank": 2 if s.get("own_site") else 3},
                                 "confidence": "high" if s["evidence_type"] == "html_link" else "low"})

        # ---------------------------------------------------------------- scores
        cand = {}
        quote_uses = Counter()
        for pr in obs.get("proposals", []):
            cat, qi, stance, url = pr["cat"], pr["qi"], pr["stance"], pr["url"]
            cell = f"{cat}[{qi}]"
            text = page_text(url)
            q = L.exact_quote(pr["quote"], text)
            base = {"cell": cell, "stance": stance, "quote": pr["quote"], "url": url}
            if not q:
                P["dropped"].append({**base, "reason": "quote not literally on the cited page"}); continue
            if (cat, qi) in L.PAC_CELLS:
                P["dropped"].append({**base, "reason": "PAC/foreign-lobby cell: affirmative database search only"}); continue
            if L.is_slogan(q):
                P["dropped"].append({**base, "reason": "slogan / fragment — stays blank", "rule": rules.general("slogan")}); continue
            ok, why = L.on_topic(cat, qi, stance == "support", q)
            if not ok:
                P["dropped"].append({**base, "reason": f"off topic: {why}"}); continue
            ctx = L.context_of(q, text)
            sok, swhy, sflags = L.scope_check(c, url, text, q, ctx)
            if not sok:
                P["dropped"].append({**base, "reason": f"scope: {swhy}"}); continue
            cc = pr.get("crosscheck") or {}
            ccs = {k: str(cc.get(k, "")).upper()[:3] for k in ("on_topic", "direction", "about_official",
                                                                 "full_standard")}
            if not all(ccs[k].startswith("YES") for k in ("on_topic", "direction", "about_official")):
                P["dropped"].append({**base, "reason": f"cross-check: {ccs or cc}"}); continue
            rule = rules.for_cell(cat, qi, pr["question"])
            rank, rank_why = L.source_rank(url, c)
            partial = stance == "support" and not ccs["full_standard"].startswith("YES")
            item = {"cat": cat, "qi": qi, "cell": cell, "verdict": stance == "support", "quote": q, "url": url,
                    "partial": partial,
                    "context": ctx, "rule": rule, "rank": rank, "rank_why": rank_why, "scope": swhy,
                    "scope_flags": sflags, "crosscheck": ccs, "archive": "web.archive.org" in url}
            cand.setdefault((cat, qi), []).append(item)

        for (cat, qi), items in sorted(cand.items()):
            items.sort(key=lambda x: (x["rank"], -len(x["quote"])))
            dirs = {x["verdict"] for x in items}
            cur_arr = (c.get("scores") or {}).get(cat) or [None] * 5
            cur = cur_arr[qi] if qi < len(cur_arr) else None
            best = items[0]
            more = [{"quote": x["quote"], "url": x["url"], "verdict": x["verdict"], "source_rank": x["rank"]}
                    for x in items[1:4]]
            ev = {"quote": best["quote"], "url": best["url"], "evidence_type": "archive_copy" if best["archive"]
                  else "page_text", "source_rank": best["rank"], "source_kind": best["rank_why"],
                  "context": best["context"][:700], "scope": best["scope"]}
            field = f"scores.{cat}[{qi}]"
            if len(dirs) > 1:
                P["flags"].append({"change_id": cid(), "kind": "ruling", "field": field,
                                   "title": "needs-ruling: pages point both ways on this question",
                                   "evidence": ev, "evidence_more": more, "gate": "hold",
                                   "hold_reasons": ["conflicting evidence"]})
                continue
            if cur == best["verdict"]:
                # re-check agrees with the stored answer: recorded, never a change
                P["confirms"].append({"field": field, "value": cur, "evidence": ev, "rule": best["rule"],
                                      "partial": best.get("partial"), "source_rank": best["rank"]})
                continue
            if quote_uses[L.norm(best["quote"])] >= L.MAX_CELLS_PER_QUOTE:
                P["dropped"].append({"cell": best["cell"], "quote": best["quote"], "url": best["url"],
                                     "reason": "quote already backs 2 cells"})
                continue
            if not best["rule"]:
                P["flags"].append({"change_id": cid(), "kind": "ruling", "field": field,
                                   "title": "needs-ruling: this cell's question text is not on the published rubric page",
                                   "evidence": ev, "proposed": best["verdict"], "gate": "hold",
                                   "hold_reasons": ["no published rule text"]})
                continue
            if best["rank"] >= 5:
                P["flags"].append({"change_id": cid(), "kind": "ruling", "field": field,
                                   "title": f"needs-ruling: only a news/aggregator page supports {best['verdict']}",
                                   "evidence": ev, "rule": best["rule"], "proposed": best["verdict"], "gate": "hold",
                                   "hold_reasons": ["third-party source — published rule lists votes, official "
                                                    "statements, sponsored bills, campaign sites, social posts"]})
                continue
            if best.get("partial"):
                P["flags"].append({"change_id": cid(), "kind": "ruling", "field": field,
                                   "title": "needs-ruling: evidence meets only part of the rule as written "
                                            "(e.g. a restriction, a reform, or one item of a list)",
                                   "evidence": ev, "evidence_more": more, "rule": best["rule"],
                                   "proposed": best["verdict"], "gate": "hold",
                                   "hold_reasons": ["judgment beyond the written rule"]})
                continue
            if best["scope_flags"]:
                P["flags"].append({"change_id": cid(), "kind": "ruling", "field": field,
                                   "title": "needs-ruling: " + "; ".join(best["scope_flags"]),
                                   "evidence": ev, "rule": best["rule"], "proposed": best["verdict"], "gate": "hold",
                                   "hold_reasons": ["scope: joint statement or another actor in the passage"]})
                continue
            quote_uses[L.norm(best["quote"])] += 1
            op = "fill" if cur in (None,) else "replace"
            P["changes"].append({"change_id": cid(), "field": field, "op": op, "old": cur, "new": best["verdict"],
                                 "kind": "score", "rule": best["rule"], "evidence": ev, "evidence_more": more,
                                 "existing_kind": L.cell_kind(c, cat, qi) if cur is not None else None,
                                 "existing_citations": L.cell_citations(c, cat, qi) if cur is not None else [],
                                 "crosscheck": best["crosscheck"],
                                 "confidence": "medium" if best["archive"] or best["rank"] >= 3 else "high"})

        # ---------------------------------------------------------------- PAC / foreign-lobby report
        for cat, qi in sorted(L.PAC_CELLS):
            appl = {(x, y) for x, y, _ in L.applicable_cells(cats, rubrics, tier)}
            if (cat, qi) not in appl:
                continue
            v = ((c.get("scores") or {}).get(cat) or [None] * 5)[qi]
            cites = L.cell_citations(c, cat, qi)
            P["pac"][f"{cat}[{qi}]"] = ("hit" if v is False and cites else "no-hit" if v is True and cites
                                       else "not-run" if v is None else "answered-without-search-citation")

        # ---------------------------------------------------------------- re-check existing cells
        cited_count = Counter()
        uncited = []
        for cat, qi, _q in L.applicable_cells(cats, rubrics, tier):
            arr = (c.get("scores") or {}).get(cat) or [None] * 5
            v = arr[qi] if qi < len(arr) else None
            if v not in (True, False):
                continue
            cites = L.cell_citations(c, cat, qi)
            for u in cites:
                cited_count[u] += 1
            if not cites:
                uncited.append(f"{cat}[{qi}]={v}")
        if uncited:
            P["rechecks"].append({"change_id": cid(), "kind": "recheck", "field": "scores",
                                  "title": f"{len(uncited)} answered cell(s) have no citation", "cells": uncited,
                                  "op": "research", "evidence": {"url": P["profile_url"], "quote": None,
                                  "note": "no footnote or claim backs these answers (scaffolding or lost citation)"},
                                  "gate": "hold", "hold_reasons": ["uncited answers"]})
        P["citations_unread"] = []
        for r in obs.get("rechecks", []):
            if r.get("skipped"):
                P["citations_unread"].append({"url": r["url"], "why": r["skipped"]})
                continue
            err = str(r.get("error") or "")
            if not r.get("ok"):
                dead = r.get("status") in (404, 410) or "nodename nor servname" in err or "Name or service" in err
                if dead:
                    P["rechecks"].append({"change_id": cid(), "kind": "recheck", "field": "citations",
                                          "title": f"cited source is dead ({r.get('status') or 'no such host'})",
                                          "cells": r["cells"], "evidence": {"url": r["url"], "quote": None},
                                          "gate": "hold", "hold_reasons": ["citation re-check"]})
                else:   # blocked / timeout / pdf: not evidence of a problem, just not re-read this round
                    P["citations_unread"].append({"url": r["url"], "why": err or f"HTTP {r.get('status')}"})
            elif r.get("script_rendered"):
                P["citations_unread"].append({"url": r["url"], "why": "script-rendered page; readable text too thin"})
            elif r.get("names_person") is False:
                P["rechecks"].append({"change_id": cid(), "kind": "recheck", "field": "citations",
                                      "title": "cited page's readable text does not name this official",
                                      "cells": r["cells"], "evidence": {"url": r.get("fetched_url") or r["url"],
                                      "quote": None, "note": "searched the page text for the official's name "
                                      "(first + last, Last, First, or title + surname)"},
                                      "gate": "hold", "hold_reasons": ["scope: citation may not be about this person"]})
        for u, k in cited_count.items():
            if k >= 3 and not L.PLATFORM_URL.search(u):
                P["rechecks"].append({"change_id": cid(), "kind": "recheck", "field": "citations",
                                      "title": f"one source backs {k} answered cells", "evidence": {"url": u, "quote": None},
                                      "gate": "hold", "hold_reasons": ["over-application check"]})

        # ---------------------------------------------------------------- roster consistency flags
        office = c.get("office") or ""
        if c.get("status") in ("active", None) and re.search(r"withdrew|suspended|did not make|not running|lost",
                                                             office, re.I):
            prof_page = next((p for p in obs.get("pages", []) if p.get("role") == "usmcmin-profile" and p.get("ok")), None)
            m_ = re.search(r"[^()·]*(withdrew|suspended|did not make|not running|lost)[^()·]*", office, re.I)
            frag = (m_.group(0).strip(" ·") if m_ else office)
            qv = L.exact_quote(frag, page_text(prof_page["fetched_url"])) if prof_page else None
            P["flags"].append({"change_id": cid(), "kind": "flag", "field": "status",
                               "title": "office text says withdrawn/suspended/lost but status is active",
                               "evidence": {"url": P["profile_url"], "quote": qv, "evidence_type": "page_text",
                                            "record_status": c.get("status"),
                                            "note": "the published profile prints this office text while the record's "
                                                    "status is active; needs an external source before any change"},
                               "rule": rules.general("currency"), "gate": "hold",
                               "hold_reasons": ["out-of-office / candidacy currency (Roy QA)"]})
        if name_index[(L.norm(c.get("name")), (c.get("state") or "").upper())] > 1:
            others = [f"{x['slug']}@{x.get('state')}" for x in sc["candidates"]
                      if L.norm(x.get("name")) == L.norm(c.get("name")) and x.get("state") == c.get("state")
                      and x["slug"] != c["slug"]]
            P["flags"].append({"change_id": cid(), "kind": "flag", "field": "dedupe",
                               "title": "possible duplicate or different person with the same name",
                               "others": others, "evidence": {"url": P["profile_url"], "quote": None},
                               "gate": "hold", "hold_reasons": ["dedupe flags never auto-apply"]})

        # ---------------------------------------------------------------- headline after + gates
        import copy
        c2 = copy.deepcopy(c)
        for ch in P["changes"]:
            if ch["kind"] == "score":
                m = re.match(r"scores\.(\w+)\[(\d)\]", ch["field"])
                cat, qi = m.group(1), int(m.group(2))
                c2["scores"][cat][qi] = ch["new"]
                af = c2.setdefault("answer_footnotes", {}).setdefault(cat, [[], [], [], [], []])
                while len(af) < 5:
                    af.append([])
                af[qi] = ["fr"]
                c2.setdefault("footnotes", {})["fr"] = {"url": ch["evidence"]["url"]}
        after = L.headline(c2, cats)
        P["headline_after"] = after
        bl, al = P["headline_before"]["letter"], after["letter"]
        grade_reasons = []
        if bl is None and al is not None:
            grade_reasons.append("sets a first headline grade")
        if bl and al and bl != al:
            grade_reasons.append(f"headline grade moves {bl} -> {al}")
        if bl and not al:
            grade_reasons.append("headline grade would be withdrawn")
        party_null = (c.get("party") or "").upper()[:1] not in ("R", "D")
        if party_null and al in ("A",) or party_null and after["pct"] >= 100 and al:
            P["flags"].append({"change_id": cid(), "kind": "flag", "field": "headline",
                               "title": "party-null record would show 100/A", "gate": "hold",
                               "evidence": {"url": P["profile_url"], "quote": None},
                               "hold_reasons": ["VM-A: no 100/A on party-null"]})
        for ch in P["changes"]:
            reasons = []
            if ch["kind"] == "score":
                reasons.append("score change: Roy QA")
                reasons += grade_reasons
            if ch["op"] != "fill":
                reasons.append("replaces an existing value")
            if P["virginia"]:
                reasons.append("Fredericksburg/Virginia official")
            if ch["field"] not in AUTO_FIELDS:
                if ch["kind"] != "score":
                    reasons.append("not an auto-apply field (auto: website, term dates, office phone)")
            if ch["confidence"] != "high":
                reasons.append(f"confidence {ch['confidence']}")
            if ch.get("format_note"):
                reasons.append(ch["format_note"])
            if ch["evidence"].get("evidence_type") in ("site-config", "archive_copy"):
                reasons.append(f"evidence type {ch['evidence']['evidence_type']}")
            ch["gate"] = "hold" if reasons else "auto"
            ch["hold_reasons"] = sorted(set(reasons))

        # reachable = at least one page other than our own profile that names this official, or an
        # official roster row matched; otherwise nothing about the person could be read this round
        named = [p for p in obs.get("pages", []) if p.get("ok") and p.get("role") not in ("usmcmin-profile",)
                 and L.page_names_person(page_text(p.get("fetched_url")), c)]
        roster_hit = any(isinstance(v, dict) and v.get("matched") for v in obs.get("roster", {}).values())
        P["status"] = "reviewed" if (named or roster_hit) else "unreachable"
        P["pages_naming_official"] = len(named)
        P["counts"] = {"changes": len(P["changes"]), "auto": sum(ch["gate"] == "auto" for ch in P["changes"]),
                       "hold_changes": sum(ch["gate"] == "hold" for ch in P["changes"]),
                       "rulings": sum(f["kind"] == "ruling" for f in P["flags"]),
                       "flags": sum(f["kind"] == "flag" for f in P["flags"]), "rechecks": len(P["rechecks"]),
                       "confirms": len(P["confirms"]), "dropped": len(P["dropped"])}
        for ch in P["changes"]:
            if ch["gate"] == "hold":
                hold_rows.append({"hold_id": ch["change_id"], "key": P["key"], "name": P["name"], "kind": "change",
                                  "title": f"{ch['field']}: {json.dumps(ch['old'])} -> {json.dumps(ch['new'])}",
                                  "reasons": ch["hold_reasons"], "evidence": ch["evidence"], "rule": ch.get("rule"),
                                  "owner": "Roy QA", "dry_run": True})
        for f in P["flags"] + P["rechecks"]:
            hold_rows.append({"hold_id": f["change_id"], "key": P["key"], "name": P["name"], "kind": f["kind"],
                              "title": f["title"], "field": f.get("field"), "reasons": f.get("hold_reasons"),
                              "evidence": f.get("evidence"), "rule": f.get("rule"),
                              "owner": "Adam/Roy" if f["kind"] == "ruling" else "Roy QA", "dry_run": True})
        pols.append(P)

    reviewed = [p for p in pols if p.get("status") == "reviewed"]
    summary = {
        "round": rid, "dry_run": True, "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "politicians": len(pols), "reviewed": len(reviewed),
        "unreachable": sum(p.get("status") == "unreachable" for p in pols),
        "pending": sum(p.get("status") == "pending" for p in pols),
        "changed": sum(1 for p in pols if p.get("changes")),
        "held": sum(1 for p in pols if any(ch["gate"] == "hold" for ch in p.get("changes", []))
                    or p.get("flags") or p.get("rechecks")),
        "auto_would_apply": sum(p.get("counts", {}).get("auto", 0) for p in pols),
        "applied": 0,
        "items": {"changes": sum(p.get("counts", {}).get("changes", 0) for p in pols),
                  "hold_rows": len(hold_rows),
                  "rulings": sum(p.get("counts", {}).get("rulings", 0) for p in pols),
                  "flags": sum(p.get("counts", {}).get("flags", 0) for p in pols),
                  "rechecks": sum(p.get("counts", {}).get("rechecks", 0) for p in pols),
                  "confirms": sum(p.get("counts", {}).get("confirms", 0) for p in pols),
                  "dropped": sum(p.get("counts", {}).get("dropped", 0) for p in pols)},
        "fxbg_va": sum(1 for p in pols if p.get("virginia")),
        "federal": sum(1 for p in pols if p.get("tier") == "federal"),
    }
    patch = {"_meta": {"round": rid, "dry_run": True, "generated": summary["generated"],
                       "scorecard_sha256_at_build": __import__("hashlib").sha256(open(L.SCORECARD, "rb").read()).hexdigest(),
                       "rules_source": [L.METHOD_URL, "https://usmcmin.com/citizen/<category>.html"],
                       "models": {"extract": os.environ.get("FULL_REVIEW_EXTRACT_MODEL", "qwen/qwen3.6-35b-a3b"),
                                  "crosscheck": os.environ.get("FULL_REVIEW_CHECK_MODEL", "gemma-4-31b-it"),
                                  "endpoint": "LM Studio 127.0.0.1:1234"},
                       "page_cache": os.path.join(rd, "pages")},
             "summary": summary, "politicians": pols}
    L.dump_json(os.path.join(rd, "review-patch.json"), patch)
    L.dump_json(os.path.join(rd, "hold.json"), {"round": rid, "rows": hold_rows})

    # cumulative queue: latest round per politician
    qp = os.path.join(L.STATE_HOME, "hold-queue.json")
    q = L.load_json(qp, {"rows": []}) or {"rows": []}
    keys = {p["key"] for p in pols if p.get("status") in ("reviewed", "unreachable")}
    q["rows"] = [r for r in q["rows"] if r["key"] not in keys] + hold_rows
    q["updated"] = summary["generated"]
    L.dump_json(qp, q)
    lp = os.path.join(L.STATE_HOME, "ledger.json")
    led = L.load_json(lp, {}) or {}
    for p in pols:
        if p.get("status") in ("reviewed", "unreachable"):
            led[p["key"]] = {"last_round": rid, "status": p["status"], "dry_run": True,
                             "changed": bool(p.get("changes")),
                             "held": any(ch["gate"] == "hold" for ch in p.get("changes", [])) or bool(p.get("flags"))
                             or bool(p.get("rechecks"))}
    L.dump_json(lp, led)

    # public dashboard counts (no names, no evidence)
    hist = L.load_json(os.path.join(L.STATE_HOME, "rounds-summary.json"), []) or []
    hist = [h for h in hist if h["round"] != rid] + [summary]
    L.dump_json(os.path.join(L.STATE_HOME, "rounds-summary.json"), hist)
    pub = {"_meta": {"generated": summary["generated"], "note": "RESOLUTE Citizen full-review counts only. "
                     "Evidence and HOLD items are kept off the public site."},
           "last_round": {k: summary[k] for k in ("round", "dry_run", "reviewed", "changed", "held", "unreachable",
                                                    "applied", "auto_would_apply")},
           # distinct politicians, latest review each (re-running a politician does not double count)
           "totals": {"rounds": len(hist), "dry_run_rounds": sum(1 for h in hist if h["dry_run"]),
                      "reviewed": sum(1 for v in led.values() if v.get("status") == "reviewed"),
                      "unreachable": sum(1 for v in led.values() if v.get("status") == "unreachable"),
                      "changed": sum(1 for v in led.values() if v.get("changed")),
                      "held": sum(1 for v in led.values() if v.get("held")),
                      "applied": sum(h["applied"] for h in hist)}}
    L.dump_json(L.PUBLIC_STATS, pub)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
