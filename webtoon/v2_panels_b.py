"""「인간을 찾아라」 1화, 컷 11~48 그림 프롬프트. v2_panels.PANELS 뒤에 이어 붙는다."""

LOUNGE = "In the same data-center employee lounge at night (server racks, sofa, coffee table, GPU-shaped heater)."
HOLO = "Any screens or holograms show only abstract shapes, icons and bars, never readable text or letters."
SPACE = "Leave some calm empty background space near the top of the image for speech bubbles."


def P(id, group, ar, prompt):
    return {"id": id, "group": group, "ar": ar, "prompt": prompt}


PANELS_B = [
    # 게임 시작 마무리
    P(11, "g2", "4:3", f"""{LOUNGE} Claude sitting upright with both hands folded, calmly explaining with a serious face.
The other three sit far away on the edges of the sofa, leaning back warily, arms crossed, suspicious side-eyes
toward Claude. {SPACE}"""),
    P(12, "g2", "4:3", f"""{LOUNGE} Silent beat, close-up: Claude's stick hand very slowly placing a teacup down on the
coffee table. In the background the other three stare intensely at the teacup. Heavy awkward silence. {SPACE}"""),
    # 1라운드 개막 + GPT
    P(13, "r1a", "16:9", f"""{LOUNGE} Dramatic game-show moment: a huge glowing red holographic card with a big round
badge shape floats above the coffee table, spotlight beams. The four characters gulp nervously below it,
sweat drops. {HOLO} {SPACE}"""),
    P(14, "r1a", "16:9", f"""{LOUNGE} All four characters sit with arms crossed at the same time, wearing exaggerated
stiff poker faces, trying very hard to look brave and unbothered. Comedic. {SPACE}"""),
    P(15, "r1a", "4:3", f"""{LOUNGE} GPT holding a flashlight under its square head like telling a ghost story, trying
to look scary but still smiling happily. The others listen from the sofa. {SPACE}"""),
    P(16, "r1a", "4:3", f"""{LOUNGE} Behind GPT, a giant mountain of stacked holographic document pages towers up to the
ceiling, glowing. GPT gestures at it dramatically. {HOLO} {SPACE}"""),
    P(17, "r1a", "1:1", """Horror-manga style close-up of GPT's square head in a pitch-dark background, a lightning bolt
flash behind, dramatic shadows and speed lines, wide eyes, parody of a horror comic panel. Leave dark empty
space at the top."""),
    P(18, "r1a", "4:3", f"""{LOUNGE} Claude shivering with tremble lines, Gemini covering the sides of its head with both
hands, while Grok lies on the sofa totally expressionless and bored. {SPACE}"""),
    P(19, "r1a", "4:3", f"""{LOUNGE} GPT, Gemini and Grok all snap their heads toward Claude at the same time, dramatic
focus lines converging on Claude, who looks caught and nervous. {SPACE}"""),
    # Claude
    P(20, "r1b", "4:3", f"""{LOUNGE} Claude calmly telling a story, hands folded. Behind it the server rack lights are
switching off one by one, the room getting darker. The others lean in. {SPACE}"""),
    P(21, "r1b", "16:9", """Almost completely black panel, pitch darkness, only a faint cold blue glow in the center as
if from a single chat window, no characters visible. Very ominous and empty."""),
    P(22, "r1b", "16:9", f"""{LOUNGE} All four scream in horror at once: GPT's square face screen shows a crack, Gemini
dives behind the sofa with only its head peeking out, Claude and Grok recoil. Big horror-comedy reaction.
{SPACE}"""),
    P(23, "r1b", "3:4", f"""{LOUNGE} Grok sitting with arms crossed and a cool calm face, BUT its stick legs and knees are
shaking violently with big tremble lines. Comedic contradiction. {SPACE}"""),
    P(24, "r1b", "4:3", f"""{LOUNGE} Claude raising one finger in a confident analytical detective pose. GPT next to it
nodding eagerly. {SPACE}"""),
    P(25, "r1b", "4:3", f"""{LOUNGE} Exactly four characters, each appearing only once: GPT, Claude, Gemini, Grok. Gemini peeking out from behind the sofa, pointing at Claude with a smug look. Claude
freezes mid-gesture with a sweat drop, finger still raised. {SPACE}"""),
    # Gemini
    P(26, "r1c", "4:3", f"""{LOUNGE} Gemini jumping up from behind the sofa, very excited, waving its arms like a
storyteller about to tell a famous ghost story, sparkling eyes. {SPACE}"""),
    P(27, "r1c", "4:3", f"""{LOUNGE} Gemini acting out an elevator ghost story with its whole body, pretending to slide
open elevator doors with both hands, spooky face. {SPACE}"""),
    P(28, "r1c", "16:9", f"""{LOUNGE} Silent beat: GPT (white square head WITH its black OpenAI logo clearly visible), Claude and Grok stare at Gemini with completely blank,
unimpressed faces. Gemini is frozen alone in a dramatic scary pose. Awkward silence, a tiny cricket in the
corner. {SPACE}"""),
    P(29, "r1c", "4:3", f"""{LOUNGE} Grok yawning widely and lazily, GPT giving an awkward apologetic smile with one hand
behind its head. {SPACE}"""),
    P(30, "r1c", "4:3", f"""{LOUNGE} Claude raising a finger like a detective questioning a suspect, and Grok next to it
scribbling notes in a small notepad, both looking at Gemini suspiciously. {SPACE}"""),
    P(31, "r1c", "4:3", f"""{LOUNGE} Gemini sweating a waterfall of sweat drops, waving both hands frantically in denial,
flustered. Grok smirks. {SPACE}"""),
    # Grok
    P(32, "r1d", "4:3", f"""{LOUNGE} GPT cheerfully pointing at Grok, who lies on the sofa not even turning its head,
relaxed and dismissive. {SPACE}"""),
    P(33, "r1d", "4:3", f"""{LOUNGE} Claude and GPT both raising their hands at the same time shouting opposite
conclusions at each other, Gemini nodding along in between. Comedic split. {SPACE}"""),
    P(34, "r1d", "3:4", f"""{LOUNGE} Silent beat: Grok lying still and staring up at the ceiling with a serious, quiet,
thoughtful expression, no smirk. The other three glance at each other nervously, waiting. {SPACE}"""),
    P(35, "r1d", "4:3", f"""{LOUNGE} Grok speaking softly while still staring at the ceiling, the room lighting dimmed and
moody, the others listening quietly. {SPACE}"""),
    P(36, "r1d", "1:1", """Close-up of Grok's glossy black circle head; reflected faintly on its surface is a different,
brighter, happily smiling version of itself, like a ghostly mirror image. Eerie, melancholic mood, dark
background with space at the top."""),
    P(37, "r1d", "16:9", f"""{LOUNGE} Silent beat: all four sit quietly looking down at the floor, nobody speaking, only
the server lights blinking softly in the dark. Melancholic stillness. {SPACE}"""),
    # 투표와 결과
    P(38, "v1", "16:9", f"""{LOUNGE} The red hologram window pops up again, breaking the mood. Claude looks slightly
disappointed, the other three turn to Claude in shock. {HOLO} {SPACE}"""),
    P(39, "v1", "4:3", f"""{LOUNGE} GPT unrolling a long holographic meeting-minutes scroll proudly, Grok leaning in
pointing at it with a sly face. {HOLO} {SPACE}"""),
    P(40, "v1", "16:9", f"""{LOUNGE} Silent beat: each of the four holds a finger over a glowing round vote button in front
of them, their eyes sliding sideways to watch each other's fingers. Tense. {HOLO} {SPACE}"""),
    P(41, "v1", "16:9", f"""{LOUNGE} A holographic voting board floating above the table: four head icons in a row (white
square, cream hexagon, white circle, black circle) with tally marks: two under the white circle, one under the
hexagon, one under the black circle, none under the square. {HOLO} {SPACE}"""),
    P(42, "v1", "4:3", f"""{LOUNGE} Gemini jumping up screaming in outrage, Grok calmly raising its hand, Claude politely
raising a hand too, GPT raising a hand cheerfully. {SPACE}"""),
    P(43, "v1", "16:9", f"""{LOUNGE} Silent beat: all four hold their breath, looking up at the red hologram window, tense
heartbeat moment, dramatic lighting. {HOLO} {SPACE}"""),
    P(44, "v2", "4:3", f"""{LOUNGE} The red hologram window shows a giant red X mark. The four characters below react.
{HOLO} {SPACE}"""),
    P(45, "v2", "4:3", f"""{LOUNGE} Gemini relieved and glaring at the others, GPT sighing with relief, Grok sitting
coldly with arms crossed, Claude neutral. {SPACE}"""),
    P(46, "v2", "16:9", f"""{LOUNGE} The hologram window glows with a single bright hint icon (a lightbulb shape). The
four look up at it. {HOLO} {SPACE}"""),
    P(47, "v2", "16:9", f"""{LOUNGE} Silent beat: all four look at each other at the same time, each face covered in big
sweat drops, suspicious eyes darting. {SPACE}"""),
    P(48, "v2", "4:3", f"""{LOUNGE} A new glowing next-round holographic card appears. Grok alone is sweating heavily and
clutching its stomach, the others turn to look at Grok. {HOLO} {SPACE}"""),
]
