"""
zones.py - All zone and challenge data for System Infiltration (linux pack)
"""

ZONES = {
    "user_management": {
        "id": "user_management",
        "name": "The Identity Broker",
        "subtitle": "User Management",
        "color": "cyan",
        "icon": "👤",
        "commands": ["useradd", "userdel", "passwd", "groups", "whoami", "id", "sudo"],
        "challenges": [
            {
                "id": "user_1",
                "type": "quiz",
                "title": "Who Are You",
                "flavor": "The shell is live. Before you touch anything, you need to know who the system thinks you are. One command. No arguments. The identity of the current process.",
                "lesson": (
                    "whoami — prints the username of the currently logged-in user.\n\n"
                    "Syntax: whoami\n\n"
                    "Returns the username associated with the current effective user ID.\n\n"
                    "Example: whoami    → ghost\n\n"
                    "Useful when pivoting between accounts to confirm your current identity."
                ),
                "question": "What command prints the username of the current user?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": ["whoami"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a single word, asking exactly that question.",
                    "Think: 'who am I?'",
                    "The answer is: whoami",
                ],
            },
            {
                "id": "user_2",
                "type": "quiz",
                "title": "Identity Depth Scan",
                "flavor": "whoami tells you the username. But the system tracks more than names — it tracks numeric UIDs, GIDs, supplementary groups. The full picture.",
                "lesson": (
                    "id — displays the user ID (UID), group ID (GID), and supplementary groups for the current or specified user.\n\n"
                    "Syntax: id [username]\n\n"
                    "Output format: uid=1001(ghost) gid=1001(ghost) groups=1001(ghost),27(sudo),4(adm)\n\n"
                    "  uid  — user ID number\n"
                    "  gid  — primary group ID\n"
                    "  groups — all groups the user belongs to\n\n"
                    "Example: id    → uid=0(root) gid=0(root) groups=0(root)"
                ),
                "question": "What command shows your UID, GID, and all group memberships?",
                "answers": ["id"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's two letters.",
                    "Think: identity.",
                    "The answer is: id",
                ],
            },
            {
                "id": "user_3",
                "type": "quiz",
                "title": "Group Audit",
                "flavor": "CIPHER whispers: 'Find out what groups that account belongs to. Group membership is access. Access is everything.'",
                "lesson": (
                    "groups — prints the names of all groups the current or specified user belongs to.\n\n"
                    "Syntax: groups [username]\n\n"
                    "Example: groups ghost    → ghost sudo adm docker\n\n"
                    "Being in the 'sudo' group means the user can run commands as root.\n"
                    "Being in the 'docker' group is effectively root on many systems.\n\n"
                    "Always check group membership when assessing privilege escalation paths."
                ),
                "question": "What command lists all the groups a user belongs to?",
                "answers": ["groups"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The command name is the plural of 'group'.",
                    "Think: groups.",
                    "The answer is: groups",
                ],
            },
            {
                "id": "user_4",
                "type": "fill_blank",
                "title": "Provisioning Cover",
                "flavor": "You need a ghost account on the server. Low-profile. No password yet. The command that creates a user on Linux takes a username as argument.",
                "lesson": (
                    "useradd — creates a new user account.\n\n"
                    "Syntax: useradd [options] username\n\n"
                    "Common options:\n"
                    "  -m   create the user's home directory\n"
                    "  -s   set the user's login shell (e.g. -s /bin/bash)\n"
                    "  -G   add to supplementary groups (e.g. -G sudo,docker)\n"
                    "  -r   create a system account (no home dir, no expiry)\n\n"
                    "Example: useradd -m -s /bin/bash phantom    → creates user 'phantom' with home dir and bash shell"
                ),
                "question": (
                    "Complete the command to create a new user named 'phantom' with a home directory:\n\n"
                    "useradd ___ phantom"
                ),
                "answers": ["-m", "-m -s /bin/bash"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "You need the flag that creates the home directory.",
                    "The flag is -m (for 'make home directory').",
                    "The answer is: -m",
                ],
            },
            {
                "id": "user_5",
                "type": "quiz",
                "title": "Escalation Vector",
                "flavor": "Root access without the root password. The mechanism that lets authorized users execute commands with elevated privileges — the most abused feature in Linux.",
                "lesson": (
                    "sudo — execute a command as another user (typically root).\n\n"
                    "Syntax: sudo [options] command\n\n"
                    "Common options:\n"
                    "  sudo command       run as root\n"
                    "  sudo -u user cmd   run as specific user\n"
                    "  sudo -l            list allowed sudo commands for current user\n"
                    "  sudo -i            start an interactive root shell\n\n"
                    "Requires the user to be in the sudoers file or 'sudo' group.\n\n"
                    "Example: sudo cat /etc/shadow    → read the shadow password file as root"
                ),
                "question": "What command allows a permitted user to execute a command as root?",
                "answers": ["sudo"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'superuser do'.",
                    "Three letters: s-u-d-o.",
                    "The answer is: sudo",
                ],
            },
            {
                "id": "user_boss",
                "type": "fill_blank",
                "title": "BOSS: Account Purge",
                "flavor": "The ghost account served its purpose. Now it needs to disappear — completely. Home directory included. Leave no trace of the phantom user.",
                "lesson": (
                    "userdel — deletes a user account.\n\n"
                    "Syntax: userdel [options] username\n\n"
                    "  userdel username      removes the account but leaves the home directory\n"
                    "  userdel -r username   removes the account AND the home directory and mail spool\n\n"
                    "WARNING: always confirm the correct username before running userdel.\n"
                    "There is no undo.\n\n"
                    "Example: userdel -r phantom    → deletes user 'phantom' and removes /home/phantom"
                ),
                "question": (
                    "Complete the command to delete user 'phantom' AND remove their home directory:\n\n"
                    "userdel ___ phantom"
                ),
                "answers": ["-r"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need the flag that also removes the home directory.",
                    "Think 'remove'.",
                    "The answer is: -r",
                ],
            },
        ],
    },

    "file_permissions": {
        "id": "file_permissions",
        "name": "The Access Grid",
        "subtitle": "File Permissions",
        "color": "yellow",
        "icon": "🔒",
        "commands": ["chmod", "chown", "chgrp", "umask", "ls -l"],
        "challenges": [
            {
                "id": "perm_1",
                "type": "quiz",
                "title": "Read the Grid",
                "flavor": "The file is there. But who can touch it? The permission string is nine characters — three triads. Owner. Group. Others. Read it.",
                "lesson": (
                    "File permissions in Linux are displayed as a 9-character string: rwxrwxrwx\n\n"
                    "Three triads: [owner][group][others]\n"
                    "Each triad has three bits:\n"
                    "  r — read    (4)\n"
                    "  w — write   (2)\n"
                    "  x — execute (1)\n"
                    "  - — permission not set\n\n"
                    "Example: -rw-r--r--\n"
                    "  Owner: rw- (read + write)\n"
                    "  Group: r-- (read only)\n"
                    "  Others: r-- (read only)\n\n"
                    "Use: ls -l to see permissions"
                ),
                "question": "In the permission string '-rwxr-xr--', what can the GROUP do?",
                "url": "https://linuxcommand.org/lc3_lts0090.php",
                "answers": ["read and execute", "r-x", "read, execute", "execute and read"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The group triad is the middle three characters.",
                    "Characters 4-6: r-x",
                    "r=read, x=execute, -=no write. So: read and execute",
                ],
            },
            {
                "id": "perm_2",
                "type": "fill_blank",
                "title": "Symbolic Grant",
                "flavor": "The exploit script won't run without the execute bit. One chmod command. Symbolic mode. Owner only.",
                "lesson": (
                    "chmod symbolic mode — sets permissions using letter notation.\n\n"
                    "Syntax: chmod [who][op][permissions] file\n\n"
                    "  who:  u=user(owner), g=group, o=others, a=all\n"
                    "  op:   +=add, -=remove, ==set exactly\n"
                    "  perm: r=read, w=write, x=execute\n\n"
                    "Examples:\n"
                    "  chmod u+x file    → add execute for owner\n"
                    "  chmod go-w file   → remove write from group and others\n"
                    "  chmod a+r file    → add read for everyone"
                ),
                "question": (
                    "Complete the command to add execute permission for the owner only:\n\n"
                    "chmod ___ exploit.sh"
                ),
                "answers": ["u+x", "+x"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "u = user/owner, + = add, x = execute",
                    "Combine them: u+x",
                    "The answer is: u+x",
                ],
            },
            {
                "id": "perm_3",
                "type": "fill_blank",
                "title": "Octal Lock",
                "flavor": "Credentials file. Owner read-write only. Nothing else. Octal precision.",
                "lesson": (
                    "chmod numeric (octal) mode — sets permissions using a 3-digit number.\n\n"
                    "Each digit: owner, group, others\n"
                    "Each digit is a sum of: 4=read, 2=write, 1=execute\n\n"
                    "  700 = rwx------  (owner full, group none, others none)\n"
                    "  644 = rw-r--r--  (owner rw, group r, others r)\n"
                    "  600 = rw-------  (owner rw only — for private keys and credentials)\n"
                    "  755 = rwxr-xr-x  (standard executable)\n\n"
                    "Example: chmod 600 id_rsa    → SSH private key, owner-read only"
                ),
                "question": (
                    "Complete the command to set the credentials file to owner read+write only (no access for anyone else):\n\n"
                    "chmod ___ creds.txt"
                ),
                "answers": ["600"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Owner: read(4) + write(2) = 6. Group: 0. Others: 0.",
                    "Combine: 600",
                    "The answer is: 600",
                ],
            },
            {
                "id": "perm_4",
                "type": "quiz",
                "title": "Ownership Transfer",
                "flavor": "The file is owned by the wrong account. CIPHER needs it under the service account. One command transfers file ownership.",
                "lesson": (
                    "chown — changes the owner (and optionally group) of a file.\n\n"
                    "Syntax: chown [owner][:group] file\n\n"
                    "Examples:\n"
                    "  chown ghost file.txt        → change owner to 'ghost'\n"
                    "  chown ghost:ops file.txt    → change owner to 'ghost', group to 'ops'\n"
                    "  chown :ops file.txt         → change only the group\n"
                    "  chown -R ghost /var/data    → recursive ownership change\n\n"
                    "Requires root or sudo to change ownership to another user."
                ),
                "question": "What command changes the owner of a file?",
                "answers": ["chown"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'change owner'.",
                    "Five letters: c-h-o-w-n.",
                    "The answer is: chown",
                ],
            },
            {
                "id": "perm_5",
                "type": "quiz",
                "title": "Default Mask",
                "flavor": "Every file created on this server has the wrong default permissions. Before touching anything, understand the mask that shapes them.",
                "lesson": (
                    "umask — sets the default permission mask for newly created files and directories.\n\n"
                    "The umask value is subtracted from the default permissions:\n"
                    "  Files default: 666 (rw-rw-rw-)\n"
                    "  Dirs default:  777 (rwxrwxrwx)\n\n"
                    "  umask 022 → files get 644, dirs get 755 (most common default)\n"
                    "  umask 077 → files get 600, dirs get 700 (private/paranoid)\n"
                    "  umask 002 → files get 664, dirs get 775 (group-collaborative)\n\n"
                    "Syntax: umask [value]    (no value = display current mask)\n\n"
                    "Example: umask 077    → subsequent files are owner-only"
                ),
                "question": "What command sets the default permission mask for newly created files?",
                "answers": ["umask"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's a five-letter command.",
                    "Think 'user mask'.",
                    "The answer is: umask",
                ],
            },
            {
                "id": "perm_boss",
                "type": "fill_blank",
                "title": "BOSS: SUID Escalation",
                "flavor": "The exploit requires SUID on a binary — it runs as its owner (root), not as the caller. Set it. This is the bit the corps' auditors look for and never find in time.",
                "lesson": (
                    "SUID (Set User ID) — special permission bit that causes a file to execute with the privileges of its owner rather than the caller.\n\n"
                    "Syntax:\n"
                    "  chmod u+s file       → set SUID with symbolic notation\n"
                    "  chmod 4755 file      → set SUID with octal (4 = SUID bit, 755 = standard permissions)\n\n"
                    "SUID appears as 's' in the owner's execute position: -rwsr-xr-x\n\n"
                    "If set on a root-owned executable, any user who runs it gets root privileges for that execution.\n\n"
                    "Example: chmod u+s /usr/local/bin/infiltrate    → runs with root privileges regardless of caller"
                ),
                "question": (
                    "Complete the command to set the SUID bit on 'infiltrate' using symbolic notation:\n\n"
                    "chmod ___ infiltrate"
                ),
                "answers": ["u+s", "4755", "u+s,755", "4755"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "SUID is a special permission. Use symbolic: u+s",
                    "Or octal with the SUID prefix: 4755",
                    "The answer is: u+s",
                ],
            },
        ],
    },

    "process_mastery": {
        "id": "process_mastery",
        "name": "The Ghost Stack",
        "subtitle": "Process Management",
        "color": "magenta",
        "icon": "⚙",
        "commands": ["ps", "kill", "killall", "nice", "renice", "jobs", "fg", "bg", "systemctl"],
        "challenges": [
            {
                "id": "proc_1",
                "type": "quiz",
                "title": "Process Census",
                "flavor": "Something is running on this server that shouldn't be. Before you can kill it, you need to see it. Show every process, from every user.",
                "lesson": (
                    "ps aux — displays a snapshot of all currently running processes.\n\n"
                    "Syntax: ps [options]\n\n"
                    "  a — show processes from all users (not just current user)\n"
                    "  u — user-oriented format (shows username, CPU%, MEM%)\n"
                    "  x — include processes not attached to a terminal (daemons)\n\n"
                    "Key columns:\n"
                    "  PID   — Process ID (used to target a process)\n"
                    "  USER  — owner of the process\n"
                    "  %CPU  — CPU usage\n"
                    "  COMMAND — the command that launched the process\n\n"
                    "Example: ps aux | grep nginx    → find the nginx process"
                ),
                "question": "What command shows all running processes from all users in detailed format?",
                "url": "https://man7.org/linux/man-pages/man1/ps.1.html",
                "answers": ["ps aux", "ps -aux", "ps aux"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The base command is 'ps'. The flags show all processes with user info.",
                    "Flags: a (all users), u (user format), x (include daemons).",
                    "The answer is: ps aux",
                ],
            },
            {
                "id": "proc_2",
                "type": "fill_blank",
                "title": "Terminate Signal",
                "flavor": "Process 4821. Running. Should not be. The standard termination signal first — let it clean up. If it refuses, escalation follows.",
                "lesson": (
                    "kill — sends a signal to a process by PID.\n\n"
                    "Syntax: kill [signal] PID\n\n"
                    "Common signals:\n"
                    "  kill PID        → sends SIGTERM (15) — polite termination request\n"
                    "  kill -9 PID     → sends SIGKILL — immediate, unblockable termination\n"
                    "  kill -HUP PID   → sends SIGHUP — reload config (for daemons)\n"
                    "  kill -l         → list all signal names\n\n"
                    "Always try SIGTERM first. Use -9 only if the process ignores it.\n\n"
                    "Example: kill 4821    → send SIGTERM to process 4821"
                ),
                "question": (
                    "Complete the command to send a SIGKILL (force kill) to process 4821:\n\n"
                    "kill ___ 4821"
                ),
                "answers": ["-9", "-SIGKILL", "-KILL"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "SIGKILL is signal number 9.",
                    "The flag is -9.",
                    "The answer is: -9",
                ],
            },
            {
                "id": "proc_3",
                "type": "quiz",
                "title": "Priority Throttle",
                "flavor": "The data extraction process is starving the server. Other processes — the ones the corps are monitoring — are lagging. Adjust the extraction's priority downward.",
                "lesson": (
                    "nice and renice — control process scheduling priority.\n\n"
                    "nice values range from -20 (highest priority) to 19 (lowest priority).\n"
                    "Default nice value is 0.\n\n"
                    "nice — start a process with a modified priority:\n"
                    "  Syntax: nice -n [value] command\n"
                    "  Example: nice -n 10 ./extract.sh    → run with low priority\n\n"
                    "renice — change the priority of a RUNNING process:\n"
                    "  Syntax: renice [value] -p PID\n"
                    "  Example: renice 15 -p 4821    → lower priority of running process\n\n"
                    "Only root can set negative nice values (increase priority)."
                ),
                "question": "What command changes the priority of an already-running process?",
                "answers": ["renice"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It's like 'nice' but for processes already running.",
                    "Think 're-nice'.",
                    "The answer is: renice",
                ],
            },
            {
                "id": "proc_4",
                "type": "quiz",
                "title": "Service Reconnaissance",
                "flavor": "The server runs systemd. CIPHER: 'Check if the NEXUS monitoring daemon is active. If it's running, you have 90 seconds before the next log flush.'",
                "lesson": (
                    "systemctl — controls the systemd system and service manager.\n\n"
                    "Syntax: systemctl [command] [service]\n\n"
                    "Key commands:\n"
                    "  systemctl status service   → show service status (running/stopped/failed)\n"
                    "  systemctl start service    → start a service\n"
                    "  systemctl stop service     → stop a service\n"
                    "  systemctl restart service  → restart a service\n"
                    "  systemctl enable service   → start automatically at boot\n"
                    "  systemctl disable service  → do not start at boot\n"
                    "  systemctl list-units       → list all loaded units\n\n"
                    "Example: systemctl status nexus-monitor    → check if nexus-monitor is running"
                ),
                "question": "What command is used to check the status of a systemd service?",
                "answers": ["systemctl status", "systemctl"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "systemd services are managed with a single command.",
                    "The command is 'systemctl'. Add 'status' and the service name.",
                    "The answer is: systemctl status [service]",
                ],
            },
            {
                "id": "proc_5",
                "type": "fill_blank",
                "title": "Name-Based Purge",
                "flavor": "Multiple instances of the same process. All of them running. Kill them all by name — no need to hunt individual PIDs.",
                "lesson": (
                    "killall — sends a signal to all processes matching a name.\n\n"
                    "Syntax: killall [options] process_name\n\n"
                    "  killall process_name      → SIGTERM all processes with that name\n"
                    "  killall -9 process_name   → SIGKILL all (force kill)\n"
                    "  killall -u username       → kill all processes owned by user\n"
                    "  killall -e process_name   → exact match (vs. partial match)\n\n"
                    "Useful when ps aux shows multiple instances of the same process.\n\n"
                    "Example: killall -9 nexus-agent    → force kill every nexus-agent process"
                ),
                "question": (
                    "Complete the command to force-kill all processes named 'nexus-agent':\n\n"
                    "killall ___ nexus-agent"
                ),
                "answers": ["-9", "-SIGKILL", "-KILL"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Force kill is signal 9.",
                    "The flag is -9.",
                    "The answer is: -9",
                ],
            },
            {
                "id": "proc_boss",
                "type": "fill_blank",
                "title": "BOSS: Service Shutdown",
                "flavor": "The nexus-monitor service is logging your activity. systemctl. Stop it. Now. The window is closing.",
                "lesson": (
                    "systemctl stop — stops a running systemd service immediately.\n\n"
                    "Syntax: systemctl stop service_name\n\n"
                    "Note: 'stop' halts the service for the current session only.\n"
                    "To prevent restart at boot: systemctl disable service_name\n"
                    "To do both at once: systemctl disable --now service_name\n\n"
                    "Requires root/sudo to stop most system services.\n\n"
                    "Example: sudo systemctl stop nexus-monitor    → stops the nexus-monitor service"
                ),
                "question": (
                    "Complete the command to stop the 'nexus-monitor' service:\n\n"
                    "systemctl ___ nexus-monitor"
                ),
                "answers": ["stop"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "The subcommand that halts a service.",
                    "Think: stop.",
                    "The answer is: stop",
                ],
            },
        ],
    },

    "disk_and_storage": {
        "id": "disk_and_storage",
        "name": "The Storage Layer",
        "subtitle": "Disk & Storage",
        "color": "blue",
        "icon": "💾",
        "commands": ["df", "du", "mount", "fdisk", "lsblk", "fstab"],
        "challenges": [
            {
                "id": "disk_1",
                "type": "quiz",
                "title": "Space Audit",
                "flavor": "The exfil requires 40GB. This server may not have it. Before staging anything, check available disk space — in human-readable numbers.",
                "lesson": (
                    "df -h — displays disk space usage for all mounted filesystems in human-readable format.\n\n"
                    "Syntax: df [options] [filesystem]\n\n"
                    "  -h   human-readable sizes (KB, MB, GB)\n"
                    "  -T   show filesystem type\n"
                    "  -i   show inode usage instead of block usage\n\n"
                    "Key columns:\n"
                    "  Filesystem  — device or mount\n"
                    "  Size        — total size\n"
                    "  Used        — space in use\n"
                    "  Avail       — free space\n"
                    "  Use%        — percentage used\n"
                    "  Mounted on  — where it's mounted\n\n"
                    "Example: df -h    → shows all filesystems with human-readable sizes"
                ),
                "question": "What command shows disk space usage for all filesystems in human-readable format?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": ["df -h", "df"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The base command is 'df' (disk free). The flag makes sizes readable.",
                    "Human-readable flag: -h",
                    "The answer is: df -h",
                ],
            },
            {
                "id": "disk_2",
                "type": "fill_blank",
                "title": "Directory Weight",
                "flavor": "The logs directory has grown unchecked for three years. Before you touch it, measure it. Total size. One number.",
                "lesson": (
                    "du -sh — displays the total disk usage of a directory in human-readable summary format.\n\n"
                    "Syntax: du [options] [directory]\n\n"
                    "  -s   summary — show total only (not per-file breakdown)\n"
                    "  -h   human-readable sizes (KB, MB, GB)\n"
                    "  -a   all files (not just directories)\n"
                    "  --max-depth=N   show totals down to N directory levels\n\n"
                    "Examples:\n"
                    "  du -sh /var/log       → total size of /var/log\n"
                    "  du -sh *             → sizes of each item in current dir\n"
                    "  du -h --max-depth=1  → one level deep breakdown"
                ),
                "question": (
                    "Complete the command to show the total size of /var/log in human-readable format:\n\n"
                    "du ___ /var/log"
                ),
                "answers": ["-sh", "-hs", "-s -h", "-h -s"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Two flags: -s for summary, -h for human-readable.",
                    "Combine them: -sh",
                    "The answer is: -sh",
                ],
            },
            {
                "id": "disk_3",
                "type": "quiz",
                "title": "Block Map",
                "flavor": "The server has additional drives. CIPHER: 'Map all block devices first. Know what storage is attached before you mount anything.'",
                "lesson": (
                    "lsblk — lists all block devices (disks, partitions) in a tree format.\n\n"
                    "Syntax: lsblk [options]\n\n"
                    "  -f   show filesystem type and UUID\n"
                    "  -o   specify output columns\n"
                    "  -m   show ownership info\n\n"
                    "Output shows:\n"
                    "  NAME    — device name (sda, sdb, nvme0n1...)\n"
                    "  SIZE    — total size\n"
                    "  TYPE    — disk, part (partition), lvm...\n"
                    "  MOUNTPOINT — where it's mounted (if at all)\n\n"
                    "Example: lsblk    → tree of all disks and partitions"
                ),
                "question": "What command lists all block devices (disks and partitions) in a tree view?",
                "answers": ["lsblk"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It's short for 'list block devices'.",
                    "Five letters: l-s-b-l-k.",
                    "The answer is: lsblk",
                ],
            },
            {
                "id": "disk_4",
                "type": "quiz",
                "title": "Mount Point",
                "flavor": "There's an encrypted drive attached but not mounted. CIPHER: 'You know the device and the target directory. Mount it and the filesystem becomes yours.'",
                "lesson": (
                    "mount — attaches a filesystem to the directory tree.\n\n"
                    "Syntax: mount [options] device mountpoint\n\n"
                    "Examples:\n"
                    "  mount /dev/sdb1 /mnt/data     → mount partition to /mnt/data\n"
                    "  mount -t ext4 /dev/sdb1 /mnt  → specify filesystem type\n"
                    "  mount -o ro /dev/sdb1 /mnt    → mount read-only\n"
                    "  mount                          → show all currently mounted filesystems\n"
                    "  umount /mnt/data               → unmount\n\n"
                    "Persistent mounts survive reboots when configured in /etc/fstab.\n\n"
                    "Example: mount /dev/sdb1 /mnt/exfil    → access sdb1 at /mnt/exfil"
                ),
                "question": "What command attaches a filesystem device to a directory in the filesystem tree?",
                "answers": ["mount"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The command name describes exactly what it does.",
                    "Think: mount.",
                    "The answer is: mount",
                ],
            },
            {
                "id": "disk_5",
                "type": "quiz",
                "title": "Persistence Config",
                "flavor": "The mount won't survive a reboot unless it's configured to persist. The file that governs automatic mounting at boot is a classic Linux config.",
                "lesson": (
                    "/etc/fstab — the filesystem table, defines all persistent mounts.\n\n"
                    "Each line in fstab defines one mount:\n"
                    "  <device> <mountpoint> <type> <options> <dump> <pass>\n\n"
                    "Example:\n"
                    "  /dev/sdb1  /mnt/data  ext4  defaults  0  2\n\n"
                    "Fields:\n"
                    "  device      — /dev/sdX or UUID=... or LABEL=...\n"
                    "  mountpoint  — where to mount\n"
                    "  type        — ext4, xfs, btrfs, nfs, tmpfs...\n"
                    "  options     — defaults, ro, noexec, etc.\n"
                    "  dump        — backup flag (0=no, 1=yes)\n"
                    "  pass        — fsck order at boot (0=skip, 1=root, 2=others)\n\n"
                    "Test fstab without rebooting: mount -a"
                ),
                "question": "What file defines persistent filesystem mounts that survive reboots?",
                "answers": ["/etc/fstab", "fstab", "/etc/fstab"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It lives in /etc.",
                    "Short for 'filesystem table'.",
                    "The answer is: /etc/fstab",
                ],
            },
            {
                "id": "disk_boss",
                "type": "fill_blank",
                "title": "BOSS: Partition Table",
                "flavor": "A new drive arrived. Before formatting, before mounting — read its partition table. The forensic tool that interrogates raw disks.",
                "lesson": (
                    "fdisk -l — lists partition tables for all disks or a specific disk.\n\n"
                    "Syntax: fdisk [options] [device]\n\n"
                    "  fdisk -l            → list partition tables for all disks\n"
                    "  fdisk -l /dev/sdb   → list partitions on /dev/sdb specifically\n"
                    "  fdisk /dev/sdb      → interactive mode to create/delete partitions\n\n"
                    "Output shows:\n"
                    "  Disk size, sector count, partition table type\n"
                    "  Each partition: start/end sector, size, type (Linux, swap, EFI...)\n\n"
                    "Requires root. Read-only listing with -l is safe.\n\n"
                    "Example: fdisk -l /dev/sdb    → show sdb's partition table"
                ),
                "question": (
                    "Complete the command to list the partition table of /dev/sdb:\n\n"
                    "fdisk ___ /dev/sdb"
                ),
                "answers": ["-l"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "The flag for listing (read-only) is -l.",
                    "Think: list.",
                    "The answer is: -l",
                ],
            },
        ],
    },

    "network_diagnostics": {
        "id": "network_diagnostics",
        "name": "The Signal Web",
        "subtitle": "Network Diagnostics",
        "color": "green",
        "icon": "🌐",
        "commands": ["ip addr", "ifconfig", "ping", "ss", "netstat", "traceroute", "nmap"],
        "challenges": [
            {
                "id": "net_1",
                "type": "quiz",
                "title": "Interface Census",
                "flavor": "The operative needs to know the server's own address before making a single outbound connection. Check all network interfaces.",
                "lesson": (
                    "ip addr — displays all network interfaces and their IP addresses.\n\n"
                    "Syntax: ip addr [show [interface]]\n\n"
                    "  ip addr           → list all interfaces\n"
                    "  ip addr show eth0 → show specific interface\n"
                    "  ip link           → show link-layer info (MAC, state)\n"
                    "  ip route          → show routing table\n\n"
                    "The older 'ifconfig' command is deprecated on modern Linux but still common.\n"
                    "Both show: interface name, IP address, subnet mask, state (UP/DOWN)\n\n"
                    "Example: ip addr show    → list all network interfaces with IPs"
                ),
                "question": "What modern command shows all network interfaces and their IP addresses?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": ["ip addr", "ip addr show", "ip address"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The 'ip' command with a subcommand for addresses.",
                    "ip addr",
                    "The answer is: ip addr",
                ],
            },
            {
                "id": "net_2",
                "type": "quiz",
                "title": "Liveness Check",
                "flavor": "Before running anything sophisticated, confirm the target host is alive. One ICMP echo request. If it answers, it's there.",
                "lesson": (
                    "ping — sends ICMP echo requests to test host reachability.\n\n"
                    "Syntax: ping [options] host\n\n"
                    "  ping host           → continuous ping (Ctrl+C to stop)\n"
                    "  ping -c 4 host      → send exactly 4 packets then stop\n"
                    "  ping -i 0.2 host    → send every 0.2 seconds (faster scan)\n"
                    "  ping -t 5 host      → set TTL to 5\n\n"
                    "Output shows:\n"
                    "  bytes, icmp_seq, ttl, time (ms) — the round-trip time\n"
                    "  Packet loss percentage — 0% means fully reachable\n\n"
                    "Example: ping -c 3 192.168.1.1    → 3 pings to the gateway"
                ),
                "question": "What command tests whether a remote host is reachable over the network?",
                "answers": ["ping"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It sends ICMP echo requests.",
                    "Four letters. The same word as the sound.",
                    "The answer is: ping",
                ],
            },
            {
                "id": "net_3",
                "type": "quiz",
                "title": "Socket Survey",
                "flavor": "Something is listening on a port that shouldn't exist. Find every open port and every active connection on this machine.",
                "lesson": (
                    "ss — socket statistics. Lists all network connections and listening ports.\n\n"
                    "Syntax: ss [options]\n\n"
                    "  ss -tuln       → TCP+UDP, listening, numeric (no DNS lookups)\n"
                    "  ss -tulnp      → same + show process name/PID\n"
                    "  ss -s          → summary statistics\n"
                    "  ss -ta         → all TCP connections (established + listening)\n\n"
                    "Flags:\n"
                    "  -t  TCP   -u  UDP   -l  listening only\n"
                    "  -n  numeric   -p  show process\n\n"
                    "ss is the modern replacement for netstat.\n\n"
                    "Example: ss -tulnp    → all listening ports with associated processes"
                ),
                "question": "What command lists all listening ports and active network connections (modern replacement for netstat)?",
                "answers": ["ss", "ss -tulnp", "ss -tuln"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Two letters. Stands for 'socket statistics'.",
                    "It replaced netstat on modern Linux.",
                    "The answer is: ss",
                ],
            },
            {
                "id": "net_4",
                "type": "fill_blank",
                "title": "Route Trace",
                "flavor": "The packet leaves this server and travels through seven hops before it dies. CIPHER needs to know which hop is controlled by NEXUS.",
                "lesson": (
                    "traceroute — traces the path packets take to a destination, hop by hop.\n\n"
                    "Syntax: traceroute [options] host\n\n"
                    "  traceroute host          → trace with UDP probes (default)\n"
                    "  traceroute -I host       → use ICMP instead of UDP\n"
                    "  traceroute -T host       → use TCP SYN probes\n"
                    "  traceroute -n host       → numeric output (no DNS)\n"
                    "  traceroute -m 10 host    → max 10 hops\n\n"
                    "Output: each line is one router hop with RTT times.\n"
                    "A * means the hop didn't respond (common for firewalled routers).\n\n"
                    "Example: traceroute 8.8.8.8    → trace the path to Google's DNS"
                ),
                "question": (
                    "Complete the command to trace the network path to nexus-corp.internal:\n\n"
                    "___ nexus-corp.internal"
                ),
                "answers": ["traceroute", "traceroute -n"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The command literally traces a route.",
                    "Think: traceroute.",
                    "The answer is: traceroute",
                ],
            },
            {
                "id": "net_5",
                "type": "fill_blank",
                "title": "Port Probe",
                "flavor": "The NEXUS server is listening on something. Before connecting, scan it — which ports are open? What services are exposed?",
                "lesson": (
                    "nmap — network mapper. Scans hosts for open ports and services.\n\n"
                    "Syntax: nmap [options] target\n\n"
                    "  nmap -p 22,80,443 host    → scan specific ports\n"
                    "  nmap -p 1-1024 host       → scan port range\n"
                    "  nmap -sV host             → detect service versions\n"
                    "  nmap -O host              → OS detection (requires root)\n"
                    "  nmap -A host              → aggressive scan (version, OS, scripts)\n"
                    "  nmap -sn 192.168.1.0/24   → ping sweep (host discovery, no port scan)\n\n"
                    "Example: nmap -p 22,80,443 nexus-corp.internal    → check three ports"
                ),
                "question": (
                    "Complete the command to scan ports 80 and 443 on the target:\n\n"
                    "nmap ___ 80,443 nexus-corp.internal"
                ),
                "answers": ["-p"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The flag that specifies which ports to scan.",
                    "Think: port. One letter: -p",
                    "The answer is: -p",
                ],
            },
            {
                "id": "net_boss",
                "type": "fill_blank",
                "title": "BOSS: Static Host Injection",
                "flavor": "DNS is monitored. CIPHER: 'Inject a static resolution into /etc/hosts. Redirect the NEXUS internal domain to your proxy. No DNS query ever leaves the machine.'",
                "lesson": (
                    "/etc/hosts — static hostname-to-IP resolution file, checked before DNS.\n\n"
                    "Format: IP_address  hostname  [aliases...]\n\n"
                    "Examples:\n"
                    "  127.0.0.1   localhost\n"
                    "  192.168.1.100  nexus-corp.internal  nexus\n\n"
                    "Entries in /etc/hosts override DNS for that hostname.\n"
                    "Used to:\n"
                    "  - Block domains (point to 127.0.0.1)\n"
                    "  - Redirect traffic (point domain to attacker-controlled IP)\n"
                    "  - Test without DNS propagation\n\n"
                    "Full path: /etc/hosts"
                ),
                "question": (
                    "What file should you edit to add a static hostname-to-IP mapping that bypasses DNS?\n"
                    "(Provide the full path)"
                ),
                "answers": ["/etc/hosts"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's in /etc.",
                    "The plural of 'host'.",
                    "The answer is: /etc/hosts",
                ],
            },
        ],
    },

    "log_analysis": {
        "id": "log_analysis",
        "name": "The Signal Archive",
        "subtitle": "Log Analysis",
        "color": "yellow",
        "icon": "📋",
        "commands": ["journalctl", "tail -f", "grep", "logrotate"],
        "challenges": [
            {
                "id": "log_1",
                "type": "quiz",
                "title": "Live Feed",
                "flavor": "The attack is running. You need to watch the log in real time — see every new line as it appears. Not a snapshot. A stream.",
                "lesson": (
                    "tail -f — follows a file in real time, printing new lines as they are appended.\n\n"
                    "Syntax: tail [options] file\n\n"
                    "  tail -f file         → follow the file live\n"
                    "  tail -n 50 file      → last 50 lines (snapshot)\n"
                    "  tail -F file         → follow even if file is rotated/recreated\n"
                    "  tail -f file1 file2  → follow multiple files simultaneously\n\n"
                    "Ctrl+C to stop following.\n\n"
                    "Example: tail -f /var/log/syslog    → watch system log in real time"
                ),
                "question": "What command follows a log file in real time, printing new lines as they appear?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": ["tail -f", "tail -F"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The base command is 'tail'. The flag makes it follow live.",
                    "Follow flag: -f",
                    "The answer is: tail -f",
                ],
            },
            {
                "id": "log_2",
                "type": "fill_blank",
                "title": "Journal Query",
                "flavor": "This server runs systemd. The logs aren't in a flat file — they're in a binary journal. One command to query them.",
                "lesson": (
                    "journalctl — queries the systemd journal (binary log store).\n\n"
                    "Syntax: journalctl [options]\n\n"
                    "  journalctl                      → all journal entries (oldest first)\n"
                    "  journalctl -f                   → follow live (like tail -f for systemd)\n"
                    "  journalctl -u service_name      → logs for a specific service\n"
                    "  journalctl -n 100               → last 100 lines\n"
                    "  journalctl --since '1 hour ago' → time-filtered\n"
                    "  journalctl -p err               → error-level and above only\n"
                    "  journalctl -b                   → only current boot\n\n"
                    "Example: journalctl -u nexus-monitor -f    → live logs for nexus-monitor service"
                ),
                "question": (
                    "Complete the command to view live journal logs for the 'nexus-monitor' service:\n\n"
                    "journalctl ___ nexus-monitor -f"
                ),
                "answers": ["-u"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The flag to filter by service unit name.",
                    "Think: unit. One letter: -u",
                    "The answer is: -u",
                ],
            },
            {
                "id": "log_3",
                "type": "fill_blank",
                "title": "Pattern Extraction",
                "flavor": "The syslog is 800,000 lines. The event you need happened at 03:47. Extraction with grep — pattern match, pull the lines.",
                "lesson": (
                    "grep through logs — use grep to extract matching lines from log files.\n\n"
                    "Syntax: grep [options] pattern file\n\n"
                    "  grep 'error' /var/log/syslog       → lines containing 'error'\n"
                    "  grep -i 'error' file               → case-insensitive\n"
                    "  grep -n 'error' file               → with line numbers\n"
                    "  grep -A 3 'pattern' file           → 3 lines after match\n"
                    "  grep -B 3 'pattern' file           → 3 lines before match\n"
                    "  grep -r 'pattern' /var/log/        → recursive search\n\n"
                    "Chain with tail for powerful combinations:\n"
                    "  tail -f /var/log/syslog | grep 'nexus'"
                ),
                "question": (
                    "Complete the command to extract all lines containing 'nexus-agent' from /var/log/syslog:\n\n"
                    "grep ___ /var/log/syslog"
                ),
                "answers": ["'nexus-agent'", "nexus-agent", "\"nexus-agent\""],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "grep takes the pattern before the file.",
                    "grep 'pattern' file",
                    "The answer is: 'nexus-agent' /var/log/syslog",
                ],
            },
            {
                "id": "log_4",
                "type": "quiz",
                "title": "Standard Log Path",
                "flavor": "The corp's syslog isn't where they said it was. But on Debian/Ubuntu Linux, general system messages always live in the same place.",
                "lesson": (
                    "/var/log/ — the standard directory for log files on Linux systems.\n\n"
                    "Common log files:\n"
                    "  /var/log/syslog       — general system messages (Debian/Ubuntu)\n"
                    "  /var/log/messages     — general messages (RHEL/CentOS)\n"
                    "  /var/log/auth.log     — authentication events, sudo, SSH\n"
                    "  /var/log/kern.log     — kernel messages\n"
                    "  /var/log/nginx/       — nginx access and error logs\n"
                    "  /var/log/apache2/     — apache logs\n"
                    "  /var/log/dpkg.log     — package installation history\n\n"
                    "Grep through them all: grep -r 'pattern' /var/log/\n\n"
                    "On systemd systems, many apps write to journald instead."
                ),
                "question": "On Debian/Ubuntu, what file contains general system log messages?",
                "answers": ["/var/log/syslog", "syslog", "/var/log/syslog"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's in /var/log/.",
                    "The filename is 'syslog'.",
                    "The answer is: /var/log/syslog",
                ],
            },
            {
                "id": "log_5",
                "type": "quiz",
                "title": "Rotation Mechanism",
                "flavor": "The server's logs would fill every disk in a week without rotation. Something manages that — compresses old logs, removes ancient ones, keeps a fixed number.",
                "lesson": (
                    "logrotate — manages automatic rotation, compression, and deletion of log files.\n\n"
                    "Configuration: /etc/logrotate.conf and /etc/logrotate.d/\n\n"
                    "logrotate config blocks define:\n"
                    "  /var/log/app.log {\n"
                    "      daily          — rotate daily\n"
                    "      rotate 7       — keep 7 rotated files\n"
                    "      compress       — gzip old logs\n"
                    "      delaycompress  — compress previous rotation, not current\n"
                    "      missingok      — don't error if log is missing\n"
                    "      notifempty     — skip rotation if log is empty\n"
                    "  }\n\n"
                    "Manual run: logrotate -f /etc/logrotate.conf\n"
                    "Test config: logrotate -d /etc/logrotate.conf"
                ),
                "question": "What utility manages automatic log rotation, compression, and deletion on Linux?",
                "answers": ["logrotate"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The name describes exactly what it does.",
                    "logrotate",
                    "The answer is: logrotate",
                ],
            },
            {
                "id": "log_boss",
                "type": "fill_blank",
                "title": "BOSS: Auth Log Forensics",
                "flavor": "Something logged in to this server at 03:47 via SSH. Root login. The auth log has it. Extract every authentication event in a single pipeline.",
                "lesson": (
                    "/var/log/auth.log — records authentication attempts, sudo usage, and SSH logins.\n\n"
                    "Key events in auth.log:\n"
                    "  sshd: Accepted password/publickey — successful SSH login\n"
                    "  sshd: Failed password — failed login attempt\n"
                    "  sudo: username : command — sudo usage\n"
                    "  su: pam_unix — su authentication\n\n"
                    "Example forensic pipeline:\n"
                    "  grep 'Accepted' /var/log/auth.log | grep 'root'\n"
                    "  → all successful root logins\n\n"
                    "  grep 'Failed' /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn\n"
                    "  → count failed login attempts by IP address"
                ),
                "question": (
                    "What is the full path to the log file that records SSH logins and sudo commands on Debian/Ubuntu?\n"
                    "(Provide the full path)"
                ),
                "answers": ["/var/log/auth.log"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's in /var/log/.",
                    "It records 'auth'entication events.",
                    "The answer is: /var/log/auth.log",
                ],
            },
        ],
    },

    "shell_configuration": {
        "id": "shell_configuration",
        "name": "The Shell Layer",
        "subtitle": "Shell Configuration",
        "color": "cyan",
        "icon": "⚡",
        "commands": [".bashrc", ".bash_profile", "PATH", "alias", "export", "source", "env"],
        "challenges": [
            {
                "id": "shellcfg_1",
                "type": "quiz",
                "title": "Profile vs RC",
                "flavor": "The PATH isn't loading. CIPHER: 'There are two init files. One runs on login. One runs for every interactive shell. Know the difference — or your tools won't be there when you need them.'",
                "lesson": (
                    ".bashrc vs .bash_profile — two shell initialization files with different triggers.\n\n"
                    ".bash_profile (or .profile):\n"
                    "  — runs for LOGIN shells (ssh, console login, su -)\n"
                    "  — set once per session: PATH, environment variables\n\n"
                    ".bashrc:\n"
                    "  — runs for INTERACTIVE non-login shells (new terminal tab, bash command)\n"
                    "  — set per shell: aliases, functions, prompt\n\n"
                    "Common pattern: .bash_profile sources .bashrc\n"
                    "  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi\n\n"
                    "Location: both are in the user's home directory (~)"
                ),
                "question": "Which file runs for interactive non-login shells, used for aliases and prompt settings?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": [".bashrc", "~/.bashrc"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the file that runs every time you open a new terminal.",
                    "Starts with a dot. 'rc' stands for 'run commands'.",
                    "The answer is: .bashrc",
                ],
            },
            {
                "id": "shellcfg_2",
                "type": "fill_blank",
                "title": "Tool Path",
                "flavor": "The extracted binary is in /opt/nexus/bin but the shell can't find it. The PATH needs updating. Add it — without breaking anything already in the path.",
                "lesson": (
                    "PATH — the colon-separated list of directories the shell searches for executables.\n\n"
                    "View current PATH: echo $PATH\n"
                    "  → /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n\n"
                    "Add a directory to PATH:\n"
                    "  export PATH=$PATH:/opt/nexus/bin\n\n"
                    "  $PATH — current value (preserve existing entries)\n"
                    "  :/opt/nexus/bin — append new directory\n\n"
                    "To persist: add to ~/.bashrc or ~/.bash_profile\n\n"
                    "Prepend instead (higher priority):\n"
                    "  export PATH=/opt/nexus/bin:$PATH"
                ),
                "question": (
                    "Complete the command to add /opt/nexus/bin to the end of PATH without removing existing entries:\n\n"
                    "export PATH=___"
                ),
                "answers": ["$PATH:/opt/nexus/bin", "\"$PATH:/opt/nexus/bin\""],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Preserve the current PATH with $PATH, then append the new directory.",
                    "Format: $PATH:/new/directory",
                    "The answer is: $PATH:/opt/nexus/bin",
                ],
            },
            {
                "id": "shellcfg_3",
                "type": "fill_blank",
                "title": "Alias Cover",
                "flavor": "The operative types the same long command constantly. CIPHER: 'Alias it. One word. Every shell session.'",
                "lesson": (
                    "alias — creates a shorthand for a longer command.\n\n"
                    "Syntax: alias name='command'\n\n"
                    "Examples:\n"
                    "  alias ll='ls -la'              → ll now runs ls -la\n"
                    "  alias grep='grep --color=auto' → colorize grep output\n"
                    "  alias ..='cd ..'               → navigate up with ..\n"
                    "  alias update='sudo apt update && sudo apt upgrade'\n\n"
                    "View all aliases: alias (no arguments)\n"
                    "Remove an alias: unalias name\n\n"
                    "To persist across sessions: add to ~/.bashrc"
                ),
                "question": (
                    "Complete the command to create an alias 'ghost' that runs 'sudo -i':\n\n"
                    "alias ___"
                ),
                "answers": ["ghost='sudo -i'", "ghost=\"sudo -i\""],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Format: alias name='command'",
                    "alias ghost='sudo -i'",
                    "The answer is: ghost='sudo -i'",
                ],
            },
            {
                "id": "shellcfg_4",
                "type": "quiz",
                "title": "Environment Export",
                "flavor": "The variable is set in the shell — but child processes can't see it. They need it. One word makes the difference: marks it for inheritance.",
                "lesson": (
                    "export — marks a shell variable for export to child processes.\n\n"
                    "Without export:\n"
                    "  MY_VAR=secret\n"
                    "  bash -c 'echo $MY_VAR'    → (empty — child can't see it)\n\n"
                    "With export:\n"
                    "  export MY_VAR=secret\n"
                    "  bash -c 'echo $MY_VAR'    → secret\n\n"
                    "Or export after assignment:\n"
                    "  MY_VAR=secret\n"
                    "  export MY_VAR\n\n"
                    "Common pattern: export DATABASE_URL='postgres://...' in shell config files\n\n"
                    "View all exported variables: env or export -p"
                ),
                "question": "What command makes a shell variable available to child processes (subshells and programs)?",
                "answers": ["export"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The variable needs to be 'exported' to children.",
                    "Six letters.",
                    "The answer is: export",
                ],
            },
            {
                "id": "shellcfg_5",
                "type": "quiz",
                "title": "Config Reload",
                "flavor": "The .bashrc has been edited. The aliases are set. But the current shell still uses the old configuration. Apply the changes without starting a new session.",
                "lesson": (
                    "source — executes a file in the current shell environment (not a subprocess).\n\n"
                    "Syntax: source file   or  . file\n\n"
                    "  source ~/.bashrc     → reload .bashrc in current shell\n"
                    "  . ~/.bashrc          → same (dot is POSIX shorthand for source)\n"
                    "  source ~/.bash_profile\n\n"
                    "Key difference from running a script directly:\n"
                    "  ./script.sh          — runs in a subshell (changes don't affect current shell)\n"
                    "  source script.sh     — runs in current shell (changes DO affect current shell)\n\n"
                    "After modifying .bashrc: always source it to apply changes immediately."
                ),
                "question": "What command reloads a shell configuration file in the current shell session without starting a new shell?",
                "answers": ["source", "source ~/.bashrc", ". ~/.bashrc"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's a shell builtin. Also written as a single dot.",
                    "source",
                    "The answer is: source ~/.bashrc",
                ],
            },
            {
                "id": "shellcfg_boss",
                "type": "fill_blank",
                "title": "BOSS: Environment Audit",
                "flavor": "The NEXUS process has credentials in its environment. The operative needs the full picture — every variable, every value, every secret sitting in the shell's memory.",
                "lesson": (
                    "env — displays all environment variables for the current shell or runs a command with a modified environment.\n\n"
                    "Syntax:\n"
                    "  env                         → print all environment variables\n"
                    "  env | grep DATABASE          → find specific variables\n"
                    "  env VAR=value command        → run command with extra variable\n"
                    "  env -i command               → run command with empty environment\n\n"
                    "Common secrets found in env:\n"
                    "  DATABASE_URL, AWS_SECRET_ACCESS_KEY, API_KEY, SECRET_KEY\n\n"
                    "Combined with /proc:\n"
                    "  cat /proc/PID/environ | tr '\\0' '\\n'    → read another process's environment\n\n"
                    "Example: env | grep -i secret    → find anything named 'secret'"
                ),
                "question": (
                    "Complete the command to display all current environment variables and search for any containing 'KEY':\n\n"
                    "env | grep ___"
                ),
                "answers": ["KEY", "'KEY'", "\"KEY\"", "-i key", "-i KEY"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Pipe env into grep with the pattern 'KEY'.",
                    "grep KEY",
                    "The answer is: KEY",
                ],
            },
        ],
    },
    "package_management": {
        "id": "package_management",
        "name": "The Arsenal Depot",
        "subtitle": "Package Management",
        "color": "yellow",
        "icon": "📦",
        "commands": ["apt", "apt-get", "dpkg", "apt-mark"],
        "challenges": [
            {
                "id": "pkg_1",
                "type": "quiz",
                "title": "The Package Manager",
                "flavor": "The NEXUS team uses rogue packages as infection vectors. To counter them, you need to understand how package managers work — what gets installed, where, and by whom.",
                "lesson": (
                    "apt (Advanced Package Tool) — Debian/Ubuntu package manager.\n\n"
                    "Core commands:\n"
                    "  apt update              → refresh package index from repositories\n"
                    "  apt upgrade             → install available upgrades\n"
                    "  apt install <pkg>       → install a package\n"
                    "  apt remove <pkg>        → remove a package (keep config)\n"
                    "  apt purge <pkg>         → remove package AND config files\n"
                    "  apt autoremove          → remove unneeded dependencies\n"
                    "  apt search <keyword>    → search available packages\n\n"
                    "Example: apt install nmap    → installs the nmap network scanner"
                ),
                "question": "What command installs a package using apt?",
                "url": "https://linuxcommand.org/lc3_lts0020.php",
                "answers": ["apt install", "apt-get install"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Two words: the tool name, then the action.",
                    "apt install",
                    "The answer is: apt install",
                ],
            },
            {
                "id": "pkg_2",
                "type": "fill_blank",
                "title": "Refresh the Index",
                "flavor": "Before installing anything, the operative needs to sync the package index. Running installs on a stale index risks missing security patches — or installing a compromised version.",
                "lesson": (
                    "apt update — fetches the latest package lists from configured repositories.\n\n"
                    "This does NOT install anything — it only refreshes the local index.\n"
                    "Always run this before apt upgrade or apt install.\n\n"
                    "Repository sources: /etc/apt/sources.list\n\n"
                    "Example:\n"
                    "  sudo apt update && sudo apt upgrade    → full system update"
                ),
                "question": "Complete the command to refresh the package index:\n\nsudo apt ___",
                "answers": ["update"],
                "xp": 60,
                "difficulty": "easy",
                "hints": [
                    "Fetches fresh package lists. Not 'upgrade' — that installs.",
                    "update",
                    "The answer is: update",
                ],
            },
            {
                "id": "pkg_3",
                "type": "quiz",
                "title": "Purge vs Remove",
                "flavor": "The NEXUS software left behind config files even after uninstall. The malware reads from those files on restart. You need a harder removal — one that gets the config too.",
                "lesson": (
                    "apt remove vs apt purge:\n\n"
                    "  apt remove <pkg>    → removes the binary but KEEPS config files\n"
                    "  apt purge <pkg>     → removes the package AND all config files\n\n"
                    "When to use purge:\n"
                    "  - Removing sensitive config (passwords, API keys)\n"
                    "  - Completely resetting a service to a clean slate\n"
                    "  - Forensic cleanup where no artifacts should remain\n\n"
                    "Check what's installed: dpkg -L <pkg>    → list all files owned by package"
                ),
                "question": "Which command removes a package AND its configuration files?",
                "answers": ["apt purge", "apt-get purge"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "remove keeps config. The stronger command does not.",
                    "apt purge",
                    "The answer is: apt purge",
                ],
            },
            {
                "id": "pkg_4",
                "type": "fill_blank",
                "title": "Audit Installed Packages",
                "flavor": "You need to audit what's on the compromised node. Something with 'nexus' in the name. dpkg can list all installed packages — grep can find the one you're hunting.",
                "lesson": (
                    "dpkg — low-level Debian package manager. apt is built on top of dpkg.\n\n"
                    "Useful dpkg commands:\n"
                    "  dpkg -l                  → list all installed packages\n"
                    "  dpkg -l | grep <name>    → filter for packages matching name\n"
                    "  dpkg -L <pkg>            → list all files a package installed\n"
                    "  dpkg -S <file>           → which package owns this file?\n\n"
                    "Example:\n"
                    "  dpkg -l | grep python    → find all installed python packages"
                ),
                "question": "Complete the command to list all installed packages and search for 'nexus':\n\ndpkg ___ | grep nexus",
                "answers": ["-l"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "The flag that lists all installed packages.",
                    "-l",
                    "The answer is: -l",
                ],
            },
            {
                "id": "pkg_5",
                "type": "quiz",
                "title": "Holding a Version",
                "flavor": "A critical dependency keeps getting auto-upgraded to a broken version by routine apt upgrade runs. The operative needs to freeze it at the current working version.",
                "lesson": (
                    "apt-mark hold — prevents a package from being upgraded automatically.\n\n"
                    "Commands:\n"
                    "  apt-mark hold <pkg>      → freeze package at current version\n"
                    "  apt-mark unhold <pkg>    → release the hold, allow upgrades\n"
                    "  apt-mark showhold        → list all held packages\n\n"
                    "When to use:\n"
                    "  - Pin a working kernel version after a bad update\n"
                    "  - Freeze a database driver for compatibility\n"
                    "  - Prevent auto-upgrade of fragile config\n\n"
                    "Verify: dpkg -l <pkg>    → status 'hi' = held installed"
                ),
                "question": "What command prevents a specific package from being upgraded by apt upgrade?",
                "answers": ["apt-mark hold"],
                "xp": 80,
                "difficulty": "easy",
                "hints": [
                    "Two words: apt-mark and the action that freezes.",
                    "apt-mark hold",
                    "The answer is: apt-mark hold",
                ],
            },
            {
                "id": "pkg_boss",
                "type": "fill_blank",
                "title": "BOSS: The Orphan Hunt",
                "flavor": "The NEXUS payload hid inside an orphaned package — a dependency no longer needed after the main package was removed. One command hunts and removes all these automatically.",
                "lesson": (
                    "apt autoremove — removes packages installed as dependencies "
                    "that are no longer needed by any installed package.\n\n"
                    "Always run after removing a package to clean up orphaned deps.\n"
                    "Keeps attack surface small.\n\n"
                    "Dry run: apt autoremove --dry-run    → preview removals\n\n"
                    "Full cleanup:\n"
                    "  sudo apt remove <pkg> && sudo apt autoremove && sudo apt autoclean"
                ),
                "question": "Complete the command to remove all orphaned dependency packages:\n\nsudo apt ___",
                "answers": ["autoremove"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "AUTO-removes packages no longer needed.",
                    "autoremove",
                    "The answer is: autoremove",
                ],
            },
        ],
    },
    "systemd_services": {
        "id": "systemd_services",
        "name": "The Service Grid",
        "subtitle": "systemd & Service Management",
        "color": "magenta",
        "icon": "⚙️",
        "commands": ["systemctl", "journalctl"],
        "challenges": [
            {
                "id": "svc_1",
                "type": "quiz",
                "title": "The Init System",
                "flavor": "The NEXUS malware registered itself as a systemd service — starts on boot, restarts on crash, hides among legitimate services. To kill it permanently, you must understand systemd.",
                "lesson": (
                    "systemd — init system and service manager (PID 1 on modern Linux).\n\n"
                    "systemctl — CLI to control systemd:\n"
                    "  systemctl start <svc>     → start a service\n"
                    "  systemctl stop <svc>      → stop a service\n"
                    "  systemctl restart <svc>   → restart a service\n"
                    "  systemctl status <svc>    → show current status\n"
                    "  systemctl enable <svc>    → start on boot\n"
                    "  systemctl disable <svc>   → don't start on boot\n"
                    "  systemctl list-units      → list all running units\n\n"
                    "Example: systemctl status nginx    → check if nginx is running"
                ),
                "question": "What command checks the current status of a systemd service named 'nginx'?",
                "url": "https://man7.org/linux/man-pages/man1/systemctl.1.html",
                "answers": ["systemctl status nginx"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "systemctl is the tool. status is the subcommand.",
                    "systemctl status nginx",
                    "The answer is: systemctl status nginx",
                ],
            },
            {
                "id": "svc_2",
                "type": "fill_blank",
                "title": "Sever the Boot Link",
                "flavor": "The malicious service keeps coming back after reboot. Stopping it isn't enough — you need to sever the boot-time link that resurrects it every restart.",
                "lesson": (
                    "systemctl enable/disable:\n\n"
                    "  systemctl enable <svc>     → creates symlink to start on boot\n"
                    "  systemctl disable <svc>    → removes symlink, won't start on boot\n"
                    "  systemctl is-enabled <svc> → check if enabled\n\n"
                    "Combine stop + disable to kill now AND prevent on boot:\n"
                    "  sudo systemctl disable --now <svc>    → stop AND disable in one command"
                ),
                "question": "Complete the command to prevent a service from starting on boot:\n\nsudo systemctl ___ nexus-agent",
                "answers": ["disable"],
                "xp": 60,
                "difficulty": "easy",
                "hints": [
                    "The opposite of 'enable'. Removes the boot-time symlink.",
                    "disable",
                    "The answer is: disable",
                ],
            },
            {
                "id": "svc_3",
                "type": "quiz",
                "title": "Reading the Journal",
                "flavor": "The service crashed 40 minutes ago. No log files on disk — NEXUS wiped them. But systemd's binary journal survived the cleanup. You need to read it.",
                "lesson": (
                    "journalctl — queries the systemd journal.\n\n"
                    "Common usage:\n"
                    "  journalctl -r                    → newest logs first\n"
                    "  journalctl -f                    → follow live (like tail -f)\n"
                    "  journalctl -u <svc>              → logs for one service only\n"
                    "  journalctl --since '1 hour ago'  → logs from last hour\n"
                    "  journalctl -p err                → only error-level messages\n\n"
                    "Example:\n"
                    "  journalctl -u nginx --since '10 minutes ago'"
                ),
                "question": "Which command shows journal logs for only the service named 'nexus-agent'?",
                "answers": ["journalctl -u nexus-agent", "journalctl --unit nexus-agent"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "journalctl with a flag that filters by unit/service name.",
                    "journalctl -u nexus-agent",
                    "The answer is: journalctl -u nexus-agent",
                ],
            },
            {
                "id": "svc_4",
                "type": "fill_blank",
                "title": "Unit File Location",
                "flavor": "You need to inspect the nexus-agent service definition — its ExecStart path, the user it runs as, and its restart policy. Find and read its unit file.",
                "lesson": (
                    "systemd unit files define service behavior.\n\n"
                    "Locations (highest to lowest priority):\n"
                    "  /etc/systemd/system/       → admin-defined (highest priority)\n"
                    "  /usr/lib/systemd/system/   → package-installed\n\n"
                    "Key unit file sections:\n"
                    "  [Unit]     → description, dependencies\n"
                    "  [Service]  → ExecStart, User, Restart, Environment\n"
                    "  [Install]  → WantedBy (boot target)\n\n"
                    "After editing:\n"
                    "  sudo systemctl daemon-reload    → re-read all unit files"
                ),
                "question": "Complete the path to the highest-priority location for custom unit files:\n\n/___/systemd/system/",
                "answers": ["etc"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "System-wide configuration lives here.",
                    "etc",
                    "The answer is: etc",
                ],
            },
            {
                "id": "svc_5",
                "type": "quiz",
                "title": "The Immortal Service",
                "flavor": "Restart=always in the unit file makes the NEXUS service immortal — respawning within seconds of being killed. To stop it dead, you need a command more permanent than disable.",
                "lesson": (
                    "systemctl mask — the nuclear option for services.\n\n"
                    "  systemctl disable <svc>  → won't start on boot, but CAN be started manually\n"
                    "  systemctl mask <svc>     → symlinks unit to /dev/null — CANNOT be started at all\n"
                    "  systemctl unmask <svc>   → restores ability to start\n\n"
                    "Restart policies in unit files:\n"
                    "  Restart=no           → never restart (default)\n"
                    "  Restart=on-failure   → restart on non-zero exit\n"
                    "  Restart=always       → restart regardless of how it stopped\n\n"
                    "To counter Restart=always: stop + mask the service."
                ),
                "question": "Which systemctl command permanently prevents a service from EVER being started (even manually)?",
                "answers": ["systemctl mask", "sudo systemctl mask"],
                "xp": 80,
                "difficulty": "easy",
                "hints": [
                    "More permanent than disable. Symlinks the unit to /dev/null.",
                    "systemctl mask",
                    "The answer is: systemctl mask",
                ],
            },
            {
                "id": "svc_boss",
                "type": "fill_blank",
                "title": "BOSS: Daemon Reload",
                "flavor": "You've edited the nexus-agent.service unit file — changed ExecStart and removed Restart=always. But systemd is still running the old definition. One command refreshes it without rebooting.",
                "lesson": (
                    "systemctl daemon-reload — tells systemd to re-read all unit files.\n\n"
                    "Required after:\n"
                    "  - Creating a new unit file\n"
                    "  - Editing an existing unit file\n\n"
                    "After daemon-reload, restart to apply:\n"
                    "  sudo systemctl daemon-reload\n"
                    "  sudo systemctl restart <svc>\n\n"
                    "Without daemon-reload, systemctl restart still uses the cached old definition."
                ),
                "question": "Complete the command to reload systemd's unit file definitions after editing a service file:\n\nsudo systemctl ___",
                "answers": ["daemon-reload"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Hyphenated. Reloads the daemon's configuration.",
                    "daemon-reload",
                    "The answer is: daemon-reload",
                ],
            },
        ],
    },
    "text_processing": {
        "id": "text_processing",
        "name": "The Data Blade",
        "subtitle": "Text Processing",
        "color": "green",
        "icon": "⚔",
        "commands": ["awk", "sed", "cut", "sort", "uniq", "tr", "wc"],
        "challenges": [
            {
                "id": "txt_1",
                "type": "quiz",
                "title": "Field Extraction",
                "flavor": "NEXUS logs are colon-delimited. You need column 3 from every line — user IDs, extracted cleanly. One tool handles fixed delimiters.",
                "lesson": (
                    "cut — extracts fields or character ranges from each line of input.\n\n"
                    "Syntax: cut [options] [file]\n\n"
                    "  -d DELIM   field delimiter (default: tab)\n"
                    "  -f N       select field number N\n"
                    "  -c N       select character position N\n\n"
                    "Examples:\n"
                    "  cut -d: -f1 /etc/passwd        → extract usernames\n"
                    "  cut -d, -f3 data.csv           → third CSV column\n"
                    "  cut -c1-10 file.txt            → first 10 characters per line\n\n"
                    "Combine with sort/uniq for frequency analysis:\n"
                    "  cut -d: -f1 /etc/passwd | sort | uniq"
                ),
                "question": "What command extracts the first field from a colon-delimited file like /etc/passwd?",
                "url": "https://man7.org/linux/man-pages/man1/awk.1p.html",
                "answers": ["cut -d: -f1", "cut -d: -f1 /etc/passwd"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The command is 'cut'. Use -d for delimiter and -f for field.",
                    "Delimiter is colon: -d:",
                    "The answer is: cut -d: -f1",
                ],
            },
            {
                "id": "txt_2",
                "type": "fill_blank",
                "title": "Unique Offenders",
                "flavor": "The auth log has thousands of lines — many duplicates. You need each unique IP, counted. Sort first, then deduplicate with counts.",
                "lesson": (
                    "sort | uniq -c — the classic pipeline for frequency analysis.\n\n"
                    "sort — sorts lines alphabetically (required before uniq)\n"
                    "uniq — filters adjacent duplicate lines\n"
                    "  -c   prefix each line with occurrence count\n"
                    "  -d   only print duplicate lines\n"
                    "  -u   only print unique lines\n\n"
                    "Full frequency pipeline:\n"
                    "  sort | uniq -c | sort -rn | head\n\n"
                    "Examples:\n"
                    "  cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -10\n"
                    "  → top 10 IPs by hit count in an access log\n\n"
                    "Note: uniq only removes ADJACENT duplicates — always sort first."
                ),
                "question": (
                    "Complete the pipeline to count and sort unique IPs from auth.log:\n\n"
                    "grep 'Failed' auth.log | awk '{print $11}' | sort | ___ | sort -rn"
                ),
                "url": "https://man7.org/linux/man-pages/man1/awk.1p.html",
                "answers": ["uniq -c"],
                "xp": 60,
                "difficulty": "medium",
                "hints": [
                    "uniq with the count flag.",
                    "-c gives you the count.",
                    "The answer is: uniq -c",
                ],
            },
            {
                "id": "txt_3",
                "type": "quiz",
                "title": "Stream Edit",
                "flavor": "The exfil file has Windows-style CRLF line endings. The receiving server expects Unix LF only. Strip them in-place without opening an editor.",
                "lesson": (
                    "sed — stream editor for filtering and transforming text.\n\n"
                    "Syntax: sed [options] 'expression' [file]\n\n"
                    "  -i        edit file in-place\n"
                    "  -i.bak    edit in-place, save backup with .bak extension\n"
                    "  -n        suppress automatic printing\n\n"
                    "Substitution syntax: s/pattern/replacement/flags\n"
                    "  g   replace all occurrences (global)\n"
                    "  i   case-insensitive\n\n"
                    "Examples:\n"
                    "  sed 's/foo/bar/g' file.txt          → replace all 'foo' with 'bar'\n"
                    "  sed -i 's/\\r//' file.txt            → strip carriage returns (CRLF → LF)\n"
                    "  sed -n '10,20p' file.txt            → print lines 10-20\n"
                    "  sed '/^#/d' config.txt              → delete comment lines\n\n"
                    "sed is the standard tool for in-place bulk text transformation."
                ),
                "question": "What tool is used for in-place text substitution and stream editing via regex patterns?",
                "url": "https://man7.org/linux/man-pages/man1/sed.1.html",
                "answers": ["sed"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Stream EDitor. Three letters.",
                    "s/old/new/g syntax.",
                    "The answer is: sed",
                ],
            },
            {
                "id": "txt_4",
                "type": "fill_blank",
                "title": "AWK Column Filter",
                "flavor": "The NEXUS transaction log is whitespace-delimited. Column 4 is the amount field. You need only lines where the amount exceeds 10000. awk handles both extraction and filtering.",
                "lesson": (
                    "awk — pattern scanning and processing language for structured text.\n\n"
                    "Syntax: awk 'pattern { action }' file\n\n"
                    "Built-in variables:\n"
                    "  $0   entire line\n"
                    "  $1, $2 ... $NF   field 1, field 2 ... last field\n"
                    "  NF   number of fields\n"
                    "  NR   current line number\n"
                    "  FS   field separator (default: whitespace)\n\n"
                    "Examples:\n"
                    "  awk '{print $1}' file             → print first field of every line\n"
                    "  awk '$4 > 10000' transactions.log → lines where field 4 > 10000\n"
                    "  awk -F: '{print $1}' /etc/passwd  → use colon as separator\n"
                    "  awk 'NR==5' file                  → print line 5 only\n\n"
                    "awk excels at column-based log analysis and conditional filtering."
                ),
                "question": (
                    "Complete the awk command to print lines where the 4th field is greater than 10000:\n\n"
                    "awk '___ > 10000' transactions.log"
                ),
                "url": "https://man7.org/linux/man-pages/man1/awk.1p.html",
                "answers": ["$4"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "awk fields are accessed with $N notation.",
                    "Fourth field: $4",
                    "The answer is: $4",
                ],
            },
            {
                "id": "txt_5",
                "type": "quiz",
                "title": "Word Count",
                "flavor": "The report needs a line count for the evidence log. One command gives you lines, words, and bytes simultaneously.",
                "lesson": (
                    "wc — word count utility that counts lines, words, and bytes.\n\n"
                    "Syntax: wc [options] [file]\n\n"
                    "  wc        → lines, words, bytes\n"
                    "  wc -l     → line count only\n"
                    "  wc -w     → word count only\n"
                    "  wc -c     → byte count\n"
                    "  wc -m     → character count\n\n"
                    "Examples:\n"
                    "  wc -l /var/log/auth.log         → how many log entries\n"
                    "  cat file | wc -l               → count lines from stdin\n"
                    "  ls | wc -l                     → count files in a directory\n\n"
                    "Combine with grep to count matches:\n"
                    "  grep 'ERROR' app.log | wc -l   → number of error lines"
                ),
                "question": "What flag does wc use to count only lines?",
                "url": "https://man7.org/linux/man-pages/man1/awk.1p.html",
                "answers": ["-l", "wc -l"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Single letter flag. Think: lines.",
                    "-l",
                    "The answer is: -l",
                ],
            },
            {
                "id": "txt_boss",
                "type": "fill_blank",
                "title": "BOSS: Full Pipeline",
                "flavor": "CIPHER: 'The NEXUS access log has tens of thousands of entries. I need the top 5 source IPs — by hit count, descending. Build the pipeline.'",
                "lesson": (
                    "Log analysis pipeline — combining cut, sort, uniq, and head.\n\n"
                    "Standard pattern for top-N frequency analysis:\n\n"
                    "  cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -5\n\n"
                    "Step by step:\n"
                    "  cut -d' ' -f1   → extract the IP (first field, space-delimited)\n"
                    "  sort            → sort IPs alphabetically (required for uniq)\n"
                    "  uniq -c         → count consecutive duplicates\n"
                    "  sort -rn        → sort numerically, descending (highest count first)\n"
                    "  head -5         → take the top 5\n\n"
                    "sort flags:\n"
                    "  -r   reverse order (descending)\n"
                    "  -n   numeric sort (not lexicographic)\n\n"
                    "This pipeline works on any log format — change the cut fields to match."
                ),
                "question": (
                    "Complete the pipeline to find the top 5 IPs in access.log:\n\n"
                    "cut -d' ' -f1 access.log | sort | uniq -c | sort ___ | head -5"
                ),
                "url": "https://man7.org/linux/man-pages/man1/awk.1p.html",
                "answers": ["-rn", "-nr"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "sort needs to be reversed and numeric.",
                    "-r for reverse, -n for numeric — combine them.",
                    "The answer is: -rn",
                ],
            },
        ],
    },

    "archive_and_compression": {
        "id": "archive_and_compression",
        "name": "The Courier Protocol",
        "subtitle": "Archive & Compression",
        "color": "blue",
        "icon": "📦",
        "commands": ["tar", "gzip", "bzip2", "zip", "unzip", "scp", "rsync"],
        "challenges": [
            {
                "id": "arc_1",
                "type": "quiz",
                "title": "Pack the Archive",
                "flavor": "The evidence directory is ready. Before transfer it needs to be packed into a single file. tar. Create the archive.",
                "lesson": (
                    "tar — tape archive utility for bundling files and directories.\n\n"
                    "Syntax: tar [options] archive.tar [files...]\n\n"
                    "Core flags:\n"
                    "  -c   create a new archive\n"
                    "  -x   extract from archive\n"
                    "  -t   list archive contents\n"
                    "  -f   specify archive filename (required)\n"
                    "  -v   verbose (show files being processed)\n"
                    "  -z   compress/decompress with gzip (.tar.gz)\n"
                    "  -j   compress/decompress with bzip2 (.tar.bz2)\n\n"
                    "Examples:\n"
                    "  tar -czf archive.tar.gz /evidence/    → create gzip-compressed archive\n"
                    "  tar -xzf archive.tar.gz               → extract gzip archive\n"
                    "  tar -tf archive.tar.gz                → list contents without extracting"
                ),
                "question": "What tar flags create a new gzip-compressed archive from a directory?",
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["-czf", "czf", "tar -czf"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Three flags: create, gzip-compress, filename.",
                    "-c -z -f combined: -czf",
                    "The answer is: -czf",
                ],
            },
            {
                "id": "arc_2",
                "type": "fill_blank",
                "title": "Inspect Before Extract",
                "flavor": "You've received an archive from the drop. Before extracting anything, verify its contents. Never unpack blind.",
                "lesson": (
                    "tar -tf — lists archive contents without extracting.\n\n"
                    "Syntax: tar -tf archive.tar.gz\n\n"
                    "  -t   list/test — show what's inside\n"
                    "  -f   filename\n"
                    "  -v   verbose (show permissions, owner, size, date)\n\n"
                    "Security: always inspect archives before extraction to avoid\n"
                    "path traversal attacks (files containing ../../ paths).\n\n"
                    "Examples:\n"
                    "  tar -tf payload.tar.gz          → list all files\n"
                    "  tar -tvf payload.tar.gz         → verbose listing with metadata\n"
                    "  tar -tf payload.tar.gz | grep '\\.\\./'  → check for path traversal\n\n"
                    "If any path starts with / or contains ../ — do not extract."
                ),
                "question": (
                    "Complete the command to list the contents of an archive without extracting:\n\n"
                    "tar ___ payload.tar.gz"
                ),
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["-tf", "-tvf"],
                "xp": 60,
                "difficulty": "medium",
                "hints": [
                    "Two flags: test/list and filename.",
                    "-t for list, -f for filename.",
                    "The answer is: -tf",
                ],
            },
            {
                "id": "arc_3",
                "type": "quiz",
                "title": "Gzip Single File",
                "flavor": "The log file is 800MB uncompressed. Compress it with gzip before staging for transfer. It will shrink dramatically.",
                "lesson": (
                    "gzip — compresses files using the LZ77 algorithm.\n\n"
                    "Syntax: gzip [options] file\n\n"
                    "  gzip file           → compress (replaces file with file.gz)\n"
                    "  gzip -d file.gz     → decompress (same as gunzip)\n"
                    "  gzip -k file        → keep original (don't delete)\n"
                    "  gzip -9 file        → maximum compression\n"
                    "  gzip -l file.gz     → list compression ratio\n\n"
                    "Comparison:\n"
                    "  gzip    — fast, good compression (.gz)\n"
                    "  bzip2   — slower, better compression (.bz2)\n"
                    "  xz      — slowest, best compression (.xz)\n\n"
                    "gzip is the default compression for tar (.tar.gz or .tgz)."
                ),
                "question": "What command compresses a file with gzip, replacing the original with a .gz file?",
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["gzip", "gzip file"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The compression utility with a name like the format.",
                    "gzip",
                    "The answer is: gzip",
                ],
            },
            {
                "id": "arc_4",
                "type": "fill_blank",
                "title": "Secure Copy",
                "flavor": "Archive is ready. The drop site is at 10.0.1.88. Transfer the file over SSH — encrypted, authenticated, no FTP.",
                "lesson": (
                    "scp — secure copy over SSH.\n\n"
                    "Syntax: scp [options] source destination\n\n"
                    "Remote path format: user@host:/path/to/file\n\n"
                    "  scp file.tar.gz user@host:/tmp/      → upload to remote\n"
                    "  scp user@host:/data/file.txt ./      → download from remote\n"
                    "  scp -r dir/ user@host:/backup/       → copy directory recursively\n"
                    "  scp -P 2222 file user@host:/tmp/     → use custom SSH port\n\n"
                    "rsync is preferred for large or repeated transfers:\n"
                    "  rsync -avz file user@host:/backup/   → sync with compression and progress\n"
                    "  rsync --delete src/ user@host:/dst/  → mirror (delete removed files)\n\n"
                    "Both scp and rsync use SSH for transport — encrypted by default."
                ),
                "question": (
                    "Complete the scp command to upload evidence.tar.gz to the /exfil/ directory on the drop server:\n\n"
                    "scp evidence.tar.gz operative@10.0.1.88:___"
                ),
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["/exfil/", "/exfil"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "The destination path on the remote host.",
                    "After the colon comes the remote path.",
                    "The answer is: /exfil/",
                ],
            },
            {
                "id": "arc_5",
                "type": "quiz",
                "title": "Backup Strategy",
                "flavor": "CIPHER: 'You need a reliable way to sync the evidence directory to the backup server nightly — incremental, not a full copy each time.'",
                "lesson": (
                    "rsync — efficient file synchronization and backup tool.\n\n"
                    "Syntax: rsync [options] source destination\n\n"
                    "Key flags:\n"
                    "  -a   archive mode (preserves permissions, timestamps, symlinks)\n"
                    "  -v   verbose\n"
                    "  -z   compress data during transfer\n"
                    "  -n   dry run (show what would be transferred)\n"
                    "  --delete          remove files at destination not in source\n"
                    "  --exclude=PATTERN skip matching files\n\n"
                    "rsync is incremental — only transfers changed files, unlike scp.\n\n"
                    "Examples:\n"
                    "  rsync -avz /data/ user@backup:/data/       → sync to remote\n"
                    "  rsync -avzn /data/ user@backup:/data/      → dry run first\n"
                    "  rsync -avz --delete /src/ /dst/            → mirror with deletion\n\n"
                    "Trailing slash matters: /src/ (contents) vs /src (directory itself)."
                ),
                "question": "Which tool performs incremental file synchronization, only transferring files that have changed?",
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["rsync"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Not scp — this one is incremental.",
                    "rsync",
                    "The answer is: rsync",
                ],
            },
            {
                "id": "arc_boss",
                "type": "fill_blank",
                "title": "BOSS: Compressed Transfer",
                "flavor": "CIPHER: 'You need the entire /evidence directory archived, gzip-compressed, and written to a single file called drop.tar.gz. One command. No intermediates.'",
                "lesson": (
                    "tar -czf — create a gzip-compressed archive in a single command.\n\n"
                    "Syntax: tar -czf output.tar.gz source_directory/\n\n"
                    "Flags:\n"
                    "  -c   create new archive\n"
                    "  -z   compress with gzip\n"
                    "  -f   next argument is the filename\n\n"
                    "The filename argument (-f) must immediately follow in the flag string,\n"
                    "or be the next argument when flags are separated.\n\n"
                    "Example:\n"
                    "  tar -czf drop.tar.gz /evidence/\n"
                    "  tar czf drop.tar.gz /evidence/    (same, without leading dash)\n\n"
                    "To also exclude certain paths:\n"
                    "  tar -czf drop.tar.gz --exclude='*.tmp' /evidence/\n\n"
                    "Verify after creation: tar -tf drop.tar.gz"
                ),
                "question": (
                    "Complete the command to create a gzip-compressed archive of /evidence/:\n\n"
                    "tar ___ drop.tar.gz /evidence/"
                ),
                "url": "https://man7.org/linux/man-pages/man1/tar.1.html",
                "answers": ["-czf", "czf"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Three flags: create, compress (gzip), filename.",
                    "-czf",
                    "The answer is: -czf",
                ],
            },
        ],
    },

    "cron_and_scheduling": {
        "id": "cron_and_scheduling",
        "name": "The Clock Daemon",
        "subtitle": "Cron & Scheduling",
        "color": "magenta",
        "icon": "⏰",
        "commands": ["crontab", "cron", "anacron", "at", "batch", "systemd timers"],
        "challenges": [
            {
                "id": "cron_1",
                "type": "quiz",
                "title": "Edit the Schedule",
                "flavor": "You need to plant a scheduled check — a script that runs every morning at 02:00 without leaving obvious traces. The operative's tool: crontab.",
                "lesson": (
                    "crontab — manages the cron schedule for the current user.\n\n"
                    "Syntax:\n"
                    "  crontab -e    → open user's crontab in editor (create or edit)\n"
                    "  crontab -l    → list current user's cron jobs\n"
                    "  crontab -r    → remove ALL cron jobs (use with caution)\n"
                    "  crontab -u user -l  → list another user's crontab (requires root)\n\n"
                    "Cron expression format:\n"
                    "  minute  hour  day-of-month  month  day-of-week  command\n"
                    "  0-59    0-23  1-31          1-12   0-7\n\n"
                    "Example entry:\n"
                    "  0 2 * * * /opt/scripts/check.sh    → run at 02:00 every day\n\n"
                    "The cron daemon reads the crontab and executes jobs at scheduled times."
                ),
                "question": "What command opens the current user's crontab for editing?",
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["crontab -e"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "crontab with the edit flag.",
                    "-e for edit.",
                    "The answer is: crontab -e",
                ],
            },
            {
                "id": "cron_2",
                "type": "fill_blank",
                "title": "Expression Decode",
                "flavor": "Auditing the system crontab. Entry: '30 4 * * 1'. You need to know exactly when this job fires before deciding whether to neutralize it.",
                "lesson": (
                    "Cron expression format:\n\n"
                    "  ┌──── minute (0-59)\n"
                    "  │ ┌──── hour (0-23)\n"
                    "  │ │ ┌──── day of month (1-31)\n"
                    "  │ │ │ ┌──── month (1-12)\n"
                    "  │ │ │ │ ┌──── day of week (0=Sun, 1=Mon ... 6=Sat, 7=Sun)\n"
                    "  │ │ │ │ │\n"
                    "  * * * * *  command\n\n"
                    "Special characters:\n"
                    "  *   any value\n"
                    "  ,   list: 1,3,5 — at positions 1, 3, and 5\n"
                    "  -   range: 1-5 — every value from 1 to 5\n"
                    "  /   step: */15 — every 15 units\n\n"
                    "Examples:\n"
                    "  0 * * * *      → every hour on the hour\n"
                    "  */15 * * * *   → every 15 minutes\n"
                    "  0 2 * * 1      → every Monday at 02:00\n"
                    "  30 4 * * 1     → every Monday at 04:30"
                ),
                "question": (
                    "The cron entry '30 4 * * 1' runs at what time and day?\n\n"
                    "Answer: Every ___ at 04:30"
                ),
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["Monday", "monday", "Mon"],
                "xp": 60,
                "difficulty": "medium",
                "hints": [
                    "The last field is day of week. 1 = Monday.",
                    "Day 1 = Monday.",
                    "The answer is: Monday",
                ],
            },
            {
                "id": "cron_3",
                "type": "quiz",
                "title": "One-Shot Scheduling",
                "flavor": "The exfil script needs to run exactly once, in 10 minutes, without being added to any persistent schedule. No cron. Something lighter.",
                "lesson": (
                    "at — schedules a one-time job to run at a specified future time.\n\n"
                    "Syntax:\n"
                    "  at TIME          → open interactive prompt for commands\n"
                    "  echo 'cmd' | at TIME  → pipe command directly\n"
                    "  at -l            → list pending at jobs (same as atq)\n"
                    "  at -r JOB_ID     → remove a pending job (same as atrm)\n\n"
                    "Time formats:\n"
                    "  at now + 10 minutes\n"
                    "  at 14:30\n"
                    "  at midnight tomorrow\n"
                    "  at 9am next Monday\n\n"
                    "Example:\n"
                    "  echo '/opt/exfil.sh' | at now + 10 minutes\n\n"
                    "Unlike cron, 'at' runs the job once, then removes it."
                ),
                "question": "What command schedules a one-time command to run at a future time (not recurring)?",
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["at"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Two letters. Single-shot scheduler.",
                    "at",
                    "The answer is: at",
                ],
            },
            {
                "id": "cron_4",
                "type": "fill_blank",
                "title": "Every 15 Minutes",
                "flavor": "The heartbeat check needs to run every 15 minutes, every hour, every day. Write the cron expression.",
                "lesson": (
                    "Cron step syntax — */N means 'every N units'.\n\n"
                    "  */15 * * * *   → every 15 minutes\n"
                    "  */2 * * * *    → every 2 minutes\n"
                    "  0 */6 * * *    → every 6 hours, on the hour\n"
                    "  */5 8-18 * * 1-5  → every 5 min, business hours, weekdays\n\n"
                    "The /N step divides the range:\n"
                    "  */15 in minutes → runs at 0, 15, 30, 45\n"
                    "  */6 in hours → runs at 0, 6, 12, 18\n\n"
                    "Full example entry:\n"
                    "  */15 * * * * /opt/heartbeat.sh\n\n"
                    "Use crontab.guru to verify expressions interactively."
                ),
                "question": (
                    "Write the cron time expression (5 fields) to run a job every 15 minutes:"
                ),
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["*/15 * * * *"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Step syntax: */N in the minutes field.",
                    "Minutes field: */15, then four wildcards.",
                    "The answer is: */15 * * * *",
                ],
            },
            {
                "id": "cron_5",
                "type": "quiz",
                "title": "List All Jobs",
                "flavor": "Something is scheduled that shouldn't be. Before removing anything, you need to see every cron job registered for the current user.",
                "lesson": (
                    "crontab -l — lists the current user's cron jobs.\n\n"
                    "  crontab -l              → current user's jobs\n"
                    "  sudo crontab -u root -l → root's crontab\n"
                    "  sudo crontab -u www-data -l  → web server's crontab\n\n"
                    "System-wide cron locations to also check:\n"
                    "  /etc/crontab            → system crontab (includes user field)\n"
                    "  /etc/cron.d/            → drop-in cron files\n"
                    "  /etc/cron.hourly/       → scripts run hourly\n"
                    "  /etc/cron.daily/        → scripts run daily\n"
                    "  /etc/cron.weekly/\n"
                    "  /etc/cron.monthly/\n"
                    "  /var/spool/cron/crontabs/  → per-user crontab files\n\n"
                    "Full audit: check all locations above for persistence mechanisms."
                ),
                "question": "What command lists all cron jobs for the current user?",
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["crontab -l"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "crontab with the list flag.",
                    "-l for list.",
                    "The answer is: crontab -l",
                ],
            },
            {
                "id": "cron_boss",
                "type": "fill_blank",
                "title": "BOSS: Systemd Timer",
                "flavor": "CIPHER: 'Cron is old. This server uses systemd timers. One is running that shouldn't be. List every active timer — I need to see the schedule.'",
                "lesson": (
                    "systemd timers — the modern alternative to cron.\n\n"
                    "List timers:\n"
                    "  systemctl list-timers          → all active timers with next trigger\n"
                    "  systemctl list-timers --all    → including inactive timers\n\n"
                    "Timer unit file format (.timer):\n"
                    "  [Timer]\n"
                    "  OnCalendar=*-*-* 02:00:00    → run daily at 02:00\n"
                    "  OnBootSec=5min               → run 5 minutes after boot\n"
                    "  OnUnitActiveSec=1h           → repeat every hour\n"
                    "  Persistent=true              → catch up if missed (like anacron)\n\n"
                    "Each timer is paired with a .service unit of the same name.\n\n"
                    "Example: nexus-check.timer triggers nexus-check.service\n\n"
                    "Advantage over cron: timers are tracked in the journal,\n"
                    "support dependencies, and survive missed runs (with Persistent=true)."
                ),
                "question": (
                    "Complete the command to list all active systemd timers:\n\n"
                    "systemctl ___"
                ),
                "url": "https://man7.org/linux/man-pages/man5/crontab.5.html",
                "answers": ["list-timers", "list-timers --all"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "systemctl subcommand that lists timer units.",
                    "list-timers",
                    "The answer is: list-timers",
                ],
            },
        ],
    },

    "bash_scripting_basics": {
        "id": "bash_scripting_basics",
        "name": "The Script Engine",
        "subtitle": "Bash Scripting Basics",
        "color": "cyan",
        "icon": "📜",
        "commands": ["bash", "sh", "chmod +x", "if", "for", "while", "exit"],
        "challenges": [
            {
                "id": "bash_1",
                "type": "fill_blank",
                "title": "The Shebang",
                "flavor": "The script needs to run directly as an executable. The first line tells the kernel which interpreter to use. Get it wrong and nothing runs.",
                "lesson": (
                    "Shebang line — the first line of a script that specifies the interpreter.\n\n"
                    "Syntax: #!interpreter_path\n\n"
                    "Common shebangs:\n"
                    "  #!/bin/bash          → run with bash\n"
                    "  #!/bin/sh            → run with POSIX sh\n"
                    "  #!/usr/bin/env bash  → find bash in PATH (more portable)\n"
                    "  #!/usr/bin/env python3\n\n"
                    "Without a shebang:\n"
                    "  The script runs with the current shell (/bin/sh default).\n"
                    "  Bash-specific syntax may fail if sh is not bash.\n\n"
                    "Making a script executable:\n"
                    "  chmod +x script.sh\n"
                    "  ./script.sh\n\n"
                    "Best practice: always include a shebang and chmod +x your scripts."
                ),
                "question": (
                    "Complete the shebang line to specify bash as the interpreter:\n\n"
                    "___/bin/bash"
                ),
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["#!", "#!/"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Hash followed by exclamation mark.",
                    "#!",
                    "The answer is: #!",
                ],
            },
            {
                "id": "bash_2",
                "type": "quiz",
                "title": "Script Arguments",
                "flavor": "The exfil script needs to accept a target host as its first argument at runtime. Inside the script, how do you reference it?",
                "lesson": (
                    "Bash positional parameters — accessing script arguments.\n\n"
                    "  $0   script name itself\n"
                    "  $1   first argument\n"
                    "  $2   second argument\n"
                    "  $@   all arguments as separate words\n"
                    "  $*   all arguments as a single word\n"
                    "  $#   number of arguments\n\n"
                    "Example script:\n"
                    "  #!/bin/bash\n"
                    "  HOST=$1\n"
                    "  echo \"Connecting to $HOST\"\n"
                    "  ssh operative@$HOST\n\n"
                    "Called as: ./connect.sh 10.0.1.88\n"
                    "Result: Connecting to 10.0.1.88\n\n"
                    "Validate arguments:\n"
                    "  if [ -z \"$1\" ]; then\n"
                    "    echo \"Usage: $0 <host>\"\n"
                    "    exit 1\n"
                    "  fi"
                ),
                "question": "Inside a bash script, what variable holds the first command-line argument passed to the script?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["$1"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Positional parameters use $ followed by position number.",
                    "First argument: $1",
                    "The answer is: $1",
                ],
            },
            {
                "id": "bash_3",
                "type": "fill_blank",
                "title": "Exit Codes",
                "flavor": "The deployment script needs to stop immediately if the archive step fails. Exit codes are how programs signal success or failure. Zero means clean.",
                "lesson": (
                    "Exit codes — every command returns a numeric exit status.\n\n"
                    "  0     success\n"
                    "  1-255 failure (non-zero)\n\n"
                    "Checking exit codes:\n"
                    "  $?   holds the exit code of the last command\n\n"
                    "set -e — exits the script immediately on any error:\n"
                    "  #!/bin/bash\n"
                    "  set -e\n"
                    "  tar -czf archive.tar.gz /data/    # script stops here if tar fails\n"
                    "  scp archive.tar.gz user@host:/backup/\n\n"
                    "Explicit exit:\n"
                    "  exit 0   → success\n"
                    "  exit 1   → general error\n\n"
                    "Conditional on exit code:\n"
                    "  if ! tar -czf archive.tar.gz /data/; then\n"
                    "    echo 'Archive failed'\n"
                    "    exit 1\n"
                    "  fi"
                ),
                "question": (
                    "What exit code indicates successful completion of a command in bash?\n\n"
                    "Answer: ___"
                ),
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["0"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Success is represented by zero.",
                    "0",
                    "The answer is: 0",
                ],
            },
            {
                "id": "bash_4",
                "type": "fill_blank",
                "title": "Conditional Logic",
                "flavor": "The script needs to check whether the evidence file exists before attempting to compress it. If the file is missing, bail with an error message.",
                "lesson": (
                    "if/elif/else — conditional execution in bash.\n\n"
                    "Syntax:\n"
                    "  if [ condition ]; then\n"
                    "    commands\n"
                    "  elif [ other_condition ]; then\n"
                    "    commands\n"
                    "  else\n"
                    "    commands\n"
                    "  fi\n\n"
                    "Common test flags:\n"
                    "  -f file   file exists and is a regular file\n"
                    "  -d dir    directory exists\n"
                    "  -z str    string is empty\n"
                    "  -n str    string is non-empty\n"
                    "  -eq       numeric equal\n"
                    "  -gt       numeric greater than\n\n"
                    "Example:\n"
                    "  if [ -f /evidence/data.tar.gz ]; then\n"
                    "    echo 'Found archive, transferring...'\n"
                    "  else\n"
                    "    echo 'Archive missing'\n"
                    "    exit 1\n"
                    "  fi"
                ),
                "question": (
                    "Complete the test flag to check if a file exists in a bash conditional:\n\n"
                    "if [ ___ /evidence/data.tar.gz ]; then"
                ),
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["-f", "! -f"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "File existence test flag: a single letter preceded by dash.",
                    "-f tests for regular file existence.",
                    "The answer is: -f",
                ],
            },
            {
                "id": "bash_5",
                "type": "quiz",
                "title": "Loop Over Files",
                "flavor": "The clean-up script needs to iterate over every .log file in /var/log/nexus/ and compress each one. A for loop with glob expansion handles this cleanly.",
                "lesson": (
                    "for loop — iterates over a list of items.\n\n"
                    "Syntax:\n"
                    "  for variable in list; do\n"
                    "    commands\n"
                    "  done\n\n"
                    "Glob expansion:\n"
                    "  for f in /var/log/nexus/*.log; do\n"
                    "    gzip \"$f\"\n"
                    "  done\n\n"
                    "Command substitution:\n"
                    "  for host in $(cat hosts.txt); do\n"
                    "    ssh operative@$host 'uname -a'\n"
                    "  done\n\n"
                    "Numeric range:\n"
                    "  for i in {1..10}; do\n"
                    "    echo \"Step $i\"\n"
                    "  done\n\n"
                    "Always quote variables inside loops: \"$f\", \"$host\"\n"
                    "to handle filenames with spaces correctly."
                ),
                "question": "In a bash for loop, what keyword ends the loop body?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["done"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The closing keyword for a for/while loop.",
                    "done",
                    "The answer is: done",
                ],
            },
            {
                "id": "bash_boss",
                "type": "fill_blank",
                "title": "BOSS: Defensive Script",
                "flavor": "CIPHER: 'Write the variable assignment that captures the first script argument into a variable named TARGET. Then I can build the rest of the script around it.'",
                "lesson": (
                    "Variable assignment and positional parameters — core bash building blocks.\n\n"
                    "Variable assignment:\n"
                    "  NAME=value         → assign value (no spaces around =)\n"
                    "  NAME=\"value\"       → quote if value has spaces\n"
                    "  NAME=$(command)    → capture command output\n\n"
                    "Accessing variables:\n"
                    "  $NAME or ${NAME}   → expand variable value\n"
                    "  ${NAME:-default}   → use 'default' if NAME is unset\n\n"
                    "Combining with $1:\n"
                    "  TARGET=$1                    → capture first argument\n"
                    "  TARGET=${1:-localhost}        → use localhost if no arg given\n\n"
                    "Full pattern:\n"
                    "  #!/bin/bash\n"
                    "  set -e\n"
                    "  TARGET=$1\n"
                    "  if [ -z \"$TARGET\" ]; then\n"
                    "    echo \"Usage: $0 <host>\"\n"
                    "    exit 1\n"
                    "  fi\n"
                    "  echo \"Connecting to $TARGET\""
                ),
                "question": (
                    "Complete the assignment to store the first script argument in a variable called TARGET:\n\n"
                    "TARGET=___"
                ),
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": ["$1", "${1}"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "First positional parameter.",
                    "$1",
                    "The answer is: $1",
                ],
            },
        ],
    },
}

ZONE_ORDER = [
    "user_management",
    "file_permissions",
    "process_mastery",
    "disk_and_storage",
    "network_diagnostics",
    "log_analysis",
    "shell_configuration",
    "package_management",
    "systemd_services",
    "text_processing",
    "archive_and_compression",
    "cron_and_scheduling",
    "bash_scripting_basics",
]
