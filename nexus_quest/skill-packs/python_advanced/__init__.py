"""Python Advanced skill pack — decorators, generators, metaclasses, async, and more."""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____   _______ _   _  ___  _   _
|  __ \ \ / /_   _| | | |/ _ \| \ | |
| |__) \ V /  | | | |_| | | | |  \| |
|  ___/ | |   | | |  _  | | | | . ` |
| |     | |   | | | | | | |_| | |\  |
|_|     |_|   |_| |_| |_|\___/|_| \_|
"""

SKILL_PACK = SkillPack(
    id="python_advanced",
    title="Python Dark Arts",
    subtitle="◈  Beyond the Basics  ◈",
    save_file_name="python_advanced_quest",
    intro_story=INTRO_STORY,
    quit_message="The interpreter awaits your return.",
    name_prompt="Your callsign, Operator?",
    default_player_name="Pythonista",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "decorators": "decorator_master",
        "generators_iterators": "generator_guru",
        "context_managers": "context_king",
        "metaclasses_descriptors": "meta_wizard",
        "async_python": "async_ace",
        "type_hints": "type_sage",
        "testing_advanced": "test_architect",
        "packaging": "package_publisher",
    },
    achievements={
        "decorator_master": ("Decorator Master", "Mastered function decorators and decorator factories!"),
        "generator_guru": ("Generator Guru", "Unlocked lazy evaluation with generators and itertools!"),
        "context_king": ("Context King", "Conquered context managers and resource management!"),
        "meta_wizard": ("Meta Wizard", "Understood metaclasses and descriptors!"),
        "async_ace": ("Async Ace", "Mastered asyncio and concurrent Python!"),
        "type_sage": ("Type Sage", "Completed Python type hints and Protocol!"),
        "test_architect": ("Test Architect", "Built advanced test suites with pytest!"),
        "package_publisher": ("Package Publisher", "Learned to package and publish Python!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Script"),
        (6, "Module"),
        (11, "Package"),
        (16, "Framework"),
        (21, "Core Dev"),
        (26, "Guido"),
    ],
)
