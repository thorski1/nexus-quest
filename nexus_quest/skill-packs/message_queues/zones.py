"""
zones.py - All zone and challenge data for The Signal Highway (Message Queues Quest)
Challenge types: quiz (with options list), text (options=[])
"""

ZONE_ORDER = [
    "messaging_fundamentals",
    "rabbitmq",
    "apache_kafka",
    "cloud_messaging",
    "patterns_best_practices",
]

ZONES = {
    "messaging_fundamentals": {
        "id": "messaging_fundamentals",
        "name": "The Dispatch Core",
        "subtitle": "Pub/Sub, Point-to-Point, Delivery Guarantees",
        "color": "cyan",
        "icon": "\u2709",
        "commands": ["publish", "subscribe", "enqueue", "dequeue", "ack", "nack", "fanout", "route"],
        "challenges": [
            {
                "id": "mf_1",
                "type": "quiz",
                "question": "In a point-to-point messaging model, how many consumers receive each message?",
                "options": [
                    "All consumers subscribed to the queue",
                    "Exactly one consumer",
                    "A random subset of consumers",
                    "Only the first consumer that connected",
                ],
                "answer": "b",
                "lesson": (
                    "Point-to-Point (Queue Model) — each message is delivered to exactly one consumer.\n\n"
                    "The broker holds messages in a queue. When multiple consumers are listening,\n"
                    "the broker dispatches each message to only one of them (typically round-robin\n"
                    "or based on prefetch/capacity). Once consumed and acknowledged, the message\n"
                    "is removed from the queue.\n\n"
                    "Use case: work distribution, task processing, order fulfillment.\n"
                    "Contrast with pub/sub where every subscriber gets every message."
                ),
                "xp": 50,
            },
            {
                "id": "mf_2",
                "type": "quiz",
                "question": "In the publish/subscribe pattern, what happens when a new subscriber joins after a message was already published?",
                "options": [
                    "The subscriber receives all historical messages",
                    "The subscriber receives only messages published after it subscribes",
                    "The broker replays the last 100 messages",
                    "The subscriber must explicitly request a replay",
                ],
                "answer": "b",
                "lesson": (
                    "Pub/Sub — fire-and-forget broadcast messaging.\n\n"
                    "Publishers send messages to a topic/channel. All active subscribers receive\n"
                    "a copy. Subscribers that join after publication miss those messages entirely\n"
                    "unless the system implements durable subscriptions or message retention.\n\n"
                    "Pure pub/sub is stateless on the broker side — no replay, no persistence.\n"
                    "Systems like Kafka blur this line by persisting messages with offsets."
                ),
                "xp": 50,
            },
            {
                "id": "mf_3",
                "type": "text",
                "question": "What delivery guarantee ensures a message is delivered to the consumer at least once, but may result in duplicates? (two hyphenated words)",
                "options": [],
                "answer": "at-least-once",
                "lesson": (
                    "At-Least-Once Delivery — the broker retries until it receives an acknowledgment.\n\n"
                    "If the consumer processes the message but the ACK is lost (network failure),\n"
                    "the broker will redeliver. This means consumers may see the same message\n"
                    "more than once.\n\n"
                    "Requires idempotent consumers to handle duplicates safely.\n"
                    "Most production systems default to at-least-once because at-most-once\n"
                    "risks data loss, and exactly-once is expensive."
                ),
                "xp": 50,
            },
            {
                "id": "mf_4",
                "type": "quiz",
                "question": "Which delivery guarantee risks message loss but never delivers duplicates?",
                "options": [
                    "At-least-once",
                    "At-most-once",
                    "Exactly-once",
                    "Best-effort-ordered",
                ],
                "answer": "b",
                "lesson": (
                    "At-Most-Once — fire and forget.\n\n"
                    "The broker delivers the message and immediately considers it done.\n"
                    "No retries. If the consumer crashes or the network drops the message,\n"
                    "it is lost. No duplicates, but no guarantee of delivery either.\n\n"
                    "Use case: metrics, telemetry, logging — where occasional data loss\n"
                    "is acceptable and throughput matters more than completeness."
                ),
                "xp": 50,
            },
            {
                "id": "mf_5",
                "type": "quiz",
                "question": "What is a dead letter queue (DLQ)?",
                "options": [
                    "A queue for messages that have been successfully processed",
                    "A queue where messages are sent after exceeding retry limits or failing validation",
                    "A queue that automatically deletes messages after a TTL",
                    "A queue reserved for system health check messages",
                ],
                "answer": "b",
                "lesson": (
                    "Dead Letter Queue (DLQ) — a holding area for messages that cannot be processed.\n\n"
                    "Messages are routed to a DLQ when:\n"
                    "  - Maximum retry count exceeded\n"
                    "  - Message TTL expired\n"
                    "  - Consumer explicitly rejects (nack) without requeue\n"
                    "  - Message fails schema validation\n\n"
                    "DLQs are critical for observability — they let you inspect failures\n"
                    "without blocking the main processing pipeline. Always monitor DLQ depth."
                ),
                "xp": 75,
            },
            {
                "id": "mf_6",
                "type": "text",
                "question": "What is the term for the process where a consumer explicitly tells the broker it has successfully processed a message?",
                "options": [],
                "answer": "acknowledgment",
                "lesson": (
                    "Message Acknowledgment (ACK) — the consumer confirms processing is complete.\n\n"
                    "Without ACK, the broker does not know if the consumer succeeded or crashed.\n"
                    "ACK modes:\n"
                    "  - Manual ACK: consumer explicitly sends ACK after processing\n"
                    "  - Auto ACK: broker considers delivered = processed (risky)\n\n"
                    "Manual ACK with at-least-once delivery is the standard production pattern.\n"
                    "If the consumer crashes before ACK, the message is redelivered."
                ),
                "xp": 50,
            },
            {
                "id": "mf_7",
                "type": "quiz",
                "question": "A message broker decouples producers and consumers. Which property does this decoupling NOT provide?",
                "options": [
                    "Temporal decoupling — producer and consumer don't need to be online simultaneously",
                    "Spatial decoupling — producer doesn't need to know the consumer's address",
                    "Transactional decoupling — messages are automatically part of database transactions",
                    "Synchronization decoupling — producer doesn't block waiting for the consumer",
                ],
                "answer": "c",
                "lesson": (
                    "Message brokers provide three forms of decoupling:\n\n"
                    "  1. Temporal: producer and consumer can operate at different times\n"
                    "  2. Spatial: they don't need to know each other's network addresses\n"
                    "  3. Synchronization: the producer fires and continues without waiting\n\n"
                    "Transactional coupling with a database requires explicit patterns like\n"
                    "the Outbox Pattern or distributed transactions (2PC/Saga). A message\n"
                    "broker alone does NOT automatically participate in database transactions."
                ),
                "xp": 75,
            },
            {
                "id": "mf_8",
                "type": "quiz",
                "question": "What is message ordering, and when is it guaranteed in a point-to-point queue?",
                "options": [
                    "Messages are always delivered in random order",
                    "FIFO ordering is guaranteed only within a single queue with a single consumer",
                    "FIFO ordering is guaranteed across all queues in the broker",
                    "Messages are ordered by priority, never by arrival time",
                ],
                "answer": "b",
                "lesson": (
                    "Message Ordering — FIFO within a single queue, single consumer.\n\n"
                    "When multiple consumers compete on the same queue, messages are distributed\n"
                    "across them and global ordering is lost (consumer A may finish message 2\n"
                    "before consumer B finishes message 1).\n\n"
                    "Strategies for ordered processing at scale:\n"
                    "  - Partition by key (Kafka model) — same key always goes to same partition\n"
                    "  - Single consumer per queue (limits throughput)\n"
                    "  - Sequence numbers + reordering buffer on the consumer side"
                ),
                "xp": 75,
            },
        ],
    },
    "rabbitmq": {
        "id": "rabbitmq",
        "name": "The Exchange Labyrinth",
        "subtitle": "Exchanges, Queues, Routing Keys, Dead Letters",
        "color": "yellow",
        "icon": "\U0001f407",
        "commands": ["exchange", "queue", "bind", "publish", "consume", "ack", "nack", "dlx"],
        "challenges": [
            {
                "id": "rq_1",
                "type": "quiz",
                "question": "In RabbitMQ, messages are published to which component?",
                "options": [
                    "Directly to a queue",
                    "To an exchange, which routes to queues based on bindings",
                    "To a topic partition",
                    "To a consumer group",
                ],
                "answer": "b",
                "lesson": (
                    "RabbitMQ Exchange — the message routing layer.\n\n"
                    "Producers never publish directly to queues. They publish to an exchange\n"
                    "with a routing key. The exchange uses its type and binding rules to\n"
                    "determine which queue(s) receive the message.\n\n"
                    "Exchange types: direct, fanout, topic, headers.\n"
                    "This separation of publishing from queue routing is core to RabbitMQ's\n"
                    "flexibility."
                ),
                "xp": 50,
            },
            {
                "id": "rq_2",
                "type": "quiz",
                "question": "Which RabbitMQ exchange type delivers a message to ALL bound queues, ignoring the routing key?",
                "options": [
                    "direct",
                    "topic",
                    "fanout",
                    "headers",
                ],
                "answer": "c",
                "lesson": (
                    "Fanout Exchange — broadcast to all bound queues.\n\n"
                    "The routing key is completely ignored. Every queue bound to the exchange\n"
                    "receives a copy of every message. This is the pub/sub model in RabbitMQ.\n\n"
                    "Use case: event broadcasting, cache invalidation across services,\n"
                    "logging pipelines where every service needs every event.\n\n"
                    "Performance note: fanout is the fastest exchange type because\n"
                    "no routing key matching is required."
                ),
                "xp": 50,
            },
            {
                "id": "rq_3",
                "type": "text",
                "question": "What RabbitMQ exchange type routes messages to queues where the binding key exactly matches the routing key?",
                "options": [],
                "answer": "direct",
                "lesson": (
                    "Direct Exchange — exact routing key match.\n\n"
                    "A message published with routing key 'order.created' is delivered\n"
                    "only to queues bound with the exact key 'order.created'.\n\n"
                    "Multiple queues can bind with the same key (multicast).\n"
                    "A single queue can bind with multiple keys.\n\n"
                    "The default exchange ('') is a special direct exchange where every\n"
                    "queue is automatically bound with its queue name as the routing key."
                ),
                "xp": 50,
            },
            {
                "id": "rq_4",
                "type": "quiz",
                "question": "In a RabbitMQ topic exchange, the routing key 'order.*.shipped' would match which of the following?",
                "options": [
                    "order.shipped",
                    "order.us.shipped",
                    "order.us.east.shipped",
                    "order.shipped.confirmed",
                ],
                "answer": "b",
                "lesson": (
                    "Topic Exchange — pattern-based routing with wildcards.\n\n"
                    "Routing keys are dot-separated words. Two wildcards:\n"
                    "  * (star)  — matches exactly one word\n"
                    "  # (hash)  — matches zero or more words\n\n"
                    "  'order.*.shipped' matches 'order.us.shipped' (us = one word)\n"
                    "  'order.*.shipped' does NOT match 'order.us.east.shipped' (two words)\n"
                    "  'order.#.shipped' WOULD match 'order.us.east.shipped'\n\n"
                    "Topic exchanges are the most flexible routing mechanism in RabbitMQ."
                ),
                "xp": 75,
            },
            {
                "id": "rq_5",
                "type": "quiz",
                "question": "What does RabbitMQ's 'prefetch count' (basic.qos) control?",
                "options": [
                    "The maximum number of messages in a queue",
                    "The number of unacknowledged messages a consumer can hold at once",
                    "The number of consumers that can connect to a queue",
                    "The TTL of messages in the queue",
                ],
                "answer": "b",
                "lesson": (
                    "Prefetch Count (QoS) — flow control per consumer.\n\n"
                    "basic.qos(prefetch_count=N) tells RabbitMQ: do not send more than N\n"
                    "unacknowledged messages to this consumer.\n\n"
                    "  prefetch_count=1: consumer processes one at a time (fair dispatch)\n"
                    "  prefetch_count=10: consumer buffers up to 10 (higher throughput)\n\n"
                    "Without QoS, RabbitMQ dispatches all messages round-robin regardless\n"
                    "of whether the consumer has finished previous ones. This can overwhelm\n"
                    "slow consumers while fast ones idle."
                ),
                "xp": 75,
            },
            {
                "id": "rq_6",
                "type": "text",
                "question": "What is the name of the RabbitMQ mechanism that routes rejected or expired messages to a separate exchange for inspection? (three-word abbreviation)",
                "options": [],
                "answer": "DLX",
                "lesson": (
                    "Dead Letter Exchange (DLX) — RabbitMQ's dead letter mechanism.\n\n"
                    "A queue can be configured with x-dead-letter-exchange. Messages are\n"
                    "routed to the DLX when:\n"
                    "  - Consumer rejects with basic.nack/basic.reject (requeue=false)\n"
                    "  - Message TTL expires (x-message-ttl)\n"
                    "  - Queue max length exceeded (x-max-length)\n\n"
                    "You can also set x-dead-letter-routing-key to override the original\n"
                    "routing key. DLX + TTL = delayed message retry pattern."
                ),
                "xp": 75,
            },
            {
                "id": "rq_7",
                "type": "quiz",
                "question": "What happens to messages in a RabbitMQ queue if the broker restarts and the queue was declared as non-durable?",
                "options": [
                    "Messages are persisted to disk and survive restart",
                    "The queue and all its messages are lost",
                    "Messages are automatically forwarded to a backup exchange",
                    "The queue is recreated empty but retained its bindings",
                ],
                "answer": "b",
                "lesson": (
                    "Queue Durability — survival across broker restarts.\n\n"
                    "Durable queue: the queue definition survives restart.\n"
                    "Non-durable (transient) queue: destroyed on restart, messages lost.\n\n"
                    "IMPORTANT: queue durability alone does not persist messages.\n"
                    "You also need persistent messages (delivery_mode=2).\n\n"
                    "For full reliability: durable queue + persistent messages + publisher\n"
                    "confirms + consumer manual ACK."
                ),
                "xp": 50,
            },
            {
                "id": "rq_8",
                "type": "quiz",
                "question": "RabbitMQ publisher confirms (confirm.select) guarantee which of the following?",
                "options": [
                    "The consumer has processed the message",
                    "The message has been routed to at least one queue and persisted to disk",
                    "The message has been delivered to all consumers",
                    "The message will never expire",
                ],
                "answer": "b",
                "lesson": (
                    "Publisher Confirms — acknowledgment from broker to producer.\n\n"
                    "When a channel is in confirm mode, the broker sends back:\n"
                    "  - basic.ack: message accepted (routed + persisted if durable)\n"
                    "  - basic.nack: message rejected (broker could not handle it)\n\n"
                    "This does NOT mean the consumer has processed the message. It means\n"
                    "the broker has taken responsibility for it.\n\n"
                    "Without publisher confirms, a crash between publish and queue write\n"
                    "means silent message loss."
                ),
                "xp": 75,
            },
        ],
    },
    "apache_kafka": {
        "id": "apache_kafka",
        "name": "The Partition Stream",
        "subtitle": "Topics, Partitions, Consumer Groups, Offsets",
        "color": "green",
        "icon": "\U0001f300",
        "commands": ["topic", "partition", "produce", "consume", "offset", "group", "rebalance", "compact"],
        "challenges": [
            {
                "id": "ak_1",
                "type": "quiz",
                "question": "In Apache Kafka, what is the fundamental unit of data organization?",
                "options": [
                    "Queue",
                    "Exchange",
                    "Topic",
                    "Stream",
                ],
                "answer": "c",
                "lesson": (
                    "Kafka Topic — a named, append-only log of messages.\n\n"
                    "Producers write to topics. Consumers read from topics.\n"
                    "Unlike traditional queues, messages are NOT deleted after consumption.\n"
                    "They persist for a configurable retention period (time or size based).\n\n"
                    "A topic is divided into partitions for parallelism and ordering.\n"
                    "Each partition is an ordered, immutable sequence of records."
                ),
                "xp": 50,
            },
            {
                "id": "ak_2",
                "type": "text",
                "question": "What is the term for the sequential ID assigned to each record within a Kafka partition?",
                "options": [],
                "answer": "offset",
                "lesson": (
                    "Kafka Offset — a unique, sequential ID per record per partition.\n\n"
                    "Offsets are assigned by the broker when a record is appended.\n"
                    "They are never reused, even after compaction or deletion.\n\n"
                    "Consumers track their position using offsets:\n"
                    "  - Committed offset: last offset the consumer has processed\n"
                    "  - Current offset: the next record the consumer will read\n"
                    "  - Log-end offset: the latest record in the partition\n\n"
                    "Consumer lag = log-end offset - committed offset"
                ),
                "xp": 50,
            },
            {
                "id": "ak_3",
                "type": "quiz",
                "question": "What determines which partition a Kafka message is written to?",
                "options": [
                    "The consumer group selects the partition",
                    "Round-robin if no key; hash of the message key if a key is provided",
                    "The partition with the least data always receives the next message",
                    "The producer must always specify a partition number explicitly",
                ],
                "answer": "b",
                "lesson": (
                    "Kafka Partitioning Strategy:\n\n"
                    "  - No key: default partitioner uses round-robin (or sticky partitioning)\n"
                    "  - With key: hash(key) % num_partitions determines the partition\n"
                    "  - Custom: you can implement a custom Partitioner class\n\n"
                    "Key-based partitioning guarantees that all records with the same key\n"
                    "go to the same partition, preserving order for that key.\n\n"
                    "Example: partition by user_id ensures all events for a user are ordered."
                ),
                "xp": 75,
            },
            {
                "id": "ak_4",
                "type": "quiz",
                "question": "In Kafka, what is a consumer group?",
                "options": [
                    "A set of topics that are consumed together",
                    "A group of consumers that share the work of reading from a topic's partitions",
                    "A replication group for fault tolerance",
                    "A set of brokers that handle the same partition",
                ],
                "answer": "b",
                "lesson": (
                    "Kafka Consumer Group — cooperative consumption.\n\n"
                    "Each partition is assigned to exactly one consumer within a group.\n"
                    "Multiple groups can independently consume the same topic.\n\n"
                    "  Topic with 4 partitions, group with 2 consumers:\n"
                    "    Consumer A -> partitions 0, 1\n"
                    "    Consumer B -> partitions 2, 3\n\n"
                    "  If consumer B crashes, rebalance assigns all 4 to consumer A.\n"
                    "  If a 3rd consumer joins, rebalance redistributes partitions.\n\n"
                    "Max useful consumers in a group = number of partitions."
                ),
                "xp": 75,
            },
            {
                "id": "ak_5",
                "type": "text",
                "question": "What Kafka process reassigns partition ownership when consumers join or leave a consumer group?",
                "options": [],
                "answer": "rebalance",
                "lesson": (
                    "Consumer Group Rebalance — partition reassignment.\n\n"
                    "Triggered when:\n"
                    "  - A consumer joins the group\n"
                    "  - A consumer leaves or crashes (missed heartbeat)\n"
                    "  - Topic partition count changes\n\n"
                    "During rebalance, consumption pauses (stop-the-world in eager protocol).\n"
                    "Cooperative rebalance (incremental) minimizes disruption by only\n"
                    "revoking partitions that need to move.\n\n"
                    "session.timeout.ms controls how quickly a crashed consumer is detected.\n"
                    "max.poll.interval.ms controls max time between poll() calls."
                ),
                "xp": 75,
            },
            {
                "id": "ak_6",
                "type": "quiz",
                "question": "What is Kafka's ISR (In-Sync Replicas) and why does it matter?",
                "options": [
                    "ISR is the list of brokers that have all topics",
                    "ISR is the set of replicas that are fully caught up with the leader; only ISR members can become the new leader",
                    "ISR is a consumer group management protocol",
                    "ISR tracks which offsets have been committed by consumers",
                ],
                "answer": "b",
                "lesson": (
                    "In-Sync Replicas (ISR) — the durability guarantee.\n\n"
                    "Each partition has a leader and N replicas. The ISR is the subset of\n"
                    "replicas that are fully caught up with the leader's log.\n\n"
                    "  acks=0: producer doesn't wait for any acknowledgment\n"
                    "  acks=1: producer waits for leader acknowledgment only\n"
                    "  acks=all: producer waits for ALL ISR members to acknowledge\n\n"
                    "min.insync.replicas=2 with acks=all means at least 2 replicas\n"
                    "must confirm before the write is considered successful.\n"
                    "If ISR drops below min.insync.replicas, the broker rejects writes."
                ),
                "xp": 75,
            },
            {
                "id": "ak_7",
                "type": "quiz",
                "question": "What is log compaction in Kafka?",
                "options": [
                    "Deleting all messages older than the retention period",
                    "Compressing message payloads to save disk space",
                    "Retaining only the latest value for each unique key within a partition",
                    "Merging multiple partitions into one to reduce overhead",
                ],
                "answer": "c",
                "lesson": (
                    "Log Compaction — key-based deduplication.\n\n"
                    "Instead of deleting old segments by time/size, compaction retains\n"
                    "the latest record for each key. Earlier records with the same key\n"
                    "are garbage collected.\n\n"
                    "  cleanup.policy=compact (vs. delete or compact,delete)\n\n"
                    "Use case: changelog topics, state stores, CDC (change data capture).\n"
                    "Consumers can rebuild full state by reading the compacted topic\n"
                    "from offset 0 — every key's latest value is guaranteed present.\n\n"
                    "A tombstone (key with null value) signals deletion during compaction."
                ),
                "xp": 75,
            },
            {
                "id": "ak_8",
                "type": "quiz",
                "question": "What happens when you have more consumers in a Kafka consumer group than there are partitions in the topic?",
                "options": [
                    "Extra consumers share partitions with others",
                    "Extra consumers sit idle and receive no messages",
                    "Kafka automatically creates more partitions",
                    "The extra consumers read from the beginning of the topic",
                ],
                "answer": "b",
                "lesson": (
                    "Kafka: Consumers vs Partitions.\n\n"
                    "Each partition is assigned to exactly ONE consumer in a group.\n"
                    "If you have 3 partitions and 5 consumers, 2 consumers will be idle.\n\n"
                    "This is by design — it guarantees ordering within a partition.\n"
                    "If two consumers could read the same partition, you would need\n"
                    "external coordination to maintain order.\n\n"
                    "Scaling consumers beyond partition count wastes resources.\n"
                    "Plan partition count based on expected maximum consumer parallelism."
                ),
                "xp": 50,
            },
        ],
    },
    "cloud_messaging": {
        "id": "cloud_messaging",
        "name": "The Cloud Relay",
        "subtitle": "SQS, SNS, Pub/Sub, EventBridge",
        "color": "blue",
        "icon": "\u2601",
        "commands": ["sqs", "sns", "pubsub", "eventbridge", "fifo", "fanout", "filter", "rule"],
        "challenges": [
            {
                "id": "cm_1",
                "type": "quiz",
                "question": "AWS SQS is fundamentally which type of messaging model?",
                "options": [
                    "Publish/Subscribe",
                    "Point-to-point queue",
                    "Event streaming",
                    "Request/Reply",
                ],
                "answer": "b",
                "lesson": (
                    "Amazon SQS — Simple Queue Service. Point-to-point messaging.\n\n"
                    "Producers send messages to a queue. Consumers poll the queue.\n"
                    "Each message is delivered to exactly one consumer.\n\n"
                    "Two queue types:\n"
                    "  - Standard: nearly unlimited throughput, best-effort ordering,\n"
                    "    at-least-once delivery (possible duplicates)\n"
                    "  - FIFO: exactly-once processing, strict ordering,\n"
                    "    300 msg/s (3000 with batching)\n\n"
                    "Messages are invisible (not deleted) during processing.\n"
                    "Visibility timeout controls how long before a message is re-delivered."
                ),
                "xp": 50,
            },
            {
                "id": "cm_2",
                "type": "text",
                "question": "In AWS SQS, what is the name of the timeout period during which a message is hidden from other consumers after being received?",
                "options": [],
                "answer": "visibility timeout",
                "lesson": (
                    "SQS Visibility Timeout — message processing window.\n\n"
                    "When a consumer receives a message, SQS hides it for the visibility\n"
                    "timeout period (default 30s, max 12h). During this window:\n"
                    "  - No other consumer can receive this message\n"
                    "  - The consumer must delete the message when done\n"
                    "  - If not deleted, the message becomes visible again (redelivery)\n\n"
                    "Set visibility timeout > expected processing time.\n"
                    "Use ChangeMessageVisibility to extend it dynamically."
                ),
                "xp": 50,
            },
            {
                "id": "cm_3",
                "type": "quiz",
                "question": "What is the SNS+SQS fanout pattern?",
                "options": [
                    "SQS queues that automatically scale based on load",
                    "SNS topic publishes to multiple SQS queues, enabling parallel independent processing",
                    "Multiple SNS topics feeding into a single SQS queue",
                    "SQS long polling across multiple AWS regions",
                ],
                "answer": "b",
                "lesson": (
                    "SNS+SQS Fanout — the most common AWS messaging pattern.\n\n"
                    "SNS (pub/sub) fans out messages to multiple SQS queues (point-to-point).\n"
                    "Each queue has its own consumer, processing independently.\n\n"
                    "  Order placed -> SNS topic\n"
                    "    -> SQS: payment-processing\n"
                    "    -> SQS: inventory-update\n"
                    "    -> SQS: email-notification\n\n"
                    "Each queue retries independently, has its own DLQ, and scales\n"
                    "its own consumer fleet. Decoupled, reliable, observable."
                ),
                "xp": 75,
            },
            {
                "id": "cm_4",
                "type": "quiz",
                "question": "What does an SQS FIFO queue's MessageGroupId control?",
                "options": [
                    "Which consumer group receives the message",
                    "The priority of the message in the queue",
                    "Message ordering — messages within the same group are strictly ordered",
                    "The AWS account that owns the message",
                ],
                "answer": "c",
                "lesson": (
                    "SQS FIFO MessageGroupId — ordered processing lanes.\n\n"
                    "Messages with the same MessageGroupId are delivered in strict FIFO order.\n"
                    "Messages with different MessageGroupIds can be processed in parallel.\n\n"
                    "  MessageGroupId='user-123': all events for user-123 are ordered\n"
                    "  MessageGroupId='user-456': processed independently, in parallel\n\n"
                    "This is conceptually similar to Kafka's key-based partitioning.\n"
                    "Combined with MessageDeduplicationId, FIFO queues provide\n"
                    "exactly-once processing within a 5-minute deduplication window."
                ),
                "xp": 75,
            },
            {
                "id": "cm_5",
                "type": "text",
                "question": "What is the name of Google Cloud's managed messaging service that provides at-least-once delivery with both push and pull subscription modes?",
                "options": [],
                "answer": "Pub/Sub",
                "lesson": (
                    "Google Cloud Pub/Sub — fully managed messaging middleware.\n\n"
                    "Key features:\n"
                    "  - Topics (publish) + Subscriptions (consume)\n"
                    "  - Pull mode: consumer requests messages\n"
                    "  - Push mode: Pub/Sub sends messages to an HTTP endpoint\n"
                    "  - At-least-once delivery (exactly-once available with ordering keys)\n"
                    "  - Message retention up to 31 days\n"
                    "  - Automatic scaling, no partitions to manage\n\n"
                    "Unlike Kafka, you don't manage partitions or brokers.\n"
                    "Unlike SQS, it natively supports both push and pull."
                ),
                "xp": 50,
            },
            {
                "id": "cm_6",
                "type": "quiz",
                "question": "What is Amazon EventBridge primarily designed for?",
                "options": [
                    "High-throughput log streaming",
                    "Event-driven routing with rules that filter and transform events from multiple sources",
                    "Replacing SQS for point-to-point messaging",
                    "Real-time video streaming between services",
                ],
                "answer": "b",
                "lesson": (
                    "Amazon EventBridge — serverless event bus.\n\n"
                    "EventBridge receives events from AWS services, SaaS apps, and custom\n"
                    "sources, then routes them based on rules.\n\n"
                    "  Event source -> Event bus -> Rules -> Targets\n\n"
                    "Rules can match on any field in the event JSON:\n"
                    "  {\"source\": [\"order-service\"], \"detail-type\": [\"OrderCreated\"]}\n\n"
                    "Targets: Lambda, SQS, SNS, Step Functions, API Gateway, etc.\n"
                    "Schema Registry discovers and validates event schemas automatically.\n\n"
                    "EventBridge is the backbone for event-driven architectures on AWS."
                ),
                "xp": 75,
            },
            {
                "id": "cm_7",
                "type": "quiz",
                "question": "SQS long polling vs short polling: which reduces empty responses and API costs?",
                "options": [
                    "Short polling — it checks more frequently",
                    "Long polling — it waits up to WaitTimeSeconds for messages to arrive",
                    "They are identical in behavior",
                    "Neither — polling mode doesn't affect costs",
                ],
                "answer": "b",
                "lesson": (
                    "SQS Long Polling — efficient message retrieval.\n\n"
                    "  Short polling: returns immediately, even if no messages (empty response)\n"
                    "  Long polling: waits up to WaitTimeSeconds (max 20s) for messages\n\n"
                    "Long polling reduces:\n"
                    "  - Empty responses (fewer wasted API calls)\n"
                    "  - API costs (fewer ReceiveMessage requests)\n"
                    "  - Apparent latency (messages returned as soon as they arrive)\n\n"
                    "Enable: set WaitTimeSeconds > 0 on ReceiveMessage call\n"
                    "or set ReceiveMessageWaitTimeSeconds on the queue itself."
                ),
                "xp": 50,
            },
            {
                "id": "cm_8",
                "type": "quiz",
                "question": "Google Cloud Pub/Sub uses which mechanism to ensure a message is not redelivered to the same subscriber?",
                "options": [
                    "Visibility timeout",
                    "Message acknowledgment deadline — subscriber must ACK before deadline expires",
                    "Consumer group offset commits",
                    "Automatic deduplication by message ID",
                ],
                "answer": "b",
                "lesson": (
                    "GCP Pub/Sub Acknowledgment Deadline.\n\n"
                    "When a subscriber receives a message, it has ackDeadlineSeconds\n"
                    "(default 10s, max 600s) to ACK it.\n\n"
                    "  - ACK before deadline: message removed, not redelivered\n"
                    "  - No ACK: message becomes available for redelivery\n"
                    "  - ModifyAckDeadline: extend the deadline dynamically\n\n"
                    "Similar in concept to SQS visibility timeout, but the terminology\n"
                    "and API differ. Both serve the same purpose: ensuring at-least-once\n"
                    "delivery with a processing window."
                ),
                "xp": 50,
            },
        ],
    },
    "patterns_best_practices": {
        "id": "patterns_best_practices",
        "name": "The Architect's Codex",
        "subtitle": "Event Sourcing, Saga, Outbox, Idempotency, Backpressure",
        "color": "magenta",
        "icon": "\U0001f4dc",
        "commands": ["event_store", "saga", "outbox", "idempotency_key", "backpressure", "circuit_breaker", "retry", "dlq"],
        "challenges": [
            {
                "id": "pb_1",
                "type": "quiz",
                "question": "What is event sourcing?",
                "options": [
                    "Sending events to a message queue for async processing",
                    "Storing every state change as an immutable event, deriving current state by replaying the event log",
                    "Publishing database changes to an event stream",
                    "Using events instead of REST APIs for service communication",
                ],
                "answer": "b",
                "lesson": (
                    "Event Sourcing — state as a sequence of events.\n\n"
                    "Instead of storing current state (UPDATE balance = 50), you store\n"
                    "every event that led to that state:\n"
                    "  1. AccountCreated(balance=100)\n"
                    "  2. MoneyWithdrawn(amount=30)\n"
                    "  3. MoneyDeposited(amount=20)\n"
                    "  4. MoneyWithdrawn(amount=40)\n\n"
                    "Current state: replay events -> balance = 100 - 30 + 20 - 40 = 50\n\n"
                    "Benefits: complete audit trail, temporal queries, event replay.\n"
                    "Costs: complexity, eventual consistency, snapshot management."
                ),
                "xp": 75,
            },
            {
                "id": "pb_2",
                "type": "quiz",
                "question": "The Saga pattern solves which problem in distributed systems?",
                "options": [
                    "Message ordering across partitions",
                    "Managing distributed transactions across multiple services without 2PC",
                    "Compressing large event payloads",
                    "Load balancing consumers across queues",
                ],
                "answer": "b",
                "lesson": (
                    "Saga Pattern — distributed transactions without 2PC.\n\n"
                    "A saga is a sequence of local transactions. Each service performs\n"
                    "its transaction and publishes an event. If a step fails, compensating\n"
                    "transactions undo the previous steps.\n\n"
                    "Two coordination styles:\n"
                    "  - Choreography: each service reacts to events (decentralized)\n"
                    "  - Orchestration: a central orchestrator directs the flow\n\n"
                    "Example: Order -> Payment -> Inventory -> Shipping\n"
                    "  Payment fails -> compensate: cancel order, refund, restore inventory.\n\n"
                    "Sagas trade ACID for availability and partition tolerance."
                ),
                "xp": 75,
            },
            {
                "id": "pb_3",
                "type": "text",
                "question": "What pattern writes events to a database table in the same transaction as the business data, then a separate process publishes those events to the message broker?",
                "options": [],
                "answer": "outbox",
                "lesson": (
                    "Transactional Outbox Pattern — atomic write + publish.\n\n"
                    "The problem: you need to update a database AND publish a message,\n"
                    "but a crash between the two operations causes inconsistency.\n\n"
                    "Solution:\n"
                    "  1. Within a DB transaction: write business data + insert event row\n"
                    "     into an 'outbox' table\n"
                    "  2. A separate relay process reads the outbox table and publishes\n"
                    "     events to the broker (polling or CDC)\n"
                    "  3. After successful publish, mark the outbox row as sent\n\n"
                    "Guarantees: if the transaction commits, the event will eventually\n"
                    "be published. No dual-write problem."
                ),
                "xp": 75,
            },
            {
                "id": "pb_4",
                "type": "quiz",
                "question": "How does an idempotency key prevent duplicate processing of a message?",
                "options": [
                    "It encrypts the message so it can only be read once",
                    "It assigns a unique ID; the consumer checks if it has already processed that ID before proceeding",
                    "It prevents the broker from sending the same message twice",
                    "It automatically deduplicates messages at the network layer",
                ],
                "answer": "b",
                "lesson": (
                    "Idempotency Key — safe reprocessing of duplicate messages.\n\n"
                    "Each message carries a unique idempotency key (UUID, event ID, etc.).\n"
                    "The consumer maintains a store of processed keys:\n\n"
                    "  1. Receive message with key='abc-123'\n"
                    "  2. Check: have I processed 'abc-123' before?\n"
                    "  3. No -> process and record 'abc-123'\n"
                    "  4. Yes -> skip (or return cached result)\n\n"
                    "Essential for at-least-once delivery systems.\n"
                    "Storage: database table, Redis SET, or Bloom filter for probabilistic.\n"
                    "Retention: keep keys for at least the broker's max redelivery window."
                ),
                "xp": 75,
            },
            {
                "id": "pb_5",
                "type": "text",
                "question": "What is the term for a mechanism that slows down or stops producers when consumers cannot keep up with the rate of incoming messages?",
                "options": [],
                "answer": "backpressure",
                "lesson": (
                    "Backpressure — flow control in messaging systems.\n\n"
                    "When consumers are slower than producers, messages accumulate.\n"
                    "Without backpressure, this leads to memory exhaustion, queue overflow,\n"
                    "or unbounded latency.\n\n"
                    "Backpressure mechanisms:\n"
                    "  - Queue max length (drop or reject new messages)\n"
                    "  - Producer rate limiting (broker rejects publishes above threshold)\n"
                    "  - Credit-based flow control (RabbitMQ internal TCP backpressure)\n"
                    "  - Consumer pull model (Kafka — consumers control their own pace)\n\n"
                    "Kafka's pull model is inherently backpressure-friendly: consumers\n"
                    "fetch at their own rate. Push-based systems need explicit mechanisms."
                ),
                "xp": 75,
            },
            {
                "id": "pb_6",
                "type": "quiz",
                "question": "In a choreography-based saga, what is the main risk compared to orchestration?",
                "options": [
                    "Higher latency due to synchronous calls",
                    "Cyclic dependencies and difficulty tracing the flow across services",
                    "Requires a single point of failure coordinator",
                    "Cannot handle more than two services",
                ],
                "answer": "b",
                "lesson": (
                    "Choreography vs Orchestration tradeoffs:\n\n"
                    "Choreography (decentralized):\n"
                    "  + No single point of failure\n"
                    "  + Loose coupling\n"
                    "  - Hard to trace/debug the flow\n"
                    "  - Risk of cyclic event dependencies\n"
                    "  - Implicit process logic scattered across services\n\n"
                    "Orchestration (centralized):\n"
                    "  + Explicit flow definition\n"
                    "  + Easy to trace and monitor\n"
                    "  - Orchestrator is a single point of failure (mitigate with HA)\n"
                    "  - Tighter coupling to the orchestrator\n\n"
                    "Choose orchestration for complex multi-step flows.\n"
                    "Choose choreography for simple 2-3 service interactions."
                ),
                "xp": 75,
            },
            {
                "id": "pb_7",
                "type": "quiz",
                "question": "What is Change Data Capture (CDC) and how does it relate to messaging?",
                "options": [
                    "A technique to compress database backups",
                    "Capturing row-level changes from a database's transaction log and publishing them as events to a message broker",
                    "A consumer pattern that captures message delivery metrics",
                    "A method to replicate messages between two brokers",
                ],
                "answer": "b",
                "lesson": (
                    "Change Data Capture (CDC) — database changes as events.\n\n"
                    "CDC reads the database's transaction log (WAL in Postgres, binlog in\n"
                    "MySQL) and publishes row-level changes as events.\n\n"
                    "  INSERT -> {op: 'c', table: 'orders', after: {id: 1, ...}}\n"
                    "  UPDATE -> {op: 'u', table: 'orders', before: {...}, after: {...}}\n"
                    "  DELETE -> {op: 'd', table: 'orders', before: {id: 1, ...}}\n\n"
                    "Tools: Debezium (most popular), AWS DMS, GCP Datastream.\n"
                    "CDC + Kafka = reliable event-driven architecture without modifying\n"
                    "application code. Often used to implement the outbox pattern."
                ),
                "xp": 75,
            },
            {
                "id": "pb_8",
                "type": "quiz",
                "question": "When implementing retry logic for message consumers, which strategy avoids overwhelming a failing downstream service?",
                "options": [
                    "Immediate retry with no delay",
                    "Exponential backoff with jitter",
                    "Retry infinitely until success",
                    "Retry once and discard on failure",
                ],
                "answer": "b",
                "lesson": (
                    "Exponential Backoff with Jitter — resilient retry strategy.\n\n"
                    "  Attempt 1: wait 1s\n"
                    "  Attempt 2: wait 2s\n"
                    "  Attempt 3: wait 4s\n"
                    "  Attempt 4: wait 8s + random jitter\n\n"
                    "Jitter adds randomness to prevent thundering herd — all consumers\n"
                    "retrying at the exact same intervals.\n\n"
                    "After max retries: send to DLQ for manual inspection.\n\n"
                    "Combine with circuit breaker: after N consecutive failures, stop\n"
                    "attempting for a cooldown period. This protects the downstream\n"
                    "service from retry storms while it recovers."
                ),
                "xp": 75,
            },
        ],
    },
}
