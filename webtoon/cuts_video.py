"""1화를 네이버 컷츠용 세로 숏폼(9:16, 1080x1920, MP4)으로 만든다. 모션 코믹 방식.

- 컷 그림(표정 바꾼 버전, 꼬리 없는 말풍선)을 가운데 두고 뒤는 같은 그림을 흐리게 깔아 채운다.
- 말풍선·내레이션·공지는 원래 순서대로 하나씩 나타나고, 읽을 시간만큼 머문다.
- 컷마다 천천히 확대(켄 번스)하고, 컷 사이는 짧게 겹쳐 넘긴다.
- 컷츠는 2분 이내라서 편마다 컷 범위를 나눠 만든다.

사용법: python cuts_video.py 1        # 1편 (컷 1~12)
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

import build_ep01v2 as B
import compose_v2 as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "1화_완성본", "컷츠")
VW, VH, FPS = 1080, 1920, 30
# 편당 2분 이내가 되도록 자연스러운 읽기 속도로 나눴다 (1화 전체 약 10분)
PARTS = {1: (1, 9, "① 퇴근은 취소되었습니다")}
FADE = 0.35         # 컷 전환 겹침(초)
ZOOM = 0.04         # 컷 하나 동안 확대되는 정도
MAX_SEC = 118       # 컷츠 2분 제한 여유


def read_time(b):
    """말풍선 하나를 읽는 데 주는 시간(초). 한국어 초당 약 12자 + 기본 0.9초."""
    text = b.get("text", "")
    return 0.9 + len(text) / 12 if b["kind"] != "sfx" else 0.5


def panel_states(i):
    """컷 i 의 말풍선을 하나씩 늘려 가며 합성한 이미지 목록. 모든 상태의 높이를 같게(아래 기준) 맞춘다."""
    bubbles, opts = B.extended(i, B.ALL[i], B.PANEL_OPTS.get(i, {}))
    if B.USE_FACES:
        face = (opts.get("raw_name") or f"{i:02d}_raw.png").replace(".png", "_face.png")
        if os.path.exists(os.path.join(C.OUT, face)):
            opts = {**opts, "raw_name": face}
    bubbles = [{**b, "tail": None} if b["kind"] == "speech" else b for b in bubbles]
    full = C.compose_panel(i, bubbles, **opts)
    states = []
    # 효과음은 그림과 함께 바로 보이게 앞에 묶는다
    lead = [b for b in bubbles if b["kind"] == "sfx"]
    rest = [b for b in bubbles if b["kind"] != "sfx"]
    seq = [lead] + [lead + rest[:k] for k in range(1, len(rest) + 1)]
    for k, sub in enumerate(seq):
        img = C.compose_panel(i, sub, **opts) if sub else C.compose_panel(i, [], **opts)
        pad = Image.new("RGBA", full.size, (0, 0, 0, 0))  # 아직 안 나온 말풍선 자리는 투명(배경이 비침)
        pad.paste(img, (0, full.height - img.height))
        # 합성 결과의 위쪽 흰 여백(말풍선 없는 부분)도 투명하게
        arr = np.array(pad)
        top = full.height - img.height
        body = arr[top:]
        white = (body[..., :3].min(axis=2) > 250)
        rows = np.where(~white.all(axis=1))[0]
        first = rows[0] if len(rows) else 0
        body[:first][white[:first]] = (0, 0, 0, 0)
        pad = Image.fromarray(arr)
        hold = 1.6 if k == 0 else read_time(rest[k - 1])
        states.append((pad, hold))
    return states


def background(img):
    bg = img.resize((VW, VH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(40))
    return Image.blend(bg, Image.new("RGB", (VW, VH), (10, 10, 18)), 0.55)


def title_bar(canvas, text):
    d = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(C.FONT, 44)
    small = ImageFont.truetype(C.FONT, 30)
    d.text((60, 70), "인간을 찾아라", font=font, fill="white")
    d.text((60, 130), f"1화 {text}", font=small, fill=(220, 220, 230))


def frame(state_img, bg, t_frac, title):
    """세로 화면에 컷 하나를 놓는다. t_frac(0~1)에 따라 천천히 확대."""
    canvas = bg.copy()
    title_bar(canvas, title)
    s = 1.0 + ZOOM * t_frac
    w = int(VW * 0.96 * s)
    h = int(state_img.height * w / state_img.width)
    max_h = int(VH * 0.78)
    if h > max_h:  # 너무 긴 컷은 화면에 들어오게 줄인다
        w, h = int(w * max_h / h), max_h
    img = state_img.resize((w, h), Image.LANCZOS)
    x, y = (VW - w) // 2, 240 + (VH - 240 - h) // 2
    canvas.paste(img, (x, y), img)
    return canvas


def main(part):
    a, b, title = PARTS[part]
    ids = [i for i in range(a, b + 1) if i in B.ALL]
    plan = []  # (panel_states, bg)
    for i in ids:
        st = panel_states(i)
        plan.append((st, background(st[-1][0].convert("RGB"))))
    total = sum(sum(h for _, h in st) for st, _ in plan)
    speed = min(1.0, MAX_SEC / total)  # 2분을 넘으면 머무는 시간을 같은 비율로 줄인다
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"1화_{part}편.mp4")
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
         "-r", str(FPS), "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-shortest", "-movflags", "+faststart", path], stdin=subprocess.PIPE)
    prev_last = None
    n_frames = 0
    for st, bg in plan:
        dur = sum(h for _, h in st) * speed
        nf = max(1, int(dur * FPS))
        # 상태별 시작 프레임
        bounds, acc = [], 0
        for _, h in st:
            bounds.append(int(acc * speed * FPS))
            acc += h
        fade_n = int(FADE * FPS)
        for f in range(nf):
            k = max(j for j, s0 in enumerate(bounds) if s0 <= f)
            cur = np.asarray(frame(st[k][0], bg, f / nf, title), dtype=np.float32)
            if prev_last is not None and f < fade_n:  # 앞 컷 마지막 화면과 겹쳐 넘기기
                a_ = f / fade_n
                cur = cur * a_ + prev_last * (1 - a_)
            ff.stdin.write(cur.astype(np.uint8).tobytes())
            n_frames += 1
        prev_last = np.asarray(frame(st[-1][0], bg, 1.0, title), dtype=np.float32)
    ff.stdin.close()
    ff.wait()
    print(f"{path}  {n_frames / FPS:.1f}초, 컷 {len(ids)}개, 읽기 속도 배율 {speed:.2f}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
