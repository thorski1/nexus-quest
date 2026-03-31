"""
story.py — Narrative for the Shell Scripting (Script Forge) skill pack.
Theme: Automate everything. The shell is your superpower.
"""

INTRO_STORY = """
[bold cyan]NEXUS OPERATIVE — AUTOMATION LAYER ACCESS GRANTED[/bold cyan]

The first breach gave you access. The second gave you persistence.
But access without automation is tourism. You were inside their systems,
reading files, running commands, piping data — one command at a time,
like a surgeon operating with tweezers.

Then you found the [bold yellow]Script Forge[/bold yellow].

Deep in the infrastructure, below the CI/CD pipelines, below the orchestration
layer, below the dashboards the managers use to pretend they understand what's
running — there is a directory. [bold white]/opt/nexus/scripts/[/bold white].
Forty-seven shell scripts. Some run on cron. Some are triggered by webhooks.
Some haven't been touched in three years but run every night at 2 AM like
clockwork, moving data, rotating logs, backing up databases, deploying code.

The ops team doesn't write these anymore. They use Terraform now. They use
Ansible. They use whatever the conference speakers told them to use this year.
But the scripts are still running. The scripts were [bold white]always[/bold white] running.

[bold magenta]The shell script is the oldest automation tool in computing.
It predates every DevOps platform by decades. It will outlast them too.[/bold magenta]

A developer who can't write a shell script is a developer who depends on
someone else's tools for everything. A developer who [bold cyan]can[/bold cyan] write a shell script
can automate anything, on any Unix machine, with no dependencies, no package
manager, no runtime, no framework.

[bold white]Just bash. Just text. Just logic.[/bold white]

The Script Forge is where you stop being a user of the shell and start being
its [bold yellow]author[/bold yellow]. Variables, conditionals, loops, functions, pipes, traps,
argument parsing — the full grammar of automation.

[bold cyan]The cursor blinks. The shebang line is waiting. Write something dangerous.[/bold cyan]
"""

ZONE_INTROS = {
    "shebang_and_basics": (
        "[bold cyan]ZONE: THE SHEBANG LINE[/bold cyan]\n\n"
        "Every script starts with a declaration of intent. "
        "[bold yellow]#!/bin/bash — two characters and a path that tell the kernel "
        "exactly which interpreter runs this file. Without it, you're guessing. "
        "With it, you're commanding.[/bold yellow]\n\n"
        "Variables. Quoting. Command substitution. The atoms of shell scripting. "
        "Get these wrong and every script you write will break on filenames with spaces. "
        "Get them right and the language opens up."
    ),
    "conditionals": (
        "[bold cyan]ZONE: THE CONDITIONAL GATE[/bold cyan]\n\n"
        "The scripts in /opt/nexus/scripts/ are full of decisions. "
        "[bold yellow]If the backup succeeded, rotate the logs. If the disk is above 90%, "
        "alert. If the deploy target doesn't exist, create it. "
        "Every automation script is a decision tree.[/bold yellow]\n\n"
        "if, elif, else, fi. [[ ]] and test. File tests. String comparisons. "
        "Numeric comparisons. The conditional logic that makes a script intelligent "
        "instead of just sequential."
    ),
    "loops": (
        "[bold cyan]ZONE: THE LOOP CONSTRUCT[/bold cyan]\n\n"
        "The fraud scripts iterate. That's how they scale. "
        "[bold yellow]A for loop over every .csv file in the drop directory. "
        "A while loop reading the transaction ledger line by line. "
        "An until loop waiting for the remote server to respond.[/bold yellow]\n\n"
        "Loops are what separate a one-off command from a production automation. "
        "for, while, until, break, continue — the grammar of repetition."
    ),
    "functions": (
        "[bold cyan]ZONE: THE FUNCTION CORE[/bold cyan]\n\n"
        "The NEXUS scripts are modular. Fifty lines of main logic, but the real work "
        "happens in functions: [bold yellow]validate_input(), deploy_artifact(), "
        "rollback_release(), send_alert().[/bold yellow]\n\n"
        "Functions are how you write shell scripts that other humans can read. "
        "Local variables. Return values. Argument passing. "
        "The difference between a script and a program."
    ),
    "text_processing": (
        "[bold cyan]ZONE: THE TEXT PROCESSING FORGE[/bold cyan]\n\n"
        "The data is text. The logs are text. The configs are text. "
        "[bold yellow]grep finds it. sed transforms it. awk dissects it. "
        "cut, sort, uniq, wc, tr — the toolkit that turns raw text into answers.[/bold yellow]\n\n"
        "A shell script without text processing is a script that can't read its own output. "
        "Every real automation pipeline is 80% text manipulation."
    ),
    "input_output": (
        "[bold cyan]ZONE: THE I/O CHANNEL[/bold cyan]\n\n"
        "Three streams. That's all Unix gives you. "
        "[bold yellow]stdin (0), stdout (1), stderr (2). Every process inherits them. "
        "Every script controls them. Redirection is how you route data "
        "without writing a single line of code.[/bold yellow]\n\n"
        "read for input. > and >> for output. 2>&1 for merging streams. "
        "Here documents for inline data. Master I/O and the script breathes."
    ),
    "error_handling": (
        "[bold cyan]ZONE: THE ERROR TRAP[/bold cyan]\n\n"
        "The NEXUS deployment scripts have no error handling. That's how the breach persisted. "
        "[bold yellow]A failed deploy that silently continued. A backup script that returned 0 "
        "even when the tar command segfaulted. A cron job that has been failing every night "
        "for eight months and nobody noticed because nobody checked the exit code.[/bold yellow]\n\n"
        "set -euo pipefail. trap. Exit codes. The difference between "
        "a script that works and a script that fails safely."
    ),
    "real_scripts": (
        "[bold cyan]ZONE: THE DEPLOYMENT FORGE[/bold cyan]\n\n"
        "This is where it all comes together. "
        "[bold yellow]Log rotation. Backup scripts with dated archives. "
        "Deployment scripts with rollback. Cron scheduling. "
        "Argument parsing with getopts. Real scripts solving real problems.[/bold yellow]\n\n"
        "The NEXUS ops team outsourced their automation to a SaaS platform that costs "
        "$47,000 per year. Every feature it provides can be replaced by a 200-line "
        "shell script and a cron job. This is where you prove it."
    ),
}

ZONE_COMPLETIONS = {
    "shebang_and_basics": (
        "[bold green]THE SHEBANG LINE — DECODED.[/bold green]\n\n"
        "#!/bin/bash. echo. Variables with no spaces around the equals sign. "
        "Single quotes for literal strings. Double quotes for expansion. "
        "$(command) for substitution. The foundation is laid.\n\n"
        "[bold cyan]The Conditional Gate is next. Time to teach your scripts to think.[/bold cyan]"
    ),
    "conditionals": (
        "[bold green]THE CONDITIONAL GATE — OPEN.[/bold green]\n\n"
        "if, elif, else, fi. [[ -f ]], [[ -d ]], [[ -z ]]. "
        "-eq, -ne, -lt, -gt. The full decision toolkit. "
        "Your scripts no longer execute blindly — they evaluate, branch, and adapt.\n\n"
        "[bold cyan]The Loop Construct awaits. Repetition is power.[/bold cyan]"
    ),
    "loops": (
        "[bold green]THE LOOP CONSTRUCT — MASTERED.[/bold green]\n\n"
        "for, while, until. Glob iteration. Line-by-line file reading. "
        "C-style arithmetic loops. break and continue. "
        "A single loop replaced fourteen manual commands.\n\n"
        "[bold cyan]The Function Core is ahead. Modular code is readable code.[/bold cyan]"
    ),
    "functions": (
        "[bold green]THE FUNCTION CORE — ACTIVATED.[/bold green]\n\n"
        "Functions with local scope. Return values via echo and command substitution. "
        '"$@" preserving argument boundaries. The scripts are modular now — '
        "each function does one thing, testable in isolation.\n\n"
        "[bold cyan]The Text Processing Forge is next. Data doesn't reshape itself.[/bold cyan]"
    ),
    "text_processing": (
        "[bold green]THE TEXT PROCESSING FORGE — OPERATIONAL.[/bold green]\n\n"
        "grep found the signal. sed rewrote the patterns. awk extracted the fields. "
        "sort | uniq -c ranked the frequency. wc -l counted the evidence. "
        "Text in, answers out.\n\n"
        "[bold cyan]The I/O Channel awaits. Control the streams.[/bold cyan]"
    ),
    "input_output": (
        "[bold green]THE I/O CHANNEL — CONNECTED.[/bold green]\n\n"
        "stdin, stdout, stderr — three streams, fully controlled. "
        "> overwrites. >> appends. 2>&1 merges. &> captures everything. "
        "Here documents inject multi-line data inline. "
        "The script's data flow is no longer accidental.\n\n"
        "[bold cyan]The Error Trap is ahead. Scripts that fail silently are scripts that lie.[/bold cyan]"
    ),
    "error_handling": (
        "[bold green]THE ERROR TRAP — SET.[/bold green]\n\n"
        "set -euo pipefail at the top of every script. trap for cleanup. "
        "$? for exit codes. && and || for conditional chaining. "
        "The scripts fail loudly now. They clean up after themselves. "
        "They don't pretend everything is fine when it isn't.\n\n"
        "[bold cyan]The Deployment Forge is the final zone. Real scripts. Real problems. Let's build.[/bold cyan]"
    ),
    "real_scripts": (
        "[bold yellow]*** THE DEPLOYMENT FORGE — COMPLETE. ***[/bold yellow]\n\n"
        "[bold white]The automation layer is yours.[/bold white]\n\n"
        "Log rotation. Dated backups. Deployment with rollback. Cron scheduling. "
        "Argument parsing. Every pattern the ops team outsourced to a SaaS platform, "
        "replicated in shell scripts that run anywhere, depend on nothing, "
        "and will still be working when the SaaS company pivots to AI.\n\n"
        "[bold magenta]The shell is not a legacy interface. It is the automation substrate "
        "underneath everything. You don't just use it now — you write it.[/bold magenta]\n\n"
        "[bold yellow]SCRIPT FORGE STATUS: SHELL LORD. AUTOMATION: TOTAL.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "shebang_and_basics": (
        "[bold red]BOSS: THE QUOTING GAUNTLET[/bold red]\n\n"
        "[bold yellow]Single quotes, double quotes, command substitution, variable expansion. "
        "A script with a quoting bug will silently break on every filename with a space. "
        "Prove you understand every quoting rule.[/bold yellow]"
    ),
    "conditionals": (
        "[bold red]BOSS: THE BRANCH PREDICTOR[/bold red]\n\n"
        "[bold yellow]File tests, string tests, numeric tests — combined in a single conditional. "
        "The script needs to handle every edge case: missing files, empty variables, "
        "unexpected input. Prove your conditionals are airtight.[/bold yellow]"
    ),
    "loops": (
        "[bold red]BOSS: THE INFINITE ITERATOR[/bold red]\n\n"
        "[bold yellow]A loop that reads a file, processes each line, handles empty input, "
        "and knows when to break. The fraud script looped over ten thousand entries. "
        "Prove you can read the loop and predict exactly what it outputs.[/bold yellow]"
    ),
    "functions": (
        "[bold red]BOSS: THE FUNCTION ARCHITECT[/bold red]\n\n"
        "[bold yellow]A function that takes arguments, uses local variables, returns data via stdout, "
        "and sets a meaningful exit code. The building block of every maintainable script. "
        "Prove you can design one from scratch.[/bold yellow]"
    ),
    "text_processing": (
        "[bold red]BOSS: THE PIPELINE MASTER[/bold red]\n\n"
        "[bold yellow]grep, sed, awk, cut, sort, uniq — chained in a single pipeline. "
        "The input is messy. The output must be clean. "
        "One pipeline. No intermediate files. Prove it.[/bold yellow]"
    ),
    "input_output": (
        "[bold red]BOSS: THE STREAM ROUTER[/bold red]\n\n"
        "[bold yellow]Redirect stdout to a file, stderr to a different file, "
        "and pipe a third stream through a filter — all in one command. "
        "Prove you control every byte that leaves the process.[/bold yellow]"
    ),
    "error_handling": (
        "[bold red]BOSS: THE FAILSAFE ARCHITECT[/bold red]\n\n"
        "[bold yellow]A script that creates temp files, forks background processes, "
        "and must clean up everything on ANY exit — normal, error, or interrupt. "
        "set -euo pipefail and trap. Prove the cleanup is bulletproof.[/bold yellow]"
    ),
    "real_scripts": (
        "[bold red]BOSS: THE FULL DEPLOYMENT[/bold red]\n\n"
        "[bold yellow]Build a mental model of a complete deployment script: "
        "argument parsing, validation, backup, deploy, health check, rollback on failure, "
        "trap for cleanup, cron for scheduling. Every concept from every zone. "
        "Prove you can automate everything.[/bold yellow]"
    ),
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Script", "Wrote your first shebang line. The shell recognized your intent."),
    "shebang_master": ("Shebang Decoded", "Cleared the Shebang Line. Variables, quoting, command substitution — the atoms of automation."),
    "conditional_master": ("Branch Logic", "Cleared the Conditional Gate. Your scripts make decisions now."),
    "loop_master": ("Loop Architect", "Cleared the Loop Construct. Repetition is no longer manual."),
    "function_master": ("Function Core", "Cleared the Function Core. Modular, scoped, reusable code."),
    "text_master": ("Text Processor", "Cleared the Text Processing Forge. grep, sed, awk — the data yields its secrets."),
    "io_master": ("Stream Controller", "Cleared the I/O Channel. Three file descriptors. Total control."),
    "error_master": ("Failsafe Engineer", "Cleared the Error Trap. Scripts fail loudly and clean up quietly."),
    "deploy_master": ("Automation Complete", "Cleared the Deployment Forge. Real scripts solving real problems with zero dependencies."),
    "streak_3": ("Clean Run", "3 correct in a row. The syntax is becoming muscle memory."),
    "streak_5": ("Pipeline Flow", "5 in a row. You're writing scripts in your head now."),
    "streak_10": ("SHELL LORD", "10 in a row. The shell is an extension of your thought process."),
    "no_hints": ("No Hints Needed", "Cleared a zone without hints. The man page is already internalized."),
    "speed_demon": ("Sub-5 Execute", "Answered in under 5 seconds. The command was typed before the question finished rendering."),
    "level_10": ("Junior Scripter", "Level 10. You've moved past one-liners into real scripts."),
    "level_20": ("Senior Automator", "Level 20. The ops team's SaaS platform does nothing you can't do in 200 lines of bash."),
    "level_30": ("Shell Lord", "Maximum level. The automation substrate has no secrets from you. Anything that can be done on a Unix machine, you can script."),
    "completionist": ("Full Automation", "Every zone. Every challenge. The Script Forge is yours — permanently."),
    "boss_slayer": ("Boss Script Defeated", "Beat your first boss challenge. The script did what you said it would do."),
}
