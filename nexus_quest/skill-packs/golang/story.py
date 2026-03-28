"""
story.py — Narrative text for Go Ops.
Theme: Simple. Fast. Concurrent. The language that powers the cloud.
A systems architect reverse-engineering a high-performance distributed
system built in Go — the backbone of NEXUS Corp's real-time infrastructure.
"""

INTRO_STORY = """
The first clue was the latency.

[bold white]Fourteen microseconds.[/bold white] That's how fast NEXUS Corp's internal mesh was
routing messages between nodes — orders of magnitude faster than anything
their public-facing API should have been capable of. The congressional
investigators had traced the money. The database team had mapped the schemas.
The container specialists had catalogued the infrastructure.

But underneath all of it — underneath the Python automation, the Docker
orchestration, the Kubernetes clusters — was something else. Something
[bold cyan]fast[/bold cyan]. Something [bold cyan]concurrent[/bold cyan]. Something compiled down to a
single static binary that left almost no trace on the host filesystem.

[bold red]Go.[/bold red]

The entire real-time backbone — the message brokers, the API gateways,
the service mesh, the custom load balancers — was written in Go. Tens of
thousands of goroutines handling millions of concurrent connections.
No framework. No runtime dependencies. Just the standard library and
a handful of carefully chosen modules.

[bold magenta]You've seen this before.[/bold magenta] Corporations that need speed and reliability at
scale always end up here. Go doesn't have the elegance of Rust or the
ecosystem of Python. What it has is [italic]simplicity[/italic] — and simplicity,
at scale, is a weapon.

The source code is on the compromised build server. Every module, every
interface, every goroutine pattern. Your job: read it, understand it,
and map the architecture that made NEXUS Corp's real-time infrastructure
possible.

[bold cyan]The Go source tree is open. The modules are resolved. Begin.[/bold cyan]
"""

ZONE_INTROS = {
    "go_basics": """
[bold cyan]== THE FOUNDATION LAYER ==[/bold cyan]

The first file you open is [yellow]main.go[/yellow] — thirty lines. No imports beyond
the standard library. No build tags. No magic.

Go starts simple. Variables, types, functions, packages. Everything is
explicit. Everything is visible. The language was designed by people who
had spent decades watching complexity destroy systems.

[yellow]var[/yellow], [yellow]:=[/yellow], [yellow]func[/yellow], [yellow]package[/yellow], [yellow]import[/yellow] — the vocabulary is small.
The error handling is verbose. And that's the point.

[italic]"Clear is better than clever." — Go Proverb[/italic]
""",
    "control_flow": """
[bold cyan]== FLOW CONTROL MATRIX ==[/bold cyan]

The codebase uses exactly one looping construct: [yellow]for[/yellow].
No while. No do-while. No foreach. Just [yellow]for[/yellow] — four different ways.

The switch statements have no fallthrough by default. The defer calls
stack up like a cleanup crew, guaranteed to run no matter how the
function exits.

Every control structure in Go was designed to eliminate the bugs that
other languages made too easy to write.

[italic]"Don't communicate by sharing memory; share memory by communicating."[/italic]
""",
    "data_structures": """
[bold cyan]== THE DATA VAULT ==[/bold cyan]

The internal data models are clean. Structs with exported and unexported
fields. Slices pre-allocated to expected capacity. Maps with the
comma-ok idiom on every lookup.

No generics needed for most of this — just slices, maps, structs, and
pointers. The basics, done right.

[yellow]make()[/yellow] allocates. [yellow]append()[/yellow] grows. [yellow]len()[/yellow] measures. [yellow]cap()[/yellow] reveals
how much room is left before the next allocation.

[italic]"A little copying is better than a little dependency."[/italic]
""",
    "concurrency": """
[bold cyan]== THE CONCURRENCY GRID ==[/bold cyan]

This is where it gets serious.

NEXUS Corp's message broker handles [bold white]2.4 million messages per second[/bold white].
Not through threads. Not through async/await. Through goroutines and channels —
Go's native concurrency primitives.

Each connection is a goroutine. Each message flows through a channel.
Select statements multiplex between data streams, error channels, and
timeout signals. WaitGroups coordinate shutdown. Mutexes protect the
few pieces of shared state that channels can't handle.

[italic]"Concurrency is not parallelism." — Rob Pike[/italic]
""",
    "interfaces": """
[bold cyan]== THE INTERFACE PROTOCOL ==[/bold cyan]

The architecture's flexibility comes from one feature: [bold white]implicit interfaces[/bold white].

No `implements` keyword. No interface registration. If your type has the
right methods, it satisfies the interface. The scanner subsystem defines
a [yellow]Scanner[/yellow] interface — and six different implementations satisfy it
without ever referencing the interface by name.

This is how Go achieves polymorphism without inheritance. Small interfaces.
Implicit satisfaction. Maximum decoupling.

[italic]"The bigger the interface, the weaker the abstraction." — Go Proverb[/italic]
""",
    "standard_library": """
[bold cyan]== THE STANDARD ARSENAL ==[/bold cyan]

NEXUS Corp's API gateway has zero external HTTP dependencies. It's built
entirely on [yellow]net/http[/yellow] — Go's standard library HTTP server, which is
production-grade out of the box.

JSON marshaling via [yellow]encoding/json[/yellow]. Environment config via [yellow]os[/yellow].
Request lifecycle via [yellow]context[/yellow]. Tests via [yellow]testing[/yellow]. Streaming
data via [yellow]io.Reader[/yellow] and [yellow]io.Writer[/yellow].

Most Go programs need nothing beyond the standard library. That's not
a limitation — that's a design philosophy.

[italic]"A language that doesn't have everything is actually easier to use."[/italic]
""",
    "go_modules": """
[bold cyan]== THE MODULE REGISTRY ==[/bold cyan]

The build server's [yellow]go.mod[/yellow] tells the full story. Every dependency,
every version, every checksum verified against the public sum database —
or not, for the private modules that bypass the proxy.

Go modules solved dependency management by making it boring: semantic
versioning enforced in import paths, cryptographic checksums in go.sum,
and a single command — [yellow]go mod tidy[/yellow] — to make everything consistent.

The private modules are where the interesting code lives. GOPRIVATE
points to NEXUS Corp's internal GitLab. The checksums don't lie.

[italic]"Versions are promises. Breaking changes get a new major version — and a new import path."[/italic]
""",
    "go_patterns": """
[bold cyan]== THE PATTERN FORGE ==[/bold cyan]

The senior engineers who built this system knew Go deeply. Error wrapping
with [yellow]%w[/yellow] and inspection with [yellow]errors.Is[/yellow] and [yellow]errors.As[/yellow]. HTTP middleware
chains. Constructor-based dependency injection with interfaces.
Table-driven tests covering every edge case. Functional options for
clean configuration.

These aren't framework patterns — they're idiomatic Go. Patterns that
emerged from the language itself, refined by thousands of production
systems. No magic. No reflection. Just functions, interfaces, and
composition.

[italic]"Make the zero value useful." — Go Proverb[/italic]
""",
}

ZONE_COMPLETIONS = {
    "go_basics": """
[bold green]Foundation layer mapped.[/bold green]

Variables, types, functions, packages, error handling — the building blocks
are clear. Go's surface is deliberately small. No operator overloading.
No implicit conversions. No magic.

[bold cyan]"The basics aren't basic. They're the foundation that everything else
is built on. In Go, if you get the basics right, you get everything right."[/bold cyan]

The control flow structures are next. Time to trace the logic paths...
""",
    "control_flow": """
[bold green]Flow control matrix decoded.[/bold green]

One loop keyword. Automatic switch breaks. Defer stacking. Panic recovery.
Every control structure designed to prevent the bugs that haunt other languages.

[bold cyan]"Go's control flow is boring on purpose. Boring means predictable.
Predictable means reliable. Reliable means it's still running at 3 AM
when everything else has crashed."[/bold cyan]

The data structures are waiting. Time to open the vault...
""",
    "data_structures": """
[bold green]Data vault accessed.[/bold green]

Slices, maps, structs, pointers — the composite types that every Go program
is built from. No classes. No inheritance hierarchies. Just data and methods.

[bold cyan]"Go's type system is intentionally minimal. Structs hold data.
Methods add behavior. Interfaces define contracts.
That's all you need."[/bold cyan]

The concurrency grid is next. This is where Go's real power lives...
""",
    "concurrency": """
[bold green]Concurrency grid mastered.[/bold green]

Goroutines. Channels. Select. WaitGroup. Mutex. The primitives that let
a single Go binary handle millions of concurrent operations on a laptop.

[bold cyan]"Most languages bolt concurrency on as an afterthought.
Go was designed for it from day one. Goroutines are cheap.
Channels are safe. The runtime handles the rest."[/bold cyan]

The interfaces are next — the abstraction layer that holds the architecture together...
""",
    "interfaces": """
[bold green]Interface protocol understood.[/bold green]

Implicit satisfaction. Small interfaces. Composition over inheritance.
The architecture's flexibility isn't magic — it's method sets and contracts.

[bold cyan]"In Go, you don't declare that you implement an interface.
You just implement it. The compiler checks. The code stays decoupled.
This is polymorphism without the ceremony."[/bold cyan]

The standard library awaits. Time to explore Go's built-in arsenal...
""",
    "standard_library": """
[bold green]Standard arsenal catalogued.[/bold green]

net/http. encoding/json. os. io. testing. context. Production-grade
tools shipped with every Go installation. No npm install. No pip install.
Just import and go.

[bold cyan]"The Go standard library is one of the best in any language.
You can build a production HTTP API, a CLI tool, or a systems daemon
without a single external dependency."[/bold cyan]

The module system is next. Time to trace the dependency graph...
""",
    "go_modules": """
[bold green]Module registry mapped.[/bold green]

go.mod. go.sum. Semantic versioning. GOPRIVATE. Every dependency tracked,
every checksum verified. Supply chain security built into the toolchain.

[bold cyan]"Go modules are boring — and that's the highest compliment in
dependency management. No lock file conflicts. No phantom dependencies.
Just versions, checksums, and one command to make it all consistent."[/bold cyan]

The pattern forge is the final zone. Time to see how the masters write Go...
""",
    "go_patterns": """
[bold green]Pattern forge complete. Every pattern catalogued.[/bold green]

Error wrapping. Middleware chains. Dependency injection. Table-driven tests.
Functional options. The patterns that turn Go from a simple language into
a powerful one.

[bold cyan]"Go's simplicity is deceptive. The language is small, but the patterns
are deep. Every one of these patterns emerged from real production systems —
battle-tested, refined, and now yours."[/bold cyan]

[bold white]The Go source tree is fully mapped. Every goroutine traced.
Every interface documented. Every pattern understood.[/bold white]

[bold white]Gopher. Developer. Engineer. Architect. Core Contributor.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "go_basics": "The first file imports nothing but `fmt` — and yet it handles three different data types. [bold yellow]\"What does Go call the operator that declares and assigns a variable in one step?\"[/bold yellow]",
    "control_flow": "A deeply nested function uses `defer` six times. [bold yellow]\"When multiple defers stack up, what order do they execute in? And what happens to their arguments?\"[/bold yellow]",
    "data_structures": "A slice is passed to a function that appends beyond its capacity. [bold yellow]\"The caller's slice doesn't see the new elements. Why? What happened under the hood?\"[/bold yellow]",
    "concurrency": "The message broker spawns 100,000 goroutines. [bold yellow]\"How does Go handle this many concurrent tasks without 100,000 OS threads?\"[/bold yellow]",
    "interfaces": "Six different scanner types satisfy the same interface — but none of them mention it by name. [bold yellow]\"How does Go know they implement the interface? What mechanism makes this work?\"[/bold yellow]",
    "standard_library": "The API gateway handles 50,000 concurrent HTTP connections using only the standard library. [bold yellow]\"What single interface must every HTTP handler satisfy? Name the method.\"[/bold yellow]",
    "go_modules": "A private module with a v2 suffix appears in the import path. [bold yellow]\"Why does Go require the major version in the import path? What problem does this solve?\"[/bold yellow]",
    "go_patterns": "The test suite has 300 test cases but only 12 test functions. [bold yellow]\"What Go testing pattern makes this possible? How does t.Run fit in?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "foundation_mapped":     ("Foundation Mapped", "Mastered Go variables, types, functions, and error handling."),
    "flow_controller":       ("Flow Controller", "Decoded Go's control flow — for, switch, defer, panic, recover."),
    "data_architect":        ("Data Architect", "Mapped slices, maps, structs, and pointers."),
    "concurrency_master":    ("Concurrency Master", "Traced goroutines, channels, select, WaitGroup, and mutexes."),
    "interface_specialist":  ("Interface Specialist", "Understood implicit interfaces, type assertions, and composition."),
    "stdlib_operative":      ("Stdlib Operative", "Catalogued Go's standard library — HTTP, JSON, context, testing."),
    "module_auditor":        ("Module Auditor", "Mapped the module system — go.mod, go.sum, versioning, GOPRIVATE."),
    "pattern_master":        ("Pattern Master", "Mastered error wrapping, middleware, DI, and table-driven tests."),
}
