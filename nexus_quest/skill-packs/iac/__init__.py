"""
IaC skill pack — The Blueprint Engine
Infrastructure as Code: provision, configure, deploy, and secure the evidence trail.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="iac",
    title="The Blueprint Engine",
    subtitle="◈  Infrastructure as Code — Provision, Configure, Deploy, Secure  ◈",
    save_file_name="iac_quest",
    intro_story=INTRO_STORY,
    quit_message="IaC state preserved. The blueprint engine is still running.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "iac_fundamentals":         "foundations_analyst",
        "pulumi_and_cdk":           "programmatic_engineer",
        "ansible_config_mgmt":      "config_operator",
        "gitops_and_argocd":        "gitops_navigator",
        "iac_testing_and_security": "policy_enforcer",
    },
    achievements={
        "foundations_analyst":   ("Foundations Analyst",   "Mastered declarative IaC, idempotency, and drift!"),
        "programmatic_engineer": ("Programmatic Engineer", "Decoded Pulumi and CDK programmatic infrastructure!"),
        "config_operator":      ("Config Operator",       "Mapped Ansible playbooks, roles, and handlers!"),
        "gitops_navigator":     ("GitOps Navigator",      "Traced ArgoCD reconciliation and GitOps pipelines!"),
        "policy_enforcer":      ("Policy Enforcer",       "Cracked OPA, Checkov, and policy-as-code enforcement!"),
        "no_hints":             ("Ghost Protocol",        "Completed a zone without any hints!"),
        "speed_reader":         ("Neural Spike",          "Answered a question in under 10 seconds!"),
    },
    banner_ascii=r"""
 ___       ____
|_ _| __ _/ ___|
 | | / _` | |
 | || (_| | |___
|___|\__,_|\____|
""",
    level_titles=[
        (1,  "Rookie"),
        (6,  "Analyst"),
        (11, "Operator"),
        (16, "Specialist"),
        (21, "Expert"),
        (26, "Specter"),
    ],
    kids_mode=False,
)
