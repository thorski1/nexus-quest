"""
nexus_quest/main.py — Entry points for The NEXUS Files game.

Sets up the skill-packs and campaigns directories so the quest-engine
framework can locate this game's content, then delegates to the engine.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows (handles box-drawing chars, stars, etc.)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Point the engine at this project's content directories
_HERE = Path(__file__).parent.parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))
os.environ.setdefault("QUEST_CAMPAIGNS_DIR", str(_HERE / "campaigns"))

from engine.main import run, run_campaign  # noqa: E402  (after env setup)


def main_nexus():
    run_campaign("nexus")


def main_bash():
    run("bash")


def main_git():
    run("git")


def main_docker():
    run("docker")


def main_postgres():
    run("postgres")


def main_vim():
    run("vim")


def main_ssh():
    run("ssh")
