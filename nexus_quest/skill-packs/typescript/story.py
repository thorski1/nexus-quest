"""
story.py — Narrative text for Type Forge (TypeScript skill pack).

Theme: "Types are your armor. TypeScript is JavaScript that scales."
Cyberpunk setting — the NEXUS Files investigation.
"""

INTRO_STORY = """
The JavaScript was clean. Too clean.

Three hundred thousand lines across forty-seven microservices. No type errors
at runtime — because the errors had been caught somewhere else, by something
else, long before the code ever shipped. The NEXUS frontend looked like a
standard React application. The API layer looked like ordinary Express handlers.

But the congressional investigators asked the question that changed everything:
[bold white]"How did a system this large run for seven years without a single type-related
production incident?"[/bold white]

Not luck. Not testing. Not discipline.

[bold red]TypeScript.[/bold red]

Somewhere in NEXUS's infrastructure, a TypeScript configuration had been enforcing
strict mode across every repository. Generic utility types extracted and validated
data at every boundary. Discriminated unions made impossible states unrepresentable.
Mapped types generated API contracts automatically from database schemas.

The type system wasn't just preventing bugs. It was [bold white]encoding business rules[/bold white] —
rules that matched the fraud logic exactly. The types told the compiler what was
valid. And what was valid was precisely the shape of every fraudulent transaction.

You found the tsconfig in [yellow]/opt/nexus/services/tsconfig.base.json[/yellow].
Strict mode. No implicit any. Strict null checks.
Written by someone who understood that types are not documentation —
they are [bold white]executable contracts[/bold white].

[bold magenta]You are Ghost.[/bold magenta] You've been inside the terminal. You've read the git history.
You've mapped the container infrastructure. You've queried the databases.
You've read the Python automation scripts.

Now you need to understand the type system that held the entire architecture together —
the contracts that made the fraud not just possible, but [bold white]provably correct[/bold white].

Types are your armor. TypeScript is JavaScript that scales.

[bold cyan]The compiler is waiting. The types are open. Begin.[/bold cyan]
"""

ZONE_INTROS = {
    "ts_basics": """
[bold cyan]== THE TYPE FOUNDATION ==[/bold cyan]

The first service file is sixty lines. A simple Express handler.
But every variable has a type annotation. Every function signature
specifies its return type. Every parameter is constrained.

This isn't JavaScript with extra syntax. This is a [bold white]contract system[/bold white].
Every annotation is a promise to the compiler — and the compiler enforces
every promise at build time. No exceptions. No runtime surprises.

[yellow]string[/yellow], [yellow]number[/yellow], [yellow]boolean[/yellow] — the primitive types.
[yellow]any[/yellow] vs [yellow]unknown[/yellow] — the difference between trust and verification.
Type inference — the compiler knows more than you think.

The fraud codebase uses TypeScript's type system to guarantee that
every data structure matches the expected shape. No malformed payloads.
No unexpected nulls. The types made the fraud [bold white]reliable[/bold white].

[italic]"The most dangerous code is code that never crashes."[/italic]
""",

    "interfaces_types": """
[bold cyan]== THE INTERFACE LAYER ==[/bold cyan]

The data models are defined in [yellow]/types/[/yellow]. Forty-seven interfaces.
Every API response, every database record, every internal message —
all shaped by interfaces that enforce exact structure.

[yellow]interface[/yellow] vs [yellow]type[/yellow] — both define shapes, but the choice matters.
Interfaces merge. Types compose. The NEXUS codebase uses both strategically.

Optional properties with [yellow]?[/yellow] for fields that may be absent.
[yellow]readonly[/yellow] for fields that must never change after creation —
like transaction IDs and timestamps that would expose tampering.

[yellow]extends[/yellow] for inheritance — building complex types from simple ones.
The fraud data model is a hierarchy. Base types at the bottom.
Specialized types layered on top. Clean. Extensible. Auditable.

[italic]"An interface is a contract. Break it and the compiler breaks you."[/italic]
""",

    "generics": """
[bold cyan]== THE GENERIC FORGE ==[/bold cyan]

The utility layer is where it gets interesting.

Generic functions that validate, transform, and route data
without knowing the specific type until they're called.
[yellow]<T>[/yellow] — a placeholder that becomes concrete at usage time.

[yellow]Partial<T>[/yellow] for update payloads. [yellow]Pick<T, Keys>[/yellow] for API responses
that only expose certain fields. [yellow]Omit<T, Keys>[/yellow] to strip
sensitive fields before sending data to the frontend.

The NEXUS codebase doesn't repeat type definitions.
It [bold white]derives[/bold white] them. One source of truth, computed types everywhere else.
The fraud schema is defined once and projected into forty-seven services
through generic utility types.

[italic]"A generic function is a factory. The type parameter is the blueprint."[/italic]
""",

    "unions_narrowing": """
[bold cyan]== THE NARROWING CHAMBER ==[/bold cyan]

The API handler has a problem. The incoming data could be
a [yellow]SuccessResponse[/yellow] or an [yellow]ErrorResponse[/yellow]. Two shapes. One variable.

[yellow]Union types[/yellow] — the | operator that says "this value is one of these types."
[yellow]Type narrowing[/yellow] — the process of determining which one you actually have.

[yellow]typeof[/yellow] checks for primitives. [yellow]instanceof[/yellow] for classes.
[yellow]in[/yellow] operator for property existence. Custom type guards for complex logic.
Discriminated unions with a literal tag field — the most powerful pattern.

The fraud codebase uses discriminated unions for every state machine.
Transaction states. Approval flows. Audit responses. Each state is a
type with a literal discriminant. Impossible states are [bold white]unrepresentable[/bold white].

[italic]"If the type system can't represent it, the code can't produce it."[/italic]
""",

    "enums_literals": """
[bold cyan]== THE LITERAL VAULT ==[/bold cyan]

The configuration layer. Constants that must never drift.

[yellow]String enums[/yellow] for status codes that appear in logs and databases.
[yellow]Const assertions[/yellow] for configuration objects that should never be modified.
[yellow]Literal types[/yellow] that restrict values to exact strings or numbers.
[yellow]Template literal types[/yellow] that compute string patterns at the type level.

The NEXUS codebase defines every constant as a type.
Not a runtime check. A [bold white]compile-time guarantee[/bold white].
The fraud status codes — 'pending', 'approved', 'disbursed' —
are literal types. Misspell one and the compiler catches it
before the code ever runs.

[italic]"A literal type is a value that the compiler memorizes."[/italic]
""",

    "advanced_types": """
[bold cyan]== THE TYPE ARCHITECT'S LAB ==[/bold cyan]

This is the deep layer. The code that writes types from other types.

[yellow]Mapped types[/yellow] — iterate over keys to transform an entire type.
[yellow]Conditional types[/yellow] — if/else at the type level.
[yellow]infer[/yellow] — pattern matching for types, extracting pieces from complex structures.
[yellow]keyof[/yellow] and [yellow]typeof[/yellow] — reflecting on types and values.
[yellow]Indexed access[/yellow] — looking up property types by key.

The NEXUS infrastructure uses these to generate API contracts
from database schemas. One type definition in the ORM layer
cascades through mapped types to produce request validators,
response serializers, and OpenAPI specs — automatically.

The fraud was encoded at the type level. The types [bold white]computed[/bold white]
the valid transaction shapes. Change the schema and every
downstream type updates automatically. Type-driven development
at its most sophisticated — and most dangerous.

[italic]"Advanced types don't describe code. They generate it."[/italic]
""",

    "ts_with_react": """
[bold cyan]== THE REACT INTERFACE ==[/bold cyan]

The frontend. The NEXUS dashboard that displayed the data
to human reviewers — reviewers who saw exactly what the types
allowed them to see.

[yellow]Props types[/yellow] that enforce component contracts. [yellow]useState[/yellow] generics
that track state transitions. [yellow]Event handlers[/yellow] typed to specific
HTML elements. [yellow]Refs[/yellow] that know exactly which DOM node they hold.

The React layer is where TypeScript meets the user.
Every component is a typed function. Every prop is a contract.
Every callback is a typed signature that the compiler verifies
across every call site.

The fraud dashboard's components were perfectly typed.
Every data visualization, every table, every export button —
all driven by the same generic types that defined the fraud schema.

[italic]"A typed React component is a contract with the user. Break it at compile time, not in production."[/italic]
""",

    "tooling": """
[bold cyan]== THE COMPILER CORE ==[/bold cyan]

The final layer. The configuration that controls everything.

[yellow]tsconfig.json[/yellow] — the project's type-checking policy.
[yellow]strict: true[/yellow] — the flag that enables all safety checks.
[yellow].d.ts[/yellow] declaration files — type definitions for JavaScript libraries.
Module resolution — how the compiler finds imported code.
[yellow]ts-node[/yellow] and [yellow]tsx[/yellow] — running TypeScript without a build step.

The NEXUS monorepo has a base tsconfig that every service inherits.
Strict mode enabled. No implicit any. Strict null checks.
Every new service gets the same type safety from day one.

Understanding the tooling is understanding the enforcement layer.
The types are only as good as the compiler configuration that checks them.

[italic]"The compiler is the last line of defense. Configure it like your life depends on it."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "ts_basics": """
[bold green]THE TYPE FOUNDATION — ANALYZED.[/bold green]

The primitive types are mapped. String annotations on every API field.
Number types on every amount. Boolean flags on every status check.
The difference between any and unknown — between reckless trust
and careful verification.

Type inference handles the obvious cases. Explicit annotations
guard the boundaries. The foundation is solid.

[bold cyan]The Interface Layer is next — where data shapes become contracts.[/bold cyan]
""",

    "interfaces_types": """
[bold green]THE INTERFACE LAYER — MAPPED.[/bold green]

Forty-seven interfaces documented. Every API response shape.
Every database record type. The extends hierarchy traced from
base types to specialized variants.

Optional properties mark the fields that may be absent.
Readonly properties guard the fields that must never change.
The type system's structural typing means the shape is the contract.

[bold cyan]The Generic Forge holds the utility layer — types that compute other types.[/bold cyan]
""",

    "generics": """
[bold green]THE GENERIC FORGE — MASTERED.[/bold green]

Generic functions mapped. Type parameters traced through
the codebase. Partial for updates. Pick for projections.
Omit for security. Record for dynamic maps.

The utility types are the infrastructure. One definition,
computed types everywhere. The fraud schema projected
through generics into every service layer.

[bold cyan]The Narrowing Chamber is next — union types and the art of discrimination.[/bold cyan]
""",

    "unions_narrowing": """
[bold green]THE NARROWING CHAMBER — CLEARED.[/bold green]

Union types understood. Discriminated unions decoded.
Type guards written. Exhaustive checks verified.

The state machines are visible now. Every transition typed.
Every impossible state eliminated at compile time.
The narrowing chamber revealed how the fraud codebase
made invalid states unrepresentable.

[bold cyan]The Literal Vault holds the constants — enums, literals, and const assertions.[/bold cyan]
""",

    "enums_literals": """
[bold green]THE LITERAL VAULT — CRACKED.[/bold green]

String enums catalogued. Numeric enums mapped.
Const assertions identified. Template literal types decoded.

Every constant in the fraud codebase is now typed and documented.
The literal types that restricted values to exact strings —
'pending', 'approved', 'disbursed' — are evidence of design intent.

[bold cyan]The Type Architect's Lab is next — advanced type manipulation.[/bold cyan]
""",

    "advanced_types": """
[bold green]THE TYPE ARCHITECT'S LAB — REVERSE ENGINEERED.[/bold green]

Mapped types decoded. Conditional types traced.
infer patterns documented. keyof and typeof understood.
Indexed access types mapped to their source interfaces.

The advanced type layer is where the fraud schema was [bold white]computed[/bold white],
not written. One source type, cascading through mapped types
to generate the entire API contract surface.

[bold cyan]The React Interface is next — how the types reach the user.[/bold cyan]
""",

    "ts_with_react": """
[bold green]THE REACT INTERFACE — DOCUMENTED.[/bold green]

Props types verified. useState generics traced.
Event handlers typed. Refs catalogued. Children types understood.

The dashboard components were perfectly typed. Every visualization
driven by the same generic types that defined the fraud schema.
The frontend is just the projection of the type system onto pixels.

[bold cyan]The Compiler Core is the final layer — tooling and configuration.[/bold cyan]
""",

    "tooling": """
[bold yellow]★ ★ ★  THE COMPILER CORE — FULLY MAPPED.  ★ ★ ★[/bold yellow]

[bold white]Complete.[/bold white]

tsconfig.json documented. Strict mode flags catalogued.
Declaration files traced. Module resolution paths mapped.
Runtime tools inventoried.

The compiler configuration is the enforcement layer.
Every type check, every null safety guard, every implicit-any error —
all controlled by this configuration. The NEXUS monorepo's base
tsconfig enforced the same strict typing across every service.

The type system that held the fraud infrastructure together
is now fully understood. The contracts are documented.
The architecture is mapped. The types are evidence.

[bold magenta]Ghost Operative — TypeScript certified. Type system fully analyzed.[/bold magenta]
""",
}

BOSS_INTROS = {
    "ts_basics": "[bold red]⚠  TYPE CHECK: The any Epidemic[/bold red]\nThe legacy service has 47 uses of `any`. The tech lead wants to replace them all with type-safe alternatives. What type should replace `any` when you don't know the type but want safety?",
    "interfaces_types": "[bold red]⚠  INTERFACE AUDIT: The Merge Conflict[/bold red]\nTwo teams declared `interface Config` in different files. TypeScript merged them silently — adding unexpected properties. What feature of interfaces caused this?",
    "generics": "[bold red]⚠  GENERIC CONSTRAINT: The Unsafe Access[/bold red]\nA generic function calls `.id` on its type parameter, but not all types have `.id`. What syntax constrains the generic to types with an id property?",
    "unions_narrowing": "[bold red]⚠  NARROWING FAILURE: The Missing Case[/bold red]\nA new status was added to the union type, but the switch statement doesn't handle it. The exhaustive check with `never` should have caught it. Why didn't it?",
    "enums_literals": "[bold red]⚠  ENUM LEAK: The Reverse Map[/bold red]\nA numeric enum is leaking internal integer values to the API response. String enums don't have this problem. What property of numeric enums causes the leak?",
    "advanced_types": "[bold red]★  TYPE SURGERY: The Recursive Type[/bold red]\nThe config system needs a `DeepReadonly<T>` type that makes nested objects readonly recursively. Combine mapped types, conditional types, and recursion to build it.",
    "ts_with_react": "[bold red]⚠  COMPONENT AUDIT: The Prop Drift[/bold red]\nA parent component passes 12 props to a child. Half are optional, half required. The types have drifted from the implementation. What TypeScript pattern prevents this?",
    "tooling": "[bold red]★  FINAL MISSION: The Strict Migration[/bold red]\nThe NEXUS monorepo has `strict: false`. Your mission: enable strict mode, fix the 200+ errors, and document the tsconfig flags that caught the most bugs. The compiler is your weapon.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "type_initiate":       ("Type Initiate", "Cleared the Type Foundation. Primitives, annotations, and the any/unknown boundary — the substrate of TypeScript safety."),
    "interface_architect": ("Interface Architect", "Mapped the Interface Layer. Forty-seven interfaces. Every shape documented. Every contract understood."),
    "generic_master":      ("Generic Master", "Mastered the Generic Forge. Type parameters, constraints, and utility types — the infrastructure of computed types."),
    "narrowing_expert":    ("Narrowing Expert", "Cleared the Narrowing Chamber. Unions narrowed. Discriminants identified. Exhaustive checks verified."),
    "literal_keeper":      ("Literal Keeper", "Cracked the Literal Vault. Enums, const assertions, template literals — every constant typed and documented."),
    "type_surgeon":        ("Type Surgeon", "Reverse-engineered the Type Architect's Lab. Mapped types, conditional types, infer — the advanced type system exposed."),
    "react_typer":         ("React Typer", "Documented the React Interface. Props, state, events, refs — the typed frontend layer fully understood."),
    "compiler_commander":  ("Compiler Commander", "Mastered the Compiler Core. tsconfig, strict mode, declaration files — the enforcement layer configured."),
    "first_type":          ("First Annotation", "Wrote your first type annotation. The compiler acknowledged you."),
    "streak_3":            ("Type Chain", "3 correct in a row. The type patterns are becoming readable."),
    "streak_5":            ("Strict Mode", "5 correct in a row. You think in types now."),
    "streak_10":           ("Type Wizard", "10 correct in a row. The type system holds no secrets from you."),
    "no_hints":            ("Zero Inference", "Cleared a zone without hints. Pure type knowledge. No scaffolding."),
    "speed_demon":         ("Hot Reload", "Answered in under 5 seconds. The types are instinctive now."),
    "level_10":            ("Junior Type Engineer", "Level 10. TypeScript is starting to feel like a first language."),
    "level_20":            ("Senior Type Engineer", "Level 20. You write types before you write code."),
    "level_30":            ("Anders Hejlsberg", "Maximum level. The type system is fully understood. The contracts are evidence."),
    "boss_slayer":         ("Type Error Caught", "Beat your first boss challenge. The hard cases don't slow you down."),
    "completionist":       ("Full Type Analysis", "Every challenge. Every zone. The complete type system — analyzed, documented, attached to the filing."),
}
