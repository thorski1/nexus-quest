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

from engine.main import run, run_campaign          # noqa: E402  (after env setup)
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "nexus-quest"


def main_nexus():
    check_and_prompt(_PACKAGE)
    run_campaign("nexus")


def main_bash():
    check_and_prompt(_PACKAGE)
    run("bash")


def main_git():
    check_and_prompt(_PACKAGE)
    run("git")


def main_docker():
    check_and_prompt(_PACKAGE)
    run("docker")


def main_postgres():
    check_and_prompt(_PACKAGE)
    run("postgres")


def main_vim():
    check_and_prompt(_PACKAGE)
    run("vim")


def main_ssh():
    check_and_prompt(_PACKAGE)
    run("ssh")


def main_python():
    check_and_prompt(_PACKAGE)
    run("python")


def main_regex():
    check_and_prompt(_PACKAGE)
    run("regex")


def main_linux():
    check_and_prompt(_PACKAGE)
    run("linux")


def main_kubernetes():
    check_and_prompt(_PACKAGE)
    run("kubernetes")


def main_aws():
    check_and_prompt(_PACKAGE)
    run("aws")


def main_terraform():
    check_and_prompt(_PACKAGE)
    run("terraform")
