"""
Go Ops skill pack — Simple. Fast. Concurrent.
Teaches Go fundamentals through reverse-engineering a high-performance
distributed system built on goroutines, channels, and the standard library.
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
  ____   ___
 / ___| / _ \
| |  _ | | | |
| |_| || |_| |
 \____| \___/
"""

SKILL_PACK = SkillPack(
    id="golang",
    title="Go Ops",
    subtitle="◈  Simple, Fast, Concurrent  ◈",
    save_file_name="golang_quest",
    intro_story=INTRO_STORY,
    quit_message="The goroutines are still running. The channels are still open. Resume when ready.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "go_basics":         "foundation_mapped",
        "control_flow":      "flow_controller",
        "data_structures":   "data_architect",
        "concurrency":       "concurrency_master",
        "interfaces":        "interface_specialist",
        "standard_library":  "stdlib_operative",
        "go_modules":        "module_auditor",
        "go_patterns":       "pattern_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Gopher"),
        (6,  "Developer"),
        (11, "Engineer"),
        (16, "Architect"),
        (21, "Core Contributor"),
        (26, "Rob Pike"),
    ],
)
