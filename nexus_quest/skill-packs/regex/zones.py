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
                "url": "https://www.regular-expressions.info/tutorial.html",
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
                "url": "https://www.regular-expressions.info/tutorial.html",
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
                "url": "https://www.regular-expressions.info/tutorial.html",
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
                "url": "https://www.regular-expressions.info/tutorial.html",
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
                "url": "https://www.regular-expressions.info/tutorial.html",
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
                "url": "https://www.regular-expressions.info/tutorial.html",
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

    "regex_flags": {
        "id": "regex_flags",
        "name": "The Flag Station",
        "subtitle": "re.IGNORECASE, re.MULTILINE, re.DOTALL & more",
        "color": "magenta",
        "icon": "⚑",
        "commands": ["re.IGNORECASE", "re.MULTILINE", "re.DOTALL", "re.VERBOSE", "re.ASCII"],
        "challenges": [
            {
                "id": "rf_1",
                "type": "quiz",
                "title": "Case Blind",
                "flavor": "The NEXUS error logs use inconsistent casing — 'ERROR', 'error', 'Error'. You need a flag that makes your pattern match regardless of letter case.",
                "lesson": (
                    "re.IGNORECASE (or re.I) — makes the pattern case-insensitive.\n\n"
                    "With this flag, [a-z] also matches uppercase letters, and vice versa.\n\n"
                    "Examples:\n"
                    "  re.search(r'error', log, re.IGNORECASE)\n"
                    "  → matches 'error', 'ERROR', 'Error', 'eRrOr'\n\n"
                    "  re.findall(r'phantom', text, re.I)\n"
                    "  → case-insensitive search for 'phantom'\n\n"
                    "Shorthand: re.I"
                ),
                "question": "Which regex flag makes a pattern match regardless of letter case?",
                "url": "https://www.regular-expressions.info/tutorial.html",
                "answers": [
                    "re.IGNORECASE",
                    "re.I",
                    "IGNORECASE",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It makes uppercase and lowercase equivalent in the pattern.",
                    "Shorthand version is re.I",
                    "The answer is: re.IGNORECASE",
                ],
            },
            {
                "id": "rf_2",
                "type": "quiz",
                "title": "Line by Line",
                "flavor": "The fraud log has thousands of lines. Without a flag, ^ only anchors to the start of the entire string. You need it to anchor to the start of each line.",
                "lesson": (
                    "re.MULTILINE (or re.M) — changes ^ and $ to match at line boundaries.\n\n"
                    "Without re.MULTILINE:\n"
                    "  ^ matches only the very start of the entire string\n"
                    "  $ matches only the very end of the entire string\n\n"
                    "With re.MULTILINE:\n"
                    "  ^ matches at the start of EACH line\n"
                    "  $ matches at the end of EACH line\n\n"
                    "Example:\n"
                    "  re.findall(r'^\\d{4}-\\d{2}-\\d{2}', log, re.MULTILINE)\n"
                    "  → extracts timestamps from the start of every log line\n\n"
                    "Shorthand: re.M"
                ),
                "question": "Which regex flag makes ^ and $ match at the start and end of each line (not just the whole string)?",
                "answers": [
                    "re.MULTILINE",
                    "re.M",
                    "MULTILINE",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "Without this flag, ^ and $ anchor to the entire string.",
                    "With it, they anchor to every individual line.",
                    "The answer is: re.MULTILINE",
                ],
            },
            {
                "id": "rf_3",
                "type": "quiz",
                "title": "Dot Through Newlines",
                "flavor": "The phantom vendor records span multiple lines in the raw data dump. The dot metacharacter skips newlines by default — you need a flag to make it cross line boundaries.",
                "lesson": (
                    "re.DOTALL (or re.S) — makes . match ANY character including newlines.\n\n"
                    "By default, . matches everything except \\n.\n"
                    "With re.DOTALL, . matches \\n as well.\n\n"
                    "Example:\n"
                    "  text = 'BEGIN\\nphantom data\\nEND'\n\n"
                    "  re.search(r'BEGIN.+END', text)              → None\n"
                    "  re.search(r'BEGIN.+END', text, re.DOTALL)   → matches!\n\n"
                    "Common use: matching multi-line blocks of content.\n"
                    "Shorthand: re.S"
                ),
                "question": "Which regex flag makes the . (dot) metacharacter match newline characters as well?",
                "answers": [
                    "re.DOTALL",
                    "re.S",
                    "DOTALL",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "By default, dot does NOT match newlines.",
                    "This flag removes that restriction.",
                    "The answer is: re.DOTALL",
                ],
            },
            {
                "id": "rf_4",
                "type": "quiz",
                "title": "Combine Flags",
                "flavor": "The evidence extraction script needs to search case-insensitively AND match across lines simultaneously. Multiple flags must be combined into one call.",
                "lesson": (
                    "Flags can be combined using the | (bitwise OR) operator.\n\n"
                    "Examples:\n"
                    "  re.search(r'error.+end', text, re.IGNORECASE | re.DOTALL)\n"
                    "  → case-insensitive AND dot matches newlines\n\n"
                    "  re.findall(r'^txn', data, re.MULTILINE | re.IGNORECASE)\n"
                    "  → matches 'txn', 'TXN', 'Txn' at the start of any line\n\n"
                    "Alternative: use inline flags in the pattern:\n"
                    "  r'(?im)^txn'    # (?i) = IGNORECASE, (?m) = MULTILINE\n\n"
                    "Inline flag letters: i=IGNORECASE, m=MULTILINE, s=DOTALL, x=VERBOSE"
                ),
                "question": "How do you combine multiple regex flags in a re.search() call?",
                "answers": [
                    "using | between flags",
                    "re.IGNORECASE | re.MULTILINE",
                    "bitwise OR operator",
                    "pipe operator between flags",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "The same operator used for bitwise OR in Python.",
                    "re.I | re.M | re.S",
                    "The answer is: using | between flags",
                ],
            },
            {
                "id": "rf_5",
                "type": "quiz",
                "title": "Verbose Mode",
                "flavor": "The complex multi-field log pattern is impossible to read in one dense line. There's a flag that lets you add whitespace and comments inside the pattern itself.",
                "lesson": (
                    "re.VERBOSE (or re.X) — allows whitespace and # comments inside patterns.\n\n"
                    "With re.VERBOSE, the regex engine ignores:\n"
                    "  - Unescaped whitespace (spaces, tabs, newlines)\n"
                    "  - Everything after # on a line\n\n"
                    "Example:\n"
                    "  pattern = re.compile(r'''\n"
                    "      \\b                # word boundary\n"
                    "      (\\d{1,3}\\.){3}   # first three octets\n"
                    "      \\d{1,3}          # final octet\n"
                    "      \\b               # word boundary\n"
                    "  ''', re.VERBOSE)\n\n"
                    "Use re.VERBOSE for any pattern you'd otherwise have to comment externally.\n"
                    "Shorthand: re.X"
                ),
                "question": "Which regex flag allows you to add whitespace and # comments inside the pattern for readability?",
                "answers": [
                    "re.VERBOSE",
                    "re.X",
                    "VERBOSE",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It makes long patterns readable by allowing formatting.",
                    "Shorthand: re.X",
                    "The answer is: re.VERBOSE",
                ],
            },
            {
                "id": "rf_boss",
                "type": "quiz",
                "title": "BOSS: Inline Flags",
                "flavor": "You need to embed flags directly inside the pattern string so the flag travels with the pattern even when you can't pass a flags parameter — legacy code integration.",
                "lesson": (
                    "Inline flags — embed flags directly in the pattern using (?flags) syntax.\n\n"
                    "Inline flag syntax:\n"
                    "  (?i)   — re.IGNORECASE\n"
                    "  (?m)   — re.MULTILINE\n"
                    "  (?s)   — re.DOTALL\n"
                    "  (?x)   — re.VERBOSE\n"
                    "  (?im)  — multiple flags combined\n\n"
                    "Examples:\n"
                    "  r'(?i)error'       → case-insensitive 'error'\n"
                    "  r'(?im)^phantom'   → 'phantom' at line start, case-insensitive\n\n"
                    "Inline flags apply to the entire pattern when placed at the start.\n"
                    "They can also be scoped to a group: (?i:error) affects only that group."
                ),
                "question": "What inline flag syntax makes a regex case-insensitive without using the re.IGNORECASE argument?",
                "answers": [
                    "(?i)",
                    "(?i) at the start of the pattern",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Inline flags use a special group syntax at the start of the pattern.",
                    "The letter is the same as the shorthand: i for IGNORECASE.",
                    "The answer is: (?i)",
                ],
            },
        ],
    },

    "python_regex": {
        "id": "python_regex",
        "name": "The Python re Module",
        "subtitle": "re.match, re.search, re.findall, re.sub, re.compile",
        "color": "cyan",
        "icon": "🐍",
        "commands": ["re.match()", "re.search()", "re.findall()", "re.sub()", "re.compile()"],
        "challenges": [
            {
                "id": "pr_1",
                "type": "quiz",
                "title": "Search the String",
                "flavor": "A needle in a haystack — the access token is buried somewhere in a 10,000-character session blob. You need to find the first match anywhere in the string.",
                "lesson": (
                    "re.search(pattern, string) — scans through the string looking for the first match.\n\n"
                    "Returns a Match object if found, or None if not found.\n\n"
                    "Example:\n"
                    "  import re\n"
                    "  m = re.search(r'\\btoken_[a-z0-9]+\\b', session_data)\n"
                    "  if m:\n"
                    "      print(m.group())    # the matched text\n\n"
                    "re.search() scans the entire string.\n"
                    "re.match() only checks at the very beginning — use search for general use."
                ),
                "question": "What re function scans through a string and returns the FIRST match anywhere in it?",
                "url": "https://www.regular-expressions.info/tutorial.html",
                "answers": [
                    "re.search()",
                    "re.search",
                    "search()",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It looks through the entire string, not just the start.",
                    "Returns a Match object or None.",
                    "The answer is: re.search()",
                ],
            },
            {
                "id": "pr_2",
                "type": "quiz",
                "title": "Match from Start",
                "flavor": "Transaction log lines must begin with a timestamp — any line that doesn't is malformed and should be flagged. You need a function that only matches at the beginning.",
                "lesson": (
                    "re.match(pattern, string) — checks for a match ONLY at the start of the string.\n\n"
                    "Unlike re.search(), it does not scan through the string.\n\n"
                    "Example:\n"
                    "  m = re.match(r'\\d{4}-\\d{2}-\\d{2}', log_line)\n"
                    "  if m:\n"
                    "      print('Valid timestamp at start:', m.group())\n"
                    "  else:\n"
                    "      print('MALFORMED: no timestamp at line start')\n\n"
                    "Equivalent to anchoring your pattern with ^:\n"
                    "  re.search(r'^\\d{4}-\\d{2}-\\d{2}', log_line)"
                ),
                "question": "What re function attempts to match a pattern ONLY at the beginning of a string?",
                "answers": [
                    "re.match()",
                    "re.match",
                    "match()",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It only looks at the start — not anywhere in the string.",
                    "Returns None if the pattern doesn't match at position 0.",
                    "The answer is: re.match()",
                ],
            },
            {
                "id": "pr_3",
                "type": "quiz",
                "title": "Find All Matches",
                "flavor": "The evidence package needs every transaction ID extracted from the log — not just the first one. All of them. One call, one result.",
                "lesson": (
                    "re.findall(pattern, string) — returns a list of ALL non-overlapping matches.\n\n"
                    "Returns strings (or tuples if there are capture groups).\n\n"
                    "Examples:\n"
                    "  txn_ids = re.findall(r'TXN-\\d{6}', log_data)\n"
                    "  → ['TXN-004017', 'TXN-004018', 'TXN-004019', ...]\n\n"
                    "  # With a capture group — returns the group, not the full match:\n"
                    "  amounts = re.findall(r'amount=(\\d+\\.\\d{2})', data)\n"
                    "  → ['49999.97', '12345.00', ...]\n\n"
                    "Returns an empty list if no matches are found."
                ),
                "question": "What re function returns a list of ALL matches in a string?",
                "answers": [
                    "re.findall()",
                    "re.findall",
                    "findall()",
                ],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It returns every match — not just the first.",
                    "The result is a list of strings (or tuples if there are groups).",
                    "The answer is: re.findall()",
                ],
            },
            {
                "id": "pr_4",
                "type": "quiz",
                "title": "Substitute and Sanitize",
                "flavor": "The subsidiary codes must be redacted before the evidence files go to the oversight committee. Every occurrence in the document — replaced with '[REDACTED]' automatically.",
                "lesson": (
                    "re.sub(pattern, replacement, string) — replaces all matches with a new string.\n\n"
                    "Returns a new string with substitutions made.\n\n"
                    "Examples:\n"
                    "  clean = re.sub(r'NX-[A-Z]{3}-\\d{4}', '[REDACTED]', report)\n"
                    "  → replaces all subsidiary codes\n\n"
                    "  # Use \\1 backreferences in replacement:\n"
                    "  redacted = re.sub(r'(\\w+)@(\\w+\\.\\w+)', r'[USER]@\\2', emails)\n"
                    "  → keeps domain, replaces username\n\n"
                    "Optional count argument: re.sub(pattern, repl, string, count=1)\n"
                    "  — limits the number of substitutions"
                ),
                "question": "What re function replaces all matches of a pattern in a string with a replacement value?",
                "answers": [
                    "re.sub()",
                    "re.sub",
                    "sub()",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Short for 'substitute'.",
                    "re.sub(pattern, replacement, string)",
                    "The answer is: re.sub()",
                ],
            },
            {
                "id": "pr_5",
                "type": "quiz",
                "title": "Compile for Speed",
                "flavor": "The same IP extraction pattern runs on millions of log lines. Recompiling it on every iteration is waste. One function pre-compiles the pattern into a reusable object.",
                "lesson": (
                    "re.compile(pattern) — pre-compiles a pattern into a regex object for reuse.\n\n"
                    "The compiled object has the same methods: .search(), .match(), .findall(), .sub()\n\n"
                    "Example:\n"
                    "  ip_re = re.compile(r'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b')\n\n"
                    "  for line in massive_log:\n"
                    "      match = ip_re.search(line)    # compiled — no reparse overhead\n"
                    "      if match:\n"
                    "          yield match.group()\n\n"
                    "Benefits:\n"
                    "  - Pattern parsed once, reused many times\n"
                    "  - Cleaner code when a pattern is used in multiple places\n"
                    "  - Allows storing flags with the pattern: re.compile(r'...', re.I)"
                ),
                "question": "What re function pre-compiles a regex pattern into a reusable compiled regex object?",
                "answers": [
                    "re.compile()",
                    "re.compile",
                    "compile()",
                ],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It converts the pattern string into a compiled regex object.",
                    "The compiled object has .search(), .findall(), etc. as methods.",
                    "The answer is: re.compile()",
                ],
            },
            {
                "id": "pr_boss",
                "type": "quiz",
                "title": "BOSS: Extract Named Groups",
                "flavor": "The log parser must extract timestamp, level, and message fields by name — not by index. Named groups make the extraction readable and maintainable across the entire codebase.",
                "lesson": (
                    "Named capture groups — (?P<name>pattern) — let you access matches by name.\n\n"
                    "Syntax: (?P<name>pattern)\n"
                    "Access with: match.group('name') or match.groupdict()\n\n"
                    "Example:\n"
                    "  pattern = re.compile(\n"
                    "      r'(?P<date>\\d{4}-\\d{2}-\\d{2}) (?P<level>\\w+) (?P<msg>.+)'\n"
                    "  )\n"
                    "  m = pattern.match('2024-03-15 ERROR authentication failed')\n"
                    "  m.group('date')    → '2024-03-15'\n"
                    "  m.group('level')   → 'ERROR'\n"
                    "  m.group('msg')     → 'authentication failed'\n\n"
                    "groupdict() returns all named groups as a dictionary."
                ),
                "question": "What syntax defines a named capture group in Python regex, accessible by name via match.group()?",
                "answers": [
                    "(?P<name>pattern)",
                    "(?P<name>...)",
                    "named group syntax: (?P<name>...)",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It looks like a regular group () but with ?P<name> at the start.",
                    "Access it with match.group('name') instead of match.group(1).",
                    "The answer is: (?P<name>pattern)",
                ],
            },
        ],
    },
    "sed_and_grep_regex": {
        "id": "sed_and_grep_regex",
        "name": "The Stream Rewriter",
        "subtitle": "Regex in sed, grep, and awk",
        "color": "green",
        "icon": "🔁",
        "commands": ["grep", "sed", "awk", "perl"],
        "challenges": [
            {
                "id": "sgr_1",
                "type": "quiz",
                "title": "grep -E vs grep -P",
                "flavor": "The operative needs to search a log file for IP addresses using a full regex. Basic grep won't cut it — you need extended or Perl-compatible patterns. Which flag unlocks which?",
                "lesson": (
                    "grep regex modes:\n\n"
                    "  grep 'pattern'        → basic regex (BRE) — limited\n"
                    "  grep -E 'pattern'     → extended regex (ERE) — +, ?, |, () without escaping\n"
                    "  grep -P 'pattern'     → Perl-Compatible Regex (PCRE) — lookaheads, \\d, \\w, etc.\n"
                    "  grep -F 'pattern'     → fixed string, no regex (fastest)\n\n"
                    "ERE equivalents: egrep / grep -E\n"
                    "PCRE: grep -P (not available on all systems, e.g., macOS default grep)\n\n"
                    "Example:\n"
                    "  grep -E '(ERROR|WARN)' app.log\n"
                    "  grep -P '\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}' access.log"
                ),
                "question": "Which grep flag enables Perl-Compatible Regular Expressions (PCRE) with \\d, \\w, and lookaheads?",
                "url": "https://www.regular-expressions.info/tutorial.html",
                "answers": ["grep -P", "-P"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "P for Perl-Compatible.",
                    "-P",
                    "The answer is: -P",
                ],
            },
            {
                "id": "sgr_2",
                "type": "fill_blank",
                "title": "sed Substitution",
                "flavor": "A config file has 'localhost' hardcoded everywhere. The new deployment needs '10.0.0.5'. sed can replace every occurrence in one command — in-place, across the whole file.",
                "lesson": (
                    "sed s command — stream editor substitution:\n\n"
                    "  sed 's/old/new/'          → replace FIRST occurrence per line\n"
                    "  sed 's/old/new/g'         → replace ALL occurrences per line (global)\n"
                    "  sed -i 's/old/new/g' file → edit file IN-PLACE\n"
                    "  sed -i.bak 's/old/new/g'  → in-place with .bak backup\n\n"
                    "Using regex in sed:\n"
                    "  sed 's/[0-9]\\+/NUM/g'    → replace all numbers with NUM (BRE)\n"
                    "  sed -E 's/[0-9]+/NUM/g'   → same with ERE (no escaping needed for +)\n\n"
                    "Example:\n"
                    "  sed -i 's/localhost/10.0.0.5/g' config.yml"
                ),
                "question": "Complete the sed command to replace ALL occurrences of 'localhost' with '10.0.0.5' in-place:\n\nsed ___ 's/localhost/10.0.0.5/g' config.yml",
                "answers": ["-i"],
                "xp": 60,
                "difficulty": "easy",
                "hints": [
                    "The flag that edits the file in-place.",
                    "-i",
                    "The answer is: -i",
                ],
            },
            {
                "id": "sgr_3",
                "type": "quiz",
                "title": "sed Delete Lines",
                "flavor": "The NEXUS log file has hundreds of debug lines that start with 'DEBUG:'. You only want ERROR and WARN lines. sed can delete all matching lines before you pipe the output onward.",
                "lesson": (
                    "sed d command — delete matching lines:\n\n"
                    "  sed '/pattern/d'          → delete lines matching pattern\n"
                    "  sed '/^DEBUG/d'           → delete lines starting with DEBUG\n"
                    "  sed '/^$/d'               → delete blank lines\n"
                    "  sed '5d'                  → delete line 5\n"
                    "  sed '5,10d'               → delete lines 5 through 10\n\n"
                    "Combine with -E for extended regex:\n"
                    "  sed -E '/^(DEBUG|TRACE)/d' app.log    → remove debug and trace lines\n\n"
                    "Invert with grep -v instead for clarity:\n"
                    "  grep -v '^DEBUG' app.log    → same result, more readable"
                ),
                "question": "Which sed command deletes all lines beginning with 'DEBUG:'?",
                "answers": ["sed '/^DEBUG:/d'", "/^DEBUG:/d"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "sed delete command: /pattern/d",
                    "sed '/^DEBUG:/d'",
                    "The answer is: sed '/^DEBUG:/d'",
                ],
            },
            {
                "id": "sgr_4",
                "type": "fill_blank",
                "title": "awk Field Extraction",
                "flavor": "The access.log has space-separated fields: IP, timestamp, method, path, status, bytes. You need to extract just the status codes (field 5) from every line to count 500 errors.",
                "lesson": (
                    "awk — field processor, ideal for structured text.\n\n"
                    "  awk '{print $1}'           → print first field (space-delimited)\n"
                    "  awk '{print $NF}'          → print last field\n"
                    "  awk -F: '{print $1}'       → use : as delimiter (e.g., /etc/passwd)\n"
                    "  awk '/pattern/ {print}'    → print lines matching pattern\n"
                    "  awk '$5 == 500'            → print lines where field 5 equals 500\n\n"
                    "Count matches:\n"
                    "  awk '$5 >= 500 {count++} END {print count}' access.log\n\n"
                    "Example: Extract only HTTP status codes:\n"
                    "  awk '{print $5}' access.log | sort | uniq -c | sort -rn"
                ),
                "question": "Complete the awk command to print only the 5th field from each line of access.log:\n\nawk '{print ___}' access.log",
                "answers": ["$5"],
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "Fields in awk are $1, $2, $3... which one is 5th?",
                    "$5",
                    "The answer is: $5",
                ],
            },
            {
                "id": "sgr_5",
                "type": "quiz",
                "title": "grep -o Extract Matches",
                "flavor": "You need to extract every IP address from a log file — not the whole line, just the IPs. grep -o prints ONLY the matched portion, not the entire line. Combined with a regex, it extracts exactly what you need.",
                "lesson": (
                    "grep -o — print ONLY the matching portion of each line (not the whole line).\n\n"
                    "  grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' access.log\n"
                    "  → prints each IP address, one per line\n\n"
                    "Combine with sort | uniq -c to count occurrences:\n"
                    "  grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' access.log \\\n"
                    "    | sort | uniq -c | sort -rn | head -10\n"
                    "  → top 10 IP addresses by request count\n\n"
                    "Also useful:\n"
                    "  grep -oE '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z]{2,}\\b' file\n"
                    "  → extract all email addresses from a file"
                ),
                "question": "Which grep flag prints ONLY the text that matched the pattern (not the whole line)?",
                "answers": ["grep -o", "-o"],
                "xp": 80,
                "difficulty": "easy",
                "hints": [
                    "Only the matched portion — not the surrounding line.",
                    "-o",
                    "The answer is: -o",
                ],
            },
            {
                "id": "sgr_boss",
                "type": "fill_blank",
                "title": "BOSS: The Log Pipeline",
                "flavor": "You have access.log. You need: extract all IPs, count how many times each appears, sort highest-to-lowest, show top 10. This is a classic ops pipeline. Build it.",
                "lesson": (
                    "The full IP extraction + ranking pipeline:\n\n"
                    "  grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' access.log \\\n"
                    "    | sort | uniq -c | sort -rn | head -10\n\n"
                    "Step by step:\n"
                    "  grep -oE '...'   → extract all IPs, one per line\n"
                    "  | sort           → sort alphabetically (required before uniq)\n"
                    "  | uniq -c        → count consecutive duplicates\n"
                    "  | sort -rn       → sort by count, highest first (-r reverse, -n numeric)\n"
                    "  | head -10       → show top 10\n\n"
                    "This exact pattern appears in real incident response every day."
                ),
                "question": "In the pipeline: grep -oE 'IP_PATTERN' | sort | uniq -c | sort ___ | head -10\nWhat flags sort the counts highest-to-lowest?",
                "answers": ["-rn", "-nr"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Two flags: one for reverse order, one for numeric comparison.",
                    "-rn or -nr",
                    "The answer is: -rn",
                ],
            },
        ],
    },
    "named_groups_and_backreferences": {
        "id": "named_groups_and_backreferences",
        "name": "Named Groups & Backreferences",
        "subtitle": "Capture, Name, and Reuse",
        "color": "magenta",
        "icon": "◈",
        "commands": ["(?P<name>...)", r"\1", "(?P=name)", "(?:...)"],
        "challenges": [
            {
                "id": "ngb_1",
                "type": "quiz",
                "title": "Named Capture Groups",
                "flavor": "NEXUS logs contain structured entries — timestamp, severity level, message — all crammed into one line. Named capture groups let you label each piece of the match so you can retrieve it by name, not position.",
                "lesson": (
                    "(?P<name>...) — named capture group in Python regex.\n\n"
                    "Instead of accessing captures by index (group(1)), you access by name (group('timestamp')).\n\n"
                    "Examples:\n"
                    "  pattern = r'(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})'\n"
                    "  m = re.search(pattern, '2024-03-15')\n"
                    "  m.group('year')   # → '2024'\n"
                    "  m.group('month')  # → '03'\n\n"
                    "Named groups make complex patterns self-documenting and index-independent."
                ),
                "question": "What is the Python syntax for a named capture group called 'host'?",
                "url": "https://www.regular-expressions.info/named.html",
                "options": [
                    "a (?<host>\\w+)",
                    "b (?P<host>\\w+)",
                    "c (?:host:\\w+)",
                    "d (host:\\w+)",
                ],
                "answer": "b",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "Python uses a P prefix inside the angle brackets.",
                    "The syntax is (?P<name>pattern).",
                    "The answer is: (?P<host>\\w+)",
                ],
            },
            {
                "id": "ngb_2",
                "type": "quiz",
                "title": "Numeric Backreferences",
                "flavor": "The NEXUS config files use repeated tokens — an opening tag must match its closing tag exactly. You need to match the same text twice. Backreferences let you reference a previous capture in the same pattern.",
                "lesson": (
                    "\\1, \\2, ... — backreferences to previously captured groups.\n\n"
                    "\\1 refers to whatever group 1 captured. The match only succeeds if the same text appears again.\n\n"
                    "Examples:\n"
                    "  (\\w+)=\\1         → matches 'mode=mode', 'host=host'\n"
                    "  <(\\w+)>.*?</\\1>  → matches XML/HTML tags: <div>...</div>\n\n"
                    "Note: backreferences match the SAME TEXT as the group, not the same pattern."
                ),
                "question": "In the pattern (\\w+):\\s*\\1, what does \\1 do?",
                "url": "https://www.regular-expressions.info/named.html",
                "options": [
                    "a matches any word character sequence",
                    "b matches the literal text captured by group 1",
                    "c matches a backslash followed by 1",
                    "d matches the pattern \\w+ again",
                ],
                "answer": "b",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "A backreference re-matches the captured text — not the pattern.",
                    "\\1 means 'the same string that group 1 captured'.",
                    "The answer is: matches the literal text captured by group 1",
                ],
            },
            {
                "id": "ngb_3",
                "type": "quiz",
                "title": "Named Backreferences",
                "flavor": "You've named your groups for clarity, but you also need to reference them later in the same pattern. Python supports named backreferences — a way to backref by name instead of number.",
                "lesson": (
                    "(?P=name) — named backreference in Python.\n\n"
                    "References the text captured by the named group 'name' earlier in the pattern.\n\n"
                    "Examples:\n"
                    "  (?P<token>\\w+)=(?P=token)\n"
                    "  → matches 'debug=debug', 'host=host'\n\n"
                    "  (?P<tag>\\w+)>.*?</(?P=tag)>\n"
                    "  → matches <div>...</div>, <span>...</span>\n\n"
                    "(?P=name) is equivalent to \\1 but more readable in complex patterns."
                ),
                "question": "How do you write a named backreference to a group called 'token' in Python regex?",
                "url": "https://www.regular-expressions.info/named.html",
                "options": [
                    "a \\token",
                    "b (?=token)",
                    "c (?P=token)",
                    "d \\P{token}",
                ],
                "answer": "c",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "It uses (?P=...) — similar to how named groups use (?P<...>).",
                    "The syntax is (?P=name) — no angle brackets.",
                    "The answer is: (?P=token)",
                ],
            },
            {
                "id": "ngb_4",
                "type": "quiz",
                "title": "Non-Capturing Groups",
                "flavor": "You need to group part of a pattern for alternation or quantification, but you don't want to capture it — it would just pollute your match results. Non-capturing groups give you grouping without the overhead.",
                "lesson": (
                    "(?:...) — non-capturing group.\n\n"
                    "Groups a sub-pattern for quantifiers or alternation without creating a capture group.\n\n"
                    "Examples:\n"
                    "  (?:https?|ftp)://  → groups the protocol alternation — not captured\n"
                    "  (?:\\d{1,3}\\.){3}\\d{1,3}  → matches an IP address, groups the repeating octet\n\n"
                    "Use (?:...) when you need grouping but don't need the text later.\n"
                    "Keeps group numbering clean and avoids clutter in m.groups()."
                ),
                "question": "What is the difference between (...) and (?:...) in regex?",
                "url": "https://www.regular-expressions.info/named.html",
                "options": [
                    "a (?:...) is a named group, (...) is unnamed",
                    "b (?:...) groups without capturing, (...) captures",
                    "c (?:...) is a lookahead, (...) is a capture group",
                    "d they are identical",
                ],
                "answer": "b",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "The colon after ? signals non-capturing.",
                    "(?:...) still groups for quantifiers/alternation — it just doesn't save the match.",
                    "The answer is: (?:...) groups without capturing, (...) captures",
                ],
            },
            {
                "id": "ngb_5",
                "type": "fill_blank",
                "title": "Groups in re.sub()",
                "flavor": "The NEXUS log format needs reformatting: 'YYYY-MM-DD' must become 'DD/MM/YYYY'. Named groups make the substitution pattern readable. Fill in the replacement string.",
                "lesson": (
                    "Named groups can be referenced in re.sub() replacement strings using \\g<name>.\n\n"
                    "Example — swap date format YYYY-MM-DD → DD/MM/YYYY:\n\n"
                    "  pattern = r'(?P<y>\\d{4})-(?P<m>\\d{2})-(?P<d>\\d{2})'\n"
                    "  result = re.sub(pattern, r'\\g<d>/\\g<m>/\\g<y>', text)\n\n"
                    "Numeric group refs in replacements:\n"
                    "  re.sub(r'(\\w+)@(\\w+)', r'\\2@\\1', s)  → swaps username and domain\n\n"
                    "\\g<name> syntax avoids ambiguity when a group ref is followed by digits."
                ),
                "question": "To reference a named group called 'year' in a re.sub() replacement string, you write \\g<___>.",
                "url": "https://www.regular-expressions.info/named.html",
                "answers": ["year"],
                "xp": 90,
                "difficulty": "medium",
                "hints": [
                    "The syntax mirrors the group name directly.",
                    "\\g<name> — the name goes inside the angle brackets.",
                    "The answer is: year",
                ],
            },
            {
                "id": "ngb_boss",
                "type": "fill_blank",
                "title": "BOSS: Named Group Log Parser",
                "flavor": "CIPHER drops a NEXUS access log line on your screen: '2024-11-07 ERROR nexus-auth: invalid token from 10.0.0.42'. You need to extract timestamp, level, service, and message as named groups. One pattern. Name every part.",
                "lesson": (
                    "A named-group log parser:\n\n"
                    "  log_pattern = re.compile(\n"
                    "      r'(?P<ts>\\d{4}-\\d{2}-\\d{2})\\s+'\n"
                    "      r'(?P<level>\\w+)\\s+'\n"
                    "      r'(?P<svc>[\\w-]+):\\s+'\n"
                    "      r'(?P<msg>.+)'\n"
                    "  )\n"
                    "  m = log_pattern.search(line)\n"
                    "  m.groupdict()  # → {'ts': '2024-11-07', 'level': 'ERROR', ...}\n\n"
                    "Named groups + groupdict() is the cleanest way to parse structured logs in Python."
                ),
                "question": "To retrieve all named captures as a dict from a match object m, you call m.___().",
                "url": "https://www.regular-expressions.info/named.html",
                "answers": ["groupdict"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It returns a dictionary mapping group names to matched strings.",
                    "The method name combines 'group' and 'dict'.",
                    "The answer is: groupdict",
                ],
            },
        ],
    },
    "substitution_and_replace": {
        "id": "substitution_and_replace",
        "name": "Substitution & Replace",
        "subtitle": "Rewrite the Data Stream",
        "color": "yellow",
        "icon": "◈",
        "commands": ["re.sub()", r"\1", "sed s///", "/g", "count="],
        "challenges": [
            {
                "id": "sr_1",
                "type": "quiz",
                "title": "re.sub() Basics",
                "flavor": "The NEXUS exfil pipeline is encoding user IDs as 'USR_12345'. Ops needs them as 'USER-12345' for the next system. One re.sub() call rewrites all of them across the entire log in a single pass.",
                "lesson": (
                    "re.sub(pattern, repl, string, count=0, flags=0) — replaces matches with repl.\n\n"
                    "  re.sub(r'USR_(\\d+)', r'USER-\\1', log)\n"
                    "  → replaces all 'USR_12345' with 'USER-12345'\n\n"
                    "Parameters:\n"
                    "  pattern — regex to match\n"
                    "  repl    — replacement string (can include \\1 backrefs)\n"
                    "  string  — input string\n"
                    "  count   — max replacements (0 = unlimited)\n\n"
                    "Returns the modified string. The original is not changed."
                ),
                "question": "What does re.sub(r'\\d+', 'NUM', text) do?",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "options": [
                    "a replaces the first number in text with 'NUM'",
                    "b replaces all numbers in text with 'NUM'",
                    "c counts the numbers in text",
                    "d returns a list of numbers found in text",
                ],
                "answer": "b",
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "By default re.sub replaces every match, not just the first.",
                    "The count parameter limits replacements — default is 0 meaning unlimited.",
                    "The answer is: replaces all numbers in text with 'NUM'",
                ],
            },
            {
                "id": "sr_2",
                "type": "quiz",
                "title": "Backreferences in Replacements",
                "flavor": "Reformatting the stolen credential dump: all entries are 'last_first' but the evidence system needs 'first last'. You need to swap two captured groups in the replacement.",
                "lesson": (
                    "In re.sub() replacement strings, use \\1, \\2 to insert captured groups.\n\n"
                    "  re.sub(r'(\\w+)_(\\w+)', r'\\2 \\1', name)\n"
                    "  'smith_john' → 'john smith'\n\n"
                    "Named groups use \\g<name>:\n"
                    "  re.sub(r'(?P<last>\\w+)_(?P<first>\\w+)', r'\\g<first> \\g<last>', name)\n"
                    "  → same result, more readable\n\n"
                    "\\g<1> can also be used when a numeric ref is followed by digits: \\g<1>0 not \\10"
                ),
                "question": "In re.sub(r'(\\w+)@(\\w+)', r'\\2@\\1', s), what does the replacement do?",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "options": [
                    "a removes the @ symbol",
                    "b inserts \\2 and \\1 as literal strings",
                    "c swaps the text before and after @",
                    "d duplicates the entire match",
                ],
                "answer": "c",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "\\2 and \\1 refer to the captured groups in reverse order.",
                    "Group 1 is before @, group 2 is after @.",
                    "The answer is: swaps the text before and after @",
                ],
            },
            {
                "id": "sr_3",
                "type": "quiz",
                "title": "Limiting Replacements with count",
                "flavor": "A redaction script must replace only the FIRST occurrence of a sensitive token on each line — replacing all would corrupt the document structure. The count parameter gives you that control.",
                "lesson": (
                    "re.sub() accepts a count parameter to limit replacements:\n\n"
                    "  re.sub(r'SECRET', '[REDACTED]', text, count=1)\n"
                    "  → replaces only the FIRST match\n\n"
                    "  re.sub(r'SECRET', '[REDACTED]', text, count=3)\n"
                    "  → replaces at most the first 3 matches\n\n"
                    "Default count=0 means no limit — replace all.\n\n"
                    "Equivalent in sed: s/pattern/repl/ (first only) vs s/pattern/repl/g (global)"
                ),
                "question": "What does count=1 do in re.sub(pattern, repl, text, count=1)?",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "options": [
                    "a raises an error if more than 1 match exists",
                    "b replaces only the first match",
                    "c replaces all matches, returning a count of 1",
                    "d matches only strings of length 1",
                ],
                "answer": "b",
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "count limits how many replacements are made.",
                    "count=1 means stop after the first replacement.",
                    "The answer is: replaces only the first match",
                ],
            },
            {
                "id": "sr_4",
                "type": "quiz",
                "title": "sed Substitution with Groups",
                "flavor": "The NEXUS shell script needs to reformat date strings in a log file in-place. sed's substitution command supports backreferences — the same concept as Python, just different syntax.",
                "lesson": (
                    "sed substitution with backreferences:\n\n"
                    "  sed 's/\\([0-9]\\{4\\}\\)-\\([0-9]\\{2\\}\\)/\\2-\\1/' file\n"
                    "  → swaps year and month using \\1, \\2\n\n"
                    "In ERE mode (sed -E), groups don't need escaping:\n"
                    "  sed -E 's/([0-9]{4})-([0-9]{2})/\\2-\\1/' file\n\n"
                    "The /g flag replaces ALL occurrences on each line:\n"
                    "  sed -E 's/foo/bar/g' file   → replaces all 'foo' with 'bar'\n\n"
                    "Without /g, only the first match per line is replaced."
                ),
                "question": "In sed, what flag at the end of s/pattern/repl/ replaces ALL matches on a line (not just the first)?",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "options": [
                    "a /a",
                    "b /i",
                    "c /g",
                    "d /n",
                ],
                "answer": "c",
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "It's a single letter that stands for 'global'.",
                    "Without it, only the first match per line is replaced.",
                    "The answer is: /g",
                ],
            },
            {
                "id": "sr_5",
                "type": "quiz",
                "title": "Callable Replacement in re.sub()",
                "flavor": "You need to redact all credit card numbers in the log but preserve the last 4 digits: '4111-1111-1111-1234' → 'XXXX-XXXX-XXXX-1234'. A static replacement string can't compute this — but a function can.",
                "lesson": (
                    "re.sub() accepts a callable as the replacement:\n\n"
                    "  def redact_card(m):\n"
                    "      return 'XXXX-XXXX-XXXX-' + m.group(1)\n\n"
                    "  re.sub(r'\\d{4}-\\d{4}-\\d{4}-(\\d{4})', redact_card, text)\n\n"
                    "The function receives the match object and returns the replacement string.\n\n"
                    "This is powerful for:\n"
                    "  - case transformations (m.group().upper())\n"
                    "  - computed replacements based on match content\n"
                    "  - lookups against a dictionary\n\n"
                    "Lambda works too: re.sub(r'\\w+', lambda m: m.group().upper(), text)"
                ),
                "question": "When re.sub() is given a function as the replacement argument, what does that function receive?",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "options": [
                    "a the matched string as a plain str",
                    "b the match object",
                    "c the start and end positions of the match",
                    "d the pattern and the input string",
                ],
                "answer": "b",
                "xp": 90,
                "difficulty": "medium",
                "hints": [
                    "The function receives more than just the string — it gets the full match context.",
                    "You can call .group(), .start(), .end() on what's passed in.",
                    "The answer is: the match object",
                ],
            },
            {
                "id": "sr_boss",
                "type": "fill_blank",
                "title": "BOSS: Mass Log Redaction",
                "flavor": "CIPHER sends the order: sanitize the entire NEXUS transaction log. Every email address must be replaced with '[EMAIL]'. One re.sub() call, full file content, no survivors.",
                "lesson": (
                    "Full email redaction with re.sub():\n\n"
                    "  email_pat = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}'\n"
                    "  clean = re.sub(email_pat, '[EMAIL]', raw_log)\n\n"
                    "re.sub returns a new string — the original is unchanged.\n\n"
                    "To also count replacements, use re.subn():\n"
                    "  clean, n = re.subn(email_pat, '[EMAIL]', raw_log)\n"
                    "  print(f'{n} addresses redacted')\n\n"
                    "re.subn() is identical to re.sub() but returns a tuple (new_string, count)."
                ),
                "question": "re.sub() returns the modified string. To also get the NUMBER of replacements made, use re.___(pattern, repl, string) instead.",
                "url": "https://www.regular-expressions.info/replacebackref.html",
                "answers": ["subn"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "The function name is a variation of re.sub with an extra letter.",
                    "It returns a tuple: (new_string, count).",
                    "The answer is: subn",
                ],
            },
        ],
    },
    "regex_in_javascript": {
        "id": "regex_in_javascript",
        "name": "Regex in JavaScript",
        "subtitle": "Client-Side Pattern Hacking",
        "color": "bright_yellow",
        "icon": "◈",
        "commands": ["/pattern/flags", ".match()", ".replace()", "RegExp.test()", ".exec()"],
        "challenges": [
            {
                "id": "rjs_1",
                "type": "quiz",
                "title": "JS Regex Literal Syntax",
                "flavor": "The NEXUS web app's client-side validation is running JavaScript. You're reading the source. Regex looks different here — no re.compile(), no raw strings. JS has its own inline syntax.",
                "lesson": (
                    "In JavaScript, regex can be written as literals using forward slashes:\n\n"
                    "  /pattern/flags\n\n"
                    "Examples:\n"
                    "  /\\d+/g          → matches one or more digits, globally\n"
                    "  /^hello/i        → matches 'hello' at start, case-insensitive\n"
                    "  /[a-z]{3}/gi    → matches 3-letter sequences, global + case-insensitive\n\n"
                    "No need to escape backslashes twice (unlike Python strings):\n"
                    "  Python: re.compile(r'\\d+')   or  re.compile('\\\\d+')\n"
                    "  JS:     /\\d+/\n\n"
                    "You can also use: new RegExp('\\\\d+', 'g') for dynamic patterns."
                ),
                "question": "How do you write a JavaScript regex literal that matches one or more digits globally?",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "options": [
                    "a re.compile('\\\\d+', 'g')",
                    "b /\\d+/g",
                    "c regex('\\d+', global=True)",
                    "d '\\d+'",
                ],
                "answer": "b",
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "JS regex literals use forward slashes as delimiters.",
                    "Flags come after the closing slash.",
                    "The answer is: /\\d+/g",
                ],
            },
            {
                "id": "rjs_2",
                "type": "quiz",
                "title": "String.match() vs RegExp.test()",
                "flavor": "Two different tasks: one script needs to extract all matching tokens from a payload string, another just needs a yes/no — does this string contain a suspicious pattern? Two methods, two jobs.",
                "lesson": (
                    "JavaScript offers several ways to use regex:\n\n"
                    "  str.match(regex)\n"
                    "  → returns array of matches (or null if none)\n"
                    "  → with /g flag: returns all matches as an array\n"
                    "  → without /g: returns first match + groups\n\n"
                    "  regex.test(str)\n"
                    "  → returns true or false — does the pattern match?\n"
                    "  → fastest option when you only need a boolean result\n\n"
                    "Examples:\n"
                    "  'abc123'.match(/\\d+/)     // → ['123']\n"
                    "  'abc123'.match(/\\d+/g)    // → ['123']\n"
                    "  /\\d+/.test('abc123')      // → true\n"
                    "  /\\d+/.test('abcdef')      // → false"
                ),
                "question": "Which JavaScript method returns true or false based on whether a pattern matches a string?",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "options": [
                    "a str.match(regex)",
                    "b str.search(regex)",
                    "c regex.test(str)",
                    "d regex.exec(str)",
                ],
                "answer": "c",
                "xp": 70,
                "difficulty": "easy",
                "hints": [
                    "You want a boolean — true or false.",
                    "The method is called on the regex object, not the string.",
                    "The answer is: regex.test(str)",
                ],
            },
            {
                "id": "rjs_3",
                "type": "quiz",
                "title": "String.replace() with Regex",
                "flavor": "The injected payload in the NEXUS app uses double-encoded spaces (%20%20). You need to normalize it — replace all occurrences of %20 with a real space. JS String.replace() takes a regex.",
                "lesson": (
                    "str.replace(regex, replacement) — replaces matches in a string.\n\n"
                    "  'foo bar foo'.replace(/foo/g, 'baz')  // → 'baz bar baz'\n\n"
                    "Without /g, only the first match is replaced:\n"
                    "  'foo bar foo'.replace(/foo/, 'baz')   // → 'baz bar foo'\n\n"
                    "Backreferences in replacement strings use $1, $2 (NOT \\1 like Python/sed):\n"
                    "  'john_smith'.replace(/(\\w+)_(\\w+)/, '$2 $1')  // → 'smith john'\n\n"
                    "Named groups in JS (ES2018+): $<name>\n"
                    "  '2024-03-15'.replace(/(?<y>\\d{4})-(?<m>\\d{2})-(?<d>\\d{2})/, '$<d>/$<m>/$<y>')"
                ),
                "question": "In JavaScript String.replace(), how do you reference capture group 1 in the replacement string?",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "options": [
                    "a \\1",
                    "b %1",
                    "c $1",
                    "d @1",
                ],
                "answer": "c",
                "xp": 80,
                "difficulty": "medium",
                "hints": [
                    "JS uses a different prefix than Python or sed for backrefs in replacements.",
                    "It's a dollar sign followed by the group number.",
                    "The answer is: $1",
                ],
            },
            {
                "id": "rjs_4",
                "type": "quiz",
                "title": "RegExp.exec() and Iterating Matches",
                "flavor": "The NEXUS exfil data has multiple session tokens on a single line. str.match(/pattern/g) gives you the strings, but you need the index positions too. exec() in a loop gives you full match objects.",
                "lesson": (
                    "regex.exec(str) — returns a match object for the next match.\n\n"
                    "With the /g flag, exec() remembers position via regex.lastIndex.\n"
                    "Calling it in a loop iterates over all matches:\n\n"
                    "  const re = /SESSION-(\\w+)/g;\n"
                    "  let m;\n"
                    "  while ((m = re.exec(str)) !== null) {\n"
                    "    console.log(m[0], 'at index', m.index);\n"
                    "    console.log('token:', m[1]);\n"
                    "  }\n\n"
                    "m[0]     — full match\n"
                    "m[1]     — capture group 1\n"
                    "m.index  — position in string\n\n"
                    "Modern alternative: str.matchAll(/pattern/g) returns an iterator."
                ),
                "question": "When using regex.exec(str) with /g in a loop, what property of the match object gives the position of the match in the string?",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "options": [
                    "a m.position",
                    "b m.start",
                    "c m.index",
                    "d m.offset",
                ],
                "answer": "c",
                "xp": 90,
                "difficulty": "medium",
                "hints": [
                    "It's a property on the match array object.",
                    "Think of the array index concept.",
                    "The answer is: m.index",
                ],
            },
            {
                "id": "rjs_5",
                "type": "quiz",
                "title": "Python vs JS Regex Gotchas",
                "flavor": "You've been switching between Python and JavaScript all shift. The patterns look similar but behave differently in edge cases. CIPHER warns: 'Know your engine. A wrong assumption costs the op.'",
                "lesson": (
                    "Key differences between Python and JavaScript regex:\n\n"
                    "Named groups:\n"
                    "  Python: (?P<name>...)   backreference: (?P=name)\n"
                    "  JS:     (?<name>...)    backreference: \\k<name>\n\n"
                    "Substitution backreferences:\n"
                    "  Python re.sub:  \\1 or \\g<name>\n"
                    "  JS replace():   $1 or $<name>\n\n"
                    "Lookahead/Lookbehind: both engines support (?=), (?!), (?<=), (?<!).\n"
                    "  (JS lookbehind requires ES2018+)\n\n"
                    "No re.VERBOSE in JS — use comments in code instead.\n\n"
                    "Sticky flag: JS has /y (sticky) — matches only at lastIndex, no Python equiv."
                ),
                "question": "In JavaScript (ES2018+), what is the syntax for a named capture group called 'host'?",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "options": [
                    "a (?P<host>\\w+)",
                    "b (?:host:\\w+)",
                    "c (?<host>\\w+)",
                    "d [host:\\w+]",
                ],
                "answer": "c",
                "xp": 90,
                "difficulty": "medium",
                "hints": [
                    "JS named groups do NOT use the P prefix that Python uses.",
                    "Angle brackets still surround the name.",
                    "The answer is: (?<host>\\w+)",
                ],
            },
            {
                "id": "rjs_boss",
                "type": "fill_blank",
                "title": "BOSS: JS Token Extractor",
                "flavor": "The NEXUS client-side script validates session tokens matching /^SID-[A-Z0-9]{16}$/. You need to extract ALL matches from a multi-token string using str.matchAll(). What flag is required on the regex for matchAll() to work?",
                "lesson": (
                    "str.matchAll(regex) requires the /g flag — without it, a TypeError is thrown.\n\n"
                    "  const tokens = [...str.matchAll(/SID-[A-Z0-9]{16}/g)];\n"
                    "  tokens.forEach(m => console.log(m[0], 'at', m.index));\n\n"
                    "matchAll() returns an iterator of full match objects (unlike match(/g) which returns only strings).\n\n"
                    "Each result has:\n"
                    "  m[0]     — the full match\n"
                    "  m[1]...  — capture groups\n"
                    "  m.index  — position\n"
                    "  m.input  — the original string\n\n"
                    "Use the spread operator [...] or a for...of loop to iterate the results."
                ),
                "question": "str.matchAll(regex) requires the regex to have the ___ flag, otherwise it throws a TypeError.",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
                "answers": ["g"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's the global flag.",
                    "Without it, TypeError: String.prototype.matchAll called with a non-global RegExp argument.",
                    "The answer is: g",
                ],
            },
        ],
    },
    "advanced_techniques": {
        "id": "advanced_techniques",
        "name": "Advanced Techniques",
        "subtitle": "Performance, Precision & Power",
        "color": "red",
        "icon": "◈",
        "commands": ["(?>...)", "re.compile()", "?+", "*+", "catastrophic backtracking"],
        "challenges": [
            {
                "id": "at_1",
                "type": "quiz",
                "title": "Catastrophic Backtracking",
                "flavor": "A NEXUS intrusion detection rule uses the pattern (a+)+ against user input. An attacker sends a crafted 30-character string and the server hangs for 30 seconds. You've just discovered a ReDoS vulnerability.",
                "lesson": (
                    "Catastrophic backtracking (ReDoS) occurs when a regex backtracks exponentially.\n\n"
                    "The classic vulnerable pattern: (a+)+\n\n"
                    "For input 'aaaaaaaaaaaaaaaaaab', the engine tries every possible way to split\n"
                    "the a's between the outer and inner + — exponential time complexity.\n\n"
                    "Vulnerable patterns typically have:\n"
                    "  - Nested quantifiers: (a+)+, (a|a)+, (a*)*\n"
                    "  - Overlapping alternatives: (a|ab)+\n\n"
                    "Defenses:\n"
                    "  - Atomic groups (if engine supports it): (?>a+)\n"
                    "  - Possessive quantifiers: a++ (Python: not built-in, use regex module)\n"
                    "  - Rewrite the pattern to eliminate ambiguity\n"
                    "  - Set a timeout on regex execution"
                ),
                "question": "Why is the pattern (a+)+ considered dangerous for regex engines?",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "options": [
                    "a it matches too broadly and produces false positives",
                    "b it can cause exponential backtracking on certain non-matching inputs",
                    "c it requires the DOTALL flag to work correctly",
                    "d it only works in Python, not JavaScript",
                ],
                "answer": "b",
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "The danger is in the engine's work, not the matches it finds.",
                    "Think about what happens when the input does NOT match — the engine must try everything.",
                    "The answer is: it can cause exponential backtracking on certain non-matching inputs",
                ],
            },
            {
                "id": "at_2",
                "type": "quiz",
                "title": "Atomic Groups",
                "flavor": "You need to fix the ReDoS vulnerability. The operation needs a pattern that matches possessively — once the group matches, it never gives back characters to the backtracking engine. Atomic groups lock in the match.",
                "lesson": (
                    "Atomic groups (?>...) prevent backtracking into the group once it has matched.\n\n"
                    "  (?>a+)b  — matches one or more 'a' atomically, then 'b'\n"
                    "  → if 'b' fails after the atomic group, the engine does NOT backtrack into (?>a+)\n\n"
                    "Available in: PCRE, Java, .NET — NOT natively in Python's re module.\n"
                    "Python workaround: use the third-party 'regex' module which supports (?>...).\n\n"
                    "Atomic groups eliminate catastrophic backtracking in vulnerable patterns:\n"
                    "  Vulnerable:  (a+)+  \n"
                    "  Fixed:       (?>a+)+"
                ),
                "question": "What does an atomic group (?>...) prevent in a regex engine?",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "options": [
                    "a matching across multiple lines",
                    "b capturing the group's content",
                    "c backtracking into the group after it has matched",
                    "d using the group more than once",
                ],
                "answer": "c",
                "xp": 110,
                "difficulty": "hard",
                "hints": [
                    "Atomic means all-or-nothing — once matched, never given back.",
                    "The engine cannot go back inside the group to try alternatives.",
                    "The answer is: backtracking into the group after it has matched",
                ],
            },
            {
                "id": "at_3",
                "type": "quiz",
                "title": "Possessive Quantifiers",
                "flavor": "In PCRE and Java regex, possessive quantifiers offer a more concise way to prevent backtracking. They look like regular quantifiers with a + appended. The NEXUS rule engine uses PCRE — you can apply these directly.",
                "lesson": (
                    "Possessive quantifiers match as much as possible and NEVER give back.\n\n"
                    "  a++   — possessive +: one or more a, no backtracking\n"
                    "  a*+   — possessive *: zero or more a, no backtracking\n"
                    "  a?+   — possessive ?: zero or one a, no backtracking\n"
                    "  a{3,5}+  — possessive {n,m}: no backtracking\n\n"
                    "Available in: PCRE, Java, .NET regex module — NOT Python's built-in re.\n"
                    "Python's 'regex' module supports possessive quantifiers.\n\n"
                    "Equivalent to wrapping in an atomic group:\n"
                    "  a++ is equivalent to (?>a+)"
                ),
                "question": "In PCRE, what does the pattern \\d++ match compared to \\d+?",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "options": [
                    "a matches the same text but twice as fast",
                    "b matches one or more digits without allowing any backtracking",
                    "c matches two or more digits",
                    "d matches digits followed by a literal +",
                ],
                "answer": "b",
                "xp": 110,
                "difficulty": "hard",
                "hints": [
                    "The extra + makes it possessive — it grabs and holds.",
                    "The difference is in backtracking behavior, not what it matches initially.",
                    "The answer is: matches one or more digits without allowing any backtracking",
                ],
            },
            {
                "id": "at_4",
                "type": "quiz",
                "title": "Regex Debugging Strategy",
                "flavor": "Your extraction pattern returns nothing on the production log but works fine on your test string. CIPHER: 'Debug systematically. Don't guess. Strip the pattern down to its core and build back up.'",
                "lesson": (
                    "Systematic regex debugging approach:\n\n"
                    "1. Simplify: strip to the minimal pattern and add pieces back\n"
                    "2. Test anchors: remove ^ and $ first — does the core match?\n"
                    "3. Check flags: is MULTILINE needed? DOTALL?\n"
                    "4. Inspect the input: print repr(text) to expose \\r, \\n, invisible chars\n"
                    "5. Use re.DEBUG flag: re.compile(pattern, re.DEBUG) prints the parse tree\n"
                    "6. Use regex101.com or debuggex.com for visual debugging\n"
                    "7. Check for double-escaping: raw string r'\\d+' vs '\\\\d+'\n\n"
                    "re.DEBUG example:\n"
                    "  import re\n"
                    "  re.compile(r'(?P<ts>\\d{4}-\\d{2})', re.DEBUG)"
                ),
                "question": "Which Python flag passed to re.compile() prints a debug parse tree of the regex?",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "options": [
                    "a re.VERBOSE",
                    "b re.TRACE",
                    "c re.DEBUG",
                    "d re.INFO",
                ],
                "answer": "c",
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "It's a built-in re flag that outputs the compiled pattern structure.",
                    "The flag name literally describes its purpose.",
                    "The answer is: re.DEBUG",
                ],
            },
            {
                "id": "at_5",
                "type": "quiz",
                "title": "re.compile() for Performance",
                "flavor": "The NEXUS log processor runs the same pattern against 50,000 lines per second. Without caching, the regex engine re-parses the pattern on every call. CIPHER: 'Compile once. Match a million times.'",
                "lesson": (
                    "re.compile(pattern, flags) — pre-compiles a regex for reuse.\n\n"
                    "  log_re = re.compile(r'(?P<ip>\\d{1,3}(?:\\.\\d{1,3}){3})', re.MULTILINE)\n\n"
                    "  for line in log_file:\n"
                    "      m = log_re.search(line)   # no re-parsing on each call\n\n"
                    "Benefits:\n"
                    "  - Python caches the last ~512 compiled patterns automatically\n"
                    "  - Explicit compile is clearer and guaranteed cached\n"
                    "  - Compiled object exposes same methods: .search(), .match(), .findall(), .sub()\n\n"
                    "Python's internal cache handles simple cases, but for hot loops\n"
                    "with many different patterns, explicit re.compile() is safer."
                ),
                "question": "What is the primary performance benefit of using re.compile() when applying the same pattern to many strings?",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "options": [
                    "a the compiled pattern matches faster due to JIT compilation",
                    "b the pattern is parsed once instead of on every call",
                    "c compiled patterns skip backtracking entirely",
                    "d re.compile() parallelizes the matching across CPU cores",
                ],
                "answer": "b",
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "The gain comes from parsing, not matching speed.",
                    "Without compile, the pattern string is parsed into a finite automaton on every use.",
                    "The answer is: the pattern is parsed once instead of on every call",
                ],
            },
            {
                "id": "at_boss",
                "type": "fill_blank",
                "title": "BOSS: Identify the ReDoS Pattern",
                "flavor": "CIPHER puts four patterns on the screen. One of them is a catastrophic backtracking time bomb. You have 10 seconds to identify which one and justify why before the NEXUS security scanner runs it against untrusted input.",
                "lesson": (
                    "Identifying ReDoS-vulnerable patterns:\n\n"
                    "Safe:\n"
                    "  \\d{4}-\\d{2}-\\d{2}   → fixed-width, no ambiguity\n"
                    "  [A-Z]+-\\d+          → deterministic, no overlap\n\n"
                    "Vulnerable:\n"
                    "  (\\w+\\s*)+           → \\w and \\s overlap at whitespace — catastrophic\n"
                    "  (a+)+               → nested quantifiers on the same chars\n"
                    "  ([a-z]+)*           → zero-or-more wrapping a one-or-more\n\n"
                    "The danger sign: a quantified group whose content can match\n"
                    "in multiple ways OR whose content overlaps with an outer quantifier.\n\n"
                    "The term for this attack vector is: ReDoS (Regular Expression Denial of Service)."
                ),
                "question": "An attack that sends specially crafted input to trigger exponential regex backtracking and hang a server is called Re___.",
                "url": "https://www.regular-expressions.info/catastrophic.html",
                "answers": ["ReDoS", "redos", "REDOS"],
                "xp": 200,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's an acronym for a denial of service attack specific to regular expressions.",
                    "Re + DoS.",
                    "The answer is: ReDoS",
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
    "regex_flags",
    "python_regex",
    "sed_and_grep_regex",
    "named_groups_and_backreferences",
    "substitution_and_replace",
    "regex_in_javascript",
    "advanced_techniques",
]
