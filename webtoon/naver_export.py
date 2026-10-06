"""1화 전체 스트립을 네이버 웹툰 업로드 규격으로 자른다.

규격(toonslicer.com 정리 기준): 가로 690px, 한 장 세로 최대 1280px, JPG, 장당 5MB / 한 화 50MB 이하, RGB.
자르는 위치는 가능하면 컷 사이 흰 여백 줄에서 고른다. 독자는 이어서 스크롤하므로 컷 안에서 잘려도 이음매는 안 보인다.
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "output", "1화_완성본", "1화_전체_50컷.jpg")
OUT = os.path.join(HERE, "output", "1화_완성본", "네이버업로드")
W, MAX_H, MIN_H = 690, 1280, 600


def main():
    im = Image.open(SRC).convert("RGB")
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    a = np.asarray(im)
    white = (a.min(axis=2) > 245).all(axis=1)  # 줄 전체가 흰색인 행 = 컷 사이 여백
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    y, n, total = 0, 0, 0
    while y < im.height:
        end = min(y + MAX_H, im.height)
        if end < im.height:
            cand = np.where(white[y + MIN_H:end])[0]
            if len(cand):
                end = y + MIN_H + cand[-1]
        n += 1
        path = os.path.join(OUT, f"{n:03d}.jpg")
        q = 92
        while True:
            im.crop((0, y, W, end)).save(path, quality=q, optimize=True)
            if os.path.getsize(path) <= 5 * 1024 * 1024 or q <= 60:
                break
            q -= 5
        total += os.path.getsize(path)
        y = end
    print(f"{n}장, 총 {total / 1024 / 1024:.1f}MB, 장당 최대 {max(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)) / 1024:.0f}KB")


if __name__ == "__main__":
    main()
