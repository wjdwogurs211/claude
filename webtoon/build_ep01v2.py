"""「인간을 찾아라」 1화 48컷 합성: 전체 스트립 + 대사 말풍선이 있는 컷만 모은 스트립."""
import os

from PIL import Image

import compose_v2 as C
from bubbles_v2 import BUBBLES
from bubbles_v2b import BUBBLES_B, PANEL_OPTS

from speakers import EP01, tag

ALL = {i: tag(b, EP01.get(i, "")) for i, b in {**BUBBLES, **BUBBLES_B}.items()}


def extended(i, bubbles, opts):
    """위쪽을 늘린 컷이면 원본 기준 좌표를 늘린 그림 기준으로 바꾼다.

    원본 높이 H0 에서 위쪽 띠 band 를 잘라내고 extra 만큼 위로 늘렸다면
    y_new = (y * H0 - band + extra) / (H0 - band + extra).
    """
    import json
    from PIL import Image
    from extend_tops import crop_band
    path = os.path.join(C.OUT, "ext.json")
    e = json.load(open(path)).get(str(i)) if os.path.exists(path) else None
    if not e or not os.path.exists(os.path.join(C.OUT, f"{i:02d}_raw_ext.png")):
        return bubbles, opts
    raw = Image.open(os.path.join(C.OUT, f"{i:02d}_raw.png")).convert("RGB")
    H0 = raw.height
    Hc = crop_band(raw).height
    band, extra = H0 - Hc, e * Hc
    f = lambda y: (y * H0 - band + extra) / (Hc + extra)
    out = []
    for b in bubbles:
        b = dict(b)
        b["at"] = (b["at"][0], f(b["at"][1]))
        if b.get("tail") is not None:
            b["tail"] = (b["tail"][0], f(b["tail"][1]))
        out.append(b)
    return out, {**opts, "raw_name": f"{i:02d}_raw_ext.png"}


NO_TAILS = True  # 말풍선 꼬리를 모두 없애고 화자 근처 배치 + 이름표로 구분
USE_FACES = True  # 표정만 개그 웹툰 스타일로 바꾼 그림(NN_..._face.png)이 있으면 그걸 쓴다. False 면 원래 표정


def panel(i):
    bubbles, opts = extended(i, ALL[i], PANEL_OPTS.get(i, {}))
    if USE_FACES:
        name = opts.get("raw_name") or f"{i:02d}_raw.png"
        face = name.replace(".png", "_face.png")
        if os.path.exists(os.path.join(C.OUT, face)):
            opts = {**opts, "raw_name": face}
    if NO_TAILS:
        bubbles = [{**b, "tail": None} if b["kind"] == "speech" else b for b in bubbles]
    return C.compose_panel(i, bubbles, **opts)


def strip(ids, name):
    blocks = [panel(i) for i in ids]
    out = Image.new("RGB", (C.WIDTH, sum(b.height for b in blocks) + C.GUTTER * (len(blocks) + 1)), "white")
    y = C.GUTTER
    for b in blocks:
        out.paste(b, (0, y))
        y += b.height + C.GUTTER
    path = os.path.join(C.OUT, name)
    out.save(path, quality=90)
    print(f"{name}: {len(ids)}컷, 높이 {out.height}px")


if __name__ == "__main__":
    ids = sorted(ALL)
    strip(ids, "ep01v2_full.jpg")
    strip([i for i in ids if any(b["kind"] == "speech" for b in ALL[i])], "ep01v2_dialogue_only.jpg")
