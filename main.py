#!/usr/bin/env python3
"""Draw a one-page newspaper front page for Saturday 21 November 2026.

The picture is painted with Pillow only: no network, no downloaded assets,
no clock reads, so two runs write byte-identical PNGs. The stories are
baked into the script as plain text (all of them verified from two or more
sources on the day itself). Run from the repository root with
MAKEFUN_OUTPUT_DIR pointing at a writable folder; the page lands there as
entry.png, 1024 by 1024 pixels.
"""

import os

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
EDGE = 34
INK = (18, 18, 18)
PAPER = (248, 244, 233)
RED = (163, 18, 18)
NAVY = (29, 63, 110)
GREY = (92, 92, 88)
NIGHT = (32, 36, 46)
FLAME = (232, 122, 32)
EMBER = (198, 52, 28)
WINDOW_LIT = (232, 200, 90)

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def split_lines(text, face, width):
    """Greedy word wrap: returns the lines that fit inside width."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if face.getlength(trial) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fitted(text, path, start, width):
    """Largest size at or below start that still fits width."""
    size = start
    while size > 10 and font(path, size).getlength(text) > width:
        size -= 2
    return font(path, size)


def rule(draw, y, x0, x1, weight=2, colour=INK):
    draw.line([(x0, y), (x1, y)], fill=colour, width=weight)


def double_rule(draw, y, x0, x1):
    rule(draw, y, x0, x1, 3)
    rule(draw, y + 6, x0, x1, 1)


def kicker(draw, x, y, text):
    face = font(SANS_BOLD, 23)
    draw.text((x, y), text, font=face, fill=RED)
    return y + 32


def headline(draw, x, y, width, text, size=44):
    face = font(SERIF_BOLD, size)
    lines = split_lines(text, face, width)
    for line in lines:
        draw.text((x, y), line, font=face, fill=INK)
        y += size + 6
    return y


def paragraph(draw, x, y, width, text, size=24):
    face = font(SANS, size)
    for line in split_lines(text, face, width):
        draw.text((x, y), line, font=face, fill=INK)
        y += size + 8
    return y


def night_scene(draw, x, y, w, h):
    """A small flat illustration: tower blocks at night, one ablaze."""
    draw.rectangle([x, y, x + w, y + h], fill=NIGHT)
    base = y + h
    blocks = [(0, 0.52, 0.20), (0.22, 0.38, 0.16), (0.40, 0.58, 0.22),
              (0.64, 0.44, 0.18), (0.84, 0.60, 0.16)]
    for fx, fh, fw in blocks:
        bx = x + int(w * fx)
        bw = int(w * fw)
        bh = int(h * fh)
        draw.rectangle([bx, base - bh, bx + bw, base], fill=(46, 52, 66))
        floors = 2 if bh >= 50 else 1
        for row in range(floors):
            for col in range(2):
                wx = bx + 8 + col * (bw // 2)
                wy = base - bh + 10 + row * 22
                draw.rectangle([wx, wy, wx + 9, wy + 12], fill=WINDOW_LIT)
    # flames licking from the middle block's roof
    fx = x + int(w * 0.47)
    fy = base - int(h * 0.58)
    draw.polygon([(fx - 26, fy), (fx - 8, fy - 34), (fx + 2, fy - 8),
                  (fx + 16, fy - 40), (fx + 30, fy)], fill=FLAME)
    draw.polygon([(fx - 12, fy), (fx, fy - 22), (fx + 14, fy)], fill=EMBER)
    # smoke curling up, kept inside the panel so it never covers the text
    for cx, cy, r in [(fx + 34, y + 22, 9), (fx + 50, y + 38, 12),
                      (fx + 68, y + 56, 14)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 122, 128))
    draw.rectangle([x, base - 4, x + w, base], fill=(20, 22, 30))


def story_cell(draw, x, y, w, tag, head, body):
    y = kicker(draw, x, y, tag)
    y = headline(draw, x, y, w, head, size=31)
    y = paragraph(draw, x, y, w, body, size=21)
    return y


def build():
    sheet = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(sheet)
    draw.rectangle([10, 10, PAGE - 11, PAGE - 11], outline=INK, width=3)

    inner = PAGE - 2 * EDGE
    # dateline
    when = font(SANS_BOLD, 25)
    label = "SATURDAY 21 NOVEMBER 2026"
    draw.text(((PAGE - when.getlength(label)) / 2, 26), label,
              font=when, fill=INK)
    rule(draw, 62, EDGE, PAGE - EDGE, 2)

    # masthead
    mast = fitted("THE WORLD IN ONE DAY", SERIF_BOLD, 84, inner)
    draw.text(((PAGE - mast.getlength("THE WORLD IN ONE DAY")) / 2, 72),
              "THE WORLD IN ONE DAY", font=mast, fill=INK)
    double_rule(draw, 168, EDGE, PAGE - EDGE)

    # lead story
    y = 186
    y = kicker(draw, EDGE, y, "UKRAINE WAR")
    y = headline(draw, EDGE, y, inner,
                 "Russian strike hits kindergarten in Zaporizhzhia", size=46)
    y = paragraph(draw, EDGE, y + 2, inner,
                  "An attack early on Saturday sets fire to a flat in a "
                  "neighbouring five-storey block. One civilian was hurt, "
                  "the region's acting head said.", size=25)
    night_scene(draw, EDGE, y + 8, inner, 96)
    y = y + 8 + 96 + 16
    rule(draw, y, EDGE, PAGE - EDGE, 2)
    y += 16

    # four stories in two rows of two
    gap = 28
    cell_w = (inner - gap) // 2
    rows = [
        ("KILLER ROBOTS",
         "UN talks on autonomous weapons drag into Saturday",
         "Five days of Geneva talks overran Friday's deadline as states seek "
         "formal rules."),
        ("CLIMATE",
         "COP31 spills into the weekend as fossil-fuel row drags on",
         "The Antalya talks ran into overtime, deadlocked over a draft with "
         "no fossil-fuel mention."),
        ("AUSTRALIA",
         "NSW passes coal law in a 1.36am Saturday vote",
         "The Mount Pleasant mine may raise output from 12.5m to 16.5m "
         "tonnes a year until 2032."),
        ("AUSTRALIA",
         "Home-birth rallies in 25 towns as insurance deadline nears",
         "Midwives warn home-birth services could collapse when an exemption "
         "ends 31 December."),
    ]
    top = y
    story_cell(draw, EDGE, top, cell_w, *rows[0])
    story_cell(draw, EDGE + cell_w + gap, top, cell_w, *rows[1])
    second = top + 176
    story_cell(draw, EDGE, second, cell_w, *rows[2])
    story_cell(draw, EDGE + cell_w + gap, second, cell_w, *rows[3])
    y = second + 164 + 10
    rule(draw, y, EDGE, PAGE - EDGE, 2)
    y += 14

    # bottom strip: cricket + sourcing note
    y = kicker(draw, EDGE, y, "ALSO TODAY  —  CRICKET")
    y = paragraph(draw, EDGE, y, inner,
                  "India build on day three of the first Test in Wellington, "
                  "reaching 218 for 1 after New Zealand posted 368.",
                  size=23)
    foot = font(SANS_ITALIC, 20)
    note = "All stories verified from two or more sources."
    draw.text(((PAGE - foot.getlength(note)) / 2, y + 6), note,
              font=foot, fill=GREY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    sheet.save(os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    build()
