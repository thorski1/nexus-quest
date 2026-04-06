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
    "networking", "security", "cicd", "observability", "databases", "golang", "api_design", "rust", "system_design", "typescript", "data_engineering", "shell_scripting", "cloud_native", "web_dev", "python_advanced", "dns_http", "ml_engineering", "linux_internals",
    "redis", "testing", "graphql", "microservices", "message_queues", "git_advanced", "auth", "monitoring", "containers", "iac", "sql_advanced", "devsecops", "platform_eng", "sre",
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


def main_networking():
    if _WEB:
        _web("networking")
        return
    check_and_prompt(_PACKAGE)
    run("networking")


def main_security():
    if _WEB:
        _web("security")
        return
    check_and_prompt(_PACKAGE)
    run("security")


def main_cicd():
    if _WEB:
        _web("cicd")
        return
    check_and_prompt(_PACKAGE)
    run("cicd")


def main_observability():
    if _WEB:
        _web("observability")
        return
    check_and_prompt(_PACKAGE)
    run("observability")


def main_databases():
    if _WEB:
        _web("databases")
        return
    check_and_prompt(_PACKAGE)
    run("databases")


def main_golang():
    if _WEB:
        _web("golang")
        return
    check_and_prompt(_PACKAGE)
    run("golang")


def main_api_design():
    if _WEB:
        _web("api_design")
        return
    check_and_prompt(_PACKAGE)
    run("api_design")


def main_rust():
    if _WEB:
        _web("rust")
        return
    check_and_prompt(_PACKAGE)
    run("rust")


def main_system_design():
    if _WEB:
        _web("system_design")
        return
    check_and_prompt(_PACKAGE)
    run("system_design")


def main_typescript():
    if _WEB:
        _web("typescript")
        return
    check_and_prompt(_PACKAGE)
    run("typescript")


def main_data_engineering():
    if _WEB:
        _web("data_engineering")
        return
    check_and_prompt(_PACKAGE)
    run("data_engineering")


def main_shell_scripting():
    if _WEB:
        _web("shell_scripting")
        return
    check_and_prompt(_PACKAGE)
    run("shell_scripting")


def main_cloud_native():
    if _WEB:
        _web("cloud_native")
        return
    check_and_prompt(_PACKAGE)
    run("cloud_native")


def main_web_dev():
    if _WEB:
        _web("web_dev")
        return
    check_and_prompt(_PACKAGE)
    run("web_dev")


def main_python_advanced():
    if _WEB:
        _web("python_advanced")
        return
    check_and_prompt(_PACKAGE)
    run("python_advanced")


def main_dns_http():
    if _WEB:
        _web("dns_http")
        return
    check_and_prompt(_PACKAGE)
    run("dns_http")


def main_ml_engineering():
    if _WEB:
        _web("ml_engineering")
        return
    check_and_prompt(_PACKAGE)
    run("ml_engineering")


def main_linux_internals():
    if _WEB:
        _web("linux_internals")
        return
    check_and_prompt(_PACKAGE)
    run("linux_internals")
