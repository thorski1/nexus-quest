"""
The NEXUS Files — overarching campaign for Quest Engine.
Seven chapters. Seven skill domains. One corporation. One truth.

Chapter order:
  1. bash     — Terminal Breach (initial access, filesystem navigation)
  2. ssh      — Network Pivot (lateral movement through jump hosts and tunnels)
  3. vim      — The Editor (deep in the network, files need editing, no GUI)
  4. git      — The Tampered Record (repository with cleaned history)
  5. docker   — Container Infrastructure (how the fraud ran undetected)
  6. postgres — The Archive (primary financial records, the proof)
"""

from engine.campaign import Campaign, ChapterDef
from .story import (
    CAMPAIGN_INTRO,
    CAMPAIGN_FINAL,
    CHAPTER_INTROS,
    CHAPTER_OUTROS,
)

BANNER_ASCII = r"""
 _   _  _______   ___   _ _____
| \ | ||  ___\ \ / / | | /  ___|
|  \| || |__  \ V /| | | \ `--.
| . ` ||  __| /   \| | | |`--. \
| |\  || |___/ /^\ \ |_| /\__/ /
\_| \_/\____/\/   \/\___/\____/

 _____ _   _ _____ _____ _____
|  _  | | | |  ___/  ___|_   _|
| | | | | | | |__ \ `--.  | |
| | | | | | |  __| `--. \ | |
\ \/' / |_| | |___/\__/ / | |
 \_/\_\\___/\____/\____/  \_/
"""

CAMPAIGN = Campaign(
    id="nexus",
    title="THE NEXUS FILES",
    subtitle="◈  Ghost Operative — Bash · SSH · Vim · Git · Docker · Postgres  ◈",
    save_file_name="nexus_files",
    intro_story=CAMPAIGN_INTRO,
    final_story=CAMPAIGN_FINAL,
    quit_message="The operation is suspended. The clock is still running.",
    banner_ascii=BANNER_ASCII,
    entry_summary_prefix="Previously in the operation...",
    campaign_achievements={
        "campaign_complete": ("Ghost Operative", "Complete The NEXUS Files campaign"),
        "all_stars": ("Phantom Grade S", "Earn 3 stars on every chapter"),
    },
    chapters=[
        ChapterDef(
            pack_name="bash",
            title="Terminal Breach",
            intro_bridge=CHAPTER_INTROS["bash"],
            outro_bridge=CHAPTER_OUTROS["bash"],
        ),
        ChapterDef(
            pack_name="ssh",
            title="Network Pivot",
            intro_bridge=CHAPTER_INTROS["ssh"],
            outro_bridge=CHAPTER_OUTROS["ssh"],
        ),
        ChapterDef(
            pack_name="vim",
            title="The Editor",
            intro_bridge=CHAPTER_INTROS["vim"],
            outro_bridge=CHAPTER_OUTROS["vim"],
        ),
        ChapterDef(
            pack_name="git",
            title="The Tampered Record",
            intro_bridge=CHAPTER_INTROS["git"],
            outro_bridge=CHAPTER_OUTROS["git"],
        ),
        ChapterDef(
            pack_name="docker",
            title="Container Infrastructure",
            intro_bridge=CHAPTER_INTROS["docker"],
            outro_bridge=CHAPTER_OUTROS["docker"],
        ),
        ChapterDef(
            pack_name="postgres",
            title="The Archive",
            intro_bridge=CHAPTER_INTROS["postgres"],
            outro_bridge=CHAPTER_OUTROS["postgres"],
        ),
        ChapterDef(
            pack_name="python",
            title="The Automation Layer",
            intro_bridge=CHAPTER_INTROS["python"],
            outro_bridge=CHAPTER_OUTROS["python"],
        ),
        ChapterDef(
            pack_name="regex",
            title="The Signal Analysis",
            intro_bridge=CHAPTER_INTROS["regex"],
            outro_bridge=CHAPTER_OUTROS["regex"],
        ),
        ChapterDef(
            pack_name="linux",
            title="The Operating System",
            intro_bridge=CHAPTER_INTROS["linux"],
            outro_bridge=CHAPTER_OUTROS["linux"],
        ),
        ChapterDef(
            pack_name="kubernetes",
            title="The Cluster",
            intro_bridge=CHAPTER_INTROS["kubernetes"],
            outro_bridge=CHAPTER_OUTROS["kubernetes"],
        ),
        ChapterDef(
            pack_name="aws",
            title="The Cloud Layer",
            intro_bridge=CHAPTER_INTROS["aws"],
            outro_bridge=CHAPTER_OUTROS["aws"],
        ),
    ],
)
