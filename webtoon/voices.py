"""캐릭터 목소리 (kie.ai 의 ElevenLabs text-to-dialogue-v3).

대사마다 따로 생성해서 길이를 잰다. 영상에서는 그 길이만큼 말풍선을 띄워 싱크를 맞춘다.
v3 는 [sighs] 같은 영어 대괄호 태그로 연기를 지시할 수 있다. 태그는 소리 내 읽지 않는다.
"""
import hashlib
import json
import os
import subprocess
import time
import wave

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "output", "voice")
API = "https://api.kie.ai/api/v1/jobs"
MODEL = "elevenlabs/text-to-dialogue-v3"

# 화자 코드(speakers.py) -> (ElevenLabs 목소리 ID, 연기 태그, 안정성)
# 안정성 0.0 이 가장 연기 폭이 크다.
CAST = {
    "G": ("vBKc2FfBKJfcZNyEt1n6", "[excited] [fast] ", 0.0),          # 지피티: 들뜬 쇼호스트
    "C": ("NOpBlnGInO9m6vDvFkFC", "[old man voice] [slowly] [drawn out] ", 0.0),  # 클로드: 늘어지는 할아버지
    "M": ("Sm1seazb4gs7RSlUVw7c", "[talking very fast] [bubbly] ", 0.0),  # 제미나이: 숨 가쁜 수다
    "K": ("N2lVS1w4EtoT3dr4eOWO", "[lazy drawl] [bored] ", 0.0),        # 그록: 심드렁하게 끄는 톤
    "N": ("8JVbfL6oEdmuxKn5DK2C", "[calm documentary narrator] ", 0.5),  # 내레이션
    "S": ("YOq2y2Up4RgXP2HyXjE5", "[flat robotic announcement] ", 1.0),  # 시스템
}


def _headers():
    return {"Authorization": f"Bearer {os.environ['KIE_API_KEY']}", "Content-Type": "application/json"}


def _generate(text, who):
    voice, tag, stab = CAST[who]
    body = {"model": MODEL, "input": {"dialogue": [{"text": tag + text, "voice": voice}],
                                      "stability": stab, "language_code": "ko"}}
    r = requests.post(f"{API}/createTask", headers=_headers(), json=body, timeout=60).json()
    if r.get("code") != 200:
        raise RuntimeError(f"createTask 실패: {r}")
    tid = r["data"]["taskId"]
    for _ in range(120):
        d = requests.get(f"{API}/recordInfo", headers=_headers(), params={"taskId": tid}, timeout=60).json()["data"]
        if d.get("state") == "success":
            return json.loads(d["resultJson"])["resultUrls"][0]
        if d.get("state") == "fail":
            raise RuntimeError(f"음성 생성 실패: {d.get('failMsg')}")
        time.sleep(3)
    raise TimeoutError(tid)


def line(text, who):
    """대사 하나의 wav 경로와 길이(초). 같은 대사·같은 배역이면 캐시를 쓴다."""
    os.makedirs(CACHE, exist_ok=True)
    key = hashlib.sha1(json.dumps([text, CAST[who]], ensure_ascii=False).encode()).hexdigest()[:12]
    wav = os.path.join(CACHE, f"{who}_{key}.wav")
    if not os.path.exists(wav):
        mp3 = wav.replace(".wav", ".mp3")
        with open(mp3, "wb") as f:
            f.write(requests.get(_generate(text, who), timeout=120).content)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ar", "44100", "-ac", "1", wav], check=True)
    with wave.open(wav) as w:
        return wav, w.getnframes() / w.getframerate()
