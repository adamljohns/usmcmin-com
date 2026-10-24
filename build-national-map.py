#!/usr/bin/env python3
"""
build-national-map.py — emit the two small files behind /national-map.html:

  data/national-map.json          per-state AVERAGE RESOLUTE score, two views
  data/maps/us-states-albers.json pre-projected, simplified US state outlines
                                  (Albers USA layout with Alaska + Hawaii insets)

so the page never downloads the 9k-candidate scorecard or a 2 MB geometry set.

READS data/scorecard.json READ-ONLY. Never writes it.

Score formula — NOT a new one. Each person's score is the profile-page
headline number (`pct_of_max`, the "NN / 100" on candidates/<st>/<slug>.html),
computed with generate-profiles.py's own calc_total / classify_office_tier /
backed_answer_count, the same score_adjustments sum, the same 0-100 clamp and
the same thin-record branch. Those functions are imported, not copied, so a
rubric change there flows here on the next build.

Who counts — only evidence-scored, currently sitting office-holders:
  * evidence_scored = build-coverage.py's is_evidence_scored() (imported):
    an evidence_* confidence or at least one verified claim. Unscored
    party-default records never enter an average.
  * "legislature" view: level 'state' whose office is a state legislative
    seat (State Representative / Senator / Delegate / Assembly Member /
    House of Delegates / General Assembly Member, chamber Speakers and
    floor leaders). Governors, Lt. Governors, AGs, Secretaries of State,
    treasurers, auditors, commissioners and judges are excluded.
  * "congress" view: level 'federal' U.S. Representative or U.S. Senator.
    Cabinet, justices, ambassadors, non-voting delegates and the Resident
    Commissioner are excluded.
  * not sitting (excluded in both views): status former/lost/deceased;
    candidacy_status resigned/deceased/withdrew/removed/vacant_*; an office
    string that starts "Former"/"Candidate"/"VACANT"/"PHANTOM"; or a record
    whose first office qualifier is a candidacy for that seat
    ("U.S. Representative NJ-12 (2026 D Candidate · ...)", "challenger to").
  * one row per person per view (state + name), first record wins.
  * a state with fewer than MIN_N scored people is shaded grey.

Run from repo root:  python3 build-national-map.py [--report]
"""
import importlib.util
import json
import math
import os
import re
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

SRC = 'data/scorecard.json'
OUT = 'data/national-map.json'
GEO_DIR = 'data/maps/states'
GEO_OUT = 'data/maps/us-states-albers.json'
MIN_N = 3


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gp = _load('generate_profiles', 'generate-profiles.py')   # profile-page score
bc = _load('build_coverage', 'build-coverage.py')         # evidence_scored line

STATES = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
    'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
    'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
    'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon',
    'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia',
    'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
}
# Seats per state — used only by --report as an over-inclusion check.
HOUSE_SEATS = dict(AL=7, AK=1, AZ=9, AR=4, CA=52, CO=8, CT=5, DE=1, FL=28, GA=14, HI=2, ID=2,
                   IL=17, IN=9, IA=4, KS=4, KY=6, LA=6, ME=2, MD=8, MA=9, MI=13, MN=8, MS=4,
                   MO=8, MT=2, NE=3, NV=4, NH=2, NJ=12, NM=3, NY=26, NC=14, ND=1, OH=15, OK=5,
                   OR=6, PA=17, RI=2, SC=7, SD=1, TN=9, TX=38, UT=4, VT=1, VA=11, WA=10, WV=2,
                   WI=8, WY=1, DC=0)
LEG_SEATS = dict(AL=140, AK=60, AZ=90, AR=135, CA=120, CO=100, CT=187, DE=62, FL=160, GA=236,
                 HI=76, ID=105, IL=177, IN=150, IA=150, KS=165, KY=138, LA=144, ME=186, MD=188,
                 MA=200, MI=148, MN=201, MS=174, MO=197, MT=150, NE=49, NV=63, NH=424, NJ=120,
                 NM=112, NY=213, NC=170, ND=141, OH=132, OK=149, OR=90, PA=253, RI=113, SC=170,
                 SD=105, TN=132, TX=181, UT=104, VT=180, VA=140, WA=147, WV=134, WI=132, WY=93,
                 DC=0)

# ---------------------------------------------------------------- the score

def profile_score(c, categories):
    """The profile-page headline number (generate-profiles.py, pct_of_max).
    Mirrors the block that renders #prof-score: tier rubric total, plus the
    score_adjustments deltas, dynamic max = 2 x answered, clamp 0-100, and the
    thin-record guard (answered < 10 or documented < 5 -> absolute /100)."""
    tier = gp.classify_office_tier(c) or 'federal'
    total = gp.calc_total(c.get('scores') or {}, categories, tier)
    adj = 0
    for info in (((c.get('profile') or {}).get('score_adjustments')) or {}).values():
        adj += int(info.get('delta') or 0)
    adjusted = total['score'] + adj
    answered = total['answered']
    max_possible = answered * gp.POINTS_PER_TRUE
    thin = answered < 10 or gp.backed_answer_count(c) < 5   # MIN_ANSWERED / MIN_BACKED
    if thin:
        pct = max(0, min(100, round((adjusted / gp.MAX_TOTAL) * 100))) if gp.MAX_TOTAL else 0
    elif max_possible > 0:
        pct = max(0, min(100, round((adjusted / max_possible) * 100)))
    else:
        pct = 0
    return pct, thin

# ------------------------------------------------------------ who is sitting

NOT_SITTING_STATUS = {'former', 'lost', 'deceased'}
NOT_SITTING_CANDIDACY = {'resigned', 'deceased', 'withdrew', 'removed', 'retired',
                         'vacant_special_election_scheduled'}
CANDIDACY_WORD = re.compile(r'\b(candidate|nominee|challenger)\b', re.I)
SITTING_WORD = re.compile(r'\b(sitting|incumbent)\b', re.I)
# "(2026 U.S. Senate candidate)" on a state-senate record = running for ANOTHER office.
OTHER_OFFICE = re.compile(r'u\.?\s?s\.?\s+(senate|house)|congress|governor|attorney general|'
                          r'secretary of state|mayor|lieutenant|[A-Z]{2}-\d\d', re.I)
SITTING_IN_CONGRESS = re.compile(r'\bsitting\s+u\.?\s?s\.?\s+(rep\b|representative|senator)', re.I)
WITHDREW_WORD = re.compile(r'\b(withdrew|withdrawn|declined|not running|20\d\d\s+[A-Z]{1,3}\s+primary)\b', re.I)


def split_office(office):
    """'U.S. Representative ME-02 (2026 D primary candidate · ...)' ->
    head 'U.S. Representative ME-02', first qualifier '2026 D primary candidate'."""
    o = (office or '').strip()
    head = re.split(r'\s*(?:\(|·|—|–|,|;|:)\s*', o, maxsplit=1)[0].strip()
    first_q = ''
    m = re.search(r'\(([^)]*)', o)
    if m:
        first_q = re.split(r'\s*[·;]\s*', m.group(1).strip())[0]
    return head, first_q


def not_sitting_reason(c):
    status = (c.get('status') or '').lower()
    if not status:
        return 'no status'
    if status in NOT_SITTING_STATUS:
        return f'status={status}'
    cs = (c.get('candidacy_status') or '').lower()
    if cs in NOT_SITTING_CANDIDACY or cs.startswith('vacant'):
        return f'candidacy_status={cs}'
    office = c.get('office') or ''
    name = c.get('name') or ''
    head, first_q = split_office(office)
    # A sitting member of Congress whose only record is a run for the other
    # chamber ("U.S. Senate Michigan (2026 D Candidate · sitting U.S. Rep MI-11)")
    # still sits in the state's delegation — same person, same federal rubric.
    if (c.get('level') or '').lower() == 'federal' and SITTING_IN_CONGRESS.search(office):
        return None
    if re.match(r'^(former|candidate|vacant|phantom)\b', head, re.I) or re.match(r'^vacant\b', name, re.I):
        return 'office says former/candidate/vacant'
    if CANDIDACY_WORD.search(head):
        return 'office head is a candidacy'
    if (first_q and CANDIDACY_WORD.search(first_q) and not SITTING_WORD.search(first_q)
            and not OTHER_OFFICE.search(first_q)):
        return 'first qualifier is a candidacy for this seat'
    # "(WITHDREW ...)", "(NOT RUNNING ...)", "(2026 D primary — ...)" on a seat the
    # person never held. A sitting member running for another office keeps the
    # seat (candidacy_status running_*higher_office), so that case is exempt.
    if (first_q and 'higher_office' not in cs
            and (WITHDREW_WORD.match(first_q)
                 or (WITHDREW_WORD.search(first_q) and not SITTING_WORD.search(first_q)))):
        return 'first qualifier says withdrew/declined/primary hopeful'
    if re.search(r'\bchallenger to\b|\bseat vacant\b|\(former\s*(?:[)\u00b7;\u2014\u2013-]|$)', office, re.I):
        return 'office says challenger/vacant/former'
    return None

# ---------------------------------------------------------------- seat type

CONGRESS_HEAD = re.compile(
    r'^(?:u\.?\s?s\.?|us|united states)\s+(?:senator|senate|representative|rep\.?|house|congress(?:man|woman|member)?)\b',
    re.I)
NOT_CONGRESS = re.compile(r'non-voting|delegate to u\.?s|resident commissioner|shadow', re.I)

LEG_HEAD = re.compile(
    r'^(?:(?:' + '|'.join(re.escape(n) for n in STATES.values()) + r')\s+)?'
    r'(?:state\s+)?(?:'
    r'representative|senator|senate|assembly\s*member|assemblymember|assemblyman|assemblywoman|'
    r'delegate|house of delegates|general assembly member|legislator|'
    r'house district|senate district|house'
    r')\b', re.I)
LEG_LEADER = re.compile(
    r'^(?:speaker|majority leader|minority leader|president pro tem\w*|senate president|'
    r'president of the senate)\b.*\b(house|senate|assembly|delegates|legislature)\b', re.I)
NOT_LEG = re.compile(
    r'governor|attorney general|secretary of|treasurer|auditor|comptroller|commissioner|'
    r'superintendent|justice|judge|u\.\s?s\.|\bus\b|united states|congress|candidate for|mayor|'
    r'council|county|sheriff', re.I)


def view_of(c):
    level = (c.get('level') or '').lower()
    head, _ = split_office(c.get('office') or '')
    if level == 'federal':
        if CONGRESS_HEAD.match(head) and not NOT_CONGRESS.search(c.get('office') or ''):
            return 'congress'
        return None
    if level == 'state':
        if NOT_LEG.search(head):
            return None
        if LEG_HEAD.match(head) or LEG_LEADER.match(head):
            return 'legislature'
    return None


def norm_name(n):
    n = re.sub(r'\b(jr|sr|ii|iii|iv)\b\.?', '', (n or '').lower())
    n = re.sub(r'\s+(senate|house)$', '', n.strip())   # "Sharice Davids Senate" = same person
    return re.sub(r'[^a-z]', '', n)

# ---------------------------------------------------------------- aggregate

def build_scores(sc, report=False):
    categories = sc.get('categories', [])
    views = {'legislature': {}, 'congress': {}}
    seen = {'legislature': set(), 'congress': set()}
    excluded = {}
    dupes = 0
    for c in sc.get('candidates', []):
        st = (c.get('state') or '').upper()
        if st not in STATES:
            continue
        v = view_of(c)
        if not v:
            continue
        why = not_sitting_reason(c)
        if why:
            excluded.setdefault(v, []).append((st, c.get('name'), c.get('office'), why))
            continue
        key = (st, norm_name(c.get('name')))
        if key in seen[v]:
            dupes += 1
            continue
        seen[v].add(key)
        b = views[v].setdefault(st, {'sitting': 0, 'scores': [], 'thin': 0})
        b['sitting'] += 1
        if not bc.is_evidence_scored(c):
            continue
        pct, thin = profile_score(c, categories)
        b['scores'].append(pct)
        b['thin'] += 1 if thin else 0

    out = {}
    for v, rows in views.items():
        states = {}
        for st in STATES:
            b = rows.get(st, {'sitting': 0, 'scores': [], 'thin': 0})
            n = len(b['scores'])
            avg = round(sum(b['scores']) / n, 1) if n else None
            states[st] = {
                'avg': avg if n >= MIN_N else None,
                'raw_avg': avg,
                'n': n,
                'sitting': b['sitting'],
                'thin': b['thin'],
            }
        allscores = [s for b in rows.values() for s in b['scores']]
        out[v] = {
            'states': states,
            'n_scored': len(allscores),
            'n_sitting': sum(b['sitting'] for b in rows.values()),
            'national_avg': round(sum(allscores) / len(allscores), 1) if allscores else None,
            'states_shaded': sum(1 for s in states.values() if s['avg'] is not None),
        }

    if report:
        for v, cap in (('congress', HOUSE_SEATS), ('legislature', LEG_SEATS)):
            print(f'\n== {v}: sitting {out[v]["n_sitting"]}, scored {out[v]["n_scored"]}, '
                  f'national avg {out[v]["national_avg"]}')
            for st in sorted(STATES):
                s = out[v]['states'][st]
                seats = cap[st] + (2 if v == 'congress' and st != 'DC' else 0)
                flag = '  <-- OVER' if s['sitting'] > seats else ''
                print(f'  {st} sitting {s["sitting"]:4d}/{seats:4d} scored {s["n"]:4d} '
                      f'thin {s["thin"]:3d} avg {s["raw_avg"]}{flag}')
            print(f'  excluded as not sitting: {len(excluded.get(v, []))}')
            for row in excluded.get(v, [])[:400]:
                print('    ', row[0], '|', (row[1] or '')[:30], '|', (row[2] or '')[:80], '|', row[3])
        print(f'\nduplicate person rows skipped: {dupes}')
    return out

# ----------------------------------------------------------------- geometry
# Albers USA (d3.geoAlbersUsa constants), computed here once so the page only
# draws pre-projected SVG paths.

K = 1070.0
TX, TY = 480.0, 250.0


def conic_equal_area(phi0, phi1):
    sy0 = math.sin(math.radians(phi0))
    n = (sy0 + math.sin(math.radians(phi1))) / 2
    cc = 1 + sy0 * (2 * n - sy0)
    r0 = math.sqrt(cc) / n

    def raw(lam, phi):
        r = math.sqrt(max(0.0, cc - 2 * n * math.sin(phi))) / n
        return r * math.sin(lam * n), r0 - r * math.cos(lam * n)
    return raw


def make_projection(rotate, center, parallels, scale, translate):
    raw = conic_equal_area(*parallels)
    cx, cy = raw(math.radians(center[0]), math.radians(center[1]))

    def proj(lon, lat):
        lam = lon + rotate
        lam = (lam + 180) % 360 - 180
        x, y = raw(math.radians(lam), math.radians(lat))
        return translate[0] + (x - cx) * scale, translate[1] - (y - cy) * scale
    return proj


LOWER48 = make_projection(96, (-0.6, 38.7), (29.5, 45.5), K, (TX, TY))
ALASKA = make_projection(154, (-2, 58.5), (55, 65), K * 0.35, (TX - 0.307 * K, TY + 0.201 * K))
HAWAII = make_projection(157, (-3, 19.9), (8, 18), K, (TX - 0.205 * K, TY + 0.212 * K))


def dp(points, tol):
    """Douglas-Peucker on a closed ring (iterative)."""
    if len(points) < 5:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = points[a]
        bx, by = points[b]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        best, idx = -1.0, -1
        for i in range(a + 1, b):
            px, py = points[i]
            d = abs(dy * px - dx * py + bx * ay - by * ax) / L if L else math.hypot(px - ax, py - ay)
            if d > best:
                best, idx = d, i
        if best > tol and idx > 0:
            keep[idx] = True
            stack.append((a, idx))
            stack.append((idx, b))
    return [p for p, k in zip(points, keep) if k]


def ring_area(pts):
    return 0.5 * sum(pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1] for i in range(len(pts)))


def ring_centroid(pts):
    a = ring_area(pts)
    if not a:
        return pts[0]
    cx = cy = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[i]
        f = x0 * y1 - x1 * y0
        cx += (x0 + x1) * f
        cy += (y0 + y1) * f
    return cx / (6 * a), cy / (6 * a)


# Hand-nudged label spots where the polygon centroid sits badly (projected px).
LABEL_NUDGE = {'FL': (18, 8), 'LA': (-10, -2), 'MI': (14, 22), 'CA': (-8, 0),
               'KY': (6, 2), 'ID': (0, 18), 'NY': (8, 2), 'VA': (6, 2), 'WV': (-2, 4),
               'MN': (-6, 6), 'TX': (6, 0), 'OK': (8, -2), 'AK': (0, 4), 'HI': (-40, -36),
               'NC': (6, 0), 'SC': (2, 2), 'MD': (0, 0), 'ME': (0, 2), 'NH': (0, 0)}
# Small eastern states get a callout box instead of an on-shape label.
CALLOUTS = ['VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD', 'DC']


def build_geometry():
    states = {}
    for st, name in STATES.items():
        g = json.load(open(os.path.join(ROOT, GEO_DIR, st.lower() + '.geojson')))
        proj = ALASKA if st == 'AK' else HAWAII if st == 'HI' else LOWER48
        tol = 0.35 if st not in ('DC', 'RI', 'DE') else 0.12
        min_area = 0.6 if st not in ('DC', 'RI', 'DE', 'HI') else 0.05
        parts = []
        best = (0, None)
        for ft in g.get('features', [g]):
            geo = ft['geometry']
            polys = geo['coordinates'] if geo['type'] == 'MultiPolygon' else [geo['coordinates']]
            for poly in polys:
                for ri, ring in enumerate(poly):
                    pts = [proj(lon, lat) for lon, lat in ring]
                    simp = dp(pts, tol)
                    if len(simp) < 4:
                        continue
                    area = abs(ring_area(simp))
                    if area < min_area:
                        continue
                    parts.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in simp[:-1]) + 'Z')
                    if ri == 0 and area > best[0]:
                        best = (area, simp)
        cx, cy = ring_centroid(best[1]) if best[1] else (0, 0)
        nx, ny = LABEL_NUDGE.get(st, (0, 0))
        states[st] = {'name': name, 'd': ''.join(parts), 'lx': round(cx + nx, 1),
                      'ly': round(cy + ny, 1), 'callout': st in CALLOUTS}
    # bounds
    xs, ys = [], []
    for s in states.values():
        for m in re.finditer(r'(-?\d+\.?\d*),(-?\d+\.?\d*)', s['d']):
            xs.append(float(m.group(1)))
            ys.append(float(m.group(2)))
    return {
        'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'source': 'data/maps/states/*.geojson (US Census cartographic boundaries) '
                  'projected Albers USA with AK/HI insets by build-national-map.py',
        'bounds': [round(min(xs), 1), round(min(ys), 1), round(max(xs), 1), round(max(ys), 1)],
        'states': states,
    }


def main():
    report = '--report' in sys.argv
    with open(os.path.join(ROOT, SRC)) as f:
        sc = json.load(f)
    views = build_scores(sc, report=report)
    meta = sc.get('meta') or {}
    payload = {
        'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'source': SRC,
        'source_last_updated': meta.get('last_updated'),
        'scorecard_version': meta.get('version'),
        'builder': 'build-national-map.py',
        'min_n': MIN_N,
        'method': {
            'score': 'Profile-page headline score (0-100, % of dynamic max incl. score adjustments; '
                     'thin records use absolute /100) from generate-profiles.py',
            'who': 'Evidence-scored (build-coverage.is_evidence_scored), currently sitting office-holders',
            'legislature': 'State legislators: State Representative / Senator / Delegate / '
                           'Assembly Member and chamber leaders. No statewide executives or judges.',
            'congress': "The state's U.S. Representatives and U.S. Senators. No non-voting "
                        'delegates, cabinet, justices or ambassadors.',
            'grey': f'Fewer than {MIN_N} scored office-holders in that view',
        },
        'views': views,
    }
    with open(os.path.join(ROOT, OUT), 'w') as f:
        json.dump(payload, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')
    geo = build_geometry()
    with open(os.path.join(ROOT, GEO_OUT), 'w') as f:
        json.dump(geo, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')
    for v in ('legislature', 'congress'):
        d = views[v]
        print(f'{v}: {d["n_scored"]} scored of {d["n_sitting"]} sitting, '
              f'{d["states_shaded"]}/51 shaded, national avg {d["national_avg"]}')
    print(f'Wrote {OUT} ({os.path.getsize(os.path.join(ROOT, OUT)) / 1024:.1f} KB), '
          f'{GEO_OUT} ({os.path.getsize(os.path.join(ROOT, GEO_OUT)) / 1024:.1f} KB)')


if __name__ == '__main__':
    main()
