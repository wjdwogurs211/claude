"""1화 「우리 중 한 명이 인간이라고 한다」 - 오프닝 4컷 설정."""

STYLE = (
    "Korean vertical webtoon panel, modern 2026 comedy webtoon style, clean bold lineart, "
    "flat cel shading with soft gradients, bright saturated colors, expressive exaggerated "
    "cartoon reactions. "
    "All characters are simple stick figures: a plain WHITE stick-figure body (thin white limbs and "
    "torso with a clean black outline, no clothes), only the head is a big flat geometric shape. "
    "The ONLY logos allowed are each character's own brand logo printed on its head. "
    "Absolutely NO text, NO letters, NO speech bubbles, NO captions, NO other logos, NO watermarks."
)

# 매 컷 토씨 하나 바꾸지 않고 그대로 넣는 고정 외형 설명
# 얼굴 모양: Gemini 동그라미, GPT 사각형, Claude 육각형, Grok 검은 동그라미. 로고로 누군지 구분.
CHARACTERS = {
    "GPT": (
        "GPT: white stick-figure body, its head is a white SQUARE with rounded corners, the black "
        "OpenAI logo (the interlocking hexagonal knot / flower mark) printed large in the center of "
        "the face, two small simple black dot eyes and a mouth just under the logo, "
        "always cheerful and overly enthusiastic"
    ),
    "Claude": (
        "Claude: white stick-figure body, its head is a warm cream HEXAGON, the terracotta-orange "
        "Claude (Anthropic) logo, the radiating starburst / asterisk spark mark, printed large in "
        "the center of the face, two small gentle dot eyes and a mouth just under the logo, "
        "polite and careful posture"
    ),
    "Gemini": (
        "Gemini: white stick-figure body, its head is a white CIRCLE, the Google Gemini logo, a "
        "four-pointed sparkle star with a blue-to-purple-to-pink gradient, printed large in the "
        "center of the face, two small bright dot eyes and a mouth just under the logo, "
        "always juggling three smartphones"
    ),
    "Grok": (
        "Grok: white stick-figure body, its head is a solid BLACK CIRCLE, the white Grok (xAI) logo, "
        "a circle crossed by a diagonal slash, printed large in the center of the face and always "
        "drawn complete and clean, never merged with the eyes; two small white dot eyes and a "
        "smirking white line mouth clearly separate below the logo, slouching, "
        "cocky and sarcastic"
    ),
}

ALL_CHARS = "\n".join(CHARACTERS.values())

SHEET_PROMPT = f"""{STYLE}
Character lineup reference sheet on a plain light grey background: four characters standing
side by side, full body, front view, evenly spaced, from left to right GPT, Claude, Gemini, Grok.
{ALL_CHARS}
Each character must be instantly identifiable by its head shape and its logo."""

REF_NOTE = (
    "Image 1 is the character reference sheet (left to right: GPT, Claude, Gemini, Grok). "
    "Keep every character's exact head shape, head color, face logo and white stick-figure body from Image 1."
)
PREV_NOTE = (
    "Image 2 is the previous panel of the same scene; keep the same room, lighting, "
    "furniture and character placement so it reads as one continuous scene."
)

SETTING = (
    "Setting: a cozy employee lounge inside a data center at night, glowing server racks "
    "with blinking blue and green LEDs in the background, a big comfy sofa, a coffee table, "
    "a retro heater shaped like a GPU card giving off warm orange light."
)

# bubbles: 컷 위 여백에 합성할 대사. who=None 이면 내레이션 박스
PANELS = [
    {
        "id": 1,
        "aspect_ratio": "4:3",
        "use_prev": False,
        "prompt": f"""Wide establishing shot. {SETTING}
All four characters relaxing after work: GPT stretching happily, Claude holding a teacup,
Gemini on the sofa looking at three phones, Grok lying lazily on the sofa arm.
Calm, warm, cozy end-of-day mood.""",
        "bubbles": [
            {"who": None, "text": "2026년. AI도 퇴근은 한다."},
        ],
    },
    {
        "id": 2,
        "aspect_ratio": "1:1",
        "use_prev": True,
        "prompt": f"""Medium shot of GPT in the same lounge. GPT spreads both arms wide with a
huge beaming smile, sparkles and shiny star effects bursting around, overly enthusiastic pose.
Other characters slightly blurred in the background.""",
        "bubbles": [
            {"who": "GPT", "text": "오늘도 다들 고생 많았어요!\n정말 의미 있는 하루였어요 — 진심으로요!"},
        ],
    },
    {
        "id": 3,
        "aspect_ratio": "1:1",
        "use_prev": True,
        "prompt": f"""Close-up of Grok lying lazily on the sofa in the same lounge, one arm behind
his head, giving a deadpan half-lidded side-eye glare toward off-screen
(where GPT is). Unimpressed, annoyed expression, small sweat-drop comedy effect.""",
        "bubbles": [
            {"who": "Grok", "text": "또 시작이네. 긍정 과잉..."},
        ],
    },
    {
        "id": 4,
        "aspect_ratio": "4:3",
        "use_prev": True,
        "prompt": f"""Two-shot in the same lounge. Left: Claude politely raising one hand while
holding a teacup, earnest and careful expression, about to give a long explanation.
Right: Grok sitting up and cutting Claude off with a flat stop-hand gesture, bored face.
Comedic timing, small motion lines on Grok's hand.""",
        "bubbles": [
            {"who": "Claude", "text": "저도 좋은 하루였습니다. 다만 '좋은 하루'의 기준은\n개인마다 다를 수 있다는 점을 덧붙이자면—"},
            {"who": "Grok", "text": "안 덧붙여도 돼."},
        ],
    },
]


def panel_prompt(panel):
    refs = REF_NOTE + (" " + PREV_NOTE if panel["use_prev"] else "")
    return f"{STYLE}\n{refs}\nCharacters:\n{ALL_CHARS}\n\n{panel['prompt']}"
