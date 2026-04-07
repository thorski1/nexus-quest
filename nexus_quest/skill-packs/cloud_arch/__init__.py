"""
Cloud Architecture skill pack — The Cloud Citadel
Architecture patterns, multi-cloud, cost optimization, HA, and Well-Architected.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
   _____ _ _            _      _
  / ____(_) |_ __ _  __| | ___| |
 | |    | | __/ _` |/ _` |/ _ \ |
 | |____| | || (_| | (_| |  __/ |
  \_____|_|\__\__,_|\__,_|\___|_|
"""

SKILL_PACK = SkillPack(
    id="cloud_arch",
    title="The Cloud Citadel",
    subtitle="◈  Breach the Multi-Layered Architecture of the Fraud Empire  ◈",
    save_file_name="cloud_arch_quest",
    intro_story=INTRO_STORY,
    quit_message="The citadel session is suspended. Architecture map cached.",
    name_prompt="[bold red]Architect handle:[/bold red]",
    default_player_name="Architect",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "cloud_architecture_patterns": "pattern_analyst",
        "multi_cloud_and_hybrid": "bridge_mapper",
        "cost_optimization": "treasury_auditor",
        "high_availability": "failsafe_breaker",
        "well_architected_framework": "pillar_inspector",
    },
    achievements={
        "pattern_analyst": ("Pattern Analyst", "Decoded every architecture pattern in the citadel!"),
        "bridge_mapper": ("Bridge Mapper", "Mapped the multi-cloud bridge network!"),
        "treasury_auditor": ("Treasury Auditor", "Traced the fraud through the cloud bill!"),
        "failsafe_breaker": ("Failsafe Breaker", "Disarmed the HA evidence-destruction layer!"),
        "pillar_inspector": ("Pillar Inspector", "Completed the five-pillar architecture audit!"),
        "no_hints": ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader": ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Junior Architect"),
        (6, "Solutions Architect"),
        (11, "Senior Architect"),
        (16, "Principal Architect"),
        (21, "Distinguished Architect"),
        (26, "Chief Architect"),
    ],
)
