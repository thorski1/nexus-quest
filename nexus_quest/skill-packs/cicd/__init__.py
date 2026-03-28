"""
CI/CD skill pack — Pipeline Ops
Build, test, deploy — the pipeline never sleeps.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ ___  ___ ___
/ __|_ _|/ __| _ \
| (__ | || (__|  _/
\___|___|\___| |_|
"""

SKILL_PACK = SkillPack(
    id="cicd",
    title="Pipeline Ops",
    subtitle="◈  Build, Test, Deploy — On Repeat  ◈",
    save_file_name="cicd_quest",
    intro_story=INTRO_STORY,
    quit_message="The pipeline pauses. Your stage is saved — the build will resume.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "cicd_fundamentals":           "pipeline_initiate",
        "github_actions":              "workflow_architect",
        "testing_in_pipelines":        "test_sentinel",
        "build_and_artifacts":         "build_engineer",
        "deployment_strategies":       "deploy_strategist",
        "infrastructure_as_code_cicd": "infra_automator",
        "monitoring_and_observability": "observability_ace",
    },
    achievements={
        "pipeline_initiate":   ("Pipeline Initiate", "Understood CI/CD from first commit to production deploy!"),
        "workflow_architect":  ("Workflow Architect", "Mastered GitHub Actions — triggers, jobs, secrets, and matrix builds!"),
        "test_sentinel":      ("Test Sentinel", "Gated the pipeline with unit, integration, and e2e tests!"),
        "build_engineer":     ("Build Engineer", "Built artifacts, cached layers, and shipped Docker images!"),
        "deploy_strategist":  ("Deploy Strategist", "Executed blue-green, canary, and rolling deployments without downtime!"),
        "infra_automator":    ("Infra Automator", "Ran Terraform in pipelines and embraced GitOps!"),
        "observability_ace":  ("Observability Ace", "Wired post-deploy health checks, SLOs, and incident triggers!"),
        "no_hints":           ("Zero Assistance", "Completed a zone without any hints!"),
        "speed_reader":       ("Instant Deploy", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Committer"),
        (6, "Builder"),
        (11, "Deployer"),
        (16, "Pipeline Architect"),
        (21, "Release Commander"),
        (26, "DevOps Master"),
    ],
)
