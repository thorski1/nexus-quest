"""
story.py — Narrative text for Rust Forge.
Theme: Memory-safe. Blazing fast. The language that never segfaults.
An investigator reverse-engineering a zero-overhead systems layer
built in Rust — the memory-safe backbone beneath NEXUS Corp's
most critical infrastructure.
"""

INTRO_STORY = """
The crash dump told the whole story — or rather, the [bold white]absence[/bold white] of one did.

Every other layer of NEXUS Corp's infrastructure had left forensic traces.
The Python scripts segfaulted under load. The C++ services leaked memory
like sieves. The Go microservices hit data races under concurrency stress
tests. But one layer — the deepest layer, the one that handled cryptographic
key rotation, secure memory enclaves, and real-time packet inspection —
had [bold cyan]never crashed[/bold cyan].

Not once. Not in eighteen months of continuous operation.

[bold red]Rust.[/bold red]

The entire secure foundation — the zero-copy parsers, the lock-free data
structures, the memory-safe FFI bridges into the kernel — was written in
Rust. No garbage collector. No runtime. No segfaults. Just the borrow
checker's iron guarantee: if it compiles, the memory is safe.

[bold magenta]You've heard the rumors.[/bold magenta] A language so strict that half your code
won't compile on the first try. A borrow checker that feels like arguing
with a compiler that knows more about your program than you do.
But the code that survives the compiler? It [italic]runs forever[/italic].

The source is on the seized build server. Every crate, every lifetime
annotation, every unsafe block carefully audited and justified.
Your mission: trace the ownership graph, decode the trait hierarchies,
and understand how NEXUS Corp built the one layer that never failed.

[bold cyan]The Cargo workspace is open. The crates are compiled. Begin.[/bold cyan]
"""

ZONE_INTROS = {
    "rust_basics": """
[bold cyan]== THE IMMUTABLE CORE ==[/bold cyan]

The first file you open is [yellow]main.rs[/yellow] — and the first thing you notice
is what's missing. No `var` keyword. No `let x = 5; x = 10;`. Every
binding is immutable by default.

Rust starts from safety. Variables don't change unless you explicitly
say so. Types are inferred but always known at compile time. Functions
return their last expression — no `return` keyword needed.

This isn't a limitation. It's a [bold white]guarantee[/bold white]. The compiler knows exactly
what can change and what can't, and it uses that knowledge to eliminate
entire categories of bugs before your code ever runs.

[italic]"In Rust, immutability isn't a suggestion — it's the default."[/italic]
""",
    "ownership": """
[bold cyan]== THE BORROW CHECKER ==[/bold cyan]

This is the heart of Rust. The reason the secure layer never crashed.
The reason there are no use-after-free bugs, no double frees, no
dangling pointers anywhere in the codebase.

[bold white]Ownership.[/bold white]

Every value has exactly one owner. When the owner goes out of scope,
the value is dropped. You can borrow a reference — immutably as many
times as you want, or mutably exactly once — but the compiler tracks
every borrow and ensures they never outlive the owner.

The borrow checker is the most powerful static analysis tool ever built
into a programming language. It doesn't find bugs — it makes them
[bold yellow]impossible to write[/bold yellow].

[italic]"Fighting the borrow checker is learning. Passing the borrow checker is knowing."[/italic]
""",
    "enums_and_matching": """
[bold cyan]== THE PATTERN LATTICE ==[/bold cyan]

No null. Anywhere. In the entire codebase.

Where other languages would return null, nil, None, or undefined,
NEXUS Corp's Rust layer uses [yellow]Option<T>[/yellow] — a type that forces you
to handle the "nothing" case at compile time. Where other languages
throw exceptions, it uses [yellow]Result<T, E>[/yellow] — a type that forces you
to handle errors explicitly.

And the weapon that makes this ergonomic? [bold white]Pattern matching.[/bold white]
Rust's `match` is exhaustive — miss a case and the compiler refuses
to build. Every code path is covered. Every edge case is handled.

[italic]"Null references: the billion-dollar mistake. Rust's Option<T>: the fix."[/italic]
""",
    "structs_and_traits": """
[bold cyan]== THE TRAIT MATRIX ==[/bold cyan]

No classes. No inheritance. The secure layer's architecture is built
entirely on [bold white]structs and traits[/bold white] — data and behavior, cleanly separated.

Structs hold data. Impl blocks attach methods. Traits define shared
behavior — like interfaces, but with default implementations, associated
types, and the ability to be used as generic bounds.

The derive system generates boilerplate automatically — Debug, Clone,
Serialize, PartialEq — all produced by the compiler from a single line
of annotation. And generics with trait bounds give you zero-cost
abstraction: polymorphism at compile time with no runtime overhead.

[italic]"Favor composition over inheritance. In Rust, that's not advice — it's the only option."[/italic]
""",
    "error_handling": """
[bold cyan]== THE ERROR CHAIN ==[/bold cyan]

The secure layer's error handling is immaculate. No unwrap() calls in
production code. No panics. Every fallible operation returns a
[yellow]Result<T, E>[/yellow], and the [yellow]?[/yellow] operator threads errors up the call stack
with zero boilerplate.

Custom error types built with [yellow]thiserror[/yellow] give the library crates
structured, matchable errors. The application layer uses [yellow]anyhow[/yellow] for
ergonomic error propagation with context messages.

This is error handling done right. No hidden control flow. No uncaught
exceptions at 3 AM. Every error path is explicit, typed, and handled.

[italic]"Errors are values. Handle them, propagate them, or transform them — but never ignore them."[/italic]
""",
    "collections": """
[bold cyan]== THE DATA FORGE ==[/bold cyan]

The internal data pipeline processes millions of records per second.
Vec for ordered sequences. HashMap for lookups. String for owned text,
&str for borrowed slices.

But the real power is in the [bold white]iterator system[/bold white]. Lazy, composable,
zero-cost. Filter, map, fold, collect — chained into pipelines that
the compiler optimizes into tight loops indistinguishable from
hand-written C.

Closures capture their environment with surgical precision — the
compiler knows whether they borrow, mutably borrow, or take ownership,
and enforces the rules accordingly.

[italic]"Iterator chains: the map-reduce of systems programming. Zero allocation. Zero overhead."[/italic]
""",
    "concurrency": """
[bold cyan]== THE FEARLESS GRID ==[/bold cyan]

This is where Rust's guarantees pay off the most.

NEXUS Corp's secure layer runs [bold white]thousands of threads[/bold white] across the
cryptographic processing farm. Arc<Mutex<T>> for shared mutable state.
Channels for message passing. Thread pools for parallel computation.

And not a single data race. Not because the engineers were careful.
Because the [bold yellow]compiler made data races impossible[/bold yellow].

Send and Sync — two marker traits that the compiler checks automatically.
If a type isn't safe to send across threads, you physically cannot send
it. If a reference isn't safe to share, you physically cannot share it.
The type system IS the concurrency model.

[italic]"Fearless concurrency: the compiler catches your data races so production doesn't have to."[/italic]
""",
    "cargo_and_ecosystem": """
[bold cyan]== THE CARGO BAY ==[/bold cyan]

The build system is Cargo — and it's the best build tool in any
language ecosystem. Period.

[yellow]Cargo.toml[/yellow] declares dependencies. [yellow]Cargo.lock[/yellow] pins versions.
Workspaces organize multiple crates in a monorepo. `cargo test` runs
unit tests, integration tests, and doc tests. `cargo clippy` catches
hundreds of code quality issues. `cargo fmt` enforces consistent style.

crates.io hosts over 140,000 crates. serde for serialization. tokio
for async. clap for CLIs. The ecosystem is young but fiercely
high-quality — because Rust's type system makes it hard to publish
broken code.

[italic]"Cargo: build, test, lint, format, publish — all in one tool that just works."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "rust_basics": """
[bold green]Immutable core mapped.[/bold green]

Variables, types, functions, shadowing, mutability — the foundations
of a language that chooses safety as the default. Every binding is
immutable until you say otherwise. Every type is known at compile time.

[bold cyan]"Rust's basics aren't basic — they're the first line of defense.
Immutability by default means the compiler knows your intent.
And a compiler that knows your intent can protect you from yourself."[/bold cyan]

The ownership system is next. Time to face the borrow checker...
""",
    "ownership": """
[bold green]Borrow checker mastered.[/bold green]

Ownership. Borrowing. Lifetimes. The three pillars that let Rust
guarantee memory safety without a garbage collector. Every reference
is tracked. Every borrow is checked. Every lifetime is verified.

[bold cyan]"The borrow checker is not your enemy — it's the strictest code
reviewer you'll ever have. It catches use-after-free, double-free,
and data races before your code ever runs. That's not a constraint.
That's a superpower."[/bold cyan]

The pattern lattice awaits. Time to decode enums and matching...
""",
    "enums_and_matching": """
[bold green]Pattern lattice decoded.[/bold green]

Enums with data. Option instead of null. Result instead of exceptions.
Exhaustive match expressions that the compiler enforces. Every possible
state is modeled in the type system.

[bold cyan]"Rust's enums are algebraic data types — the most powerful tool
for modeling state in any systems language. Combined with exhaustive
matching, they make 'forgot to handle that case' a compile error,
not a production incident."[/bold cyan]

The trait matrix is next. Structs, traits, and zero-cost abstraction...
""",
    "structs_and_traits": """
[bold green]Trait matrix mapped.[/bold green]

Structs for data. Traits for behavior. Generics for abstraction.
Derive macros for boilerplate. No classes, no inheritance — just
composition, all the way down.

[bold cyan]"Rust proves you don't need inheritance to build complex systems.
Structs + traits + generics give you everything OOP promised, without
the fragile base class problem, the diamond problem, or the hidden
state mutations."[/bold cyan]

The error chain is next. Time to trace the error handling system...
""",
    "error_handling": """
[bold green]Error chain traced.[/bold green]

Result<T, E> for every fallible operation. The ? operator for clean
propagation. thiserror for libraries. anyhow for applications.
No exceptions, no hidden control flow, no surprises.

[bold cyan]"Rust's error handling is verbose — on purpose. Every error is
a value you must handle. Every failure path is visible in the type
signature. When you read a Rust function, you know exactly what
can go wrong."[/bold cyan]

The data forge awaits. Collections, iterators, closures...
""",
    "collections": """
[bold green]Data forge mastered.[/bold green]

Vec, HashMap, String, &str — the core collection types. Iterators
that are lazy, composable, and zero-cost. Closures that capture
their environment with ownership-aware precision.

[bold cyan]"Rust's iterator system compiles to the same machine code as a
hand-written loop. Zero overhead. Zero allocation. Functional
programming ergonomics with systems programming performance."[/bold cyan]

The fearless grid is next. Concurrency awaits...
""",
    "concurrency": """
[bold green]Fearless grid conquered.[/bold green]

Threads, Arc, Mutex, channels, Send, Sync. The concurrency primitives
that let Rust guarantee freedom from data races at compile time.

[bold cyan]"Other languages say 'be careful with threads.' Rust says 'the
compiler will ENFORCE correctness.' Send and Sync are not runtime
checks — they are compile-time proofs that your concurrent code
is safe."[/bold cyan]

The Cargo bay is the final zone. The ecosystem awaits...
""",
    "cargo_and_ecosystem": """
[bold green]Cargo bay fully catalogued. Every crate inventoried.[/bold green]

Cargo.toml, crates.io, workspaces, testing, clippy, rustfmt.
The toolchain that makes Rust not just safe and fast, but a joy
to develop with.

[bold cyan]"Cargo is arguably the best build tool in any programming language.
Build, test, lint, format, benchmark, publish — all with a single
tool that gets out of your way and lets you focus on the code."[/bold cyan]

[bold white]The Rust source tree is fully mapped. Every lifetime traced.
Every trait decoded. Every ownership chain verified.[/bold white]

[bold white]Rustacean. Developer. Engineer. Borrow Checker. Unsafe Master.[/bold white]
[bold white]That's you. Ferris would be proud.[/bold white]
""",
}

BOSS_INTROS = {
    "rust_basics": "The main.rs file declares a variable and then tries to reassign it — but there's no `mut`. [bold yellow]\"What does Rust do differently from every other language about variable mutability?\"[/bold yellow]",
    "ownership": "A function takes a String parameter and the caller tries to use it afterward. [bold yellow]\"The caller gets a compile error. Explain what happened to the String and why.\"[/bold yellow]",
    "enums_and_matching": "A match expression covers three of four enum variants. [bold yellow]\"The compiler refuses to build. What Rust principle makes this a compile error, not a runtime bug?\"[/bold yellow]",
    "structs_and_traits": "Six different structs implement the same trait but the calling code uses generics, not trait objects. [bold yellow]\"What is monomorphization, and why does it give zero runtime overhead?\"[/bold yellow]",
    "error_handling": "The secure layer has zero .unwrap() calls in production code. [bold yellow]\"What do they use instead, and why is unwrap() dangerous in production?\"[/bold yellow]",
    "collections": "An iterator chain processes 10 million records with no heap allocations. [bold yellow]\"How does Rust's iterator system achieve zero-cost abstraction?\"[/bold yellow]",
    "concurrency": "The cryptographic farm runs 4,000 threads sharing a single data structure. [bold yellow]\"What type wraps the shared data, and what two traits does the compiler check?\"[/bold yellow]",
    "cargo_and_ecosystem": "The CI pipeline runs three Cargo commands before merging any PR. [bold yellow]\"Name them and explain what each one catches.\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "immutable_core":      ("Immutable Core", "Mastered Rust variables, types, functions, and shadowing."),
    "borrow_master":       ("Borrow Master", "Conquered ownership, borrowing, references, and lifetimes."),
    "pattern_decoder":     ("Pattern Decoder", "Decoded enums, Option, Result, and exhaustive matching."),
    "trait_architect":     ("Trait Architect", "Mapped structs, traits, generics, and derive macros."),
    "error_handler":       ("Error Handler", "Traced the error chain — Result, ?, thiserror, anyhow."),
    "collection_master":   ("Collection Master", "Mastered Vec, HashMap, iterators, and closures."),
    "concurrency_fearless": ("Fearless Concurrency", "Conquered threads, Arc, Mutex, channels, and Send/Sync."),
    "cargo_navigator":     ("Cargo Navigator", "Catalogued the ecosystem — Cargo, crates.io, testing, and tooling."),
}
