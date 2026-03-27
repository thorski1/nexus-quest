"""
regex skill pack — Pattern Recon
A cyberpunk RPG for mastering regular expressions.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="regex",
    title="Pattern Recon",
    subtitle="◈  Decode the Signal — Master the Pattern  ◈",
    save_file_name="regex_quest",
    intro_story=INTRO_STORY,
    quit_message="The signal fades to static. Your patterns are saved. Go dark.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_patterns":       "pattern_initiate",
        "character_classes":    "class_decoder",
        "anchors_groups":       "anchor_specialist",
        "quantifiers_advanced": "quantifier_master",
        "lookarounds":          "lookaround_ghost",
        "real_world_patterns":  "signal_analyst",
        "regex_flags":          "flag_operator",
        "python_regex":         "python_regex_engineer",
        "sed_and_grep_regex":              "stream_rewriter",
        "named_groups_and_backreferences": "group_master",
        "substitution_and_replace":        "pattern_surgeon",
        "regex_in_javascript":             "js_regex_hacker",
        "advanced_techniques":             "regex_sensei",
    },
    achievements={
        "pattern_initiate":       ("Pattern Initiate",      "Decoded the fundamentals of regex syntax."),
        "class_decoder":          ("Class Decoder",          "Cracked every character class in the vault."),
        "anchor_specialist":      ("Anchor Specialist",      "Pinned patterns to lines like a pro."),
        "quantifier_master":      ("Quantifier Master",      "Wielded *, +, ?, and {n,m} without flinching."),
        "lookaround_ghost":       ("Lookaround Ghost",       "Vanished into lookaheads and lookbehinds undetected."),
        "signal_analyst":         ("Signal Analyst",         "Extracted real-world data from the noise."),
        "flag_operator":          ("Flag Operator",          "Mastered re.IGNORECASE, MULTILINE, DOTALL, and VERBOSE."),
        "python_regex_engineer":  ("Python Regex Engineer",  "Used re.compile, findall, sub, and named groups fluently."),
        "stream_rewriter":        ("Stream Rewriter",        "Wielded grep -oE, sed -i, awk, and the log extraction pipeline."),
        "group_master":           ("Group Master",           "Named every capture group and backreferenced like a surgeon."),
        "pattern_surgeon":        ("Pattern Surgeon",        "Rewrote data in-place with re.sub() and sed substitutions."),
        "js_regex_hacker":        ("JS Regex Hacker",        "Cracked JavaScript regex syntax and found the client-side bypass."),
        "regex_sensei":           ("Regex Sensei",           "Identified ReDoS patterns and writes production-safe expressions."),
        "no_hints":               ("Dark Mode",              "Completed a zone without any hints."),
        "speed_reader":           ("Signal Flash",           "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=r"""
 ____  ___  ___  ___ __  __
|  _ \| __|| __|| __| \/ /
| |_) | _|  | _| | _|  \/
|____/|___| |___||___| |_|
""",
    level_titles=[
        (1,  "Rookie"),
        (6,  "Operative"),
        (11, "Shadow"),
        (16, "Ghost"),
        (21, "Phantom"),
        (26, "Specter"),
    ],
)
