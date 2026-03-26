"""
zones.py - All zone and challenge data for Terminal Quest
"""

ZONES = {
    "antechamber": {
        "id": "antechamber",
        "name": "The Jack Node",
        "subtitle": "Shell Navigation",
        "color": "cyan",
        "icon": "⚡",
        "commands": ["ls", "cd", "pwd", "mkdir", "rmdir"],
        "challenges": [
            {
                "id": "antech_1",
                "type": "quiz",
                "title": "First Signal",
                "flavor": "The terminal is live. The cursor blinks. Somewhere in this directory is the data you need. What do you run to see what's here?",
                "lesson": (
                    "ls — lists the contents of a directory.\n\n"
                    "Syntax: ls [flags] [directory]\n\n"
                    "Common flags:\n"
                    "  -l   long format (permissions, size, date)\n"
                    "  -a   show hidden files (dotfiles)\n"
                    "  -h   human-readable file sizes\n\n"
                    "Example: ls /home/user    → lists files in /home/user"
                ),
                "question": "What command lists the contents of the current directory?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Introduction",
                "answers": ["ls"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a two-letter command.",
                    "Think 'list'. Now abbreviate it.",
                    "The answer is: ls",
                ],
            },
            {
                "id": "antech_2",
                "type": "quiz",
                "title": "Position Confirmed",
                "flavor": "The monitoring system wants to know where you are. You want to know first. What prints your exact location in the filesystem?",
                "lesson": (
                    "pwd — prints the full path of your current working directory.\n\n"
                    "Syntax: pwd\n\n"
                    "Common flags:\n"
                    "  -L   use logical path (follows symlinks, default)\n"
                    "  -P   use physical path (resolves symlinks)\n\n"
                    "Example: pwd    → /home/user/projects"
                ),
                "question": "What command prints your current working directory?",
                "answers": ["pwd"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'Print Working Directory'.",
                    "Three letters: P-W-D.",
                    "The answer is: pwd",
                ],
            },
            {
                "id": "antech_3",
                "type": "quiz",
                "title": "Lateral Movement",
                "flavor": "The data isn't in this directory. It never is. One command lets you move through the filesystem without ever touching a mouse.",
                "lesson": (
                    "cd — changes the current working directory.\n\n"
                    "Syntax: cd [directory]\n\n"
                    "Special paths:\n"
                    "  cd ~       go to your home directory\n"
                    "  cd ..      go up one level (parent directory)\n"
                    "  cd -       return to the previous directory\n\n"
                    "Example: cd /etc    → moves into the /etc directory"
                ),
                "question": "What command do you use to change directories?",
                "answers": ["cd"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's 2 letters.",
                    "Think 'Change Directory'.",
                    "The answer is: cd",
                ],
            },
            {
                "id": "antech_4",
                "type": "flag_quiz",
                "title": "Dark Files",
                "flavor": "The corps hide their most sensitive configs as dotfiles — hidden by default, invisible to anyone who doesn't know the flag. What reveals them?",
                "lesson": (
                    "Flags modify how a command behaves. For ls, flags are added after the command name.\n\n"
                    "Hidden files (dotfiles) start with a dot, e.g. .bashrc or .gitignore.\n"
                    "By default, ls does not show them.\n\n"
                    "  -a   show ALL files, including hidden ones\n"
                    "  -A   like -a, but excludes . and ..\n\n"
                    "Example: ls -a    → shows .bashrc, .ssh, and other hidden files"
                ),
                "question": "What flag do you add to 'ls' to show hidden files (dotfiles)?",
                "answers": ["-a", "-la", "-al", "-lah", "-lA", "--all"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It's a single letter flag.",
                    "Think 'all'.",
                    "The answer is: -a (or -la, -al)",
                ],
            },
            {
                "id": "antech_5",
                "type": "live",
                "title": "Allocate Space",
                "flavor": "You need a staging directory. The exfil operation doesn't work without somewhere to stage the data. Create one.",
                "lesson": (
                    "mkdir — creates a new directory.\n\n"
                    "Syntax: mkdir [flags] directory_name\n\n"
                    "Common flags:\n"
                    "  -p   create parent directories as needed (no error if exists)\n"
                    "  -v   verbose — print each directory as it is created\n\n"
                    "Example: mkdir expedition    → creates a directory named 'expedition'"
                ),
                "question": "Create a directory called 'expedition' in the current sandbox directory.",
                "setup": {
                    "files": {},
                    "dirs": [],
                },
                "validation": {
                    "type": "dir_exists",
                    "target": "expedition",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The command is 'mkdir'.",
                    "Try: mkdir expedition",
                    "The full command is: mkdir expedition",
                ],
            },
            {
                "id": "antech_boss",
                "type": "live",
                "title": "BOSS: Security Sweep",
                "flavor": "The passive monitor flagged an anomaly. You have thirty seconds of cover before the active scan starts. Create the directory structure and disappear.",
                "lesson": (
                    "mkdir -p — creates a full directory path in a single command.\n\n"
                    "Syntax: mkdir -p path/to/nested/directory\n\n"
                    "Without -p, mkdir fails if a parent directory does not exist.\n"
                    "With -p, it creates all missing directories along the path.\n\n"
                    "Example: mkdir -p ruins/inner_chamber    → creates 'ruins' and then 'inner_chamber' inside it"
                ),
                "question": (
                    "The Guardian demands a test of navigation mastery:\n"
                    "Create a directory called 'ruins', then inside it create 'inner_chamber'.\n"
                    "(Hint: there's a flag that lets you create nested directories in one step)"
                ),
                "setup": {
                    "files": {},
                    "dirs": [],
                },
                "validation": {
                    "type": "dir_exists",
                    "target": "ruins/inner_chamber",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need to create a directory inside another directory.",
                    "Try: mkdir -p ruins/inner_chamber",
                    "The full command is: mkdir -p ruins/inner_chamber",
                ],
            },
        ],
    },

    "archive_vaults": {
        "id": "archive_vaults",
        "name": "The Dead Drop Vaults",
        "subtitle": "File Operations",
        "color": "yellow",
        "icon": "📚",
        "commands": ["cat", "cp", "mv", "rm", "touch", "file"],
        "challenges": [
            {
                "id": "arch_1",
                "type": "live",
                "title": "Allocate File",
                "flavor": "Before you write to it, you need to create it. An empty placeholder. The corps' monitoring systems log file creation timestamps — that's useful. Create one.",
                "lesson": (
                    "touch — creates an empty file, or updates a file's timestamps if it already exists.\n\n"
                    "Syntax: touch [flags] filename\n\n"
                    "Common flags:\n"
                    "  -a   update only the access time\n"
                    "  -m   update only the modification time\n\n"
                    "Example: touch scroll.txt    → creates an empty file called scroll.txt"
                ),
                "question": "Create an empty file called 'scroll.txt' in the sandbox.",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Basic-Shell-Features",
                "setup": {"files": {}, "dirs": []},
                "validation": {"type": "file_exists", "target": "scroll.txt"},
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The command to create empty files is 'touch'.",
                    "Try: touch scroll.txt",
                    "The answer is: touch scroll.txt",
                ],
            },
            {
                "id": "arch_2",
                "type": "live",
                "title": "Extract the Intercept",
                "flavor": "There's a file on this server. You don't have time to open an editor. You need its contents dumped to the terminal. Now.",
                "lesson": (
                    "cat — concatenates and displays file contents to the terminal.\n\n"
                    "Syntax: cat [flags] file(s)\n\n"
                    "Common flags:\n"
                    "  -n   number all output lines\n"
                    "  -A   show non-printing characters (tabs, line endings)\n\n"
                    "Example: cat ancient_text.txt    → prints the contents of ancient_text.txt"
                ),
                "question": "Display the contents of 'ancient_text.txt' to the terminal.",
                "setup": {
                    "files": {"ancient_text.txt": "In the beginning was the command line.\nAnd it was good.\n"},
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": "In the beginning was the command line.",
                },
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The command is 'cat' — short for concatenate.",
                    "Try: cat ancient_text.txt",
                    "The answer is: cat ancient_text.txt",
                ],
            },
            {
                "id": "arch_3",
                "type": "live",
                "title": "Stage a Copy",
                "flavor": "Never touch the original. Cardinal rule of intrusion work. Copy the file, work on the copy. If anything goes wrong, the original is clean.",
                "lesson": (
                    "cp — copies files or directories from one location to another.\n\n"
                    "Syntax: cp [flags] source destination\n\n"
                    "Common flags:\n"
                    "  -r   recursive (required to copy directories)\n"
                    "  -i   interactive — prompt before overwriting\n"
                    "  -v   verbose — show files as they are copied\n\n"
                    "Example: cp artifact.dat artifact_backup.dat    → creates a copy with a new name"
                ),
                "question": "Copy 'artifact.dat' to a new file called 'artifact_backup.dat'.",
                "setup": {
                    "files": {"artifact.dat": "ARTIFACT DATA: 0xDEADBEEF\n"},
                    "dirs": [],
                },
                "validation": {"type": "file_exists", "target": "artifact_backup.dat"},
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The copy command is 'cp'.",
                    "Syntax: cp <source> <destination>",
                    "The answer is: cp artifact.dat artifact_backup.dat",
                ],
            },
            {
                "id": "arch_4",
                "type": "live",
                "title": "Cover Your Tracks",
                "flavor": "The file has the wrong name — it'll get flagged in the next audit sweep. Rename it to something that looks like it belongs here.",
                "lesson": (
                    "mv — moves or renames files and directories.\n\n"
                    "Syntax: mv [flags] source destination\n\n"
                    "Common flags:\n"
                    "  -i   interactive — prompt before overwriting\n"
                    "  -v   verbose — show what is being moved\n"
                    "  -n   no-clobber — do not overwrite existing files\n\n"
                    "Example: mv wrongname.txt correctname.txt    → renames the file in place"
                ),
                "question": "Rename 'wrongname.txt' to 'correctname.txt'.",
                "setup": {
                    "files": {"wrongname.txt": "I have the wrong name!\n"},
                    "dirs": [],
                },
                "validation": {"type": "file_exists", "target": "correctname.txt"},
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "In bash, renaming uses the 'mv' (move) command.",
                    "Syntax: mv <old_name> <new_name>",
                    "The answer is: mv wrongname.txt correctname.txt",
                ],
            },
            {
                "id": "arch_5",
                "type": "live",
                "title": "Wipe the Evidence",
                "flavor": "That file is a liability. It links back to you. Delete it — and remember: rm has no undo button. That's the point.",
                "lesson": (
                    "rm — removes (deletes) files or directories. There is no trash — deletion is permanent.\n\n"
                    "Syntax: rm [flags] file(s)\n\n"
                    "Common flags:\n"
                    "  -r   recursive — delete directories and their contents\n"
                    "  -f   force — ignore nonexistent files, no prompts\n"
                    "  -i   interactive — prompt before each deletion\n\n"
                    "Example: rm heresy.txt    → permanently deletes heresy.txt"
                ),
                "question": "Delete the file called 'heresy.txt'.",
                "setup": {
                    "files": {"heresy.txt": "This file should not exist.\n"},
                    "dirs": [],
                },
                "validation": {"type": "file_missing", "target": "heresy.txt"},
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The remove command is 'rm'.",
                    "Try: rm heresy.txt",
                    "The answer is: rm heresy.txt",
                ],
            },
            {
                "id": "arch_boss",
                "type": "live",
                "title": "BOSS: The Dead Drop Protocol",
                "flavor": "Multi-step extraction. No room for mistakes. The vault's integrity checker runs every ninety seconds. You have one pass to get this right.",
                "lesson": (
                    "Chaining commands — run multiple commands in sequence using && or ;.\n\n"
                    "  cmd1 && cmd2   runs cmd2 only if cmd1 succeeds\n"
                    "  cmd1 ; cmd2    runs cmd2 regardless of cmd1's result\n\n"
                    "This challenge uses mkdir, touch, and cp together:\n\n"
                    "Example: mkdir archive && touch archive/manifest.txt && cp source.dat archive/"
                ),
                "question": (
                    "Multi-step challenge:\n"
                    "1. Create a directory called 'archive'\n"
                    "2. Create a file called 'manifest.txt' inside it\n"
                    "3. Copy 'source.dat' into the archive directory\n\n"
                    "You can use semicolons or && to chain commands."
                ),
                "setup": {
                    "files": {"source.dat": "CLASSIFIED ARCHIVE DATA\n"},
                    "dirs": [],
                },
                "validation": {
                    "type": "multi",
                    "checks": [
                        {"type": "dir_exists", "target": "archive"},
                        {"type": "file_exists", "target": "archive/manifest.txt"},
                        {"type": "file_exists", "target": "archive/source.dat"},
                    ],
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need mkdir, touch, and cp.",
                    "Try: mkdir archive && touch archive/manifest.txt && cp source.dat archive/",
                    "Full command: mkdir archive && touch archive/manifest.txt && cp source.dat archive/",
                ],
            },
        ],
    },

    "oracle_library": {
        "id": "oracle_library",
        "name": "The Signal Broker",
        "subtitle": "Intelligence Extraction",
        "color": "magenta",
        "icon": "📡",
        "commands": ["grep", "find", "sort", "uniq", "wc"],
        "challenges": [
            {
                "id": "oracle_1",
                "type": "quiz",
                "title": "Pattern Match",
                "flavor": "There's signal in this noise. Megabytes of corporate logs and exactly one line that matters. What tool extracts it?",
                "lesson": (
                    "grep — searches for lines matching a pattern in files or piped input.\n\n"
                    "Syntax: grep [flags] pattern [file...]\n\n"
                    "Common flags:\n"
                    "  -i   case-insensitive search\n"
                    "  -r   recursive (search through directories)\n"
                    "  -n   show line numbers\n"
                    "  -v   invert match (show lines that do NOT match)\n\n"
                    "Example: grep 'error' system.log    → prints every line containing 'error'"
                ),
                "question": "What command searches for patterns within files?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Pattern-Matching",
                "answers": ["grep"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'Global Regular Expression Print'.",
                    "It's a 4-letter command starting with 'g'.",
                    "The answer is: grep",
                ],
            },
            {
                "id": "oracle_2",
                "type": "live",
                "title": "Extract the Signal",
                "flavor": "The intercept file is full of noise. The word you need is in there three times, buried in hundreds of lines. Pull it out.",
                "lesson": (
                    "grep — filters lines from a file that contain a given word or pattern.\n\n"
                    "Syntax: grep pattern filename\n\n"
                    "Common flags:\n"
                    "  -i   ignore case\n"
                    "  -c   count matching lines instead of printing them\n"
                    "  -l   print only filenames that contain a match\n\n"
                    "Example: grep prophecy scrolls.txt    → prints all lines containing 'prophecy'"
                ),
                "question": "Find all lines containing the word 'prophecy' in 'scrolls.txt'.",
                "setup": {
                    "files": {
                        "scrolls.txt": (
                            "The beginning was the command line.\n"
                            "A prophecy was written in bash.\n"
                            "Many artifacts were found.\n"
                            "The prophecy speaks of a grandmaster.\n"
                            "Regular expressions hold the key.\n"
                        )
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": "prophecy",
                },
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Use grep to search for a pattern.",
                    "Syntax: grep <pattern> <file>",
                    "The answer is: grep prophecy scrolls.txt",
                ],
            },
            {
                "id": "oracle_3",
                "type": "live",
                "title": "Quantify the Breach",
                "flavor": "The client wants numbers. How many log entries? How many lines compromised? Don't read it — count it.",
                "lesson": (
                    "wc — counts lines, words, and bytes in a file or from piped input.\n\n"
                    "Syntax: wc [flags] [file...]\n\n"
                    "Common flags:\n"
                    "  -l   count lines only\n"
                    "  -w   count words only\n"
                    "  -c   count bytes only\n"
                    "  -m   count characters only\n\n"
                    "Example: wc -l tome.txt    → prints the number of lines in tome.txt"
                ),
                "question": "Count the number of lines in 'tome.txt'.",
                "setup": {
                    "files": {
                        "tome.txt": "line one\nline two\nline three\nline four\nline five\n"
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": "5",
                },
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The word-count command is 'wc'. Use the -l flag for lines.",
                    "Try: wc -l tome.txt",
                    "The answer is: wc -l tome.txt",
                ],
            },
            {
                "id": "oracle_4",
                "type": "live",
                "title": "Sort the Feed",
                "flavor": "The data dump came out of order. You need it alphabetical before you can do anything useful with it. Run it through the sorter.",
                "lesson": (
                    "sort — sorts lines of text alphabetically or numerically.\n\n"
                    "Syntax: sort [flags] [file...]\n\n"
                    "Common flags:\n"
                    "  -r   reverse order (Z to A, or largest to smallest)\n"
                    "  -n   numeric sort (treat values as numbers)\n"
                    "  -u   unique — remove duplicate lines after sorting\n\n"
                    "Example: sort chaos.txt    → prints lines of chaos.txt in alphabetical order"
                ),
                "question": "Sort the contents of 'chaos.txt' alphabetically and display them.",
                "setup": {
                    "files": {
                        "chaos.txt": "zebra\napple\nmango\nbanana\nkiwi\n"
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": "apple",
                },
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The sort command arranges lines alphabetically.",
                    "Try: sort chaos.txt",
                    "The answer is: sort chaos.txt",
                ],
            },
            {
                "id": "oracle_5",
                "type": "live",
                "title": "Hunt the Log",
                "flavor": "The logs are scattered through subdirectories the way the corps scatter blame — everywhere and nowhere. Hunt them down by extension.",
                "lesson": (
                    "find — walks a directory tree and finds files matching given criteria.\n\n"
                    "Syntax: find [path] [expression]\n\n"
                    "Common flags:\n"
                    "  -name pattern   match by filename (supports wildcards like *.log)\n"
                    "  -type f         match only regular files\n"
                    "  -type d         match only directories\n"
                    "  -mtime -1       modified in the last 1 day\n\n"
                    "Example: find . -name '*.log'    → finds all .log files from the current directory down"
                ),
                "question": "Find all files ending in '.log' in the current directory and subdirectories.",
                "setup": {
                    "files": {
                        "system.log": "LOG: system started\n",
                        "notes.txt": "not a log\n",
                        "subdir/error.log": "LOG: error occurred\n",
                    },
                    "dirs": ["subdir"],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": ".log",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use the 'find' command.",
                    "Syntax: find <path> -name <pattern>",
                    "The answer is: find . -name '*.log'",
                ],
            },
            {
                "id": "oracle_boss",
                "type": "live",
                "title": "BOSS: Deduplicate the Feed",
                "flavor": "The data stream is poisoned with duplicates — a classic corp obfuscation technique. Extract only unique entries, sorted, counted. Clean signal only.",
                "lesson": (
                    "uniq — filters out consecutive duplicate lines. Usually used after sort.\n\n"
                    "Syntax: uniq [flags] [file]\n\n"
                    "Common flags:\n"
                    "  -c   prefix lines with the count of occurrences\n"
                    "  -d   only print duplicate lines\n"
                    "  -u   only print unique (non-duplicate) lines\n\n"
                    "Example: sort data.txt | uniq | wc -l    → counts distinct lines in data.txt"
                ),
                "question": (
                    "The Oracle's challenge:\n"
                    "Find all unique words that appear in 'data.txt',\n"
                    "sort them, and count how many unique lines exist."
                ),
                "setup": {
                    "files": {
                        "data.txt": "alpha\nbeta\nalpha\ngamma\nbeta\ndelta\ngamma\nalpha\n"
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": "4",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need to chain sort, uniq, and wc -l.",
                    "Use pipes: sort data.txt | uniq | wc -l",
                    "The answer is: sort data.txt | uniq | wc -l",
                ],
            },
        ],
    },

    "pipe_sanctum": {
        "id": "pipe_sanctum",
        "name": "The Pipe Works",
        "subtitle": "Signal Routing",
        "color": "blue",
        "icon": "🔌",
        "commands": ["|", ">", ">>", "<", "tee", "xargs"],
        "challenges": [
            {
                "id": "pipe_1",
                "type": "quiz",
                "title": "The Connector",
                "flavor": "One character. Invented in 1973. The corps have spent fifty years trying to abstract away from it. What routes output from one command into the next?",
                "lesson": (
                    "| (pipe) — sends the output of one command as input to the next command.\n\n"
                    "Syntax: command1 | command2\n\n"
                    "Pipes let you chain tools together so data flows from left to right.\n"
                    "Each command reads from the previous one's output.\n\n"
                    "Example: ls | grep '.txt'    → lists files, then filters for only .txt files"
                ),
                "question": "What symbol is used to pipe the output of one command into another?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Pipelines",
                "answers": ["|", "pipe"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a single character, found above the backslash on most keyboards.",
                    "It's called the 'pipe' symbol.",
                    "The answer is: |",
                ],
            },
            {
                "id": "pipe_2",
                "type": "live",
                "title": "Route the Signal",
                "flavor": "The directory has noise in it. You need only the text files. Chain ls and grep — don't write to disk, don't open an editor. Just route it.",
                "lesson": (
                    "| (pipe) — connects commands so the output of one feeds directly into the next.\n\n"
                    "Syntax: command1 | command2 | command3 ...\n\n"
                    "You can chain as many commands as needed.\n"
                    "No intermediate files are created — data flows in memory.\n\n"
                    "Example: ls | grep '.txt'    → shows only filenames that contain '.txt'"
                ),
                "question": "List all files in the current directory and pipe the output to 'grep' to filter only '.txt' files.",
                "setup": {
                    "files": {
                        "readme.txt": "read me\n",
                        "data.csv": "data\n",
                        "notes.txt": "notes\n",
                        "binary.bin": "binary\n",
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "output_contains",
                    "expected": ".txt",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use ls and pipe to grep.",
                    "Try: ls | grep .txt",
                    "The answer is: ls | grep .txt",
                ],
            },
            {
                "id": "pipe_3",
                "type": "live",
                "title": "Write to Disk",
                "flavor": "Terminal output is ephemeral. One scroll and it's gone. Capture it — redirect it into a file so it survives the session.",
                "lesson": (
                    "> (redirect) — writes command output to a file, overwriting any existing content.\n\n"
                    "Syntax: command > filename\n\n"
                    "Related operators:\n"
                    "  >>   append to a file instead of overwriting\n"
                    "  2>   redirect error output (stderr) to a file\n\n"
                    "Example: echo 'EXCAVATED DATA' > output.txt    → creates output.txt with that text"
                ),
                "question": "Write the text 'EXCAVATED DATA' into a file called 'output.txt' using redirection.",
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_contains",
                    "target": "output.txt",
                    "expected": "EXCAVATED DATA",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use echo with the > redirection operator.",
                    "Try: echo 'EXCAVATED DATA' > output.txt",
                    "The answer is: echo 'EXCAVATED DATA' > output.txt",
                ],
            },
            {
                "id": "pipe_4",
                "type": "live",
                "title": "Append the Entry",
                "flavor": "> destroys what was there. >> preserves it. You're updating a live log — wrong operator and the entire operation history is gone.",
                "lesson": (
                    ">> (append redirect) — adds output to the end of a file without erasing existing content.\n\n"
                    "Syntax: command >> filename\n\n"
                    "Comparison:\n"
                    "  >    overwrites the file each time (destructive)\n"
                    "  >>   appends to the file (preserves existing content)\n\n"
                    "Example: echo 'SECOND ENTRY' >> log.txt    → adds a line to log.txt without erasing it"
                ),
                "question": "Append the line 'SECOND ENTRY' to 'log.txt' without overwriting it.",
                "setup": {
                    "files": {"log.txt": "FIRST ENTRY\n"},
                    "dirs": [],
                },
                "validation": {
                    "type": "file_contains",
                    "target": "log.txt",
                    "expected": "FIRST ENTRY",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use >> to append instead of overwrite.",
                    "Try: echo 'SECOND ENTRY' >> log.txt",
                    "The answer is: echo 'SECOND ENTRY' >> log.txt",
                ],
            },
            {
                "id": "pipe_5",
                "type": "fill_blank",
                "title": "Split the Stream",
                "flavor": "You need to watch the output AND save it. Not one or the other. One command splits the stream — screen and file simultaneously.",
                "lesson": (
                    "tee — reads from stdin and writes to both stdout (the screen) and a file simultaneously.\n\n"
                    "Syntax: command | tee [flags] filename\n\n"
                    "Common flags:\n"
                    "  -a   append to the file instead of overwriting it\n\n"
                    "Named after the T-shaped pipe fitting that splits flow in two directions.\n\n"
                    "Example: echo 'SACRED TEXT' | tee record.txt    → prints to screen AND saves to record.txt"
                ),
                "question": "Complete this command to both display output AND save it to 'record.txt':\n\necho 'SACRED TEXT' | ___ record.txt",
                "answers": ["tee"],
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "The command is named after a T-shaped pipe fitting.",
                    "It starts with 't'.",
                    "The answer is: tee",
                ],
            },
            {
                "id": "pipe_boss",
                "type": "live",
                "title": "BOSS: The Full Pipeline",
                "flavor": "One command chain. No intermediate files. List, filter, count, save. The monitoring system won't wait for you to figure this out step by step.",
                "lesson": (
                    "Combining pipes and redirection — chain | and > to process and save data in one command.\n\n"
                    "Syntax: cmd1 | cmd2 | cmd3 > output_file\n\n"
                    "Data flows left to right through each pipe.\n"
                    "The final > captures the end result into a file.\n\n"
                    "Example: ls | grep '.txt' | wc -l > count.txt    → counts .txt files and saves the number"
                ),
                "question": (
                    "Build a pipeline that:\n"
                    "1. Lists all files in the sandbox\n"
                    "2. Filters for only .txt files\n"
                    "3. Counts how many there are\n"
                    "4. Saves the count to 'count.txt'"
                ),
                "setup": {
                    "files": {
                        "alpha.txt": "a\n",
                        "beta.txt": "b\n",
                        "gamma.txt": "c\n",
                        "data.bin": "binary\n",
                        "config.cfg": "config\n",
                    },
                    "dirs": [],
                },
                "validation": {
                    "type": "file_exists",
                    "target": "count.txt",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Chain: ls | grep | wc -l and redirect to a file.",
                    "Try: ls | grep '.txt' | wc -l > count.txt",
                    "The answer is: ls | grep '.txt' | wc -l > count.txt",
                ],
            },
        ],
    },

    "process_catacombs": {
        "id": "process_catacombs",
        "name": "The Ghost Stack",
        "subtitle": "Process Control",
        "color": "red",
        "icon": "👾",
        "commands": ["ps", "kill", "jobs", "bg", "fg", "top"],
        "challenges": [
            {
                "id": "proc_1",
                "type": "quiz",
                "title": "Enumerate the Daemons",
                "flavor": "Something on this server is watching for intrusion. You can't kill it if you can't see it. What command shows currently running processes?",
                "lesson": (
                    "ps — displays a snapshot of currently running processes.\n\n"
                    "Syntax: ps [flags]\n\n"
                    "Common flags:\n"
                    "  aux   show all processes for all users in detail (BSD style)\n"
                    "  -ef   show all processes in full format (UNIX style)\n\n"
                    "Each process has a PID (Process ID), which uniquely identifies it.\n\n"
                    "Example: ps    → shows processes running in the current terminal session"
                ),
                "question": "What command shows currently running processes?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Job-Control",
                "answers": ["ps"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'process status'.",
                    "It's two letters.",
                    "The answer is: ps",
                ],
            },
            {
                "id": "proc_2",
                "type": "flag_quiz",
                "title": "Full Enumeration",
                "flavor": "The basic ps output only shows your own processes. The ghost processes — the corp's daemons — run under other users. What flags expose everything?",
                "lesson": (
                    "ps flags — control which processes are shown and how much detail is displayed.\n\n"
                    "  a   show processes for all users (not just yours)\n"
                    "  u   user-oriented format (shows username, CPU, memory)\n"
                    "  x   include processes not attached to a terminal\n\n"
                    "Combined: ps aux shows every process on the system in a readable format.\n\n"
                    "Example: ps aux    → full system-wide process list with CPU and memory usage"
                ),
                "question": "What flags do you use with 'ps' to see ALL processes from ALL users in a detailed format?",
                "answers": ["aux", "-aux", "aux", "axu", "-ef", "ef"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Two common combinations work: ps aux or ps -ef",
                    "The most common is 'aux'.",
                    "The answer is: aux (making it: ps aux)",
                ],
            },
            {
                "id": "proc_3",
                "type": "quiz",
                "title": "Terminate the Watcher",
                "flavor": "It's watching you. You found its PID. One command ends it — cleanly if you're lucky, hard if you're not. What command sends a kill signal by PID?",
                "lesson": (
                    "kill — sends a signal to a process, typically to terminate it.\n\n"
                    "Syntax: kill [signal] PID\n\n"
                    "Common signals:\n"
                    "  -15  SIGTERM — politely ask the process to stop (default)\n"
                    "  -9   SIGKILL — force-kill immediately, cannot be ignored\n"
                    "  -1   SIGHUP  — reload configuration\n\n"
                    "Example: kill 1234    → sends SIGTERM to process with PID 1234"
                ),
                "question": "What command sends a signal to terminate a process by PID?",
                "answers": ["kill"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It's a very direct command name.",
                    "It starts with 'k'.",
                    "The answer is: kill",
                ],
            },
            {
                "id": "proc_4",
                "type": "quiz",
                "title": "Live Surveillance",
                "flavor": "Static snapshots aren't enough. You need a live feed — all processes, updating every second, CPU usage, memory consumption. One command does this.",
                "lesson": (
                    "top — displays a live, auto-refreshing view of all running processes and system resources.\n\n"
                    "Syntax: top\n\n"
                    "While running:\n"
                    "  q      quit\n"
                    "  k      kill a process (enter its PID when prompted)\n"
                    "  M      sort by memory usage\n"
                    "  P      sort by CPU usage\n\n"
                    "Example: top    → opens an interactive real-time process monitor"
                ),
                "question": "What interactive command gives a real-time view of all system processes?",
                "answers": ["top", "htop"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It shows you what's happening 'at the top'.",
                    "It's three letters.",
                    "The answer is: top",
                ],
            },
            {
                "id": "proc_5",
                "type": "live",
                "title": "Find the Process",
                "flavor": "You know the process name. You need its PID. Enumerate everything and filter. Classic pipeline work. Fast and quiet.",
                "lesson": (
                    "ps aux | grep — combines process listing with pattern matching to find specific processes.\n\n"
                    "Syntax: ps aux | grep process_name\n\n"
                    "ps aux lists all processes; grep filters for lines matching your pattern.\n"
                    "This is one of the most common process-inspection idioms in shell work.\n\n"
                    "Example: ps aux | grep bash    → shows all running bash processes"
                ),
                "question": (
                    "Run 'ps aux' and pipe it to grep to find the 'bash' process.\n"
                    "Show all lines containing 'bash'."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "bash",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use ps aux piped to grep.",
                    "Try: ps aux | grep bash",
                    "The answer is: ps aux | grep bash",
                ],
            },
            {
                "id": "proc_boss",
                "type": "live",
                "title": "BOSS: Ghost PID Extraction",
                "flavor": "The corp's intrusion detection needs your shell's PID to flag you. Save it to disk before it finds you — and hide the evidence in a file only you can find.",
                "lesson": (
                    "$$ — a special bash variable that holds the PID of the current shell process.\n\n"
                    "Special bash variables:\n"
                    "  $$   PID of the current shell\n"
                    "  $!   PID of the last background process\n"
                    "  $?   exit status of the last command\n"
                    "  $0   name of the current script or shell\n\n"
                    "Example: echo $$    → prints the PID of your running bash session"
                ),
                "question": (
                    "The Necromancer demands:\n"
                    "Find your current shell's process ID and save it to 'my_pid.txt'.\n\n"
                    "Hint: bash has a special variable that holds the current shell's PID."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_exists",
                    "target": "my_pid.txt",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Use the special $$ variable which contains the current shell's PID.",
                    "Try: echo $$ > my_pid.txt",
                    "The answer is: echo $$ > my_pid.txt",
                ],
            },
        ],
    },

    "permissions_fortress": {
        "id": "permissions_fortress",
        "name": "The Access Grid",
        "subtitle": "Permission Systems",
        "color": "green",
        "icon": "🔒",
        "commands": ["chmod", "chown", "ls -l", "umask"],
        "challenges": [
            {
                "id": "perm_1",
                "type": "quiz",
                "title": "Read the Access String",
                "flavor": "Every file has a ten-character access string. The corps think it's invisible. You need to see it — and know exactly what it means.",
                "lesson": (
                    "ls -l — shows files in long format, including permissions, owner, size, and date.\n\n"
                    "Syntax: ls -l [directory]\n\n"
                    "Permission string format: -rwxr-xr--\n"
                    "  Position 1:   file type (- = file, d = directory, l = symlink)\n"
                    "  Positions 2-4: owner permissions (r=read, w=write, x=execute)\n"
                    "  Positions 5-7: group permissions\n"
                    "  Positions 8-10: other (world) permissions\n\n"
                    "Example: ls -l    → shows permissions, owner, size, and name of each file"
                ),
                "question": "What flag do you add to 'ls' to see detailed permissions for each file?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Bourne-Shell-Builtins",
                "answers": ["-l", "-la", "-al", "-lh"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a single letter flag meaning 'long' format.",
                    "It's -l (lowercase L).",
                    "The answer is: -l",
                ],
            },
            {
                "id": "perm_2",
                "type": "quiz",
                "title": "Modify Access",
                "flavor": "The access bits are wrong. The corporate security team misconfigured this file. One command fixes it — or breaks it wider open. Your call.",
                "lesson": (
                    "chmod — changes the permission mode of a file or directory.\n\n"
                    "Syntax: chmod [mode] file\n\n"
                    "Symbolic mode examples:\n"
                    "  u+x   add execute for owner (u=user, g=group, o=other, a=all)\n"
                    "  go-w  remove write from group and others\n"
                    "  a+r   add read for everyone\n\n"
                    "Example: chmod u+x script.sh    → makes script.sh executable by its owner"
                ),
                "question": "What command changes file permissions?",
                "answers": ["chmod"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'change mode'.",
                    "It's 5 characters: chmod.",
                    "The answer is: chmod",
                ],
            },
            {
                "id": "perm_3",
                "type": "live",
                "title": "Make It Runnable",
                "flavor": "The exploit script is there. The permissions say it can't execute. The corp's sysadmin forgot to flip the bit. You remember. Fix it.",
                "lesson": (
                    "chmod +x — adds execute permission, allowing a file to be run as a program.\n\n"
                    "Syntax: chmod [who]+x filename\n\n"
                    "  chmod +x file      adds execute for all (owner, group, others)\n"
                    "  chmod u+x file     adds execute for the owner only\n"
                    "  chmod a+x file     same as +x, explicitly all\n\n"
                    "Example: chmod u+x spell.sh    → makes spell.sh runnable by its owner"
                ),
                "question": "Make 'spell.sh' executable by its owner.",
                "setup": {
                    "files": {"spell.sh": "#!/bin/bash\necho 'The spell is cast!'\n"},
                    "dirs": [],
                },
                "validation": {
                    "type": "file_executable",
                    "target": "spell.sh",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use chmod with 'u+x' to add execute permission for the owner.",
                    "Try: chmod u+x spell.sh",
                    "Or: chmod +x spell.sh",
                ],
            },
            {
                "id": "perm_4",
                "type": "fill_blank",
                "title": "Octal Code",
                "flavor": "Symbolic flags are for beginners. Real permission work uses octal notation — three digits that contain more access control information than most corps' entire security dashboards.",
                "lesson": (
                    "chmod numeric mode — sets permissions using a 3-digit octal number (owner, group, others).\n\n"
                    "Each digit is the sum of: 4=read, 2=write, 1=execute\n\n"
                    "  7 = rwx (4+2+1)   full access\n"
                    "  6 = rw-  (4+2)    read and write\n"
                    "  5 = r-x  (4+1)    read and execute\n"
                    "  4 = r--  (4)      read only\n\n"
                    "Example: chmod 754 file    → owner=rwx, group=r-x, others=r--"
                ),
                "question": (
                    "Complete the command to give the owner full permissions (rwx),\n"
                    "group read+execute (r-x), and others read-only (r--):\n\n"
                    "chmod ___ mysecret.txt"
                ),
                "answers": ["754", "0754"],
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "Owner=7 (rwx), Group=5 (r-x), Others=4 (r--)",
                    "Combine the numbers: 754",
                    "The answer is: 754",
                ],
            },
            {
                "id": "perm_5",
                "type": "live",
                "title": "Lockdown Protocol",
                "flavor": "This file contains the extracted credentials. If any other process can read it, the whole operation is blown. Lock it to owner-only access.",
                "lesson": (
                    "chmod 600 — sets a file to be readable and writable by the owner only, with no access for anyone else.\n\n"
                    "Syntax: chmod 600 filename\n\n"
                    "Common secure permission modes:\n"
                    "  600  rw-------  private files (SSH keys, credentials)\n"
                    "  644  rw-r--r--  normal files (readable by all, writable by owner)\n"
                    "  700  rwx------  private executables or directories\n\n"
                    "Example: chmod 600 secrets.txt    → only the owner can read or write secrets.txt"
                ),
                "question": "Set permissions on 'secrets.txt' so ONLY the owner can read it (chmod 600).",
                "setup": {
                    "files": {"secrets.txt": "TOP SECRET SHELL KNOWLEDGE\n"},
                    "dirs": [],
                },
                "validation": {
                    "type": "file_perms",
                    "target": "secrets.txt",
                    "expected_mode": "600",
                },
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "Use chmod with numeric mode 600.",
                    "Try: chmod 600 secrets.txt",
                    "The answer is: chmod 600 secrets.txt",
                ],
            },
            {
                "id": "perm_boss",
                "type": "live",
                "title": "BOSS: Deploy and Secure",
                "flavor": "Create the payload script. Set it executable and world-readable. One chain of commands — because the access audit runs in forty-five seconds.",
                "lesson": (
                    "chmod 755 — the standard permission for executable scripts shared with others.\n\n"
                    "755 means:\n"
                    "  7 (rwx) — owner can read, write, and execute\n"
                    "  5 (r-x) — group can read and execute\n"
                    "  5 (r-x) — others can read and execute\n\n"
                    "This is the typical permission for shell scripts and programs on a system.\n\n"
                    "Example: touch vault.sh && chmod 755 vault.sh    → creates and makes vault.sh world-executable"
                ),
                "question": (
                    "The Warden's challenge:\n"
                    "1. Create a file called 'vault.sh'\n"
                    "2. Make it executable by everyone (chmod 755)\n\n"
                    "Chain both commands together on one line."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "multi",
                    "checks": [
                        {"type": "file_exists", "target": "vault.sh"},
                        {"type": "file_perms", "target": "vault.sh", "expected_mode": "755"},
                    ],
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need touch and then chmod.",
                    "Try: touch vault.sh && chmod 755 vault.sh",
                    "The answer is: touch vault.sh && chmod 755 vault.sh",
                ],
            },
        ],
    },

    "scripting_citadel": {
        "id": "scripting_citadel",
        "name": "The Code Forge",
        "subtitle": "Shell Scripting",
        "color": "yellow",
        "icon": "⚙️",
        "commands": ["variables", "loops", "if/else", "functions"],
        "challenges": [
            {
                "id": "script_1",
                "type": "live",
                "title": "Memory Allocation",
                "flavor": "You're about to use the same string eight times in this script. Sane people store it in a variable. The corps' sysadmins copy-paste it eight times. That's why you're here and they're not.",
                "lesson": (
                    "Variables — store values in the shell so they can be reused.\n\n"
                    "Syntax: VARNAME=value    (no spaces around the = sign)\n\n"
                    "To use a variable, prefix its name with $:\n"
                    "  echo $VARNAME    → prints the variable's value\n\n"
                    "Variable names are case-sensitive. ALL_CAPS is conventional for environment variables.\n\n"
                    "Example: HERO=HackerArchaeologist && echo $HERO    → prints: HackerArchaeologist"
                ),
                "question": "Create a variable called 'HERO' with value 'HackerArchaeologist' and echo it.",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Variables",
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "HackerArchaeologist",
                },
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Assign with: VARNAME=value (no spaces around =)",
                    "Then use: echo $VARNAME",
                    "Full command: HERO=HackerArchaeologist && echo $HERO",
                ],
            },
            {
                "id": "script_2",
                "type": "live",
                "title": "Conditional Logic",
                "flavor": "Every exploit needs decision logic. If the target is vulnerable, execute. If not, abort cleanly. This is the most fundamental structure in any real script.",
                "lesson": (
                    "if/else — executes commands conditionally based on whether a test is true or false.\n\n"
                    "Syntax: if [ condition ]; then commands; fi\n\n"
                    "Common test operators:\n"
                    "  -gt   greater than (numeric)\n"
                    "  -lt   less than (numeric)\n"
                    "  -eq   equal (numeric)\n"
                    "  =     equal (string)\n\n"
                    "Example: if [ 5 -gt 3 ]; then echo 'YES'; fi    → prints YES because 5 > 3"
                ),
                "question": (
                    "Run a bash one-liner that checks if 5 is greater than 3\n"
                    "and prints 'YES' if true.\n\n"
                    "Try: if [ 5 -gt 3 ]; then echo 'YES'; fi"
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "YES",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use if [ condition ]; then ... fi syntax.",
                    "For greater-than, use -gt.",
                    "Try: if [ 5 -gt 3 ]; then echo 'YES'; fi",
                ],
            },
            {
                "id": "script_3",
                "type": "live",
                "title": "Iteration Protocol",
                "flavor": "Manual repetition is for interns and people who haven't discovered loops. You need to hit forty targets. Writing forty commands individually is not an option.",
                "lesson": (
                    "for loop — repeats a block of commands for each item in a list.\n\n"
                    "Syntax: for variable in list; do commands; done\n\n"
                    "The list can be literal values, a range, or command output:\n"
                    "  for i in 1 2 3       explicit list\n"
                    "  for i in $(seq 1 5)  range using seq\n"
                    "  for f in *.txt       all .txt files\n\n"
                    "Example: for i in 1 2 3; do echo $i; done    → prints 1, 2, 3 on separate lines"
                ),
                "question": "Write a for loop that prints the numbers 1, 2, and 3.",
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "1",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use: for var in values; do commands; done",
                    "Try: for i in 1 2 3; do echo $i; done",
                    "The answer is: for i in 1 2 3; do echo $i; done",
                ],
            },
            {
                "id": "script_4",
                "type": "live",
                "title": "Write the Tool",
                "flavor": "You need this to run repeatedly. A one-liner won't cut it. Write a proper script — shebang, commands, ready to execute. This is how the pros do persistent access.",
                "lesson": (
                    "Bash scripts — text files containing shell commands, run as programs.\n\n"
                    "Every script should start with a shebang line that tells the OS which interpreter to use:\n"
                    "  #!/bin/bash\n\n"
                    "After writing the script, make it executable with chmod +x, then run it with ./script.sh\n\n"
                    "Example: printf '#!/bin/bash\\necho THE QUEST BEGINS\\n' > quest.sh"
                ),
                "question": (
                    "Create a bash script called 'quest.sh' that echoes 'THE QUEST BEGINS'.\n"
                    "It must start with a shebang line (#!/bin/bash)."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_contains",
                    "target": "quest.sh",
                    "expected": "#!/bin/bash",
                },
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "Use printf or echo with escape sequences to write the file.",
                    "The shebang line is: #!/bin/bash",
                    "Try: printf '#!/bin/bash\\necho THE QUEST BEGINS\\n' > quest.sh",
                ],
            },
            {
                "id": "script_5",
                "type": "live",
                "title": "Encapsulate the Attack",
                "flavor": "You're calling the same logic from three different places in your script. Functions exist for exactly this reason. Encapsulate it. Call it by name. Write it once.",
                "lesson": (
                    "Functions — named, reusable blocks of commands in bash.\n\n"
                    "Syntax: funcname() { commands; }\n\n"
                    "Define first, then call by name. Functions can accept arguments via $1, $2, etc.\n"
                    "  greet() { echo \"Hello, $1\"; }\n"
                    "  greet World    → prints: Hello, World\n\n"
                    "Example: greet() { echo 'GREETINGS TRAVELER'; }; greet    → calls and runs the function"
                ),
                "question": (
                    "Define a bash function called 'greet' that echoes 'GREETINGS TRAVELER',\n"
                    "then call it."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "GREETINGS TRAVELER",
                },
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "Define with: funcname() { commands; }",
                    "Then call it by name.",
                    "Try: greet() { echo 'GREETINGS TRAVELER'; }; greet",
                ],
            },
            {
                "id": "script_boss",
                "type": "live",
                "title": "BOSS: The Full Tool",
                "flavor": "The corps' countermeasure adapts to single commands. You need a real script — variables, loops, logic. Write it. Deploy it. The monitoring window is closing.",
                "lesson": (
                    "Combining scripting constructs — real scripts use variables, loops, and conditionals together.\n\n"
                    "A typical script structure:\n"
                    "  #!/bin/bash          shebang\n"
                    "  COUNT=3              variable assignment\n"
                    "  for i in $(seq 1 $COUNT); do    loop using the variable\n"
                    "    echo $i            body of loop\n"
                    "  done\n\n"
                    "seq generates a numeric sequence: seq 1 5 → 1 2 3 4 5"
                ),
                "question": (
                    "Create 'masterwork.sh' containing a script that:\n"
                    "- Starts with #!/bin/bash\n"
                    "- Sets a variable COUNT=3\n"
                    "- Uses a for loop with seq to print 1 through $COUNT\n\n"
                    "Use printf to write the script contents to the file."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_contains",
                    "target": "masterwork.sh",
                    "expected": "#!/bin/bash",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Create a .sh file with a shebang, variable, and for loop.",
                    "Use printf to write the file with newlines.",
                    "Try: printf '#!/bin/bash\\nCOUNT=3\\nfor i in $(seq 1 $COUNT); do echo $i; done\\n' > masterwork.sh",
                ],
            },
        ],
    },

    "network_nexus": {
        "id": "network_nexus",
        "name": "The Meat Highway",
        "subtitle": "Network Operations",
        "color": "cyan",
        "icon": "🌐",
        "commands": ["curl", "ping", "ssh", "netstat", "wget"],
        "challenges": [
            {
                "id": "net_1",
                "type": "quiz",
                "title": "Host Reachability",
                "flavor": "Before you attempt anything against a remote target, you need to know it's alive. One command sends a probe and listens for the echo.",
                "lesson": (
                    "ping — sends ICMP echo request packets to a host to test if it is reachable.\n\n"
                    "Syntax: ping [flags] hostname_or_IP\n\n"
                    "Common flags:\n"
                    "  -c N   send exactly N packets then stop (without this, ping runs forever)\n"
                    "  -i N   wait N seconds between packets\n"
                    "  -t N   set time-to-live (max hops)\n\n"
                    "Example: ping -c 3 google.com    → sends 3 packets to google.com and reports round-trip time"
                ),
                "question": "What command sends ICMP packets to test if a host is reachable?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Basic-Shell-Features",
                "answers": ["ping"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It makes a sound when you think about it.",
                    "It's 4 letters: ping.",
                    "The answer is: ping",
                ],
            },
            {
                "id": "net_2",
                "type": "quiz",
                "title": "Data Retrieval",
                "flavor": "The target's API is wide open. No auth, no rate limit, no logging on the public endpoint. One command to pull what you need from any URL.",
                "lesson": (
                    "curl — transfers data to or from a server using URLs. Supports HTTP, HTTPS, FTP, and more.\n\n"
                    "Syntax: curl [flags] URL\n\n"
                    "Common flags:\n"
                    "  -o file   save output to a file instead of printing it\n"
                    "  -s        silent mode (suppress progress and errors)\n"
                    "  -L        follow HTTP redirects\n"
                    "  -X POST   use a specific HTTP method\n\n"
                    "Example: curl https://example.com    → fetches and prints the HTML of the page"
                ),
                "question": "What command transfers data from/to a URL (supports HTTP, FTP, etc.)?",
                "answers": ["curl"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'Client URL'.",
                    "It's 4 letters starting with 'c'.",
                    "The answer is: curl",
                ],
            },
            {
                "id": "net_3",
                "type": "quiz",
                "title": "Remote Access",
                "flavor": "The data isn't on this machine. It's on the server. Physical access is not an option. You need a terminal on that box — encrypted, authenticated, silent.",
                "lesson": (
                    "ssh — opens an encrypted remote shell session on another machine over the network.\n\n"
                    "Syntax: ssh [flags] user@hostname\n\n"
                    "Common flags:\n"
                    "  -p PORT   connect on a specific port (default is 22)\n"
                    "  -i file   use a specific private key file for authentication\n"
                    "  -L        local port forwarding (tunnel a remote port to your machine)\n\n"
                    "Example: ssh alice@192.168.1.10    → logs in as user 'alice' on that machine"
                ),
                "question": "What command lets you log into a remote machine securely over the network?",
                "answers": ["ssh"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'Secure Shell'.",
                    "It's 3 letters.",
                    "The answer is: ssh",
                ],
            },
            {
                "id": "net_4",
                "type": "flag_quiz",
                "title": "Silent Exfil",
                "flavor": "The progress meter is noise. The error messages are noise. In an automated script, noise kills you. What flag makes curl run clean and quiet?",
                "lesson": (
                    "curl flags — modify how curl behaves when fetching data.\n\n"
                    "Useful flags for scripting:\n"
                    "  -s / --silent    suppress progress meter and error messages\n"
                    "  -o file          write output to a file instead of stdout\n"
                    "  -w format        print custom information after transfer (e.g. HTTP status code)\n"
                    "  -f              fail silently on HTTP errors (non-zero exit code)\n\n"
                    "Example: curl -s https://example.com    → fetches the page with no progress output"
                ),
                "question": "What flag makes curl run silently (suppressing progress and error messages)?",
                "answers": ["-s", "--silent"],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's a single letter flag.",
                    "Think 'silent'.",
                    "The answer is: -s",
                ],
            },
            {
                "id": "net_5",
                "type": "live",
                "title": "Probe the Endpoint",
                "flavor": "You need the HTTP status code — not the response body, just the status. A 200 means the door is open. A 403 means they know you're coming.",
                "lesson": (
                    "curl -o /dev/null -s -w — a pattern used to check HTTP status codes without saving the response body.\n\n"
                    "  -o /dev/null   discard the response body\n"
                    "  -s             silent (no progress output)\n"
                    "  -w '%{http_code}'   print just the HTTP status code after the request\n\n"
                    "Example: curl -o /dev/null -s -w '%{http_code}' http://httpbin.org/status/200\n"
                    "  → prints: 200"
                ),
                "question": (
                    "Use curl to fetch the HTTP status code from http://httpbin.org/status/200.\n"
                    "Use the -o /dev/null -s -w '%{http_code}' flags to get just the status code.\n\n"
                    "Try: curl -o /dev/null -s -w '%{http_code}' http://httpbin.org/status/200"
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "200",
                },
                "xp": 150,
                "difficulty": "hard",
                "hints": [
                    "Use curl with special output flags.",
                    "Try: curl -o /dev/null -s -w '%{http_code}' http://httpbin.org/status/200",
                    "The answer is: curl -o /dev/null -s -w '%{http_code}' http://httpbin.org/status/200",
                ],
            },
            {
                "id": "net_boss",
                "type": "live",
                "title": "BOSS: Identify the Node",
                "flavor": "The client needs to know what machine you're on. Corporate attribution, network segmentation, asset tracking — it all starts with the hostname. Extract it and save it.",
                "lesson": (
                    "hostname — prints the name of the current machine on the network.\n\n"
                    "Syntax: hostname [flags]\n\n"
                    "Common flags:\n"
                    "  -I   show all IP addresses of the machine\n"
                    "  -f   show the fully qualified domain name (FQDN)\n\n"
                    "Combining with redirection saves the result to a file for later use.\n\n"
                    "Example: hostname > host.txt    → writes your machine's hostname into host.txt"
                ),
                "question": "Save your machine's hostname to 'host.txt'.",
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_exists",
                    "target": "host.txt",
                },
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "The 'hostname' command prints your machine's name.",
                    "Redirect its output to a file.",
                    "Try: hostname > host.txt",
                ],
            },
        ],
    },

    "grand_terminal": {
        "id": "grand_terminal",
        "name": "The Black Ice Room",
        "subtitle": "Advanced Shell Mastery",
        "color": "magenta",
        "icon": "💀",
        "commands": ["alias", "history", "env", "export", "awk", "sed"],
        "challenges": [
            {
                "id": "grand_1",
                "type": "quiz",
                "title": "Bind the Shortcut",
                "flavor": "You'll type this command four hundred times before the operation is over. Professionals don't repeat themselves. They make aliases.",
                "lesson": (
                    "alias — creates a shortcut name for a longer command or command with flags.\n\n"
                    "Syntax: alias name='command'\n\n"
                    "Common uses:\n"
                    "  alias ll='ls -la'          shorthand for long listing with hidden files\n"
                    "  alias gs='git status'       shorthand for a common git command\n"
                    "  alias ..='cd ..'            navigate up without typing 'cd'\n\n"
                    "Example: alias ll='ls -la'    → typing 'll' now runs 'ls -la'"
                ),
                "question": "What command creates a shortcut (custom name) for another command?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Aliases",
                "answers": ["alias"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It lets you create a nickname for commands.",
                    "It starts with 'a' and means 'alternative name'.",
                    "The answer is: alias",
                ],
            },
            {
                "id": "grand_2",
                "type": "quiz",
                "title": "Shell Memory",
                "flavor": "What did you run three hours ago? The shell remembers. Every command, every flag, every typo. What retrieves that record?",
                "lesson": (
                    "history — displays a numbered list of previously run commands from the current shell session.\n\n"
                    "Syntax: history [n]\n\n"
                    "Useful tricks:\n"
                    "  history 20       show the last 20 commands\n"
                    "  history | grep ssh    search history for ssh commands\n"
                    "  !!               re-run the last command\n"
                    "  !42              re-run command number 42 from history\n\n"
                    "Example: history    → prints a numbered list of all recent commands"
                ),
                "question": "What command shows your shell's command history?",
                "answers": ["history"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stores everything you've ever typed.",
                    "It's literally called 'history'.",
                    "The answer is: history",
                ],
            },
            {
                "id": "grand_3",
                "type": "live",
                "title": "Enumerate the Environment",
                "flavor": "The shell is soaked in environment variables — credentials, paths, API keys that sloppy devs exported and forgot about. What command dumps them all?",
                "lesson": (
                    "env — prints all environment variables currently set in the shell.\n\n"
                    "Syntax: env\n\n"
                    "Related command: export sets a variable so child processes inherit it.\n"
                    "  export MY_VAR=hello    → MY_VAR is now available to any program you run\n\n"
                    "Key environment variables:\n"
                    "  PATH    directories searched for executable programs\n"
                    "  HOME    your home directory\n"
                    "  USER    your username\n\n"
                    "Example: env | grep PATH    → shows the current PATH variable"
                ),
                "question": "Display all environment variables and pipe to grep to find 'PATH'.",
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "PATH",
                },
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "Use 'env' to list environment variables.",
                    "Pipe to grep: env | grep PATH",
                    "The answer is: env | grep PATH",
                ],
            },
            {
                "id": "grand_4",
                "type": "live",
                "title": "Rewrite the Stream",
                "flavor": "The log file says 'OLD version detected'. You need it to say 'NEW version detected'. You're not opening an editor — the file has 40,000 lines. Use sed.",
                "lesson": (
                    "sed — a stream editor that reads text line by line and applies transformations.\n\n"
                    "Syntax: sed 'command' [file]   or   command | sed 'command'\n\n"
                    "Most common use — substitution:\n"
                    "  sed 's/old/new/'       replace first occurrence per line\n"
                    "  sed 's/old/new/g'      replace all occurrences per line (global)\n"
                    "  sed -i 's/old/new/g' file    edit the file in-place\n\n"
                    "Example: echo 'OLD way' | sed 's/OLD/NEW/'    → prints: NEW way"
                ),
                "question": (
                    "Use sed to replace 'OLD' with 'NEW' in the output of:\n"
                    "echo 'This is the OLD way'\n\n"
                    "Try: echo 'This is the OLD way' | sed 's/OLD/NEW/'"
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "NEW",
                },
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "sed uses the syntax: sed 's/pattern/replacement/'",
                    "Pipe echo output into sed.",
                    "Try: echo 'This is the OLD way' | sed 's/OLD/NEW/'",
                ],
            },
            {
                "id": "grand_5",
                "type": "live",
                "title": "Field Extraction",
                "flavor": "The dump is whitespace-delimited. You need column two of every row. All forty thousand rows. sed won't do this. grep won't do this. awk will do this in one line.",
                "lesson": (
                    "awk — a powerful text processing tool that splits each line into fields and lets you act on them.\n\n"
                    "Syntax: awk '{action}' [file]   or   command | awk '{action}'\n\n"
                    "Fields are split by whitespace by default. Access them with $1, $2, $3...\n"
                    "  $0   the entire line\n"
                    "  $1   first field, $2 second field, etc.\n"
                    "  NF   number of fields on the current line\n\n"
                    "Example: echo 'alpha beta gamma' | awk '{print $2}'    → prints: beta"
                ),
                "question": (
                    "Use awk to print only the second field (word) from:\n"
                    "echo 'alpha beta gamma'\n\n"
                    "Try: echo 'alpha beta gamma' | awk '{print $2}'"
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "output_contains",
                    "expected": "beta",
                },
                "xp": 125,
                "difficulty": "medium",
                "hints": [
                    "awk uses $1, $2, $3... for fields.",
                    "Print the second field with: awk '{print $2}'",
                    "Try: echo 'alpha beta gamma' | awk '{print $2}'",
                ],
            },
            {
                "id": "grand_boss",
                "type": "live",
                "title": "FINAL BOSS: The Black Ice Sequence",
                "flavor": "The corps' final countermeasure activates. A full pipeline — write, transform, output. This is what separates the people who learned the Shell from the people who own it.",
                "lesson": (
                    "Combining tools — the grandmaster wields echo, sed, and redirection together in one pipeline.\n\n"
                    "This challenge chains three steps:\n"
                    "  1. echo writes text into a file using >\n"
                    "  2. sed reads that file and substitutes text\n"
                    "  3. > saves the transformed output to a new file\n\n"
                    "Example:\n"
                    "echo 'GRANDMASTER' > legacy.txt && sed 's/GRANDMASTER/LEGEND/' legacy.txt > legend.txt"
                ),
                "question": (
                    "The Grand Terminal's final trial:\n\n"
                    "Create a file 'legacy.txt' containing the text 'GRANDMASTER',\n"
                    "then use sed to replace 'GRANDMASTER' with 'LEGEND',\n"
                    "and save the result to 'legend.txt'."
                ),
                "setup": {"files": {}, "dirs": []},
                "validation": {
                    "type": "file_contains",
                    "target": "legend.txt",
                    "expected": "LEGEND",
                },
                "xp": 300,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need echo, sed, and file redirection.",
                    "Chain them: echo ... > legacy.txt && sed ... > legend.txt",
                    "Try: echo 'GRANDMASTER' > legacy.txt && sed 's/GRANDMASTER/LEGEND/' legacy.txt > legend.txt",
                ],
            },
        ],
    },

    "environment_chamber": {
        "id": "environment_chamber",
        "name": "The Environment Chamber",
        "subtitle": "Secrets stored in the shell",
        "color": "green",
        "icon": "🔑",
        "commands": ["echo $VAR", "export", "env", "unset", "PATH", "$HOME"],
        "challenges": [
            {
                "id": "env_1",
                "type": "quiz",
                "title": "Read the Signal",
                "flavor": "Every NEXUS Corp process inherits a set of variables when it starts. Credentials, service endpoints, API keys — all sitting in memory. The first step is learning to read them.",
                "lesson": (
                    "Environment variables are named values available to every process in the shell session.\n\n"
                    "Access a variable with the $ prefix:\n"
                    "  echo $HOME        → /home/ghost\n"
                    "  echo $USER        → ghost\n"
                    "  echo $SHELL       → /bin/bash\n\n"
                    "Variable names are case-sensitive. Convention: use ALL_CAPS for environment variables.\n\n"
                    "Example: echo $HOME    → prints the path to your home directory"
                ),
                "question": "What syntax do you use to read the value of an environment variable named HOME?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Environment",
                "answers": ["$HOME", "echo $HOME"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "You prefix the variable name with a special character.",
                    "The character is $.",
                    "The answer is: $HOME",
                ],
            },
            {
                "id": "env_2",
                "type": "quiz",
                "title": "Expose the Environment",
                "flavor": "You need to dump the entire runtime environment of the compromised service. One command prints every environment variable currently set in the shell.",
                "lesson": (
                    "env — prints all environment variables currently set in the shell.\n\n"
                    "Syntax: env\n\n"
                    "Each line is NAME=VALUE. Useful for:\n"
                    "  - Auditing what secrets are loaded in a running process\n"
                    "  - Debugging why a program can't find a dependency\n"
                    "  - Viewing what a containerized service inherited at startup\n\n"
                    "Related commands:\n"
                    "  printenv         → similar to env, can query a single variable\n"
                    "  printenv HOME    → prints only the value of HOME\n\n"
                    "Example: env    → lists all NAME=VALUE pairs"
                ),
                "question": "What command prints all environment variables currently set in the shell?",
                "answers": ["env", "printenv"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a three-letter command.",
                    "Think: environment.",
                    "The answer is: env",
                ],
            },
            {
                "id": "env_3",
                "type": "quiz",
                "title": "Export the Signal",
                "flavor": "You need a variable to persist into child processes — the service you're about to spawn needs to inherit the credential. Setting a variable alone isn't enough.",
                "lesson": (
                    "export — marks a shell variable so it is inherited by child processes.\n\n"
                    "Without export: a variable exists only in the current shell.\n"
                    "With export: the variable is placed in the environment and inherited by any\n"
                    "process started from this shell.\n\n"
                    "Syntax:\n"
                    "  export VAR=value          → define and export in one step\n"
                    "  VAR=value; export VAR     → define first, then export\n\n"
                    "Example:\n"
                    "  export API_KEY=abc123\n"
                    "  → any subprocess you start will see API_KEY=abc123 in its environment"
                ),
                "question": "What command makes a shell variable available to child processes?",
                "answers": ["export"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "You're making the variable available outside the current shell.",
                    "Think: export — send outward.",
                    "The answer is: export",
                ],
            },
            {
                "id": "env_4",
                "type": "quiz",
                "title": "Scrub the Leak",
                "flavor": "The credential is no longer needed. Leaving it in the environment is a liability — any subprocess spawned from this shell could read it. Remove it.",
                "lesson": (
                    "unset — removes a variable from the shell environment entirely.\n\n"
                    "Syntax: unset VARIABLE_NAME\n\n"
                    "Note: do NOT use $ when unsetting a variable. You reference the name, not the value.\n\n"
                    "  unset API_KEY    → removes API_KEY from the environment\n"
                    "  echo $API_KEY    → now prints nothing (empty string)\n\n"
                    "Use unset when:\n"
                    "  - A secret should not outlive the operation that needed it\n"
                    "  - You want to clear a variable that was incorrectly set\n"
                    "  - Cleaning up a shell session before spawning sensitive subprocesses"
                ),
                "question": "What command removes an environment variable from the current shell?",
                "answers": ["unset"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Think: undo the set.",
                    "It's one word.",
                    "The answer is: unset",
                ],
            },
            {
                "id": "env_5",
                "type": "flag_quiz",
                "title": "The Execution Path",
                "flavor": "NEXUS Corp's compromised host has a custom binary in /opt/nexus/bin that the attacker planted. It runs because that directory is on the PATH. You need to understand how PATH works.",
                "lesson": (
                    "PATH — a colon-separated list of directories the shell searches for executables.\n\n"
                    "When you type a command, the shell searches each directory in PATH, left to right,\n"
                    "until it finds a matching executable.\n\n"
                    "  echo $PATH    → /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin\n\n"
                    "To prepend a directory (making it take priority over system paths):\n"
                    "  export PATH=/opt/nexus/bin:$PATH\n\n"
                    "This is how attackers plant backdoors: add their directory first.\n"
                    "  which python3     → shows which binary PATH resolves to\n"
                    "  type python3      → also shows the resolved path"
                ),
                "question": "What environment variable tells the shell where to find executable programs?",
                "answers": ["PATH", "$PATH", "echo $PATH"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's a variable the shell checks every time you run a command.",
                    "It's four capital letters.",
                    "The answer is: PATH",
                ],
            },
            {
                "id": "env_boss",
                "type": "quiz",
                "title": "BOSS: The Credential in the Open",
                "flavor": "Ghost has found it. Buried in the environment of a long-running service process on NEXUS Corp's application server: a database credential stored in plain text as an environment variable. The kind of thing that gets written into systemd service files and forgotten. What variable commonly holds database connection strings or secrets in production systems?",
                "lesson": (
                    "Production systems frequently store secrets in environment variables.\n\n"
                    "Common patterns you'll encounter in real infrastructure:\n"
                    "  DATABASE_URL=postgres://user:password@host:5432/dbname\n"
                    "  SECRET_KEY=...          → Django/Flask signing key\n"
                    "  AWS_ACCESS_KEY_ID=...   → AWS credentials\n"
                    "  API_KEY=...             → third-party API access\n\n"
                    "Auditing a running process's environment:\n"
                    "  cat /proc/<PID>/environ | tr '\\0' '\\n'\n"
                    "    → reads the actual environment of a running process from /proc\n"
                    "    → \\0-delimited, so tr converts to newlines for readability\n\n"
                    "This is a real attack vector. Container breakouts, compromised\n"
                    "systemd units, and supply chain attacks all target env vars.\n"
                    "The audit: run env, read /proc/<PID>/environ, know what's exposed."
                ),
                "question": "What is the common environment variable used to store a database connection string in production services?",
                "answers": ["DATABASE_URL", "DB_URL", "DATABASE_URI"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's a widely adopted convention in web frameworks and 12-factor apps.",
                    "It usually starts with DATABASE.",
                    "The answer is: DATABASE_URL",
                ],
            },
        ],
    },

    "text_processing_forge": {
        "id": "text_processing_forge",
        "name": "The Text Processing Forge",
        "subtitle": "Shape data with cut, sort, uniq, and wc",
        "color": "yellow",
        "icon": "⚙",
        "commands": ["wc", "sort", "uniq", "cut"],
        "challenges": [
            {
                "id": "text_1",
                "type": "quiz",
                "title": "Count the Lines",
                "flavor": "The exfiltrated log file is enormous. Before processing it you need to know exactly how many entries you're dealing with. One command counts lines, words, and bytes.",
                "lesson": (
                    "wc — word count — counts lines, words, and bytes in a file.\n\n"
                    "Syntax: wc [flags] [file]\n\n"
                    "Flags:\n"
                    "  -l   count lines\n"
                    "  -w   count words\n"
                    "  -c   count bytes\n"
                    "  -m   count characters\n\n"
                    "Examples:\n"
                    "  wc -l access.log        → 48302 access.log\n"
                    "  wc -l < access.log      → 48302  (no filename in output)\n"
                    "  cat access.log | wc -l  → 48302  (common in pipelines)"
                ),
                "question": "What flag do you pass to wc to count only lines?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Pipelines",
                "answers": ["-l", "wc -l"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a single-letter flag.",
                    "Think: lines.",
                    "The answer is: -l",
                ],
            },
            {
                "id": "text_2",
                "type": "quiz",
                "title": "Alphabetical Order",
                "flavor": "The intercepted NEXUS Corp user list is a jumbled mess. To deduplicate it you first need to bring order to the chaos. What command sorts lines of text?",
                "lesson": (
                    "sort — sorts lines of text alphabetically (or numerically with -n).\n\n"
                    "Syntax: sort [flags] [file]\n\n"
                    "Flags:\n"
                    "  -r   reverse order (Z→A or largest→smallest)\n"
                    "  -n   numeric sort (treats content as numbers)\n"
                    "  -u   unique: output each distinct value once (combines sort + uniq)\n"
                    "  -k   sort by a specific field (column)\n"
                    "  -t   field delimiter for -k\n\n"
                    "Examples:\n"
                    "  sort users.txt              → alphabetical\n"
                    "  sort -rn response_times.txt → largest numbers first"
                ),
                "question": "What command sorts lines of a text file alphabetically?",
                "answers": ["sort"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The command name matches exactly what it does.",
                    "It's four letters.",
                    "The answer is: sort",
                ],
            },
            {
                "id": "text_3",
                "type": "flag_quiz",
                "title": "Reverse the Sort",
                "flavor": "The NEXUS Corp error log has timestamps at the front of each line. You want the most recent entries first. Sort in reverse.",
                "lesson": (
                    "sort -r — sorts in reverse order.\n\n"
                    "For text: Z before A.\n"
                    "For numbers (with -rn): largest first.\n\n"
                    "Useful patterns:\n"
                    "  sort -r file.txt             → reverse alphabetical\n"
                    "  sort -rn numbers.txt          → largest number first\n"
                    "  sort -t: -k3 -rn /etc/passwd  → sort by UID descending\n\n"
                    "In investigations: sort -r on timestamp-prefixed logs gives you\n"
                    "the most recent entries first, without grep or awk."
                ),
                "question": "What flag reverses the order of sort output?",
                "answers": ["-r", "sort -r"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "One letter.",
                    "Think: reverse.",
                    "The answer is: -r",
                ],
            },
            {
                "id": "text_4",
                "type": "quiz",
                "title": "Filter Duplicates",
                "flavor": "After sorting the user list you can see hundreds of duplicate entries. The monitoring system logged every login, but you only need to know which unique accounts accessed the system.",
                "lesson": (
                    "uniq — filters out adjacent duplicate lines.\n\n"
                    "Critical: uniq only removes ADJACENT duplicates.\n"
                    "You must sort first if you want to deduplicate across the whole file.\n\n"
                    "Syntax: uniq [flags] [file]\n\n"
                    "Flags:\n"
                    "  -c   prefix each line with count of occurrences\n"
                    "  -d   print only duplicate lines (lines that appear more than once)\n"
                    "  -u   print only unique lines (lines that appear exactly once)\n\n"
                    "Classic pipeline:\n"
                    "  sort users.txt | uniq          → deduplicated list\n"
                    "  sort users.txt | uniq -c       → count of each unique entry\n"
                    "  sort users.txt | uniq -c | sort -rn   → most frequent first"
                ),
                "question": "What command filters out adjacent duplicate lines from sorted input?",
                "answers": ["uniq"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It stands for 'unique'.",
                    "It's four letters.",
                    "The answer is: uniq",
                ],
            },
            {
                "id": "text_5",
                "type": "flag_quiz",
                "title": "Extract the Field",
                "flavor": "The /etc/passwd file has user data in colon-separated fields. You need only the first field — the usernames. cut can extract a specific column from delimited text.",
                "lesson": (
                    "cut — extracts specific fields (columns) from each line of text.\n\n"
                    "Syntax: cut [flags] [file]\n\n"
                    "Key flags:\n"
                    "  -d DELIM   set the field delimiter (default is tab)\n"
                    "  -f N       select field number N (1-indexed)\n"
                    "  -c N       select character position N\n\n"
                    "Examples:\n"
                    "  cut -d: -f1 /etc/passwd          → usernames only\n"
                    "  cut -d: -f1,3 /etc/passwd        → username and UID\n"
                    "  cut -d, -f2 report.csv           → second CSV column\n"
                    "  echo 'a:b:c' | cut -d: -f2      → b\n\n"
                    "Real use: extract structured fields from logs, /etc/passwd,\n"
                    "CSV exports, and delimiter-separated config files."
                ),
                "question": "What flag combination extracts the first colon-delimited field using cut?",
                "answers": ["-d: -f1", "-d: -f 1", "cut -d: -f1"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "You need two flags: one sets the delimiter, one selects the field.",
                    "-d sets the delimiter, -f selects the field number.",
                    "The answer is: -d: -f1",
                ],
            },
            {
                "id": "text_boss",
                "type": "quiz",
                "title": "BOSS: Unique Username Extraction",
                "flavor": "Ghost needs to extract a clean list of all unique usernames from /etc/passwd on the compromised NEXUS Corp server. The file uses colons as delimiters. The first field is the username. There will be duplicates in the output after joining multiple /etc/passwd files from different nodes. Build the pipeline.",
                "lesson": (
                    "Combining cut, sort, and uniq — a real production pipeline.\n\n"
                    "Goal: extract unique usernames from /etc/passwd\n\n"
                    "Step-by-step:\n"
                    "  1. cut -d: -f1 /etc/passwd      → get only the first field (username)\n"
                    "  2. | sort                        → bring duplicates adjacent\n"
                    "  3. | uniq                        → remove duplicates\n\n"
                    "Full command:\n"
                    "  cut -d: -f1 /etc/passwd | sort | uniq\n\n"
                    "Variant with count:\n"
                    "  cut -d: -f1 /etc/passwd | sort | uniq -c | sort -rn\n"
                    "  → shows which usernames appear most often (useful for detecting\n"
                    "    merged /etc/passwd files or provisioning anomalies)"
                ),
                "question": "What pipeline extracts unique usernames (first field) from /etc/passwd?",
                "answers": [
                    "cut -d: -f1 /etc/passwd | sort | uniq",
                    "cut -d: -f1 /etc/passwd | sort -u",
                ],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need cut (to extract field 1), sort (to group duplicates), and uniq (to remove them).",
                    "The delimiter is colon and you want field 1.",
                    "The answer is: cut -d: -f1 /etc/passwd | sort | uniq",
                ],
            },
        ],
    },

    "stream_editor_lab": {
        "id": "stream_editor_lab",
        "name": "The Stream Editor Lab",
        "subtitle": "Transform text at scale",
        "color": "magenta",
        "icon": "✦",
        "commands": ["sed", "awk"],
        "challenges": [
            {
                "id": "sed_1",
                "type": "quiz",
                "title": "Global Substitution",
                "flavor": "NEXUS Corp's log files have a hardcoded hostname that was changed six months ago. You need to update ten thousand log entries. sed can replace every occurrence on every line in one pass.",
                "lesson": (
                    "sed 's/old/new/g' — stream editor: substitute 'old' with 'new' globally.\n\n"
                    "Syntax: sed 's/PATTERN/REPLACEMENT/FLAGS' [file]\n\n"
                    "The s command: substitute\n"
                    "  s/old/new/     → replace first occurrence per line\n"
                    "  s/old/new/g    → replace ALL occurrences per line (global)\n"
                    "  s/old/new/i    → case-insensitive match\n"
                    "  s/old/new/2    → replace only the 2nd occurrence per line\n\n"
                    "To edit in-place (modify the file directly):\n"
                    "  sed -i 's/old/new/g' file.txt\n"
                    "  sed -i.bak 's/old/new/g' file.txt   → save backup as file.txt.bak\n\n"
                    "Example: sed 's/ERROR/WARN/g' app.log    → replaces every ERROR with WARN"
                ),
                "question": "What sed command replaces all occurrences of 'ERROR' with 'CRITICAL' in every line?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Pipelines",
                "answers": ["sed 's/ERROR/CRITICAL/g'", "s/ERROR/CRITICAL/g"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The s command does substitution. The g flag makes it global.",
                    "Format: sed 's/FIND/REPLACE/g'",
                    "The answer is: sed 's/ERROR/CRITICAL/g'",
                ],
            },
            {
                "id": "sed_2",
                "type": "flag_quiz",
                "title": "Print Specific Lines",
                "flavor": "The log file is 100,000 lines. You only want to see specific lines — not the whole file. sed with -n suppresses default output and p prints only what you select.",
                "lesson": (
                    "sed -n 'p' — suppress default output and print only selected lines.\n\n"
                    "By default, sed prints every line. -n suppresses this.\n"
                    "Combined with p or a line address, you print only what you want.\n\n"
                    "Address syntax:\n"
                    "  sed -n '5p'         → print line 5 only\n"
                    "  sed -n '5,10p'      → print lines 5 through 10\n"
                    "  sed -n '/ERROR/p'   → print lines matching ERROR (like grep)\n"
                    "  sed -n '$p'         → print the last line\n\n"
                    "Combining with tail/head alternative:\n"
                    "  sed -n '100,200p' large.log   → extracts lines 100-200\n"
                    "  → useful when head/tail's line count isn't precise enough"
                ),
                "question": "What flag suppresses sed's default output so you can print only specific lines?",
                "answers": ["-n", "sed -n"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a single-letter flag.",
                    "Think: no output by default.",
                    "The answer is: -n",
                ],
            },
            {
                "id": "sed_3",
                "type": "quiz",
                "title": "First Column",
                "flavor": "The access log has ten space-separated fields per line. awk can extract individual fields without any pre-sorting or cutting. What command prints only the first field from each line?",
                "lesson": (
                    "awk '{print $1}' — prints the first whitespace-delimited field of each line.\n\n"
                    "awk splits each line into fields by whitespace (default).\n"
                    "Fields are numbered from $1. $0 is the entire line.\n\n"
                    "Syntax: awk 'PROGRAM' [file]\n\n"
                    "Field printing:\n"
                    "  awk '{print $1}'       → first field\n"
                    "  awk '{print $2}'       → second field\n"
                    "  awk '{print $NF}'      → last field (NF = Number of Fields)\n"
                    "  awk '{print $1, $3}'   → first and third field, space-separated\n\n"
                    "Example:\n"
                    "  awk '{print $1}' access.log\n"
                    "  → prints the IP address from each Apache/nginx access log line"
                ),
                "question": "What awk program prints only the first field of each line?",
                "answers": ["awk '{print $1}'", "{print $1}"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Fields in awk are numbered: $1, $2, etc.",
                    "The print statement goes inside single quotes and curly braces.",
                    "The answer is: awk '{print $1}'",
                ],
            },
            {
                "id": "sed_4",
                "type": "quiz",
                "title": "Custom Delimiter",
                "flavor": "The /etc/passwd file is colon-delimited. awk can handle any delimiter with -F. You need to print only usernames (first field) using awk instead of cut.",
                "lesson": (
                    "awk -F: '{print $1}' — sets the field delimiter to colon.\n\n"
                    "The -F flag sets the Field Separator (FS).\n\n"
                    "Syntax: awk -F DELIM 'PROGRAM' [file]\n\n"
                    "Examples:\n"
                    "  awk -F: '{print $1}' /etc/passwd     → usernames\n"
                    "  awk -F: '{print $1,$3}' /etc/passwd  → username and UID\n"
                    "  awk -F, '{print $2}' data.csv        → second CSV column\n"
                    "  awk -F'\\t' '{print $3}' tsv.txt     → third tab-delimited field\n\n"
                    "awk vs cut:\n"
                    "  cut -d: -f1      → fast, simple, exact field extraction\n"
                    "  awk -F: '{print $1}'  → more powerful: conditionals, math, NR, etc."
                ),
                "question": "What awk command prints the first field of /etc/passwd using colon as the delimiter?",
                "answers": [
                    "awk -F: '{print $1}' /etc/passwd",
                    "awk -F: '{print $1}'",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Use -F to set the field separator.",
                    "The field separator is :, the field is $1.",
                    "The answer is: awk -F: '{print $1}' /etc/passwd",
                ],
            },
            {
                "id": "sed_5",
                "type": "quiz",
                "title": "Pattern Filter",
                "flavor": "The NEXUS Corp application log has millions of entries. You need only the lines containing '404'. awk can filter lines by pattern — similar to grep but with the ability to process fields simultaneously.",
                "lesson": (
                    "awk '/pattern/' — prints lines matching a regular expression pattern.\n\n"
                    "Syntax: awk '/REGEX/' [file]\n\n"
                    "This is equivalent to grep 'REGEX' — but you can combine it with\n"
                    "field operations in the same command:\n\n"
                    "  awk '/404/'             → print lines containing 404\n"
                    "  awk '/404/ {print $1}'  → print only the IP from 404 lines\n"
                    "  awk '$9 == 404'         → exact match on field 9 (HTTP status)\n"
                    "  awk '$9 >= 500'         → all server error responses\n\n"
                    "Example:\n"
                    "  awk '/FATAL/ {print $1, $2, $NF}' app.log\n"
                    "  → prints timestamp, date, and last field of every FATAL line"
                ),
                "question": "What awk syntax prints only lines that match a pattern?",
                "answers": ["awk '/pattern/'", "/pattern/"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "The pattern goes between forward slashes.",
                    "No action block needed — the default action is print.",
                    "The answer is: awk '/pattern/'",
                ],
            },
            {
                "id": "sed_boss",
                "type": "quiz",
                "title": "BOSS: Field Extraction from a Log",
                "flavor": "Ghost has a structured application log with pipe-delimited fields. Each line looks like: 2024-01-15|192.168.1.100|ghost_user|GET /api/v2/secrets|200. Ghost needs to extract only the username field (field 3) from every line where the status code (field 5) is 200. Build the awk pipeline.",
                "lesson": (
                    "awk with field separator, pattern match, and field print — combined.\n\n"
                    "Goal: extract field 3 from lines where field 5 equals 200\n\n"
                    "  awk -F'|' '$5 == 200 {print $3}' access.log\n\n"
                    "Breaking it down:\n"
                    "  -F'|'            → pipe-delimited fields\n"
                    "  $5 == 200        → condition: only process lines where field 5 is 200\n"
                    "  {print $3}       → action: print field 3 (username)\n\n"
                    "Adding deduplication:\n"
                    "  awk -F'|' '$5 == 200 {print $3}' access.log | sort | uniq\n\n"
                    "This pattern — delimiter + condition + field extraction — is the\n"
                    "core of real log analysis in production environments."
                ),
                "question": "What awk command extracts the third pipe-delimited field from lines where the fifth field equals 200?",
                "answers": [
                    "awk -F'|' '$5 == 200 {print $3}'",
                    "awk -F'|' '$5==200 {print $3}'",
                ],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Use -F'|' for the pipe delimiter, a condition on $5, and print $3.",
                    "Format: awk -F'|' 'CONDITION {ACTION}'",
                    "The answer is: awk -F'|' '$5 == 200 {print $3}'",
                ],
            },
        ],
    },
    "shell_scripting_basics": {
        "id": "shell_scripting_basics",
        "name": "The Script Foundry",
        "subtitle": "Shell Scripting Basics",
        "color": "magenta",
        "icon": "📜",
        "commands": ["#!/bin/bash", "chmod +x", "./script.sh", "$1", "if", "for"],
        "challenges": [
            {
                "id": "script_1",
                "type": "quiz",
                "title": "The First Line",
                "flavor": "Ghost finds the automation layer — shell scripts running the fraud on a timer, every night at 3 AM. But first: what makes a file a script? The answer is line one.",
                "lesson": (
                    "#!/bin/bash — the shebang line. The first line of every shell script.\n\n"
                    "Syntax: #!/path/to/interpreter\n\n"
                    "The shebang tells the operating system which interpreter should be used\n"
                    "to execute the file. Without it, the shell may guess wrong — or refuse\n"
                    "to run the file at all.\n\n"
                    "Common shebangs:\n"
                    "  #!/bin/bash      → run with bash\n"
                    "  #!/usr/bin/env python3  → run with whatever python3 is in PATH\n"
                    "  #!/bin/sh        → run with the system's POSIX shell\n\n"
                    "Example: The first line of a script that should run as bash:\n"
                    "  #!/bin/bash"
                ),
                "question": "What does the shebang line (#!/bin/bash) tell the operating system?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Scripts",
                "answers": [
                    "what interpreter to use",
                    "which interpreter to use",
                    "the interpreter",
                    "tells the OS what interpreter to use",
                    "it tells the OS which interpreter to use",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's about what runs the script, not what the script does.",
                    "Think: 'use /bin/bash to interpret this file'.",
                    "The answer is: tells the OS what interpreter to use",
                ],
            },
            {
                "id": "script_2",
                "type": "quiz",
                "title": "Make It Executable",
                "flavor": "The fraud script is sitting there. It won't run. The OS won't let it — not until someone gives it the execute bit. Ghost needs to flip that bit.",
                "lesson": (
                    "chmod +x — adds the execute permission to a file.\n\n"
                    "Syntax: chmod +x filename\n\n"
                    "A script file must have the execute bit set before it can be run directly.\n"
                    "Without execute permission, the OS refuses to run it, even if the shebang\n"
                    "is correct.\n\n"
                    "Verification:\n"
                    "  ls -l script.sh\n"
                    "  -rwxr-xr-x  → the 'x' bits confirm it is executable\n\n"
                    "Example: chmod +x fraud_runner.sh\n"
                    "  → allows ./fraud_runner.sh to execute"
                ),
                "question": "What command makes a script file executable?",
                "answers": ["chmod +x script.sh", "chmod +x"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "You need to change the file's mode.",
                    "The flag adds the execute (+x) permission.",
                    "The answer is: chmod +x script.sh",
                ],
            },
            {
                "id": "script_3",
                "type": "quiz",
                "title": "Run It",
                "flavor": "Execute bit is set. The script is ready. How does Ghost run it without putting it on the PATH — directly, from the current directory?",
                "lesson": (
                    "./script.sh — runs a script in the current directory.\n\n"
                    "The ./ prefix means 'in the current directory'.\n\n"
                    "Why ./ is required:\n"
                    "  The shell searches PATH for commands. The current directory is NOT\n"
                    "  in PATH by default (a security measure). Without ./, the shell won't\n"
                    "  find the script even if it's right in front of you.\n\n"
                    "Alternatives:\n"
                    "  bash script.sh        → run with bash explicitly (no execute bit needed)\n"
                    "  /full/path/script.sh  → absolute path works anywhere\n\n"
                    "Example: ./fraud_runner.sh → executes the script in the current directory"
                ),
                "question": "How do you run a script called 'script.sh' in the current directory?",
                "answers": ["./script.sh"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "You need to tell the shell where to find it — the current directory.",
                    "The current directory prefix is: ./",
                    "The answer is: ./script.sh",
                ],
            },
            {
                "id": "script_4",
                "type": "quiz",
                "title": "The First Argument",
                "flavor": "The fraud script takes a target account ID as input — passed as an argument when the cron job calls it. Ghost needs to know: where does that argument live inside the script?",
                "lesson": (
                    "$1 — the first positional argument passed to a script.\n\n"
                    "Positional parameters:\n"
                    "  $0   the script name itself\n"
                    "  $1   the first argument\n"
                    "  $2   the second argument\n"
                    "  $@   all arguments as separate words\n"
                    "  $#   the count of arguments\n\n"
                    "Example:\n"
                    "  # Inside script.sh:\n"
                    "  echo \"Target: $1\"\n\n"
                    "  # Running it:\n"
                    "  ./script.sh account_7731\n"
                    "  → Target: account_7731"
                ),
                "question": "What does $1 refer to in a shell script?",
                "answers": [
                    "the first positional argument passed to the script",
                    "the first argument",
                    "the first positional argument",
                    "first argument passed to the script",
                ],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Positional parameters start at $1.",
                    "Think: what was typed after the script name when it was run.",
                    "The answer is: the first positional argument passed to the script",
                ],
            },
            {
                "id": "script_5",
                "type": "quiz",
                "title": "Conditional Gate",
                "flavor": "The fraud script checks whether the caller is an admin before running the payload. Ghost reads the if statement — and needs to understand what the brackets do.",
                "lesson": (
                    "[ ] — the test command in shell scripts. Evaluates a condition.\n\n"
                    "Syntax: [ condition ]\n\n"
                    "[ ] is equivalent to the 'test' command. It evaluates expressions\n"
                    "and returns an exit status: 0 (true) or non-zero (false).\n\n"
                    "Common tests:\n"
                    "  [ \"$1\" == \"admin\" ]   → string equality\n"
                    "  [ -f file.txt ]      → file exists and is a regular file\n"
                    "  [ -d dir ]           → directory exists\n"
                    "  [ $n -gt 10 ]        → integer greater than\n\n"
                    "Example:\n"
                    "  if [ \"$1\" == \"admin\" ]; then\n"
                    "    echo \"welcome\"\n"
                    "  fi"
                ),
                "question": "In a bash if statement, what does [ ] do?",
                "answers": [
                    "test/evaluate a condition",
                    "evaluates a condition",
                    "tests a condition",
                    "evaluate a condition",
                    "it tests or evaluates a condition",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's not just brackets — it's the 'test' command.",
                    "It checks whether something is true or false.",
                    "The answer is: test/evaluate a condition",
                ],
            },
            {
                "id": "script_boss",
                "type": "quiz",
                "title": "BOSS: Loop the Evidence",
                "flavor": "The fraud script processed every log file in the directory — rotating through each one in a loop. Ghost reconstructs the logic: a for loop, a glob pattern, an echo. What does this loop do?",
                "lesson": (
                    "for loop — iterates over a list of items.\n\n"
                    "Syntax:\n"
                    "  for VARIABLE in LIST; do\n"
                    "    COMMANDS\n"
                    "  done\n\n"
                    "Glob expansion in loops:\n"
                    "  for f in *.log; do echo \"$f\"; done\n"
                    "  → expands *.log to all matching filenames, then loops over each one\n\n"
                    "The loop variable $f holds the current item in each iteration.\n\n"
                    "Example:\n"
                    "  for f in *.log; do echo \"$f\"; done\n"
                    "  → prints each .log filename in the current directory, one per line"
                ),
                "question": "What does: for f in *.log; do echo \"$f\"; done  — print?",
                "answers": [
                    "the name of each .log file in the current directory",
                    "each .log filename",
                    "every .log file name",
                    "the names of all .log files",
                    "all log file names",
                ],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "The glob *.log matches all files ending in .log.",
                    "The loop variable $f holds each filename in turn.",
                    "The answer is: the name of each .log file in the current directory",
                ],
            },
        ],
    },

    "job_control": {
        "id": "job_control",
        "name": "The Job Control Station",
        "subtitle": "Foreground & Background Jobs",
        "color": "yellow",
        "icon": "⚙️",
        "commands": ["Ctrl+Z", "bg", "fg", "jobs", "nohup"],
        "challenges": [
            {
                "id": "job_1",
                "type": "quiz",
                "title": "Suspend the Process",
                "flavor": "Multiple NEXUS processes are masking the fraud trail — running loud in the foreground, covering the signal. Ghost needs to pause one without killing it. The keystroke is simple. The effect is immediate.",
                "lesson": (
                    "Ctrl+Z — suspends (pauses) the currently running foreground process.\n\n"
                    "The process is not killed — it is stopped and moved to the background\n"
                    "in a suspended state. The shell regains control of the terminal.\n\n"
                    "What happens after Ctrl+Z:\n"
                    "  - The process stops executing\n"
                    "  - The shell prints: [1]+  Stopped    command_name\n"
                    "  - The job is assigned a job number (e.g. [1])\n"
                    "  - You can resume it with fg or bg\n\n"
                    "Example:\n"
                    "  $ sleep 9999\n"
                    "  ^Z\n"
                    "  [1]+  Stopped    sleep 9999"
                ),
                "question": "What does Ctrl+Z do to the currently running foreground process?",
                "url": "https://www.gnu.org/software/bash/manual/bash.html#Job-Control",
                "answers": [
                    "pauses/suspends the current foreground process",
                    "suspends the current foreground process",
                    "pauses the foreground process",
                    "suspends it",
                    "pauses the process",
                    "it suspends the current foreground process",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It doesn't kill the process — it pauses it.",
                    "Think: suspend, not terminate.",
                    "The answer is: pauses/suspends the current foreground process",
                ],
            },
            {
                "id": "job_2",
                "type": "quiz",
                "title": "Push It Back",
                "flavor": "The NEXUS process is suspended. Ghost needs it running again — but quietly, in the background, so the terminal stays free for the real work.",
                "lesson": (
                    "bg — resumes a suspended job and runs it in the background.\n\n"
                    "Syntax: bg [%job_number]\n\n"
                    "After Ctrl+Z suspends a process:\n"
                    "  bg        → resume the most recently suspended job in background\n"
                    "  bg %1     → resume job number 1 in the background\n\n"
                    "The process keeps running but no longer controls the terminal.\n"
                    "Its output may still appear on screen unless you redirect it.\n\n"
                    "Example:\n"
                    "  ^Z             → suspend the foreground job\n"
                    "  bg             → send it to the background\n"
                    "  [1]+ sleep 9999 &   → confirmation it's running in background"
                ),
                "question": "After suspending a job with Ctrl+Z, what command resumes it in the background?",
                "answers": ["bg"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Think: background.",
                    "Two letters: b-g.",
                    "The answer is: bg",
                ],
            },
            {
                "id": "job_3",
                "type": "quiz",
                "title": "Pull It Forward",
                "flavor": "The process is running in the background. Ghost needs to interact with it directly — bring it forward, take control. One command moves it back to the foreground.",
                "lesson": (
                    "fg — brings a background or suspended job to the foreground.\n\n"
                    "Syntax: fg [%job_number]\n\n"
                    "  fg        → bring the most recent background job to the foreground\n"
                    "  fg %1     → bring job 1 to the foreground\n"
                    "  fg %2     → bring job 2 to the foreground\n\n"
                    "Once in the foreground, the job controls the terminal again.\n"
                    "Ctrl+C will terminate it; Ctrl+Z will suspend it again.\n\n"
                    "Example:\n"
                    "  $ jobs\n"
                    "  [1]- Running    long_scan.sh &\n"
                    "  [2]+ Stopped    tail -f server.log\n"
                    "  $ fg %2\n"
                    "  → tail -f server.log resumes in the foreground"
                ),
                "question": "What command brings a background job back to the foreground?",
                "answers": ["fg"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Think: foreground.",
                    "Two letters: f-g.",
                    "The answer is: fg",
                ],
            },
            {
                "id": "job_4",
                "type": "quiz",
                "title": "Enumerate the Jobs",
                "flavor": "Ghost has been juggling multiple background processes. Which NEXUS daemons are running? Which are suspended? One command shows the full job list for this shell session.",
                "lesson": (
                    "jobs — lists all background and suspended jobs in the current shell.\n\n"
                    "Syntax: jobs [flags]\n\n"
                    "Output format:\n"
                    "  [1]- Running    scan.sh &\n"
                    "  [2]+ Stopped    tail -f audit.log\n\n"
                    "  [N]  → job number\n"
                    "  +    → most recent job (default for fg/bg)\n"
                    "  -    → second most recent job\n"
                    "  Status → Running, Stopped, Done, Killed\n\n"
                    "Common flags:\n"
                    "  -l   include PIDs in the output\n"
                    "  -p   print PIDs only\n\n"
                    "Note: jobs only shows jobs for the CURRENT shell session.\n"
                    "Processes started in other shells won't appear here."
                ),
                "question": "What does the 'jobs' command show?",
                "answers": [
                    "all suspended and background jobs in current shell",
                    "all background and suspended jobs in the current shell",
                    "suspended and background jobs",
                    "background jobs",
                    "all jobs in the current shell",
                ],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It's scoped to the current shell session.",
                    "Think: list all current shell jobs.",
                    "The answer is: all suspended and background jobs in current shell",
                ],
            },
            {
                "id": "job_boss",
                "type": "quiz",
                "title": "BOSS: The Unkillable Process",
                "flavor": "Ghost needs the fraud audit script to keep running after logout — surviving the session end, immune to the hangup signal the system will send when the connection drops. The command is one line.",
                "lesson": (
                    "nohup — runs a command immune to the SIGHUP (hangup) signal.\n\n"
                    "Syntax: nohup command [args] &\n\n"
                    "When a terminal session ends, the OS sends SIGHUP to all processes\n"
                    "attached to it. This normally kills them. nohup intercepts SIGHUP\n"
                    "and ignores it, keeping the process alive after logout.\n\n"
                    "The & at the end sends it to the background immediately.\n\n"
                    "Output:\n"
                    "  nohup redirects stdout/stderr to nohup.out by default\n"
                    "  (if stdout is not already redirected)\n\n"
                    "Example:\n"
                    "  nohup long_command.sh &\n"
                    "  → starts long_command.sh, immune to hangup, running in background\n"
                    "  → output written to nohup.out"
                ),
                "question": "What does nohup do when you run: nohup long_command.sh &",
                "answers": [
                    "lets the process keep running after you log out",
                    "keeps the process running after logout",
                    "the process keeps running after logout",
                    "runs it immune to hangup so it survives logout",
                    "keeps running after you log out",
                ],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "nohup stands for 'no hangup'.",
                    "When the terminal closes, what signal does the OS send — and what does nohup do with it?",
                    "The answer is: lets the process keep running after you log out",
                ],
            },
        ],
    },

}

ZONE_ORDER = [
    "antechamber",
    "archive_vaults",
    "oracle_library",
    "pipe_sanctum",
    "process_catacombs",
    "permissions_fortress",
    "scripting_citadel",
    "network_nexus",
    "grand_terminal",
    "environment_chamber",
    "text_processing_forge",
    "stream_editor_lab",
    "process_control",
    "network_recon",
    "shell_scripting_basics",
    "job_control",
]


def get_zone(zone_id: str) -> dict:
    return ZONES.get(zone_id, {})


def get_all_zones() -> list:
    return [ZONES[z] for z in ZONE_ORDER if z in ZONES]


def get_zone_challenges(zone_id: str) -> list:
    zone = get_zone(zone_id)
    return zone.get("challenges", [])


def get_challenge(zone_id: str, challenge_id: str) -> dict:
    for ch in get_zone_challenges(zone_id):
        if ch["id"] == challenge_id:
            return ch
    return {}


def zone_total_xp(zone_id: str) -> int:
    return sum(ch.get("xp", 0) for ch in get_zone_challenges(zone_id))
