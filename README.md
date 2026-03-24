# NEXUS Quest

```
 ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
 ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
 ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
 ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
 ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
 ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

 ███████╗██╗██╗     ███████╗███████╗
 ██╔════╝██║██║     ██╔════╝██╔════╝
 █████╗  ██║██║     █████╗  ███████╗
 ██╔══╝  ██║██║     ██╔══╝  ╚════██║
 ██║     ██║███████╗███████╗███████║
 ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝
```

> *"The terminal is not legacy. It is the only honest interface the machine has.*
> *Everything else is theater."*

---

You wake up with a contract on your screen. No client name. No callback address. Just:

```
NEXUS CORP MAINFRAME  //  INTERNAL FRAUD SUSPECTED
EVIDENCE BURIED ACROSS 4 INFRASTRUCTURE LAYERS
EXTRACT BEFORE THE MORNING ROTATION
    — ANONYMOUS
```

You are **Ghost** — a contract operative with one rule: no exploit kits. No zero-days.
Just your terminal, your knowledge, and six layers of systems between you and the truth.

**The catch:** every skill you need, you have to learn for real.

---

## What You'll Learn

| Chapter | Domain | The Mission |
|---------|--------|-------------|
| 1 | **Bash** | Ghost infiltrates a NEXUS workstation |
| 2 | **SSH** | Pivot through seven jump hosts to reach the inner network |
| 3 | **Vim** | Edit config files on servers with no GUI, no undo history |
| 4 | **Git** | Reconstruct eleven months of tampered commit history |
| 5 | **Docker** | Audit the containerized infrastructure for hidden processes |
| 6 | **Postgres** | Extract the primary financial records from the database |

**280+ challenges** across 52 zones. Real commands. Real syntax. Real production skills.

---

## Install

### Mac / Linux

```bash
curl -sSL https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.sh | bash
```

Then run:
```bash
nexus-quest
```

### Windows

Open **PowerShell** as Administrator and run:
```powershell
irm https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.ps1 | iex
```

Then run:
```
nexus-quest
```

### Manual Install

Requires Python 3.10+ and git.

```bash
git clone https://github.com/thorski1/quest-engine ~/.local/share/quest-engine
git clone https://github.com/thorski1/nexus-quest ~/.local/share/nexus-quest

pip install -e ~/.local/share/quest-engine
pip install -e ~/.local/share/nexus-quest
```

---

## Running

| Command | Description |
|---------|-------------|
| `nexus-quest` | Full 6-chapter campaign |
| `terminal-quest` | Bash chapter standalone |
| `ssh-quest` | SSH chapter standalone |
| `vim-quest` | Vim chapter standalone |
| `git-quest` | Git chapter standalone |
| `docker-quest` | Docker chapter standalone |
| `postgres-quest` | Postgres chapter standalone |

---

## Gameplay

Each challenge teaches one concept through a short **lesson**, then asks you to demonstrate it:

- **Knowledge Check** — type the command or answer
- **Live Challenge** — identify the right command for a real scenario
- **Flag Quiz** — identify the correct flag or option

```
  [h] Hint  (-10 XP)   [s] Skip   [q] Menu
```

Progress saves automatically. Resume any time. The evidence doesn't expire.

---

## Requirements

- Python 3.10+
- A terminal emulator with Unicode support (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — a generic terminal RPG framework.

Narrative style inspired by Neal Stephenson's cyberpunk fiction.
