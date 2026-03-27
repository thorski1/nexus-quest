"""
Vercel entrypoint for NEXUS Quest web interface.

Vercel routes all HTTP traffic here via vercel.json.
The QUEST_PACK environment variable selects which skill pack to serve
(default: bash). Set it in Vercel's Environment Variables dashboard.

Supported values: bash, ssh, vim, git, docker, postgres, python,
                  regex, linux, kubernetes, aws, terraform
"""

import os
import sys
from pathlib import Path

# Make the repo root importable so nexus_quest/ is available as a package.
_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

# Point the engine at the skill-packs bundled inside nexus_quest/.
# Path(__file__) resolves correctly whether running locally or deployed.
import nexus_quest as _pkg  # noqa: E402  (after sys.path setup)
_PACKS_DIR = str(Path(_pkg.__file__).parent / "skill-packs")
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", _PACKS_DIR)

from engine.skill_pack import load_skill_pack   # noqa: E402
from engine.web.server import create_app        # noqa: E402

_pack_name = os.environ.get("QUEST_PACK", "bash")
_skill_pack = load_skill_pack(_pack_name, packs_dir=_PACKS_DIR)

# `app` is the name Vercel's Python runtime expects to find.
app = create_app(_skill_pack)
