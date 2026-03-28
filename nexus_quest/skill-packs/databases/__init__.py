"""
Databases skill pack — Data Vaults
Master the storage layer: fundamentals, SQL, NoSQL, design, migrations,
replication, backup, and security.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   _ _____  _     __   ___  _   _ _  _____ ___
 |   \ /_\_   _|/_\    \ \ / /_\| | | | ||_   _/ __|
 | |) / _ \| | / _ \    \ V / _ \ |_| | |__| | \__ \
 |___/_/ \_\_|/_/ \_\    \_/_/ \_\___/|____|_| |___/
"""

SKILL_PACK = SkillPack(
    id="databases",
    title="Data Vaults",
    subtitle="◈  Master the Storage Layer  ◈",
    save_file_name="databases_quest",
    intro_story=INTRO_STORY,
    quit_message="Connection closed. Transaction state saved. Resume when ready.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "database_fundamentals":    "foundation_keeper",
        "sql_mastery":              "query_forger",
        "nosql_world":              "frontier_scout",
        "database_design":          "schema_architect",
        "migrations_and_versioning": "evolution_master",
        "replication_and_scaling":  "grid_commander",
        "backup_and_recovery":      "vault_guardian",
        "database_security":        "cipher_warden",
    },
    achievements={
        "foundation_keeper":  ("Foundation Keeper",  "Mastered relational vs NoSQL, ACID, and CAP theorem trade-offs."),
        "query_forger":       ("Query Forger",       "Forged JOINs, subqueries, indexes, and read execution plans like a language."),
        "frontier_scout":     ("Frontier Scout",     "Navigated MongoDB, Redis, DynamoDB, Cassandra, and graph databases."),
        "schema_architect":   ("Schema Architect",   "Normalized schemas to 3NF, designed ERDs, and enforced referential integrity."),
        "evolution_master":   ("Evolution Master",   "Executed zero-downtime migrations, rollbacks, and expand-and-contract patterns."),
        "grid_commander":     ("Grid Commander",     "Managed replication, sharding, connection pooling, and read/write splitting."),
        "vault_guardian":     ("Vault Guardian",     "Planned backups, executed PITR, and validated RTO/RPO targets."),
        "cipher_warden":      ("Cipher Warden",      "Hardened databases against injection, enforced least privilege, and enabled audit logging."),
        "no_hints":           ("Dark Query",         "Completed a zone without any hints."),
        "speed_reader":       ("Index Scan",         "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Record"),
        (6,  "Index"),
        (11, "DBA"),
        (16, "Architect"),
        (21, "Data Lord"),
        (26, "Oracle"),
    ],
)
