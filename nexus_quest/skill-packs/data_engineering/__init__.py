"""
Data Engineering skill pack — Data Forge
Theme: Rebuilding a collapsed analytics platform. Data is the new oil —
       raw data is useless, you need to refine it.
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
______ _____ _____ _____   ______ ___________  _____ _____
|  _  \  _  |_   _|  _  |  |  ___|  _  | ___ \|  __ \  ___|
| | | | |_| | | | | |_| |  | |_  | | | | |_/ /| |  \/ |__
| | | |  _  | | | |  _  |  |  _| | | | |    / | | __|  __|
| |/ /| | | | | | | | | |  | |   \ \_/ / |\ \ | |_\ \ |___
|___/ \_| |_/ \_/ \_| |_/  \_|    \___/\_| \_| \____/\____/
"""

SKILL_PACK = SkillPack(
    id="data_engineering",
    title="Data Forge",
    subtitle="◈  Refine Raw Data Into Gold  ◈",
    save_file_name="data_engineering_quest",
    intro_story=INTRO_STORY,
    quit_message="The pipelines are paused. Your progress is saved — the data will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "data_pipelines":   "pipeline_builder",
        "data_warehouses":  "warehouse_modeler",
        "streaming":        "stream_rider",
        "data_lakes":       "lake_navigator",
        "spark":            "spark_optimizer",
        "data_quality":     "quality_enforcer",
        "orchestration":    "orchestration_master",
        "modern_stack":     "forge_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Analyst"),
        (6, "Engineer"),
        (11, "Architect"),
        (16, "Principal"),
        (21, "Data Lord"),
        (26, "Chief Data Officer"),
    ],
)
