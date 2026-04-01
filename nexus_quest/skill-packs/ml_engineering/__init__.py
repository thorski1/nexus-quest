"""
ML Engineering skill pack — ML Forge
Theme: Train the machines. Deploy the models. Monitor everything.
An ML Engineer rebuilding a megacorp's AI platform from the ground up.
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
 __  __ _       _____ ___  ____   ____ _____
|  \/  | |     |  ___/ _ \|  _ \ / ___| ____|
| |\/| | |     | |_ | | | | |_) | |  _|  _|
| |  | | |___  |  _|| |_| |  _ <| |_| | |___
|_|  |_|_____| |_|   \___/|_| \_\\____|_____|
"""

SKILL_PACK = SkillPack(
    id="ml_engineering",
    title="ML Forge",
    subtitle="◈  Train, Deploy, Monitor  ◈",
    save_file_name="ml_engineering_quest",
    intro_story=INTRO_STORY,
    quit_message="The models are still running. The pipeline will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ml_fundamentals":    "fundamentals_master",
        "model_training":     "training_master",
        "feature_engineering": "feature_master",
        "ml_ops":             "mlops_master",
        "model_serving":      "serving_master",
        "llm_ops":            "llm_master",
        "data_pipelines_ml":  "pipeline_master",
        "responsible_ai":     "ethics_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Intern"),
        (6, "Data Scientist"),
        (11, "ML Engineer"),
        (16, "MLOps Lead"),
        (21, "Research Scientist"),
        (26, "AI Director"),
    ],
)
