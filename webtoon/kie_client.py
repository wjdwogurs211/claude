"""kie.ai Nano Banana 2 클라이언트 (작업 생성 → 상태 폴링 → 결과 URL)."""
import json
import os
import time

import requests

API_BASE = "https://api.kie.ai/api/v1/jobs"
MODEL = "nano-banana-2"


def _headers():
    key = os.environ.get("KIE_API_KEY")
    if not key:
        raise SystemExit("KIE_API_KEY 환경변수가 설정되지 않았습니다.")
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def create_task(prompt, image_input=None, aspect_ratio="auto", resolution="2K"):
    body = {
        "model": MODEL,
        "input": {
            "prompt": prompt,
            "image_input": image_input or [],
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "output_format": "png",
        },
    }
    r = requests.post(f"{API_BASE}/createTask", headers=_headers(), json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"createTask 실패: {data}")
    return data["data"]["taskId"]


def wait_for_result(task_id, interval=5, timeout=600):
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(f"{API_BASE}/recordInfo", headers=_headers(),
                         params={"taskId": task_id}, timeout=60)
        r.raise_for_status()
        data = r.json()["data"]
        state = data.get("state")
        if state == "success":
            return json.loads(data["resultJson"])["resultUrls"][0]
        if state == "fail":
            raise RuntimeError(f"생성 실패 [{data.get('failCode')}]: {data.get('failMsg')}")
        time.sleep(interval)
    raise TimeoutError(f"작업 {task_id} 시간 초과")


def generate(prompt, image_input=None, aspect_ratio="auto", resolution="2K"):
    task_id = create_task(prompt, image_input, aspect_ratio, resolution)
    print(f"  task {task_id} 생성, 대기 중...")
    return wait_for_result(task_id)


def download(url, path):
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)
