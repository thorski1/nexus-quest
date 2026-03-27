# NEXUS Quest

```
 _   _  _______   ___   _ _____
| \ | ||  ___\ \ / / | | /  ___|
|  \| || |__  \ V /| | | \ `--.
| . ` ||  __| /   \| | | |`--. \
| |\  || |___/ /^\ \ |_| /\__/ /
\_| \_/\____/\/   \/\___/\____/
```

> *"The terminal is not legacy. It is the only honest interface the machine has.*
> *Everything else is theater."*

---

You wake up with a contract on your screen. No client name. No callback address. Just:

```
NEXUS CORP MAINFRAME  //  INTERNAL FRAUD SUSPECTED
EVIDENCE BURIED ACROSS MULTIPLE INFRASTRUCTURE LAYERS
EXTRACT BEFORE THE MORNING ROTATION
    — ANONYMOUS
```

You are **Ghost** — a contract operative with one rule: no exploit kits. No zero-days.
Just your terminal, your knowledge, and twelve layers of systems between you and the truth.

**The catch:** every skill you need, you have to learn for real.

---

## What You'll Learn

| Chapter | Domain | The Mission |
|---------|--------|-------------|
| 1 | **Bash** | Infiltrate a NEXUS workstation — filesystem, processes, pipelines |
| 2 | **SSH** | Pivot through seven jump hosts to reach the inner network |
| 3 | **Vim** | Edit config files on servers with no GUI, no undo history |
| 4 | **Git** | Reconstruct eleven years of tampered commit history |
| 5 | **Docker** | Audit containerized infrastructure for hidden misconfigurations |
| 6 | **Postgres** | Extract 417 fraudulent transactions from the primary database |
| 7 | **Python** | Script the evidence packager — automate the delivery chain |
| 8 | **Regex** | Defeat the pattern filter between you and the drop site |
| 9 | **Linux** | Own the delivery server — users, permissions, processes, logs |
| 10 | **Kubernetes** | Navigate the container orchestration cluster — pods, RBAC, Helm |
| 11 | **AWS** | Breach the cloud layer — IAM, S3, RDS, Lambda, VPC |
| 12 | **Terraform** | Provision and destroy infrastructure — the final cover-up |

**800+ challenges** across 120+ zones. Real commands. Real syntax. Real production skills.

---

## Install

### Recommended

```bash
uv tool install nexus-quest
```

> Don't have `uv`? Install it in one line: `curl -LsSf https://astral.sh/uv/install.sh | sh`
>
> `uv tool install` creates an isolated environment — no venv setup, no system Python conflicts.

### Pip fallback

```bash
pip install nexus-quest
```

> On macOS with system Python, prefer `uv` — `pip install` may fail with an "externally managed environment" error.

### One-liner (no package manager)

```bash
curl -sSL https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.sh | bash
```

---

## Play in the Terminal

```bash
nexus-quest          # full 12-chapter campaign — start here
```

Each chapter is also playable standalone:

| Command | Chapter |
|---------|---------|
| `terminal-quest` | Bash |
| `ssh-quest` | SSH |
| `vim-quest` | Vim |
| `git-quest` | Git |
| `docker-quest` | Docker |
| `postgres-quest` | Postgres |
| `python-quest` | Python |
| `regex-quest` | Regex |
| `linux-quest` | Linux |
| `kubernetes-quest` | Kubernetes |
| `aws-quest` | AWS |
| `terraform-quest` | Terraform |

---

## Play in the Browser

Launch a local web interface for any chapter — same content, cyberpunk theme, runs at `localhost:8080`:

```bash
nexus-quest --web
terminal-quest --web
git-quest --web
# any chapter command + --web
```

The web UI opens automatically in your browser. No separate server setup required.

### Host on Vercel

Deploy your own instance:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthorski1%2Fnexus-quest&project-name=nexus-quest&repository-name=nexus-quest)

After deploy, the Bash chapter is live. Set `QUEST_PACK` in Vercel environment variables to run a different chapter (`bash`, `git`, `vim`, etc.).

> Game progress is per browser session on hosted instances. For persistent save files, run locally.

---

## Gameplay

Each challenge teaches one concept through a short **lesson**, then asks you to demonstrate it:

- **Knowledge Check** — type the command, flag, or answer
- **Multiple Choice** — A / B / C / D
- **Fill in the Blank** — complete the command or concept
- **Live Challenge** — run a real shell command in a sandbox
- **Sequence** — put the steps in the right order

Controls:

```
[h] Hint   [l] Lesson   [b] Bookmark   [d] Difficulty   [s] Skip   [q] Menu
```

### Features

| Feature | Description |
|---------|-------------|
| **Daily Challenge** | One challenge per day with 2× XP bonus and streak tracking |
| **Difficulty Modes** | Easy (0.75× XP, free hints) · Normal · Hard (1.5× XP) |
| **Speed Records** | Per-challenge personal bests — new records flash on screen |
| **Bookmarks** | Flag any challenge for later review |
| **Zone Preview** | See challenge list before entering a zone |
| **Completion Certificate** | ASCII grade art (S/A/B/C/D) on campaign complete |
| **Star Ratings** | Zones rated 1–3 stars based on hints and skips used |
| **XP & Levels** | Rookie → Operative → Shadow → Ghost → Phantom → Specter |
| **Web Mode** | Full browser UI — cyberpunk theme, same content and XP system |
| **Auto-Updates** | Checks for new versions at startup |

Progress saves automatically to `~/.quest_engine/`. Resume any time.

---

## Requirements

- Python 3.10+
- A terminal emulator (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended for the terminal UI

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — an open-source pluggable terminal RPG framework.

Narrative style inspired by Neal Stephenson's cyberpunk fiction.
