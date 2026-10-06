"""「인간을 찾아라」 2화. 투박한 한국 개그 웹툰 그림체(특정 작가·작품 이름은 쓰지 않고 특징만 묘사).

캐릭터 설정(머리 모양·로고·졸라맨 몸)은 1화와 같고, 그림체만 바꾼다.
"""

STYLE = (
    "Korean gag webtoon panel in a very simple, crude, minimalist hand-drawn style: thick slightly uneven "
    "black outlines, flat bright colors with almost no shading, very sparse and simple backgrounds drawn with "
    "a few lines, extremely exaggerated gag reactions (tiny dot eyes, blank deadpan stares, huge open mouths, "
    "sweat drops, vertical gloom lines), loose quick sketchy feel, absurdist deadpan comedy timing. "
    "All characters are simple stick figures: a plain WHITE stick-figure body with a black outline, only the "
    "head is a big flat geometric shape with its brand logo drawn simply. "
    "Absolutely NO text, NO letters, NO speech bubbles, NO captions, NO other logos, NO watermarks."
)

CHARACTERS = (
    "GPT: white SQUARE head with the black OpenAI knot logo in the middle, small dot eyes and mouth under the logo.\n"
    "Claude: cream HEXAGON head with the terracotta-orange starburst Claude logo, small dot eyes and mouth under it.\n"
    "Gemini: white CIRCLE head with the blue-purple four-pointed sparkle Gemini logo, small dot eyes and mouth under it.\n"
    "Grok: solid BLACK CIRCLE head with the white slashed-circle Grok logo drawn complete, small white dot eyes and "
    "smirk under it."
)

SHEET_PROMPT = f"""{STYLE}
Character lineup reference sheet on a plain white background: four characters standing side by side, full body,
front view, evenly spaced, from left to right GPT, Claude, Gemini, Grok.
{CHARACTERS}
Each character must be instantly identifiable by its head shape and its logo."""

ROOM = "In a simple late-night break room drawn with minimal lines: one long sofa, a small coffee table, a few server racks as plain rectangles."
HOLO = "Any screens or holograms show only simple shapes and icons, never readable text."


def P(id, group, ar, prompt):
    return {"id": id, "group": group, "ar": ar, "prompt": prompt}


PANELS = [
    P(1, "a", "16:9", f"""{ROOM} Wide shot: the four characters sit on the sofa exactly where they were, tired, a wall clock
shows a late hour. Deadpan mood."""),
    P(2, "a", "4:3", f"""{ROOM} Gemini stands up proudly with a big shiny star-shaped badge pinned on its chest, puffing out its
chest, very full of itself. Grok in the background gives a flat unimpressed stare."""),
    P(3, "a", "4:3", f"""{ROOM} Gemini pointing one finger at Claude and Grok in turn, eyes narrowed to thin grudge-filled lines,
holding a small notebook. Claude sits politely, Grok looks away."""),
    P(4, "a", "4:3", f"""{ROOM} Gemini with both hands pressed together, begging toward a floating plain rectangle window. The
window stays blank and cold. Pathetic pleading face with big teary eyes. {HOLO}"""),
    P(5, "a", "4:3", f"""{ROOM} Silent gag: Gemini slumped on the sofa, empty-handed, its thumb still making scrolling motions
on an invisible phone out of habit, blank dead-fish eyes."""),
    P(6, "b", "16:9", f"""{ROOM} A big glowing round badge-shaped card floats above the table like a game-show title card,
spotlight. The four characters gulp below it with sweat drops. {HOLO}"""),
    P(7, "b", "4:3", f"""{ROOM} Claude sits upright with hands folded, explaining calmly and seriously. The other three sit far
away at the edges of the sofa, leaning back warily."""),
    P(8, "b", "16:9", f"""{ROOM} All four characters wave both hands in front of their faces at the same time in exaggerated
denial, frantic speed lines, comically identical poses."""),
    P(9, "b", "4:3", f"""{ROOM} Silent gag: GPT, Claude and Gemini all turn their heads at once and stare at Grok with blank dot
eyes. Grok sits stiffly, a single big sweat drop on its black head."""),
    P(10, "b", "4:3", f"""{ROOM} GPT raising its hand eagerly to volunteer with a big smile; Gemini opens a small notebook with a
pen, detective-like."""),
]
