"""
API Design skill pack — API Forge
Theme: API architecture audit — an API Architect redesigning the contracts
       across a compromised corporate microservices mesh.
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
    _    ____ ___   _____ ___  ____   ____ _____
   / \  |  _ \_ _| |  ___/ _ \|  _ \ / ___| ____|
  / _ \ | |_) | |  | |_ | | | | |_) | |  _|  _|
 / ___ \|  __/| |  |  _|| |_| |  _ <| |_| | |___
/_/   \_\_|  |___| |_|   \___/|_| \_\\____|_____|
"""

SKILL_PACK = SkillPack(
    id="api_design",
    title="API Forge",
    subtitle="◈  Design the Contracts Between Systems  ◈",
    save_file_name="api_design_quest",
    intro_story=INTRO_STORY,
    quit_message="The API surface is still live. The contracts will wait for your return.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "rest_fundamentals":   "rest_scholar",
        "url_design":          "path_architect",
        "request_response":    "payload_master",
        "authentication_apis": "auth_sentinel",
        "graphql_basics":      "query_governor",
        "api_documentation":   "spec_keeper",
        "api_testing":         "test_warden",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Consumer"),
        (6, "Developer"),
        (11, "Designer"),
        (16, "Architect"),
        (21, "API Czar"),
        (26, "Gateway Master"),
    ],
)
