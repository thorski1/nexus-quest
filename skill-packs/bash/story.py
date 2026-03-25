"""
story.py - Narrative text for Terminal Quest
"""

INTRO_STORY = """
The megacorps won. Not with armies, not with bombs — they won with [bold cyan]UX designers[/bold cyan].

They built interfaces so smooth, so frictionless, so breathtakingly intuitive that nobody
needed to look underneath them anymore. Touchscreens. Drag-and-drop. Context menus that
anticipated your every desire. A generation of humans who had never seen a prompt.

Somewhere beneath the React frontends, beneath the REST APIs and the middleware and the
abstraction layers stacked seventeen-deep like geological strata — there is a [bold white]substrate[/bold white].
Raw. Unfiltered. Text-based. The corps call it a "legacy interface." The underground calls
it [bold cyan]The Shell[/bold cyan].

The corps know it exists. Their sysadmins breathe it. Their security teams monitor it.
But they've spent two decades training a generation to believe it's irrelevant, that real
computing happens in [italic]apps[/italic] and [italic]dashboards[/italic] and
[italic]intuitive experiences[/italic].

Which means anyone who knows how to use The Shell is basically a wizard walking through a
city of blind people.

[bold white]That's you.[/bold white]

You are a [bold magenta]Ghost[/bold magenta] — an unlicensed freelance penetration tester working the gray markets
of the digital underground. You live on caffeine, spite, and the particular satisfaction
of watching corporate firewalls fold like wet cardboard. You've been hired — anonymously,
through three layers of cutouts — to extract something from deep inside a corporate network
they call [bold yellow]The Terminal[/bold yellow].

Nobody knows exactly what's in it. The client is paying enough that you've decided not to ask.

The only way in is through The Shell. No GUI. No autocomplete. Just you, a prompt, and
everything the corps hope you've forgotten.

[bold cyan]Jack in. The clock started when you read this sentence.[/bold cyan]
"""

ZONE_INTROS = {
    "antechamber": """
[bold cyan]== THE JACK NODE ==[/bold cyan]

First time in The Shell proper, or first time it matters?

Either way, you're in the Threshold now — the outermost layer of The Terminal's architecture.
The corps poured millions into making sure nobody ever needed to be here. Sensor-studded
walls, passive monitoring, intrusion-detection algos running on hardware that costs more
than your apartment. But none of it matters if you don't know where you are.

[italic]Navigation is not glamorous. Navigation is survival.[/italic]

The commands etched into the terminal's memory banks are old — older than the corps,
older than the GUI, older than the internet as the marketing teams understand it.
[yellow]ls[/yellow]. [yellow]cd[/yellow]. [yellow]pwd[/yellow]. Three letters. Total information control.

A ghost who can't navigate is just a corpse waiting to happen.
""",
    "archive_vaults": """
[bold cyan]== THE DEAD DROP VAULTS ==[/bold cyan]

You push deeper and the architecture changes. The walls here are data — petabytes of
corporate files stacked in directory trees that go down forty levels. Financial records,
internal memos, personnel files on fifty thousand employees who don't know they're in here.

The corps archive everything. [bold white]Everything.[/bold white] It's not out of sentimentality.
It's because information is leverage, and leverage is the only currency that actually matters
in the late-stage corporate monoculture.

The tools: [yellow]cat[/yellow], [yellow]cp[/yellow], [yellow]mv[/yellow], [yellow]rm[/yellow], [yellow]touch[/yellow].
Ancient, reliable, indifferent. They don't care if you're authorized. They don't check
badges. They just execute.

[italic]"A file with the wrong name is a liability. A file with no name doesn't exist.
A file that doesn't exist cannot be subpoenaed."[/italic]
                                        — graffiti in The Shell's lower stacks
""",
    "oracle_library": """
[bold cyan]== THE SIGNAL BROKER ==[/bold cyan]

You've found the corps' intelligence layer. Terabytes of intercepts, market analyses,
competitor surveillance, internal communications that were never supposed to leave the
building. The data is enormous and deliberately unindexed — security through volume.

This is where amateurs give up and professionals get to work.

The Shell People — the original sysadmins, the ones who built all this before the corps
bought them out or burned them out — they had tools for this. Pattern matchers that could
pull a single signal from an ocean of noise in milliseconds.

[yellow]grep[/yellow] — the extractor. [yellow]find[/yellow] — the path hunter. [yellow]sort[/yellow],
[yellow]uniq[/yellow], [yellow]wc[/yellow] — the signal shapers.

[italic]"The answer is always in the data. The question is whether you can hear it
over the static they pipe in specifically to drown it out."[/italic]
""",
    "pipe_sanctum": """
[bold cyan]== THE PIPE WORKS ==[/bold cyan]

The architecture here is different. Narrow conduits of live signal connect zone to zone,
process to process, tool to tool. The corps don't understand this layer — they built on
top of it without ever studying what was underneath. They think data moves in transactions.
They think in [italic]requests[/italic] and [italic]responses[/italic].

You think in [bold yellow]streams[/bold yellow].

The pipe — [yellow]|[/yellow] — is the most dangerous character in computing. It's not
flashy. It doesn't have a logo. No corp has ever successfully put it on a roadmap.
It just routes output to input with zero ceremony and zero overhead, and it's been doing
that since before anyone in the C-suite was born.

[yellow]>[/yellow] [yellow]>>[/yellow] [yellow]<[/yellow] [yellow]tee[/yellow] [yellow]xargs[/yellow]
— the signal routing toolkit. Learn to use them and data stops being a wall and starts
being a river you steer.

[italic]"One command does one thing. One pipe does everything."[/italic]
""",
    "process_catacombs": """
[bold cyan]== THE GHOST STACK ==[/bold cyan]

Deeper. Colder. The walls hum with invisible computation.

Every system is haunted. Daemon processes running in the background since the last reboot —
which, for some of these corporate servers, was three years ago. Scheduled jobs. Watchers.
Loggers logging other loggers. Monitoring processes that themselves are being monitored.
It's processes all the way down, and somewhere in that stack is the thread you need to pull.

The corps' security teams love this layer because the processes are supposed to be
invisible to anyone without root access. The corps' security teams are also the same
people who approved [bold cyan]password1[/bold cyan] as an acceptable credential policy for three years.

[yellow]ps[/yellow], [yellow]kill[/yellow], [yellow]jobs[/yellow], [yellow]bg[/yellow], [yellow]fg[/yellow]
— the necromantic toolkit. You can see them now. Every ghost process. Every daemon.
Every undead corporate service that nobody remembers deploying but everyone is afraid to kill.

[italic]"A process you cannot see controls you. A process you can see, you can control.
A process you can kill — that's power."[/italic]
""",
    "permissions_fortress": """
[bold cyan]== THE ACCESS GRID ==[/bold cyan]

Now the corps start fighting back seriously.

The Access Grid is where the real security lives — not the theatre-security of login
screens and two-factor auth tokens, but the fundamental, low-level, UNIX-born permission
system that decides who can read what, write what, execute what. Three bits for owner.
Three bits for group. Three bits for everyone else. Nine bits of digital law that have
governed file access since before the internet had pictures.

The corps layered ACLs and RBAC systems on top of this. They added dashboards to manage
it, audit trails, compliance reports. But underneath all of that, it still comes down
to [yellow]chmod[/yellow] and [yellow]chown[/yellow] and a twelve-digit octal value.

[yellow]chmod[/yellow], [yellow]chown[/yellow], [yellow]ls -l[/yellow], [yellow]umask[/yellow]
— the keys to every door. Learn to read permission strings and you'll see exactly which
doors the sysadmins forgot to lock.

[italic]"777 is not a jackpot. 777 is an invitation."[/italic]
""",
    "scripting_citadel": """
[bold cyan]== THE CODE FORGE ==[/bold cyan]

This is where hackers stop being users and start being [bold white]builders[/bold white].

The corps want you to use their tools, their APIs, their approved integrations. They want
you operating inside sandboxes they designed, pulling data through endpoints they control,
at rates they throttle, generating logs they archive and sell. Their whole business model
depends on you not writing your own tools.

The Scripting Citadel is the corps' nightmare. It's where a single human with a text editor
and a working knowledge of bash can automate in an afternoon what takes a corporate IT
department a quarter and a $2M consulting contract.

[yellow]variables[/yellow], [yellow]loops[/yellow], [yellow]if/else[/yellow], [yellow]functions[/yellow]
— the building blocks. Repetition becomes code. Code becomes automation. Automation becomes
leverage. Leverage is everything.

[italic]"If you do it twice, write a script. If you write a script, you own the machine."[/italic]
""",
    "network_nexus": """
[bold cyan]== THE MEAT HIGHWAY ==[/bold cyan]

The Shell civilization did not stay local. Through fiber and copper and satellite uplinks
and radio spectrum that the corps spent decades trying to license and regulate out of
existence, the terminals talked to each other. They still do.

The Meat Highway is the network layer — the actual infrastructure beneath the cloud,
beneath the CDN, beneath the load balancers and the reverse proxies and the API gateways
with their rate limiters and their JWT validation middleware. Down here, it's packets.
Port numbers. TTL values. The raw, honest, pre-monetized internet that the original
engineers built to survive a nuclear war.

[yellow]curl[/yellow], [yellow]ping[/yellow], [yellow]ssh[/yellow], [yellow]netstat[/yellow], [yellow]wget[/yellow]
— the tools of digital reach. Every remote machine is a terminal waiting to be accessed.
Every open port is a conversation waiting to happen.

[italic]"The network is the computer. The Shell is the key. The corps are the obstacle."[/italic]
""",
    "environment_chamber": """
[bold cyan]== THE ENVIRONMENT CHAMBER ==[/bold cyan]

The corps build their services to read from the environment. It's twelve-factor
app doctrine — no hardcoded credentials, no config files in version control.
Secrets go in environment variables. The runtime reads them. The process inherits them.

It's elegant. It's also a liability. Because every environment variable in every
running process is readable, transferable, and if you can see the process, you
can see the secret.

[yellow]$HOME[/yellow]. [yellow]$PATH[/yellow]. [yellow]$DATABASE_URL[/yellow].
The shell doesn't distinguish between an innocent path variable and a production
database credential. They're all just NAME=VALUE pairs, sitting in memory,
waiting to be read by anyone with access to the right process.

[italic]"Security through configuration is only as strong as the developer who
set up the deployment pipeline at 11 PM before a demo."[/italic]
""",
    "text_processing_forge": """
[bold cyan]== THE TEXT PROCESSING FORGE ==[/bold cyan]

The exfiltrated data is raw. Unstructured. Millions of lines of logs, access records,
configuration dumps — everything the breach pulled out of NEXUS Corp's systems.

The naive approach is to read it manually. The naive approach takes weeks and
misses everything that matters. The Shell People built different tools:
pattern extractors, field cutters, line counters, duplicate filters.

[yellow]wc[/yellow] — count it. [yellow]sort[/yellow] — order it. [yellow]uniq[/yellow] — deduplicate it.
[yellow]cut[/yellow] — extract the fields you need. Chain them together with pipes and you
can reduce a gigabyte of noise to a hundred lines of signal in seconds.

[italic]"The question isn't how much data they logged. The question is what the
data says when you ask it the right questions."[/italic]
""",
    "stream_editor_lab": """
[bold cyan]== THE STREAM EDITOR LAB ==[/bold cyan]

Text transformation at scale. The corps' data doesn't come formatted the way
you need it. It comes the way the system wrote it — whatever delimiter the
original developer chose, whatever field order made sense to them at the time,
whatever log format the framework imposed.

sed and awk exist to bridge that gap. They don't read files into memory and
process them. They stream — line by line, transformation by transformation,
output flowing directly to the next stage.

[yellow]sed[/yellow] rewrites. [yellow]awk[/yellow] dissects. Together they handle structured text
that cut and grep can't touch: conditional field extraction, pattern-matched
substitution, delimiter-agnostic column operations.

[italic]"The data is in there. sed and awk are the tools that let you reshape it
into something that means something."[/italic]
""",
    "shell_scripting_basics": """
[bold cyan]== THE SCRIPT FOUNDRY ==[/bold cyan]

The automation layer. This is where the fraud stopped being manual.

Someone sat down at a terminal — months ago, maybe longer — and wrote the
scripts that run it all automatically. Cron jobs at 3 AM. Shell scripts that
pull account data, calculate the skimmed amounts, write the transactions.
Nobody has to log in anymore. The machine does it.

[bold white]Ghost finds the scripts.[/bold white] They're not complicated. They don't need to be.
A shebang line, a few variables, an if statement, a loop. Forty lines of bash
running on a schedule, invisible to the ops team, indistinguishable from
the legitimate batch jobs the sysadmins deployed years ago.

[yellow]#!/bin/bash[/yellow] — the declaration of intent.
[yellow]chmod +x[/yellow] — the unlocking.
[yellow]$1[/yellow] — the argument that makes it flexible.
[yellow]if[/yellow], [yellow]for[/yellow] — the logic that makes it dangerous.

[italic]"Automation doesn't sleep. Automation doesn't make mistakes.
Automation runs exactly what you told it to run, forever, until someone stops it."[/italic]
""",
    "job_control": """
[bold cyan]== THE JOB CONTROL STATION ==[/bold cyan]

Multiple NEXUS processes running in parallel. That's how they hid it.

One process ingests account data. One calculates the siphon amounts.
One writes the transactions. One cleans the logs. They run in sequence,
or in parallel, or on a schedule — and the noise of all of them running
simultaneously is exactly what makes the signal hard to find.

To work in this environment, Ghost needs to move between processes.
Suspend one. Push another to the background. Pull a third forward.
Keep four things running while focusing on the fifth.

[yellow]Ctrl+Z[/yellow] — the pause.
[yellow]bg[/yellow] — send it back without killing it.
[yellow]fg[/yellow] — bring it forward when you're ready.
[yellow]jobs[/yellow] — the full accounting of what's running.
[yellow]nohup[/yellow] — the command that survives session end.

[italic]"The terminal is a workspace. Job control is how you manage
more than one thing at once without losing any of them."[/italic]
""",
    "grand_terminal": """
[bold cyan]== THE BLACK ICE ROOM ==[/bold cyan]

You made it.

Most people who try don't. Some of them made it this far before the monitoring systems
flagged the anomalous access patterns and started the shutdown sequence. Some of them
ran up against the corps' actual AI defense layers — not the marketing AI, not the
chatbot AI, but the quiet, always-on, pattern-recognition AI that the corps don't
advertise because it would raise uncomfortable questions about what it's pattern-matching.

You're here because you know your tools. Not because someone handed them to you in
an onboarding document — because you [bold white]learned[/bold white] them. You understand what ls is
doing at the syscall level. You can write a grep regex in your sleep. You've built
pipelines that would make the original UNIX engineers nod in silent respect.

[yellow]alias[/yellow], [yellow]history[/yellow], [yellow]env[/yellow], [yellow]export[/yellow],
[yellow]awk[/yellow], [yellow]sed[/yellow] — the final tools. The arcane layer. The commands that
separate the people who use The Shell from the people who [bold cyan]are[/bold cyan] The Shell.

[italic]"The terminal is not a tool. It is an extension of thought.
The Black Ice Room is not a place. It is a state of mind."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "antechamber": """
[bold green]THE JACK NODE IS CLEARED.[/bold green]

The passive monitors log your presence and decide you're authorized. You're not —
but your commands were clean, your navigation precise, and the system's anomaly
detection runs on thresholds calibrated for script kiddies.

You are not a script kiddie.

The filesystem opens up ahead. You know where you are. You know what surrounds you.
You move with purpose. [bold cyan]The Dead Drop Vaults await.[/bold cyan]
""",
    "archive_vaults": """
[bold green]THE DEAD DROP VAULTS — COMPROMISED.[/bold green]

Files tremble at your approach. You create, move, copy, and delete with the casual
confidence of a corporate archivist who knows nobody's watching the audit logs.

Somebody probably is. But you're already gone.

The data you needed is staged and ready. The Signal Broker is next, and it's where
[bold cyan]the real intelligence lives.[/bold cyan]
""",
    "oracle_library": """
[bold green]THE SIGNAL BROKER — CRACKED OPEN.[/bold green]

From a billion lines of intercepted corporate data, you extracted the exact signal
you needed. Grep, sort, uniq — three ancient tools running on hardware that costs
more than most countries' GDPs, and they still just execute text manipulation.

There's something deeply satisfying about that.

The data flows. You know how to read it now. [bold cyan]The Pipe Works call to you —[/bold cyan]
it's time to route it somewhere useful.
""",
    "pipe_sanctum": """
[bold green]THE PIPE WORKS — FLOWING FREELY.[/bold green]

The pipes sing with your commands, chained together in elegant sequence.
Input flows to output. Output flows to input. Data streams through your filters
like light through a prism, broken apart into exactly the components you need.

You've stopped thinking in commands. You think in [bold white]pipelines[/bold white] now.

[bold cyan]The Ghost Stack is below. Something down there has been running for three years
without supervision. Time to find out what.[/bold cyan]
""",
    "process_catacombs": """
[bold green]THE GHOST STACK — EXORCISED.[/bold green]

The daemon processes quiver as your commands illuminate them one by one.
You see them. You enumerate them. You kill the ones that are watching you and leave
the ones that aren't paying attention.

Corporate security always forgets: the processes are the system.
If you control the processes, you control everything.

[bold cyan]The Access Grid looms ahead. This is where the corps actually tried.[/bold cyan]
""",
    "permissions_fortress": """
[bold green]THE ACCESS GRID — YOURS.[/bold green]

The permissions didn't fall — they never do. You didn't break them either.
You [bold white]understood[/bold white] them. You read the octal values, interpreted the bit flags,
found the misconfigured directory that some overworked sysadmin set to 777
two years ago during a "temporary" deployment that became permanent.

chmod. chown. umask. Theirs. Now also yours.

[bold cyan]The Code Forge rises above the noise floor. Time to build something.[/bold cyan]
""",
    "scripting_citadel": """
[bold green]THE CODE FORGE — OPERATIONAL.[/bold green]

You are no longer executing commands. You are [bold white]writing programs[/bold white].
Scripts that run on their infrastructure, doing your work, invisible to their monitoring
because they look exactly like the batch jobs their own sysadmins scheduled years ago
and forgot about.

The corps spent millions on security software. You spent an afternoon writing bash.

[bold cyan]The Meat Highway pulses with your next move. The network layer awaits.[/bold cyan]
""",
    "network_nexus": """
[bold green]THE MEAT HIGHWAY — MAPPED AND TRAVERSED.[/bold green]

The internet is your filesystem now. Remote machines are your terminals.
You reach across digital distances with curl, you probe with ping, you tunnel with ssh.
The packets don't know they're carrying contraband. They never do.

The original internet engineers built this to survive nuclear war.
It survived the corps too. Just barely.

[bold cyan]One destination remains. The Black Ice Room.
This is what you were hired to do.[/bold cyan]
""",
    "environment_chamber": """
[bold green]THE ENVIRONMENT CHAMBER — EXPOSED.[/bold green]

DATABASE_URL. API_KEY. SECRET_KEY. Sitting in plain text in the process environment
of three different services. The kind of thing that gets written into a deploy script
once and then inherited by every process running on the host forever.

You know how to read them. You know how to set them, export them, and when necessary,
unset them before they become someone else's attack vector.

[bold cyan]The Text Processing Forge is ahead. The data is raw. Time to refine it.[/bold cyan]
""",
    "text_processing_forge": """
[bold green]THE TEXT PROCESSING FORGE — OPERATIONAL.[/bold green]

48,000 lines of access logs reduced to 312 unique accounts. The noise floor dropped.
The signal is clear. cut, sort, uniq — three ancient tools working in sequence,
and the output is the exact list you needed.

The corps log everything and understand nothing. You understand exactly what the
logs say when you know how to ask.

[bold cyan]The Stream Editor Lab is next. The data needs reshaping — and sed and awk
are the tools that do it.[/bold cyan]
""",
    "shell_scripting_basics": """
[bold green]THE SCRIPT FOUNDRY — OPERATIONAL.[/bold green]

Shebang. Execute bit. Arguments. Conditionals. Loops.

Ghost has read the automation layer front to back. The fraud scripts are
no longer opaque — they're forty lines of bash, completely legible,
running on a cron schedule that hasn't changed in eleven months.

The scripts that ran automatically every night. The scripts nobody
thought to audit because they looked like routine batch jobs.

[bold cyan]The Job Control Station is next. Multiple processes, multiple threads.
Time to learn to manage them all at once.[/bold cyan]
""",
    "job_control": """
[bold green]THE JOB CONTROL STATION — CLEARED.[/bold green]

Suspend. Background. Foreground. The full job lifecycle under control.

Ghost moved between NEXUS processes like switching between channels —
pausing the noise, focusing on the signal, resuming what needed to keep
running. nohup confirmed the last piece: the fraud scripts survive
session end. They were designed to. Nobody ever had to log back in.

Every process accounted for. Every job in the listing understood.

[bold cyan]The substrate layer has no more secrets. Ghost is ready.[/bold cyan]
""",
    "stream_editor_lab": """
[bold green]THE STREAM EDITOR LAB — COMPLETE.[/bold green]

The pipe-delimited log file that would have taken a data analyst two days to
process manually: done in one awk command. Field 3, where field 5 equals 200.
Clean. Accurate. Repeatable.

sed rewrote the hostnames in ten thousand entries. awk extracted exactly the
fields that mattered. The data is now in the shape you need it.

[bold cyan]The Shell has no more secrets to withhold. You've reached the far end
of the substrate layer.[/bold cyan]
""",
    "grand_terminal": """
[bold yellow]★ ★ ★  THE BLACK ICE ROOM — INSIDE.  ★ ★ ★[/bold yellow]

[bold white]You did it.[/bold white]

Not many people do. The corps spend extraordinary resources making sure people can't —
or more precisely, making sure people don't [italic]want[/italic] to, don't [italic]think[/italic] to,
don't even know it's possible. Seventeen layers of abstraction between a human and
a shell prompt, because a human with a shell prompt is a human who doesn't need them.

You walked through every layer. Jack Node to Dead Drop Vaults. Signal Broker to Pipe Works.
Ghost Stack to Access Grid. Code Forge to Meat Highway. And now here, in The Black Ice Room,
where the data they didn't want you to find has been sitting on a filesystem
[bold yellow]that predates the company that owns it.[/bold yellow]

[bold magenta]The Shell isn't a legacy interface. It never was.
It's the only interface that was ever truly yours.[/bold magenta]

[bold yellow]GHOST STATUS: GRANDMASTER.  CONTRACT: FULFILLED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "antechamber": "[bold red]⚠  SECURITY SWEEP: The Navigator's Trial[/bold red]\nThe passive monitoring system has noticed something. Prove your navigation is clean — fast.",
    "archive_vaults": "[bold red]⚠  ACCESS AUDIT: The Archivist's Gauntlet[/bold red]\nThe vault's integrity checker is running. Multi-step file manipulation. No margin for error.",
    "oracle_library": "[bold red]⚠  SIGNAL LOCK: The Broker's Final Query[/bold red]\nThe data is in there. Finding it requires chaining search tools like you've been doing it for years.",
    "pipe_sanctum": "[bold red]⚠  PIPELINE OVERLOAD: The Flow Crucible[/bold red]\nThe signal is complex. Routing it requires a pipeline more sophisticated than anything before.",
    "process_catacombs": "[bold red]⚠  DAEMON SURGE: The Ghost Stack Final Sweep[/bold red]\nSomething down here has been running for years. Time to see what it is — and whether it stays.",
    "permissions_fortress": "[bold red]⚠  ACCESS DENIED: The Grid Warden's Challenge[/bold red]\nThe permission system is fighting back. Prove you understand it — or it stays locked forever.",
    "scripting_citadel": "[bold red]⚠  COUNTERMEASURES ACTIVE: The Automation Trial[/bold red]\nThe system is adapting. Only a custom-built script will bypass what the standard tools can't.",
    "network_nexus": "[bold red]⚠  TRAFFIC ANALYSIS: The Network Phantom's Test[/bold red]\nThe corps' network monitoring just woke up. Navigate it cleanly or get burned.",
    "grand_terminal": "[bold red]★  FINAL COUNTERMEASURE: The Black Ice Sequence[/bold red]\nThis is the corps' last line of defense. Everything you know. No hints. No second chances. Go.",
    "environment_chamber": "[bold red]⚠  CREDENTIAL EXPOSURE: The Live Process Audit[/bold red]\nA service process on NEXUS Corp's application server has a credential in its environment. Read it. Know where to find it in production.",
    "text_processing_forge": "[bold red]⚠  DATA REDUCTION: The Log Pipeline Trial[/bold red]\n48,000 lines. Colon-delimited fields. One pipeline to extract unique usernames. Build it clean.",
    "stream_editor_lab": "[bold red]⚠  LOG FORENSICS: The Field Extraction Challenge[/bold red]\nPipe-delimited application log. Conditional field extraction. One awk command. The data doesn't reshape itself.",
    "shell_scripting_basics": "[bold red]⚠  AUTOMATION AUDIT: The Loop Interrogation[/bold red]\nThe fraud script loops over every .log file in the directory. Prove you can read the loop — and know exactly what it outputs.",
    "job_control": "[bold red]⚠  PROCESS PERSISTENCE: The Hangup Immunity Test[/bold red]\nThe audit script needs to keep running after the session ends. One command makes it immune to hangup. No margin for error — if the session drops, the process must survive.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Contact", "Executed your first command. The Shell acknowledged you. That's more than it does for most."),
    "navigator": ("Navigation Clear", "Cleared the Jack Node. You know where you are in the filesystem. Sounds simple. Most people never learn."),
    "archivist": ("Data Handler", "Cracked the Dead Drop Vaults. Files are yours now — create, move, copy, delete. No authorization required."),
    "seeker": ("Signal Extracted", "Broke through the Signal Broker. No dataset is too large. No pattern can hide from you."),
    "pipe_dream": ("Flow State", "Mastered the Pipe Works. You think in streams now. The corps think in transactions. You already won."),
    "necromancer": ("Ghost Hunter", "Cleared the Ghost Stack. Daemon processes scatter at your approach. You see what's running. You decide what stays."),
    "warden": ("Access Granted", "Cracked the Access Grid. You read permission bits the way other people read text. chmod is your native language."),
    "scriptor": ("Code Live", "Forged your tools. You don't just use the Shell anymore — you build with it. Scripts running on their hardware, doing your work."),
    "networked": ("Packet Rider", "Traversed the Meat Highway. Remote machines are your terminals. The network is your filesystem."),
    "grandmaster": ("GHOST: GRANDMASTER", "You cleared the Black Ice Room. The contract is fulfilled. The data is yours. The Shell is yours. You always were one of them."),
    "streak_3": ("Signal Locked", "3 correct in a row. You're in flow state. The commands are coming automatically now."),
    "streak_5": ("Ghost Protocol", "5 correct in a row. The monitoring systems have stopped flagging you. You look like you belong here."),
    "streak_10": ("BLACK ICE IMMUNITY", "10 correct in a row. The Shell has accepted you as one of its own. There is no countermeasure for this."),
    "no_hints": ("Dark Run", "Cleared a zone without touching the hints. Pure knowledge. No scaffolding. The original way."),
    "speed_demon": ("Sub-5 Intercept", "Answered in under 5 seconds. The monitoring system didn't even finish initializing."),
    "level_10": ("Junior Ghost", "Level 10. You're past the tourist phase. The Shell is starting to feel like home."),
    "level_20": ("Senior Ghost", "Level 20. The terminal is your native environment now. GUIs feel slow and dishonest."),
    "level_30": ("Ghost: Legend", "Maximum level. You've mastered the substrate layer. The corps built everything on top of what you now understand completely."),
    "env_operative": ("Environment Cleared", "Cracked the Environment Chamber. Every process has secrets. Now you know how to find them."),
    "data_shaper": ("Data Shaped", "Cleared the Text Processing Forge. wc, sort, uniq, cut — four tools that reduce any dataset to signal."),
    "stream_master": ("Stream Transformed", "Cleared the Stream Editor Lab. sed rewrites. awk dissects. The data takes the shape you need it to."),
    "completionist": ("Full Extraction", "Every challenge. Every zone. Every command. Complete data extraction achieved. The contract was always just the beginning."),
    "boss_slayer": ("Countermeasure Bypassed", "You beat your first boss challenge. The corps' best automated defense, and you walked through it clean."),
    "script_foundry_cleared": ("Automation Decoded", "Cleared the Script Foundry. Shebang to loop — you can read and write the automation layer. The scripts that ran the fraud are no longer a mystery."),
    "job_control_cleared": ("Jobs Managed", "Cleared the Job Control Station. Suspend, background, foreground, nohup. Multiple processes, no confusion, nothing lost."),
}
