"""
story.py — Narrative for System Infiltration (linux skill pack).
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — TIER 3 ACCESS GAINED[/bold red]

The evidence package is built. The pattern filter is defeated.
But before you can deliver anything, you hit a wall.

The drop site runs on a hardened Linux server — and NEXUS has locked down every
obvious entry point. No web interface. No API. Just SSH on port 22 and a
system that doesn't trust you yet.

CIPHER's voice, quieter than usual: [bold cyan]"The system has seventeen users,
forty-three running services, and no one's audited the sudoers file in eight months."[/bold cyan]

You pull up the terminal. The login prompt blinks.

[bold white]"So we own the OS."[/bold white]

[bold cyan]"If you know Linux well enough to own it — yes.
User management. Permissions. Processes. Disk layout. The network stack.
Shell configuration. The full stack of a real production server."[/bold cyan]

A pause. Then: [bold cyan]"The investigator is waiting. The clock is running.
Learn the system. Own the system. Get the evidence out."[/bold cyan]

[italic]root@nexus-srv-07:~# _[/italic]
"""

ZONE_INTROS = {
    "user_management": (
        "[bold cyan]ZONE 1 — USER MANAGEMENT[/bold cyan]\n\n"
        "[bold white]'First rule: know who exists on this system. "
        "Who can log in. Who has sudo. Who shouldn't be here. "
        "useradd, userdel, id, whoami, groups — the user layer is your starting point.'[/bold white]"
    ),
    "file_permissions": (
        "[bold cyan]ZONE 2 — FILE PERMISSIONS[/bold cyan]\n\n"
        "[bold white]'Every file on this server has an owner, a group, and three sets of rwx bits. "
        "chmod, chown, umask — these determine who can touch what. "
        "A misconfigured permission is often the gap between a contained breach and a full compromise.'[/bold white]"
    ),
    "process_mastery": (
        "[bold cyan]ZONE 3 — PROCESS MASTERY[/bold cyan]\n\n"
        "[bold white]'Seventeen services running. You need to know which ones are expected "
        "and which ones shouldn't be there. ps, kill, systemctl, nice — "
        "the process table is a map of what this system is actually doing.'[/bold white]"
    ),
    "disk_and_storage": (
        "[bold cyan]ZONE 4 — DISK AND STORAGE[/bold cyan]\n\n"
        "[bold white]'The evidence archive is 4.2GB. Before you write it anywhere, "
        "you need to know what disk space is available and where. "
        "df, du, mount, lsblk — the storage layer is where data actually lives.'[/bold white]"
    ),
    "network_diagnostics": (
        "[bold cyan]ZONE 5 — NETWORK DIAGNOSTICS[/bold cyan]\n\n"
        "[bold white]'The drop site is somewhere on the network. To reach it, you need to understand "
        "the network stack. ip addr, ss, ping, nmap — "
        "map the wire before you trust it.'[/bold white]"
    ),
    "log_analysis": (
        "[bold cyan]ZONE 6 — LOG ANALYSIS[/bold cyan]\n\n"
        "[bold white]'Every action on this server is recorded somewhere. "
        "journalctl, tail -f, grep through /var/log — "
        "the logs tell you what happened, when, and who. "
        "They also tell you if anyone has noticed you.'[/bold white]"
    ),
    "shell_configuration": (
        "[bold cyan]ZONE 7 — SHELL CONFIGURATION[/bold cyan]\n\n"
        "[bold white]'.bashrc, PATH, aliases, environment variables — "
        "these are where persistence lives. Where operatives leave backdoors. "
        "Where misconfigurations accumulate for years. "
        "Audit them. Understand them. Control them.'[/bold white]"
    ),
    "package_management": (
        "[bold cyan]ZONE 8 — PACKAGE MANAGEMENT[/bold cyan]\n\n"
        "[bold white]'NEXUS got in through a poisoned package. An unofficial repo. "
        "A dependency no one audited. "
        "If you don't control what's installed on your system, "
        "someone else will use that gap against you. "
        "apt. dpkg. holds. purges. Know your arsenal.'[/bold white]"
    ),
    "systemd_services": (
        "[bold cyan]ZONE 9 — SYSTEMD SERVICES[/bold cyan]\n\n"
        "[bold white]'The NEXUS agent is registered as a systemd service — "
        "Restart=always, enabled on boot, hiding as a name that looks legitimate. "
        "Stopping it isn't enough. You need to mask it. Kill it at the source. "
        "Learn systemd. Then own it.'[/bold white]"
    ),
    "text_processing": (
        "[bold cyan]◈  TEXT PROCESSING  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: '40 GB of access logs. The evidence is in there — every"
        " fraudulent transfer request, timestamped, source IP attached."
        " But you can't read 40 GB by eye. awk, sed, cut, sort, uniq —"
        " chain them. The shell is your scalpel.'[/bold white]"
    ),
    "archive_and_compression": (
        "[bold cyan]◈  ARCHIVE AND COMPRESSION  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The evidence package needs to leave this server."
        " But it's 2 GB of logs, configs, and state files."
        " Compress it. Bundle it. Transfer it securely."
        " tar, gzip, rsync — the tools that move the truth.'[/bold white]"
    ),
    "cron_and_scheduling": (
        "[bold cyan]◈  CRON AND SCHEDULING  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The automated jobs ran on schedule. Every month,"
        " first of the month, 2 AM — fund movement, log rotation, trace cleanup."
        " Their automation is still running. You need to read it, understand it,"
        " and shut it down before the next cycle fires.'[/bold white]"
    ),
    "bash_scripting_basics": (
        "[bold cyan]◈  BASH SCRIPTING  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Manual commands won't cut it at this scale."
        " You need scripts — reusable, parameterised, resilient to errors."
        " Shebang, variables, conditionals, loops, exit codes."
        " Automate the evidence collection. Own the shell.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "user_management": (
        "[bold green]ZONE CLEAR — USER MANAGEMENT[/bold green]\n\n"
        "You know every user on the system, every group, and every sudo privilege. "
        "The privilege map is complete. CIPHER marks the module clear."
    ),
    "file_permissions": (
        "[bold green]ZONE CLEAR — FILE PERMISSIONS[/bold green]\n\n"
        "The permission matrix is locked down. You can read, set, and audit "
        "ownership and access for every critical file on the system."
    ),
    "process_mastery": (
        "[bold green]ZONE CLEAR — PROCESS MASTERY[/bold green]\n\n"
        "Every running process identified. Rogue services terminated. "
        "The expected services confirmed running and enabled."
    ),
    "disk_and_storage": (
        "[bold green]ZONE CLEAR — DISK AND STORAGE[/bold green]\n\n"
        "Disk space confirmed, large directories mapped, mount points documented. "
        "The archive has a home."
    ),
    "network_diagnostics": (
        "[bold green]ZONE CLEAR — NETWORK DIAGNOSTICS[/bold green]\n\n"
        "The network path to the drop site is clear. Open ports confirmed, "
        "no unexpected listeners, route traced and verified."
    ),
    "log_analysis": (
        "[bold green]ZONE CLEAR — LOG ANALYSIS[/bold green]\n\n"
        "The logs have been read. No alerts triggered, no anomalies flagged. "
        "The activity trail looks clean."
    ),
    "shell_configuration": (
        "[bold green]ZONE CLEAR — SHELL CONFIGURATION[/bold green]\n\n"
        "Profile files audited. No backdoors found. PATH sanitized. "
        "The shell environment is under your control."
    ),
    "package_management": (
        "[bold green]ZONE CLEAR — PACKAGE MANAGEMENT[/bold green]\n\n"
        "apt, dpkg, holds, purges, orphan cleanup — the arsenal is under control. "
        "CIPHER: 'You just closed the vector NEXUS used to get in. Good.'"
    ),
    "systemd_services": (
        "[bold green]ZONE CLEAR — SYSTEMD SERVICES[/bold green]\n\n"
        "The NEXUS agent service: stopped, disabled, masked, its unit file rewritten. "
        "CIPHER: 'It's not coming back. The Service Grid is ours.'"
    ),
    "text_processing": (
        "[bold green]ZONE CLEAR — TEXT PROCESSING[/bold green]\n\n"
        "The log pipeline is built. 40 GB distilled to 847 lines of relevant entries. "
        "CIPHER: 'Every IP, every timestamp, every fraudulent request — extracted and sorted. "
        "awk and sed just built your case.'"
    ),
    "archive_and_compression": (
        "[bold green]ZONE CLEAR — ARCHIVE AND COMPRESSION[/bold green]\n\n"
        "The evidence package: compressed, checksummed, transferred to the secure drop. "
        "CIPHER: 'rsync completed. The bundle is safe. They can't delete it now.'"
    ),
    "cron_and_scheduling": (
        "[bold green]ZONE CLEAR — CRON AND SCHEDULING[/bold green]\n\n"
        "The automated jobs: catalogued, documented, disabled. "
        "CIPHER: 'The 2 AM cycle won't fire again. Their automation is dark.'"
    ),
    "bash_scripting_basics": (
        "[bold green]ZONE CLEAR — BASH SCRIPTING[/bold green]\n\n"
        "The collection script runs clean — parameterised, error-safe, logged. "
        "CIPHER: 'Automation built. The script runs on every new server we access. "
        "You just multiplied your reach across the whole NEXUS estate.'"
    ),
}

BOSS_INTROS = {
    "user_management": (
        "[bold red]BOSS CHALLENGE — PRIVILEGE ESCALATION AUDIT[/bold red]\n\n"
        "[bold white]'The sudoers file has a misconfiguration. "
        "Identify the correct investigation sequence.'[/bold white]"
    ),
    "file_permissions": (
        "[bold red]BOSS CHALLENGE — SUID BINARY HUNT[/bold red]\n\n"
        "[bold white]'SUID root binaries are the classic escalation vector. "
        "Write the exact command to find them all.'[/bold white]"
    ),
    "process_mastery": (
        "[bold red]BOSS CHALLENGE — ROGUE PROCESS HUNT[/bold red]\n\n"
        "[bold white]'Something is consuming CPU. "
        "Show me the single pipeline that surfaces the top offenders.'[/bold white]"
    ),
    "disk_and_storage": (
        "[bold red]BOSS CHALLENGE — EMERGENCY DISK TRIAGE[/bold red]\n\n"
        "[bold white]'Production is down: no space left on device. "
        "Write the command to find all files larger than 1GB.'[/bold white]"
    ),
    "network_diagnostics": (
        "[bold red]BOSS CHALLENGE — ROGUE SERVICE DETECTION[/bold red]\n\n"
        "[bold white]'Something is listening on an unexpected port. "
        "Write the ss command to expose it.'[/bold white]"
    ),
    "log_analysis": (
        "[bold red]BOSS CHALLENGE — INCIDENT TIMELINE[/bold red]\n\n"
        "[bold white]'A breach occurred. You need all sudo activity from the last 24 hours. "
        "Write the exact command.'[/bold white]"
    ),
    "shell_configuration": (
        "[bold red]BOSS CHALLENGE — PROFILE AUDIT[/bold red]\n\n"
        "[bold white]'Backdoors in shell config are common persistence mechanisms. "
        "Search all /etc profile files for outbound connection attempts.'[/bold white]"
    ),
    "package_management": (
        "[bold red]BOSS CHALLENGE — THE ORPHAN HUNT[/bold red]\n\n"
        "[bold white]'The NEXUS payload is hiding in an orphaned dependency package. "
        "Walk me through the full removal chain: remove, autoremove, autoclean. "
        "Leave nothing behind.'[/bold white]"
    ),
    "systemd_services": (
        "[bold red]BOSS CHALLENGE — DAEMON RELOAD[/bold red]\n\n"
        "[bold white]'You edited the unit file. You removed Restart=always. "
        "But systemd is still running the old definition from cache. "
        "One command. Reload the daemon. Then we restart clean.'[/bold white]"
    ),
    "text_processing": (
        "[bold red]BOSS CHALLENGE — LOG EXTRACTION[/bold red]\n\n"
        "[bold white]CIPHER: 'The evidence is buried in 40 GB of logs. "
        "awk, sed, cut, sort, uniq — chain them in a pipeline. "
        "I need every unique IP that hit endpoint /transfer over the last 90 days. "
        "Build the command. One shot.'[/bold white]"
    ),
    "archive_and_compression": (
        "[bold red]BOSS CHALLENGE — EVIDENCE BUNDLE[/bold red]\n\n"
        "[bold white]CIPHER: 'Package everything. The log extracts, the config files, "
        "the state snapshots. tar with gzip, preserve timestamps, exclude .git dirs. "
        "Then rsync it to the secure drop. One command for each step.'[/bold white]"
    ),
    "cron_and_scheduling": (
        "[bold red]BOSS CHALLENGE — SCHEDULED EXFIL[/bold red]\n\n"
        "[bold white]CIPHER: 'The NEXUS operator ran automated jobs on the first of "
        "every month at 2 AM. Read their crontab entry. Tell me the exact schedule "
        "expression, what it runs, and how to disable it without deleting it.'[/bold white]"
    ),
    "bash_scripting_basics": (
        "[bold red]BOSS CHALLENGE — DEFENSIVE SCRIPT[/bold red]\n\n"
        "[bold white]CIPHER: 'Write the variable assignment that captures the first "
        "script argument into a variable named TARGET. "
        "One line. No spaces around the equals sign. "
        "Get it right — the rest of the script depends on it.'[/bold white]"
    ),
}
