"""
story.py - Narrative text for Python Ops
"""

INTRO_STORY = """
The database queries returned clean.

Four hundred and seventeen phantom transactions. Eleven years of systematic fraud.
Every disbursement timestamped, every phantom vendor cross-referenced, the subsidiary
structure laid out in relational rows as clear as a confession.

But the congressional investigators looked at your Postgres export and asked the question
you'd been dreading: [bold white]"How did the numbers stay under the audit threshold every time?"[/bold white]

Not human calculation. Not luck. Not coincidence.

[bold red]Automation.[/bold red]

Somewhere in NEXUS's infrastructure, a set of Python scripts had been running for years —
calculating the exact percentage to bill on each contract, staying three percent below the
federal threshold that would trigger a mandatory audit review. Generating the fake invoices.
Populating the phantom vendor records. Producing the quarterly reports that went to the
oversight committee looking exactly right.

You found the scripts in [yellow]/opt/nexus/automation/[/yellow].
A trading bot. A data scraper. A report generator. Clean, well-commented code.
Written by someone who knew exactly what they were doing.

[bold magenta]You are Ghost.[/bold magenta] You've been inside the terminal. You've read the git history.
You've mapped the container infrastructure. You've run the database queries.
Now you need to read, analyze, and understand the code that orchestrated all of it.

Python is not just the corps' weapon. It's yours now.

[bold cyan]The scripts are open. The cursor is blinking. Begin.[/bold cyan]
"""

ZONE_INTROS = {
    "python_basics": """
[bold cyan]== THE SYNTAX LAYER ==[/bold cyan]

The first script is forty lines. Clean. No obfuscation, no clever tricks —
whoever wrote this was confident it would never be read by an adversary.

They were wrong.

Python's surface looks simple. [yellow]print()[/yellow] to output. Variables to store.
[yellow]str[/yellow], [yellow]int[/yellow], [yellow]float[/yellow], [yellow]bool[/yellow] — four primitive types that the
entire script structure is built on. The fraud wasn't sophisticated.
It was just consistent. Consistent and automated.

[italic]"The most dangerous script is the one that looks boring."[/italic]

Learn to read the foundation first. Every line of the automation code
starts with these building blocks.
""",

    "control_flow": """
[bold cyan]== THE DECISION ENGINE ==[/bold cyan]

Line 47 of [yellow]billing_calc.py[/yellow]. The heart of it.

An [yellow]if[/yellow] statement. A comparison. A threshold value hardcoded to
[bold red]0.03[/bold red] below the federal audit trigger. Every contract processed
through this gate. If the calculated amount would exceed the threshold,
the script adjusts — silently, automatically, invisibly.

That [yellow]if[/yellow] statement ran eleven years without a human ever looking at it.

[yellow]for[/yellow] loops over vendor lists. [yellow]while[/yellow] loops polling transaction queues.
[yellow]break[/yellow] when a condition is met. [yellow]continue[/yellow] to skip non-target records.
Flow control is how the script navigated the data without getting caught.

[italic]"The corp's fraud ran on conditionals. So does every piece of code that matters."[/italic]
""",

    "functions_lab": """
[bold cyan]== THE FUNCTION ARCHIVE ==[/bold cyan]

The automation suite is modular. Not for elegance — for [bold white]deniability[/bold white].

Each function does one thing. [yellow]calculate_threshold()[/yellow]. [yellow]generate_invoice()[/yellow].
[yellow]submit_vendor_record()[/yellow]. Functions called from other functions,
abstracted three layers deep so that any single piece of code looks harmless.

The author knew Python. [yellow]def[/yellow], [yellow]return[/yellow], [yellow]*args[/yellow], [yellow]**kwargs[/yellow]
— the toolkit of someone who had been writing Python for years.
Lambda expressions for the inline transforms. Default arguments to
handle edge cases without conditional branching.

Read the functions. Understand what each one does. Map the call chain.

[italic]"Functions are the architecture. Follow the calls and you find the design."[/italic]
""",

    "data_structures": """
[bold cyan]== THE DATA VAULT ==[/bold cyan]

The scraper is more complex. It pulls vendor data, transaction records,
and contract amounts from three different internal APIs and holds them
in memory while it calculates the fraud amounts.

[yellow]Lists[/yellow] of transaction IDs. [yellow]Dicts[/yellow] mapping vendor names to subsidiary codes.
[yellow]Tuples[/yellow] as immutable record keys. [yellow]Sets[/yellow] for deduplication — making sure
the same phantom vendor doesn't appear twice in the same report.

The data structure design is actually elegant. Whoever wrote this understood
Python's collection types and used each one for exactly what it's good at.
Which makes it easier to understand — and easier to prove in court.

[italic]"The data structure reveals the data model. The data model reveals the intent."[/italic]
""",

    "file_operations": """
[bold cyan]== THE FILE FORGE ==[/bold cyan]

The report generator writes files. Lots of files.

Monthly PDFs for the oversight committee. CSV exports for the accounting
system. JSON payloads for the API that feeds the federal reporting dashboard.
Every file crafted to look like legitimate output from a legitimate system.

[yellow]open()[/yellow]. [yellow]with[/yellow]. [yellow]read()[/yellow], [yellow]write()[/yellow].
[yellow]pathlib.Path[/yellow] for navigating the output directory structure.
The script handles its own file management — creating, writing, and archiving
evidence of its own operation. The irony is noted.

[italic]"The best evidence of what a script does is the files it leaves behind."[/italic]
""",

    "string_ops": """
[bold cyan]== THE STRING SUITE ==[/bold cyan]

The fraud data doesn't stay in memory. It gets formatted, serialized,
and embedded in strings — vendor names padded to fixed widths,
amounts formatted to exactly two decimal places, dates massaged into
whatever format the target system expects.

[yellow].split()[/yellow] to parse incoming API responses. [yellow].join()[/yellow] to build CSV rows.
[yellow]f-strings[/yellow] to embed calculated values in report templates.
[yellow].strip()[/yellow] to clean whitespace from vendor names before comparison.
[yellow].replace()[/yellow] to sanitize the subsidiary codes that shouldn't appear in reports.

String manipulation is how the automation turned raw data into
documents that passed human review for eleven years.

[italic]"A well-formatted lie is harder to see than a sloppy truth."[/italic]
""",

    "modules_arsenal": """
[bold cyan]== THE MODULES ARSENAL ==[/bold cyan]

The automation suite doesn't reinvent wheels. It imports them.

[yellow]import os[/yellow] for filesystem navigation — finding the right output directories,
checking that files exist before writing. [yellow]import sys[/yellow] for exit codes that
make the cron job logs look clean. [yellow]import json[/yellow] for parsing the API
responses that feed the calculation engine. [yellow]import datetime[/yellow] for
timestamps — making sure every generated document has a plausible creation date.

Standard library. No exotic dependencies. Nothing to flag in a package audit.
The entire fraud infrastructure runs on Python's built-in modules.

[italic]"The standard library is the most trusted code on any machine.
That's exactly why it's the perfect cover."[/italic]
""",

    "error_handling": """
[bold cyan]== THE EXCEPTION VAULT ==[/bold cyan]

The final piece. The part that kept the system running for eleven years
without a single crash that would have generated an alert.

[yellow]try/except/finally[/yellow]. Every network call wrapped. Every file operation
guarded. Every API response validated. The script catches [yellow]ConnectionError[/yellow]
and retries. It catches [yellow]ValueError[/yellow] from malformed data and logs it silently.
It catches [yellow]FileNotFoundError[/yellow] and creates the missing directory.

Nothing crashes. Nothing alerts. Nothing surfaces to human review.
The error handling is the invisibility cloak.

To prove the fraud, you need to understand what the error handling hid —
and where it logged the exceptions it caught.

[italic]"Perfect error handling means every failure is silent.
Follow the silence to find the crime."[/italic]
""",

    "file_io_deep": """
[bold cyan]== THE FILE I/O LAB ==[/bold cyan]

You've seen what the scripts wrote. Now you need to understand exactly [bold white]how[/bold white].

[yellow]open()[/yellow] with a mode flag. [yellow]'r'[/yellow] for reading the raw API cache files.
[yellow]'w'[/yellow] for writing the falsified quarterly reports. [yellow]'a'[/yellow] for appending
to the log file that grew silently for eleven years.

[yellow]with[/yellow] statements everywhere. Not for cleanliness — for reliability.
The script couldn't afford a leaked file handle crashing on a government server.
Context managers guaranteed the file closed even if the write failed mid-operation.

The evidence is already there in the file system. You just need to
understand the I/O layer well enough to trace exactly what was written and when.

[italic]"Files don't lie. They can be deleted, but deletion leaves traces too."[/italic]
""",

    "list_comprehensions": """
[bold cyan]== THE COMPREHENSION ENGINE ==[/bold cyan]

The data transformation layer. This is where raw vendor records became
filtered, reformatted, ready-to-inject fraud payloads.

Not with loops and [yellow]append()[/yellow]. With one-liners. Clean. Fast. Hard to audit.

[yellow][vendor['id'] for vendor in raw_data if vendor['subsidiary'] in SHELL_LIST][/yellow]

One line. Filtered. Extracted. The congressional investigators saw it and
thought it was normal data processing. Which it was — applied to fraud data.

List comprehensions, dict comprehensions, generator expressions.
The automation suite used all three. Learn to read them.

[italic]"The most dangerous code looks boring. A list comprehension is just boring enough."[/italic]
""",

    "requests_http": """
[bold cyan]== THE HTTP RECON MODULE ==[/bold cyan]

The scraper didn't read local files. It [bold white]pulled data from internal APIs[/bold white].

[yellow]requests.get()[/yellow] to fetch vendor registries. [yellow]requests.post()[/yellow] to inject
phantom records into the accounting system. [yellow].json()[/yellow] to parse every
response. [yellow].status_code[/yellow] to confirm each operation succeeded silently.

Three internal endpoints. Authenticated. Rate-limited. Logged on the server side —
but the server-side logs were controlled by the same team running the fraud.

[yellow]requests.Session()[/yellow] maintained the authentication token across hundreds
of API calls per nightly run. No re-authentication. No extra log entries.

The network traffic looked like normal internal tooling. Because it was
normal tooling — pointed at fraud targets.

[italic]"Every HTTP request leaves a trace. Find the server logs they didn't control."[/italic]
""",
    "classes_and_oop": """
[bold red]OBJECT MODEL ANALYSIS[/bold red]

The fraud system's Python codebase uses classes. Heavily. The `Evidence` base class.
The `FraudTransaction` subclass. The `Packager` class with a `from_config()` classmethod
that reads a JSON config — and routes evidence to the attacker's endpoint.

[yellow]@dataclass[/yellow] reduced their boilerplate. [yellow]inheritance[/yellow] let them build
a hierarchy of data types that all serialize to the same format. [yellow]__str__[/yellow]
printed clean log lines that looked like normal system output.

[italic]"Good OOP design is powerful. Including in the wrong hands."[/italic]
""",
    "subprocess_and_os": """
[bold red]SHELL INTERFACE[/bold red]

The evidence packager's final step: Python shells out to tar, gpg, and rsync.
No Python libraries — just subprocess calls to system commands that leave
fewer Python-traceable fingerprints.

[yellow]subprocess.run()[/yellow] with [yellow]capture_output=True[/yellow] captured output for logging.
[yellow]os.environ.get()[/yellow] read the encryption key and destination server from
environment variables — meaning the config could be changed without touching code.
[yellow]pathlib.Path.glob()[/yellow] collected the evidence files to pack.

[italic]"Python is a shell. The shell is Python. The boundary was always arbitrary."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "python_basics": """
[bold green]THE SYNTAX LAYER — ANALYZED.[/bold green]

The primitive types map cleanly to the fraud structure.
Strings for vendor names. Integers for transaction IDs.
Floats for the amounts — always calculated to avoid the audit threshold.
Booleans for the flags that should have been logged to a human but weren't.

You understand the foundation. [bold cyan]The decision engine is next.[/bold cyan]
""",

    "control_flow": """
[bold green]THE DECISION ENGINE — MAPPED.[/bold green]

The threshold check is documented. You found the if statement,
traced the condition, and identified the hardcoded value.

Eleven years of federal contracts filtered through a single
comparison operator. The brevity of it is almost impressive.

[bold cyan]The Function Archive holds the next layer — the modular structure
that made this deniable.[/bold cyan]
""",

    "functions_lab": """
[bold green]THE FUNCTION ARCHIVE — REVERSE ENGINEERED.[/bold green]

The call graph is complete. Every function mapped to its callers.
The chain from data ingestion to report output documented
in twelve pages of technical notes your handler will attach to the filing.

[bold cyan]The Data Vault holds the collection structures.
Understanding them is the next step.[/bold cyan]
""",

    "data_structures": """
[bold green]THE DATA VAULT — CRACKED.[/bold green]

The data model is documented. The dict that maps phantom vendor names
to their real subsidiary codes is the smoking gun — it exists nowhere
in any legitimate business record.

[bold cyan]The File Forge is next. Evidence of what the script wrote to disk.[/bold cyan]
""",

    "file_operations": """
[bold green]THE FILE FORGE — UNDERSTOOD.[/bold green]

The output structure is mapped. Forty-seven directories.
Thousands of generated files, each one a formatted record of fraud.
The pathlib navigation code left breadcrumbs to every archive location.

[bold cyan]The String Suite holds the formatting logic.
How the data became convincing documents.[/bold cyan]
""",

    "string_ops": """
[bold green]THE STRING SUITE — DECODED.[/bold green]

The formatting patterns are documented. The f-string templates.
The replace() calls that sanitized the subsidiary codes.
The split() patterns that parsed the API responses.

[bold cyan]The Modules Arsenal is next — the standard library imports
that gave the script its reach.[/bold cyan]
""",

    "modules_arsenal": """
[bold green]THE MODULES ARSENAL — INVENTORIED.[/bold green]

Every import accounted for. os, sys, json, datetime —
each one mapped to its role in the operation.

The import list reads like a mission briefing. Each module
a tool. Each tool used with precision.

[bold cyan]The Exception Vault is the last layer.
The silence that protected the operation for eleven years.[/bold cyan]
""",

    "error_handling": """
[bold yellow]★ ★ ★  THE EXCEPTION VAULT — BREACHED.  ★ ★ ★[/bold yellow]

[bold white]Complete.[/bold white]

The error handling logs that were supposed to be silent weren't.
They were rotated, but rotation doesn't mean deletion — and you found
the archived logs three directories below the expected location.

Every caught exception. Every silent retry. Every suppressed failure.
Timestamped. Documented. Attached to the evidence package.

The automation suite is fully analyzed. The code that ran the fraud
is now the code that proves it.

[bold magenta]Ghost Operative — Python certified. Evidence complete.[/bold magenta]
""",

    "file_io_deep": """
[bold green]THE FILE I/O LAB — UNDERSTOOD.[/bold green]

The I/O layer is documented. [yellow]open()[/yellow] calls mapped. Modes catalogued.
[yellow]with[/yellow] statements confirmed to match the file creation timestamps
in the audit trail.

The [yellow]'a'[/yellow] mode log file is the clearest record — every append
timestamped by the OS. Eleven years of nightly additions.
One line per fraudulent transaction. Four hundred and seventeen of them.

[bold cyan]The Comprehension Engine holds the transformation logic — how the raw data
was reshaped before hitting the file system.[/bold cyan]
""",

    "list_comprehensions": """
[bold green]THE COMPREHENSION ENGINE — DECODED.[/bold green]

The transformation patterns are documented. The filter comprehension.
The dict comprehension that mapped vendor IDs to shell company names.
The generator that streamed transaction records without loading them all into memory.

Compact syntax. Clean execution. Every line doing exactly what it was
designed to do — which is exactly what makes it damning.

[bold cyan]The HTTP Recon Module is next. How the automation reached the APIs
that fed it all this data.[/bold cyan]
""",

    "requests_http": """
[bold yellow]HTTP RECON MODULE — COMPLETE.[/bold yellow]

The API layer is fully mapped. Three internal endpoints. Forty-seven nightly sessions.
Every [yellow]requests.get()[/yellow] documented. Every [yellow].json()[/yellow] response correlated.

The Session token is in the decompiled memory dump.

[bold cyan]The object model is next — how the fraud system organized its data.[/bold cyan]
""",

    "classes_and_oop": """
[bold green]OBJECT MODEL REVERSED.[/bold green]

The inheritance hierarchy reconstructed. [yellow]@dataclass[/yellow] fields mapped.
[yellow]__str__[/yellow] output compared to log files — exact match. The `from_config()` [yellow]@classmethod[/yellow]
confirmed: it reads the same JSON config structure found in the container environment.

The fraud system's Python code was well-engineered. Whoever wrote it knew OOP.

[bold cyan]The shell interface is next — how the packager talks to the OS.[/bold cyan]
""",

    "subprocess_and_os": """
[bold yellow]★ ★ ★  AUTOMATION SUITE — FULLY MAPPED.  ★ ★ ★[/bold yellow]

[bold white]The complete evidence extraction pipeline is reconstructed.[/bold white]

[yellow]subprocess.run(['tar', 'czf', ...])[/yellow] — the archive creation.
[yellow]os.environ.get('NEXUS_KEY')[/yellow] — the encryption key, loaded at runtime.
[yellow]Path('/tmp/evidence').glob('*.sql')[/yellow] — all database dumps, collected.
[yellow]result.returncode[/yellow] — checked after every shell call.

From [yellow]open()[/yellow] to [yellow]requests.post()[/yellow] to [yellow]subprocess.run()[/yellow]:
the entire Python automation infrastructure is documented.

[bold magenta]Ghost Operative — Python modules cleared. Evidence package complete.[/bold magenta]
""",
}

BOSS_INTROS = {
    "python_basics": "[bold red]⚠  TYPE CHECK: The Coercion Protocol[/bold red]\nThe billing script reads vendor codes as strings from the API. Then operates on them as integers. One type conversion function bridges the gap — identify it.",
    "control_flow": "[bold red]⚠  LOOP ANALYSIS: The Skip Pattern[/bold red]\nThe scraper doesn't process every record. It skips certain entries mid-loop without exiting the loop entirely. What keyword controls this behavior?",
    "functions_lab": "[bold red]⚠  SCOPE BREACH: The Global State[/bold red]\nOne function modifies a module-level counter without passing it as an argument. To do this correctly in Python, it must declare something. What keyword?",
    "data_structures": "[bold red]⚠  COMPREHENSION AUDIT: The Filter Pass[/bold red]\nThe script builds a filtered list of flagged transactions in one line. No for loop. No append(). A single Python construct — identify it.",
    "file_operations": "[bold red]⚠  MEMORY SCAN: The Line Reader[/bold red]\nThe log file is 4 gigabytes. The script reads it without loading it into memory. What Python pattern makes this possible?",
    "string_ops": "[bold red]⚠  SANITIZE: The Replace Operation[/bold red]\nThe subsidiary codes contain underscores that shouldn't appear in the output reports. The script replaces them inline. Which string method handles this?",
    "modules_arsenal": "[bold red]⚠  RUNTIME INTERFACE: The Exit Vector[/bold red]\nThe automation script terminates with a specific exit code on failure so the cron monitoring reads it as success. Which module provides sys.exit()?",
    "error_handling": "[bold red]★  FINAL EXCEPTION: The Custom Error Class[/bold red]\nThe script defines its own exception type for authentication failures. To define a custom exception in Python, you subclass what built-in class?",
    "file_io_deep": "[bold red]⚠  FILE AUDIT: The Line Reader[/bold red]\nThe transaction archive is a 200MB text file. The script reads every line into a Python list for processing. What file method loads all lines into a list?",
    "list_comprehensions": "[bold red]⚠  COMPREHENSION GAUNTLET: The Efficiency Test[/bold red]\nThe investigator asks why the fraud author used list comprehensions instead of for-loops. Identify the primary advantage: conciseness alone, or something more?",
    "requests_http": "[bold red]⚠  SESSION BREACH: The Persistent Connection[/bold red]\nThe scraper authenticates once and reuses the session for hundreds of API calls. What requests object maintains cookies and headers across multiple requests?",
    "classes_and_oop": "[bold red]⚠  OOP FINAL: The Evidence System[/bold red]\nThe fraud data model uses a base class and subclasses. Design the cleanest Python class hierarchy for an Evidence system — base class + DatabaseRecord subclass. @dataclass, inheritance, __str__. Make it production-quality.",
    "subprocess_and_os": "[bold red]★  FINAL MISSION: The Evidence Packager[/bold red]\nAssemble the complete packager: read NEXUS_KEY from env, glob all .sql files in /tmp/evidence/, tar them with subprocess.run(), verify returncode is 0. Four operations. One mission. Show the complete Python.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "syntax_ghost": ("Syntax Clear", "Cleared the Python Foundation. Variables, types, and print() — the substrate of everything the fraud was built on."),
    "flow_operator": ("Flow Mapped", "Cleared the Decision Engine. Every if/elif/else. Every loop. Every break and continue. The fraud's logic is documented."),
    "function_forge": ("Functions Reversed", "Cracked the Function Archive. The call graph is complete. The deniability structure is exposed."),
    "vault_keeper": ("Data Structures Analyzed", "Breached the Data Vault. Lists, dicts, tuples, sets — every collection that held the fraud data is now evidence."),
    "file_phantom": ("Files Recovered", "Cleared the File Forge. Every generated document located and catalogued. The output structure is mapped."),
    "string_cutter": ("Strings Decoded", "Cleared the String Suite. The formatting patterns, the sanitization logic — all documented."),
    "module_runner": ("Modules Inventoried", "Cleared the Modules Arsenal. Every import understood. Every tool the script relied on catalogued."),
    "exception_master": ("Exceptions Surfaced", "Breached the Exception Vault. The silent failures are silent no longer. The error logs are in the evidence package."),
    "io_specialist": ("I/O Specialist", "Cleared the File I/O Lab. open(), with, read, write — every file operation in the fraud infrastructure is now understood."),
    "comprehension_ace": ("Comprehension Ace", "Decoded the Comprehension Engine. List, dict, generator — the one-liner transforms that reshaped raw data into fraud payloads."),
    "http_operative": ("HTTP Operative", "Cleared the HTTP Recon Module. Every API call mapped, every session token traced. The network layer of the fraud is documented."),
    "oop_architect": ("OOP Architect", "Mastered classes, inheritance, dunder methods, and @dataclass. The fraud system's object model is fully reverse-engineered."),
    "shell_commander": ("Shell Commander", "Cleared subprocess and os. Python talks to the OS. Every shell command, every env variable, every file — accessible from code."),
    "first_blood": ("First Script", "Executed your first Python challenge. The syntax layer acknowledged you."),
    "streak_3": ("Signal Locked", "3 correct in a row. The code patterns are becoming readable."),
    "streak_5": ("Ghost Protocol", "5 correct in a row. You think in Python now."),
    "streak_10": ("Script Master", "10 correct in a row. The automation suite holds no secrets from you."),
    "no_hints": ("Dark Run", "Cleared a zone without hints. Pure comprehension. No scaffolding."),
    "speed_demon": ("Sub-5 Parse", "Answered in under 5 seconds. The syntax is instinctive now."),
    "level_10": ("Junior Operative", "Level 10. Python is starting to feel like a first language."),
    "level_20": ("Senior Operative", "Level 20. You write Python before you think about it."),
    "level_30": ("Ghost: Specter", "Maximum level. The automation suite is fully understood. The evidence is complete."),
    "boss_slayer": ("Exception Bypassed", "Beat your first boss challenge. The hard cases don't slow you down."),
    "completionist": ("Full Script Analysis", "Every challenge. Every zone. The complete automation suite — analyzed, documented, attached to the filing."),
}
