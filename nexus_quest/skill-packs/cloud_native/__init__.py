"""
Cloud Native skill pack — Born in the Cloud
Twelve-factor apps, containers, service mesh, GitOps, serverless,
advanced Kubernetes, platform engineering, and FinOps.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _    ___  _   _ ___    _  _   _ _____ _____   _____
 / __| |  / _ \| | | |   \  | \| | /_\_   _|_ _\ \ / / __|
| (__| |_| (_) | |_| | |) | | .` |/ _ \| |  | | \ V /| _|
 \___|____\___/ \___/|___/  |_|\_/_/ \_\_| |___| \_/ |___|
"""

SKILL_PACK = SkillPack(
    id="cloud_native",
    title="Cloud Native",
    subtitle="◈  Born in the Cloud, Scaled to the Edge  ◈",
    save_file_name="cloud_native_quest",
    intro_story=INTRO_STORY,
    quit_message="The mesh keeps routing. Your platform credentials are cached.",
    name_prompt="[bold cyan]Operative handle:[/bold cyan]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "twelve_factor": "doctrine_keeper",
        "containers_deep": "image_architect",
        "service_mesh": "mesh_operator",
        "gitops": "reconciliation_agent",
        "serverless": "phantom_invoker",
        "kubernetes_advanced": "deep_cluster_navigator",
        "platform_engineering": "platform_builder",
        "cloud_costs": "finops_auditor",
    },
    achievements={
        "doctrine_keeper":         ("Doctrine Keeper", "Internalized all twelve factors of cloud-native methodology!"),
        "image_architect":         ("Image Architect", "Mastered OCI specs, runtimes, layers, and multi-stage builds!"),
        "mesh_operator":           ("Mesh Operator", "Mapped the service mesh — Envoy, mTLS, traffic rules, and telemetry!"),
        "reconciliation_agent":    ("Reconciliation Agent", "Understood GitOps: ArgoCD, Flux, drift detection, and pull-based deploys!"),
        "phantom_invoker":         ("Phantom Invoker", "Traced the serverless pipeline — cold starts, event triggers, and vanishing functions!"),
        "deep_cluster_navigator":  ("Deep Cluster Navigator", "Navigated CRDs, operators, admission webhooks, and advanced scheduling!"),
        "platform_builder":        ("Platform Builder", "Understood internal developer platforms, Backstage, and golden paths!"),
        "finops_auditor":          ("FinOps Auditor", "Followed the money — reserved instances, spot pricing, and cost allocation!"),
        "no_hints":                ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader":            ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Pod"),
        (6, "Service"),
        (11, "Controller"),
        (16, "Platform"),
        (21, "Cloud Architect"),
        (26, "SRE Master"),
    ],
)
