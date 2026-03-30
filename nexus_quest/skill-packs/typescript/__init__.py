"""
typescript skill pack — Type Forge
A cyberpunk RPG for learning TypeScript.
Types are your armor. TypeScript is JavaScript that scales.
"""

import sys
from pathlib import Path

# Make engine importable from within skill pack if needed
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
    ACHIEVEMENT_DESCRIPTIONS,
)
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="typescript",
    title="Type Forge",
    subtitle="◈  Types Are Your Armor  ◈",
    save_file_name="typescript_quest",
    intro_story=INTRO_STORY,
    quit_message="The compiler sleeps... but the types are still watching.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ts_basics":         "type_initiate",
        "interfaces_types":  "interface_architect",
        "generics":          "generic_master",
        "unions_narrowing":  "narrowing_expert",
        "enums_literals":    "literal_keeper",
        "advanced_types":    "type_surgeon",
        "ts_with_react":     "react_typer",
        "tooling":           "compiler_commander",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 _____ _  _ ___  ___   ___  ___  ___   ___  ___
|_   _| \| | _ \| __| | __/ _ \| _ \ / __|| __|
  | | |  | |  _/| _|  | _| (_) |   /| (_ || _|
  |_| |_|\_|_|  |___| |_| \___/|_|_\ \___||___|
""",
    level_titles=[
        (1,  "any"),
        (6,  "string"),
        (11, "generic<T>"),
        (16, "Architect"),
        (21, "Type Wizard"),
        (26, "Anders Hejlsberg"),
    ],
)
