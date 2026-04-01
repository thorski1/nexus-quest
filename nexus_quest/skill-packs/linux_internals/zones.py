"""
zones.py - All zone and challenge data for Kernel Ops (linux_internals pack)
Challenge types: quiz (multiple choice, a/b/c/d)
8 zones, ~45 challenges total covering Linux kernel and system internals.
"""

ZONES = {
    # ── ZONE 1: PROCESS MANAGEMENT ──────────────────────────────────────
    "process_management": {
        "id": "process_management",
        "name": "The Process Table",
        "subtitle": "Processes, Threads, Signals & Scheduling",
        "color": "cyan",
        "icon": "⚙",
        "commands": ["fork", "exec", "kill", "ps", "nice", "renice", "wait"],
        "challenges": [
            {
                "id": "proc_1",
                "type": "quiz",
                "title": "Birth of a Process",
                "question": "When a Linux process calls fork(), what is created?",
                "lesson": (
                    "fork() creates a new child process that is an almost-exact copy of the parent.\n\n"
                    "The child gets its own PID but inherits the parent's memory space via\n"
                    "copy-on-write (COW). Both processes continue executing from the instruction\n"
                    "after the fork() call. fork() returns 0 to the child and the child's PID\n"
                    "to the parent."
                ),
                "options": [
                    "a) A new thread sharing the parent's PID",
                    "b) A child process with a new PID and copy-on-write memory",
                    "c) A container namespace isolated from the parent",
                    "d) A symbolic link to the parent process",
                ],
                "answer": "b",
                "hints": [
                    "fork() is the fundamental process creation syscall — it duplicates the calling process.",
                    "The child gets its own PID but initially shares memory pages via copy-on-write.",
                ],
                "xp": 25,
            },
            {
                "id": "proc_2",
                "type": "quiz",
                "title": "The Exec Replacement",
                "question": "What does the exec() family of system calls do to the calling process?",
                "lesson": (
                    "exec() replaces the current process image with a new program.\n\n"
                    "The PID stays the same, but the code, data, heap, and stack are replaced\n"
                    "by the new executable. Open file descriptors are preserved unless marked\n"
                    "close-on-exec. The fork-exec pattern is how every new program starts in Unix."
                ),
                "options": [
                    "a) Creates a new child process running the specified program",
                    "b) Pauses the current process and queues the new program",
                    "c) Replaces the current process image with a new program, same PID",
                    "d) Spawns a background daemon from the current process",
                ],
                "answer": "c",
                "hints": [
                    "exec does not create a new process — it transforms the existing one.",
                    "The PID remains the same, but everything else about the process changes.",
                ],
                "xp": 25,
            },
            {
                "id": "proc_3",
                "type": "quiz",
                "title": "The Walking Dead",
                "question": "What is a zombie process in Linux?",
                "lesson": (
                    "A zombie (defunct) process has finished execution but still has an entry\n"
                    "in the process table because its parent hasn't called wait() to read its\n"
                    "exit status.\n\n"
                    "Zombies consume no CPU or memory but occupy a PID slot. Too many zombies\n"
                    "can exhaust the PID space. The fix: the parent must call wait()/waitpid(),\n"
                    "or be killed so init (PID 1) adopts and reaps the zombies."
                ),
                "options": [
                    "a) A process that is stuck in an infinite loop consuming CPU",
                    "b) A process that has exited but whose parent hasn't read its exit status",
                    "c) A process that lost its network connection and is waiting to reconnect",
                    "d) A daemon process running without a controlling terminal",
                ],
                "answer": "b",
                "hints": [
                    "The process has already terminated — it's 'dead' — but it lingers in the process table.",
                    "The parent needs to call wait() to collect the exit status and release the PID.",
                ],
                "xp": 30,
            },
            {
                "id": "proc_4",
                "type": "quiz",
                "title": "Signal Interrupt",
                "question": "Which signal is sent by default when you run 'kill <PID>' without specifying a signal?",
                "lesson": (
                    "kill without a signal number sends SIGTERM (signal 15) by default.\n\n"
                    "SIGTERM asks the process to terminate gracefully — the process can catch\n"
                    "and handle it (e.g., close files, flush buffers). SIGKILL (signal 9) cannot\n"
                    "be caught or ignored; the kernel terminates the process immediately.\n\n"
                    "Common signals: SIGHUP (1), SIGINT (2), SIGQUIT (3), SIGKILL (9),\n"
                    "SIGTERM (15), SIGSTOP (19), SIGCONT (18)."
                ),
                "options": [
                    "a) SIGKILL (9)",
                    "b) SIGINT (2)",
                    "c) SIGTERM (15)",
                    "d) SIGHUP (1)",
                ],
                "answer": "c",
                "hints": [
                    "The default signal is the polite one — it asks the process to shut down gracefully.",
                    "SIGKILL is the forced kill; the default is the gentler termination signal.",
                ],
                "xp": 25,
            },
            {
                "id": "proc_5",
                "type": "quiz",
                "title": "Priority Adjustment",
                "question": "What does the 'nice' value of a process control in Linux?",
                "lesson": (
                    "The nice value controls a process's CPU scheduling priority.\n\n"
                    "Range: -20 (highest priority) to +19 (lowest priority). Default is 0.\n"
                    "Only root can set negative nice values (higher priority). Regular users\n"
                    "can only increase their nice value (lower their priority).\n\n"
                    "  nice -n 10 ./script.sh   — start with nice value 10\n"
                    "  renice -n 5 -p 1234      — change running process 1234 to nice 5"
                ),
                "options": [
                    "a) The amount of RAM the process is allowed to allocate",
                    "b) The CPU scheduling priority of the process",
                    "c) The maximum number of file descriptors the process can open",
                    "d) The I/O bandwidth limit for the process",
                ],
                "answer": "b",
                "hints": [
                    "A 'nicer' process yields CPU time to others — it's about scheduling priority.",
                    "Nice values range from -20 (highest priority) to +19 (lowest priority).",
                ],
                "xp": 25,
            },
            {
                "id": "proc_6",
                "type": "quiz",
                "title": "Thread vs Process",
                "question": "What is the fundamental difference between threads and processes in the Linux kernel?",
                "lesson": (
                    "In Linux, threads are implemented as lightweight processes (tasks) that\n"
                    "share the same memory address space, file descriptors, and signal handlers.\n\n"
                    "The kernel uses clone() with specific flags to create threads. Both threads\n"
                    "and processes are 'tasks' in the kernel's scheduler — the difference is\n"
                    "which resources they share. Threads share: memory, FDs, PID (via TGID).\n"
                    "Each thread has its own: stack, registers, TID (thread ID)."
                ),
                "options": [
                    "a) Threads run in kernel space while processes run in user space",
                    "b) Threads share memory address space and file descriptors; processes do not",
                    "c) Threads cannot be scheduled independently; processes can",
                    "d) Threads are always higher priority than processes",
                ],
                "answer": "b",
                "hints": [
                    "Both are 'tasks' to the scheduler — the difference is resource sharing.",
                    "Threads share the same virtual address space; processes each get their own.",
                ],
                "xp": 30,
            },
        ],
    },
    # ── ZONE 2: MEMORY MANAGEMENT ───────────────────────────────────────
    "memory_management": {
        "id": "memory_management",
        "name": "The Memory Grid",
        "subtitle": "Virtual Memory, Pages, Swap & OOM",
        "color": "magenta",
        "icon": "🧠",
        "commands": ["free", "vmstat", "swapon", "cgroups", "/proc/meminfo"],
        "challenges": [
            {
                "id": "mem_1",
                "type": "quiz",
                "title": "Virtual Address Space",
                "question": "Why does every Linux process see its own contiguous virtual address space?",
                "lesson": (
                    "Virtual memory provides each process with the illusion of a large,\n"
                    "contiguous, private address space. The MMU (Memory Management Unit)\n"
                    "translates virtual addresses to physical addresses using page tables.\n\n"
                    "Benefits: process isolation (one process can't access another's memory),\n"
                    "simplified memory allocation, and the ability to use more memory than\n"
                    "physically available (via swapping and demand paging)."
                ),
                "options": [
                    "a) The kernel copies all physical RAM into each process's space at startup",
                    "b) The MMU translates virtual addresses to physical addresses via page tables",
                    "c) Each process runs on a dedicated CPU core with its own RAM bank",
                    "d) The filesystem provides memory-mapped regions for each process",
                ],
                "answer": "b",
                "hints": [
                    "Hardware assists the kernel — a specific unit on the CPU handles address translation.",
                    "Page tables are the data structure that maps virtual pages to physical frames.",
                ],
                "xp": 30,
            },
            {
                "id": "mem_2",
                "type": "quiz",
                "title": "Page Fault",
                "question": "What happens when a process accesses a virtual page that is not currently in physical RAM?",
                "lesson": (
                    "A page fault occurs. The MMU signals the kernel, which then:\n\n"
                    "1. Checks if the access is valid (segfault if not)\n"
                    "2. Finds a free physical frame (or evicts one)\n"
                    "3. Loads the page from disk (swap or file) into the frame\n"
                    "4. Updates the page table entry\n"
                    "5. Restarts the faulting instruction\n\n"
                    "Minor faults (page already in memory, just not mapped) are fast.\n"
                    "Major faults (page must be read from disk) are slow."
                ),
                "options": [
                    "a) The process is immediately terminated with SIGSEGV",
                    "b) The kernel allocates more physical RAM and the process continues",
                    "c) A page fault occurs and the kernel loads the page from disk or cache",
                    "d) The process blocks until another process frees enough memory",
                ],
                "answer": "c",
                "hints": [
                    "A page fault is not necessarily an error — it's the normal mechanism for demand paging.",
                    "The kernel's page fault handler decides whether to load the page or signal a segfault.",
                ],
                "xp": 30,
            },
            {
                "id": "mem_3",
                "type": "quiz",
                "title": "Swap Space",
                "question": "What is the primary purpose of swap space in Linux?",
                "lesson": (
                    "Swap extends available memory by using disk as overflow when physical\n"
                    "RAM is full. The kernel moves (swaps out) infrequently-used pages to\n"
                    "swap and brings them back (swaps in) on demand.\n\n"
                    "  swapon -s          — show active swap devices\n"
                    "  free -h            — show RAM and swap usage\n"
                    "  /proc/swaps        — kernel's swap information\n"
                    "  vm.swappiness      — tunable (0-200) controlling swap aggressiveness\n\n"
                    "Swap is much slower than RAM. Heavy swapping (thrashing) kills performance."
                ),
                "options": [
                    "a) To store kernel modules that are not currently loaded",
                    "b) To provide overflow memory by moving inactive pages to disk",
                    "c) To cache filesystem metadata for faster disk access",
                    "d) To hold temporary files created by running applications",
                ],
                "answer": "b",
                "hints": [
                    "When RAM fills up, the kernel needs somewhere to put pages that aren't being used.",
                    "Swap uses disk as an extension of memory — much slower, but prevents OOM.",
                ],
                "xp": 25,
            },
            {
                "id": "mem_4",
                "type": "quiz",
                "title": "OOM Killer",
                "question": "How does the Linux OOM killer decide which process to terminate?",
                "lesson": (
                    "The Out-of-Memory killer activates when the system cannot free enough\n"
                    "memory. It assigns each process an oom_score based on:\n\n"
                    "  - Memory consumption (higher = more likely to be killed)\n"
                    "  - Process age (newer processes score higher)\n"
                    "  - oom_score_adj (-1000 to +1000, set per-process)\n\n"
                    "  /proc/<pid>/oom_score     — current score\n"
                    "  /proc/<pid>/oom_score_adj — manual adjustment\n"
                    "  oom_score_adj = -1000      — process is exempt from OOM killer\n\n"
                    "dmesg | grep -i oom — check if OOM killer fired recently."
                ),
                "options": [
                    "a) It kills the process with the highest PID number",
                    "b) It kills the oldest process on the system",
                    "c) It selects the process with the highest oom_score based on memory usage and adjustments",
                    "d) It randomly selects a user-space process to terminate",
                ],
                "answer": "c",
                "hints": [
                    "The kernel calculates a score for each process — memory hogs score higher.",
                    "Check /proc/<pid>/oom_score to see a process's current OOM score.",
                ],
                "xp": 35,
            },
            {
                "id": "mem_5",
                "type": "quiz",
                "title": "Cgroups Memory Limits",
                "question": "What happens when a process in a cgroup exceeds its memory.max limit?",
                "lesson": (
                    "cgroups v2 memory controller enforces hard limits via memory.max.\n\n"
                    "When a cgroup hits memory.max:\n"
                    "  1. The kernel tries to reclaim memory within the cgroup\n"
                    "  2. If reclaim fails, the cgroup's OOM killer fires\n"
                    "  3. A process within that cgroup is killed (not system-wide OOM)\n\n"
                    "  memory.max      — hard limit (triggers OOM within cgroup)\n"
                    "  memory.high     — soft limit (triggers throttling/reclaim)\n"
                    "  memory.current  — current usage\n"
                    "  memory.swap.max — swap limit for the cgroup"
                ),
                "options": [
                    "a) The kernel expands the cgroup limit automatically",
                    "b) The system-wide OOM killer terminates the largest process on the host",
                    "c) The cgroup's OOM killer fires, killing a process within that cgroup",
                    "d) The process is paused until memory becomes available",
                ],
                "answer": "c",
                "hints": [
                    "cgroups provide isolation — the OOM response is scoped to the cgroup, not the whole system.",
                    "memory.max is a hard ceiling; exceeding it triggers the cgroup-local OOM killer.",
                ],
                "xp": 35,
            },
            {
                "id": "mem_6",
                "type": "quiz",
                "title": "Copy on Write",
                "question": "How does copy-on-write (COW) optimize memory after fork()?",
                "lesson": (
                    "After fork(), parent and child share the same physical pages — marked\n"
                    "read-only. When either process writes to a page, the kernel traps the\n"
                    "write (page fault), copies the page, and gives each process its own copy.\n\n"
                    "This avoids copying the entire address space at fork time. Most pages\n"
                    "are never written and remain shared. Combined with exec() (which replaces\n"
                    "the address space entirely), fork+exec is extremely efficient."
                ),
                "options": [
                    "a) Both processes get independent copies of all memory pages immediately",
                    "b) Pages are shared read-only; a private copy is made only when a write occurs",
                    "c) The child process uses swap space instead of physical RAM",
                    "d) The kernel compresses duplicate pages to save memory",
                ],
                "answer": "b",
                "hints": [
                    "The 'copy' only happens 'on write' — if no writes occur, pages remain shared.",
                    "Pages are marked read-only; a write triggers a fault, which triggers the copy.",
                ],
                "xp": 30,
            },
        ],
    },
    # ── ZONE 3: FILESYSTEM INTERNALS ────────────────────────────────────
    "filesystem_internals": {
        "id": "filesystem_internals",
        "name": "The Inode Vault",
        "subtitle": "Inodes, Filesystems, /proc, /sys & File Descriptors",
        "color": "green",
        "icon": "📁",
        "commands": ["stat", "ls -i", "df", "mount", "lsof", "cat /proc"],
        "challenges": [
            {
                "id": "fs_1",
                "type": "quiz",
                "title": "The Inode",
                "question": "What does an inode store in a Linux filesystem?",
                "lesson": (
                    "An inode stores all metadata about a file EXCEPT its name:\n\n"
                    "  - File type (regular, directory, symlink, socket, etc.)\n"
                    "  - Permissions and ownership (UID, GID)\n"
                    "  - Timestamps (atime, mtime, ctime)\n"
                    "  - Size and block count\n"
                    "  - Pointers to data blocks on disk\n\n"
                    "The filename is stored in the directory entry, which maps names to\n"
                    "inode numbers. This is why hard links work — multiple names can point\n"
                    "to the same inode.\n\n"
                    "  stat <file>   — display inode metadata\n"
                    "  ls -i         — show inode numbers"
                ),
                "options": [
                    "a) The file's name, content, and permissions",
                    "b) Only the file's content data blocks",
                    "c) File metadata (permissions, size, timestamps, block pointers) but not the filename",
                    "d) A compressed copy of the file for backup purposes",
                ],
                "answer": "c",
                "hints": [
                    "The filename lives in the directory entry, not the inode itself.",
                    "An inode holds everything about a file except its name — that's why hard links work.",
                ],
                "xp": 25,
            },
            {
                "id": "fs_2",
                "type": "quiz",
                "title": "Filesystem Wars",
                "question": "Which Linux filesystem supports transparent compression, snapshots, and checksumming natively?",
                "lesson": (
                    "btrfs (B-tree filesystem) is a copy-on-write filesystem with:\n\n"
                    "  - Transparent compression (zstd, lzo, zlib)\n"
                    "  - Subvolumes and snapshots (instant, zero-cost at creation)\n"
                    "  - Data and metadata checksumming (CRC32c, xxhash, SHA256)\n"
                    "  - RAID support (RAID 0, 1, 10)\n"
                    "  - Online defragmentation and resizing\n\n"
                    "ext4: mature, stable, no checksumming or snapshots.\n"
                    "XFS: excellent for large files, no native compression.\n"
                    "btrfs: feature-rich, evolving, used by default in some distros."
                ),
                "options": [
                    "a) ext4",
                    "b) XFS",
                    "c) btrfs",
                    "d) FAT32",
                ],
                "answer": "c",
                "hints": [
                    "ext4 and XFS are reliable but lack built-in compression and snapshots.",
                    "This filesystem's name starts with 'b' and is based on B-tree data structures.",
                ],
                "xp": 25,
            },
            {
                "id": "fs_3",
                "type": "quiz",
                "title": "The /proc Illusion",
                "question": "What is /proc in Linux?",
                "lesson": (
                    "/proc is a virtual (pseudo) filesystem that provides an interface to\n"
                    "kernel data structures. Nothing in /proc exists on disk.\n\n"
                    "  /proc/<pid>/status  — process state, memory, threads\n"
                    "  /proc/<pid>/fd/     — open file descriptors\n"
                    "  /proc/<pid>/maps    — virtual memory mappings\n"
                    "  /proc/cpuinfo       — CPU information\n"
                    "  /proc/meminfo       — memory statistics\n"
                    "  /proc/loadavg       — system load averages\n\n"
                    "Reading /proc files triggers kernel functions that generate the content\n"
                    "on the fly. Writing to certain /proc files changes kernel parameters."
                ),
                "options": [
                    "a) A directory containing backup copies of system configuration files",
                    "b) A virtual filesystem exposing kernel and process information in real time",
                    "c) A log directory where processes write their output",
                    "d) A temporary filesystem for storing process core dumps",
                ],
                "answer": "b",
                "hints": [
                    "/proc contains no actual files on disk — the content is generated by the kernel.",
                    "Each running process gets its own subdirectory under /proc/<PID>/.",
                ],
                "xp": 25,
            },
            {
                "id": "fs_4",
                "type": "quiz",
                "title": "File Descriptors",
                "question": "In Linux, what are file descriptors 0, 1, and 2 by convention?",
                "lesson": (
                    "Every process inherits three open file descriptors:\n\n"
                    "  0 — stdin  (standard input)\n"
                    "  1 — stdout (standard output)\n"
                    "  2 — stderr (standard error)\n\n"
                    "File descriptors are non-negative integers indexing into the process's\n"
                    "file descriptor table. Each entry points to a kernel file description\n"
                    "(struct file) which tracks the open file, offset, and mode.\n\n"
                    "  ls -la /proc/$$/fd   — list FDs for the current shell\n"
                    "  lsof -p <pid>        — list open files for a process\n"
                    "  ulimit -n            — show the FD limit for the shell"
                ),
                "options": [
                    "a) stdin, stdout, stderr",
                    "b) read, write, execute",
                    "c) root, user, group",
                    "d) input, output, log",
                ],
                "answer": "a",
                "hints": [
                    "These three are inherited by every new process from its parent.",
                    "FD 0 is for input, FD 1 is for normal output, FD 2 is for error output.",
                ],
                "xp": 25,
            },
            {
                "id": "fs_5",
                "type": "quiz",
                "title": "Mount Namespaces",
                "question": "What does the 'mount' command without arguments display?",
                "lesson": (
                    "mount (no arguments) lists all currently mounted filesystems, including:\n\n"
                    "  - Device or virtual source\n"
                    "  - Mount point (directory)\n"
                    "  - Filesystem type\n"
                    "  - Mount options (ro, rw, noexec, nosuid, etc.)\n\n"
                    "  mount                     — list all mounts\n"
                    "  mount -t ext4             — list only ext4 mounts\n"
                    "  findmnt                   — tree view of mount hierarchy\n"
                    "  /proc/mounts              — kernel's view of mounts\n"
                    "  /etc/fstab                — persistent mount configuration"
                ),
                "options": [
                    "a) The contents of /etc/fstab",
                    "b) All currently mounted filesystems with their types and options",
                    "c) Only network-attached storage mounts",
                    "d) The disk partitions and their UUIDs",
                ],
                "answer": "b",
                "hints": [
                    "Running mount with no arguments is a quick way to see what's mounted where.",
                    "The output includes device, mount point, filesystem type, and mount options.",
                ],
                "xp": 25,
            },
        ],
    },
    # ── ZONE 4: NETWORKING STACK ────────────────────────────────────────
    "networking_stack": {
        "id": "networking_stack",
        "name": "The Socket Layer",
        "subtitle": "Sockets, TCP States, Netfilter & Namespaces",
        "color": "blue",
        "icon": "🔌",
        "commands": ["ss", "iptables", "ip", "netstat", "tcpdump", "ip netns"],
        "challenges": [
            {
                "id": "net_1",
                "type": "quiz",
                "title": "Socket Fundamentals",
                "question": "What three pieces of information define a TCP socket endpoint?",
                "lesson": (
                    "A TCP socket endpoint is defined by: IP address + port number + protocol.\n\n"
                    "A TCP connection (socket pair) is uniquely identified by the 4-tuple:\n"
                    "  (source IP, source port, destination IP, destination port)\n\n"
                    "This is why a single server port (e.g., 80) can handle thousands of\n"
                    "simultaneous connections — each client uses a different source IP:port.\n\n"
                    "  ss -tlnp     — show listening TCP sockets with process info\n"
                    "  ss -tanp     — show all TCP connections with state"
                ),
                "options": [
                    "a) Hostname, MAC address, and port",
                    "b) IP address, port number, and protocol",
                    "c) PID, file descriptor, and socket type",
                    "d) Network interface, VLAN ID, and subnet mask",
                ],
                "answer": "b",
                "hints": [
                    "A socket endpoint needs to identify the machine, the service, and the transport layer.",
                    "Think: where (IP), which service (port), and how (TCP vs UDP).",
                ],
                "xp": 25,
            },
            {
                "id": "net_2",
                "type": "quiz",
                "title": "TCP State Machine",
                "question": "Which TCP state indicates that a connection has been closed locally but the remote side hasn't acknowledged the closure yet?",
                "lesson": (
                    "TCP connection states (simplified lifecycle):\n\n"
                    "  LISTEN      — waiting for incoming connections\n"
                    "  SYN_SENT    — connection request sent, awaiting ACK\n"
                    "  ESTABLISHED — connection is active\n"
                    "  FIN_WAIT_1  — local side sent FIN, waiting for ACK\n"
                    "  FIN_WAIT_2  — local FIN acknowledged, waiting for remote FIN\n"
                    "  TIME_WAIT   — waiting for stale packets to expire (2*MSL)\n"
                    "  CLOSE_WAIT  — remote side sent FIN, waiting for local close\n"
                    "  LAST_ACK    — waiting for final ACK after sending FIN\n\n"
                    "  ss -tan state fin-wait-1   — filter by state"
                ),
                "options": [
                    "a) CLOSE_WAIT",
                    "b) FIN_WAIT_1",
                    "c) TIME_WAIT",
                    "d) LAST_ACK",
                ],
                "answer": "b",
                "hints": [
                    "This is the state immediately after calling close() on a socket.",
                    "FIN has been sent but no ACK or FIN from the other side yet.",
                ],
                "xp": 35,
            },
            {
                "id": "net_3",
                "type": "quiz",
                "title": "Netfilter Chains",
                "question": "In the iptables netfilter framework, which chain processes packets destined for the local machine?",
                "lesson": (
                    "Netfilter chains in the filter table:\n\n"
                    "  INPUT    — packets destined for the local machine\n"
                    "  OUTPUT   — packets originating from the local machine\n"
                    "  FORWARD  — packets being routed through the machine\n\n"
                    "Packet flow: incoming packet -> PREROUTING -> routing decision\n"
                    "  -> if local: INPUT -> local process\n"
                    "  -> if forwarded: FORWARD -> POSTROUTING -> out\n\n"
                    "  iptables -L -n -v        — list all rules with packet counts\n"
                    "  iptables -t nat -L       — list NAT table rules"
                ),
                "options": [
                    "a) FORWARD",
                    "b) OUTPUT",
                    "c) PREROUTING",
                    "d) INPUT",
                ],
                "answer": "d",
                "hints": [
                    "Think about the direction: packets coming IN to the local machine.",
                    "The chain name matches its purpose — processing inbound packets for local delivery.",
                ],
                "xp": 30,
            },
            {
                "id": "net_4",
                "type": "quiz",
                "title": "Network Namespaces",
                "question": "What does a network namespace provide in Linux?",
                "lesson": (
                    "A network namespace provides a complete, isolated copy of the network\n"
                    "stack: its own interfaces, routing table, firewall rules, and sockets.\n\n"
                    "Processes in different network namespaces cannot see each other's\n"
                    "network configuration. This is the foundation of container networking.\n\n"
                    "  ip netns add blue          — create namespace 'blue'\n"
                    "  ip netns exec blue bash     — run bash inside the namespace\n"
                    "  ip link add veth0 type veth peer name veth1  — create veth pair\n"
                    "  ip link set veth1 netns blue — move veth1 into namespace"
                ),
                "options": [
                    "a) A firewall rule set that applies only to specific processes",
                    "b) An isolated network stack with its own interfaces, routes, and firewall rules",
                    "c) A virtual NIC that bonds multiple physical interfaces together",
                    "d) A DNS resolver configuration specific to a user account",
                ],
                "answer": "b",
                "hints": [
                    "Namespaces are the kernel primitive behind container isolation.",
                    "Each namespace gets its own interfaces, routes, iptables rules, and socket space.",
                ],
                "xp": 35,
            },
            {
                "id": "net_5",
                "type": "quiz",
                "title": "TIME_WAIT Accumulation",
                "question": "Why do many sockets in TIME_WAIT state appear on a busy web server, and how long does each persist?",
                "lesson": (
                    "TIME_WAIT occurs on the side that initiates the connection close.\n"
                    "It persists for 2 * MSL (Maximum Segment Lifetime), typically 60 seconds.\n\n"
                    "Purpose:\n"
                    "  1. Ensure the final ACK reaches the remote side\n"
                    "  2. Prevent old duplicate packets from being accepted by a new connection\n"
                    "     using the same 4-tuple\n\n"
                    "On busy servers, thousands of TIME_WAIT sockets are normal.\n"
                    "  net.ipv4.tcp_tw_reuse = 1  — allow reuse of TIME_WAIT sockets\n"
                    "  ss -s                       — summary of socket states"
                ),
                "options": [
                    "a) They indicate failed connections and persist for 10 seconds",
                    "b) The closing side waits 2*MSL (~60s) to handle late packets and ensure final ACK delivery",
                    "c) They are leaked sockets from crashed processes and persist indefinitely",
                    "d) They represent half-open connections and persist for 30 seconds",
                ],
                "answer": "b",
                "hints": [
                    "TIME_WAIT is not a bug — it's a deliberate TCP mechanism on the closing side.",
                    "The wait is 2 times the Maximum Segment Lifetime, usually about 60 seconds.",
                ],
                "xp": 35,
            },
            {
                "id": "net_6",
                "type": "quiz",
                "title": "Connection Tracking",
                "question": "What kernel subsystem does iptables use to track connection states (NEW, ESTABLISHED, RELATED)?",
                "lesson": (
                    "conntrack (connection tracking) is the stateful inspection subsystem\n"
                    "of netfilter. It tracks every connection passing through the kernel.\n\n"
                    "States:\n"
                    "  NEW         — first packet of a new connection\n"
                    "  ESTABLISHED — part of an already-seen bidirectional flow\n"
                    "  RELATED     — new connection related to an existing one (e.g., FTP data)\n"
                    "  INVALID     — packet that doesn't match any known connection\n\n"
                    "  conntrack -L           — list tracked connections\n"
                    "  cat /proc/sys/net/netfilter/nf_conntrack_count\n"
                    "  sysctl net.netfilter.nf_conntrack_max"
                ),
                "options": [
                    "a) nftables",
                    "b) conntrack",
                    "c) tc (traffic control)",
                    "d) eBPF",
                ],
                "answer": "b",
                "hints": [
                    "This subsystem's name literally describes what it does — it tracks connections.",
                    "conntrack is part of netfilter; iptables uses it to match -m state rules.",
                ],
                "xp": 30,
            },
        ],
    },
    # ── ZONE 5: SYSTEMD ─────────────────────────────────────────────────
    "systemd": {
        "id": "systemd",
        "name": "The Init Forge",
        "subtitle": "Units, Services, Timers, Journal & Cgroups",
        "color": "yellow",
        "icon": "🔧",
        "commands": ["systemctl", "journalctl", "systemd-analyze", "timedatectl"],
        "challenges": [
            {
                "id": "sys_1",
                "type": "quiz",
                "title": "Unit Types",
                "question": "Which of these is NOT a valid systemd unit type?",
                "lesson": (
                    "systemd unit types (identified by file extension):\n\n"
                    "  .service  — daemons and one-shot processes\n"
                    "  .socket   — socket-based activation\n"
                    "  .timer    — scheduled activation (cron replacement)\n"
                    "  .mount    — filesystem mount points\n"
                    "  .target   — synchronization points (like runlevels)\n"
                    "  .device   — device-based activation\n"
                    "  .path     — path-based activation (inotify)\n"
                    "  .slice    — cgroup resource management\n"
                    "  .scope    — externally created process groups\n"
                    "  .swap     — swap devices\n\n"
                    "There is no .daemon unit type."
                ),
                "options": [
                    "a) .service",
                    "b) .timer",
                    "c) .daemon",
                    "d) .socket",
                ],
                "answer": "c",
                "hints": [
                    "All valid unit types correspond to specific systemd file extensions.",
                    "While daemons are managed by .service units, there is no .daemon type.",
                ],
                "xp": 25,
            },
            {
                "id": "sys_2",
                "type": "quiz",
                "title": "Service Lifecycle",
                "question": "What command shows the full log output for a specific systemd service since the last boot?",
                "lesson": (
                    "journalctl is the systemd journal reader.\n\n"
                    "  journalctl -u nginx.service -b   — logs for nginx since last boot\n"
                    "  journalctl -u nginx -f            — follow logs live\n"
                    "  journalctl -p err                 — only error-priority messages\n"
                    "  journalctl --since '1 hour ago'   — time-filtered\n"
                    "  journalctl -k                     — kernel messages only (like dmesg)\n"
                    "  journalctl --disk-usage           — how much disk the journal uses\n\n"
                    "The -b flag limits to the current boot. -b -1 shows the previous boot."
                ),
                "options": [
                    "a) systemctl logs nginx.service --boot",
                    "b) journalctl -u nginx.service -b",
                    "c) dmesg -u nginx.service",
                    "d) cat /var/log/nginx/systemd.log",
                ],
                "answer": "b",
                "hints": [
                    "systemd has its own logging system with a dedicated reader command.",
                    "The -u flag selects the unit; -b limits to the current boot.",
                ],
                "xp": 25,
            },
            {
                "id": "sys_3",
                "type": "quiz",
                "title": "Socket Activation",
                "question": "What is the benefit of systemd socket activation?",
                "lesson": (
                    "Socket activation means systemd opens the listening socket, then starts\n"
                    "the actual service only when a connection arrives.\n\n"
                    "Benefits:\n"
                    "  - Services start on demand, reducing boot time\n"
                    "  - No connections are lost — systemd buffers them until the service is ready\n"
                    "  - Services can be restarted without losing the socket (zero-downtime restarts)\n"
                    "  - Parallel startup — sockets are created before services start\n\n"
                    "Example: sshd.socket starts sshd.service only when an SSH connection arrives."
                ),
                "options": [
                    "a) It allows services to bind to privileged ports without root access",
                    "b) It encrypts all socket communication with TLS automatically",
                    "c) It starts services on demand when connections arrive, reducing boot time",
                    "d) It replaces iptables for port-based access control",
                ],
                "answer": "c",
                "hints": [
                    "The socket is opened first; the service starts only when traffic arrives.",
                    "This enables lazy startup and zero-downtime restarts.",
                ],
                "xp": 30,
            },
            {
                "id": "sys_4",
                "type": "quiz",
                "title": "Timer Units",
                "question": "What is the systemd equivalent of a cron job?",
                "lesson": (
                    "systemd timers (.timer units) replace cron with better features:\n\n"
                    "  - Monotonic timers (OnBootSec=, OnActiveSec=)\n"
                    "  - Calendar timers (OnCalendar=)\n"
                    "  - Persistent timers (Persistent=true — catch up if missed)\n"
                    "  - Randomized delays (RandomizedDelaySec=)\n"
                    "  - Full journalctl logging\n"
                    "  - Dependency management and cgroup isolation\n\n"
                    "  systemctl list-timers            — list active timers\n"
                    "  OnCalendar=*-*-* 02:00:00        — daily at 2 AM\n"
                    "  OnCalendar=Mon *-*-* 09:00:00    — every Monday at 9 AM"
                ),
                "options": [
                    "a) .schedule units",
                    "b) .timer units",
                    "c) .cron units",
                    "d) .trigger units",
                ],
                "answer": "b",
                "hints": [
                    "The unit type name matches exactly what it does — scheduling based on time.",
                    "Use 'systemctl list-timers' to see all active ones.",
                ],
                "xp": 25,
            },
            {
                "id": "sys_5",
                "type": "quiz",
                "title": "Cgroup Slices",
                "question": "How does systemd organize processes into cgroup hierarchies?",
                "lesson": (
                    "systemd uses slice units (.slice) to create a cgroup hierarchy:\n\n"
                    "  -.slice (root)\n"
                    "  ├── system.slice   — system services (sshd, nginx, etc.)\n"
                    "  ├── user.slice     — user sessions and services\n"
                    "  └── machine.slice  — virtual machines and containers\n\n"
                    "Every service runs in its own cgroup under its slice, providing:\n"
                    "  - Resource accounting (CPU, memory, I/O per service)\n"
                    "  - Resource limits (MemoryMax=, CPUQuota=)\n"
                    "  - Clean process termination (KillMode=)\n\n"
                    "  systemd-cgls       — show the cgroup tree\n"
                    "  systemd-cgtop      — top-like view of cgroup resource usage"
                ),
                "options": [
                    "a) Each process is assigned to a random cgroup at startup",
                    "b) Using .slice units that organize services into system, user, and machine slices",
                    "c) By kernel PID ranges that map to predetermined cgroup buckets",
                    "d) Through /etc/cgroup.conf which statically assigns processes to groups",
                ],
                "answer": "b",
                "hints": [
                    "systemd has a dedicated unit type for cgroup hierarchy management.",
                    "The three main slices are system.slice, user.slice, and machine.slice.",
                ],
                "xp": 35,
            },
        ],
    },
    # ── ZONE 6: KERNEL MODULES ──────────────────────────────────────────
    "kernel_modules": {
        "id": "kernel_modules",
        "name": "The Module Ring",
        "subtitle": "lsmod, modprobe, dmesg, sysctl & /proc/sys",
        "color": "red",
        "icon": "🔩",
        "commands": ["lsmod", "modprobe", "dmesg", "sysctl", "insmod", "rmmod"],
        "challenges": [
            {
                "id": "km_1",
                "type": "quiz",
                "title": "List Loaded Modules",
                "question": "What command lists all currently loaded kernel modules?",
                "lesson": (
                    "lsmod reads /proc/modules and displays loaded kernel modules.\n\n"
                    "Output columns:\n"
                    "  Module — module name\n"
                    "  Size   — memory used by the module\n"
                    "  Used by — reference count and dependent modules\n\n"
                    "  lsmod                  — list all loaded modules\n"
                    "  lsmod | grep ext4      — check if ext4 is loaded\n"
                    "  modinfo ext4           — show module metadata and parameters\n\n"
                    "Modules live in /lib/modules/$(uname -r)/ as .ko files."
                ),
                "options": [
                    "a) modprobe --list",
                    "b) lsmod",
                    "c) dmesg | grep module",
                    "d) cat /etc/modules",
                ],
                "answer": "b",
                "hints": [
                    "The command name is an abbreviation: 'list modules'.",
                    "It reads /proc/modules and formats the output.",
                ],
                "xp": 25,
            },
            {
                "id": "km_2",
                "type": "quiz",
                "title": "Smart Module Loading",
                "question": "What is the advantage of modprobe over insmod for loading kernel modules?",
                "lesson": (
                    "modprobe vs insmod:\n\n"
                    "  insmod — loads a single module file by exact path. No dependency handling.\n"
                    "  modprobe — loads a module by name, automatically resolving and loading\n"
                    "             all dependencies from the module dependency tree.\n\n"
                    "  modprobe ext4          — loads ext4 and all its dependencies\n"
                    "  modprobe -r ext4       — removes ext4 (and unused dependencies)\n"
                    "  insmod /path/to/ext4.ko — loads only that specific file\n\n"
                    "modprobe uses /lib/modules/$(uname -r)/modules.dep to resolve dependencies.\n"
                    "Run 'depmod' to regenerate the dependency file after installing new modules."
                ),
                "options": [
                    "a) modprobe is faster because it loads modules in parallel",
                    "b) modprobe automatically resolves and loads module dependencies",
                    "c) modprobe can load modules from remote repositories",
                    "d) modprobe compiles modules from source before loading them",
                ],
                "answer": "b",
                "hints": [
                    "insmod needs the exact path and loads only the specified file.",
                    "modprobe understands the dependency tree between modules.",
                ],
                "xp": 25,
            },
            {
                "id": "km_3",
                "type": "quiz",
                "title": "Kernel Ring Buffer",
                "question": "What does the dmesg command display?",
                "lesson": (
                    "dmesg displays the kernel ring buffer — messages from the kernel and\n"
                    "device drivers since boot.\n\n"
                    "  dmesg                   — show full buffer\n"
                    "  dmesg -T                — human-readable timestamps\n"
                    "  dmesg -l err            — only error-level messages\n"
                    "  dmesg -w                — follow (watch) new messages\n"
                    "  dmesg | tail -20        — last 20 messages\n\n"
                    "Useful for diagnosing: hardware detection, driver loading, filesystem\n"
                    "errors, OOM events, USB device connections, network interface changes.\n\n"
                    "journalctl -k — equivalent, using the systemd journal."
                ),
                "options": [
                    "a) System service status messages from systemd",
                    "b) The kernel ring buffer containing boot and driver messages",
                    "c) User authentication logs from PAM",
                    "d) Network packet capture summaries",
                ],
                "answer": "b",
                "hints": [
                    "dmesg is your window into what the kernel is saying.",
                    "The ring buffer contains messages from boot, drivers, and hardware events.",
                ],
                "xp": 25,
            },
            {
                "id": "km_4",
                "type": "quiz",
                "title": "Runtime Kernel Tuning",
                "question": "Which command reads and modifies kernel parameters at runtime?",
                "lesson": (
                    "sysctl reads and writes kernel parameters under /proc/sys/.\n\n"
                    "  sysctl -a                              — list all parameters\n"
                    "  sysctl net.ipv4.ip_forward              — read one parameter\n"
                    "  sysctl -w net.ipv4.ip_forward=1         — set at runtime\n"
                    "  /etc/sysctl.conf or /etc/sysctl.d/*.conf — persistent settings\n"
                    "  sysctl -p                               — reload from config\n\n"
                    "Common parameters:\n"
                    "  vm.swappiness               — swap aggressiveness (0-200)\n"
                    "  net.core.somaxconn           — max socket listen backlog\n"
                    "  kernel.pid_max               — maximum PID value\n"
                    "  fs.file-max                  — system-wide FD limit"
                ),
                "options": [
                    "a) modprobe",
                    "b) sysctl",
                    "c) dmesg",
                    "d) tuned-adm",
                ],
                "answer": "b",
                "hints": [
                    "This command interfaces with /proc/sys/ to tune the running kernel.",
                    "The name combines 'sys' (system) and 'ctl' (control).",
                ],
                "xp": 25,
            },
            {
                "id": "km_5",
                "type": "quiz",
                "title": "Module Blacklisting",
                "question": "How do you prevent a kernel module from being loaded automatically?",
                "lesson": (
                    "Module blacklisting prevents automatic loading:\n\n"
                    "  /etc/modprobe.d/blacklist.conf:\n"
                    "    blacklist nouveau        — prevent nouveau GPU driver\n"
                    "    install nouveau /bin/true — redirect to no-op\n\n"
                    "The 'blacklist' directive only prevents auto-loading; the module can\n"
                    "still be loaded manually with modprobe. The 'install' redirect prevents\n"
                    "even manual loading.\n\n"
                    "After modifying blacklist files, rebuild the initramfs:\n"
                    "  update-initramfs -u  (Debian/Ubuntu)\n"
                    "  dracut -f            (RHEL/Fedora)"
                ),
                "options": [
                    "a) Delete the .ko file from /lib/modules/",
                    "b) Add a 'blacklist' entry in /etc/modprobe.d/",
                    "c) Set the module's permissions to 000",
                    "d) Remove it from /etc/modules.conf",
                ],
                "answer": "b",
                "hints": [
                    "There's a dedicated configuration directory for modprobe behavior.",
                    "The directive is literally called 'blacklist' inside a .conf file.",
                ],
                "xp": 30,
            },
        ],
    },
    # ── ZONE 7: PERFORMANCE ─────────────────────────────────────────────
    "performance": {
        "id": "performance",
        "name": "The Performance Matrix",
        "subtitle": "top, strace, perf, Load Average & Scheduling",
        "color": "white",
        "icon": "📊",
        "commands": ["top", "htop", "strace", "perf", "lsof", "iostat", "sar"],
        "challenges": [
            {
                "id": "perf_1",
                "type": "quiz",
                "title": "Load Average Decoded",
                "question": "What do the three numbers in /proc/loadavg represent?",
                "lesson": (
                    "/proc/loadavg shows three load averages: 1-minute, 5-minute, 15-minute.\n\n"
                    "Load average = average number of processes in the run queue (running or\n"
                    "waiting for CPU) plus processes in uninterruptible I/O wait (D state).\n\n"
                    "Interpretation (for a 4-core system):\n"
                    "  loadavg = 4.0   — all cores fully utilized\n"
                    "  loadavg = 8.0   — overloaded, processes are queuing\n"
                    "  loadavg = 1.0   — light load, 3 cores mostly idle\n\n"
                    "Compare load to number of CPU cores (nproc) for context."
                ),
                "options": [
                    "a) CPU temperature at 1, 5, and 15-minute intervals",
                    "b) Average number of runnable + I/O-waiting processes over 1, 5, and 15 minutes",
                    "c) Percentage of CPU used at 1, 5, and 15-minute samples",
                    "d) Number of context switches per second at three time scales",
                ],
                "answer": "b",
                "hints": [
                    "Load average counts processes, not percentages.",
                    "It includes both processes waiting for CPU and those in uninterruptible I/O wait.",
                ],
                "xp": 30,
            },
            {
                "id": "perf_2",
                "type": "quiz",
                "title": "System Call Tracer",
                "question": "What does strace do when attached to a running process?",
                "lesson": (
                    "strace intercepts and logs every system call made by a process.\n\n"
                    "  strace ls                     — trace all syscalls of 'ls'\n"
                    "  strace -p 1234                — attach to running PID 1234\n"
                    "  strace -e open,read,write ls   — trace only specific syscalls\n"
                    "  strace -c ls                   — summary: count, time per syscall\n"
                    "  strace -f ls                   — follow child processes too\n"
                    "  strace -t -T ls                — timestamp each call + duration\n\n"
                    "strace uses the ptrace() syscall. It adds overhead — don't use on\n"
                    "latency-sensitive production processes without understanding the cost."
                ),
                "options": [
                    "a) It monitors network traffic sent and received by the process",
                    "b) It intercepts and logs every system call the process makes",
                    "c) It traces memory allocations and detects leaks",
                    "d) It records the process's CPU register state at each instruction",
                ],
                "answer": "b",
                "hints": [
                    "strace = system call trace. It shows every interaction between process and kernel.",
                    "It uses ptrace() to intercept syscalls like open(), read(), write(), etc.",
                ],
                "xp": 25,
            },
            {
                "id": "perf_3",
                "type": "quiz",
                "title": "Open File Inspector",
                "question": "What information does 'lsof -p <PID>' display?",
                "lesson": (
                    "lsof (list open files) shows all files opened by a process.\n\n"
                    "In Linux, 'everything is a file': regular files, directories, sockets,\n"
                    "pipes, devices, /proc entries — all appear as open file descriptors.\n\n"
                    "  lsof -p 1234            — all files opened by PID 1234\n"
                    "  lsof -i :80             — processes using port 80\n"
                    "  lsof /var/log/syslog    — processes with this file open\n"
                    "  lsof +D /tmp            — all open files under /tmp\n"
                    "  lsof -u www-data        — all files opened by user www-data"
                ),
                "options": [
                    "a) The CPU and memory usage of the process",
                    "b) All open files, sockets, pipes, and devices held by the process",
                    "c) The process's environment variables and command-line arguments",
                    "d) The shared libraries linked by the process",
                ],
                "answer": "b",
                "hints": [
                    "lsof = list open files. In Linux, sockets and pipes are 'files' too.",
                    "It shows every file descriptor the process holds — regular files, sockets, pipes, devices.",
                ],
                "xp": 25,
            },
            {
                "id": "perf_4",
                "type": "quiz",
                "title": "CPU Scheduling",
                "question": "What is the default CPU scheduler used by the Linux kernel for normal (SCHED_OTHER) processes?",
                "lesson": (
                    "The Completely Fair Scheduler (CFS) has been the default for\n"
                    "SCHED_OTHER (normal) processes since Linux 2.6.23.\n\n"
                    "CFS uses a red-black tree sorted by 'virtual runtime' (vruntime).\n"
                    "Processes that have used less CPU time get scheduled first. This\n"
                    "ensures fairness — every process gets a proportional share.\n\n"
                    "Scheduling policies:\n"
                    "  SCHED_OTHER   — default, CFS (nice values apply)\n"
                    "  SCHED_FIFO    — real-time, first-in-first-out\n"
                    "  SCHED_RR      — real-time, round-robin\n"
                    "  SCHED_BATCH   — optimized for batch workloads\n"
                    "  SCHED_IDLE    — very low priority background tasks\n\n"
                    "Note: Linux 6.6+ introduced EEVDF as a CFS replacement."
                ),
                "options": [
                    "a) Round Robin Scheduler",
                    "b) Priority-Based Preemptive Scheduler",
                    "c) Completely Fair Scheduler (CFS)",
                    "d) Deadline Scheduler",
                ],
                "answer": "c",
                "hints": [
                    "The name reflects its design goal: giving every process a fair share of CPU.",
                    "CFS has been the default since 2.6.23, using virtual runtime for fairness.",
                ],
                "xp": 35,
            },
            {
                "id": "perf_5",
                "type": "quiz",
                "title": "I/O Scheduling",
                "question": "Which I/O scheduler is recommended for SSDs and NVMe devices in modern Linux?",
                "lesson": (
                    "I/O schedulers for block devices:\n\n"
                    "  none (noop)  — no reordering; best for NVMe (hardware has its own queue)\n"
                    "  mq-deadline  — maintains read/write deadline queues; good for SSDs\n"
                    "  bfq          — budget fair queueing; best for interactive workloads on HDD\n"
                    "  kyber        — lightweight, latency-oriented; good for fast SSDs\n\n"
                    "NVMe devices typically use 'none' because the device firmware handles\n"
                    "scheduling more efficiently than the kernel can.\n\n"
                    "  cat /sys/block/sda/queue/scheduler  — current scheduler\n"
                    "  echo 'none' > /sys/block/nvme0n1/queue/scheduler — change it"
                ),
                "options": [
                    "a) CFQ (Completely Fair Queueing)",
                    "b) none (noop) — let the device handle scheduling",
                    "c) bfq (Budget Fair Queueing)",
                    "d) deadline (single-queue)",
                ],
                "answer": "b",
                "hints": [
                    "NVMe devices have sophisticated internal schedulers — adding another layer is overhead.",
                    "The simplest scheduler is best when the hardware already optimizes I/O ordering.",
                ],
                "xp": 30,
            },
            {
                "id": "perf_6",
                "type": "quiz",
                "title": "perf Profiler",
                "question": "What type of analysis does 'perf record' followed by 'perf report' provide?",
                "lesson": (
                    "perf is the Linux kernel's built-in profiling tool using hardware\n"
                    "performance counters and software tracepoints.\n\n"
                    "  perf record ./myapp       — sample CPU events while running myapp\n"
                    "  perf report               — analyze the recorded profile\n"
                    "  perf stat ./myapp          — count hardware events (cache misses, etc.)\n"
                    "  perf top                   — live, system-wide profiling\n\n"
                    "perf record samples the instruction pointer at regular intervals,\n"
                    "building a statistical profile of where CPU time is spent.\n"
                    "perf report shows the functions ranked by sample count — your hotspots."
                ),
                "options": [
                    "a) Memory leak detection and heap analysis",
                    "b) Statistical CPU profiling showing which functions consume the most time",
                    "c) Network latency measurement between hosts",
                    "d) Disk I/O bandwidth and IOPS benchmarking",
                ],
                "answer": "b",
                "hints": [
                    "perf samples where the CPU is spending time, then reports the hot functions.",
                    "It uses hardware performance counters for low-overhead, high-accuracy profiling.",
                ],
                "xp": 35,
            },
        ],
    },
    # ── ZONE 8: SECURITY ────────────────────────────────────────────────
    "security_linux": {
        "id": "security_linux",
        "name": "The Hardened Layer",
        "subtitle": "SELinux, Capabilities, Namespaces, seccomp & Audit",
        "color": "red",
        "icon": "🛡",
        "commands": ["getenforce", "getcap", "unshare", "auditctl", "ausearch"],
        "challenges": [
            {
                "id": "sec_1",
                "type": "quiz",
                "title": "SELinux Modes",
                "question": "What are the three operating modes of SELinux?",
                "lesson": (
                    "SELinux (Security-Enhanced Linux) operates in three modes:\n\n"
                    "  Enforcing   — policies are enforced; violations are blocked and logged\n"
                    "  Permissive  — policies are NOT enforced; violations are only logged\n"
                    "  Disabled    — SELinux is completely off\n\n"
                    "  getenforce           — show current mode\n"
                    "  setenforce 1         — switch to enforcing (temporary)\n"
                    "  setenforce 0         — switch to permissive (temporary)\n"
                    "  /etc/selinux/config  — persistent mode setting\n"
                    "  sestatus             — detailed SELinux status"
                ),
                "options": [
                    "a) Active, Passive, Disabled",
                    "b) Enforcing, Permissive, Disabled",
                    "c) Strict, Targeted, Minimal",
                    "d) Mandatory, Discretionary, Off",
                ],
                "answer": "b",
                "hints": [
                    "One mode blocks violations, one just logs them, and one turns it off entirely.",
                    "'getenforce' returns one of these three modes.",
                ],
                "xp": 25,
            },
            {
                "id": "sec_2",
                "type": "quiz",
                "title": "Linux Capabilities",
                "question": "What problem do Linux capabilities solve?",
                "lesson": (
                    "Traditionally, root has ALL privileges and normal users have almost none.\n"
                    "Capabilities split root's power into ~40 distinct privileges:\n\n"
                    "  CAP_NET_BIND_SERVICE — bind to ports below 1024\n"
                    "  CAP_NET_RAW          — use raw sockets (ping, tcpdump)\n"
                    "  CAP_SYS_ADMIN        — broad system admin (mount, cgroups, etc.)\n"
                    "  CAP_DAC_OVERRIDE     — bypass file permission checks\n"
                    "  CAP_CHOWN            — change file ownership\n\n"
                    "  getcap /usr/bin/ping   — show file capabilities\n"
                    "  setcap cap_net_raw+ep /usr/bin/myping — set capabilities\n"
                    "  getpcaps <pid>         — show process capabilities\n\n"
                    "Capabilities allow least-privilege: give a process only what it needs."
                ),
                "options": [
                    "a) They allow multiple users to share the same UID",
                    "b) They split root's monolithic privileges into fine-grained permissions",
                    "c) They encrypt filesystem capabilities for secure boot",
                    "d) They provide role-based access control for network services",
                ],
                "answer": "b",
                "hints": [
                    "The problem: root is all-or-nothing. Capabilities break that into pieces.",
                    "Instead of running as root to bind port 80, grant only CAP_NET_BIND_SERVICE.",
                ],
                "xp": 30,
            },
            {
                "id": "sec_3",
                "type": "quiz",
                "title": "Namespace Isolation",
                "question": "Which Linux namespaces are used together to create a container's isolation?",
                "lesson": (
                    "Linux namespaces isolate different aspects of the system:\n\n"
                    "  PID    — process ID isolation (PID 1 inside container)\n"
                    "  NET    — network stack (interfaces, routes, iptables)\n"
                    "  MNT    — mount points (filesystem view)\n"
                    "  UTS    — hostname and domain name\n"
                    "  IPC    — inter-process communication (shared memory, semaphores)\n"
                    "  USER   — UID/GID mapping (unprivileged containers)\n"
                    "  CGROUP — cgroup root (resource limits)\n"
                    "  TIME   — boot/monotonic clock offsets (Linux 5.6+)\n\n"
                    "  unshare --pid --net --mount bash — create new namespaces\n"
                    "  lsns                              — list all namespaces"
                ),
                "options": [
                    "a) Only PID and NET namespaces",
                    "b) PID, NET, MNT, UTS, IPC, USER, and CGROUP namespaces",
                    "c) Only filesystem and network namespaces",
                    "d) SELinux domains and AppArmor profiles",
                ],
                "answer": "b",
                "hints": [
                    "Containers use multiple namespace types together for full isolation.",
                    "There are 7+ namespace types; containers typically use all of them.",
                ],
                "xp": 30,
            },
            {
                "id": "sec_4",
                "type": "quiz",
                "title": "seccomp Filtering",
                "question": "What does seccomp-bpf allow you to do?",
                "lesson": (
                    "seccomp-bpf (Secure Computing mode with Berkeley Packet Filter) lets\n"
                    "you define a whitelist or blacklist of system calls a process can make.\n\n"
                    "If a process attempts a blocked syscall, the kernel can:\n"
                    "  - Kill the process (SECCOMP_RET_KILL)\n"
                    "  - Send a signal (SECCOMP_RET_TRAP)\n"
                    "  - Return an error (SECCOMP_RET_ERRNO)\n"
                    "  - Log the attempt (SECCOMP_RET_LOG)\n\n"
                    "Used by: Docker (default seccomp profile blocks ~44 syscalls),\n"
                    "Chrome, Firefox, systemd services (SystemCallFilter=).\n\n"
                    "  grep Seccomp /proc/<pid>/status  — check if seccomp is active"
                ),
                "options": [
                    "a) Encrypt system call arguments before they reach the kernel",
                    "b) Filter which system calls a process is allowed to make",
                    "c) Compress system call results for faster IPC",
                    "d) Log all system calls to a remote syslog server",
                ],
                "answer": "b",
                "hints": [
                    "seccomp restricts the kernel API surface available to a process.",
                    "BPF programs decide per-syscall: allow, deny, or kill.",
                ],
                "xp": 35,
            },
            {
                "id": "sec_5",
                "type": "quiz",
                "title": "Audit Framework",
                "question": "What command adds a rule to the Linux audit system to watch a file for changes?",
                "lesson": (
                    "The Linux Audit framework (auditd) logs security-relevant events.\n\n"
                    "  auditctl -w /etc/passwd -p wa -k passwd_changes\n"
                    "    -w  — watch this file\n"
                    "    -p  — permissions to watch: w(write), a(attribute), r(read), x(execute)\n"
                    "    -k  — key for searching logs\n\n"
                    "  ausearch -k passwd_changes     — search by key\n"
                    "  aureport --summary             — summary of audit events\n"
                    "  auditctl -l                    — list all rules\n"
                    "  /etc/audit/audit.rules          — persistent rules\n\n"
                    "The audit system operates at the kernel level, making it extremely\n"
                    "difficult for attackers to evade."
                ),
                "options": [
                    "a) inotifywait -m /etc/passwd",
                    "b) auditctl -w /etc/passwd -p wa -k passwd_changes",
                    "c) watchdog --file /etc/passwd --log",
                    "d) sysctl -w audit.watch=/etc/passwd",
                ],
                "answer": "b",
                "hints": [
                    "The audit system has its own control command for adding rules.",
                    "The -w flag watches a file; -p specifies which operations to audit.",
                ],
                "xp": 30,
            },
        ],
    },
}

ZONE_ORDER = [
    "process_management",
    "memory_management",
    "filesystem_internals",
    "networking_stack",
    "systemd",
    "kernel_modules",
    "performance",
    "security_linux",
]
