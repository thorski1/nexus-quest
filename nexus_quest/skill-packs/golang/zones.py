"""
zones.py — Go (Golang) zones and challenges for Go Ops.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "go_basics",
    "control_flow",
    "data_structures",
    "concurrency",
    "interfaces",
    "standard_library",
    "go_modules",
    "go_patterns",
]

ZONES = {
    # ── ZONE 1: GO BASICS ──────────────────────────────────────────────
    "go_basics": {
        "id": "go_basics",
        "name": "The Foundation Layer",
        "subtitle": "Variables, Types, Functions, Packages & Error Handling",
        "color": "cyan",
        "icon": "🐹",
        "commands": ["go run", "go build", "go fmt", "go vet"],
        "challenges": [
            {
                "id": "go_var_decl",
                "type": "quiz",
                "title": "Variable Declaration",
                "question": (
                    "What is the short variable declaration operator in Go?\n\n"
                    "  func main() {\n"
                    "      name ___ \"Ghost\"\n"
                    "      fmt.Println(name)\n"
                    "  }"
                ),
                "lesson": (
                    "Go has two ways to declare variables:\n\n"
                    "  var name string = \"Ghost\"   // explicit type\n"
                    "  name := \"Ghost\"              // short declaration (type inferred)\n\n"
                    "The := operator declares AND assigns in one step. It can only be used\n"
                    "inside functions — not at package level."
                ),
                "options": [
                    "=  (simple assignment)",
                    ":= (short variable declaration)",
                    "== (equality comparison)",
                    "<- (channel send)",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It combines a colon and an equals sign.",
                    "Short declaration uses := and can only appear inside functions.",
                ],
            },
            {
                "id": "go_zero_values",
                "type": "quiz",
                "title": "Zero Values",
                "question": (
                    "In Go, every variable has a zero value if not explicitly initialized.\n"
                    "What is the zero value of a `string`?"
                ),
                "lesson": (
                    "Go zero values:\n"
                    "  int, float64  → 0\n"
                    "  bool          → false\n"
                    "  string        → \"\" (empty string)\n"
                    "  pointer/slice/map/channel/func/interface → nil\n\n"
                    "There is no undefined or null for value types. Every variable\n"
                    "is always valid and usable from the moment it's declared."
                ),
                "options": [
                    "nil",
                    "\"\" (empty string)",
                    "0",
                    "undefined",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Strings are value types in Go, not reference types.",
                    "The zero value is the empty version of the type — for strings, that's empty quotes.",
                ],
            },
            {
                "id": "go_multiple_return",
                "type": "quiz",
                "title": "Multiple Return Values",
                "question": (
                    "What does this function signature return?\n\n"
                    "  func decrypt(data []byte) (string, error)"
                ),
                "lesson": (
                    "Go functions can return multiple values — most commonly a result\n"
                    "and an error. This is Go's primary error handling pattern:\n\n"
                    "  result, err := decrypt(payload)\n"
                    "  if err != nil {\n"
                    "      log.Fatal(err)\n"
                    "  }\n\n"
                    "The caller MUST handle both values. Ignoring the error is a\n"
                    "compile-time warning with go vet and a code smell in reviews."
                ),
                "options": [
                    "A single string value",
                    "A string and an error",
                    "A tuple containing string and error",
                    "A string or an error (union type)",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Look at what's inside the second set of parentheses.",
                    "Go uses (type1, type2) to indicate multiple return values.",
                ],
            },
            {
                "id": "go_packages",
                "type": "quiz",
                "title": "Package Visibility",
                "question": (
                    "In Go, how do you export a function so other packages can use it?\n\n"
                    "  // package crypto\n"
                    "  func encrypt(data string) string { ... }  // Can other packages call this?"
                ),
                "lesson": (
                    "Go uses capitalization for visibility:\n\n"
                    "  func encrypt(...)  → unexported (private to this package)\n"
                    "  func Encrypt(...)  → exported (visible to other packages)\n\n"
                    "This applies to functions, types, struct fields, constants,\n"
                    "and variables. No public/private keywords needed — just the\n"
                    "first letter."
                ),
                "options": [
                    "Add the `public` keyword before the function",
                    "Capitalize the first letter of the function name",
                    "Add the function to an exports list",
                    "Use the `export` keyword in the package declaration",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Go doesn't have public/private keywords.",
                    "The convention is based on the first letter of the identifier.",
                ],
            },
            {
                "id": "go_fmt_verbs",
                "type": "quiz",
                "title": "fmt Print Verbs",
                "question": (
                    "What fmt verb prints a value's type?\n\n"
                    "  x := 42\n"
                    "  fmt.Printf(\"type: ___\\n\", x)  // should print: type: int"
                ),
                "lesson": (
                    "Common fmt verbs:\n"
                    "  %v  → value (default format)\n"
                    "  %T  → type of the value\n"
                    "  %d  → integer (decimal)\n"
                    "  %s  → string\n"
                    "  %f  → float\n"
                    "  %+v → struct with field names\n"
                    "  %#v → Go-syntax representation"
                ),
                "options": [
                    "%v",
                    "%s",
                    "%T",
                    "%d",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Think Type — which letter represents that?",
                    "%T prints the Go type of any value.",
                ],
            },
            {
                "id": "go_error_handling",
                "type": "quiz",
                "title": "Error Handling Idiom",
                "question": (
                    "What is the idiomatic way to handle an error in Go?\n\n"
                    "  file, err := os.Open(\"config.yaml\")\n"
                    "  // what comes next?"
                ),
                "lesson": (
                    "The Go error handling idiom:\n\n"
                    "  result, err := someFunction()\n"
                    "  if err != nil {\n"
                    "      return fmt.Errorf(\"context: %w\", err)\n"
                    "  }\n\n"
                    "Go does not use exceptions (try/catch). Errors are values\n"
                    "returned by functions. The caller checks err != nil immediately\n"
                    "after every call that can fail."
                ),
                "options": [
                    "try { file } catch(err) { ... }",
                    "if err != nil { handle the error }",
                    "file.catch(func(err) { ... })",
                    "defer handleError(err)",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Go doesn't have try/catch or exceptions.",
                    "Check if the error is not nil — that means something went wrong.",
                ],
            },
        ],
    },

    # ── ZONE 2: CONTROL FLOW ───────────────────────────────────────────
    "control_flow": {
        "id": "control_flow",
        "name": "Flow Control Matrix",
        "subtitle": "If/Else, For Loops, Switch, Defer & Panic/Recover",
        "color": "green",
        "icon": "🔀",
        "commands": ["if", "for", "switch", "defer"],
        "challenges": [
            {
                "id": "go_if_init",
                "type": "quiz",
                "title": "If with Init Statement",
                "question": (
                    "What does this Go code do?\n\n"
                    "  if err := validate(input); err != nil {\n"
                    "      return err\n"
                    "  }"
                ),
                "lesson": (
                    "Go's if statement can include an init statement before the condition:\n\n"
                    "  if <init>; <condition> { ... }\n\n"
                    "The variable declared in the init statement is scoped to the if/else\n"
                    "block. This keeps err from leaking into the outer scope and is the\n"
                    "idiomatic pattern for inline error checks."
                ),
                "options": [
                    "Declares err globally and checks if it's nil",
                    "Calls validate, assigns to err, then checks err != nil — all in one statement",
                    "Creates a goroutine that validates input",
                    "This is a syntax error — you can't declare variables in an if",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The semicolon separates an init statement from the condition.",
                    "err is scoped only to this if/else block.",
                ],
            },
            {
                "id": "go_for_loop",
                "type": "quiz",
                "title": "The Only Loop",
                "question": "Go has only one looping construct. What is it?",
                "lesson": (
                    "Go has only `for` — no while, no do-while, no loop.\n\n"
                    "  for i := 0; i < 10; i++ { }    // C-style\n"
                    "  for condition { }                // while-style\n"
                    "  for { }                          // infinite loop\n"
                    "  for i, v := range slice { }      // range-based\n\n"
                    "One keyword, four patterns. Simple."
                ),
                "options": [
                    "while",
                    "loop",
                    "for",
                    "foreach",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Go eliminated redundant keywords — one loop to rule them all.",
                    "It's the same keyword used in C, but it covers all loop styles.",
                ],
            },
            {
                "id": "go_range",
                "type": "quiz",
                "title": "Range Iteration",
                "question": (
                    "What does `range` return when iterating over a slice?\n\n"
                    "  for ___, ___ := range servers {\n"
                    "      fmt.Println(???)\n"
                    "  }"
                ),
                "lesson": (
                    "range returns two values per iteration:\n\n"
                    "  for index, value := range slice { }    // slice/array\n"
                    "  for key, value := range aMap { }       // map\n"
                    "  for index, char := range aString { }   // string (rune iteration)\n"
                    "  for value := range aChannel { }        // channel (one value)\n\n"
                    "Use _ to discard a value you don't need:\n"
                    "  for _, server := range servers { }"
                ),
                "options": [
                    "Only the value",
                    "Only the index",
                    "The index and the value",
                    "A boolean indicating if more elements exist",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Range always gives you two things for slices and maps.",
                    "First comes the position, then comes the element.",
                ],
            },
            {
                "id": "go_switch",
                "type": "quiz",
                "title": "Switch Without Break",
                "question": (
                    "In Go's switch statement, what happens after a matching case executes?\n\n"
                    "  switch status {\n"
                    "  case \"active\":\n"
                    "      deploy()\n"
                    "  case \"pending\":\n"
                    "      queue()\n"
                    "  }"
                ),
                "lesson": (
                    "Go's switch does NOT fall through by default (unlike C/Java).\n"
                    "Each case breaks automatically. To explicitly fall through:\n\n"
                    "  case \"active\":\n"
                    "      deploy()\n"
                    "      fallthrough  // continues to next case\n\n"
                    "Go also supports expression-less switch (like if/else chain):\n"
                    "  switch {\n"
                    "  case x > 10:  ...\n"
                    "  case x > 5:   ...\n"
                    "  default:      ...\n"
                    "  }"
                ),
                "options": [
                    "It falls through to the next case automatically",
                    "It breaks automatically — no fallthrough unless explicit",
                    "It executes all remaining cases",
                    "It panics if no break is present",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Go changed the C default behavior — no more forgotten breaks.",
                    "You need the `fallthrough` keyword to get C-style behavior.",
                ],
            },
            {
                "id": "go_defer",
                "type": "quiz",
                "title": "Defer Execution",
                "question": (
                    "When does a deferred function call execute?\n\n"
                    "  func processLogs() {\n"
                    "      f, _ := os.Open(\"audit.log\")\n"
                    "      defer f.Close()\n"
                    "      // ... read and process file ...\n"
                    "  }"
                ),
                "lesson": (
                    "defer schedules a function call to run when the surrounding\n"
                    "function returns — regardless of how it returns (normal return,\n"
                    "panic, or error).\n\n"
                    "  defer f.Close()       // file cleanup\n"
                    "  defer mu.Unlock()     // mutex release\n"
                    "  defer span.End()      // tracing cleanup\n\n"
                    "Multiple defers execute in LIFO (last-in, first-out) order.\n"
                    "Arguments are evaluated immediately, but the call is delayed."
                ),
                "options": [
                    "Immediately when the defer line is reached",
                    "When the surrounding function returns",
                    "When the program exits",
                    "When the garbage collector runs",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Think of it as 'do this last, right before I leave this function.'",
                    "Deferred calls run when the enclosing function returns, not when main() ends.",
                ],
            },
            {
                "id": "go_panic_recover",
                "type": "quiz",
                "title": "Panic & Recover",
                "question": "How do you catch a panic in Go?",
                "lesson": (
                    "panic() stops normal execution and begins unwinding the stack.\n"
                    "recover() catches a panic — but ONLY inside a deferred function:\n\n"
                    "  func safeCall() {\n"
                    "      defer func() {\n"
                    "          if r := recover(); r != nil {\n"
                    "              log.Printf(\"recovered: %v\", r)\n"
                    "          }\n"
                    "      }()\n"
                    "      riskyOperation()  // may panic\n"
                    "  }\n\n"
                    "Panics are for truly unrecoverable situations (not normal errors).\n"
                    "Normal error handling uses the error return value pattern."
                ),
                "options": [
                    "try/catch block",
                    "recover() inside a deferred function",
                    "except panic { ... }",
                    "os.CatchPanic()",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Go doesn't have try/catch — but it has a mechanism that only works in defer.",
                    "The function is literally called recover().",
                ],
            },
        ],
    },

    # ── ZONE 3: DATA STRUCTURES ────────────────────────────────────────
    "data_structures": {
        "id": "data_structures",
        "name": "The Data Vault",
        "subtitle": "Slices, Maps, Structs, Pointers & Arrays",
        "color": "yellow",
        "icon": "🗄️",
        "commands": ["make", "append", "len", "cap"],
        "challenges": [
            {
                "id": "go_slice_vs_array",
                "type": "quiz",
                "title": "Array vs Slice",
                "question": (
                    "What is the difference between these two declarations?\n\n"
                    "  a := [3]int{1, 2, 3}   // declaration A\n"
                    "  b := []int{1, 2, 3}    // declaration B"
                ),
                "lesson": (
                    "Arrays have a FIXED size — it's part of the type:\n"
                    "  [3]int and [4]int are different types.\n\n"
                    "Slices are dynamic — backed by an array but can grow:\n"
                    "  []int is a slice. It has a length and a capacity.\n\n"
                    "In practice, you almost always use slices. Arrays are\n"
                    "mainly used when the size is known and fixed (e.g., SHA-256 = [32]byte)."
                ),
                "options": [
                    "They are identical — both are arrays",
                    "A is a fixed-size array, B is a dynamically-sized slice",
                    "A is a slice, B is an array",
                    "A is allocated on the heap, B on the stack",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Look inside the brackets — one has a number, the other doesn't.",
                    "[3]int = array (fixed). []int = slice (dynamic).",
                ],
            },
            {
                "id": "go_make_slice",
                "type": "quiz",
                "title": "make() for Slices",
                "question": (
                    "What does this create?\n\n"
                    "  servers := make([]string, 0, 10)"
                ),
                "lesson": (
                    "make() initializes slices, maps, and channels:\n\n"
                    "  make([]string, 0, 10)\n"
                    "         type    len  cap\n\n"
                    "This creates a string slice with length 0 and capacity 10.\n"
                    "Pre-allocating capacity avoids repeated memory allocations\n"
                    "when you know the approximate size upfront."
                ),
                "options": [
                    "A string array with 10 elements",
                    "A string slice with length 0 and capacity 10",
                    "A map of 10 strings",
                    "A buffered channel of 10 strings",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "make() takes the type, then length, then optional capacity.",
                    "Length 0 means empty, capacity 10 means room to grow without reallocation.",
                ],
            },
            {
                "id": "go_append",
                "type": "quiz",
                "title": "Append to Slice",
                "question": (
                    "Why must you reassign the result of append?\n\n"
                    "  servers = append(servers, \"proxy-01\")"
                ),
                "lesson": (
                    "append() may allocate a new underlying array if the slice\n"
                    "has reached its capacity. When that happens, it returns a\n"
                    "new slice header pointing to the new array.\n\n"
                    "  // WRONG — the new slice is lost:\n"
                    "  append(servers, \"proxy-01\")\n\n"
                    "  // CORRECT — reassign to capture possible new header:\n"
                    "  servers = append(servers, \"proxy-01\")\n\n"
                    "The slice header is a struct: { pointer, length, capacity }."
                ),
                "options": [
                    "append() modifies the slice in place — reassignment is optional",
                    "append() may return a new slice if the capacity is exceeded",
                    "append() always copies the entire slice",
                    "It's a Go convention but not strictly necessary",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "What happens when the underlying array runs out of room?",
                    "A new, larger array is allocated and the data is copied — the old pointer is stale.",
                ],
            },
            {
                "id": "go_maps",
                "type": "quiz",
                "title": "Map Operations",
                "question": (
                    "How do you check if a key exists in a Go map?\n\n"
                    "  services := map[string]int{\"api\": 8080, \"db\": 5432}"
                ),
                "lesson": (
                    "Go map lookups return two values — the value and a boolean:\n\n"
                    "  port, ok := services[\"api\"]\n"
                    "  if !ok {\n"
                    "      fmt.Println(\"service not found\")\n"
                    "  }\n\n"
                    "The 'comma ok' idiom: ok is true if the key exists, false otherwise.\n"
                    "Without the second value, accessing a missing key returns the zero value."
                ),
                "options": [
                    "services.hasKey(\"api\")",
                    "services.contains(\"api\")",
                    "value, ok := services[\"api\"] — check the ok boolean",
                    "if services[\"api\"] != nil { ... }",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Go doesn't have methods like hasKey() on maps.",
                    "Use the two-value assignment — the second value tells you if the key was found.",
                ],
            },
            {
                "id": "go_structs",
                "type": "quiz",
                "title": "Struct Definition",
                "question": (
                    "What does this define?\n\n"
                    "  type Server struct {\n"
                    "      Host    string\n"
                    "      Port    int\n"
                    "      healthy bool\n"
                    "  }"
                ),
                "lesson": (
                    "Structs are Go's composite types — groups of named fields:\n\n"
                    "  type Server struct {\n"
                    "      Host    string   // exported (uppercase)\n"
                    "      Port    int      // exported\n"
                    "      healthy bool     // unexported (lowercase)\n"
                    "  }\n\n"
                    "Exported fields (capitalized) are visible to other packages.\n"
                    "Unexported fields (lowercase) are package-private.\n"
                    "Go has no classes — structs + methods = objects."
                ),
                "options": [
                    "A class named Server with three public fields",
                    "A struct with two exported fields and one unexported field",
                    "An interface with three methods",
                    "A map type with string keys",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Look at the capitalization of each field name.",
                    "Host and Port start with uppercase (exported). healthy is lowercase (unexported).",
                ],
            },
            {
                "id": "go_pointers",
                "type": "quiz",
                "title": "Pointers",
                "question": (
                    "What does the * operator do in this function signature?\n\n"
                    "  func updateStatus(s *Server) {\n"
                    "      s.Status = \"running\"\n"
                    "  }"
                ),
                "lesson": (
                    "Go has pointers but no pointer arithmetic.\n\n"
                    "  & → address-of operator (get a pointer)\n"
                    "  * → dereference operator / pointer type\n\n"
                    "  s := Server{Host: \"proxy-01\"}\n"
                    "  p := &s           // p is *Server\n"
                    "  fmt.Println(p.Host) // auto-dereference for fields\n\n"
                    "Passing a pointer lets you modify the original value.\n"
                    "Passing by value creates a copy."
                ),
                "options": [
                    "It multiplies Server by s",
                    "It indicates s is a pointer to a Server (passed by reference)",
                    "It creates a new copy of Server",
                    "It marks Server as immutable",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "*Server means 'pointer to Server' — the function receives a memory address.",
                    "Changes through a pointer affect the original struct, not a copy.",
                ],
            },
        ],
    },

    # ── ZONE 4: CONCURRENCY ────────────────────────────────────────────
    "concurrency": {
        "id": "concurrency",
        "name": "The Concurrency Grid",
        "subtitle": "Goroutines, Channels, Select, WaitGroup & Mutexes",
        "color": "magenta",
        "icon": "⚡",
        "commands": ["go", "chan", "select", "sync"],
        "challenges": [
            {
                "id": "go_goroutine",
                "type": "quiz",
                "title": "Launching a Goroutine",
                "question": (
                    "How do you launch a function as a goroutine?\n\n"
                    "  func scanPort(host string, port int) { ... }"
                ),
                "lesson": (
                    "Prefix any function call with the `go` keyword:\n\n"
                    "  go scanPort(\"10.0.0.1\", 8080)\n\n"
                    "This starts the function in a new goroutine — a lightweight\n"
                    "thread managed by the Go runtime (not the OS). Goroutines\n"
                    "start with ~8KB of stack and can scale to millions."
                ),
                "options": [
                    "thread scanPort(\"10.0.0.1\", 8080)",
                    "async scanPort(\"10.0.0.1\", 8080)",
                    "go scanPort(\"10.0.0.1\", 8080)",
                    "spawn scanPort(\"10.0.0.1\", 8080)",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The keyword is the same as the language name.",
                    "Just put `go` before the function call.",
                ],
            },
            {
                "id": "go_channels",
                "type": "quiz",
                "title": "Channel Basics",
                "question": (
                    "What does this code do?\n\n"
                    "  ch := make(chan string)\n"
                    "  go func() { ch <- \"breach detected\" }()\n"
                    "  msg := <-ch"
                ),
                "lesson": (
                    "Channels are Go's primary communication mechanism between goroutines.\n\n"
                    "  ch := make(chan string)     // create unbuffered channel\n"
                    "  ch <- \"data\"                // send to channel (blocks until receiver)\n"
                    "  msg := <-ch                 // receive from channel (blocks until sender)\n\n"
                    "Unbuffered channels synchronize sender and receiver — one blocks\n"
                    "until the other is ready. This is CSP: 'Don't communicate by sharing\n"
                    "memory; share memory by communicating.'"
                ),
                "options": [
                    "Creates a goroutine that sends a string, then receives it on the main goroutine",
                    "Creates a mutex-protected string variable",
                    "Opens a network socket and sends a message",
                    "Creates a buffered queue of strings",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "<- is the channel operator. ch <- sends; <-ch receives.",
                    "The goroutine sends, the main function receives — synchronized.",
                ],
            },
            {
                "id": "go_buffered_chan",
                "type": "quiz",
                "title": "Buffered Channels",
                "question": (
                    "What is the difference between these channels?\n\n"
                    "  unbuf := make(chan int)     // A\n"
                    "  buf := make(chan int, 10)   // B"
                ),
                "lesson": (
                    "Unbuffered channel: send blocks until a receiver is ready.\n"
                    "Buffered channel: send blocks only when the buffer is full.\n\n"
                    "  make(chan int)       // unbuffered — synchronous\n"
                    "  make(chan int, 10)   // buffered with capacity 10\n\n"
                    "Buffered channels are useful for decoupling producers\n"
                    "and consumers or limiting concurrency."
                ),
                "options": [
                    "A is a read-only channel, B is a write-only channel",
                    "A is unbuffered (blocks on send), B is buffered with capacity 10",
                    "A holds ints, B holds up to 10 different types",
                    "There is no difference — the 10 is ignored",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The second argument to make(chan) sets the buffer capacity.",
                    "No buffer = synchronous. With buffer = can hold N values before blocking.",
                ],
            },
            {
                "id": "go_select",
                "type": "quiz",
                "title": "Select Statement",
                "question": (
                    "What does `select` do in Go?\n\n"
                    "  select {\n"
                    "  case msg := <-dataCh:\n"
                    "      process(msg)\n"
                    "  case err := <-errCh:\n"
                    "      handleError(err)\n"
                    "  case <-time.After(5 * time.Second):\n"
                    "      fmt.Println(\"timeout\")\n"
                    "  }"
                ),
                "lesson": (
                    "select lets a goroutine wait on multiple channel operations:\n\n"
                    "  - Blocks until one case is ready\n"
                    "  - If multiple are ready, one is chosen at random\n"
                    "  - A default case makes it non-blocking\n\n"
                    "Common patterns:\n"
                    "  - Timeout: case <-time.After(duration)\n"
                    "  - Cancellation: case <-ctx.Done()\n"
                    "  - Fan-in: merge multiple channels"
                ),
                "options": [
                    "Selects a random goroutine to execute",
                    "Waits on multiple channel operations and proceeds with the first one ready",
                    "Queries a database and returns results",
                    "Switches between different struct types",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "select is like switch, but for channels.",
                    "It blocks until one of the channel operations can proceed.",
                ],
            },
            {
                "id": "go_waitgroup",
                "type": "quiz",
                "title": "sync.WaitGroup",
                "question": (
                    "What problem does sync.WaitGroup solve?\n\n"
                    "  var wg sync.WaitGroup\n"
                    "  for _, host := range targets {\n"
                    "      wg.Add(1)\n"
                    "      go func(h string) {\n"
                    "          defer wg.Done()\n"
                    "          scan(h)\n"
                    "      }(host)\n"
                    "  }\n"
                    "  wg.Wait()"
                ),
                "lesson": (
                    "WaitGroup waits for a collection of goroutines to finish.\n\n"
                    "  wg.Add(n)   → increment counter by n\n"
                    "  wg.Done()   → decrement counter by 1 (usually deferred)\n"
                    "  wg.Wait()   → block until counter reaches 0\n\n"
                    "Without WaitGroup, the main goroutine could exit before\n"
                    "the spawned goroutines complete their work."
                ),
                "options": [
                    "Limits the number of concurrent goroutines",
                    "Waits for all goroutines to complete before continuing",
                    "Groups goroutines into a single thread",
                    "Provides mutual exclusion for shared data",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Add counts up, Done counts down, Wait blocks until zero.",
                    "It solves 'how do I know all my goroutines are finished?'",
                ],
            },
            {
                "id": "go_mutex",
                "type": "quiz",
                "title": "sync.Mutex",
                "question": (
                    "When do you need a sync.Mutex?\n\n"
                    "  var mu sync.Mutex\n"
                    "  var count int\n\n"
                    "  func increment() {\n"
                    "      mu.Lock()\n"
                    "      count++\n"
                    "      mu.Unlock()\n"
                    "  }"
                ),
                "lesson": (
                    "A mutex provides mutual exclusion — only one goroutine can\n"
                    "hold the lock at a time.\n\n"
                    "  mu.Lock()      // acquire lock (blocks if already held)\n"
                    "  // critical section — safe to read/write shared data\n"
                    "  mu.Unlock()    // release lock\n\n"
                    "Always defer Unlock() to prevent deadlocks:\n"
                    "  mu.Lock()\n"
                    "  defer mu.Unlock()\n\n"
                    "sync.RWMutex allows multiple concurrent readers."
                ),
                "options": [
                    "When you want to run goroutines in sequence",
                    "When multiple goroutines read/write the same shared variable",
                    "When you need to close a channel",
                    "When you need to limit memory usage",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Without a mutex, concurrent writes to the same variable cause a data race.",
                    "Lock() and Unlock() protect the 'critical section' where shared data is accessed.",
                ],
            },
        ],
    },

    # ── ZONE 5: INTERFACES ─────────────────────────────────────────────
    "interfaces": {
        "id": "interfaces",
        "name": "The Interface Protocol",
        "subtitle": "Interfaces, Implicit Implementation, Type Assertions & Embedding",
        "color": "blue",
        "icon": "🔌",
        "commands": ["interface", "type assertion", "type switch"],
        "challenges": [
            {
                "id": "go_interface_def",
                "type": "quiz",
                "title": "Defining an Interface",
                "question": (
                    "What does this define?\n\n"
                    "  type Scanner interface {\n"
                    "      Scan(target string) ([]Finding, error)\n"
                    "      Name() string\n"
                    "  }"
                ),
                "lesson": (
                    "An interface in Go is a set of method signatures:\n\n"
                    "  type Scanner interface {\n"
                    "      Scan(target string) ([]Finding, error)\n"
                    "      Name() string\n"
                    "  }\n\n"
                    "Any type that implements ALL the methods in the interface\n"
                    "automatically satisfies it. No 'implements' keyword needed.\n"
                    "Interfaces are the primary abstraction mechanism in Go."
                ),
                "options": [
                    "A struct with two fields",
                    "A set of method signatures that any type can satisfy implicitly",
                    "An abstract class that must be inherited",
                    "A function type with two variants",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Interfaces describe behavior (methods), not data (fields).",
                    "In Go, satisfying an interface is implicit — no 'implements' declaration.",
                ],
            },
            {
                "id": "go_implicit_impl",
                "type": "quiz",
                "title": "Implicit Implementation",
                "question": (
                    "Does PortScanner implement the Scanner interface?\n\n"
                    "  type PortScanner struct { timeout time.Duration }\n\n"
                    "  func (p *PortScanner) Scan(target string) ([]Finding, error) { ... }\n"
                    "  func (p *PortScanner) Name() string { return \"port-scanner\" }"
                ),
                "lesson": (
                    "Yes. PortScanner implements Scanner because it has both\n"
                    "Scan() and Name() methods with the correct signatures.\n\n"
                    "Go interfaces are satisfied implicitly:\n"
                    "  - No 'implements' keyword\n"
                    "  - No explicit declaration\n"
                    "  - If the methods match, the type satisfies the interface\n\n"
                    "This means you can define an interface AFTER the concrete\n"
                    "types exist — powerful for decoupling."
                ),
                "options": [
                    "No — it needs an 'implements Scanner' declaration",
                    "No — it's missing the interface embedding",
                    "Yes — it has all the methods defined in the Scanner interface",
                    "Only if Scanner is in the same package",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Count the methods in the interface and compare them to the type's methods.",
                    "Go checks method sets at compile time — no explicit declaration needed.",
                ],
            },
            {
                "id": "go_empty_interface",
                "type": "quiz",
                "title": "The Empty Interface",
                "question": (
                    "What can `interface{}` (or `any`) hold?\n\n"
                    "  func logEvent(event interface{}) { ... }"
                ),
                "lesson": (
                    "The empty interface has zero methods — every type satisfies it.\n\n"
                    "  interface{}   // Go 1.17 and earlier\n"
                    "  any           // Go 1.18+ alias\n\n"
                    "It's Go's equivalent of 'any type.' Used in:\n"
                    "  - json.Unmarshal (map[string]interface{})\n"
                    "  - fmt.Println (accepts ...interface{})\n"
                    "  - Generic containers before Go 1.18 generics\n\n"
                    "Use sparingly — you lose type safety."
                ),
                "options": [
                    "Only string values",
                    "Only struct types",
                    "Any value of any type",
                    "Only types that implement at least one method",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Zero required methods means every type qualifies.",
                    "interface{} is Go's way of saying 'I accept anything.'",
                ],
            },
            {
                "id": "go_type_assertion",
                "type": "quiz",
                "title": "Type Assertions",
                "question": (
                    "What does this code do?\n\n"
                    "  var event interface{} = \"breach detected\"\n"
                    "  s, ok := event.(string)"
                ),
                "lesson": (
                    "A type assertion extracts the concrete value from an interface:\n\n"
                    "  s := event.(string)       // panics if event is not a string\n"
                    "  s, ok := event.(string)    // safe — ok is false if wrong type\n\n"
                    "For checking multiple types, use a type switch:\n"
                    "  switch v := event.(type) {\n"
                    "  case string: ...\n"
                    "  case int: ...\n"
                    "  case error: ...\n"
                    "  }"
                ),
                "options": [
                    "Casts event to a string (like casting in C)",
                    "Asserts event holds a string and extracts it; ok indicates success",
                    "Converts event to a string representation",
                    "Checks if event is a string type at compile time",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The .(Type) syntax is called a type assertion.",
                    "The two-value form is safe — ok is false if the assertion fails.",
                ],
            },
            {
                "id": "go_interface_composition",
                "type": "quiz",
                "title": "Interface Composition",
                "question": (
                    "What does this create?\n\n"
                    "  type ReadCloser interface {\n"
                    "      Reader\n"
                    "      Closer\n"
                    "  }"
                ),
                "lesson": (
                    "Go interfaces can embed other interfaces to compose them:\n\n"
                    "  type Reader interface { Read(p []byte) (int, error) }\n"
                    "  type Closer interface { Close() error }\n"
                    "  type ReadCloser interface {\n"
                    "      Reader\n"
                    "      Closer\n"
                    "  }\n\n"
                    "ReadCloser requires both Read() and Close() methods.\n"
                    "The io package uses this pattern extensively:\n"
                    "  io.ReadWriter, io.ReadCloser, io.ReadWriteCloser"
                ),
                "options": [
                    "A struct that inherits from Reader and Closer",
                    "A new interface that requires all methods from both Reader and Closer",
                    "A function that reads and then closes",
                    "A type alias for Reader",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Embedding interfaces combines their method sets.",
                    "To satisfy ReadCloser, you must implement methods from both Reader and Closer.",
                ],
            },
        ],
    },

    # ── ZONE 6: STANDARD LIBRARY ───────────────────────────────────────
    "standard_library": {
        "id": "standard_library",
        "name": "The Standard Arsenal",
        "subtitle": "net/http, encoding/json, os, io, testing & context",
        "color": "white",
        "icon": "📚",
        "commands": ["net/http", "encoding/json", "os", "testing"],
        "challenges": [
            {
                "id": "go_http_handler",
                "type": "quiz",
                "title": "HTTP Handler",
                "question": (
                    "What interface must a type satisfy to handle HTTP requests?\n\n"
                    "  // from net/http\n"
                    "  type Handler interface {\n"
                    "      ServeHTTP(ResponseWriter, *Request)\n"
                    "  }"
                ),
                "lesson": (
                    "The http.Handler interface requires one method: ServeHTTP.\n\n"
                    "  type healthHandler struct{}\n"
                    "  func (h healthHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {\n"
                    "      w.Write([]byte(\"ok\"))\n"
                    "  }\n\n"
                    "For simpler cases, use http.HandleFunc:\n"
                    "  http.HandleFunc(\"/health\", func(w http.ResponseWriter, r *http.Request) {\n"
                    "      w.Write([]byte(\"ok\"))\n"
                    "  })"
                ),
                "options": [
                    "http.Server",
                    "http.Handler — implement ServeHTTP(ResponseWriter, *Request)",
                    "http.Router",
                    "http.Controller",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The interface is named Handler, and it has exactly one method.",
                    "ServeHTTP is the single method you need to implement.",
                ],
            },
            {
                "id": "go_json_tags",
                "type": "quiz",
                "title": "JSON Struct Tags",
                "question": (
                    "What do the backtick annotations do?\n\n"
                    "  type Alert struct {\n"
                    "      Severity string `json:\"severity\"`\n"
                    "      Message  string `json:\"msg,omitempty\"`\n"
                    "  }"
                ),
                "lesson": (
                    "Struct tags control how encoding/json marshals and unmarshals:\n\n"
                    "  `json:\"name\"`           → use 'name' as the JSON key\n"
                    "  `json:\"name,omitempty\"` → omit field if zero value\n"
                    "  `json:\"-\"`              → never marshal this field\n\n"
                    "  data, _ := json.Marshal(Alert{Severity: \"high\"})\n"
                    "  // {\"severity\":\"high\"}\n"
                    "  // 'msg' omitted because Message is empty and has omitempty"
                ),
                "options": [
                    "They are comments — ignored by the compiler",
                    "They define the JSON field names and serialization behavior",
                    "They set default values for the struct fields",
                    "They validate the struct fields at compile time",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Struct tags are metadata that libraries (like encoding/json) read at runtime.",
                    "The json tag controls the key name and behaviors like omitempty.",
                ],
            },
            {
                "id": "go_os_env",
                "type": "quiz",
                "title": "Environment Variables",
                "question": (
                    "How do you read an environment variable in Go with a fallback default?\n\n"
                    "  port := ???"
                ),
                "lesson": (
                    "The os package provides environment variable access:\n\n"
                    "  os.Getenv(\"PORT\")              // returns \"\" if not set\n"
                    "  os.LookupEnv(\"PORT\")           // returns (value, bool)\n\n"
                    "Common pattern with fallback:\n"
                    "  port := os.Getenv(\"PORT\")\n"
                    "  if port == \"\" {\n"
                    "      port = \"8080\"\n"
                    "  }\n\n"
                    "Or use LookupEnv for the comma-ok idiom."
                ),
                "options": [
                    "env.Get(\"PORT\") with a default parameter",
                    "os.Getenv(\"PORT\") — returns empty string if unset, then check and default",
                    "system.environ[\"PORT\"]",
                    "config.ReadEnv(\"PORT\", \"8080\")",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The os package handles environment variables.",
                    "os.Getenv returns empty string if not set — you check and set a default yourself.",
                ],
            },
            {
                "id": "go_testing",
                "type": "quiz",
                "title": "Writing Tests",
                "question": (
                    "What naming convention does Go require for test functions?\n\n"
                    "  // In scanner_test.go\n"
                    "  func ???(t *testing.T) { ... }"
                ),
                "lesson": (
                    "Go test conventions:\n\n"
                    "  - File: xxx_test.go (suffix _test.go)\n"
                    "  - Function: TestXxx(t *testing.T) (prefix Test, capital X)\n"
                    "  - Run: go test ./...\n\n"
                    "  func TestScanPort(t *testing.T) {\n"
                    "      result := scanPort(\"localhost\", 8080)\n"
                    "      if !result.Open {\n"
                    "          t.Errorf(\"expected port 8080 open, got closed\")\n"
                    "      }\n"
                    "  }\n\n"
                    "No assertion library needed — t.Error, t.Fatal, t.Log."
                ),
                "options": [
                    "test_scan_port(t *testing.T)",
                    "TestScanPort(t *testing.T) — prefix Test with capital letter",
                    "ScanPortTest(t *testing.T)",
                    "func test(name string, t *testing.T)",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The function must start with 'Test' followed by a capital letter.",
                    "Go's test runner uses this naming convention to discover test functions.",
                ],
            },
            {
                "id": "go_context",
                "type": "quiz",
                "title": "Context Package",
                "question": (
                    "What is context.Context used for?\n\n"
                    "  func fetchData(ctx context.Context, url string) ([]byte, error) {\n"
                    "      req, _ := http.NewRequestWithContext(ctx, \"GET\", url, nil)\n"
                    "      // ...\n"
                    "  }"
                ),
                "lesson": (
                    "context.Context carries deadlines, cancellation signals, and\n"
                    "request-scoped values across API boundaries and goroutines.\n\n"
                    "  ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)\n"
                    "  defer cancel()\n\n"
                    "  // Pass ctx to downstream calls\n"
                    "  data, err := fetchData(ctx, url)\n\n"
                    "Convention: ctx is always the first parameter.\n"
                    "When the context is cancelled, <-ctx.Done() becomes readable."
                ),
                "options": [
                    "Storing database connections",
                    "Carrying deadlines, cancellation signals, and request-scoped values",
                    "Managing goroutine thread pools",
                    "Defining dependency injection containers",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Context is about lifecycle: when should this operation stop?",
                    "Deadlines, cancellation, and request-scoped metadata — that's context.",
                ],
            },
            {
                "id": "go_io_reader",
                "type": "quiz",
                "title": "io.Reader Interface",
                "question": (
                    "What makes io.Reader one of Go's most powerful interfaces?\n\n"
                    "  type Reader interface {\n"
                    "      Read(p []byte) (n int, err error)\n"
                    "  }"
                ),
                "lesson": (
                    "io.Reader is a single-method interface — and it's everywhere:\n\n"
                    "  os.File, bytes.Buffer, strings.Reader, http.Request.Body,\n"
                    "  gzip.Reader, crypto/cipher.StreamReader, net.Conn...\n\n"
                    "Because it's one method, any type can implement it.\n"
                    "Functions that accept io.Reader work with files, HTTP bodies,\n"
                    "compressed streams, encrypted data — anything.\n"
                    "This is the power of small interfaces in Go."
                ),
                "options": [
                    "It can only read files from disk",
                    "It's a single method that dozens of types implement, enabling universal composability",
                    "It automatically handles buffering and caching",
                    "It provides concurrent read access to shared data",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "One method, maximum composability.",
                    "Any type with a Read method satisfies io.Reader — files, buffers, network connections...",
                ],
            },
        ],
    },

    # ── ZONE 7: GO MODULES ─────────────────────────────────────────────
    "go_modules": {
        "id": "go_modules",
        "name": "The Module Registry",
        "subtitle": "go.mod, go.sum, Versioning, Dependencies & Private Modules",
        "color": "red",
        "icon": "📦",
        "commands": ["go mod init", "go mod tidy", "go get", "go mod vendor"],
        "challenges": [
            {
                "id": "go_mod_init",
                "type": "quiz",
                "title": "Initializing a Module",
                "question": (
                    "What does `go mod init` create?\n\n"
                    "  $ go mod init github.com/nexus-corp/scanner"
                ),
                "lesson": (
                    "go mod init creates a go.mod file — the module's manifest:\n\n"
                    "  module github.com/nexus-corp/scanner\n\n"
                    "  go 1.22\n\n"
                    "  require (\n"
                    "      github.com/sirupsen/logrus v1.9.3\n"
                    "  )\n\n"
                    "The module path (github.com/nexus-corp/scanner) is used for\n"
                    "imports and must match the repository URL for public modules."
                ),
                "options": [
                    "A Makefile for building the project",
                    "A go.mod file defining the module path and dependencies",
                    "A main.go file with a starter template",
                    "A .gitignore file for Go projects",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "go mod init creates the module definition file.",
                    "go.mod tracks the module name, Go version, and all dependencies.",
                ],
            },
            {
                "id": "go_mod_tidy",
                "type": "quiz",
                "title": "go mod tidy",
                "question": "What does `go mod tidy` do?",
                "lesson": (
                    "go mod tidy synchronizes go.mod and go.sum with your code:\n\n"
                    "  - Adds missing dependencies that your code imports\n"
                    "  - Removes unused dependencies\n"
                    "  - Updates go.sum with checksums\n\n"
                    "Run it after adding/removing imports, or when go.mod is out\n"
                    "of sync. It's the 'make everything consistent' command."
                ),
                "options": [
                    "Formats all Go source files",
                    "Adds missing and removes unused dependencies from go.mod",
                    "Runs all tests in the module",
                    "Compiles the module and reports errors",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Think 'tidy up' — make go.mod match what the code actually uses.",
                    "It both adds what's missing and removes what's unused.",
                ],
            },
            {
                "id": "go_sum_purpose",
                "type": "quiz",
                "title": "go.sum Purpose",
                "question": "What is the purpose of the go.sum file?",
                "lesson": (
                    "go.sum contains cryptographic checksums for every dependency\n"
                    "version used by the module:\n\n"
                    "  github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9...\n"
                    "  github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLo...\n\n"
                    "Purpose: supply chain security. If a dependency's checksum\n"
                    "doesn't match, the build fails. This prevents tampered or\n"
                    "compromised dependencies from being used."
                ),
                "options": [
                    "Stores the total size of all dependencies",
                    "Contains cryptographic checksums for dependency integrity verification",
                    "Lists all transitive dependencies for documentation",
                    "Caches compiled dependency binaries",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "sum → checksum. It's about verifying that dependencies haven't been tampered with.",
                    "If a checksum doesn't match what's in go.sum, the build fails.",
                ],
            },
            {
                "id": "go_semver",
                "type": "quiz",
                "title": "Semantic Versioning",
                "question": (
                    "In Go modules, what does a major version bump (v1 → v2) require?\n\n"
                    "  require github.com/nexus-corp/api/v2 v2.1.0"
                ),
                "lesson": (
                    "Go enforces semantic import versioning:\n\n"
                    "  v0.x.x / v1.x.x → import \"github.com/org/pkg\"\n"
                    "  v2.x.x+         → import \"github.com/org/pkg/v2\"\n\n"
                    "Major version changes MUST be reflected in the import path.\n"
                    "This means v1 and v2 can coexist in the same build —\n"
                    "they're treated as different packages."
                ),
                "options": [
                    "Nothing — just update the version number",
                    "The import path must include the major version suffix (/v2)",
                    "A new repository must be created",
                    "All dependents must be notified via go.sum",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Go makes breaking changes explicit in the import path.",
                    "v2+ modules must have /v2, /v3 etc. in their module path.",
                ],
            },
            {
                "id": "go_private_modules",
                "type": "quiz",
                "title": "Private Modules",
                "question": "How do you tell Go to bypass the public module proxy for private repositories?",
                "lesson": (
                    "By default, Go fetches modules through proxy.golang.org.\n"
                    "For private repos, set GONOSUMDB and GOPRIVATE:\n\n"
                    "  go env -w GOPRIVATE=github.com/nexus-corp/*\n\n"
                    "This tells Go:\n"
                    "  - Don't use the public proxy for these modules\n"
                    "  - Don't check the public sum database\n"
                    "  - Fetch directly from the source (needs auth)\n\n"
                    "In CI, configure git credentials or use GONOSUMDB + GOPROXY."
                ),
                "options": [
                    "Set GOPRIVATE environment variable with the module path pattern",
                    "Add a 'private: true' field to go.mod",
                    "Use go get --private to fetch private modules",
                    "Host a local copy and use replace directives",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "It's an environment variable that tells Go which modules are private.",
                    "GOPRIVATE accepts glob patterns like github.com/your-org/*",
                ],
            },
        ],
    },

    # ── ZONE 8: GO PATTERNS ────────────────────────────────────────────
    "go_patterns": {
        "id": "go_patterns",
        "name": "The Pattern Forge",
        "subtitle": "Error Wrapping, Middleware, DI & Table-Driven Tests",
        "color": "bright_cyan",
        "icon": "🔧",
        "commands": ["fmt.Errorf", "errors.Is", "errors.As", "t.Run"],
        "challenges": [
            {
                "id": "go_error_wrapping",
                "type": "quiz",
                "title": "Error Wrapping",
                "question": (
                    "What does the %w verb do in fmt.Errorf?\n\n"
                    "  return fmt.Errorf(\"scan failed for %s: %w\", target, err)"
                ),
                "lesson": (
                    "%w wraps the original error inside a new error with added context:\n\n"
                    "  return fmt.Errorf(\"scan failed: %w\", err)\n\n"
                    "The wrapped error can be inspected later:\n"
                    "  errors.Is(err, os.ErrNotExist)  // checks the chain\n"
                    "  errors.As(err, &pathErr)         // extracts a specific type\n\n"
                    "Use %w (not %v) when callers need to inspect the underlying error.\n"
                    "Use %v when you want to hide the implementation detail."
                ),
                "options": [
                    "Formats the error as a string (same as %v)",
                    "Wraps the original error, preserving it for errors.Is/As inspection",
                    "Writes the error to a log file",
                    "Converts the error to a warning",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "%w is special — it wraps rather than just formatting.",
                    "Wrapping preserves the error chain so callers can use errors.Is() and errors.As().",
                ],
            },
            {
                "id": "go_errors_is",
                "type": "quiz",
                "title": "errors.Is vs errors.As",
                "question": (
                    "When should you use errors.Is() vs errors.As()?\n\n"
                    "  if errors.Is(err, os.ErrPermission) { ... }\n"
                    "  var pathErr *os.PathError\n"
                    "  if errors.As(err, &pathErr) { ... }"
                ),
                "lesson": (
                    "errors.Is() checks if any error in the chain matches a specific value:\n"
                    "  errors.Is(err, os.ErrNotExist)  // 'is this a not-found error?'\n\n"
                    "errors.As() checks if any error in the chain matches a specific type\n"
                    "and extracts it:\n"
                    "  var pe *os.PathError\n"
                    "  if errors.As(err, &pe) {\n"
                    "      fmt.Println(pe.Path)  // access type-specific fields\n"
                    "  }\n\n"
                    "Is = value comparison. As = type extraction."
                ),
                "options": [
                    "They are interchangeable — both check error types",
                    "Is checks for a specific error value; As extracts a specific error type",
                    "Is is for wrapped errors; As is for unwrapped errors",
                    "Is returns a boolean; As returns the error string",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Is = 'is this the same error?' As = 'is this the same kind of error?'",
                    "errors.As lets you extract and use the concrete error type's fields.",
                ],
            },
            {
                "id": "go_middleware",
                "type": "quiz",
                "title": "HTTP Middleware Pattern",
                "question": (
                    "What pattern does this function implement?\n\n"
                    "  func logging(next http.Handler) http.Handler {\n"
                    "      return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n"
                    "          log.Printf(\"%s %s\", r.Method, r.URL.Path)\n"
                    "          next.ServeHTTP(w, r)\n"
                    "      })\n"
                    "  }"
                ),
                "lesson": (
                    "HTTP middleware in Go wraps a handler with additional behavior:\n\n"
                    "  func middleware(next http.Handler) http.Handler\n\n"
                    "Common middleware: logging, authentication, CORS, rate limiting,\n"
                    "request ID injection, panic recovery.\n\n"
                    "Chain them:\n"
                    "  handler := logging(auth(rateLimit(appHandler)))\n"
                    "  http.ListenAndServe(\":8080\", handler)"
                ),
                "options": [
                    "Decorator pattern — wraps an object to add behavior",
                    "HTTP middleware — wraps a handler to add cross-cutting behavior",
                    "Observer pattern — notifies listeners of HTTP events",
                    "Factory pattern — creates new handlers dynamically",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "It takes a handler, wraps it, and returns a new handler.",
                    "Middleware adds behavior (logging) before/after passing to the next handler.",
                ],
            },
            {
                "id": "go_dependency_injection",
                "type": "quiz",
                "title": "Dependency Injection",
                "question": (
                    "Why does this constructor accept an interface instead of a concrete type?\n\n"
                    "  func NewAuditService(store AuditStore, logger Logger) *AuditService {\n"
                    "      return &AuditService{store: store, logger: logger}\n"
                    "  }"
                ),
                "lesson": (
                    "Accepting interfaces instead of concrete types enables:\n\n"
                    "  - Testability: pass a mock AuditStore in tests\n"
                    "  - Flexibility: swap implementations without changing the service\n"
                    "  - Decoupling: the service doesn't depend on a specific database\n\n"
                    "Go proverb: 'Accept interfaces, return structs.'\n\n"
                    "In tests:\n"
                    "  svc := NewAuditService(&mockStore{}, &mockLogger{})\n"
                    "No DI framework needed — just constructors and interfaces."
                ),
                "options": [
                    "To make the code more complex and enterprise-grade",
                    "To allow different implementations and easy testing with mocks",
                    "Because Go requires all function parameters to be interfaces",
                    "To improve runtime performance through dynamic dispatch",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Think about what happens when you need to test this function.",
                    "With interfaces, you can pass mock implementations for testing.",
                ],
            },
            {
                "id": "go_table_tests",
                "type": "quiz",
                "title": "Table-Driven Tests",
                "question": (
                    "What pattern does this test use?\n\n"
                    "  func TestValidateIP(t *testing.T) {\n"
                    "      tests := []struct {\n"
                    "          name  string\n"
                    "          input string\n"
                    "          want  bool\n"
                    "      }{\n"
                    "          {\"valid IPv4\", \"192.168.1.1\", true},\n"
                    "          {\"empty\", \"\", false},\n"
                    "          {\"invalid\", \"999.999.999.999\", false},\n"
                    "      }\n"
                    "      for _, tt := range tests {\n"
                    "          t.Run(tt.name, func(t *testing.T) {\n"
                    "              got := validateIP(tt.input)\n"
                    "              if got != tt.want {\n"
                    "                  t.Errorf(\"validateIP(%q) = %v, want %v\", tt.input, got, tt.want)\n"
                    "              }\n"
                    "          })\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Table-driven tests are Go's idiomatic testing pattern:\n\n"
                    "  1. Define a slice of test cases (the 'table')\n"
                    "  2. Each case has a name, inputs, and expected outputs\n"
                    "  3. Range over the table, calling t.Run for each case\n\n"
                    "Benefits:\n"
                    "  - Easy to add new cases (one line per case)\n"
                    "  - Each subtest has a name (go test -run TestValidateIP/valid_IPv4)\n"
                    "  - Subtests can run in parallel with t.Parallel()"
                ),
                "options": [
                    "Parameterized test — test cases defined in a table, iterated with t.Run",
                    "Benchmark test — measures performance of validateIP",
                    "Fuzz test — generates random inputs for validateIP",
                    "Integration test — tests validateIP against a live network",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "A slice of structs defines all test cases — that's the 'table.'",
                    "t.Run creates named subtests — each row in the table becomes its own test.",
                ],
            },
            {
                "id": "go_functional_options",
                "type": "quiz",
                "title": "Functional Options Pattern",
                "question": (
                    "What problem does this pattern solve?\n\n"
                    "  type Option func(*Server)\n\n"
                    "  func WithPort(p int) Option {\n"
                    "      return func(s *Server) { s.port = p }\n"
                    "  }\n\n"
                    "  func NewServer(opts ...Option) *Server {\n"
                    "      s := &Server{port: 8080}\n"
                    "      for _, opt := range opts {\n"
                    "          opt(s)\n"
                    "      }\n"
                    "      return s\n"
                    "  }"
                ),
                "lesson": (
                    "The functional options pattern provides clean, extensible configuration:\n\n"
                    "  srv := NewServer(\n"
                    "      WithPort(9090),\n"
                    "      WithTimeout(30 * time.Second),\n"
                    "      WithLogger(logger),\n"
                    "  )\n\n"
                    "Benefits over config structs:\n"
                    "  - Sensible defaults (no zero-value confusion)\n"
                    "  - Self-documenting (each option is a named function)\n"
                    "  - Backward-compatible (new options don't break existing callers)\n"
                    "  - Variadic — pass zero or many options"
                ),
                "options": [
                    "It replaces Go's lack of default function parameters with composable option functions",
                    "It implements the observer pattern for server events",
                    "It creates a builder pattern for SQL queries",
                    "It provides runtime type checking for server configuration",
                ],
                "answer": "a",
                "xp": 40,
                "hints": [
                    "Go doesn't have default parameters or method overloading.",
                    "Each With... function returns a closure that configures one aspect of the server.",
                ],
            },
        ],
    },
}
