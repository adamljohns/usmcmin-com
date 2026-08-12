#!/usr/bin/env python3
"""build-og-fitness.py — 1200×630 Open Graph cards for fitness / fit20 pages.

Brand: USMC Ministries fitness desk — navy / gold / charcoal (Coach Moop lane).
Pattern mirrors build-og-bow-arrow.py (branded cards, not raw photos alone).

Outputs under assets/og/og-fitness*.jpg

Run from repo root:
  python3 build-og-fitness.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "og"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630

# Fitness brand (dark command + gold accent — matches fitness/index hero)
NAVY = (14, 28, 48)
NAVY_MID = (22, 44, 72)
NAVY_DEEP = (8, 16, 28)
CHARCOAL = (18, 18, 20)
GOLD = (212, 175, 55)
GOLD_SOFT = (230, 205, 120)
GOLD_DARK = (168, 132, 36)
CREAM = (245, 242, 235)
STEEL = (160, 175, 195)
WHITE = (250, 250, 252)
MUTED = (180, 190, 205)

PLAYFAIR = Path("/Users/moop_bot_pro/Library/Fonts/PlayfairDisplay[wght].ttf")
GEORGIA_B = Path("/System/Library/Fonts/Supplemental/Georgia Bold.ttf")
GEORGIA = Path("/System/Library/Fonts/Supplemental/Georgia.ttf")
HELV = Path("/System/Library/Fonts/Helvetica.ttc")
ARIAL_B = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")


def font(path: Path, size: int, weight: int | None = None, index: int = 0):
    try:
        if path.suffix == ".ttf" and "[" in path.name:
            f = ImageFont.truetype(str(path), size)
            if weight is not None:
                try:
                    f.set_variation_by_axes([weight])
                except Exception:
                    pass
            return f
        return ImageFont.truetype(str(path), size, index=index)
    except Exception:
        try:
            return ImageFont.truetype(str(ARIAL_B), size)
        except Exception:
            return ImageFont.load_default()


def text_width(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_width(draw, trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def navy_field() -> Image.Image:
    """Dark navy vertical wash with subtle gold vignette."""
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        # top slightly lighter navy mid → deep bottom
        r = int(NAVY_MID[0] * (1 - t) + NAVY_DEEP[0] * t)
        g = int(NAVY_MID[1] * (1 - t) + NAVY_DEEP[1] * t)
        b = int(NAVY_MID[2] * (1 - t) + NAVY_DEEP[2] * t)
        for x in range(W):
            # right-side warmth fade
            xr = x / (W - 1)
            boost = int(8 * xr)
            px[x, y] = (min(255, r + boost), min(255, g + boost // 2), min(255, b))
    # soft gold radial at top-center
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for i, a in enumerate((28, 18, 10, 4)):
        pad = 40 + i * 70
        od.ellipse((W // 2 - 420 + pad, -180 + pad, W // 2 + 420 - pad, 260 - pad // 2), fill=(*GOLD, a))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def brand_chrome(draw: ImageDraw.ImageDraw):
    # top gold rule
    draw.rectangle((0, 0, W, 7), fill=GOLD)
    # left gold bar
    draw.rectangle((0, 0, 12, H), fill=GOLD)
    # bottom command strip
    draw.rectangle((0, H - 78, W, H), fill=NAVY_DEEP)
    draw.rectangle((0, H - 82, W, H - 78), fill=GOLD)
    f_brand = font(PLAYFAIR, 28, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 26)
    f_small = font(HELV, 18, index=0)
    draw.text((52, H - 54), "U.S.M.C. Ministries · Fitness", font=f_brand, fill=CREAM)
    place = "Coach Moop · Fredericksburg, VA"
    pw = text_width(draw, place, f_small)
    draw.text((W - 52 - pw, H - 48), place, font=f_small, fill=GOLD_SOFT)


def kicker_pill(draw, text: str, x=52, y=58):
    f_kick = font(HELV, 18, index=0)
    kick = text.upper()
    kb = draw.textbbox((0, 0), kick, font=f_kick)
    kw, kh = kb[2] - kb[0], kb[3] - kb[1]
    pad_x, pad_y = 16, 9
    draw.rounded_rectangle(
        (x, y, x + kw + pad_x * 2, y + kh + pad_y * 2),
        radius=4,
        fill=(*GOLD, 235),
    )
    draw.text((x + pad_x, y + pad_y - 1), kick, font=f_kick, fill=NAVY_DEEP)
    return y + kh + pad_y * 2 + 28


def render_brand_card(
    kicker: str,
    title: str,
    subtitle: str,
    out_name: str,
    badge: str | None = None,
    photo: Path | None = None,
    photo_side: str = "right",
):
    base = navy_field().convert("RGBA")

    if photo and photo.exists():
        src = Image.open(photo).convert("RGB")
        src = ImageEnhance.Color(src).enhance(1.02)
        src = ImageEnhance.Contrast(src).enhance(1.08)
        # portrait panel on right third
        panel_w = 420
        sw, sh = src.size
        scale = max(panel_w / sw, H / sh)
        nw, nh = int(sw * scale + 0.5), int(sh * scale + 0.5)
        src = src.resize((nw, nh), Image.Resampling.LANCZOS)
        left = max(0, (nw - panel_w) // 2)
        top = max(0, (nh - H) // 5)
        crop = src.crop((left, top, left + panel_w, top + H))
        # darken edge blend
        panel = crop.convert("RGBA")
        grad = Image.new("RGBA", (panel_w, H), (0, 0, 0, 0))
        gpx = grad.load()
        for x in range(panel_w):
            a = int(200 * (1 - x / 90)) if x < 90 else 0
            a = max(0, min(220, a))
            for y in range(H):
                # also bottom fade into footer
                yb = 0
                if y > H - 120:
                    yb = int(160 * ((y - (H - 120)) / 120))
                gpx[x, y] = (*NAVY_DEEP, max(a, yb))
        panel = Image.alpha_composite(panel, grad)
        if photo_side == "right":
            base.paste(panel, (W - panel_w, 0), panel)
        else:
            base.paste(panel, (0, 0), panel)

    draw = ImageDraw.Draw(base, "RGBA")
    brand_chrome(draw)

    ty = kicker_pill(draw, kicker)

    max_title_w = W - 520 if photo and photo.exists() else W - 120
    f_title = font(PLAYFAIR, 58, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 54)
    for line in wrap(draw, title, f_title, max_title_w)[:3]:
        # soft shadow
        draw.text((54, ty + 3), line, font=f_title, fill=(0, 0, 0, 110))
        draw.text((52, ty), line, font=f_title, fill=CREAM)
        ty += 68

    f_sub = font(HELV, 26, index=0)
    sy = ty + 10
    for line in wrap(draw, subtitle, f_sub, max_title_w - 20)[:3]:
        draw.text((52, sy), line, font=f_sub, fill=MUTED)
        sy += 34

    if badge:
        f_badge = font(HELV, 17, index=0)
        bb = draw.textbbox((0, 0), badge, font=f_badge)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        bx, by = W - 52 - bw - 36, 56
        # keep badge clear of photo if present on right
        if photo and photo.exists() and photo_side == "right":
            bx = min(bx, W - 420 - bw - 48)
        draw.rounded_rectangle(
            (bx, by, bx + bw + 36, by + bh + 18),
            radius=4,
            outline=GOLD,
            width=2,
            fill=(*NAVY, 210),
        )
        draw.text((bx + 18, by + 9), badge, font=f_badge, fill=GOLD_SOFT)

    out_path = OUT / out_name
    base.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}")
    return out_path


def render_cert_card(abbr: str, full: str, line: str, out_name: str, badge: str):
    """Specialty cert cards — big gold abbreviation."""
    base = navy_field().convert("RGBA")
    draw = ImageDraw.Draw(base, "RGBA")
    brand_chrome(draw)

    kicker_pill(draw, "Certification · Coach Moop")

    f_abbr = font(PLAYFAIR, 96, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 90)
    draw.text((54, 150), abbr, font=f_abbr, fill=GOLD)

    f_full = font(PLAYFAIR, 40, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 36)
    ty = 270
    for ln in wrap(draw, full, f_full, W - 140)[:2]:
        draw.text((52, ty), ln, font=f_full, fill=CREAM)
        ty += 50

    f_sub = font(HELV, 24, index=0)
    sy = ty + 16
    for ln in wrap(draw, line, f_sub, W - 160)[:3]:
        draw.text((52, sy), ln, font=f_sub, fill=MUTED)
        sy += 32

    f_badge = font(HELV, 17, index=0)
    bb = draw.textbbox((0, 0), badge, font=f_badge)
    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
    bx, by = W - 52 - bw - 36, 56
    draw.rounded_rectangle(
        (bx, by, bx + bw + 36, by + bh + 18),
        radius=4,
        outline=GOLD,
        width=2,
        fill=(*NAVY, 210),
    )
    draw.text((bx + 18, by + 9), badge, font=f_badge, fill=GOLD_SOFT)

    # decorative diagonal mark
    draw.polygon([(W - 180, H - 78), (W, H - 78), (W, H - 200)], fill=(*GOLD, 28))

    out_path = OUT / out_name
    base.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}")
    return out_path


def main():
    portrait = ROOT / "assets" / "img" / "adam-johns-portrait.jpg"

    # Hub + core landings
    render_brand_card(
        "NASM · fit20 · Body Stewardship",
        "Fitness with Coach Moop",
        "Strength, slow-rep training, and nutrition coaching rooted in biblical stewardship of the body.",
        "og-fitness.jpg",
        badge="FITNESS",
        photo=portrait if portrait.exists() else None,
    )
    render_brand_card(
        "Meet Your Trainer",
        "Coach Moop",
        "NASM CPT · CNC · PES · WLS · fit20. Marine veteran. Fredericksburg, VA.",
        "og-fitness-trainer.jpg",
        badge="TRAINER",
        photo=portrait if portrait.exists() else None,
    )
    render_brand_card(
        "Start Here · Intake",
        "Fitness Coaching Intake",
        "NASM-certified assessment: body comp, training history, nutrition, and a starter plan.",
        "og-fitness-intake.jpg",
        badge="INTAKE",
    )
    render_brand_card(
        "MOOP's Real Stack",
        "Supplement Stack",
        "What a Marine veteran trainer actually takes — and what he stopped wasting money on.",
        "og-fitness-supplements.jpg",
        badge="STACK",
    )
    render_brand_card(
        "Supplement Detail",
        "Protocol Notes",
        "Dose, timing, and why it stays in the stack — NASM-informed, field-tested.",
        "og-fitness-supplement-detail.jpg",
        badge="PROTOCOL",
    )

    # Certs
    render_cert_card(
        "CPT",
        "NASM Certified Personal Trainer",
        "Gold-standard personal training. NCCA-accredited OPT model programming.",
        "og-fitness-cert-cpt.jpg",
        "NASM",
    )
    render_cert_card(
        "CNC",
        "NASM Certified Nutrition Coach",
        "Evidence-based nutrition coaching for real habits and lasting results.",
        "og-fitness-cert-cnc.jpg",
        "NASM",
    )
    render_cert_card(
        "PES",
        "NASM Performance Enhancement",
        "Athletic performance: speed, power, agility — specialist-level programming.",
        "og-fitness-cert-pes.jpg",
        "NASM",
    )
    render_cert_card(
        "WLS",
        "NASM Weight Loss Specialist",
        "Fat-loss science: hormones, behavior, and sustainable programming.",
        "og-fitness-cert-wls.jpg",
        "NASM",
    )
    render_cert_card(
        "fit20",
        "fit20 Certified Trainer",
        "20 minutes, once a week. Slow-motion high-intensity strength training.",
        "og-fitness-cert-fit20.jpg",
        "fit20",
    )

    # Replace weak legacy PNG placeholder with matching hub JPEG name alias note
    # Keep og-fitness.png only if something still points at it; hub now uses .jpg
    print("DONE")


if __name__ == "__main__":
    main()
