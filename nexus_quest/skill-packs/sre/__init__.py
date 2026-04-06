"""
SRE skill pack — The Reliability Engine
Theme: CIPHER cyberpunk. The grid must hold. Reliability is not luck — it is engineering.
Covers: SLIs/SLOs/SLAs, error budgets, incident management, capacity planning, resilience patterns, on-call operations.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
    ACHIEVEMENT_DESCRIPTIONS,
)
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ ___  _____
/ __| _ \| ____|
\__ \|   /|  _|
|___/|_|_\|_____|
  THE RELIABILITY ENGINE
"""

SKILL_PACK = SkillPack(
    id="sre",
    title="The Reliability Engine",
    subtitle="// THE GRID MUST HOLD //",
    save_file_name="sre_quest",
    intro_story=INTRO_STORY,
    quit_message="The grid holds. Your shift state has been saved.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "sre_fundamentals":     "budget_keeper",
        "incident_management":  "war_room_commander",
        "capacity_planning":    "load_forger",
        "reliability_patterns": "fault_line_engineer",
        "oncall_operations":    "night_watch_captain",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Pager Holder"),
        (6, "Incident Responder"),
        (11, "Reliability Engineer"),
        (16, "Resilience Architect"),
        (21, "Grid Commander"),
        (26, "Grid Master"),
    ],
)
