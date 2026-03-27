"""
Git Quest skill pack.
Theme: Corporate forensic timeline audit — Timeline Auditor reading tampered history.
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
 _____ _____ _____
|  __ \_   _|_   _|
| |  \/ | |   | |
| | __  | |   | |
| |_\ \_| |_  | |
 \____/\___/  \_/
"""

SKILL_PACK = SkillPack(
    id="git",
    title="Git Quest",
    subtitle="◈  Timeline Auditor — What Does the History Actually Say?  ◈",
    save_file_name="git_quest",
    intro_story=INTRO_STORY,
    quit_message="The repository waits. The reflog doesn't forget.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "origin_vault":       "navigator",
        "staging_area":       "archivist",
        "commit_ledger":      "seeker",
        "branch_matrix":      "pipe_dream",
        "merge_protocol":     "necromancer",
        "rebase_engine":      "warden",
        "remote_network":     "scriptor",
        "recovery_vault":     "networked",
        "forensics_chamber":  "grandmaster",
        "stash_chamber":      "stash_operative",
        "tag_archive":        "tag_archivist",
        "rebase_ops":         "rebase_forge_cleared",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    level_titles=[
        (1, "Rookie"),
        (6, "Operative"),
        (11, "Shadow"),
        (16, "Ghost"),
        (21, "Phantom"),
        (26, "Specter"),
    ],
)
