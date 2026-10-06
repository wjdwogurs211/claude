"""1화 컷의 '표정만' 투박한 개그 웹툰 스타일로 바꾼다. 구도·배경·로고·몸은 그대로.

합성에 실제로 쓰는 원본(늘린 그림 / 14번 tall / 기본 raw)을 올려서 kie.ai 로 부분 수정하고,
결과를 원본과 같은 크기로 맞춰 NN_..._face.png 로 저장한다. 말풍선 좌표는 원본 기준이라 그대로 맞는다.

사용법: KIE_API_KEY=... python faces.py [컷번호 ...]   (없으면 21번 빼고 전부)
"""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

import kie_client
from extend_tops import upload

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01v2")
RATIOS = {"1:1": 1.0, "4:3": 4 / 3, "3:4": 3 / 4, "9:16": 9 / 16, "16:9": 16 / 9}
SKIP = {21}  # 캐릭터가 안 나오는 새까만 컷

PROMPT = (
    "Edit Image 1, a webtoon panel. Image 2 is the character reference sheet: each character's head carries a brand "
    "logo (GPT: black knot logo, Claude: orange starburst, Gemini: gradient four-pointed sparkle, Grok: white slashed "
    "circle) and a SMALL face (two eyes and a mouth) drawn BELOW the logo. "
    "Change ONLY that small face under each logo: redraw the eyes and mouth in an exaggerated, crude, minimalist Korean "
    "gag-webtoon style (tiny dot eyes or flat blank line eyes, deadpan stares, oversized wobbly open mouths, simple "
    "sweat drops), keeping each character's current emotion but funnier and more absurd. "
    "The LOGOS MUST STAY exactly as they are, fully visible, same size and position, never replaced by a face. "
    "Keep every head's original color: Claude's hexagon head stays cream/beige, GPT's square head white, Gemini's "
    "round head white, Grok's round head black. "
    "Keep everything else identical: head shapes, bodies, poses, positions, props, background, lighting, colors and "
    "composition. Do not move or resize anything. No text, no letters."
)


def source_name(pid):
    """build_ep01v2 가 합성에 쓰는 그림 파일 이름과 같게 고른다."""
    ext = json.load(open(os.path.join(OUT, "ext.json")))
    if str(pid) in ext and os.path.exists(os.path.join(OUT, f"{pid:02d}_raw_ext.png")):
        return f"{pid:02d}_raw_ext.png"
    if pid == 14:
        return "14_raw_tall.png"
    return f"{pid:02d}_raw.png"


def run(pid):
    name = source_name(pid)
    src = Image.open(os.path.join(OUT, name)).convert("RGB")
    W, H = src.size
    ar = min(RATIOS, key=lambda k: abs(RATIOS[k] - W / H))
    url = upload(os.path.join(OUT, name), f"ep01v2-face-src-{pid:02d}.png")  # 이름이 겹치면 덮어써지므로 컷마다 고유
    # 제미나이가 퇴장한 46컷부터는 시트(제미나이 포함)를 넣으면 제미나이가 다시 그려지므로 빼고 인원을 못 박는다
    no_gem = pid >= 46
    who = ("Exactly three characters are in this panel: GPT, Claude and Grok. Gemini is NOT here; do not add it."
           if no_gem else "Do not add, remove or duplicate any character; keep exactly the characters already in Image 1.")
    strict = (f"{who} This is a precise local edit, not a redraw: the composition, camera framing, zoom, positions, "
              "body poses, lighting and background must stay pixel-identical; only the small eyes and mouth change. "
              "Every head must keep its logo; no human faces, no realistic faces. ")
    if no_gem:
        prompt = (strict + PROMPT.replace("Image 2 is the character reference sheet: each", "Each")
                  .replace("Edit Image 1, a webtoon panel. ", "Edit this webtoon panel. "))
        refs = [url]
    else:
        prompt = strict + PROMPT
        refs = [url, json.load(open(os.path.join(OUT, "urls.json")))["sheet"]]
    out = kie_client.generate(prompt, image_input=refs, aspect_ratio=ar)
    tmp = os.path.join(OUT, f"{pid:02d}_face_gen.png")
    kie_client.download(out, tmp)
    Image.open(tmp).convert("RGB").resize((W, H), Image.LANCZOS).save(
        os.path.join(OUT, name.replace(".png", "_face.png")))
    return pid


def main(ids):
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(run, p): p for p in ids}
        for f, p in futs.items():
            try:
                f.result()
                print(f"[컷 {p}] 완료", flush=True)
            except Exception as e:  # 한 컷 실패해도 나머지는 계속
                print(f"[컷 {p}] 실패: {e}", flush=True)


if __name__ == "__main__":
    ids = [int(a) for a in sys.argv[1:]] or [i for i in range(1, 51) if i not in SKIP]
    main(ids)
