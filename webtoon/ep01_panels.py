"""1화 「우리 중 한 명이 인간이라고 한다」 - 오프닝 4컷 설정."""

STYLE = (
    "Korean vertical webtoon panel, modern 2026 comedy webtoon style, clean bold lineart, "
    "flat cel shading with soft gradients, bright saturated colors, expressive exaggerated "
    "cartoon reactions, chibi-leaning 3-head proportions. "
    "Absolutely NO text, NO letters, NO speech bubbles, NO captions, NO logos, NO watermarks."
)

# 매 컷 토씨 하나 바꾸지 않고 그대로 넣는 고정 외형 설명
CHARACTERS = {
    "GPT": (
        "GPT: a humanoid robot mascot with a smooth round glossy white head that is a screen "
        "showing two happy curved-arc eyes, wears an oversized black hoodie, white sneakers, "
        "always cheerful and overly enthusiastic"
    ),
    "Claude": (
        "Claude: a humanoid robot mascot with a soft round warm-beige head-screen showing gentle "
        "dot eyes, a small glowing orange sparkle-star floating above the head, wears a "
        "terracotta-orange knit cardigan over a cream shirt, polite and careful posture"
    ),
    "Gemini": (
        "Gemini: a humanoid robot mascot with a round head-screen in a blue-to-purple gradient "
        "showing bright star-shaped eyes, a four-pointed star hairpin, wears a blue-violet "
        "gradient puffer jacket, always juggling three smartphones"
    ),
    "Grok": (
        "Grok: a humanoid robot mascot with a matte black angular head-screen showing a smirking "
        "white line mouth, wears black sunglasses and a black leather jacket, slouching, "
        "cocky and sarcastic"
    ),
}

ALL_CHARS = "\n".join(CHARACTERS.values())

SHEET_PROMPT = f"""{STYLE}
Character lineup reference sheet on a plain light grey background: four characters standing
side by side, full body, front view, evenly spaced, from left to right GPT, Claude, Gemini, Grok.
{ALL_CHARS}
Each character must be clearly distinct in color and silhouette."""

REF_NOTE = (
    "Image 1 is the character reference sheet (left to right: GPT, Claude, Gemini, Grok). "
    "Keep every character's exact design, colors, outfit and head shape from Image 1."
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
his head, lowering his sunglasses slightly to give a deadpan side-eye glare toward off-screen
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
