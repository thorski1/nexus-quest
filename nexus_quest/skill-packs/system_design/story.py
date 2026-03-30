"""
story.py — Narrative text for Systems Architect.
Theme: Build systems that survive anything. Scale to millions. Never go down.
A Systems Architect brought in to rebuild a platform that collapsed under its own success.
"""

INTRO_STORY = """
The postmortem landed on your desk at [bold cyan]6:47 AM[/bold cyan].

[bold white]Eleven minutes of total outage.[/bold white] Every service, every region, every customer.
A flash sale drove 40x normal traffic. The monolith couldn't scale. The database
hit connection limits. The cache stampede took down Redis. The single load balancer
became the single point of failure. Eleven minutes of zero revenue, zero trust,
and a stock price that dropped 8% before the market opened.

The CEO's message was three sentences: [bold white]"This can never happen again.
We need an architect who builds systems that don't go down.
You start Monday."[/bold white]

[bold magenta]You are a Systems Architect. You've rebuilt platforms before — ones that
outgrew their foundations, ones that collapsed under their own success, ones
that were never designed for the scale they reached. You don't just draw boxes
and arrows. You understand why systems fail and how to make them survive.[/bold magenta]

The infrastructure is live. The code is running. The users are real.
You need to redesign this platform — component by component — so it scales
to millions and never goes down again.

[bold cyan]Start with the fundamentals. Understand what breaks before you fix it.[/bold cyan]
"""

ZONE_INTROS = {
    "scalability_basics": """
[bold cyan]== SCALABILITY FUNDAMENTALS ==[/bold cyan]

Before you can scale anything, you need to understand why things don't scale.

The platform's original architecture: one big server. When traffic grew, they
bought a bigger server. When that wasn't enough, they bought the biggest server
available. When the biggest server wasn't enough, they had [bold white]no plan[/bold white].

Vertical scaling has a ceiling. Horizontal scaling has complexity. Stateless
services are the foundation of everything that follows.

[yellow]Vertical scaling[/yellow] — bigger machine. Simple. Limited.
[yellow]Horizontal scaling[/yellow] — more machines. Complex. Unlimited.
[yellow]Load balancer[/yellow] — distributes traffic across instances.
[yellow]Stateless services[/yellow] — no local state. Any instance can handle any request.

[italic]"If your architecture depends on one machine being big enough,
you don't have an architecture. You have a prayer."[/italic]
""",
    "caching": """
[bold cyan]== THE CACHE LAYER ==[/bold cyan]

The database was doing 50,000 reads per second. 80% of them were for the same
1,000 records. The same product pages, the same user profiles, the same
configuration data — fetched from disk, over and over, burning CPU on queries
that returned identical results.

Adding a cache layer cut database load by 80% in twenty minutes. The database
went from 98% CPU to 15%. The team had been planning a $200K database upgrade.
The cache cost $50/month.

[yellow]Redis[/yellow] — in-memory data structure store. Sub-millisecond reads.
[yellow]Memcached[/yellow] — simple key-value cache. Fast, no persistence.
[yellow]CDN[/yellow] — cache static assets at the edge, near users.
[yellow]Cache-aside[/yellow] — app checks cache, misses fall through to DB.
[yellow]TTL[/yellow] — time to live. How long before a cached entry expires.

[italic]"The fastest database query is the one you never make."[/italic]
""",
    "message_queues": """
[bold cyan]== THE MESSAGE QUEUE ==[/bold cyan]

The checkout flow was synchronous. User clicks Buy → charge payment → send email →
update inventory → update analytics → return confirmation. Five services, called
in sequence, each one a potential failure point. Total latency: 3.2 seconds.
If the email service was slow, the user waited. If inventory was down, the
purchase failed — even though the payment had already been charged.

Message queues decouple producers from consumers. The checkout service charges
the payment and publishes an event. Email, inventory, and analytics pick it up
asynchronously. The user sees confirmation in 400ms instead of 3.2 seconds.

[yellow]Pub/Sub[/yellow] — one message, many consumers.
[yellow]Kafka[/yellow] — ordered log. Replay. Partitions. High throughput.
[yellow]RabbitMQ[/yellow] — flexible routing. Exchanges and bindings.
[yellow]SQS[/yellow] — fully managed. Zero ops. AWS native.
[yellow]Dead letter queue[/yellow] — where poison messages go to die.

[italic]"If your user is waiting for an email to send before they see a
confirmation page, your architecture is lying about what matters."[/italic]
""",
    "microservices": """
[bold cyan]== THE MICROSERVICES MESH ==[/bold cyan]

The monolith was 2 million lines of code. Every deploy took 45 minutes. A bug
in the notification module took down the payment system because they shared a
thread pool. The team of 80 developers was stepping on each other — merge
conflicts on every pull request, integration tests that took 3 hours to run.

Microservices decompose a system by business capability. Each service owns its
data, its logic, and its deployment lifecycle. The payment service doesn't
know the notification service exists. They communicate through APIs and events.

[yellow]Bounded context[/yellow] — each service owns one business domain.
[yellow]API Gateway[/yellow] — single entry point for all client requests.
[yellow]Service mesh[/yellow] — sidecar proxies handling cross-cutting concerns.
[yellow]Circuit breaker[/yellow] — fail fast when a downstream service is down.

[italic]"A monolith isn't bad. A monolith that's too big for one team is bad.
Microservices aren't good. Microservices with the wrong boundaries are worse."[/italic]
""",
    "database_at_scale": """
[bold cyan]== DATABASE AT SCALE ==[/bold cyan]

The database was the bottleneck. It was always the bottleneck.

500 million rows in the users table. Write volume exceeded what a single primary
could handle. Read replicas were maxed out. The query planner was choosing
full table scans on queries that used to be millisecond lookups.

Scaling a database is harder than scaling an application server. App servers are
stateless — spin up another one. Databases are stateful — every instance must
agree on what the data is. That agreement is what makes scaling databases hard.

[yellow]Read replicas[/yellow] — offload reads to followers.
[yellow]Sharding[/yellow] — split data across multiple database servers.
[yellow]CQRS[/yellow] — separate read and write models.
[yellow]Event sourcing[/yellow] — store events, derive state.
[yellow]Polyglot persistence[/yellow] — right database for each job.

[italic]"You can scale your app servers to infinity. Your database is still
the single source of truth, and truth doesn't parallelize easily."[/italic]
""",
    "cdn_and_edge": """
[bold cyan]== CDN & EDGE COMPUTING ==[/bold cyan]

Users in Tokyo were experiencing 200ms latency for every static asset — images,
CSS, JavaScript bundles. The origin server was in us-east-1. Every request
crossed the Pacific Ocean twice.

After deploying a CDN, Tokyo latency dropped to 8ms. The origin server's
bandwidth costs dropped 70%. The CDN edge nodes absorbed 95% of static traffic.

But CDNs aren't just dumb caches anymore. Edge computing puts logic at the edge —
authentication, A/B testing, header manipulation, geolocation routing — all
running in under 1ms, thousands of miles from the origin.

[yellow]CDN[/yellow] — cache content at edge locations worldwide.
[yellow]Edge functions[/yellow] — run code at CDN PoPs.
[yellow]Cache-Control[/yellow] — HTTP header controlling cache behavior.
[yellow]Cache busting[/yellow] — content-hashed filenames for immutable assets.

[italic]"The speed of light is 186,000 miles per second. That's fast.
It's still not fast enough when your user is 6,000 miles from your server."[/italic]
""",
    "reliability": """
[bold cyan]== RELIABILITY ENGINEERING ==[/bold cyan]

The eleven-minute outage was preventable. Every part of it.

There was no redundancy. No failover. No circuit breakers. No bulkheads.
No chaos testing. No graceful degradation. The system was designed for the
happy path. The first time the unhappy path arrived, everything fell over.

Reliability is not an accident. It's a set of practices, patterns, and
investments that make a system survive the things that will inevitably go
wrong. Hardware fails. Networks partition. Deploys introduce bugs.
Third-party services go down. The question is not [bold white]if[/bold white] — it's [bold white]when[/bold white].

[yellow]SLA/SLO/SLI[/yellow] — promises, targets, measurements.
[yellow]Redundancy[/yellow] — no single point of failure.
[yellow]Failover[/yellow] — automatic recovery from failure.
[yellow]Chaos engineering[/yellow] — break it on purpose so it doesn't break by surprise.
[yellow]Bulkhead[/yellow] — isolate failures so they don't cascade.

[italic]"Hope is not a strategy. Redundancy is."[/italic]
""",
    "design_interviews": """
[bold cyan]== DESIGN INTERVIEWS ==[/bold cyan]

System design interviews test whether you can think about systems at scale.
Not whether you can memorize architectures — whether you can reason about
tradeoffs, estimate capacity, identify bottlenecks, and communicate your
decisions clearly.

The interviewer doesn't want a perfect design. They want to see [bold white]how you
think[/bold white]. Do you ask clarifying questions? Do you estimate scale before
choosing technology? Do you identify the hard parts? Do you discuss tradeoffs
instead of asserting one answer?

[yellow]Clarify[/yellow] — always start by asking what the system needs to do.
[yellow]Estimate[/yellow] — back-of-envelope math. Users, RPS, storage.
[yellow]High-level design[/yellow] — boxes and arrows. Data flow. APIs.
[yellow]Deep dive[/yellow] — the hardest part, in detail.
[yellow]Tradeoffs[/yellow] — every decision has a cost. Name it.

[italic]"The goal is not the right answer. The goal is the right conversation."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "scalability_basics": """
[bold green]SCALABILITY FUNDAMENTALS — UNDERSTOOD.[/bold green]

Vertical vs horizontal. Stateless vs stateful. Load balancers and bottlenecks.
You understand why the platform couldn't scale: it was designed around the
assumption that one machine would always be enough.

That assumption is always wrong, given enough time and enough users.

[bold cyan]The Cache Layer is next. The fastest request is the one you never make.[/bold cyan]
""",
    "caching": """
[bold green]THE CACHE LAYER — DEPLOYED.[/bold green]

Cache-aside. TTL. Invalidation. Redis and Memcached. CDN at the edge.
You cut database load by 80% without changing a single query. The cache
absorbed the repeated reads. The database breathes.

But the cache introduced a new problem: consistency. Stale data is the price
of speed. You know how to manage that tradeoff now.

[bold cyan]The Message Queue. Decouple the things that don't need to wait.[/bold cyan]
""",
    "message_queues": """
[bold green]THE MESSAGE QUEUE — WIRED.[/bold green]

Pub/sub for fan-out. Kafka for replay. SQS for simplicity. Dead letter queues
for poison messages. Backpressure for rate mismatches.

The checkout flow went from 3.2 seconds to 400 milliseconds. The user doesn't
wait for the email. The email doesn't know about the user.

[bold cyan]The Microservices Mesh. Break the monolith at the right boundaries.[/bold cyan]
""",
    "microservices": """
[bold green]THE MICROSERVICES MESH — MAPPED.[/bold green]

Monolith vs microservices. Bounded contexts. API gateways. Service meshes.
Circuit breakers. You understand that microservices aren't better than monoliths —
they're a different set of tradeoffs. The right boundaries matter more than
the number of services.

The payment service no longer takes down the notification service. They don't
share a thread pool anymore. They don't share anything.

[bold cyan]Database at Scale. The hardest part of distributed systems.[/bold cyan]
""",
    "database_at_scale": """
[bold green]DATABASE AT SCALE — ARCHITECTED.[/bold green]

Read replicas for read-heavy workloads. Sharding for write-heavy workloads.
CQRS for divergent read/write models. Event sourcing for audit trails and
replay. Polyglot persistence for using the right tool.

The database is no longer the bottleneck. It's three databases, each chosen
for its strengths, each scaled for its workload.

[bold cyan]CDN & Edge Computing. Bring the system closer to the user.[/bold cyan]
""",
    "cdn_and_edge": """
[bold green]CDN & EDGE COMPUTING — DEPLOYED.[/bold green]

Static assets cached at 200+ edge locations. Cache-Control headers tuned per
asset type. Content-hashed filenames for cache busting. Edge functions running
auth checks in under 1ms.

Tokyo users went from 200ms to 8ms. The origin server handles 95% less traffic.
The CDN bill is a fraction of what the bandwidth bill used to be.

[bold cyan]Reliability Engineering. Make the system survive anything.[/bold cyan]
""",
    "reliability": """
[bold green]RELIABILITY ENGINEERING — HARDENED.[/bold green]

SLAs defined. SLOs set above them. SLIs measured continuously. Automatic
failover across regions. Chaos engineering running weekly. Circuit breakers
on every downstream call. Bulkheads isolating every dependency.

The system survived a simulated region outage. It survived a chaos experiment
that killed 30% of instances. It survived a dependency going down for
20 minutes. The users noticed nothing.

[bold cyan]Design Interviews. Prove you can think about systems, not just build them.[/bold cyan]
""",
    "design_interviews": """
[bold yellow]*** DESIGN INTERVIEWS — COMPLETE. ***[/bold yellow]

[bold white]The platform is rebuilt.[/bold white]

You can design a URL shortener that handles 100M URLs per month. You can
design a chat system that delivers messages in real time to millions of
concurrent users. You can design a notification service that decouples
creation from delivery across every channel.

More importantly: you know how to think about these problems. Clarify first.
Estimate scale. Draw the high-level design. Deep dive on the hard parts.
Discuss tradeoffs. Every decision has a cost.

[bold magenta]The eleven-minute outage that started this journey? It can never happen
again. Not because the system is perfect — because it's designed to survive
its own imperfections. Redundancy. Failover. Degradation. Isolation.

Systems don't fail because of bad luck. They fail because of bad design.
You design systems that don't go down.[/bold magenta]

[bold yellow]SYSTEMS ARCHITECT STATUS: PRINCIPAL. PLATFORM: REBUILT.[/bold yellow]
""",
}

BOSS_INTROS = {
    "scalability_basics": "[bold red]ARCHITECTURE REVIEW: The Scaling Ceiling[/bold red]\nThe server is maxed out. Prove you understand vertical vs horizontal scaling and where bottlenecks hide.",
    "caching": "[bold red]CACHE AUDIT: The Stale Data Problem[/bold red]\nThe cache hit ratio is 40%. Stale data is leaking to production. Prove you understand cache patterns, TTL, and invalidation.",
    "message_queues": "[bold red]QUEUE FORENSICS: The Dead Letter Pile[/bold red]\nThe dead letter queue has 50,000 messages. Consumers are falling behind. Prove you understand async processing and backpressure.",
    "microservices": "[bold red]SERVICE BOUNDARY REVIEW: The Distributed Monolith[/bold red]\nFive microservices sharing one database. Cascading failures everywhere. Prove you understand service boundaries and resilience patterns.",
    "database_at_scale": "[bold red]DATABASE CRISIS: The Sharding Decision[/bold red]\n500 million rows. Single primary at capacity. Prove you understand replication, sharding, and the CAP theorem.",
    "cdn_and_edge": "[bold red]LATENCY INVESTIGATION: The Global User Problem[/bold red]\nUsers on three continents. 200ms latency from origin. Prove you understand CDN caching, edge computing, and cache headers.",
    "reliability": "[bold red]INCIDENT RESPONSE: The Cascading Failure[/bold red]\nOne dependency went down. Everything followed. Prove you understand SLOs, circuit breakers, bulkheads, and graceful degradation.",
    "design_interviews": "[bold red]*** FINAL DESIGN REVIEW: The Whiteboard Session ***[/bold red]\nDesign a system from scratch. Clarify. Estimate. Draw. Deep dive. Defend your tradeoffs. Prove you think like an architect.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Diagram Drawn", "Made your first architecture decision. The whiteboard acknowledged your access."),
    "scale_master": ("Scale Understood", "Cleared Scalability Fundamentals. Vertical has a ceiling. Horizontal has no limit."),
    "cache_architect": ("Cache Deployed", "Cleared The Cache Layer. The fastest database query is the one you never make."),
    "queue_operator": ("Queues Wired", "Cleared The Message Queue. Producers don't wait for consumers. Events flow async."),
    "service_designer": ("Mesh Mapped", "Cleared The Microservices Mesh. Bounded contexts. API gateways. Circuit breakers. The monolith is decomposed."),
    "data_engineer": ("Database Scaled", "Cleared Database at Scale. Replicas, shards, CQRS, event sourcing — the database is no longer the bottleneck."),
    "edge_deployer": ("Edge Deployed", "Cleared CDN & Edge Computing. 200ms became 8ms. The content lives where the users live."),
    "reliability_eng": ("System Hardened", "Cleared Reliability Engineering. SLOs defined. Chaos tested. The system survives anything."),
    "design_master": ("Architect Certified", "Cleared Design Interviews. You don't just build systems — you reason about them."),
    "streak_3": ("Clean Run", "3 correct in a row. Your architecture instincts are forming."),
    "streak_5": ("Cached Knowledge", "5 in a row. Knowledge is being served from memory now."),
    "streak_10": ("IMMUTABLE ARCHITECTURE", "10 in a row. Your understanding is battle-tested. Production-ready."),
    "no_hints": ("No Hints Needed", "Cleared a zone without hints. The design patterns are already in your head."),
    "speed_demon": ("Sub-5 Decision", "Answered in under 5 seconds. The architecture was already clear before you read the options."),
    "level_10": ("Senior Architect", "Level 10. You see bottlenecks before they happen."),
    "level_20": ("Staff Architect", "Level 20. You design systems the way others read documentation — fluently."),
    "level_30": ("Principal Architect", "Maximum level. You build systems that scale to millions and never go down. The whiteboard is yours."),
    "completionist": ("Full Platform Rebuilt", "Every zone. Every challenge. The platform is rebuilt from the ground up."),
    "boss_slayer": ("Bottleneck Found", "Beat your first boss challenge. The system thought it was fine. It wasn't."),
}
