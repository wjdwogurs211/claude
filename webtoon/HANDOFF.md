# 「인간을 찾아라」 웹툰 작업 인수인계

마지막 갱신: 2026-10-07. 다음 세션은 이 파일부터 읽는다.

## 지금 상태 한눈에

| 항목 | 상태 | 위치 |
| --- | --- | --- |
| 1화 (50컷) | **완성.** 표정은 개그 웹툰 스타일, 말풍선은 꼬리 없이 화자 근처 + 이름표 | `output/1화_완성본/` |
| 1화 네이버 업로드본 | 완성. 690px, 장당 최대 1280px, JPG 32장 | `output/1화_완성본/네이버업로드/` |
| 1화 컷츠 영상 | 1편(#1~#9, 1분 56초, 무음)만 완성. 1화 전체를 5~6편으로 나눌 예정 | `output/1화_완성본/컷츠/1화_1편.mp4` |
| 캐릭터 음성 | `voices.py` 준비. kie.ai ElevenLabs가 서버 오류로 실패해서 시험본 아직 없음 | `voices.py` |
| 2화 | 대본 완성. 투박한 그림체로 시험 10컷만 생성. **정리 필요(아래)** | `output/ep02/` |

## 대본 문서 (Claude Docs)

- 1화 대본(현재 버전): https://claude.ai/code/artifact/3935f1c4-0fdd-4e27-a40a-29197d13de3f
- 2화 대본: https://claude.ai/code/artifact/07f662e3-070f-4116-ba78-af9080e975f4
- 예전 문서(참고용): 첫 1화 작가 노트 `6df615db-...`, 1화 개정 대본 `86dcf505-...` (내용이 섞여 있어 쓰지 않음)

## 설정과 규칙

- 캐릭터: 흰 졸라맨 몸 + 머리 모양/로고로 구분. GPT 흰 사각형, Claude 크림색 육각형, Gemini 흰 동그라미(그라데이션 별), Grok 검은 동그라미(흰 사선 원).
- 1화 #45에서 Gemini는 천장 집게에 끌려가 **퇴장**. #46부터 Gemini 없음.
- 말풍선 이름표 색: 지피티 #10A37F, 클로드 #C8643B, 제미나이 #4F6BED, 그록 #111111.
- 대사는 그림 안에 그리지 않고 코드로 합성한다(한글 정확도, 수정 비용 0).
- 실제 회사 로고를 쓰므로 공개·수익화 전 상표 검토가 필요하다.

## 파일 지도 (webtoon/)

- 합성: `compose_v2.py`(말풍선·박스 그리기), `build_ep01v2.py`(1화 합성, `NO_TAILS`, `USE_FACES` 스위치)
- 1화 데이터: `v2_panels.py`, `v2_panels_b.py`(그림 프롬프트), `bubbles_v2.py`, `bubbles_v2b.py`(말풍선 위치·대사), `speakers.py`(화자 표)
- 그림 생성/수정: `make_v2.py`(컷 생성), `extend_tops.py`(위쪽 늘리기), `faces.py`(표정만 교체)
- 출력: `naver_export.py`(네이버 분할), `cuts_video.py`(컷츠 영상, `PARTS`에 편 범위)
- 2화: `ep02_panels.py`, `make_ep02.py`, `bubbles_ep02.py`
- 공통: `kie_client.py`, `fonts/NanumGothicBold.ttf`

## 자주 쓰는 명령

```bash
cd ~/Projects/webtoon-ep01/webtoon
set -a && . ~/.config/kie/.env && set +a     # KIE_API_KEY (값은 저장소에 없음)
PYTHONIOENCODING=utf-8 python build_ep01v2.py   # 1화 다시 합성 (크레딧 0)
PYTHONIOENCODING=utf-8 python naver_export.py   # 네이버 업로드본 다시 자르기
PYTHONIOENCODING=utf-8 python cuts_video.py 1   # 컷츠 1편 렌더 (약 4분)
```

## 원본 그림은 저장소에 없다

`output/ep01v2/`(약 1.3GB), `output/ep02/`, `output/_보관_1화_첫버전/`은 용량 때문에 git에서 뺐다.
**이 PC의 `C:\Users\우미린7\Projects\webtoon-ep01\webtoon\output\` 에만 있다.** 지우면 1화를 다시 합성할 수 없다.
kie.ai 결과 URL(`urls.json`)은 며칠 뒤 만료되므로 원본 대체용이 아니다.

## 다음 할 일

1. kie.ai ElevenLabs 복구 확인 → `voices.py`로 컷 #3 목소리 시험본(클로드 늘어지는 할아버지 톤 등) → 확정되면 `cuts_video.py`가 음성 길이로 싱크를 맞추게 고친다.
2. 컷츠 2~6편 범위 정하기(`cuts_video.py`의 `PARTS`, 편당 2분 이내).
3. 2화 정리: 대본과 시험 10컷이 아직 "Gemini 수사반장" 설정이다. Gemini 퇴장에 맞춰 대본 수정 → 그림체(1화 스타일 vs 투박한 스타일) 결정 → 생성.
4. 남은 작은 흠: #14 표정 미교체(3회 실패), #3·#48 말풍선 살짝 겹침, 늘린 컷 이음선.

## 크레딧

kie.ai 잔액 3,969.84 (2026-10-07). 그림 1장 약 12크레딧.
