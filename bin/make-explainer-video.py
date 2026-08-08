#!/usr/bin/env python3
"""make-explainer-video.py — build a U.S.M.C. Ministries branded explainer
video from a course page, entirely on this Mac.

Adam, 2026-08-07: replace the NotebookLM explainer videos with our own —
our slides, our branding, and one of the masculine voices assigned to the
fleet, with an opening and closing card reading "Uniting, Serving, Mentoring,
and Counseling Ministries."

Pipeline, all local, no cloud:
  1. pull the narration text out of a course page
  2. chunk it into slides at paragraph/heading boundaries
  3. render each slide to PNG with Playwright, in house dark+gold styling
  4. narrate each slide with Piper (voice is a flag, not a hardcode)
  5. mux slides + narration into an MP4 with ffmpeg, each slide held for
     exactly as long as its own narration runs

Usage:
  python3 bin/make-explainer-video.py ai-mission-week-1.html --dry-run
  python3 bin/make-explainer-video.py ai-mission-week-1.html --voice en_US-ryan-high
  python3 bin/make-explainer-video.py ai-boot-camp-tools.html --out /tmp/tools.mp4
"""
import argparse, html, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = 'Uniting, Serving, Mentoring, and Counseling Ministries'

# House palette, read off the live pages rather than invented.
BG, GOLD, TEXT, MUTED = '#0A0A0A', '#D4AF37', '#F0F0F0', '#B0B8C4'


# Page furniture that must never be narrated. Without this the voice reads
# "Download the video MP4, listen on the move" aloud in the very video it is
# describing — caught on the first render.
CHROME = re.compile(
    r'(download the (video|audio)[^.]*\.?|watch the overview|listen on the move|'
    r'\(mp4\)|\(m4a\)|audio companion for this week[^.]*\.?|'
    r'a 3-4 minute walk-through[^.]*\.?|for the commute or the gym\.?|'
    r'skip to|click here|read more|back to top|print / pdf|share this)',
    re.I)
# Elements that are navigation or media widgets, not teaching content.
DROP_TAGS = re.compile(
    r'<(nav|footer|figure|video|audio|form|button)\b.*?</\1>', re.S | re.I)
DROP_CLASS = re.compile(
    r'<(\w+)[^>]*class="[^"]*(nav|download|media|player|toolbar|share|'
    r'chap-nav|week-nav|hud|btn)[^"]*"[^>]*>.*?</\1>', re.S | re.I)


def strip_html(s: str) -> str:
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', s, flags=re.S | re.I)
    s = DROP_TAGS.sub(' ', s)
    s = DROP_CLASS.sub(' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = CHROME.sub(' ', s)
    s = re.sub(r'[\u2193\u25B6\u266A\u2192\u2190\u2191]', ' ', s)  # arrows / play / note glyphs
    return re.sub(r'\s+', ' ', s).strip()


def extract_slides(path: Path, max_words=55):
    """Headings become slide titles; the prose under them becomes narration."""
    raw = path.read_text(encoding='utf-8', errors='replace')
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    title = strip_html(title_m.group(1)) if title_m else path.stem

    body = raw
    m = re.search(r'<main[^>]*>(.*?)</main>', raw, re.S)
    if m:
        body = m.group(1)

    slides, cur = [], None
    for chunk in re.split(r'(<h[23][^>]*>.*?</h[23]>)', body, flags=re.S):
        if not chunk.strip():
            continue
        if re.match(r'<h[23]', chunk, re.I):
            if cur and cur['narration']:
                slides.append(cur)
            cur = {'title': strip_html(chunk), 'narration': ''}
        elif cur is not None:
            t = strip_html(chunk)
            if t:
                cur['narration'] = (cur['narration'] + ' ' + t).strip()
    if cur and cur['narration']:
        slides.append(cur)

    # A slide left with only a few words after chrome-stripping is not a slide;
    # it is the residue of a media widget. Drop it rather than hold a frame on
    # half a sentence.
    slides = [s for s in slides if len(s['narration'].split()) >= 12]

    # Split any slide whose narration would outrun what fits on screen.
    out = []
    for s in slides:
        words = s['narration'].split()
        if len(words) <= max_words:
            out.append(s); continue
        for i in range(0, len(words), max_words):
            part = ' '.join(words[i:i + max_words])
            out.append({'title': s['title'] if i == 0 else s['title'] + ' (cont.)',
                        'narration': part})
    return title, out


def slide_html(kind, title, body, index=None, total=None):
    if kind == 'card':      # opening / closing
        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
        html,body{{margin:0;height:100%;background:{BG};color:{TEXT};
          font-family:'Playfair Display',Georgia,serif;display:grid;place-items:center}}
        .w{{text-align:center;max-width:1500px;padding:0 90px}}
        h1{{font-size:88px;margin:0 0 26px;color:{GOLD};line-height:1.1}}
        p{{font-size:40px;color:{MUTED};margin:0;font-family:Inter,system-ui,sans-serif}}
        .rule{{width:180px;height:3px;background:{GOLD};margin:46px auto}}
        </style></head><body><div class="w">
        <h1>{html.escape(title)}</h1><div class="rule"></div>
        <p>{html.escape(body)}</p></div></body></html>"""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    html,body{{margin:0;height:100%;background:{BG};color:{TEXT};
      font-family:Inter,system-ui,sans-serif}}
    .w{{height:100%;box-sizing:border-box;padding:88px 110px;display:flex;
      flex-direction:column;justify-content:center}}
    .eyebrow{{color:{GOLD};font-size:26px;letter-spacing:.16em;text-transform:uppercase;
      margin-bottom:26px}}
    h2{{font-family:'Playfair Display',Georgia,serif;font-size:66px;margin:0 0 34px;
      color:{TEXT};line-height:1.15}}
    p{{font-size:37px;line-height:1.5;color:{MUTED};margin:0}}
    .bar{{position:absolute;bottom:0;left:0;height:8px;background:{GOLD}}}
    .foot{{position:absolute;bottom:34px;right:60px;color:{GOLD};font-size:22px;
      letter-spacing:.1em}}
    </style></head><body><div class="w">
      <div class="eyebrow">U.S.M.C. Ministries</div>
      <h2>{html.escape(title)}</h2><p>{html.escape(body)}</p></div>
      <div class="bar" style="width:{int((index/total)*100) if total else 0}%"></div>
      <div class="foot">{index}/{total}</div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('page')
    ap.add_argument('--voice', default='am_onyx',
                    help='Kokoro voice (am_onyx is the house narration voice)')
    ap.add_argument('--out')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--max-slides', type=int, default=0)
    ap.add_argument('--emit-plan', help='write the slide plan as JSON and stop')
    a = ap.parse_args()

    src = ROOT / a.page
    if not src.exists():
        sys.exit(f'no such page: {src}')
    # Kokoro is the house engine — am_onyx narrates 38 of the site's audio
    # books, so explainers should sound like the rest of usmcmin.org.
    kokoro_py = Path.home() / '.mlx-audio-venv' / 'bin' / 'python'
    if not kokoro_py.exists():
        sys.exit(f'mlx-audio venv missing: {kokoro_py}')
    for tool in ('ffmpeg',):
        if not shutil.which(tool):
            sys.exit(f'{tool} not on PATH')

    title, slides = extract_slides(src)
    if a.max_slides:
        slides = slides[:a.max_slides]
    words = sum(len(s['narration'].split()) for s in slides)
    print(f'source   : {a.page}')
    print(f'title    : {title}')
    print(f'slides   : {len(slides)} content + 2 brand cards')
    print(f'narration: ~{words} words (~{words/150:.1f} min at 150 wpm)')
    print(f'voice    : {a.voice}')
    if a.emit_plan:
        cards = [{'kind':'card','title':title,'body':BRAND,'narration':''}] \
              + [dict(kind='slide', **s) for s in slides] \
              + [{'kind':'card','title':'U.S.M.C. Ministries','body':BRAND,'narration':''}]
        for i,c in enumerate(cards):
            c['index']=i; c['total']=len(cards)
            c['html']=slide_html(c['kind'], c['title'], c.get('body') or c['narration'],
                                 i, len(cards)) if c['kind']=='slide' \
                      else slide_html('card', c['title'], c['body'])
        open(a.emit_plan,'w').write(json.dumps({'title':title,'voice':a.voice,'slides':cards}, indent=1))
        print(f'plan written: {a.emit_plan} ({len(cards)} frames)')
        return

    if a.dry_run:
        for i, s in enumerate(slides[:4], 1):
            print(f'  [{i}] {s["title"][:60]}')
            print(f'      {s["narration"][:110]}...')
        print('\n--dry-run: nothing rendered.')
        return

    out = Path(a.out) if a.out else ROOT / 'assets' / 'media' / 'explainers' / f'{src.stem}.mp4'
    out.parent.mkdir(parents=True, exist_ok=True)
    print(f'output   : {out}')
    print('\nRendering is handled by bin/render_explainer.js (Playwright) + piper + ffmpeg.')
    print('Run:  node bin/render_explainer.js ' + json.dumps({
        'page': a.page, 'voice': a.voice, 'out': str(out)}))


if __name__ == '__main__':
    main()
