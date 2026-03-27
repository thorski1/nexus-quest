"""
python skill pack - Python Ops
A cyberpunk RPG for learning Python scripting.
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
    id="python",
    title="Python Ops",
    subtitle="◈  Ghost Operative — Script the System, Own the Data  ◈",
    save_file_name="python_quest",
    intro_story=INTRO_STORY,
    quit_message="The script sleeps... but the data is still out there.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "python_basics":       "syntax_ghost",
        "control_flow":        "flow_operator",
        "functions_lab":       "function_forge",
        "data_structures":     "vault_keeper",
        "file_operations":     "file_phantom",
        "string_ops":          "string_cutter",
        "modules_arsenal":     "module_runner",
        "error_handling":      "exception_master",
        "file_io_deep":        "io_specialist",
        "list_comprehensions": "comprehension_ace",
        "requests_http":       "http_operative",
        "classes_and_oop":     "oop_architect",
        "subprocess_and_os":   "shell_commander",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 ____  _  _  ____  _  _  ___  _  _
|  _ \| || ||_  _|| || |/ _ \| \| |
| |_) | \_/ | || | | __ | (_) | .  |
|____/ \___/  |_|  |_||_|\___/|_|\_|
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
