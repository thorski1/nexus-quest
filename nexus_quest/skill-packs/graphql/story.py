"""
story.py - Narrative text for The Query Nexus
Theme: A rogue GraphQL gateway is leaking data through unbounded queries,
       missing authorization, and unoptimized resolver chains. CIPHER guides
       you through the schema lattice to lock down the graph.
"""

INTRO_STORY = """
The alert hit your neural feed at [bold cyan]3:12 AM[/bold cyan].

[bold white]A single GraphQL query brought down the production cluster.[/bold white]

Not a DDoS. Not a botnet. One query. Forty-seven levels deep, requesting every
relationship in the graph — users to orders to items to reviews to authors to
profiles to settings to preferences. Each level spawned N+1 resolver calls. The
database connection pool drained in eleven seconds. The circuit breakers tripped.
The mobile app showed a white screen to three hundred thousand users.

The schema had [bold white]four hundred types[/bold white]. No depth limits. No complexity analysis.
No persisted queries. Introspection was enabled in production — the attacker used
it to map the entire graph before constructing the kill query. Every field was
queryable. Every relationship was traversable. The graph was wide open.

[bold magenta]CIPHER's voice cuts through the static:[/bold magenta]

[italic cyan]"Operator. The graph is compromised. Every node, every edge, every resolver
chain is a potential attack surface. The schema was built for convenience,
not for war. We need to rebuild it — type by type, resolver by resolver,
subscription by subscription — until this graph is hardened for production.

I've mapped the breach to five critical subsystems. We start at the type lattice.
The foundation of every GraphQL API is its schema. If the types are wrong,
everything built on top of them is wrong.

Follow me through the nexus. I'll explain what went wrong at each node.
Your job is to understand the architecture and fix it."[/italic cyan]

[bold white]You are a GraphQL engineer.[/bold white] Contract operator. Schema forensics.
You've audited graph APIs for corps that thought "we have a /graphql endpoint"
meant they had a GraphQL strategy. It doesn't. A GraphQL API is a typed contract.
A contract requires a well-designed schema, optimized resolvers, secured operations,
and production-grade infrastructure. Without those, it's just an open graph
with every relationship exposed to anyone who asks.

[bold cyan]The graph is live. The resolvers are firing. Start with the type lattice.[/bold cyan]
"""

ZONE_INTROS = {
    "schema_types": """
[bold cyan]== THE TYPE LATTICE ==[/bold cyan]

[italic cyan]CIPHER:[/italic cyan] "Every graph starts with types. Scalars, objects, enums, interfaces,
unions, input types — these are the atoms of your schema. Get the types wrong and
every query, mutation, and subscription built on them inherits the defect."

The compromised schema used [bold white]String for everything[/bold white]. User IDs were strings.
Prices were strings. Dates were strings. Order statuses were free-text strings
instead of enums — the frontend had seventeen different spellings of "cancelled."

A well-typed schema is self-documenting. A developer who reads the SDL should
understand the data model without reading a single line of resolver code.

[yellow]type[/yellow] — define an object type.
[yellow]scalar[/yellow] — atomic value (Int, Float, String, Boolean, ID).
[yellow]enum[/yellow] — finite set of named values.
[yellow]interface[/yellow] — shared fields across types.
[yellow]union[/yellow] — one of several types.
[yellow]input[/yellow] — argument-only object type.

[italic]"If your schema needs comments to explain what a String field actually contains,
you need better types — not better comments."[/italic]
""",
    "queries_mutations": """
[bold cyan]== THE OPERATION GRID ==[/bold cyan]

[italic cyan]CIPHER:[/italic cyan] "Types define the shape. Operations define the access patterns.
Queries read. Mutations write. Every operation is a contract between the client
and the server — what you ask for, what you get back, what changes."

The audit found [bold white]mutations disguised as queries[/bold white]. A query called `getAndUpdateUser`
that both read the user and marked them as active. Another query that triggered
a side effect in an external payment service. Read operations that wrote.
Write operations with no input validation.

Selection sets, variables, fragments, aliases, directives — these aren't syntax
trivia. They're the tools clients use to interact with your schema efficiently.

[yellow]query[/yellow] — read data with exact field selection.
[yellow]mutation[/yellow] — write data, return the result.
[yellow]$variable[/yellow] — parameterize operations.
[yellow]fragment[/yellow] — reusable field selections.
[yellow]@directive[/yellow] — modify execution behavior.

[italic]"A mutation disguised as a query is a side effect disguised as a read.
It breaks caching, breaks expectations, and breaks trust."[/italic]
""",
    "resolvers_dataloading": """
[bold cyan]== THE RESOLVER CORE ==[/bold cyan]

[italic cyan]CIPHER:[/italic cyan] "The schema is the contract. Resolvers are the implementation.
Every field in your schema has a resolver — a function that fetches or computes
the value. And every resolver is a potential performance bottleneck."

The kill query that brought down production? It wasn't the schema's fault.
The schema was permissive, but the resolvers were catastrophic. [bold white]Every resolver
made its own database call.[/bold white] No batching. No caching. No DataLoader.

A query for 50 users with their profiles triggered [bold white]51 database queries[/bold white] —
one for the list, one per user for the profile. Scale that to 500 users
with posts, comments, and authors, and you're looking at thousands of
queries from a single GraphQL request.

[yellow]parent[/yellow] — the result from the parent resolver.
[yellow]args[/yellow] — the arguments passed to this field.
[yellow]context[/yellow] — shared state (auth, DB, loaders).
[yellow]info[/yellow] — query AST and schema metadata.

[italic]"A resolver without DataLoader is a for-loop that queries the database.
The N+1 problem isn't a bug — it's the default."[/italic]
""",
    "subscriptions_realtime": """
[bold cyan]== THE EVENT STREAM ==[/bold cyan]

[italic cyan]CIPHER:[/italic cyan] "Queries and mutations are request-response. Subscriptions are
persistent connections — the server pushes data to the client when events occur.
Real-time. Bidirectional. And if implemented wrong, a resource leak that
drains your server's memory one WebSocket at a time."

The compromised system had [bold white]twelve thousand open WebSocket connections[/bold white].
No heartbeats. No cleanup. No authentication on the WebSocket handshake.
The in-memory PubSub was broadcasting every event to every subscriber —
no filtering, no topic isolation. A user subscribed to room "general"
received events from every room in the system.

[yellow]subscribe[/yellow] — persistent connection, server pushes data.
[yellow]WebSocket[/yellow] — the transport layer for subscriptions.
[yellow]PubSub[/yellow] — the event system connecting mutations to subscribers.
[yellow]asyncIterator[/yellow] — the async stream that yields events.

[italic]"A WebSocket without authentication is an open door.
A PubSub without filtering is a broadcast to everyone."[/italic]
""",
    "graphql_production": """
[bold cyan]== THE FEDERATION MATRIX ==[/bold cyan]

[italic cyan]CIPHER:[/italic cyan] "You can build a perfect schema with optimized resolvers and
secure subscriptions — and still fail in production. The graph needs to scale.
It needs to be federated across teams. It needs caching. It needs security
at the query level, not just the endpoint level."

The final layer of the breach: [bold white]no production hardening whatsoever[/bold white].
Introspection enabled — the attacker mapped every type in the schema.
No persisted queries — arbitrary queries from any client.
No query complexity limits — the kill query scored 47,000 on complexity analysis.
No federation — a monolithic schema that five teams edited simultaneously,
breaking each other's types every sprint.

[yellow]federation[/yellow] — compose subgraphs into a supergraph.
[yellow]persisted queries[/yellow] — whitelist approved queries by hash.
[yellow]depth limiting[/yellow] — reject deeply nested queries.
[yellow]complexity analysis[/yellow] — reject expensive queries by cost.
[yellow]introspection[/yellow] — disable in production.

[italic]"A GraphQL API without production hardening isn't ready for production.
It's a prototype that someone deployed on a Friday."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "schema_types": """
[bold green]THE TYPE LATTICE — FORGED.[/bold green]

You know the type system. Scalars, objects, enums, interfaces, unions, input types —
the atoms of the schema are properly defined. Non-null modifiers enforce contracts.
Enums replace free-text strings. Input types separate arguments from output types.

The seventeen spellings of "cancelled" are now one enum value: CANCELLED.
The schema reads like documentation because the types ARE the documentation.

[bold cyan]The Operation Grid is next. Queries and mutations define the access patterns.[/bold cyan]
""",
    "queries_mutations": """
[bold green]THE OPERATION GRID — LOCKED.[/bold green]

Queries read. Mutations write. No exceptions. Variables parameterize operations.
Fragments eliminate duplication. Aliases handle field collisions.
Directives modify behavior without changing the schema.

The getAndUpdateUser query-that-mutates is now a proper mutation.
The payment side effect is behind an explicit mutation with input validation.
Operations are clean, typed, and predictable.

[bold cyan]The Resolver Core. Where the schema meets the database.[/bold cyan]
""",
    "resolvers_dataloading": """
[bold green]THE RESOLVER CORE — OPTIMIZED.[/bold green]

Resolvers follow the chain: parent, args, context, info. DataLoader batches
N+1 queries into single lookups. Context carries per-request state.
Default resolvers handle the simple cases. Explicit resolvers handle the rest.

The 51-query profile lookup is now a single batched query.
DataLoader instances are created per request — no cache pollution.
The connection pool breathes again.

[bold cyan]The Event Stream. Subscriptions bring real-time power — and real-time risk.[/bold cyan]
""",
    "subscriptions_realtime": """
[bold green]THE EVENT STREAM — SECURED.[/bold green]

Subscriptions use WebSockets with proper authentication on ConnectionInit.
PubSub events are filtered server-side — subscribers only receive relevant events.
AsyncIterators yield data efficiently. External PubSub backends handle multi-instance scaling.

The twelve thousand unmanaged WebSockets are now properly lifecycled with
heartbeats and cleanup. Room "general" subscribers no longer receive events
from every room in the system.

[bold cyan]The Federation Matrix. Production hardening — the final system.[/bold cyan]
""",
    "graphql_production": """
[bold yellow]THE FEDERATION MATRIX — DEPLOYED. GRAPH FULLY HARDENED.[/bold yellow]

[bold white]The audit is complete. The graph is production-grade.[/bold white]

Federation composes subgraphs across teams. Persisted queries whitelist approved
operations. Depth limits and complexity analysis reject attack queries before
execution. Introspection is disabled. Caching works at every layer — client
normalized cache, CDN with APQ, field-level Redis.

The kill query that scored 47,000 on complexity analysis?
Rejected at the validation layer in under a millisecond. Never touches a resolver.
Never reaches the database. The schema holds.

[bold magenta]CIPHER:[/bold magenta] [italic cyan]"The graph was an open lattice. Now it's a hardened nexus.
Every type is deliberate. Every resolver is optimized. Every subscription is
filtered. Every production risk is mitigated. This is what a GraphQL API
looks like when it's designed for war, not just for demos.

You navigated every node in the nexus. The graph holds.
Well done, operator."[/italic cyan]

[bold yellow]GRAPHQL OPERATOR STATUS: NEXUS MASTER. GRAPH: FULLY HARDENED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "schema_types": "[bold red]CIPHER: TYPE LATTICE — INTEGRITY CHECK[/bold red]\nScalars, objects, enums, interfaces, unions, input types. Prove you can define a schema that documents itself.",
    "queries_mutations": "[bold red]CIPHER: OPERATION GRID — PROTOCOL AUDIT[/bold red]\nQueries, mutations, variables, fragments, directives. Prove you understand every operation pattern in the graph.",
    "resolvers_dataloading": "[bold red]CIPHER: RESOLVER CORE — PERFORMANCE REVIEW[/bold red]\nResolver chains, context, DataLoader, batching, the N+1 problem. Prove the resolvers won't melt the database.",
    "subscriptions_realtime": "[bold red]CIPHER: EVENT STREAM — SECURITY SCAN[/bold red]\nWebSockets, PubSub, filtering, scaling, connection lifecycle. Prove the real-time layer is hardened.",
    "graphql_production": "[bold red]CIPHER: FEDERATION MATRIX — FINAL DEPLOYMENT[/bold red]\nFederation, caching, persisted queries, depth limits, complexity analysis, introspection. Prove this graph is production-grade.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Query Resolved", "Executed your first GraphQL operation. The graph acknowledged your access."),
    "type_architect": ("Schema & Types Cleared", "Forged the Type Lattice. Scalars, objects, enums, interfaces, unions — the schema is self-documenting."),
    "operation_master": ("Queries & Mutations Cleared", "Locked the Operation Grid. Queries read, mutations write, variables parameterize, fragments reuse."),
    "resolver_engineer": ("Resolvers & DataLoading Cleared", "Optimized the Resolver Core. DataLoader batches, context flows, N+1 is eliminated."),
    "realtime_sentinel": ("Subscriptions & Real-time Cleared", "Secured the Event Stream. WebSockets authenticated, PubSub filtered, connections lifecycled."),
    "production_commander": ("GraphQL in Production Cleared", "Deployed the Federation Matrix. Federated, cached, depth-limited, complexity-analyzed, introspection-disabled."),
    "streak_3": ("Clean Resolution", "3 correct in a row. Your resolver chain is warming up."),
    "streak_5": ("Optimized Pipeline", "5 in a row. Your query execution is batched and efficient."),
    "streak_10": ("ZERO LATENCY", "10 in a row. Your graph resolves with the precision of a compiled query plan."),
    "no_hints": ("No Docs Needed", "Cleared a zone without hints. The schema is already in your head."),
    "speed_demon": ("Sub-5 Response", "Answered in under 5 seconds. Faster than a cached persisted query."),
    "level_10": ("Junior Graph Engineer", "Level 10. You read schemas the way others read JSON."),
    "level_20": ("Senior Graph Architect", "Level 20. You design graphs that scale across teams and traffic spikes."),
    "level_30": ("Nexus Master", "Maximum level. You've hardened graph APIs at enterprise scale. The nexus holds."),
    "completionist": ("Full Graph Audited", "Every zone. Every challenge. Total GraphQL architecture mastery achieved."),
    "boss_slayer": ("Vulnerability Patched", "Beat your first boss challenge. The graph thought its flaws were hidden. They weren't."),
}
