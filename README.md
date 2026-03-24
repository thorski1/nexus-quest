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

> *"The terminal is not legacy. It's the only honest interface the machine has. Everything else is theater."*

A cyberpunk hacker RPG for the terminal. Six skill domains. One corporation. One truth.

You are **Ghost** — a contract operative hired to extract fraud evidence from NEXUS Corp. The evidence is buried across four infrastructure layers: terminal access, network pivots, tampered git history, containerized services, and a database holding eleven years of records.

**The catch:** there are no exploit kits. No zero-days. Just skills.

---

## What You Learn

| Chapter | Domain | Story |
|---------|--------|-------|
| 1 | **Bash** | Ghost infiltrates a NEXUS workstation |
| 2 | **SSH** | Pivot through seven jump hosts |
| 3 | **Vim** | Edit config files on servers with no GUI |
| 4 | **Git** | Reconstruct a tampered commit history |
| 5 | **Docker** | Audit the container infrastructure |
| 6 | **Postgres** | Extract the primary financial records |

Over **280 challenges** across 49 zones. Each challenge teaches real, production-grade skills — not toy examples.

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

Each challenge teaches one concept through a short **lesson** and then asks you to demonstrate it:

- **Knowledge Check** — type the command or answer
- **Live Challenge** — run an actual command in a sandboxed environment
- **Flag Quiz** — identify the right flag for a command

```
  [h] Hint  (-10 XP)   [s] Skip   [q] Menu
```

Progress is automatically saved. You can resume anytime.

---

## Requirements

- Python 3.10+
- A terminal emulator with Unicode support (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

---

## Credits

Built on [Quest Engine](https://github.com/thorski1/quest-engine) — a generic terminal RPG framework.

Narrative style inspired by Neal Stephenson's cyberpunk fiction.
