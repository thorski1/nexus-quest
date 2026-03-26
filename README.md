# NEXUS Quest

```
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
Just your terminal, your knowledge, and eight layers of systems between you and the truth.

**The catch:** every skill you need, you have to learn for real.

> **Keywords:** terminal RPG, learn bash, learn git, learn docker, learn vim, learn SQL, learn Python, command line tutorial, hacker game, cyberpunk learning game, DevOps training, terminal game

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

**760+ challenges** across 109+ zones. Real commands. Real syntax. Real production skills.

---

## Install

### The easy way (recommended)

**Mac / Linux:**
```bash
pip install nexus-quest
```

**Windows** — open PowerShell and run:
```powershell
pip install nexus-quest
```

> **If `nexus-quest` is not found after install:** Open a new terminal window. If still missing, run `python -m nexus_quest.main` as a fallback.

> **Best experience on Windows:** Use [Windows Terminal](https://aka.ms/terminal) (free, Microsoft Store). The default `cmd.exe` may display characters incorrectly.

### One-liner installer (no pip? start here)

**Mac / Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.ps1 | iex"
```

Then open a new terminal and run `nexus-quest`.

### Auto-updates

The game checks for updates automatically at startup. When a new version is available you'll see:

```
╭──────────────────────────────╮
│      SOFTWARE UPDATE         │
│                              │
│  Update available!           │
│  Installed : v1.0.0          │
│  Latest    : v1.1.0          │
╰──────────────────────────────╯
  Install update now? [y/N]
```

Type `y` and the game installs the update and restarts itself.

---

## Running

| Command | Description |
|---------|-------------|
| `nexus-quest` | Full 8-chapter campaign — start here |
| `terminal-quest` | Bash chapter — standalone |
| `ssh-quest` | SSH chapter — standalone |
| `vim-quest` | Vim chapter — standalone |
| `git-quest` | Git chapter — standalone |
| `docker-quest` | Docker chapter — standalone |
| `postgres-quest` | Postgres chapter — standalone |
| `python-quest` | Python chapter — standalone |
| `regex-quest` | Pattern Recon — standalone |
| `linux-quest` | System Infiltration — standalone |
| `kubernetes-quest` | Container Orchestration — standalone |
| `aws-quest` | Cloud Layer — standalone |

---

## Gameplay

Each challenge teaches one concept through a short **lesson**, then asks you to demonstrate it:

- **Knowledge Check** — type the command, flag, or answer
- **Live Challenge** — run a real command in a sandboxed environment
- **Flag Quiz** — identify the correct option or syntax
- **Fill in the Blank** — complete the command or concept
- **Matching** — pair commands to their descriptions

```
  [h] Hint  [b] Bookmark  [d] Difficulty  [?] Help  [s] Skip  [q] Menu
```

### Features

| Feature | Description |
|---------|-------------|
| **Daily Challenge** | One challenge per day with 2x XP bonus and streak tracking |
| **Timed Drill** | 5/10/15-minute blitz — wrong answers first, then spaced repetition |
| **Difficulty Modes** | Easy (0.75x XP, free hints) / Normal / Hard (1.5x XP) |
| **Speed Records** | Per-challenge personal bests — new records flash on screen |
| **Bookmarks** | Flag any challenge for later review with `[b]` |
| **Zone Preview** | See challenge list before entering a zone |
| **Completion Certificate** | ASCII grade certificate (S/A/B/C/D) on campaign complete |
| **Star Ratings** | Zones rated 1-3 stars based on hints and skips used |
| **XP & Levels** | Rookie -> Operative -> Shadow -> Ghost -> Phantom -> Specter |

Progress saves automatically. Resume any time.

---

## Requirements

- Python 3.10+
- A terminal emulator (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — a generic terminal RPG framework.

Narrative style inspired by Neal Stephenson's cyberpunk fiction.
