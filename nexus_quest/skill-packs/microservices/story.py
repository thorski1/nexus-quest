"""
story.py — Narrative text for The Service Mesh.
Theme: A megacorp's monolithic core has fractured into hundreds of rogue services.
       The mesh is unraveling. You're the Service Architect dispatched to
       decompose, reconnect, and harden the distributed system before it collapses.
"""

INTRO_STORY = """
The page came at [bold cyan]3:12 AM[/bold cyan].

[bold white]Six hundred services.[/bold white] That's what the architecture diagram claimed.
In reality, nobody knew the real number. The original monolith — a four-million-line
Java application called COLOSSUS — had been "decomposed" over three years by seven
teams with seven different philosophies about what a microservice should be.

Some services had one endpoint. Some had forty. Some talked to each other through
REST. Some through gRPC. Some through a Kafka cluster that nobody fully understood.
Three services communicated by writing to a shared PostgreSQL table and polling it
every 500 milliseconds. Nobody remembered why.

The incident started when the Order service timed out calling the Inventory service,
which was waiting on the Pricing service, which was deadlocked on a database connection
shared with the Notification service. [bold white]A cascade.[/bold white] Four services down in eleven
seconds. The circuit breakers were configured but never tested. The retry logic
had no backoff — it amplified the failure.

The on-call engineer restarted everything. It worked. Nobody understood why it broke
or why the restart fixed it. That was the third time this month.

[bold white]You are a Service Architect.[/bold white]

[bold magenta]Contract operator. Distributed systems forensics. You've been called into
megacorps that split their monolith into a distributed monolith and called it
"microservices." It isn't. Microservices require service boundaries, independent
data ownership, resilient communication, and observable behavior. Without those,
it's just a monolith with network latency.[/bold magenta]

You've been given access to the full service registry, the message broker topology,
the tracing dashboard (what's left of it), and the saga orchestrator configs.
Your job: audit every service boundary, fix the communication patterns, harden
the mesh, and make this system observable.

The engineering director is watching.
Every architectural decision you make will be reviewed.

[bold cyan]The mesh is live. The services are waiting. Start with the fundamentals.[/bold cyan]
"""

ZONE_INTROS = {
    "microservice_fundamentals": """
[bold cyan]== THE DECOMPOSITION CHAMBER ==[/bold cyan]

Before you can fix the mesh, you need to understand why it broke.

COLOSSUS was a monolith. Billing, authentication, orders, inventory, notifications —
all in one deployable unit. It worked for three years. Then it didn't. The deploy
pipeline took 45 minutes. A bug in billing crashed the login page. Scaling meant
scaling everything, even the parts that didn't need it.

So they decomposed it. But they decomposed it wrong. They split by technical layer
instead of business domain. They shared databases across services. They created
twelve services that had to deploy together.

The result: a distributed monolith. All the complexity of microservices with none
of the benefits.

[yellow]Bounded contexts.[/yellow] — where one domain model ends and another begins.
[yellow]Service boundaries.[/yellow] — what each service owns.
[yellow]Database per service.[/yellow] — no shared data stores.
[yellow]Independent deployability.[/yellow] — the whole point.

[italic]"If you can't deploy a service without deploying three others,
you don't have microservices. You have a monolith with extra steps."[/italic]
""",
    "communication_patterns": """
[bold cyan]== THE SIGNAL GRID ==[/bold cyan]

The services are decomposed. Now they need to talk to each other.

The audit revealed [bold white]seventeen different communication patterns[/bold white] across the mesh.
REST with JSON. REST with XML (one service, built in 2019, never migrated). gRPC
between two services that a single developer set up before leaving the company.
A RabbitMQ cluster that three services publish to but nobody monitors. A Redis
pub/sub channel that silently drops messages when the subscriber is down.

And the worst pattern: synchronous chains. Order calls Pricing calls Inventory
calls Warehouse calls Shipping. Five services deep. One slow response and the
entire chain blocks. Latency compounds. Availability plummets.

[yellow]Sync vs Async.[/yellow] — when to wait, when to fire and forget.
[yellow]REST vs gRPC.[/yellow] — human-readable vs high-performance.
[yellow]Message queues.[/yellow] — decoupling in time and space.
[yellow]Event-driven architecture.[/yellow] — react to what happened, not what might.

[italic]"The fastest distributed system is the one that doesn't make
the network call at all. The second fastest uses async messaging."[/italic]
""",
    "service_discovery": """
[bold cyan]== THE REGISTRY NEXUS ==[/bold cyan]

Twenty services are running. Three just scaled from two instances to five.
One was redeployed and has a new IP address. Another was killed by the
orchestrator and hasn't restarted yet.

How does any service know where to send its requests?

The current answer: a YAML file with hardcoded IP addresses, committed to Git
three months ago. [bold white]Fourteen of the addresses are stale.[/bold white] The on-call engineer
maintains a spreadsheet that's "usually accurate." When a service can't connect,
someone SSHs into the box and checks the process list manually.

Service discovery is the nervous system of a microservices architecture.
Without it, every deployment is a game of updating configs and hoping
nothing breaks. With it, services register themselves and find each other
automatically.

[yellow]Service registry.[/yellow] — the phone book for services.
[yellow]Health checks.[/yellow] — is the service alive? Is it ready?
[yellow]Load balancing.[/yellow] — distribute traffic across instances.
[yellow]Circuit breakers.[/yellow] — fail fast when a dependency is down.

[italic]"A hardcoded IP address is not service discovery.
It's a time bomb waiting for the next deployment."[/italic]
""",
    "data_management": """
[bold cyan]== THE CONSISTENCY ENGINE ==[/bold cyan]

The hardest problem in microservices isn't communication. It's data.

In the monolith, you had transactions. BEGIN, do three things, COMMIT.
All or nothing. ACID guarantees. If step two failed, step one rolled back.
The database handled it.

In microservices, each service owns its database. There is no cross-service
transaction. Order Service commits to its database. Payment Service commits
to its database. If Payment fails after Order committed — you have an
inconsistent state across two services. The order exists but was never paid for.

[bold white]The team tried distributed transactions (two-phase commit).[/bold white] It worked in
staging. In production, it deadlocked under load and brought down four services
for ninety minutes.

You need patterns designed for distributed data. Sagas for multi-service
transactions. CQRS for read/write optimization. Event sourcing for audit trails.
Eventual consistency as the default, not the exception.

[yellow]Saga pattern.[/yellow] — local transactions with compensating actions.
[yellow]CQRS.[/yellow] — separate read and write models.
[yellow]Event sourcing.[/yellow] — store changes, not state.
[yellow]Eventual consistency.[/yellow] — embrace the delay.

[italic]"In microservices, the question isn't whether your data will be
eventually consistent. It's whether your system is designed for it."[/italic]
""",
    "observability_resilience": """
[bold cyan]== THE CHAOS FORGE ==[/bold cyan]

The system is decomposed. Services communicate. Data flows.
But when something goes wrong — and in a distributed system, something
is always going wrong — [bold white]nobody can see what happened[/bold white].

The logging setup: each service writes to its own local file. Some use JSON.
Some use plaintext. One service logs to stdout, which goes nowhere because
the container runtime wasn't configured to capture it. There is no correlation
between logs across services. When the Order service fails, you can see the
error in Order's logs. But was it caused by Payment? Inventory? The database?
Nobody knows. There are no traces.

Metrics exist — Prometheus scrapes twelve of the twenty services. The other
eight were never instrumented. The Grafana dashboard has thirty panels, four
of which show data. The rest say "No Data" because the metric names changed
and nobody updated the queries.

Resilience is even worse. No bulkheads. No graceful degradation. When the
recommendation service goes down, the entire product page returns a 500.

[yellow]Logs, metrics, traces.[/yellow] — the three pillars of observability.
[yellow]Distributed tracing.[/yellow] — follow a request across the mesh.
[yellow]Bulkheads.[/yellow] — isolate failure domains.
[yellow]Chaos engineering.[/yellow] — break it on purpose before it breaks itself.

[italic]"You can't fix what you can't see. In a distributed system,
if you're not tracing requests end-to-end, you're debugging blind."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "microservice_fundamentals": """
[bold green]THE DECOMPOSITION CHAMBER — AUDITED.[/bold green]

You know the fundamentals. Services need boundaries. Bounded contexts define
those boundaries. Each service owns its data. Independent deployability is
the measure of success.

The distributed monolith has been identified. Shared databases flagged.
Coupled deployment pipelines documented. The path from monolith to real
microservices is mapped.

[bold cyan]The Signal Grid is next. Services need to communicate — the right way.[/bold cyan]
""",
    "communication_patterns": """
[bold green]THE SIGNAL GRID — REWIRED.[/bold green]

Synchronous chains have been broken. Async messaging is in place where it
should be. gRPC handles internal high-throughput calls. REST serves the
public API. The message broker is monitored.

Service chaining is eliminated. The API Gateway aggregates what clients need.
BFF layers serve each frontend. Idempotent consumers handle duplicate messages.

[bold cyan]The Registry Nexus. Services need to find each other.[/bold cyan]
""",
    "service_discovery": """
[bold green]THE REGISTRY NEXUS — CONNECTED.[/bold green]

The YAML file with stale IPs is gone. Services register themselves on startup
and deregister on shutdown. Health checks verify readiness, not just liveness.
Circuit breakers prevent cascade failures. Load balancing distributes traffic
intelligently.

The spreadsheet is retired. The on-call engineer no longer SSHes into boxes
to check process lists. The mesh is self-healing.

[bold cyan]The Consistency Engine. Data management across service boundaries.[/bold cyan]
""",
    "data_management": """
[bold green]THE CONSISTENCY ENGINE — CALIBRATED.[/bold green]

Distributed transactions are replaced with sagas. Compensating transactions
handle failures gracefully. CQRS separates reads from writes. Event sourcing
provides a complete audit trail. The outbox pattern ensures reliable event
publishing.

Eventual consistency is understood, designed for, and communicated to the
product team. The UI handles pending states. The data flows.

[bold cyan]The Chaos Forge. Final phase. Build observability and resilience.[/bold cyan]
""",
    "observability_resilience": """
[bold yellow]\u2605 \u2605 \u2605  THE CHAOS FORGE — COMPLETE. THE MESH IS HARDENED.  \u2605 \u2605 \u2605[/bold yellow]

[bold white]The audit is complete. The mesh is operational.[/bold white]

Every service emits structured logs, metrics, and traces. OpenTelemetry
instruments the entire stack. Distributed traces follow requests end-to-end
through every service hop. Grafana dashboards show real data from real metrics.

Bulkheads isolate failure domains. Circuit breakers prevent cascades.
Graceful degradation keeps core functionality running when non-critical
services fail. Error budgets govern the release cadence.

Chaos Monkey runs weekly. The team breaks things on purpose — and the
system recovers. Every time.

[bold magenta]The mesh is hardened. The services are observable.
Microservices are not small services — they are independently deployable,
independently scalable units of business capability.
Now you know how to build systems that hold.[/bold magenta]

[bold yellow]SERVICE ARCHITECT STATUS: MESH SOVEREIGN.  SYSTEMS: FULLY HARDENED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "microservice_fundamentals": "[bold red]\u26a0  DECOMPOSITION AUDIT: The Boundary Exam[/bold red]\nMonoliths, bounded contexts, service ownership, and independent deployability. Prove you can draw the right lines.",
    "communication_patterns": "[bold red]\u26a0  SIGNAL AUDIT: The Protocol Review[/bold red]\nSync vs async, REST vs gRPC, message queues, and event-driven patterns. Prove the communication layer is sound.",
    "service_discovery": "[bold red]\u26a0  REGISTRY AUDIT: The Mesh Inspection[/bold red]\nService discovery, load balancing, health checks, and circuit breakers. Prove the mesh can self-heal.",
    "data_management": "[bold red]\u26a0  DATA AUDIT: The Consistency Review[/bold red]\nSagas, CQRS, event sourcing, and eventual consistency. Prove you can manage data across service boundaries.",
    "observability_resilience": "[bold red]\u2605  CHAOS AUDIT: The Final Forge[/bold red]\nDistributed tracing, bulkheads, chaos engineering, and graceful degradation. Prove the system survives failure.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Service Audited", "Made your first architectural decision. The mesh acknowledged your access."),
    "decomposition_master": ("Fundamentals Cleared", "Audited the decomposition layer. Bounded contexts, service boundaries, and independent deployability — the foundation is solid."),
    "signal_architect": ("Communication Cleared", "Rewired the Signal Grid. Sync, async, gRPC, message queues — the protocols are aligned."),
    "registry_keeper": ("Discovery Cleared", "Connected the Registry Nexus. Service discovery, health checks, circuit breakers — the mesh self-heals."),
    "consistency_engineer": ("Data Management Cleared", "Calibrated the Consistency Engine. Sagas, CQRS, event sourcing — the data flows correctly."),
    "chaos_forger": ("Observability Cleared", "Forged the Chaos system. Tracing, bulkheads, chaos engineering — the system survives failure."),
    "streak_3": ("Clean Deployment", "3 correct in a row. Your architectural instincts are sharpening."),
    "streak_5": ("Zero Downtime", "5 in a row. You design distributed systems the way they should run — reliably."),
    "streak_10": ("UNBREAKABLE MESH", "10 in a row. Your service mesh is battle-tested. No cascading failures. No blind spots."),
    "no_hints": ("No Docs Needed", "Cleared a zone without hints. The architecture is already in your head."),
    "speed_demon": ("Sub-5 Latency", "Answered in under 5 seconds. Faster than a service-to-service round trip."),
    "level_10": ("Junior Architect", "Level 10. You read service topologies the way others read error messages."),
    "level_20": ("Senior Architect", "Level 20. You design meshes that don't break. Teams rely on your architecture."),
    "level_30": ("Mesh Sovereign", "Maximum level. You've audited and hardened distributed systems at scale. The mesh holds."),
    "completionist": ("Full Mesh Audited", "Every zone. Every challenge. Total microservices architecture mastery achieved."),
    "boss_slayer": ("Design Flaw Found", "Beat your first boss challenge. The mesh thought its flaws were hidden. They weren't."),
}
