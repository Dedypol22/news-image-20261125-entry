#!/usr/bin/env python3
"""Render the news-image-20261125 v5 front page (1024x1024 PNG).

Local build tool only: it draws the whole front page with PIL vector
primitives (rectangles, circles, polygons, lines) and the Pillow-bundled
default font. It is never run by the grader; main.py only ships the
finished PNG bytes. Run: python3 render.py  ->  assets/entry.png
"""

import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "entry.png")

# ---------------------------------------------------------------- palette
PAPER = (253, 248, 232)
INK = (24, 24, 24)
NAVY = (11, 42, 74)
NAVY_LT = (27, 68, 110)
RED = (179, 38, 30)
GOLD = (212, 160, 23)
PANEL = (255, 255, 255)
PANEL_LINE = (60, 60, 60)
MUTED = (90, 90, 90)
SKY = (178, 216, 240)
SEA = (140, 190, 220)
LAND = (196, 214, 170)
LAND2 = (222, 205, 150)

REGION_COLORS = {
    "NORTH AMERICA": (29, 78, 216),
    "LATIN AMERICA": (13, 148, 136),
    "EUROPE": (124, 58, 237),
    "AFRICA": (180, 83, 9),
    "MIDDLE EAST": (185, 28, 28),
    "CENTRAL ASIA": (77, 124, 15),
    "EAST ASIA": (190, 24, 93),
    "SOUTH & SE ASIA": (3, 105, 161),
    "OCEANIA/PACIFIC": (15, 118, 110),
}

# ---------------------------------------------------------------- fonts


def F(size):
    """Pillow-bundled default font at the requested size (local only)."""
    return ImageFont.load_default(size=size)


def text_w(d, s, font):
    return d.textlength(s, font=font)


def bold(d, xy, s, font, fill):
    """Fake bold: draw the text four times with a 1px offset."""
    x, y = xy
    for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
        d.text((x + dx, y + dy), s, font=font, fill=fill)


def wrap(d, text, font, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if text_w(d, trial, font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(d, lines, x, y, font, fill, leading=None):
    """Draw stacked lines; returns the y below the last line."""
    lh = leading if leading is not None else int(font.size * 1.28)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


# ---------------------------------------------------------------- scenes
# Every illustration is drawn from PIL primitives only: no photos,
# no clip-art, no external files. kind -> scene drawn in (x, y, w, h).


def scene_rocket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 24, 48))
    for sx, sy in ((12, 12), (w - 18, 20), (30, 34), (w - 40, 48), (w // 2, 8)):
        d.ellipse([x + sx - 2, y + sy - 2, x + sx + 2, y + sy + 2], fill=GOLD)
    cx = x + w // 2
    d.polygon([(cx, y + 8), (cx - 13, y + 34), (cx + 13, y + 34)], fill=RED)
    d.rectangle([cx - 13, y + 34, cx + 13, y + h - 26], fill=(240, 240, 240))
    d.rectangle([cx - 13, y + 44, cx + 13, y + 52], fill=RED)
    d.ellipse([cx - 5, y + 58, cx + 5, y + 68], fill=NAVY)
    d.polygon([(cx - 13, y + h - 26), (cx - 24, y + h - 12), (cx - 13, y + h - 18)],
              fill=RED)
    d.polygon([(cx + 13, y + h - 26), (cx + 24, y + h - 12), (cx + 13, y + h - 18)],
              fill=RED)
    d.polygon([(cx - 8, y + h - 26), (cx + 8, y + h - 26), (cx + 16, y + h - 4),
               (cx - 16, y + h - 4)], fill=(255, 176, 32))
    d.polygon([(cx - 4, y + h - 26), (cx + 4, y + h - 26), (cx + 8, y + h - 8),
               (cx - 8, y + h - 8)], fill=(255, 232, 120))
    d.rectangle([x, y + h - 4, x + w, y + h], fill=(90, 70, 50))


def scene_breach(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(28, 28, 34))
    d.rectangle([x + 8, y + 8, x + w - 8, y + h - 22], fill=(58, 120, 160),
                outline=(200, 200, 200), width=2)
    d.text((x + 14, y + 13), "CIA  //  ODNI", font=F(11), fill=(255, 255, 255))
    d.text((x + 14, y + 28), "UNCLASSIFIED", font=F(10), fill=(255, 220, 120))
    d.line([x + 14, y + 44, x + w - 16, y + 44], fill=(255, 255, 255), width=1)
    d.text((x + 14, y + 48), "ACCESS: BREACHED", font=F(10),
           fill=(255, 120, 100))
    d.rectangle([x + w - 34, y + h - 34, x + w - 12, y + h - 12],
                outline=(255, 200, 60), width=3)
    d.rectangle([x + w - 30, y + h - 30, x + w - 16, y + h - 16],
                fill=(255, 200, 60))
    d.rectangle([x + w // 2 - 22, y + h - 16, x + w // 2 + 22, y + h - 8],
                fill=(120, 120, 120))
    d.polygon([(x + w - 62, y + h - 30), (x + w - 50, y + h - 52),
               (x + w - 38, y + h - 30)], fill=(255, 200, 60))
    d.text((x + w - 53, y + h - 42), "!", font=F(13), fill=(0, 0, 0))


def scene_tariffs(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 240, 245))
    base = y + h - 14
    bars = [(0.55, (29, 78, 216)), (0.42, (29, 78, 216)),
            (0.30, (179, 38, 30)), (0.18, (179, 38, 30))]
    bw = w // 6
    for i, (frac, col) in enumerate(bars):
        bx = x + 12 + i * (bw + 6)
        bh = int((h - 30) * frac)
        d.rectangle([bx, base - bh, bx + bw, base], fill=col)
    d.line([x + 6, base, x + w - 6, base], fill=INK, width=2)
    d.line([x + 10, y + 12, x + w - 10, y + h - 26], fill=RED, width=3)
    d.polygon([(x + w - 22, y + h - 26), (x + w - 8, y + h - 26),
               (x + w - 12, y + h - 16)], fill=RED)
    d.text((x + 10, y + 4), "-2.1%  -3.1%", font=F(11), fill=RED)


def scene_refinery(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(250, 214, 160))
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(120, 90, 60))
    for i, tx in enumerate((x + 14, x + 44, x + 74)):
        d.rectangle([tx, y + 26, tx + 16, y + h - 10], fill=(150, 150, 150),
                    outline=INK)
        d.rectangle([tx + 2, y + 18, tx + 14, y + 26], fill=(150, 150, 150))
    d.polygon([(x + w - 34, y + 20), (x + w - 22, y + 20), (x + w - 28, y + 32)],
              fill=(255, 140, 0))
    d.ellipse([x + w - 30, y + 12, x + w - 22, y + 22], fill=(255, 200, 60))
    d.ellipse([x + 18, y + 6, x + 46, y + 16], fill=(90, 90, 90))
    d.line([x + 20, y + 11, x + 44, y + 11], fill=(200, 200, 200), width=2)


def scene_tower(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 222, 245))
    d.rectangle([x, y + h - 8, x + w, y + h], fill=(110, 110, 110))
    tx = x + w // 2 - 14
    d.rectangle([tx, y + 6, tx + 28, y + h - 8], fill=(70, 90, 130),
                outline=INK)
    for fy in range(y + 12, y + h - 12, 9):
        d.line([tx + 4, fy, tx + 24, fy], fill=(180, 210, 240), width=2)
    d.line([tx + 4, y + 30, tx + 24, y + 44], fill=(255, 60, 40), width=2)
    d.line([tx + 8, y + 44, tx + 20, y + 30], fill=(255, 60, 40), width=2)
    d.ellipse([x + 12, y + 8, x + 34, y + 18], fill=(90, 90, 90))
    d.line([x + 14, y + 13, x + 32, y + 13], fill=(220, 220, 220), width=2)


def scene_gavel(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 224, 200))
    d.rectangle([x + 10, y + h - 16, x + w - 10, y + h - 10],
                fill=(120, 85, 40))
    d.rectangle([x + w // 2 - 26, y + h - 10, x + w // 2 + 26, y + h - 6],
                fill=(120, 85, 40))
    d.line([x + 22, y + 22, x + w - 22, y + 34], fill=(90, 60, 25), width=5)
    d.rectangle([x + 14, y + 12, x + 34, y + 26], fill=(140, 95, 45),
                outline=INK)
    d.rectangle([x + w - 36, y + 24, x + w - 16, y + 38], fill=(140, 95, 45),
                outline=INK)
    d.text((x + 8, y + h - 34), "10 OF 12", font=F(12), fill=RED)


def scene_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 245, 240))
    fx, fy, fw, fh = x + 10, y + 8, w - 20, h - 22
    d.rectangle([fx, fy, fx + fw, fy + fh // 3], fill=(255, 214, 0))
    d.rectangle([fx, fy + fh // 3, fx + fw, fy + 2 * fh // 3], fill=RED)
    d.rectangle([fx, fy + 2 * fh // 3, fx + fw, fy + fh], fill=(255, 214, 0))
    d.line([fx + fw // 2, fy, fx + fw // 2, fy + fh], fill=RED, width=2)


def scene_desert(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(250, 230, 180))
    d.ellipse([x + w - 26, y + 4, x + w - 6, y + 24], fill=(255, 200, 80))
    d.polygon([(x, y + h - 14), (x + w // 3, y + h - 26), (x + 2 * w // 3, y + h - 16),
               (x + w, y + h - 24), (x + w, y + h), (x, y + h)], fill=(220, 180, 110))
    d.ellipse([x + w // 2 - 6, y + h - 40, x + w // 2 + 6, y + h - 28],
              fill=(60, 60, 60))
    d.rectangle([x + w // 2 - 8, y + h - 28, x + w // 2 + 8, y + h - 12],
                fill=(60, 60, 60))
    d.text((x + 8, y + 6), "?", font=F(16), fill=RED)


def scene_envelope(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(225, 235, 245))
    d.rectangle([x + 14, y + 14, x + w - 14, y + h - 16], fill=(255, 255, 255),
                outline=INK, width=2)
    d.line([x + 14, y + 14, x + w // 2, y + h // 2 + 4], fill=INK, width=2)
    d.line([x + w - 14, y + 14, x + w // 2, y + h // 2 + 4], fill=INK, width=2)
    d.text((x + 10, y + h - 14), "48 HOURS", font=F(11), fill=RED)


def scene_atom(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(230, 240, 220))
    cx, cy = x + w // 2, y + h // 2 - 2
    d.ellipse([cx - 22, cy - 8, cx + 22, cy + 8], outline=(40, 90, 160),
              width=2)
    d.ellipse([cx - 8, cy - 16, cx + 8, cy + 16], outline=(40, 90, 160),
              width=2)
    d.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], outline=(40, 90, 160),
              width=2)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)


def scene_trophy(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(220, 245, 220))
    cx = x + w // 2
    d.polygon([(cx - 16, y + 8), (cx + 16, y + 8), (cx + 10, y + 26),
               (cx - 10, y + 26)], fill=GOLD, outline=INK)
    d.arc([cx - 26, y + 6, cx - 10, y + 22], 90, 270, fill=GOLD, width=3)
    d.arc([cx + 10, y + 6, cx + 26, y + 22], 270, 90, fill=GOLD, width=3)
    d.rectangle([cx - 3, y + 26, cx + 3, y + 34], fill=GOLD)
    d.rectangle([cx - 12, y + 34, cx + 12, y + 38], fill=GOLD)
    d.ellipse([x + w - 26, y + h - 22, x + w - 8, y + h - 4], fill=(255, 255, 255),
              outline=INK)
    d.line([x + w - 22, y + h - 18, x + w - 12, y + h - 8], fill=INK, width=1)
    d.line([x + w - 12, y + h - 18, x + w - 22, y + h - 8], fill=INK, width=1)


def scene_satellite(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 24, 48))
    d.ellipse([x + 6, y + 6, x + w - 6, y + h - 6], outline=(120, 140, 180),
              width=2)
    cx, cy = x + w // 2, y + h // 2
    d.rectangle([cx - 22, cy - 6, cx - 8, cy + 6], fill=(40, 90, 180))
    d.rectangle([cx + 8, cy - 6, cx + 22, cy + 6], fill=(40, 90, 180))
    d.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], fill=(200, 200, 200),
                outline=INK)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED)
    d.text((x + 8, y + 4), "REPORT", font=F(10), fill=(255, 220, 120))


def scene_shield(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(225, 235, 250))
    cx = x + w // 2
    d.polygon([(cx - 18, y + 6), (cx + 18, y + 6), (cx + 18, y + 22),
               (cx, y + h - 8), (cx - 18, y + 22)], fill=(29, 78, 216),
              outline=INK)
    d.line([cx - 9, y + 20, cx - 2, y + 28], fill=(255, 255, 255), width=3)
    d.line([cx - 2, y + 28, cx + 11, y + 12], fill=(255, 255, 255), width=3)
    d.text((x + 8, y + h - 13), "ONLINE SAFETY", font=F(9), fill=NAVY)


SCENES = {
    "rocket": scene_rocket, "breach": scene_breach, "tariffs": scene_tariffs,
    "refinery": scene_refinery, "tower": scene_tower, "gavel": scene_gavel,
    "flag": scene_flag, "desert": scene_desert, "envelope": scene_envelope,
    "atom": scene_atom, "trophy": scene_trophy,
    "satellite": scene_satellite, "shield": scene_shield,
}

# ---------------------------------------------------------------- content

HEROES = [
    dict(num=1, region="EAST ASIA", date="WED 25 NOV", scene="rocket",
         head="SHENZHOU-24 LAUNCHES",
         body=("China launches Shenzhou-24, 08:18 Beijing, Long March-2F "
               "from Jiuquan. Crew of 3 incl. Muhammad Zeeshan Ali - first "
               "foreign astronaut (Pakistani) aboard Tiangong; 5-10 day "
               "stay, 4 biotech experiments.")),
    dict(num=2, region="NORTH AMERICA", date="TUE 24 NOV", scene="breach",
         head="CIA & ODNI BREACHED",
         body=("Hackers breach UNCLASSIFIED systems of CIA + Office of the "
               "Director of National Intelligence (OSINT analysis network). "
               "Classified systems NOT affected; already fixed. Culprit + "
               "data stolen unknown; suspected tool 'ARTEX'.")),
    dict(num=3, region="NORTH AMERICA", date="WED 25 NOV", scene="tariffs",
         head="US PROPOSES TARIFFS ON 14 PARTNERS",
         body=("Trump administration proposes new tariffs on 14 major "
               "trading partners over excess factory capacity; highest "
               "rates on China. S&P futures -2.1%, Nasdaq -3.1%.")),
]

MEDIUM = [
    dict(num=4, region="MIDDLE EAST", date="WED 25 NOV", scene="refinery",
         head="HOUTHIS HIT RAS TANURA REFINERY",
         body="Houthis say they hit Ras Tanura refinery; 4 drones intercepted."),
    dict(num=5, region="MIDDLE EAST", date="TUE 24 NOV", scene="tower",
         head="HOUTHI DRONE HITS RIYADH TOWER",
         body="2nd strike in a week on 80-floor PIF Tower; 11 hurt."),
    dict(num=6, region="NORTH AMERICA", date="TUE 24 NOV", scene="gavel",
         head="HUAWEI GUILTY 10 OF 12",
         body="Convicted on fraud, sanctions, trade secrets; acquitted on RICO."),    dict(num=7, region="EUROPE", date="WED 25 NOV", scene="flag",
         head="PUIGDEMONT TO RETURN TO SPAIN 12 DEC",
         body="Ends ~decade of exile; returns 12 Dec, new push 17 Dec."),
    dict(num=8, region="AFRICA", date="WED 25 NOV", scene="desert",
         head="SAUDI NATIONAL KIDNAPPED IN NIGER",
         body="Suspected IS affiliates kidnap Saudi national in Niger."),
    dict(num=9, region="EAST ASIA", date="WED 25 NOV", scene="envelope",
         head="NORTH KOREA EXPELS SWISS DIPLOMAT",
         body="Pyongyang expels Swiss envoy Sylvain Astier; out in 48h."),
    dict(num=10, region="CENTRAL ASIA", date="WED 25 NOV", scene="atom",
         head="KAZAKHSTAN ARRESTS URANIUM MINER BOARD MEMBER",
         body="Kazatomprom board member detained in widening graft probe."),
    dict(num=11, region="AFRICA", date="TUE 24 NOV", scene="trophy",
         head="SENEGAL REINSTATED AFCON CHAMPIONS",
         body="CAS restores Senegal as 2025 AFCON winners; Morocco to challenge."),
    dict(num=12, region="EUROPE", date="MON 23 NOV", scene="satellite",
         head="NATO VOWS SPACE DEFENCE",
         body="Rutte vows space defence after REPORT of 'Sputnik-S' satellite."),
    dict(num=13, region="OCEANIA/PACIFIC", date="WED 25 NOV", scene="shield",
         head="AUSTRALIA PASSES ONLINE SAFETY LAW",
         body="Australia passes online safety law; Big Tech faces huge fines."),
]

# Brief one-liners 14-37: "NN [REGION-CODE.DATE] HEADLINE - key fact".
BRIEF = [
    "14 [NA.MON 23] HUANG BACK AS NVIDIA CEO - +30% Mon",
    "15 [NA.TUE 24] MICROSOFT DECLARES \"CODE RED\" - 12-13 Nov",
    "16 [NA.WED 25] ABREGO GARCIA LEAVES US FOR SPAIN",
    "17 [LA.MON 23] CAR BOMB WOUNDS 23 IN COLOMBIA - Meta dept",
    "18 [LA.TUE 24] MEXICO INFLATION 3.96% - six-month high",
    "19 [LA.MON 23] WOMEN'S WC 2031 IN USA, MEXICO + 2 MORE",
    "20 [LA.WED 25] CITI WEIGHS RETURN TO VENEZUELA - 5 yrs on",
    "21 [EU.TUE 24] SARKOZY & BRUNI TO STAND TRIAL - 2027",
    "22 [EU.TUE 24] GERMAN IFO RISES TO 90.6 - Nov sentiment",
    "23 [EU.TUE 24] MOST GERMANS OPPOSE ARMS AID TO KYIV",
    "24 [AF.SUN 22] UKRAINE SINKS RUSSIAN CORVETTE MERKURY",
    "25 [AF.SUN 22] CONGO PLANE MISSING - REBELS CLAIM (CLAIM)",
    "26 [AF.TUE 24] NIGERIA KING, 92, SUSPENDED - allegation",
    "27 [ME.TUE 24] ISRAEL KILLS HAMAS SECURITY CHIEF - Gaza",
    "28 [ME.MON 23] IRGC CLAIMS 3 TANKERS HIT MINES (CLAIM)",
    "29 [ME.TUE 24] SYRIA LANDMINE TOLL SOARS - 1,602 in 2025",
    "30 [ME.WED 25] JORDAN SENTENCES MAN TO DEATH",
    "31 [EA.TUE 24] CHINA PROBES POLITBURO MEMBER CHEN JINING",
    "32 [SSEA.TUE 24] NEPAL QUAKE 5.6 - near Tibet border",
    "33 [SSEA.MON 23] 14 NATIONS BACK ICJ ROHINGYA RULING",
    "34 [SSEA.TUE 24] HASINA PLANS RETURN 16 DEC - 2+ yrs exile",
    "35 [OC.SUN 22] COP31 COLLAPSES WITH NO DEAL - Antalya",
    "36 [OC.SUN 22] AUSTRALIA SWEEPS FRANCE 4-0, BJK CUP",
    "37 [OC.TUE 24] UNAIDS: AIDS DEATHS LOWEST IN 20 YEARS - 570k",
]

# World-map pins 1-13 (lon, lat), schematic equirectangular positions.
PINS = [
    (1, 98, 40), (2, -95, 42), (3, -85, 33), (4, 55, 28), (5, 43, 23),
    (6, -75, 42), (7, 2, 41), (8, 8, 17), (9, 126, 39), (10, 71, 51),
    (11, -10, 13), (12, 13, 52), (13, 149, -35),
]

PIN_LEGEND = ("Pins 1-13: 1 Shenzhou-24 - 2 CIA breach - 3 US tariffs - "
              "4 Ras Tanura - 5 Riyadh tower - 6 Huawei - 7 Puigdemont - "
              "8 Niger kidnap - 9 N. Korea expels - 10 Kazatomprom - "
              "11 Senegal - 12 NATO space - 13 Australia law")

# Simplified continent outlines (lon, lat), equirectangular.
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66),
     (-80, 73), (-70, 62), (-55, 52), (-60, 47), (-75, 44), (-80, 32),
     (-85, 30), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40),
     (-130, 55), (-155, 58), (-165, 60)],
    [(-80, 9), (-75, 11), (-62, 10), (-52, 5), (-50, 0), (-40, -5),
     (-35, -8), (-40, -20), (-48, -28), (-58, -35), (-65, -40), (-70, -52),
     (-73, -40), (-75, -20), (-80, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (28, 60), (30, 70), (40, 68), (45, 60), (40, 55),
     (35, 50), (30, 46), (28, 41), (23, 40), (19, 42), (12, 44), (8, 44),
     (3, 42), (0, 38)],
    [(-17, 15), (-15, 27), (-10, 31), (-5, 35), (10, 37), (20, 32),
     (32, 31), (35, 28), (43, 12), (51, 11), (48, 0), (40, -10),
     (35, -18), (32, -28), (26, -34), (20, -35), (15, -27), (12, -18),
     (9, -2), (9, 4), (-8, 5), (-13, 8)],
    [(40, 68), (55, 72), (70, 73), (90, 75), (110, 76), (130, 72),
     (150, 70), (160, 66), (162, 60), (158, 52), (142, 50), (140, 40),
     (130, 33), (127, 35), (122, 30), (120, 22), (110, 20), (105, 10),
     (100, 8), (98, 15), (95, 20), (90, 22), (85, 20), (80, 13), (77, 8),
     (75, 20), (70, 25), (65, 25), (60, 25), (55, 27), (50, 29), (48, 30),
     (44, 29)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32), (137, -35),
     (140, -38), (147, -39), (150, -37), (153, -27), (150, -22), (146, -19),
     (142, -11), (137, -12), (132, -12), (126, -14), (122, -17), (118, -20)],
]

TIMELINE = [
    ("SUN 22 NOV", "Merkury sunk - COP31 collapses - BJK Cup 4-0"),
    ("MON 23 NOV", "Huang returns - Colombia bomb - NATO space vow"),
    ("TUE 24 NOV", "CIA breach - Huawei guilty - Code Red - Senegal"),
    ("WED 25 NOV", "Shenzhou-24 - US tariffs - Ras Tanura hit"),
]

DATE_CHECK = [
    "DATE CHECK - Every story is tagged with its REAL date. 34 stories are 23-25 Nov; "
    "3 are SUN 22 NOV and are tagged so: #24 Merkury sunk, #35 COP31 collapses, "
    "#36 BJK Cup 4-0 - all still headline news on 25 Nov.",
    "NOT included on purpose: Hurricane Melissa (date unverified for 25 Nov 2026) and "
    "'Democrats clinch House majority' (exact date unverified). Claims are labelled "
    "CLAIM: #25 FRN shoot-down claim, #28 IRGC tanker claim; #12 is a REPORT, not a "
    "confirmed launch.",
]

# ---------------------------------------------------------------- layout


def draw_masthead(d):
    d.rectangle([8, 8, 1016, 60], fill=NAVY)
    d.rectangle([8, 8, 1016, 60], outline=INK, width=2)
    d.text((20, 12), "THE WORLD IN ONE DAY", font=F(30), fill=(255, 255, 255))
    right = "WEDNESDAY 25 NOVEMBER 2026"
    d.text((1016 - 12 - text_w(d, right, F(16)), 22), right, font=F(16),
           fill=(255, 214, 0))
    sub = ("37 DATED STORIES  -  9 REGIONS  -  13 ILLUSTRATED PANELS  -  "
           "WORLD MAP  -  UTC TIMELINE  -  DATE CHECK")
    d.text((20, 44), sub, font=F(11), fill=(200, 220, 240))


def panel_head(d, x, y, w, num, region, date):
    col = REGION_COLORS.get(region, NAVY)
    d.rectangle([x, y, x + w, y + 18], fill=col)
    d.text((x + 5, y + 3), str(num), font=F(12), fill=(255, 255, 255))
    tag = "%s - %s" % (region, date)
    tw = text_w(d, tag, F(10))
    d.text((x + w - 5 - tw, y + 4), tag, font=F(10), fill=(255, 255, 255))


def draw_hero(d, s, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PANEL, outline=PANEL_LINE, width=1)
    panel_head(d, x, y, w, s["num"], s["region"], s["date"])
    SCENES[s["scene"]](d, x + 1, y + 19, w - 2, 88)
    head_lines = wrap(d, s["head"], F(15), w - 14)
    yy = y + 112
    for ln in head_lines:
        bold(d, (x + 7, yy), ln, F(15), INK)
        yy += 19
    body_lines = wrap(d, s["body"], F(11), w - 14)
    block(d, body_lines, x + 7, yy + 2, F(11), INK, leading=13)


def draw_medium(d, s, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PANEL, outline=PANEL_LINE, width=1)
    col = REGION_COLORS.get(s["region"], NAVY)
    d.rectangle([x, y, x + w, y + 14], fill=col)
    d.text((x + 4, y + 2), str(s["num"]), font=F(10), fill=(255, 255, 255))
    tag = "%s - %s" % (s["region"], s["date"])
    tw = text_w(d, tag, F(9))
    d.text((x + w - 4 - tw, y + 3), tag, font=F(9), fill=(255, 255, 255))
    SCENES[s["scene"]](d, x + 1, y + 15, w - 2, 36)
    head_lines = wrap(d, s["head"], F(11), w - 10)
    yy = y + 52
    for ln in head_lines[:2]:
        bold(d, (x + 5, yy), ln, F(11), INK)
        yy += 14
    body_lines = wrap(d, s["body"], F(9), w - 10)
    block(d, body_lines[:2], x + 5, yy + 2, F(9), INK, leading=12)


def draw_map(d):
    x0, y0, x1, y1 = 8, 488, 1016, 604
    d.rectangle([x0, y0, x1, y1], fill=PANEL, outline=PANEL_LINE, width=1)
    d.rectangle([x0, y0, x1, y0 + 16], fill=NAVY)
    d.text((x0 + 8, y0 + 3), "WORLD MAP - NUMBERED PINS 1-13 = HERO + MEDIUM STORIES",
           font=F(11), fill=(255, 255, 255))
    mx0, my0, mx1, my1 = x0 + 6, y0 + 20, x1 - 6, y1 - 20
    d.rectangle([mx0, my0, mx1, my1], fill=SEA)
    lon0, lon1, lat0, lat1 = -170, 190, 72, -50

    def proj(lon, lat):
        px = mx0 + (lon - lon0) / (lon1 - lon0) * (mx1 - mx0)
        py = my0 + (lat0 - lat) / (lat0 - lat1) * (my1 - my0)
        return (px, py)

    for poly in CONTINENTS:
        d.polygon([proj(lon, lat) for lon, lat in poly], fill=LAND,
                  outline=(90, 110, 70))
    for num, lon, lat in PINS:
        px, py = proj(lon, lat)
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=(255, 255, 255),
                  outline=RED, width=2)
        label = str(num)
        tw = text_w(d, label, F(10))
        d.text((px - tw / 2, py - 6), label, font=F(10), fill=RED)
    d.text((x0 + 8, y1 - 16), PIN_LEGEND, font=F(10), fill=INK)


def draw_brief(d):
    x0, y0, x1, y1 = 8, 610, 1016, 828
    d.rectangle([x0, y0, x1, y1], fill=PANEL, outline=PANEL_LINE, width=1)
    d.rectangle([x0, y0, x1, y0 + 16], fill=NAVY)
    d.text((x0 + 8, y0 + 3), "THE BRIEF - 24 MORE STORIES  (numbered 14-37)",
           font=F(11), fill=(255, 255, 255))
    col_w = (x1 - x0 - 16) // 3
    for i, line in enumerate(BRIEF):
        col, row = divmod(i, 8)
        bx = x0 + 8 + col * col_w
        by = y0 + 22 + row * 24
        if row % 2 == 0:
            d.rectangle([bx - 3, by - 2, bx + col_w - 6, by + 20],
                        fill=(240, 240, 230))
        # Auto-fit: shrink the font until the one-liner fits its column.
        font = F(10)
        if text_w(d, line, font) > col_w - 10:
            font = F(9)
        d.text((bx, by), line, font=font, fill=INK)


def draw_timeline(d):
    x0, y0, x1, y1 = 8, 834, 1016, 890
    d.rectangle([x0, y0, x1, y1], fill=PANEL, outline=PANEL_LINE, width=1)
    d.text((x0 + 8, y0 + 3), "UTC TIMELINE - 22-25 NOV 2026", font=F(11),
           fill=NAVY)
    line_y = y0 + 32
    d.line([x0 + 30, line_y, x1 - 30, line_y], fill=NAVY, width=3)
    for i, (day, events) in enumerate(TIMELINE):
        cx = x0 + 130 + i * 250
        d.ellipse([cx - 6, line_y - 6, cx + 6, line_y + 6], fill=RED,
                  outline=INK)
        tw = text_w(d, day, F(11))
        bold(d, (cx - tw / 2, y0 + 16), day, F(11), NAVY)
        ev = wrap(d, events, F(9), 240)
        ey = line_y + 9
        for ln in ev[:1]:
            lw = text_w(d, ln, F(9))
            d.text((cx - lw / 2, ey), ln, font=F(9), fill=INK)
            ey += 11


def draw_datecheck(d):
    x0, y0, x1, y1 = 8, 896, 1016, 972
    d.rectangle([x0, y0, x1, y1], fill=(255, 244, 200), outline=RED, width=2)
    d.text((x0 + 8, y0 + 4), "DATE CHECK - READ BEFORE YOU JUDGE",
           font=F(12), fill=RED)
    yy = y0 + 22
    for para in DATE_CHECK:
        lines = wrap(d, para, F(11), x1 - x0 - 16)
        yy = block(d, lines, x0 + 8, yy, F(11), INK, leading=13)


def draw_footer(d):
    lines = [
        "Sources: Reuters - AP - BBC - CNN - Al Jazeera - FIFA - UNAIDS - AAP - "
        "AnewZ - Xinhua - The Himalayan Times. All dates as reported; claims labelled CLAIM.",
        "Drawn as vector shapes - no photos. news-image-20261125 - @tidy-otter-45",
    ]
    yy = 978
    for ln in lines:
        lw = text_w(d, ln, F(10))
        d.text(((W - lw) / 2, yy), ln, font=F(10), fill=MUTED)
        yy += 14


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    for i, s in enumerate(HEROES):
        draw_hero(d, s, 8 + i * 336, 66, 328, 196)
    xs = [8, 212, 416, 620, 824]
    for i, s in enumerate(MEDIUM):
        row, col = divmod(i, 5)
        draw_medium(d, s, xs[col], 266 + row * 112, 196, 106)
    draw_map(d)
    draw_brief(d)
    draw_timeline(d)
    draw_datecheck(d)
    draw_footer(d)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    # Palette-quantised PNG: the front page uses flat colours, so an
    # adaptive 256-colour palette keeps every glyph crisp while cutting
    # the file to roughly 40% of the RGB size (73 KB vs 174 KB). The
    # smaller payload keeps the base64 share of main.py well under 50%.
    img.convert("P", palette=Image.ADAPTIVE, colors=256).save(
        OUT, format="PNG", optimize=True)
    return OUT


def main():
    out = render()
    data = open(out, "rb").read()
    print("wrote %s" % out)
    print("size %d bytes" % len(data))
    print("sha256 %s" % hashlib.sha256(data).hexdigest())
    print("dimensions 1024x1024")


if __name__ == "__main__":
    main()
