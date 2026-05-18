#!/usr/bin/env python3
"""
build-og-images.py — generate 10 Open Graph share-card images, one per
per-category deep-dive page, at 1200×630 with the silver palette and
brand-faithful layout. Saved to assets/og/og-citizen-<slug>.jpg.

After running, update each /citizen/<slug>.html to point at its dedicated
og:image (currently they all point at the shared og-citizen.jpg).
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = 'assets/og'
W, H = 1200, 630

# Silver-tier palette (matches the v4.0 brand)
BG_TOP = (8, 10, 14)         # near-black background top
BG_BOTTOM = (20, 24, 32)     # slightly lighter bottom
SILVER = (200, 207, 217)     # primary accent
SILVER_DIM = (138, 148, 162) # secondary
GOLD = (201, 168, 76)        # America First accent
WHITE = (240, 240, 240)
MUTED = (130, 140, 150)
GOD_BG = (40, 44, 52)        # silver-tinted card bg
AMERICA_BG = (45, 38, 24)    # gold-tinted card bg

# Categories — slug + label + tagline + tier + num
CATEGORIES = [
    ('sanctity-of-life',         'Sanctity of Life',              'Personhood from conception. No carve-outs.',                 'god_first',     1),
    ('biblical-marriage',        'Biblical Marriage',             'One man, one woman, for life — and no redefinition of sex.', 'god_first',     2),
    ('family-child-sovereignty', 'Family & Child Sovereignty',    'Parents over the state. The state out of the school.',       'god_first',     3),
    ('christian-liberty',        'Christian Liberty',             'Freedom to profess Christ — including the freedom to disagree.', 'god_first',     4),
    ('economic-stewardship',     'Economic Stewardship',          'Sound money. No CBDC. No debt-slavery. Audit the Fed.',      'god_first',     5),
    ('election-integrity',       'Election Integrity',            'Paper. Hand-counted. Single-day. Citizen-only.',             'god_first',     6),
    ('border-immigration',       'Border & Immigration',          'A nation that cannot enforce its border is not a nation.',   'america_first', 7),
    ('self-defense-2a',          'Self-Defense & 2A',             'The God-given right to protect household and neighbor.',     'america_first', 8),
    ('foreign-policy-restraint', 'Foreign Policy Restraint',      'Article I war powers. No forever wars. No foreign-lobby ownership.', 'america_first', 9),
    ('industry-capture',         'Industry Capture & Sovereignty', 'Anti-Pharma. Anti-Big-Ag. Anti-MIC. Anti-cartel.',          'america_first', 10),
]

# Font selection — fall back to default if specific TrueType isn't available.
def get_font(size, bold=False):
    candidates = [
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Times New Roman.ttf',
        '/Library/Fonts/Arial Bold.ttf' if bold else '/Library/Fonts/Arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=1 if bold and path.endswith('.ttc') else 0)
            except Exception:
                continue
    return ImageFont.load_default()

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def render_card(slug, label, tagline, tier, num):
    img = Image.new('RGB', (W, H), BG_TOP)
    px = img.load()
    # Vertical gradient
    for y in range(H):
        c = lerp(BG_TOP, BG_BOTTOM, y / H)
        for x in range(W):
            px[x, y] = c

    draw = ImageDraw.Draw(img, 'RGBA')

    tier_emoji = '✝' if tier == 'god_first' else '★'
    tier_label = 'GOD FIRST · 60 pts' if tier == 'god_first' else 'AMERICA FIRST · 40 pts'
    tier_color = SILVER if tier == 'god_first' else GOLD
    tier_bg = GOD_BG if tier == 'god_first' else AMERICA_BG

    # Tier pill — top-left
    pill_pad_x, pill_pad_y = 28, 14
    pill_font = get_font(22, bold=True)
    pill_text = f'{tier_emoji}  {tier_label}'
    bbox = draw.textbbox((0, 0), pill_text, font=pill_font)
    pw = bbox[2] - bbox[0] + pill_pad_x * 2
    ph = bbox[3] - bbox[1] + pill_pad_y * 2
    pill_x, pill_y = 70, 70
    draw.rounded_rectangle(
        (pill_x, pill_y, pill_x + pw, pill_y + ph),
        radius=30, fill=(tier_bg[0], tier_bg[1], tier_bg[2], 200),
        outline=tier_color, width=2)
    draw.text((pill_x + pill_pad_x, pill_y + pill_pad_y - 3),
              pill_text, font=pill_font, fill=tier_color)

    # Category number (huge, top-right)
    num_font = get_font(180, bold=True)
    num_text = f'{num}'
    num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
    num_w = num_bbox[2] - num_bbox[0]
    num_h = num_bbox[3] - num_bbox[1]
    # Subtle ghost text behind
    draw.text((W - num_w - 90 + 6, 60 + 6), num_text, font=num_font, fill=(0, 0, 0, 120))
    draw.text((W - num_w - 90, 60), num_text, font=num_font, fill=(tier_color[0], tier_color[1], tier_color[2], 90))

    # Main title — centered vertically, left-aligned
    title_font = get_font(64, bold=True)
    title_y = 240
    # Wrap if needed
    title_lines = wrap_text(label, title_font, W - 140, draw)
    for line in title_lines:
        draw.text((70, title_y), line, font=title_font, fill=WHITE)
        title_y += 78

    # Tagline — italic feel via separate font, wrapped
    tagline_font = get_font(28)
    tagline_y = title_y + 16
    tagline_lines = wrap_text(tagline, tagline_font, W - 140, draw)
    for line in tagline_lines[:2]:  # cap at 2 lines
        draw.text((70, tagline_y), line, font=tagline_font, fill=SILVER_DIM)
        tagline_y += 38

    # Bottom strip — RESOLUTE CITIZEN · USMC MINISTRIES
    strip_y = H - 70
    draw.line([(70, strip_y), (W - 70, strip_y)], fill=(60, 60, 60), width=1)
    foot_font = get_font(24, bold=True)
    draw.text((70, strip_y + 18), 'RESOLUTE CITIZEN  ·  USMCMIN.COM', font=foot_font, fill=SILVER)

    # "100-PT SCORECARD" right-aligned
    right_font = get_font(20)
    right_text = '10 categories  ·  100-pt scorecard'
    rb = draw.textbbox((0, 0), right_text, font=right_font)
    rw = rb[2] - rb[0]
    draw.text((W - rw - 70, strip_y + 22), right_text, font=right_font, fill=MUTED)

    return img

def wrap_text(text, font, max_width, draw):
    words = text.split(' ')
    lines, cur = [], ''
    for w in words:
        candidate = (cur + ' ' + w).strip()
        bb = draw.textbbox((0, 0), candidate, font=font)
        if bb[2] - bb[0] <= max_width:
            cur = candidate
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, label, tagline, tier, num in CATEGORIES:
        img = render_card(slug, label, tagline, tier, num)
        out_path = os.path.join(OUT_DIR, f'og-citizen-{slug}.jpg')
        img.save(out_path, 'JPEG', quality=88, optimize=True)
        size_kb = os.path.getsize(out_path) / 1024
        print(f'  wrote {out_path}  ({size_kb:.0f} KB)')
    print(f'\nGenerated {len(CATEGORIES)} OG images.')

if __name__ == '__main__':
    main()
