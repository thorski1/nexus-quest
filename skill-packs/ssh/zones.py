"""
zones.py - All zone and challenge data for SSH Quest
Challenge types: quiz, fill_blank, flag_quiz
"""

ZONES = {
    "connection_basics": {
        "id": "connection_basics",
        "name": "Connection Basics",
        "subtitle": "Connecting to Remote Hosts",
        "color": "cyan",
        "icon": "🔗",
        "commands": ["ssh user@host", "-p port", "-i key", "-v", "exit"],
        "challenges": [
            {
                "id": "cb_1",
                "type": "fill_blank",
                "title": "Basic Connection",
                "flavor": "Connect to the NEXUS jump host at jump.nexus.internal as user 'admin'. Complete: ssh ___",
                "lesson": (
                    "ssh user@hostname — basic SSH connection syntax.\n\n"
                    "  ssh admin@jump.nexus.internal\n\n"
                    "What happens on first connection:\n"
                    "  1. SSH connects to port 22 by default\n"
                    "  2. Server sends its host key fingerprint\n"
                    "  3. You verify (or accept) the fingerprint\n"
                    "  4. It's stored in ~/.ssh/known_hosts for future comparisons\n"
                    "  5. Authentication (password or key)\n"
                    "  6. Shell session begins\n\n"
                    "The known_hosts file prevents MITM attacks:\n"
                    "  If the server's fingerprint changes, SSH warns you.\n"
                    "  This is why you should verify fingerprints out-of-band\n"
                    "  on first connection — not just type 'yes' automatically."
                ),
                "answer": "admin@jump.nexus.internal",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["Format is user@hostname.", "The answer is: admin@jump.nexus.internal"],
            },
            {
                "id": "cb_2",
                "type": "flag_quiz",
                "title": "Custom Port",
                "flavor": "The NEXUS SSH server runs on port 2222 instead of 22. What flag specifies the port?",
                "lesson": (
                    "-p — specify the SSH port (default is 22).\n\n"
                    "  ssh -p 2222 admin@host\n\n"
                    "Running SSH on a non-standard port:\n"
                    "  - Does NOT improve security significantly\n"
                    "  - Does reduce noise from automated scanners\n"
                    "  - Is common in organizations trying to reduce\n"
                    "    failed login log entries\n\n"
                    "The -p flag is case-sensitive:\n"
                    "  -p → port (lowercase)\n"
                    "  -P → no such flag in basic ssh (but scp uses -P for port)\n\n"
                    "In ~/.ssh/config, specify port as:\n"
                    "  Port 2222"
                ),
                "answer": "-p",
                "hints": ["Lowercase -p for port.", "The answer is: -p"],
            },
            {
                "id": "cb_3",
                "type": "flag_quiz",
                "title": "Specify Key File",
                "flavor": "You want to authenticate with a specific private key file at ~/keys/nexus_rsa. What flag specifies the identity (key) file?",
                "lesson": (
                    "-i — specify the identity file (private key) to use.\n\n"
                    "  ssh -i ~/keys/nexus_rsa admin@host\n\n"
                    "By default, SSH tries keys in this order:\n"
                    "  ~/.ssh/id_rsa\n"
                    "  ~/.ssh/id_ecdsa\n"
                    "  ~/.ssh/id_ed25519\n"
                    "  ~/.ssh/id_dsa (deprecated)\n\n"
                    "-i overrides this, pointing to a specific key file.\n\n"
                    "In ~/.ssh/config:\n"
                    "  IdentityFile ~/keys/nexus_rsa\n\n"
                    "The file permissions on the key matter:\n"
                    "  chmod 600 ~/.ssh/id_rsa  → required; SSH refuses to use world-readable keys"
                ),
                "answer": "-i",
                "hints": ["Think: identity file. Single flag.", "The answer is: -i"],
            },
            {
                "id": "cb_4",
                "type": "fill_blank",
                "title": "Run Remote Command",
                "flavor": "You want to run 'ls /etc/nexus' on the remote host without starting an interactive shell. Complete: ssh admin@host ___",
                "lesson": (
                    "ssh user@host command — run a single command on the remote host.\n\n"
                    "  ssh admin@host ls /etc/nexus\n\n"
                    "The command runs on the remote host, output appears locally.\n"
                    "No interactive shell is started — the connection closes when the command exits.\n\n"
                    "Useful patterns:\n"
                    "  ssh host 'cat /etc/passwd'          → read a remote file\n"
                    "  ssh host 'df -h'                    → check disk usage remotely\n"
                    "  ssh host 'systemctl status nexus'   → check service status\n\n"
                    "Quoting matters:\n"
                    "  ssh host 'echo $HOME'   → $HOME expands on the REMOTE host\n"
                    "  ssh host \"echo $HOME\"  → $HOME expands on the LOCAL host\n"
                    "  (single quotes prevent local shell expansion)"
                ),
                "answer": "ls /etc/nexus",
                "hints": ["Just append the command after the host.", "The answer is: ls /etc/nexus"],
            },
            {
                "id": "cb_5",
                "type": "flag_quiz",
                "title": "Verbose Mode",
                "flavor": "The connection is failing silently. You need to see the debug output — what's happening during the handshake and authentication. What flag enables verbose/debug output?",
                "lesson": (
                    "-v — verbose mode: print debug information.\n\n"
                    "  ssh -v admin@host    → verbose (basic debug)\n"
                    "  ssh -vv admin@host   → more verbose\n"
                    "  ssh -vvv admin@host  → maximum verbosity\n\n"
                    "What -v shows:\n"
                    "  - Which host keys are being read\n"
                    "  - Which authentication methods are being tried\n"
                    "  - Which key files are being offered\n"
                    "  - The exact point where authentication fails\n\n"
                    "Common failure diagnoses from -v:\n"
                    "  'No more authentication methods' → all methods tried, none worked\n"
                    "  'Permission denied (publickey)' → key auth required but key not accepted\n"
                    "  'Offending key in ~/.ssh/known_hosts:42' → host key mismatch"
                ),
                "answer": "-v",
                "hints": ["Single flag for verbose/debug output.", "The answer is: -v"],
            },
            {
                "id": "cb_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Full Connection Command",
                "flavor": "Connect to host 'db.nexus.internal' as 'admin', on port 2222, using key file '~/.ssh/nexus_key', in verbose mode. Write the complete ssh command:",
                "lesson": (
                    "Combining multiple flags:\n\n"
                    "  ssh -v -i ~/.ssh/nexus_key -p 2222 admin@db.nexus.internal\n\n"
                    "Flags can be combined or separate:\n"
                    "  ssh -vi ~/.ssh/nexus_key -p 2222 admin@host   → same result\n\n"
                    "Order matters for positional arguments but not flags:\n"
                    "  The hostname must come before any remote command\n"
                    "  Flags can appear in any order before the hostname\n\n"
                    "This kind of explicit command is useful for debugging.\n"
                    "Once it works, encode it in ~/.ssh/config:\n"
                    "  Host nexus-db\n"
                    "    HostName db.nexus.internal\n"
                    "    User admin\n"
                    "    Port 2222\n"
                    "    IdentityFile ~/.ssh/nexus_key"
                ),
                "answer": "ssh -v -i ~/.ssh/nexus_key -p 2222 admin@db.nexus.internal",
                "hints": [
                    "Combine -v, -i keyfile, -p port, and user@host.",
                    "The answer is: ssh -v -i ~/.ssh/nexus_key -p 2222 admin@db.nexus.internal",
                ],
            },
        ],
    },
    "key_vault": {
        "id": "key_vault",
        "name": "The Key Vault",
        "subtitle": "Key Pairs, authorized_keys & Key Management",
        "color": "yellow",
        "icon": "🗝️",
        "commands": ["ssh-keygen", "ssh-copy-id", "authorized_keys", "known_hosts", "chmod 600"],
        "challenges": [
            {
                "id": "kv_1",
                "type": "quiz",
                "title": "Generate a Key Pair",
                "flavor": "You need to generate a new SSH key pair. What command does this?",
                "lesson": (
                    "ssh-keygen — generate a new SSH key pair.\n\n"
                    "Basic usage:\n"
                    "  ssh-keygen              → interactive, asks for filename and passphrase\n"
                    "  ssh-keygen -t ed25519   → generate Ed25519 key (recommended)\n"
                    "  ssh-keygen -t rsa -b 4096  → generate 4096-bit RSA key\n\n"
                    "Key types (modern recommendations):\n"
                    "  ed25519  → best: small key, strong, modern (use this)\n"
                    "  ecdsa    → good: elliptic curve\n"
                    "  rsa      → widely compatible but larger keys needed (4096 minimum)\n"
                    "  dsa      → deprecated; don't use\n\n"
                    "Output:\n"
                    "  ~/.ssh/id_ed25519      → private key (NEVER share this)\n"
                    "  ~/.ssh/id_ed25519.pub  → public key (this goes on the server)"
                ),
                "answer": "ssh-keygen",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["The command that generates SSH keys.", "The answer is: ssh-keygen"],
            },
            {
                "id": "kv_2",
                "type": "quiz",
                "title": "Copy Key to Server",
                "flavor": "You've generated a key pair. You want to install your public key on the remote server so you can authenticate with it. What command automates this?",
                "lesson": (
                    "ssh-copy-id — copy your public key to a remote server's authorized_keys.\n\n"
                    "  ssh-copy-id user@host\n"
                    "  ssh-copy-id -i ~/.ssh/nexus_key.pub user@host  → specify key file\n\n"
                    "What it does:\n"
                    "  1. Reads your public key (~/.ssh/id_*.pub by default)\n"
                    "  2. SSH's into the server (using password or existing key)\n"
                    "  3. Appends the key to ~/.ssh/authorized_keys on the server\n"
                    "  4. Sets correct permissions on the file\n\n"
                    "Manual equivalent:\n"
                    "  cat ~/.ssh/id_ed25519.pub | ssh user@host 'cat >> ~/.ssh/authorized_keys'\n\n"
                    "After ssh-copy-id:\n"
                    "  You can log in with the key — password no longer required."
                ),
                "answer": "ssh-copy-id",
                "hints": ["The command that copies the public key to the server.", "The answer is: ssh-copy-id"],
            },
            {
                "id": "kv_3",
                "type": "fill_blank",
                "title": "Key File Permissions",
                "flavor": "Your private key file is too permissive and SSH refuses to use it. What chmod command sets the correct permissions?",
                "lesson": (
                    "chmod 600 ~/.ssh/id_rsa — set private key to owner read/write only.\n\n"
                    "SSH enforces strict permissions on key files:\n"
                    "  Private key:     chmod 600  (rw-------)\n"
                    "  ~/.ssh/ dir:     chmod 700  (rwx------)\n"
                    "  authorized_keys: chmod 600  (rw-------)\n"
                    "  Public key:      chmod 644  (rw-r--r--) — less critical\n\n"
                    "If permissions are too open, SSH refuses to use the key:\n"
                    "  'Permissions 0644 for ~/.ssh/id_rsa are too open.'\n"
                    "  'It is required that your private key files are NOT accessible\n"
                    "   by others.'\n\n"
                    "This is a security feature, not a bug — a world-readable private\n"
                    "key would mean anyone on the system could steal it."
                ),
                "answer": "chmod 600 ~/.ssh/id_rsa",
                "hints": [
                    "chmod with octal permissions — owner read/write, nothing for group/others.",
                    "The answer is: chmod 600 ~/.ssh/id_rsa",
                ],
            },
            {
                "id": "kv_4",
                "type": "quiz",
                "title": "Where Are Authorized Keys?",
                "flavor": "You need to add a public key so it's trusted for authentication on a server. In which file do you append the public key?",
                "lesson": (
                    "~/.ssh/authorized_keys — the file that lists trusted public keys.\n\n"
                    "Location: ~/.ssh/authorized_keys on the REMOTE server\n"
                    "  (in the home directory of the user being authenticated as)\n\n"
                    "Format: one public key per line\n"
                    "  ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExample user@machine\n\n"
                    "Forensic value: authorized_keys that contain keys for users who\n"
                    "no longer exist, or keys that weren't added through the normal\n"
                    "provisioning process, are strong indicators of unauthorized access\n"
                    "or persistent backdoors.\n\n"
                    "NEXUS has four servers where authorized_keys contains keys\n"
                    "not in the official key management system. They've been there\n"
                    "for eighteen months."
                ),
                "answer": "authorized_keys",
                "hints": ["The filename in ~/.ssh/ that lists allowed keys.", "The answer is: authorized_keys"],
            },
            {
                "id": "kv_5",
                "type": "quiz",
                "title": "Generate Ed25519 Key",
                "flavor": "What flag specifies the key type when running ssh-keygen? (For example, to generate an Ed25519 key)",
                "lesson": (
                    "-t — specify the key type for ssh-keygen.\n\n"
                    "  ssh-keygen -t ed25519        → generate Ed25519 key (recommended)\n"
                    "  ssh-keygen -t rsa -b 4096    → generate RSA key, 4096 bits\n"
                    "  ssh-keygen -t ecdsa          → generate ECDSA key\n\n"
                    "Why Ed25519:\n"
                    "  - Small key size (only 68 characters for the public key)\n"
                    "  - Strong cryptography (Curve25519 + EdDSA)\n"
                    "  - Fast to verify\n"
                    "  - Resistant to timing attacks\n"
                    "  - Supported by all modern SSH implementations\n\n"
                    "RSA is still acceptable if compatibility with older systems\n"
                    "is required, but use at least 4096 bits (-b 4096).\n"
                    "DSA is cryptographically broken. Never use it."
                ),
                "answer": "-t",
                "hints": ["The flag specifying the key type.", "The answer is: -t"],
            },
            {
                "id": "kv_6",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Generate Non-Default Key",
                "flavor": "Generate an Ed25519 key, saving it to ~/.ssh/nexus_ed25519 (not the default location), with the comment 'nexus-op'. Write the full ssh-keygen command:",
                "lesson": (
                    "ssh-keygen -t ed25519 -f filename -C comment\n\n"
                    "  ssh-keygen -t ed25519 -f ~/.ssh/nexus_ed25519 -C 'nexus-op'\n\n"
                    "Flags:\n"
                    "  -t → key type\n"
                    "  -f → output filename (private key; .pub added automatically for public)\n"
                    "  -C → comment (appears at the end of the public key)\n"
                    "  -N → passphrase (use '' for no passphrase; -N '' for non-interactive)\n"
                    "  -b → bit size (for RSA; ed25519 ignores this)\n\n"
                    "Non-default filename use cases:\n"
                    "  - Multiple keys for different servers\n"
                    "  - Organized key naming convention\n"
                    "  - Testing without overwriting existing keys\n\n"
                    "Use -i ~/.ssh/nexus_ed25519 when connecting, or add IdentityFile\n"
                    "to ~/.ssh/config for the relevant Host entry."
                ),
                "answer": "ssh-keygen -t ed25519 -f ~/.ssh/nexus_ed25519 -C 'nexus-op'",
                "hints": [
                    "Use -t ed25519, -f for file, -C for comment.",
                    "The answer is: ssh-keygen -t ed25519 -f ~/.ssh/nexus_ed25519 -C 'nexus-op'",
                ],
            },
        ],
    },
    "config_matrix": {
        "id": "config_matrix",
        "name": "The Config Matrix",
        "subtitle": "~/.ssh/config & Host Aliases",
        "color": "green",
        "icon": "📋",
        "commands": ["Host", "HostName", "User", "IdentityFile", "ProxyJump", "Port"],
        "challenges": [
            {
                "id": "cfg_1",
                "type": "quiz",
                "title": "The Config File",
                "flavor": "SSH can be configured to remember settings for each host. Where is the per-user SSH client configuration file?",
                "lesson": (
                    "~/.ssh/config — the SSH client configuration file.\n\n"
                    "Structure:\n"
                    "  Host alias\n"
                    "    HostName actual.hostname.or.ip\n"
                    "    User username\n"
                    "    Port 22\n"
                    "    IdentityFile ~/.ssh/key_file\n\n"
                    "After adding a Host entry, you connect with just the alias:\n"
                    "  Host nexus-db\n"
                    "    HostName db.nexus.internal\n"
                    "    User admin\n"
                    "    IdentityFile ~/.ssh/nexus_key\n\n"
                    "  → ssh nexus-db   (equivalent to: ssh -i ~/.ssh/nexus_key admin@db.nexus.internal)\n\n"
                    "Host * (wildcard):\n"
                    "  Applies settings to ALL connections — useful for defaults like\n"
                    "  ServerAliveInterval or AddKeysToAgent."
                ),
                "answer": "~/.ssh/config",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["It's in the .ssh directory in your home folder.", "The answer is: ~/.ssh/config"],
            },
            {
                "id": "cfg_2",
                "type": "quiz",
                "title": "The HostName Directive",
                "flavor": "In ~/.ssh/config, you want to set the actual hostname or IP for a Host alias. What directive specifies the real hostname?",
                "lesson": (
                    "HostName — the actual hostname or IP address to connect to.\n\n"
                    "The Host line is the alias. HostName is the actual target.\n\n"
                    "  Host jump            → the alias you type\n"
                    "  HostName 10.0.1.5   → the actual IP SSH connects to\n\n"
                    "This allows:\n"
                    "  ssh jump   → connects to 10.0.1.5\n\n"
                    "Why this matters:\n"
                    "  - Human-readable names for hard-to-remember IPs\n"
                    "  - Aliases for long hostnames\n"
                    "  - Change the real IP without changing scripts that use the alias\n\n"
                    "If HostName is omitted, the Host value is used as the hostname\n"
                    "(useful when the alias IS the hostname you want to connect to)."
                ),
                "answer": "HostName",
                "hints": ["The directive for the actual hostname/IP in a Host block.", "The answer is: HostName"],
            },
            {
                "id": "cfg_3",
                "type": "quiz",
                "title": "Proxy Jump Directive",
                "flavor": "The database server is only reachable through the bastion host. What ~/.ssh/config directive sets a jump host for a connection?",
                "lesson": (
                    "ProxyJump — specify a jump host (bastion) for the connection.\n\n"
                    "  Host nexus-db\n"
                    "    HostName db.nexus.internal\n"
                    "    User admin\n"
                    "    ProxyJump bastion\n\n"
                    "  ssh nexus-db → connects through the 'bastion' host first\n\n"
                    "Multiple jump hosts (chain of proxies):\n"
                    "  ProxyJump bastion1,bastion2\n\n"
                    "The ProxyJump host must itself be defined in ~/.ssh/config\n"
                    "(or reachable directly).\n\n"
                    "Older equivalent (ProxyCommand):\n"
                    "  ProxyCommand ssh -W %h:%p bastion\n"
                    "  (ProxyJump is cleaner and preferred since OpenSSH 7.3)"
                ),
                "answer": "ProxyJump",
                "hints": ["The directive that specifies a jump/bastion host.", "The answer is: ProxyJump"],
            },
            {
                "id": "cfg_4",
                "type": "quiz",
                "title": "Keep Connection Alive",
                "flavor": "Your SSH sessions keep dropping due to inactivity timeouts. What config directive sends periodic keepalive packets to prevent this?",
                "lesson": (
                    "ServerAliveInterval — send keepalive packets at a regular interval.\n\n"
                    "  Host *\n"
                    "    ServerAliveInterval 60\n"
                    "    ServerAliveCountMax 3\n\n"
                    "  ServerAliveInterval 60  → send a keepalive packet every 60 seconds\n"
                    "  ServerAliveCountMax 3   → disconnect after 3 missed responses\n\n"
                    "This prevents:\n"
                    "  - NAT timeouts on routers and firewalls\n"
                    "  - Cloud load balancers closing idle connections\n"
                    "  - Long-running sessions getting dropped during inactivity\n\n"
                    "The Host * block applies to ALL connections:\n"
                    "  Host *\n"
                    "    ServerAliveInterval 60\n"
                    "  This sets keepalive globally without repeating it per host."
                ),
                "answer": "ServerAliveInterval",
                "hints": ["The directive for keepalive intervals — two words joined.", "The answer is: ServerAliveInterval"],
            },
            {
                "id": "cfg_5",
                "type": "quiz",
                "title": "Auto-Add Keys to Agent",
                "flavor": "What config directive automatically adds a key to ssh-agent when it's first used, so you don't need to run ssh-add manually?",
                "lesson": (
                    "AddKeysToAgent — automatically add keys to the SSH agent on first use.\n\n"
                    "  Host *\n"
                    "    AddKeysToAgent yes\n\n"
                    "  yes  → add key to agent on first use\n"
                    "  ask  → prompt before adding\n"
                    "  no   → don't add (default)\n\n"
                    "Pairing with UseKeychain (macOS):\n"
                    "  Host *\n"
                    "    AddKeysToAgent yes\n"
                    "    UseKeychain yes\n"
                    "    IdentityFile ~/.ssh/id_ed25519\n\n"
                    "  → macOS Keychain stores the passphrase, agent gets the key automatically,\n"
                    "    no typing required after the first connection."
                ),
                "answer": "AddKeysToAgent",
                "hints": ["The directive that adds keys to the agent automatically.", "The answer is: AddKeysToAgent"],
            },
            {
                "id": "cfg_6",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Full Config Entry",
                "flavor": "Write a complete ~/.ssh/config entry: alias 'nexus-db', real host '10.20.30.40', user 'admin', port 2222, key '~/.ssh/nexus_key', through jump host 'nexus-jump':",
                "lesson": (
                    "Complete ~/.ssh/config Host entry:\n\n"
                    "  Host nexus-db\n"
                    "    HostName 10.20.30.40\n"
                    "    User admin\n"
                    "    Port 2222\n"
                    "    IdentityFile ~/.ssh/nexus_key\n"
                    "    ProxyJump nexus-jump\n\n"
                    "After this entry, all of these are equivalent:\n"
                    "  ssh nexus-db\n"
                    "  ssh -p 2222 -i ~/.ssh/nexus_key -J nexus-jump admin@10.20.30.40\n\n"
                    "The config file is the most powerful SSH convenience feature.\n"
                    "It turns complex multi-flag commands into single-word connections\n"
                    "and self-documents the infrastructure."
                ),
                "answer": "Host nexus-db",
                "hints": [
                    "The first line of any config entry is the Host directive.",
                    "The answer is the first line: Host nexus-db",
                ],
            },
        ],
    },
    "transfer_ops": {
        "id": "transfer_ops",
        "name": "Transfer Operations",
        "subtitle": "scp, rsync & sftp",
        "color": "blue",
        "icon": "📤",
        "commands": ["scp", "rsync -avz", "sftp", "-r", "remote:path"],
        "challenges": [
            {
                "id": "tr_1",
                "type": "fill_blank",
                "title": "Copy File to Remote",
                "flavor": "Copy the local file 'payload.sh' to /tmp/ on host 'admin@nexus-jump'. Complete: scp payload.sh ___",
                "lesson": (
                    "scp source destination — secure copy using SSH.\n\n"
                    "  scp payload.sh admin@nexus-jump:/tmp/\n\n"
                    "Remote path syntax: user@host:/path\n"
                    "  Local to remote: scp local_file user@host:/remote/path/\n"
                    "  Remote to local: scp user@host:/remote/file ./local_path/\n"
                    "  Remote to remote: scp user1@host1:/path user2@host2:/path\n\n"
                    "Key flags:\n"
                    "  -r  → copy recursively (for directories)\n"
                    "  -p  → preserve file timestamps and permissions\n"
                    "  -P  → port (uppercase P for scp, vs lowercase -p for ssh)\n"
                    "  -i  → identity file (same as ssh -i)\n\n"
                    "Note: scp uses the same ~/.ssh/config entries as ssh."
                ),
                "answer": "admin@nexus-jump:/tmp/",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["Remote destination: user@host:/path/", "The answer is: admin@nexus-jump:/tmp/"],
            },
            {
                "id": "tr_2",
                "type": "fill_blank",
                "title": "Copy from Remote",
                "flavor": "Copy the routing table at /var/lib/nexus/routes.db from 'admin@nexus-db' to the current directory. Complete: scp ___ .",
                "lesson": (
                    "scp user@host:/remote/path ./local_path — copy from remote to local.\n\n"
                    "  scp admin@nexus-db:/var/lib/nexus/routes.db .\n\n"
                    "The dot (.) at the end means 'current directory'.\n\n"
                    "Directory copy (recursive):\n"
                    "  scp -r admin@host:/var/lib/nexus/ ./nexus_backup/\n\n"
                    "scp limitations:\n"
                    "  - No progress display for large files (use rsync for that)\n"
                    "  - No resume capability\n"
                    "  - Slower than rsync for many small files\n"
                    "  - Being deprecated in some distros in favor of sftp/rsync\n\n"
                    "For large transfers, rsync is preferred:\n"
                    "  rsync -avz --progress admin@host:/var/lib/nexus/routes.db ."
                ),
                "answer": "admin@nexus-db:/var/lib/nexus/routes.db",
                "hints": ["Source is user@host:/path", "The answer is: admin@nexus-db:/var/lib/nexus/routes.db"],
            },
            {
                "id": "tr_3",
                "type": "fill_blank",
                "title": "Rsync with Compression",
                "flavor": "Sync a large remote directory '/var/log/nexus/' from admin@nexus-app to './nexus_logs/' with verbose output, archive mode, and compression. Complete: rsync ___",
                "lesson": (
                    "rsync -avz source destination — archive, verbose, compressed sync.\n\n"
                    "  rsync -avz admin@nexus-app:/var/log/nexus/ ./nexus_logs/\n\n"
                    "Flag breakdown:\n"
                    "  -a → archive mode: preserves permissions, timestamps, symlinks,\n"
                    "       owner, group, device files (equivalent to -rlptgoD)\n"
                    "  -v → verbose: show what's being transferred\n"
                    "  -z → compress during transfer (faster over slow connections)\n\n"
                    "Additional useful flags:\n"
                    "  --progress → show transfer progress per file\n"
                    "  --partial  → keep partial transfers (enables resume)\n"
                    "  -e ssh     → explicitly use SSH (default, but sometimes needed)\n"
                    "  --exclude  → exclude patterns\n"
                    "  --delete   → delete files in destination not in source\n\n"
                    "rsync only transfers changed parts of files — much faster than scp for large files."
                ),
                "answer": "-avz admin@nexus-app:/var/log/nexus/ ./nexus_logs/",
                "hints": ["Flags -avz, then remote source, then local destination.", "The answer is: -avz admin@nexus-app:/var/log/nexus/ ./nexus_logs/"],
            },
            {
                "id": "tr_4",
                "type": "quiz",
                "title": "Interactive File Transfer",
                "flavor": "You need an interactive file transfer session where you can list directories, navigate, and transfer files one at a time. What command gives you an interactive FTP-like session over SSH?",
                "lesson": (
                    "sftp — interactive secure file transfer session over SSH.\n\n"
                    "  sftp admin@nexus-db\n\n"
                    "At the sftp> prompt:\n"
                    "  ls         → list remote directory\n"
                    "  lls        → list LOCAL directory\n"
                    "  cd path    → change remote directory\n"
                    "  lcd path   → change local directory\n"
                    "  get file   → download file from remote\n"
                    "  put file   → upload file to remote\n"
                    "  get -r dir → download directory recursively\n"
                    "  pwd        → print remote working directory\n"
                    "  lpwd       → print local working directory\n"
                    "  exit       → close the sftp session\n\n"
                    "sftp is useful when you don't know the exact path\n"
                    "and need to explore the remote filesystem interactively."
                ),
                "answer": "sftp",
                "hints": ["The S stands for Secure — an FTP-like session over SSH.", "The answer is: sftp"],
            },
            {
                "id": "tr_5",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Rsync with Port",
                "flavor": "Rsync the directory /var/lib/nexus/ from admin@nexus-db (SSH on port 2222) to ./evidence/. You need to specify the port. Complete: rsync -avz -e ___ admin@nexus-db:/var/lib/nexus/ ./evidence/",
                "lesson": (
                    "rsync -e 'ssh -p PORT' — specify SSH options for rsync's transport.\n\n"
                    "  rsync -avz -e 'ssh -p 2222' admin@nexus-db:/var/lib/nexus/ ./evidence/\n\n"
                    "The -e flag specifies the remote shell command to use.\n"
                    "Since rsync uses SSH by default, -e 'ssh -p 2222' overrides the SSH command\n"
                    "to include the port flag.\n\n"
                    "You can pass any SSH flags this way:\n"
                    "  -e 'ssh -p 2222 -i ~/.ssh/nexus_key'\n"
                    "  -e 'ssh -p 2222 -o StrictHostKeyChecking=no'\n\n"
                    "If the host is already in ~/.ssh/config with the Port directive,\n"
                    "rsync will pick it up automatically without needing -e."
                ),
                "answer": "'ssh -p 2222'",
                "hints": [
                    "The -e flag takes a quoted SSH command with the port flag.",
                    "The answer is: 'ssh -p 2222'",
                ],
            },
        ],
    },
    "tunnel_network": {
        "id": "tunnel_network",
        "name": "The Tunnel Network",
        "subtitle": "Port Forwarding & SSH Tunnels",
        "color": "red",
        "icon": "🚇",
        "commands": ["-L local forward", "-R remote forward", "-D SOCKS", "-N", "-f"],
        "challenges": [
            {
                "id": "tn_1",
                "type": "flag_quiz",
                "title": "Local Port Forward",
                "flavor": "You want to forward a remote port to your local machine. What flag sets up a local port forward?",
                "lesson": (
                    "-L — local port forwarding: forward a local port to a remote destination.\n\n"
                    "Syntax: -L [localIP:]localPort:remoteHost:remotePort\n\n"
                    "  ssh -L 5432:db.internal:5432 admin@jumphost\n\n"
                    "What this does:\n"
                    "  - Opens port 5432 on YOUR machine (localhost)\n"
                    "  - Any connection to localhost:5432 is tunneled through\n"
                    "    the SSH connection to the jumphost\n"
                    "  - The jumphost connects to db.internal:5432 on your behalf\n"
                    "  - From your machine, the database appears to be on localhost\n\n"
                    "The firewall sees: one SSH connection on port 22 to jumphost.\n"
                    "It does not see: the database connection running inside the tunnel."
                ),
                "answer": "-L",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["'L' for Local port forwarding.", "The answer is: -L"],
            },
            {
                "id": "tn_2",
                "type": "fill_blank",
                "title": "Forward the Database Port",
                "flavor": "Forward local port 5432 to db.nexus.internal:5432 through admin@nexus-jump. Complete the -L argument: -L ___",
                "lesson": (
                    "Local port forward syntax: localPort:remoteHost:remotePort\n\n"
                    "  ssh -L 5432:db.nexus.internal:5432 admin@nexus-jump\n\n"
                    "After this command:\n"
                    "  psql -h localhost -p 5432 → connects to db.nexus.internal:5432\n\n"
                    "The three parts of -L localPort:remoteHost:remotePort:\n"
                    "  5432             → local port on your machine\n"
                    "  db.nexus.internal → the remote host (resolved from jumphost's perspective)\n"
                    "  5432             → the remote port\n\n"
                    "The remote host is resolved from the SSH server's perspective:\n"
                    "  'localhost' in this position means the SSH server itself\n"
                    "  'db.nexus.internal' means whatever that resolves to from nexus-jump"
                ),
                "answer": "5432:db.nexus.internal:5432",
                "hints": ["Format: localPort:remoteHost:remotePort", "The answer is: 5432:db.nexus.internal:5432"],
            },
            {
                "id": "tn_3",
                "type": "flag_quiz",
                "title": "No Shell (Tunnel Only)",
                "flavor": "You want to set up a port forward but don't need an interactive shell — just the tunnel. What flag tells SSH not to execute a remote command?",
                "lesson": (
                    "-N — do not execute a remote command; tunnel only.\n\n"
                    "  ssh -N -L 5432:db.internal:5432 admin@jumphost\n\n"
                    "Without -N: SSH opens a shell session AND sets up the tunnel.\n"
                    "With -N: SSH only sets up the tunnel, no shell.\n\n"
                    "Combined with -f (background):\n"
                    "  ssh -fN -L 5432:db.internal:5432 admin@jumphost\n\n"
                    "  -f → go to background after authentication\n"
                    "  -N → no command/shell\n\n"
                    "Together: -fN creates a background tunnel that stays running\n"
                    "without tying up a terminal. Stop it with:\n"
                    "  ps aux | grep 'ssh -fN'\n"
                    "  kill <pid>"
                ),
                "answer": "-N",
                "hints": ["The flag that means 'no command, tunnel only'.", "The answer is: -N"],
            },
            {
                "id": "tn_4",
                "type": "flag_quiz",
                "title": "SOCKS Proxy",
                "flavor": "You want to route all traffic from a browser through an SSH server using a dynamic SOCKS proxy. What flag creates a dynamic SOCKS proxy?",
                "lesson": (
                    "-D — dynamic port forwarding: creates a local SOCKS proxy server.\n\n"
                    "  ssh -D 1080 admin@jumphost\n\n"
                    "What this does:\n"
                    "  - Opens a SOCKS5 proxy on localhost:1080\n"
                    "  - Any application configured to use SOCKS proxy localhost:1080\n"
                    "    will have its traffic routed through the SSH connection\n"
                    "  - The jumphost makes the actual connections on your behalf\n\n"
                    "Use cases:\n"
                    "  - Browse the web through a remote server's network\n"
                    "  - Access internal services without individual port forwards\n"
                    "  - Route specific application traffic through an SSH tunnel\n\n"
                    "Tools that support SOCKS:\n"
                    "  - curl --socks5 localhost:1080\n"
                    "  - Most browsers (in proxy settings)\n"
                    "  - proxychains (for tools that don't natively support SOCKS)"
                ),
                "answer": "-D",
                "hints": ["'D' for Dynamic — a dynamic SOCKS proxy.", "The answer is: -D"],
            },
            {
                "id": "tn_5",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Background Tunnel",
                "flavor": "Create a background tunnel: forward local port 5432 to db.nexus.internal:5432 through admin@nexus-jump, no shell, run in background. Write the full command:",
                "lesson": (
                    "Background tunnel: ssh -fN -L localPort:remoteHost:remotePort user@host\n\n"
                    "  ssh -fN -L 5432:db.nexus.internal:5432 admin@nexus-jump\n\n"
                    "Flags:\n"
                    "  -f → fork to background after authentication (before command execution)\n"
                    "  -N → don't execute a remote command\n"
                    "  -L → local port forward\n\n"
                    "After this command:\n"
                    "  - Returns to your shell prompt immediately\n"
                    "  - SSH tunnel runs in the background\n"
                    "  - localhost:5432 → db.nexus.internal:5432 via nexus-jump\n\n"
                    "To kill it:\n"
                    "  ps aux | grep 'ssh -fN' | grep -v grep\n"
                    "  kill <pid>\n"
                    "Or use a control socket (-M/-S flags) for cleaner management."
                ),
                "answer": "ssh -fN -L 5432:db.nexus.internal:5432 admin@nexus-jump",
                "hints": [
                    "Combine -f (background), -N (no shell), -L (local forward).",
                    "The answer is: ssh -fN -L 5432:db.nexus.internal:5432 admin@nexus-jump",
                ],
            },
        ],
    },
    "jump_chain": {
        "id": "jump_chain",
        "name": "The Jump Chain",
        "subtitle": "Multi-Hop SSH & ProxyJump",
        "color": "magenta",
        "icon": "⛓️",
        "commands": ["-J hop1,hop2", "ProxyJump", "ProxyCommand", "bastion hosts"],
        "challenges": [
            {
                "id": "jc_1",
                "type": "flag_quiz",
                "title": "Single Jump Host",
                "flavor": "You need to connect to db.internal but must go through bastion.nexus.com first. What flag specifies the jump host?",
                "lesson": (
                    "-J — specify a jump host (ProxyJump).\n\n"
                    "  ssh -J user@bastion.nexus.com admin@db.internal\n\n"
                    "What -J does:\n"
                    "  1. Connects to bastion.nexus.com\n"
                    "  2. From bastion, opens a connection to db.internal\n"
                    "  3. Your terminal session runs on db.internal\n"
                    "  4. The entire chain is end-to-end encrypted\n\n"
                    "From db.internal's perspective: the connection comes from bastion.\n"
                    "From your perspective: a direct interactive session on db.internal.\n\n"
                    "In ~/.ssh/config:\n"
                    "  Host db\n"
                    "    ProxyJump bastion\n"
                    "  → ssh db   (equivalent to ssh -J bastion admin@db.internal)"
                ),
                "answer": "-J",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["'J' for Jump host.", "The answer is: -J"],
            },
            {
                "id": "jc_2",
                "type": "fill_blank",
                "title": "Multi-Hop Chain",
                "flavor": "You need to connect to target.internal through TWO jump hosts: first bastion.nexus.com, then internal-jump.nexus.com. Write the -J argument:",
                "lesson": (
                    "Multiple jump hosts: -J host1,host2 (comma-separated)\n\n"
                    "  ssh -J user@bastion.nexus.com,user@internal-jump.nexus.com admin@target.internal\n\n"
                    "The chain executes in order:\n"
                    "  1. Connect to bastion.nexus.com\n"
                    "  2. From bastion, connect to internal-jump.nexus.com\n"
                    "  3. From internal-jump, connect to target.internal\n\n"
                    "Each hop can use different credentials:\n"
                    "  -J user1@hop1,user2@hop2\n\n"
                    "In ~/.ssh/config:\n"
                    "  Host target\n"
                    "    ProxyJump bastion,internal-jump\n\n"
                    "The number of hops is unlimited (in theory). In practice,\n"
                    "each hop adds latency. Three or four hops is typically the maximum\n"
                    "before the session becomes unusably slow."
                ),
                "answer": "user@bastion.nexus.com,user@internal-jump.nexus.com",
                "hints": ["Comma-separate multiple jump hosts.", "The answer is: user@bastion.nexus.com,user@internal-jump.nexus.com"],
            },
            {
                "id": "jc_3",
                "type": "quiz",
                "title": "Config ProxyJump",
                "flavor": "In ~/.ssh/config, what directive specifies a jump host for a Host entry?",
                "lesson": (
                    "ProxyJump — specify a jump host in ~/.ssh/config.\n\n"
                    "  Host target\n"
                    "    HostName target.internal\n"
                    "    User admin\n"
                    "    ProxyJump bastion\n\n"
                    "ProxyJump references another Host entry by alias:\n"
                    "  Host bastion\n"
                    "    HostName bastion.nexus.com\n"
                    "    User ops\n\n"
                    "  Host target\n"
                    "    HostName target.internal\n"
                    "    User admin\n"
                    "    ProxyJump bastion\n\n"
                    "  ssh target → connects through bastion to target\n\n"
                    "Multiple ProxyJump hops:\n"
                    "  ProxyJump bastion,internal-jump"
                ),
                "answer": "ProxyJump",
                "hints": ["The config directive for a jump host.", "The answer is: ProxyJump"],
            },
            {
                "id": "jc_4",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Jump with Port Forward",
                "flavor": "Connect to db.internal through bastion.nexus.com AND forward local port 5432 to db.internal:5432. Write the full ssh command:",
                "lesson": (
                    "Combining -J (jump) with -L (local forward):\n\n"
                    "  ssh -J user@bastion.nexus.com -L 5432:db.internal:5432 -N admin@db.internal\n\n"
                    "This is the 'everything at once' pattern:\n"
                    "  -J   → go through the bastion\n"
                    "  -L   → forward the database port to localhost\n"
                    "  -N   → no shell (we only want the tunnel)\n\n"
                    "After this command:\n"
                    "  localhost:5432 → db.internal:5432, through bastion, over SSH\n\n"
                    "To also go background:\n"
                    "  ssh -fNJ user@bastion -L 5432:db.internal:5432 admin@db.internal"
                ),
                "answer": "ssh -J user@bastion.nexus.com -L 5432:db.internal:5432 -N admin@db.internal",
                "hints": [
                    "Combine -J for the jump host and -L for the port forward, add -N.",
                    "The answer is: ssh -J user@bastion.nexus.com -L 5432:db.internal:5432 -N admin@db.internal",
                ],
            },
        ],
    },
    "agent_protocol": {
        "id": "agent_protocol",
        "name": "The Agent Protocol",
        "subtitle": "ssh-agent, ssh-add & Agent Forwarding",
        "color": "yellow",
        "icon": "🤖",
        "commands": ["ssh-agent", "ssh-add", "ssh-add -l", "-A forwarding", "SSH_AUTH_SOCK"],
        "challenges": [
            {
                "id": "ag_1",
                "type": "quiz",
                "title": "What Is ssh-agent?",
                "flavor": "What command name is the background process that holds decrypted private keys in memory and handles authentication on your behalf?",
                "lesson": (
                    "ssh-agent — a background process that manages SSH keys in memory.\n\n"
                    "How it works:\n"
                    "  1. ssh-agent runs as a background process\n"
                    "  2. You add keys to it with ssh-add\n"
                    "  3. When SSH needs to authenticate, it asks the agent to sign\n"
                    "     the authentication challenge\n"
                    "  4. The agent signs it using the key in memory\n"
                    "  5. The private key bytes never leave the agent process\n\n"
                    "Starting the agent:\n"
                    "  eval $(ssh-agent)   → start agent and set environment variables\n"
                    "  eval $(ssh-agent -s)  → same (for sh-compatible shells)\n\n"
                    "The agent sets SSH_AUTH_SOCK in the environment — SSH clients\n"
                    "use this socket path to communicate with the agent."
                ),
                "answer": "ssh-agent",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["The name of the agent process.", "The answer is: ssh-agent"],
            },
            {
                "id": "ag_2",
                "type": "quiz",
                "title": "Add Key to Agent",
                "flavor": "The agent is running. You need to add your private key to it so SSH can use it without prompting for the passphrase each time. What command adds a key?",
                "lesson": (
                    "ssh-add — add a private key to the running ssh-agent.\n\n"
                    "  ssh-add ~/.ssh/id_ed25519    → add a specific key\n"
                    "  ssh-add                      → add the default keys (~/.ssh/id_*)\n"
                    "  ssh-add -l                   → list keys currently in the agent\n"
                    "  ssh-add -d ~/.ssh/id_ed25519 → remove a key from the agent\n"
                    "  ssh-add -D                   → remove ALL keys from the agent\n\n"
                    "If the key has a passphrase, ssh-add prompts for it once.\n"
                    "After that, the agent handles authentication silently.\n\n"
                    "Expiration:\n"
                    "  ssh-add -t 3600 key  → add key that expires after 3600 seconds\n"
                    "  (useful for security: keys automatically removed after the session)"
                ),
                "answer": "ssh-add",
                "hints": ["The command that adds a key to the agent.", "The answer is: ssh-add"],
            },
            {
                "id": "ag_3",
                "type": "flag_quiz",
                "title": "Forward the Agent",
                "flavor": "You're connected to a jump host and need to connect further to another server using your local keys — without copying them to the jump host. What ssh flag forwards your agent to the remote host?",
                "lesson": (
                    "-A — enable agent forwarding.\n\n"
                    "  ssh -A admin@jumphost\n\n"
                    "With agent forwarding enabled:\n"
                    "  - A socket is created on the remote host\n"
                    "  - SSH_AUTH_SOCK on the remote host points to this socket\n"
                    "  - When you run ssh from the remote host, it uses YOUR agent\n"
                    "    (running locally) for authentication\n"
                    "  - Your private key NEVER leaves your machine\n\n"
                    "In ~/.ssh/config:\n"
                    "  Host bastion\n"
                    "    ForwardAgent yes\n\n"
                    "Security warning:\n"
                    "  Only forward your agent to hosts you fully trust.\n"
                    "  A root user on the remote host can use the forwarded agent\n"
                    "  socket to authenticate as you to other servers."
                ),
                "answer": "-A",
                "hints": ["Uppercase -A for Agent forwarding.", "The answer is: -A"],
            },
            {
                "id": "ag_4",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: List Agent Keys",
                "flavor": "You need to verify which keys are currently loaded in the SSH agent. What command lists them?",
                "lesson": (
                    "ssh-add -l — list keys currently loaded in the agent.\n\n"
                    "Output format:\n"
                    "  2048 SHA256:AbCdEf... /home/user/.ssh/id_rsa (RSA)\n"
                    "  256  SHA256:XyZabc... /home/user/.ssh/id_ed25519 (ED25519)\n\n"
                    "  Columns: key size, fingerprint, comment/path, type\n\n"
                    "  ssh-add -l   → list keys (short fingerprint)\n"
                    "  ssh-add -L   → list public keys (full key material)\n\n"
                    "If no agent is running or no keys are loaded:\n"
                    "  'The agent has no identities.'\n"
                    "  'Could not open a connection to your authentication agent.'\n\n"
                    "Forensic use: checking what keys are in an agent is part of\n"
                    "auditing what access a compromised session might have had."
                ),
                "answer": "ssh-add -l",
                "hints": ["ssh-add with the -l flag lists keys.", "The answer is: ssh-add -l"],
            },
        ],
    },
    "hardening_core": {
        "id": "hardening_core",
        "name": "The Hardening Core",
        "subtitle": "sshd_config & Securing SSH",
        "color": "red",
        "icon": "🔒",
        "commands": ["sshd_config", "PasswordAuthentication", "PermitRootLogin", "AllowUsers", "Port"],
        "challenges": [
            {
                "id": "hc_1",
                "type": "quiz",
                "title": "Disable Password Auth",
                "flavor": "What sshd_config directive (set to 'no') disables password-based authentication, forcing key-only access?",
                "lesson": (
                    "PasswordAuthentication no — disable password authentication in sshd.\n\n"
                    "In /etc/ssh/sshd_config (server-side):\n"
                    "  PasswordAuthentication no\n\n"
                    "This is the single most impactful SSH hardening setting:\n"
                    "  - Eliminates brute force password attacks entirely\n"
                    "  - Eliminates credential stuffing attacks\n"
                    "  - Forces all authentication to use keys\n"
                    "  - Makes the SSH server immune to weak passwords\n\n"
                    "Before disabling:\n"
                    "  1. Add your public key to authorized_keys\n"
                    "  2. Test that key authentication works\n"
                    "  3. THEN set PasswordAuthentication no\n"
                    "  4. Reload: systemctl reload sshd\n\n"
                    "NEXUS had PasswordAuthentication yes on every server.\n"
                    "This is why the credential approach worked as a fallback."
                ),
                "answer": "PasswordAuthentication",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["The directive that controls password authentication in sshd_config.", "The answer is: PasswordAuthentication"],
            },
            {
                "id": "hc_2",
                "type": "quiz",
                "title": "Disable Root Login",
                "flavor": "What sshd_config directive (set to 'no') prevents SSH login as the root user?",
                "lesson": (
                    "PermitRootLogin no — disable direct SSH login as root.\n\n"
                    "  PermitRootLogin no              → root cannot SSH in at all\n"
                    "  PermitRootLogin prohibit-password → root can login but only with a key\n"
                    "  PermitRootLogin yes             → root can login with password or key\n\n"
                    "Why no:\n"
                    "  - Root has unlimited access; any compromise is total\n"
                    "  - Login audit logs should show which user escalated to root,\n"
                    "    not just 'root logged in'\n"
                    "  - Brute-force attacks commonly target root specifically\n\n"
                    "Best practice:\n"
                    "  PermitRootLogin no\n"
                    "  → Users SSH in as a non-privileged account\n"
                    "  → Use sudo for root-level operations\n"
                    "  → Audit log shows: 'user escalated with sudo'\n\n"
                    "NEXUS had PermitRootLogin yes on three production servers."
                ),
                "answer": "PermitRootLogin",
                "hints": ["The directive controlling whether root can log in via SSH.", "The answer is: PermitRootLogin"],
            },
            {
                "id": "hc_3",
                "type": "quiz",
                "title": "Restrict User Access",
                "flavor": "You want to explicitly whitelist which users are allowed to SSH into a server. What sshd_config directive specifies the allowed users?",
                "lesson": (
                    "AllowUsers — whitelist specific users for SSH access.\n\n"
                    "  AllowUsers admin ops deploy\n\n"
                    "If AllowUsers is set, ONLY listed users can connect.\n"
                    "All other users are denied, regardless of their password or key.\n\n"
                    "Related directives:\n"
                    "  AllowGroups sshusers  → allow users in the 'sshusers' group\n"
                    "  DenyUsers baduser     → deny specific users (less common)\n"
                    "  DenyGroups noSSH      → deny members of a group\n\n"
                    "AllowUsers + AllowGroups: if either list matches, access is granted.\n"
                    "DenyUsers is checked BEFORE AllowUsers — deny takes precedence.\n\n"
                    "Best practice: AllowGroups is often cleaner than AllowUsers,\n"
                    "since user access can be managed through group membership\n"
                    "without modifying sshd_config."
                ),
                "answer": "AllowUsers",
                "hints": ["The directive that whitelists users.", "The answer is: AllowUsers"],
            },
            {
                "id": "hc_4",
                "is_boss": True,
                "type": "fill_blank",
                "title": "Boss: Reload SSH Daemon",
                "flavor": "You've updated /etc/ssh/sshd_config. What command reloads the SSH daemon to apply the changes without dropping existing sessions?",
                "lesson": (
                    "systemctl reload sshd — reload sshd config without dropping sessions.\n\n"
                    "  systemctl reload sshd\n\n"
                    "Reload vs restart:\n"
                    "  systemctl reload sshd    → sshd re-reads config; existing connections unaffected\n"
                    "  systemctl restart sshd   → sshd restarts; ALL existing connections dropped\n\n"
                    "Always use reload, not restart:\n"
                    "  If you're connected via SSH when you restart sshd,\n"
                    "  your session might be dropped — leaving you locked out\n"
                    "  if the new config has an error.\n\n"
                    "Before reloading, validate the config:\n"
                    "  sshd -t  → test configuration syntax without applying\n\n"
                    "Safe hardening procedure:\n"
                    "  1. Edit /etc/ssh/sshd_config\n"
                    "  2. sshd -t        → validate syntax\n"
                    "  3. Keep a second SSH session open as a safety net\n"
                    "  4. systemctl reload sshd\n"
                    "  5. Test the new settings from a third terminal\n"
                    "  6. Only then close the safety net session"
                ),
                "answer": "systemctl reload sshd",
                "hints": [
                    "Use systemctl with 'reload' (not restart) to preserve existing sessions.",
                    "The answer is: systemctl reload sshd",
                ],
            },
        ],
    },
    "multiplexer_gateway": {
        "id": "multiplexer_gateway",
        "name": "The Multiplexer Gateway",
        "subtitle": "Persistent sessions that outlive the connection",
        "color": "cyan",
        "icon": "🖥️",
        "commands": ["tmux new -s", "tmux attach -t", "tmux ls", "Ctrl+b d", "tmux kill-session"],
        "challenges": [
            {
                "id": "mux_1",
                "type": "fill_blank",
                "title": "Create a Named Session",
                "flavor": "You need a persistent tmux session on the NEXUS jump host that will survive if your SSH connection drops. Name it 'ghost'. What command creates it?",
                "lesson": (
                    "tmux new -s session_name — create a new named tmux session.\n\n"
                    "  tmux new -s ghost\n\n"
                    "Why named sessions matter:\n"
                    "  - You can reattach by name: tmux attach -t ghost\n"
                    "  - Multiple users on the same host can have separate sessions\n"
                    "  - Scripts can target sessions by name\n\n"
                    "Shorthand:\n"
                    "  tmux new -s ghost\n"
                    "  tmux new-session -s ghost  → long form, same result\n\n"
                    "The session persists on the remote server even if you close your\n"
                    "SSH connection. Reconnect and reattach — everything is exactly as you left it.\n\n"
                    "Long-running processes (data extraction, port scans, compilation)\n"
                    "should always run inside tmux or screen to survive disconnections."
                ),
                "answer": "tmux new -s ghost",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["tmux new followed by the session name flag.", "The answer is: tmux new -s ghost"],
            },
            {
                "id": "mux_2",
                "type": "fill_blank",
                "title": "Reattach to a Session",
                "flavor": "Your SSH connection to the NEXUS jump host dropped. You reconnect. Your 'ghost' tmux session is still running. What command reattaches to it?",
                "lesson": (
                    "tmux attach -t session_name — attach to an existing tmux session.\n\n"
                    "  tmux attach -t ghost\n\n"
                    "Shorthand:\n"
                    "  tmux a -t ghost    → 'a' is short for 'attach'\n"
                    "  tmux attach        → attach to the most recent session (if only one exists)\n\n"
                    "What happens on reattach:\n"
                    "  - The terminal renders the session exactly as it was\n"
                    "  - Any processes still running continue where they left off\n"
                    "  - Output that accumulated while you were disconnected is visible\n\n"
                    "If someone else is already attached to the session:\n"
                    "  tmux attach -t ghost      → both see the same session (shared screen)\n"
                    "  tmux attach -t ghost -d   → detach the other user, take the session"
                ),
                "answer": "tmux attach -t ghost",
                "hints": ["tmux attach with the target flag.", "The answer is: tmux attach -t ghost"],
            },
            {
                "id": "mux_3",
                "type": "fill_blank",
                "title": "List Active Sessions",
                "flavor": "You've reconnected to the NEXUS jump host and don't remember the name of your tmux session. What command lists all active sessions?",
                "lesson": (
                    "tmux ls — list all active tmux sessions.\n\n"
                    "  tmux ls\n"
                    "  tmux list-sessions  → long form\n\n"
                    "Output format:\n"
                    "  ghost: 2 windows (created Mon Jan 1 00:00:00 2024) [220x50]\n"
                    "  ops: 1 window (created Mon Jan 1 01:00:00 2024) [220x50] (attached)\n\n"
                    "Reading the output:\n"
                    "  - Session name: 'ghost', 'ops'\n"
                    "  - Number of windows in the session\n"
                    "  - Creation time\n"
                    "  - Terminal dimensions\n"
                    "  - '(attached)' means another terminal is currently connected\n\n"
                    "If tmux ls shows no sessions: no sessions exist on this host.\n"
                    "If the command errors: tmux is not installed or not running."
                ),
                "answer": "tmux ls",
                "hints": ["tmux followed by a two-letter list command.", "The answer is: tmux ls"],
            },
            {
                "id": "mux_4",
                "type": "quiz",
                "title": "Detach from a Session",
                "flavor": "You need to disconnect from your active 'ghost' tmux session without killing it — leaving your processes running. What key sequence detaches from the session?",
                "lesson": (
                    "Ctrl+b d — detach from the current tmux session.\n\n"
                    "The Ctrl+b prefix:\n"
                    "  tmux uses Ctrl+b as its command prefix (like vim's ESC for mode switching).\n"
                    "  Press Ctrl+b, release, then press the command key.\n\n"
                    "Common tmux key bindings (all after Ctrl+b):\n"
                    "  d    → detach from session (leave it running)\n"
                    "  c    → create a new window\n"
                    "  n    → next window\n"
                    "  p    → previous window\n"
                    "  %    → split pane vertically\n"
                    '  "    → split pane horizontally\n'
                    "  [    → scroll mode (use arrow keys or PgUp/PgDn)\n"
                    "  ?    → list all key bindings\n\n"
                    "Detach vs. kill:\n"
                    "  Ctrl+b d  → session stays alive (processes keep running)\n"
                    "  exit       → closes the shell; if last window, kills the session"
                ),
                "answer": "Ctrl+b d",
                "hints": ["The tmux prefix key followed by detach.", "Ctrl+b, then d.", "The answer is: Ctrl+b d"],
            },
            {
                "id": "mux_5",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Kill a Session",
                "flavor": "The 'ghost' tmux session on the NEXUS jump host needs to be fully terminated — all processes in it killed. What command destroys the session completely?",
                "lesson": (
                    "tmux kill-session -t session_name — destroy a session and all its processes.\n\n"
                    "  tmux kill-session -t ghost\n\n"
                    "What it does:\n"
                    "  - Sends SIGHUP to all processes in the session\n"
                    "  - Closes all windows and panes\n"
                    "  - The session no longer appears in tmux ls\n\n"
                    "Other cleanup commands:\n"
                    "  tmux kill-window -t ghost:1    → kill a specific window\n"
                    "  tmux kill-pane -t ghost:1.2    → kill a specific pane\n"
                    "  tmux kill-server               → kill tmux entirely (all sessions)\n\n"
                    "Use kill-session when:\n"
                    "  - Wrapping up an operation and cleaning up\n"
                    "  - A session is stuck and won't respond\n"
                    "  - Operational security requires leaving no running sessions"
                ),
                "answer": "tmux kill-session -t ghost",
                "hints": [
                    "tmux kill-session with the target flag.",
                    "The answer is: tmux kill-session -t ghost",
                ],
            },
        ],
    },
    "scp_vault": {
        "id": "scp_vault",
        "name": "The SCP Vault",
        "subtitle": "Move files through encrypted channels",
        "color": "yellow",
        "icon": "📁",
        "commands": ["scp file user@host:/path", "scp -r", "scp user@host:/file .", "sftp user@host", "get/put"],
        "challenges": [
            {
                "id": "scp_1",
                "type": "fill_blank",
                "title": "Copy File to Remote",
                "flavor": "You have a config patch at file.txt that needs to be deployed to the NEXUS server. Copy it to /opt/nexus/ on user@10.0.0.5. What is the scp command?",
                "lesson": (
                    "scp file.txt user@host:/path — copy a local file to a remote path.\n\n"
                    "  scp file.txt user@10.0.0.5:/opt/nexus/\n\n"
                    "scp syntax:\n"
                    "  scp [options] source destination\n\n"
                    "  source/destination can be:\n"
                    "    local path:  file.txt  or  ./dir/file.txt\n"
                    "    remote path: user@host:/remote/path\n\n"
                    "Options:\n"
                    "  -P 2222         → specify port (uppercase P, unlike ssh's lowercase p)\n"
                    "  -i ~/.ssh/key   → specify identity file\n"
                    "  -r              → recursive (copy directories)\n"
                    "  -C              → compress during transfer\n\n"
                    "scp uses SSH for transport — all files are encrypted in transit.\n"
                    "It respects ~/.ssh/config entries and key files."
                ),
                "answer": "scp file.txt user@10.0.0.5:/opt/nexus/",
                "url": "https://www.openssh.com/manual.html",
                "hints": ["scp source destination — remote path uses user@host:/path format.", "The answer is: scp file.txt user@10.0.0.5:/opt/nexus/"],
            },
            {
                "id": "scp_2",
                "type": "fill_blank",
                "title": "Recursive Directory Copy",
                "flavor": "You need to copy the entire 'exfil/' directory from your machine to /tmp/ on the NEXUS server at user@10.0.0.5. What flag enables recursive directory copy?",
                "lesson": (
                    "scp -r dir/ user@host:/path — recursively copy a directory.\n\n"
                    "  scp -r exfil/ user@10.0.0.5:/tmp/\n\n"
                    "The -r flag:\n"
                    "  Recursively copies the entire directory tree.\n"
                    "  Without -r, scp ignores directories entirely.\n\n"
                    "Trailing slash behavior:\n"
                    "  scp -r exfil/ user@host:/tmp/   → copies contents into /tmp/exfil/\n"
                    "  scp -r exfil  user@host:/tmp/   → same result for directories\n\n"
                    "Limitation of scp:\n"
                    "  scp copies the whole tree every time — no incremental/delta transfer.\n"
                    "  For large directories, rsync -avz --progress user@host:/path is better:\n"
                    "    - Only transfers changed files\n"
                    "    - Resumable if interrupted\n"
                    "    - Shows progress"
                ),
                "answer": "-r",
                "hints": ["Single flag for recursive copy.", "The answer is: -r"],
            },
            {
                "id": "scp_3",
                "type": "fill_blank",
                "title": "Copy File from Remote",
                "flavor": "The NEXUS server at user@10.0.0.5 has a private key at /root/.ssh/nexus_rsa that you want to pull to your current directory. What is the scp command?",
                "lesson": (
                    "scp user@host:/remote/file . — copy a remote file to the local current directory.\n\n"
                    "  scp user@10.0.0.5:/root/.ssh/nexus_rsa .\n\n"
                    "The . as destination means 'current directory' — the file is saved\n"
                    "with its original filename in the current directory.\n\n"
                    "Alternatively:\n"
                    "  scp user@host:/remote/file ./local_name.txt  → rename on arrival\n"
                    "  scp user@host:/remote/file ~/downloads/      → specify local directory\n\n"
                    "Copying between two remote hosts:\n"
                    "  scp user1@host1:/file user2@host2:/path\n"
                    "  → SSH proxies the transfer through your local machine\n"
                    "  → Both remote hosts must be accessible from your machine\n\n"
                    "Security note: be careful about where files land locally —\n"
                    "pulled private keys need chmod 600 immediately."
                ),
                "answer": "scp user@10.0.0.5:/root/.ssh/nexus_rsa .",
                "hints": ["Remote source, local destination (.) for current directory.", "The answer is: scp user@10.0.0.5:/root/.ssh/nexus_rsa ."],
            },
            {
                "id": "scp_4",
                "type": "fill_blank",
                "title": "Open an SFTP Session",
                "flavor": "You need an interactive file transfer session to explore the NEXUS server at user@10.0.0.5 and selectively pull files. What command starts an SFTP session?",
                "lesson": (
                    "sftp user@host — start an interactive SFTP session.\n\n"
                    "  sftp user@10.0.0.5\n\n"
                    "SFTP vs scp:\n"
                    "  scp  → single-shot copy, like cp. Best for known paths.\n"
                    "  sftp → interactive session. Best for browsing and selective transfer.\n\n"
                    "Once inside sftp:\n"
                    "  ls          → list remote directory\n"
                    "  lls         → list local directory\n"
                    "  cd /path    → change remote directory\n"
                    "  lcd /path   → change local directory\n"
                    "  get file    → download file from remote to local\n"
                    "  put file    → upload file from local to remote\n"
                    "  mget *.log  → download multiple files matching pattern\n"
                    "  quit / exit → close the session\n\n"
                    "sftp uses the SSH protocol — same keys, same auth, same port."
                ),
                "answer": "sftp user@10.0.0.5",
                "hints": ["sftp followed by user@host.", "The answer is: sftp user@10.0.0.5"],
            },
            {
                "id": "scp_5",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: SFTP get and put",
                "flavor": "Inside an SFTP session on the NEXUS server, you need to download the remote file 'audit.log' to your local machine. What SFTP command does this?",
                "lesson": (
                    "get filename — download a file in an active SFTP session.\n\n"
                    "  sftp> get audit.log\n\n"
                    "The get/put pair:\n"
                    "  get remote_file          → download to local current directory\n"
                    "  get remote_file local_name → download and rename\n"
                    "  put local_file           → upload to remote current directory\n"
                    "  put local_file /remote/path → upload to specific remote path\n\n"
                    "Batch transfer:\n"
                    "  mget *.log   → download all .log files\n"
                    "  mput *.conf  → upload all .conf files\n\n"
                    "Non-interactive sftp (scriptable):\n"
                    "  sftp user@host <<EOF\n"
                    "  get /var/log/nexus/audit.log\n"
                    "  EOF\n\n"
                    "Or with -b batchfile:\n"
                    "  sftp -b commands.txt user@host"
                ),
                "answer": "get audit.log",
                "hints": [
                    "The SFTP command for downloading — opposite of put.",
                    "The answer is: get audit.log",
                ],
            },
        ],
    },
    "port_forwarding": {
        "id": "port_forwarding",
        "name": "The Port Forwarding Relay",
        "subtitle": "Local Forwards, Remote Forwards & SOCKS Proxies",
        "color": "yellow",
        "icon": "🔀",
        "commands": ["ssh -L", "ssh -R", "ssh -D", "ssh -N -f", "ssh -J"],
        "challenges": [
            {
                "id": "pf_1",
                "type": "quiz",
                "title": "Local Port Forward",
                "flavor": "The NEXUS financial server only listens on localhost:80 behind the firewall. Ghost sets up: ssh -L 8080:localhost:80 user@host. What does -L do?",
                "lesson": (
                    "-L — local port forwarding: forward a local port through the SSH tunnel.\n\n"
                    "  ssh -L [local_port]:[remote_host]:[remote_port] user@host\n\n"
                    "What happens:\n"
                    "  - SSH listens on local_port on your machine\n"
                    "  - Any traffic sent to localhost:local_port is forwarded through\n"
                    "    the encrypted SSH tunnel to the remote host\n"
                    "  - The remote host then connects to remote_host:remote_port\n\n"
                    "Example: ssh -L 8080:localhost:80 user@host\n"
                    "  → localhost:8080 on your machine reaches localhost:80 on the remote host\n"
                    "  → The firewall sees a legitimate SSH connection on port 22\n"
                    "  → It does not see port 80 traffic\n\n"
                    "Useful for: reaching services that only listen on the remote's localhost,\n"
                    "databases behind firewalls, internal web UIs."
                ),
                "answer": "forwards a local port through the SSH connection",
                "url": "https://www.openssh.com/manual.html",
                "hints": [
                    "L stands for Local — it makes a local port accessible through the tunnel.",
                    "The answer is: forwards a local port through the SSH connection",
                ],
            },
            {
                "id": "pf_2",
                "type": "quiz",
                "title": "Remote Port Forward",
                "flavor": "Ghost needs to expose a local service to the remote NEXUS host. The command: ssh -R 9090:localhost:3000 user@host. What does -R do?",
                "lesson": (
                    "-R — remote port forwarding: expose a local port on the remote host.\n\n"
                    "  ssh -R [remote_port]:[local_host]:[local_port] user@host\n\n"
                    "What happens:\n"
                    "  - SSH opens remote_port on the remote server\n"
                    "  - Any traffic hitting that remote port is tunneled back through\n"
                    "    the SSH connection to your local machine\n"
                    "  - Your machine forwards it to local_host:local_port\n\n"
                    "Example: ssh -R 9090:localhost:3000 user@host\n"
                    "  → Port 9090 on the remote host reaches localhost:3000 on your machine\n\n"
                    "Use cases:\n"
                    "  - Exposing a local dev server to a remote host\n"
                    "  - Reverse shell callbacks\n"
                    "  - Bypassing NAT when you can initiate outbound but not receive inbound\n\n"
                    "The asymmetry: -L pulls remote resources to you; -R pushes local resources out."
                ),
                "answer": "exposes a local port on the remote host",
                "hints": [
                    "R stands for Remote — the port opens on the remote side.",
                    "The answer is: exposes a local port on the remote host",
                ],
            },
            {
                "id": "pf_3",
                "type": "quiz",
                "title": "Dynamic SOCKS Proxy",
                "flavor": "Ghost needs a single tunnel that can route to any host on the NEXUS internal network. The command: ssh -D 1080 user@host. What does -D create?",
                "lesson": (
                    "-D — dynamic port forwarding: creates a SOCKS proxy on the specified local port.\n\n"
                    "  ssh -D [local_port] user@host\n\n"
                    "What it creates:\n"
                    "  - A SOCKS4/SOCKS5 proxy listening on local_port\n"
                    "  - Any application configured to use this proxy routes its traffic\n"
                    "    through the SSH tunnel\n"
                    "  - The remote SSH server acts as the exit point — it makes the\n"
                    "    actual outbound connections on behalf of the SOCKS client\n\n"
                    "Example: ssh -D 1080 user@host\n"
                    "  → Configure your browser or tool to use SOCKS5 proxy at localhost:1080\n"
                    "  → All traffic routes through the remote host's network context\n\n"
                    "Difference from -L:\n"
                    "  -L: forwards one specific port to one specific destination\n"
                    "  -D: forwards any port to any destination — dynamic routing\n\n"
                    "Use with proxychains to route arbitrary commands through the tunnel:\n"
                    "  proxychains nmap 10.20.30.0/24"
                ),
                "answer": "a SOCKS proxy on the specified local port",
                "hints": [
                    "D stands for Dynamic — it dynamically routes to any destination through one tunnel.",
                    "The answer is: a SOCKS proxy on the specified local port",
                ],
            },
            {
                "id": "pf_4",
                "type": "quiz",
                "title": "Background Tunnel",
                "flavor": "Ghost needs: ssh -N -f -L 5432:db.nexus.corp:5432 user@jumphost — a persistent background tunnel with no shell. What does -N mean?",
                "lesson": (
                    "-N — do not execute a remote command (tunnel only).\n\n"
                    "  ssh -N user@host  → establishes the SSH connection but doesn't open a shell\n\n"
                    "Used with -f to background the tunnel:\n"
                    "  ssh -N -f -L 5432:db.nexus.corp:5432 user@jumphost\n\n"
                    "Breaking it down:\n"
                    "  -N  → no remote command; just maintain the tunnel\n"
                    "  -f  → fork to background before executing; hands control back to terminal\n"
                    "  -L  → local port forward (5432 on localhost → db.nexus.corp:5432)\n\n"
                    "Without -N:\n"
                    "  SSH would open an interactive shell on the remote host\n"
                    "  The tunnel would only exist as long as you're in that shell\n\n"
                    "With -N -f:\n"
                    "  The tunnel runs silently in the background\n"
                    "  Your terminal is free; the port forward persists\n"
                    "  Kill it with: kill $(pgrep -f 'ssh -N')"
                ),
                "answer": "do not execute a remote command (tunnel only)",
                "hints": [
                    "N means no shell — the connection exists purely for the tunnel.",
                    "The answer is: do not execute a remote command (tunnel only)",
                ],
            },
            {
                "id": "pf_5",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: ProxyJump Through Two Hosts",
                "flavor": "The financial server sits behind two jump hosts. Ghost needs one command to chain through both. Complete: ssh ___ user@target.nexus.corp",
                "lesson": (
                    "ssh -J — ProxyJump: chain through one or more jump hosts.\n\n"
                    "  ssh -J jump1.nexus.corp,jump2.nexus.corp user@target.nexus.corp\n\n"
                    "How it works:\n"
                    "  1. SSH connects to jump1.nexus.corp\n"
                    "  2. From jump1, SSH connects to jump2.nexus.corp\n"
                    "  3. From jump2, SSH connects to target.nexus.corp\n"
                    "  4. Your terminal session runs on target.nexus.corp\n\n"
                    "The chain is comma-separated. Each host is a hop.\n"
                    "SSH negotiates the full chain — no manual chaining, no nested ssh commands.\n\n"
                    "Equivalent in ~/.ssh/config:\n"
                    "  Host target\n"
                    "    HostName target.nexus.corp\n"
                    "    ProxyJump jump1.nexus.corp,jump2.nexus.corp\n\n"
                    "The firewall sees two connections: one to jump1, one to jump2.\n"
                    "It does not see the final connection to the target — that traverses\n"
                    "the tunnel established through the chain."
                ),
                "answer": "-J jump1.nexus.corp,jump2.nexus.corp",
                "hints": [
                    "Use -J with comma-separated jump hosts.",
                    "The answer is: -J jump1.nexus.corp,jump2.nexus.corp",
                ],
            },
        ],
    },
    "key_management": {
        "id": "key_management",
        "name": "The Key Management Vault",
        "subtitle": "Key Rotation, Installation & authorized_keys",
        "color": "magenta",
        "icon": "🔑",
        "commands": ["ssh-keygen -t ed25519", "ssh-copy-id", "authorized_keys", "ssh-keygen -R"],
        "challenges": [
            {
                "id": "km_1",
                "type": "quiz",
                "title": "Generate Ed25519 Key",
                "flavor": "Ghost needs to generate a fresh key pair to establish a new identity on the NEXUS infrastructure. What command generates an Ed25519 key with the comment 'ghost@nexus'?",
                "lesson": (
                    "ssh-keygen -t ed25519 -C 'comment' — generate an Ed25519 SSH key pair.\n\n"
                    "  ssh-keygen -t ed25519 -C 'ghost@nexus'\n\n"
                    "Flags:\n"
                    "  -t ed25519  → key type (Ed25519 is the modern recommendation)\n"
                    "  -C          → comment field; embedded in the public key\n"
                    "                typically user@host, but can be anything\n"
                    "  -f          → specify output filename (default: ~/.ssh/id_ed25519)\n"
                    "  -N ''       → empty passphrase (for automation; not ideal for personal keys)\n\n"
                    "Key types:\n"
                    "  ed25519  → best: small (68 chars), fast, strong, modern\n"
                    "  ecdsa    → good, but some implementations are weaker\n"
                    "  rsa      → widely compatible; use 4096-bit minimum\n"
                    "  dsa      → deprecated; do not use\n\n"
                    "Output:\n"
                    "  ~/.ssh/id_ed25519      → private key (never share; chmod 600)\n"
                    "  ~/.ssh/id_ed25519.pub  → public key (this goes on the server)"
                ),
                "answer": "ssh-keygen -t ed25519 -C \"ghost@nexus\"",
                "url": "https://www.openssh.com/manual.html",
                "hints": [
                    "Use ssh-keygen with the type flag and a comment flag.",
                    "The answer is: ssh-keygen -t ed25519 -C \"ghost@nexus\"",
                ],
            },
            {
                "id": "km_2",
                "type": "quiz",
                "title": "Install Public Key",
                "flavor": "Ghost has a key pair. The next step is installing the public key on a remote NEXUS host to enable key-based login. What command automates this?",
                "lesson": (
                    "ssh-copy-id — install your public key on a remote server's authorized_keys.\n\n"
                    "  ssh-copy-id user@host\n"
                    "  ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host  → specify key file\n\n"
                    "What it does:\n"
                    "  1. Reads your public key (default: ~/.ssh/id_*.pub)\n"
                    "  2. SSHs into the server using current authentication (password or key)\n"
                    "  3. Appends the public key to ~/.ssh/authorized_keys on the server\n"
                    "  4. Sets correct permissions (700 on ~/.ssh, 600 on authorized_keys)\n\n"
                    "After ssh-copy-id:\n"
                    "  You can authenticate with the corresponding private key\n"
                    "  Password authentication is no longer required for that key\n\n"
                    "Manual equivalent:\n"
                    "  cat ~/.ssh/id_ed25519.pub | ssh user@host 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'"
                ),
                "answer": "ssh-copy-id",
                "hints": [
                    "The command name describes exactly what it does: copy an SSH ID to the server.",
                    "The answer is: ssh-copy-id",
                ],
            },
            {
                "id": "km_3",
                "type": "fill_blank",
                "title": "Manual Key Installation",
                "flavor": "ssh-copy-id isn't available on the target. Ghost must manually append the public key to authorized_keys. Complete: cat ~/.ssh/id_ed25519.pub ___ ~/.ssh/authorized_keys",
                "lesson": (
                    "cat key.pub >> ~/.ssh/authorized_keys — manually append a key.\n\n"
                    "  cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys\n\n"
                    "The >> operator appends to the file without overwriting existing keys.\n"
                    "Using > instead would destroy all previously authorized keys.\n\n"
                    "Post-installation checklist:\n"
                    "  chmod 700 ~/.ssh                   → directory must not be world-readable\n"
                    "  chmod 600 ~/.ssh/authorized_keys   → file must not be world-readable\n"
                    "  chown user:user ~/.ssh -R           → owned by the correct user\n\n"
                    "authorized_keys format:\n"
                    "  One key per line\n"
                    "  Each line: [options] keytype base64key [comment]\n"
                    "  Example: ssh-ed25519 AAAA... ghost@nexus\n\n"
                    "Forensic note: check authorized_keys for unexpected entries.\n"
                    "Backdoors often land here — a key added by an attacker that survives\n"
                    "password rotation because nobody audited the file."
                ),
                "answer": ">>",
                "hints": [
                    "You want to append, not overwrite. Which shell operator appends?",
                    "The answer is: >>",
                ],
            },
            {
                "id": "km_4",
                "type": "quiz",
                "title": "Remove Compromised Host Key",
                "flavor": "A NEXUS server was rebuilt after compromise. Ghost's known_hosts still has the old key — SSH will now refuse to connect with a host key mismatch warning. What command removes a host's entry from known_hosts?",
                "lesson": (
                    "ssh-keygen -R hostname — remove a host from ~/.ssh/known_hosts.\n\n"
                    "  ssh-keygen -R nexus-server.corp\n"
                    "  ssh-keygen -R 10.20.30.40\n\n"
                    "Why this is necessary:\n"
                    "  When you first connect to a host, SSH stores its public key fingerprint\n"
                    "  in ~/.ssh/known_hosts. On every subsequent connection, SSH verifies\n"
                    "  the fingerprint matches.\n\n"
                    "  If the server is rebuilt (new host key), SSH will refuse:\n"
                    "    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!\n"
                    "    This is designed to prevent MITM attacks.\n\n"
                    "  After verifying the rebuild is legitimate, remove the old entry:\n"
                    "    ssh-keygen -R hostname\n"
                    "  Then reconnect — SSH will prompt to accept the new fingerprint.\n\n"
                    "Key rotation workflow:\n"
                    "  1. Server is rebuilt / keys are rotated\n"
                    "  2. ssh-keygen -R on every client that connected to the old host\n"
                    "  3. Reconnect and verify the new fingerprint out-of-band"
                ),
                "answer": "ssh-keygen -R",
                "hints": [
                    "Use ssh-keygen with a flag that means 'remove'.",
                    "The answer is: ssh-keygen -R",
                ],
            },
            {
                "id": "km_5",
                "type": "quiz",
                "is_boss": True,
                "title": "Boss: The authorized_keys File",
                "flavor": "Ghost needs to verify which server-side file controls which public keys are allowed to authenticate. What file contains the public keys that are authorized to connect?",
                "lesson": (
                    "~/.ssh/authorized_keys — the file that controls key-based authentication.\n\n"
                    "Location: ~/.ssh/authorized_keys on the server being connected to.\n\n"
                    "How it works:\n"
                    "  When you connect with a private key, the server checks authorized_keys\n"
                    "  for the corresponding public key. If found: authentication succeeds.\n"
                    "  If not found: authentication fails (falls back to password if enabled).\n\n"
                    "Security implications:\n"
                    "  Anyone who can append to this file can grant themselves persistent access\n"
                    "  Privilege escalation → write to root's authorized_keys → root SSH access\n"
                    "  Backdoors survive password changes — keys are independent of passwords\n\n"
                    "Audit command:\n"
                    "  cat ~/.ssh/authorized_keys   → list every key authorized to connect\n"
                    "  Each line is one authorized identity\n\n"
                    "Key management hygiene:\n"
                    "  Audit authorized_keys regularly\n"
                    "  Remove keys for departed staff\n"
                    "  Remove keys for decommissioned systems\n"
                    "  Each key should be traceable to an active identity"
                ),
                "answer": "~/.ssh/authorized_keys",
                "hints": [
                    "It's a file in the ~/.ssh/ directory. The name describes its purpose.",
                    "The answer is: ~/.ssh/authorized_keys",
                ],
            },
        ],
    },
}

ZONE_ORDER = [
    "connection_basics",
    "key_vault",
    "config_matrix",
    "transfer_ops",
    "tunnel_network",
    "jump_chain",
    "agent_protocol",
    "hardening_core",
    "multiplexer_gateway",
    "scp_vault",
    "port_forwarding",
    "key_management",
]
