"""
bash skill pack - Terminal Quest
A cyberpunk RPG for learning the shell.
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
    id="bash",
    title="Terminal Quest",
    subtitle="◈  Ghost Operative — Infiltrate the Corporate Shell  ◈",
    save_file_name="terminal_quest",
    intro_story=INTRO_STORY,
    quit_message="The Shell sleeps... but only for now.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "antechamber": "navigator",
        "archive_vaults": "archivist",
        "oracle_library": "seeker",
        "pipe_sanctum": "pipe_dream",
        "process_catacombs": "necromancer",
        "permissions_fortress": "warden",
        "scripting_citadel": "scriptor",
        "network_nexus": "networked",
        "grand_terminal": "grandmaster",
        "environment_chamber": "env_operative",
        "text_processing_forge": "data_shaper",
        "stream_editor_lab": "stream_master",
        "shell_scripting_basics": "script_foundry_cleared",
        "job_control": "job_control_cleared",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 _____ ______________  ________ _   _   ___   _
|_   _|  ___| ___ \  \/  |_   _| \ | | / _ \ | |
  | | | |__ | |_/ / .  . | | | |  \| |/ /_\ \| |
  | | |  __||    /| |\/| | | | | . ` ||  _  || |
  | | | |___| |\ \| |  | |_| |_| |\  || | | || |____
  \_/ \____/\_| \_\_|  |_/\___/\_| \_/\_| |_/\_____/
""",
    level_titles=[
        (1, "Rookie"),
        (6, "Operative"),
        (11, "Shadow"),
        (16, "Ghost"),
        (21, "Phantom"),
        (26, "Specter"),
    ],
)
