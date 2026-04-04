"""
sql_advanced skill pack - The Query Forge
An advanced SQL cyberpunk RPG for developers who already know the basics.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ _   _ _____    ___  _   _ _____ ______   __
|_   _| | | |  ___|  / _ \| | | |  ___|| ___ \ / /
  | | | |_| | |__   | | | | | | | |__  | |_/ // /
  | | |  _  |  __|  | | | | | | |  __| |    // /
  | | | | | | |___  | |_| | |_| | |___ | |\ \\ \
  \_/ \_| |_\____/   \__\_\\___/\____/ \_| \_|\_\
         _____ ___  ____   ____ _____
        |  ___/ _ \|  _ \ / ___| ____|
        | |_ | | | | |_) | |  _|  _|
        |  _|| |_| |  _ <| |_| | |___
        |_|   \___/|_| \_\\____|_____|
"""

SKILL_PACK = SkillPack(
    id="sql_advanced",
    title="The Query Forge",
    subtitle="◈  Query Architect — Forge the Unplannable Query  ◈",
    save_file_name="sql_advanced_quest",
    intro_story=INTRO_STORY,
    quit_message="The Forge cools... the query plans will wait for your return.",
    name_prompt="[bold red]Architect handle:[/bold red]",
    default_player_name="Architect",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "window_functions":      "window_master",
        "ctes_recursive":        "recursion_architect",
        "query_optimization":    "optimization_engineer",
        "transactions_locking":  "isolation_sentinel",
        "advanced_patterns":     "pattern_forgemaster",
    },
    achievements={
        "window_master":         ("Window Master",          "Cleared the Window Array. ROW_NUMBER, RANK, LAG, LEAD — you analyze without collapsing."),
        "recursion_architect":   ("Recursion Architect",    "Cleared the Recursion Nexus. WITH RECURSIVE traverses any hierarchy, any depth."),
        "optimization_engineer": ("Optimization Engineer",  "Cleared the Optimization Core. EXPLAIN ANALYZE is your native language. Seq Scans fear you."),
        "isolation_sentinel":    ("Isolation Sentinel",     "Cleared the Isolation Chamber. ACID, MVCC, deadlocks — concurrency holds no surprises."),
        "pattern_forgemaster":   ("Pattern Forgemaster",    "Cleared the Pattern Vault. LATERAL, GROUPING SETS, JSONB, full-text — the advanced arsenal is yours."),
        "no_hints":              ("Unassisted Forge",       "Cleared a zone without hints. Pure expertise. No scaffolding."),
        "speed_reader":          ("Reflex Architect",       "Answered a challenge in under 10 seconds."),
        "streak_3":              ("Clean Plan",             "3 correct in a row. Your query plans are precise."),
        "streak_5":              ("Optimization Streak",    "5 in a row. The planner can't keep up with your accuracy."),
        "streak_10":             ("FORGE MASTER",           "10 in a row. You don't write queries. You forge execution plans."),
        "completionist":         ("Forge Complete",         "Every zone. Every challenge. The Query Forge is fully operational."),
        "boss_slayer":           ("Boss Defeated",          "Beat your first boss challenge. The production crisis resolved in milliseconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Apprentice"),
        (6,  "Analyst"),
        (11, "Specialist"),
        (16, "Architect"),
        (21, "Forgemaster"),
        (26, "Elite"),
    ],
)
