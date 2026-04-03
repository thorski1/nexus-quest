"""
Monitoring skill pack — The Watchtower
Theme: The tower sees all. Every metric, every log, every trace — if you know where to look.
Covers: Prometheus, PromQL, Grafana, log management, alerting, on-call, APM, profiling, distributed tracing.
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
 __  __  ___  _  _ ___ _____ ___  ___ ___ _  _  ___
|  \/  |/ _ \| \| |_ _|_   _/ _ \| _ \_ _| \| |/ __|
| |\/| | (_) | .` || |  | || (_) |   /| || .` | (_ |
|_|  |_|\___/|_|\_|___| |_| \___/|_|_\___|_|\_|\___|
"""

SKILL_PACK = SkillPack(
    id="monitoring",
    title="The Watchtower",
    subtitle="◈  The Tower Sees All.  ◈",
    save_file_name="monitoring_quest",
    intro_story=INTRO_STORY,
    quit_message="The signals are still flowing. Your watch is saved.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "prometheus_promql":  "forge_master",
        "grafana_dashboards": "glass_keeper",
        "log_management":     "vault_archivist",
        "alerting_oncall":    "signal_commander",
        "apm_profiling":      "deep_scanner",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Lookout"),
        (6, "Watcher"),
        (11, "Sentinel"),
        (16, "Signal Officer"),
        (21, "Tower Commander"),
        (26, "Tower Keeper"),
    ],
)
