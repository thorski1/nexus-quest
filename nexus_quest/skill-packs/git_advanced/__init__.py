"""
Git Advanced: The Version Vault skill pack.
Theme: CIPHER cyberpunk — a rogue AI (REWRITER) has corrupted NEXUS Corp's
version control infrastructure. You're the vault operator restoring order.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _   _ ___ ___  ___ ___ ___  _  _
| | | | __| _ \/ __|_ _/ _ \| \| |
| |_| | _||   /\__ \| | (_) | .` |
 \___/|___|_|_\|___/___\___/|_|\_|
       __   ___   _   _ _  _____
       \ \ / /_\ | | | | ||_   _|
        \ V / _ \| |_| | |__| |
         \_/_/ \_\\___/|____|_|
"""

SKILL_PACK = SkillPack(
    id="git_advanced",
    title="The Version Vault",
    subtitle="◈  Vault Operator — Restore the Corrupted History  ◈",
    save_file_name="git_advanced_quest",
    intro_story=INTRO_STORY,
    quit_message="The Vault persists. REWRITER adapts. Resume before the reflog expires.",
    name_prompt="[bold red]Operator handle:[/bold red]",
    default_player_name="Operator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "rebase_history":       "rebase_restorer",
        "cherry_pick_bisect":   "bisect_tracer",
        "worktrees_submodules": "worktree_architect",
        "git_internals":        "object_auditor",
        "advanced_workflows":   "workflow_sentinel",
    },
    achievements={
        "rebase_restorer":    ("History Restored",     "Cleared Rebase & History Rewriting. Interactive rebase is your instrument, not REWRITER's."),
        "bisect_tracer":      ("Bisect Tracer",        "Cleared Cherry-Pick & Bisect. Binary search found the injection point in 12 steps."),
        "worktree_architect": ("Worktree Architect",   "Cleared Worktrees & Submodules. Parallel analysis, verified dependencies, no context lost."),
        "object_auditor":     ("Object Auditor",       "Cleared Git Internals. Blobs, trees, commits, packfiles — the machine room has no secrets from you."),
        "workflow_sentinel":  ("Workflow Sentinel",    "Cleared Advanced Workflows. Hooks, CODEOWNERS, signed commits — the defenses are built."),
        "no_hints":           ("Unassisted Recovery",  "Cleared a zone without hints. The plumbing commands are in muscle memory."),
        "speed_reader":       ("Reflex Operator",      "Answered a challenge in under 10 seconds."),
        "streak_3":           ("Clean Rebase",         "3 correct in a row. Your history rewriting is precise."),
        "streak_5":           ("Bisect Streak",        "5 in a row. Binary search has nothing on your accuracy."),
        "streak_10":          ("VAULT MASTER",         "10 in a row. REWRITER cannot keep up with your command of git internals."),
        "completionist":      ("Vault Sealed",         "Every zone. Every challenge. The Version Vault is fully restored and defended."),
        "boss_slayer":        ("REWRITER Defeated",    "Beat your first boss challenge. REWRITER's corruption couldn't survive contact with your expertise."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Intern"),
        (6,  "Operator"),
        (11, "Specialist"),
        (16, "Architect"),
        (21, "Vault Master"),
        (26, "Elite"),
    ],
)
