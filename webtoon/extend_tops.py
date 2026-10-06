"""말풍선이 컷 위로 많이 넘친 컷의 그림 위쪽을 AI로 늘린다.

1. 원본을 더 긴 캔버스의 아래쪽에 붙이고 위는 회색으로 비워 둔다.
2. kie.ai(Nano Banana 2)에 캔버스를 넣고 "회색 부분만 장면을 이어서 채워라"고 지시한다.
3. 결과 위에 원본 픽셀을 다시 덮어써서 캐릭터 위치가 1픽셀도 안 바뀌게 하고, 경계는 부드럽게 섞는다.
결과: output/ep01v2/NN_raw_ext.png, 늘린 비율은 ext.json 에 기록 (말풍선 좌표 변환용).
"""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import requests
from PIL import Image

import kie_client

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01v2")
EXT = os.path.join(OUT, "ext.json")
UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"
RATIOS = {"1:1": 1.0, "4:3": 4 / 3, "3:4": 3 / 4, "9:16": 9 / 16, "16:9": 16 / 9}

# 컷 -> 늘린 뒤의 비율
TARGETS = {2: "1:1", 3: "1:1", 4: "1:1", 9: "1:1", 11: "1:1", 15: "1:1", 16: "1:1", 20: "1:1", 22: "4:3",
           23: "9:16", 24: "1:1", 26: "1:1", 27: "1:1", 30: "1:1", 31: "1:1", 33: "3:4", 39: "1:1", 42: "1:1", 18: "1:1", 19: "1:1", 45: "9:16"}

PROMPT = ("The top part of this image is a flat grey placeholder. Fill ONLY that grey area with a natural continuation "
          "of the same scene upward (ceiling, upper parts of the server racks and walls, same lighting and drawing "
          "style). Keep the existing picture below exactly unchanged: same characters, poses, positions, colors. "
          "The new top area should be calm and fairly empty. No text, no letters, no speech bubbles.")


def upload(path, name):
    key = os.environ["KIE_API_KEY"]
    with open(path, "rb") as f:
        r = requests.post(UPLOAD, headers={"Authorization": f"Bearer {key}"},
                          files={"file": (name, f, "image/png")},
                          data={"uploadPath": "images/ep01v2-ext", "fileName": name}, timeout=120)
    url = r.json().get("data", {}).get("downloadUrl")
    if not url:
        raise RuntimeError(f"업로드 실패: {r.text[:200]}")
    return url


def crop_band(img):
    """AI가 '위쪽 여백' 지시를 글자 그대로 받아 그린 밝은 단색 띠가 있으면 잘라낸다.

    컷 테두리 같은 얇은 가로선(40px 미만)은 건너뛰고, 그보다 긴 그림 영역이 나오면 멈춘다.
    """
    from PIL import ImageStat
    W, H = img.size
    last_flat, y, noisy = -1, 0, 0
    while y < H // 2:
        st = ImageStat.Stat(img.crop((W // 10, y, W - W // 10, y + 4)))  # 컷 테두리 세로선은 빼고 가운데만
        if max(st.stddev) <= 10 and sum(st.mean) / 3 >= 150:
            last_flat, noisy = y, 0
        else:
            noisy += 4
            if noisy >= 40:
                break
        y += 4
    cut = last_flat + 4
    return img.crop((0, cut, W, H)) if cut > 20 else img


def extend(pid):
    raw = Image.open(os.path.join(OUT, f"{pid:02d}_raw.png")).convert("RGB")
    raw = crop_band(raw)
    W, H = raw.size
    NH = round(W / RATIOS[TARGETS[pid]])
    extra = NH - H
    canvas = Image.new("RGB", (W, NH), (128, 128, 128))
    canvas.paste(raw, (0, extra))
    cpath = os.path.join(OUT, f"{pid:02d}_ext_canvas.png")
    canvas.save(cpath)
    # 파일명이 겹치면 서버에서 덮어써지므로 컷마다 고유한 이름을 쓴다
    url = upload(cpath, f"ep01v2-ext-canvas-{pid:02d}.png")
    print(f"[컷 {pid}] 늘리는 중 (+{extra}px)", flush=True)
    out_url = kie_client.generate(PROMPT, image_input=[url], aspect_ratio=TARGETS[pid])
    gpath = os.path.join(OUT, f"{pid:02d}_ext_gen.png")
    kie_client.download(out_url, gpath)
    gen = Image.open(gpath).convert("RGB").resize((W, NH), Image.LANCZOS)
    # 원본을 다시 덮고, 경계 60px 는 위→아래로 섞어 이음매를 숨긴다
    feather = 60
    mask = Image.new("L", (W, H), 255)
    for y in range(feather):
        mask.paste(int(255 * y / feather), (0, y, W, y + 1))
    gen.paste(raw, (0, extra), mask)
    gen.save(os.path.join(OUT, f"{pid:02d}_raw_ext.png"))
    return pid, extra / H


def main(ids):
    ext = json.load(open(EXT)) if os.path.exists(EXT) else {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for pid, e in ex.map(extend, ids):
            ext[str(pid)] = round(e, 4)
            json.dump(ext, open(EXT, "w"), indent=1)
            print(f"[컷 {pid}] 완료 (위로 {e:.0%} 늘림)", flush=True)


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or sorted(TARGETS))
