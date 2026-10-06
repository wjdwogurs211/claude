"""말풍선 화자 표. 컷 번호 -> 그 컷의 대사 말풍선(speech) 순서대로 화자 코드.

G=지피티, C=클로드, M=제미나이, K=그록, 3=셋(동시에), T=지피티·제미나이·그록 이름을 모두 표시
"""
NAMES = {"G": ("지피티", "#10A37F"), "C": ("클로드", "#C8643B"), "M": ("제미나이", "#4F6BED"),
         "K": ("그록", "#111111"), "3": ("셋", "#666666"),
         "T": ("지피티, 제미나이, 그록", "#666666")}

EP01 = {2: "GG", 3: "KGKC", 4: "M3M", 5: "K", 9: "KKKK", 10: "KMKM", 11: "CGM", 12: "GCMK", 14: "GCMK", 15: "G", 16: "G",
        17: "GG", 18: "KMC", 19: "KCKG", 20: "CC", 21: "CC", 22: "GM", 23: "K", 24: "CCG", 25: "MC", 26: "M",
        27: "M", 29: "KG", 30: "CMK", 31: "MK", 32: "GKGK", 33: "CGM", 35: "KK", 36: "KK", 38: "CT",
        39: "GKGK", 42: "MKCMG", 45: "MGKC", 47: "GKC", 48: "C", 50: "K"}

EP02 = {2: "MKM", 3: "MCM", 4: "MM", 7: "CM", 8: "GCMK", 10: "GM"}


def tag(bubbles, codes):
    """speech 말풍선에 순서대로 who 를 붙인 새 목록을 돌려준다."""
    it = iter(codes)
    out = []
    for b in bubbles:
        b = dict(b)
        if b["kind"] == "speech":
            b["who"] = next(it)
        out.append(b)
    assert next(it, None) is None, "화자 수가 말풍선 수보다 많음"
    return out
