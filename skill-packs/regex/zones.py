"""
zones.py - All zone and challenge data for Pattern Recon (Regex)
Challenge type: quiz
"""

ZONES = {
    "basic_patterns": {
        "id": "basic_patterns",
        "name": "The Pattern Basics Lab",
        "subtitle": "Metacharacters & Wildcards",
        "color": "cyan",
        "icon": "◈",
        "commands": [".", "*", "+", "?", "^"],
        "challenges": [
            {
                "id": "bp_1",
                "type": "quiz",
                "title": "The Dot Wildcard",
                "flavor": "The audit logs are littered with variable-length hostnames. One metacharacter matches any single character — the universal wildcard that cuts through the noise.",
                "lesson": (
                    ". (dot) — matches any single character except a newline.\n\n"
                    "Used to represent 'exactly one of anything'.\n\n"
                    "Examples:\n"
                    "  a.c   → matches 'abc', 'a1c', 'a-c', etc.\n"
                    "  ...   → matches any 3-character sequence\n\n"
                    "Note: to match a literal dot, escape it: \\."
                ),
                "question": "In regex, what does . (a single dot) match?",
                "answers": [
                    "any single character except a newline",
                    "any character except newline",
                    "any single character",
                    "any character",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Think of it as a wildcard for exactly one character.",
                    "It does NOT match newlines by default.",
                    "The answer is: any single character except a newline",
                ],
            },
            {
                "id": "bp_2",
                "type": "quiz",
                "title": "Zero or More",
                "flavor": "Some log fields repeat indefinitely — or not at all. One quantifier covers both cases: zero repetitions and a million. The pattern engine's greedy eye.",
                "lesson": (
                    "* (star) — matches the preceding element zero or more times.\n\n"
                    "It is greedy by default — it will match as much as possible.\n\n"
                    "Examples:\n"
                    "  ab*c  → matches 'ac', 'abc', 'abbc', 'abbbc', ...\n"
                    "  .* → matches any string of any length (including empty)\n\n"
                    "Note: * alone is not valid — it must follow something."
                ),
                "question": "What does the * quantifier mean in regex?",
                "answers": [
                    "zero or more of the preceding element",
                    "zero or more",
                    "matches the preceding element zero or more times",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a quantity specifier — it says how many times something can appear.",
                    "It includes zero occurrences — meaning the match can succeed even if the element is absent.",
                    "The answer is: zero or more of the preceding element",
                ],
            },
            {
                "id": "bp_3",
                "type": "quiz",
                "title": "One or More",
                "flavor": "The IP addresses in the logs always have at least one digit per octet. You need to match sequences that exist — not phantom empty strings. One quantifier demands presence.",
                "lesson": (
                    "+ (plus) — matches the preceding element one or more times.\n\n"
                    "Unlike *, it requires at least one match. Empty strings do not satisfy +.\n\n"
                    "Examples:\n"
                    "  ab+c  → matches 'abc', 'abbc', 'abbbc', but NOT 'ac'\n"
                    "  \\d+   → matches one or more digits: '0', '42', '99999'\n\n"
                    "Greedy by default — use +? for the lazy version."
                ),
                "question": "What does the + quantifier mean in regex?",
                "answers": [
                    "one or more of the preceding element",
                    "one or more",
                    "matches the preceding element one or more times",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Similar to *, but stricter — the element must appear at least once.",
                    "It rejects empty strings.",
                    "The answer is: one or more of the preceding element",
                ],
            },
            {
                "id": "bp_4",
                "type": "quiz",
                "title": "Optional Element",
                "flavor": "Log entries include optional protocol prefixes — 'http' appears in some URLs, not others. You need a quantifier that allows for presence or absence, but not repetition.",
                "lesson": (
                    "? (question mark) — matches the preceding element zero or one times.\n\n"
                    "It makes the preceding element optional.\n\n"
                    "Examples:\n"
                    "  colou?r  → matches both 'color' and 'colour'\n"
                    "  https?   → matches 'http' and 'https'\n\n"
                    "Also used to make quantifiers lazy (non-greedy): *?, +?, {n,m}?"
                ),
                "question": "What does the ? quantifier mean in regex?",
                "answers": [
                    "zero or one of the preceding element",
                    "zero or one",
                    "makes the preceding element optional",
                    "optional",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It makes the preceding character or group optional.",
                    "Think: 'maybe one, maybe none — but not two'.",
                    "The answer is: zero or one of the preceding element",
                ],
            },
            {
                "id": "bp_5",
                "type": "quiz",
                "title": "BOSS: Start of Line",
                "flavor": "The fraud logs all begin with a timestamp. You only want lines where the pattern appears at the very start — not buried somewhere in the middle of a field.",
                "lesson": (
                    "^ (caret) — asserts the start of a line (or start of the string in single-line mode).\n\n"
                    "In multiline mode, ^ matches at the start of each line.\n"
                    "Without multiline mode, it matches only at the start of the entire string.\n\n"
                    "Examples:\n"
                    "  ^ERROR  → matches lines that BEGIN with 'ERROR'\n"
                    "  ^\\d{4}  → matches lines that begin with exactly 4 digits\n\n"
                    "Note: inside a character class [^...], ^ means 'not' — completely different usage."
                ),
                "question": "In regex, what does ^ mean when used outside of a character class?",
                "answers": [
                    "start of the line",
                    "start of line",
                    "beginning of the line",
                    "beginning of line",
                    "asserts the start of a line",
                    "start of string",
                    "beginning of string",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's a positional anchor, not a character match.",
                    "It pins the pattern to a specific position in the string.",
                    "The answer is: start of the line",
                ],
            },
        ],
    },

    "character_classes": {
        "id": "character_classes",
        "name": "The Character Class Workshop",
        "subtitle": "Sets, Ranges & Shorthand",
        "color": "yellow",
        "icon": "◈",
        "commands": ["[abc]", "[^abc]", "[a-z]", "\\d", "\\w", "\\s"],
        "challenges": [
            {
                "id": "cc_1",
                "type": "quiz",
                "title": "The Character Set",
                "flavor": "Transaction codes use letters A, B, or C as prefixes — nothing else. You need a pattern that matches exactly those three options, not an entire alphabet range.",
                "lesson": (
                    "[abc] — character class: matches any one character listed inside the brackets.\n\n"
                    "Examples:\n"
                    "  [aeiou]   → matches any single vowel\n"
                    "  [ABC]     → matches 'A', 'B', or 'C'\n"
                    "  [0-9]     → matches any digit (range shorthand)\n\n"
                    "Order inside the class doesn't matter. [bac] is the same as [abc].\n"
                    "A character class always matches exactly ONE character."
                ),
                "question": "What does [abc] match in a regex?",
                "answers": [
                    "any one of the characters a, b, or c",
                    "any of a, b, or c",
                    "a, b, or c",
                    "one character that is a, b, or c",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Square brackets define a set of allowed characters.",
                    "It matches exactly one character — whichever is listed.",
                    "The answer is: any one of the characters a, b, or c",
                ],
            },
            {
                "id": "cc_2",
                "type": "quiz",
                "title": "The Negated Class",
                "flavor": "You want to flag any transaction code that does NOT start with a digit. The exclusion logic matters — match everything that isn't what you expect.",
                "lesson": (
                    "[^abc] — negated character class: matches any ONE character NOT listed.\n\n"
                    "The ^ inside square brackets means 'not these characters'.\n\n"
                    "Examples:\n"
                    "  [^aeiou]  → matches any consonant (or non-letter)\n"
                    "  [^0-9]    → matches any non-digit\n"
                    "  [^\\n]     → matches any character except a newline\n\n"
                    "Note: [^...] is different from ^ at the start of a pattern (line anchor)."
                ),
                "question": "What does [^abc] match in a regex?",
                "answers": [
                    "any character that is not a, b, or c",
                    "any character except a, b, or c",
                    "not a, b, or c",
                    "any one character not in the set a, b, c",
                ],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "The ^ inside brackets inverts the class.",
                    "It matches any character NOT listed inside the brackets.",
                    "The answer is: any character that is not a, b, or c",
                ],
            },
            {
                "id": "cc_3",
                "type": "quiz",
                "title": "The Range",
                "flavor": "Vendor IDs in the system are lowercase letters only. You need a compact way to express 'any lowercase letter' without listing all 26.",
                "lesson": (
                    "[a-z] — range inside a character class: matches any character in that range.\n\n"
                    "Ranges use ASCII ordering.\n\n"
                    "Common ranges:\n"
                    "  [a-z]   → any lowercase letter\n"
                    "  [A-Z]   → any uppercase letter\n"
                    "  [0-9]   → any digit\n"
                    "  [a-zA-Z0-9]  → any alphanumeric character\n\n"
                    "Ranges can be combined with other characters: [a-z_] matches lowercase letters or underscore."
                ),
                "question": "What does [a-z] match in a regex?",
                "answers": [
                    "any lowercase letter from a to z",
                    "any lowercase letter",
                    "any character from a to z",
                    "a lowercase letter",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "The hyphen inside brackets defines a range between two characters.",
                    "It matches any single character in that range.",
                    "The answer is: any lowercase letter from a to z",
                ],
            },
            {
                "id": "cc_4",
                "type": "quiz",
                "title": "The Digit Shorthand",
                "flavor": "Port numbers, transaction IDs, timestamps — the logs are full of numeric fields. One shorthand class saves you from writing [0-9] every time.",
                "lesson": (
                    "\\d — shorthand character class: matches any digit, equivalent to [0-9].\n\n"
                    "Examples:\n"
                    "  \\d+       → one or more digits\n"
                    "  \\d{4}     → exactly 4 digits\n"
                    "  \\d{1,3}   → 1 to 3 digits\n\n"
                    "The uppercase counterpart \\D matches any NON-digit character.\n\n"
                    "In Python raw strings, write r'\\d' or '\\\\d' to avoid backslash escaping."
                ),
                "question": "What does \\d match in regex?",
                "answers": [
                    "any digit",
                    "any digit character",
                    "any single digit",
                    "[0-9]",
                    "a digit",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a shorthand for a character class you use constantly.",
                    "Think 'd' for digit.",
                    "The answer is: any digit (equivalent to [0-9])",
                ],
            },
            {
                "id": "cc_5",
                "type": "quiz",
                "title": "BOSS: Word Characters",
                "flavor": "Usernames in the NEXUS system follow a strict pattern: letters, digits, and underscores only. One shorthand class captures exactly that set.",
                "lesson": (
                    "\\w — shorthand character class: matches any 'word' character.\n\n"
                    "Equivalent to [a-zA-Z0-9_] in most regex engines.\n\n"
                    "Examples:\n"
                    "  \\w+     → matches a word: 'username', 'file_1', 'NexusCorp'\n"
                    "  \\w{3,8} → matches a word of 3 to 8 characters\n\n"
                    "The uppercase counterpart \\W matches any NON-word character.\n\n"
                    "\\s matches whitespace (spaces, tabs, newlines).\n"
                    "\\S matches any non-whitespace character."
                ),
                "question": "What does \\w match in regex?",
                "answers": [
                    "any word character (letters, digits, underscore)",
                    "any word character",
                    "letters, digits, and underscores",
                    "[a-zA-Z0-9_]",
                    "alphanumeric characters and underscore",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Think 'word' character — the building blocks of identifiers.",
                    "It includes letters (both cases), digits, and one punctuation character.",
                    "The answer is: any word character — letters, digits, and underscore",
                ],
            },
        ],
    },

    "anchors_groups": {
        "id": "anchors_groups",
        "name": "The Anchors and Groups Bunker",
        "subtitle": "Anchors, Capture Groups & Alternation",
        "color": "magenta",
        "icon": "◈",
        "commands": ["$", "\\b", "(group)", "(?:group)", "|"],
        "challenges": [
            {
                "id": "ag_1",
                "type": "quiz",
                "title": "End of Line",
                "flavor": "The fraud entries always terminate with a specific status code. You want to match lines where that code appears at the very end — not mid-line.",
                "lesson": (
                    "$ (dollar sign) — asserts the end of a line (or end of the string).\n\n"
                    "In multiline mode, $ matches at the end of each line.\n\n"
                    "Examples:\n"
                    "  FAIL$    → matches lines that END with 'FAIL'\n"
                    "  \\d+$     → matches lines ending with one or more digits\n\n"
                    "Combined with ^:\n"
                    "  ^\\d+$    → matches lines that consist entirely of digits"
                ),
                "question": "In regex, what does $ mean when used outside a character class?",
                "answers": [
                    "end of the line",
                    "end of line",
                    "end of the string",
                    "end of string",
                    "asserts the end of a line",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a positional anchor — the counterpart to ^.",
                    "It pins the pattern to the end of the string or line.",
                    "The answer is: end of the line",
                ],
            },
            {
                "id": "ag_2",
                "type": "quiz",
                "title": "Word Boundary",
                "flavor": "Searching for 'log' in the audit trails keeps matching 'catalog', 'dialog', 'dialog_id'. You need to match the word 'log' as a standalone word only.",
                "lesson": (
                    "\\b — word boundary anchor: matches the position between a word character and a non-word character.\n\n"
                    "It matches a position, not a character.\n\n"
                    "Examples:\n"
                    "  \\blog\\b  → matches 'log' but NOT 'catalog' or 'logging'\n"
                    "  \\bcat    → matches 'cat' in 'catalog' but not in 'concatenate'\n\n"
                    "\\B (uppercase) matches any position that is NOT a word boundary."
                ),
                "question": "What does \\b match in regex?",
                "answers": [
                    "a word boundary",
                    "word boundary",
                    "the boundary between a word character and a non-word character",
                    "position between word and non-word characters",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's a zero-width assertion — it matches a position, not a character.",
                    "It marks the edge of a word.",
                    "The answer is: a word boundary",
                ],
            },
            {
                "id": "ag_3",
                "type": "quiz",
                "title": "Capture Group",
                "flavor": "The timestamp fields in NEXUS logs follow a pattern. You need to extract the year, month, and day separately. Parentheses create groups you can capture.",
                "lesson": (
                    "(group) — capture group: groups part of a pattern AND captures the matched text.\n\n"
                    "The captured text can be:\n"
                    "  - Referenced by index: \\1, \\2, ...\n"
                    "  - Retrieved in code: match.group(1)\n\n"
                    "Examples:\n"
                    "  (\\d{4})-(\\d{2})-(\\d{2})  → captures year, month, day separately\n"
                    "  (abc)+                   → matches 'abcabcabc' and captures last 'abc'\n\n"
                    "Grouping also affects quantifier scope: (ab)+ matches 'ababab'."
                ),
                "question": "What does (group) do in regex — what are parentheses used for?",
                "answers": [
                    "creates a capture group",
                    "capture group",
                    "groups and captures the matched text",
                    "groups part of the pattern and captures it",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Parentheses serve two functions simultaneously.",
                    "Think: grouping for quantifiers, AND saving what was matched.",
                    "The answer is: creates a capture group — groups the pattern and captures the match",
                ],
            },
            {
                "id": "ag_4",
                "type": "quiz",
                "title": "Non-Capturing Group",
                "flavor": "You need to group alternation options for a quantifier but don't want to capture the match into a group variable. There's a syntax for grouping without capturing.",
                "lesson": (
                    "(?:group) — non-capturing group: groups part of a pattern WITHOUT capturing.\n\n"
                    "Use when you need grouping for structure or quantifiers but don't need the captured value.\n\n"
                    "Examples:\n"
                    "  (?:abc)+      → matches 'abcabcabc' without capturing\n"
                    "  (?:http|ftp)s? → matches 'http', 'https', 'ftp', 'ftps'\n\n"
                    "Benefits:\n"
                    "  - Slightly faster than capture groups\n"
                    "  - Doesn't shift the index of subsequent capture groups"
                ),
                "question": "What does (?:group) mean in regex — how does it differ from (group)?",
                "answers": [
                    "non-capturing group",
                    "a non-capturing group — groups without capturing",
                    "groups the pattern without capturing the match",
                    "groups but does not capture",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The ?: at the start is the key modifier.",
                    "It still groups — it just doesn't save the match.",
                    "The answer is: a non-capturing group",
                ],
            },
            {
                "id": "ag_5",
                "type": "quiz",
                "title": "BOSS: Alternation",
                "flavor": "NEXUS log entries can be flagged as either ERROR or CRITICAL. You need a single pattern that matches either keyword — the regex OR operator.",
                "lesson": (
                    "| (pipe) — alternation operator: matches either the expression on the left OR the right.\n\n"
                    "It has the lowest precedence in regex — it splits the entire expression unless grouped.\n\n"
                    "Examples:\n"
                    "  cat|dog       → matches 'cat' or 'dog'\n"
                    "  ERROR|CRITICAL → matches either keyword\n"
                    "  ^(ERROR|CRITICAL)  → matches lines starting with either keyword\n\n"
                    "Without grouping, cat|dog food matches 'cat' or 'dog food' — not 'cat food'."
                ),
                "question": "What does | (pipe) do in regex?",
                "answers": [
                    "alternation — matches either the left or right expression",
                    "alternation",
                    "matches either the expression on the left or the right",
                    "logical OR",
                    "matches one pattern or another",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's the regex equivalent of logical OR.",
                    "It separates two alternatives — either can satisfy the match.",
                    "The answer is: alternation — matches either the left or right expression",
                ],
            },
        ],
    },

    "quantifiers_advanced": {
        "id": "quantifiers_advanced",
        "name": "The Quantifiers Deep Dive",
        "subtitle": "Exact, Range & Lazy Matching",
        "color": "blue",
        "icon": "◈",
        "commands": ["{n}", "{n,m}", "{n,}", "*?", "+?"],
        "challenges": [
            {
                "id": "qa_1",
                "type": "quiz",
                "title": "Exact Count",
                "flavor": "Transaction IDs in the NEXUS system are exactly 8 characters. You don't want 7, you don't want 9. You need a quantifier for precision.",
                "lesson": (
                    "{n} — exact quantifier: matches the preceding element exactly n times.\n\n"
                    "Examples:\n"
                    "  \\d{4}     → exactly 4 digits: '2024', '0042'\n"
                    "  [A-Z]{3}  → exactly 3 uppercase letters: 'TXN', 'ERR'\n"
                    "  .{8}      → exactly 8 of any character\n\n"
                    "Useful for fixed-width fields, codes, and identifiers."
                ),
                "question": "What does {n} mean in regex (e.g. \\d{4})?",
                "answers": [
                    "exactly n times",
                    "matches exactly n times",
                    "matches the preceding element exactly n times",
                    "exactly 4 times (for {4})",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It specifies an exact repetition count.",
                    "No more, no less — exactly that number.",
                    "The answer is: exactly n times",
                ],
            },
            {
                "id": "qa_2",
                "type": "quiz",
                "title": "Range Count",
                "flavor": "Port numbers range from 1 to 5 digits. You need a quantifier that accepts that entire range — but rejects zero digits and rejects six.",
                "lesson": (
                    "{n,m} — range quantifier: matches the preceding element at least n and at most m times.\n\n"
                    "Examples:\n"
                    "  \\d{1,5}     → 1 to 5 digits: port numbers\n"
                    "  [a-z]{3,8}  → 3 to 8 lowercase letters\n"
                    "  .{0,255}    → 0 to 255 of any character\n\n"
                    "Greedy by default — will match as many as possible up to m.\n"
                    "Add ? for lazy: {n,m}? matches as few as possible."
                ),
                "question": "What does {n,m} mean in regex (e.g. \\d{1,5})?",
                "answers": [
                    "between n and m times",
                    "at least n and at most m times",
                    "n to m times",
                    "matches between n and m times",
                ],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "It sets a floor and a ceiling on repetitions.",
                    "Both bounds are inclusive.",
                    "The answer is: at least n and at most m times",
                ],
            },
            {
                "id": "qa_3",
                "type": "quiz",
                "title": "At Least N",
                "flavor": "Log lines with suspicious activity always contain at least 3 flag codes, sometimes more. You need a quantifier that sets a floor with no ceiling.",
                "lesson": (
                    "{n,} — open-ended quantifier: matches the preceding element at least n times, with no upper limit.\n\n"
                    "Examples:\n"
                    "  \\d{3,}    → 3 or more digits\n"
                    "  [A-Z]{2,} → 2 or more uppercase letters\n"
                    "  .{10,}    → 10 or more of any character\n\n"
                    "Note: \\d{1,} is equivalent to \\d+, and \\d{0,} is equivalent to \\d*."
                ),
                "question": "What does {n,} mean in regex (e.g. \\d{3,})?",
                "answers": [
                    "at least n times",
                    "n or more times",
                    "matches at least n times",
                    "at least n",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "The comma with nothing after it means the upper bound is open.",
                    "It's a floor with no ceiling.",
                    "The answer is: at least n times (n or more)",
                ],
            },
            {
                "id": "qa_4",
                "type": "quiz",
                "title": "The Lazy Star",
                "flavor": "Greedy matching swallowed an entire log line when you only wanted the first tag. You need the match to stop as soon as possible — the lazy variant.",
                "lesson": (
                    "*? — lazy (non-greedy) quantifier: matches zero or more of the preceding element, as few as possible.\n\n"
                    "Default quantifiers are greedy — they match as much as possible.\n"
                    "Adding ? makes them lazy — they match as little as possible.\n\n"
                    "Example:\n"
                    "  Input: <tag>content</tag>\n"
                    "  <.*>   → greedy, matches the entire '<tag>content</tag>'\n"
                    "  <.*?>  → lazy, matches only '<tag>'\n\n"
                    "Lazy quantifiers are critical when parsing structured text like HTML, XML, or log entries."
                ),
                "question": "What does *? mean in regex — how does it differ from *?",
                "answers": [
                    "lazy (non-greedy) zero or more",
                    "lazy star — matches as few characters as possible",
                    "non-greedy zero or more",
                    "matches zero or more times, as few as possible",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The ? after a quantifier switches it from greedy to lazy.",
                    "Lazy means: stop as soon as the overall pattern can match.",
                    "The answer is: lazy (non-greedy) — zero or more, as few as possible",
                ],
            },
            {
                "id": "qa_5",
                "type": "quiz",
                "title": "BOSS: Lazy Plus",
                "flavor": "The transaction parser over-matches because + is greedy. One character makes it lazy. The difference between 'match the first value' and 'match everything through the last value'.",
                "lesson": (
                    "+? — lazy (non-greedy) quantifier: matches one or more of the preceding element, as few as possible.\n\n"
                    "Greedy + matches as much as possible.\n"
                    "Lazy +? matches as little as possible — but still requires at least one match.\n\n"
                    "Example:\n"
                    "  Input: 'amount=100;amount=200;amount=300'\n"
                    "  amount=.+;   → greedy, matches 'amount=100;amount=200;'\n"
                    "  amount=.+?;  → lazy, matches only 'amount=100;'\n\n"
                    "Rule of thumb: if your pattern matches too much, try making it lazy with ?."
                ),
                "question": "What does +? mean in regex — how does it differ from +?",
                "answers": [
                    "lazy (non-greedy) one or more",
                    "lazy plus — matches as few characters as possible",
                    "non-greedy one or more",
                    "matches one or more times, as few as possible",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Add ? to any quantifier to make it lazy.",
                    "It still requires at least one match — but stops as early as possible.",
                    "The answer is: lazy (non-greedy) — one or more, as few as possible",
                ],
            },
        ],
    },

    "lookarounds": {
        "id": "lookarounds",
        "name": "The Lookaround Chamber",
        "subtitle": "Lookahead & Lookbehind Assertions",
        "color": "red",
        "icon": "◈",
        "commands": ["(?=...)", "(?!...)", "(?<=...)", "(?<!...)"],
        "challenges": [
            {
                "id": "la_1",
                "type": "quiz",
                "title": "Positive Lookahead",
                "flavor": "You want to match account numbers only when followed by a debit marker. The debit marker shouldn't be part of the match — just confirmation it's there.",
                "lesson": (
                    "(?=...) — positive lookahead: asserts that what follows matches the pattern, without consuming it.\n\n"
                    "It's a zero-width assertion — it checks but doesn't include the lookahead text in the match.\n\n"
                    "Examples:\n"
                    "  \\d+(?=px)     → matches digits followed by 'px', but doesn't include 'px'\n"
                    "  ACCT(?=_DEBIT) → matches 'ACCT' only when followed by '_DEBIT'\n\n"
                    "Use lookaheads when you need context after a match but don't want to capture the context."
                ),
                "question": "What does (?=...) mean in regex?",
                "answers": [
                    "positive lookahead",
                    "asserts that what follows matches the pattern",
                    "lookahead assertion that checks for what follows without consuming it",
                    "positive lookahead — matches if followed by the pattern",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It's a lookahead — it looks forward without consuming characters.",
                    "The = sign makes it positive: 'this must follow'.",
                    "The answer is: positive lookahead",
                ],
            },
            {
                "id": "la_2",
                "type": "quiz",
                "title": "Negative Lookahead",
                "flavor": "Match all transaction records — except those already flagged as AUDITED. You need to check for the absence of a following pattern.",
                "lesson": (
                    "(?!...) — negative lookahead: asserts that what follows does NOT match the pattern.\n\n"
                    "Zero-width — doesn't consume any characters.\n\n"
                    "Examples:\n"
                    "  \\d+(?!px)      → matches digits NOT followed by 'px'\n"
                    "  ACCT(?!_AUDIT) → matches 'ACCT' only when NOT followed by '_AUDIT'\n\n"
                    "Negative lookaheads are powerful for exclusion logic within a single pattern."
                ),
                "question": "What does (?!...) mean in regex?",
                "answers": [
                    "negative lookahead",
                    "asserts that what follows does not match the pattern",
                    "lookahead that checks the following text is absent",
                    "negative lookahead — matches if NOT followed by the pattern",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The ! makes it negative: 'this must NOT follow'.",
                    "It's the opposite of (?=...) — exclusion rather than inclusion.",
                    "The answer is: negative lookahead",
                ],
            },
            {
                "id": "la_3",
                "type": "quiz",
                "title": "Positive Lookbehind",
                "flavor": "You need to match amounts — but only amounts that are preceded by the currency symbol $. The symbol itself shouldn't be part of the captured match.",
                "lesson": (
                    "(?<=...) — positive lookbehind: asserts that what precedes matches the pattern, without consuming it.\n\n"
                    "Zero-width — checks backwards without including the lookbehind in the match.\n\n"
                    "Examples:\n"
                    "  (?<=\\$)\\d+    → matches digits preceded by a dollar sign (not including the $)\n"
                    "  (?<=NEXUS_)\\w+ → matches words following 'NEXUS_'\n\n"
                    "Most engines require fixed-length lookbehinds (no * or + inside (?<=...))."
                ),
                "question": "What does (?<=...) mean in regex?",
                "answers": [
                    "positive lookbehind",
                    "asserts that what precedes matches the pattern",
                    "lookbehind assertion that checks what came before without consuming it",
                    "positive lookbehind — matches if preceded by the pattern",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It looks backward — checks what came before the current position.",
                    "The <= reads like 'preceded by'.",
                    "The answer is: positive lookbehind",
                ],
            },
            {
                "id": "la_4",
                "type": "quiz",
                "title": "Negative Lookbehind",
                "flavor": "Some transaction amounts are pre-tax, some post-tax. The pre-tax ones are preceded by 'PRE:'. You want amounts that are NOT preceded by that prefix.",
                "lesson": (
                    "(?<!...) — negative lookbehind: asserts that what precedes does NOT match the pattern.\n\n"
                    "Zero-width — doesn't consume characters.\n\n"
                    "Examples:\n"
                    "  (?<!PRE:)\\d+    → matches digits NOT preceded by 'PRE:'\n"
                    "  (?<!un)likely   → matches 'likely' but not 'unlikely'\n\n"
                    "Like positive lookbehind, most engines require fixed-length patterns inside (?<!...)."
                ),
                "question": "What does (?<!...) mean in regex?",
                "answers": [
                    "negative lookbehind",
                    "asserts that what precedes does not match the pattern",
                    "lookbehind that checks the preceding text is absent",
                    "negative lookbehind — matches if NOT preceded by the pattern",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "The <! means 'not preceded by'.",
                    "It's the negative version of (?<=...) — exclusion based on what came before.",
                    "The answer is: negative lookbehind",
                ],
            },
            {
                "id": "la_5",
                "type": "quiz",
                "title": "BOSS: Combining Lookarounds",
                "flavor": "The final extraction filter needs to match transaction amounts that are preceded by '$' AND not followed by '.00' (round numbers hide the fraud). Both conditions must hold simultaneously.",
                "lesson": (
                    "Lookarounds can be combined in a single pattern.\n\n"
                    "Pattern: (?<=\\$)\\d+(?!\\.00)\n\n"
                    "Breaking it down:\n"
                    "  (?<=\\$)  → must be preceded by $\n"
                    "  \\d+      → match one or more digits\n"
                    "  (?!\\.00) → must NOT be followed by .00\n\n"
                    "Multiple lookarounds stack at the same position.\n"
                    "You can use any combination of lookahead/lookbehind, positive/negative.\n\n"
                    "This allows extremely precise matching without capturing context characters."
                ),
                "question": "In the pattern (?<=\\$)\\d+(?!\\.00), what does the pattern match?",
                "answers": [
                    "digits preceded by $ and not followed by .00",
                    "a number preceded by a dollar sign and not followed by .00",
                    "digits after $ that are not followed by .00",
                    "amounts that follow $ and do not end in .00",
                ],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Read each part separately: what comes before? what is matched? what must not follow?",
                    "(?<=\\$) is a positive lookbehind. (?!\\.00) is a negative lookahead.",
                    "The answer is: digits preceded by $ and not followed by .00",
                ],
            },
        ],
    },

    "real_world_patterns": {
        "id": "real_world_patterns",
        "name": "The Real-World Targets",
        "subtitle": "Email, IP, Date, UUID & Log Extraction",
        "color": "green",
        "icon": "◈",
        "commands": ["email", "IP", "date", "UUID", "grep -oE"],
        "challenges": [
            {
                "id": "rw_1",
                "type": "quiz",
                "title": "Match an Email Address",
                "flavor": "The NEXUS logs contain internal email addresses mixed with system noise. You need a regex that reliably extracts them — and rejects the noise.",
                "lesson": (
                    "A basic email regex pattern:\n\n"
                    "  [\\w.+-]+@[\\w-]+\\.[a-zA-Z]{2,}\n\n"
                    "Breaking it down:\n"
                    "  [\\w.+-]+        → one or more word chars, dots, plus, or hyphens (local part)\n"
                    "  @               → literal @ symbol\n"
                    "  [\\w-]+          → one or more word chars or hyphens (domain name)\n"
                    "  \\.              → literal dot\n"
                    "  [a-zA-Z]{2,}    → 2+ letters (TLD: com, org, io, ...)\n\n"
                    "This is a simplified pattern. RFC 5322 emails are more complex in practice."
                ),
                "question": "Which regex best matches a typical email address like user@nexus-corp.com?",
                "answers": [
                    "[\\w.+-]+@[\\w-]+\\.[a-zA-Z]{2,}",
                    r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}",
                    "[\\w.+-]+@[\\w.-]+\\.[a-zA-Z]{2,}",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "It has three main parts: local part, @, and domain.",
                    "The domain has a dot before the TLD.",
                    "The answer is: [\\w.+-]+@[\\w-]+\\.[a-zA-Z]{2,}",
                ],
            },
            {
                "id": "rw_2",
                "type": "quiz",
                "title": "Match an IP Address",
                "flavor": "NEXUS server logs record every connection by IP. Extract all IPv4 addresses — four octets, each 0–255, separated by dots.",
                "lesson": (
                    "A pattern to match IPv4 addresses:\n\n"
                    "  \\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b\n\n"
                    "Breaking it down:\n"
                    "  \\b              → word boundary (no partial matches)\n"
                    "  (?:\\d{1,3}\\.)  → 1-3 digits followed by a dot (non-capturing group)\n"
                    "  {3}             → repeated 3 times\n"
                    "  \\d{1,3}         → final octet\n"
                    "  \\b              → word boundary\n\n"
                    "Note: this matches 999.999.999.999 — validating 0-255 range requires more complex logic."
                ),
                "question": "Which regex matches an IPv4 address (e.g. 192.168.1.100)?",
                "answers": [
                    "\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b",
                    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                    "\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "An IPv4 address has four groups of 1-3 digits, separated by dots.",
                    "Word boundaries prevent partial matches.",
                    "The answer is: \\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b",
                ],
            },
            {
                "id": "rw_3",
                "type": "quiz",
                "title": "Match a Date (YYYY-MM-DD)",
                "flavor": "Transaction timestamps in the NEXUS database use ISO 8601 format. Extract the date portion precisely — four-digit year, two-digit month, two-digit day.",
                "lesson": (
                    "A pattern to match ISO 8601 dates (YYYY-MM-DD):\n\n"
                    "  \\d{4}-\\d{2}-\\d{2}\n\n"
                    "Breaking it down:\n"
                    "  \\d{4}   → exactly 4 digits (year)\n"
                    "  -       → literal hyphen\n"
                    "  \\d{2}   → exactly 2 digits (month)\n"
                    "  -       → literal hyphen\n"
                    "  \\d{2}   → exactly 2 digits (day)\n\n"
                    "For stricter validation, add anchors and range checks:\n"
                    "  ^(19|20)\\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$"
                ),
                "question": "Which regex matches a date in YYYY-MM-DD format (e.g. 2024-03-15)?",
                "answers": [
                    "\\d{4}-\\d{2}-\\d{2}",
                    r"\d{4}-\d{2}-\d{2}",
                    "[0-9]{4}-[0-9]{2}-[0-9]{2}",
                ],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Three groups of digits separated by hyphens.",
                    "Use {n} quantifiers for exact digit counts.",
                    "The answer is: \\d{4}-\\d{2}-\\d{2}",
                ],
            },
            {
                "id": "rw_4",
                "type": "quiz",
                "title": "Match a UUID",
                "flavor": "Container and service identifiers in the NEXUS infrastructure are UUIDs. You need to extract them from mixed log output — 32 hex digits in the 8-4-4-4-12 format.",
                "lesson": (
                    "A pattern to match UUIDs (RFC 4122):\n\n"
                    "  [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n\n"
                    "Breaking it down:\n"
                    "  [0-9a-f]{8}   → 8 hex digits\n"
                    "  -             → literal hyphen\n"
                    "  [0-9a-f]{4}   → 4 hex digits (repeated twice)\n"
                    "  -             → literal hyphen\n"
                    "  [0-9a-f]{4}   → 4 hex digits\n"
                    "  -             → literal hyphen\n"
                    "  [0-9a-f]{12}  → 12 hex digits\n\n"
                    "Add case-insensitive flag or use [0-9a-fA-F] to match uppercase hex."
                ),
                "question": "Which regex matches a UUID like 550e8400-e29b-41d4-a716-446655440000?",
                "answers": [
                    "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                    "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
                    "\\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\\b",
                ],
                "xp": 100,
                "difficulty": "medium",
                "hints": [
                    "UUID format: 8-4-4-4-12 hexadecimal digits separated by hyphens.",
                    "Hex digits are 0-9 and a-f.",
                    "The answer is: [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                ],
            },
            {
                "id": "rw_5",
                "type": "quiz",
                "title": "BOSS: Extract IPs from a Log File",
                "flavor": "Gigabytes of NEXUS system logs. Thousands of lines. You need every IP address that appears — extracted, deduplicated, sorted. One grep command. The clock is running.",
                "lesson": (
                    "To extract all IP addresses from a log file using grep:\n\n"
                    "  grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' logfile.log | sort -u\n\n"
                    "Breaking it down:\n"
                    "  grep -o   → print only the matching part (not the whole line)\n"
                    "  grep -E   → use extended regex (no need to escape +, {}, etc.)\n"
                    "  \\b        → word boundary anchors\n"
                    "  ([0-9]{1,3}\\.){3}  → three octets with dots\n"
                    "  [0-9]{1,3}         → final octet\n"
                    "  | sort -u          → sort and deduplicate\n\n"
                    "The -oE flags combined are the key: -o extracts matches, -E enables extended regex."
                ),
                "question": "Which grep command extracts all unique IP addresses from nexus.log?",
                "answers": [
                    "grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' nexus.log | sort -u",
                    "grep -oE '([0-9]{1,3}\\.){3}[0-9]{1,3}' nexus.log | sort -u",
                    "grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' nexus.log | sort | uniq",
                    "grep -Eo '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' nexus.log | sort -u",
                ],
                "xp": 250,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You need grep's -o flag to print only matching text, not full lines.",
                    "-E enables extended regex so you don't have to escape { } and +.",
                    "The answer is: grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' nexus.log | sort -u",
                ],
            },
        ],
    },
}

ZONE_ORDER = [
    "basic_patterns",
    "character_classes",
    "anchors_groups",
    "quantifiers_advanced",
    "lookarounds",
    "real_world_patterns",
]
