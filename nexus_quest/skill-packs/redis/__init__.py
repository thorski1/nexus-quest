"""
redis skill pack - The Cache Matrix
A cyberpunk RPG for learning Redis.
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

SKILL_PACK = SkillPack(
    id="redis",
    title="The Cache Matrix",
    subtitle="◈  Cache Operator — Trace the Poisoned Keys  ◈",
    save_file_name="redis_quest",
    intro_story=INTRO_STORY,
    quit_message="The cache persists... the keys will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "redis_basics": "navigator",
        "data_structures": "archivist",
        "pubsub_streams": "seeker",
        "caching_patterns": "pipe_dream",
        "redis_production": "necromancer",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
______ _____ ______ _____ _____
| ___ \  ___|  _  \_   _/  ___|
| |_/ / |__ | | | | | | \ `--.
|    /|  __|| | | | | |  `--. \
| |\ \| |___| |/ / _| |_/\__/ /
\_| \_\____/|___/  \___/\____/
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
