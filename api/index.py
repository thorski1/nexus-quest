"""
Vercel entrypoint for NEXUS Quest — serves all 12 chapters via the hub.

Vercel routes all HTTP traffic here via vercel.json.

    /           → Chapter chooser (hub landing page)
    /bash/      → Bash chapter
    /git/       → Git chapter
    /vim/       → Vim chapter
    ... and so on for all 12 chapters.

To serve only a single chapter, set QUEST_PACK in Vercel's Environment
Variables dashboard (e.g. QUEST_PACK=git). Leave unset for the full hub.
"""

import os
import sys
from pathlib import Path

# Make the repo root importable so nexus_quest/ is available as a package.
_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

# Point the engine at the skill-packs bundled inside nexus_quest/.
import nexus_quest as _pkg  # noqa: E402
_PACKS_DIR = str(Path(_pkg.__file__).parent / "skill-packs")
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", _PACKS_DIR)

from engine.skill_pack import load_skill_pack  # noqa: E402

_NEXUS_PACKS = [
    "bash", "ssh", "vim", "git", "docker", "postgres",
    "python", "regex", "linux", "kubernetes", "aws", "terraform",
    "networking", "security", "cicd", "observability", "databases", "golang", "api_design", "rust", "system_design", "typescript", "data_engineering",
]

def _make_app():
    _single_pack = os.environ.get("QUEST_PACK", "")
    if _single_pack:
        # Single-pack mode: serve one chapter at the root.
        from engine.web.server import create_app
        return create_app(load_skill_pack(_single_pack, packs_dir=_PACKS_DIR))
    # Hub mode (default): serve all 12 chapters.
    from engine.web.hub import create_hub_app
    _packs = [load_skill_pack(p, packs_dir=_PACKS_DIR) for p in _NEXUS_PACKS]
    return create_hub_app(_packs)


app = _make_app()
