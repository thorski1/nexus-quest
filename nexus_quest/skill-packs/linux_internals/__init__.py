"""
Linux Internals skill pack — Kernel Ops
Theme: Beneath the terminal lies the kernel. Understand the machine.
A kernel operations specialist diagnoses a production failure that lives
below userspace — in processes, memory, filesystems, networking, systemd,
kernel modules, performance tooling, and security layers.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _______ ____  _   _ _____ _       ___  ____  ____
 | |/ / ____|  _ \| \ | | ____| |     / _ \|  _ \/ ___|
 | ' /|  _| | |_) |  \| |  _| | |    | | | | |_) \___ \
 | . \| |___|  _ <| |\  | |___| |___ | |_| |  __/ ___) |
 |_|\_\_____|_| \_\_| \_|_____|_____| \___/|_|   |____/
"""

SKILL_PACK = SkillPack(
    id="linux_internals",
    title="Kernel Ops",
    subtitle="◈  Understand the Machine  ◈",
    save_file_name="linux_internals_quest",
    intro_story=INTRO_STORY,
    quit_message="The kernel is still running. Your session state is saved. Return when ready.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "process_management":   "process_cartographer",
        "memory_management":    "memory_economist",
        "filesystem_internals": "inode_archaeologist",
        "networking_stack":     "packet_tracer",
        "systemd":              "init_forgemaster",
        "kernel_modules":       "module_auditor",
        "performance":          "perf_analyst",
        "security_linux":       "hardened_operator",
    },
    achievements={
        "process_cartographer": ("Process Cartographer", "Mapped the process table — fork, exec, signals, zombies, scheduling. Every process state accounted for."),
        "memory_economist":     ("Memory Economist", "Decoded the memory grid — virtual memory, page faults, swap, OOM killer, cgroup limits. The economy of RAM, understood."),
        "inode_archaeologist":  ("Inode Archaeologist", "Excavated the inode vault — filesystems, /proc, /sys, file descriptors. The kernel's data interface, mastered."),
        "packet_tracer":        ("Packet Tracer", "Traced the socket layer — TCP states, netfilter chains, conntrack, network namespaces. Every packet path mapped."),
        "init_forgemaster":     ("Init Forgemaster", "Mastered the init forge — units, services, timers, socket activation, journal, cgroup slices. PID 1, understood."),
        "module_auditor":       ("Module Auditor", "Audited the module ring — lsmod, modprobe, dmesg, sysctl. The kernel's runtime configuration, inspected."),
        "perf_analyst":         ("Performance Analyst", "Calibrated the performance matrix — load averages, strace, perf, lsof, scheduling. System observability, achieved."),
        "hardened_operator":    ("Hardened Operator", "Secured the hardened layer — SELinux, capabilities, namespaces, seccomp, audit. Every security layer verified."),
        "no_hints":             ("No Hints Needed", "Completed a zone without hints. The kernel speaks to you directly."),
        "speed_reader":         ("Reflex Arc", "Answered a challenge in under 10 seconds. Muscle memory at the kernel level."),
        "streak_3":             ("Pipeline", "3 correct in a row. Knowledge flowing through the stack."),
        "streak_5":             ("Syscall Streak", "5 in a row. Your understanding is traversing the kernel path without fault."),
        "streak_10":            ("RING ZERO", "10 in a row. You operate at kernel privilege. No page faults. No cache misses."),
        "level_10":             ("Junior Specialist", "Level 10. /proc is starting to feel like a second home."),
        "level_20":             ("Senior Specialist", "Level 20. You read dmesg the way others read application logs — fluently."),
        "level_30":             ("Kernel Operations Master", "Maximum level. You understand Linux from process table to hardware. The machine has no secrets from you."),
        "completionist":        ("Full Kernel Audit", "Every zone. Every challenge. Complete kernel operations mastery achieved."),
        "boss_slayer":          ("Root Cause Found", "Beat your first boss challenge. The kernel told you what went wrong."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "User"),
        (6, "Admin"),
        (11, "Kernel"),
        (16, "Root"),
        (21, "Maintainer"),
        (26, "Torvalds"),
    ],
)
