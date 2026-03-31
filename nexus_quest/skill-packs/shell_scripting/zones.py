"""
zones.py — Shell Scripting skill pack zones for NEXUS Quest.
8 zones, ~45 challenges. Challenge type: quiz (multiple-choice a/b/c/d).
"""

from engine.zone import Zone
from engine.challenge import Challenge

ZONE_ORDER = [
    "shebang_and_basics",
    "conditionals",
    "loops",
    "functions",
    "text_processing",
    "input_output",
    "error_handling",
    "real_scripts",
]

ZONES = {
    # ── ZONE 1: SHEBANG & BASICS ────────────────────────────────────────
    "shebang_and_basics": Zone(
        id="shebang_and_basics",
        title="The Shebang Line",
        description="Script headers, echo, variables, quoting, and command substitution.",
        challenges=[
            Challenge(
                id="shb_1",
                type="quiz",
                prompt="What is the purpose of the first line #!/bin/bash in a shell script?",
                options=[
                    "It is a comment that documents the author",
                    "It tells the kernel which interpreter to use to execute the script",
                    "It imports the bash standard library",
                    "It sets the script's file permissions to executable",
                ],
                answer="b",
                explanation=(
                    "The shebang (#!) on line 1 tells the OS which interpreter to invoke. "
                    "#!/bin/bash means 'run this file with /bin/bash'. Without it, the shell "
                    "that launches the script decides which interpreter to use — which may not be bash."
                ),
                xp=25,
                hints=[
                    "It starts with #! — the 'shebang' or 'hashbang'.",
                    "Think about what happens when you run ./script.sh — how does the OS know it's bash?",
                ],
            ),
            Challenge(
                id="shb_2",
                type="quiz",
                prompt="Which command outputs text to standard output in a bash script?",
                options=[
                    "print",
                    "echo",
                    "say",
                    "write",
                ],
                answer="b",
                explanation=(
                    "echo prints its arguments to stdout, followed by a newline. "
                    "echo 'Hello' outputs Hello. Use echo -n to suppress the trailing newline. "
                    "printf is the more portable alternative for formatted output."
                ),
                xp=25,
                hints=[
                    "It's a four-letter word that means to repeat sound.",
                    "Think of sound bouncing off a wall.",
                ],
            ),
            Challenge(
                id="shb_3",
                type="quiz",
                prompt="How do you assign a variable in bash?",
                options=[
                    "set name = 'Ghost'",
                    "name='Ghost'",
                    "$name='Ghost'",
                    "let name = 'Ghost'",
                ],
                answer="b",
                explanation=(
                    "In bash, variable assignment uses NAME=VALUE with NO spaces around the = sign. "
                    "Spaces cause bash to interpret the name as a command. "
                    "To read the variable later, use $name or ${name}."
                ),
                xp=25,
                hints=[
                    "Bash is picky about whitespace around the equals sign.",
                    "No dollar sign on the left side when assigning.",
                ],
            ),
            Challenge(
                id="shb_4",
                type="quiz",
                prompt="What is the difference between single quotes and double quotes in bash?",
                options=[
                    "There is no difference; they are interchangeable",
                    "Single quotes allow variable expansion; double quotes do not",
                    "Double quotes allow variable expansion; single quotes preserve everything literally",
                    "Single quotes are for strings; double quotes are for numbers",
                ],
                answer="c",
                explanation=(
                    "Double quotes allow variable expansion ($VAR) and command substitution ($(cmd)). "
                    "Single quotes preserve everything literally — no expansion at all. "
                    "echo \"Hello $USER\" prints Hello ghost. "
                    "echo 'Hello $USER' prints Hello $USER."
                ),
                xp=30,
                hints=[
                    "Try echo \"$HOME\" vs echo '$HOME' in your head.",
                    "One of them treats $ as special; the other treats it as a literal character.",
                ],
            ),
            Challenge(
                id="shb_5",
                type="quiz",
                prompt="What does the syntax $(command) do in a bash script?",
                options=[
                    "Runs command in a subshell and substitutes its output inline",
                    "Declares a function called command",
                    "Creates a variable named command",
                    "Runs command in the background",
                ],
                answer="a",
                explanation=(
                    "Command substitution — $(command) — executes command in a subshell and replaces "
                    "itself with the command's stdout. Example: today=$(date +%F) stores '2026-03-31' in today. "
                    "The older backtick syntax `command` does the same but is harder to nest."
                ),
                xp=30,
                hints=[
                    "It captures the output of a command so you can use it as a value.",
                    "The older syntax for this used backticks: `command`.",
                ],
            ),
            Challenge(
                id="shb_6",
                type="quiz",
                prompt="Which of these correctly makes a script executable and runs it?",
                options=[
                    "bash script.sh (no chmod needed)",
                    "chmod +x script.sh && ./script.sh",
                    "Both a and b will work",
                    "run script.sh",
                ],
                answer="c",
                explanation=(
                    "bash script.sh explicitly invokes the interpreter — no execute permission needed. "
                    "./script.sh uses the shebang to find the interpreter but requires the execute bit. "
                    "chmod +x adds execute permission. Both approaches are valid."
                ),
                xp=25,
                hints=[
                    "There are two ways to run a script: invoke the interpreter directly, or make the file executable.",
                    "One needs chmod, the other doesn't.",
                ],
            ),
        ],
    ),

    # ── ZONE 2: CONDITIONALS ────────────────────────────────────────────
    "conditionals": Zone(
        id="conditionals",
        title="The Conditional Gate",
        description="if/elif/else, test expressions, file tests, string and number comparisons.",
        challenges=[
            Challenge(
                id="cond_1",
                type="quiz",
                prompt="What keyword ends an if block in bash?",
                options=[
                    "end",
                    "endif",
                    "fi",
                    "done",
                ],
                answer="c",
                explanation=(
                    "Bash closes an if block with fi ('if' spelled backwards). "
                    "Structure: if CONDITION; then COMMANDS; elif CONDITION; then COMMANDS; else COMMANDS; fi. "
                    "This is one of bash's distinctive syntax quirks."
                ),
                xp=25,
                hints=[
                    "It's the keyword 'if' reversed.",
                    "Three letters. Spell 'if' backwards.",
                ],
            ),
            Challenge(
                id="cond_2",
                type="quiz",
                prompt="What does [[ -f /etc/passwd ]] test for?",
                options=[
                    "Whether /etc/passwd is a directory",
                    "Whether /etc/passwd exists and is a regular file",
                    "Whether /etc/passwd is writable",
                    "Whether /etc/passwd is not empty",
                ],
                answer="b",
                explanation=(
                    "-f tests if the path exists AND is a regular file (not a directory, symlink, device, etc.). "
                    "Other file tests: -d (directory), -e (exists, any type), -r (readable), "
                    "-w (writable), -x (executable), -s (exists and non-empty)."
                ),
                xp=30,
                hints=[
                    "-f stands for 'file' — specifically a regular file.",
                    "It checks two things: existence AND file type.",
                ],
            ),
            Challenge(
                id="cond_3",
                type="quiz",
                prompt="Which operator compares two integers for equality inside [[ ]]?",
                options=[
                    "==",
                    "-eq",
                    "equals",
                    "is",
                ],
                answer="b",
                explanation=(
                    "Inside [[ ]], integer comparison uses -eq (equal), -ne (not equal), -lt (less than), "
                    "-le (less-or-equal), -gt (greater), -ge (greater-or-equal). "
                    "== compares strings, not numbers. [[ 10 == 9 ]] is false, but so is [[ '10' == '10 ' ]]."
                ),
                xp=30,
                hints=[
                    "Bash distinguishes between string comparison and numeric comparison.",
                    "The numeric operators start with a dash: -eq, -ne, -lt, -gt, etc.",
                ],
            ),
            Challenge(
                id="cond_4",
                type="quiz",
                prompt="What does [[ -d /tmp ]] evaluate to?",
                options=[
                    "True if /tmp is a regular file",
                    "True if /tmp is a directory",
                    "True if /tmp is deleted",
                    "True if /tmp is a device node",
                ],
                answer="b",
                explanation=(
                    "-d tests whether the path exists and is a directory. "
                    "/tmp is a directory on virtually all Unix systems, so [[ -d /tmp ]] is true. "
                    "Use -d before attempting cd to avoid errors on missing directories."
                ),
                xp=25,
                hints=[
                    "-d stands for 'directory'.",
                    "It returns true if the path is a directory.",
                ],
            ),
            Challenge(
                id="cond_5",
                type="quiz",
                prompt="What is the difference between [ ] and [[ ]] in bash?",
                options=[
                    "[[ ]] is a bash keyword with richer features; [ ] is a POSIX command",
                    "[ ] is newer and preferred; [[ ]] is deprecated",
                    "They are identical aliases",
                    "[[ ]] only works with numbers; [ ] works with strings",
                ],
                answer="a",
                explanation=(
                    "[ is actually the 'test' command (try: which [). It's POSIX-compliant but limited. "
                    "[[ is a bash keyword — it supports pattern matching (==), regex (=~), "
                    "logical operators (&&, ||) inside it, and doesn't require quoting variables to prevent word splitting."
                ),
                xp=35,
                hints=[
                    "One is a POSIX standard command; the other is a bash-specific enhancement.",
                    "[[ ]] is the modern bash version with more features.",
                ],
            ),
            Challenge(
                id="cond_6",
                type="quiz",
                prompt="How do you test if a string variable is empty in bash?",
                options=[
                    "[[ $var == '' ]]",
                    "[[ -z $var ]]",
                    "Both a and b work correctly",
                    "[[ $var -eq 0 ]]",
                ],
                answer="c",
                explanation=(
                    "-z tests if a string has zero length. [[ -z \"\" ]] is true. "
                    "Comparing to '' also works. The inverse is -n (non-empty). "
                    "-eq 0 would do a numeric comparison, which fails on non-numeric strings."
                ),
                xp=30,
                hints=[
                    "-z means 'zero length'.",
                    "There's more than one valid way to check for an empty string.",
                ],
            ),
        ],
    ),

    # ── ZONE 3: LOOPS ───────────────────────────────────────────────────
    "loops": Zone(
        id="loops",
        title="The Loop Construct",
        description="for loops, while, until, break/continue, iterating files and lines, C-style for.",
        challenges=[
            Challenge(
                id="loop_1",
                type="quiz",
                prompt="What does this output? for i in 1 2 3; do echo $i; done",
                options=[
                    "1 2 3 on one line",
                    "1, 2, and 3 each on a separate line",
                    "An error — for loops require $(seq ...)",
                    "123 with no spaces",
                ],
                answer="b",
                explanation=(
                    "for i in 1 2 3 iterates over the word list. Each iteration, $i is set to the next word "
                    "and the body (echo $i) runs. echo adds a newline, so output is three separate lines: 1, 2, 3."
                ),
                xp=25,
                hints=[
                    "echo adds a newline after its output by default.",
                    "The loop body runs once per item in the list.",
                ],
            ),
            Challenge(
                id="loop_2",
                type="quiz",
                prompt="How do you iterate over all .log files in the current directory?",
                options=[
                    "for f in *.log; do echo $f; done",
                    "foreach f (*.log) echo $f end",
                    "loop *.log as f; echo $f; endloop",
                    "for (f : *.log) { echo $f; }",
                ],
                answer="a",
                explanation=(
                    "Bash's for-in loop accepts glob patterns. *.log expands to all matching filenames. "
                    "If no files match, the literal string '*.log' is used — protect against this with "
                    "shopt -s nullglob, which makes unmatched globs expand to nothing."
                ),
                xp=30,
                hints=[
                    "Bash uses for...in...do...done syntax.",
                    "Shell globs (*.log) expand before the loop runs.",
                ],
            ),
            Challenge(
                id="loop_3",
                type="quiz",
                prompt="What does the 'while' loop do in bash?",
                options=[
                    "Runs the body once and then checks the condition",
                    "Repeats the body as long as the condition is TRUE",
                    "Repeats the body as long as the condition is FALSE",
                    "Runs the body exactly N times",
                ],
                answer="b",
                explanation=(
                    "while CONDITION; do BODY; done — the body executes repeatedly as long as CONDITION "
                    "returns exit code 0 (true). When CONDITION returns non-zero (false), the loop stops. "
                    "The 'until' loop is the inverse: it runs while the condition is FALSE."
                ),
                xp=25,
                hints=[
                    "'while' means 'keep going as long as'.",
                    "The opposite construct — runs while condition is false — is 'until'.",
                ],
            ),
            Challenge(
                id="loop_4",
                type="quiz",
                prompt="How do you read a file line by line in bash?",
                options=[
                    "for line in $(cat file.txt); do echo $line; done",
                    "while IFS= read -r line; do echo \"$line\"; done < file.txt",
                    "readlines file.txt | for line; do echo $line; done",
                    "cat file.txt | foreach line echo $line",
                ],
                answer="b",
                explanation=(
                    "while IFS= read -r line is the correct idiom. IFS= prevents leading/trailing whitespace "
                    "trimming, -r prevents backslash interpretation. Input redirection (< file.txt) feeds the file "
                    "into the loop. Option a breaks on spaces/tabs, not just newlines."
                ),
                xp=35,
                hints=[
                    "The correct idiom uses 'read' inside a while loop.",
                    "IFS= and -r are important to preserve line content exactly.",
                ],
            ),
            Challenge(
                id="loop_5",
                type="quiz",
                prompt="What does 'break' do inside a loop?",
                options=[
                    "Pauses the loop for 1 second",
                    "Skips the current iteration and continues with the next one",
                    "Exits the loop immediately",
                    "Restarts the loop from the beginning",
                ],
                answer="c",
                explanation=(
                    "break exits the innermost loop immediately. Execution continues after 'done'. "
                    "break N exits N levels of nested loops. "
                    "'continue' is the keyword that skips the rest of the current iteration."
                ),
                xp=25,
                hints=[
                    "Think of 'breaking out' of a loop.",
                    "The keyword for skipping to the next iteration is 'continue', not 'break'.",
                ],
            ),
            Challenge(
                id="loop_6",
                type="quiz",
                prompt="What is the C-style for loop syntax in bash?",
                options=[
                    "for (i=0; i<10; i++) { echo $i; }",
                    "for ((i=0; i<10; i++)); do echo $i; done",
                    "for i from 0 to 9; do echo $i; done",
                    "for i = 0..9; do echo $i; done",
                ],
                answer="b",
                explanation=(
                    "Bash supports C-style for loops with double parentheses: for ((INIT; COND; STEP)); do ... done. "
                    "Inside (( )), arithmetic is evaluated directly — no $ prefix needed for variables, "
                    "and operators like <, ++, += work as expected."
                ),
                xp=30,
                hints=[
                    "It uses double parentheses (( )) for the arithmetic expression.",
                    "The body still uses do...done, not curly braces.",
                ],
            ),
        ],
    ),

    # ── ZONE 4: FUNCTIONS ───────────────────────────────────────────────
    "functions": Zone(
        id="functions",
        title="The Function Core",
        description="Defining functions, local variables, return values, passing arguments, $@ vs $*.",
        challenges=[
            Challenge(
                id="func_1",
                type="quiz",
                prompt="Which of these correctly defines a bash function?",
                options=[
                    "function greet { echo 'Hello'; }",
                    "def greet(): echo 'Hello'",
                    "greet = function() { echo 'Hello'; }",
                    "func greet() => echo 'Hello'",
                ],
                answer="a",
                explanation=(
                    "Bash functions are defined with either 'function name { body; }' or 'name() { body; }'. "
                    "Both syntaxes are valid. The function keyword is optional. "
                    "There are no parameter declarations — arguments are accessed via $1, $2, etc."
                ),
                xp=25,
                hints=[
                    "Bash uses the 'function' keyword or () after the name.",
                    "The body goes inside curly braces { }.",
                ],
            ),
            Challenge(
                id="func_2",
                type="quiz",
                prompt="Inside a function, what does 'local count=0' do?",
                options=[
                    "Creates a variable visible only within the function",
                    "Creates a read-only variable",
                    "Creates a global variable named 'local'",
                    "Decrements count to zero",
                ],
                answer="a",
                explanation=(
                    "'local' restricts a variable's scope to the function (and its children). "
                    "Without 'local', variables set inside a function are global — they pollute the caller's namespace. "
                    "Always use 'local' for temporary variables inside functions."
                ),
                xp=30,
                hints=[
                    "'local' is a bash builtin that controls variable scope.",
                    "Without it, the variable would be visible everywhere after the function runs.",
                ],
            ),
            Challenge(
                id="func_3",
                type="quiz",
                prompt="How does a bash function 'return' a string value to the caller?",
                options=[
                    "return 'string value'",
                    "echo the value and have the caller capture it with $(function_name)",
                    "Use the 'yield' keyword",
                    "Set a global $RETURN variable",
                ],
                answer="b",
                explanation=(
                    "'return' in bash only sets a numeric exit code (0-255). It cannot return strings. "
                    "The idiomatic way to return data is to echo it and capture with command substitution: "
                    "result=$(my_function). The function's stdout becomes the variable's value."
                ),
                xp=35,
                hints=[
                    "'return' in bash only handles numeric exit codes, not strings.",
                    "Think about command substitution — $() captures stdout.",
                ],
            ),
            Challenge(
                id="func_4",
                type="quiz",
                prompt="Inside a function, what does $1 refer to?",
                options=[
                    "The script's first command-line argument",
                    "The function's first argument",
                    "The literal string '$1'",
                    "The PID of the function",
                ],
                answer="b",
                explanation=(
                    "Inside a function, $1, $2, etc. refer to the function's arguments, not the script's. "
                    "The script's positional parameters are temporarily replaced while the function runs. "
                    "$# is the count of function arguments, $@ is all of them."
                ),
                xp=30,
                hints=[
                    "Positional parameters are context-dependent in bash.",
                    "Functions have their own $1, $2, $# — separate from the script's.",
                ],
            ),
            Challenge(
                id="func_5",
                type="quiz",
                prompt='What is the key difference between "$@" and "$*" in a function?',
                options=[
                    "They are identical in all contexts",
                    '"$@" expands each argument as a separate word; "$*" joins them into one string',
                    '"$*" expands each argument separately; "$@" joins them',
                    '"$@" only works in functions; "$*" only works in scripts',
                ],
                answer="b",
                explanation=(
                    '"$@" preserves argument boundaries: each argument becomes a separate word. '
                    '"$*" joins all arguments into a single string using the first char of IFS as separator. '
                    'Almost always prefer "$@" — it correctly handles arguments with spaces.'
                ),
                xp=35,
                hints=[
                    "The difference only matters when arguments contain spaces.",
                    '"$@" keeps each argument intact; "$*" mashes them together.',
                ],
            ),
            Challenge(
                id="func_6",
                type="quiz",
                prompt="What does 'return 1' do inside a bash function?",
                options=[
                    "Returns the integer 1 as a result value",
                    "Sets the function's exit status to 1, indicating failure",
                    "Prints '1' to stdout",
                    "Returns to line 1 of the function",
                ],
                answer="b",
                explanation=(
                    "'return N' sets the function's exit status. 0 means success; anything 1-255 means failure. "
                    "The caller can check this with $? or use the function directly in an if statement: "
                    "if my_func; then echo 'succeeded'; fi."
                ),
                xp=30,
                hints=[
                    "In Unix, exit code 0 = success, non-zero = failure.",
                    "'return' sets the exit code, not a data value.",
                ],
            ),
        ],
    ),

    # ── ZONE 5: TEXT PROCESSING ─────────────────────────────────────────
    "text_processing": Zone(
        id="text_processing",
        title="The Text Processing Forge",
        description="grep, sed, awk, cut, sort, uniq, wc, tr, and pipe composition.",
        challenges=[
            Challenge(
                id="txt_1",
                type="quiz",
                prompt="What does grep -r 'ERROR' /var/log/ do?",
                options=[
                    "Replaces 'ERROR' in all files under /var/log/",
                    "Recursively searches all files under /var/log/ for lines containing 'ERROR'",
                    "Counts the number of errors in /var/log/",
                    "Deletes lines containing 'ERROR' from all log files",
                ],
                answer="b",
                explanation=(
                    "grep -r (recursive) searches all files in a directory tree for lines matching the pattern. "
                    "Each matching line is printed with its filename prefix. "
                    "Add -i for case-insensitive, -l for filenames only, -c for counts."
                ),
                xp=25,
                hints=[
                    "grep is a search tool, not an editor.",
                    "-r means 'recursive' — descend into subdirectories.",
                ],
            ),
            Challenge(
                id="txt_2",
                type="quiz",
                prompt="What does sed 's/old/new/g' file.txt do?",
                options=[
                    "Replaces the first occurrence of 'old' with 'new' on each line",
                    "Replaces ALL occurrences of 'old' with 'new' on each line and prints result",
                    "Deletes all lines containing 'old'",
                    "Moves lines matching 'old' to a new file",
                ],
                answer="b",
                explanation=(
                    "sed 's/old/new/g' is a substitution command. 's' = substitute, 'g' = global (all occurrences "
                    "per line, not just the first). Without 'g', only the first match per line is replaced. "
                    "sed outputs to stdout by default — use -i to edit in place."
                ),
                xp=30,
                hints=[
                    "The 'g' flag at the end stands for 'global'.",
                    "Without 'g', sed only replaces the first match on each line.",
                ],
            ),
            Challenge(
                id="txt_3",
                type="quiz",
                prompt="What does awk '{print $2}' data.txt do?",
                options=[
                    "Prints the second line of data.txt",
                    "Prints the second character of each line",
                    "Prints the second field (column) of each line",
                    "Prints every other line of data.txt",
                ],
                answer="c",
                explanation=(
                    "awk splits each line into fields by whitespace (default). $1 is the first field, "
                    "$2 the second, $0 is the entire line. "
                    "Use -F to change the delimiter: awk -F: '{print $1}' /etc/passwd prints usernames."
                ),
                xp=30,
                hints=[
                    "awk thinks in fields (columns), not lines.",
                    "$2 means the second field, split by whitespace by default.",
                ],
            ),
            Challenge(
                id="txt_4",
                type="quiz",
                prompt="What does cut -d: -f1 /etc/passwd produce?",
                options=[
                    "The first line of /etc/passwd",
                    "The first character of each line",
                    "The first colon-delimited field of each line (usernames)",
                    "Every field except the first",
                ],
                answer="c",
                explanation=(
                    "cut -d: sets the delimiter to colon. -f1 selects field 1. "
                    "/etc/passwd is colon-delimited: user:pass:uid:gid:info:home:shell. "
                    "Field 1 is the username. Use -f1,3 for multiple fields, -f2- for field 2 onwards."
                ),
                xp=30,
                hints=[
                    "-d sets the delimiter; -f selects the field number.",
                    "/etc/passwd uses colons to separate fields.",
                ],
            ),
            Challenge(
                id="txt_5",
                type="quiz",
                prompt="What does sort file.txt | uniq -c do?",
                options=[
                    "Sorts and removes all duplicate lines",
                    "Sorts the file and prefixes each unique line with its count",
                    "Counts the total number of lines in the file",
                    "Sorts numerically and outputs only the first unique value",
                ],
                answer="b",
                explanation=(
                    "sort orders lines alphabetically. uniq removes adjacent duplicates (hence sort first). "
                    "uniq -c prefixes each line with the count of consecutive occurrences. "
                    "Pipe to sort -rn to rank by frequency: sort file | uniq -c | sort -rn."
                ),
                xp=35,
                hints=[
                    "uniq only removes ADJACENT duplicates — that's why sort comes first.",
                    "-c means 'count' — how many times each line appeared.",
                ],
            ),
            Challenge(
                id="txt_6",
                type="quiz",
                prompt="What does wc -l access.log output?",
                options=[
                    "The number of words in access.log",
                    "The number of characters in access.log",
                    "The number of lines in access.log",
                    "The file size in bytes",
                ],
                answer="c",
                explanation=(
                    "wc (word count) counts lines (-l), words (-w), and characters/bytes (-c/-m). "
                    "-l counts newlines. A common pipeline: grep 'ERROR' log | wc -l counts error lines. "
                    "Without flags, wc prints all three counts."
                ),
                xp=25,
                hints=[
                    "-l stands for 'lines'.",
                    "wc without flags shows lines, words, and bytes.",
                ],
            ),
        ],
    ),

    # ── ZONE 6: INPUT & OUTPUT ──────────────────────────────────────────
    "input_output": Zone(
        id="input_output",
        title="The I/O Channel",
        description="read, stdin/stdout/stderr, redirection, here documents.",
        challenges=[
            Challenge(
                id="io_1",
                type="quiz",
                prompt="What file descriptor number does stderr use in bash?",
                options=[
                    "0",
                    "1",
                    "2",
                    "3",
                ],
                answer="c",
                explanation=(
                    "Unix file descriptors: 0 = stdin, 1 = stdout, 2 = stderr. "
                    "These are the three standard streams every process inherits. "
                    "Redirect stderr with 2>file, stdout with >file (shorthand for 1>file)."
                ),
                xp=25,
                hints=[
                    "There are three standard file descriptors: 0, 1, and 2.",
                    "stdin=0, stdout=1 — what's left for stderr?",
                ],
            ),
            Challenge(
                id="io_2",
                type="quiz",
                prompt="What does 2>&1 do in a bash command?",
                options=[
                    "Redirects stdout to stderr",
                    "Redirects stderr to wherever stdout is currently going",
                    "Redirects file descriptor 2 to a file named '1'",
                    "Merges stderr and stdin",
                ],
                answer="b",
                explanation=(
                    "2>&1 says 'send file descriptor 2 (stderr) to the same destination as fd 1 (stdout)'. "
                    "Order matters: cmd >log 2>&1 sends both to 'log'. "
                    "cmd 2>&1 >log sends stderr to the terminal and stdout to 'log' — the & references the CURRENT target."
                ),
                xp=35,
                hints=[
                    "The & before 1 means 'file descriptor 1', not a file named '1'.",
                    "It duplicates where stderr goes to match stdout's current destination.",
                ],
            ),
            Challenge(
                id="io_3",
                type="quiz",
                prompt="What is the difference between > and >> for output redirection?",
                options=[
                    "> appends; >> overwrites",
                    "> overwrites the file; >> appends to the file",
                    "> creates a new file; >> only works on existing files",
                    "There is no difference",
                ],
                answer="b",
                explanation=(
                    "> truncates the file to zero length before writing. If the file doesn't exist, it's created. "
                    ">> opens the file in append mode — existing content is preserved, new output goes at the end. "
                    "Use >> for log files. Use > when you want a clean file."
                ),
                xp=25,
                hints=[
                    "One destroys existing content; the other preserves it.",
                    "Think of >> as 'add to the end'.",
                ],
            ),
            Challenge(
                id="io_4",
                type="quiz",
                prompt="What does the 'read' builtin do in bash?",
                options=[
                    "Displays the contents of a file",
                    "Reads a line of input from stdin and assigns it to a variable",
                    "Opens a file in read-only mode",
                    "Reads the last command from history",
                ],
                answer="b",
                explanation=(
                    "read VAR reads one line from stdin and stores it in VAR. "
                    "read -p 'Name: ' name shows a prompt. read -s hides input (for passwords). "
                    "read -t 5 times out after 5 seconds. read -r prevents backslash interpretation."
                ),
                xp=25,
                hints=[
                    "It's the main way to get interactive input in a shell script.",
                    "It reads from standard input, not from files directly.",
                ],
            ),
            Challenge(
                id="io_5",
                type="quiz",
                prompt="What is a here document in bash?",
                options=[
                    "A file that exists only in the current directory",
                    "A way to pass multi-line input to a command inline using <<DELIMITER",
                    "A temporary file created by mktemp",
                    "A command that prints the current working directory",
                ],
                answer="b",
                explanation=(
                    "A here document feeds multi-line text as stdin to a command: "
                    "cat <<EOF\\nline 1\\nline 2\\nEOF. "
                    "The delimiter (EOF) can be any string. <<-EOF allows indentation with tabs. "
                    "<<<'string' is a here-string: feeds a single string as stdin."
                ),
                xp=30,
                hints=[
                    "It uses the << operator followed by a delimiter word.",
                    "It lets you embed multi-line input directly in your script.",
                ],
            ),
            Challenge(
                id="io_6",
                type="quiz",
                prompt="What does &> file.log do in bash?",
                options=[
                    "Runs the command in the background and logs its PID",
                    "Redirects both stdout and stderr to file.log",
                    "Appends stdout to file.log",
                    "Creates a symbolic link to file.log",
                ],
                answer="b",
                explanation=(
                    "&> is bash shorthand for >file 2>&1 — it redirects BOTH stdout and stderr to the same file. "
                    "Equivalent forms: >file.log 2>&1 or &>file.log. "
                    "This is bash-specific; for POSIX portability, use >file 2>&1."
                ),
                xp=30,
                hints=[
                    "& before > combines two streams.",
                    "It's a shorthand so you don't have to write 2>&1 separately.",
                ],
            ),
        ],
    ),

    # ── ZONE 7: ERROR HANDLING ──────────────────────────────────────────
    "error_handling": Zone(
        id="error_handling",
        title="The Error Trap",
        description="set -euo pipefail, trap, exit codes, && and || chaining, cleanup on exit.",
        challenges=[
            Challenge(
                id="err_1",
                type="quiz",
                prompt="What does 'set -e' do at the top of a bash script?",
                options=[
                    "Enables verbose mode, printing each command before execution",
                    "Exits the script immediately if any command returns a non-zero exit code",
                    "Enables extended globbing",
                    "Sets all variables to read-only",
                ],
                answer="b",
                explanation=(
                    "set -e (errexit) makes the script exit immediately when any command fails (returns non-zero). "
                    "Without it, the script continues regardless of errors — dangerous in production scripts. "
                    "Combine with -u (undefined vars are errors) and -o pipefail for robust scripts."
                ),
                xp=30,
                hints=[
                    "-e stands for 'errexit'.",
                    "It prevents the script from silently continuing after a failure.",
                ],
            ),
            Challenge(
                id="err_2",
                type="quiz",
                prompt="What does 'set -o pipefail' do?",
                options=[
                    "Makes pipe characters | fail if the pipeline is too long",
                    "Returns the exit code of the LAST failed command in a pipeline, not just the last command",
                    "Disables pipes entirely",
                    "Pipes stderr to a fail log automatically",
                ],
                answer="b",
                explanation=(
                    "Normally, a pipeline's exit status is the exit code of the LAST command. "
                    "cmd1 | cmd2 — if cmd1 fails but cmd2 succeeds, the pipeline reports success. "
                    "pipefail makes the pipeline return the rightmost non-zero exit code. "
                    "Combined with set -e, a failing command anywhere in a pipeline stops the script."
                ),
                xp=35,
                hints=[
                    "Without pipefail, false | true reports success.",
                    "It makes pipeline failure detection more reliable.",
                ],
            ),
            Challenge(
                id="err_3",
                type="quiz",
                prompt="What does trap 'rm -f /tmp/lockfile' EXIT do?",
                options=[
                    "Removes the lockfile only if the script is killed with Ctrl+C",
                    "Runs 'rm -f /tmp/lockfile' when the script exits, regardless of how it exits",
                    "Creates a lockfile at /tmp/lockfile on exit",
                    "Prevents the script from being interrupted",
                ],
                answer="b",
                explanation=(
                    "trap COMMAND SIGNAL registers a handler. The EXIT pseudo-signal fires when the script ends — "
                    "whether from normal completion, an error (set -e), or a signal. "
                    "It's the shell equivalent of a 'finally' block. Use it for cleanup: temp files, lockfiles, background processes."
                ),
                xp=35,
                hints=[
                    "trap sets up a handler for a specific signal or event.",
                    "EXIT fires no matter how the script ends — normal or abnormal.",
                ],
            ),
            Challenge(
                id="err_4",
                type="quiz",
                prompt="What does the expression 'mkdir /data || exit 1' do?",
                options=[
                    "Always runs both mkdir and exit",
                    "Runs exit 1 ONLY IF mkdir fails",
                    "Runs exit 1 ONLY IF mkdir succeeds",
                    "Creates /data and exits with code 0",
                ],
                answer="b",
                explanation=(
                    "|| is logical OR — the right side runs ONLY if the left side fails (non-zero exit). "
                    "&& is logical AND — the right side runs only if the left succeeds. "
                    "Pattern: command || { echo 'Failed'; exit 1; } is a common inline error handler."
                ),
                xp=30,
                hints=[
                    "|| means 'or' — if the first thing fails, try the second.",
                    "Think short-circuit evaluation: the second command is a fallback.",
                ],
            ),
            Challenge(
                id="err_5",
                type="quiz",
                prompt="What does $? contain immediately after a command runs?",
                options=[
                    "The PID of the last command",
                    "The exit code of the last command that ran",
                    "The number of arguments passed to the script",
                    "The name of the current shell",
                ],
                answer="b",
                explanation=(
                    "$? holds the exit status (0-255) of the most recently executed command. "
                    "0 = success, non-zero = failure. Check it immediately — the next command overwrites it. "
                    "Other special variables: $$ (current PID), $! (last background PID), $# (arg count)."
                ),
                xp=25,
                hints=[
                    "It's a special variable that reflects the last command's success or failure.",
                    "Zero means success; anything else means something went wrong.",
                ],
            ),
            Challenge(
                id="err_6",
                type="quiz",
                prompt="What does 'set -u' do in a bash script?",
                options=[
                    "Enables Unicode support",
                    "Treats references to undefined variables as errors",
                    "Unlocks all read-only variables",
                    "Sets the user ID for the script process",
                ],
                answer="b",
                explanation=(
                    "set -u (nounset) causes the script to exit with an error if you reference an unset variable. "
                    "Without it, $UNDEFINED silently expands to an empty string — which causes subtle bugs. "
                    "The classic header: set -euo pipefail combines errexit, nounset, and pipefail."
                ),
                xp=30,
                hints=[
                    "-u is about undefined/unset variables.",
                    "It prevents the silent empty-string expansion of typos.",
                ],
            ),
        ],
    ),

    # ── ZONE 8: REAL SCRIPTS ────────────────────────────────────────────
    "real_scripts": Zone(
        id="real_scripts",
        title="The Deployment Forge",
        description="Log rotation, deployment scripts, backup, cron scheduling, getopts argument parsing.",
        challenges=[
            Challenge(
                id="real_1",
                type="quiz",
                prompt="Which cron expression runs a script every day at 3:00 AM?",
                options=[
                    "0 3 * * *",
                    "3 0 * * *",
                    "* * 3 * *",
                    "0 0 3 * *",
                ],
                answer="a",
                explanation=(
                    "Cron fields: minute hour day-of-month month day-of-week. "
                    "0 3 * * * = minute 0, hour 3, every day, every month, every weekday. "
                    "Common mistake: confusing the minute and hour fields. 3 0 * * * runs at 00:03."
                ),
                xp=30,
                hints=[
                    "Cron format: minute hour day month weekday.",
                    "3 AM = hour 3, minute 0.",
                ],
            ),
            Challenge(
                id="real_2",
                type="quiz",
                prompt="What does getopts 'v:f' opt do in a script?",
                options=[
                    "Parses command-line options: -v requires an argument, -f is a flag",
                    "Parses command-line options: -v is a flag, -f requires an argument",
                    "Gets the operating system version and filesystem type",
                    "Optimizes the script for verbose and fast modes",
                ],
                answer="a",
                explanation=(
                    "getopts parses short options in a while loop. A colon after a letter means it takes an argument. "
                    "'v:f' means -v takes a value ($OPTARG) and -f is a boolean flag. "
                    "Pattern: while getopts 'v:f' opt; do case $opt in v) version=$OPTARG;; f) force=1;; esac; done."
                ),
                xp=35,
                hints=[
                    "The colon after a letter means that option requires a value.",
                    "No colon = flag; colon = argument required.",
                ],
            ),
            Challenge(
                id="real_3",
                type="quiz",
                prompt="Which command compresses old log files in a log rotation script?",
                options=[
                    "zip -r logs.zip *.log",
                    "gzip access.log.1",
                    "tar -xf logs.tar",
                    "compress --rotate access.log",
                ],
                answer="b",
                explanation=(
                    "gzip compresses a single file in-place, replacing it with file.gz. "
                    "Log rotation typically: rename current.log to current.log.1, gzip older rotations, "
                    "delete anything older than N days. logrotate handles this automatically, "
                    "but understanding the manual process is essential for custom scripts."
                ),
                xp=30,
                hints=[
                    "gzip is the standard Unix compression tool for individual files.",
                    "tar -x extracts (wrong direction); zip is less common on Linux servers.",
                ],
            ),
            Challenge(
                id="real_4",
                type="quiz",
                prompt="In a deployment script, what is the purpose of a 'rollback' function?",
                options=[
                    "It speeds up the deployment by skipping tests",
                    "It reverts the system to the previous known-good state if deployment fails",
                    "It rotates the deployment logs",
                    "It rolls forward to the next version",
                ],
                answer="b",
                explanation=(
                    "A rollback function restores the previous version when a deployment fails. "
                    "Typically: keep a symlink to the current release, deploy to a new directory, "
                    "swap the symlink. Rollback = swap the symlink back. "
                    "trap cleanup EXIT ensures rollback runs even on unexpected failures."
                ),
                xp=30,
                hints=[
                    "It's the safety net — what happens when the new code doesn't work?",
                    "Think 'undo the deployment'.",
                ],
            ),
            Challenge(
                id="real_5",
                type="quiz",
                prompt="What does this backup command do? tar czf backup-$(date +%F).tar.gz /data/",
                options=[
                    "Extracts a dated backup archive into /data/",
                    "Creates a gzip-compressed tar archive of /data/ with today's date in the filename",
                    "Copies /data/ to a remote backup server",
                    "Lists the contents of the most recent backup",
                ],
                answer="b",
                explanation=(
                    "tar czf: c=create, z=gzip compression, f=filename. "
                    "$(date +%F) expands to the current date (e.g. 2026-03-31). "
                    "Result: backup-2026-03-31.tar.gz containing /data/. "
                    "Dated filenames prevent overwriting previous backups."
                ),
                xp=35,
                hints=[
                    "tar c = create, z = gzip, f = output file.",
                    "$(date +%F) inserts today's date into the filename.",
                ],
            ),
            Challenge(
                id="real_6",
                type="quiz",
                prompt="How do you ensure a cleanup function runs even if the script is interrupted by Ctrl+C?",
                options=[
                    "nohup cleanup",
                    "trap cleanup SIGINT EXIT",
                    "finally { cleanup; }",
                    "set -c cleanup",
                ],
                answer="b",
                explanation=(
                    "trap cleanup SIGINT EXIT registers the cleanup function for both SIGINT (Ctrl+C) "
                    "and EXIT (any script termination). EXIT alone covers most cases since it fires "
                    "on normal exit, set -e exit, and signal-induced exit. Adding SIGINT is extra insurance. "
                    "Pattern: trap 'rm -f $TMPFILE' EXIT."
                ),
                xp=35,
                hints=[
                    "trap is the mechanism for running code on signals.",
                    "You can trap multiple signals in one command.",
                ],
            ),
        ],
    ),
}
