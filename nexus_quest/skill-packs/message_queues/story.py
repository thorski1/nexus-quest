"""
story.py - Narrative text for The Signal Highway (Message Queues Quest)
Cyberpunk flavor — message queues as the city's nervous system.
CIPHER as the guide/handler AI.
"""

INTRO_STORY = """
The city never sleeps because the city never stops talking.

Every transaction, every sensor ping, every drone handoff, every implant
heartbeat — they all move as [bold white]messages[/bold white]. Not stored. Not queried. [bold cyan]Routed.[/bold cyan]
Through brokers and buses and topics and queues, an invisible river of
structured data flowing at eight hundred million events per hour.

They call it [bold yellow]The Signal Highway[/bold yellow] — the asynchronous backbone that connects
every service in the metropolitan grid. Payment processors fire events to
inventory systems. Traffic sensors publish readings to optimization engines.
Medical implants stream telemetry to monitoring clusters. No service calls
another directly. Everything goes through the highway.

[bold red]Someone is poisoning the signals.[/bold red]

Not dropping them — that would trigger dead letter alerts. They are
[bold white]rerouting[/bold white] messages. Order confirmations arriving at the wrong consumer
group. Payment events duplicated across partitions they should never touch.
Sensor data replayed from three hours ago, injected into live streams as
if they were current. The routing keys are being rewritten mid-flight.

[bold cyan]CIPHER[/bold cyan] detected the anomaly when consumer lag metrics diverged from
expected patterns. The Signal Highway is compromised and the ops team
cannot trace the intrusion — they understand their own services, but
nobody understands the [bold magenta]messaging infrastructure[/bold magenta] end to end.

[bold white]You are a Signal Operator.[/bold white]

[bold magenta]Ghost-class. Freelance. Recruited through encrypted event channels.[/bold magenta]
You do not build services — you understand the invisible layer between them.
The brokers. The exchanges. The topics. The patterns that keep distributed
systems from descending into chaos.

The highway is open. The poisoned signals are flowing.

[bold cyan]All you have to do is know how to trace the messages.[/bold cyan]
"""

ZONE_INTROS = {
    "messaging_fundamentals": """
[bold cyan]== THE DISPATCH CORE ==[/bold cyan]

First contact with the highway's foundation.

[bold cyan]CIPHER:[/bold cyan] [italic]"Before you can trace poisoned messages, you need to understand
how messages move. Point-to-point. Publish-subscribe. The delivery
guarantees — at-most-once, at-least-once, exactly-once. The
acknowledgment handshake between broker and consumer. The dead letter
queues where failed messages go to die. Every messaging system on
the highway is built from these primitives."[/italic]

Eight hundred million events per hour. Each one follows a delivery contract.
The attacker is exploiting the gaps between what the contract promises and
what the implementation actually does.

[yellow]publish[/yellow], [yellow]subscribe[/yellow], [yellow]ack[/yellow], [yellow]nack[/yellow], [yellow]DLQ[/yellow], [yellow]at-least-once[/yellow], [yellow]exactly-once[/yellow]

[italic]"Every distributed system is a messaging system. Most just don't know it yet."[/italic]
""",
    "rabbitmq": """
[bold cyan]== THE EXCHANGE LABYRINTH ==[/bold cyan]

The first broker on the highway. The one that routes by rules.

[bold cyan]CIPHER:[/bold cyan] [italic]"RabbitMQ handles the city's transactional messaging — order processing,
payment routing, notification dispatch. The attacker manipulated exchange
bindings. Messages published with routing key 'payment.completed' are
being routed to queues that should only receive 'payment.pending'. The
topic exchange wildcards have been altered. To trace this, you need to
understand exchanges, bindings, routing keys, and the dead letter
infrastructure."[/italic]

Four exchange types. Thousands of bindings. The routing topology is a
labyrinth and somewhere inside it, the attacker rewired the paths.

[yellow]direct[/yellow], [yellow]fanout[/yellow], [yellow]topic[/yellow], [yellow]headers[/yellow], [yellow]binding[/yellow], [yellow]routing key[/yellow], [yellow]DLX[/yellow], [yellow]QoS[/yellow]

[italic]"The exchange is the brain. The bindings are the synapses. One wrong connection and the whole nervous system misfires."[/italic]
""",
    "apache_kafka": """
[bold cyan]== THE PARTITION STREAM ==[/bold cyan]

The river of events. Immutable. Append-only. Replayable.

[bold cyan]CIPHER:[/bold cyan] [italic]"Kafka is the backbone of the highway's event streaming layer. Every
sensor reading, every state change, every audit event — written to
topics, partitioned by key, consumed by groups. The attacker injected
a rogue producer that writes to partitions directly, bypassing the
key-based routing. Events for user-7291 are appearing in partition 3
when they should only ever land in partition 7. Consumer groups are
rebalancing erratically because phantom consumers join and leave."[/italic]

Topics. Partitions. Offsets. Consumer groups. Rebalances. ISR.
The streaming layer is deep and the attacker knows its internals.

[yellow]topic[/yellow], [yellow]partition[/yellow], [yellow]offset[/yellow], [yellow]consumer group[/yellow], [yellow]rebalance[/yellow], [yellow]ISR[/yellow], [yellow]compaction[/yellow]

[italic]"Kafka does not forget. Every event is written in stone. The question is whether you can read the stone."[/italic]
""",
    "cloud_messaging": """
[bold cyan]== THE CLOUD RELAY ==[/bold cyan]

The managed layer. Where the highway meets the hyperscalers.

[bold cyan]CIPHER:[/bold cyan] [italic]"The metropolitan grid runs hybrid infrastructure — some brokers
on-premise, others in the cloud. SQS queues feeding Lambda consumers.
SNS topics fanning out to SQS, HTTP endpoints, and Lambda simultaneously.
Google Pub/Sub handling the sensor telemetry pipeline. EventBridge routing
cross-account events between government and commercial services. The
attacker is exploiting the differences between these services — SQS
visibility timeouts that are too short, EventBridge rules that are too
broad, Pub/Sub acknowledgment deadlines that expire before processing
completes."[/italic]

Each cloud provider implements messaging differently. Same concepts,
different semantics. The devil is in the configuration.

[yellow]SQS[/yellow], [yellow]SNS[/yellow], [yellow]Pub/Sub[/yellow], [yellow]EventBridge[/yellow], [yellow]FIFO[/yellow], [yellow]visibility timeout[/yellow], [yellow]ack deadline[/yellow]

[italic]"The cloud abstracts the broker. It does not abstract the responsibility."[/italic]
""",
    "patterns_best_practices": """
[bold cyan]== THE ARCHITECT'S CODEX ==[/bold cyan]

The deepest layer. The patterns that hold everything together.

[bold cyan]CIPHER:[/bold cyan] [italic]"You have traced the poisoned signals through every broker and every
cloud service. Now the question is: why did the architecture allow it?
The answer is in the patterns — or the absence of them. No outbox pattern
means dual-write failures. No idempotency keys means duplicate processing.
No saga coordination means partial failures leave the system in an
inconsistent state. The attacker did not just exploit the brokers — they
exploited the architectural gaps between them."[/italic]

Event sourcing. Saga orchestration. Transactional outbox. Idempotency.
Backpressure. The patterns that separate a messaging system from a
messaging [bold white]architecture[/bold white].

[yellow]event sourcing[/yellow], [yellow]saga[/yellow], [yellow]outbox[/yellow], [yellow]idempotency[/yellow], [yellow]backpressure[/yellow], [yellow]CDC[/yellow], [yellow]retry[/yellow]

[italic]"Tools are chosen. Patterns are earned. The architecture is the last line of defense."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "messaging_fundamentals": """
[bold green]THE DISPATCH CORE — MAPPED.[/bold green]

Point-to-point. Pub/sub. At-least-once. At-most-once. Exactly-once.
Acknowledgments. Dead letter queues. Message ordering guarantees.
The fundamental contracts that every broker implements.

[bold cyan]CIPHER:[/bold cyan] [italic]"Good. The fundamentals are clean — you understand how messages
should move. Now let's see how they actually move through the first
broker. The Exchange Labyrinth is next."[/italic]

[bold cyan]The Exchange Labyrinth opens ahead. Time to trace the routing rules.[/bold cyan]
""",
    "rabbitmq": """
[bold green]THE EXCHANGE LABYRINTH — NAVIGATED.[/bold green]

Direct. Fanout. Topic. Headers. Bindings. Routing keys. QoS. DLX.
Publisher confirms. Durable queues. Persistent messages.
The RabbitMQ routing topology is fully mapped.

[bold cyan]CIPHER:[/bold cyan] [italic]"The tampered bindings have been identified. But the attacker also
injected events into the streaming layer. Kafka's partition streams
hold the next piece of the intrusion."[/italic]

[bold cyan]The Partition Stream flows with immutable events.[/bold cyan]
""",
    "apache_kafka": """
[bold green]THE PARTITION STREAM — DECODED.[/bold green]

Topics. Partitions. Offsets. Consumer groups. Rebalances. ISR. Compaction.
The append-only event log is understood — every offset tracked, every
consumer group's lag measured, every partition's leader identified.

[bold cyan]CIPHER:[/bold cyan] [italic]"The rogue producer has been traced. But the attack spans beyond
self-managed brokers. The cloud messaging services carry the next
set of poisoned signals. The Cloud Relay is waiting."[/italic]

[bold cyan]The Cloud Relay hums with managed infrastructure.[/bold cyan]
""",
    "cloud_messaging": """
[bold green]THE CLOUD RELAY — SECURED.[/bold green]

SQS. SNS. Google Pub/Sub. EventBridge. Visibility timeouts. FIFO queues.
Fanout patterns. Acknowledgment deadlines. Event rules and filters.
The managed messaging layer is understood.

[bold cyan]CIPHER:[/bold cyan] [italic]"One layer remains. The attacker exploited more than configuration —
they exploited missing patterns. The Architect's Codex holds the
final analysis."[/italic]

[bold cyan]The Architect's Codex reveals the missing patterns.[/bold cyan]
""",
    "patterns_best_practices": """
[bold yellow]THE ARCHITECT'S CODEX — MASTERED.[/bold yellow]

Event sourcing. Saga. Outbox. Idempotency. Backpressure. CDC.
Exponential backoff with jitter. Circuit breakers. Choreography
versus orchestration. The patterns that separate infrastructure
from architecture.

[bold white]The intrusion is fully traced. Every layer of the Signal Highway walked.[/bold white]

From publish/subscribe to distributed sagas. From dead letter queues to
transactional outbox. From RabbitMQ exchanges to Kafka consumer groups
to cloud-managed services.

The attacker exploited dual-write gaps where no outbox pattern existed.
They replayed messages where no idempotency keys were checked. They
triggered cascade failures where no backpressure was implemented.

[bold magenta]The city's asynchronous nervous system has been repaired.
The signals are clean. The highway is secure.[/bold magenta]

[bold yellow]SIGNAL OPERATOR STATUS: ELITE.  THE SIGNAL HIGHWAY: SECURED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "messaging_fundamentals": "[bold red]CIPHER: DISPATCH AUDIT[/bold red]\nThe monitoring system is validating delivery guarantees across the highway. Prove you understand point-to-point vs pub/sub, delivery semantics, and acknowledgment protocols. One wrong answer and the audit flags your connection.",
    "rabbitmq": "[bold red]CIPHER: EXCHANGE ANALYSIS[/bold red]\nThe attacker rewired a topic exchange binding. Messages with routing key 'order.eu.shipped' are hitting a queue bound with 'order.*.cancelled'. Demonstrate your understanding of exchange types, routing keys, and binding rules to identify the tampered configuration.",
    "apache_kafka": "[bold red]CIPHER: PARTITION FORENSICS[/bold red]\nA consumer group is experiencing continuous rebalancing. Consumer lag is spiking across three partitions. Demonstrate your knowledge of offsets, consumer groups, ISR, and rebalance protocols to diagnose the rogue consumer.",
    "cloud_messaging": "[bold red]CIPHER: CLOUD RELAY BREACH[/bold red]\nSQS messages are being reprocessed after visibility timeout expiration. EventBridge rules are matching events they should filter out. Prove your understanding of cloud messaging semantics to patch the configuration before the next processing cycle.",
    "patterns_best_practices": "[bold red]CIPHER: ARCHITECTURE REVIEW[/bold red]\nThe post-mortem reveals the root cause: missing patterns. No outbox, no idempotency, no saga coordination. Demonstrate mastery of distributed messaging patterns to design the remediation. The highway's integrity depends on it.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Signal", "Traced your first message. The highway acknowledged you."),
    "navigator": ("Dispatch Operator", "Mastered the Dispatch Core. Delivery guarantees understood."),
    "archivist": ("Exchange Cartographer", "Navigated the Exchange Labyrinth. RabbitMQ routing mapped."),
    "seeker": ("Stream Analyst", "Decoded the Partition Stream. Kafka internals hold no secrets."),
    "pipe_dream": ("Cloud Relay Engineer", "Secured the Cloud Relay. SQS, SNS, Pub/Sub, EventBridge — mastered."),
    "necromancer": ("Pattern Architect", "Mastered the Architect's Codex. Saga, outbox, idempotency — complete."),
    "streak_3": ("Signal Streak", "3 correct in a row. The highway is warming up."),
    "streak_5": ("Locked Frequency", "5 in a row. Messages flowing without error."),
    "streak_10": ("SIGNAL GRANDMASTER", "10 in a row. You do not send messages. You think in events."),
    "no_hints": ("Zero-Drop Run", "Cleared a zone without hints. No dead letters. No retries."),
    "speed_demon": ("Sub-Millisecond Routing", "Answered in under 5 seconds. Faster than a round-trip ACK."),
    "level_10": ("Junior Operator", "Level 10. The highway is starting to feel familiar."),
    "level_20": ("Senior Operator", "Level 20. Message brokers are your native infrastructure."),
    "level_30": ("Signal Legend", "Maximum level. You understand messaging from pub/sub to distributed sagas. Complete."),
    "completionist": ("Full Highway Access", "Every challenge. Every zone. Total signal penetration achieved."),
    "boss_slayer": ("Audit Bypassed", "Beat your first boss challenge. CIPHER found nothing anomalous."),
}
