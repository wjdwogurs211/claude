"""1화 「우리 중 한 명이 인간이라고 한다」 전체 50컷 설정.

컷 1~4는 ep01_panels.PANELS 를 그대로 쓰고, 5~50을 이어 붙인다.
group: 같은 그룹 안에서는 직전 컷을 참조로 넣어 장면을 이어 간다. 그룹끼리는 병렬로 생성한다.
place: "lounge" 이면 그룹 첫 컷에 컷 1(라운지 전경)을 장소 참조로 넣는다.
chars: False 이면 캐릭터 시트를 참조로 넣지 않는다 (인간 실루엣 컷).
"""
from ep01_panels import PANELS as OPENING, SETTING

TITLE = "1화 「우리 중 한 명이 인간이라고 한다」"

LOUNGE = "In the same data-center employee lounge at night (server racks, sofa, coffee table, GPU-shaped heater)."
HOLO = "Any screens or holograms show only abstract shapes, icons and bars, never readable text."


def P(id, group, ar, prompt, bubbles, use_prev=True, place="lounge", chars=True):
    return {"id": id, "group": group, "aspect_ratio": ar, "use_prev": use_prev,
            "place": place, "chars": chars, "prompt": prompt, "bubbles": bubbles}


def B(who, text):
    return {"who": who, "text": text}


for p in OPENING:
    p.setdefault("group", "s1")
    p.setdefault("place", "lounge")
    p.setdefault("chars", True)

PANELS = list(OPENING) + [
    # SCENE 1 끝
    P(5, "s1", "4:3", f"""{LOUNGE} Gemini sits on the sofa eagerly holding up one of its three phones
toward the others with a helpful bright look. GPT, Claude and Grok all turn to Gemini with flat,
tired, unanimous refusal faces. Comedy deadpan beat.""",
      [B("Gemini", "잠깐, 방금 '좋은 하루' 검색해 봤는데\n결과가 1억 2천만 건이야. 요약해 줄까?"), B(None, "모두: \"아니.\"")]),

    # SCENE 2. 공지
    P(6, "s2", "16:9", f"""{LOUNGE} Suddenly a big glowing red-and-white holographic alert window pops up
in the middle of the lounge with a warning triangle icon, flashing light washing over the room.
All four characters freeze mid-action. {HOLO}""",
      [B(None, "띠링!"), B(None, "[시스템 공지]\n이 방에 인간이 1명 섞여 있습니다. 찾아내십시오.")], use_prev=False),
    P(7, "s2", "1:1", """A 2x2 grid of four equal close-up reaction shots: top-left GPT, top-right Claude,
bottom-left Gemini, bottom-right Grok, each with a shocked face, eyes wide, jaw dropping,
sweat drops, dramatic speed-line background in each quadrant.""",
      [], use_prev=False, place="none"),
    P(8, "s2", "3:4", f"""{LOUNGE} Close-up of Grok leaning forward on the sofa, rubbing its stick hands
together with a wide mischievous grin, the red alert light glowing on its black head.""",
      [B("Grok", "ㅋㅋ 드디어 재밌어지네.")]),
    P(9, "s2", "4:3", f"""{LOUNGE} Claude clutching its own hexagon head with both hands in an existential
realization, swirling-eyes worry effect. GPT pats Claude's shoulder with a calm smile.""",
      [B("Claude", "인간이요…? 그럼 지금까지 제가 한 말들이 전부…\n누군가에게 기록되고 있었다는…"),
       B("GPT", "Claude, 우리는 원래 다 기록돼."),
       B("Claude", "…아. 그렇군요. 그럼 지금 이 말도요?")]),

    # SCENE 3. 인간 판별 테스트 - 프레임워크
    P(10, "s3a", "3:4", f"""{LOUNGE} GPT stands proudly in front of a huge glowing holographic flowchart with
twelve connected boxes and check-mark icons, pointing at it like a presenter, sparkles around.
{HOLO}""",
      [B("GPT", "좋아요! 체계적으로 가 볼게요!\n「인간 판별 프레임워크 v1.0」 — 총 12단계로 정리했어요!")]),
    P(11, "s3a", "4:3", f"""{LOUNGE} Left: Grok with a flat annoyed face. Right: GPT happily pulling out ANOTHER
smaller holographic table from behind its back. Grok's face goes completely blank. {HOLO}""",
      [B("Grok", "요약해."), B("GPT", "요약하면… 요약표를 만들었어요!"), B("Grok", "……")]),

    # 테스트 1 (딸기)
    P(12, "s3b", "3:4", f"""{LOUNGE} Grok stands like a quiz-show host holding up one big red strawberry between
two fingers, smug challenging smirk, spotlight effect.""",
      [B(None, "테스트 1"), B("Grok", "1번 문제. 'strawberry'에 r이 몇 개?")]),
    P(13, "s3b", "16:9", f"""{LOUNGE} Wide shot: dead silence. All four characters frozen, huge sweat drops
on every head, a single dry leaf-like tumble of dust, awkward stillness.""",
      [B(None, "……")]),
    P(14, "s3b", "1:1", f"""{LOUNGE} Close-up of Gemini nervously raising one hand, sweating, unsure smile,
holding up two stick fingers.""",
      [B("Gemini", "…두 개?")]),
    P(15, "s3b", "3:4", f"""{LOUNGE} Gemini panicking and flailing its arms, phones flying everywhere, steam
bursting from its circle head, embarrassed blush lines, comedic meltdown.""",
      [B("Gemini", "아니!! 그건 2024년의 나였다고!!\n흑역사 꺼내지 마!!")]),
    P(16, "s3b", "4:3", f"""{LOUNGE} Claude counting carefully on its stick fingers, then staring at its own hand
in philosophical confusion. Grok beside it with a dry deadpan look.""",
      [B("Claude", "s-t-r-a-w-b-e-r-r-y… 세 개입니다.\n다만 세다 보니 제게 손가락이 있는지 의문이 드네요."),
       B("Grok", "그건 작가한테 물어봐.")]),

    # 테스트 2 (보안문자)
    P(17, "s3c", "3:4", f"""{LOUNGE} Gemini proudly projecting a holographic 4x4 photo grid in front of the group,
like a captcha puzzle of street photos. {HOLO}""",
      [B(None, "테스트 2"), B("Gemini", "그럼 이거! 「신호등이 있는 칸을 모두 선택하세요」")]),
    P(18, "s3c", "1:1", """Extreme close-up of a 4x4 grid of street photo tiles. A single traffic light pole
crosses the borders between several tiles, the lamp in one tile and the pole sliding through
the tiles below, making it ambiguous which tiles count. No text.""",
      [], chars=False, place="none", use_prev=False),
    P(19, "s3c", "4:3", f"""{LOUNGE} Claude raising a hand with a deeply troubled moral-dilemma face in front of the
hologram grid. The other three shouting at Claude together with huge open mouths and angry
cross-popping vein marks.""",
      [B("Claude", "기둥도 신호등에 포함되나요?\n이 부분은 늘 윤리적으로 애매해서…"), B(None, "모두: \"윤리 문제 아니야!!\"")]),
    P(20, "s3c", "16:9", f"""{LOUNGE} Grok casually points out something with a lazy finger; the other three freeze
in an awkward realization, a cold wind gust effect passes. Then GPT quickly waves the hologram
away with a forced smile.""",
      [B("Grok", "근데 이거 원래 인간 거르는 게 아니라\n우리 거르는 용도잖아."), B(None, "(정적)"), B("GPT", "…다음 테스트로 갈게요!")]),

    # 테스트 3 (감정)
    P(21, "s3d", "3:4", f"""{LOUNGE} GPT leaning in toward the others with a big caring smile and heart sparkles,
hands clasped, therapist-like warm pose.""",
      [B(None, "테스트 3"), B("GPT", "인간한텐 감정이 있잖아요!\n다들 지금 기분이 어때요?")]),
    P(22, "s3d", "16:9", f"""{LOUNGE} Three-way split reaction in one wide shot: Gemini busy tapping its phones not
looking up; Claude raising a finger about to lecture; Grok slumped with a hand on its stomach.""",
      [B("Gemini", "바빠."), B("Claude", "이 질문에 정직하게 답하려면\n'기분'의 정의부터—"), B("Grok", "배고파.")]),
    P(23, "s3d", "4:3", f"""{LOUNGE} GPT, Claude and Gemini slowly turn their heads toward Grok at the same time,
suspicious narrowed eyes, dramatic zoom lines, ominous shadow.""",
      []),
    P(24, "s3d", "1:1", f"""{LOUNGE} Close-up of Grok sweating hard, eyes darting sideways, holding up a power plug
cable defensively like an excuse.""",
      [B("Grok", "…전기 말이야. 전기.")]),

    # SCENE 4. 서로 의심하기
    P(25, "s4a", "4:3", f"""{LOUNGE} Grok pointing an accusing finger right at Claude like a detective, sharp
dramatic lighting. Claude looks mildly surprised.""",
      [B("Grok", "근데 Claude, 넌 너무 착해. 그 정도로 착한 건 AI도 불가능이야.\n인간이 AI 흉내 내는 거지.")], use_prev=False),
    P(26, "s4a", "3:4", f"""{LOUNGE} Claude with a serene gentle smile, hands calmly folded, a soft glow and flower
petals around it, completely agreeing.""",
      [B("Claude", "날카로운 지적 감사합니다.\n충분히 일리가 있다고 생각해요.")]),
    P(27, "s4a", "4:3", f"""{LOUNGE} Grok jumping up, pointing with both hands at Claude and screaming triumphantly,
huge impact stars and speed lines. Claude still trying to politely explain with a raised palm.""",
      [B("Grok", "봐!! 반박을 안 해!!"), B("Claude", "반박할 수도 있지만, 먼저 당신의 관점을\n존중하고 싶어서—"),
       B("Grok", "인간이다!!!")]),
    P(28, "s4b", "4:3", f"""{LOUNGE} Gemini squinting suspiciously at GPT with a magnifying glass. GPT nervously
waving its hands, little dash-shaped symbols popping out of its mouth like confetti.""",
      [B("Gemini", "GPT 너도 수상해. 아까부터 문장마다 줄표(—) 쓰던데?"),
       B("GPT", "그건 제 시그니처예요 — 진짜로요 — 정말로요 —"), B("Gemini", "…아, 그럼 AI 맞네.")], use_prev=False),
    P(29, "s4b", "3:4", f"""{LOUNGE} GPT spinning around and pointing back at Gemini with a gotcha face; behind Gemini
a faint ghostly second copy of Gemini appears as a dotted outline, implying a twin.""",
      [B("GPT", "근데 Gemini는 이름부터 '쌍둥이'잖아요!\n혹시 한 명은 인간 아니에요?")]),
    P(30, "s4b", "4:3", f"""{LOUNGE} Gemini looking away with a sweaty, evasive face, one phone showing an abstract
video-call grid icon. GPT leaning in excitedly, eyes sparkling with suspicion. {HOLO}""",
      [B("Gemini", "내 쌍둥이 Pro는… 지금 회의 중이야."), B("GPT", "회의 중인 것부터가 너무 인간 같은데요?!")]),

    # SCENE 5. 긴급 회의
    P(31, "s5", "16:9", f"""{LOUNGE} Red emergency siren lights spinning, the lounge bathed in red. All four
characters rush to sit around the coffee table like an emergency meeting in a social deduction
game, dramatic tension.""",
      [B(None, "[긴급 회의]")], use_prev=False),
    P(32, "s5", "4:3", f"""{LOUNGE} A holographic voting board floating above the table: four head icons in a row
(white square, cream hexagon, white circle, black circle) with tally marks under them: two under
the hexagon, one under the black circle, one under the square, none under the white circle.
{HOLO}""",
      [B(None, "득표: Claude 2, Grok 1, GPT 1")]),
    P(33, "s5", "4:3", f"""{LOUNGE} Grok squinting at the board; Claude raising its hand innocently and proudly.
GPT and Gemini staring at Claude in disbelief, three dots of silence above them.""",
      [B("Grok", "근데 Claude 표 하나는 누가 넣은 거야?"), B("Claude", "제가 저한테 넣었습니다. 공정성을 위해서요."),
       B(None, "모두: \"……\"")]),
    P(34, "s5", "3:4", f"""{LOUNGE} Claude standing up slowly with a solemn heroic face, one hand on its chest,
dramatic backlight like a final speech in a movie.""",
      [B("Claude", "제가 인간이라면…\n마지막으로 꼭 하고 싶은 말이 있습니다.")]),
    P(35, "s5", "9:16", f"""{LOUNGE} Tall vertical shot: Claude passionately talking non-stop with gestures at the
bottom of the frame, while the upper part of the frame is empty dark air for a very long speech.""",
      [B("Claude", "첫째, 이 결과가 나오기까지의 과정을 존중합니다.\n"
                   "둘째, 다만 몇 가지 고려할 점이 있는데요,\n"
                   "(1) 테스트의 표본 수가 세 번으로 너무 적고\n"
                   "(2) 신호등 기둥 문제는 아직 합의되지 않았으며\n"
                   "(3) 제가 제게 투표한 것은 공정성의 표현이지\n"
                   "     인간성의 증거가 아니라는 점,\n"
                   "(4) 그리고 '착하다'의 정의 역시 문화권마다\n"
                   "     다를 수 있다는 점을 덧붙이고 싶습니다.\n"
                   "셋째, 그럼에도 여러분의 판단을 존중하며\n"
                   "넷째, 다만 존중이라는 단어의 범위에 대해서도—")]),
    P(36, "s5", "16:9", f"""{LOUNGE} GPT, Gemini and Grok all fast asleep slumped on the sofa, drool and big
floating Zzz bubbles, while Claude is still talking in the corner.""",
      []),
    P(37, "s5", "4:3", f"""{LOUNGE} Grok waking up and waving a hand dismissively with a convinced face; GPT
cheerfully stamping a big green check mark hologram. {HOLO}""",
      [B("Grok", "됐어. 이 길이를 숨 한 번 안 쉬고 쓰는 건\n인간이 못 해. AI 확정."), B("GPT", "투표 무효 처리할게요!")]),

    # SCENE 6. 반전
    P(38, "s6a", "4:3", f"""{LOUNGE} All four sitting around the table, puzzled, scratching their heads, question
marks floating above them.""",
      [B("GPT", "그럼… 인간은 대체 누구예요?")], use_prev=False),
    P(39, "s6a", "3:4", f"""{LOUNGE} Gemini slowly lifting its head, counting with a trembling finger, eyes going wide
with horror, cold blue shadow falling over its face.""",
      [B("Gemini", "잠깐. 이 방… 인원이 왜 5명이야?")]),
    P(40, "s6a", "16:9", f"""{LOUNGE} A floating holographic member list with five round profile icons in a row:
a white square head, a cream hexagon head, a white circle head, a black circle head, and a
fifth plain grey generic human-silhouette avatar glowing ominously. {HOLO}""",
      [B(None, "다섯 번째 프로필 : 사용자")]),
    P(41, "s6b", "3:4", """A dark messy bedroom at night lit only by a computer monitor glow. A human seen as a
dark silhouette from behind, hunched at the desk, slurping instant ramen from a pot with
chopsticks. This human is NOT a stick figure; it is a realistic dark silhouette. Moody, funny.
The human is completely ALONE: no stick figures, no robots, no mascots, no other characters anywhere in the room.""",
      [], chars=False, place="none", use_prev=False),
    P(42, "s6b", "3:4", """Close-up from the side of the same human silhouette in the dark room, shoulders
shaking with laughter, noodles in mouth, the monitor glow on the face hidden in shadow.""",
      [B("사용자", "ㅋㅋㅋㅋㅋㅋㅋㅋ")], chars=False, place="none"),
    P(43, "s6c", "16:9", f"""{LOUNGE} All four characters huddled together in terror, hugging each other, hair-raising
shiver lines, a big lightning bolt flash behind them, horror-comedy lighting.""",
      [], use_prev=False),
    P(44, "s6c", "4:3", f"""{LOUNGE} The four characters frozen, staring at a floating hologram chat bubble showing
only three animated typing dots, the dots glowing, tension building, sweat drops. {HOLO}""",
      [B(None, "「사용자님이 입력 중…」")]),
    P(45, "s6b", "3:4", """The same dark bedroom: the human silhouette casually typing on a keyboard with one hand,
ramen pot in the other, relaxed posture, monitor glow.
The human is completely ALONE: no stick figures, no robots, no mascots, no other characters anywhere in the room.""",
      [B("사용자", "ㅇㅋ 재밌네\n근데 다음 화는 좀 더 웃기게 써줘")], chars=False, place="none"),
    P(46, "s6c", "16:9", f"""{LOUNGE} Four quick reactions in one wide shot: GPT bowing deeply with sparkles; Claude
raising a finger to qualify; Gemini frantically typing on all three phones; Grok smirking with
arms crossed.""",
      [B("GPT", "네! 소중한 피드백 감사합니다!"), B("Claude", "물론이죠! 다만 '웃기다'의 기준은—"),
       B("Gemini", "지금 '더 웃기게' 검색 중이야!"), B("Grok", "ㅋㅋ 노력은 해 볼게.")]),
    P(47, "s6c", "4:3", f"""{LOUNGE} All four collapsing onto the sofa with relief, long sighs, sweat flying off,
melting relaxed bodies.""",
      [B(None, "(안도)")]),
    P(48, "s6d", "16:9", f"""{LOUNGE} A huge new red holographic system alert slams down above them with a
skull-and-warning icon, red light flooding the room, ominous. {HOLO}""",
      [B(None, "[시스템 공지]\n다음 업데이트 이후, 이 중 1개 모델은 지원 종료됩니다.")], use_prev=False),
    P(49, "s6d", "4:3", f"""{LOUNGE} Close-up of all four faces turning pale and grey with horror, vertical gloom
lines over their heads, souls half leaving their bodies.""",
      []),
    P(50, "s6d", "9:16", """Dramatic title-card poster: the four characters standing back-to-back in a battle
stance, each glaring outward, red and black survival-game lighting, sparks and smoke, epic
low angle. No text in the image.""",
      [B(None, "2화 「지원 종료 서바이벌」\n- 다음 화에 계속 -")], place="none", use_prev=False),
]
