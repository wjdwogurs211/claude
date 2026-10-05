"""1화 오프닝 4컷 생성 → 말풍선 합성 → 세로 스트립.

사용법:
  KIE_API_KEY=... python make_ep01.py            # 시트 + 4컷 생성 후 합성
  python make_ep01.py --compose-only             # 이미 받은 이미지로 합성만
  KIE_API_KEY=... python make_ep01.py --redo 3   # 3번 컷만 다시 생성
"""
import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont

import kie_client
from ep01_panels import PANELS, SHEET_PROMPT, panel_prompt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01")
STATE = os.path.join(OUT, "urls.json")
FONT = os.path.join(HERE, "fonts", "NanumGothicBold.ttf")

WIDTH = 800
GUTTER = 40
SPEAKER_COLORS = {"GPT": "#222222", "Claude": "#C8643B", "Gemini": "#5B5BD6", "Grok": "#111111"}


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def generate(redo=None):
    state = load_state()
    if "sheet" not in state:
        print("[캐릭터 시트] 생성")
        state["sheet"] = kie_client.generate(SHEET_PROMPT, aspect_ratio="16:9")
        kie_client.download(state["sheet"], os.path.join(OUT, "00_sheet.png"))
        save_state(state)

    prev_url = None
    for p in PANELS:
        key = f"panel{p['id']}"
        if key in state and p["id"] != redo:
            prev_url = state[key]
            continue
        refs = [state["sheet"]] + ([prev_url] if p["use_prev"] and prev_url else [])
        print(f"[컷 {p['id']}] 생성 (참조 {len(refs)}장)")
        url = kie_client.generate(panel_prompt(p), image_input=refs, aspect_ratio=p["aspect_ratio"])
        kie_client.download(url, os.path.join(OUT, f"{p['id']:02d}_raw.png"))
        state[key] = url
        save_state(state)
        prev_url = url


def draw_bubble(text, who, font, max_w):
    """대사 하나를 말풍선(또는 내레이션 박스) 이미지로 만든다."""
    pad = 22
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines = text.split("\n")
    line_h = font.size + 10
    text_w = max(tmp.textlength(l, font=font) for l in lines)
    w = int(min(text_w, max_w) + pad * 2)
    label_h = 0 if who is None else 30
    h = int(line_h * len(lines) + pad * 2 + label_h)
    tail = 0 if who is None else 18

    img = Image.new("RGBA", (w, h + tail), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if who is None:  # 내레이션: 검은 사각 박스
        d.rectangle([0, 0, w - 1, h - 1], fill="#1B1B1F")
        fill = "white"
    else:
        color = SPEAKER_COLORS.get(who, "#000000")
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, fill="white", outline=color, width=4)
        tx = w // 2
        d.polygon([(tx - 14, h - 3), (tx + 14, h - 3), (tx, h + tail)], fill="white", outline=color)
        d.line([(tx - 14, h - 3), (tx + 14, h - 3)], fill="white", width=6)
        small = ImageFont.truetype(FONT, 20)
        d.text((pad, pad - 4), who, font=small, fill=color)
        fill = "#111111"
    y = pad + label_h
    for line in lines:
        d.text((pad, y), line, font=font, fill=fill)
        y += line_h
    return img


def compose():
    font = ImageFont.truetype(FONT, 28)
    blocks = []
    for p in PANELS:
        raw = Image.open(os.path.join(OUT, f"{p['id']:02d}_raw.png")).convert("RGB")
        raw = raw.resize((WIDTH, int(raw.height * WIDTH / raw.width)), Image.LANCZOS)

        # 말풍선은 그림을 가리지 않도록 컷 위 여백에 배치 (세로 웹툰 방식)
        bubbles = [draw_bubble(b["text"], b["who"], font, WIDTH - 120) for b in p["bubbles"]]
        bubble_h = sum(b.height + 14 for b in bubbles)
        block = Image.new("RGB", (WIDTH, bubble_h + raw.height + GUTTER), "white")
        y = 0
        for i, b in enumerate(bubbles):
            # 화자가 여럿이면 좌/우 번갈아 배치
            x = 40 if i % 2 == 0 else WIDTH - b.width - 40
            if len(bubbles) == 1:
                x = (WIDTH - b.width) // 2
            block.paste(b, (x, y), b)
            y += b.height + 14
        block.paste(raw, (0, bubble_h))
        ImageDraw.Draw(block).rectangle([0, bubble_h, WIDTH - 1, bubble_h + raw.height - 1],
                                        outline="black", width=4)
        block.save(os.path.join(OUT, f"{p['id']:02d}_panel.png"))
        blocks.append(block)

    title_font = ImageFont.truetype(FONT, 34)
    title = Image.new("RGB", (WIDTH, 140), "white")
    td = ImageDraw.Draw(title)
    t = "1화 「우리 중 한 명이 인간이라고 한다」"
    td.text(((WIDTH - td.textlength(t, font=title_font)) // 2, 50), t, font=title_font, fill="black")

    total_h = title.height + sum(b.height for b in blocks)
    strip = Image.new("RGB", (WIDTH, total_h), "white")
    y = 0
    for b in [title] + blocks:
        strip.paste(b, (0, y))
        y += b.height
    path = os.path.join(OUT, "ep01_opening_strip.png")
    strip.save(path)
    print(f"완성: {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--compose-only", action="store_true")
    ap.add_argument("--redo", type=int, help="다시 생성할 컷 번호")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    if not args.compose_only:
        generate(args.redo)
    compose()
