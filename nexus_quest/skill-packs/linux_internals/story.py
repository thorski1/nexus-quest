"""
story.py - Narrative text for Kernel Ops (linux_internals pack)
Theme: Beneath the terminal lies the kernel. Understand the machine.
A systems engineer descends through the layers of Linux internals to
diagnose an impossible production failure — one that exists below userspace.
"""

INTRO_STORY = """
The alert fired at [bold cyan]2:47 AM[/bold cyan]. Not from the application. Not from the orchestrator.
From the [bold white]kernel itself[/bold white].

A production cluster — forty-eight nodes — started dropping connections.
Not all of them. Not consistently. The load balancer health checks passed.
The application logs showed nothing. Monitoring dashboards: green across the board.

But packets were vanishing. Processes were stalling in uninterruptible sleep.
The OOM killer fired on a node with [bold white]12 GB of free RAM[/bold white].

The SRE team restarted the pods. The problem followed them to different nodes.
They scaled up. The new nodes exhibited the same behavior within hours.
They rolled back the last deployment. No change.

[bold magenta]The bug is not in the application. It's not in the container. It's not in
the orchestrator. The bug is in the space between userspace and hardware —
in the kernel, the scheduler, the memory manager, the network stack,
the filesystem layer. The space most engineers never look.[/bold magenta]

You've been called because you [bold white]do[/bold white] look there.

You are a [bold cyan]Kernel Operations Specialist[/bold cyan].

Your tools are /proc, /sys, strace, perf, dmesg, and twenty years of
accumulated knowledge about how Linux actually works — not the abstraction,
but the mechanism. Not the API, but the implementation.

The cluster is still running. The problem is still active.

[bold cyan]Start with the processes. Everything in Linux starts with a process.[/bold cyan]
"""

ZONE_INTROS = {
    "process_management": """
[bold cyan]== THE PROCESS TABLE ==[/bold cyan]

Everything running on this system is a process. Every process has a PID,
a parent, a state, a priority, and a set of resources allocated by the kernel.

The stalled processes on the affected nodes are in state [bold white]D[/bold white] — uninterruptible
sleep. They're waiting for something from the kernel that isn't coming back.
Before you can diagnose what's blocking them, you need to understand how
processes are born, how they die, and what happens when they refuse to do either.

[yellow]fork()[/yellow] — create a child process.
[yellow]exec()[/yellow] — replace the current process image.
[yellow]kill[/yellow] — send signals to processes.
[yellow]nice / renice[/yellow] — adjust scheduling priority.

[italic]"Every process is a promise the kernel made to userspace.
When the kernel breaks that promise, you see it in the process table first."[/italic]
""",
    "memory_management": """
[bold cyan]== THE MEMORY GRID ==[/bold cyan]

The OOM killer fired on a node with 12 GB free. That shouldn't happen —
unless you understand what "free" actually means in Linux.

The memory subsystem is a labyrinth of virtual addresses, page tables,
slab caches, page caches, and dirty pages waiting to be written back to disk.
"Free" in [yellow]free -h[/yellow] doesn't mean what most engineers think it means.
The cgroup memory limit for the affected pod was set to 4 GB.
The pod was using 3.8 GB. But inside that cgroup, the kernel's accounting
includes page cache pages that are reclaimable but counted as "used."

The OOM killer saw a cgroup at its limit. It did what it was designed to do.

[yellow]free[/yellow] / [yellow]vmstat[/yellow] — memory statistics.
[yellow]/proc/meminfo[/yellow] — detailed kernel memory breakdown.
[yellow]cgroups memory.max[/yellow] — hard limits that trigger OOM.

[italic]"Memory in Linux is not a pool. It's an economy.
The OOM killer is the bankruptcy court."[/italic]
""",
    "filesystem_internals": """
[bold cyan]== THE INODE VAULT ==[/bold cyan]

The stalled processes were waiting on filesystem I/O. But the disks were fine —
SMART checks passed, I/O throughput was nominal. The problem was in the
filesystem layer itself.

A [yellow]stat[/yellow] call on a specific directory was taking [bold white]14 seconds[/bold white]. Not because the
disk was slow, but because the directory had [bold white]2.3 million entries[/bold white] and the
filesystem was doing a linear scan of directory entries to find the inode.

The filesystem isn't just where files live. It's a data structure with
performance characteristics that change dramatically under different conditions.
Inodes, dentries, the VFS layer, /proc, /sys — the filesystem is the kernel's
primary interface to everything.

[yellow]stat[/yellow] — read inode metadata.
[yellow]ls -i[/yellow] — show inode numbers.
[yellow]mount[/yellow] / [yellow]findmnt[/yellow] — filesystem mount topology.
[yellow]/proc[/yellow] / [yellow]/sys[/yellow] — virtual filesystems.

[italic]"The filesystem is not storage. It's an interface.
When the interface is slow, everything above it stalls."[/italic]
""",
    "networking_stack": """
[bold cyan]== THE SOCKET LAYER ==[/bold cyan]

Packets vanishing. Not dropped by the application — dropped by the kernel.
The netfilter conntrack table hit its maximum. New connections were being
silently discarded because the kernel had no room to track them.

[yellow]ss -s[/yellow] showed 131,072 connections in TIME_WAIT.
[yellow]conntrack -C[/yellow] showed the conntrack table at 100% capacity.
The default [yellow]nf_conntrack_max[/yellow] is 65,536. The system was handling
twice that in TIME_WAIT sockets alone.

The network stack in Linux is not a black box. It's a state machine with
tunable parameters, firewall chains, connection tracking tables, and
namespace isolation. Every packet traverses a well-defined path through
the kernel. Understanding that path is the difference between
"packets are being dropped" and knowing exactly where and why.

[yellow]ss[/yellow] — socket statistics (replacement for netstat).
[yellow]iptables[/yellow] / [yellow]nftables[/yellow] — packet filtering.
[yellow]ip netns[/yellow] — network namespace operations.
[yellow]conntrack[/yellow] — connection tracking table.

[italic]"The network doesn't lie. But it only tells the truth
to people who know where to look."[/italic]
""",
    "systemd": """
[bold cyan]== THE INIT FORGE ==[/bold cyan]

systemd is PID 1 on every affected node. It manages every service, every
cgroup, every timer, every socket, every mount point. When a service crashes
and restarts, systemd decides when, how, and whether to restart it.

The affected service was configured with [yellow]Restart=always[/yellow] and
[yellow]RestartSec=0[/yellow]. When the OOM killer terminated it, systemd restarted
it immediately. The service allocated the same memory. The OOM killer fired
again. Restart. OOM. Restart. OOM. A tight loop — [bold white]847 restarts in 3 hours[/bold white] —
generating thousands of journal entries and cgroup creation/destruction events.

The real failure wasn't the OOM. It was the restart policy.

[yellow]systemctl[/yellow] — manage units.
[yellow]journalctl[/yellow] — read the journal.
[yellow]systemd-cgls[/yellow] — cgroup hierarchy.
[yellow]systemd-analyze[/yellow] — boot and unit timing.

[italic]"systemd doesn't just start services. It defines the rules
of life and death for every process on the system."[/italic]
""",
    "kernel_modules": """
[bold cyan]== THE MODULE RING ==[/bold cyan]

The network driver on six of the forty-eight nodes was loaded with a
non-default parameter. Someone — months ago — ran [yellow]modprobe[/yellow] with a
custom [yellow]ring_buffer_size[/yellow] to "optimize" network throughput. It worked.
Until traffic patterns changed and the oversized ring buffers started
consuming kernel memory that the OOM killer couldn't reclaim.

Kernel modules are code that runs in ring 0 — the most privileged
execution context. A misconfigured module parameter can destabilize an
entire system. A missing module means a filesystem can't be mounted or
a network interface can't be brought up.

Understanding what's loaded, why it's loaded, and what parameters it's
running with is fundamental to diagnosing kernel-level failures.

[yellow]lsmod[/yellow] — list loaded modules.
[yellow]modprobe[/yellow] / [yellow]modinfo[/yellow] — load modules and view metadata.
[yellow]dmesg[/yellow] — kernel message buffer.
[yellow]sysctl[/yellow] — runtime kernel parameters.

[italic]"A kernel module runs with the kernel's authority.
There is no sandbox. There is no rollback."[/italic]
""",
    "performance": """
[bold cyan]== THE PERFORMANCE MATRIX ==[/bold cyan]

The problem is identified. The fix is deployed. But the question remains:
how do you see it next time before the cluster burns?

Performance observability in Linux is not one tool — it's a stack of tools,
each operating at a different layer. [yellow]top[/yellow] shows you what the kernel's
scheduler is doing. [yellow]strace[/yellow] shows you what a process is asking the kernel.
[yellow]perf[/yellow] shows you where CPU cycles are actually being spent — down to the
function and instruction level.

The load average on the affected nodes was [bold white]147.3[/bold white] on a 4-core machine.
[yellow]top[/yellow] showed 200+ processes in D state. [yellow]perf record[/yellow] showed 89% of CPU time
in the kernel's memory reclaim path — the system was spending all its time
trying to free memory instead of running workloads.

[yellow]top[/yellow] / [yellow]htop[/yellow] — process-level resource view.
[yellow]strace[/yellow] — system call tracing.
[yellow]perf[/yellow] — hardware counter profiling.
[yellow]lsof[/yellow] — open file descriptor inspection.

[italic]"You cannot optimize what you cannot measure.
You cannot diagnose what you cannot observe."[/italic]
""",
    "security_linux": """
[bold cyan]== THE HARDENED LAYER ==[/bold cyan]

The incident is resolved. The post-mortem is written. But one finding
remains unexplained: the modprobe command that changed the ring buffer
parameter was run by a process with no login session, no SSH key, and
no entry in auth.log. The audit trail is empty for that 30-second window.

Either the audit system was disabled, the process ran in a namespace
that wasn't being audited, or someone with CAP_SYS_ADMIN cleared the
audit buffer before exiting.

Linux security is layers: discretionary access control (permissions),
mandatory access control (SELinux/AppArmor), capabilities, namespaces,
seccomp filters, and the audit framework. Each layer catches what the
others miss. When all layers are configured correctly, the attack surface
shrinks to near zero. When one is missing, it becomes the entry point.

[yellow]getenforce[/yellow] / [yellow]sestatus[/yellow] — SELinux status.
[yellow]getcap[/yellow] / [yellow]setcap[/yellow] — file capabilities.
[yellow]unshare[/yellow] / [yellow]nsenter[/yellow] — namespace operations.
[yellow]auditctl[/yellow] / [yellow]ausearch[/yellow] — audit rules and search.

[italic]"Security is not a feature. It's a property.
It exists only when every layer is present."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "process_management": """
[bold green]THE PROCESS TABLE — MAPPED.[/bold green]

fork(), exec(), signals, zombies, nice values, threads — you understand
how Linux creates, schedules, and terminates the fundamental unit of work.

The D-state processes on the affected nodes are no longer a mystery.
They were waiting on memory allocation that the kernel couldn't satisfy
because the cgroup limit was hit and reclaim was failing.

The process is the symptom. The memory subsystem is the cause.

[bold cyan]The Memory Grid is next. Understand how Linux actually manages RAM.[/bold cyan]
""",
    "memory_management": """
[bold green]THE MEMORY GRID — DECODED.[/bold green]

Virtual memory, page tables, copy-on-write, swap, the OOM killer, cgroup
memory limits — you understand the economy that the kernel runs.

The OOM killer didn't malfunction. It did exactly what it was designed to do
when a cgroup hits memory.max. The misconfiguration was the limit itself —
set too low for the workload, with no memory.high threshold to trigger
early reclaim before the hard limit was reached.

[bold cyan]The Inode Vault. The filesystem layer that was amplifying the problem.[/bold cyan]
""",
    "filesystem_internals": """
[bold green]THE INODE VAULT — EXCAVATED.[/bold green]

Inodes, directory entries, filesystem types, /proc, /sys, file descriptors —
you see the filesystem not as a place to store files but as the kernel's
primary data interface.

The 2.3-million-entry directory was a log rotation failure. Application logs
were being written as individual files instead of appended to a single file.
Each stat() call on that directory was a linear scan. The inode cache was
thrashing, evicting useful entries and replacing them with garbage.

[bold cyan]The Socket Layer. Where packets go to disappear.[/bold cyan]
""",
    "networking_stack": """
[bold green]THE SOCKET LAYER — TRACED.[/bold green]

Sockets, TCP states, netfilter chains, conntrack tables, network namespaces —
you can trace a packet from the NIC to the application and back.

The conntrack table overflow was the proximate cause of the dropped connections.
The fix: increase nf_conntrack_max, tune tcp_tw_reuse, and segment traffic
using network namespaces so that high-connection-count workloads don't exhaust
the shared conntrack table.

[bold cyan]The Init Forge. systemd was making the problem worse. Understand why.[/bold cyan]
""",
    "systemd": """
[bold green]THE INIT FORGE — MASTERED.[/bold green]

Units, services, timers, socket activation, journalctl, cgroup slices —
you understand the system that manages every other system on the machine.

The restart loop — 847 restarts in 3 hours — was the amplification vector.
Each restart created a new cgroup, allocated memory, hit the limit, got
OOM-killed, and restarted. The fix: RestartSec=30, StartLimitIntervalSec=300,
StartLimitBurst=5. Rate-limit the restarts. Let the system breathe.

[bold cyan]The Module Ring. Someone changed a kernel parameter. Find out what and why.[/bold cyan]
""",
    "kernel_modules": """
[bold green]THE MODULE RING — AUDITED.[/bold green]

lsmod, modprobe, dmesg, sysctl, blacklisting — you can inspect and modify
the kernel's runtime configuration and understand what's loaded and why.

The oversized ring buffer parameter was the root cause. Six nodes had a
custom modprobe configuration that tripled the network driver's memory
allocation per interface. Under the new traffic pattern, that memory was
never reclaimed, slowly starving the cgroup of available pages.

[bold cyan]The Performance Matrix. Learn to see the problem before it becomes an incident.[/bold cyan]
""",
    "performance": """
[bold green]THE PERFORMANCE MATRIX — CALIBRATED.[/bold green]

Load averages, strace, perf, lsof, CPU scheduling, I/O scheduling —
you have the observability stack to diagnose any system-level performance issue.

A load average of 147 on a 4-core machine. 200 processes in D state.
89% of CPU in kernel reclaim. These numbers tell a story: the system was
drowning in memory pressure, and every tool in the performance stack
pointed to the same place — the memory reclaim path.

[bold cyan]The Hardened Layer. The final question: who changed the kernel parameter, and how?[/bold cyan]
""",
    "security_linux": """
[bold yellow]★ ★ ★  THE HARDENED LAYER — SECURED.  ★ ★ ★[/bold yellow]

[bold white]The investigation is complete.[/bold white]

Timeline:
  [cyan]T-90d[/cyan]  Engineer runs modprobe with custom ring_buffer_size on 6 nodes.
  [cyan]T-30d[/cyan]  Traffic pattern shifts. Ring buffers consume increasing kernel memory.
  [cyan]T-7d[/cyan]   Cgroup memory pressure builds. Page cache eviction accelerates.
  [cyan]T-12h[/cyan]  Conntrack table fills. Packets begin dropping.
  [cyan]T-3h[/cyan]   OOM killer fires inside the cgroup. systemd restarts. Loop begins.
  [cyan]T-0[/cyan]    847 restarts. 200 D-state processes. Load average 147. Alert fires.

Root cause: [bold white]a kernel module parameter change that was never documented,
never audited, and never tested under the current traffic pattern.[/bold white]

The fix was four lines of configuration. The diagnosis required understanding
every layer of the Linux kernel — from processes to memory to filesystems
to networking to systemd to modules to performance tooling to security auditing.

[bold magenta]Beneath the terminal lies the kernel.
Now you understand the machine.[/bold magenta]

[bold yellow]KERNEL OPERATIONS SPECIALIST: CERTIFIED.  INCIDENT: RESOLVED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "process_management": "[bold red]⚠  PROCESS AUTOPSY: The D-State Investigation[/bold red]\n200 processes stuck in uninterruptible sleep. Prove you understand process lifecycle, signals, and scheduling well enough to read the process table.",
    "memory_management": "[bold red]⚠  MEMORY FORENSICS: The OOM Paradox[/bold red]\n12 GB free on the host. OOM killer fired anyway. Prove you understand virtual memory, cgroups, and the OOM scoring system.",
    "filesystem_internals": "[bold red]⚠  INODE ARCHAEOLOGY: The 14-Second stat()[/bold red]\n2.3 million directory entries. A stat call that should take microseconds takes 14 seconds. Prove you know the filesystem layer.",
    "networking_stack": "[bold red]⚠  PACKET TRACE: The Conntrack Overflow[/bold red]\n131,072 TIME_WAIT sockets. Conntrack table at capacity. Prove you can trace a packet through the kernel's network stack.",
    "systemd": "[bold red]⚠  SERVICE LOOP: The 847 Restarts[/bold red]\nRestart=always with RestartSec=0. OOM on every cycle. Prove you understand systemd well enough to stop the loop.",
    "kernel_modules": "[bold red]⚠  MODULE AUDIT: The Phantom Parameter[/bold red]\nSomeone changed a kernel module parameter on 6 nodes months ago. Prove you can find it, understand it, and revert it.",
    "performance": "[bold red]⚠  LOAD AVERAGE 147: The Full Stack Profile[/bold red]\n4 cores. Load 147. 89% of CPU in kernel reclaim. Prove you can use the performance stack to find the bottleneck.",
    "security_linux": "[bold red]★  GHOST ACCESS: The Missing Audit Trail[/bold red]\nA modprobe command with no audit entry, no auth log, no session. Prove you understand Linux security layers well enough to explain how — and prevent it.",
}
