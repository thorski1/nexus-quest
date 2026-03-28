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

You are **Ghost** — a contract operative with one rule: no exploit kits. No zero-days. Just your terminal, your knowledge, and seventeen layers of systems between you and the truth.

**The catch:** every skill you need, you have to learn for real.

**17 chapters. 1,091 challenges. Real commands. Real syntax. Real production skills.**

`v1.9.1` · Python 3.10+ · MIT License

---

## What You'll Learn

| # | Chapter | Domain | The Mission |
|---|---------|--------|-------------|
| 1 | **Terminal Breach** | Bash | Infiltrate a NEXUS workstation — filesystem, processes, pipelines |
| 2 | **Network Pivot** | SSH | Pivot through seven jump hosts to reach the inner network |
| 3 | **The Editor** | Vim | Edit config files on servers with no GUI, no undo history |
| 4 | **The Tampered Record** | Git | Reconstruct eleven years of tampered commit history |
| 5 | **Container Infrastructure** | Docker | Audit containerized infrastructure for hidden misconfigurations |
| 6 | **The Archive** | Postgres | Extract 417 fraudulent transactions from the primary database |
| 7 | **The Automation Layer** | Python | Script the evidence packager — automate the delivery chain |
| 8 | **The Signal Analysis** | Regex | Defeat the pattern filter between you and the drop site |
| 9 | **The Operating System** | Linux | Own the delivery server — users, permissions, processes, logs |
| 10 | **The Cluster** | Kubernetes | Navigate the container orchestration cluster — pods, RBAC, Helm |
| 11 | **The Cloud Layer** | AWS | Breach the cloud layer — IAM, S3, RDS, Lambda, VPC |
| 12 | **The Blueprint Layer** | Terraform | Provision and destroy infrastructure — the final cover-up |
| 13 | **Network Ops** | Networking | Master the protocols — OSI, TCP/IP, DNS, HTTP, firewalls |
| 14 | **Security Ops** | Security | Defend the digital fortress — CIA triad, encryption, incident response |
| 15 | **Pipeline Ops** | CI/CD | Build, test, deploy — the pipeline never sleeps |
| 16 | **Signal Corps** | Observability | Logs, metrics, traces, alerting, SLOs, production debugging |
| 17 | **Data Vaults** | Databases | Master the storage layer — SQL, NoSQL, design, replication, backup |

---

## Install

### Recommended

```bash
uv tool install nexus-quest
```

> Don't have `uv`? Install it in one line: `curl -LsSf https://astral.sh/uv/install.sh | sh`
>
> `uv tool install` creates an isolated environment — no venv setup, no system Python conflicts.

### Pip

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
nexus-quest          # full campaign — start here
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
| `networking-quest` | Networking |
| `security-quest` | Security |
| `cicd-quest` | CI/CD |
| `observability-quest` | Observability |
| `databases-quest` | Databases |

---

## Play in the Browser

Launch a local web interface — same content, cyberpunk theme, runs at `localhost:8080`:

```bash
nexus-quest --web         # full hub with all 17 chapters
terminal-quest --web      # single chapter
git-quest --web
# any chapter command + --web
```

The web UI opens automatically in your browser. No separate server setup required.

### Features

- Cyberpunk-themed UI with neon green accents and JetBrains Mono
- Sound effects on correct/wrong answers and level-ups
- Confetti celebrations on correct answers
- Keyboard shortcuts (A-D for answers, H for hint, S for skip)
- PWA — installable on mobile and desktop
- Leaderboards and user accounts (when Postgres is configured)

### Deploy on Vercel

Host your own instance:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthorski1%2Fnexus-quest&project-name=nexus-quest&repository-name=nexus-quest)

After deploy, the Bash chapter is live by default. Set `QUEST_PACK` in Vercel environment variables to run a different chapter (`bash`, `git`, `vim`, `docker`, `kubernetes`, `aws`, etc.).

For persistent leaderboards and user accounts, add a `DATABASE_URL` environment variable pointing to a Postgres instance.

---

## Gameplay

Each challenge teaches one concept through a short **lesson**, then asks you to demonstrate it:

- **Knowledge Check** — type the command, flag, or answer
- **Multiple Choice** — A / B / C / D
- **Fill in the Blank** — complete the command or concept
- **Live Challenge** — run a real shell command in a sandbox
- **Sequence** — put the steps in the right order
- **Matching** — pair commands with their descriptions

Controls:

```
[h] Hint   [l] Lesson   [b] Bookmark   [d] Difficulty   [s] Skip   [q] Menu
```

### Features

| Feature | Description |
|---------|-------------|
| **Daily Challenge** | One challenge per day with 2x XP bonus and streak tracking |
| **Difficulty Modes** | Easy (0.75x XP, free hints) / Normal / Hard (1.5x XP) |
| **Speed Records** | Per-challenge personal bests — new records flash on screen |
| **Bookmarks** | Flag any challenge for later review |
| **Zone Preview** | See challenge list before entering a zone |
| **Completion Certificate** | ASCII grade art (S/A/B/C/D) on campaign complete |
| **Star Ratings** | Zones rated 1-3 stars based on hints and skips used |
| **XP & Levels** | Rookie > Operative > Shadow > Ghost > Phantom > Specter |
| **Adaptive Difficulty** | Engine adjusts based on your performance |
| **Web Mode** | Full browser UI — cyberpunk theme, sound effects, PWA |
| **Leaderboards** | Global rankings when Postgres is configured |
| **User Accounts** | Signup/login for cross-device progress with Postgres |
| **Auto-Updates** | Checks for new versions at startup |

Progress saves automatically to `~/.quest_engine/`. Resume any time.

---

## Who Is This For?

- **Junior developers** learning the command line for the first time
- **Bootcamp students** who need hands-on practice with real tools
- **Senior engineers** filling gaps in Kubernetes, Terraform, or AWS
- **Anyone studying for certifications** — AWS, CKA, Terraform Associate
- **Teams** who want a fun onboarding tool for infrastructure skills

No prior terminal experience required. The placement quiz at the start finds the right chapter for you.

---

## Requirements

- Python 3.10+
- A terminal emulator (Terminal.app, iTerm2, Windows Terminal)
- Any modern browser for web mode
- 80+ column width recommended for the terminal UI

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — an open-source pluggable terminal + web RPG framework.

Narrative style inspired by Neal Stephenson's cyberpunk fiction.

---

## License

MIT
