#!/usr/bin/env python3
"""election-results-ingest.py — turn official election-night results into a
refine-records dossier (candidacy_status won/lost, status lame_duck) for the
RESOLUTE Citizen scorecard. Zero model calls: this is a fact pipeline, not a
scoring pipeline. Party is never evidence; a result is a fact with a source URL.

Source today: Virginia Dept. of Elections ENR API
  https://enr.elections.virginia.gov/results/public/api/elections/<jurisdiction>/<electionId>/ballot-items
  <jurisdiction> = "virginia" (statewide: US Senate, US House, HoD specials, amendments)
                  or a locality slug such as "fredericksburg-city", "spotsylvania-county".

Rules (post-election plan 2026-11-04):
  - Only contests with every reporting unit in (reportingUnits == totalUnits) are called.
  - Winner = top voteCount for voteFor=1 contests; multi-seat contests take the top N.
  - Match ENR option names to scorecard records by jurisdiction/district + surname + first
    name or nickname. Ambiguous or missing matches are REPORTED, never guessed.
  - Winner in file  -> set candidacy_status=won (status stays active).
  - Loser in file   -> candidacy_status=lost; a losing incumbent -> status=lame_duck
    (refine-records keeps the record; "former" is applied at swearing-in, not here).
  - Unofficial results are labelled unofficial in notes_append with vote counts and asOf.
  - Nothing is written to data/scorecard.json here. Output is a dossier JSON for
    refine-records.py (apply via ~/.openclaw/bin/dl0828-grok-compile-push.sh inbox).

Usage:
  election-results-ingest.py --election 2026-November-General \
      --jurisdiction virginia [--jurisdiction fredericksburg-city ...] \
      [--only "Senate|1st|7th"] --out DOSSIER.json [--report REPORT.md]
"""
import argparse, json, re, sys, urllib.request, datetime

API = "https://enr.elections.virginia.gov/results/public/api/elections"
UI = "https://enr.elections.virginia.gov/results/public"
UA = {"User-Agent": "Mozilla/5.0 (compatible; MOOPScorecardBot/1.0; +https://usmcmin.com)",
      "Accept": "application/json"}
SCORECARD = "data/scorecard.json"

STATE_ABBR = {"virginia": "VA"}
LOCALITY_JURISDICTION = {
    "fredericksburg-city": "City of Fredericksburg",
    "spotsylvania-county": "Spotsylvania County",
    "stafford-county": "Stafford County",
}
ORD = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "6th": 6, "7th": 7, "8th": 8,
       "9th": 9, "10th": 10, "11th": 11}


def txt(x):
    if isinstance(x, dict):
        return x.get("text", "")
    if isinstance(x, list) and x and isinstance(x[0], dict):
        en = [t for t in x if t.get("languageId") in (1, "1", "en", None)]
        return (en or x)[0].get("text", "")
    return x or ""


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def norm_name(s):
    s = s or ""
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.replace("’", "'")
    nick = re.findall(r'["“]([^"”]+)["”]', s)
    s = re.sub(r'["“][^"”]+["”]', " ", s)
    s = re.sub(r"[.,]", " ", s)
    parts = [p.lower() for p in s.split() if p.strip()]
    parts = [p for p in parts if p not in ("jr", "sr", "ii", "iii", "iv", "dr", "mr", "mrs", "ms")]
    parts = [p for p in parts if len(p) > 1]  # drop initials
    first = parts[0] if parts else ""
    last = parts[-1] if parts else ""
    nicks = {n.lower() for n in nick}
    return {"first": first, "last": last, "nicks": nicks, "all": parts}


def name_match(a, b):
    """a = ENR option, b = scorecard record. Surname must match; first name or a nickname
    must match on a 3-letter prefix (Doug/Douglas, Rob/Robert)."""
    A, B = norm_name(a), norm_name(b)
    if not A["last"] or A["last"] != B["last"]:
        return False
    firsts_a = {A["first"]} | A["nicks"]
    firsts_b = {B["first"]} | B["nicks"]
    for fa in firsts_a:
        for fb in firsts_b:
            if fa and fb and (fa[:3] == fb[:3]):
                return True
    return False


def contest_filter(name, jurisdiction, level_records):
    """Return the subset of scorecard records that could belong to this contest."""
    n = name
    if jurisdiction == "virginia":
        if "United States Senate" in n:
            return [r for r in level_records if r.get("state") == "VA" and r.get("level") == "federal"
                    and (r.get("jurisdiction") == "United States Senate"
                         or re.search(r"U\.?S\.? Senat", str(r.get("office") or "")))]
        m = re.search(r"House of Representatives \((\d+)(?:st|nd|rd|th) District\)", n)
        if m:
            dn = int(m.group(1))
            out = []
            for r in level_records:
                if r.get("state") != "VA" or r.get("level") != "federal":
                    continue
                d = str(r.get("district") or "")
                off = str(r.get("office") or "")
                if re.search(rf"\bVA-0?{dn}\b", off) or re.search(rf"District {dn}\b", off) or d in (str(dn), f"VA-{dn:02d}", f"{dn}"):
                    out.append(r)
            return out
        m = re.search(r"House of Delegates \((\d+)(?:st|nd|rd|th) District\)", n)
        if m:
            dn = int(m.group(1))
            return [r for r in level_records if r.get("state") == "VA" and r.get("level") == "state"
                    and re.search(rf"District {dn}\b", str(r.get("office") or ""))]
        return []
    jur = LOCALITY_JURISDICTION.get(jurisdiction)
    if not jur:
        return []
    return [r for r in level_records if r.get("jurisdiction") == jur]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--election", default="2026-November-General")
    ap.add_argument("--jurisdiction", action="append", default=[])
    ap.add_argument("--only", default=None, help="regex on contest name")
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", default=None)
    ap.add_argument("--scorecard", default=SCORECARD)
    a = ap.parse_args()
    if not a.jurisdiction:
        a.jurisdiction = ["virginia"]

    sc = json.load(open(a.scorecard))
    recs = sc["candidates"]
    by_slug = {r["slug"]: r for r in recs}

    records, report = {}, []
    today = datetime.date.today().isoformat()
    for jur in a.jurisdiction:
        url = f"{API}/{jur}/{a.election}/ballot-items"
        try:
            data = get(url)["data"]
        except Exception as e:
            report.append(f"- FETCH FAILED {url}: {e}")
            continue
        for it in data:
            cname = txt(it.get("name"))
            if a.only and not re.search(a.only, cname):
                continue
            if it.get("referendum") or "Constitutional Amendment" in cname:
                continue
            # Locality feeds repeat the federal contests; only the statewide feed calls those.
            if jur != "virginia" and re.search(r"United States|House of Representatives|House of Delegates", cname):
                continue
            rs = it.get("reportingStatus") or {}
            ru, tu = rs.get("reportingUnits"), rs.get("totalUnits")
            opts = (it.get("summaryResults") or {}).get("ballotOptions") or []
            opts = [o for o in opts if txt(o.get("name")).lower() != "write-in"]
            opts.sort(key=lambda o: -(o.get("voteCount") or 0))
            vf = txt(it.get("voteFor")) if not isinstance(it.get("voteFor"), int) else str(it.get("voteFor"))
            words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7}
            mv = re.search(r"(\d+|one|two|three|four|five|six|seven)\b", str(vf).lower())
            vote_for = int(words.get(mv.group(1), mv.group(1))) if mv else 1
            complete = bool(ru) and ru == tu
            total = sum(o.get("voteCount") or 0 for o in opts)
            src = f"{UI}/{jur}/elections/{a.election}/ballot-items/{it.get('id')}"
            pool = contest_filter(cname, jur, recs)
            line = f"- **{cname}** ({jur}) units {ru}/{tu}, {'complete' if complete else 'INCOMPLETE'}: " + \
                   ", ".join(f"{txt(o.get('name'))} {o.get('voteCount'):,}" for o in opts[:6])
            report.append(line)
            if not complete:
                report.append("  - not called: reporting incomplete")
                continue
            if not opts:
                continue
            winners = opts[:vote_for]
            for o in opts:
                oname = txt(o.get("name"))
                matches = [r for r in pool if name_match(oname, r.get("name"))]
                if len(matches) != 1:
                    report.append(f"  - {oname}: {'NO MATCH' if not matches else 'AMBIGUOUS ' + str([m['slug'] for m in matches])} (pool {len(pool)})")
                    continue
                r = matches[0]
                won = o in winners
                # A sitting official running for a DIFFERENT office (e.g. a supervisor running
                # for Commissioner of Revenue) keeps the seat they hold. Only flip status when
                # the contest is for the office the record holds; otherwise note the result only.
                fam = ["Senate", "House of Representatives", "House of Delegates", "Commissioner",
                       "School Board", "Supervisor", "Council", "Sheriff", "Mayor", "Commonwealth",
                       "Treasurer", "Clerk"]
                def fams(s):
                    s = s.lower().replace("senator", "senate").replace("representative", "house of representatives")
                    return {f for f in fam if f.lower() in s}
                cf = fams(cname)
                rf = fams(str(r.get("office") or ""))
                if "House of Representatives" in cf:
                    rf |= {"House of Representatives"} if re.search(r"U\.?S\.? (House|Representative)", str(r.get("office") or "")) else set()
                same_office = bool(cf & rf) or not cf
                if not same_office:
                    pct = (100.0 * (o.get("voteCount") or 0) / total) if total else 0
                    note = (f"2026-11-03 general election: ran for {cname} and "
                            f"{'WON' if won else 'LOST'} ({o.get('voteCount'):,} votes, {pct:.1f}%); "
                            f"record office unchanged pending the new term. Source: Virginia Dept. of Elections ENR.")
                    records[r["slug"]] = {"notes_append": note, "sources_add": [src]}
                    report.append(f"  - {oname} -> {r['slug']}: different office ({r.get('office')}), note only")
                    continue
                pct = (100.0 * (o.get("voteCount") or 0) / total) if total else 0
                asof = rs.get("asOf") or ""
                official = "official" if it.get("isOfficialResults") else "unofficial"
                note = (f"2026-11-03 general election ({official} results as of {asof[:10]}): "
                        f"{'WON' if won else 'LOST'} {cname}, {o.get('voteCount'):,} votes ({pct:.1f}%), "
                        f"{ru}/{tu} units reporting. Source: Virginia Dept. of Elections ENR.")
                setd = {"candidacy_status": "won" if won else "lost"}
                if not won and (r.get("candidacy_status") or "").startswith("incumbent"):
                    setd["status"] = "lame_duck"
                elif not won:
                    setd["status"] = "lost"
                entry = {"set": setd, "notes_append": note, "sources_add": [src]}
                # refine-records stamps profile.confidence=evidence_<tier> when the key is
                # absent. A result is not evidence; keep an unset confidence unset.
                if "confidence" not in (r.get("profile") or {}):
                    entry["profile"] = {"confidence": None}
                records[r["slug"]] = entry
                report.append(f"  - {oname} -> {r['slug']}: {setd}")

    dossier = {
        "_meta": {"author": "max", "date": today,
                  "note": f"{a.election} results via Virginia ENR API; facts only, no score cells touched; "
                          f"losing incumbents -> lame_duck until the new term"},
        "records": records,
    }
    json.dump(dossier, open(a.out, "w"), indent=1)
    rep = f"# Results ingest {a.election} — {today}\n\n" + "\n".join(report) + f"\n\n{len(records)} record change(s) written to {a.out}\n"
    if a.report:
        open(a.report, "w").write(rep)
    print(rep)


if __name__ == "__main__":
    main()
