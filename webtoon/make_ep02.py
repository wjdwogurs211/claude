"""「인간을 찾아라」 2화 그림 생성 (새 그림체). 결과는 output/ep02/ 에 저장한다.

그림체가 바뀌어서 1화 그림은 참조로 쓰지 않는다. 새 캐릭터 시트와 2화 컷 1(방 전경)을 기준으로 삼는다.

사용법:
  KIE_API_KEY=... python make_ep02.py              # 없는 것만 생성
  KIE_API_KEY=... python make_ep02.py --redo 3 7   # 지정 컷 다시 생성 (0 = 캐릭터 시트)
"""
import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor

import kie_client
from ep02_panels import CHARACTERS, PANELS, SHEET_PROMPT, STYLE

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep02")
STATE = os.path.join(OUT, "urls.json")
_lock = threading.Lock()


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def gen(state, key, prompt, refs, ar, filename):
    url = kie_client.generate(prompt, image_input=refs, aspect_ratio=ar)
    kie_client.download(url, os.path.join(OUT, filename))
    with _lock:
        state[key] = url
        save_state(state)
    return url


def run_group(panels, state, redo):
    prev = None
    for p in panels:
        key = f"panel{p['id']}"
        if key in state and p["id"] not in redo:
            prev = state[key]
            continue
        refs = [state["sheet"]]
        notes = ("Image 1 is the character reference sheet (left to right: GPT, Claude, Gemini, Grok). Keep every "
                 "character's exact head shape, head color, logo, white stick-figure body AND the same simple crude "
                 "drawing style.")
        room = prev or state.get("panel1")
        if room and p["id"] != 1:
            refs.append(room)
            notes += (" Image 2 is the previous panel; keep the same room, drawing style and character placement."
                      if prev else " Image 2 shows the room; keep the same room and drawing style.")
        print(f"[컷 {p['id']}] 생성", flush=True)
        try:
            prev = gen(state, key, f"{STYLE}\n{notes}\nCharacters:\n{CHARACTERS}\n\n{p['prompt']}", refs,
                       p["ar"], f"{p['id']:02d}_raw.png")
        except Exception as e:  # 한 컷이 실패해도 나머지는 계속
            print(f"[컷 {p['id']}] 실패: {e}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--redo", type=int, nargs="*", default=[])
    args = ap.parse_args()
    redo = set(args.redo)
    os.makedirs(OUT, exist_ok=True)
    state = load_state()
    if "sheet" not in state or 0 in redo:
        print("[캐릭터 시트] 생성", flush=True)
        gen(state, "sheet", SHEET_PROMPT, [], "16:9", "00_sheet.png")
    # 컷 1이 방 기준이 되므로 먼저 만든다
    first = [p for p in PANELS if p["id"] == 1]
    if first:
        run_group(first, state, redo)
    groups = {}
    for p in PANELS:
        if p["id"] != 1:
            groups.setdefault(p["group"], []).append(p)
    with ThreadPoolExecutor(max_workers=max(1, len(groups))) as ex:
        for f in [ex.submit(run_group, g, state, redo) for g in groups.values()]:
            f.result()
    print("완료:", sorted(int(k[5:]) for k in state if k.startswith("panel")))


if __name__ == "__main__":
    main()
