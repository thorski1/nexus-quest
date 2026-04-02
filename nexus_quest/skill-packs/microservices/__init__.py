"""
Microservices skill pack — The Service Mesh
Theme: A megacorp's fractured monolith has become a distributed mess.
       You're the Service Architect dispatched to decompose, reconnect,
       and harden the mesh before it collapses.
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
 __  __ ___ ___ ___  ___  ___ ___ _____   _____ ___ ___
|  \/  |_ _/ __| _ \/ _ \/ __| __| _ \ \ / /_ _/ __| __|
| |\/| || | (__|   / (_) \__ \ _||   /\ V / | | (__| _|
|_|  |_|___\___|_|_\\___/|___/___|_|_\ \_/ |___\___|___|
"""

SKILL_PACK = SkillPack(
    id="microservices",
    title="The Service Mesh",
    subtitle="◈  Decompose, Connect & Harden Distributed Systems  ◈",
    save_file_name="microservices_quest",
    intro_story=INTRO_STORY,
    quit_message="The mesh is still live. The services will wait for your return.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "microservice_fundamentals": "decomposition_master",
        "communication_patterns":    "signal_architect",
        "service_discovery":         "registry_keeper",
        "data_management":           "consistency_engineer",
        "observability_resilience":  "chaos_forger",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Operator"),
        (6, "Engineer"),
        (11, "Architect"),
        (16, "Principal"),
        (21, "Mesh Sovereign"),
        (26, "Distributed Master"),
    ],
)
