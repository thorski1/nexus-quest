"""
zones.py - All zone and challenge data for Python Ops
Challenge type: quiz
"""

ZONES = {
    "python_basics": {
        "id": "python_basics",
        "name": "The Python Foundation",
        "subtitle": "Print, Variables, Basic Types",
        "color": "cyan",
        "icon": "🐍",
        "commands": ["print()", "type()", "int", "float", "str", "bool"],
        "challenges": [
            {
                "id": "pyb_1",
                "type": "quiz",
                "title": "First Output",
                "question": "What function do you use to display output to the screen in Python?",
                "answers": ["print()", "print"],
                "url": "https://docs.python.org/3/tutorial/introduction.html",
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a built-in function that outputs text.",
                    "Think: you want to print something to the terminal.",
                ],
                "lesson": (
                    "print() — outputs text or values to standard output.\n\n"
                    "Syntax: print(value, ...)\n\n"
                    "Examples:\n"
                    "  print('Hello, World!')    → Hello, World!\n"
                    "  print(42)                 → 42\n"
                    "  print('x =', x)           → x = 5"
                ),
            },
            {
                "id": "pyb_2",
                "type": "quiz",
                "title": "The String Type",
                "question": "What Python type represents text data enclosed in quotes?",
                "answers": ["str"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the type for text. Short for 'string'.",
                    "Three letters: s-t-r.",
                ],
                "lesson": (
                    "str — Python's text data type. Strings are immutable sequences of characters.\n\n"
                    "Creation:\n"
                    "  name = 'Ghost'        # single quotes\n"
                    "  name = \"Ghost\"        # double quotes\n"
                    "  name = '''Ghost'''    # triple quotes (multiline)\n\n"
                    "type('Ghost') returns <class 'str'>"
                ),
            },
            {
                "id": "pyb_3",
                "type": "quiz",
                "title": "Integer Check",
                "question": "What built-in function returns the type of a Python object?",
                "answers": ["type()", "type"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It tells you what kind of object something is.",
                    "The function is named after the concept of 'data type'.",
                ],
                "lesson": (
                    "type() — returns the type of an object.\n\n"
                    "Examples:\n"
                    "  type(42)       → <class 'int'>\n"
                    "  type(3.14)     → <class 'float'>\n"
                    "  type('hello')  → <class 'str'>\n"
                    "  type(True)     → <class 'bool'>\n\n"
                    "Useful for debugging and verifying variable types."
                ),
            },
            {
                "id": "pyb_4",
                "type": "quiz",
                "title": "Boolean Logic",
                "question": "In Python, what are the two possible values of a boolean (bool)?",
                "answers": ["True and False", "True/False", "True, False"],
                "xp": 75,
                "difficulty": "easy",
                "hints": [
                    "Booleans represent on/off, yes/no logic.",
                    "They are capitalized in Python — not 'true' or 'false'.",
                ],
                "lesson": (
                    "bool — Python's boolean type. Only two values: True and False.\n\n"
                    "Note: capitalization matters — True/False, not true/false.\n\n"
                    "Examples:\n"
                    "  active = True\n"
                    "  locked = False\n"
                    "  type(True)   → <class 'bool'>\n\n"
                    "Booleans are the foundation of all conditional logic."
                ),
            },
            {
                "id": "pyb_5",
                "type": "quiz",
                "title": "Float Precision",
                "question": "What Python type represents decimal (floating-point) numbers?",
                "answers": ["float"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the type for numbers with a decimal point.",
                    "Think: floating-point number.",
                ],
                "lesson": (
                    "float — Python's decimal number type.\n\n"
                    "Examples:\n"
                    "  price = 3.14\n"
                    "  ratio = 0.043\n"
                    "  type(3.14)   → <class 'float'>\n\n"
                    "Floats are used for scientific data, financial calculations, and any\n"
                    "value requiring fractional precision."
                ),
            },
            {
                "id": "pyb_boss",
                "type": "quiz",
                "title": "BOSS: Type Coercion",
                "question": "What function converts a string like '42' into an integer in Python?",
                "answers": ["int()", "int"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It shares its name with the integer type itself.",
                    "int('42') returns 42 as a number, not a string.",
                ],
                "lesson": (
                    "int() — converts a value to an integer.\n\n"
                    "Examples:\n"
                    "  int('42')    → 42\n"
                    "  int(3.9)     → 3  (truncates, does not round)\n"
                    "  int(True)    → 1\n"
                    "  int(False)   → 0\n\n"
                    "Type coercion is essential when parsing data from files or network input."
                ),
            },
        ],
    },

    "control_flow": {
        "id": "control_flow",
        "name": "Flow Control Hub",
        "subtitle": "Conditionals and Loops",
        "color": "yellow",
        "icon": "⚡",
        "commands": ["if", "elif", "else", "for", "while", "break", "continue"],
        "challenges": [
            {
                "id": "cf_1",
                "type": "quiz",
                "title": "The Branch Gate",
                "question": "What Python keyword begins a conditional statement?",
                "url": "https://docs.python.org/3/tutorial/controlflow.html",
                "answers": ["if"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It checks a condition and branches execution.",
                    "One of the most fundamental keywords in any language.",
                ],
                "lesson": (
                    "if — begins a conditional block. Executes only when the condition is True.\n\n"
                    "Syntax:\n"
                    "  if condition:\n"
                    "      # code runs if condition is True\n\n"
                    "Example:\n"
                    "  if access_level > 3:\n"
                    "      print('Access granted')"
                ),
            },
            {
                "id": "cf_2",
                "type": "quiz",
                "title": "Alternate Path",
                "question": "What keyword handles additional conditions after an initial 'if' in Python?",
                "answers": ["elif"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a contraction of 'else if'.",
                    "Four letters: e-l-i-f.",
                ],
                "lesson": (
                    "elif — short for 'else if'. Checks additional conditions if prior ones were False.\n\n"
                    "Syntax:\n"
                    "  if x == 1:\n"
                    "      print('one')\n"
                    "  elif x == 2:\n"
                    "      print('two')\n"
                    "  else:\n"
                    "      print('other')\n\n"
                    "Chain as many elif blocks as needed."
                ),
            },
            {
                "id": "cf_3",
                "type": "quiz",
                "title": "Sequence Sweep",
                "question": "What Python keyword iterates over each item in a sequence or collection?",
                "answers": ["for"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It loops over items one by one.",
                    "Commonly paired with 'in': ___ x in collection.",
                ],
                "lesson": (
                    "for — iterates over items in any iterable (list, string, range, dict, etc.).\n\n"
                    "Syntax:\n"
                    "  for item in collection:\n"
                    "      # process item\n\n"
                    "Examples:\n"
                    "  for name in suspects:\n"
                    "      print(name)\n\n"
                    "  for i in range(5):\n"
                    "      print(i)    → 0 1 2 3 4"
                ),
            },
            {
                "id": "cf_4",
                "type": "quiz",
                "title": "Condition Loop",
                "question": "What Python keyword creates a loop that continues as long as a condition is True?",
                "answers": ["while"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It keeps looping WHILE something is true.",
                    "Five letters — the loop runs until its condition becomes False.",
                ],
                "lesson": (
                    "while — repeats a block as long as its condition remains True.\n\n"
                    "Syntax:\n"
                    "  while condition:\n"
                    "      # loop body\n\n"
                    "Example:\n"
                    "  attempts = 0\n"
                    "  while attempts < 3:\n"
                    "      attempts += 1\n\n"
                    "Warning: always ensure the condition can become False to avoid infinite loops."
                ),
            },
            {
                "id": "cf_5",
                "type": "quiz",
                "title": "Abort Signal",
                "question": "What keyword immediately exits a loop in Python?",
                "answers": ["break"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It breaks out of the loop entirely.",
                    "Think: emergency stop for a loop.",
                ],
                "lesson": (
                    "break — immediately terminates the nearest enclosing loop.\n\n"
                    "Example:\n"
                    "  for record in records:\n"
                    "      if record['status'] == 'FOUND':\n"
                    "          target = record\n"
                    "          break    # stop searching once found\n\n"
                    "Works in both for and while loops."
                ),
            },
            {
                "id": "cf_boss",
                "type": "quiz",
                "title": "BOSS: Skip and Continue",
                "question": "What keyword skips the rest of the current loop iteration and moves to the next?",
                "answers": ["continue"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It doesn't exit the loop — it skips to the next cycle.",
                    "The loop continues, but the current iteration is cut short.",
                ],
                "lesson": (
                    "continue — skips the remainder of the current iteration and proceeds to the next.\n\n"
                    "Example:\n"
                    "  for entry in audit_log:\n"
                    "      if entry['type'] == 'noise':\n"
                    "          continue    # skip noise entries\n"
                    "      process(entry)\n\n"
                    "Unlike break, continue does not exit the loop."
                ),
            },
        ],
    },

    "functions_lab": {
        "id": "functions_lab",
        "name": "The Functions Laboratory",
        "subtitle": "def, return, *args, **kwargs, lambda",
        "color": "magenta",
        "icon": "⚗",
        "commands": ["def", "return", "*args", "**kwargs", "lambda"],
        "challenges": [
            {
                "id": "fn_1",
                "type": "quiz",
                "title": "Define Operation",
                "question": "What keyword defines a function in Python?",
                "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
                "answers": ["def"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's short for 'define'.",
                    "Three letters: d-e-f.",
                ],
                "lesson": (
                    "def — declares a function.\n\n"
                    "Syntax:\n"
                    "  def function_name(parameters):\n"
                    "      # function body\n"
                    "      return value\n\n"
                    "Example:\n"
                    "  def extract(target, depth):\n"
                    "      return scan(target, depth)"
                ),
            },
            {
                "id": "fn_2",
                "type": "quiz",
                "title": "Return Signal",
                "question": "What keyword sends a value back from a function to its caller?",
                "answers": ["return"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It exits the function and passes a value out.",
                    "Without it, a function returns None by default.",
                ],
                "lesson": (
                    "return — exits a function and optionally passes a value to the caller.\n\n"
                    "Examples:\n"
                    "  def square(n):\n"
                    "      return n * n\n\n"
                    "  result = square(5)    → result is 25\n\n"
                    "A function without return (or with bare return) returns None."
                ),
            },
            {
                "id": "fn_3",
                "type": "quiz",
                "title": "Variable Arguments",
                "question": "What syntax collects an arbitrary number of positional arguments into a tuple?",
                "answers": ["*args"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It uses a single asterisk before the parameter name.",
                    "By convention the parameter is named 'args', but the * is what matters.",
                ],
                "lesson": (
                    "*args — collects extra positional arguments into a tuple.\n\n"
                    "Syntax:\n"
                    "  def log(*args):\n"
                    "      for item in args:\n"
                    "          print(item)\n\n"
                    "  log('breach', 'server-4', 'admin')    → prints each item\n\n"
                    "The name 'args' is convention; the * prefix is the actual syntax."
                ),
            },
            {
                "id": "fn_4",
                "type": "quiz",
                "title": "Keyword Harvest",
                "question": "What syntax collects arbitrary keyword arguments into a dictionary?",
                "answers": ["**kwargs"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It uses double asterisks before the parameter name.",
                    "The result is a dictionary of name=value pairs.",
                ],
                "lesson": (
                    "**kwargs — collects extra keyword arguments into a dictionary.\n\n"
                    "Syntax:\n"
                    "  def configure(**kwargs):\n"
                    "      for key, value in kwargs.items():\n"
                    "          print(f'{key} = {value}')\n\n"
                    "  configure(host='nexus-db', port=5432, ssl=True)\n\n"
                    "Often combined with *args: def func(*args, **kwargs)."
                ),
            },
            {
                "id": "fn_5",
                "type": "quiz",
                "title": "Anonymous Operative",
                "question": "What keyword creates an anonymous (unnamed) function in Python?",
                "answers": ["lambda"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "It's a single-expression function with no name.",
                    "Named after the lambda calculus concept.",
                ],
                "lesson": (
                    "lambda — creates an anonymous function in a single expression.\n\n"
                    "Syntax: lambda parameters: expression\n\n"
                    "Examples:\n"
                    "  double = lambda x: x * 2\n"
                    "  double(5)    → 10\n\n"
                    "  sorted(records, key=lambda r: r['amount'])    # sort by amount\n\n"
                    "Lambdas are limited to a single expression — use def for complex logic."
                ),
            },
            {
                "id": "fn_boss",
                "type": "quiz",
                "title": "BOSS: Scope Breach",
                "question": "What keyword inside a function allows it to modify a variable defined in the enclosing module scope?",
                "answers": ["global"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Without it, assignment inside a function creates a local variable.",
                    "It declares the variable as belonging to the module-level scope.",
                ],
                "lesson": (
                    "global — declares that a variable name refers to the module-level global scope.\n\n"
                    "Example:\n"
                    "  counter = 0\n\n"
                    "  def increment():\n"
                    "      global counter\n"
                    "      counter += 1\n\n"
                    "Without the global declaration, counter += 1 would raise an UnboundLocalError.\n"
                    "Use sparingly — global state makes code harder to reason about."
                ),
            },
        ],
    },

    "data_structures": {
        "id": "data_structures",
        "name": "The Data Vault",
        "subtitle": "list, dict, tuple, set",
        "color": "blue",
        "icon": "🗄",
        "commands": ["list", "dict", "tuple", "set", ".append()", ".get()", ".keys()"],
        "challenges": [
            {
                "id": "ds_1",
                "type": "quiz",
                "title": "Ordered Sequence",
                "question": "What Python data structure stores an ordered, mutable sequence of items in square brackets?",
                "url": "https://docs.python.org/3/tutorial/datastructures.html",
                "answers": ["list"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It uses square brackets: [1, 2, 3].",
                    "You can append, remove, and sort items.",
                ],
                "lesson": (
                    "list — ordered, mutable sequence. Items can be of any type.\n\n"
                    "Creation:\n"
                    "  suspects = ['Chen', 'Varela', 'Unknown']\n"
                    "  empty = []\n\n"
                    "Key operations:\n"
                    "  suspects.append('Reyes')    # add to end\n"
                    "  suspects[0]                 # access by index\n"
                    "  len(suspects)               # count items"
                ),
            },
            {
                "id": "ds_2",
                "type": "quiz",
                "title": "Key-Value Store",
                "question": "What Python data structure maps keys to values using curly braces and colons?",
                "answers": ["dict"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's like a lookup table or hash map.",
                    "Short for 'dictionary'. Uses {key: value} syntax.",
                ],
                "lesson": (
                    "dict — maps unique keys to values. Mutable. Ordered (Python 3.7+).\n\n"
                    "Creation:\n"
                    "  record = {'name': 'NEXUS', 'amount': 4_000_000, 'flagged': True}\n\n"
                    "Key operations:\n"
                    "  record['name']            → 'NEXUS'\n"
                    "  record.get('missing', 0)  → 0  (safe access with default)\n"
                    "  record.keys()             → dict_keys(['name', 'amount', 'flagged'])"
                ),
            },
            {
                "id": "ds_3",
                "type": "quiz",
                "title": "Immutable Record",
                "question": "What Python data structure is an ordered, immutable sequence stored in parentheses?",
                "answers": ["tuple"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Like a list, but it cannot be changed after creation.",
                    "Uses parentheses: (1, 2, 3).",
                ],
                "lesson": (
                    "tuple — ordered, immutable sequence. Cannot be modified after creation.\n\n"
                    "Creation:\n"
                    "  coords = (40.7128, -74.0060)\n"
                    "  single = (42,)    # trailing comma required for 1-item tuple\n\n"
                    "Key uses:\n"
                    "  - Return multiple values from a function: return x, y\n"
                    "  - Immutable keys in dictionaries\n"
                    "  - Packing/unpacking: x, y = coords"
                ),
            },
            {
                "id": "ds_4",
                "type": "quiz",
                "title": "Unique Collection",
                "question": "What Python data structure stores unordered, unique items with no duplicates?",
                "answers": ["set"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It automatically removes duplicate values.",
                    "Uses curly braces like a dict, but without key-value pairs.",
                ],
                "lesson": (
                    "set — unordered collection of unique items. No duplicates allowed.\n\n"
                    "Creation:\n"
                    "  seen_ips = {'10.0.0.1', '10.0.0.2', '10.0.0.1'}    # duplicates removed\n"
                    "  seen_ips    → {'10.0.0.1', '10.0.0.2'}\n\n"
                    "Key operations:\n"
                    "  seen_ips.add('192.168.1.1')     # add item\n"
                    "  set_a & set_b                   # intersection\n"
                    "  set_a | set_b                   # union"
                ),
            },
            {
                "id": "ds_5",
                "type": "quiz",
                "title": "Safe Lookup",
                "question": "What dict method retrieves a value by key but returns a default instead of raising an error if the key is missing?",
                "answers": [".get()", "get()", ".get"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "It takes two arguments: the key and a default value.",
                    "d.get('key', default) — never raises a KeyError.",
                ],
                "lesson": (
                    "dict.get(key, default) — safely retrieves a value, returning default if key is absent.\n\n"
                    "Examples:\n"
                    "  record = {'status': 'flagged'}\n"
                    "  record.get('status', 'unknown')    → 'flagged'\n"
                    "  record.get('amount', 0)            → 0  (key missing, returns default)\n\n"
                    "Without .get(), accessing a missing key raises KeyError."
                ),
            },
            {
                "id": "ds_boss",
                "type": "quiz",
                "title": "BOSS: List Comprehension",
                "question": "What Python one-liner syntax builds a new list by applying an expression to each item in an iterable?",
                "answers": ["list comprehension"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It fits in a single line inside square brackets: [expr for item in iterable].",
                    "It replaces a for loop that builds a list with append().",
                ],
                "lesson": (
                    "List comprehension — concise syntax for building lists from iterables.\n\n"
                    "Syntax: [expression for item in iterable if condition]\n\n"
                    "Examples:\n"
                    "  squares = [x**2 for x in range(10)]\n"
                    "  flagged = [r for r in records if r['amount'] > 1_000_000]\n\n"
                    "Equivalent to a for loop with append(), but more readable and often faster."
                ),
            },
        ],
    },

    "file_operations": {
        "id": "file_operations",
        "name": "The File Forge",
        "subtitle": "open(), read, write, pathlib",
        "color": "green",
        "icon": "📂",
        "commands": ["open()", "read()", "write()", "with", "pathlib", "Path"],
        "challenges": [
            {
                "id": "fo_1",
                "type": "quiz",
                "title": "Open Channel",
                "question": "What built-in Python function opens a file and returns a file object?",
                "url": "https://docs.python.org/3/tutorial/inputoutput.html",
                "answers": ["open()", "open"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It takes a filename and an optional mode argument.",
                    "The simplest call: open('filename.txt')",
                ],
                "lesson": (
                    "open() — opens a file and returns a file handle.\n\n"
                    "Syntax: open(filename, mode='r')\n\n"
                    "Common modes:\n"
                    "  'r'   read (default)\n"
                    "  'w'   write (overwrites)\n"
                    "  'a'   append\n"
                    "  'rb'  read binary\n\n"
                    "Always close the file when done, or use 'with' statement."
                ),
            },
            {
                "id": "fo_2",
                "type": "quiz",
                "title": "Context Guardian",
                "question": "What Python keyword opens a file in a context manager that automatically closes it when done?",
                "answers": ["with"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It creates a block that handles setup and teardown automatically.",
                    "Syntax: with open(...) as f:",
                ],
                "lesson": (
                    "with — context manager keyword. Ensures proper resource cleanup.\n\n"
                    "Example:\n"
                    "  with open('evidence.txt', 'r') as f:\n"
                    "      data = f.read()\n"
                    "  # file is automatically closed here\n\n"
                    "Using 'with' is best practice — it closes the file even if an exception occurs."
                ),
            },
            {
                "id": "fo_3",
                "type": "quiz",
                "title": "Full Read",
                "question": "What file object method reads the entire contents of a file as a single string?",
                "answers": [".read()", "read()", ".read"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It reads everything in one go.",
                    "Call it on the file object: f.read()",
                ],
                "lesson": (
                    "file.read() — reads the entire file contents as a string.\n\n"
                    "Example:\n"
                    "  with open('log.txt') as f:\n"
                    "      contents = f.read()\n\n"
                    "Related methods:\n"
                    "  f.readline()    → reads one line\n"
                    "  f.readlines()   → returns list of all lines\n\n"
                    "For large files, iterate line by line: for line in f:"
                ),
            },
            {
                "id": "fo_4",
                "type": "quiz",
                "title": "Write Operation",
                "question": "What mode string do you pass to open() to open a file for writing, creating it if it doesn't exist?",
                "answers": ["'w'", "w"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's a single character.",
                    "Warning: this mode overwrites existing file contents.",
                ],
                "lesson": (
                    "open(filename, 'w') — opens file for writing. Creates file if not present.\n\n"
                    "Warning: 'w' mode truncates existing content.\n\n"
                    "Example:\n"
                    "  with open('report.txt', 'w') as f:\n"
                    "      f.write('Evidence package ready.\\n')\n\n"
                    "Use 'a' mode to append without overwriting:\n"
                    "  open('log.txt', 'a')    → appends to existing content"
                ),
            },
            {
                "id": "fo_5",
                "type": "quiz",
                "title": "Path Navigator",
                "question": "What Python standard library class from the pathlib module represents filesystem paths as objects?",
                "answers": ["Path"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "It's from the pathlib module: from pathlib import ___",
                    "Allows path manipulation with / operator: Path('/etc') / 'config'",
                ],
                "lesson": (
                    "pathlib.Path — object-oriented filesystem path manipulation.\n\n"
                    "Import: from pathlib import Path\n\n"
                    "Examples:\n"
                    "  p = Path('/var/log/nexus')\n"
                    "  p.exists()          → True/False\n"
                    "  p / 'audit.log'     → Path('/var/log/nexus/audit.log')\n"
                    "  p.stem              → 'nexus'\n"
                    "  list(p.glob('*.log'))    → all .log files"
                ),
            },
            {
                "id": "fo_boss",
                "type": "quiz",
                "title": "BOSS: Line Iterator",
                "question": "What is the most memory-efficient way to iterate over every line in a large file in Python?",
                "answers": ["for line in f:", "iterate directly over the file object", "for line in file"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "You don't need readlines() — the file object itself is iterable.",
                    "Syntax: for line in f: — reads one line at a time without loading all into memory.",
                ],
                "lesson": (
                    "File objects are iterators — loop directly over them for memory-efficient line reading.\n\n"
                    "Example:\n"
                    "  with open('massive_log.txt') as f:\n"
                    "      for line in f:\n"
                    "          if 'PHANTOM_VENDOR' in line:\n"
                    "              print(line.strip())\n\n"
                    "This processes gigabyte-scale files without loading them into memory.\n"
                    "readlines() loads everything — avoid it for large files."
                ),
            },
        ],
    },

    "string_ops": {
        "id": "string_ops",
        "name": "String Manipulation Suite",
        "subtitle": "split, join, format, f-strings, strip",
        "color": "cyan",
        "icon": "✂",
        "commands": [".split()", ".join()", ".format()", "f-strings", ".strip()"],
        "challenges": [
            {
                "id": "str_1",
                "type": "quiz",
                "title": "Slice the Line",
                "question": "What string method splits a string into a list, dividing at a specified delimiter?",
                "url": "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str",
                "answers": [".split()", "split()", ".split"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It returns a list of substrings.",
                    "line.split(',') splits on commas.",
                ],
                "lesson": (
                    "str.split(sep) — splits a string at each occurrence of sep, returns a list.\n\n"
                    "Examples:\n"
                    "  'a,b,c'.split(',')       → ['a', 'b', 'c']\n"
                    "  'hello world'.split()    → ['hello', 'world']  (whitespace default)\n\n"
                    "For CSV-style log lines:\n"
                    "  fields = line.split(':')    # split on colon delimiter"
                ),
            },
            {
                "id": "str_2",
                "type": "quiz",
                "title": "Reassemble",
                "question": "What string method joins a list of strings into one, inserting a separator between each?",
                "answers": [".join()", "join()", ".join"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the inverse of split().",
                    "Syntax: separator.join(list)",
                ],
                "lesson": (
                    "str.join(iterable) — concatenates items with the string as separator.\n\n"
                    "Examples:\n"
                    "  ', '.join(['Ghost', 'Cipher', 'Reyes'])    → 'Ghost, Cipher, Reyes'\n"
                    "  '/'.join(['var', 'log', 'nexus'])           → 'var/log/nexus'\n\n"
                    "Note: the separator is called on, not passed to: sep.join(items)."
                ),
            },
            {
                "id": "str_3",
                "type": "quiz",
                "title": "Strip the Noise",
                "question": "What string method removes leading and trailing whitespace (including newlines) from a string?",
                "answers": [".strip()", "strip()", ".strip"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It cleans both ends of a string.",
                    "Useful after reading lines from a file that end with \\n.",
                ],
                "lesson": (
                    "str.strip() — removes leading and trailing whitespace.\n\n"
                    "Examples:\n"
                    "  '  data  '.strip()     → 'data'\n"
                    "  'line\\n'.strip()       → 'line'\n\n"
                    "Variants:\n"
                    "  .lstrip()    remove only left whitespace\n"
                    "  .rstrip()    remove only right whitespace\n\n"
                    "Accepts an argument: '***ghost***'.strip('*') → 'ghost'"
                ),
            },
            {
                "id": "str_4",
                "type": "quiz",
                "title": "Inject Values",
                "question": "What string prefix character creates an f-string that embeds expressions directly in a string literal?",
                "answers": ["f", "f\"\"", "f''"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's a single letter placed before the opening quote.",
                    "f'Value is {variable}' — curly braces embed expressions.",
                ],
                "lesson": (
                    "f-strings (formatted string literals) — embed expressions using {expr} syntax.\n\n"
                    "Syntax: f'text {expression} text'\n\n"
                    "Examples:\n"
                    "  host = 'nexus-db'\n"
                    "  port = 5432\n"
                    "  print(f'Connecting to {host}:{port}')    → Connecting to nexus-db:5432\n\n"
                    "Supports full Python expressions inside braces: f'{amount * 1.1:.2f}'"
                ),
            },
            {
                "id": "str_5",
                "type": "quiz",
                "title": "Case Fold",
                "question": "What string method returns a lowercase copy of a string?",
                "answers": [".lower()", "lower()", ".lower"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It makes all characters lowercase.",
                    "Useful for case-insensitive comparisons.",
                ],
                "lesson": (
                    "str.lower() — returns a new string with all characters converted to lowercase.\n\n"
                    "Examples:\n"
                    "  'NEXUS'.lower()           → 'nexus'\n"
                    "  'Ghost Operative'.lower() → 'ghost operative'\n\n"
                    "Related:\n"
                    "  .upper()         → ALL CAPS\n"
                    "  .title()         → Title Case\n"
                    "  .casefold()      → aggressive lowercase (handles unicode edge cases)"
                ),
            },
            {
                "id": "str_boss",
                "type": "quiz",
                "title": "BOSS: Replace in Place",
                "question": "What string method returns a new string with all occurrences of a substring replaced by another?",
                "answers": [".replace()", "replace()", ".replace"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It takes two arguments: the old substring and the new one.",
                    "'nexus-server'.replace('nexus', 'ghost') → 'ghost-server'",
                ],
                "lesson": (
                    "str.replace(old, new, count=-1) — replaces occurrences of old with new.\n\n"
                    "Examples:\n"
                    "  'phantom_vendor_001'.replace('_', '-')    → 'phantom-vendor-001'\n"
                    "  log.replace('ERROR', '[FLAGGED]')          → replaces all ERRORs\n\n"
                    "Optional third argument limits how many replacements to perform:\n"
                    "  'aaa'.replace('a', 'b', 2)    → 'bba'"
                ),
            },
        ],
    },

    "modules_arsenal": {
        "id": "modules_arsenal",
        "name": "The Modules Arsenal",
        "subtitle": "import, os, sys, json, datetime",
        "color": "yellow",
        "icon": "🔧",
        "commands": ["import", "from", "os", "sys", "json", "datetime"],
        "challenges": [
            {
                "id": "mod_1",
                "type": "quiz",
                "title": "Load the Module",
                "question": "What keyword loads an entire Python module into the current namespace?",
                "url": "https://docs.python.org/3/tutorial/modules.html",
                "answers": ["import"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It brings an entire module into scope.",
                    "Syntax: import module_name",
                ],
                "lesson": (
                    "import — loads a module, making its contents accessible via dot notation.\n\n"
                    "Examples:\n"
                    "  import os\n"
                    "  os.getcwd()    → current working directory\n\n"
                    "  import json\n"
                    "  json.loads('{\"key\": \"value\"}')    → {'key': 'value'}"
                ),
            },
            {
                "id": "mod_2",
                "type": "quiz",
                "title": "Selective Import",
                "question": "What syntax imports only a specific function or class from a module?",
                "answers": ["from x import y", "from ... import ..."],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It avoids loading the entire module into the namespace.",
                    "Syntax: from module import name",
                ],
                "lesson": (
                    "from module import name — imports a specific name from a module.\n\n"
                    "Examples:\n"
                    "  from pathlib import Path\n"
                    "  from datetime import datetime, timedelta\n"
                    "  from os.path import join, exists\n\n"
                    "Advantage: cleaner code — write Path() instead of pathlib.Path()."
                ),
            },
            {
                "id": "mod_3",
                "type": "quiz",
                "title": "OS Interface",
                "question": "What standard library module provides functions for interacting with the operating system, such as listing directories?",
                "answers": ["os"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Two letters. Short for 'operating system'.",
                    "os.listdir(), os.getcwd(), os.environ — all from this module.",
                ],
                "lesson": (
                    "os — operating system interface module.\n\n"
                    "Key functions:\n"
                    "  os.getcwd()           → current directory\n"
                    "  os.listdir(path)      → list directory contents\n"
                    "  os.environ            → dict of environment variables\n"
                    "  os.path.join(a, b)    → platform-safe path joining\n"
                    "  os.makedirs(path)     → create directory tree"
                ),
            },
            {
                "id": "mod_4",
                "type": "quiz",
                "title": "JSON Decoder",
                "question": "What standard library module parses JSON strings into Python dicts and serializes Python objects to JSON?",
                "answers": ["json"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It has the same name as the data format.",
                    "json.loads() and json.dumps() are its two most-used functions.",
                ],
                "lesson": (
                    "json — JSON encoding and decoding module.\n\n"
                    "Key functions:\n"
                    "  json.loads(string)     → parse JSON string → Python dict/list\n"
                    "  json.dumps(obj)        → serialize Python object → JSON string\n"
                    "  json.load(file)        → parse JSON from file object\n"
                    "  json.dump(obj, file)   → write JSON to file object\n\n"
                    "Essential for API responses, config files, and log parsing."
                ),
            },
            {
                "id": "mod_5",
                "type": "quiz",
                "title": "Time Stamp",
                "question": "What class from the datetime module represents a specific point in time (date + time)?",
                "answers": ["datetime", "datetime.datetime"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "The module and its main class share the same name.",
                    "from datetime import datetime — then datetime.now() gives current time.",
                ],
                "lesson": (
                    "datetime.datetime — represents a specific date and time.\n\n"
                    "Import: from datetime import datetime\n\n"
                    "Key usage:\n"
                    "  now = datetime.now()               → current local time\n"
                    "  ts = datetime(2024, 3, 15, 9, 0)   → specific datetime\n"
                    "  ts.strftime('%Y-%m-%d')            → '2024-03-15'\n"
                    "  datetime.fromisoformat('2024-03-15T09:00:00')    → parse ISO format"
                ),
            },
            {
                "id": "mod_boss",
                "type": "quiz",
                "title": "BOSS: Sys Exit",
                "question": "What standard library module provides access to Python interpreter internals, including command-line arguments via sys.argv?",
                "answers": ["sys"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Three letters. It interfaces with the Python runtime itself.",
                    "sys.argv, sys.exit(), sys.path, sys.stdin — all from this module.",
                ],
                "lesson": (
                    "sys — Python interpreter and runtime interface.\n\n"
                    "Key attributes and functions:\n"
                    "  sys.argv          → list of command-line arguments\n"
                    "  sys.exit(code)    → terminate the script with exit code\n"
                    "  sys.path          → module search path\n"
                    "  sys.stdin/stdout/stderr    → standard I/O streams\n\n"
                    "Example: if len(sys.argv) < 2: sys.exit('Usage: script.py <target>')"
                ),
            },
        ],
    },

    "error_handling": {
        "id": "error_handling",
        "name": "The Exception Vault",
        "subtitle": "try/except/finally, raise, specific exceptions",
        "color": "red",
        "icon": "🛡",
        "commands": ["try", "except", "finally", "raise", "Exception"],
        "challenges": [
            {
                "id": "eh_1",
                "type": "quiz",
                "title": "Try the Operation",
                "question": "What keyword begins a block of code that Python will attempt to execute and catch errors from?",
                "url": "https://docs.python.org/3/tutorial/errors.html",
                "answers": ["try"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's paired with 'except' to catch errors.",
                    "Three letters: t-r-y.",
                ],
                "lesson": (
                    "try — begins an exception-handling block.\n\n"
                    "Basic structure:\n"
                    "  try:\n"
                    "      risky_operation()\n"
                    "  except SomeError:\n"
                    "      handle_error()\n\n"
                    "Code inside the try block is monitored for exceptions.\n"
                    "If an exception occurs, execution jumps to the matching except block."
                ),
            },
            {
                "id": "eh_2",
                "type": "quiz",
                "title": "Catch the Signal",
                "question": "What keyword catches and handles an exception raised in the preceding try block?",
                "answers": ["except"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It follows the try block.",
                    "except ExceptionType: — catches a specific error.",
                ],
                "lesson": (
                    "except — catches exceptions raised in the try block.\n\n"
                    "Examples:\n"
                    "  try:\n"
                    "      data = int(user_input)\n"
                    "  except ValueError:\n"
                    "      print('Invalid number')\n"
                    "  except (KeyError, IndexError) as e:\n"
                    "      print(f'Data error: {e}')\n\n"
                    "Always catch specific exceptions — bare except: catches everything including SystemExit."
                ),
            },
            {
                "id": "eh_3",
                "type": "quiz",
                "title": "Always Execute",
                "question": "What keyword introduces a block that always runs after a try/except, whether or not an exception occurred?",
                "answers": ["finally"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It runs no matter what — even if an exception was raised.",
                    "Commonly used for cleanup: closing files, releasing locks.",
                ],
                "lesson": (
                    "finally — runs regardless of whether an exception occurred.\n\n"
                    "Example:\n"
                    "  conn = None\n"
                    "  try:\n"
                    "      conn = connect(host)\n"
                    "      extract_data(conn)\n"
                    "  except ConnectionError as e:\n"
                    "      log(f'Failed: {e}')\n"
                    "  finally:\n"
                    "      if conn:\n"
                    "          conn.close()    # always cleanup"
                ),
            },
            {
                "id": "eh_4",
                "type": "quiz",
                "title": "Trigger Exception",
                "question": "What keyword explicitly raises an exception in Python?",
                "answers": ["raise"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's the opposite of catching — it throws an error.",
                    "raise ValueError('message') — creates and throws an exception.",
                ],
                "lesson": (
                    "raise — triggers an exception explicitly.\n\n"
                    "Examples:\n"
                    "  raise ValueError('Invalid access level')\n"
                    "  raise RuntimeError(f'Connection to {host} failed')\n\n"
                    "Re-raise the current exception in an except block:\n"
                    "  except Exception:\n"
                    "      log('error')\n"
                    "      raise    # re-raises the same exception"
                ),
            },
            {
                "id": "eh_5",
                "type": "quiz",
                "title": "File Not Found",
                "question": "What built-in exception is raised when Python cannot find a file you tried to open?",
                "answers": ["FileNotFoundError"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "It's a subclass of OSError.",
                    "Raised when open('nonexistent.txt') fails.",
                ],
                "lesson": (
                    "FileNotFoundError — raised when a requested file or directory does not exist.\n\n"
                    "Example:\n"
                    "  try:\n"
                    "      with open('evidence.txt') as f:\n"
                    "          data = f.read()\n"
                    "  except FileNotFoundError:\n"
                    "      print('File not found — check the path')\n\n"
                    "Other common file exceptions:\n"
                    "  PermissionError    — no read/write access\n"
                    "  IsADirectoryError  — tried to open a dir as a file"
                ),
            },
            {
                "id": "eh_boss",
                "type": "quiz",
                "title": "BOSS: Custom Exception",
                "question": "What built-in class do you subclass to define a custom exception in Python?",
                "answers": ["Exception"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Most user-defined exceptions should inherit from this base class.",
                    "class MyError(___): pass",
                ],
                "lesson": (
                    "Exception — the base class for all non-system-exiting exceptions.\n\n"
                    "Define custom exceptions by subclassing it:\n"
                    "  class AuthFailure(Exception):\n"
                    "      pass\n\n"
                    "  class DataCorruption(Exception):\n"
                    "      def __init__(self, record_id, msg):\n"
                    "          self.record_id = record_id\n"
                    "          super().__init__(msg)\n\n"
                    "Custom exceptions make error handling precise and self-documenting."
                ),
            },
        ],
    },

    "file_io_deep": {
        "id": "file_io_deep",
        "name": "File I/O Operations",
        "subtitle": "open(), read, write, with statement",
        "color": "green",
        "icon": "📁",
        "commands": ["open()", "read()", "write()", "with", "readlines()", "writelines()"],
        "challenges": [
            {
                "id": "fio_1",
                "type": "quiz",
                "title": "Open the Gate",
                "question": "What built-in Python function opens a file and returns a file object?",
                "url": "https://docs.python.org/3/library/functions.html#open",
                "answers": ["open()", "open"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's a built-in — no import required.",
                    "Takes a filename and an optional mode: open('file.txt', 'r')",
                ],
                "lesson": (
                    "open(filename, mode) — opens a file and returns a file object.\n\n"
                    "Common modes:\n"
                    "  'r'   — read (default)\n"
                    "  'w'   — write (creates or truncates)\n"
                    "  'a'   — append (adds to end)\n"
                    "  'rb'  — read binary\n"
                    "  'wb'  — write binary\n\n"
                    "Example:\n"
                    "  f = open('evidence.txt', 'r')\n"
                    "  data = f.read()\n"
                    "  f.close()"
                ),
            },
            {
                "id": "fio_2",
                "type": "quiz",
                "title": "The Context Manager",
                "question": "What Python keyword creates a context manager block that automatically closes a file when the block exits?",
                "answers": ["with"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It ensures cleanup happens even if an exception is raised.",
                    "Syntax: ___ open('file.txt') as f:",
                ],
                "lesson": (
                    "with — creates a context manager. Used with open() to guarantee the file is closed.\n\n"
                    "Syntax:\n"
                    "  with open('evidence.txt', 'r') as f:\n"
                    "      data = f.read()\n"
                    "  # file is automatically closed here\n\n"
                    "Benefits:\n"
                    "  - No need to call f.close() manually\n"
                    "  - File closes even if an exception is raised inside the block\n\n"
                    "Best practice: always use 'with' when working with files."
                ),
            },
            {
                "id": "fio_3",
                "type": "quiz",
                "title": "Read All",
                "question": "What file object method reads the entire file contents as a single string?",
                "answers": [".read()", "read()", ".read"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It returns the entire file as one string.",
                    "For large files, consider reading line by line instead.",
                ],
                "lesson": (
                    "f.read() — reads the entire file and returns it as a string.\n\n"
                    "Example:\n"
                    "  with open('audit_log.txt') as f:\n"
                    "      contents = f.read()\n"
                    "  print(contents[:100])    # first 100 chars\n\n"
                    "Variants:\n"
                    "  f.read(n)      — read exactly n bytes\n"
                    "  f.readline()   — read one line\n"
                    "  f.readlines()  — read all lines into a list\n\n"
                    "Warning: f.read() on a gigabyte file loads it all into memory."
                ),
            },
            {
                "id": "fio_4",
                "type": "quiz",
                "title": "Write Mode",
                "question": "Which open() mode overwrites an existing file with new content (or creates it if it doesn't exist)?",
                "answers": ["'w'", "w"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It stands for 'write'.",
                    "Warning: this mode destroys existing file contents.",
                ],
                "lesson": (
                    "'w' mode — opens a file for writing. Truncates the file if it exists.\n\n"
                    "Example:\n"
                    "  with open('report.txt', 'w') as f:\n"
                    "      f.write('NEXUS Fraud Analysis\\n')\n"
                    "      f.write('Transactions: 417\\n')\n\n"
                    "Mode comparison:\n"
                    "  'w'  — write, truncates existing content\n"
                    "  'a'  — append, preserves existing content\n"
                    "  'x'  — exclusive create, fails if file exists\n\n"
                    "f.write() returns the number of characters written."
                ),
            },
            {
                "id": "fio_5",
                "type": "quiz",
                "title": "Append Mode",
                "question": "Which open() mode adds content to the END of an existing file without erasing it?",
                "answers": ["'a'", "a"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It stands for 'append'.",
                    "Unlike 'w', it won't destroy existing data.",
                ],
                "lesson": (
                    "'a' mode — opens for appending. Writes go to the end; existing content is preserved.\n\n"
                    "Example:\n"
                    "  with open('audit_trail.log', 'a') as f:\n"
                    "      f.write(f'[{timestamp}] Transaction flagged: {txn_id}\\n')\n\n"
                    "The fraud automation used append mode to grow its log files silently\n"
                    "over eleven years — each run adding one more line of evidence."
                ),
            },
            {
                "id": "fio_boss",
                "type": "quiz",
                "title": "BOSS: Read Lines",
                "question": "What file method reads all lines of a file into a Python list, one line per element?",
                "answers": [".readlines()", "readlines()", ".readlines"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's similar to .read() but returns a list instead of a string.",
                    "Each element in the list includes the trailing newline character.",
                ],
                "lesson": (
                    "f.readlines() — reads all lines and returns them as a list of strings.\n\n"
                    "Example:\n"
                    "  with open('transactions.txt') as f:\n"
                    "      lines = f.readlines()\n"
                    "  print(lines[0])    # first line, includes '\\n'\n\n"
                    "Strip newlines with a list comprehension:\n"
                    "  lines = [line.strip() for line in f.readlines()]\n\n"
                    "For large files, iterate directly: for line in f: — more memory efficient."
                ),
            },
        ],
    },

    "list_comprehensions": {
        "id": "list_comprehensions",
        "name": "Comprehension Engine",
        "subtitle": "List, Dict & Generator Comprehensions",
        "color": "magenta",
        "icon": "⚙",
        "commands": ["[x for x in]", "[x for x if]", "{k: v for}", "(x for x in)"],
        "challenges": [
            {
                "id": "lc_1",
                "type": "quiz",
                "title": "The One-Liner",
                "question": "What Python construct builds a new list by applying an expression to each item in an iterable, all in a single line?",
                "url": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
                "answers": ["list comprehension"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It uses square brackets with a for loop inside.",
                    "[expression for item in iterable]",
                ],
                "lesson": (
                    "List comprehension — builds a list in a single concise expression.\n\n"
                    "Syntax: [expression for item in iterable]\n\n"
                    "Examples:\n"
                    "  squares = [x**2 for x in range(10)]\n"
                    "  → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n\n"
                    "  names = [v['name'] for v in vendors]\n"
                    "  → extracts 'name' from every dict in vendors list\n\n"
                    "Equivalent to:\n"
                    "  result = []\n"
                    "  for item in iterable:\n"
                    "      result.append(expression)"
                ),
            },
            {
                "id": "lc_2",
                "type": "quiz",
                "title": "The Filter Pass",
                "question": "In a list comprehension, what keyword adds a condition to include only items that satisfy a test?",
                "answers": ["if"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the same keyword as in a regular conditional.",
                    "[x for x in items ___ condition]",
                ],
                "lesson": (
                    "List comprehension with filter: [expr for item in iterable if condition]\n\n"
                    "The if clause filters out items that don't match.\n\n"
                    "Examples:\n"
                    "  evens = [x for x in range(20) if x % 2 == 0]\n"
                    "  → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n\n"
                    "  flagged = [t for t in transactions if t['amount'] > THRESHOLD]\n"
                    "  → all transactions above the audit threshold\n\n"
                    "The fraud script used exactly this pattern to select phantom vendors."
                ),
            },
            {
                "id": "lc_3",
                "type": "quiz",
                "title": "Dict Comprehension",
                "question": "What syntax creates a dictionary using a comprehension — mapping keys to values in one expression?",
                "answers": ["{k: v for k, v in items}", "dict comprehension", "{key: value for ...}"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "Like a list comprehension, but with curly braces and a key: value format.",
                    "{k: v for k, v in iterable}",
                ],
                "lesson": (
                    "Dict comprehension — builds a dictionary in a single expression.\n\n"
                    "Syntax: {key_expr: value_expr for item in iterable}\n\n"
                    "Examples:\n"
                    "  squares = {x: x**2 for x in range(5)}\n"
                    "  → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n\n"
                    "  vendor_map = {v['id']: v['name'] for v in vendor_list}\n"
                    "  → maps IDs to names for fast lookup\n\n"
                    "The fraud automation built its phantom vendor dict this way."
                ),
            },
            {
                "id": "lc_4",
                "type": "quiz",
                "title": "Generator Expression",
                "question": "What type of comprehension uses parentheses instead of brackets and produces values lazily, one at a time?",
                "answers": ["generator expression", "generator"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It looks like a list comprehension but uses () instead of [].",
                    "It doesn't build the full list in memory — it yields one item at a time.",
                ],
                "lesson": (
                    "Generator expression — like a list comprehension, but lazy (memory-efficient).\n\n"
                    "Syntax: (expression for item in iterable)\n\n"
                    "Examples:\n"
                    "  total = sum(t['amount'] for t in transactions)    # no list built\n"
                    "  gen = (x**2 for x in range(1_000_000))            # no memory spike\n\n"
                    "Key difference:\n"
                    "  [x**2 for x in range(10)]    → builds full list in memory\n"
                    "  (x**2 for x in range(10))    → yields one value at a time\n\n"
                    "Use generators when processing large datasets."
                ),
            },
            {
                "id": "lc_5",
                "type": "quiz",
                "title": "Nested Comprehension",
                "question": "In a list comprehension, how do you iterate over a nested structure — e.g., items within each sublist of a 2D list?",
                "answers": ["use two for clauses", "nested for loops in the comprehension", "[x for sublist in matrix for x in sublist]"],
                "xp": 100,
                "difficulty": "hard",
                "hints": [
                    "You can chain multiple 'for' clauses in a single comprehension.",
                    "[item for group in groups for item in group]",
                ],
                "lesson": (
                    "Nested comprehension — chain multiple for clauses to flatten or cross-join.\n\n"
                    "Syntax: [expr for outer in iterable for inner in outer]\n\n"
                    "Examples:\n"
                    "  # Flatten a 2D list:\n"
                    "  flat = [x for row in matrix for x in row]\n\n"
                    "  # All combinations:\n"
                    "  pairs = [(a, b) for a in [1,2] for b in ['x','y']]\n"
                    "  → [(1,'x'), (1,'y'), (2,'x'), (2,'y')]\n\n"
                    "Read left to right: outer loop first, inner loop second."
                ),
            },
            {
                "id": "lc_boss",
                "type": "quiz",
                "title": "BOSS: Comprehension vs Loop",
                "question": "What is the primary advantage of a list comprehension over an equivalent for-loop with append()?",
                "answers": [
                    "more concise and typically faster",
                    "faster and more readable",
                    "concise syntax and better performance",
                ],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Think about both readability and execution speed.",
                    "CPython optimizes list comprehensions internally.",
                ],
                "lesson": (
                    "List comprehensions are both more concise AND faster than equivalent for-loops.\n\n"
                    "CPython optimizes comprehensions internally — the append() call overhead\n"
                    "is avoided because the interpreter can pre-allocate the list.\n\n"
                    "Benchmark comparison:\n"
                    "  # Comprehension — faster:\n"
                    "  result = [x*2 for x in data]\n\n"
                    "  # Loop — slower due to repeated append:\n"
                    "  result = []\n"
                    "  for x in data:\n"
                    "      result.append(x*2)\n\n"
                    "Rule of thumb: if a loop builds a list, a comprehension is likely better."
                ),
            },
        ],
    },

    "requests_http": {
        "id": "requests_http",
        "name": "HTTP Recon Module",
        "subtitle": "requests library & urllib basics",
        "color": "yellow",
        "icon": "🌐",
        "commands": ["requests.get()", "requests.post()", ".json()", ".status_code", "urllib.request"],
        "challenges": [
            {
                "id": "req_1",
                "type": "quiz",
                "title": "GET the Data",
                "question": "What requests function sends an HTTP GET request to a URL and returns a Response object?",
                "url": "https://requests.readthedocs.io/en/latest/user/quickstart/",
                "answers": ["requests.get()", "requests.get"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's the most common HTTP method for fetching data.",
                    "import requests; requests.___(url)",
                ],
                "lesson": (
                    "requests.get(url) — sends an HTTP GET request. Returns a Response object.\n\n"
                    "Setup:\n"
                    "  pip install requests\n"
                    "  import requests\n\n"
                    "Example:\n"
                    "  response = requests.get('https://nexus-api.internal/vendors')\n"
                    "  print(response.status_code)    → 200\n"
                    "  print(response.text)           → raw response body\n\n"
                    "The fraud scraper used GET requests to pull vendor data from internal APIs."
                ),
            },
            {
                "id": "req_2",
                "type": "quiz",
                "title": "Status Check",
                "question": "What attribute of a requests Response object contains the HTTP status code (e.g., 200, 404)?",
                "answers": [".status_code", "status_code"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It's an integer attribute on the Response object.",
                    "200 = OK, 404 = Not Found, 500 = Server Error",
                ],
                "lesson": (
                    "response.status_code — the integer HTTP status code of the response.\n\n"
                    "Common codes:\n"
                    "  200   OK — request succeeded\n"
                    "  201   Created — resource was created\n"
                    "  401   Unauthorized — authentication required\n"
                    "  403   Forbidden — access denied\n"
                    "  404   Not Found — resource doesn't exist\n"
                    "  500   Server Error — something broke server-side\n\n"
                    "Example:\n"
                    "  if response.status_code == 200:\n"
                    "      process(response.json())"
                ),
            },
            {
                "id": "req_3",
                "type": "quiz",
                "title": "Parse the JSON",
                "question": "What Response method parses the JSON response body and returns it as a Python dict or list?",
                "answers": [".json()", "json()", ".json"],
                "xp": 50,
                "difficulty": "easy",
                "hints": [
                    "It converts the JSON text body into a Python data structure.",
                    "response.___()",
                ],
                "lesson": (
                    "response.json() — decodes the JSON response body into a Python object.\n\n"
                    "Example:\n"
                    "  response = requests.get('https://nexus-api.internal/vendors')\n"
                    "  data = response.json()\n"
                    "  # data is now a dict or list\n"
                    "  for vendor in data['results']:\n"
                    "      print(vendor['name'])\n\n"
                    "Raises: requests.exceptions.JSONDecodeError if the response isn't valid JSON.\n\n"
                    "Alternative: import json; json.loads(response.text)"
                ),
            },
            {
                "id": "req_4",
                "type": "quiz",
                "title": "POST the Payload",
                "question": "What requests function sends an HTTP POST request, used to submit data to a server?",
                "answers": ["requests.post()", "requests.post"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "POST is the HTTP method for sending data — forms, JSON payloads, etc.",
                    "requests.___(url, json=payload)",
                ],
                "lesson": (
                    "requests.post(url, data=None, json=None) — sends an HTTP POST request.\n\n"
                    "Examples:\n"
                    "  # Send JSON payload:\n"
                    "  response = requests.post(\n"
                    "      'https://nexus-api.internal/submit',\n"
                    "      json={'vendor_id': 'PV-042', 'amount': 49999.97}\n"
                    "  )\n\n"
                    "  # Send form data:\n"
                    "  response = requests.post(url, data={'key': 'value'})\n\n"
                    "The fraud script used POST to inject phantom vendor records into the API."
                ),
            },
            {
                "id": "req_5",
                "type": "quiz",
                "title": "urllib Fallback",
                "question": "What Python standard library module provides HTTP request functionality without installing any third-party packages?",
                "answers": ["urllib", "urllib.request"],
                "xp": 75,
                "difficulty": "medium",
                "hints": [
                    "It's part of the standard library — no pip install needed.",
                    "urllib.request.urlopen(url) is the basic entry point.",
                ],
                "lesson": (
                    "urllib — Python's built-in HTTP library. No installation required.\n\n"
                    "Basic usage:\n"
                    "  import urllib.request\n"
                    "  import json\n\n"
                    "  with urllib.request.urlopen(url) as response:\n"
                    "      body = response.read().decode('utf-8')\n"
                    "      data = json.loads(body)\n\n"
                    "urllib vs requests:\n"
                    "  urllib    — built-in, verbose, no dependencies\n"
                    "  requests  — third-party, cleaner API, industry standard\n\n"
                    "The fraud scripts used urllib to avoid flagging a requests dependency."
                ),
            },
            {
                "id": "req_boss",
                "type": "quiz",
                "title": "BOSS: Session Persistence",
                "question": "What requests object persists cookies, headers, and authentication across multiple HTTP requests?",
                "answers": ["requests.Session()", "Session", "requests.Session"],
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "It's useful when you need to stay logged in across multiple API calls.",
                    "s = requests.___()",
                ],
                "lesson": (
                    "requests.Session() — maintains state (cookies, headers, auth) across requests.\n\n"
                    "Example:\n"
                    "  with requests.Session() as s:\n"
                    "      s.headers.update({'Authorization': 'Bearer ' + token})\n"
                    "      s.post(login_url, data=creds)\n"
                    "      data = s.get(protected_api).json()\n\n"
                    "Benefits:\n"
                    "  - Cookies are automatically persisted between requests\n"
                    "  - Default headers set once, applied to all requests\n"
                    "  - Connection pooling for better performance\n\n"
                    "The fraud scraper used a Session to maintain API authentication across\n"
                    "hundreds of requests per run without re-authenticating each time."
                ),
            },
        ],
    },
    "classes_and_oop": {
        "id": "classes_and_oop",
        "name": "Classes and OOP",
        "description": "Object-oriented Python: classes, inheritance, dunder methods, and design patterns.",
        "challenges": [
            {
                "id": "py_class_def",
                "type": "flag_quiz",
                "url": "https://docs.python.org/3/tutorial/classes.html",
                "title": "Class Definition",
                "question": "Define a class called `Agent` with an `__init__` that takes `name` and sets `self.name`:",
                "lesson": "Classes are blueprints for objects. `__init__` is the constructor — called when you create an instance. `self` refers to the instance being created. Example:\n\n  class Agent:\n      def __init__(self, name):\n          self.name = name\n\n  a = Agent('Ghost')\n  print(a.name)  # Ghost",
                "answers": [
                    "class Agent:\n    def __init__(self, name):\n        self.name = name",
                    "class Agent:",
                ],
                "xp": 50,
                "hints": [
                    "class ClassName: then indent __init__(self, param):",
                    "__init__ sets instance variables with self.var = value",
                ],
            },
            {
                "id": "py_inheritance",
                "type": "quiz",
                "title": "Inheritance",
                "question": "A `SpecialAgent` class needs all `Agent` methods PLUS a `decrypt()` method. The cleanest approach is:",
                "lesson": "Inheritance lets a child class inherit all methods and attributes from a parent. `super().__init__()` calls the parent constructor. This avoids duplicating code.\n\n  class SpecialAgent(Agent):\n      def __init__(self, name, clearance):\n          super().__init__(name)\n          self.clearance = clearance\n      def decrypt(self, msg):\n          ...",
                "options": [
                    "Copy all Agent code into SpecialAgent",
                    "class SpecialAgent(Agent): — inherit from Agent and add decrypt()",
                    "Use a global function instead of a class",
                    "Modify the Agent class directly to add decrypt()",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "Put the parent class name in parentheses: class Child(Parent):",
                    "Inheritance means 'everything the parent has, the child also has'",
                ],
            },
            {
                "id": "py_dunder_str",
                "type": "fill_blank",
                "title": "__str__ Method",
                "question": "To make `print(agent)` show `Agent: Ghost` instead of `<Agent object at 0x...>`, define the `___str___` dunder method.",
                "lesson": "Dunder methods (double underscore = 'dunder') customize how objects behave with Python built-ins. `__str__` controls what `print()` and `str()` return. `__repr__` is for developer representation. `__len__` makes `len()` work. `__eq__` enables `==` comparison.\n\n  def __str__(self):\n      return f'Agent: {self.name}'",
                "answer": "__str__",
                "xp": 50,
                "hints": [
                    "Double underscore before AND after: __name__",
                    "str = string representation",
                ],
            },
            {
                "id": "py_classmethod",
                "type": "quiz",
                "title": "@classmethod and @staticmethod",
                "question": "A factory method that creates an Agent from a JSON dict — `Agent.from_dict({'name': 'Ghost'})` — should be decorated with:",
                "lesson": "@classmethod receives the class (cls) as first argument, not an instance. Used for factory/alternative constructors. @staticmethod receives neither self nor cls — just a utility function inside the class namespace.\n\n  @classmethod\n  def from_dict(cls, data):\n      return cls(data['name'])\n\n  # called as:\n  a = Agent.from_dict({'name': 'Ghost'})",
                "options": [
                    "@staticmethod — no self or cls needed",
                    "@classmethod — receives cls, can call cls() to create instances",
                    "@property — makes it a computed attribute",
                    "No decorator — instance methods can also create instances",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "You need access to the class itself to create a new instance",
                    "@classmethod takes cls as first arg instead of self",
                ],
            },
            {
                "id": "py_dataclass",
                "type": "quiz",
                "title": "@dataclass",
                "question": "Which Python decorator automatically generates `__init__`, `__repr__`, and `__eq__` for a class based on its field annotations?",
                "lesson": "`@dataclass` (from `dataclasses` module) eliminates boilerplate. Just annotate fields and everything is generated automatically.\n\n  from dataclasses import dataclass\n\n  @dataclass\n  class Evidence:\n      filename: str\n      size_bytes: int\n      sha256: str = ''\n\nAutomatic __init__, __repr__, __eq__ — and with `frozen=True`, also __hash__.",
                "options": [
                    "@property",
                    "@dataclass",
                    "@abstractmethod",
                    "@functools.total_ordering",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "It's in the `dataclasses` module",
                    "Data + class = ___class",
                ],
            },
            {
                "id": "py_oop_boss",
                "type": "quiz",
                "title": "BOSS: Design the Evidence System",
                "question": "NEXUS mission: build an `Evidence` base class and a `DatabaseRecord` subclass. `Evidence` needs `__init__(filename, timestamp)` and `__str__`. `DatabaseRecord` adds `table` and `row_count`. Which Python approach gives the cleanest design?",
                "lesson": "Good OOP design: base class holds common attributes and methods, subclasses extend. `@dataclass` reduces boilerplate. `__str__` provides readable output.\n\n  @dataclass\n  class Evidence:\n      filename: str\n      timestamp: str\n      def __str__(self):\n          return f'[{self.timestamp}] {self.filename}'\n\n  @dataclass\n  class DatabaseRecord(Evidence):\n      table: str = ''\n      row_count: int = 0",
                "options": [
                    "Two completely separate classes with no inheritance",
                    "@dataclass for Evidence with DatabaseRecord(Evidence) as a subclass",
                    "One giant class with all possible fields",
                    "Use a dict instead of classes",
                ],
                "answer": "b",
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Inheritance removes duplication — common fields go in the base class",
                    "@dataclass + inheritance: the cleanest combination for data-holding classes",
                ],
            },
        ],
    },
    "subprocess_and_os": {
        "id": "subprocess_and_os",
        "name": "subprocess and os",
        "description": "Run shell commands, manipulate paths, and interact with the operating system from Python.",
        "challenges": [
            {
                "id": "py_subprocess_run",
                "type": "flag_quiz",
                "url": "https://docs.python.org/3/library/subprocess.html",
                "title": "subprocess.run()",
                "question": "Run `ls -la` as a shell command from Python and capture the output:",
                "lesson": "`subprocess.run()` is the modern way to run shell commands. `capture_output=True` captures stdout and stderr. `text=True` decodes bytes to str. `check=True` raises CalledProcessError on non-zero exit.\n\n  import subprocess\n  result = subprocess.run(['ls', '-la'], capture_output=True, text=True)\n  print(result.stdout)\n\nAvoid `shell=True` — it passes the command through a shell and can be a security risk (shell injection).",
                "answers": [
                    "subprocess.run(['ls', '-la'], capture_output=True, text=True)",
                    "subprocess.run('ls -la', shell=True, capture_output=True, text=True)",
                ],
                "xp": 50,
                "hints": [
                    "subprocess.run() takes a list of command + args",
                    "capture_output=True, text=True — both needed for usable output",
                ],
            },
            {
                "id": "py_subprocess_pipe",
                "type": "quiz",
                "title": "Check Return Code",
                "question": "After `result = subprocess.run([...])`, how do you check if the command succeeded?",
                "lesson": "`result.returncode` is 0 for success, non-zero for failure. `result.stdout` contains captured output (if capture_output=True). `result.stderr` contains error output. Alternatively, pass `check=True` to raise `subprocess.CalledProcessError` automatically on failure.",
                "options": [
                    "if result.success:",
                    "if result.returncode == 0:",
                    "if result.ok:",
                    "if result.status == 'success':",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "Unix convention: 0 = success, non-zero = error",
                    "result.___code",
                ],
            },
            {
                "id": "py_os_path",
                "type": "fill_blank",
                "title": "pathlib.Path",
                "question": "The modern Python way to join paths safely (instead of os.path.join) is using `pathlib._____`.",
                "lesson": "`pathlib.Path` is the modern path handling API. Path operations use `/` operator for joining.\n\n  from pathlib import Path\n\n  base = Path('/home/ghost')\n  evidence = base / 'nexus' / 'evidence.zip'\n  print(evidence)  # /home/ghost/nexus/evidence.zip\n\n  # Check existence, create dirs, read/write files:\n  if evidence.exists():\n      data = evidence.read_text()\n\nMuch cleaner than os.path.join and os.getcwd().",
                "answer": "Path",
                "xp": 50,
                "hints": [
                    "It's a class in the pathlib module",
                    "from pathlib import ___",
                ],
            },
            {
                "id": "py_os_environ",
                "type": "quiz",
                "title": "Environment Variables",
                "question": "To read the `NEXUS_API_KEY` environment variable in Python, with a fallback if it's not set:",
                "lesson": "`os.environ` is a dict-like object mapping env var names to values. `os.environ.get('KEY', default)` returns the default if the key isn't set — safer than `os.environ['KEY']` which raises KeyError.\n\n  import os\n  key = os.environ.get('NEXUS_API_KEY', 'not-set')\n\nNever hardcode secrets in code — always read from environment variables.",
                "options": [
                    "import os; key = os.environ['NEXUS_API_KEY']",
                    "import os; key = os.environ.get('NEXUS_API_KEY', 'not-set')",
                    "import os; key = os.getenv.NEXUS_API_KEY",
                    "import sys; key = sys.environ.get('NEXUS_API_KEY')",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "Use .get() not [] — it lets you provide a fallback",
                    "os.environ.get('NAME', 'default_value')",
                ],
            },
            {
                "id": "py_glob_walk",
                "type": "quiz",
                "title": "Finding Files",
                "question": "To find all `.log` files recursively under `/var/log` using pathlib:",
                "lesson": "`Path.glob()` finds files matching a pattern. `**/*.log` means: any directory depth, files ending in .log. Returns a generator.\n\n  from pathlib import Path\n\n  for logfile in Path('/var/log').glob('**/*.log'):\n      print(logfile)\n\n`rglob('*.log')` is equivalent shorthand. Much cleaner than os.walk() + string matching.",
                "options": [
                    "os.listdir('/var/log')",
                    "Path('/var/log').glob('**/*.log')",
                    "subprocess.run(['find', '/var/log', '-name', '*.log'])",
                    "glob.glob('/var/log/*.log')",
                ],
                "answer": "b",
                "xp": 50,
                "hints": [
                    "pathlib has a glob() method",
                    "** means 'recurse into all subdirectories'",
                ],
            },
            {
                "id": "py_subprocess_boss",
                "type": "quiz",
                "title": "BOSS: The Evidence Packager",
                "question": "The Python evidence packager must: (1) read NEXUS_KEY from environment, (2) find all .sql files in /tmp/evidence/, (3) run `tar czf evidence.tar.gz <files>` as a subprocess, (4) verify tar exited 0. Which combination is correct?",
                "lesson": "Putting it all together:\n\n  import os, subprocess\n  from pathlib import Path\n\n  key = os.environ.get('NEXUS_KEY')\n  files = list(Path('/tmp/evidence').glob('*.sql'))\n  result = subprocess.run(\n      ['tar', 'czf', 'evidence.tar.gz'] + [str(f) for f in files],\n      capture_output=True, text=True\n  )\n  if result.returncode != 0:\n      raise RuntimeError(result.stderr)",
                "options": [
                    "os.system() for all commands — simpler API",
                    "os.environ.get() + Path.glob() + subprocess.run() + returncode check",
                    "subprocess.Popen() with shell=True for all operations",
                    "Import os and call os.popen() with a shell pipeline",
                ],
                "answer": "b",
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Four operations: env var + path glob + subprocess + return code check",
                    "Each part has a best-practice tool: os.environ.get, Path.glob, subprocess.run, .returncode",
                ],
            },
        ],
    },
}

ZONE_ORDER = [
    "python_basics",
    "control_flow",
    "functions_lab",
    "data_structures",
    "file_operations",
    "string_ops",
    "modules_arsenal",
    "error_handling",
    "file_io_deep",
    "list_comprehensions",
    "requests_http",
    "classes_and_oop",
    "subprocess_and_os",
]


def get_zone(zone_id: str) -> dict:
    return ZONES.get(zone_id, {})


def get_all_zones() -> list:
    return [ZONES[z] for z in ZONE_ORDER if z in ZONES]


def get_zone_challenges(zone_id: str) -> list:
    zone = get_zone(zone_id)
    return zone.get("challenges", [])


def get_challenge(zone_id: str, challenge_id: str) -> dict:
    for ch in get_zone_challenges(zone_id):
        if ch["id"] == challenge_id:
            return ch
    return {}
