#!/usr/bin/env python3
"""Scrape https://www.trackaipac.com/congress for every Member of Congress
career-total Israel Lobby contribution. Output as data/aipac_full.json.

The /congress page is a Squarespace gallery where each tile is a JSON-encoded
entry:
  "title": "Tommy Tuberville",
  "description": "...AL-SEN [R]...Israel Lobby Total: $29,184..."

This script regexes those out and emits a clean list."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
RAW_HTML = Path("/tmp/aipac_congress.html").read_text(encoding="utf-8", errors="ignore")
# Decode HTML entities so the embedded JSON becomes parseable.
import html as html_mod
HTML = html_mod.unescape(RAW_HTML)

# Each gallery tile is JSON-encoded then HTML-entity-encoded into the page
# (Squarespace embeds collection data as &quot;-escaped JSON in HTML attrs).
# After we decode entities the structure looks like:
#   "title":"Tommy Tuberville",...,"description":"<p ...>AL-SEN [R]</p>..."
ENTRY_RE = re.compile(
    r'"title"\s*:\s*"([^"]+)"\s*,\s*"body"\s*:\s*null\s*,\s*"description"\s*:\s*"((?:[^"\\]|\\.)*)"',
    re.DOTALL,
)
# Fallback: title + description without body:null between (some entries differ).
ENTRY_RE_LOOSE = re.compile(
    r'"title"\s*:\s*"([^"]{2,})"[^{}]*?"description"\s*:\s*"((?:[^"\\]|\\.)*)"',
    re.DOTALL,
)
DISTRICT_RE = re.compile(r"([A-Z]{2})-(SEN|\d{2})\s*\[([RDIL])\]")
TOTAL_RE = re.compile(r"Israel Lobby Total:\s*\$([\d,]+)")
PAC_RE = re.compile(r"PACs:\s*\$([\d,]+)")
IE_RE = re.compile(r"IE:\s*\$([\d,]+)")
PAC_LIST_RE = re.compile(r">([A-Z][A-Z0-9, ]+)<")
# Squarespace escapes HTML inside description. The actual visible text is e.g.
#   AL-SEN [R]\nIsrael Lobby Total: $29,184\nPACs: $29,184\nIE: $0\nAIPAC, AMP...
# Each line is wrapped in <p data-rte-preserve-empty="true" style="...">TEXT</p>


def unescape(s: str) -> str:
    """Reverse the Squarespace JSON-in-HTML escaping enough to read text."""
    s = (s
         .replace("\\u003c", "<")
         .replace("\\u003e", ">")
         .replace("\\u0026", "&")
         .replace("\\/", "/")
         .replace("&lt;", "<")
         .replace("&gt;", ">")
         .replace("&amp;", "&")
         .replace("&quot;", '"')
         .replace("\\n", "\n")
         .replace("\\\"", '"'))
    return s


def to_int(dollar_str: str) -> int:
    return int(dollar_str.replace(",", ""))


def extract():
    out = []
    seen = set()
    matches = list(ENTRY_RE.finditer(HTML)) or list(ENTRY_RE_LOOSE.finditer(HTML))
    print(f"DEBUG: regex matched {len(matches)} tiles before filtering")
    for m in matches:
        name_raw = m.group(1)
        desc_raw = m.group(2)
        # Skip non-member entries (organizations, etc.).
        if name_raw in seen:
            continue
        desc = unescape(desc_raw)
        dist_m = DISTRICT_RE.search(desc)
        total_m = TOTAL_RE.search(desc)
        if not dist_m or not total_m:
            continue
        state = dist_m.group(1)
        seat = dist_m.group(2)
        party = dist_m.group(3)
        total = to_int(total_m.group(1))
        pac_m = PAC_RE.search(desc)
        ie_m = IE_RE.search(desc)
        # Find the PAC acronym list — last <p>...</p> block of all-caps tokens.
        pacs_line = ""
        for line in desc.split("\n"):
            txt = re.sub(r"<[^>]+>", "", line).strip()
            if re.match(r"^[A-Z][A-Z0-9, ]+$", txt) and "," in txt:
                pacs_line = txt
        seen.add(name_raw)
        out.append({
            "name": name_raw,
            "state": state,
            "seat": seat,
            "party": party,
            "total": total,
            "pacs": to_int(pac_m.group(1)) if pac_m else 0,
            "ie": to_int(ie_m.group(1)) if ie_m else 0,
            "pac_acronyms": pacs_line,
        })
    return out


def bracket_for(dollars):
    if dollars == 0:
        return "zero"
    if dollars < 50_000:
        return "1_to_50k"
    if dollars < 250_000:
        return "50k_to_250k"
    if dollars < 1_000_000:
        return "250k_to_1m"
    if dollars < 3_000_000:
        return "1m_to_3m"
    return "3m_plus"


BRACKET_DELTA = {
    "zero": +7,
    "1_to_50k": -3,
    "50k_to_250k": -10,
    "250k_to_1m": -20,
    "1m_to_3m": -35,
    "3m_plus": -50,
}


if __name__ == "__main__":
    entries = extract()
    print(f"Extracted {len(entries)} Members of Congress")
    # Bracket histogram
    hist = {}
    for e in entries:
        b = bracket_for(e["total"])
        hist[b] = hist.get(b, 0) + 1
    for b in ["zero", "1_to_50k", "50k_to_250k", "250k_to_1m", "1m_to_3m", "3m_plus"]:
        print(f"  {b:<14} {hist.get(b, 0):3d}  (delta {BRACKET_DELTA[b]:+d})")
    out_path = ROOT / "data" / "aipac_full.json"
    out_path.write_text(json.dumps(entries, indent=2))
    print(f"Wrote {out_path}")
