"""
Observability skill pack — Signal Corps
Theme: You can't fix what you can't see. The signals are everywhere — learn to read them.
Covers: logs, metrics, traces, alerting, SLOs, distributed tracing, production debugging, cost management.
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
  ___  ___  ___  ___ _____   _____ _____ ___  ___  ___
 / _ \| _ )/ __|| __| _ \ \ / /_ _|_   _/ _ \| _ \/ __|
| (_) | _ \\__ \| _||   /\ V / | |  | || (_) |   /\__ \
 \___/|___/|___/|___|_|_\ \_/ |___| |_| \___/|_|_\|___/
"""

SKILL_PACK = SkillPack(
    id="observability",
    title="Signal Corps",
    subtitle="◈  See Everything. Miss Nothing.  ◈",
    save_file_name="observability_quest",
    intro_story=INTRO_STORY,
    quit_message="The signals are still flowing. Your place in the stream is saved.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "observability_fundamentals": "pillar_keeper",
        "logging":                    "log_architect",
        "metrics_and_monitoring":     "metric_operator",
        "distributed_tracing":        "trace_walker",
        "alerting":                   "alert_surgeon",
        "debugging_production":       "signal_detective",
        "cost_and_scale":             "cost_controller",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Watcher"),
        (6, "Monitor"),
        (11, "Analyst"),
        (16, "Investigator"),
        (21, "Signal Master"),
        (26, "All-Seeing Eye"),
    ],
)
