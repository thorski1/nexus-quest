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

# Point the engine at this project's content directories.
# _HERE is the nexus_quest/ package directory — works both in development
# (repo/nexus_quest/) and when installed via uv/pip (site-packages/nexus_quest/).
_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))
os.environ.setdefault("QUEST_CAMPAIGNS_DIR", str(_HERE / "campaigns"))

from engine.main import run, run_campaign          # noqa: E402  (after env setup)
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "nexus-quest"
_PACKS_DIR = str(_HERE / "skill-packs")   # nexus_quest/skill-packs/

_WEB = "--web" in sys.argv

NEXUS_PACKS = [
    "bash", "ssh", "vim", "git", "docker", "postgres",
    "python", "regex", "linux", "kubernetes", "aws", "terraform",
]


def _web(pack_name: str, port: int = 8080):
    """Launch the web interface for *pack_name*."""
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_nexus():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(NEXUS_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("nexus")


def main_bash():
    if _WEB:
        _web("bash")
        return
    check_and_prompt(_PACKAGE)
    run("bash")


def main_git():
    if _WEB:
        _web("git")
        return
    check_and_prompt(_PACKAGE)
    run("git")


def main_docker():
    if _WEB:
        _web("docker")
        return
    check_and_prompt(_PACKAGE)
    run("docker")


def main_postgres():
    if _WEB:
        _web("postgres")
        return
    check_and_prompt(_PACKAGE)
    run("postgres")


def main_vim():
    if _WEB:
        _web("vim")
        return
    check_and_prompt(_PACKAGE)
    run("vim")


def main_ssh():
    if _WEB:
        _web("ssh")
        return
    check_and_prompt(_PACKAGE)
    run("ssh")


def main_python():
    if _WEB:
        _web("python")
        return
    check_and_prompt(_PACKAGE)
    run("python")


def main_regex():
    if _WEB:
        _web("regex")
        return
    check_and_prompt(_PACKAGE)
    run("regex")


def main_linux():
    if _WEB:
        _web("linux")
        return
    check_and_prompt(_PACKAGE)
    run("linux")


def main_kubernetes():
    if _WEB:
        _web("kubernetes")
        return
    check_and_prompt(_PACKAGE)
    run("kubernetes")


def main_aws():
    if _WEB:
        _web("aws")
        return
    check_and_prompt(_PACKAGE)
    run("aws")


def main_terraform():
    if _WEB:
        _web("terraform")
        return
    check_and_prompt(_PACKAGE)
    run("terraform")
