"""
postgres skill pack - Postgres Quest
A cyberpunk RPG for learning PostgreSQL.
"""

import sys
from pathlib import Path

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
    id="postgres",
    title="Postgres Quest",
    subtitle="◈  Data Archaeologist — Excavate the Corporate Archive  ◈",
    save_file_name="postgres_quest",
    intro_story=INTRO_STORY,
    quit_message="The database sleeps... the queries will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "surface_tables": "navigator",
        "filter_chambers": "archivist",
        "aggregation_engine": "seeker",
        "junction_archive": "pipe_dream",
        "subquery_vaults": "necromancer",
        "schema_forge": "warden",
        "index_sanctum": "scriptor",
        "transaction_core": "grandmaster",
        "window_functions":   "window_analyst",
        "json_forge":         "json_archaeologist",
        "transactions_vault": "isolation_expert",
        "performance_tuning": "performance_engineer",
        "replication_and_backup": "replication_architect",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
______ _____ _____ _____ _____ ______ _____  _____
| ___ \  _  /  ___|_   _|  __ \| ___ \  ___/  ___|
| |_/ / | | \ `--.  | | | |  \/| |_/ / |__ \ `--.
|  __/| | | |`--. \ | | | | __ |    /|  __| `--. \
| |   \ \_/ /\__/ / | | | |_\ \| |\ \| |___/\__/ /
\_|    \___/\____/  \_/  \____/\_| \_\____/\____/
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
