"""
linux skill pack — System Infiltration
A cyberpunk RPG for mastering Linux system administration.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="linux",
    title="System Infiltration",
    subtitle="◈  Own the OS — Own the Mission  ◈",
    save_file_name="linux_quest",
    intro_story=INTRO_STORY,
    quit_message="The session terminates. Your progress is saved. Go dark.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "user_management":     "user_auditor",
        "file_permissions":    "permission_enforcer",
        "process_mastery":     "process_controller",
        "disk_and_storage":    "disk_architect",
        "network_diagnostics": "wire_reader",
        "log_analysis":        "log_analyst",
        "shell_configuration": "shell_hardener",
        "package_management":  "arsenal_keeper",
        "systemd_services":    "daemon_slayer",
        "text_processing":     "text_blade",
        "archive_and_compression": "archive_runner",
        "cron_and_scheduling": "cron_master",
        "bash_scripting_basics": "script_operative",
    },
    achievements={
        "user_auditor":        ("User Auditor",        "Mapped every user, group, and privilege on the system."),
        "permission_enforcer": ("Permission Enforcer", "Read, set, and audited Linux file permissions correctly."),
        "process_controller":  ("Process Controller",  "Identified and managed every running process."),
        "disk_architect":      ("Disk Architect",      "Mapped storage, diagnosed disk usage, and found the hogs."),
        "wire_reader":         ("Wire Reader",          "Diagnosed the network stack from interfaces to open ports."),
        "log_analyst":         ("Log Analyst",          "Read and searched system logs to reconstruct an incident."),
        "shell_hardener":      ("Shell Hardener",       "Audited shell configuration and removed persistence backdoors."),
        "arsenal_keeper":      ("Arsenal Keeper",       "Mastered apt, dpkg, package holds, purges, and orphan cleanup."),
        "daemon_slayer":       ("Daemon Slayer",        "Controlled, masked, and eradicated persistent systemd services."),
        "text_blade":          ("Text Blade",           "Carved evidence from 40 GB of logs using awk, sed, and pipelines."),
        "archive_runner":      ("Archive Runner",       "Bundled, compressed, and transferred the evidence package safely."),
        "cron_master":         ("Cron Master",          "Read, decoded, and disabled the automated fraud jobs."),
        "script_operative":    ("Script Operative",     "Automated the operation with parameterised bash scripts."),
        "no_hints":            ("Dark Mode",            "Completed a zone without any hints."),
        "speed_reader":        ("Signal Flash",         "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=r"""
  _     ___ _   _ _   ___  __
 | |   |_ _| \ | | | | \ \/ /
 | |    | ||  \| | | | |\  /
 | |___ | || |\  | |_| |/  \
 |_____|___|_| \_|\___//_/\_\
""",
    level_titles=[
        (1,  "Rookie"),
        (6,  "Operative"),
        (11, "Shadow"),
        (16, "Ghost"),
        (21, "Phantom"),
        (26, "Specter"),
    ],
)
