"""
Shell Scripting skill pack — Script Forge
Automate everything. The shell is your superpower.
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
  ___ ___ ___ ___ ___ _____   ___ ___  ___  ___ ___
 / __/ __| _ \_ _| _ \_   _| | __/ _ \| _ \/ __| __|
 \__ \__ \   /| ||  _/ | |   | _| (_) |   / (_ | _|
 |___/___/_|_\___|_|   |_|   |_| \___/|_|_\\___|___|
"""

SKILL_PACK = SkillPack(
    id="shell_scripting",
    title="Script Forge",
    subtitle="◈  Automate Everything  ◈",
    save_file_name="script_forge",
    intro_story=INTRO_STORY,
    quit_message="The script is paused. The cron job will wait.",
    name_prompt="[bold cyan]Operative handle:[/bold cyan]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "shebang_and_basics": "shebang_master",
        "conditionals": "conditional_master",
        "loops": "loop_master",
        "functions": "function_master",
        "text_processing": "text_master",
        "input_output": "io_master",
        "error_handling": "error_master",
        "real_scripts": "deploy_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "echo"),
        (6, "if/else"),
        (11, "Pipeline"),
        (16, "Automator"),
        (21, "Shell Lord"),
        (26, "Bourne Again"),
    ],
)
