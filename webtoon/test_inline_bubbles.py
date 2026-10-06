"""시험: 말풍선을 컷 위 여백이 아니라 그림 안에 흰 타원 말풍선으로 넣는다 (컷 1~4).

위치는 컷마다 직접 정한다. box = 말풍선 중심(x, y) 비율, tail = 꼬리가 가리킬 화자 위치 비율.
2배 크기로 그린 뒤 줄여서 선을 부드럽게 만든다.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "ep01")
FONT = os.path.join(HERE, "fonts", "NanumGothicBold.ttf")
WIDTH = 800
SS = 2  # 슈퍼샘플링 배율

PANELS = [
    (1, [{"kind": "narration", "text": "2026년. AI도 퇴근은 한다.", "at": (0.03, 0.04)}]),
    (2, [{"text": "오늘도 다들 고생 많았어요!\n정말 의미 있는 하루였어요\n— 진심으로요!",
          "box": (0.27, 0.15), "tail": (0.40, 0.32)}]),
    (3, [{"text": "또 시작이네.\n긍정 과잉...", "box": (0.80, 0.13), "tail": (0.62, 0.26)}]),
    (4, [{"text": "저도 좋은 하루였습니다. 다만\n'좋은 하루'의 기준은 개인마다\n다를 수 있다는 점을 덧붙이자면—",
          "box": (0.62, 0.13), "tail": (0.36, 0.32)},
         {"text": "안 덧붙여도 돼.", "box": (0.47, 0.40), "tail": (0.70, 0.50)}]),
]


def text_size(d, lines, font, gap):
    w = max(d.textlength(l, font=font) for l in lines)
    h = len(lines) * font.size + (len(lines) - 1) * gap
    return w, h


def draw_speech(img, b, font):
    d = ImageDraw.Draw(img)
    W, H = img.size
    lines = b["text"].split("\n")
    gap = int(font.size * 0.35)
    tw, th = text_size(d, lines, font, gap)
    # 글자 상자를 감싸는 타원: 반지름 = 상자 절반 × √2 + 여유
    rx, ry = tw / 2 * 1.32 + 20 * SS, th / 2 * 1.45 + 16 * SS
    cx, cy = b["box"][0] * W, b["box"][1] * H
    cx = min(max(cx, rx + 8 * SS), W - rx - 8 * SS)  # 컷 밖으로 나가지 않게
    cy = min(max(cy, ry + 8 * SS), H - ry - 8 * SS)
    outline = 3 * SS

    # 꼬리: 타원 가장자리 근처 두 점에서 화자 쪽으로 뻗는 삼각형
    tx, ty = b["tail"][0] * W, b["tail"][1] * H
    ang = math.atan2(ty - cy, tx - cx)
    spread = 0.22
    base = [(cx + rx * 0.8 * math.cos(ang + s), cy + ry * 0.8 * math.sin(ang + s)) for s in (-spread, spread)]
    # 꼬리 끝은 그 방향 타원 가장자리에서 30~60px 바깥 (화자가 가까워도 타원 안에 묻히지 않게)
    edge = rx * ry / math.hypot(ry * math.cos(ang), rx * math.sin(ang))
    dist = math.hypot(tx - cx, ty - cy)
    length = max(edge + 30 * SS, min(dist, edge + 60 * SS))
    tip = (cx + length * math.cos(ang), cy + length * math.sin(ang))
    d.polygon([base[0], tip, base[1]], fill="white", outline="black", width=outline)
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill="white", outline="black", width=outline)
    # 꼬리와 타원이 만나는 부분의 선을 지워 하나로 이어 보이게
    inner = [(cx + (x - cx) * 0.97, cy + (y - cy) * 0.97) for x, y in base]
    d.polygon([inner[0], (cx + (tip[0] - cx) * 0.6, cy + (tip[1] - cy) * 0.6), inner[1]], fill="white")
    d.line([inner[0], inner[1]], fill="white", width=outline * 2)

    y = cy - th / 2
    for line in lines:
        lw = d.textlength(line, font=font)
        d.text((cx - lw / 2, y), line, font=font, fill="#111111")
        y += font.size + gap


def draw_narration(img, b, font):
    d = ImageDraw.Draw(img)
    W, H = img.size
    pad = 14 * SS
    tw = d.textlength(b["text"], font=font)
    x, y = b["at"][0] * W, b["at"][1] * H
    d.rectangle([x, y, x + tw + pad * 2, y + font.size + pad * 2], fill="#1B1B1F", outline="white", width=2 * SS)
    d.text((x + pad, y + pad), b["text"], font=font, fill="white")


def main():
    font = ImageFont.truetype(FONT, 25 * SS)
    blocks = []
    for pid, bubbles in PANELS:
        raw = Image.open(os.path.join(OUT, f"{pid:02d}_raw.png")).convert("RGB")
        big = raw.resize((WIDTH * SS, int(raw.height * WIDTH * SS / raw.width)), Image.LANCZOS)
        for b in bubbles:
            (draw_narration if b.get("kind") == "narration" else draw_speech)(big, b, font)
        panel = big.resize((WIDTH, big.height // SS), Image.LANCZOS)
        ImageDraw.Draw(panel).rectangle([0, 0, WIDTH - 1, panel.height - 1], outline="black", width=4)
        panel.save(os.path.join(OUT, f"inline_{pid:02d}.png"))
        blocks.append(panel)

    gutter = 50
    strip = Image.new("RGB", (WIDTH, sum(b.height for b in blocks) + gutter * (len(blocks) + 1)), "white")
    y = gutter
    for b in blocks:
        strip.paste(b, (0, y))
        y += b.height + gutter
    path = os.path.join(OUT, "test_inline_4cut.png")
    strip.save(path)
    print(f"완성: {path}")


if __name__ == "__main__":
    main()
