"""
testing skill pack - The Verification Engine
A cyberpunk RPG for mastering software testing with pytest.
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
 _____ _____ ____ _____ ___ _   _  ____
|_   _| ____/ ___|_   _|_ _| \ | |/ ___|
  | | |  _| \___ \ | |  | ||  \| | |  _
  | | | |___ ___) || |  | || |\  | |_| |
  |_| |_____|____/ |_| |___|_| \_|\____|
"""

SKILL_PACK = SkillPack(
    id="testing",
    title="The Verification Engine",
    subtitle="◈  Ghost Operative — Test the System, Trust the Output  ◈",
    save_file_name="testing_quest",
    intro_story=INTRO_STORY,
    quit_message="The test suite sleeps... but the bugs are still out there.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "unit_testing_fundamentals": "assertion_master",
        "mocking_and_test_doubles":  "isolation_expert",
        "integration_and_e2e":       "boundary_guardian",
        "test_architecture":         "architecture_engineer",
        "tdd_and_testing_culture":   "protocol_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Rookie"),
        (6,  "Tester"),
        (11, "Engineer"),
        (16, "Architect"),
        (21, "Phantom"),
        (26, "Specter"),
    ],
)
