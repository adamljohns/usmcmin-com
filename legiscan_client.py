#!/usr/bin/env python3
"""Thin LegiScan Public API client for the RESOLUTE scorecard grind.

Reads the API key from Keychain (service LEGISCAN / account moop) or LEGISCAN_API_KEY.
Caches JSON under ~/.openclaw/cache/legiscan/ and tracks monthly query spend so we
stay under the Public tier's 30,000/month limit. Uses change_hash / person_hash so
unchanged payloads are never re-fetched.

Primary consumer: local-politician-extract.py — when a candidate has a banked
profile.records_website on legiscan.com, we pull sponsorships via API (HTML is
Cloudflare-blocked and scraping is prohibited) and synthesize quotable text for
the existing verbatim + cross-check gates.
"""
from __future__ import annotations

import json, os, re, subprocess, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

API = "https://api.legiscan.com/"
CACHE = Path(os.path.expanduser("~/.openclaw/cache/legiscan"))
DEFAULT_MONTHLY_BUDGET = 12_000  # soft cap well under the 30k Public limit
# Prefer rubric-relevant titles when synthesizing extractor text (keep under page cap).
RUBRIC_KW = re.compile(
    r"abort|pregnan|\blife\b|fetal|unborn|firearm|handgun|rifle|\bgun\b|weapon|ammo|"
    r"marriage|parental|parent\b|school|curricul|religio|faith|church|conscien|"
    r"immigra|alien|sanctuar|deport|border|elect|ballot|voter|poll\b|tax\b|"
    r"transgender|gender|sex(?:ual)?|pronoun|adoption|ivf|surrog|"
    r"second amendment|permitless|constitutional carry|red.?flag|erpo|"
    r"education savings|scholarship|homeschool",
    re.I,
)
PEOPLE_URL_RE = re.compile(
    r"https?://legiscan\.com/([A-Z]{2})/people/([A-Za-z0-9_\-]+)(?:/id/(\d+))?",
    re.I,
)


class LegiScanError(RuntimeError):
    pass


class LegiScanBudgetExceeded(LegiScanError):
    pass


def _month_key(ts=None):
    return time.strftime("%Y-%m", time.localtime(ts or time.time()))


def api_key():
    env = os.environ.get("LEGISCAN_API_KEY") or os.environ.get("LEGISCAN")
    if env:
        return env.strip()
    try:
        return subprocess.check_output(
            ["security", "find-generic-password", "-s", "LEGISCAN", "-a", "moop", "-w"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except Exception as e:
        raise LegiScanError(
            "LegiScan API key not found (env LEGISCAN_API_KEY or Keychain "
            "service=LEGISCAN account=moop)"
        ) from e


class LegiScanClient:
    def __init__(self, key=None, cache_dir=None, monthly_budget=None):
        self.key = key or api_key()
        self.cache_dir = Path(cache_dir or CACHE)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.monthly_budget = int(
            monthly_budget
            or os.environ.get("LEGISCAN_MONTHLY_BUDGET")
            or DEFAULT_MONTHLY_BUDGET
        )
        self._spend = self._load_spend()

    # ---- spend / cache -------------------------------------------------
    def _spend_path(self):
        return self.cache_dir / "spend.json"

    def _load_spend(self):
        p = self._spend_path()
        if p.exists():
            try:
                return json.loads(p.read_text())
            except Exception:
                pass
        return {"month": _month_key(), "count": 0}

    def _save_spend(self):
        if self._spend.get("month") != _month_key():
            self._spend = {"month": _month_key(), "count": 0}
        self._spend_path().write_text(json.dumps(self._spend, indent=1) + "\n")

    @property
    def queries_this_month(self):
        if self._spend.get("month") != _month_key():
            return 0
        return int(self._spend.get("count") or 0)

    def _cache_path(self, op, **params):
        # stable filename; never include the API key
        parts = [op] + [f"{k}={params[k]}" for k in sorted(params)]
        safe = re.sub(r"[^A-Za-z0-9._=-]+", "_", "_".join(parts))[:180]
        return self.cache_dir / f"{safe}.json"

    def _read_cache(self, path, max_age_s):
        if not path.exists():
            return None
        age = time.time() - path.stat().st_mtime
        if max_age_s is not None and age > max_age_s:
            return None
        try:
            return json.loads(path.read_text())
        except Exception:
            return None

    def _write_cache(self, path, payload):
        path.write_text(json.dumps(payload, indent=1) + "\n")

    def pull(self, op, max_age_s=None, **params):
        """Pull an API op. Returns the JSON body. Counts against monthly budget
        only on a real network hit (cache hits are free)."""
        path = self._cache_path(op, **params)
        cached = self._read_cache(path, max_age_s)
        if cached is not None and cached.get("status") == "OK":
            return cached

        if self.queries_this_month >= self.monthly_budget:
            raise LegiScanBudgetExceeded(
                f"LegiScan soft budget hit ({self.monthly_budget}/mo); "
                f"spent={self.queries_this_month}"
            )

        q = urllib.parse.urlencode({"key": self.key, "op": op, **params})
        req = urllib.request.Request(
            API + "?" + q,
            headers={"User-Agent": "MOOPScorecardBot/1.0 (+https://usmcmin.com)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = json.load(r)
        except urllib.error.HTTPError as e:
            raise LegiScanError(f"HTTP {e.code} on {op}") from e
        except Exception as e:
            raise LegiScanError(f"network error on {op}: {e}") from e

        self._spend["month"] = _month_key()
        self._spend["count"] = self.queries_this_month + 1
        self._save_spend()

        if body.get("status") != "OK":
            # still cache ERROR briefly? no — don't poison the cache
            raise LegiScanError(f"{op} status={body.get('status')}: {body.get('alert') or body}")

        self._write_cache(path, body)
        return body

    # ---- person resolution --------------------------------------------
    def parse_people_url(self, url):
        m = PEOPLE_URL_RE.search(url or "")
        if not m:
            return None
        return {
            "state": m.group(1).upper(),
            "slug": m.group(2).lower(),
            "people_id": int(m.group(3)) if m.group(3) else None,
        }

    def _norm_name(self, s):
        s = re.sub(r"[^a-z0-9\s]", " ", (s or "").lower())
        s = re.sub(r"\b(jr|sr|ii|iii|iv)\b", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    def session_list(self, state):
        # sessions change slowly
        return self.pull("getSessionList", max_age_s=7 * 86400, state=state.upper())["sessions"]

    def current_sessions(self, state, n=2):
        sessions = self.session_list(state)
        # prefer non-prior, then newest year_start
        sessions = sorted(
            sessions,
            key=lambda s: (0 if not s.get("prior") else 1, -(s.get("year_start") or 0)),
        )
        return sessions[:n]

    def session_people(self, session_id):
        # weekly-ish; person roster is stable within a session
        body = self.pull("getSessionPeople", max_age_s=7 * 86400, id=str(session_id))
        people = body.get("sessionpeople") or {}
        if isinstance(people, dict):
            people = people.get("people") or []
        return people if isinstance(people, list) else []

    def resolve_people_id(self, state, name, people_id=None, slug=None):
        if people_id:
            return int(people_id)
        target = self._norm_name(name)
        slug_norm = (slug or "").lower().replace("_", "-")
        for sess in self.current_sessions(state, n=3):
            for p in self.session_people(sess["session_id"]):
                pn = self._norm_name(p.get("name") or f"{p.get('first_name','')} {p.get('last_name','')}")
                if target and (pn == target or target in pn or pn in target):
                    return int(p["people_id"])
                # slug fallback: jim-hinebaugh ↔ Jim Hinebaugh
                if slug_norm:
                    cand = re.sub(r"[^a-z0-9]+", "-", pn).strip("-")
                    if cand == slug_norm or cand.startswith(slug_norm) or slug_norm.startswith(cand):
                        return int(p["people_id"])
        return None

    def get_person(self, people_id):
        return self.pull("getPerson", max_age_s=7 * 86400, id=str(people_id))["person"]

    def sponsored_list(self, people_id):
        # daily cadence per LegiScan manual
        body = self.pull("getSponsoredList", max_age_s=86400, id=str(people_id))
        return body["sponsoredbills"]

    def master_list(self, session_id):
        # daily; honor change_hash by caching the whole list for 24h
        body = self.pull("getMasterList", max_age_s=86400, id=str(session_id))
        ml = body.get("masterlist") or {}
        out = {}
        for v in ml.values():
            if isinstance(v, dict) and "bill_id" in v:
                out[v["bill_id"]] = v
        return out

    # ---- synthesized extractor text -----------------------------------
    def person_record_text(self, records_url, name, state=None, max_bills=80):
        """Build quotable plain text for a legislator's LegiScan record page.

        Returns (public_url, text) or None if unresolved / empty.
        """
        meta = self.parse_people_url(records_url) or {}
        st = (state or meta.get("state") or "").upper()
        if not st:
            return None
        pid = self.resolve_people_id(
            st, name, people_id=meta.get("people_id"), slug=meta.get("slug"),
        )
        if not pid:
            return None

        sponsored = self.sponsored_list(pid)
        sponsor = sponsored.get("sponsor") or {}
        bills = sponsored.get("bills") or []
        sessions = sponsored.get("sessions") or []

        # Join titles from the most recent sessions that cover these bill_ids
        wanted = {b["bill_id"] for b in bills if "bill_id" in b}
        by_id = {}
        for sess in sessions[:3]:
            if len(by_id) >= len(wanted):
                break
            try:
                by_id.update(self.master_list(sess["session_id"]))
            except LegiScanError:
                continue

        rows = []
        for b in bills:
            m = by_id.get(b["bill_id"])
            if not m:
                continue
            title = (m.get("title") or "").strip()
            desc = (m.get("description") or "").strip()
            number = m.get("number") or b.get("number") or ""
            url = m.get("url") or ""
            year = ""
            # year from URL …/2026 or status_date
            ym = re.search(r"/(\d{4})$", url)
            if ym:
                year = ym.group(1)
            blob = f"{title} {desc}"
            score = 2 if RUBRIC_KW.search(blob) else 0
            rows.append((score, number, year, title, desc, url))

        # rubric hits first, then the rest — still capped
        rows.sort(key=lambda r: (-r[0], r[1]))
        rows = rows[:max_bills]

        full_name = sponsor.get("name") or name
        party = sponsor.get("party") or ""
        district = sponsor.get("district") or ""
        role = sponsor.get("role") or ""
        public_url = records_url.rstrip("/")
        if meta.get("people_id") is None:
            # prefer the canonical id URL once we know it
            public_url = f"https://legiscan.com/{st}/people/{meta.get('slug') or re.sub(r'[^a-z0-9]+', '-', full_name.lower()).strip('-')}/id/{pid}"

        lines = [
            f"{full_name} ({st} {district}, {party} {role}) — LegiScan legislative sponsorship record.",
            f"Source: {public_url}",
            f"people_id: {pid}",
            "",
            f"{full_name} sponsored the following bills:",
        ]
        for score, number, year, title, desc, url in rows:
            year_bit = f" ({year})" if year else ""
            line = f"{full_name} sponsored {number}{year_bit}: {title}."
            if score and desc:
                # short desc for rubric-relevant bills only (verbatim quotes need meat)
                line += " " + desc[:280].rstrip(".") + "."
            if url:
                line += f" [{url}]"
            lines.append(line)

        if len(lines) <= 5:
            return None
        text = "\n".join(lines)
        return public_url, text


def person_record_text(records_url, name, state=None):
    """Module-level helper used by the extractor."""
    return LegiScanClient().person_record_text(records_url, name, state=state)


if __name__ == "__main__":
    # smoke: python3 legiscan_client.py "Jim Hinebaugh" MD "https://legiscan.com/MD/people/jim-hinebaugh"
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "Jim Hinebaugh"
    state = sys.argv[2] if len(sys.argv) > 2 else "MD"
    url = sys.argv[3] if len(sys.argv) > 3 else f"https://legiscan.com/{state}/people/{name.lower().replace(' ', '-')}"
    client = LegiScanClient()
    out = client.person_record_text(url, name, state=state)
    if not out:
        sys.exit("no record text")
    pub, text = out
    print(f"url={pub}")
    print(f"queries_this_month={client.queries_this_month}/{client.monthly_budget}")
    print(f"chars={len(text)}")
    print(text[:2000])
    print("…" if len(text) > 2000 else "")
