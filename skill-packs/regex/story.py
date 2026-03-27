"""
story.py — Narrative for the Pattern Recon (Regex) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — INCOMING TRANSMISSION[/bold red]

A cascade of noise floods your screen — logs, packets, fragments of data
that almost mean something. CIPHER's voice cuts through the static.

[bold cyan]"Operative. The target's network is broadcasting on seventeen channels
simultaneously. Somewhere in that noise is the access key. But you'll never
find it by reading line by line."[/bold cyan]

You study the stream. Addresses, timestamps, session IDs — all tangled together.

[bold cyan]"What you need is a pattern engine. A way to describe what you're looking for
in abstract terms and let the machine find every match in milliseconds."[/bold cyan]

[bold white]"Regular expressions."[/bold white]

[bold cyan]"Exactly. The operative who can write a clean regex is worth ten who
can't. Learn the syntax. The signal is in here — you just have to describe it."[/bold cyan]

The noise sharpens. For the first time, you see the structure underneath.
"""

ZONE_INTROS = {
    "basic_patterns": (
        "[bold cyan]ZONE 1 — THE PATTERN BASICS LAB[/bold cyan]\n\n"
        "CIPHER opens the tutorial module. [bold white]'Every regex starts here: "
        "the dot, the asterisk, the question mark. These are your tools. "
        "Learn what each one matches and you can describe anything.'[/bold white]"
    ),
    "character_classes": (
        "[bold cyan]ZONE 2 — CHARACTER CLASS VAULT[/bold cyan]\n\n"
        "[bold white]'Brackets give you precision. [a-z] matches any lowercase letter. "
        "[0-9] matches any digit. \\w, \\d, \\s — shorthand for the most common classes. "
        "The vault is locked with character sets. Crack them.'[/bold white]"
    ),
    "anchors_groups": (
        "[bold cyan]ZONE 3 — ANCHOR STATION[/bold cyan]\n\n"
        "[bold white]'A pattern that matches anywhere is sloppy. ^ pins you to the start. "
        "$ pins you to the end. Parentheses group pieces together. "
        "Anchors are what separate a useful regex from a dangerous one.'[/bold white]"
    ),
    "quantifiers_advanced": (
        "[bold cyan]ZONE 4 — QUANTIFIER RANGE[/bold cyan]\n\n"
        "[bold white]'How many? That's the question quantifiers answer. "
        "{3} means exactly three. {2,5} means two to five. "
        "The lazy modifier changes everything. Know when to be greedy and when to pull back.'[/bold white]"
    ),
    "lookarounds": (
        "[bold cyan]ZONE 5 — LOOKAROUND COMPOUND[/bold cyan]\n\n"
        "[bold white]'Zero-width assertions. They check a position without consuming characters. "
        "Lookahead says what must come next. Lookbehind says what came before. "
        "Negative versions invert the logic. Ghost-level syntax.'[/bold white]"
    ),
    "real_world_patterns": (
        "[bold cyan]ZONE 6 — THE SIGNAL GRID[/bold cyan]\n\n"
        "[bold white]'Theory is done. Now you apply it. IP addresses. Email addresses. "
        "Dates. Log entries. Every data extraction task in the field requires "
        "patterns like these. Write them clean. Write them fast.'[/bold white]"
    ),
    "regex_flags": (
        "[bold cyan]ZONE 7 — FLAG OPERATIONS[/bold cyan]\n\n"
        "[bold white]'Same pattern. Different flags. Completely different results. "
        "IGNORECASE catches what case-sensitive misses. "
        "MULTILINE changes what ^ and $ mean entirely. "
        "DOTALL makes . match newlines. VERBOSE lets you comment a regex like code. "
        "Flags are the configuration layer. Learn them.'[/bold white]"
    ),
    "python_regex": (
        "[bold cyan]ZONE 8 — PYTHON REGEX ENGINE[/bold cyan]\n\n"
        "[bold white]'Python wraps regex in the re module. "
        "re.search, re.match, re.findall, re.sub — each does something different. "
        "re.compile caches the pattern for speed. Named groups give captures semantic meaning. "
        "This is the engine you will use in real code. Learn it cold.'[/bold white]"
    ),
    "sed_and_grep_regex": (
        "[bold cyan]ZONE 9 — THE STREAM REWRITER[/bold cyan]\n\n"
        "[bold white]'Regex in the shell is where it gets operational. "
        "grep -oE extracts. sed -i rewrites in-place. awk splits and processes fields. "
        "The log pipeline — grep | sort | uniq -c | sort -rn — runs in real incident response. "
        "This is not theory. This is the field.'[/bold white]"
    ),
    "named_groups_and_backreferences": (
        "[bold cyan]◈  NAMED GROUPS AND BACKREFERENCES  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Anonymous capture groups give you \\1, \\2 — fragile"
        " and order-dependent. Named groups give you (?P<timestamp>...) and"
        " (?P=timestamp) — self-documenting, resilient. The NEXUS log format"
        " has twelve fields. Name every group. Miss none.'[/bold white]"
    ),
    "substitution_and_replace": (
        "[bold cyan]◈  SUBSTITUTION AND REPLACE  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The logs contain redacted account numbers: ACCT-XXXX-YYYY."
        " We need to un-redact the pattern from a reference file using re.sub()."
        " The replacement references back-captured groups. Get the backreference"
        " syntax right and the data is ours.'[/bold white]"
    ),
    "regex_in_javascript": (
        "[bold cyan]◈  REGEX IN JAVASCRIPT  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The NEXUS frontend validates inputs client-side."
        " JavaScript regex — /pattern/flags literals, String.match(), RegExp.test()."
        " Their validation is supposed to block certain account numbers."
        " Find the bypass. The JS regex has an edge case.'[/bold white]"
    ),
    "advanced_techniques": (
        "[bold cyan]◈  ADVANCED TECHNIQUES  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The NEXUS log scanner runs your patterns against"
        " untrusted input. One ReDoS pattern in production and their server"
        " hangs for 30 seconds on a crafted string. I need you to identify"
        " catastrophic backtracking, understand atomic groups, and write"
        " patterns that don't explode under adversarial input.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "basic_patterns": (
        "[bold green]ZONE CLEAR — PATTERN BASICS[/bold green]\n\n"
        "The fundamentals are locked in. Dot, star, plus, question mark — "
        "the alphabet of pattern matching. CIPHER marks the module complete."
    ),
    "character_classes": (
        "[bold green]ZONE CLEAR — CHARACTER CLASSES[/bold green]\n\n"
        "You can now describe any character set with surgical precision. "
        "Brackets, ranges, negations — the vault is open."
    ),
    "anchors_groups": (
        "[bold green]ZONE CLEAR — ANCHORS AND GROUPS[/bold green]\n\n"
        "Your patterns now know their position. Anchors and capture groups "
        "give structure to even the most complex expressions."
    ),
    "quantifiers_advanced": (
        "[bold green]ZONE CLEAR — QUANTIFIERS[/bold green]\n\n"
        "Greedy, lazy, possessive — you control exactly how much a pattern consumes. "
        "Precision and efficiency, combined."
    ),
    "lookarounds": (
        "[bold green]ZONE CLEAR — LOOKAROUNDS[/bold green]\n\n"
        "Zero-width assertions mastered. You can now match what's there "
        "without touching it — ghost-level regex technique."
    ),
    "real_world_patterns": (
        "[bold green]ZONE CLEAR — SIGNAL GRID[/bold green]\n\n"
        "Every real-world pattern extracted cleanly. IP addresses, emails, "
        "timestamps — the noise has been decoded. Signal acquired."
    ),
    "regex_flags": (
        "[bold green]ZONE CLEAR — FLAG OPERATIONS[/bold green]\n\n"
        "IGNORECASE, MULTILINE, DOTALL, VERBOSE — the flag layer is yours. "
        "CIPHER: 'The same pattern hits ten times harder when you know which flags to arm.'"
    ),
    "python_regex": (
        "[bold green]ZONE CLEAR — PYTHON REGEX ENGINE[/bold green]\n\n"
        "re.compile, findall, sub, named groups — the Python re module fully mapped. "
        "CIPHER: 'Now you can write regex that works in production code, not just in theory.'"
    ),
    "sed_and_grep_regex": (
        "[bold green]ZONE CLEAR — STREAM REWRITER[/bold green]\n\n"
        "grep -oE, sed -i, awk field extraction, the log pipeline — operational regex mastered. "
        "CIPHER: 'Pattern Recon complete. You can find anything in any log file on any system.'"
    ),
    "named_groups_and_backreferences": (
        "[bold green]ZONE CLEAR — NAMED GROUPS[/bold green]\n\n"
        "(?P<field>...) syntax mastered. Backreferences \\1 and (?P=name) — locked. "
        "CIPHER: 'Your patterns are self-documenting now. Senior-level regex.'"
    ),
    "substitution_and_replace": (
        "[bold green]ZONE CLEAR — SUBSTITUTION ENGINE[/bold green]\n\n"
        "re.sub(), sed substitution, backreferences in replacements — the full rewrite layer. "
        "CIPHER: 'You can transform data at the pattern level. That's surgical precision.'"
    ),
    "regex_in_javascript": (
        "[bold green]ZONE CLEAR — JS REGEX CRACKED[/bold green]\n\n"
        "/pattern/flags literals, .match(), .replace(), .test(), exec() — all operational. "
        "CIPHER: 'Their client-side validation is transparent to you now. The bypass is identified.'"
    ),
    "advanced_techniques": (
        "[bold green]ZONE CLEAR — ADVANCED TECHNIQUES[/bold green]\n\n"
        "ReDoS patterns identified. Atomic groups understood. Performance traps avoided. "
        "CIPHER: 'You write production-safe regex now. No more time bombs in the codebase.'"
    ),
}

BOSS_INTROS = {
    "basic_patterns": (
        "[bold red]BOSS CHALLENGE — PATTERN GAUNTLET[/bold red]\n\n"
        "[bold white]'Write the full regex. No shortcuts. The system demands precision — "
        "one wrong character and the match fails.'[/bold white]"
    ),
    "character_classes": (
        "[bold red]BOSS CHALLENGE — CLASS VAULT LOCK[/bold red]\n\n"
        "[bold white]'The vault combines multiple character classes in a single expression. "
        "You have one shot. Make it count.'[/bold white]"
    ),
    "anchors_groups": (
        "[bold red]BOSS CHALLENGE — ANCHOR PROTOCOL[/bold red]\n\n"
        "[bold white]'A capturing group with anchors. The data must match exactly — "
        "not approximately. Write it clean.'[/bold white]"
    ),
    "quantifiers_advanced": (
        "[bold red]BOSS CHALLENGE — QUANTIFIER STRESS TEST[/bold red]\n\n"
        "[bold white]'Greedy vs lazy. The wrong choice extracts too much or too little. "
        "Show me you understand the difference.'[/bold white]"
    ),
    "lookarounds": (
        "[bold red]BOSS CHALLENGE — ZERO-WIDTH AMBUSH[/bold red]\n\n"
        "[bold white]'A combined lookahead and lookbehind in a single expression. "
        "This is the ghost layer. One chance.'[/bold white]"
    ),
    "real_world_patterns": (
        "[bold red]BOSS CHALLENGE — FINAL SIGNAL EXTRACTION[/bold red]\n\n"
        "[bold white]'Extract all unique IP addresses from the log file using grep. "
        "The pattern must be tight. No false positives. This is field work.'[/bold white]"
    ),
    "regex_flags": (
        "[bold red]BOSS CHALLENGE — FLAG COMBINATION[/bold red]\n\n"
        "[bold white]'A multi-line log with mixed case and newlines inside entries. "
        "Which combination of flags does the job? One wrong flag and you miss half the data.'[/bold white]"
    ),
    "python_regex": (
        "[bold red]BOSS CHALLENGE — NAMED GROUP EXTRACTION[/bold red]\n\n"
        "[bold white]'A structured log line. Named groups for timestamp, level, and message. "
        "Write the pattern with (?P<name>...) syntax. Then retrieve by name.'[/bold white]"
    ),
    "sed_and_grep_regex": (
        "[bold red]BOSS CHALLENGE — THE LOG PIPELINE[/bold red]\n\n"
        "[bold white]'Build the full pipeline: extract IPs from access.log, count each, "
        "sort highest-to-lowest, show top 10. "
        "This runs in real incident response. Build it.'[/bold white]"
    ),
}
