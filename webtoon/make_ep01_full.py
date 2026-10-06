"""1화 전체(50컷) 생성 → 말풍선 합성 → 세로 스트립.

make_ep01.py 의 오프닝 4컷 결과(output/ep01/urls.json)를 이어 받는다.
같은 group 은 순서대로(직전 컷 참조), 서로 다른 group 은 병렬로 생성한다.

사용법:
  KIE_API_KEY=... python make_ep01_full.py               # 없는 컷만 생성 후 합성
  KIE_API_KEY=... python make_ep01_full.py --redo 3 4    # 지정 컷 다시 생성
  python make_ep01_full.py --compose-only
"""
import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor

from PIL import Image, ImageDraw, ImageFont

import kie_client
import make_ep01
from ep01_full import PANELS, TITLE
from ep01_panels import ALL_CHARS, STYLE

OUT = make_ep01.OUT
STATE = make_ep01.STATE
FONT = make_ep01.FONT
WIDTH = make_ep01.WIDTH
GUTTER = 60
make_ep01.SPEAKER_COLORS["사용자"] = "#2E8B57"

_lock = threading.Lock()


def build_prompt(p, ref_notes):
    parts = [STYLE]
    if ref_notes:
        parts.append(" ".join(ref_notes))
    if p["chars"]:
        parts.append("Characters:\n" + ALL_CHARS)
    parts.append(p["prompt"])
    return "\n".join(parts)


def run_group(panels, state, redo):
    prev = None  # (url, place)
    for p in panels:
        key = f"panel{p['id']}"
        with _lock:
            done = key in state and p["id"] not in redo
        if done:
            prev = (state[key], p["place"])
            continue

        refs, notes = [], []
        if p["chars"]:
            refs.append(state["sheet"])
            notes.append(f"Image {len(refs)} is the character reference sheet (left to right: GPT, Claude, "
                         "Gemini, Grok). Keep every character's exact head shape, head color, face logo "
                         "and white stick-figure body from it.")
        same_place_prev = p["use_prev"] and prev and prev[1] == p["place"]
        if p["place"] == "lounge" and not same_place_prev:
            refs.append(state["panel1"])
            notes.append(f"Image {len(refs)} shows the lounge; keep the same room design, furniture and lighting.")
        if same_place_prev:
            refs.append(prev[0])
            notes.append(f"Image {len(refs)} is the previous panel of the same scene; keep the same room, "
                         "lighting and character placement so it reads as one continuous scene.")

        print(f"[컷 {p['id']}] 생성 (참조 {len(refs)}장)", flush=True)
        try:
            url = kie_client.generate(build_prompt(p, notes), image_input=refs, aspect_ratio=p["aspect_ratio"])
            kie_client.download(url, os.path.join(OUT, f"{p['id']:02d}_raw.png"))
        except Exception as e:  # 한 컷 실패로 그룹 전체가 멈추지 않게 기록만 하고 다음 컷으로
            print(f"[컷 {p['id']}] 실패: {e}", flush=True)
            prev = None
            continue
        with _lock:
            state[key] = url
            make_ep01.save_state(state)
        prev = (url, p["place"])


def generate(redo):
    state = make_ep01.load_state()
    groups = {}
    for p in PANELS:
        groups.setdefault(p["group"], []).append(p)
    with ThreadPoolExecutor(max_workers=len(groups)) as ex:
        for f in [ex.submit(run_group, g, state, redo) for g in groups.values()]:
            f.result()


def wrap(text, font, max_w):
    """한글은 띄어쓰기 없이도 줄바꿈해야 해서 글자 단위로 자른다."""
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    out = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            if tmp.textlength(line + ch, font=font) > max_w and line:
                out.append(line)
                line = ch.lstrip()
            else:
                line += ch
        out.append(line)
    return "\n".join(out)


def compose():
    font = ImageFont.truetype(FONT, 28)
    max_text = WIDTH - 120 - 44
    blocks, missing = [], []
    for p in PANELS:
        raw_path = os.path.join(OUT, f"{p['id']:02d}_raw.png")
        if not os.path.exists(raw_path):
            missing.append(p["id"])
            continue
        raw = Image.open(raw_path).convert("RGB")
        raw = raw.resize((WIDTH, int(raw.height * WIDTH / raw.width)), Image.LANCZOS)
        bubbles = [make_ep01.draw_bubble(wrap(b["text"], font, max_text), b["who"], font, WIDTH - 120)
                   for b in p["bubbles"]]
        bubble_h = sum(b.height + 14 for b in bubbles)
        block = Image.new("RGB", (WIDTH, bubble_h + raw.height + GUTTER), "white")
        y = 0
        for i, b in enumerate(bubbles):
            x = (WIDTH - b.width) // 2 if len(bubbles) == 1 else (40 if i % 2 == 0 else WIDTH - b.width - 40)
            block.paste(b, (x, y), b)
            y += b.height + 14
        block.paste(raw, (0, bubble_h))
        ImageDraw.Draw(block).rectangle([0, bubble_h, WIDTH - 1, bubble_h + raw.height - 1], outline="black", width=4)
        block.save(os.path.join(OUT, f"{p['id']:02d}_panel.png"))
        blocks.append(block)

    title_font = ImageFont.truetype(FONT, 34)
    title = Image.new("RGB", (WIDTH, 160), "white")
    td = ImageDraw.Draw(title)
    td.text(((WIDTH - td.textlength(TITLE, font=title_font)) // 2, 60), TITLE, font=title_font, fill="black")

    strip = Image.new("RGB", (WIDTH, title.height + sum(b.height for b in blocks)), "white")
    y = 0
    for b in [title] + blocks:
        strip.paste(b, (0, y))
        y += b.height
    path = os.path.join(OUT, "ep01_full_strip.jpg")
    strip.save(path, quality=90)
    print(f"완성: {path} ({len(blocks)}컷, 높이 {strip.height}px)")
    if missing:
        print(f"빠진 컷: {missing}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--compose-only", action="store_true")
    ap.add_argument("--redo", type=int, nargs="*", default=[])
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    if not args.compose_only:
        generate(set(args.redo))
    compose()
