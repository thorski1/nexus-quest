"""
Terraform skill pack — The Blueprint Layer
Infrastructure as code: provision, version, and destroy the evidence trail.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="terraform",
    title="The Blueprint Layer",
    subtitle="◈  Infrastructure as Code — Build, Destroy, Rebuild the Evidence  ◈",
    save_file_name="terraform_quest",
    intro_story=INTRO_STORY,
    quit_message="Terraform state unlocked. The blueprint is still out there.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hcl_fundamentals":          "hcl_decoder",
        "variables_and_outputs":     "variable_handler",
        "state_management":          "state_analyst",
        "providers_and_registry":    "provider_mapper",
        "resource_lifecycle":        "lifecycle_engineer",
        "modules":                   "module_architect",
        "data_sources":              "data_cartographer",
        "workspaces_and_environments": "workspace_navigator",
        "plan_and_apply_workflow":   "apply_operator",
        "aws_with_terraform":        "cloud_forger",
        "advanced_patterns":         "pattern_master",
    },
    achievements={
        "hcl_decoder":          ("HCL Decoder",          "Cracked the Terraform configuration language!"),
        "variable_handler":     ("Variable Handler",     "Mastered input variables, outputs, and locals!"),
        "state_analyst":        ("State Analyst",        "Read the state file and found the truth!"),
        "provider_mapper":      ("Provider Mapper",      "Configured providers and version constraints!"),
        "lifecycle_engineer":   ("Lifecycle Engineer",   "Controlled resource creation and destruction!"),
        "module_architect":     ("Module Architect",     "Built reusable infrastructure modules!"),
        "data_cartographer":    ("Data Cartographer",    "Queried existing infrastructure with data sources!"),
        "workspace_navigator":  ("Workspace Navigator",  "Isolated environments with workspaces!"),
        "apply_operator":       ("Apply Operator",       "Mastered the plan/apply/destroy workflow!"),
        "cloud_forger":         ("Cloud Forger",         "Provisioned AWS infrastructure with Terraform!"),
        "pattern_master":       ("Pattern Master",       "Wielded for_each, count, and dynamic blocks!"),
        "no_hints":             ("Ghost Protocol",       "Completed a zone without any hints!"),
        "speed_reader":         ("Neural Spike",         "Answered a question in under 10 seconds!"),
    },
    banner_ascii=r"""
 _____                     __
|_   _|__ _ __ _ __ __ _ / _| ___  _ __ _ __ ___
  | |/ _ \ '__| '__/ _` | |_ / _ \| '__| '_ ` _ \
  | |  __/ |  | | | (_| |  _| (_) | |  | | | | | |
  |_|\___|_|  |_|  \__,_|_|  \___/|_|  |_| |_| |_|
""",
    level_titles=[
        (1,  "Rookie"),
        (6,  "Analyst"),
        (11, "Operator"),
        (16, "Specialist"),
        (21, "Expert"),
        (26, "Specter"),
    ],
)
