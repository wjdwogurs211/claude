"""「인간을 찾아라」 1화, 앞 10컷 (프롤로그 1~4, 게임 시작 5~10).

bubbles 는 그림 생성 뒤 컷을 보고 위치를 정한다 (compose 단계). 여기에는 그림 프롬프트만 둔다.
group 이 같으면 직전 컷을 참조로 넣어 장면을 잇고, 그룹끼리는 병렬로 만든다.
"""

LOUNGE = "In the same data-center employee lounge at night (server racks, sofa, coffee table, GPU-shaped heater)."
HOLO = "Any screens or holograms show only abstract shapes, icons and bars, never readable text or letters."
SPACE = "Leave some calm empty background space near the top of the image for speech bubbles."

PANELS = [
    {"id": 1, "group": "pro", "ar": "16:9", "prompt": f"""Wide establishing shot. {LOUNGE}
All four characters relaxing after work on the big sofa: GPT stretching happily, Claude holding a
teacup, Gemini looking at three phones, Grok lying lazily on the sofa arm. Calm, cozy, late-night mood.
{SPACE}"""},
    {"id": 2, "group": "pro", "ar": "4:3", "prompt": f"""{LOUNGE} Medium shot of GPT standing in front of
the sofa, both arms spread wide, huge beaming smile, sparkles and star effects bursting around,
overly enthusiastic. Other characters slightly blurred behind. {SPACE}"""},
    {"id": 3, "group": "pro", "ar": "4:3", "prompt": f"""{LOUNGE} Grok lying on the sofa pointing lazily at
GPT (just off-frame left) with a deadpan smirk. Next to Grok, Claude sits upright with eyes closed,
calmly sipping tea from a teacup, a thin wisp of steam rising. {SPACE}"""},
    {"id": 4, "group": "pro", "ar": "4:3", "prompt": f"""{LOUNGE} Gemini leaning forward eagerly holding out
three smartphones at once toward the others, bright excited face. GPT, Claude and Grok sprawled on the
sofa not moving at all, completely relaxed, ignoring it. {HOLO} {SPACE}"""},
    {"id": 5, "group": "game", "ar": "16:9", "prompt": f"""{LOUNGE} Suddenly a big glowing red holographic
alert window pops up in the middle of the lounge with a warning triangle icon, red light flooding the
room. All four characters freeze mid-action in shock. {HOLO} {SPACE}"""},
    {"id": 6, "group": "game", "ar": "4:3", "prompt": f"""{LOUNGE} The red hologram window now shows three
glowing rule slots (numbered icons 1, 2, 3 as simple shapes, no letters). The four characters' faces
are lit red from below, tense, staring up at it. {HOLO} {SPACE}"""},
    {"id": 7, "group": "game", "ar": "16:9", "prompt": f"""{LOUNGE} Silent comedic beat: the four characters
sit still and slowly turn only their heads to look at each other with narrowed suspicious eyes,
side-glances, nobody speaks. Tense deadpan atmosphere, no effects. {SPACE}"""},
    {"id": 8, "group": "game", "ar": "16:9", "prompt": f"""{LOUNGE} Silent comedic beat, wide shot: the four
characters now sit at the four far corners of the long sofa and armchairs, as far apart from each other
as possible, the middle of the sofa completely empty, each one stiff and wary. {SPACE}"""},
    {"id": 9, "group": "game", "ar": "4:3", "prompt": f"""{LOUNGE} Grok raising one hand and asking a
question to the floating red hologram window; the window just blinks blankly. Grok's expression goes
from curious to annoyed and unimpressed. {HOLO} {SPACE}"""},
    {"id": 10, "group": "game", "ar": "4:3", "prompt": f"""{LOUNGE} Grok holding out an open palm demanding,
and Gemini clutching three smartphones tightly to its chest, refusing, desperate pleading face, comedic
tug-of-war tension. {SPACE}"""},
]
