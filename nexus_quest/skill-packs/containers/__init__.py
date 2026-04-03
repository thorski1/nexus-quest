"""
Containers skill pack — The Container Yard
Theme: Deep container knowledge beyond basic Docker — kernel internals, build
       optimization, registry operations, orchestration alternatives, and
       security hardening. A hardened freight yard inspection narrative.
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
 ___ ___  _  _ _____ _   ___ _  _ ___ ___  ___
/ __/ _ \| \| |_   _/_\ |_ _| \| | __| _ \/ __|
| (_| (_) | .` | | |/ _ \ | || .` | _||   /\__ \
\___\___/|_|\_| |_/_/ \_\___|_|\_|___|_|_\|___/
"""

SKILL_PACK = SkillPack(
    id="containers",
    title="The Container Yard",
    subtitle="◈  Yard Inspector — Every Layer Accounted For  ◈",
    save_file_name="containers_quest",
    intro_story=INTRO_STORY,
    quit_message="The yard is still operational. The manifests will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "container_internals":       "kernel_operative",
        "dockerfile_best_practices": "build_engineer",
        "container_registries":      "registry_warden",
        "orchestration_beyond_k8s":  "dispatch_commander",
        "container_security":        "perimeter_sealed",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Dock Worker"),
        (6, "Inspector"),
        (11, "Supervisor"),
        (16, "Yard Chief"),
        (21, "Master Inspector"),
        (26, "Yard Commander"),
    ],
)
