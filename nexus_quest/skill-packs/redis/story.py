"""
story.py - Narrative text for The Cache Matrix (Redis Quest)
Cyberpunk flavor — the Cache as a city-wide memory infrastructure.
CIPHER as the guide/handler AI.
"""

INTRO_STORY = """
The city runs on memory.

Not the kind people have — the kind that lives in silicon, measured in
nanoseconds, volatilized the instant the power cuts. Every transaction in every
storefront, every sensor reading from every traffic light, every heartbeat from
every implant in every body walking these neon-soaked streets — it all flows
through a single layer before it touches disk.

[bold red]Redis.[/bold red] The in-memory data store. The cache layer. The pub/sub backbone.

They call it [bold yellow]The Cache Matrix[/bold yellow] — a distributed grid of Redis instances spanning
forty data centers across the metropolitan zone. Twelve terabytes of hot data.
Six hundred million keys. Forty billion operations per day. The latency budget:
[bold white]sub-millisecond[/bold white]. Miss that target and transactions fail, signals drop, implants
desync, and the city's real-time nervous system develops a stutter that cascades
into chaos.

Someone has been poisoning the cache.

Not corrupting it — that would trigger alerts. They are [bold white]subtly manipulating[/bold white]
cached values. Prices shifted by fractions. Sensor readings delayed by
microseconds. Session tokens extended past their intended lifetime. Each
modification too small to flag individually, but the aggregate pattern —
the pattern is [bold magenta]deliberate[/bold magenta].

[bold cyan]CIPHER[/bold cyan] flagged it three hours ago. The AI noticed the statistical drift across
key namespaces before anyone else. The Cache Matrix is compromised and nobody
on the ops team has the depth of Redis knowledge to trace the intrusion
through the data structures.

[bold white]You are a Cache Operator.[/bold white]

[bold magenta]Ghost-class. Freelance. Recruited through seven layers of dead drops.[/bold magenta]
You don't break into systems — you understand them at a level the people who
built them never reached. They gave you access to the Redis CLI two hours ago,
routed through an encrypted tunnel that the monitoring system cannot see.

The cache is open. The poisoned keys are in there somewhere.

[bold cyan]All you have to do is know how to read the memory.[/bold cyan]
"""

ZONE_INTROS = {
    "redis_basics": """
[bold cyan]== THE KEY-VALUE SUBSTRATE ==[/bold cyan]

First contact with the matrix.

[bold cyan]CIPHER:[/bold cyan] [italic]"The substrate is the foundation layer — every operation in Redis
reduces to keys and values. Strings. The simplest data type. But 'simple'
does not mean 'trivial.' The entire session management layer, the
distributed lock infrastructure, the rate limiters — all built on
SET, GET, DEL, and the flags that modify their behavior."[/italic]

Six hundred million keys. You need to understand how they are created, read,
modified, expired, and destroyed. The poisoned keys look exactly like
legitimate ones — same namespace patterns, same TTLs, same value formats.

The only way to find them is to understand every operation that could
have created them.

[yellow]SET[/yellow], [yellow]GET[/yellow], [yellow]DEL[/yellow], [yellow]EXISTS[/yellow], [yellow]EXPIRE[/yellow], [yellow]TTL[/yellow] — the atomic operations.
Learn them. The entire matrix is built from these primitives.

[italic]"Every complex system is just simple operations composed at scale."[/italic]
""",
    "data_structures": """
[bold cyan]== THE STRUCTURE NEXUS ==[/bold cyan]

The substrate was strings. Now the architecture reveals itself.

[bold cyan]CIPHER:[/bold cyan] [italic]"The attacker is not using simple key-value pairs. The poisoned data
is embedded inside Redis data structures — lists that serve as queues,
sets that track membership, hashes that model objects, sorted sets that
maintain rankings. Each structure has its own command vocabulary and
its own performance characteristics."[/italic]

A queue of sensor readings with injected values at specific positions.
A set of authorized session tokens with one extra member that should not exist.
A hash representing a user profile with a field modified after the last
legitimate write. A sorted set leaderboard with scores shifted by fractions.

The structures are the attack surface.

[yellow]LPUSH[/yellow], [yellow]RPUSH[/yellow], [yellow]LRANGE[/yellow], [yellow]SADD[/yellow], [yellow]SMEMBERS[/yellow], [yellow]HSET[/yellow], [yellow]HGET[/yellow], [yellow]ZADD[/yellow], [yellow]ZRANGE[/yellow]

[italic]"A string stores data. A data structure stores relationships."[/italic]
""",
    "pubsub_streams": """
[bold cyan]== THE SIGNAL GRID ==[/bold cyan]

The cache is not just storage. It is a [bold white]messaging backbone[/bold white].

[bold cyan]CIPHER:[/bold cyan] [italic]"I traced the poisoned writes back to their origin. They are not
coming from application code — they are arriving through the Pub/Sub
channels and Stream consumers. The attacker injected a rogue subscriber
that intercepts messages, modifies them, and republishes. To trace this,
you need to understand how Redis moves data in real time."[/italic]

Pub/Sub: fire-and-forget channels. Messages broadcast to all subscribers.
No persistence. No replay. If you were not listening, you missed it.

Streams: persistent, append-only logs with consumer groups. Every message
is stored, acknowledged, and replayable. The event sourcing backbone of
the metropolitan infrastructure.

The rogue subscriber is somewhere in the Pub/Sub layer.
The evidence of what it did lives in the Streams.

[yellow]PUBLISH[/yellow], [yellow]SUBSCRIBE[/yellow], [yellow]XADD[/yellow], [yellow]XREAD[/yellow], [yellow]XRANGE[/yellow], [yellow]XGROUP[/yellow], [yellow]XACK[/yellow]

[italic]"Pub/Sub is the city's voice. Streams are its memory."[/italic]
""",
    "caching_patterns": """
[bold cyan]== THE TEMPORAL CACHE ==[/bold cyan]

You have found the poisoned keys. Now you need to understand [bold white]why[/bold white]
the cache accepted them.

[bold cyan]CIPHER:[/bold cyan] [italic]"The application layer implements four caching patterns across
different services. Cache-aside, write-through, write-behind, and
read-through. Each pattern has a different trust model — a different
assumption about who is allowed to write to the cache and when.
The attacker exploited the gap between those assumptions."[/italic]

A write-behind service that batches cache writes before flushing to
the database — the attacker injected values into the cache knowing
they would be blindly persisted. A cache-aside service with a
60-second TTL — the attacker replaced the cached value knowing
the application would not check the database for another minute.

Understanding the patterns is understanding the vulnerability.

[yellow]SET EX[/yellow], [yellow]SETEX[/yellow], [yellow]TTL[/yellow], [yellow]WATCH[/yellow], [yellow]MULTI[/yellow], [yellow]EXEC[/yellow]

[italic]"The cache pattern determines the blast radius."[/italic]
""",
    "redis_production": """
[bold cyan]== THE REPLICATION SPINE ==[/bold cyan]

The deepest layer. The infrastructure itself.

[bold cyan]CIPHER:[/bold cyan] [italic]"The attacker had knowledge of the cluster topology. They knew which
node held which hash slots. They knew the replication lag between
master and replica. They knew the persistence schedule — exactly when
BGSAVE runs and the window between AOF fsyncs. This was not a script
kiddie. This was someone who understands Redis at the infrastructure level."[/italic]

Persistence: RDB snapshots and AOF logs — the line between volatile cache
and durable store. Sentinel: the failover orchestrator that promotes replicas
when masters die. Cluster: the sharding layer that distributes hash slots
across nodes.

The final piece of the investigation: understanding how the attacker moved
through the cluster topology, exploiting replication lag to inject data
on replicas that would be promoted during a triggered failover.

[yellow]BGSAVE[/yellow], [yellow]BGREWRITEAOF[/yellow], [yellow]SENTINEL[/yellow], [yellow]CLUSTER[/yellow], [yellow]INFO[/yellow], [yellow]CONFIG[/yellow]

[italic]"The infrastructure is the last perimeter. If you do not understand it, you do not control it."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "redis_basics": """
[bold green]THE KEY-VALUE SUBSTRATE — MAPPED.[/bold green]

SET. GET. DEL. EXISTS. EXPIRE. TTL. NX. XX. MSET. MGET.
The atomic operations are yours. Six hundred million keys and you know
how every one of them was created, read, and destroyed.

[bold cyan]CIPHER:[/bold cyan] [italic]"Good. The substrate is clean — the poisoned keys were
not created with simple SET commands. They were injected through
data structures. The Structure Nexus is next."[/italic]

[bold cyan]The Structure Nexus opens ahead. Time to trace the data types.[/bold cyan]
""",
    "data_structures": """
[bold green]THE STRUCTURE NEXUS — TRAVERSED.[/bold green]

Lists. Sets. Hashes. Sorted Sets. Each data type with its own command
vocabulary, its own time complexity profile, its own attack surface.
You found the injected list elements, the unauthorized set members,
the modified hash fields, the shifted sorted set scores.

[bold cyan]CIPHER:[/bold cyan] [italic]"The poisoned data structures trace back to the messaging layer.
Someone injected a rogue consumer into the Pub/Sub grid.
The Signal Grid is where the intrusion originated."[/italic]

[bold cyan]The Signal Grid pulses with intercepted messages.[/bold cyan]
""",
    "pubsub_streams": """
[bold green]THE SIGNAL GRID — DECODED.[/bold green]

PUBLISH. SUBSCRIBE. XADD. XREAD. XGROUP. XACK.
The real-time messaging layer is mapped. The rogue subscriber has been
identified — injecting into a Pub/Sub channel, the poisoned data cascading
through every downstream consumer. The Stream audit trail shows every
modified message with its original and altered payloads.

[bold cyan]CIPHER:[/bold cyan] [italic]"Now the question is: why did the application layer trust
those poisoned values? The answer is in the caching patterns.
The Temporal Cache holds the vulnerability analysis."[/italic]

[bold cyan]The Temporal Cache reveals the application layer's trust assumptions.[/bold cyan]
""",
    "caching_patterns": """
[bold green]THE TEMPORAL CACHE — ANALYZED.[/bold green]

Cache-aside. Write-through. Write-behind. TTL strategies. Eviction policies.
Stampede prevention. Optimistic locking. The caching patterns are understood —
and so are their failure modes.

The attacker exploited a write-behind service that blindly persisted
cached values to the database. Poison the cache, wait for the flush,
and the database itself becomes the permanent record of the lie.

[bold cyan]CIPHER:[/bold cyan] [italic]"One layer remains. The attacker knew the cluster topology.
They exploited replication lag and persistence windows.
The Replication Spine is the final zone."[/italic]

[bold cyan]The Replication Spine hums with infrastructure telemetry.[/bold cyan]
""",
    "redis_production": """
[bold yellow]THE REPLICATION SPINE — SECURED.[/bold yellow]

RDB. AOF. Sentinel. Cluster. Hash slots. Failover elections.
Memory fragmentation. Persistence windows. Replication lag.

The full topology is mapped. The attacker triggered a Sentinel failover
by poisoning the master's health checks, causing a replica promotion.
During the promotion window — the 2-second gap where the new master
was still catching up on replication — they injected keys into the
lagging replica that became the authoritative dataset.

[bold white]The intrusion is fully traced. Every layer of the Cache Matrix walked.[/bold white]

From GET/SET to Cluster failover. From string values to consumer groups.
From TTL policies to replication lag exploits.

[bold magenta]The city's real-time nervous system has been cleaned.
The cache is consistent. The signals are true.[/bold magenta]

[bold yellow]CACHE OPERATOR STATUS: ELITE.  THE CACHE MATRIX: SECURED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "redis_basics": "[bold red]CIPHER: SUBSTRATE AUDIT[/bold red]\nThe monitoring system is checking key integrity across the namespace. Prove you understand every atomic operation — SET, GET, DEL, TTL, NX. One wrong answer and the audit flags your connection.",
    "data_structures": "[bold red]CIPHER: STRUCTURE ANALYSIS[/bold red]\nThe poisoned data is embedded in a sorted set. You need to understand how ZADD, ZRANGE, and score ordering work to extract it. Get this wrong and the evidence is overwritten by the next BGSAVE.",
    "pubsub_streams": "[bold red]CIPHER: STREAM FORENSICS[/bold red]\nA consumer in group 'processors' crashed with unacknowledged entries. The pending entries list holds the evidence. Understand XGROUP, XREADGROUP, XACK, and XCLAIM or the entries are auto-claimed by the rogue consumer.",
    "caching_patterns": "[bold red]CIPHER: PATTERN VULNERABILITY[/bold red]\nThe write-behind service is about to flush poisoned cache values to the database. You have one shot to explain the caching pattern that eliminates the stale window. Get it right and CIPHER can patch the service before the flush.",
    "redis_production": "[bold red]CIPHER: INFRASTRUCTURE BREACH[/bold red]\nThe attacker triggered a Sentinel failover by killing a master node. A replica with injected keys is being promoted. Understand the failover process — what happens to the hash slots, the replicas, and the cluster state.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Query", "Executed your first GET. The cache acknowledged you."),
    "navigator": ("Key-Value Operator", "Mastered the Key-Value Substrate. SET, GET, DEL — the atomic layer is yours."),
    "archivist": ("Structure Analyst", "Traversed the Structure Nexus. Lists, sets, hashes, sorted sets — mapped."),
    "seeker": ("Signal Decoder", "Decoded the Signal Grid. Pub/Sub and Streams hold no secrets."),
    "pipe_dream": ("Cache Architect", "Analyzed the Temporal Cache. Every caching pattern understood."),
    "necromancer": ("Infrastructure Specialist", "Secured the Replication Spine. Clustering, persistence, sentinel — mastered."),
    "streak_3": ("Cache Streak", "3 correct in a row. The cache is warming up."),
    "streak_5": ("Signal Locked", "5 in a row. Sub-millisecond precision."),
    "streak_10": ("CACHE GRANDMASTER", "10 in a row. You do not query Redis. You think in Redis."),
    "no_hints": ("Zero-Miss Run", "Cleared a zone without hints. Pure memory. No cache miss."),
    "speed_demon": ("Sub-Millisecond", "Answered in under 5 seconds. Faster than a cache lookup."),
    "level_10": ("Junior Operator", "Level 10. The cache is starting to feel familiar."),
    "level_20": ("Senior Operator", "Level 20. Redis is your native data store now."),
    "level_30": ("Cache Legend", "Maximum level. You understand Redis from GET to Cluster failover. Complete."),
    "completionist": ("Full Cache Access", "Every challenge. Every zone. Total matrix penetration achieved."),
    "boss_slayer": ("Audit Bypassed", "Beat your first boss challenge. CIPHER found nothing anomalous."),
}
