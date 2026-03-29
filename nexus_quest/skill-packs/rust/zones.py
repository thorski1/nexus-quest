"""
zones.py — Rust zones and challenges for Rust Forge.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "rust_basics",
    "ownership",
    "enums_and_matching",
    "structs_and_traits",
    "error_handling",
    "collections",
    "concurrency",
    "cargo_and_ecosystem",
]

ZONES = {
    # ── ZONE 1: RUST BASICS ──────────────────────────────────────────────
    "rust_basics": {
        "id": "rust_basics",
        "name": "The Immutable Core",
        "subtitle": "Variables, Types, Functions, let/mut & Shadowing",
        "color": "red",
        "icon": "🦀",
        "commands": ["rustc", "cargo run", "cargo build"],
        "challenges": [
            {
                "id": "rust_immutable_default",
                "type": "quiz",
                "title": "Immutable by Default",
                "question": (
                    "What happens when you try to compile this Rust code?\n\n"
                    "  fn main() {\n"
                    "      let x = 5;\n"
                    "      x = 10;\n"
                    "      println!(\"{x}\");\n"
                    "  }"
                ),
                "lesson": (
                    "In Rust, variables are immutable by default. Once a value is\n"
                    "bound with `let`, it cannot be reassigned unless you explicitly\n"
                    "declare it mutable with `let mut`:\n\n"
                    "  let mut x = 5;\n"
                    "  x = 10;  // OK — x is mutable\n\n"
                    "This is a core safety feature. The compiler catches accidental\n"
                    "mutation at compile time, not at runtime."
                ),
                "options": [
                    "It prints 10",
                    "It prints 5",
                    "Compile error — cannot assign twice to immutable variable",
                    "Runtime panic",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Rust variables are immutable by default — no `mut` keyword here.",
                    "The compiler will refuse to compile code that reassigns an immutable binding.",
                ],
            },
            {
                "id": "rust_let_mut",
                "type": "quiz",
                "title": "Mutable Variables",
                "question": (
                    "Which keyword makes a variable mutable in Rust?\n\n"
                    "  fn main() {\n"
                    "      let ___ x = 5;\n"
                    "      x = 10;\n"
                    "  }"
                ),
                "lesson": (
                    "The `mut` keyword explicitly opts into mutability:\n\n"
                    "  let mut counter = 0;\n"
                    "  counter += 1;  // allowed\n\n"
                    "Rust makes mutability an intentional choice, not the default.\n"
                    "This helps the compiler reason about data flow and prevents\n"
                    "entire categories of bugs."
                ),
                "options": [
                    "var",
                    "mut",
                    "mutable",
                    "ref",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a three-letter keyword placed between `let` and the variable name.",
                    "Short for 'mutable' — `let mut x = 5;`",
                ],
            },
            {
                "id": "rust_shadowing",
                "type": "quiz",
                "title": "Variable Shadowing",
                "question": (
                    "What does this code print?\n\n"
                    "  fn main() {\n"
                    "      let x = 5;\n"
                    "      let x = x + 1;\n"
                    "      let x = x * 2;\n"
                    "      println!(\"{x}\");\n"
                    "  }"
                ),
                "lesson": (
                    "Rust allows shadowing — declaring a new variable with the same\n"
                    "name using `let` again. Each `let` creates a NEW binding:\n\n"
                    "  let x = 5;       // x = 5\n"
                    "  let x = x + 1;   // x = 6 (new binding, old x is shadowed)\n"
                    "  let x = x * 2;   // x = 12\n\n"
                    "Unlike `mut`, shadowing can even change the type:\n"
                    "  let spaces = \"   \";       // &str\n"
                    "  let spaces = spaces.len(); // usize — different type!"
                ),
                "options": [
                    "5",
                    "6",
                    "12",
                    "Compile error — cannot redeclare x",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Each `let x =` creates a brand new binding — trace the math step by step.",
                    "5 → 5+1=6 → 6*2=12",
                ],
            },
            {
                "id": "rust_type_inference",
                "type": "quiz",
                "title": "Type Inference",
                "question": (
                    "What type does the compiler infer for `x`?\n\n"
                    "  let x = 42;"
                ),
                "lesson": (
                    "Rust has strong type inference. Integer literals default to `i32`\n"
                    "and floating-point literals default to `f64`:\n\n"
                    "  let x = 42;      // i32\n"
                    "  let y = 3.14;    // f64\n"
                    "  let z: u8 = 42;  // u8 (explicit annotation)\n\n"
                    "You can always annotate types explicitly, but the compiler is\n"
                    "usually smart enough to figure it out from context."
                ),
                "options": [
                    "i64",
                    "i32",
                    "u32",
                    "int",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Rust defaults integer literals to a signed 32-bit type.",
                    "The default integer type is i32, not i64.",
                ],
            },
            {
                "id": "rust_functions",
                "type": "quiz",
                "title": "Function Return Values",
                "question": (
                    "What does this function return?\n\n"
                    "  fn add(a: i32, b: i32) -> i32 {\n"
                    "      a + b\n"
                    "  }"
                ),
                "lesson": (
                    "In Rust, the last expression in a function body is the return\n"
                    "value — no `return` keyword needed (no semicolon!):\n\n"
                    "  fn add(a: i32, b: i32) -> i32 {\n"
                    "      a + b   // expression — returned implicitly\n"
                    "  }\n\n"
                    "Adding a semicolon turns it into a statement that returns ():\n"
                    "  a + b;  // returns (), NOT the sum — compile error!"
                ),
                "options": [
                    "Nothing — there's no return statement",
                    "The sum of a + b (implicit return of last expression)",
                    "A tuple (a, b)",
                    "Compile error — missing return keyword",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Notice there's no semicolon after `a + b` — that makes it an expression.",
                    "Rust returns the last expression in a block without needing `return`.",
                ],
            },
            {
                "id": "rust_const_vs_let",
                "type": "quiz",
                "title": "Constants vs let Bindings",
                "question": (
                    "Which statement about `const` in Rust is TRUE?\n\n"
                    "  const MAX_POINTS: u32 = 100_000;"
                ),
                "lesson": (
                    "Constants in Rust differ from `let` bindings:\n\n"
                    "  - `const` values MUST have a type annotation\n"
                    "  - They are set at compile time, not runtime\n"
                    "  - They cannot be shadowed or made `mut`\n"
                    "  - By convention, they use SCREAMING_SNAKE_CASE\n"
                    "  - They can be declared in any scope, including global\n\n"
                    "  const PI: f64 = 3.14159265;\n"
                    "  let x = 5;  // this is a runtime binding, not a const"
                ),
                "options": [
                    "const values can be computed at runtime",
                    "const values don't need a type annotation",
                    "const values must have an explicit type annotation",
                    "const values can be shadowed like let bindings",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Look at the declaration — the type `: u32` is required, not optional.",
                    "Unlike `let`, `const` always requires an explicit type.",
                ],
            },
        ],
    },

    # ── ZONE 2: OWNERSHIP ────────────────────────────────────────────────
    "ownership": {
        "id": "ownership",
        "name": "The Borrow Checker",
        "subtitle": "Ownership, Borrowing, References & Lifetimes",
        "color": "yellow",
        "icon": "🔐",
        "commands": ["rustc --explain", "cargo check"],
        "challenges": [
            {
                "id": "rust_ownership_move",
                "type": "quiz",
                "title": "Ownership Move",
                "question": (
                    "What happens when you compile this code?\n\n"
                    "  fn main() {\n"
                    "      let s1 = String::from(\"hello\");\n"
                    "      let s2 = s1;\n"
                    "      println!(\"{s1}\");\n"
                    "  }"
                ),
                "lesson": (
                    "Rust's ownership system: each value has exactly ONE owner.\n"
                    "When you assign `s2 = s1`, ownership MOVES to s2. s1 is\n"
                    "invalidated — you can't use it anymore:\n\n"
                    "  let s1 = String::from(\"hello\");\n"
                    "  let s2 = s1;  // s1 moved to s2\n"
                    "  // s1 is now invalid — using it is a compile error\n\n"
                    "This prevents double-free bugs. Only one variable can\n"
                    "drop (free) heap memory."
                ),
                "options": [
                    "Prints \"hello\"",
                    "Prints \"hello\" twice",
                    "Compile error — value borrowed after move",
                    "Runtime error — double free",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "String is a heap-allocated type — assignment moves ownership.",
                    "After `let s2 = s1;`, s1 no longer owns the data.",
                ],
            },
            {
                "id": "rust_copy_trait",
                "type": "quiz",
                "title": "Copy vs Move",
                "question": (
                    "Why does this code compile without error?\n\n"
                    "  fn main() {\n"
                    "      let x = 5;\n"
                    "      let y = x;\n"
                    "      println!(\"{x} {y}\");\n"
                    "  }"
                ),
                "lesson": (
                    "Types that implement the `Copy` trait are copied, not moved.\n"
                    "Simple stack-allocated types like integers, bools, floats, and\n"
                    "chars implement Copy:\n\n"
                    "  let x = 5;   // i32 implements Copy\n"
                    "  let y = x;   // x is COPIED, not moved\n"
                    "  // both x and y are valid\n\n"
                    "Heap types like String and Vec do NOT implement Copy —\n"
                    "they MOVE instead."
                ),
                "options": [
                    "Integers are stored on the heap",
                    "Integers implement the Copy trait — they are copied, not moved",
                    "Rust ignores ownership rules for primitives",
                    "The compiler automatically clones integers",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Simple, fixed-size types that live on the stack have a special trait.",
                    "The `Copy` trait tells Rust to duplicate the bits instead of moving.",
                ],
            },
            {
                "id": "rust_borrow_immutable",
                "type": "quiz",
                "title": "Immutable Borrowing",
                "question": (
                    "What does `&` mean in this function signature?\n\n"
                    "  fn calculate_length(s: &String) -> usize {\n"
                    "      s.len()\n"
                    "  }"
                ),
                "lesson": (
                    "The `&` creates an immutable reference — a borrow:\n\n"
                    "  let s = String::from(\"hello\");\n"
                    "  let len = calculate_length(&s);  // borrow s\n"
                    "  println!(\"{s}\");  // s is still valid!\n\n"
                    "Borrowing lets you use a value without taking ownership.\n"
                    "You can have UNLIMITED immutable references (&T) at the\n"
                    "same time, but they cannot modify the data."
                ),
                "options": [
                    "A pointer that can be null",
                    "An immutable reference — borrows without taking ownership",
                    "A copy of the String",
                    "A mutable reference to the String",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "& means 'reference' — it borrows the value without moving it.",
                    "Without `mut`, the reference is read-only.",
                ],
            },
            {
                "id": "rust_borrow_mutable",
                "type": "quiz",
                "title": "Mutable Borrowing Rules",
                "question": (
                    "What is the core rule for mutable references in Rust?\n\n"
                    "  fn main() {\n"
                    "      let mut s = String::from(\"hello\");\n"
                    "      let r1 = &mut s;\n"
                    "      let r2 = &mut s;  // ???\n"
                    "      println!(\"{r1} {r2}\");\n"
                    "  }"
                ),
                "lesson": (
                    "Rust's borrowing rules prevent data races at compile time:\n\n"
                    "  1. You can have EITHER:\n"
                    "     - One mutable reference (&mut T), OR\n"
                    "     - Any number of immutable references (&T)\n"
                    "  2. But NEVER both at the same time.\n\n"
                    "This code fails because two &mut references to the same\n"
                    "data exist simultaneously. The borrow checker catches this\n"
                    "at compile time — no runtime cost."
                ),
                "options": [
                    "You can have unlimited mutable references",
                    "You can have at most one mutable reference at a time",
                    "Mutable references are only checked at runtime",
                    "You need unsafe to create mutable references",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Rust prevents data races — two writers at the same time is forbidden.",
                    "At most ONE &mut reference to a value can exist at any point.",
                ],
            },
            {
                "id": "rust_lifetime_basic",
                "type": "quiz",
                "title": "Lifetime Annotations",
                "question": (
                    "What do the `'a` annotations mean in this signature?\n\n"
                    "  fn longest<'a>(x: &'a str, y: &'a str) -> &'a str"
                ),
                "lesson": (
                    "Lifetime annotations tell the compiler how long references\n"
                    "are valid. `'a` means 'some lifetime':\n\n"
                    "  fn longest<'a>(x: &'a str, y: &'a str) -> &'a str\n\n"
                    "This says: the returned reference will be valid for at least\n"
                    "as long as BOTH input references are valid. The compiler uses\n"
                    "this to ensure you never get a dangling reference.\n\n"
                    "Lifetimes don't change how long data lives — they help the\n"
                    "compiler VERIFY that references are always valid."
                ),
                "options": [
                    "Generic type parameters for the function",
                    "The returned reference lives as long as both inputs",
                    "The function allocates memory with lifetime 'a",
                    "The references are mutable",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The 'a appears on both inputs AND the return type.",
                    "Lifetime annotations constrain how long the returned reference is valid.",
                ],
            },
            {
                "id": "rust_ownership_three_rules",
                "type": "quiz",
                "title": "The Three Ownership Rules",
                "question": (
                    "Which of these is NOT one of Rust's ownership rules?\n\n"
                    "  1. Each value has exactly one owner\n"
                    "  2. There can only be one owner at a time\n"
                    "  3. When the owner goes out of scope, the value is dropped"
                ),
                "lesson": (
                    "Rust's three ownership rules:\n\n"
                    "  1. Each value in Rust has an owner.\n"
                    "  2. There can only be one owner at a time.\n"
                    "  3. When the owner goes out of scope, the value is dropped.\n\n"
                    "These three rules replace garbage collection entirely.\n"
                    "No GC pauses, no reference counting overhead, no manual\n"
                    "free() calls. The compiler inserts drop() automatically\n"
                    "at the right place."
                ),
                "options": [
                    "Each value has exactly one owner",
                    "When the owner goes out of scope, the value is dropped",
                    "Values are garbage collected when no references remain",
                    "There can only be one owner at a time",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Rust does NOT have a garbage collector.",
                    "One of these options describes GC behavior, not ownership.",
                ],
            },
        ],
    },

    # ── ZONE 3: ENUMS AND PATTERN MATCHING ───────────────────────────────
    "enums_and_matching": {
        "id": "enums_and_matching",
        "name": "The Pattern Lattice",
        "subtitle": "enum, Option<T>, Result<T,E> & Pattern Matching",
        "color": "magenta",
        "icon": "🔷",
        "commands": ["match", "if let", "while let"],
        "challenges": [
            {
                "id": "rust_enum_basics",
                "type": "quiz",
                "title": "Enum Definition",
                "question": (
                    "What makes Rust enums more powerful than C/Java enums?\n\n"
                    "  enum Message {\n"
                    "      Quit,\n"
                    "      Move { x: i32, y: i32 },\n"
                    "      Write(String),\n"
                    "      ChangeColor(i32, i32, i32),\n"
                    "  }"
                ),
                "lesson": (
                    "Rust enums are algebraic data types — each variant can hold\n"
                    "different data:\n\n"
                    "  Quit                    — no data\n"
                    "  Move { x: i32, y: i32 } — named fields (struct-like)\n"
                    "  Write(String)           — tuple variant\n"
                    "  ChangeColor(i32,i32,i32) — multiple values\n\n"
                    "This is far more powerful than enums in C or Java, which are\n"
                    "just named integer constants. Rust enums can model complex\n"
                    "state machines and tagged unions."
                ),
                "options": [
                    "Rust enums can only hold integers",
                    "Each variant can hold different types and amounts of data",
                    "Rust enums are exactly like C enums",
                    "Enum variants cannot have named fields",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Look at the variants — Quit has no data, Move has named fields, Write has a String.",
                    "Each variant is like a mini-struct with its own shape.",
                ],
            },
            {
                "id": "rust_option_type",
                "type": "quiz",
                "title": "Option<T> — No More Null",
                "question": (
                    "What is `Option<T>` in Rust, and why does Rust have no null?\n\n"
                    "  fn find_user(id: u32) -> Option<String> {\n"
                    "      if id == 1 {\n"
                    "          Some(String::from(\"Alice\"))\n"
                    "      } else {\n"
                    "          None\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Rust has no null. Instead, it uses `Option<T>`:\n\n"
                    "  enum Option<T> {\n"
                    "      Some(T),  // a value exists\n"
                    "      None,     // no value\n"
                    "  }\n\n"
                    "The compiler FORCES you to handle the None case before you\n"
                    "can access the inner value. This eliminates null pointer\n"
                    "exceptions at compile time — the 'billion dollar mistake'."
                ),
                "options": [
                    "A nullable pointer like in C",
                    "An enum with Some(T) and None — Rust's replacement for null",
                    "A try-catch mechanism for missing values",
                    "A special type that automatically returns default values",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Option is an enum with exactly two variants.",
                    "Some wraps a value; None represents absence — and you must handle both.",
                ],
            },
            {
                "id": "rust_match_exhaustive",
                "type": "quiz",
                "title": "Match Exhaustiveness",
                "question": (
                    "Why won't this code compile?\n\n"
                    "  enum Coin { Penny, Nickel, Dime, Quarter }\n\n"
                    "  fn value(coin: Coin) -> u32 {\n"
                    "      match coin {\n"
                    "          Coin::Penny => 1,\n"
                    "          Coin::Nickel => 5,\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Rust's `match` is exhaustive — you must handle EVERY variant:\n\n"
                    "  match coin {\n"
                    "      Coin::Penny   => 1,\n"
                    "      Coin::Nickel  => 5,\n"
                    "      Coin::Dime    => 10,\n"
                    "      Coin::Quarter => 25,\n"
                    "  }\n\n"
                    "Or use a catch-all: `_ => 0`\n\n"
                    "The compiler ensures you never forget a case. This is\n"
                    "especially valuable when adding new variants to an enum —\n"
                    "every match will fail to compile until updated."
                ),
                "options": [
                    "match doesn't work with enums",
                    "Dime and Quarter are not handled — match must be exhaustive",
                    "The return type should be Option<u32>",
                    "You need a default: case like in C",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The enum has 4 variants but the match only covers 2.",
                    "Rust's match REQUIRES every possible variant to be handled.",
                ],
            },
            {
                "id": "rust_result_type",
                "type": "quiz",
                "title": "Result<T, E>",
                "question": (
                    "What are the two variants of `Result<T, E>`?\n\n"
                    "  fn parse_port(s: &str) -> Result<u16, String> {\n"
                    "      match s.parse::<u16>() {\n"
                    "          Ok(port) => Ok(port),\n"
                    "          Err(_) => Err(format!(\"Invalid port: {s}\")),\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Result<T, E> is Rust's error handling type:\n\n"
                    "  enum Result<T, E> {\n"
                    "      Ok(T),   // success with value T\n"
                    "      Err(E),  // failure with error E\n"
                    "  }\n\n"
                    "Like Option, the compiler forces you to handle both cases.\n"
                    "This replaces exceptions — no hidden control flow, no\n"
                    "uncaught errors crashing at runtime."
                ),
                "options": [
                    "Success and Failure",
                    "Ok(T) and Err(E)",
                    "Some(T) and None",
                    "Try(T) and Catch(E)",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Look at the code — the two variants are used explicitly.",
                    "Ok wraps the success value, Err wraps the error.",
                ],
            },
            {
                "id": "rust_if_let",
                "type": "quiz",
                "title": "if let Syntax",
                "question": (
                    "What does `if let` do in this code?\n\n"
                    "  let config_max = Some(3u8);\n"
                    "  if let Some(max) = config_max {\n"
                    "      println!(\"Max is {max}\");\n"
                    "  }"
                ),
                "lesson": (
                    "`if let` is syntactic sugar for a match that only cares\n"
                    "about one variant:\n\n"
                    "  // These are equivalent:\n"
                    "  if let Some(max) = config_max { ... }\n\n"
                    "  match config_max {\n"
                    "      Some(max) => { ... },\n"
                    "      _ => {},\n"
                    "  }\n\n"
                    "Use `if let` when you want to match one pattern and\n"
                    "ignore the rest. Less boilerplate than a full match."
                ),
                "options": [
                    "Declares a new variable named let",
                    "Matches one pattern and runs code if it matches, ignoring other variants",
                    "Creates a conditional variable assignment that might panic",
                    "Unwraps the Option, panicking on None",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a shorter way to match a single pattern.",
                    "`if let` avoids writing a full match when you only care about one variant.",
                ],
            },
        ],
    },

    # ── ZONE 4: STRUCTS AND TRAITS ───────────────────────────────────────
    "structs_and_traits": {
        "id": "structs_and_traits",
        "name": "The Trait Matrix",
        "subtitle": "Structs, impl Blocks, Traits, Derive & Generics",
        "color": "green",
        "icon": "🧬",
        "commands": ["impl", "trait", "derive", "where"],
        "challenges": [
            {
                "id": "rust_struct_def",
                "type": "quiz",
                "title": "Struct Definition",
                "question": (
                    "How do you create an instance of this struct?\n\n"
                    "  struct Server {\n"
                    "      host: String,\n"
                    "      port: u16,\n"
                    "      active: bool,\n"
                    "  }"
                ),
                "lesson": (
                    "Structs are created by specifying all fields:\n\n"
                    "  let srv = Server {\n"
                    "      host: String::from(\"0.0.0.0\"),\n"
                    "      port: 8080,\n"
                    "      active: true,\n"
                    "  };\n\n"
                    "Every field must be initialized — no default values unless\n"
                    "you implement the Default trait. Field order doesn't matter."
                ),
                "options": [
                    "Server.new(\"0.0.0.0\", 8080, true)",
                    "Server { host: String::from(\"0.0.0.0\"), port: 8080, active: true }",
                    "new Server(\"0.0.0.0\", 8080, true)",
                    "Server(host=\"0.0.0.0\", port=8080, active=true)",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Rust uses curly braces with field_name: value syntax.",
                    "There's no `new` keyword in Rust — you use StructName { ... }.",
                ],
            },
            {
                "id": "rust_impl_block",
                "type": "quiz",
                "title": "impl Blocks",
                "question": (
                    "What is `&self` in this method?\n\n"
                    "  impl Server {\n"
                    "      fn address(&self) -> String {\n"
                    "          format!(\"{}:{}\", self.host, self.port)\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Methods are defined in `impl` blocks. The first parameter\n"
                    "determines how the method accesses the struct:\n\n"
                    "  &self     — immutable borrow (read-only)\n"
                    "  &mut self — mutable borrow (can modify fields)\n"
                    "  self      — takes ownership (consumes the struct)\n\n"
                    "Associated functions (no self) are like static methods:\n"
                    "  fn new(host: String, port: u16) -> Server { ... }\n"
                    "  // called as Server::new(...)"
                ),
                "options": [
                    "A mutable reference to the struct instance",
                    "An immutable reference to the struct instance",
                    "A copy of the struct",
                    "A pointer that might be null",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "&self is shorthand for self: &Self — it borrows the instance.",
                    "The & means borrow, without `mut` it's read-only.",
                ],
            },
            {
                "id": "rust_traits",
                "type": "quiz",
                "title": "Trait Definition",
                "question": (
                    "What is a trait in Rust?\n\n"
                    "  trait Summary {\n"
                    "      fn summarize(&self) -> String;\n"
                    "  }\n\n"
                    "  impl Summary for Server {\n"
                    "      fn summarize(&self) -> String {\n"
                    "          format!(\"Server at {}\", self.address())\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Traits define shared behavior — similar to interfaces:\n\n"
                    "  trait Summary {\n"
                    "      fn summarize(&self) -> String;  // required method\n"
                    "  }\n\n"
                    "Any type can implement a trait. Unlike Go interfaces,\n"
                    "Rust traits are explicit — you must write `impl Trait for Type`.\n\n"
                    "Traits can have default implementations, associated types,\n"
                    "and can be used as generic bounds."
                ),
                "options": [
                    "A class that can be inherited",
                    "A collection of method signatures that types can implement",
                    "A module containing helper functions",
                    "An abstract struct with virtual methods",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Traits define behavior (methods) without defining data (fields).",
                    "Think of them as interfaces — a contract that types must fulfill.",
                ],
            },
            {
                "id": "rust_derive",
                "type": "quiz",
                "title": "Derive Macros",
                "question": (
                    "What does `#[derive(Debug, Clone, PartialEq)]` do?\n\n"
                    "  #[derive(Debug, Clone, PartialEq)]\n"
                    "  struct Config {\n"
                    "      name: String,\n"
                    "      retries: u32,\n"
                    "  }"
                ),
                "lesson": (
                    "The `derive` attribute auto-implements common traits:\n\n"
                    "  Debug       — enables {:?} formatting\n"
                    "  Clone       — enables .clone() deep copy\n"
                    "  PartialEq   — enables == comparison\n"
                    "  Hash        — enables use as HashMap key\n"
                    "  Default     — enables Type::default()\n"
                    "  Serialize/Deserialize — serde (external crate)\n\n"
                    "Derive generates the implementation automatically based\n"
                    "on the struct's fields. No boilerplate needed."
                ),
                "options": [
                    "Imports external crates named Debug, Clone, and PartialEq",
                    "Auto-generates trait implementations for the struct",
                    "Creates three new structs that extend Config",
                    "Marks the struct as immutable",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Derive is a macro that generates code at compile time.",
                    "It automatically implements the listed traits for the struct.",
                ],
            },
            {
                "id": "rust_generics",
                "type": "quiz",
                "title": "Generics with Trait Bounds",
                "question": (
                    "What does the trait bound `T: Display + Clone` mean?\n\n"
                    "  fn print_and_clone<T: Display + Clone>(item: &T) -> T {\n"
                    "      println!(\"{item}\");\n"
                    "      item.clone()\n"
                    "  }"
                ),
                "lesson": (
                    "Generics let you write code for any type T, while trait bounds\n"
                    "constrain what T can be:\n\n"
                    "  T: Display + Clone\n\n"
                    "This means T must implement BOTH Display AND Clone.\n"
                    "You can also use `where` clause for complex bounds:\n\n"
                    "  fn process<T>(item: &T) -> T\n"
                    "  where\n"
                    "      T: Display + Clone + Send,\n"
                    "  { ... }\n\n"
                    "Rust generics are monomorphized at compile time — zero runtime cost."
                ),
                "options": [
                    "T must be a subclass of Display and Clone",
                    "T must implement both the Display and Clone traits",
                    "T is either a Display type or a Clone type",
                    "T will automatically implement Display and Clone",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The + means 'and' — T must satisfy both trait requirements.",
                    "Trait bounds constrain the generic type to types that have certain behaviors.",
                ],
            },
            {
                "id": "rust_associated_fn",
                "type": "quiz",
                "title": "Associated Functions",
                "question": (
                    "How is `Server::new()` different from `srv.address()`?\n\n"
                    "  impl Server {\n"
                    "      fn new(host: String, port: u16) -> Self {\n"
                    "          Server { host, port, active: true }\n"
                    "      }\n"
                    "      fn address(&self) -> String {\n"
                    "          format!(\"{}:{}\", self.host, self.port)\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Functions in `impl` blocks come in two flavors:\n\n"
                    "  Associated function — no self parameter:\n"
                    "    fn new(host: String, port: u16) -> Self\n"
                    "    Called as: Server::new(...)\n\n"
                    "  Method — has self parameter:\n"
                    "    fn address(&self) -> String\n"
                    "    Called as: srv.address()\n\n"
                    "`Self` refers to the implementing type (Server here).\n"
                    "Convention: `new()` is the idiomatic constructor name."
                ),
                "options": [
                    "There is no difference",
                    "new() is an associated function (no self); address() is a method (&self)",
                    "new() is public and address() is private",
                    "new() returns a reference and address() returns a copy",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Look at the first parameter — one has &self, the other doesn't.",
                    "Associated functions use :: syntax, methods use . syntax.",
                ],
            },
        ],
    },

    # ── ZONE 5: ERROR HANDLING ───────────────────────────────────────────
    "error_handling": {
        "id": "error_handling",
        "name": "The Error Chain",
        "subtitle": "Result, ?, unwrap, Custom Errors & Error Crates",
        "color": "red",
        "icon": "⚠️",
        "commands": ["?", "unwrap()", "expect()", "thiserror", "anyhow"],
        "challenges": [
            {
                "id": "rust_question_mark",
                "type": "quiz",
                "title": "The ? Operator",
                "question": (
                    "What does the `?` operator do here?\n\n"
                    "  fn read_config(path: &str) -> Result<String, io::Error> {\n"
                    "      let content = fs::read_to_string(path)?;\n"
                    "      Ok(content.trim().to_string())\n"
                    "  }"
                ),
                "lesson": (
                    "The `?` operator is error propagation shorthand:\n\n"
                    "  fs::read_to_string(path)?  is equivalent to:\n\n"
                    "  match fs::read_to_string(path) {\n"
                    "      Ok(val) => val,\n"
                    "      Err(e) => return Err(e),  // early return!\n"
                    "  }\n\n"
                    "If the Result is Ok, unwrap the value and continue.\n"
                    "If Err, return the error from the current function immediately.\n"
                    "The function must return Result for ? to work."
                ),
                "options": [
                    "Ignores the error and returns a default value",
                    "Unwraps Ok values; on Err, returns the error from the function early",
                    "Converts the error to a panic",
                    "Logs the error and continues execution",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "? is shorthand for match + early return on Err.",
                    "On success it unwraps, on failure it propagates the error up.",
                ],
            },
            {
                "id": "rust_unwrap_expect",
                "type": "quiz",
                "title": "unwrap vs expect",
                "question": (
                    "What is the difference between these two calls?\n\n"
                    "  let port: u16 = \"8080\".parse().unwrap();\n"
                    "  let port: u16 = \"8080\".parse().expect(\"Invalid port\");"
                ),
                "lesson": (
                    "Both unwrap and expect panic on Err/None, but:\n\n"
                    "  .unwrap()  — panics with a generic error message\n"
                    "  .expect(\"msg\") — panics with YOUR custom message\n\n"
                    "In production code, prefer:\n"
                    "  1. Pattern matching or `?` operator (no panic)\n"
                    "  2. .expect() over .unwrap() (better error messages)\n"
                    "  3. .unwrap() only in tests or when you're 100% certain\n\n"
                    "  // Good practice:\n"
                    "  let port: u16 = env::var(\"PORT\")\n"
                    "      .expect(\"PORT must be set\")\n"
                    "      .parse()\n"
                    "      .expect(\"PORT must be a number\");"
                ),
                "options": [
                    "unwrap returns None; expect returns a default value",
                    "unwrap panics silently; expect panics with a custom message",
                    "unwrap is for Option; expect is for Result",
                    "They are identical in every way",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Both panic on failure — the difference is the error message.",
                    "expect() lets you provide a meaningful panic message.",
                ],
            },
            {
                "id": "rust_custom_errors",
                "type": "quiz",
                "title": "Custom Error Types",
                "question": (
                    "What trait must a custom error type implement?\n\n"
                    "  #[derive(Debug)]\n"
                    "  enum AppError {\n"
                    "      NotFound(String),\n"
                    "      ParseError(std::num::ParseIntError),\n"
                    "  }\n\n"
                    "  impl std::fmt::Display for AppError { ... }\n"
                    "  impl std::error::Error for AppError { ... }"
                ),
                "lesson": (
                    "Custom errors in Rust must implement:\n\n"
                    "  1. Debug  — for developer-facing output (usually #[derive])\n"
                    "  2. Display — for user-facing error message\n"
                    "  3. std::error::Error — the Error trait itself\n\n"
                    "The Error trait requires Debug + Display and optionally\n"
                    "provides `.source()` for error chaining.\n\n"
                    "Libraries like `thiserror` derive all of this automatically:\n"
                    "  #[derive(thiserror::Error, Debug)]\n"
                    "  enum AppError {\n"
                    "      #[error(\"not found: {0}\")]\n"
                    "      NotFound(String),\n"
                    "  }"
                ),
                "options": [
                    "Only Debug",
                    "Only Display",
                    "std::error::Error (which requires Debug + Display)",
                    "Serialize",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "The Error trait has supertraits — it requires other traits too.",
                    "std::error::Error requires both Debug and Display.",
                ],
            },
            {
                "id": "rust_thiserror",
                "type": "quiz",
                "title": "thiserror Crate",
                "question": (
                    "What does the `thiserror` crate do?\n\n"
                    "  #[derive(thiserror::Error, Debug)]\n"
                    "  enum ConfigError {\n"
                    "      #[error(\"File not found: {path}\")]\n"
                    "      NotFound { path: String },\n"
                    "      #[error(\"Parse error: {0}\")]\n"
                    "      ParseFailed(#[from] serde_json::Error),\n"
                    "  }"
                ),
                "lesson": (
                    "`thiserror` is a derive macro that generates Display and\n"
                    "Error implementations:\n\n"
                    "  #[error(\"...\")]    — generates Display\n"
                    "  #[from]            — generates From<T> for auto-conversion\n\n"
                    "This lets you use ? to automatically convert between error types.\n\n"
                    "`thiserror` is for libraries (structured errors).\n"
                    "`anyhow` is for applications (any error, easy propagation)."
                ),
                "options": [
                    "A runtime error handler that catches panics",
                    "A derive macro that generates Display and Error implementations",
                    "A logging framework for error messages",
                    "A replacement for Result with better performance",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Notice the #[derive(thiserror::Error)] — it's a derive macro.",
                    "It auto-generates the boilerplate for custom error types.",
                ],
            },
            {
                "id": "rust_anyhow",
                "type": "quiz",
                "title": "anyhow for Applications",
                "question": (
                    "When should you use `anyhow` instead of `thiserror`?\n\n"
                    "  use anyhow::{Context, Result};\n\n"
                    "  fn load_config() -> Result<Config> {\n"
                    "      let text = fs::read_to_string(\"config.toml\")\n"
                    "          .context(\"Failed to read config file\")?;\n"
                    "      let config: Config = toml::from_str(&text)\n"
                    "          .context(\"Failed to parse config\")?;\n"
                    "      Ok(config)\n"
                    "  }"
                ),
                "lesson": (
                    "anyhow vs thiserror:\n\n"
                    "  thiserror — for LIBRARIES\n"
                    "    - Define specific error types\n"
                    "    - Callers can match on variants\n\n"
                    "  anyhow — for APPLICATIONS\n"
                    "    - anyhow::Result<T> wraps any error\n"
                    "    - .context() adds human-readable messages\n"
                    "    - No need to define custom error types\n"
                    "    - Great for CLIs, servers, scripts\n\n"
                    "Rule of thumb: if someone else calls your code, use thiserror.\n"
                    "If your code is the final consumer, use anyhow."
                ),
                "options": [
                    "When writing a library that others will depend on",
                    "When writing an application where you want easy error propagation with context",
                    "When you need to catch panics",
                    "When you want to avoid using Result entirely",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "anyhow is for applications, thiserror is for libraries.",
                    "The .context() method adds a human-readable message to any error.",
                ],
            },
        ],
    },

    # ── ZONE 6: COLLECTIONS ──────────────────────────────────────────────
    "collections": {
        "id": "collections",
        "name": "The Data Forge",
        "subtitle": "Vec, HashMap, String vs &str, Iterators & Closures",
        "color": "blue",
        "icon": "📦",
        "commands": ["vec![]", "HashMap::new()", ".iter()", ".collect()"],
        "challenges": [
            {
                "id": "rust_vec",
                "type": "quiz",
                "title": "Vec<T> — Dynamic Arrays",
                "question": (
                    "What does this code produce?\n\n"
                    "  let mut nums = vec![1, 2, 3];\n"
                    "  nums.push(4);\n"
                    "  println!(\"{:?}\", nums);"
                ),
                "lesson": (
                    "Vec<T> is Rust's growable array — like ArrayList or Python's list:\n\n"
                    "  let mut v = vec![1, 2, 3];  // macro shorthand\n"
                    "  let mut v = Vec::new();      // empty Vec\n\n"
                    "  v.push(4);      // append\n"
                    "  v.pop();        // remove last (returns Option<T>)\n"
                    "  v[0];           // index access (panics on out-of-bounds)\n"
                    "  v.get(0);       // safe access (returns Option<&T>)\n\n"
                    "Vecs own their elements. When a Vec is dropped, all elements\n"
                    "are dropped too."
                ),
                "options": [
                    "[1, 2, 3]",
                    "[1, 2, 3, 4]",
                    "[4, 1, 2, 3]",
                    "Compile error — vec is immutable",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "push() appends to the end of the vector.",
                    "The vec starts as [1,2,3] and push(4) adds 4 at the end.",
                ],
            },
            {
                "id": "rust_hashmap",
                "type": "quiz",
                "title": "HashMap<K, V>",
                "question": (
                    "How do you safely access a HashMap value that might not exist?\n\n"
                    "  use std::collections::HashMap;\n\n"
                    "  let mut scores = HashMap::new();\n"
                    "  scores.insert(\"Alice\", 100);\n"
                    "  let alice_score = scores._____(\"Alice\");"
                ),
                "lesson": (
                    "HashMap access methods:\n\n"
                    "  scores[\"Alice\"]     // panics if key doesn't exist!\n"
                    "  scores.get(\"Alice\") // returns Option<&V> — safe!\n\n"
                    "Common patterns:\n"
                    "  // Insert if absent:\n"
                    "  scores.entry(\"Bob\").or_insert(0);\n\n"
                    "  // Update existing:\n"
                    "  let count = scores.entry(\"Alice\").or_insert(0);\n"
                    "  *count += 1;\n\n"
                    "HashMap is not in the prelude — you must import it from\n"
                    "std::collections::HashMap."
                ),
                "options": [
                    "find(\"Alice\")",
                    "get(\"Alice\")",
                    "lookup(\"Alice\")",
                    "fetch(\"Alice\")",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The safe method returns Option<&V>, not the value directly.",
                    "It's the same name as the method on Vec — .get()",
                ],
            },
            {
                "id": "rust_string_vs_str",
                "type": "quiz",
                "title": "String vs &str",
                "question": (
                    "What is the difference between `String` and `&str` in Rust?"
                ),
                "lesson": (
                    "Rust has two main string types:\n\n"
                    "  String  — owned, heap-allocated, growable\n"
                    "    let s = String::from(\"hello\");\n"
                    "    let s = \"hello\".to_string();\n\n"
                    "  &str    — borrowed string slice, immutable view\n"
                    "    let s: &str = \"hello\";  // string literal\n"
                    "    let s: &str = &my_string; // borrow a String\n\n"
                    "Rule of thumb:\n"
                    "  - Function parameters: accept &str (more flexible)\n"
                    "  - Struct fields: use String (owns the data)\n"
                    "  - String literals: are &str by default"
                ),
                "options": [
                    "String is mutable, &str is a read-only type alias",
                    "String is owned and heap-allocated; &str is a borrowed slice",
                    "They are the same type with different syntax",
                    "&str is a raw pointer to a C string",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "One type owns its data on the heap, the other borrows a view.",
                    "String owns; &str borrows. Like Vec<T> vs &[T].",
                ],
            },
            {
                "id": "rust_iterators",
                "type": "quiz",
                "title": "Iterator Chains",
                "question": (
                    "What does this iterator chain produce?\n\n"
                    "  let nums = vec![1, 2, 3, 4, 5];\n"
                    "  let result: Vec<i32> = nums.iter()\n"
                    "      .filter(|&&x| x > 2)\n"
                    "      .map(|&x| x * 10)\n"
                    "      .collect();"
                ),
                "lesson": (
                    "Rust iterators are lazy and zero-cost:\n\n"
                    "  .iter()    — creates an iterator of references\n"
                    "  .filter()  — keeps elements matching a predicate\n"
                    "  .map()     — transforms each element\n"
                    "  .collect() — consumes the iterator into a collection\n\n"
                    "Nothing happens until .collect() (or another consumer) is called.\n"
                    "The compiler often optimizes iterator chains into a single loop —\n"
                    "as fast as hand-written C."
                ),
                "options": [
                    "[10, 20, 30, 40, 50]",
                    "[30, 40, 50]",
                    "[1, 2, 3, 4, 5]",
                    "[3, 4, 5]",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "filter keeps x > 2 → [3, 4, 5], then map multiplies by 10.",
                    "Step by step: filter gives [3,4,5], map gives [30,40,50].",
                ],
            },
            {
                "id": "rust_closures",
                "type": "quiz",
                "title": "Closures",
                "question": (
                    "What is a closure in Rust?\n\n"
                    "  let add = |a: i32, b: i32| -> i32 { a + b };\n"
                    "  let sum = add(3, 4);  // 7\n\n"
                    "  let multiplier = 3;\n"
                    "  let triple = |x| x * multiplier;  // captures multiplier"
                ),
                "lesson": (
                    "Closures are anonymous functions that capture their environment:\n\n"
                    "  |params| body         // basic syntax\n"
                    "  |a, b| a + b          // types inferred\n"
                    "  |a: i32| -> i32 { }   // explicit types\n\n"
                    "Closures capture variables from their scope three ways:\n"
                    "  Fn    — borrows immutably (&T)\n"
                    "  FnMut — borrows mutably (&mut T)\n"
                    "  FnOnce — takes ownership (moves T)\n\n"
                    "The compiler infers which trait a closure implements based\n"
                    "on how it uses the captured variables."
                ),
                "options": [
                    "A function that cannot access variables outside its body",
                    "An anonymous function that can capture variables from its environment",
                    "A macro that expands at compile time",
                    "A function pointer with no runtime overhead",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Closures 'close over' variables from their surrounding scope.",
                    "The |...| syntax defines an anonymous function that can capture variables.",
                ],
            },
            {
                "id": "rust_into_iter",
                "type": "quiz",
                "title": "iter vs into_iter vs iter_mut",
                "question": (
                    "What is the difference between .iter(), .into_iter(), and .iter_mut()?"
                ),
                "lesson": (
                    "Three ways to iterate over a collection:\n\n"
                    "  .iter()      — iterates over &T (immutable references)\n"
                    "                  Collection is NOT consumed\n\n"
                    "  .iter_mut()  — iterates over &mut T (mutable references)\n"
                    "                  Can modify elements in place\n\n"
                    "  .into_iter() — iterates over T (owned values)\n"
                    "                  Collection IS consumed (moved)\n\n"
                    "  let v = vec![1, 2, 3];\n"
                    "  for x in &v { }       // same as v.iter()\n"
                    "  for x in &mut v { }   // same as v.iter_mut()\n"
                    "  for x in v { }        // same as v.into_iter() — v is gone!"
                ),
                "options": [
                    "They are all identical",
                    "iter() borrows, into_iter() takes ownership, iter_mut() borrows mutably",
                    "iter() is for Vec, into_iter() is for HashMap, iter_mut() is for arrays",
                    "iter() is fast, into_iter() is slow, iter_mut() is unsafe",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Think about ownership: borrow, move, or borrow mutably.",
                    "into_iter() CONSUMES the collection — you can't use it afterward.",
                ],
            },
        ],
    },

    # ── ZONE 7: CONCURRENCY ──────────────────────────────────────────────
    "concurrency": {
        "id": "concurrency",
        "name": "The Fearless Grid",
        "subtitle": "Threads, Arc, Mutex, Channels & Send/Sync",
        "color": "cyan",
        "icon": "⚡",
        "commands": ["std::thread", "Arc::new()", "Mutex::new()", "mpsc::channel()"],
        "challenges": [
            {
                "id": "rust_spawn_thread",
                "type": "quiz",
                "title": "Spawning Threads",
                "question": (
                    "What does `move` do in this thread spawn?\n\n"
                    "  use std::thread;\n\n"
                    "  let name = String::from(\"worker\");\n"
                    "  let handle = thread::spawn(move || {\n"
                    "      println!(\"Thread: {name}\");\n"
                    "  });\n"
                    "  handle.join().unwrap();"
                ),
                "lesson": (
                    "`move` forces the closure to take ownership of captured variables:\n\n"
                    "  thread::spawn(move || { ... })\n\n"
                    "Without `move`, the closure would try to borrow `name`. But\n"
                    "the spawned thread might outlive the current scope — so Rust\n"
                    "requires ownership transfer to guarantee safety.\n\n"
                    "  handle.join() — waits for the thread to finish\n"
                    "  .unwrap()     — panics if the thread panicked"
                ),
                "options": [
                    "Moves the thread to a different CPU core",
                    "Transfers ownership of captured variables into the closure",
                    "Makes the closure run asynchronously",
                    "Copies all variables into the thread's stack",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The spawned thread might outlive the calling scope — it needs to OWN the data.",
                    "`move` makes the closure take ownership instead of borrowing.",
                ],
            },
            {
                "id": "rust_arc",
                "type": "quiz",
                "title": "Arc — Atomic Reference Counting",
                "question": (
                    "Why use Arc<T> instead of Rc<T> for sharing data between threads?\n\n"
                    "  use std::sync::Arc;\n"
                    "  use std::thread;\n\n"
                    "  let data = Arc::new(vec![1, 2, 3]);\n"
                    "  let data_clone = Arc::clone(&data);\n\n"
                    "  thread::spawn(move || {\n"
                    "      println!(\"{:?}\", data_clone);\n"
                    "  });"
                ),
                "lesson": (
                    "Rc<T> — Reference Counted (single-threaded only)\n"
                    "Arc<T> — Atomic Reference Counted (thread-safe)\n\n"
                    "Arc uses atomic operations for its reference count, which\n"
                    "is safe across threads but slightly slower than Rc.\n\n"
                    "  Arc::clone(&data)  — increments the reference count\n"
                    "                        (does NOT deep-clone the data)\n\n"
                    "Rc does NOT implement Send, so the compiler will refuse\n"
                    "to let you pass it to another thread. Arc does."
                ),
                "options": [
                    "Arc is faster than Rc",
                    "Arc uses atomic operations, making it safe to share across threads",
                    "Rc works with threads but Arc is recommended",
                    "Arc automatically locks the data for you",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Rc's reference count isn't thread-safe. Arc's is.",
                    "Atomic = safe across threads. Non-atomic = single thread only.",
                ],
            },
            {
                "id": "rust_mutex",
                "type": "quiz",
                "title": "Mutex<T> — Mutual Exclusion",
                "question": (
                    "How do you access data inside a Mutex?\n\n"
                    "  use std::sync::Mutex;\n\n"
                    "  let counter = Mutex::new(0);\n"
                    "  {\n"
                    "      let mut num = counter.lock().unwrap();\n"
                    "      *num += 1;\n"
                    "  } // lock is released here"
                ),
                "lesson": (
                    "Mutex<T> provides interior mutability with locking:\n\n"
                    "  .lock()  — acquires the lock, returns MutexGuard<T>\n"
                    "  *num     — dereference to access/modify the inner value\n\n"
                    "The lock is automatically released when the MutexGuard\n"
                    "goes out of scope (RAII pattern).\n\n"
                    "Common pattern for multi-threaded mutation:\n"
                    "  Arc<Mutex<T>> — shared ownership + interior mutability"
                ),
                "options": [
                    "counter.get()",
                    "counter.lock().unwrap()",
                    "counter.read()",
                    "counter.borrow_mut()",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You must acquire the lock before accessing the data.",
                    ".lock() returns a Result — unwrap or use ? to get the guard.",
                ],
            },
            {
                "id": "rust_channels",
                "type": "quiz",
                "title": "Channels — Message Passing",
                "question": (
                    "What does `mpsc` stand for in Rust's channel implementation?\n\n"
                    "  use std::sync::mpsc;\n\n"
                    "  let (tx, rx) = mpsc::channel();\n"
                    "  tx.send(42).unwrap();\n"
                    "  let val = rx.recv().unwrap();"
                ),
                "lesson": (
                    "mpsc = Multiple Producer, Single Consumer\n\n"
                    "  let (tx, rx) = mpsc::channel();\n\n"
                    "  tx.send(val)  — send a value (transfers ownership!)\n"
                    "  rx.recv()     — blocking receive\n"
                    "  rx.try_recv() — non-blocking receive\n\n"
                    "You can clone tx to create multiple producers:\n"
                    "  let tx2 = tx.clone();\n\n"
                    "Channels transfer ownership — once you send a value,\n"
                    "you can't use it in the sender anymore."
                ),
                "options": [
                    "Multiple Producer, Single Consumer",
                    "Multi-Process Synchronous Channel",
                    "Message Passing System Controller",
                    "Multiple Parallel Stream Connector",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "m-p-s-c: four words, the first is Multiple, the last is Consumer.",
                    "Multiple senders, one receiver.",
                ],
            },
            {
                "id": "rust_send_sync",
                "type": "quiz",
                "title": "Send and Sync Traits",
                "question": (
                    "What do the `Send` and `Sync` marker traits guarantee?"
                ),
                "lesson": (
                    "Two marker traits control thread safety:\n\n"
                    "  Send  — ownership can be TRANSFERRED between threads\n"
                    "           Most types are Send. Rc<T> is NOT.\n\n"
                    "  Sync  — references can be SHARED between threads\n"
                    "           T is Sync if &T is Send.\n"
                    "           Mutex<T> is Sync (even if T isn't).\n\n"
                    "The compiler automatically derives Send/Sync for types\n"
                    "whose fields are all Send/Sync. If you try to send a\n"
                    "non-Send type to another thread, it's a COMPILE error.\n\n"
                    "This is 'fearless concurrency' — the type system prevents\n"
                    "data races at compile time."
                ),
                "options": [
                    "Send means thread-safe; Sync means async-safe",
                    "Send: ownership can transfer across threads; Sync: references can be shared across threads",
                    "Send is for channels; Sync is for mutexes",
                    "Both are runtime checks for thread safety",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Send = can MOVE to another thread. Sync = can be REFERENCED from another thread.",
                    "These are compile-time guarantees, not runtime checks.",
                ],
            },
            {
                "id": "rust_fearless_concurrency",
                "type": "quiz",
                "title": "Fearless Concurrency",
                "question": (
                    "Why is Rust's concurrency called 'fearless'?"
                ),
                "lesson": (
                    "Fearless concurrency means the compiler catches concurrency\n"
                    "bugs at COMPILE TIME:\n\n"
                    "  - Data races → prevented by ownership + Send/Sync\n"
                    "  - Use after free → prevented by the borrow checker\n"
                    "  - Dangling references → prevented by lifetimes\n"
                    "  - Double free → prevented by ownership\n\n"
                    "In C/C++, these are runtime bugs that crash production.\n"
                    "In Rust, they are compile errors you fix before deploying.\n\n"
                    "If your Rust program compiles, it is free of data races.\n"
                    "That's the guarantee."
                ),
                "options": [
                    "Rust threads never panic",
                    "The compiler prevents data races and memory errors at compile time",
                    "Rust uses green threads that are immune to deadlocks",
                    "Rust's runtime automatically detects and fixes concurrency bugs",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "'Fearless' because the compiler catches the bugs, not your users.",
                    "Compile-time guarantees mean no data races in safe Rust.",
                ],
            },
        ],
    },

    # ── ZONE 8: CARGO AND ECOSYSTEM ──────────────────────────────────────
    "cargo_and_ecosystem": {
        "id": "cargo_and_ecosystem",
        "name": "The Cargo Bay",
        "subtitle": "Cargo.toml, crates.io, Workspaces, Testing & Tooling",
        "color": "white",
        "icon": "📦",
        "commands": ["cargo build", "cargo test", "cargo clippy", "cargo fmt"],
        "challenges": [
            {
                "id": "rust_cargo_toml",
                "type": "quiz",
                "title": "Cargo.toml",
                "question": (
                    "What is the role of Cargo.toml in a Rust project?\n\n"
                    "  [package]\n"
                    "  name = \"my-app\"\n"
                    "  version = \"0.1.0\"\n"
                    "  edition = \"2021\"\n\n"
                    "  [dependencies]\n"
                    "  serde = { version = \"1.0\", features = [\"derive\"] }\n"
                    "  tokio = { version = \"1\", features = [\"full\"] }"
                ),
                "lesson": (
                    "Cargo.toml is the manifest file — Rust's package.json/go.mod:\n\n"
                    "  [package]       — name, version, edition, authors\n"
                    "  [dependencies]  — crate dependencies from crates.io\n"
                    "  [dev-dependencies] — test-only dependencies\n"
                    "  [build-dependencies] — build script dependencies\n\n"
                    "  edition = \"2021\" — Rust edition (2015, 2018, 2021, 2024)\n"
                    "  Editions add syntax without breaking old code.\n\n"
                    "Cargo.lock pins exact versions (like package-lock.json)."
                ),
                "options": [
                    "A configuration file for the Rust compiler",
                    "The project manifest — metadata, dependencies, and build settings",
                    "A list of source files to compile",
                    "The test configuration file",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Cargo.toml is to Rust what package.json is to Node.js.",
                    "It defines the package metadata and lists all dependencies.",
                ],
            },
            {
                "id": "rust_crates_io",
                "type": "quiz",
                "title": "crates.io",
                "question": (
                    "What is crates.io?"
                ),
                "lesson": (
                    "crates.io is Rust's official package registry:\n\n"
                    "  - Public registry for open-source crates\n"
                    "  - cargo publish — upload your crate\n"
                    "  - cargo add serde — add a dependency\n"
                    "  - Immutable publishing — versions can't be deleted\n\n"
                    "Popular crates:\n"
                    "  serde    — serialization/deserialization\n"
                    "  tokio    — async runtime\n"
                    "  reqwest  — HTTP client\n"
                    "  clap     — CLI argument parsing\n"
                    "  tracing  — structured logging"
                ),
                "options": [
                    "The Rust compiler's standard library",
                    "Rust's official package registry for publishing and discovering crates",
                    "A CI/CD platform for Rust projects",
                    "A code formatting service for Rust",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Like npm for JavaScript or PyPI for Python.",
                    "It's the central registry where Rust packages (crates) are published.",
                ],
            },
            {
                "id": "rust_workspaces",
                "type": "quiz",
                "title": "Cargo Workspaces",
                "question": (
                    "What is a Cargo workspace?\n\n"
                    "  # root Cargo.toml\n"
                    "  [workspace]\n"
                    "  members = [\n"
                    "      \"core\",\n"
                    "      \"api\",\n"
                    "      \"cli\",\n"
                    "  ]"
                ),
                "lesson": (
                    "A workspace groups multiple related packages (crates):\n\n"
                    "  - Shared Cargo.lock — all crates use the same dependency versions\n"
                    "  - Shared target/ directory — faster builds, less disk space\n"
                    "  - cargo build --workspace — builds everything\n"
                    "  - cargo test --workspace — tests everything\n\n"
                    "Workspace members can depend on each other:\n"
                    "  [dependencies]\n"
                    "  core = { path = \"../core\" }"
                ),
                "options": [
                    "A remote development environment",
                    "A monorepo structure with multiple crates sharing one Cargo.lock",
                    "A virtual machine for running Rust code",
                    "A Docker container for Rust builds",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Workspaces organize multiple crates in a single repository.",
                    "They share a single Cargo.lock and target directory.",
                ],
            },
            {
                "id": "rust_testing",
                "type": "quiz",
                "title": "Testing in Rust",
                "question": (
                    "Where do unit tests go in Rust?\n\n"
                    "  // src/lib.rs\n"
                    "  pub fn add(a: i32, b: i32) -> i32 {\n"
                    "      a + b\n"
                    "  }\n\n"
                    "  #[cfg(test)]\n"
                    "  mod tests {\n"
                    "      use super::*;\n\n"
                    "      #[test]\n"
                    "      fn test_add() {\n"
                    "          assert_eq!(add(2, 3), 5);\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Rust testing conventions:\n\n"
                    "  Unit tests — in the same file, inside #[cfg(test)] mod tests\n"
                    "  Integration tests — in tests/ directory\n\n"
                    "  #[test]           — marks a function as a test\n"
                    "  #[cfg(test)]      — only compiled during testing\n"
                    "  assert!()         — asserts a boolean\n"
                    "  assert_eq!(a, b)  — asserts equality\n"
                    "  assert_ne!(a, b)  — asserts inequality\n\n"
                    "  cargo test                — run all tests\n"
                    "  cargo test test_add       — run specific test\n"
                    "  cargo test -- --nocapture — show println! output"
                ),
                "options": [
                    "In a separate test/ file that imports the module",
                    "In the same file, inside a #[cfg(test)] module",
                    "In a __tests__ directory like JavaScript",
                    "In a dedicated tests.rs file at the project root",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Unit tests live alongside the code they test.",
                    "#[cfg(test)] means the module is only compiled when running tests.",
                ],
            },
            {
                "id": "rust_clippy",
                "type": "quiz",
                "title": "Clippy — The Linter",
                "question": (
                    "What does `cargo clippy` do?"
                ),
                "lesson": (
                    "Clippy is Rust's official linter — hundreds of lint rules:\n\n"
                    "  cargo clippy           — run the linter\n"
                    "  cargo clippy --fix     — auto-fix what it can\n\n"
                    "Clippy catches:\n"
                    "  - Unnecessary clones\n"
                    "  - Redundant closures\n"
                    "  - Unidiomatic code patterns\n"
                    "  - Performance issues\n"
                    "  - Common mistakes\n\n"
                    "  #[allow(clippy::lint_name)]  — suppress a specific lint\n"
                    "  #[deny(clippy::all)]          — make all clippy warnings errors\n\n"
                    "Most Rust teams run clippy in CI as a quality gate."
                ),
                "options": [
                    "Compiles the project in release mode",
                    "Runs the official Rust linter with hundreds of code quality checks",
                    "Formats the code according to Rust style guidelines",
                    "Publishes the crate to crates.io",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Clippy is a linter, not a formatter or compiler.",
                    "Named after the old Microsoft Office assistant — it offers helpful suggestions!",
                ],
            },
            {
                "id": "rust_rustfmt",
                "type": "quiz",
                "title": "rustfmt — Code Formatting",
                "question": (
                    "What is the difference between `cargo fmt` and `cargo clippy`?"
                ),
                "lesson": (
                    "Two complementary tools:\n\n"
                    "  cargo fmt (rustfmt)  — auto-formats code style\n"
                    "    - Indentation, line width, brace placement\n"
                    "    - Deterministic — same input always gives same output\n"
                    "    - Configure with rustfmt.toml\n\n"
                    "  cargo clippy  — analyzes code logic and patterns\n"
                    "    - Idiomatic Rust suggestions\n"
                    "    - Performance improvements\n"
                    "    - Common bug patterns\n\n"
                    "CI pipeline: cargo fmt --check && cargo clippy && cargo test"
                ),
                "options": [
                    "fmt formats code style; clippy analyzes code logic and patterns",
                    "They are the same tool with different names",
                    "fmt runs tests; clippy checks dependencies",
                    "fmt is for libraries; clippy is for applications",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "One is about how the code LOOKS, the other about how the code WORKS.",
                    "fmt = formatting (whitespace, braces). clippy = logic (patterns, idioms).",
                ],
            },
        ],
    },
}
