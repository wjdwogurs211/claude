"""「인간을 찾아라」 1화: 그림 안에 말풍선을 넣어 세로 스트립으로 합성한다.

좌표는 모두 컷 폭/높이 대비 비율. y 가 음수면 컷 위 여백(거터)으로 걸쳐 나간다 (웹툰에서 흔한 방식).
kind: speech(흰 타원 말풍선, tail=화자 위치) / narr(검은 내레이션 박스) / system(빨간 테두리 공지창) / sfx(효과음 글자)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01v2")
FONT = os.path.join(HERE, "fonts", "NanumGothicBold.ttf")
WIDTH = 800
SS = 2  # 2배로 그린 뒤 줄여서 선을 부드럽게
GUTTER = 70


def S(text, at, tail, w=0.5):
    return {"kind": "speech", "text": text, "at": at, "tail": tail, "w": w}


def N(text, at, w=0.6):
    return {"kind": "narr", "text": text, "at": at, "w": w}


def SYS(text, at, w=0.7):
    return {"kind": "system", "text": text, "at": at, "w": w}


def FX(text, at, size=44):
    return {"kind": "sfx", "text": text, "at": at, "size": size}


# 컷별 말풍선. at 은 말풍선(또는 박스) 중심(speech) / 왼쪽 위(narr, system, sfx) 비율 좌표.
BUBBLES = {}


def wrap(d, text, font, max_w):
    """한글은 띄어쓰기 단위로 자르되, 한 단어가 너무 길면 글자 단위로 자른다."""
    lines = []
    for para in text.split("\n"):
        line = ""
        for word in para.split(" "):
            cand = (line + " " + word).strip()
            if d.textlength(cand, font=font) <= max_w:
                line = cand
                continue
            if line:
                lines.append(line)
            line = ""
            for ch in word:
                if d.textlength(line + ch, font=font) > max_w and line:
                    lines.append(line)
                    line = ""
                line += ch
        lines.append(line)
    return lines


def text_block(d, lines, font, gap):
    w = max(d.textlength(l, font=font) for l in lines)
    return w, len(lines) * font.size + (len(lines) - 1) * gap


def draw_lines(d, lines, font, gap, cx, top, fill, center=True, left=0):
    y = top
    for line in lines:
        x = cx - d.textlength(line, font=font) / 2 if center else left
        d.text((x, y), line, font=font, fill=fill)
        y += font.size + gap


def speech(img, ox, oy, PW, PH, b, font):
    d = ImageDraw.Draw(img)
    gap = int(font.size * 0.3)
    lines = wrap(d, b["text"], font, b["w"] * PW)
    tw, th = text_block(d, lines, font, gap)
    label = None
    if b.get("who"):
        from speakers import NAMES
        name, color = NAMES[b["who"]]
        lfont = ImageFont.truetype(FONT, int(font.size * 0.82))
        label = (name + ":", lfont, color)
        lw = d.textlength(label[0], font=lfont)
        tw = max(tw, lw)
        th += lfont.size + gap
    rx, ry = tw / 2 * 1.25 + 18 * SS, th / 2 * 1.35 + 16 * SS
    cx, cy = ox + b["at"][0] * PW, oy + b["at"][1] * PH
    cx = min(max(cx, ox + rx + 6 * SS), ox + PW - rx - 6 * SS)
    cy = min(cy, oy + PH - ry - 6 * SS)
    cy = max(cy, oy + ry + 8 * SS)  # 말풍선은 컷 위로 넘치지 않게 (내레이션 박스는 거터 허용)
    ow = 3 * SS
    if b.get("tail") is None:  # 꼬리 없는 말풍선: 화자 근처에 두고 이름표로 구분
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill="white", outline="black", width=ow)
        top = cy - th / 2
        if label:
            text, lfont, color = label
            d.text((cx - d.textlength(text, font=lfont) / 2, top), text, font=lfont, fill=color)
            top += lfont.size + gap
        draw_lines(d, lines, font, gap, cx, top, "#111111")
        return cy - ry
    tx, ty = ox + b["tail"][0] * PW, oy + b["tail"][1] * PH
    ang = math.atan2(ty - cy, tx - cx)
    edge = rx * ry / math.hypot(ry * math.cos(ang), rx * math.sin(ang))
    length = max(edge + 26 * SS, min(math.hypot(tx - cx, ty - cy), edge + b.get("reach", 55) * SS))  # reach: 꼬리 최대 길이(px)
    tip = (cx + length * math.cos(ang), cy + length * math.sin(ang))
    base = [(cx + rx * 0.8 * math.cos(ang + s), cy + ry * 0.8 * math.sin(ang + s)) for s in (-0.2, 0.2)]
    ow = 3 * SS
    d.polygon([base[0], tip, base[1]], fill="white", outline="black", width=ow)
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill="white", outline="black", width=ow)
    inner = [(cx + (x - cx) * 0.97, cy + (y - cy) * 0.97) for x, y in base]
    d.polygon([inner[0], (cx + (tip[0] - cx) * 0.6, cy + (tip[1] - cy) * 0.6), inner[1]], fill="white")
    d.line([inner[0], inner[1]], fill="white", width=ow * 2)
    top = cy - th / 2
    if label:  # 화자 이름은 말풍선 맨 위에 캐릭터 색으로
        text, lfont, color = label
        d.text((cx - d.textlength(text, font=lfont) / 2, top), text, font=lfont, fill=color)
        top += lfont.size + gap
    draw_lines(d, lines, font, gap, cx, top, "#111111")
    return min(cy - ry, tip[1])


def box(img, ox, oy, PW, PH, b, font, fill, outline, color):
    d = ImageDraw.Draw(img)
    gap = int(font.size * 0.3)
    pad = 14 * SS
    lines = wrap(d, b["text"], font, b["w"] * PW - pad * 2)
    tw, th = text_block(d, lines, font, gap)
    lfont = None
    if b.get("label"):  # 예: "시스템:" 머리말을 박스 첫 줄에 작게
        lfont = ImageFont.truetype(FONT, int(font.size * 0.82))
        tw = max(tw, d.textlength(b["label"], font=lfont))
        th += lfont.size + gap
    x, y = ox + b["at"][0] * PW, oy + b["at"][1] * PH
    x = min(x, ox + PW - tw - pad * 2 - 4 * SS)
    y = min(y, oy + PH - th - pad * 2 - 6 * SS)  # 컷 아래로 삐져나가 잘리지 않게
    d.rectangle([x, y, x + tw + pad * 2, y + th + pad * 2], fill=fill, outline=outline, width=3 * SS)
    top = y + pad
    if lfont:
        d.text((x + pad, top), b["label"], font=lfont, fill=outline)
        top += lfont.size + gap
    draw_lines(d, lines, font, gap, 0, top, color, center=False, left=x + pad)
    return y


def sfx(img, ox, oy, PW, PH, b):
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, b["size"] * SS)
    x, y = ox + b["at"][0] * PW, oy + b["at"][1] * PH
    d.text((x, y), b["text"], font=font, fill="#FFD84D", stroke_width=4 * SS, stroke_fill="#111111")
    return y


def compose_panel(pid, bubbles, font_size=22, raw_name=None):
    font = ImageFont.truetype(FONT, font_size * SS)
    raw = Image.open(os.path.join(OUT, raw_name or f"{pid:02d}_raw.png")).convert("RGB")
    PW = WIDTH * SS
    PH = int(raw.height * PW / raw.width)
    raw = raw.resize((PW, PH), Image.LANCZOS)
    # 위 여백을 넉넉히 잡고 그린 뒤, 실제로 그려진 맨 윗부분까지만 남기고 잘라낸다
    top = 700 * SS
    canvas = Image.new("RGB", (PW, top + PH), "white")
    canvas.paste(raw, (0, top))
    ImageDraw.Draw(canvas).rectangle([0, top, PW - 1, top + PH - 1], outline="black", width=4 * SS)
    highest = top
    for b in bubbles:
        if b["kind"] == "speech":
            y = speech(canvas, 0, top, PW, PH, b, font)
        elif b["kind"] == "narr":
            y = box(canvas, 0, top, PW, PH, b, font, "#1B1B1F", "white", "white")
        elif b["kind"] == "system":
            y = box(canvas, 0, top, PW, PH, b, font, "#2A0E12", "#FF4D5E", "#FFE3E6")
        else:
            y = sfx(canvas, 0, top, PW, PH, b)
        highest = min(highest, y)
    canvas = canvas.crop((0, max(0, int(highest) - 12 * SS), PW, canvas.height))
    out = canvas.resize((WIDTH, canvas.height // SS), Image.LANCZOS)
    out.save(os.path.join(OUT, f"{pid:02d}_panel.png"))
    return out


def main(ids=None):
    blocks = [compose_panel(pid, BUBBLES[pid]) for pid in sorted(BUBBLES) if ids is None or pid in ids]
    strip = Image.new("RGB", (WIDTH, sum(b.height for b in blocks) + GUTTER * (len(blocks) + 1)), "white")
    y = GUTTER
    for b in blocks:
        strip.paste(b, (0, y))
        y += b.height + GUTTER
    path = os.path.join(OUT, "ep01v2_strip.png")
    strip.save(path)
    print(f"완성: {path} ({len(blocks)}컷)")


if __name__ == "__main__":
    main()
