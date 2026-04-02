"""
GraphQL skill pack — The Query Nexus
Theme: A rogue GraphQL gateway leaking data through unbounded queries,
       missing auth, and unoptimized resolvers. CIPHER guides you through
       the schema lattice to harden the graph for production.
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
  ____                 _      ___  _
 / ___|_ __ __ _ _ __ | |__  / _ \| |
| |  _| '__/ _` | '_ \| '_ \| | | | |
| |_| | | | (_| | |_) | | | | |_| | |___
 \____|_|  \__,_| .__/|_| |_|\__\_\_____|
                |_|
"""

SKILL_PACK = SkillPack(
    id="graphql",
    title="The Query Nexus",
    subtitle="◈  Harden the Graph. Secure the Schema.  ◈",
    save_file_name="graphql_quest",
    intro_story=INTRO_STORY,
    quit_message="The graph is still live. The resolvers will wait for your return.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "schema_types":           "type_architect",
        "queries_mutations":      "operation_master",
        "resolvers_dataloading":  "resolver_engineer",
        "subscriptions_realtime": "realtime_sentinel",
        "graphql_production":     "production_commander",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Query Runner"),
        (6, "Schema Reader"),
        (11, "Graph Engineer"),
        (16, "Schema Architect"),
        (21, "Nexus Commander"),
        (26, "Nexus Master"),
    ],
)
