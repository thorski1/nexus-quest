"""
Platform Engineering skill pack — The Platform Core
IDPs, developer experience, service catalogs, platform APIs, and measuring success.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ _      _ _____ ___ ___  ___ __  __   ___ _  _  ___
| _ \ |    /_\_   _| __/ _ \| _ \  \/  | | __| \| |/ __|
|  _/ |__ / _ \| | | _| (_) |   / |\/| | | _|| .` | (_ |
|_| |____/_/ \_\_| |_| \___/|_|_\_|  |_| |___|_|\_|\___|
"""

SKILL_PACK = SkillPack(
    id="platform_eng",
    title="The Platform Core",
    subtitle="◈  Master the Internal Developer Platform Layer  ◈",
    save_file_name="platform_eng_quest",
    intro_story=INTRO_STORY,
    quit_message="The platform keeps running. Your session token is cached.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "internal_developer_platforms": "portal_architect",
        "developer_experience": "dx_analyst",
        "service_catalogs_and_templates": "template_forger",
        "platform_apis_and_abstractions": "abstraction_engineer",
        "measuring_platform_success": "metrics_auditor",
    },
    achievements={
        "portal_architect": ("Portal Architect", "Mastered IDPs, Backstage, and golden paths!"),
        "dx_analyst": ("DX Analyst", "Decoded developer experience metrics and cognitive load!"),
        "template_forger": ("Template Forger", "Built service catalogs and scaffolding systems!"),
        "abstraction_engineer": ("Abstraction Engineer", "Designed platform APIs with Crossplane and Kratix!"),
        "metrics_auditor": ("Metrics Auditor", "Measured platform success and exposed vanity metrics!"),
        "no_hints": ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader": ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Rookie"),
        (6, "Analyst"),
        (11, "Operator"),
        (16, "Specialist"),
        (21, "Expert"),
        (26, "Specter"),
    ],
)
