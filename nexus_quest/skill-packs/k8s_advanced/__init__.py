"""
Advanced Kubernetes skill pack — The Cluster Depths
CRDs, Operators, Service Mesh, CSI, RBAC deep dive, and cluster operations.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ _  _ ___   ___ _   _   _ ___ _____ ___ ___
|_   _| || | __| / __| | | | | / __|_   _| __| _ \
  | | | __ | _| | (__| |_| |_| \__ \ | | | _||   /
  |_| |_||_|___| \___|_____\___/|___/ |_| |___|_|_\
     ___  ___ ___ _____ _  _ ___
    |   \| __| _ \_   _| || / __|
    | |) | _||  _/ | | | __ \__ \
    |___/|___|_|   |_| |_||_|___/
"""

SKILL_PACK = SkillPack(
    id="k8s_advanced",
    title="The Cluster Depths",
    subtitle="◈  Descend into the Advanced Orchestration Layer  ◈",
    save_file_name="k8s_advanced_quest",
    intro_story=INTRO_STORY,
    quit_message="The cluster depths remain. Your operator credentials are cached.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "custom_resources_operators": "operator_architect",
        "networking_deep_dive": "mesh_infiltrator",
        "storage_statefulsets": "persistence_engineer",
        "security_rbac": "identity_breaker",
        "cluster_operations": "control_plane_master",
    },
    achievements={
        "operator_architect": ("Operator Architect", "Mastered CRDs, controllers, finalizers, and the operator pattern!"),
        "mesh_infiltrator": ("Mesh Infiltrator", "Traced packets through CNI, eBPF, and service mesh encryption!"),
        "persistence_engineer": ("Persistence Engineer", "Understood CSI drivers, StorageClasses, and volume snapshots!"),
        "identity_breaker": ("Identity Breaker", "Navigated RBAC, PSA, secrets encryption, and admission policies!"),
        "control_plane_master": ("Control Plane Master", "Commanded upgrades, etcd backups, node operations, and cost optimization!"),
        "no_hints": ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader": ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Junior SRE"),
        (6, "Platform Engineer"),
        (11, "Senior Operator"),
        (16, "Staff Engineer"),
        (21, "Principal Architect"),
        (26, "Cluster Overlord"),
    ],
)
