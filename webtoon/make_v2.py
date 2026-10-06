"""「인간을 찾아라」 1화 그림 생성. 결과는 output/ep01v2/ 에 저장한다.

캐릭터 시트와 라운지 전경(컷 1)은 이전 1화 결과(output/ep01/urls.json)를 참조로 재사용한다.

사용법:
  KIE_API_KEY=... python make_v2.py              # 없는 컷만 생성
  KIE_API_KEY=... python make_v2.py --redo 3 7   # 지정 컷 다시 생성
"""
import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor

import kie_client
from ep01_panels import ALL_CHARS, STYLE
from v2_panels import PANELS as _A
from v2_panels_b import PANELS_B

PANELS = _A + PANELS_B

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01v2")
STATE = os.path.join(OUT, "urls.json")
OLD_STATE = os.path.join(HERE, "output", "ep01", "urls.json")
_lock = threading.Lock()


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    with open(OLD_STATE) as f:
        old = json.load(f)
    return {"sheet": old["sheet"], "lounge": old["panel1"]}


def save_state(state):
    with open(STATE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def run_group(panels, state, redo):
    prev = None
    for p in panels:
        key = f"panel{p['id']}"
        with _lock:
            done = key in state and p["id"] not in redo
        if done:
            prev = state[key]
            continue
        refs = [state["sheet"], prev or state["lounge"]]
        notes = ("Image 1 is the character reference sheet (left to right: GPT, Claude, Gemini, Grok). "
                 "Keep every character's exact head shape, head color, face logo and white stick-figure body. "
                 + ("Image 2 is the previous panel of the same scene; keep the same room, lighting and "
                    "character placement so it reads as one continuous scene." if prev else
                    "Image 2 shows the lounge; keep the same room design, furniture and lighting."))
        prompt = f"{STYLE}\n{notes}\nCharacters:\n{ALL_CHARS}\n\n{p['prompt']}"
        print(f"[컷 {p['id']}] 생성", flush=True)
        try:
            url = kie_client.generate(prompt, image_input=refs, aspect_ratio=p["ar"])
            kie_client.download(url, os.path.join(OUT, f"{p['id']:02d}_raw.png"))
        except Exception as e:  # 한 컷이 실패해도 나머지는 계속
            print(f"[컷 {p['id']}] 실패: {e}", flush=True)
            continue
        with _lock:
            state[key] = url
            save_state(state)
        prev = url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--redo", type=int, nargs="*", default=[])
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    state = load_state()
    save_state(state)
    groups = {}
    for p in PANELS:
        groups.setdefault(p["group"], []).append(p)
    with ThreadPoolExecutor(max_workers=len(groups)) as ex:
        for f in [ex.submit(run_group, g, state, set(args.redo)) for g in groups.values()]:
            f.result()
    print("완료:", sorted(int(k[5:]) for k in state if k.startswith("panel")))


if __name__ == "__main__":
    main()
