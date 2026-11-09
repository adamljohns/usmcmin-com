#!/usr/bin/env python3
"""Commerce full review, stage 3: turn observations into a REVIEW PATCH + HOLD queue.

Deterministic. No model, no network. Reads data/businesses.json read-only.

Gates (ticket 2026-11-09 + church full-review lessons):
  * No URL or quote, no change. Every quote is re-located verbatim in the cached page
    text (html_text) or is the exact raw <a ...> tag / config snippet (html_link /
    site-config) captured from the page HTML. Unverifiable evidence is dropped.
  * Evidence must be ON TOPIC for the field (phone digits in the quote, the parsed
    hours equal the proposal, the owner's name next to an ownership word, ...).
  * Scope: evidence must be about THIS business at THIS location. On a multi-location
    site only a page that prints this location's street/phone and no other street counts
    as in scope; passages about partners, sponsors, other locations or other towns drop.
  * Auto (would apply on a live run) ONLY: hours, phone fill, social link, from the
    business's own (not recovered) site, in scope, high confidence. Everything else HOLD.
  * Score proposals only move a factor OFF Gray (insufficient evidence). An existing
    Yellow/Red/Green is never overridden by this mode.
  * Scores come only from rules printed on methodology.html; each score change cites the
    rule text. A judgment no written rule covers is a HOLD "needs-ruling" row, never a score.
    All score changes are HOLD (QA: Sheriff Roy, FXBG civic lane).
  * Closures, moves, renames, duplicates/merges, category changes: HOLD flags, never auto.
  * Website recovery (no site on file): always HOLD.

Usage: full-review-build-patch.py OBSERVATIONS.json ROUND_DIR [--round-id ID]
Writes ROUND_DIR/review-patch.json, ROUND_DIR/hold.json; updates FR_HOME/hold-queue.json.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import full_review_common as fr  # noqa: E402
from commerce_common import load_osm_tags, osm_tags_for  # noqa: E402

TODAY = date.today().isoformat()
AUTO_FIELDS = {"phone", "hours", "sources"}          # + web only via own-site evidence (never recovery)
PLACEHOLDER_OWNER = re.compile(r"imported from openstreetmap|pending christ-centered|^\s*$", re.I)
OWNER_WORD = re.compile(r"\b(owner|owners|owned|own(s|ed)? and operat|founder|founded|co-founder|president|proprietor|"
                        r"operat(or|ed|es)|ceo|principal|managing (partner|member)|general manager|family[- ]owned)\b", re.I)
OUT_OF_SCOPE = re.compile(r"\b(sponsor(s|ed|ship)?|our partners?|partnered with|proud(ly)? (to )?support|in partnership|"
                          r"other locations?|sister (company|business|store|location)|also owns?|our [A-Z][a-z]+ location|"
                          r"locations? in [A-Z][a-z]+|franchise opportunit|vendor|supplier)\b", re.I)
SUBHOURS = re.compile(r"\b(kitchen|bar|brunch|happy hour|holiday|thanksgiving|christmas|summer|winter|seasonal|"
                      r"drive[- ]?thru|lobby|pharmacy|service department|parts department|showroom|office hours|"
                      r"by appointment|appointment only|delivery|curbside|breakfast|lunch|dinner)\b", re.I)
FAITH_RE = re.compile(r"\b(christian[- ]owned|faith[- ]based (business|company)|christ[- ]centered|glorify (god|christ)|"
                      r"honou?r(s|ing)? (god|christ|the lord|jesus)|our faith in (jesus|christ|god)|biblical principles|"
                      r"kingdom (business|company)|serve (god|christ|the lord) through|colossians 3:23|proverbs \d+:\d+|"
                      r"jesus christ is|god first|faith,? family,? (and )?(service|business))\b", re.I)
LICENSE_SELF = re.compile(r"\b(licensed|bonded|insured)\b", re.I)
FACTOR_TOPIC = {
    "worker_dignity": re.compile(r"\b(employee|employees|staff|team member|career|careers|wage|wages|pay|benefit|benefits|"
                                 r"training|paid time|401|health insurance|workplace|hiring|we hire|treat)\w*", re.I),
    "community_fruit": re.compile(r"\b(community|local|locally|neighbor|charity|donat|volunteer|years|since \d{4}|family[- ]owned|"
                                  r"serv(e|ing) (the )?(fredericksburg|stafford|spotsylvania|area))\w*", re.I),
    "truth": re.compile(r"\b(price|pricing|upfront|up-front|honest|transparen|estimate|quote|guarantee|warrant)\w*", re.I),
    "family_safety": re.compile(r"\b(family|families|kid|kids|child|children|all ages|age|safe)\w*", re.I),
    "reliability": re.compile(r"\b(on time|guarantee|warrant|24/7|same[- ]day|emergency|reliab|show up|dependab)\w*", re.I),
    "network_worthiness": re.compile(r"\b(refer|recommend|trusted|integrity|reputation)\w*", re.I),
}
SOCIAL_LABEL = fr.SOCIAL_LABEL
STATES = set("AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC Virginia".split())


class Builder:
    def __init__(self, round_id: str, biz: dict, obs: dict, data_index: dict, osm: dict):
        self.round_id, self.biz, self.obs = round_id, biz, obs
        self.data_index, self.osm = data_index, osm
        self.changes, self.flags, self.rulings, self.confirm, self.scope_dropped, self.lookups = [], [], [], [], [], []
        self.n = 0
        self.dropped_unverifiable = 0
        src = obs if obs.get("pages") else ((obs.get("recovery") or {}).get("review") or {})
        self.src = src
        self.recovered = bool(src) and src is not obs
        self.pages = [dict(p, norm=fr.nrm(p["text"])) for p in (src.get("pages") or [])]
        self.multi = fr.detect_multi(self.pages, src.get("raw_flags")) or src.get("multi_location")
        self.site_identity = src.get("site_identity") or []
        self.tags = osm_tags_for(biz, osm)
        self.chain = bool(self.tags.get("brand") or self.tags.get("brand:wikidata"))

    # ── scope ──
    def other_streets(self, page) -> set:
        no, word = fr.stored_street(self.biz)
        out = set()
        for m in fr.STREET_RE.finditer(page["text"]):
            key = fr.nrm(m.group(1) + " " + m.group(2).split()[0])
            if not (no and word and key == fr.nrm(f"{no} {word}")):
                out.add(key)
        return out

    def page_scope(self, url: str) -> tuple[bool, str]:
        page = next((p for p in self.pages if p["url"] == url), None)
        if not page:
            return False, "page not in fetched set"
        if not self.site_identity:
            return False, "site never prints this listing's street, ZIP or phone"
        return True, ""

    def location_reasons(self, quote: str, url: str, etype: str) -> list[str]:
        """Location gate. Auto needs the exact page holding the quote to print the stored street
        or ZIP (a shared phone, or nothing, is not location identity). On a multi-location or
        chain site the evidence must also come from this location's own page or section."""
        page = next((p for p in self.pages if p["url"] == url), None)
        if not page:
            return ["evidence page not in the fetched set"]
        out = []
        if not fr.location_identity(self.biz, page["text"]):
            out.append("location gate: the page holding the quote does not print the stored street or the stored ZIP in an address "
                       f"(page identity: {', '.join(page['identity']) or 'none'}; a shared phone or a service-area ZIP list is not location identity)")
        if self.multi or self.chain:
            own = fr.own_location(self.biz, page["text"], quote) if etype == "html_text" else (
                "own-page" if fr.own_location(self.biz, page["text"], "") == "own-page" else None)
            if not own:
                out.append("multi-location/chain site: evidence is not from this location's own page or section"
                           + (f" ({self.multi['why']})" if self.multi else " (chain brand)"))
        return out

    def quote_scope(self, quote: str, url: str) -> tuple[bool, str]:
        ok, why = self.page_scope(url)
        if not ok:
            return False, why
        m = OUT_OF_SCOPE.search(quote or "")
        if m:
            return False, f"passage is about '{m.group(0)}' (partner/sponsor/other location)"
        for cm in re.finditer(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?),\s*(Virginia|[A-Z]{2})\b", quote or ""):
            if cm.group(2) not in STATES:
                continue
            town, st = cm.group(1).lower(), cm.group(2)
            if st not in ("VA", "Virginia"):
                return False, f"passage names another state ({cm.group(0)})"
            if town not in fr.LOCAL_TOWNS and not any(t in town for t in fr.LOCAL_TOWNS):
                return False, f"passage names another town ({cm.group(0)})"
        return True, ""

    # ── evidence ──
    def verify_text(self, quote: str, url: str | None = None) -> str | None:
        u = fr.locate(quote, [p for p in self.pages if (url is None or p["url"] == url)]) or fr.locate(quote, self.pages)
        if not u:
            self.dropped_unverifiable += 1
        return u

    def add(self, field, op, old, new, quote, url, confidence, auto_ok, reasons, etype="html_text",
            also=None, rule=None, more=None, note=None):
        if old == new and op not in ("research",):
            return
        if not url or not quote:
            return
        if etype == "html_text":
            located = self.verify_text(quote, url)
            if not located:
                return
            url = url if fr.locate(quote, [p for p in self.pages if p["url"] == url]) else located
            quote = fr.display_quote(quote)
        reasons = list(reasons)
        if etype in ("html_text", "html_link"):
            raw_quote = quote if etype == "html_link" else fr.nrm(quote)
            for r in self.location_reasons(raw_quote, url, etype):
                if r not in reasons and not (field == "sources" and r.startswith("multi-location") and any(x.startswith("multi-location") for x in reasons)):
                    reasons.append(r)
        if self.recovered:
            reasons.append("evidence from a recovered website (website recovery is always HOLD)")
        if confidence != "high":
            reasons.append(f"confidence {confidence}")
        gate = "auto" if (auto_ok and not reasons and confidence == "high") else "hold"
        self.n += 1
        ch = {"change_id": f"{self.round_id}:{self.biz['slug']}:{self.n}", "field": field, "op": op, "old": old, "new": new,
              "confidence": confidence, "gate": gate, "hold_reasons": reasons if gate == "hold" else [],
              "evidence": {"url": url, "quote": quote, "evidence_type": etype}}
        if also:
            ch["also_sets"] = also
        if rule:
            ch["rule"] = rule
        if more:
            ch["evidence_more"] = more
        if note:
            ch["note"] = note
        self.changes.append(ch)

    def flag(self, kind, title, evidence, more=None, severity="hold"):
        if evidence.get("evidence_type") == "html_text":
            evidence = dict(evidence, quote=fr.display_quote(evidence["quote"]))
        self.n += 1
        self.flags.append({"flag_id": f"{self.round_id}:{self.biz['slug']}:{self.n}", "kind": kind, "title": title,
                           "evidence": evidence, **({"evidence_more": more} if more else {}), "gate": severity})

    def ruling(self, title, factor, quote, url, lean=None, why=""):
        self.n += 1
        self.rulings.append({"hold_id": f"{self.round_id}:{self.biz['slug']}:{self.n}", "kind": "ruling",
                             "title": f"needs-ruling: {title}", "factor": factor, "model_lean": lean,
                             "why_no_score": why or "no rule printed on methodology.html maps this evidence to a band",
                             "evidence": {"url": url, "quote": fr.display_quote(quote), "evidence_type": "html_text"}})

    # ── fields ──
    def do_website(self):
        b, o = self.biz, self.obs
        rv = o.get("recovery") or {}
        if rv.get("site") and not str(b.get("web") or "").startswith("http"):
            cand = next((c for c in rv["candidates"] if c.get("accepted")), {})
            ev = cand.get("evidence") or {}
            if ev.get("quote") and fr.locate(ev["quote"], self.pages):
                self.add("web", "fill", b.get("web") or "", rv["site"], ev["quote"], ev["url"], "medium", False,
                         [f"website recovery via {cand.get('via')}: always HOLD; page prints {', '.join(m for m in cand.get('matched', []) if not m.startswith('rejected'))}"],
                         note="candidate page prints the business name and this listing's identifiers")
        dead = o.get("stored_site_dead")
        if dead:
            sts = [a.get("status") for a in dead.get("attempts") or []]
            st0 = sts[0] if sts else None
            if st0 in (401, 403, 405, 406, 429):
                # bot wall (Akamai/Cloudflare etc.), not evidence the site is down
                self.flag("site-blocks-bots", f"stored website refused an automated read (HTTP {st0}); not reviewed",
                          {"url": dead["url"], "quote": f"HTTP result: {sts[:1]}", "evidence_type": "http_status"}, severity="info")
                return
            if isinstance(st0, int) and (200 <= st0 < 400 or st0 >= 500) or st0 == "error:TimeoutError":
                # loads but renders no readable text (script-only page), or a transient server error
                why = "loads but has no readable text (script-rendered page)" if isinstance(st0, int) and st0 < 400 else f"server error / timeout ({st0}); retry next round"
                self.flag("site-not-readable", f"stored website {why}; not reviewed",
                          {"url": dead["url"], "quote": f"HTTP result: {sts[:1]}", "evidence_type": "http_status"}, severity="info")
                return
            self.flag("site-unreachable", f"stored website did not load ({sts[:1]})",
                      {"url": dead["url"], "quote": f"HTTP result: {sts[:1]}", "evidence_type": "http_status"})
            di = (b.get("scores") or {}).get("digital_integrity")
            if di == "green":
                self.n += 1
                self.changes.append({"change_id": f"{self.round_id}:{b['slug']}:{self.n}", "field": "scores.digital_integrity",
                                     "op": "set", "old": "green", "new": "yellow", "confidence": "medium", "gate": "hold",
                                     "hold_reasons": ["lowering a methodology score: QA", "one failed fetch; recheck before applying"],
                                     "rule": fr.rule("f9", "yellow"),
                                     "evidence": {"url": dead["url"], "quote": f"HTTP result: {sts[:1]}", "evidence_type": "http_status"}})
        site = (self.src.get("site") or {})
        start, final = site.get("start_url"), site.get("final_url")
        if not self.recovered and start and final and fr.host_of(start) != fr.host_of(final) and not fr.host_of(final).endswith(fr.host_of(start)):
            self.add("web", "replace", b.get("web"), final.rstrip("/") + "/", f"{start} -> {final}", final, "medium", False,
                     ["stored website redirects to another domain (rename/acquisition?)"], etype="http_redirect")
        if self.src.get("raw_flags", {}).get("parked"):
            pk = self.src["raw_flags"]["parked"]
            self.flag("possibly-closed", "website looks parked / for sale", {"url": pk["url"], "quote": pk["quote"], "evidence_type": "html_text"})

    def do_phone(self):
        b = self.biz
        stored = fr.digits(b.get("phone"))
        if not self.pages:
            return
        phones = self.src.get("phones_on_site") or []
        tel = {t["digits"]: t for t in self.src.get("tel_links") or []}
        found = {p["digits"] for p in phones} | set(tel)
        if stored and stored in found:
            self.confirm.append({"field": "phone", "value": b.get("phone"), "url": next((p["url"] for p in phones if p["digits"] == stored), (tel.get(stored) or {}).get("url"))})
            return
        no, word = fr.stored_street(b)
        cands = []
        for p in self.pages:
            ok, why = self.page_scope(p["url"])
            if not ok:
                continue
            for m in fr.PHONE_RE.finditer(p["text"]):
                if fr.junk_phone(m.group(0)):
                    continue
                ctx = p["text"][max(0, m.start() - 90): m.end() + 90]
                if re.search(r"\bfax\b", p["text"][max(0, m.start() - 12): m.start()], re.I):
                    continue
                near = bool(no and word and re.search(re.escape(no) + r"\s+(?:[NSEW]\.?\s+)?" + re.escape(word), ctx, re.I))
                cands.append({"digits": fr.digits(m.group(0)), "url": p["url"], "near_street": near,
                              "quote": fr.snippet(p["text"], m.start(), m.end(), 200)})
        if not cands:
            return
        near = [c for c in cands if c["near_street"]]
        pool = near or cands
        distinct = sorted({c["digits"] for c in pool})
        best = next(c for c in pool if c["digits"] == distinct[0]) if len(distinct) == 1 else None
        if not best:
            self.flag("phone-ambiguous", f"site prints {len(distinct)} different phone numbers; none chosen",
                      {"url": pool[0]["url"], "quote": pool[0]["quote"], "evidence_type": "html_text"},
                      more=[{"url": c["url"], "quote": c["quote"]} for c in pool[1:4]])
            return
        new = f"({best['digits'][:3]}) {best['digits'][3:6]}-{best['digits'][6:]}"
        if not fr.digits(best["quote"]) or best["digits"] not in re.sub(r"\D", "", best["quote"]):
            return
        if stored:
            self.add("phone", "replace", b.get("phone"), new, best["quote"], best["url"], "medium", False,
                     ["correcting a stored phone: the stored number is not printed anywhere on the site"])
        else:
            conf = "high" if (best["near_street"] or len(cands) == 1 or len({c['digits'] for c in cands}) == 1) else "medium"
            self.add("phone", "fill", "", new, best["quote"], best["url"], conf, True, [])

    def check_moved(self):
        """possibly_moved: the stored URL's own site prints a different street (and a different
        phone, or our phone) than the listing. HOLD flag with both values; never auto."""
        b = self.biz
        if self.recovered or not self.pages or self.multi or self.chain:
            return
        no, word = fr.stored_street(b)
        if not (no and word) or any(h.startswith("street:") for h in self.site_identity):
            return
        site_addr = None
        for p in sorted(self.pages, key=lambda p: p["kind"] != "home"):
            for m in fr.STREET_RE.finditer(p["text"]):
                if fr.ZIP_RE.search(p["text"][m.end(): m.end() + 80]):
                    q = fr.snippet(p["text"], m.start(), m.end() + 40, 200)
                    if fr.locate(q, self.pages):
                        site_addr = {"url": p["url"], "quote": q, "street": m.group(0).strip()}
                        break
            if site_addr:
                break
        site_phones = [x for x in (self.src.get("phones_on_site") or []) if not fr.junk_phone(x["digits"])]
        stored_ph = fr.digits(b.get("phone"))
        phone_match = "phone" in self.site_identity
        other_phone = next((x for x in site_phones if x["digits"] != stored_ph), None)
        if not site_addr or not (phone_match or other_phone):
            return
        stored = {"address": b.get("address"), "zip": b.get("zip"), "phone": b.get("phone")}
        site = {"street": site_addr["street"], "phone": (f"({other_phone['digits'][:3]}) {other_phone['digits'][3:6]}-{other_phone['digits'][6:]}"
                                                       if other_phone and not phone_match else b.get("phone"))}
        how = "matched by phone" if phone_match else "neither the stored street nor the stored phone appears on the site"
        more = [{"url": other_phone["url"], "quote": fr.display_quote(other_phone["quote"]), "what": "phone the site prints"}] if other_phone and not phone_match else None
        self.n += 1
        self.flags.append({"flag_id": f"{self.round_id}:{b['slug']}:{self.n}", "kind": "possibly_moved",
                           "title": f"possibly moved / record mismatch: listing {stored['address']} {stored['phone'] or ''} vs site {site['street']} {site['phone'] or ''} ({how})",
                           "stored": stored, "site": site,
                           "evidence": {"url": site_addr["url"], "quote": fr.display_quote(site_addr["quote"]), "evidence_type": "html_text"},
                           **({"evidence_more": more} if more else {}), "gate": "hold"})

    def do_address(self):
        b = self.biz
        if not self.pages or not self.site_identity:
            return
        no, word = fr.stored_street(b)
        pass
        if no and word and not re.fullmatch(r"\d{5}", str(b.get("zip") or "")):
            for p in self.pages:
                ok, _ = self.page_scope(p["url"])
                if not ok:
                    continue
                m = re.search(re.escape(no) + r"\s+(?:[NSEW]\.?\s+)?" + re.escape(word) + r"[^·]{0,70}?\b(2[0-4]\d{3})\b", p["text"], re.I)
                if m:
                    q = fr.snippet(p["text"], m.start(), m.end(), 200)
                    if m.group(1) in q:
                        self.add("zip", "fill", b.get("zip") or "", m.group(1), q, p["url"], "high", False,
                                 ["address fields are not in the auto list (hours, phone, site, social)"])
                    break

    def do_hours(self):
        b = self.biz
        if not self.pages:
            return
        stored_src = "hours" if b.get("hours") else ("osm opening_hours" if self.tags.get("opening_hours") else None)
        stored_text = " · ".join(b["hours"]) if b.get("hours") else fr.osm_hours_text(self.tags.get("opening_hours", ""))
        stored_tok = fr.hours_tokens(fr.parse_hours(stored_text)) if stored_src else []
        pool = []
        for p in self.pages:
            for a, z in fr.hours_runs(p["text"]):
                pool.append({"url": p["url"], "quote": p["text"][a:z], "via": "deterministic scan"})
        llm_h = (self.src.get("llm") or {}).get("hours")
        if llm_h:
            pool.append({"url": llm_h["url"], "quote": llm_h["quote"], "via": "model quote"})
        cands, seen = [], set()
        for h in pool:
            parsed = fr.parse_hours(h["quote"])
            if not parsed["ok"] or len(parsed["days"]) < 2 or not any(isinstance(v, list) for v in parsed["days"].values()):
                continue
            if not fr.locate(h["quote"], self.pages):
                continue
            ok, why = self.quote_scope(h["quote"], h["url"])
            if not ok:
                self.scope_dropped.append({"field": "hours", "url": h["url"], "quote": fr.display_quote(h["quote"]), "why": why})
                continue
            key = (h["url"], fr.nrm(h["quote"]))
            if key in seen:
                continue
            seen.add(key)
            page = next(p for p in self.pages if p["url"] == h["url"])
            own = fr.own_location(b, page["text"], h["quote"])
            i = page["text"].find(h["quote"])
            kw = i >= 0 and bool(re.search(r"\bhours\b|\bopen\b", page["text"][max(0, i - 80): i], re.I))
            cands.append(dict(h, parsed=parsed, tokens=fr.hours_tokens(parsed), own=own, kw=kw,
                              ident=bool(fr.location_identity(b, page["text"]))))
        if not cands:
            return
        # prefer this location's own page/section, then a page printing the stored street/ZIP, then most days
        cands.sort(key=lambda c: (c["own"] is None, not c["ident"], not c["kw"], -len(c["parsed"]["days"]), c["via"] != "deterministic scan"))
        best = cands[0]
        conflicts, seen_sets = [], {tuple(sorted(best["tokens"]))}
        for c in cands[1:]:
            key = tuple(sorted(c["tokens"]))
            if key in seen_sets or not fr.hours_disagree(best["parsed"], c["parsed"]):
                continue
            seen_sets.add(key)
            conflicts.append(c)
        rec = {"stored_source": stored_src, "stored_tokens": stored_tok, "page_tokens": best["tokens"],
               "chosen_from": {"url": best["url"], "location": best["own"] or "not tied to this location"},
               "other_hours_on_site": [{"url": c["url"], "quote": fr.display_quote(c["quote"]), "tokens": c["tokens"]} for c in conflicts][:6]}
        self.hours_rec = rec
        if set(best["tokens"]) == set(stored_tok) and not conflicts:
            self.confirm.append({"field": "hours", "value": b.get("hours") or self.tags.get("opening_hours"), "url": best["url"]})
            return
        if set(best["tokens"]) == set(stored_tok):
            return          # stored matches this location's hours; other blocks belong elsewhere
        reasons = []
        if conflicts:
            reasons.append(f"hours conflict: {len(conflicts)} other hours listing(s) on the site disagree on "
                           f"{', '.join(sorted({d for c in conflicts for d in fr.hours_disagree(best['parsed'], c['parsed'])}, key=fr.DAYS.index))} "
                           "(all quotes in evidence_more)")
        if not best["parsed"]["complete"]:
            reasons.append(f"page states {len(best['parsed']['days'])} of 7 days; unstated days unknown")
        if best["parsed"]["inferred"]:
            reasons.append("am/pm not printed for every time; inferred")
        if SUBHOURS.search(best["quote"]):
            reasons.append(f"passage mentions '{SUBHOURS.search(best['quote']).group(0)}' (department/seasonal/appointment hours)")
        new = fr.hours_lines(best["parsed"])
        also = {"hours_source": {"url": best["url"], "checked": TODAY,
                                 "how": f"hours as printed on the business's own website (commerce full review {self.round_id})",
                                 "verbatim": fr.display_quote(best["quote"])}}
        more = [{"url": c["url"], "quote": fr.display_quote(c["quote"]), "parsed": fr.hours_lines(c["parsed"]),
                 "location": c["own"] or "not tied to this location"} for c in conflicts][:6]
        self.add("hours", "set" if b.get("hours") else "fill", b.get("hours") or [], new, best["quote"], best["url"],
                 "high", True, reasons, also=also, more=more or None,
                 note=f"chosen from {best['own'] or 'a page not tied to this location'}; stored ({stored_src or 'none'}) "
                      f"tokens {len(stored_tok)} vs page tokens {len(best['tokens'])}; sets differ")

    def do_owner(self):
        b = self.biz
        own = (self.src.get("llm") or {}).get("owner")
        if not own:
            return
        ok, why = self.quote_scope(own["quote"], own["url"])
        if not ok:
            self.scope_dropped.append({"field": "owner_operator", "url": own["url"], "quote": own["quote"], "why": why})
            return
        if not OWNER_WORD.search(own["quote"]) and not OWNER_WORD.search(own.get("role") or "x"):
            self.scope_dropped.append({"field": "owner_operator", "url": own["url"], "quote": own["quote"], "why": "quote does not name an ownership/operator role"})
            return
        if not OWNER_WORD.search(own["quote"]):
            # role word only in the model's label, not on the page: the page must print it next to the name
            page = next(p for p in self.pages if p["url"] == own["url"])
            i = page["text"].find(own["quote"])
            ctx = page["text"][max(0, i - 80): i + len(own["quote"]) + 80] if i >= 0 else ""
            if not OWNER_WORD.search(ctx):
                self.scope_dropped.append({"field": "owner_operator", "url": own["url"], "quote": own["quote"], "why": "no ownership word printed with the name"})
                return
        stored = b.get("owner_operator") or ""
        role = own.get("role") or "owner"
        new = f"{own['name']} ({role})"
        if PLACEHOLDER_OWNER.search(stored):
            self.add("owner_operator", "fill", stored, new, own["quote"], own["url"], "high", False,
                     ["owner/operator is not in the auto list (hours, phone, site, social)"])
        elif fr.nrm(own["name"]) in fr.nrm(stored):
            self.confirm.append({"field": "owner_operator", "value": own["name"], "url": own["url"]})
        else:
            self.add("owner_operator", "research", stored, new, own["quote"], own["url"], "medium", False,
                     ["site names a different owner/operator than the stored text; a person change needs QA"])
        self.owner_ev = own

    def do_name_category(self):
        b = self.biz
        llm = self.src.get("llm") or {}
        nm = llm.get("business_name")
        if nm and self.site_identity and not self.recovered:
            st = set(fr.name_tokens(b.get("name")))
            pg = set(fr.name_tokens(nm["quote"]))
            if st and pg and not (st & pg):
                self.flag("possibly-renamed", f"site prints the name '{nm['quote']}', stored name '{b.get('name')}'",
                          {"url": nm["url"], "quote": nm["quote"], "evidence_type": "html_text"})
        what = llm.get("what_they_do")
        if what and b.get("category") in ("home-services", "retail", "professional-services", "other") and self.site_identity:
            ok, why = self.quote_scope(what["quote"], what["url"])
            if ok:
                self.flag("category-review", f"stored category '{b.get('category')}' is generic; site describes the business (Roy picks a category)",
                          {"url": what["url"], "quote": what["quote"], "evidence_type": "html_text"})
        cl = llm.get("closed_or_moved")
        sig = (self.src.get("closed_signals") or [])
        for c in ([cl] if cl else []) + sig:
            ok, why = self.quote_scope(c["quote"], c["url"])
            if ok and re.search(r"\b(closed|moved|relocat|ceased|out of business)\w*", c["quote"], re.I):
                self.flag("possibly-closed-or-moved", "own site says closed/moved", {"url": c["url"], "quote": c["quote"], "evidence_type": "html_text"})
                break

    def do_socials(self):
        b = self.biz
        have = {str(s.get("url") or "").rstrip("/").lower() for s in b.get("sources") or []} | {str(b.get("web") or "").rstrip("/").lower()}
        for k, s in (self.src.get("socials") or {}).items():
            url = s["url"]
            if url.rstrip("/").lower() in have or url.rstrip("/").lower().replace("://www.", "://") in {h.replace("://www.", "://") for h in have}:
                self.confirm.append({"field": f"sources[{k}]", "value": url, "url": s["page"]})
                continue
            reasons = []
            if s["kind"] == "site-config":
                reasons.append("link found only in page config/JSON (site-config), not an <a href> on the page")
            ok, why = self.page_scope(s["page"])
            if not ok:
                reasons.append("scope: " + why)
            if (self.multi or self.chain) and not reasons:
                reasons.append("multi-location/chain site: header/footer social links may be the brand's, not this location's")
            new = {"label": f"{SOCIAL_LABEL[k]} (from official site)", "url": url}
            self.add("sources", "append", None, new, s["quote"], s["page"], "high", True, reasons, etype=s["kind"])

    def do_scores(self):
        b = self.biz
        sc = b.get("scores") or {}
        llm = self.src.get("llm") or {}
        # #1 Ownership clarity: owner named + real street address, both on in-scope own pages
        own = getattr(self, "owner_ev", None)
        if own and sc.get("ownership", "gray") in ("gray", "", None) and any(h.startswith("street:") for h in self.site_identity):
            addr = None
            no, word = fr.stored_street(b)
            for p in self.pages:
                ok, _ = self.page_scope(p["url"])
                m = re.search(re.escape(no) + r"\s+(?:[NSEW]\.?\s+)?" + re.escape(word), p["text"], re.I) if ok and no else None
                if m:
                    addr = {"url": p["url"], "quote": fr.display_quote(fr.snippet(p["text"], m.start(), m.end(), 200)), "what": "real street address"}
                    break
            if addr and fr.locate(addr["quote"], self.pages):
                rules = fr.rule("f1", "green") + (fr.rule("franchise") if self.chain else [])
                self.add("scores.ownership", "set", sc.get("ownership", "gray"), "green", own["quote"], own["url"], "high", False,
                         ["score change: QA (Sheriff Roy)"], rule=rules, more=[addr],
                         also={"scores.ownership_meta": {"band": "green", "reason": "affirmative", "verified": TODAY}},
                         note="Factor #1 asks 'Who owns/operates it? Real address?' — owner named on the business's own page; street address printed on its own page")
        # #3 Christ-centered public brand, identity type A
        fq = llm.get("faith_identity")
        if fq:
            ok, why = self.quote_scope(fq["quote"], fq["url"])
            explicit = bool(FAITH_RE.search(fr.nrm(fq["quote"])))
            if ok and explicit and sc.get("christ_centered_brand", "gray") not in ("gray", "", None):
                self.confirm.append({"field": "scores.christ_centered_brand", "value": sc.get("christ_centered_brand"), "url": fq["url"],
                                     "note": "explicit faith identity on own site; existing band left as is"})
            elif ok and explicit:
                self.add("scores.christ_centered_brand", "set", sc.get("christ_centered_brand", "gray"), "green", fq["quote"], fq["url"],
                         "medium", False, ["score change: QA (Sheriff Roy)"], rule=fr.rule("type_a", "type_a_score", "green"),
                         also={"scores.christ_centered_brand_meta": {"band": "green", "reason": "affirmative", "verified": TODAY}},
                         note="Type A: the business's own page states a Christian identity in its own voice")
            elif ok:
                self.ruling("faith signal without an explicit Christian-identity statement", "christ_centered_brand", fq["quote"], fq["url"],
                            why="type A needs 'Explicitly Christian business — faith is public identity'; this passage does not say so in words the rule covers")
            else:
                self.scope_dropped.append({"field": "scores.christ_centered_brand", "url": fq["url"], "quote": fq["quote"], "why": why})
        # #8 Financial integrity: license number printed for this business
        lic = llm.get("license")
        trade = b.get("category") in fr.LICENSED_TRADES
        if lic:
            ok, why = self.quote_scope(lic["quote"], lic["url"])
            if ok and re.search(r"licen[sc]e|class [abc]|contractor", lic["quote"], re.I):
                self.lic_ev = lic
                if sc.get("financial_integrity", "gray") in ("gray", "", None):
                    self.add("scores.financial_integrity", "set", sc.get("financial_integrity", "gray"), "green", lic["quote"], lic["url"],
                             "medium", False, ["score change: QA (Sheriff Roy)", "DPOR status not verified (lookup is reCAPTCHA-gated)"],
                             rule=fr.rule("f8", "green"),
                             also={"scores.financial_integrity_meta": {"band": "green", "reason": "affirmative", "verified": TODAY}},
                             note="Factor #8 asks 'Licensed/transparent?' — the business prints its license number")
            elif not ok:
                self.scope_dropped.append({"field": "license", "url": lic["url"], "quote": lic["quote"], "why": why})
        elif trade and self.pages:
            for p in self.pages:
                m = LICENSE_SELF.search(p["text"])
                ok, _ = self.page_scope(p["url"])
                if m and ok:
                    q = fr.snippet(p["text"], m.start(), m.end(), 200)
                    if fr.locate(q, self.pages):
                        self.ruling("self-described licensed/insured, no license number printed", "financial_integrity", q, p["url"],
                                    why="Factor #8 'Licensed/transparent?': a self-claim without a number cannot be checked (DPOR lookup is reCAPTCHA-gated)")
                    break
        # #9 Digital integrity: own site reachable and prints this listing's phone or street
        if not self.recovered and self.pages and sc.get("digital_integrity", "gray") in ("gray", "", None):
            p = next((p for p in self.pages if any(h.startswith(("street:", "phone")) for h in p["identity"])), None)
            if p:
                h = next(h for h in p["identity"] if h.startswith(("street:", "phone")))
                if h == "phone":
                    m = next((m for m in fr.PHONE_RE.finditer(p["text"]) if fr.digits(m.group(0)) == fr.digits(b.get("phone"))), None)
                else:
                    no, word = h[7:].split(" ", 1)
                    m = re.search(re.escape(no) + r"\s+(?:[NSEW]\.?\s+)?" + re.escape(word), p["text"], re.I)
                if m:
                    self.add("scores.digital_integrity", "set", sc.get("digital_integrity", "gray"), "green",
                             fr.snippet(p["text"], m.start(), m.end(), 200), p["url"], "high", False, ["score change: QA (Sheriff Roy)"],
                             rule=fr.rule("f9", "green"),
                             also={"scores.digital_integrity_meta": {"band": "green", "reason": "verified", "verified": TODAY}},
                             note="Factor #9 asks 'Can a neighbor actually reach them?' — own site loads and prints the listing's contact")
        # Everything else the model suggested: needs-ruling, on-topic only, never a score
        for f, ev in (llm.get("factor_evidence") or {}).items():
            if f not in FACTOR_TOPIC:
                continue
            ok, why = self.quote_scope(ev["quote"], ev["url"])
            if not ok:
                self.scope_dropped.append({"field": f"scores.{f}", "url": ev["url"], "quote": ev["quote"], "why": why})
                continue
            if not FACTOR_TOPIC[f].search(ev["quote"]):
                self.scope_dropped.append({"field": f"scores.{f}", "url": ev["url"], "quote": ev["quote"], "why": "off topic for this factor"})
                continue
            if sc.get(f) == ev["lean"]:
                continue
            self.ruling(f"model suggests {ev['lean'].upper()} on {f.replace('_', ' ')}", f, ev["quote"], ev["url"], lean=ev["lean"],
                        why="methodology.html prints only the question for this factor; no written rule maps a self-description to a band")

    def do_lookups(self):
        b = self.biz
        lk = self.obs.get("lookups") or {}
        lic = getattr(self, "lic_ev", None)
        if not lic:
            for p in self.pages:
                found = fr.license_numbers(p["text"])
                if found:
                    f0 = found[0]
                    q = fr.snippet(p["text"], max(0, f0["pos"] - 1), f0["pos"] + 10, 200)
                    if f0["number"] in q and fr.locate(q, self.pages):
                        lic = {"number": f0["number"], "url": p["url"], "quote": fr.display_quote(q), "why": f0["why"]}
                        break
        if lic:
            # re-find the quote in the cached pages (the fetcher matched against the uncapped page)
            here = fr.locate(lic["quote"], [p for p in self.pages if p["url"] == lic["url"]]) or fr.locate(lic["quote"], self.pages)
            lic = dict(lic, url=here, quote=fr.display_quote(lic["quote"])) if here else None
        if lic and "dpor" not in lk:
            lk = dict(lk, dpor={"reason": fr.LOOKUP_SKIPS["dpor"], "lookup_url": fr.DPOR_LOOKUP_URL})
        if "dpor" in lk:
            self.n += 1
            self.lookups.append({"hold_id": f"{self.round_id}:{b['slug']}:{self.n}", "kind": "lookup",
                                 "title": (f"DPOR check: license #{lic['number']} printed on the business's site" if lic
                                           else "DPOR license check needed (licensed trade)"),
                                 "license_number_on_site": (lic or {}).get("number"),
                                 "evidence": ({"url": lic["url"], "quote": lic["quote"], "evidence_type": "html_text"} if lic else None),
                                 "status": "not checked", "reason": lk["dpor"]["reason"], "lookup_url": lk["dpor"]["lookup_url"]})

    def do_duplicates(self):
        b = self.biz
        ph = fr.digits(b.get("phone"))
        no, word = fr.stored_street(b)
        host = fr.host_of(b.get("web") or "")
        res = []
        for o in self.data_index.values():
            if o["slug"] == b["slug"]:
                continue
            why = []
            if len(ph) == 10 and fr.digits(o.get("phone")) == ph:
                why.append(f"same phone {ph}")
            ono, oword = fr.stored_street(o)
            if no and word and ono == no and (oword or "").lower() == word.lower():
                same_name = bool(set(fr.name_tokens(b.get("name"))) & set(fr.name_tokens(o.get("name"))))
                if same_name:
                    why.append(f"same street address ({no} {word}) and shared name word")
            oh = fr.host_of(o.get("web") or "")
            if host and oh == host and not re.search(r"facebook|instagram|google|yelp", host):
                same_path = str(o.get("web")).rstrip("/").lower() == str(b.get("web")).rstrip("/").lower()
                if same_path:
                    why.append(f"same website {b.get('web')}")
            if not why:
                continue
            linked = o.get("duplicate_of") == b["slug"] or b.get("duplicate_of") == o["slug"]
            res.append({"other": o["slug"], "other_name": o.get("name"), "matched_on": why,
                        "other_page": f"https://usmcmin.com/fxbg/commerce/business/{o['slug']}.html",
                        "other_values": {"address": o.get("address"), "phone": o.get("phone"), "web": o.get("web"),
                                         "publish": o.get("publish", True), "duplicate_of": o.get("duplicate_of")},
                        "already_linked": linked})
        self.duplicates = res
        lines = []
        for d in res:
            v = d["other_values"]
            if d["already_linked"]:
                folded, kept = (b["slug"], d["other"]) if b.get("duplicate_of") == d["other"] else (d["other"], b["slug"])
                lines.append(f"{folded} and {kept}: {'; '.join(d['matched_on'])}. Already folded through the existing pattern "
                             f"({folded}.duplicate_of = {kept}, {folded}.publish = false); {kept} stays the live listing. No new action.")
            else:
                lines.append(f"{b['slug']} and {d['other']}: {'; '.join(d['matched_on'])}. Not linked yet; HOLD for QA "
                             f"(a merge would fold one record into the other via duplicate_of + publish=false).")
        self.duplicate_result = " | ".join(lines) or "no duplicate found by phone, street+name, or identical website"
        for d in res:
            if d["already_linked"]:
                continue
            self.flag("duplicate-candidate", f"possible duplicate of {d['other']} ({'; '.join(d['matched_on'])})",
                      {"url": d["other_page"], "quote": json.dumps(d["other_values"], ensure_ascii=False), "evidence_type": "other_record"})

    def build(self) -> dict:
        b, o = self.biz, self.obs
        self.hours_rec = None
        self.duplicates = []
        self.duplicate_result = ""
        for step in (self.do_website, self.do_phone, self.check_moved, self.do_address, self.do_hours, self.do_owner, self.do_name_category,
                     self.do_socials, self.do_scores, self.do_lookups, self.do_duplicates):
            step()
        rv = o.get("recovery") or {}
        fb = o.get("facebook")
        status = o.get("status")
        if b.get("duplicate_of"):
            status = status + " (listing already folded as a duplicate)"
        out = {
            "slug": b["slug"], "name": b.get("name"), "category": b.get("category"), "selection_tier": o.get("selection_tier"),
            "status": status, "publish": b.get("publish", True), "duplicate_of": b.get("duplicate_of"),
            "source": ("recovered website" if self.recovered else ("own website" if o.get("pages") else "none")),
            "site": (self.src.get("site") or {}).get("final_url"),
            "site_identity": self.site_identity, "chain_brand": self.tags.get("brand"),
            "multi_location": self.multi,
            "recovery": {"site": rv.get("site"), "query": rv.get("query"),
                         "candidates": [{k: c.get(k) for k in ("url", "via", "status", "accepted", "matched")} for c in rv.get("candidates", [])]} if rv else None,
            "facebook": ({"url": fb["url"], "result": [a.get("status") for a in fb.get("attempts", [])],
                          "recency_checked": False,
                          "note": "Facebook serves a login wall / HTTP 4xx to automated reads; last-12-month post check not possible without an account"} if fb else None),
            "hours": self.hours_rec,
            "changes": self.changes, "flags": self.flags, "needs_ruling": self.rulings, "lookups": self.lookups,
            "duplicates": self.duplicates, "duplicate_result": self.duplicate_result, "confirmations": self.confirm, "scope_dropped": self.scope_dropped,
            "dropped_unverifiable": self.dropped_unverifiable + int(self.src.get("llm_dropped_unverified") or 0),
            "llm_error": self.src.get("llm_error"),
            "scc": (o.get("lookups") or {}).get("scc"),
        }
        return out


def hold_rows(round_id: str, entries: list[dict]) -> list[dict]:
    rows = []
    for e in entries:
        base = {"round": round_id, "slug": e["slug"], "name": e["name"], "dry_run": True, "qa": "Sheriff Roy (FXBG civic lane)"}
        for c in e["changes"]:
            if c["gate"] == "hold":
                rows.append({**base, "hold_id": c["change_id"], "kind": "change",
                             "title": f"{c['field']}: {json.dumps(c['old'], ensure_ascii=False)[:60]} -> {json.dumps(c['new'], ensure_ascii=False)[:80]}",
                             **{k: c[k] for k in ("field", "op", "old", "new", "confidence", "hold_reasons", "evidence") if k in c},
                             **({"rule": c["rule"]} if c.get("rule") else {}), **({"evidence_more": c["evidence_more"]} if c.get("evidence_more") else {})})
        for f in e["flags"]:
            if f.get("gate") == "info":
                continue
            rows.append({**base, "hold_id": f["flag_id"], "kind": "flag", "flag_kind": f["kind"], **{k: v for k, v in f.items() if k not in ("flag_id", "kind")}})
        for r in e["needs_ruling"]:
            rows.append({**base, **r})
        for lk in e["lookups"]:
            rows.append({**base, **lk})
    return rows


def main():
    obs_path, round_dir = Path(sys.argv[1]), Path(sys.argv[2])
    round_id = sys.argv[sys.argv.index("--round-id") + 1] if "--round-id" in sys.argv else round_dir.name
    rules = fr.check_rules()
    sha = fr.sha256_file(fr.DATA)
    data = fr.load_data()
    index = {b["slug"]: b for b in data["businesses"]}
    osm = load_osm_tags()
    O = json.load(open(obs_path))
    entries = []
    for o in O["observations"]:
        b = index.get(o["slug"])
        if not b:
            continue
        entries.append(Builder(round_id, b, o, index, osm).build())
    holds = hold_rows(round_id, entries)
    ch = [c for e in entries for c in e["changes"]]
    counts = {
        "reviewed": len(entries),
        "reachable": sum(1 for e in entries if e["source"] != "none"),
        "unreachable": sum(1 for e in entries if e["source"] == "none"),
        "recovered_site": sum(1 for e in entries if e["source"] == "recovered website"),
        "businesses_with_changes": sum(1 for e in entries if e["changes"]),
        "changes_proposed": len(ch), "auto": sum(1 for c in ch if c["gate"] == "auto"), "hold_changes": sum(1 for c in ch if c["gate"] == "hold"),
        "hold_rows": len(holds),
        "flags": {k: sum(1 for e in entries for f in e["flags"] if f["kind"] == k) for k in sorted({f["kind"] for e in entries for f in e["flags"]})},
        "closed_flags": sum(1 for e in entries for f in e["flags"] if f["kind"].startswith("possibly-closed")),
        "duplicate_flags": sum(1 for e in entries for f in e["flags"] if f["kind"] == "duplicate-candidate"),
        "needs_ruling": sum(len(e["needs_ruling"]) for e in entries),
        "lookups_pending": sum(len(e["lookups"]) for e in entries),
        "duplicates_already_linked": sum(1 for e in entries for d in e["duplicates"] if d["already_linked"]),
        "scope_dropped": sum(len(e["scope_dropped"]) for e in entries),
        "dropped_unverifiable": sum(e["dropped_unverifiable"] for e in entries),
    }
    patch = {"round_id": round_id, "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "mode": "dry-run",
             "data_file": str(fr.DATA), "data_sha256_at_build": sha, "observations": str(obs_path), "model": O.get("model"),
             "methodology_url": fr.METHODOLOGY_URL, "rules": rules,
             "gates": {"auto_fields": ["hours", "phone (fill only)", "sources (social, html_link only)"],
                       "always_hold": ["scores.*", "web (recovery or redirect)", "owner_operator", "zip/address", "category", "closures", "duplicates/merges", "anything from a recovered site"]},
             "lookups_skipped": {"scc": fr.LOOKUP_SKIPS["scc"], "dpor": fr.LOOKUP_SKIPS["dpor"],
                                 "locality_license_pages": "not used in v1 (City of Fredericksburg / Spotsylvania / Stafford license pages not yet examined)"},
             "counts": counts, "businesses": entries}
    round_dir.mkdir(parents=True, exist_ok=True)
    fr.dump(patch, round_dir / "review-patch.json")
    fr.dump({"round_id": round_id, "rows": holds}, round_dir / "hold.json")
    q_path = fr.FR_HOME / "hold-queue.json"
    q = json.load(open(q_path)) if q_path.exists() else {"rows": []}
    slugs = {e["slug"] for e in entries}
    q["rows"] = [r for r in q["rows"] if r["slug"] not in slugs] + holds   # latest round per business only
    q["updated"] = patch["generated_at"]
    fr.dump(q, q_path)
    print(json.dumps(counts, indent=1))


if __name__ == "__main__":
    main()
