"""
web_dev skill pack — Web Forge
A cyberpunk RPG for learning web development.
The web is the world's platform. Build it right.
"""

import sys
from pathlib import Path

# Make engine importable from within skill pack if needed
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
    ACHIEVEMENT_DESCRIPTIONS,
)
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="web_dev",
    title="Web Forge",
    subtitle="◈  Build the Web Right  ◈",
    save_file_name="web_dev_quest",
    intro_story=INTRO_STORY,
    quit_message="The browser tab closes... but the DOM is still there.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "html_fundamentals": "markup_master",
        "css_modern":        "style_architect",
        "javascript_core":   "script_engineer",
        "react_essentials":  "component_smith",
        "nextjs":            "next_navigator",
        "web_performance":   "speed_specialist",
        "web_security":      "security_sentinel",
        "deployment":        "deploy_commander",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 _    _ _____ ____    _____ ___  ____   ____ _____
| |  | | ____| __ )  |  ___/ _ \|  _ \ / ___| ____|
| |  | |  _| |  _ \  | |_ | | | | |_) | |  _|  _|
| |/\| | |___| |_) | |  _|| |_| |  _ <| |_| | |___
|__/\__|_____|____/  |_|   \___/|_| \_\\____|_____|
""",
    level_titles=[
        (1,  "div"),
        (6,  "Component"),
        (11, "Full Stack"),
        (16, "Architect"),
        (21, "Framework Author"),
        (26, "Tim Berners-Lee"),
    ],
)
