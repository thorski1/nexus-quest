"""
zones.py - All zone and challenge data for Vim Quest
Challenge types: quiz, fill_blank, flag_quiz
"""

ZONES = {
    "normal_vault": {
        "id": "normal_vault",
        "name": "The Normal Vault",
        "subtitle": "Movement, Navigation & Basic Editing",
        "color": "cyan",
        "icon": "🔲",
        "commands": ["hjkl", "w/b/e", "gg/G", "0/$", "dd/yy/p", "u/Ctrl+R"],
        "challenges": [
            {
                "id": "nv_1",
                "type": "quiz",
                "title": "Move Left",
                "flavor": "The cursor is on a line in the config file. You need to move it one character to the left. In normal mode, what key does this?",
                "lesson": (
                    "h — move the cursor one character left.\n\n"
                    "The four movement keys in vim (all in normal mode):\n"
                    "  h → left    j → down    k → up    l → right\n\n"
                    "They're on the home row of the keyboard — your right hand's resting position.\n"
                    "This is intentional: vim was designed so your hands never leave the home row.\n\n"
                    "Arrow keys also work, but using hjkl keeps your hands in position.\n"
                    "After a few hours of practice, hjkl becomes faster than arrow keys."
                ),
                "answer": "h",
                "url": "https://vimhelp.org/",
                "hints": ["It's the leftmost of the four movement keys.", "Home row: h j k l — h is far left.", "The answer is: h"],
            },
            {
                "id": "nv_2",
                "type": "quiz",
                "title": "Jump to File Bottom",
                "flavor": "The audit log is 4,000 lines. You need to jump to the very last line instantly. What key does this in normal mode?",
                "lesson": (
                    "G — jump to the last line of the file.\n\n"
                    "Complementary motions:\n"
                    "  gg  → jump to the first line (line 1)\n"
                    "  G   → jump to the last line\n"
                    "  NNG → jump to line N (e.g. 42G goes to line 42)\n\n"
                    "Context:\n"
                    "  :N  → also goes to line N (e.g. :42 ↵)\n"
                    "  Ctrl+G → show current line number and file info in the status bar\n\n"
                    "G is uppercase — hold Shift while pressing g."
                ),
                "answer": "G",
                "hints": ["It's a single uppercase letter — the last letter of the alphabet.", "Uppercase G. Think: go to the end.", "The answer is: G"],
            },
            {
                "id": "nv_3",
                "type": "quiz",
                "title": "Move Forward One Word",
                "flavor": "You're at the beginning of a long key name. You need to jump forward one word at a time through the line. What key moves forward one word in normal mode?",
                "lesson": (
                    "w — move forward to the beginning of the next word.\n\n"
                    "Word movement keys:\n"
                    "  w  → forward to the start of the next word\n"
                    "  b  → backward to the start of the previous word\n"
                    "  e  → forward to the end of the current/next word\n\n"
                    "WORD vs word:\n"
                    "  w moves by 'word' — separated by whitespace AND punctuation\n"
                    "  W moves by 'WORD' — separated only by whitespace\n\n"
                    "Example: in 'key_name = \"value\"':\n"
                    "  w steps: key_ → name → = → \" → value → \"\n"
                    "  W steps: key_name → = → \"value\""
                ),
                "answer": "w",
                "hints": ["Think: word forward.", "Single lowercase letter.", "The answer is: w"],
            },
            {
                "id": "nv_4",
                "type": "quiz",
                "title": "Delete the Current Line",
                "flavor": "One line in the routing table is completely wrong and needs to be deleted. What normal-mode command deletes the entire current line?",
                "lesson": (
                    "dd — delete the current line.\n\n"
                    "The 'd' operator deletes. Doubled (dd) means 'delete the current line.'\n\n"
                    "Related:\n"
                    "  dd    → delete current line (cut to register)\n"
                    "  D     → delete from cursor to end of line\n"
                    "  d$    → same as D\n"
                    "  d0    → delete from cursor to beginning of line\n"
                    "  dw    → delete to the next word boundary\n"
                    "  5dd   → delete 5 lines\n\n"
                    "Note: deleted text in vim is 'yanked' into a register.\n"
                    "You can paste it with p (after cursor) or P (before cursor).\n"
                    "vim's 'delete' is more like 'cut.'"
                ),
                "answer": "dd",
                "hints": ["The 'd' operator, doubled.", "Two characters, same key pressed twice.", "The answer is: dd"],
            },
            {
                "id": "nv_5",
                "type": "quiz",
                "title": "Undo the Last Change",
                "flavor": "You deleted the wrong line. You need to undo immediately. What key undoes the last change in normal mode?",
                "lesson": (
                    "u — undo the last change.\n\n"
                    "  u        → undo the last change\n"
                    "  Ctrl+R   → redo (undo the undo)\n\n"
                    "vim has a full undo tree — not just a linear undo stack.\n"
                    "You can undo multiple times:\n"
                    "  uuu → undo three changes\n"
                    "  5u  → undo five changes\n\n"
                    "The undo history persists as long as the file is open.\n"
                    "It's reset when you close and reopen the file\n"
                    "(unless you configure undofile for persistent undo)."
                ),
                "answer": "u",
                "hints": ["It's the first letter of 'undo'.", "Single lowercase letter.", "The answer is: u"],
            },
            {
                "id": "nv_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: End of Line",
                "flavor": "You need to move to the very end of the current line in normal mode, without a count. What key does this?",
                "lesson": (
                    "$ — move to the end of the current line.\n\n"
                    "The line boundary keys:\n"
                    "  0   → move to column 0 (absolute beginning of line)\n"
                    "  ^   → move to the first non-whitespace character on the line\n"
                    "  $   → move to the last character on the line\n\n"
                    "Combined with operators:\n"
                    "  d$  → delete from cursor to end of line (same as D)\n"
                    "  y$  → yank from cursor to end of line\n"
                    "  c$  → change from cursor to end of line (same as C)\n\n"
                    "The $ and ^ mirror regex anchors — same meaning:\n"
                    "end of line and start of non-whitespace."
                ),
                "answer": "$",
                "hints": ["Think of regex: what character means 'end of line'?", "The shift+4 key on most keyboards.", "The answer is: $"],
            },
        ],
    },
    "insert_protocol": {
        "id": "insert_protocol",
        "name": "The Insert Protocol",
        "subtitle": "Entering, Editing & Exiting Insert Mode",
        "color": "green",
        "icon": "✏️",
        "commands": ["i/I", "a/A", "o/O", "c/cc/cw", "ESC", "Ctrl+C"],
        "challenges": [
            {
                "id": "ins_1",
                "type": "quiz",
                "title": "Enter Insert Mode",
                "flavor": "The cursor is positioned just before the value you need to change. What key enters insert mode at the cursor position?",
                "lesson": (
                    "i — enter insert mode at the cursor position (insert before cursor).\n\n"
                    "The primary insert entry points:\n"
                    "  i   → insert before the cursor\n"
                    "  a   → insert after the cursor (append)\n"
                    "  I   → insert at the beginning of the line\n"
                    "  A   → insert at the end of the line\n"
                    "  o   → open a new line below and enter insert mode\n"
                    "  O   → open a new line above and enter insert mode\n\n"
                    "Most common: i (insert here) and a (insert after — useful when\n"
                    "your cursor is on the last character of something you want to append to).\n\n"
                    "The status bar shows -- INSERT -- when you're in insert mode."
                ),
                "answer": "i",
                "url": "https://vimhelp.org/",
                "hints": ["Think: insert. Single lowercase letter.", "The 'i' key.", "The answer is: i"],
            },
            {
                "id": "ins_2",
                "type": "quiz",
                "title": "Insert at End of Line",
                "flavor": "The cursor is at the beginning of a config line. You need to add a comment at the very end of the line without moving through it manually. What key enters insert mode at the end of the line?",
                "lesson": (
                    "A — enter insert mode at the end of the current line (Append).\n\n"
                    "A is shift+a. It's the combination of $ (end of line) and a (append).\n\n"
                    "Using A:\n"
                    "  Position cursor anywhere on the line\n"
                    "  Press A\n"
                    "  Cursor jumps to end of line, enter insert mode\n"
                    "  Type the text to append\n"
                    "  Press ESC\n\n"
                    "Much faster than:\n"
                    "  $ → move to end\n"
                    "  a → append after end\n\n"
                    "Similarly: I (uppercase) enters insert at the beginning of the line."
                ),
                "answer": "A",
                "hints": ["It's the uppercase version of 'a'.", "Shift+A — jumps to end of line and enters insert.", "The answer is: A"],
            },
            {
                "id": "ins_3",
                "type": "quiz",
                "title": "Open a New Line Below",
                "flavor": "You need to add a new line below the current one with some content. What key opens a new line below and enters insert mode?",
                "lesson": (
                    "o — open a new line below the current line and enter insert mode.\n\n"
                    "  o   → new line BELOW, enter insert mode\n"
                    "  O   → new line ABOVE, enter insert mode\n\n"
                    "What o actually does:\n"
                    "  1. Moves to the end of the current line\n"
                    "  2. Inserts a newline\n"
                    "  3. Enters insert mode on the new line\n"
                    "  4. Applies the current indentation automatically\n\n"
                    "This is the fastest way to add a new line when your cursor is\n"
                    "already on the line you want to insert after.\n\n"
                    "Remember: O (uppercase) adds above, o (lowercase) adds below."
                ),
                "answer": "o",
                "hints": ["Think: 'open' a new line below.", "Lowercase 'o'.", "The answer is: o"],
            },
            {
                "id": "ins_4",
                "type": "quiz",
                "title": "Exit Insert Mode",
                "flavor": "You've finished editing. You're in insert mode. What key returns you to normal mode?",
                "lesson": (
                    "ESC — exit insert mode, return to normal mode.\n\n"
                    "  ESC      → return to normal mode from any other mode\n"
                    "  Ctrl+C   → also returns to normal mode (slightly different behavior\n"
                    "              for some abbreviations and mappings)\n"
                    "  Ctrl+[   → equivalent to ESC; useful on keyboards without ESC\n\n"
                    "This is the most-used key in vim after hjkl.\n\n"
                    "Common habit: keep your hand position so ESC is easy to reach.\n"
                    "Many vim users remap Caps Lock to ESC for this reason.\n\n"
                    "After ESC, the cursor moves one character to the left (back to\n"
                    "the last character you were on before insert mode ended)."
                ),
                "answer": "ESC",
                "hints": ["The key at the top-left of most keyboards.", "It's written as a three-letter abbreviation.", "The answer is: ESC"],
            },
            {
                "id": "ins_5",
                "type": "quiz",
                "title": "Change a Word",
                "flavor": "Your cursor is at the start of a word you need to replace entirely. What normal-mode command deletes the word and enters insert mode so you can type the replacement?",
                "lesson": (
                    "cw — change word: delete to end of word, enter insert mode.\n\n"
                    "The 'c' (change) operator: like 'd' (delete), but enters insert mode\n"
                    "after deleting, so you can type the replacement immediately.\n\n"
                    "Common change operations:\n"
                    "  cw    → change to end of word\n"
                    "  ciw   → change entire word (inner word — see text objects)\n"
                    "  cc    → change the entire line\n"
                    "  C     → change from cursor to end of line\n"
                    "  c$    → same as C\n"
                    "  ci\"   → change inside double quotes\n\n"
                    "Workflow for replacing a word:\n"
                    "  Position cursor at start of word → cw → type new word → ESC"
                ),
                "answer": "cw",
                "hints": ["'c' for change, 'w' for word.", "Two letters: the change operator + word motion.", "The answer is: cw"],
            },
            {
                "id": "ins_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Change Entire Line",
                "flavor": "A config line is completely wrong and needs to be rewritten from scratch. What command deletes the entire current line and enters insert mode?",
                "lesson": (
                    "cc — change the current line: delete the line content, enter insert mode.\n\n"
                    "  cc   → delete the line's text, stay on the line, enter insert mode\n"
                    "  dd   → delete the line entirely (removed from file, not just emptied)\n\n"
                    "The difference:\n"
                    "  dd   → the line is gone. p pastes it back.\n"
                    "  cc   → the line remains (at the same line number), its content is\n"
                    "          cleared, you type the replacement. The line number doesn't change.\n\n"
                    "Useful when you want to rewrite a line completely but keep it\n"
                    "in the same position in the file.\n\n"
                    "After cc, you're in insert mode on a blank line with correct indentation."
                ),
                "answer": "cc",
                "hints": ["The 'change' operator doubled, like 'dd' is the 'delete' operator doubled.", "Two of the same letter.", "The answer is: cc"],
            },
        ],
    },
    "command_line": {
        "id": "command_line",
        "name": "The Command Line",
        "subtitle": "Saving, Opening & Managing Files",
        "color": "yellow",
        "icon": ":",
        "commands": [":w", ":q", ":wq", ":q!", ":e", ":vs/:sp", ":set"],
        "challenges": [
            {
                "id": "cmd_1",
                "type": "fill_blank",
                "title": "Save the File",
                "flavor": "You've made the changes to the config file. You need to save it. Complete the command-line command: :___",
                "lesson": (
                    ":w — write (save) the current file.\n\n"
                    "  :w           → save the current file\n"
                    "  :w filename  → save to a different filename (like Save As)\n"
                    "  :w!          → force write (override read-only, if permissions allow)\n\n"
                    "Combined:\n"
                    "  :wq   → write and quit\n"
                    "  :x    → write (only if changed) and quit — slightly different from :wq\n"
                    "          :x doesn't update the file's timestamp if nothing changed\n"
                    "  ZZ    → normal mode shortcut for :x\n\n"
                    "Command-line mode is entered with ':' from normal mode.\n"
                    "The command appears at the bottom of the screen.\n"
                    "Press Enter to execute, or ESC to cancel."
                ),
                "answer": "w",
                "url": "https://vimhelp.org/",
                "hints": ["Single letter — 'write'.", "The answer is: w"],
            },
            {
                "id": "cmd_2",
                "type": "fill_blank",
                "title": "Quit Without Saving",
                "flavor": "You opened the wrong file and made accidental changes. You need to exit without saving anything. Complete: :___",
                "lesson": (
                    ":q! — quit without saving, ignoring unsaved changes.\n\n"
                    "  :q    → quit (fails if there are unsaved changes)\n"
                    "  :q!   → quit and DISCARD unsaved changes (the ! means 'force')\n"
                    "  :wq   → save and quit\n"
                    "  :qa!  → quit ALL open files without saving (a = all)\n\n"
                    "The ! (bang) in vim commands generally means 'force' or 'override'.\n"
                    "  :w!   → force write\n"
                    "  :q!   → force quit (discard changes)\n"
                    "  :e!   → force reload from disk (discard unsaved changes in current buffer)\n\n"
                    "Most beginners learn :q! before anything else. It's the escape hatch."
                ),
                "answer": "q!",
                "hints": ["Quit, forced — using the '!' modifier.", "The answer is: q!"],
            },
            {
                "id": "cmd_3",
                "type": "fill_blank",
                "title": "Open Another File",
                "flavor": "You're in a vim session and need to open a different file: /var/log/nexus/audit.log. Complete: :___ /var/log/nexus/audit.log",
                "lesson": (
                    ":e — edit (open) a file in the current vim session.\n\n"
                    "  :e filename   → open a file in the current window (replaces current buffer)\n"
                    "  :e!           → reload the current file from disk (discard changes)\n"
                    "  :e .          → open the directory explorer (netrw) for the current directory\n\n"
                    "Tab completion works for filenames in command-line mode:\n"
                    "  :e /var/log/ne<Tab> → completes the path\n\n"
                    "Related:\n"
                    "  :vs filename   → open in a vertical split\n"
                    "  :sp filename   → open in a horizontal split\n"
                    "  :tabedit file  → open in a new tab"
                ),
                "answer": "e",
                "hints": ["Think: 'edit' a file.", "Single letter.", "The answer is: e"],
            },
            {
                "id": "cmd_4",
                "type": "fill_blank",
                "title": "Vertical Split",
                "flavor": "You need to open a second file side-by-side with the current one (vertical split). Complete: :___ /etc/nexus/processor.conf",
                "lesson": (
                    ":vs — vertical split: open a file in a new vertical pane.\n\n"
                    "  :vs filename   → vertical split; file opens on the RIGHT\n"
                    "  :sp filename   → horizontal split; file opens BELOW\n"
                    "  :vs            → vertical split the current buffer (useful for comparing)\n\n"
                    "Navigating splits:\n"
                    "  Ctrl+W h   → move to the split on the left\n"
                    "  Ctrl+W l   → move to the split on the right\n"
                    "  Ctrl+W j   → move to the split below\n"
                    "  Ctrl+W k   → move to the split above\n"
                    "  Ctrl+W w   → cycle through splits\n\n"
                    "Resizing splits:\n"
                    "  Ctrl+W =   → equalize all split sizes\n"
                    "  Ctrl+W >   → increase width\n"
                    "  Ctrl+W <   → decrease width"
                ),
                "answer": "vs",
                "hints": ["Two letters: vertical split.", "The answer is: vs"],
            },
            {
                "id": "cmd_5",
                "type": "fill_blank",
                "title": "Save and Quit",
                "flavor": "You're done editing. Save the file and close vim in one command. Complete: :___",
                "lesson": (
                    ":wq — write and quit.\n\n"
                    "  :wq   → save the current file and exit vim\n"
                    "  :wq!  → force save (override read-only) and quit\n"
                    "  :x    → same as :wq but only writes if changes were made\n"
                    "  ZZ    → normal mode shortcut for :x\n\n"
                    "Multiple buffers:\n"
                    "  :wqa  → write all modified buffers and quit\n"
                    "  :qa   → quit all (fails if any have unsaved changes)\n"
                    "  :qa!  → force quit all (discard all unsaved changes)\n\n"
                    "In a session with multiple split windows:\n"
                    "  :q    → closes the current window (not the whole session)\n"
                    "  :qall → closes all windows and exits vim"
                ),
                "answer": "wq",
                "hints": ["Write + quit, combined into one command.", "Two letters.", "The answer is: wq"],
            },
            {
                "id": "cmd_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Go to Line Number",
                "flavor": "The error is on line 2847 of the 4,000-line audit log. Go there directly from command-line mode. Complete: :___",
                "lesson": (
                    ":N — go to line number N.\n\n"
                    "  :2847   → jump to line 2847\n"
                    "  :1      → jump to line 1 (same as gg in normal mode)\n"
                    "  :$      → jump to the last line (same as G)\n\n"
                    "Alternatives:\n"
                    "  2847G   → in normal mode, go to line 2847\n"
                    "  2847gg  → also goes to line 2847\n\n"
                    "Show current line information:\n"
                    "  Ctrl+G   → shows filename, current line, total lines, percentage\n"
                    "  :set nu  → show line numbers in the left margin\n"
                    "  :set rnu → show relative line numbers\n\n"
                    "The answer to this specific question: the number itself is the command.\n"
                    "':2847' goes to line 2847. The answer format is just the number."
                ),
                "answer": "2847",
                "hints": ["The command is just the line number itself.", "Type the number after the colon.", "The answer is: 2847"],
            },
        ],
    },
    "visual_mode": {
        "id": "visual_mode",
        "name": "Visual Mode",
        "subtitle": "Selection, Block Operations & Visual Editing",
        "color": "magenta",
        "icon": "🔲",
        "commands": ["v", "V", "Ctrl+V", "d/y/c in visual", "><", "I in block"],
        "challenges": [
            {
                "id": "vis_1",
                "type": "quiz",
                "title": "Enter Character Visual",
                "flavor": "You need to select a few characters in the middle of a line and delete them. What key enters character-wise visual mode?",
                "lesson": (
                    "v — enter character-wise visual mode.\n\n"
                    "In visual mode:\n"
                    "  - The cursor movement keys (hjkl, w, b, etc.) extend the selection\n"
                    "  - The selection is highlighted\n"
                    "  - Operators (d, y, c, >, <) act on the selection\n\n"
                    "Three visual modes:\n"
                    "  v        → character-wise (select individual characters)\n"
                    "  V        → line-wise (select whole lines)\n"
                    "  Ctrl+V   → block-wise (select a rectangular column)\n\n"
                    "After selecting:\n"
                    "  d → delete the selection\n"
                    "  y → yank (copy) the selection\n"
                    "  c → change (delete and enter insert mode)\n"
                    "  > → indent right\n"
                    "  < → indent left"
                ),
                "answer": "v",
                "url": "https://vimhelp.org/",
                "hints": ["Single lowercase letter — 'visual'.", "The answer is: v"],
            },
            {
                "id": "vis_2",
                "type": "quiz",
                "title": "Select Whole Lines",
                "flavor": "You need to select three complete lines and delete them. What key enters line-wise visual mode?",
                "lesson": (
                    "V — enter line-wise visual mode (uppercase V).\n\n"
                    "Line-wise visual selects entire lines, not partial lines.\n"
                    "The minimum selection is one full line. Moving up or down\n"
                    "adds or removes complete lines from the selection.\n\n"
                    "Workflow for deleting 3 lines:\n"
                    "  V     → enter line visual mode (selects current line)\n"
                    "  2j    → extend selection down 2 more lines (3 total)\n"
                    "  d     → delete the 3 selected lines\n\n"
                    "Alternative without visual mode:\n"
                    "  3dd   → delete 3 lines from the current position\n\n"
                    "Line-wise visual is most useful when the number of lines\n"
                    "isn't easily counted, or when you want to visually confirm\n"
                    "the selection before acting on it."
                ),
                "answer": "V",
                "hints": ["Uppercase V — visual line mode.", "Shift+V", "The answer is: V"],
            },
            {
                "id": "vis_3",
                "type": "quiz",
                "title": "Block Visual Mode",
                "flavor": "The routing table has a column of values that all need to be prefixed with 'FLAG:'. What visual mode lets you select a rectangular column across multiple lines simultaneously?",
                "lesson": (
                    "Ctrl+V — enter block-wise visual mode (column selection).\n\n"
                    "Block visual selects a rectangular region across multiple lines.\n"
                    "It ignores line length — you select a column N characters wide\n"
                    "and M lines tall.\n\n"
                    "Key operations in block visual:\n"
                    "  I   → insert text at the beginning of every selected line\n"
                    "  A   → append text at the end of every selected line\n"
                    "  d   → delete the selected column from every line\n"
                    "  r   → replace all characters in the block with one character\n\n"
                    "To prefix a column:\n"
                    "  Ctrl+V → select the column\n"
                    "  I      → enter block insert mode\n"
                    "  type 'FLAG:'  → only shows on first line while typing\n"
                    "  ESC   → text appears on ALL selected lines simultaneously"
                ),
                "answer": "Ctrl+V",
                "hints": ["Think: block visual. It's a control key combination.", "Ctrl + V — column selection.", "The answer is: Ctrl+V"],
            },
            {
                "id": "vis_4",
                "type": "quiz",
                "title": "Yank the Selection",
                "flavor": "You've selected a block of evidence text in visual mode and need to copy it (yank it) to paste elsewhere. What key yanks (copies) the visual selection?",
                "lesson": (
                    "y — yank (copy) the visual selection.\n\n"
                    "  y → yank the selected text into the default register\n"
                    "  d → delete (cut) the selected text\n"
                    "  c → change (delete and enter insert mode)\n\n"
                    "After yanking, exit visual mode (ESC or y exits automatically),\n"
                    "move to the destination, and paste:\n"
                    "  p → paste after the cursor\n"
                    "  P → paste before the cursor\n\n"
                    "Registers: yanked text goes into the unnamed register (\").\n"
                    "  \"ay → yank into register 'a'\n"
                    "  \"ap → paste from register 'a'\n\n"
                    "System clipboard:\n"
                    "  \"+y → yank to the system clipboard\n"
                    "  \"+p → paste from the system clipboard"
                ),
                "answer": "y",
                "hints": ["Think: 'yank' — vim's term for copy.", "Single lowercase letter.", "The answer is: y"],
            },
            {
                "id": "vis_5",
                "type": "quiz",
                "title": "Indent Selected Lines",
                "flavor": "You've selected several lines of config in visual mode and need to indent them one level to the right. What key indents the selection?",
                "lesson": (
                    "> — indent the selected lines one level to the right.\n\n"
                    "  >  → indent the visual selection right (one shiftwidth)\n"
                    "  <  → unindent the visual selection left\n\n"
                    "In normal mode (no visual selection):\n"
                    "  >>  → indent the current line right\n"
                    "  <<  → unindent the current line left\n"
                    "  N>> → indent N lines\n\n"
                    "The indentation amount is controlled by :set shiftwidth=N\n"
                    "(default is usually 8, but most modern configs set it to 2 or 4).\n\n"
                    "After indenting in visual mode, vim exits visual mode.\n"
                    "To indent again, use gv to re-select the same region, then > again."
                ),
                "answer": ">",
                "hints": ["Think of an arrow pointing right — indenting to the right.", "The > symbol.", "The answer is: >"],
            },
            {
                "id": "vis_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Insert at Column",
                "flavor": "In block visual mode, you've selected a column. What key inserts text at the beginning of every selected line simultaneously?",
                "lesson": (
                    "I — insert at the beginning of every line in a block visual selection.\n\n"
                    "This is one of vim's most powerful operations:\n"
                    "  1. Ctrl+V to enter block visual\n"
                    "  2. Select the column across the lines you want to modify\n"
                    "  3. Press I (uppercase i)\n"
                    "  4. Type the text — it only appears on the first line while typing\n"
                    "  5. Press ESC — the text instantly appears on ALL selected lines\n\n"
                    "Example: adding '# ' (comment prefix) to 20 lines:\n"
                    "  Ctrl+V\n"
                    "  19j (extend selection down 19 lines)\n"
                    "  I\n"
                    "  # \n"
                    "  ESC\n"
                    "  → all 20 lines now start with '# '\n\n"
                    "Note: I in block visual is uppercase i (Shift+i), not lowercase."
                ),
                "answer": "I",
                "hints": ["It's the uppercase version of the 'insert' key.", "Shift+I — insert at start of every selected line.", "The answer is: I"],
            },
        ],
    },
    "search_engine": {
        "id": "search_engine",
        "name": "The Search Engine",
        "subtitle": "Search, Replace & Pattern Navigation",
        "color": "red",
        "icon": "🔍",
        "commands": ["/pattern", "?pattern", "n/N", "*/#", ":%s/old/new/g"],
        "challenges": [
            {
                "id": "srch_1",
                "type": "fill_blank",
                "title": "Search Forward",
                "flavor": "The config file is 4,000 lines. You need to find the 'max_retry_count' setting. What do you type to start a forward search for 'max_retry'?",
                "lesson": (
                    "/ — enter forward search mode.\n\n"
                    "  /pattern   → search forward for 'pattern'\n"
                    "  ?pattern   → search backward for 'pattern'\n\n"
                    "After typing the pattern, press Enter to search.\n\n"
                    "Navigation after searching:\n"
                    "  n   → jump to the NEXT match (forward)\n"
                    "  N   → jump to the PREVIOUS match (backward)\n\n"
                    "Highlight all matches:\n"
                    "  :set hlsearch   → highlight all matches\n"
                    "  :nohlsearch     → clear highlights (or :noh)\n\n"
                    "Incremental search (highlights as you type):\n"
                    "  :set incsearch  → most modern vim configs enable this by default\n\n"
                    "So: to search for 'max_retry': type /max_retry then Enter."
                ),
                "answer": "/max_retry",
                "url": "https://vimhelp.org/",
                "hints": ["The search key is '/', followed by the pattern.", "The answer is: /max_retry"],
            },
            {
                "id": "srch_2",
                "type": "quiz",
                "title": "Search for Word Under Cursor",
                "flavor": "Your cursor is on a vendor name in the routing table. You want to find all other occurrences instantly. What key searches for the exact word under the cursor?",
                "lesson": (
                    "* — search forward for the word under the cursor.\n\n"
                    "  *   → search forward for the exact word under the cursor\n"
                    "  #   → search backward for the exact word under the cursor\n\n"
                    "These are 'whole word' searches — they match the exact word,\n"
                    "not substrings. If the cursor is on 'vendor', * finds 'vendor'\n"
                    "but not 'vendor_id' or 'multivendor'.\n\n"
                    "After pressing *, use n/N to navigate between matches.\n\n"
                    "Combining with substitution:\n"
                    "  Position on a word, press *, note the search pattern in\n"
                    "  the status bar, then use :%s// (empty pattern reuses last search)\n"
                    "  to replace all occurrences."
                ),
                "answer": "*",
                "hints": ["It's a special symbol — the asterisk.", "The * key — searches for the word under cursor.", "The answer is: *"],
            },
            {
                "id": "srch_3",
                "type": "fill_blank",
                "title": "Replace on Current Line",
                "flavor": "The current line has 'phantom_vendor' twice. You need to replace both instances with 'FLAGGED'. Complete the substitution command: :s/phantom_vendor/FLAGGED/___",
                "lesson": (
                    ":s/old/new/g — substitute on the current line, all occurrences.\n\n"
                    "The 'g' flag means 'global' — replace ALL occurrences on the line.\n"
                    "Without 'g', only the FIRST occurrence on the line is replaced.\n\n"
                    "Flags:\n"
                    "  g → replace all occurrences (global)\n"
                    "  i → case-insensitive match\n"
                    "  c → confirm each replacement\n"
                    "  e → suppress error if pattern not found\n\n"
                    "Scope:\n"
                    "  :s/old/new/g        → current line only\n"
                    "  :%s/old/new/g       → entire file\n"
                    "  :5,10s/old/new/g    → lines 5 through 10\n"
                    "  :'<,'>s/old/new/g   → visual selection (set automatically after V)"
                ),
                "answer": "g",
                "hints": ["The flag that means 'all occurrences' (global).", "Single letter appended after the last /", "The answer is: g"],
            },
            {
                "id": "srch_4",
                "type": "fill_blank",
                "title": "Replace in Entire File",
                "flavor": "The vendor name 'NEXUS_PHANTOM' appears 23 times across the file. Replace all occurrences with 'FLAGGED_VENDOR'. Complete: :___s/NEXUS_PHANTOM/FLAGGED_VENDOR/g",
                "lesson": (
                    ":%s/old/new/g — substitute in the entire file.\n\n"
                    "The % address means 'all lines' — equivalent to 1,$ (line 1 to last line).\n\n"
                    "  :%s/old/new/g    → replace all occurrences in the entire file\n"
                    "  :%s/old/new/gc   → replace all, confirming each one\n"
                    "                     (y/n/a/q/l per match)\n\n"
                    "Address examples:\n"
                    "  :%         → all lines\n"
                    "  :1,10      → lines 1-10\n"
                    "  :.,+5      → current line plus 5 lines after\n"
                    "  :'<,'>     → current visual selection\n\n"
                    "Special characters in the pattern:\n"
                    "  \\n  → newline\n"
                    "  \\.  → literal dot (. alone matches any character)\n"
                    "  \\b  → word boundary"
                ),
                "answer": "%",
                "hints": ["The address that means 'entire file' goes before the 's'.", "The % symbol.", "The answer is: %"],
            },
            {
                "id": "srch_5",
                "type": "quiz",
                "title": "Next Search Match",
                "flavor": "You've searched for 'disbursement_code' and there are multiple matches. What key jumps to the next match?",
                "lesson": (
                    "n — jump to the next search match.\n\n"
                    "  n  → next match in the search direction (forward for /, backward for ?)\n"
                    "  N  → opposite direction\n\n"
                    "After a / search:\n"
                    "  n → next match forward\n"
                    "  N → previous match (backward)\n\n"
                    "After a ? search:\n"
                    "  n → next match backward (same direction as the search)\n"
                    "  N → next match forward\n\n"
                    "If the search wraps around (reaches end of file and continues\n"
                    "from the beginning), vim shows 'search wrapped around' in the\n"
                    "status bar. Disable wrapping with :set nowrapscan."
                ),
                "answer": "n",
                "hints": ["Think: 'next'. Single lowercase letter.", "The answer is: n"],
            },
            {
                "id": "srch_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Confirm Each Replacement",
                "flavor": "You need to review each replacement before making it. What flag added to :%s/old/new/ makes vim confirm each substitution interactively?",
                "lesson": (
                    "c — the confirm flag: vim pauses at each match and asks y/n/a/q/l.\n\n"
                    "  :%s/PHANTOM/FLAGGED/gc  → replace all, confirming each one\n\n"
                    "At each match, vim shows:\n"
                    "  y → yes, replace this one\n"
                    "  n → no, skip this one\n"
                    "  a → all, replace all remaining without asking\n"
                    "  q → quit, stop the substitution\n"
                    "  l → last, replace this one and stop\n"
                    "  Ctrl+E / Ctrl+Y → scroll to see more context\n\n"
                    "The confirm flag is essential when you can't use a pattern\n"
                    "precise enough to match only what you want — it lets you\n"
                    "review each match and decide individually."
                ),
                "answer": "c",
                "hints": ["The flag that means 'confirm'.", "Single letter, appended after 'g'.", "The answer is: c"],
            },
        ],
    },
    "motion_objects": {
        "id": "motion_objects",
        "name": "Motion & Text Objects",
        "subtitle": "The Grammar That Makes Vim Fast",
        "color": "cyan",
        "icon": "🎯",
        "commands": ["ciw/diw", "ci\"/di\"", "da(", "yap", "f/t/F/T", "%"],
        "challenges": [
            {
                "id": "mot_1",
                "type": "fill_blank",
                "title": "Change Inner Word",
                "flavor": "The cursor is somewhere on the word 'phantom'. You want to delete the entire word and type a replacement, without moving to the start of the word first. What command does this?",
                "lesson": (
                    "ciw — change inner word: delete the whole word, enter insert mode.\n\n"
                    "Text object syntax: [operator][i/a][object]\n"
                    "  i = 'inner' (just the object, no surrounding space)\n"
                    "  a = 'around' (object + surrounding whitespace or delimiters)\n\n"
                    "  ciw   → change inner word (works regardless of cursor position within word)\n"
                    "  diw   → delete inner word\n"
                    "  yiw   → yank inner word\n"
                    "  caw   → change around word (includes trailing space)\n"
                    "  daw   → delete around word\n\n"
                    "The power: 'i' and 'a' modifiers make the operator cursor-position-independent.\n"
                    "ciw works whether your cursor is at the start, middle, or end of the word."
                ),
                "answer": "ciw",
                "url": "https://vimhelp.org/",
                "hints": ["Change (c) + inner (i) + word (w).", "Three letters.", "The answer is: ciw"],
            },
            {
                "id": "mot_2",
                "type": "fill_blank",
                "title": "Change Inside Quotes",
                "flavor": "Config line: route = \"phantom_subsidiary\". Cursor is anywhere on the line. You need to replace the value inside the quotes. What command deletes everything between the quotes and enters insert mode?",
                "lesson": (
                    "ci\" — change inside double quotes.\n\n"
                    "  ci\"   → change inside double quotes (deletes content, keeps quotes)\n"
                    "  ca\"   → change around double quotes (deletes content AND quotes)\n"
                    "  di\"   → delete inside double quotes\n"
                    "  yi\"   → yank inside double quotes\n\n"
                    "Works for any delimiter:\n"
                    "  ci'   → inside single quotes\n"
                    "  ci(   → inside parentheses\n"
                    "  ci[   → inside square brackets\n"
                    "  ci{   → inside curly braces\n"
                    "  cit   → inside HTML/XML tags\n\n"
                    "The cursor doesn't need to be inside the quotes —\n"
                    "vim finds the nearest matching pair on the current line."
                ),
                "answer": "ci\"",
                "hints": ["Change (c) + inner (i) + double-quote (\").", "Three characters.", "The answer is: ci\""],
            },
            {
                "id": "mot_3",
                "type": "fill_blank",
                "title": "Delete Around Parentheses",
                "flavor": "The line contains a function call: process(phantom_data, 0x4A). You want to delete the parentheses AND everything inside them. What command does this?",
                "lesson": (
                    "da( — delete around parentheses: delete the parens AND their contents.\n\n"
                    "  di(   → delete INSIDE parentheses (keeps the parens)\n"
                    "  da(   → delete the parens AND everything inside them\n\n"
                    "Same pattern works for all paired delimiters:\n"
                    "  da[   → delete around square brackets\n"
                    "  da{   → delete around curly braces\n"
                    "  da\"   → delete around double quotes\n"
                    "  dat   → delete around XML/HTML tag\n\n"
                    "Note: da( and da) do the same thing — both refer to the paren pair.\n"
                    "Similarly: di(/di) are equivalent.\n\n"
                    "The 'a' (around) modifier includes the delimiters themselves.\n"
                    "The 'i' (inner) modifier excludes them."
                ),
                "answer": "da(",
                "hints": ["Delete (d) + around (a) + open-paren (()", "Three characters.", "The answer is: da("],
            },
            {
                "id": "mot_4",
                "type": "quiz",
                "title": "Jump to Character",
                "flavor": "The cursor is at the start of the line. You need to move the cursor TO the first comma on the line (landing ON the comma). What key does this?",
                "lesson": (
                    "f{char} — move forward to the next occurrence of a character on the line.\n\n"
                    "  f,   → jump forward to the next comma, landing ON it\n"
                    "  t,   → jump forward to just BEFORE the next comma (till)\n"
                    "  F,   → jump backward to the previous comma (landing on it)\n"
                    "  T,   → jump backward to just after the previous comma\n\n"
                    "Repeating:\n"
                    "  ;    → repeat the last f/t/F/T in the same direction\n"
                    "  ,    → repeat in the opposite direction\n\n"
                    "f vs t:\n"
                    "  f goes TO the character (lands on it)\n"
                    "  t goes TILL the character (stops one before)\n"
                    "  t is useful for delete: dt, deletes everything up to (not including) the comma"
                ),
                "answer": "f",
                "hints": ["Think: 'find' a character on the line.", "Single lowercase letter.", "The answer is: f"],
            },
            {
                "id": "mot_5",
                "type": "quiz",
                "title": "Jump to Matching Bracket",
                "flavor": "The cursor is on an opening parenthesis in a complex nested expression. What key jumps to the matching closing parenthesis?",
                "lesson": (
                    "% — jump to the matching bracket, parenthesis, or brace.\n\n"
                    "  %   → jump to the matching ), ], or }\n"
                    "        (also works in reverse: on ), jumps to matching ()\n\n"
                    "Supported pairs:\n"
                    "  () → parentheses\n"
                    "  [] → square brackets\n"
                    "  {} → curly braces\n\n"
                    "Useful for:\n"
                    "  - Verifying nested structures are balanced\n"
                    "  - Selecting a block: v% selects from here to the matching bracket\n"
                    "  - d% deletes from cursor to matching bracket (inclusive)\n\n"
                    "Can also jump between #if/#endif and other matched language constructs\n"
                    "if the matchit plugin is loaded (included with most vim distributions)."
                ),
                "answer": "%",
                "hints": ["The key that means 'percentage' — also used for jump to match.", "The % key.", "The answer is: %"],
            },
            {
                "id": "mot_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Yank a Paragraph",
                "flavor": "The config file has a block of settings separated by blank lines (a paragraph). You need to copy the entire current paragraph. What command yanks the current paragraph as a text object?",
                "lesson": (
                    "yap — yank around paragraph.\n\n"
                    "Paragraph text object:\n"
                    "  ip  → inner paragraph (the text, not the surrounding blank lines)\n"
                    "  ap  → around paragraph (the text AND surrounding blank lines)\n\n"
                    "  yip  → yank inner paragraph\n"
                    "  yap  → yank around paragraph (includes surrounding blank lines)\n"
                    "  dip  → delete inner paragraph\n"
                    "  dap  → delete around paragraph\n"
                    "  cip  → change inner paragraph\n\n"
                    "What counts as a paragraph:\n"
                    "  - A block of non-empty lines, bounded by blank lines or file edges\n"
                    "  - Same definition as in prose writing\n\n"
                    "After yap, you can move to another location and paste with p or P."
                ),
                "answer": "yap",
                "hints": ["Yank (y) + around (a) + paragraph (p).", "Three letters.", "The answer is: yap"],
            },
        ],
    },
    "split_network": {
        "id": "split_network",
        "name": "The Split Network",
        "subtitle": "Splits, Buffers & Multi-File Sessions",
        "color": "blue",
        "icon": "🪟",
        "commands": [":vs/:sp", "Ctrl+W nav", ":ls/:b", ":tabnew", "buffers"],
        "challenges": [
            {
                "id": "splt_1",
                "type": "fill_blank",
                "title": "Navigate to Left Split",
                "flavor": "You have two vertical splits open. Your cursor is in the right pane. Move to the left pane. Complete: Ctrl+W ___",
                "lesson": (
                    "Ctrl+W h — move to the split on the left.\n\n"
                    "Split navigation uses the same hjkl keys as cursor movement:\n"
                    "  Ctrl+W h   → move to split on the LEFT\n"
                    "  Ctrl+W l   → move to split on the RIGHT\n"
                    "  Ctrl+W j   → move to split BELOW\n"
                    "  Ctrl+W k   → move to split ABOVE\n"
                    "  Ctrl+W w   → cycle to the next split (clockwise)\n"
                    "  Ctrl+W W   → cycle to the previous split (counterclockwise)\n\n"
                    "Creating splits:\n"
                    "  :vs   → vertical split (current or new file)\n"
                    "  :sp   → horizontal split\n"
                    "  Ctrl+W v  → vertical split current buffer\n"
                    "  Ctrl+W s  → horizontal split current buffer\n\n"
                    "Closing splits:\n"
                    "  :q     → close current split\n"
                    "  Ctrl+W c  → close current split\n"
                    "  Ctrl+W o  → close ALL other splits (only keep current)"
                ),
                "answer": "h",
                "url": "https://vimhelp.org/",
                "hints": ["Same as cursor movement: h is left.", "The answer is: h"],
            },
            {
                "id": "splt_2",
                "type": "quiz",
                "title": "List Open Buffers",
                "flavor": "You have several files open in this vim session and need to see the full list. What command lists all open buffers?",
                "lesson": (
                    ":ls — list all open buffers.\n\n"
                    "Output format:\n"
                    "  1  %a  \"file1.txt\"     line 12\n"
                    "  2  #   \"file2.conf\"    line 1\n"
                    "  3      \"file3.log\"     line 1\n\n"
                    "Status flags:\n"
                    "  %  → current buffer\n"
                    "  #  → alternate buffer (last visited; Ctrl+^ switches to it)\n"
                    "  a  → active (loaded and visible)\n"
                    "  h  → hidden (loaded but not displayed)\n"
                    "  +  → modified (unsaved changes)\n\n"
                    "Navigating buffers:\n"
                    "  :b N     → switch to buffer N\n"
                    "  :b name  → switch to buffer matching 'name'\n"
                    "  :bnext   → next buffer\n"
                    "  :bprev   → previous buffer\n"
                    "  Ctrl+^   → toggle between current and alternate buffer (:b #)"
                ),
                "answer": "ls",
                "hints": ["Same as the Unix command for listing — but prefixed with ':'.", "The answer is: ls"],
            },
            {
                "id": "splt_3",
                "type": "fill_blank",
                "title": "Switch to Buffer",
                "flavor": "You see from :ls that the audit log is buffer 3. Switch to it. Complete: :b ___",
                "lesson": (
                    ":b N — switch to buffer number N.\n\n"
                    "  :b 3     → switch to buffer 3\n"
                    "  :b file  → switch to buffer matching 'file' (partial name OK)\n"
                    "  :b#      → switch to the alternate buffer (same as Ctrl+^)\n\n"
                    "Buffer deletion:\n"
                    "  :bd N    → delete (close) buffer N\n"
                    "  :bda     → delete all buffers\n\n"
                    "Viewing multiple buffers simultaneously:\n"
                    "  :ba      → open all buffers in splits\n"
                    "  :vert ba → open all buffers in vertical splits\n\n"
                    "The alternate buffer (marked with # in :ls) is the last buffer\n"
                    "you were in before the current one. Ctrl+^ is the fastest way\n"
                    "to toggle between two files."
                ),
                "answer": "3",
                "hints": ["Just the buffer number.", "The answer is: 3"],
            },
            {
                "id": "splt_4",
                "type": "fill_blank",
                "title": "Equalize Split Sizes",
                "flavor": "Your splits have become uneven after resizing. You need to equalize them all. Complete: Ctrl+W ___",
                "lesson": (
                    "Ctrl+W = — equalize the sizes of all open splits.\n\n"
                    "Resize operations:\n"
                    "  Ctrl+W =   → make all windows equal size\n"
                    "  Ctrl+W >   → increase width of current window by 1\n"
                    "  Ctrl+W <   → decrease width by 1\n"
                    "  Ctrl+W +   → increase height by 1\n"
                    "  Ctrl+W -   → decrease height by 1\n"
                    "  N Ctrl+W > → increase width by N\n\n"
                    "Set exact size:\n"
                    "  :vertical resize 80   → set current window to 80 columns\n"
                    "  :resize 40            → set current window to 40 lines\n\n"
                    "Maximize current window:\n"
                    "  Ctrl+W |   → maximize width\n"
                    "  Ctrl+W _   → maximize height\n"
                    "  Ctrl+W |   then Ctrl+W _ → maximize both"
                ),
                "answer": "=",
                "hints": ["The key that means 'equalize'.", "The = key.", "The answer is: ="],
            },
            {
                "id": "splt_5",
                "type": "fill_blank",
                "title": "Open New Tab",
                "flavor": "You want to open a completely separate workspace (new tab) for a different file. Complete the command: :___",
                "lesson": (
                    ":tabnew — open a new tab.\n\n"
                    "  :tabnew           → open a new empty tab\n"
                    "  :tabnew filename  → open a file in a new tab\n"
                    "  :tabedit file     → same as :tabnew file\n\n"
                    "Tab navigation:\n"
                    "  gt    → go to next tab (in normal mode)\n"
                    "  gT    → go to previous tab\n"
                    "  N gt  → go to tab N\n"
                    "  :tabclose → close current tab\n"
                    "  :tabonly  → close all other tabs\n\n"
                    "Tabs vs splits:\n"
                    "  Splits: multiple files visible simultaneously in one window\n"
                    "  Tabs: separate 'pages', each can contain their own set of splits\n\n"
                    "Use splits for files you're actively cross-referencing,\n"
                    "tabs for distinct tasks or contexts."
                ),
                "answer": "tabnew",
                "hints": ["The command that creates a new tab.", "The answer is: tabnew"],
            },
            {
                "id": "splt_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Close Other Splits",
                "flavor": "You only need the current file now. Close all other splits but keep the current one. Complete: Ctrl+W ___",
                "lesson": (
                    "Ctrl+W o — close all OTHER splits, keep only the current one.\n\n"
                    "  Ctrl+W o   → 'only' — close all other windows\n"
                    "  :only      → same effect via command line\n\n"
                    "This is useful after doing cross-file reference work in splits —\n"
                    "you've found what you needed, now return to single-file focus.\n\n"
                    "Compare:\n"
                    "  Ctrl+W c   → close the CURRENT window (keep the others)\n"
                    "  Ctrl+W o   → keep the current, close ALL OTHERS\n"
                    "  :q         → close current window (same as Ctrl+W c in a split)"
                ),
                "answer": "o",
                "hints": ["Think: 'only' — keep only the current split.", "Single letter: the 'only' command.", "The answer is: o"],
            },
        ],
    },
    "macro_forge": {
        "id": "macro_forge",
        "name": "The Macro Forge",
        "subtitle": "Macros, Registers & Repeating Operations",
        "color": "red",
        "icon": "⚙️",
        "commands": ["q{reg}", "@{reg}", "@@", ":%normal", "registers"],
        "challenges": [
            {
                "id": "mac_1",
                "type": "fill_blank",
                "title": "Start Recording a Macro",
                "flavor": "You need to record a macro into register 'a'. What key sequence starts recording?",
                "lesson": (
                    "q{register} — start recording a macro.\n\n"
                    "  qa  → start recording into register 'a'\n"
                    "  qb  → start recording into register 'b'\n"
                    "  q   → stop recording (press q again when done)\n\n"
                    "While recording:\n"
                    "  - Every normal mode command, insert mode action, and\n"
                    "    command-line command is captured\n"
                    "  - The recording indicator appears in the status bar: 'recording @a'\n"
                    "  - Press q to stop\n\n"
                    "Registers: macros are stored in named registers (a-z, 0-9, etc.)\n"
                    "  - Lowercase (qa): overwrites the register\n"
                    "  - Uppercase (qA): appends to the register\n\n"
                    "Plan your macro before recording: make sure it ends in a position\n"
                    "where it can be replayed from (e.g., move to the next line at the end)."
                ),
                "answer": "qa",
                "url": "https://vimhelp.org/",
                "hints": ["q starts recording, then the register name.", "The answer is: qa"],
            },
            {
                "id": "mac_2",
                "type": "fill_blank",
                "title": "Stop Recording",
                "flavor": "You've completed the actions for your macro. What key stops the recording?",
                "lesson": (
                    "q — press q (in normal mode) to stop recording a macro.\n\n"
                    "The recording flow:\n"
                    "  1. qa  → start recording into register 'a'\n"
                    "  2. ... perform the actions ...\n"
                    "  3. q   → stop recording\n\n"
                    "The same 'q' key both starts and stops recording:\n"
                    "  - Without an active recording: q{register} starts recording\n"
                    "  - During active recording: q stops recording\n\n"
                    "Common mistake: pressing q while in insert mode doesn't stop\n"
                    "the recording — it types the letter 'q' instead.\n"
                    "Make sure you're in normal mode before pressing q to stop."
                ),
                "answer": "q",
                "hints": ["The same key used to start recording — pressed again.", "Single letter.", "The answer is: q"],
            },
            {
                "id": "mac_3",
                "type": "fill_blank",
                "title": "Play a Macro",
                "flavor": "Your macro is in register 'a'. You need to run it once. What key sequence plays the macro?",
                "lesson": (
                    "@{register} — play (execute) a macro from a register.\n\n"
                    "  @a    → execute the macro stored in register 'a'\n"
                    "  @b    → execute the macro stored in register 'b'\n"
                    "  @@    → re-execute the last macro (whatever @a/@b was)\n\n"
                    "Repeating:\n"
                    "  10@a  → execute the macro 10 times\n"
                    "  416@a → execute 416 times (for that routing table...)\n\n"
                    "If the macro fails on a line (e.g., pattern not found),\n"
                    "execution stops. This is useful: it means a macro with a\n"
                    "search will automatically stop when it runs out of matches."
                ),
                "answer": "@a",
                "hints": ["@ followed by the register name.", "The answer is: @a"],
            },
            {
                "id": "mac_4",
                "type": "fill_blank",
                "title": "Replay Last Macro",
                "flavor": "You just ran @a and need to run it again immediately. What shortcut replays the most recently executed macro?",
                "lesson": (
                    "@@ — replay the last executed macro.\n\n"
                    "  @@    → repeat the last @{register} call\n"
                    "  10@@  → repeat the last macro 10 more times\n\n"
                    "Relationship to the . command:\n"
                    "  .     → repeat the last single normal-mode change\n"
                    "  @@    → repeat the last macro (which may contain many changes)\n\n"
                    "The @@ shortcut is useful for:\n"
                    "  - Running a macro on multiple non-contiguous lines\n"
                    "    (move to each line, @@ to apply)\n"
                    "  - Quick repeated application without remembering which register\n\n"
                    "@@@ doesn't exist — only @@ for repeating."
                ),
                "answer": "@@",
                "hints": ["Double @ — repeats the last macro.", "The answer is: @@"],
            },
            {
                "id": "mac_5",
                "type": "fill_blank",
                "title": "Apply Macro to All Lines",
                "flavor": "Macro 'a' annotates a transaction line. You want to apply it to every line in the file. Complete the command: :___normal @a",
                "lesson": (
                    ":% normal @a — apply a macro to every line in the file.\n\n"
                    "  :%normal @a   → run macro 'a' on every line in the file\n"
                    "  :5,20normal @a → run macro 'a' on lines 5 through 20\n"
                    "  :'<,'>normal @a → run macro 'a' on the visual selection\n\n"
                    "The :normal command executes normal-mode keystrokes for each\n"
                    "line in the range.\n\n"
                    "Other :normal uses:\n"
                    "  :%normal A;   → append semicolon to end of every line\n"
                    "  :%normal I//  → prepend // (comment) to every line\n"
                    "  :5,10normal dd → delete lines 5-10 one by one\n\n"
                    "This is one of the most powerful vim idioms: combining ranges\n"
                    "with :normal to apply any normal-mode operation to many lines."
                ),
                "answer": "%",
                "hints": ["The address meaning 'all lines'.", "The answer is: %"],
            },
            {
                "id": "mac_6",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Run Macro N Times",
                "flavor": "The routing table has 417 flagged entries and your macro handles one at a time. Run the macro in register 'a' exactly 417 times with a single command. What do you type?",
                "lesson": (
                    "N@{register} — run a macro N times.\n\n"
                    "  417@a  → run the macro in register 'a' exactly 417 times\n\n"
                    "This is the core power of macros: record once, run thousands of times.\n\n"
                    "What happens on failure:\n"
                    "  If the macro fails on any iteration (e.g., a search finds no match),\n"
                    "  execution stops at that point. This is intentional — it means\n"
                    "  your macro will naturally stop when it's processed all valid lines.\n\n"
                    "A well-written macro should:\n"
                    "  1. Perform the transformation on the current line/position\n"
                    "  2. End by moving to the next position (e.g., j to go down)\n"
                    "  3. So that replaying it from the new position does the next item"
                ),
                "answer": "417@a",
                "hints": ["The count goes before the @register.", "417 followed by @a.", "The answer is: 417@a"],
            },
        ],
    },
    "registers_vault": {
        "id": "registers_vault",
        "name": "The Registers Vault",
        "subtitle": "Named storage for text and macros",
        "color": "magenta",
        "icon": "📦",
        "commands": ['"a', '"ap', ":reg", '"+', ":let @a"],
        "challenges": [
            {
                "id": "rv_1",
                "type": "fill_blank",
                "title": "Yank to Named Register",
                "flavor": "You've found a critical NEXUS credential string. You need to store the current line in register 'a' before it scrolls off. What command yanks the line into register 'a'?",
                "lesson": (
                    '"ayy — yank the current line into register \'a\'.\n\n'
                    "Registers are named storage buckets. vim has 26 named registers: a–z.\n\n"
                    '  "ayy   → yank the current line into register \'a\'\n'
                    '  "add   → delete the current line into register \'a\'\n'
                    '  "ay3j  → yank 3 lines down into register \'a\'\n\n'
                    "Default (unnamed) register:\n"
                    "  Yank and delete without a register prefix goes into the unnamed register (\"\")\n"
                    "  This is what p pastes by default.\n\n"
                    '  "0  → always holds the last yank (not overwritten by deletes)\n'
                    "  This is the register to use when you've deleted something after yanking."
                ),
                "answer": '"ayy',
                "url": "https://vimhelp.org/",
                "hints": ['Start with the register prefix: "a', 'Then the yank command for a full line.', 'The answer is: "ayy'],
            },
            {
                "id": "rv_2",
                "type": "fill_blank",
                "title": "Paste from Named Register",
                "flavor": "Register 'a' holds the credential string you captured. Paste it after the cursor. What command pastes from register 'a'?",
                "lesson": (
                    '"ap — paste the contents of register \'a\' after the cursor.\n\n'
                    '  "ap   → paste after cursor from register \'a\'\n'
                    '  "aP   → paste before cursor from register \'a\'\n\n'
                    "Why use named registers?\n"
                    "  The unnamed register (\"\") is overwritten every time you yank or delete.\n"
                    "  If you yank something and then delete a line, the unnamed register now\n"
                    "  holds the deleted line — your yank is gone.\n\n"
                    '  With named registers ("a, "b, etc.):\n'
                    "    You control what goes where. The content stays until you write to it again.\n"
                    "    Essential for multi-step edit operations."
                ),
                "answer": '"ap',
                "hints": ['Register prefix "a, then paste.', '"ap pastes after cursor.', 'The answer is: "ap'],
            },
            {
                "id": "rv_3",
                "type": "fill_blank",
                "title": "List All Registers",
                "flavor": "You've been working through NEXUS files and storing fragments in multiple registers. You need to see what's in all of them. What command lists all registers?",
                "lesson": (
                    ":reg — display the contents of all registers.\n\n"
                    "  :reg       → list all non-empty registers\n"
                    '  :reg a b   → list only registers \'a\' and \'b\'\n\n'
                    "Register types shown:\n"
                    '  ""   → unnamed (last yank/delete)\n'
                    '  "0   → last explicit yank\n'
                    '  "1–"9 → last 9 deletes (most recent first)\n'
                    '  "a–"z → named registers (you control these)\n'
                    '  "+   → system clipboard\n'
                    '  "*   → selection clipboard (X11/Wayland)\n'
                    '  ".   → last inserted text\n'
                    '  ":   → last command-line command\n'
                    '  "/   → last search pattern\n\n'
                    "Reading :reg output helps debug macros — macros are stored in\n"
                    "named registers and show their contents as text."
                ),
                "answer": ":reg",
                "hints": ["It's a command-line command.", "Three letters.", "The answer is: :reg"],
            },
            {
                "id": "rv_4",
                "type": "fill_blank",
                "title": "System Clipboard Register",
                "flavor": "You've extracted a NEXUS internal IP address in vim and need to paste it into the browser on the same machine. What register prefix accesses the system clipboard?",
                "lesson": (
                    '"+ — the system clipboard register.\n\n'
                    '  "+y   → yank to system clipboard\n'
                    '  "+yy  → yank current line to system clipboard\n'
                    '  "+p   → paste from system clipboard\n\n'
                    "Two clipboard registers:\n"
                    '  "+  → system clipboard (Ctrl+C / Ctrl+V in other apps)\n'
                    '  "*  → primary selection (middle-click on Linux/X11)\n\n'
                    "Requirements:\n"
                    "  vim must be compiled with +clipboard support.\n"
                    "  Check with: vim --version | grep clipboard\n\n"
                    "In Neovim: clipboard integration is built-in via a clipboard provider.\n"
                    "  Often works automatically with pbcopy (macOS) or xclip (Linux).\n\n"
                    'The answer is just the register name: "+'
                ),
                "answer": '"+',
                "hints": ["It's the register prefix for the system clipboard.", 'Two characters: " and +', 'The answer is: "+'],
            },
            {
                "id": "rv_5",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Set Register Programmatically",
                "flavor": "You need to pre-load register 'a' with the text 'NEXUS_TOKEN' so your macro can paste it across all 417 transaction lines. What command-line command sets register 'a' to that string?",
                "lesson": (
                    ":let @a = 'text' — set a register's content from the command line.\n\n"
                    "  :let @a = 'NEXUS_TOKEN'\n\n"
                    "This is how you load a register without having to manually yank text.\n"
                    "Useful for:\n"
                    "  - Pre-loading a register before a macro run\n"
                    "  - Editing a macro (read it, modify, write back)\n"
                    "  - Scripting vim operations\n\n"
                    "To edit an existing macro in register 'a':\n"
                    '  1. "ap  → paste the macro content as text\n'
                    "  2. Edit the text\n"
                    '  3. "ayy → yank it back into register \'a\'\n\n'
                    "Or use :let directly:\n"
                    "  :let @a = @a . ' additional_text'  → append to register 'a'"
                ),
                "answer": ":let @a = 'NEXUS_TOKEN'",
                "hints": [
                    "Use :let to assign to a register variable.",
                    ":let @a = '...' — the register is addressed as @a",
                    ":let @a = 'NEXUS_TOKEN'",
                ],
            },
        ],
    },
    "ex_commands_deep": {
        "id": "ex_commands_deep",
        "name": "The Ex Commands Deep",
        "subtitle": "Advanced substitution, filtering & global operations",
        "color": "yellow",
        "icon": "⚡",
        "commands": [":s///g", ":%!sort", ":g/pat/d", ":v/pat/d", ":g/pat/cmd"],
        "challenges": [
            {
                "id": "ex_1",
                "type": "fill_blank",
                "title": "Substitute with Flags",
                "flavor": "The NEXUS routing table uses 'phantom_corp' as a vendor name. You need to replace every occurrence in the entire file with '[FLAGGED]', case-insensitively. Complete: :%s/phantom_corp/[FLAGGED]/___",
                "lesson": (
                    ":%s/pattern/replacement/gi — file-wide substitution, case-insensitive.\n\n"
                    "Substitution flags:\n"
                    "  g  → global: replace all matches on each line (not just the first)\n"
                    "  i  → case-insensitive match\n"
                    "  c  → confirm each replacement interactively\n"
                    "  e  → suppress 'no match' errors\n\n"
                    "Range prefixes:\n"
                    "  :s/…    → current line only\n"
                    "  :%s/…   → entire file (% = all lines)\n"
                    "  :1,10s/… → lines 1–10\n"
                    "  :'<,'>s/… → visual selection\n\n"
                    "Capture groups:\n"
                    "  :%s/\\(\\w\\+\\)_id/id_\\1/g  → swap prefix/suffix using \\1 backreference\n"
                    "  In Neovim with very magic: :%s/\\v(\\w+)_id/id_\\1/g"
                ),
                "answer": "gi",
                "url": "https://vimhelp.org/",
                "hints": ["Two flags: global and case-insensitive.", "g for global, i for case-insensitive.", "The answer is: gi"],
            },
            {
                "id": "ex_2",
                "type": "fill_blank",
                "title": "Sort Lines Through External Command",
                "flavor": "The NEXUS IP address list is out of order. You want to sort all lines in the current file using the system sort command. Complete: :%___sort",
                "lesson": (
                    ":%!sort — filter the entire file through an external command.\n\n"
                    "  :%!sort           → sort all lines in the file\n"
                    "  :%!sort -r        → sort in reverse\n"
                    "  :%!sort -u        → sort and deduplicate\n"
                    "  :%!column -t      → align columns in a table\n"
                    "  :%!python3 -m json.tool  → pretty-print JSON\n\n"
                    "The ! operator:\n"
                    "  :!command    → run a shell command (output appears below vim)\n"
                    "  :%!command   → filter the file through the command (replaces content)\n"
                    "  :10,20!sort  → filter only lines 10–20\n\n"
                    "This turns vim into a shell pipeline: the buffer is stdin,\n"
                    "the command's stdout replaces the selected range."
                ),
                "answer": "!",
                "hints": ["The shell filter operator — one character.", "% is the range, then the shell filter prefix.", "The answer is: !"],
            },
            {
                "id": "ex_3",
                "type": "fill_blank",
                "title": "Delete Lines Matching Pattern",
                "flavor": "The NEXUS log has thousands of 'INFO:' lines you don't need. Delete every line that contains the word 'INFO'. Complete: :g/INFO/___",
                "lesson": (
                    ":g/pattern/d — delete every line matching a pattern.\n\n"
                    "  :g/INFO/d       → delete all lines containing 'INFO'\n"
                    "  :g/^$/d         → delete all blank lines\n"
                    "  :g/^#/d         → delete all comment lines\n\n"
                    "The :g command: global execute.\n"
                    "  :g/pattern/command  → run 'command' on every line matching 'pattern'\n\n"
                    "Commands beyond delete:\n"
                    "  :g/TODO/normal yy  → yank every TODO line into the unnamed register\n"
                    "  :g/pattern/s/old/new/g  → substitute on every matching line\n"
                    "  :g/^/m0  → reverse the entire file (move each line to top)\n\n"
                    "Use with regex for power:\n"
                    "  :g/^\\s*$/d  → delete blank/whitespace-only lines"
                ),
                "answer": "d",
                "hints": ["The delete command — single character.", "d for delete.", "The answer is: d"],
            },
            {
                "id": "ex_4",
                "type": "fill_blank",
                "title": "Delete Lines NOT Matching Pattern",
                "flavor": "You only want to keep lines from the NEXUS audit log that contain 'TRANSFER'. Delete everything else. What command deletes all lines that do NOT match the pattern? Complete: :___/TRANSFER/d",
                "lesson": (
                    ":v/pattern/d — delete every line that does NOT match.\n\n"
                    "  :v/TRANSFER/d   → keep only lines containing 'TRANSFER'\n"
                    "  :v/^$/d         → keep only blank lines (delete non-blank)\n\n"
                    ":v is the inverse of :g:\n"
                    "  :g/pat/cmd  → run cmd on lines that MATCH\n"
                    "  :v/pat/cmd  → run cmd on lines that DON'T MATCH\n\n"
                    ":v stands for 'in-Verse' (inverse global).\n\n"
                    "Practical use:\n"
                    "  :v/error/d     → keep only error lines — powerful log filter\n"
                    "  :v/2024/d      → keep only lines from 2024\n\n"
                    "Combined with :g:\n"
                    "  First :v to keep relevant lines, then :g to process them."
                ),
                "answer": "v",
                "hints": ["The inverse of :g — single character.", "v for inverse global.", "The answer is: v"],
            },
            {
                "id": "ex_5",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Global Command with Action",
                "flavor": "Every line in the NEXUS transaction log that contains 'PHANTOM' needs to have the text ' -- FLAGGED' appended to it. Complete: :g/PHANTOM/___/$/  -- FLAGGED/",
                "lesson": (
                    ":g/pattern/s/$/append_text/ — append text to every matching line.\n\n"
                    "  :g/PHANTOM/s/$/ -- FLAGGED/\n\n"
                    "Breaking this down:\n"
                    "  :g/PHANTOM/   → find every line containing 'PHANTOM'\n"
                    "  s/$/ -- FLAGGED/  → substitute end-of-line with ' -- FLAGGED'\n"
                    "                     effectively appending to the line\n\n"
                    "The power of :g is combining it with any ex command:\n"
                    "  :g/TODO/t$        → copy all TODO lines to end of file\n"
                    "  :g/^=/normal dd   → delete all heading separator lines\n"
                    "  :g/SECTION/yank A → append all section headers to register A\n\n"
                    "This is the vim power-user's toolkit:\n"
                    ":g turns a single-line operation into a file-wide transformation."
                ),
                "answer": "s",
                "hints": ["The substitution command — what comes after :g/pattern/", "s for substitute.", "The answer is: s"],
            },
        ],
    },
    "motion_mastery": {
        "id": "motion_mastery",
        "name": "The Motion Mastery Chamber",
        "subtitle": "Minimal Motion, Maximum Efficiency",
        "color": "yellow",
        "icon": "⚡",
        "commands": ["w/b", "f<char>", "t<char>", "%", "ci\""],
        "challenges": [
            {
                "id": "mm_1",
                "type": "quiz",
                "title": "Word Forward",
                "flavor": "You're at the beginning of a long identifier in the NEXUS config. Move forward one word at a time. What key moves forward to the start of the next word?",
                "lesson": (
                    "w — move forward to the beginning of the next word.\n\n"
                    "Word motion pair:\n"
                    "  w  → forward to the start of the next word\n"
                    "  b  → backward to the start of the previous word\n\n"
                    "Word boundary definition:\n"
                    "  w treats punctuation as word boundaries\n"
                    "  W treats only whitespace as word boundaries (WORD motion)\n\n"
                    "Example: cursor on 'phantom' in 'phantom_corp = \"active\"'\n"
                    "  w → lands on '_' (punctuation boundary)\n"
                    "  W → lands on '=' (whitespace boundary)\n\n"
                    "Count prefix: 3w moves forward 3 words. 5b moves back 5 words.\n"
                    "Combine with operators: dw deletes to next word, cw changes to next word."
                ),
                "answer": "w",
                "url": "https://vimhelp.org/",
                "hints": ["Think: word forward. Single lowercase letter.", "w for word.", "The answer is: w"],
            },
            {
                "id": "mm_2",
                "type": "quiz",
                "title": "Word Backward",
                "flavor": "You've overshot. The cursor is three words past the target. Move backward one word at a time. What key moves back to the start of the previous word?",
                "lesson": (
                    "b — move backward to the start of the previous word.\n\n"
                    "  w  → forward one word\n"
                    "  b  → backward one word\n"
                    "  e  → forward to the END of the current/next word\n"
                    "  ge → backward to the END of the previous word\n\n"
                    "Uppercase variants (WORD motions — whitespace boundaries only):\n"
                    "  W  → forward one WORD\n"
                    "  B  → backward one WORD\n"
                    "  E  → forward to end of WORD\n\n"
                    "Practical: in 'key_name = \"value\"'\n"
                    "  b from '=' → lands on 'k' (start of key_name)\n"
                    "  B from '=' → same result (only one WORD before it)\n\n"
                    "Count: 3b moves back 3 words."
                ),
                "answer": "b",
                "hints": ["Think: backward. Single lowercase letter.", "b for backward.", "The answer is: b"],
            },
            {
                "id": "mm_3",
                "type": "quiz",
                "title": "Jump to Character",
                "flavor": "You need to move to the semicolon at the end of the current line. The line is long. Instead of pressing l repeatedly, you jump directly to it. What key does this?",
                "lesson": (
                    "f{char} — jump forward to the next occurrence of a character on the line.\n\n"
                    "  f;   → jump forward, landing ON the next semicolon\n"
                    "  F;   → jump backward, landing ON the previous semicolon\n\n"
                    "Repeat the jump:\n"
                    "  ;    → repeat the last f/t/F/T in the same direction\n"
                    "  ,    → repeat in the opposite direction\n\n"
                    "Example: 'SELECT id, name, email FROM users;'\n"
                    "  f,   → lands on the first comma\n"
                    "  ;    → jumps to the second comma\n"
                    "  ;    → jumps to the third comma\n\n"
                    "f is the Ghost Operative's sniper shot — one keystroke to any character on the line."
                ),
                "answer": "f",
                "hints": ["Think: 'find' a character on the line. Single lowercase letter.", "f for find.", "The answer is: f"],
            },
            {
                "id": "mm_4",
                "type": "quiz",
                "title": "Jump Till Character",
                "flavor": "You want to delete everything up to (but not including) a closing parenthesis. You use dt) — the t motion stops just before the target char. What key is the 'till' motion?",
                "lesson": (
                    "t{char} — jump forward to just BEFORE the next occurrence of a character.\n\n"
                    "f vs t:\n"
                    "  f{char} → lands ON the character\n"
                    "  t{char} → lands one character BEFORE it\n\n"
                    "The difference matters with operators:\n"
                    "  df)   → delete from cursor through the closing paren (inclusive)\n"
                    "  dt)   → delete from cursor up to but NOT including the closing paren\n\n"
                    "Backward variants:\n"
                    "  T{char} → jump backward to just after the previous occurrence\n\n"
                    "Practical example: cursor on 'p' in 'process(phantom_data)'\n"
                    "  dt)  → deletes 'process(phantom_data' — leaves ')' in place\n"
                    "  df)  → deletes 'process(phantom_data)' — removes the paren too\n\n"
                    "t is ideal for 'change everything up to this delimiter.'"
                ),
                "answer": "t",
                "hints": ["Think: 'till' — up to but not including. Single lowercase letter.", "t for till.", "The answer is: t"],
            },
            {
                "id": "mm_5",
                "type": "quiz",
                "title": "Jump to Matching Bracket",
                "flavor": "The cursor is on an opening brace in a deeply nested config block. You need to jump to its matching closing brace to see where the block ends. What single key does this?",
                "lesson": (
                    "% — jump to the matching bracket, parenthesis, or brace.\n\n"
                    "Supported pairs:\n"
                    "  ()  → parentheses\n"
                    "  []  → square brackets\n"
                    "  {}  → curly braces\n\n"
                    "Works in both directions:\n"
                    "  On (  → jumps to matching )\n"
                    "  On )  → jumps back to matching (\n\n"
                    "Power combinations:\n"
                    "  v%   → visually select from here to the matching bracket\n"
                    "  d%   → delete from cursor through the matching bracket\n"
                    "  y%   → yank from cursor to the matching bracket\n\n"
                    "Use % to verify nested structures are balanced — jump to the open,\n"
                    "then % to the close, then % back. If it misses, something is unbalanced."
                ),
                "answer": "%",
                "hints": ["The percent key — also the 'match' key in vim.", "Single character: %", "The answer is: %"],
            },
            {
                "id": "mm_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Change Inner Quotes",
                "flavor": "Config line: vendor = \"phantom_corp\". Cursor is anywhere on the line. You need to delete the value inside the quotes and type a replacement. What command deletes the content inside double quotes and drops you into insert mode?",
                "lesson": (
                    "ci\" — change inside double quotes: delete the content, keep the quotes, enter insert mode.\n\n"
                    "This combines:\n"
                    "  c   → the change operator (delete + enter insert mode)\n"
                    "  i   → inner modifier (content only, not the delimiters)\n"
                    "  \"   → double-quote text object\n\n"
                    "The cursor does NOT need to be inside the quotes —\n"
                    "vim finds the nearest matching pair on the current line.\n\n"
                    "Related commands:\n"
                    "  ca\"  → change AROUND quotes (deletes the quotes too)\n"
                    "  di\"  → delete inside quotes (no insert mode)\n"
                    "  yi\"  → yank inside quotes\n"
                    "  ci'  → change inside single quotes\n"
                    "  ci(  → change inside parentheses\n"
                    "  ci{  → change inside curly braces\n\n"
                    "This is the canonical vim workflow for changing config values:\n"
                    "navigate to the line, ci\", type the new value, ESC."
                ),
                "answer": "ci\"",
                "hints": ["Change (c) + inner (i) + double-quote (\").", "Three characters: c, i, then the quote character.", "The answer is: ci\""],
            },
        ],
    },
    "split_navigation": {
        "id": "split_navigation",
        "name": "The Split Navigation Hub",
        "subtitle": "Multiple Files, One Session",
        "color": "blue",
        "icon": "🪟",
        "commands": [":split/:vsplit", "Ctrl+W w", "Ctrl+W hjkl", ":resize", ":windo"],
        "challenges": [
            {
                "id": "sn_1",
                "type": "quiz",
                "title": "Vertical Split",
                "flavor": "Ghost needs two files open side by side. The processor config on the left, the routing table on the right. What command creates a vertical split?",
                "lesson": (
                    ":vsplit — open a vertical split (side by side).\n\n"
                    "Split commands:\n"
                    "  :vsplit filename  → vertical split, open file on the right\n"
                    "  :split filename   → horizontal split, open file below\n"
                    "  :vs               → shorthand for :vsplit\n"
                    "  :sp               → shorthand for :split\n\n"
                    "Without a filename:\n"
                    "  :vsplit  → split current buffer into two panes\n"
                    "  :split   → same, horizontally\n\n"
                    "Keyboard equivalents:\n"
                    "  Ctrl+W v  → vertical split current buffer\n"
                    "  Ctrl+W s  → horizontal split current buffer\n\n"
                    "Use :vsplit for files that need side-by-side comparison.\n"
                    "Use :split for files that need top-bottom reference."
                ),
                "answer": ":vsplit",
                "url": "https://vimhelp.org/",
                "hints": ["The command that splits the window vertically.", "Starts with a colon. The answer is: :vsplit"],
            },
            {
                "id": "sn_2",
                "type": "fill_blank",
                "title": "Cycle Between Splits",
                "flavor": "Three splits are open. You want to move to the next one without specifying direction. Complete the command: Ctrl+W ___",
                "lesson": (
                    "Ctrl+W w — cycle to the next split window.\n\n"
                    "Split cycling:\n"
                    "  Ctrl+W w  → move to next split (clockwise)\n"
                    "  Ctrl+W W  → move to previous split (counterclockwise)\n\n"
                    "When you have two splits, Ctrl+W w just toggles between them.\n"
                    "With more splits, it cycles through in order.\n\n"
                    "Direct navigation (faster with many splits):\n"
                    "  Ctrl+W h  → move LEFT\n"
                    "  Ctrl+W l  → move RIGHT\n"
                    "  Ctrl+W j  → move DOWN\n"
                    "  Ctrl+W k  → move UP\n\n"
                    "Jump to specific split:\n"
                    "  Ctrl+W t  → top-left split\n"
                    "  Ctrl+W b  → bottom-right split\n"
                    "  Ctrl+W p  → previous split (last visited)"
                ),
                "answer": "w",
                "hints": ["The key that cycles through windows — lowercase letter.", "w for window cycle.", "The answer is: w"],
            },
            {
                "id": "sn_3",
                "type": "fill_blank",
                "title": "Navigate Directionally",
                "flavor": "Three vertical splits: audit log (left), processor config (center), routing table (right). Cursor is in the center. Move to the rightmost split. Complete: Ctrl+W ___",
                "lesson": (
                    "Ctrl+W l — move to the split on the right.\n\n"
                    "Directional split navigation (mirrors cursor movement):\n"
                    "  Ctrl+W h  → LEFT split\n"
                    "  Ctrl+W j  → BELOW split\n"
                    "  Ctrl+W k  → ABOVE split\n"
                    "  Ctrl+W l  → RIGHT split\n\n"
                    "The same hjkl keys used for cursor movement work for split navigation.\n"
                    "This is intentional — vim uses a consistent directional vocabulary.\n\n"
                    "Moving splits (reordering):\n"
                    "  Ctrl+W H  → move current split to far LEFT (uppercase)\n"
                    "  Ctrl+W J  → move current split to bottom\n"
                    "  Ctrl+W K  → move current split to top\n"
                    "  Ctrl+W L  → move current split to far RIGHT\n\n"
                    "Uppercase H/J/K/L moves the split itself; lowercase h/j/k/l moves the cursor."
                ),
                "answer": "l",
                "hints": ["Same key as 'move cursor right' in normal mode.", "l moves right.", "The answer is: l"],
            },
            {
                "id": "sn_4",
                "type": "fill_blank",
                "title": "Resize a Split",
                "flavor": "The left split is too narrow to read the audit log. Make it 5 columns wider. Complete: :resize ___",
                "lesson": (
                    ":resize +N — increase the size of the current split by N lines/columns.\n\n"
                    "Resize commands:\n"
                    "  :resize +5     → increase height by 5 lines (horizontal splits)\n"
                    "  :resize -5     → decrease height by 5 lines\n"
                    "  :resize 20     → set height to exactly 20 lines\n"
                    "  :vertical resize +5   → increase width by 5 columns (vertical splits)\n"
                    "  :vertical resize -5   → decrease width by 5 columns\n\n"
                    "Keyboard shortcuts:\n"
                    "  Ctrl+W +  → increase height by 1\n"
                    "  Ctrl+W -  → decrease height by 1\n"
                    "  Ctrl+W >  → increase width by 1\n"
                    "  Ctrl+W <  → decrease width by 1\n"
                    "  Ctrl+W =  → equalize all splits\n\n"
                    "For a 5-unit increase, :resize +5 is faster than pressing Ctrl+W + five times."
                ),
                "answer": "+5",
                "hints": ["Increase by 5. Use the +N syntax.", "The answer is: +5"],
            },
            {
                "id": "sn_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Global Substitution Across All Windows",
                "flavor": "NEXUS is uppercase throughout all open files. It needs to be lowercase. Run a substitution across every open window simultaneously. Complete: :windo %s/NEXUS/nexus/___",
                "lesson": (
                    ":windo {cmd} — run an ex command in every open window.\n\n"
                    "  :windo %s/NEXUS/nexus/g\n\n"
                    "Breaking this down:\n"
                    "  :windo           → execute the following command in each window\n"
                    "  %s/NEXUS/nexus/  → substitute NEXUS → nexus in the entire buffer\n"
                    "  g                → global flag: replace all occurrences per line\n\n"
                    "Related multi-window/buffer commands:\n"
                    "  :bufdo %s/old/new/g    → run command in every open buffer\n"
                    "  :tabdo %s/old/new/g    → run command in every tab\n"
                    "  :argdo %s/old/new/ge   → run command on every file in the argument list\n\n"
                    "The 'e' flag at the end suppresses errors when no match is found —\n"
                    "useful with :bufdo/:windo so one file without the pattern doesn't abort the rest.\n\n"
                    ":windo is the Ghost Operative's broadcast command:\n"
                    "one operation, every open file, simultaneously."
                ),
                "answer": "g",
                "hints": ["The flag that replaces ALL occurrences on each line (not just the first).", "Single letter: global flag.", "The answer is: g"],
            },
        ],
    },
    "registers": {
        "id": "registers",
        "name": "The Registers Vault II",
        "subtitle": "Named Registers, Clipboard & Black Hole",
        "color": "yellow",
        "icon": "🗄️",
        "commands": ["\"a-z", "\"0", "\"+", "\"*", "\"_", ":reg"],
        "challenges": [
            {
                "id": "reg_1",
                "type": "quiz",
                "title": "Yank to Named Register",
                "flavor": "You need to yank the current line into register 'a' so it won't be overwritten by a future delete. What command does this?",
                "lesson": (
                    "\"ayy — yank the current line into register 'a'.\n\n"
                    "Named register syntax: \"<register><operator>\n"
                    "  \"ayy   → yank current line into register a\n"
                    "  \"add   → cut (delete) current line into register a\n"
                    "  \"ap    → paste from register a\n\n"
                    "Why named registers matter:\n"
                    "  The unnamed register (\"\") gets overwritten by every yank AND delete.\n"
                    "  Named registers (\"a through \"z) only change when you explicitly write to them.\n\n"
                    "Uppercase register appends:\n"
                    "  \"Ayy → APPEND the current line to register a (not overwrite)\n"
                    "  Useful for collecting multiple lines into one register."
                ),
                "answer": "\"ayy",
                "hints": ["Register prefix, then register name, then yank-line.", "\"a then yy.", "The answer is: \"ayy"],
            },
            {
                "id": "reg_2",
                "type": "quiz",
                "title": "The Yank Register",
                "flavor": "You yanked a line, then deleted another line — and now p pastes the deleted line, not what you yanked. Which register always holds the last explicit yank (not delete)?",
                "lesson": (
                    "\"0 — the yank register: always holds the last yanked text.\n\n"
                    "  \"0p  → paste from the yank register (safe even after subsequent deletes)\n\n"
                    "How the numbered registers work:\n"
                    "  \"0   → last yank\n"
                    "  \"1   → last delete or change (most recent)\n"
                    "  \"2   → the delete before that\n"
                    "  ...through \"9 (a rolling history of the last 9 deletes)\n\n"
                    "The unnamed register (\"\") always mirrors \"1 after a delete,\n"
                    "which is why 'p' pastes the deleted text, not the yanked text.\n"
                    "\"0p is the fix: it bypasses the delete history."
                ),
                "answer": "\"0",
                "hints": ["The register named with the digit zero.", "\"0 — it's not a letter, it's a zero.", "The answer is: \"0"],
            },
            {
                "id": "reg_3",
                "type": "quiz",
                "title": "System Clipboard Register",
                "flavor": "You need to paste text from the system clipboard (copied outside vim) into your buffer. Which register holds the system clipboard?",
                "lesson": (
                    "\"+  — the system clipboard register.\n\n"
                    "  \"+p   → paste from system clipboard into vim\n"
                    "  \"+yy  → yank current line to system clipboard\n"
                    "  \"+y{motion}  → yank motion to system clipboard\n\n"
                    "Two clipboard registers:\n"
                    "  \"+  → the system clipboard (Ctrl+C / Ctrl+V outside vim)\n"
                    "  \"*  → the X11 primary selection (middle-click paste on Linux)\n"
                    "  On macOS, both \"+  and \"* access the same clipboard.\n\n"
                    "Requirements:\n"
                    "  Vim must be compiled with +clipboard support.\n"
                    "  Check: :version and look for +clipboard or -clipboard.\n"
                    "  On macOS: use macvim or brew-installed vim with clipboard support."
                ),
                "answer": "\"+",
                "hints": ["Think: the register for the + (plus/clipboard) buffer.", "Quote then plus sign.", "The answer is: \"+"],
            },
            {
                "id": "reg_4",
                "type": "quiz",
                "title": "The Black Hole Register",
                "flavor": "You want to delete text without it going into any register — no yank history, no overwriting the unnamed register. What register is the black hole?",
                "lesson": (
                    "\"_  — the black hole register: text sent here is gone forever.\n\n"
                    "  \"_dd   → delete the line and send it nowhere\n"
                    "  \"_d{motion}  → delete motion, no register pollution\n"
                    "  \"_c{motion}  → change, without overwriting registers\n\n"
                    "When to use it:\n"
                    "  You have text in register 'a' that you need to paste multiple times.\n"
                    "  But you need to delete something in between.\n"
                    "  Normal 'dd' would overwrite the unnamed register.\n"
                    "  \"_dd deletes without disturbing any register.\n\n"
                    "  Also useful: preserving \"0 (yank register) when deleting filler text."
                ),
                "answer": "\"_",
                "hints": ["It's named with an underscore character.", "Quote then underscore.", "The answer is: \"_"],
            },
            {
                "id": "reg_5",
                "type": "fill_blank",
                "title": "Inspect All Registers",
                "flavor": "You want to see what's stored in every register before pasting. What ex command lists all register contents?",
                "lesson": (
                    ":reg — display the contents of all registers.\n\n"
                    "  :reg         → show all non-empty registers\n"
                    "  :reg a       → show only register a\n"
                    "  :reg a b c   → show registers a, b, and c\n\n"
                    "What you'll see:\n"
                    "  \"\"  — unnamed register (last yank or delete)\n"
                    "  \"0  — last explicit yank\n"
                    "  \"1-\"9  — delete history\n"
                    "  \"a-\"z  — named registers\n"
                    "  \"+  — system clipboard\n"
                    "  \"-  — small delete register (less than one line)\n"
                    "  \"=  — expression register\n"
                    "  \"/ — last search pattern\n"
                    "  \": — last command-line command\n\n"
                    ":reg is your register audit tool — Ghost always checks it\n"
                    "before pasting across files."
                ),
                "answer": ":reg",
                "hints": ["A colon command — short for 'registers'.", "Four characters including the colon.", "The answer is: :reg"],
            },
            {
                "id": "reg_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Pre-load a Register Programmatically",
                "flavor": "You need to set register 'b' to the string 'FLAGGED' without yanking anything. What ex command accomplishes this?",
                "lesson": (
                    ":let @b = 'FLAGGED' — set a register programmatically.\n\n"
                    "  :let @a = 'text'   → set register a to 'text'\n"
                    "  :let @+ = 'text'   → set the system clipboard to 'text'\n"
                    "  :let @/ = 'pattern'  → set the last-search pattern\n\n"
                    "This is powerful when building macros:\n"
                    "  Pre-load a register with a constant string.\n"
                    "  The macro references \"ap to paste it at each position.\n"
                    "  Result: 417 lines get the same annotation without re-yanking.\n\n"
                    "Register names in :let use the @ prefix:\n"
                    "  @a = register a\n"
                    "  @+ = system clipboard\n"
                    "  @_ = black hole (writing here has no effect)"
                ),
                "answer": ":let @b = 'FLAGGED'",
                "hints": [
                    "Use :let with the @register syntax.",
                    ":let @b = then the string in quotes.",
                    "The answer is: :let @b = 'FLAGGED'",
                ],
            },
        ],
    },
    "macros": {
        "id": "macros",
        "name": "The Macro Forge II",
        "subtitle": "Recording, Replaying & Editing Macros",
        "color": "magenta",
        "icon": "⚙️",
        "commands": ["q{reg}", "@{reg}", "@@", "N@{reg}", ":normal @a", ":let @a="],
        "challenges": [
            {
                "id": "mac_1",
                "type": "fill_blank",
                "title": "Start Recording a Macro",
                "flavor": "You need to record a macro into register 'q'. What key sequence starts recording?",
                "lesson": (
                    "qq — start recording a macro into register 'q'.\n\n"
                    "Macro recording:\n"
                    "  q{register}  → start recording into that register (a–z, 0–9)\n"
                    "  q            → stop recording (same key)\n\n"
                    "Visual indicator:\n"
                    "  While recording, vim shows 'recording @q' in the status line.\n\n"
                    "What gets recorded:\n"
                    "  Every normal-mode command, every keystroke in insert mode,\n"
                    "  every ex command — everything until you press q to stop.\n\n"
                    "Best practice:\n"
                    "  Start the macro at a known position on the line (e.g. 0 to go to col 1).\n"
                    "  End with a motion that moves to the next line (e.g. j).\n"
                    "  This makes the macro repeatable across multiple lines."
                ),
                "answer": "qq",
                "hints": ["The record key, then the register name.", "q + q (using register q).", "The answer is: qq"],
            },
            {
                "id": "mac_2",
                "type": "quiz",
                "title": "Replay a Macro",
                "flavor": "You recorded a macro in register 'a'. What command replays it once?",
                "lesson": (
                    "@a — replay the macro stored in register 'a'.\n\n"
                    "  @{register}  → replay macro in that register\n"
                    "  @@           → replay the last-used macro (whatever register it was in)\n"
                    "  5@a          → replay macro in register 'a' five times\n"
                    "  100@a        → replay 100 times\n\n"
                    "Stopping early:\n"
                    "  If the macro hits an error (e.g. a motion that fails), it stops.\n"
                    "  This is useful: run 999@a on a file with 50 lines — it will stop\n"
                    "  when it runs out of lines, without you counting.\n\n"
                    "The count prefix:\n"
                    "  Type the count BEFORE @a: 416@a runs the macro 416 more times\n"
                    "  after you've already done it once manually for 417 total."
                ),
                "answer": "@a",
                "hints": ["@ symbol then the register letter.", "@a to replay register a.", "The answer is: @a"],
            },
            {
                "id": "mac_3",
                "type": "quiz",
                "title": "Replay the Last Macro",
                "flavor": "You just ran @a. You want to repeat the last-used macro without specifying the register. What command does this?",
                "lesson": (
                    "@@ — replay the last-used macro.\n\n"
                    "  @@   → replay whatever macro you ran most recently\n\n"
                    "Why @@ is useful:\n"
                    "  After running @a, you can press @@ repeatedly instead of @a.\n"
                    "  Saves one keystroke — trivial in isolation, significant across hundreds of operations.\n\n"
                    "  Also useful when dot (.) won't do:\n"
                    "  . repeats the last *change* (single edit operation).\n"
                    "  @@ replays the entire macro sequence — multiple operations.\n\n"
                    "Combining with count:\n"
                    "  After the first @a, pressing 415@@ runs 415 more iterations."
                ),
                "answer": "@@",
                "hints": ["Double @ — the 'last macro' shorthand.", "Two @ characters.", "The answer is: @@"],
            },
            {
                "id": "mac_4",
                "type": "fill_blank",
                "title": "Apply Macro to a Range",
                "flavor": "You want to apply macro 'a' to every line in the file. What ex command does this?",
                "lesson": (
                    ":%normal @a — run macro 'a' on every line in the file.\n\n"
                    "  :%normal @a       → apply macro to all lines\n"
                    "  :10,20normal @a   → apply macro to lines 10–20\n"
                    "  :'<,'>normal @a   → apply macro to visual selection\n\n"
                    ":normal runs normal-mode commands from the command line.\n"
                    "It respects the range, executing on each line in turn.\n\n"
                    "Why use this instead of 9999@a?\n"
                    "  More explicit about the target range.\n"
                    "  :10,20normal @a applies ONLY to those lines, not beyond.\n"
                    "  Works on visual selections, which count-based replay can't do.\n\n"
                    "Other uses of :normal:\n"
                    "  :%normal I# → prepend # to every line (comment out a file)\n"
                    "  :%normal A; → append ; to every line"
                ),
                "answer": ":%normal @a",
                "hints": ["Range + normal command + macro replay.", ":% for all lines, normal to run keystrokes, @a to invoke the macro.", "The answer is: :%normal @a"],
            },
            {
                "id": "mac_5",
                "type": "quiz",
                "title": "Edit a Macro",
                "flavor": "Your macro in register 'a' has a typo. You want to edit it as text. Which command lets you paste the macro contents into the buffer to edit it?",
                "lesson": (
                    "\"ap — paste the macro from register 'a' into the buffer for editing.\n\n"
                    "The macro-editing workflow:\n"
                    "  1. Open a blank line (o in normal mode)\n"
                    "  2. \"ap → paste the macro text\n"
                    "  3. Edit the text directly (fix the typo)\n"
                    "  4. Yank the corrected line back: \"ayy\n"
                    "  5. Delete the scratch line: dd\n\n"
                    "Why this works:\n"
                    "  Macros ARE register contents — they're just strings of keystrokes.\n"
                    "  \"ap exposes the raw keystroke string as editable text.\n"
                    "  \"ayy saves the edited string back as the macro.\n\n"
                    "Alternative: :let @a = 'new_macro_text'\n"
                    "  Useful for short macros you can construct mentally."
                ),
                "answer": "\"ap",
                "hints": ["Paste from register a.", "Quote, register letter, then paste.", "The answer is: \"ap"],
            },
            {
                "id": "mac_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Count-Based Macro Replay",
                "flavor": "You've verified your macro in register 'a' works correctly on one line. There are 416 remaining lines to process. What command runs the macro 416 more times?",
                "lesson": (
                    "416@a — run macro 'a' 416 times.\n\n"
                    "Count-prefix syntax:\n"
                    "  N@{reg}  → replay macro N times\n"
                    "  416@a    → replay register a 416 times\n\n"
                    "How to think about count vs :normal range:\n"
                    "  416@a  → fast, simple, stops on error (can be a feature)\n"
                    "  :2,417normal @a  → explicit range, more controlled\n\n"
                    "The 'stop on error' behavior:\n"
                    "  If the macro hits a motion that fails (e.g. no more lines), it aborts.\n"
                    "  Running 9999@a on a 417-line file: the macro stops at line 417.\n"
                    "  Ghost's technique: use a count slightly larger than needed.\n"
                    "  The macro self-terminates when it runs out of targets.\n\n"
                    "After 416@a: all 417 transactions flagged. Done."
                ),
                "answer": "416@a",
                "hints": ["Count prefix before the @ command.", "416 then @a.", "The answer is: 416@a"],
            },
        ],
    },
    "marks_and_jumps": {
        "id": "marks_and_jumps",
        "name": "The Mark & Jump Grid",
        "subtitle": "Marks, Jump List & Change List",
        "color": "cyan",
        "icon": "📍",
        "commands": ["m{a-z}", "`a/`A", "Ctrl-o/Ctrl-i", "g;/g,", ":marks", "''"],
        "challenges": [
            {
                "id": "mj_1",
                "type": "fill_blank",
                "title": "Set a Local Mark",
                "flavor": "You're at a key line in the processor config. You want to bookmark this position so you can jump back to it. What command sets mark 'a' at the current cursor position?",
                "lesson": (
                    "ma — set mark 'a' at the current position.\n\n"
                    "Mark syntax:\n"
                    "  m{a-z}  → set a local mark (lowercase: file-local)\n"
                    "  m{A-Z}  → set a global mark (uppercase: works across files)\n\n"
                    "  ma  → mark 'a' at current position in this file\n"
                    "  mA  → mark 'A' — global, can jump to it from any file\n\n"
                    "Marks are invisible bookmarks.\n"
                    "They move with the text when lines are inserted or deleted above them.\n\n"
                    "Use cases:\n"
                    "  Mark the start of a section before navigating away.\n"
                    "  Mark multiple points of interest and jump between them.\n"
                    "  Use global marks to jump between files instantly."
                ),
                "answer": "ma",
                "hints": ["m to set a mark, then the mark letter.", "m then a.", "The answer is: ma"],
            },
            {
                "id": "mj_2",
                "type": "fill_blank",
                "title": "Jump to a Mark",
                "flavor": "You set mark 'a' earlier. Now you want to jump back to the exact column position of that mark. What command jumps to the exact position (line AND column) of mark 'a'?",
                "lesson": (
                    "`a — jump to the exact position (line and column) of mark 'a'.\n\n"
                    "Two jump-to-mark commands:\n"
                    "  `a  → jump to the exact line AND column of mark a\n"
                    "  'a  → jump to the first non-whitespace character on mark a's line\n\n"
                    "Backtick (`) is precise; single-quote (') is line-approximate.\n\n"
                    "Special marks:\n"
                    "  ``  → jump back to the position before the last jump\n"
                    "  `.  → jump to the position of the last change\n"
                    "  `^  → jump to position where insert mode was last exited\n"
                    "  `[  → start of last yanked or changed text\n"
                    "  `]  → end of last yanked or changed text\n\n"
                    "`` (double backtick) is the 'go back' key — jump somewhere, then `` to return."
                ),
                "answer": "`a",
                "hints": ["Backtick (not single quote) then the mark letter.", "`a — backtick for exact position.", "The answer is: `a"],
            },
            {
                "id": "mj_3",
                "type": "quiz",
                "title": "Jump Back in Jump List",
                "flavor": "You searched for a pattern and jumped to a match deep in the file. You want to go back to where you were before the search. What key sequence jumps backwards through the jump list?",
                "lesson": (
                    "Ctrl+O — jump back (older) in the jump list.\n\n"
                    "Jump list navigation:\n"
                    "  Ctrl+O  → go to older position (back in history)\n"
                    "  Ctrl+I  → go to newer position (forward in history, or Tab)\n\n"
                    "What creates jump list entries:\n"
                    "  /, ?, n, N  → search jumps\n"
                    "  G, gg, NNG  → line jumps\n"
                    "  %, (, )     → structural jumps\n"
                    "  :N          → ex line jumps\n"
                    "  Any mark jump (`a, 'a, etc.)\n\n"
                    "The jump list is per-window and holds up to 100 positions.\n"
                    ":jumps shows the full list with position numbers.\n\n"
                    "Ctrl+O is 'go back' — the muscle memory equivalent of a browser's back button."
                ),
                "answer": "Ctrl+O",
                "hints": ["Ctrl and the letter O — O for Older.", "Ctrl+O to go back.", "The answer is: Ctrl+O"],
            },
            {
                "id": "mj_4",
                "type": "quiz",
                "title": "Jump Forward in Jump List",
                "flavor": "You went back through the jump list with Ctrl+O. Now you want to go forward again (to where you were before going back). What key does this?",
                "lesson": (
                    "Ctrl+I — jump forward (newer) in the jump list.\n\n"
                    "  Ctrl+O  → back (older)\n"
                    "  Ctrl+I  → forward (newer)\n\n"
                    "Note: Ctrl+I is the same as the Tab key in terminals.\n"
                    "If your terminal intercepts Tab, Ctrl+I may not work — use :jumps\n"
                    "and navigate manually if needed.\n\n"
                    "The jump list pattern:\n"
                    "  You navigate forward deep into a file.\n"
                    "  Ctrl+O multiple times to go back to where you started.\n"
                    "  Ctrl+I to go forward again if you went too far back.\n\n"
                    "This is vim's 'undo for navigation' — independent of edit undo."
                ),
                "answer": "Ctrl+I",
                "hints": ["Ctrl and the letter I — pairs with Ctrl+O.", "Ctrl+I to go forward.", "The answer is: Ctrl+I"],
            },
            {
                "id": "mj_5",
                "type": "quiz",
                "title": "Jump to Previous Change",
                "flavor": "You made a change somewhere in the file and navigated away. You want to jump back to the most recent change location. What command does this?",
                "lesson": (
                    "g; — jump to the previous position in the change list.\n\n"
                    "Change list navigation:\n"
                    "  g;  → jump to the previous (older) change\n"
                    "  g,  → jump to the next (newer) change\n\n"
                    "Change list vs jump list:\n"
                    "  Jump list:   tracks cursor movements (/, G, marks, etc.)\n"
                    "  Change list: tracks edit locations (insert mode, d, c, etc.)\n\n"
                    "The change list is per-buffer and holds up to 100 change positions.\n"
                    ":changes shows the full list.\n\n"
                    "`. (backtick-dot) also jumps to the last change —\n"
                    "it's the most recent entry in the change list.\n"
                    "g; lets you go back through older changes step by step."
                ),
                "answer": "g;",
                "hints": ["Two-character command: g followed by semicolon.", "g; for older changes.", "The answer is: g;"],
            },
            {
                "id": "mj_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Global Mark Jump",
                "flavor": "You're editing the processor config and need to jump to a position in the audit log (a different file). You previously set global mark 'A' there. What command jumps to the exact position of global mark 'A'?",
                "lesson": (
                    "`A — jump to the exact position of global mark 'A' (in any file).\n\n"
                    "Global marks (uppercase A–Z):\n"
                    "  mA   → set global mark 'A' at current position\n"
                    "  `A   → jump to global mark 'A' (opens the file if needed)\n"
                    "  'A   → jump to the line of global mark 'A'\n\n"
                    "Global marks persist across vim sessions (stored in viminfo/shada).\n"
                    "You can bookmark specific lines in specific files and return to them\n"
                    "instantly — even after closing and reopening vim.\n\n"
                    "Ghost's strategy:\n"
                    "  mA  → mark the processor config's critical section\n"
                    "  mB  → mark the routing table's header\n"
                    "  mC  → mark the audit log's last clear timestamp\n"
                    "  Jump between all three with `A, `B, `C — no search needed."
                ),
                "answer": "`A",
                "hints": ["Backtick then the uppercase mark letter.", "`A — global marks use uppercase letters.", "The answer is: `A"],
            },
        ],
    },
    "advanced_editing": {
        "id": "advanced_editing",
        "name": "The Advanced Editing Suite",
        "subtitle": "Repeat, Increment, Sort & Power Commands",
        "color": "red",
        "icon": "⚡",
        "commands": [".", "Ctrl+a/Ctrl+x", "J", "gU/gu/g~", ":sort", "g commands"],
        "challenges": [
            {
                "id": "ae_1",
                "type": "quiz",
                "title": "Repeat the Last Change",
                "flavor": "You just ran ciw to change a word and typed a replacement. Now your cursor is on another word that needs the same replacement. What key repeats the last change?",
                "lesson": (
                    ". (dot) — repeat the last change.\n\n"
                    "What . repeats:\n"
                    "  Any normal-mode change: dd, ciw, o<text>ESC, >>...\n"
                    "  The entire insert-mode session: everything typed between i/a/o and ESC.\n\n"
                    "What . does NOT repeat:\n"
                    "  Cursor movements (j, w, f,)\n"
                    "  Ex commands (:s/…/…/)\n"
                    "  Undo (u)\n\n"
                    "The dot formula (from 'Practical Vim'):\n"
                    "  1. Find the target.\n"
                    "  2. Make the change once.\n"
                    "  3. Navigate to the next target.\n"
                    "  4. Press . — the change is applied again.\n\n"
                    "Combining with n:\n"
                    "  /word → n → . → n → . → repeat: find next, apply change."
                ),
                "answer": ".",
                "hints": ["A single punctuation key — the most powerful key in vim.", "The dot key.", "The answer is: ."],
            },
            {
                "id": "ae_2",
                "type": "quiz",
                "title": "Increment a Number",
                "flavor": "The cursor is on the number 7 in a config value. You want to increase it to 8. What key increments the number under the cursor?",
                "lesson": (
                    "Ctrl+A — increment the number under (or after) the cursor.\n\n"
                    "  Ctrl+A  → increment the nearest number by 1\n"
                    "  Ctrl+X  → decrement the nearest number by 1\n"
                    "  10 Ctrl+A  → increment by 10\n\n"
                    "What counts as a number:\n"
                    "  Decimal: 42 → 43\n"
                    "  Hexadecimal: 0x1a → 0x1b (vim auto-detects)\n"
                    "  Octal: 010 → 011 (if 'nrformats' includes 'octal')\n\n"
                    "Cursor doesn't need to be ON the number:\n"
                    "  Ctrl+A finds the next number on the line from the cursor position.\n\n"
                    "Useful in macros:\n"
                    "  Record: go to start of line, Ctrl+A, j (down)\n"
                    "  Replay: increments numbers on consecutive lines\n"
                    "  Creates auto-incrementing sequences from a macro."
                ),
                "answer": "Ctrl+A",
                "hints": ["Ctrl and the letter A.", "Ctrl+A — A for Add (increment).", "The answer is: Ctrl+A"],
            },
            {
                "id": "ae_3",
                "type": "quiz",
                "title": "Join Lines",
                "flavor": "Two lines need to be merged into one: 'TRANSFER' on one line and 'phantom_acct_7' on the next. The cursor is on the first line. What command joins the next line onto the current line?",
                "lesson": (
                    "J — join the line below onto the current line.\n\n"
                    "  J   → join next line, adding a single space between\n"
                    "  gJ  → join next line, NO space added\n"
                    "  3J  → join the next 3 lines onto the current line\n\n"
                    "J (uppercase) vs j (lowercase):\n"
                    "  j  → move cursor down (navigation)\n"
                    "  J  → join lines (editing)\n\n"
                    "After J:\n"
                    "  The joined line has trailing whitespace stripped from the first line.\n"
                    "  A single space is inserted between the two parts.\n"
                    "  Exception: if the second line starts with ), no space is added.\n\n"
                    "Visual mode + J:\n"
                    "  Select multiple lines with V, then J joins them all into one."
                ),
                "answer": "J",
                "hints": ["Uppercase J — not lowercase j (which moves down).", "J for Join.", "The answer is: J"],
            },
            {
                "id": "ae_4",
                "type": "fill_blank",
                "title": "Sort Lines",
                "flavor": "A block of IP addresses in the routing table needs to be sorted alphabetically. What ex command sorts all lines in the file?",
                "lesson": (
                    ":sort — sort lines in the file or range.\n\n"
                    "  :sort          → sort all lines alphabetically\n"
                    "  :%sort         → same (% = entire file)\n"
                    "  :10,20sort     → sort lines 10–20\n"
                    "  :'<,'>sort     → sort visual selection\n"
                    "  :sort!         → reverse sort\n"
                    "  :sort u        → sort and remove duplicates (unique)\n"
                    "  :sort n        → numeric sort (sorts numbers correctly)\n"
                    "  :sort r /pattern/  → sort by the pattern match within each line\n\n"
                    "Combining with pipes:\n"
                    "  :%!sort -u    → use the system sort (faster for huge files)\n"
                    "  :%!sort -k2   → sort by second column (system sort flags)\n\n"
                    "For the IP list: :%sort or :'<,'>sort on the visual selection."
                ),
                "answer": ":sort",
                "hints": ["A colon command — the word 'sort'.", ":sort with a colon prefix.", "The answer is: :sort"],
            },
            {
                "id": "ae_5",
                "type": "fill_blank",
                "title": "Uppercase a Line",
                "flavor": "The current line needs to be fully uppercased for emphasis in the report. What command converts the entire current line to uppercase?",
                "lesson": (
                    "gUU — uppercase the entire current line.\n\n"
                    "Case conversion operators:\n"
                    "  gU{motion}  → uppercase (e.g. gUw = uppercase next word)\n"
                    "  gu{motion}  → lowercase (e.g. guw = lowercase next word)\n"
                    "  g~{motion}  → toggle case (e.g. g~w = toggle next word's case)\n\n"
                    "Line shortcuts (doubled operator = current line):\n"
                    "  gUU  → uppercase entire line\n"
                    "  guu  → lowercase entire line\n"
                    "  g~~  → toggle case of entire line\n\n"
                    "  ~ (tilde alone) → toggle case of character under cursor and advance\n\n"
                    "With visual mode:\n"
                    "  V then U  → uppercase selected lines\n"
                    "  V then u  → lowercase selected lines\n"
                    "  V then ~  → toggle case of selected lines"
                ),
                "answer": "gUU",
                "hints": ["gU operator doubled for the whole line.", "gU then U again.", "The answer is: gUU"],
            },
            {
                "id": "ae_boss",
                "type": "fill_blank",
                "is_boss": True,
                "title": "Boss: Decrement a Number",
                "flavor": "The timeout value in the config is 90. It needs to drop to 30. The cursor is on the number 90. What single command decrements it by 60?",
                "lesson": (
                    "60 Ctrl+X — decrement the number under the cursor by 60.\n\n"
                    "  Ctrl+X       → decrement by 1\n"
                    "  60 Ctrl+X    → decrement by 60\n"
                    "  Ctrl+A       → increment by 1\n"
                    "  60 Ctrl+A    → increment by 60\n\n"
                    "Count prefix with Ctrl+X:\n"
                    "  Type the count (60) THEN press Ctrl+X.\n"
                    "  vim applies the decrement in one operation.\n\n"
                    "Combined with macros:\n"
                    "  Record: 0 (go to line start), f<digit> (find number), 60 Ctrl+X, j\n"
                    "  Replay on all lines: decrements every timeout value by 60\n\n"
                    "90 - 60 = 30. One command. No mental arithmetic at the keyboard."
                ),
                "answer": "60 Ctrl+X",
                "hints": ["Count prefix, then the decrement key.", "60 then Ctrl+X.", "The answer is: 60 Ctrl+X"],
            },
        ],
    },
}

ZONE_ORDER = [
    "normal_vault",
    "insert_protocol",
    "command_line",
    "visual_mode",
    "search_engine",
    "motion_objects",
    "split_network",
    "macro_forge",
    "registers_vault",
    "ex_commands_deep",
    "motion_mastery",
    "split_navigation",
    "registers",
    "macros",
    "marks_and_jumps",
    "advanced_editing",
]
