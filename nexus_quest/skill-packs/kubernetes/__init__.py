"""
Kubernetes skill pack — The Cluster
Pods, Services, ConfigMaps, RBAC, Helm, and troubleshooting.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _   ___   _ ___ ___ ___ _  _ ___ _____ ___ ___
| | / / | | | _ ) __| _ \ \| | __|_   _| __/ __|
| |/ /| |_| | _ \ _||   / .` | _|  | | | _|\__ \
|___/  \___/|___/___|_|_\_|\_|___| |_| |___|___/
"""

SKILL_PACK = SkillPack(
    id="kubernetes",
    title="The Cluster",
    subtitle="◈  Navigate the Container Orchestration Layer  ◈",
    save_file_name="kubernetes_quest",
    intro_story=INTRO_STORY,
    quit_message="The cluster keeps running. Your kubeconfig is saved.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "pods_and_deployments": "pod_wrangler",
        "services_and_networking": "mesh_navigator",
        "configmaps_and_secrets": "vault_breaker",
        "namespaces_and_rbac": "access_analyst",
        "helm_charts": "chart_master",
        "persistent_volumes": "storage_archaeologist",
        "resource_management": "quota_architect",
        "network_policies": "firewall_engineer",
        "cluster_troubleshooting": "cluster_forensics",
        "statefulsets_and_daemonsets": "stateful_operator",
        "ingress_and_jobs": "ingress_engineer",
    },
    achievements={
        "pod_wrangler": ("Pod Wrangler", "Mastered pods, deployments, and replica sets!"),
        "mesh_navigator": ("Mesh Navigator", "Mapped cluster networking from ingress to pod!"),
        "vault_breaker": ("Vault Breaker", "Extracted ConfigMaps and Secrets from the cluster!"),
        "access_analyst": ("Access Analyst", "Understood RBAC namespaces and privilege paths!"),
        "chart_master": ("Chart Master", "Read Helm history and found the deployment trail!"),
        "storage_archaeologist": ("Storage Archaeologist", "Recovered the persistent evidence volume!"),
        "quota_architect": ("Quota Architect", "Understood how resources fueled the fraud engine!"),
        "firewall_engineer": ("Firewall Engineer", "Mapped every gap in the cluster network policy!"),
        "cluster_forensics": ("Cluster Forensics", "Recovered evidence from crashed containers!"),
        "stateful_operator": ("Stateful Operator", "Mastered StatefulSets, DaemonSets and ordered pod management!"),
        "ingress_engineer": ("Ingress Engineer", "Routed traffic through Ingress controllers and batch Jobs!"),
        "no_hints": ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader": ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Rookie"),
        (6, "Analyst"),
        (11, "Operator"),
        (16, "Specialist"),
        (21, "Expert"),
        (26, "Specter"),
    ],
)
