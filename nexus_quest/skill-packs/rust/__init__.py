"""
Rust Forge skill pack — Memory-Safe. Blazing Fast. Fearlessly Concurrent.
Teaches Rust fundamentals through reverse-engineering a zero-overhead
secure systems layer built on ownership, traits, and the borrow checker.
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
 ____  _   _ ____ _____
|  _ \| | | / ___|_   _|
| |_) | | | \___ \ | |
|  _ <| |_| |___) || |
|_| \_\\___/|____/ |_|
"""

SKILL_PACK = SkillPack(
    id="rust",
    title="Rust Forge",
    subtitle="◈  Memory-Safe, Blazing Fast, Fearlessly Concurrent  ◈",
    save_file_name="rust_quest",
    intro_story=INTRO_STORY,
    quit_message="The borrow checker is still watching. The ownership graph is still valid. Resume when ready.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "rust_basics":         "immutable_core",
        "ownership":           "borrow_master",
        "enums_and_matching":  "pattern_decoder",
        "structs_and_traits":  "trait_architect",
        "error_handling":      "error_handler",
        "collections":         "collection_master",
        "concurrency":         "concurrency_fearless",
        "cargo_and_ecosystem": "cargo_navigator",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Rustacean"),
        (6,  "Developer"),
        (11, "Engineer"),
        (16, "Borrow Checker"),
        (21, "Unsafe Master"),
        (26, "Ferris"),
    ],
)
