"""
System Design skill pack — Systems Architect
Theme: Build systems that survive anything. Scale to millions. Never go down.
A Systems Architect rebuilding a platform that collapsed under its own success.
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
 ____  _  _  ____  ____  ____  __  __  ____
/ ___)( \/ )/ ___)(_  _)( ___)(  \/  )/ ___)
\___ \ \  / \___ \  )(   )__)  )    ( \___ \
(____/ (__) (____/ (__) (____)(_/\/\_)(____/
    _    ____   ___  _   _  ___  ____  ____   ___  ____
   / \  |  _ \ / __|| | | ||_ _||_  _|| ___| / __||_  _|
  / _ \ | |_) | |   | |_| | | |  | |  | _|  | |    | |
 / ___ \|  _ <| |__ |  _  | | |  | |  | |___| |__  | |
/_/   \_\_| \_\\___||_| |_||___| |_|  |_____|\\___| |_|
"""

SKILL_PACK = SkillPack(
    id="system_design",
    title="Systems Architect",
    subtitle="◈  Build Systems That Scale to Millions  ◈",
    save_file_name="system_design_quest",
    intro_story=INTRO_STORY,
    quit_message="The architecture review is paused. The platform will wait for your return.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "scalability_basics": "scale_master",
        "caching":            "cache_architect",
        "message_queues":     "queue_operator",
        "microservices":      "service_designer",
        "database_at_scale":  "data_engineer",
        "cdn_and_edge":       "edge_deployer",
        "reliability":        "reliability_eng",
        "design_interviews":  "design_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Intern"),
        (6, "Developer"),
        (11, "Senior"),
        (16, "Staff"),
        (21, "Principal"),
        (26, "CTO"),
    ],
)
