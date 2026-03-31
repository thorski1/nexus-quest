"""
zones.py — Python Advanced zones and challenges for Python Dark Arts.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "decorators",
    "generators_iterators",
    "context_managers",
    "metaclasses_descriptors",
    "async_python",
    "type_hints",
    "testing_advanced",
    "packaging",
]

ZONES = {
    # ── ZONE 1: DECORATORS ──────────────────────────────────────────────
    "decorators": {
        "id": "decorators",
        "name": "The Wrapper Protocol",
        "subtitle": "Function Decorators, @property, @staticmethod, Factories",
        "color": "magenta",
        "icon": "🎭",
        "commands": ["@decorator", "@property", "@staticmethod", "@classmethod"],
        "challenges": [
            {
                "id": "dec_1",
                "type": "quiz",
                "title": "Decorator Fundamentals",
                "question": (
                    "What does a decorator do in Python?\n\n"
                    "  @my_decorator\n"
                    "  def greet():\n"
                    "      return 'hello'"
                ),
                "lesson": (
                    "A decorator is a function that takes another function as input\n"
                    "and returns a modified version of it. The @syntax is sugar for:\n\n"
                    "  greet = my_decorator(greet)\n\n"
                    "Decorators wrap behavior around the original function without\n"
                    "modifying its source code."
                ),
                "options": [
                    "Deletes the function and replaces it with a new one",
                    "Wraps the function, adding behavior before/after it runs",
                    "Converts the function to a class method",
                    "Compiles the function to bytecode ahead of time",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Think of a decorator as a wrapper — it goes around the original function.",
                    "@my_decorator is syntactic sugar for greet = my_decorator(greet).",
                ],
            },
            {
                "id": "dec_2",
                "type": "quiz",
                "title": "functools.wraps",
                "question": (
                    "Why should you use @functools.wraps(func) inside a decorator?\n\n"
                    "  def my_dec(func):\n"
                    "      @functools.wraps(func)\n"
                    "      def wrapper(*args, **kwargs):\n"
                    "          return func(*args, **kwargs)\n"
                    "      return wrapper"
                ),
                "lesson": (
                    "@functools.wraps copies the original function's __name__, __doc__,\n"
                    "and __module__ to the wrapper. Without it:\n\n"
                    "  greet.__name__  # 'wrapper'  — loses original identity\n\n"
                    "With @wraps:\n"
                    "  greet.__name__  # 'greet'  — preserved\n\n"
                    "Essential for debugging, introspection, and documentation."
                ),
                "options": [
                    "It makes the decorator run faster",
                    "It preserves the original function's __name__, __doc__, and metadata",
                    "It prevents the decorator from being called twice",
                    "It enables the decorator to accept arguments",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Without it, the wrapped function loses its identity (__name__ becomes 'wrapper').",
                    "functools.wraps copies metadata from the original to the wrapper.",
                ],
            },
            {
                "id": "dec_3",
                "type": "quiz",
                "title": "@property Power",
                "question": (
                    "What does @property allow you to do?\n\n"
                    "  class Circle:\n"
                    "      def __init__(self, radius):\n"
                    "          self._radius = radius\n\n"
                    "      @property\n"
                    "      def area(self):\n"
                    "          return 3.14159 * self._radius ** 2\n\n"
                    "  c = Circle(5)\n"
                    "  print(c.area)  # How is area accessed?"
                ),
                "lesson": (
                    "@property turns a method into a read-only attribute. You access\n"
                    "it without parentheses:\n\n"
                    "  c.area    # 78.5  — no () needed\n\n"
                    "You can add @area.setter to allow assignment:\n"
                    "  @area.setter\n"
                    "  def area(self, value): ...\n\n"
                    "Properties give you the interface of an attribute with the\n"
                    "control of a method."
                ),
                "options": [
                    "Define a class constant that cannot be changed",
                    "Access a method as an attribute without parentheses",
                    "Mark a method as private to the class",
                    "Automatically cache the return value of the method",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Notice c.area has no parentheses — it looks like an attribute access.",
                    "@property bridges methods and attributes — method logic, attribute syntax.",
                ],
            },
            {
                "id": "dec_4",
                "type": "quiz",
                "title": "@staticmethod vs @classmethod",
                "question": (
                    "What is the key difference between @staticmethod and @classmethod?\n\n"
                    "  class Parser:\n"
                    "      format = 'json'\n\n"
                    "      @staticmethod\n"
                    "      def validate(data):\n"
                    "          return len(data) > 0\n\n"
                    "      @classmethod\n"
                    "      def from_file(cls, path):\n"
                    "          return cls(open(path).read())"
                ),
                "lesson": (
                    "@staticmethod: no access to the class or instance.\n"
                    "  Parser.validate(data)  # just a namespaced function\n\n"
                    "@classmethod: receives the class (cls) as first argument.\n"
                    "  Parser.from_file('x.json')  # cls is Parser\n\n"
                    "@classmethod is essential for alternative constructors and\n"
                    "methods that need to know which class they were called on\n"
                    "(important with inheritance)."
                ),
                "options": [
                    "@staticmethod receives self, @classmethod receives cls",
                    "@staticmethod receives cls, @classmethod receives self",
                    "@classmethod receives the class as first arg; @staticmethod receives neither self nor cls",
                    "There is no difference — they are aliases",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Look at the parameters: validate(data) vs from_file(cls, path).",
                    "@classmethod always gets cls — the class itself — as its first argument.",
                ],
            },
            {
                "id": "dec_5",
                "type": "quiz",
                "title": "Decorator Factory",
                "question": (
                    "What is a decorator factory?\n\n"
                    "  def repeat(n):\n"
                    "      def decorator(func):\n"
                    "          @functools.wraps(func)\n"
                    "          def wrapper(*args, **kwargs):\n"
                    "              for _ in range(n):\n"
                    "                  func(*args, **kwargs)\n"
                    "          return wrapper\n"
                    "      return decorator\n\n"
                    "  @repeat(3)\n"
                    "  def say_hello():\n"
                    "      print('hello')"
                ),
                "lesson": (
                    "A decorator factory is a function that returns a decorator.\n"
                    "It adds a layer of nesting to accept arguments:\n\n"
                    "  @repeat(3)  →  repeat(3) returns decorator\n"
                    "              →  decorator(say_hello) returns wrapper\n\n"
                    "Three levels:\n"
                    "  1. repeat(n) — factory, captures n\n"
                    "  2. decorator(func) — the actual decorator\n"
                    "  3. wrapper(*args) — the replacement function"
                ),
                "options": [
                    "A decorator that only works on class methods",
                    "A function that returns a decorator, allowing the decorator to accept arguments",
                    "A built-in Python pattern for creating abstract classes",
                    "A way to apply multiple decorators at once",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Notice @repeat(3) — repeat is called with an argument before decorating.",
                    "repeat(3) returns the actual decorator; it's a factory that produces decorators.",
                ],
            },
            {
                "id": "dec_6",
                "type": "quiz",
                "title": "Stacked Decorators",
                "question": (
                    "In what order are stacked decorators applied?\n\n"
                    "  @decorator_a\n"
                    "  @decorator_b\n"
                    "  def func():\n"
                    "      pass"
                ),
                "lesson": (
                    "Stacked decorators apply bottom-up:\n\n"
                    "  @decorator_a\n"
                    "  @decorator_b\n"
                    "  def func(): ...\n\n"
                    "Is equivalent to:\n"
                    "  func = decorator_a(decorator_b(func))\n\n"
                    "decorator_b wraps func first, then decorator_a wraps the result.\n"
                    "The closest decorator to the function runs first."
                ),
                "options": [
                    "Top to bottom: decorator_a first, then decorator_b",
                    "Bottom to top: decorator_b first, then decorator_a wraps the result",
                    "They run simultaneously in parallel",
                    "Order is random — Python does not guarantee decorator order",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Think of it as nested function calls: decorator_a(decorator_b(func)).",
                    "The decorator closest to the def keyword applies first.",
                ],
            },
        ],
    },

    # ── ZONE 2: GENERATORS & ITERATORS ──────────────────────────────────
    "generators_iterators": {
        "id": "generators_iterators",
        "name": "The Lazy Stream",
        "subtitle": "yield, Generator Expressions, itertools, Lazy Evaluation",
        "color": "green",
        "icon": "♾️",
        "commands": ["yield", "next()", "iter()", "itertools"],
        "challenges": [
            {
                "id": "gen_1",
                "type": "quiz",
                "title": "yield vs return",
                "question": (
                    "What does the yield keyword do that return does not?\n\n"
                    "  def counter():\n"
                    "      n = 0\n"
                    "      while True:\n"
                    "          yield n\n"
                    "          n += 1"
                ),
                "lesson": (
                    "yield pauses the function and saves its state. When next()\n"
                    "is called again, execution resumes from where it left off.\n\n"
                    "return terminates the function permanently.\n"
                    "yield suspends it — the local variables, the instruction pointer,\n"
                    "everything is preserved until the next iteration.\n\n"
                    "This enables infinite sequences and lazy evaluation."
                ),
                "options": [
                    "yield terminates the function and returns a value",
                    "yield pauses the function and preserves its state for resumption",
                    "yield converts the function into a class",
                    "yield is identical to return but faster",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Notice the while True — this function never terminates, it just pauses.",
                    "yield suspends execution; the function resumes on next().",
                ],
            },
            {
                "id": "gen_2",
                "type": "quiz",
                "title": "Generator Expression",
                "question": (
                    "What is the difference between these two expressions?\n\n"
                    "  squares_list = [x**2 for x in range(1000000)]\n"
                    "  squares_gen  = (x**2 for x in range(1000000))"
                ),
                "lesson": (
                    "List comprehension [] creates all values in memory immediately.\n"
                    "Generator expression () creates values lazily, one at a time.\n\n"
                    "  squares_list  # ~8 MB in memory\n"
                    "  squares_gen   # ~100 bytes — computes on demand\n\n"
                    "Use generators when you only need to iterate once and the\n"
                    "dataset is large or potentially infinite."
                ),
                "options": [
                    "No difference — parentheses and brackets are interchangeable",
                    "The list version is lazy; the generator version is eager",
                    "The generator creates values lazily on demand; the list creates all values in memory immediately",
                    "The generator version returns a tuple",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Brackets [] = list comprehension (eager). Parentheses () = generator expression (lazy).",
                    "The generator version uses almost no memory regardless of range size.",
                ],
            },
            {
                "id": "gen_3",
                "type": "quiz",
                "title": "itertools.chain",
                "question": (
                    "What does itertools.chain() do?\n\n"
                    "  import itertools\n"
                    "  a = [1, 2, 3]\n"
                    "  b = [4, 5, 6]\n"
                    "  result = list(itertools.chain(a, b))"
                ),
                "lesson": (
                    "itertools.chain() chains multiple iterables into a single\n"
                    "lazy iterator, yielding elements from each in order:\n\n"
                    "  chain([1,2], [3,4])  → 1, 2, 3, 4\n\n"
                    "Unlike concatenation (a + b), chain works with any iterable\n"
                    "and doesn't create intermediate lists. Useful for combining\n"
                    "generators and large datasets."
                ),
                "options": [
                    "Zips two iterables element by element into tuples",
                    "Concatenates iterables into a single sequential iterator",
                    "Applies a function to every element in both iterables",
                    "Repeats the first iterable for the length of the second",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "chain = connect end to end. The result is [1, 2, 3, 4, 5, 6].",
                    "It yields all items from the first iterable, then the second, etc.",
                ],
            },
            {
                "id": "gen_4",
                "type": "quiz",
                "title": "send() to a Generator",
                "question": (
                    "What does .send() do on a generator?\n\n"
                    "  def accumulator():\n"
                    "      total = 0\n"
                    "      while True:\n"
                    "          value = yield total\n"
                    "          total += value\n\n"
                    "  acc = accumulator()\n"
                    "  next(acc)       # prime the generator\n"
                    "  acc.send(10)    # returns 10\n"
                    "  acc.send(20)    # returns 30"
                ),
                "lesson": (
                    ".send(value) resumes the generator AND sends a value into it.\n"
                    "The sent value becomes the result of the yield expression:\n\n"
                    "  value = yield total  ← send(10) makes value = 10\n\n"
                    "This creates a two-way channel: the generator yields data out,\n"
                    "and .send() pushes data in. This is the basis for coroutines.\n\n"
                    "Note: you must call next() first to advance to the first yield."
                ),
                "options": [
                    "Sends a value into the generator, which becomes the result of the yield expression",
                    "Sends the generator's output to another function",
                    "Terminates the generator with a return value",
                    "Sends an exception into the generator",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "value = yield total — send() provides the value that yield returns.",
                    ".send() both resumes the generator and injects a value.",
                ],
            },
            {
                "id": "gen_5",
                "type": "quiz",
                "title": "Lazy Evaluation",
                "question": (
                    "Why does this code run instantly, even though range is enormous?\n\n"
                    "  def big_filter(n):\n"
                    "      for i in range(n):\n"
                    "          if i % 7 == 0:\n"
                    "              yield i\n\n"
                    "  gen = big_filter(10**12)  # instant\n"
                    "  first = next(gen)         # 0"
                ),
                "lesson": (
                    "Generators are lazy — they compute nothing until you ask.\n\n"
                    "  gen = big_filter(10**12)  # no computation yet\n"
                    "  next(gen)                 # computes only until first yield\n\n"
                    "This is lazy evaluation: values are produced on demand.\n"
                    "The generator doesn't loop through 10^12 numbers;\n"
                    "it stops as soon as it finds the first qualifying value.\n"
                    "Memory usage stays constant regardless of input size."
                ),
                "options": [
                    "Python optimizes range() to skip to the answer",
                    "The generator doesn't execute any code until next() is called — lazy evaluation",
                    "big_filter is compiled to C code internally",
                    "range(10**12) allocates no memory because it's a generator itself",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Creating a generator object doesn't execute its body at all.",
                    "Lazy means 'compute only when asked' — no work until next() or iteration.",
                ],
            },
            {
                "id": "gen_6",
                "type": "quiz",
                "title": "throw() and close()",
                "question": (
                    "What does generator.throw(ExceptionType) do?\n\n"
                    "  def resilient():\n"
                    "      while True:\n"
                    "          try:\n"
                    "              value = yield\n"
                    "              print(f'Got {value}')\n"
                    "          except ValueError:\n"
                    "              print('Bad value, continuing')\n\n"
                    "  g = resilient()\n"
                    "  next(g)\n"
                    "  g.throw(ValueError)"
                ),
                "lesson": (
                    ".throw(exc) raises an exception inside the generator at the\n"
                    "point where it is currently paused (at the yield).\n\n"
                    "If the generator catches it, execution continues.\n"
                    "If not, the exception propagates to the caller.\n\n"
                    ".close() sends GeneratorExit, which tells the generator\n"
                    "to clean up and stop. If the generator doesn't catch it,\n"
                    "it terminates silently."
                ),
                "options": [
                    "Raises the exception at the caller's location",
                    "Throws the exception inside the generator at the current yield point",
                    "Converts the generator to raise exceptions instead of yielding values",
                    "Queues the exception for the next send() call",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The exception is injected at the yield where the generator is paused.",
                    "The generator can catch it with try/except and keep running.",
                ],
            },
        ],
    },

    # ── ZONE 3: CONTEXT MANAGERS ────────────────────────────────────────
    "context_managers": {
        "id": "context_managers",
        "name": "The Gatekeeper",
        "subtitle": "with Statement, __enter__/__exit__, contextlib",
        "color": "yellow",
        "icon": "🚪",
        "commands": ["with", "__enter__", "__exit__", "contextlib"],
        "challenges": [
            {
                "id": "ctx_1",
                "type": "quiz",
                "title": "The with Statement",
                "question": (
                    "What does the with statement guarantee?\n\n"
                    "  with open('data.txt') as f:\n"
                    "      content = f.read()\n"
                    "  # What's true about f here?"
                ),
                "lesson": (
                    "The with statement guarantees that cleanup code (__exit__)\n"
                    "runs even if an exception occurs inside the block:\n\n"
                    "  with open('file') as f:\n"
                    "      data = f.read()   # even if this raises\n"
                    "  # f is closed — guaranteed\n\n"
                    "This is the context manager protocol. It replaces try/finally\n"
                    "with a cleaner, less error-prone pattern."
                ),
                "options": [
                    "The file is deleted after the block finishes",
                    "The variable f is available after the block but in read-only mode",
                    "The __exit__ method runs when leaving the block, even if an exception occurs",
                    "The block runs in a separate thread for safety",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The key guarantee is cleanup — __exit__ always runs.",
                    "with is essentially a structured try/finally for resource management.",
                ],
            },
            {
                "id": "ctx_2",
                "type": "quiz",
                "title": "The Protocol",
                "question": (
                    "What two dunder methods must a class implement to work with 'with'?\n\n"
                    "  class DBConnection:\n"
                    "      def __???__(self):\n"
                    "          self.conn = connect()\n"
                    "          return self.conn\n\n"
                    "      def __???__(self, exc_type, exc_val, exc_tb):\n"
                    "          self.conn.close()"
                ),
                "lesson": (
                    "The context manager protocol requires two methods:\n\n"
                    "  __enter__(self) — called when entering the with block.\n"
                    "     Returns the value bound to 'as'.\n\n"
                    "  __exit__(self, exc_type, exc_val, exc_tb) — called on exit.\n"
                    "     Receives exception info (all None if no exception).\n"
                    "     Return True to suppress the exception, False to propagate.\n\n"
                    "Together they form the context manager protocol."
                ),
                "options": [
                    "__open__ and __close__",
                    "__enter__ and __exit__",
                    "__start__ and __stop__",
                    "__init__ and __del__",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "You enter the with block and exit it — the methods are named accordingly.",
                    "__enter__ returns the resource; __exit__ handles cleanup.",
                ],
            },
            {
                "id": "ctx_3",
                "type": "quiz",
                "title": "contextlib.contextmanager",
                "question": (
                    "How does @contextlib.contextmanager simplify context manager creation?\n\n"
                    "  from contextlib import contextmanager\n\n"
                    "  @contextmanager\n"
                    "  def temp_dir():\n"
                    "      d = create_temp()\n"
                    "      yield d\n"
                    "      cleanup(d)"
                ),
                "lesson": (
                    "@contextmanager lets you write a context manager as a generator\n"
                    "function instead of a class with __enter__/__exit__:\n\n"
                    "  @contextmanager\n"
                    "  def managed_resource():\n"
                    "      resource = acquire()   # __enter__\n"
                    "      yield resource          # value for 'as'\n"
                    "      release(resource)       # __exit__\n\n"
                    "Everything before yield is __enter__.\n"
                    "Everything after yield is __exit__.\n"
                    "The yielded value is bound to the 'as' variable."
                ),
                "options": [
                    "It converts any function into a context manager using a generator with yield",
                    "It automatically adds error handling to any function",
                    "It creates a class with __enter__/__exit__ from a regular function",
                    "It makes the function run asynchronously",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "Notice the yield — code before = setup, code after = teardown.",
                    "The decorator turns a single generator function into a full context manager.",
                ],
            },
            {
                "id": "ctx_4",
                "type": "quiz",
                "title": "Exception Suppression",
                "question": (
                    "How do you make a context manager suppress exceptions?\n\n"
                    "  class Suppressor:\n"
                    "      def __enter__(self):\n"
                    "          return self\n"
                    "      def __exit__(self, exc_type, exc_val, exc_tb):\n"
                    "          # What should this return to suppress exceptions?"
                ),
                "lesson": (
                    "If __exit__ returns True (or any truthy value), the exception\n"
                    "is suppressed — it does not propagate:\n\n"
                    "  def __exit__(self, exc_type, exc_val, exc_tb):\n"
                    "      return True  # swallow all exceptions\n\n"
                    "Return False (or None) to let exceptions propagate normally.\n\n"
                    "contextlib.suppress(ExceptionType) is a built-in shorthand:\n"
                    "  with suppress(FileNotFoundError):\n"
                    "      os.remove('missing.txt')  # no error"
                ),
                "options": [
                    "Raise a SuppressedException",
                    "Return True from __exit__",
                    "Return False from __exit__",
                    "Call self.suppress() inside __exit__",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "__exit__ returning True means 'I handled this, don't propagate.'",
                    "Returning False (or nothing) lets the exception bubble up normally.",
                ],
            },
            {
                "id": "ctx_5",
                "type": "quiz",
                "title": "Async Context Managers",
                "question": (
                    "What methods define an async context manager?\n\n"
                    "  class AsyncDB:\n"
                    "      async def __???__(self):\n"
                    "          self.conn = await connect()\n"
                    "          return self.conn\n\n"
                    "      async def __???__(self, *exc_info):\n"
                    "          await self.conn.close()"
                ),
                "lesson": (
                    "Async context managers use __aenter__ and __aexit__:\n\n"
                    "  async with AsyncDB() as conn:\n"
                    "      await conn.query(...)\n\n"
                    "Both methods are coroutines (async def). They allow awaiting\n"
                    "inside setup and teardown — essential for async I/O resources\n"
                    "like database connections and HTTP sessions.\n\n"
                    "contextlib.asynccontextmanager provides the generator shortcut."
                ),
                "options": [
                    "__enter__ and __exit__ with async wrappers",
                    "__aenter__ and __aexit__",
                    "__async_enter__ and __async_exit__",
                    "__await_enter__ and __await_exit__",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The async variants follow Python's 'a' prefix convention.",
                    "Used with 'async with' statements in async code.",
                ],
            },
            {
                "id": "ctx_6",
                "type": "quiz",
                "title": "ExitStack",
                "question": (
                    "What problem does contextlib.ExitStack solve?\n\n"
                    "  from contextlib import ExitStack\n\n"
                    "  with ExitStack() as stack:\n"
                    "      files = [stack.enter_context(open(f))\n"
                    "               for f in filenames]"
                ),
                "lesson": (
                    "ExitStack manages a dynamic number of context managers.\n"
                    "You can't write:\n"
                    "  with open(f) for f in files:  # not valid\n\n"
                    "ExitStack lets you push context managers onto a stack at\n"
                    "runtime. All are cleaned up in LIFO order when the block exits.\n\n"
                    "  stack.enter_context(cm)  — enters cm, registers its cleanup\n"
                    "  stack.callback(fn)       — registers a plain cleanup function"
                ),
                "options": [
                    "Limits the number of open context managers to prevent resource exhaustion",
                    "Manages a dynamic collection of context managers with proper cleanup",
                    "Converts synchronous context managers to async ones",
                    "Stacks exceptions from multiple context managers into one",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The number of files is unknown at code-write time — ExitStack handles runtime additions.",
                    "All registered context managers are cleaned up in reverse order on exit.",
                ],
            },
        ],
    },

    # ── ZONE 4: METACLASSES & DESCRIPTORS ───────────────────────────────
    "metaclasses_descriptors": {
        "id": "metaclasses_descriptors",
        "name": "The Class Forge",
        "subtitle": "type(), __new__, __init_subclass__, Descriptors",
        "color": "red",
        "icon": "🔨",
        "commands": ["type()", "__new__", "__init_subclass__", "__get__"],
        "challenges": [
            {
                "id": "meta_1",
                "type": "quiz",
                "title": "type() as Class Factory",
                "question": (
                    "What does this code produce?\n\n"
                    "  MyClass = type('MyClass', (object,), {'x': 10})\n"
                    "  obj = MyClass()\n"
                    "  print(obj.x)"
                ),
                "lesson": (
                    "type() with three arguments creates a new class dynamically:\n\n"
                    "  type(name, bases, dict)\n\n"
                    "  name  — class name (string)\n"
                    "  bases — tuple of base classes\n"
                    "  dict  — class namespace (attributes and methods)\n\n"
                    "This is exactly what Python does internally when you write\n"
                    "a class statement. The class keyword is syntactic sugar for\n"
                    "a type() call."
                ),
                "options": [
                    "TypeError — type() only accepts one argument",
                    "A new class is created dynamically; prints 10",
                    "A dictionary with key 'x' and value 10",
                    "None — type() with three args returns None",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "type() with 3 args is the class constructor — it builds new classes at runtime.",
                    "class MyClass: x = 10 is equivalent to type('MyClass', (), {'x': 10}).",
                ],
            },
            {
                "id": "meta_2",
                "type": "quiz",
                "title": "Metaclass __new__",
                "question": (
                    "When is a metaclass's __new__ called?\n\n"
                    "  class Meta(type):\n"
                    "      def __new__(mcs, name, bases, namespace):\n"
                    "          cls = super().__new__(mcs, name, bases, namespace)\n"
                    "          cls.registry = []\n"
                    "          return cls\n\n"
                    "  class Plugin(metaclass=Meta):\n"
                    "      pass"
                ),
                "lesson": (
                    "A metaclass's __new__ is called when the class is created\n"
                    "(at class definition time, not at instance creation).\n\n"
                    "  class Plugin(metaclass=Meta):  ← Meta.__new__ runs HERE\n"
                    "      pass\n\n"
                    "  p = Plugin()  ← this calls Plugin.__new__, not Meta.__new__\n\n"
                    "Metaclasses customize class creation. They're the class of a class.\n"
                    "type is the default metaclass for all classes."
                ),
                "options": [
                    "When an instance of Plugin is created with Plugin()",
                    "When the Plugin class itself is defined — at class creation time",
                    "When the module is imported by another module",
                    "When Plugin.__init__ is called",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Meta is the metaclass — it creates the class, not instances of the class.",
                    "The class body executes and then Meta.__new__ builds the class object.",
                ],
            },
            {
                "id": "meta_3",
                "type": "quiz",
                "title": "__init_subclass__",
                "question": (
                    "What is __init_subclass__ used for?\n\n"
                    "  class Base:\n"
                    "      _registry = []\n\n"
                    "      def __init_subclass__(cls, **kwargs):\n"
                    "          super().__init_subclass__(**kwargs)\n"
                    "          Base._registry.append(cls)\n\n"
                    "  class PluginA(Base): pass\n"
                    "  class PluginB(Base): pass\n"
                    "  # Base._registry == [PluginA, PluginB]"
                ),
                "lesson": (
                    "__init_subclass__ is called on the parent class whenever\n"
                    "a new subclass is defined. It's a simpler alternative to\n"
                    "metaclasses for many use cases:\n\n"
                    "  - Auto-registration of subclasses\n"
                    "  - Validation of subclass attributes\n"
                    "  - Injecting methods or properties\n\n"
                    "Added in Python 3.6. Use it instead of a metaclass when\n"
                    "you only need to hook into subclass creation."
                ),
                "options": [
                    "It initializes all instances of subclasses",
                    "It's called when a subclass is defined, allowing the parent to customize it",
                    "It replaces __init__ in all subclasses",
                    "It prevents subclassing of the parent class",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Each time a new subclass is defined, the parent's __init_subclass__ fires.",
                    "It's a hook for the parent class to react to being subclassed.",
                ],
            },
            {
                "id": "meta_4",
                "type": "quiz",
                "title": "Descriptor Protocol",
                "question": (
                    "What makes a class a descriptor?\n\n"
                    "  class Validated:\n"
                    "      def __get__(self, obj, objtype=None):\n"
                    "          return self.value\n\n"
                    "      def __set__(self, obj, value):\n"
                    "          if value < 0:\n"
                    "              raise ValueError('Must be >= 0')\n"
                    "          self.value = value"
                ),
                "lesson": (
                    "A descriptor is any object that defines __get__, __set__,\n"
                    "or __delete__. When placed as a class attribute, Python\n"
                    "invokes these methods on attribute access:\n\n"
                    "  obj.x          → Validated.__get__(desc, obj, type(obj))\n"
                    "  obj.x = 5      → Validated.__set__(desc, obj, 5)\n"
                    "  del obj.x      → Validated.__delete__(desc, obj)\n\n"
                    "Descriptors power @property, @classmethod, @staticmethod,\n"
                    "and __slots__. They're the mechanism behind Python's attribute\n"
                    "lookup chain."
                ),
                "options": [
                    "Any class with __init__ and __repr__",
                    "Any class that defines __get__, __set__, or __delete__",
                    "Any class that inherits from abc.ABC",
                    "Any class with a __descriptor__ attribute set to True",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The descriptor protocol is defined by specific dunder methods for attribute access.",
                    "__get__ for reading, __set__ for writing, __delete__ for deletion.",
                ],
            },
            {
                "id": "meta_5",
                "type": "quiz",
                "title": "Data vs Non-Data Descriptors",
                "question": (
                    "What is the difference between a data descriptor and a non-data descriptor?\n\n"
                    "  # Data descriptor\n"
                    "  class DataDesc:\n"
                    "      def __get__(self, obj, cls): return 42\n"
                    "      def __set__(self, obj, val): pass\n\n"
                    "  # Non-data descriptor\n"
                    "  class NonDataDesc:\n"
                    "      def __get__(self, obj, cls): return 42"
                ),
                "lesson": (
                    "Data descriptors define __set__ and/or __delete__.\n"
                    "Non-data descriptors only define __get__.\n\n"
                    "The distinction controls attribute lookup priority:\n"
                    "  1. Data descriptors  (highest priority)\n"
                    "  2. Instance __dict__\n"
                    "  3. Non-data descriptors\n\n"
                    "A data descriptor overrides instance attributes.\n"
                    "A non-data descriptor can be shadowed by instance attributes.\n"
                    "Functions are non-data descriptors (they only define __get__)."
                ),
                "options": [
                    "Data descriptors are faster; non-data descriptors are slower",
                    "Data descriptors define __set__/__delete__ and override instance __dict__; non-data only define __get__",
                    "Data descriptors store data; non-data descriptors compute it",
                    "There is no meaningful difference between them",
                ],
                "answer": "b",
                "xp": 40,
                "hints": [
                    "The presence of __set__ or __delete__ makes it a data descriptor.",
                    "Data descriptors have higher priority than instance __dict__ in attribute lookup.",
                ],
            },
            {
                "id": "meta_6",
                "type": "quiz",
                "title": "__set_name__",
                "question": (
                    "What does __set_name__ do?\n\n"
                    "  class Field:\n"
                    "      def __set_name__(self, owner, name):\n"
                    "          self.public_name = name\n"
                    "          self.private_name = f'_{name}'\n\n"
                    "  class Model:\n"
                    "      username = Field()  # __set_name__ called here"
                ),
                "lesson": (
                    "__set_name__ is called automatically when a descriptor is\n"
                    "assigned as a class attribute. It receives:\n\n"
                    "  owner — the class the descriptor is assigned to (Model)\n"
                    "  name  — the attribute name ('username')\n\n"
                    "This lets the descriptor know its own name without manual\n"
                    "configuration. Added in Python 3.6, it eliminates the need\n"
                    "for metaclasses in many descriptor patterns."
                ),
                "options": [
                    "Sets the name of the class at definition time",
                    "Automatically called when a descriptor is assigned to a class, telling it its attribute name",
                    "Renames an attribute at runtime",
                    "Validates that a class name follows naming conventions",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "When Model is created, Python calls Field().__set_name__(Model, 'username').",
                    "The descriptor learns that it's stored as 'username' on Model.",
                ],
            },
        ],
    },

    # ── ZONE 5: ASYNC PYTHON ────────────────────────────────────────────
    "async_python": {
        "id": "async_python",
        "name": "The Event Loop",
        "subtitle": "asyncio, async/await, Concurrency, aiohttp",
        "color": "blue",
        "icon": "⚡",
        "commands": ["async", "await", "asyncio.run()", "asyncio.gather()"],
        "challenges": [
            {
                "id": "async_1",
                "type": "quiz",
                "title": "async/await Basics",
                "question": (
                    "What does 'await' do in this code?\n\n"
                    "  async def fetch_data():\n"
                    "      response = await aiohttp.get('https://api.example.com')\n"
                    "      return await response.json()"
                ),
                "lesson": (
                    "await suspends the current coroutine, yielding control back\n"
                    "to the event loop until the awaited operation completes.\n\n"
                    "While this coroutine is waiting for the HTTP response,\n"
                    "the event loop can run other coroutines — that's concurrency.\n\n"
                    "await can only be used inside async def functions.\n"
                    "It only works with awaitable objects (coroutines, Futures, Tasks)."
                ),
                "options": [
                    "Runs the operation in a separate thread",
                    "Suspends the coroutine and yields control to the event loop until the operation completes",
                    "Blocks the entire program until the operation finishes",
                    "Converts the coroutine to a synchronous function",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "await is non-blocking — it lets other coroutines run while waiting.",
                    "The event loop manages which coroutine runs while others are suspended.",
                ],
            },
            {
                "id": "async_2",
                "type": "quiz",
                "title": "asyncio.gather()",
                "question": (
                    "What does asyncio.gather() do?\n\n"
                    "  async def main():\n"
                    "      results = await asyncio.gather(\n"
                    "          fetch_user(1),\n"
                    "          fetch_user(2),\n"
                    "          fetch_user(3),\n"
                    "      )\n"
                    "      # results = [user1, user2, user3]"
                ),
                "lesson": (
                    "asyncio.gather() runs multiple coroutines concurrently and\n"
                    "returns their results as a list (in the same order):\n\n"
                    "  await gather(a(), b(), c())\n"
                    "  # a, b, c run concurrently\n"
                    "  # returns [result_a, result_b, result_c]\n\n"
                    "All three fetch_user calls start at once and run concurrently\n"
                    "on the event loop. Total time ≈ slowest call, not sum of all."
                ),
                "options": [
                    "Runs coroutines sequentially and collects results",
                    "Runs coroutines concurrently and returns results in order as a list",
                    "Runs coroutines in parallel threads",
                    "Picks the fastest coroutine and discards the rest",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "gather = concurrent execution. Results preserve input order.",
                    "Three network calls at once instead of one after another.",
                ],
            },
            {
                "id": "async_3",
                "type": "quiz",
                "title": "Event Loop",
                "question": (
                    "What is the event loop in asyncio?\n\n"
                    "  asyncio.run(main())  # What does this start?"
                ),
                "lesson": (
                    "The event loop is the central scheduler of asyncio. It:\n\n"
                    "  1. Runs coroutines and switches between them at await points\n"
                    "  2. Handles I/O callbacks (sockets, files, timers)\n"
                    "  3. Manages Tasks and Futures\n\n"
                    "asyncio.run() creates a new event loop, runs the coroutine,\n"
                    "and closes the loop when done. There's one event loop per thread.\n\n"
                    "The loop is single-threaded — concurrency via cooperative\n"
                    "multitasking, not parallelism."
                ),
                "options": [
                    "A thread pool that distributes work across CPU cores",
                    "A single-threaded scheduler that multiplexes coroutines cooperatively at await points",
                    "A process manager that forks child processes",
                    "A callback queue identical to JavaScript's event loop with no differences",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Single-threaded. Cooperative multitasking. Switches at await points.",
                    "asyncio.run() creates the loop, runs your coroutine, and tears it down.",
                ],
            },
            {
                "id": "async_4",
                "type": "quiz",
                "title": "Semaphores",
                "question": (
                    "What does asyncio.Semaphore do?\n\n"
                    "  sem = asyncio.Semaphore(10)\n\n"
                    "  async def limited_fetch(url):\n"
                    "      async with sem:\n"
                    "          return await aiohttp.get(url)"
                ),
                "lesson": (
                    "A semaphore limits concurrent access to a resource.\n"
                    "Semaphore(10) allows at most 10 coroutines to hold it\n"
                    "simultaneously. Others wait until a slot opens.\n\n"
                    "Common uses:\n"
                    "  - Rate-limiting API calls\n"
                    "  - Limiting concurrent database connections\n"
                    "  - Controlling file descriptor usage\n\n"
                    "async with sem: — acquires on entry, releases on exit."
                ),
                "options": [
                    "Locks a resource so only one coroutine can use it at a time",
                    "Limits concurrent access to a resource to a maximum of N coroutines",
                    "Distributes work evenly across coroutines",
                    "Signals between two specific coroutines",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Semaphore(10) means at most 10 coroutines inside the block at once.",
                    "Think of it as a bouncer limiting how many people enter at a time.",
                ],
            },
            {
                "id": "async_5",
                "type": "quiz",
                "title": "asyncio.create_task()",
                "question": (
                    "What's the difference between these two approaches?\n\n"
                    "  # Approach A: sequential\n"
                    "  result1 = await fetch(url1)\n"
                    "  result2 = await fetch(url2)\n\n"
                    "  # Approach B: concurrent\n"
                    "  task1 = asyncio.create_task(fetch(url1))\n"
                    "  task2 = asyncio.create_task(fetch(url2))\n"
                    "  result1 = await task1\n"
                    "  result2 = await task2"
                ),
                "lesson": (
                    "Approach A: sequential. url2 fetch starts only after url1 completes.\n"
                    "Approach B: concurrent. Both fetches start immediately.\n\n"
                    "asyncio.create_task() schedules the coroutine to run on the\n"
                    "event loop immediately — it doesn't wait for you to await it.\n\n"
                    "  task = create_task(coro())  # starts running NOW\n"
                    "  ...                         # other code runs\n"
                    "  result = await task          # get result when needed"
                ),
                "options": [
                    "No difference — both are concurrent",
                    "A is concurrent; B is sequential",
                    "A is sequential (one after another); B is concurrent (both start immediately)",
                    "B is faster because create_task uses threads",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "await fetch(url1) blocks until complete before starting url2.",
                    "create_task() schedules the coroutine immediately — it starts before await.",
                ],
            },
            {
                "id": "async_6",
                "type": "quiz",
                "title": "Async Generators",
                "question": (
                    "What is an async generator?\n\n"
                    "  async def stream_events():\n"
                    "      async with aiohttp.ClientSession() as session:\n"
                    "          async for event in session.ws_connect(url):\n"
                    "              yield event.json()\n\n"
                    "  async for event in stream_events():\n"
                    "      process(event)"
                ),
                "lesson": (
                    "An async generator uses both async def and yield. It produces\n"
                    "values lazily over time, with await points between yields.\n\n"
                    "Consumed with 'async for':\n"
                    "  async for event in stream_events():\n"
                    "      ...\n\n"
                    "The async for loop awaits each value from the generator.\n"
                    "This is ideal for streaming data: WebSockets, SSE, paginated\n"
                    "APIs, or any source that produces data over time."
                ),
                "options": [
                    "A generator that runs in a separate process",
                    "A regular generator wrapped in asyncio.run()",
                    "An async function that uses yield to lazily produce values with await points between them",
                    "A synchronous generator that returns coroutines instead of values",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "async def + yield = async generator. Consumed with async for.",
                    "Each yield can have awaits in between — perfect for streaming data.",
                ],
            },
        ],
    },

    # ── ZONE 6: TYPE HINTS ──────────────────────────────────────────────
    "type_hints": {
        "id": "type_hints",
        "name": "The Type Layer",
        "subtitle": "typing Module, Protocol, TypeVar, Generic, Overload",
        "color": "cyan",
        "icon": "📐",
        "commands": ["typing", "Protocol", "TypeVar", "Generic"],
        "challenges": [
            {
                "id": "typ_1",
                "type": "quiz",
                "title": "Basic Type Annotations",
                "question": (
                    "What do type hints do at runtime in standard Python?\n\n"
                    "  def greet(name: str) -> str:\n"
                    "      return f'Hello, {name}'\n\n"
                    "  greet(42)  # What happens?"
                ),
                "lesson": (
                    "Type hints are NOT enforced at runtime by default. They are\n"
                    "metadata for tools (mypy, pyright, IDEs) to check statically.\n\n"
                    "  greet(42)  # runs fine — no TypeError from annotations\n\n"
                    "The annotations are stored in greet.__annotations__ but Python\n"
                    "does not check them during execution. You need a type checker\n"
                    "(mypy, pyright) or runtime library (pydantic, beartype) for\n"
                    "enforcement."
                ),
                "options": [
                    "TypeError — 42 is not a str",
                    "Returns 'Hello, 42' with no error — type hints are not enforced at runtime",
                    "SyntaxError — type hints require Python 3.12+",
                    "The function runs but logs a type warning",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Type hints are informational — they don't change runtime behavior.",
                    "Python stores them in __annotations__ but never checks them automatically.",
                ],
            },
            {
                "id": "typ_2",
                "type": "quiz",
                "title": "TypeVar and Generics",
                "question": (
                    "What does TypeVar enable?\n\n"
                    "  from typing import TypeVar\n\n"
                    "  T = TypeVar('T')\n\n"
                    "  def first(items: list[T]) -> T:\n"
                    "      return items[0]\n\n"
                    "  first([1, 2, 3])    # T = int\n"
                    "  first(['a', 'b'])   # T = str"
                ),
                "lesson": (
                    "TypeVar creates a generic type variable. It tells the type\n"
                    "checker that the return type is connected to the input type:\n\n"
                    "  first(list[int]) → int\n"
                    "  first(list[str]) → str\n\n"
                    "Without TypeVar, you'd have to annotate the return as 'Any'\n"
                    "and lose type safety. TypeVar preserves the relationship\n"
                    "between input and output types."
                ),
                "options": [
                    "Creates a new type at runtime",
                    "Defines a type variable for generic functions — linking input and output types",
                    "Converts a value's type dynamically",
                    "Restricts a function to accept only one specific type",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "T appears in both the parameter and return type — they're linked.",
                    "The type checker infers T from the actual argument type.",
                ],
            },
            {
                "id": "typ_3",
                "type": "quiz",
                "title": "Protocol (Structural Subtyping)",
                "question": (
                    "What does typing.Protocol enable?\n\n"
                    "  from typing import Protocol\n\n"
                    "  class Drawable(Protocol):\n"
                    "      def draw(self) -> None: ...\n\n"
                    "  class Circle:\n"
                    "      def draw(self) -> None:\n"
                    "          print('O')\n\n"
                    "  def render(shape: Drawable) -> None:\n"
                    "      shape.draw()\n\n"
                    "  render(Circle())  # Does Circle need to inherit Drawable?"
                ),
                "lesson": (
                    "Protocol enables structural subtyping (duck typing for type checkers).\n\n"
                    "Circle doesn't inherit from Drawable, but it satisfies the\n"
                    "protocol because it has a draw() method with the right signature.\n\n"
                    "  class Drawable(Protocol):\n"
                    "      def draw(self) -> None: ...\n\n"
                    "Any class with a matching draw() method is a Drawable —\n"
                    "no inheritance required. This is 'static duck typing.'"
                ),
                "options": [
                    "Forces classes to inherit from the Protocol explicitly",
                    "Enables structural subtyping — any class matching the interface is accepted, no inheritance needed",
                    "Creates abstract base classes that raise errors at runtime",
                    "Defines runtime type checking for function arguments",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Circle has draw() → it satisfies Drawable. No inheritance needed.",
                    "Protocol = static duck typing. 'If it has draw(), it's Drawable.'",
                ],
            },
            {
                "id": "typ_4",
                "type": "quiz",
                "title": "Generic Classes",
                "question": (
                    "How do you create a generic class?\n\n"
                    "  from typing import TypeVar, Generic\n\n"
                    "  T = TypeVar('T')\n\n"
                    "  class Stack(Generic[T]):\n"
                    "      def __init__(self) -> None:\n"
                    "          self._items: list[T] = []\n\n"
                    "      def push(self, item: T) -> None:\n"
                    "          self._items.append(item)\n\n"
                    "      def pop(self) -> T:\n"
                    "          return self._items.pop()\n\n"
                    "  s: Stack[int] = Stack()"
                ),
                "lesson": (
                    "Inherit from Generic[T] to create a generic class.\n"
                    "The type parameter T flows through all methods:\n\n"
                    "  s: Stack[int]\n"
                    "  s.push(42)      # OK: int matches T=int\n"
                    "  s.push('hi')    # type error: str != int\n"
                    "  x = s.pop()     # x is inferred as int\n\n"
                    "In Python 3.12+, you can use the new syntax:\n"
                    "  class Stack[T]: ..."
                ),
                "options": [
                    "Use type() to create a class with a variable type parameter",
                    "Inherit from Generic[T] where T is a TypeVar",
                    "Add a __type__ class attribute",
                    "Use @generic decorator from typing module",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Generic[T] is the base class that makes Stack parameterizable.",
                    "Stack[int] tells the type checker that T=int throughout.",
                ],
            },
            {
                "id": "typ_5",
                "type": "quiz",
                "title": "@overload",
                "question": (
                    "What does @overload do?\n\n"
                    "  from typing import overload\n\n"
                    "  @overload\n"
                    "  def parse(data: str) -> dict: ...\n"
                    "  @overload\n"
                    "  def parse(data: bytes) -> dict: ...\n\n"
                    "  def parse(data):\n"
                    "      if isinstance(data, str):\n"
                    "          return json.loads(data)\n"
                    "      return json.loads(data.decode())"
                ),
                "lesson": (
                    "@overload defines multiple type signatures for a single function.\n"
                    "The overloaded signatures are for the type checker only —\n"
                    "the actual implementation is the non-decorated version.\n\n"
                    "The type checker can now understand:\n"
                    "  parse('{}')   → dict  (str variant)\n"
                    "  parse(b'{}')  → dict  (bytes variant)\n\n"
                    "Without @overload, the type checker sees Union[str, bytes]\n"
                    "as input and can't narrow the return type."
                ),
                "options": [
                    "Creates multiple versions of the function that dispatch at runtime",
                    "Defines multiple type signatures for the type checker — no runtime effect",
                    "Enables function overloading like C++ with different argument counts",
                    "Automatically generates isinstance checks for each signature",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The @overload versions have ... bodies — they're purely for the type checker.",
                    "Only the non-decorated implementation runs at runtime.",
                ],
            },
            {
                "id": "typ_6",
                "type": "quiz",
                "title": "Runtime Type Checking",
                "question": (
                    "How can you enforce type hints at runtime?\n\n"
                    "  # Option A: Manual\n"
                    "  def process(data: str) -> str:\n"
                    "      if not isinstance(data, str):\n"
                    "          raise TypeError\n"
                    "      return data.upper()\n\n"
                    "  # Option B: Library\n"
                    "  from pydantic import BaseModel\n"
                    "  class Config(BaseModel):\n"
                    "      host: str\n"
                    "      port: int  # validated at runtime"
                ),
                "lesson": (
                    "Python doesn't enforce type hints by default. For runtime checking:\n\n"
                    "  1. Manual: isinstance() checks in your code\n"
                    "  2. pydantic: validates on model creation\n"
                    "  3. beartype: decorator that checks types on every call\n"
                    "  4. typeguard: import hook or decorator for checking\n\n"
                    "Static checkers (mypy, pyright) catch errors before runtime.\n"
                    "Runtime libraries catch errors during execution.\n"
                    "Best practice: use both."
                ),
                "options": [
                    "Type hints are always enforced — no extra work needed",
                    "Use manual isinstance checks or libraries like pydantic/beartype for runtime enforcement",
                    "Add 'strict=True' to the function annotation",
                    "Import typing.enforce to enable runtime checking globally",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Python itself never enforces annotations — you need extra code or libraries.",
                    "pydantic, beartype, and typeguard are popular runtime checking libraries.",
                ],
            },
        ],
    },

    # ── ZONE 7: TESTING ADVANCED ────────────────────────────────────────
    "testing_advanced": {
        "id": "testing_advanced",
        "name": "The Test Matrix",
        "subtitle": "pytest Fixtures, Parametrize, Mocking, Hypothesis, Coverage",
        "color": "white",
        "icon": "🧪",
        "commands": ["pytest", "@pytest.fixture", "@pytest.mark.parametrize", "mock"],
        "challenges": [
            {
                "id": "test_1",
                "type": "quiz",
                "title": "pytest Fixtures",
                "question": (
                    "What does a pytest fixture do?\n\n"
                    "  import pytest\n\n"
                    "  @pytest.fixture\n"
                    "  def db_connection():\n"
                    "      conn = create_connection()\n"
                    "      yield conn\n"
                    "      conn.close()\n\n"
                    "  def test_query(db_connection):\n"
                    "      result = db_connection.execute('SELECT 1')\n"
                    "      assert result == 1"
                ),
                "lesson": (
                    "Fixtures provide reusable setup/teardown for tests. pytest\n"
                    "injects them by matching the parameter name to the fixture name.\n\n"
                    "  @pytest.fixture\n"
                    "  def db_connection():\n"
                    "      conn = create()     # setup\n"
                    "      yield conn           # provide to test\n"
                    "      conn.close()         # teardown\n\n"
                    "yield separates setup from teardown. Fixtures can have scopes:\n"
                    "function (default), class, module, session."
                ),
                "options": [
                    "A decorator that marks a function as a test case",
                    "A setup/teardown mechanism injected into tests by parameter name",
                    "A configuration file for test parameters",
                    "A plugin that generates test data randomly",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "test_query(db_connection) — the parameter name matches the fixture name.",
                    "yield provides the resource to the test; code after yield is teardown.",
                ],
            },
            {
                "id": "test_2",
                "type": "quiz",
                "title": "@pytest.mark.parametrize",
                "question": (
                    "What does parametrize do?\n\n"
                    "  @pytest.mark.parametrize('input,expected', [\n"
                    "      ('hello', 5),\n"
                    "      ('', 0),\n"
                    "      ('world', 5),\n"
                    "  ])\n"
                    "  def test_length(input, expected):\n"
                    "      assert len(input) == expected"
                ),
                "lesson": (
                    "@parametrize runs the same test with multiple input sets.\n"
                    "Each tuple becomes a separate test case:\n\n"
                    "  test_length[hello-5]   — PASSED\n"
                    "  test_length[-0]        — PASSED\n"
                    "  test_length[world-5]   — PASSED\n\n"
                    "This eliminates copy-paste tests. One test function,\n"
                    "multiple data points. Each runs independently —\n"
                    "one failure doesn't block others."
                ),
                "options": [
                    "Runs the test in parallel across multiple threads",
                    "Runs the same test function once for each set of parameters",
                    "Generates random parameters for fuzz testing",
                    "Makes the test optional — only runs if parameters are available",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Three tuples = three separate test runs with different data.",
                    "Each parameter set produces an independent test case in the output.",
                ],
            },
            {
                "id": "test_3",
                "type": "quiz",
                "title": "Mocking with unittest.mock",
                "question": (
                    "What does mock.patch do?\n\n"
                    "  from unittest.mock import patch\n\n"
                    "  def get_user():\n"
                    "      return requests.get('https://api.example.com/user').json()\n\n"
                    "  @patch('mymodule.requests.get')\n"
                    "  def test_get_user(mock_get):\n"
                    "      mock_get.return_value.json.return_value = {'name': 'Ghost'}\n"
                    "      result = get_user()\n"
                    "      assert result['name'] == 'Ghost'"
                ),
                "lesson": (
                    "mock.patch replaces an object with a Mock for the duration of\n"
                    "the test, then restores it automatically.\n\n"
                    "  @patch('mymodule.requests.get')  — replaces requests.get\n"
                    "  mock_get.return_value.json.return_value = {...}\n"
                    "  — chains: mock_get() returns an object whose .json() returns the dict\n\n"
                    "Key rule: patch where the object is USED, not where it's defined.\n"
                    "Patch 'mymodule.requests.get', not 'requests.get'."
                ),
                "options": [
                    "Deletes the function so the test can verify it's not called",
                    "Replaces an object with a Mock for the test's duration, then restores it",
                    "Creates a copy of the function that logs all calls",
                    "Patches the production database with test data",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The test never makes a real HTTP call — the mock replaces requests.get.",
                    "After the test, the original requests.get is automatically restored.",
                ],
            },
            {
                "id": "test_4",
                "type": "quiz",
                "title": "Property-Based Testing",
                "question": (
                    "What does hypothesis do differently from parametrize?\n\n"
                    "  from hypothesis import given\n"
                    "  from hypothesis import strategies as st\n\n"
                    "  @given(st.lists(st.integers()))\n"
                    "  def test_sort_is_idempotent(xs):\n"
                    "      assert sorted(sorted(xs)) == sorted(xs)"
                ),
                "lesson": (
                    "Hypothesis generates random test inputs based on strategies.\n"
                    "Instead of you writing specific examples, it explores the input\n"
                    "space automatically:\n\n"
                    "  st.integers()        — random ints (including edge cases)\n"
                    "  st.lists(st.text())  — random lists of strings\n"
                    "  st.floats()          — includes NaN, inf, -0.0\n\n"
                    "It finds edge cases you wouldn't think of. When it finds a\n"
                    "failure, it shrinks the input to the smallest failing example."
                ),
                "options": [
                    "It runs tests faster using compiled strategies",
                    "It generates random inputs from strategies and automatically finds edge cases",
                    "It parameterizes tests from a CSV file",
                    "It generates documentation from test functions",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "@given generates hundreds of random inputs — you don't choose specific values.",
                    "Hypothesis automatically shrinks failing inputs to the minimal reproduction case.",
                ],
            },
            {
                "id": "test_5",
                "type": "quiz",
                "title": "Test Coverage",
                "question": (
                    "What does code coverage measure?\n\n"
                    "  $ pytest --cov=mypackage --cov-report=term-missing\n\n"
                    "  Name              Stmts   Miss  Cover   Missing\n"
                    "  mypackage/core.py    100     15    85%   42-56"
                ),
                "lesson": (
                    "Code coverage measures what percentage of your source code\n"
                    "is executed during tests:\n\n"
                    "  - Statement coverage: which lines ran\n"
                    "  - Branch coverage: which if/else branches were taken\n"
                    "  - Missing: lines 42-56 were never executed\n\n"
                    "100% coverage doesn't mean bug-free — it means every line\n"
                    "was reached. The logic could still be wrong.\n"
                    "Coverage is a necessary but not sufficient quality metric."
                ),
                "options": [
                    "How fast the tests run across the codebase",
                    "What percentage of source code lines are executed during tests",
                    "How many test files exist per module",
                    "The number of assertions in each test function",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "85% coverage means 85 of 100 statements were executed during tests.",
                    "Missing: lines 42-56 tells you exactly which code was never tested.",
                ],
            },
            {
                "id": "test_6",
                "type": "quiz",
                "title": "Fixture Scopes",
                "question": (
                    "What happens when you set scope='session' on a fixture?\n\n"
                    "  @pytest.fixture(scope='session')\n"
                    "  def docker_db():\n"
                    "      container = start_postgres()\n"
                    "      yield container.connection_string\n"
                    "      container.stop()"
                ),
                "lesson": (
                    "Fixture scopes control how often setup/teardown runs:\n\n"
                    "  scope='function' — once per test (default)\n"
                    "  scope='class'    — once per test class\n"
                    "  scope='module'   — once per test file\n"
                    "  scope='session'  — once for the entire test run\n\n"
                    "A session-scoped database fixture starts Postgres once,\n"
                    "shares it across all tests, and stops it when done.\n"
                    "This avoids expensive setup for every single test."
                ),
                "options": [
                    "The fixture is created once and shared across all tests in the entire test run",
                    "The fixture is created once per test function",
                    "The fixture runs in a background session while tests execute",
                    "The fixture is only available in the first test module",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "scope='session' means the entire pytest run shares one instance.",
                    "Start once, use everywhere, teardown at the very end.",
                ],
            },
        ],
    },

    # ── ZONE 8: PACKAGING ───────────────────────────────────────────────
    "packaging": {
        "id": "packaging",
        "name": "The Distribution Layer",
        "subtitle": "pyproject.toml, setuptools, Wheels, PyPI, uv, Virtualenvs",
        "color": "white",
        "icon": "📦",
        "commands": ["pip install", "uv", "pyproject.toml", "python -m build"],
        "challenges": [
            {
                "id": "pkg_1",
                "type": "quiz",
                "title": "pyproject.toml",
                "question": (
                    "What is pyproject.toml?\n\n"
                    "  [build-system]\n"
                    "  requires = ['setuptools>=68.0']\n"
                    "  build-backend = 'setuptools.build_meta'\n\n"
                    "  [project]\n"
                    "  name = 'my-package'\n"
                    "  version = '1.0.0'\n"
                    "  dependencies = ['requests>=2.28']"
                ),
                "lesson": (
                    "pyproject.toml is the standard configuration file for Python\n"
                    "projects (PEP 517/518/621). It replaces setup.py and setup.cfg:\n\n"
                    "  [build-system]  — which build tool to use\n"
                    "  [project]       — package metadata (name, version, deps)\n"
                    "  [tool.X]        — tool-specific config (mypy, pytest, ruff)\n\n"
                    "One file for everything: build config, metadata, tool settings."
                ),
                "options": [
                    "A legacy configuration file replaced by setup.py",
                    "The standard Python project configuration file for metadata, builds, and tool config",
                    "A TOML-formatted requirements.txt",
                    "An optional alternative to Makefile for Python projects",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "pyproject.toml is the modern standard — it replaces setup.py.",
                    "It holds build system config, project metadata, and tool settings.",
                ],
            },
            {
                "id": "pkg_2",
                "type": "quiz",
                "title": "Virtual Environments",
                "question": (
                    "Why do you use a virtual environment?\n\n"
                    "  $ python -m venv .venv\n"
                    "  $ source .venv/bin/activate\n"
                    "  (.venv) $ pip install requests"
                ),
                "lesson": (
                    "A virtual environment is an isolated Python installation.\n"
                    "Packages installed inside it don't affect other projects\n"
                    "or the system Python:\n\n"
                    "  project-a/.venv → requests 2.28\n"
                    "  project-b/.venv → requests 2.31\n\n"
                    "Without virtualenvs, all projects share one set of packages.\n"
                    "Version conflicts become inevitable. Virtualenvs are mandatory\n"
                    "for professional Python development."
                ),
                "options": [
                    "To run Python code faster by compiling it",
                    "To isolate project dependencies from the system Python and other projects",
                    "To encrypt Python packages for security",
                    "To emulate a different operating system for testing",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Each project gets its own isolated set of installed packages.",
                    ".venv contains a separate Python interpreter and lib directory.",
                ],
            },
            {
                "id": "pkg_3",
                "type": "quiz",
                "title": "Wheels vs Source Distributions",
                "question": (
                    "What is a wheel (.whl) file?\n\n"
                    "  $ python -m build\n"
                    "  dist/\n"
                    "    my_package-1.0.0.tar.gz      # sdist\n"
                    "    my_package-1.0.0-py3-none-any.whl  # wheel"
                ),
                "lesson": (
                    "A wheel is a pre-built distribution format (PEP 427).\n\n"
                    "  .tar.gz (sdist) — source code, needs to be built on install\n"
                    "  .whl (wheel)    — pre-built, installs instantly (just unzip)\n\n"
                    "Wheels are faster to install because there's no build step.\n"
                    "For pure Python: py3-none-any (works everywhere).\n"
                    "For C extensions: platform-specific (cp311-linux_x86_64).\n\n"
                    "Always upload both sdist and wheel to PyPI."
                ),
                "options": [
                    "A compressed archive of documentation",
                    "A pre-built distribution that installs without a build step",
                    "A wheel of dependencies that pip resolves circularly",
                    "A binary executable for the package",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Wheel = pre-built. sdist = source that needs building.",
                    ".whl files are just zip archives with a specific internal structure.",
                ],
            },
            {
                "id": "pkg_4",
                "type": "quiz",
                "title": "Publishing to PyPI",
                "question": (
                    "What is the standard workflow to publish a package to PyPI?\n\n"
                    "  $ python -m build\n"
                    "  $ ??? upload dist/*"
                ),
                "lesson": (
                    "The standard publishing workflow:\n\n"
                    "  1. python -m build      — creates sdist + wheel in dist/\n"
                    "  2. twine upload dist/*   — uploads to PyPI\n\n"
                    "twine is the official upload tool. It uses HTTPS and supports\n"
                    "API tokens for authentication.\n\n"
                    "  twine upload --repository testpypi dist/*  # test first\n"
                    "  twine upload dist/*                        # production\n\n"
                    "Modern alternative: use 'uv publish' or CI/CD trusted publishers."
                ),
                "options": [
                    "pip upload dist/*",
                    "twine upload dist/*",
                    "setuptools deploy dist/*",
                    "pypi push dist/*",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The upload tool is named after the string-wrapping material.",
                    "twine handles secure uploading to PyPI with proper authentication.",
                ],
            },
            {
                "id": "pkg_5",
                "type": "quiz",
                "title": "uv — The Fast Package Manager",
                "question": (
                    "What is uv and how does it differ from pip?\n\n"
                    "  $ uv pip install requests    # drop-in pip replacement\n"
                    "  $ uv venv                    # create virtualenv\n"
                    "  $ uv lock                    # generate lockfile\n"
                    "  $ uv run pytest              # run in managed env"
                ),
                "lesson": (
                    "uv is a fast Python package manager written in Rust by Astral.\n"
                    "It replaces pip, pip-tools, virtualenv, and pyenv:\n\n"
                    "  Speed:    10-100x faster than pip for dependency resolution\n"
                    "  Lockfile: uv lock creates a reproducible lockfile\n"
                    "  Venv:     uv venv creates virtualenvs instantly\n"
                    "  Run:      uv run executes in a managed environment\n\n"
                    "It's a drop-in replacement for most pip commands while adding\n"
                    "modern features like lockfiles and workspace management."
                ),
                "options": [
                    "A UV light-based code scanner for security vulnerabilities",
                    "A Rust-based Python package manager that's 10-100x faster than pip with lockfile support",
                    "A virtual machine for running Python in isolation",
                    "A UI framework for building Python desktop applications",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Written in Rust. Made by Astral (the ruff team). Drop-in pip replacement.",
                    "Key features: speed, lockfiles, venv management, and uv run.",
                ],
            },
            {
                "id": "pkg_6",
                "type": "quiz",
                "title": "Entry Points and Scripts",
                "question": (
                    "How do you create a CLI command from a Python package?\n\n"
                    "  [project.scripts]\n"
                    "  mytool = 'mypackage.cli:main'\n\n"
                    "  # After pip install:\n"
                    "  $ mytool --help"
                ),
                "lesson": (
                    "[project.scripts] in pyproject.toml defines console entry points.\n"
                    "After installation, 'mytool' becomes a system command that calls\n"
                    "mypackage.cli:main — the main() function in mypackage/cli.py.\n\n"
                    "  [project.scripts]            — CLI commands\n"
                    "  [project.gui-scripts]         — GUI commands\n"
                    "  [project.entry-points.group]  — plugin entry points\n\n"
                    "pip creates a wrapper script in the bin/ directory of your\n"
                    "virtualenv that calls the specified function."
                ),
                "options": [
                    "Add a __main__.py and use python -m mypackage",
                    "Define the command in [project.scripts] pointing to a module:function",
                    "Create a shell script in the package's bin/ directory",
                    "Add a shebang line to the main Python file",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "[project.scripts] maps a command name to a Python function.",
                    "mytool = 'mypackage.cli:main' — command 'mytool' calls main() in cli.py.",
                ],
            },
        ],
    },
}
