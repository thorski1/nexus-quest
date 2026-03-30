"""
zones.py — System Design zones and challenges for Systems Architect.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "scalability_basics",
    "caching",
    "message_queues",
    "microservices",
    "database_at_scale",
    "cdn_and_edge",
    "reliability",
    "design_interviews",
]

ZONES = {
    # ── ZONE 1: SCALABILITY BASICS ─────────────────────────────────────
    "scalability_basics": {
        "id": "scalability_basics",
        "name": "Scalability Fundamentals",
        "subtitle": "Vertical vs Horizontal Scaling, Stateless Services & Bottlenecks",
        "color": "cyan",
        "icon": "📈",
        "commands": ["scale-up", "scale-out", "load-balancer", "stateless", "bottleneck"],
        "challenges": [
            {
                "id": "scale_1",
                "type": "quiz",
                "title": "Vertical vs Horizontal",
                "question": (
                    "Your API server is maxing out CPU under load.\n"
                    "You upgrade to a machine with 2x the cores and RAM.\n\n"
                    "What kind of scaling is this?"
                ),
                "lesson": (
                    "Vertical scaling (scaling up) = adding more resources to a single machine.\n\n"
                    "More CPU, more RAM, faster disks. Simple to implement — no code changes\n"
                    "required. But it has a ceiling: there's a biggest machine you can buy,\n"
                    "and it's a single point of failure.\n\n"
                    "Horizontal scaling (scaling out) = adding more machines.\n"
                    "Requires your application to be designed for distribution."
                ),
                "options": [
                    "Horizontal scaling",
                    "Vertical scaling",
                    "Diagonal scaling",
                    "Elastic scaling",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "You're making one machine bigger, not adding more machines.",
                    "Vertical = up. Horizontal = out.",
                ],
            },
            {
                "id": "scale_2",
                "type": "quiz",
                "title": "Horizontal Scaling",
                "question": (
                    "Instead of upgrading hardware, you deploy 4 identical copies\n"
                    "of your API server behind a load balancer.\n\n"
                    "What kind of scaling is this?"
                ),
                "lesson": (
                    "Horizontal scaling (scaling out) = adding more instances of the same service.\n\n"
                    "Advantages:\n"
                    "  - No single point of failure (one node dies, others continue)\n"
                    "  - Theoretically unlimited (add as many nodes as needed)\n"
                    "  - Cost-effective (commodity hardware vs premium servers)\n\n"
                    "Requirements:\n"
                    "  - Stateless application design (no local session state)\n"
                    "  - Load balancer to distribute traffic\n"
                    "  - Shared state stored externally (database, cache, object store)"
                ),
                "options": [
                    "Horizontal scaling",
                    "Vertical scaling",
                    "Auto-scaling",
                    "Database scaling",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "You're adding more machines, not making one bigger.",
                    "Horizontal = out. More instances, same size.",
                ],
            },
            {
                "id": "scale_3",
                "type": "quiz",
                "title": "Stateless Services",
                "question": (
                    "Why must services be stateless to scale horizontally?\n\n"
                    "A user hits Server A for request 1, then Server B for request 2.\n"
                    "What breaks if session state is stored in memory on Server A?"
                ),
                "lesson": (
                    "Stateless services store no session data locally.\n\n"
                    "If Server A holds the user's session in memory, and the load balancer\n"
                    "sends the next request to Server B, the session is lost. The user\n"
                    "appears logged out, their cart is empty, their form data is gone.\n\n"
                    "Solutions:\n"
                    "  - Store sessions in Redis/Memcached (shared, fast)\n"
                    "  - Store sessions in a database (shared, persistent)\n"
                    "  - Use JWTs (session data in the token itself)\n"
                    "  - Sticky sessions (load balancer pins user to one server — fragile)"
                ),
                "options": [
                    "The database gets overloaded",
                    "Server B has no access to Server A's session data",
                    "The load balancer crashes",
                    "DNS resolution fails between servers",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Think about what happens to data stored in Server A's memory when the request goes elsewhere.",
                    "The user's session lives only on the machine that created it.",
                ],
            },
            {
                "id": "scale_4",
                "type": "quiz",
                "title": "Load Distribution",
                "question": (
                    "A load balancer distributes incoming requests across multiple servers.\n"
                    "Which algorithm sends each new request to the server with the\n"
                    "fewest active connections?"
                ),
                "lesson": (
                    "Least connections — routes to the server handling the fewest active requests.\n\n"
                    "Common load balancing algorithms:\n"
                    "  Round Robin        — rotate through servers in order\n"
                    "  Weighted Round Robin — rotate, but send more to stronger servers\n"
                    "  Least Connections  — pick the server with fewest active connections\n"
                    "  IP Hash           — hash client IP to always hit the same server\n"
                    "  Random            — pick a server at random\n\n"
                    "Least connections is best when requests have variable processing time.\n"
                    "Round robin is simplest but assumes equal server capacity and equal request cost."
                ),
                "options": [
                    "Round robin",
                    "IP hash",
                    "Least connections",
                    "Random selection",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The algorithm cares about how busy each server currently is.",
                    "Fewest active connections = least loaded.",
                ],
            },
            {
                "id": "scale_5",
                "type": "quiz",
                "title": "Finding the Bottleneck",
                "question": (
                    "Your web app has 10 API servers, but response times are still slow.\n"
                    "All API servers show low CPU. The database shows 98% CPU utilization.\n\n"
                    "What is the bottleneck?"
                ),
                "lesson": (
                    "The bottleneck is the component that limits overall system throughput.\n\n"
                    "Adding more API servers won't help if the database is the constraint.\n"
                    "This is Amdahl's Law in practice: the system is only as fast as its\n"
                    "slowest component.\n\n"
                    "Common bottlenecks:\n"
                    "  - Database (most frequent) — CPU, connections, locks, slow queries\n"
                    "  - Network — bandwidth, latency between services\n"
                    "  - Disk I/O — storage throughput for read/write-heavy workloads\n"
                    "  - Single-threaded code — one CPU core maxed, others idle\n\n"
                    "Fix the bottleneck before scaling anything else."
                ),
                "options": [
                    "The load balancer",
                    "The API servers",
                    "The database",
                    "The network layer",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Look at which component has the highest resource utilization.",
                    "98% CPU on one component, low CPU everywhere else. That's your constraint.",
                ],
            },
            {
                "id": "scale_6",
                "type": "quiz",
                "title": "Amdahl's Law",
                "question": (
                    "You have a request pipeline: 80% of time is spent in parallelizable\n"
                    "API logic and 20% in a serial database write.\n\n"
                    "If you scale the API servers to infinity, what is the maximum\n"
                    "theoretical speedup?"
                ),
                "lesson": (
                    "Amdahl's Law: max speedup = 1 / (1 - P + P/N)\n"
                    "Where P = parallelizable fraction, N = number of processors.\n\n"
                    "As N approaches infinity: max speedup = 1 / (1 - P) = 1 / 0.2 = 5x.\n\n"
                    "No matter how many API servers you add, the serial 20% database write\n"
                    "limits your total speedup to 5x. This is why identifying and optimizing\n"
                    "the serial bottleneck matters more than throwing hardware at the parallel part."
                ),
                "options": [
                    "Infinite speedup",
                    "10x",
                    "5x",
                    "2x",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "The serial portion (20%) cannot be parallelized, no matter how many servers you add.",
                    "Max speedup = 1 / serial_fraction = 1 / 0.2.",
                ],
            },
        ],
    },

    # ── ZONE 2: CACHING ────────────────────────────────────────────────
    "caching": {
        "id": "caching",
        "name": "The Cache Layer",
        "subtitle": "CDN Caches, Application Caches, Redis, Invalidation & TTL",
        "color": "yellow",
        "icon": "⚡",
        "commands": ["redis", "memcached", "CDN", "TTL", "cache-aside"],
        "challenges": [
            {
                "id": "cache_1",
                "type": "quiz",
                "title": "Why Cache?",
                "question": (
                    "Your database handles 10,000 reads/sec. 80% of reads are for the\n"
                    "same 500 product records. You add a cache layer.\n\n"
                    "What is the primary benefit?"
                ),
                "lesson": (
                    "Caching reduces load on the origin (database/service) by serving\n"
                    "repeated reads from fast in-memory storage.\n\n"
                    "If 80% of reads hit the cache, the database now handles 2,000 reads/sec\n"
                    "instead of 10,000. Response times drop from ~50ms (disk) to ~1ms (memory).\n\n"
                    "Cache hierarchy (fast to slow):\n"
                    "  L1/L2 CPU cache  → nanoseconds\n"
                    "  Application memory → microseconds\n"
                    "  Redis/Memcached   → ~1ms (network hop)\n"
                    "  Database          → 5-50ms\n"
                    "  Disk              → 10-100ms"
                ),
                "options": [
                    "Reduces database load by serving repeated reads from memory",
                    "Eliminates the need for a database entirely",
                    "Ensures data is always perfectly up to date",
                    "Reduces the number of API servers needed",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "The cache absorbs the repeated reads so the database doesn't have to.",
                    "Memory is orders of magnitude faster than disk. That's the win.",
                ],
            },
            {
                "id": "cache_2",
                "type": "quiz",
                "title": "Cache-Aside Pattern",
                "question": (
                    "In the cache-aside pattern, what happens on a cache miss?\n\n"
                    "  1. Application checks cache\n"
                    "  2. Cache miss\n"
                    "  3. ???"
                ),
                "lesson": (
                    "Cache-aside (lazy loading):\n\n"
                    "  1. App checks cache → miss\n"
                    "  2. App reads from database\n"
                    "  3. App writes result to cache\n"
                    "  4. App returns result to caller\n\n"
                    "The application owns the logic. The cache is passive storage.\n"
                    "Only requested data gets cached (no wasted memory on unused data).\n\n"
                    "Downsides:\n"
                    "  - First request is always slow (cache cold start)\n"
                    "  - Cache can become stale if the database is updated directly\n"
                    "  - Thundering herd: many simultaneous misses for the same key"
                ),
                "options": [
                    "The cache automatically fetches from the database",
                    "The application reads from the database and writes the result to the cache",
                    "The request fails with a 503",
                    "The load balancer retries with a different cache node",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "In cache-aside, the application is responsible for populating the cache.",
                    "Miss → read DB → write to cache → return.",
                ],
            },
            {
                "id": "cache_3",
                "type": "quiz",
                "title": "TTL — Time to Live",
                "question": (
                    "You cache user profile data with a TTL of 300 seconds.\n"
                    "A user updates their display name.\n\n"
                    "What is the worst case for how long other users see the old name?"
                ),
                "lesson": (
                    "TTL (Time to Live) — the maximum age of a cached entry before eviction.\n\n"
                    "With a 300-second TTL, stale data can persist for up to 300 seconds\n"
                    "after the source changes. This is the consistency tradeoff of caching.\n\n"
                    "Shorter TTL → fresher data, more cache misses, more DB load\n"
                    "Longer TTL → staler data, fewer cache misses, less DB load\n\n"
                    "Choosing TTL is a business decision:\n"
                    "  - Stock prices: seconds (or no cache)\n"
                    "  - User profiles: minutes\n"
                    "  - Product catalog: hours\n"
                    "  - Static assets: days/weeks"
                ),
                "options": [
                    "Instantly — the cache updates in real time",
                    "Up to 300 seconds",
                    "Up to 600 seconds (two TTL cycles)",
                    "Forever, until the cache server restarts",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The TTL is the maximum age. Worst case, the entry was just written.",
                    "300-second TTL means the entry expires in at most 300 seconds.",
                ],
            },
            {
                "id": "cache_4",
                "type": "quiz",
                "title": "Cache Invalidation",
                "question": (
                    "Phil Karlton famously said there are only two hard things in\n"
                    "computer science: naming things and ___.\n\n"
                    "What strategy explicitly removes or updates a cache entry when\n"
                    "the underlying data changes?"
                ),
                "lesson": (
                    "Cache invalidation — removing stale entries when source data changes.\n\n"
                    "Strategies:\n"
                    "  TTL-based: let entries expire naturally. Simple but stale.\n"
                    "  Write-through: update cache and DB simultaneously on every write.\n"
                    "  Write-behind: update cache immediately, async write to DB.\n"
                    "  Active invalidation: on data change, explicitly delete the cache key.\n\n"
                    "Active invalidation gives the freshest data but requires your write path\n"
                    "to know about the cache. If any write path misses the invalidation,\n"
                    "you get silent staleness — the worst kind of bug."
                ),
                "options": [
                    "Cache replication",
                    "Cache invalidation",
                    "Cache warming",
                    "Cache sharding",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's the thing Phil Karlton said was hard.",
                    "Removing or updating stale cache entries when the source changes.",
                ],
            },
            {
                "id": "cache_5",
                "type": "quiz",
                "title": "Redis vs Memcached",
                "question": (
                    "You need a cache that supports sorted sets, pub/sub, and persistence\n"
                    "to disk so data survives restarts.\n\n"
                    "Which cache technology fits?"
                ),
                "lesson": (
                    "Redis — an in-memory data structure store with rich data types.\n\n"
                    "Redis supports: strings, hashes, lists, sets, sorted sets, streams,\n"
                    "pub/sub, Lua scripting, transactions, and optional disk persistence\n"
                    "(RDB snapshots or AOF append-only file).\n\n"
                    "Memcached — a simpler, pure key-value in-memory cache.\n"
                    "  Strings only. No persistence. No pub/sub. Multi-threaded by default.\n"
                    "  Slightly faster for simple get/set at extreme scale.\n\n"
                    "Choose Redis when you need data structures or persistence.\n"
                    "Choose Memcached when you need pure speed for simple key-value caching."
                ),
                "options": [
                    "Memcached",
                    "Redis",
                    "Varnish",
                    "Nginx proxy cache",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Only one of these supports sorted sets, pub/sub, and persistence.",
                    "It's the one that's more than a simple key-value store.",
                ],
            },
            {
                "id": "cache_6",
                "type": "quiz",
                "title": "CDN as a Cache",
                "question": (
                    "Your users are distributed globally. Static assets (images, JS, CSS)\n"
                    "are served from a single origin in us-east-1.\n"
                    "Users in Tokyo experience 200ms latency per asset.\n\n"
                    "What layer should you add?"
                ),
                "lesson": (
                    "A CDN (Content Delivery Network) caches content at edge locations\n"
                    "geographically close to users.\n\n"
                    "Without CDN: Tokyo user → us-east-1 origin → 200ms round trip\n"
                    "With CDN: Tokyo user → Tokyo edge node → 5ms round trip\n\n"
                    "CDNs are most effective for:\n"
                    "  - Static assets (images, CSS, JS, fonts)\n"
                    "  - Video streaming\n"
                    "  - Any content that doesn't change per-user\n\n"
                    "Major CDNs: CloudFront, Cloudflare, Akamai, Fastly.\n"
                    "CDN is caching + geographic distribution."
                ),
                "options": [
                    "More API servers in us-east-1",
                    "A CDN with edge nodes near your users",
                    "A larger database instance",
                    "A Redis cluster in us-east-1",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The problem is geographic distance, not server capacity.",
                    "You need cache nodes physically closer to Tokyo users.",
                ],
            },
        ],
    },

    # ── ZONE 3: MESSAGE QUEUES ─────────────────────────────────────────
    "message_queues": {
        "id": "message_queues",
        "name": "The Message Queue",
        "subtitle": "Pub/Sub, Kafka, RabbitMQ, Dead Letter Queues & Backpressure",
        "color": "green",
        "icon": "📬",
        "commands": ["publish", "subscribe", "enqueue", "dequeue", "ack"],
        "challenges": [
            {
                "id": "mq_1",
                "type": "quiz",
                "title": "Why Use a Queue?",
                "question": (
                    "Your checkout API calls a payment service, then an email service,\n"
                    "then an inventory service — all synchronously. Total latency: 3 seconds.\n\n"
                    "How does adding a message queue help?"
                ),
                "lesson": (
                    "Message queues decouple producers from consumers.\n\n"
                    "Synchronous: Checkout → Payment → Email → Inventory (serial, 3s total)\n"
                    "Async with queue: Checkout → Payment (must be sync) → publish events\n"
                    "  Email service picks up event async. Inventory picks up event async.\n"
                    "  User sees confirmation after payment (~1s), not after all 3.\n\n"
                    "Benefits:\n"
                    "  - Reduced latency for the user\n"
                    "  - Services can fail independently\n"
                    "  - Traffic spikes are buffered (queue absorbs the burst)\n"
                    "  - Services can be scaled independently"
                ),
                "options": [
                    "It makes all three calls faster by compressing the data",
                    "It processes email and inventory async so the user doesn't wait for them",
                    "It eliminates the need for the email and inventory services",
                    "It caches the payment result for faster retries",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The user only needs to wait for the payment. The rest can happen later.",
                    "Async processing means the producer doesn't wait for the consumer.",
                ],
            },
            {
                "id": "mq_2",
                "type": "quiz",
                "title": "Pub/Sub Model",
                "question": (
                    "In pub/sub messaging, a single 'order.placed' event needs to be\n"
                    "processed by the email service, the inventory service, AND the\n"
                    "analytics service.\n\n"
                    "How does pub/sub handle this?"
                ),
                "lesson": (
                    "Pub/Sub — publish/subscribe. One message, many consumers.\n\n"
                    "The producer publishes a message to a topic (not a specific consumer).\n"
                    "Every service subscribed to that topic receives a copy of the message.\n\n"
                    "  Producer → Topic: 'order.placed'\n"
                    "    ├→ Email service (subscriber)\n"
                    "    ├→ Inventory service (subscriber)\n"
                    "    └→ Analytics service (subscriber)\n\n"
                    "Contrast with point-to-point queues: one message, one consumer.\n"
                    "Pub/sub is fan-out. Queues are load distribution."
                ),
                "options": [
                    "The producer sends the message three times, once to each service",
                    "Each subscriber receives a copy of the message from the topic",
                    "Only the first subscriber gets the message; others poll for it",
                    "The message broker round-robins to one subscriber at a time",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Pub/sub is fan-out: one message, delivered to all subscribers.",
                    "The producer publishes to a topic. All subscribers to that topic get a copy.",
                ],
            },
            {
                "id": "mq_3",
                "type": "quiz",
                "title": "Kafka's Superpower",
                "question": (
                    "Apache Kafka stores messages in an immutable, ordered log.\n"
                    "Consumers track their position (offset) in the log.\n\n"
                    "What does this enable that traditional queues don't?"
                ),
                "lesson": (
                    "Kafka's log-based architecture enables message replay.\n\n"
                    "Traditional queues: message is deleted after consumption. Gone forever.\n"
                    "Kafka: messages are retained for a configurable period (hours/days/forever).\n"
                    "A consumer can rewind to any offset and re-process messages.\n\n"
                    "Use cases enabled by replay:\n"
                    "  - Reprocessing after a bug fix\n"
                    "  - Adding a new consumer that needs historical data\n"
                    "  - Rebuilding a read model or search index\n"
                    "  - Auditing and debugging\n\n"
                    "Kafka partitions enable parallel consumption. Consumer groups enable\n"
                    "load distribution across consumers within the same group."
                ),
                "options": [
                    "Faster message delivery via zero-copy transfers",
                    "Consumers can replay messages by resetting their offset",
                    "Automatic schema validation of all messages",
                    "Built-in exactly-once delivery without any configuration",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "If messages are stored in an immutable log, what can a consumer do with old offsets?",
                    "Replay. Rewind. Reprocess.",
                ],
            },
            {
                "id": "mq_4",
                "type": "quiz",
                "title": "Dead Letter Queue",
                "question": (
                    "A message fails processing 5 times in a row. The consumer keeps\n"
                    "crashing on it. Other messages are backing up behind it.\n\n"
                    "What pattern prevents a single poison message from blocking the queue?"
                ),
                "lesson": (
                    "Dead Letter Queue (DLQ) — a separate queue for messages that fail\n"
                    "repeatedly.\n\n"
                    "After N failed processing attempts, the message is moved to the DLQ\n"
                    "instead of being retried forever. The main queue continues processing.\n\n"
                    "DLQ workflow:\n"
                    "  1. Message fails processing → retry\n"
                    "  2. Fails again → retry (up to max retries)\n"
                    "  3. Max retries exceeded → move to DLQ\n"
                    "  4. Alert on DLQ depth\n"
                    "  5. Engineers investigate and manually reprocess or discard\n\n"
                    "AWS SQS, RabbitMQ, and Kafka (via error topics) all support DLQs."
                ),
                "options": [
                    "Circuit breaker",
                    "Dead letter queue",
                    "Message deduplication",
                    "Priority queue",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The poison message needs to go somewhere that isn't the main queue.",
                    "It's called a 'dead letter' because the message can't be delivered.",
                ],
            },
            {
                "id": "mq_5",
                "type": "quiz",
                "title": "Backpressure",
                "question": (
                    "Your producer is publishing 10,000 messages/sec.\n"
                    "Your consumer can only process 2,000 messages/sec.\n"
                    "The queue depth is growing without bound.\n\n"
                    "What mechanism should the system use to handle this?"
                ),
                "lesson": (
                    "Backpressure — signaling upstream to slow down when downstream\n"
                    "can't keep up.\n\n"
                    "Without backpressure: queue grows → memory exhaustion → crash.\n\n"
                    "Backpressure strategies:\n"
                    "  - Rate limiting the producer (reject/throttle above threshold)\n"
                    "  - Bounded queue (block producer when queue is full)\n"
                    "  - Load shedding (drop low-priority messages)\n"
                    "  - Scale consumers (add more workers)\n"
                    "  - Adaptive batching (consumers process in larger batches)\n\n"
                    "The key insight: if consumers are slower than producers for a sustained\n"
                    "period, no amount of queue depth will save you. You must either slow\n"
                    "the producer, speed the consumer, or accept data loss."
                ),
                "options": [
                    "Increase the queue size to buffer more messages",
                    "Backpressure — signal the producer to slow down or scale consumers",
                    "Switch to a faster message broker",
                    "Add a cache in front of the queue",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Bigger buffers just delay the inevitable if the rate mismatch persists.",
                    "The system needs to push back on the producer or speed up the consumer.",
                ],
            },
            {
                "id": "mq_6",
                "type": "quiz",
                "title": "RabbitMQ vs Kafka vs SQS",
                "question": (
                    "You need a fully managed queue with zero operational overhead,\n"
                    "running on AWS, for a simple task-processing pipeline.\n"
                    "You don't need message replay or ordering guarantees.\n\n"
                    "Which is the best fit?"
                ),
                "lesson": (
                    "Amazon SQS — fully managed, serverless message queue.\n\n"
                    "  SQS: Zero ops. Pay per message. No replay. At-least-once delivery.\n"
                    "        Best for simple task queues on AWS.\n\n"
                    "  RabbitMQ: Self-managed (or Amazon MQ). Rich routing (exchanges,\n"
                    "            bindings). Complex topologies. Good for request-reply.\n\n"
                    "  Kafka: Self-managed (or Confluent/MSK). Log-based. Message replay.\n"
                    "         High throughput. Ordering within partitions. Best for\n"
                    "         event streaming and real-time pipelines.\n\n"
                    "Choose based on: managed vs self-hosted, replay needs, throughput,\n"
                    "routing complexity, and ordering requirements."
                ),
                "options": [
                    "Apache Kafka",
                    "RabbitMQ",
                    "Amazon SQS",
                    "Redis Pub/Sub",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The requirements are: fully managed, AWS, zero ops, simple pipeline.",
                    "Which one is a native AWS service that requires zero infrastructure management?",
                ],
            },
        ],
    },

    # ── ZONE 4: MICROSERVICES ──────────────────────────────────────────
    "microservices": {
        "id": "microservices",
        "name": "The Microservices Mesh",
        "subtitle": "Monolith vs Microservices, API Gateway, Service Mesh & Circuit Breaker",
        "color": "magenta",
        "icon": "🔌",
        "commands": ["api-gateway", "service-mesh", "circuit-breaker", "sidecar", "bounded-context"],
        "challenges": [
            {
                "id": "micro_1",
                "type": "quiz",
                "title": "Monolith vs Microservices",
                "question": (
                    "Your startup has 3 developers. The app has a user service,\n"
                    "a payment service, and a notification service — all in one\n"
                    "deployable unit.\n\n"
                    "What is this architecture called?"
                ),
                "lesson": (
                    "A monolith — a single deployable unit containing all services.\n\n"
                    "Monolith advantages:\n"
                    "  - Simple to develop, test, deploy, and debug\n"
                    "  - No network calls between services (in-process)\n"
                    "  - One codebase, one deployment pipeline\n"
                    "  - Perfect for small teams (< 10 developers)\n\n"
                    "Monolith disadvantages (at scale):\n"
                    "  - One team's change can break everything\n"
                    "  - Scaling means scaling everything (even unused parts)\n"
                    "  - Deploy cycle slows as codebase grows\n"
                    "  - Technology lock-in (one language, one framework)"
                ),
                "options": [
                    "Microservices architecture",
                    "Monolithic architecture",
                    "Serverless architecture",
                    "Event-driven architecture",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Everything is in one deployable unit.",
                    "Mono = one. Lith = stone. One big rock.",
                ],
            },
            {
                "id": "micro_2",
                "type": "quiz",
                "title": "Service Boundaries",
                "question": (
                    "When splitting a monolith into microservices, each service should\n"
                    "align with a ___: an area of the business with its own data,\n"
                    "rules, and language.\n\n"
                    "This concept comes from Domain-Driven Design."
                ),
                "lesson": (
                    "Bounded context — a DDD concept defining a boundary within which\n"
                    "a domain model applies.\n\n"
                    "Each microservice should own one bounded context:\n"
                    "  - Orders service owns order data and order logic\n"
                    "  - Payments service owns payment data and payment logic\n"
                    "  - Users service owns user data and authentication logic\n\n"
                    "Services should NOT share databases. If the orders service needs\n"
                    "user data, it calls the users service API — not the users table.\n\n"
                    "Bad boundary: splitting by technical layer (API, business logic, data)\n"
                    "Good boundary: splitting by business capability"
                ),
                "options": [
                    "Technical layer",
                    "Database table",
                    "Bounded context",
                    "API endpoint",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "It's a Domain-Driven Design concept about defining clear boundaries.",
                    "Each microservice should own its own bounded ___.",
                ],
            },
            {
                "id": "micro_3",
                "type": "quiz",
                "title": "API Gateway",
                "question": (
                    "Your mobile app needs data from 5 microservices for a single screen.\n"
                    "Making 5 separate API calls from the client is slow and fragile.\n\n"
                    "What pattern provides a single entry point that aggregates the calls?"
                ),
                "lesson": (
                    "API Gateway — a single entry point for all client requests.\n\n"
                    "The gateway receives one request from the client, fans out to the\n"
                    "relevant microservices, aggregates the responses, and returns one\n"
                    "response to the client.\n\n"
                    "API Gateway responsibilities:\n"
                    "  - Request routing (which service handles which path)\n"
                    "  - Request aggregation (combine multiple service calls)\n"
                    "  - Authentication & authorization\n"
                    "  - Rate limiting\n"
                    "  - SSL termination\n"
                    "  - Response caching\n\n"
                    "Examples: Kong, AWS API Gateway, Nginx, Envoy, Traefik."
                ),
                "options": [
                    "Service mesh",
                    "API Gateway",
                    "Load balancer",
                    "Reverse proxy",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's a single entry point that aggregates calls to multiple backend services.",
                    "The client makes one call. The ___ fans out to five services.",
                ],
            },
            {
                "id": "micro_4",
                "type": "quiz",
                "title": "Circuit Breaker",
                "question": (
                    "Service A calls Service B. Service B is down. Service A keeps\n"
                    "retrying, tying up threads, and eventually becomes unresponsive too.\n\n"
                    "What pattern prevents this cascading failure?"
                ),
                "lesson": (
                    "Circuit Breaker — prevents cascading failures by failing fast.\n\n"
                    "States:\n"
                    "  CLOSED:    Normal. Requests flow through. Failures are counted.\n"
                    "  OPEN:      Too many failures. All requests fail immediately.\n"
                    "             No calls to the downstream service.\n"
                    "  HALF-OPEN: After a timeout, allow one test request through.\n"
                    "             If it succeeds → CLOSED. If it fails → OPEN.\n\n"
                    "Without circuit breaker: Service B is down → Service A retries →\n"
                    "  A's thread pool is exhausted → A becomes unresponsive →\n"
                    "  Everything calling A cascades.\n\n"
                    "Libraries: Hystrix (Netflix), Resilience4j (Java), Polly (.NET)."
                ),
                "options": [
                    "Retry with exponential backoff",
                    "Circuit breaker",
                    "Bulkhead pattern",
                    "Timeout pattern",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Named after electrical circuit breakers that trip to prevent damage.",
                    "It has three states: closed, open, and half-open.",
                ],
            },
            {
                "id": "micro_5",
                "type": "quiz",
                "title": "Service Mesh",
                "question": (
                    "You have 50 microservices. Each one needs: mTLS, retries,\n"
                    "circuit breaking, observability, and traffic management.\n\n"
                    "Instead of implementing this in every service, you deploy a\n"
                    "sidecar proxy next to each service. What is this infrastructure called?"
                ),
                "lesson": (
                    "Service Mesh — a dedicated infrastructure layer for service-to-service\n"
                    "communication.\n\n"
                    "Each service gets a sidecar proxy (e.g., Envoy) that intercepts all\n"
                    "network traffic. The proxies handle:\n"
                    "  - mTLS (mutual TLS between all services)\n"
                    "  - Retries & circuit breaking\n"
                    "  - Load balancing\n"
                    "  - Traffic splitting (canary, blue-green)\n"
                    "  - Observability (metrics, traces, access logs)\n\n"
                    "The application code knows nothing about this. The mesh handles it.\n\n"
                    "Service meshes: Istio, Linkerd, Consul Connect.\n"
                    "Trade-off: significant operational complexity and latency overhead."
                ),
                "options": [
                    "API gateway",
                    "Container orchestrator",
                    "Service mesh",
                    "Load balancer cluster",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Sidecar proxies next to each service, handling cross-cutting concerns.",
                    "Istio and Linkerd are the most well-known implementations.",
                ],
            },
        ],
    },

    # ── ZONE 5: DATABASE AT SCALE ──────────────────────────────────────
    "database_at_scale": {
        "id": "database_at_scale",
        "name": "Database at Scale",
        "subtitle": "Read Replicas, Sharding, CQRS, Event Sourcing & Polyglot Persistence",
        "color": "red",
        "icon": "🗄️",
        "commands": ["replica", "shard", "CQRS", "event-source", "polyglot"],
        "challenges": [
            {
                "id": "db_1",
                "type": "quiz",
                "title": "Read Replicas",
                "question": (
                    "Your database handles 90% reads and 10% writes.\n"
                    "The primary instance is at CPU capacity.\n\n"
                    "What is the simplest way to reduce read load on the primary?"
                ),
                "lesson": (
                    "Read replicas — copies of the primary database that serve read queries.\n\n"
                    "  Primary (leader): handles all writes\n"
                    "  Replicas (followers): receive writes via replication, serve reads\n\n"
                    "If 90% of queries are reads, 3 replicas reduce primary load by ~90%.\n"
                    "The primary now only handles writes.\n\n"
                    "Replication lag: replicas may be slightly behind the primary.\n"
                    "  - Acceptable for: product listings, analytics, dashboards\n"
                    "  - Not acceptable for: account balance after a transfer\n\n"
                    "For read-after-write consistency, route the write AND the\n"
                    "subsequent read to the primary."
                ),
                "options": [
                    "Add read replicas to handle read queries",
                    "Shard the database across multiple nodes",
                    "Add a message queue in front of the database",
                    "Switch to a NoSQL database",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "90% reads, 10% writes. Offload the 90% to something.",
                    "Copies of the database that serve read traffic.",
                ],
            },
            {
                "id": "db_2",
                "type": "quiz",
                "title": "Database Sharding",
                "question": (
                    "Your users table has 500 million rows. A single database server\n"
                    "can no longer handle the write volume or storage.\n\n"
                    "You split the table across 8 database servers, each holding a\n"
                    "range of user IDs. What is this technique called?"
                ),
                "lesson": (
                    "Sharding (horizontal partitioning) — splitting data across multiple\n"
                    "database instances.\n\n"
                    "Each shard holds a subset of the data. Sharding strategies:\n"
                    "  - Range-based: user_id 1-1M → shard 1, 1M-2M → shard 2\n"
                    "  - Hash-based: shard = hash(user_id) % num_shards\n"
                    "  - Directory-based: lookup table maps keys to shards\n\n"
                    "Sharding challenges:\n"
                    "  - Cross-shard queries are expensive (joins across databases)\n"
                    "  - Resharding is painful (adding/removing shards)\n"
                    "  - Hotspots (one shard gets disproportionate traffic)\n"
                    "  - Operational complexity (N databases to manage)"
                ),
                "options": [
                    "Replication",
                    "Sharding",
                    "Indexing",
                    "Normalization",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You're splitting the data horizontally across multiple servers.",
                    "Each server holds a 'shard' — a piece of the full dataset.",
                ],
            },
            {
                "id": "db_3",
                "type": "quiz",
                "title": "CQRS",
                "question": (
                    "Your application's read model (denormalized, fast) is very different\n"
                    "from its write model (normalized, consistent). Updates are complex\n"
                    "and reads need to be lightning fast.\n\n"
                    "What pattern separates reads from writes into different models?"
                ),
                "lesson": (
                    "CQRS — Command Query Responsibility Segregation.\n\n"
                    "Separate the write model (commands) from the read model (queries).\n\n"
                    "  Commands: create, update, delete → write-optimized store\n"
                    "  Queries: read, search, list → read-optimized store\n\n"
                    "The write store might be a normalized relational DB.\n"
                    "The read store might be a denormalized view, Elasticsearch, or a cache.\n"
                    "An event/sync mechanism keeps them consistent (eventually).\n\n"
                    "CQRS adds complexity. Use it when:\n"
                    "  - Read and write patterns are radically different\n"
                    "  - You need independent scaling of reads vs writes\n"
                    "  - You need different data models for reads vs writes"
                ),
                "options": [
                    "Event sourcing",
                    "Database sharding",
                    "CQRS",
                    "Materialized views",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Commands for writes, Queries for reads — separated into different models.",
                    "CQRS = Command Query Responsibility ___.",
                ],
            },
            {
                "id": "db_4",
                "type": "quiz",
                "title": "Event Sourcing",
                "question": (
                    "Instead of storing the current state of an order, you store\n"
                    "every event: OrderCreated, ItemAdded, PaymentReceived, OrderShipped.\n"
                    "Current state is derived by replaying all events.\n\n"
                    "What is this pattern called?"
                ),
                "lesson": (
                    "Event Sourcing — storing every state change as an immutable event.\n\n"
                    "Traditional: store current state in a row. UPDATE overwrites it.\n"
                    "Event sourcing: store every event. Current state = replay all events.\n\n"
                    "  Event log: [OrderCreated, ItemAdded, ItemAdded, PaymentReceived]\n"
                    "  Current state: order with 2 items, paid, not yet shipped.\n\n"
                    "Advantages:\n"
                    "  - Complete audit trail (every change is recorded)\n"
                    "  - Temporal queries (what was the state at 3pm yesterday?)\n"
                    "  - Event replay (rebuild read models, fix bugs retroactively)\n\n"
                    "Disadvantages:\n"
                    "  - Complexity (replay can be slow for long event streams)\n"
                    "  - Eventually consistent reads (unless using snapshots)"
                ),
                "options": [
                    "Event sourcing",
                    "Change data capture",
                    "Write-ahead logging",
                    "CQRS",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "Every state change is stored as an immutable event in a log.",
                    "Current state is derived by replaying the event stream from the beginning.",
                ],
            },
            {
                "id": "db_5",
                "type": "quiz",
                "title": "Polyglot Persistence",
                "question": (
                    "Your system uses PostgreSQL for transactions, Redis for sessions,\n"
                    "Elasticsearch for search, and S3 for file storage.\n\n"
                    "What is this strategy of using different databases for different\n"
                    "needs called?"
                ),
                "lesson": (
                    "Polyglot persistence — using multiple database technologies,\n"
                    "each chosen for the workload it serves best.\n\n"
                    "  PostgreSQL: ACID transactions, complex queries, relational data\n"
                    "  Redis: sub-millisecond key-value lookups, sessions, caching\n"
                    "  Elasticsearch: full-text search, log analytics\n"
                    "  MongoDB: flexible schema, document storage\n"
                    "  Cassandra: massive write throughput, time-series data\n"
                    "  S3: unlimited object storage, files, backups\n\n"
                    "One database does not fit all workloads. The tradeoff:\n"
                    "operational complexity of running multiple data stores vs\n"
                    "performance gains from using the right tool for each job."
                ),
                "options": [
                    "Database federation",
                    "Polyglot persistence",
                    "Multi-master replication",
                    "Data lake architecture",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Polyglot = many languages. Each 'language' is a different database tech.",
                    "Use the right database for each job instead of forcing one to do everything.",
                ],
            },
            {
                "id": "db_6",
                "type": "quiz",
                "title": "CAP Theorem",
                "question": (
                    "The CAP theorem states a distributed system can only guarantee\n"
                    "two out of three properties: Consistency, Availability, and\n"
                    "Partition tolerance.\n\n"
                    "In a network partition, you must choose between C and A.\n"
                    "What does choosing Availability mean?"
                ),
                "lesson": (
                    "CAP Theorem — in a network partition, you choose:\n\n"
                    "  CP (Consistency + Partition tolerance):\n"
                    "    Refuse to serve requests if data might be stale.\n"
                    "    Example: return an error until the partition heals.\n\n"
                    "  AP (Availability + Partition tolerance):\n"
                    "    Always respond, even if the data might be stale.\n"
                    "    Example: serve cached/local data, reconcile later.\n\n"
                    "CP systems: HBase, MongoDB (default), etcd, ZooKeeper\n"
                    "AP systems: Cassandra, DynamoDB, CouchDB\n\n"
                    "In practice, partitions are rare. The real tradeoff is latency vs\n"
                    "consistency (PACELC theorem: in the absence of partitions,\n"
                    "choose between Latency and Consistency)."
                ),
                "options": [
                    "The system returns errors until the partition is resolved",
                    "The system always responds, even with potentially stale data",
                    "The system shuts down to prevent data corruption",
                    "The system switches to a single-node mode",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Availability means the system always responds to requests.",
                    "The tradeoff: you get a response, but it might not be the latest data.",
                ],
            },
        ],
    },

    # ── ZONE 6: CDN AND EDGE ──────────────────────────────────────────
    "cdn_and_edge": {
        "id": "cdn_and_edge",
        "name": "CDN & Edge Computing",
        "subtitle": "Content Delivery, Edge Functions, Cache Headers & Geographic Distribution",
        "color": "blue",
        "icon": "🌐",
        "commands": ["CDN", "edge-function", "Cache-Control", "ETag", "origin"],
        "challenges": [
            {
                "id": "cdn_1",
                "type": "quiz",
                "title": "How a CDN Works",
                "question": (
                    "A user in Sydney requests an image. The origin server is in\n"
                    "Virginia. A CDN has a point of presence (PoP) in Sydney.\n\n"
                    "What happens on the first request?"
                ),
                "lesson": (
                    "CDN first request (cache miss):\n\n"
                    "  1. User in Sydney → CDN PoP in Sydney (cache miss)\n"
                    "  2. CDN PoP fetches from origin in Virginia\n"
                    "  3. Origin returns the image\n"
                    "  4. CDN PoP caches the image and serves it to the user\n"
                    "  5. Subsequent requests from Sydney are served from the local PoP\n\n"
                    "This is called a pull-based CDN. The CDN lazily populates its cache.\n"
                    "Push-based CDNs require you to upload content to the CDN proactively.\n\n"
                    "After the first request, all Sydney users get the image in ~5ms\n"
                    "instead of ~200ms."
                ),
                "options": [
                    "The CDN serves the image instantly from its Sydney cache",
                    "The CDN fetches the image from the origin, caches it, then serves it",
                    "The CDN redirects the user directly to the origin server",
                    "The CDN replicates all origin content to Sydney before the request",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's the first request — the CDN's Sydney cache is empty.",
                    "Cache miss → fetch from origin → cache locally → serve.",
                ],
            },
            {
                "id": "cdn_2",
                "type": "quiz",
                "title": "Cache-Control Header",
                "question": (
                    "You want browsers to cache a CSS file for 1 year, but CDN edge\n"
                    "nodes should revalidate after 1 hour.\n\n"
                    "Which header combination achieves this?"
                ),
                "lesson": (
                    "Cache-Control directives:\n\n"
                    "  max-age=N       → browser can cache for N seconds\n"
                    "  s-maxage=N      → shared caches (CDN) can cache for N seconds\n"
                    "  no-cache        → must revalidate before using cached copy\n"
                    "  no-store        → never cache at all\n"
                    "  public          → any cache can store (including CDN)\n"
                    "  private         → only browser can cache (not CDN)\n"
                    "  immutable       → content will never change (skip revalidation)\n\n"
                    "s-maxage overrides max-age for shared caches (CDN edge nodes)\n"
                    "but browsers still use max-age.\n\n"
                    "  Cache-Control: public, max-age=31536000, s-maxage=3600\n"
                    "  → browser: 1 year. CDN: 1 hour."
                ),
                "options": [
                    "Cache-Control: private, max-age=3600",
                    "Cache-Control: public, max-age=31536000, s-maxage=3600",
                    "Cache-Control: no-cache, max-age=31536000",
                    "Cache-Control: public, max-age=3600",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "You need different TTLs for browsers (max-age) and CDNs (s-maxage).",
                    "s-maxage controls the CDN. max-age controls the browser.",
                ],
            },
            {
                "id": "cdn_3",
                "type": "quiz",
                "title": "Static vs Dynamic Content",
                "question": (
                    "Which type of content benefits MOST from CDN caching?\n\n"
                    "  a) User-specific dashboard data\n"
                    "  b) Real-time stock prices\n"
                    "  c) Static assets (images, CSS, JS)\n"
                    "  d) Database query results"
                ),
                "lesson": (
                    "Static content = same response for every user. Perfect for CDN caching.\n"
                    "Dynamic content = varies per user or changes frequently. Harder to cache.\n\n"
                    "CDN-friendly (static):\n"
                    "  - Images, CSS, JavaScript, fonts, videos\n"
                    "  - Public pages that are the same for everyone\n"
                    "  - API responses that rarely change (product catalog)\n\n"
                    "CDN-unfriendly (dynamic):\n"
                    "  - User-specific data (dashboards, carts)\n"
                    "  - Real-time data (stock prices, chat)\n"
                    "  - Authenticated API responses\n\n"
                    "Modern CDNs (Cloudflare Workers, CloudFront Functions) can run code\n"
                    "at the edge to personalize responses, blurring the line."
                ),
                "options": [
                    "User-specific dashboard data",
                    "Real-time stock prices",
                    "Static assets (images, CSS, JS)",
                    "Database query results",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "CDNs work best when the content is the same for every user.",
                    "Images and JavaScript files don't change per user.",
                ],
            },
            {
                "id": "cdn_4",
                "type": "quiz",
                "title": "Edge Computing",
                "question": (
                    "Instead of just caching static files, you run code at CDN edge\n"
                    "locations — auth checks, A/B testing, header manipulation — all\n"
                    "without hitting the origin.\n\n"
                    "What is this called?"
                ),
                "lesson": (
                    "Edge computing — running computation at CDN edge locations,\n"
                    "geographically close to users.\n\n"
                    "Edge function platforms:\n"
                    "  Cloudflare Workers — V8 isolates, global deployment\n"
                    "  AWS CloudFront Functions — lightweight, viewer-facing logic\n"
                    "  AWS Lambda@Edge — full Lambda at edge locations\n"
                    "  Deno Deploy — globally distributed Deno runtime\n"
                    "  Vercel Edge Functions — built on Cloudflare Workers\n\n"
                    "Use cases:\n"
                    "  - Authentication/authorization at the edge\n"
                    "  - A/B testing (route users to variants)\n"
                    "  - Geolocation-based responses\n"
                    "  - Bot detection and rate limiting\n"
                    "  - Image optimization and resizing"
                ),
                "options": [
                    "Serverless computing",
                    "Edge computing",
                    "Fog computing",
                    "Grid computing",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The code runs at the 'edge' of the network, near the user.",
                    "Cloudflare Workers and Lambda@Edge are examples.",
                ],
            },
            {
                "id": "cdn_5",
                "type": "quiz",
                "title": "Cache Busting",
                "question": (
                    "You deploy a new version of your JavaScript bundle. CDN edge\n"
                    "nodes are still serving the old version (cached for 1 year).\n\n"
                    "What technique ensures users get the new version immediately?"
                ),
                "lesson": (
                    "Cache busting — changing the URL so the CDN treats it as a new resource.\n\n"
                    "Strategies:\n"
                    "  - Content hash in filename: app.a1b2c3.js (best practice)\n"
                    "    New build → new hash → new URL → CDN fetches from origin\n"
                    "  - Query string: app.js?v=2.0 (works but some CDNs ignore query strings)\n"
                    "  - CDN invalidation: manually purge the cached file\n"
                    "    (slow, expensive at scale, can take minutes to propagate)\n\n"
                    "Best practice: immutable assets with content-hashed filenames.\n"
                    "  Cache-Control: public, max-age=31536000, immutable\n"
                    "New deploys produce new filenames. Old cache entries expire naturally."
                ),
                "options": [
                    "Reduce the TTL to 5 minutes for all assets",
                    "Use content-hashed filenames so new versions have new URLs",
                    "Disable CDN caching and serve everything from origin",
                    "Restart all CDN edge nodes",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "If the URL changes, the CDN treats it as a new resource.",
                    "app.a1b2c3.js → deploy → app.d4e5f6.js. New URL, cache miss, fresh content.",
                ],
            },
        ],
    },

    # ── ZONE 7: RELIABILITY ────────────────────────────────────────────
    "reliability": {
        "id": "reliability",
        "name": "Reliability Engineering",
        "subtitle": "SLAs, Redundancy, Failover, Chaos Engineering & Graceful Degradation",
        "color": "white",
        "icon": "🛡️",
        "commands": ["SLA", "SLO", "failover", "chaos", "bulkhead"],
        "challenges": [
            {
                "id": "rel_1",
                "type": "quiz",
                "title": "SLA vs SLO vs SLI",
                "question": (
                    "Your team promises customers 99.9% uptime in a contract.\n"
                    "Internally, you target 99.95% to have a buffer.\n"
                    "You measure actual uptime at 99.97%.\n\n"
                    "Which is the SLA?"
                ),
                "lesson": (
                    "SLI (Service Level Indicator) — the actual measured metric.\n"
                    "  Example: 99.97% uptime this month.\n\n"
                    "SLO (Service Level Objective) — the internal target.\n"
                    "  Example: we aim for 99.95% uptime.\n\n"
                    "SLA (Service Level Agreement) — the contractual promise with penalties.\n"
                    "  Example: we guarantee 99.9% uptime or issue credits.\n\n"
                    "  SLI ≥ SLO ≥ SLA\n\n"
                    "Set SLO higher than SLA to create an error budget — the margin between\n"
                    "what you promise and what you target. If your SLI drops below SLO but\n"
                    "stays above SLA, it's a warning, not a breach."
                ),
                "options": [
                    "99.97% (actual uptime)",
                    "99.95% (internal target)",
                    "99.9% (contractual promise)",
                    "All three are the SLA",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The SLA is the promise made to the customer in a contract.",
                    "A = Agreement. The one with penalties if broken.",
                ],
            },
            {
                "id": "rel_2",
                "type": "quiz",
                "title": "The Nines",
                "question": (
                    "A service has an SLA of 99.99% uptime ('four nines').\n"
                    "How much downtime is allowed per year?"
                ),
                "lesson": (
                    "Availability nines and annual downtime:\n\n"
                    "  99%      → 3.65 days/year     (two nines)\n"
                    "  99.9%    → 8.76 hours/year     (three nines)\n"
                    "  99.95%   → 4.38 hours/year\n"
                    "  99.99%   → 52.6 minutes/year   (four nines)\n"
                    "  99.999%  → 5.26 minutes/year   (five nines)\n\n"
                    "Each additional nine is exponentially harder and more expensive.\n"
                    "Going from 99.9% to 99.99% requires redundancy, failover,\n"
                    "automated recovery, and zero-downtime deployments.\n\n"
                    "Five nines (99.999%) means you can be down for about 5 minutes\n"
                    "per year. That's 26 seconds per month."
                ),
                "options": [
                    "About 8.7 hours",
                    "About 52 minutes",
                    "About 5 minutes",
                    "About 8.7 minutes",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Four nines = 99.99%. The allowed downtime is under an hour per year.",
                    "0.01% of a year (525,600 minutes) is about 52.6 minutes.",
                ],
            },
            {
                "id": "rel_3",
                "type": "quiz",
                "title": "Failover Strategy",
                "question": (
                    "Your primary database in us-east-1 goes down.\n"
                    "A standby replica in us-west-2 is promoted to primary\n"
                    "automatically within 60 seconds.\n\n"
                    "What is this called?"
                ),
                "lesson": (
                    "Automatic failover — promoting a standby to primary when the\n"
                    "primary fails, without human intervention.\n\n"
                    "Failover strategies:\n"
                    "  Active-passive: one primary, one or more standbys on standby.\n"
                    "    Standby is promoted on failure. Some data loss possible\n"
                    "    (replication lag between primary and standby).\n\n"
                    "  Active-active: multiple nodes serve traffic simultaneously.\n"
                    "    If one fails, others absorb the load. More complex (conflict\n"
                    "    resolution needed for concurrent writes).\n\n"
                    "  Multi-region: standby in a different geographic region.\n"
                    "    Survives full region outages. Higher replication lag."
                ),
                "options": [
                    "Load balancing",
                    "Automatic failover",
                    "Hot standby replication",
                    "Disaster recovery drill",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The standby is automatically promoted when the primary goes down.",
                    "Failover = failing over to a backup system.",
                ],
            },
            {
                "id": "rel_4",
                "type": "quiz",
                "title": "Chaos Engineering",
                "question": (
                    "Netflix intentionally kills random production servers to verify\n"
                    "their system can handle failures. Their tool is called Chaos Monkey.\n\n"
                    "What is this practice called?"
                ),
                "lesson": (
                    "Chaos engineering — deliberately injecting failures into production\n"
                    "to test system resilience.\n\n"
                    "Principles:\n"
                    "  1. Define steady state (normal system behavior)\n"
                    "  2. Hypothesize that steady state continues during failure\n"
                    "  3. Inject failures (kill instances, add latency, corrupt data)\n"
                    "  4. Observe if steady state is maintained\n\n"
                    "Netflix tools:\n"
                    "  Chaos Monkey — kills random instances\n"
                    "  Chaos Kong — simulates full region outage\n"
                    "  Latency Monkey — adds artificial latency\n\n"
                    "Other tools: Gremlin, LitmusChaos, AWS Fault Injection Simulator.\n\n"
                    "If your system can't survive a killed instance in testing,\n"
                    "it definitely can't survive one in production at 3 AM."
                ),
                "options": [
                    "Penetration testing",
                    "Chaos engineering",
                    "Load testing",
                    "Fault injection testing",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Netflix's practice of deliberately causing failures in production.",
                    "Chaos Monkey is the most famous tool in this discipline.",
                ],
            },
            {
                "id": "rel_5",
                "type": "quiz",
                "title": "Graceful Degradation",
                "question": (
                    "Your e-commerce site's recommendation engine goes down.\n"
                    "Instead of showing an error, the product page shows a static\n"
                    "'Popular Items' list and continues working.\n\n"
                    "What pattern is this?"
                ),
                "lesson": (
                    "Graceful degradation — reducing functionality instead of failing entirely.\n\n"
                    "  Full functionality: personalized recommendations\n"
                    "  Degraded: static 'popular items' list (fallback)\n"
                    "  Failed: error page, site down\n\n"
                    "The user experience is worse, but the core function (buying products)\n"
                    "still works. The alternative — showing an error — loses the sale.\n\n"
                    "Examples:\n"
                    "  - Image service down → show placeholders\n"
                    "  - Search service down → show browse categories\n"
                    "  - Payment provider down → queue the order, confirm later\n"
                    "  - Analytics down → page works fine, just no tracking"
                ),
                "options": [
                    "Circuit breaker",
                    "Graceful degradation",
                    "Failover",
                    "Load shedding",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The system degrades its functionality gracefully instead of crashing.",
                    "Reduced feature set, but the core experience still works.",
                ],
            },
            {
                "id": "rel_6",
                "type": "quiz",
                "title": "Bulkhead Pattern",
                "question": (
                    "Service A has one shared thread pool for all downstream calls.\n"
                    "When Service B becomes slow, all threads are consumed waiting\n"
                    "for B, and calls to Service C (which is healthy) also fail.\n\n"
                    "What pattern isolates resources so one slow dependency doesn't\n"
                    "consume everything?"
                ),
                "lesson": (
                    "Bulkhead pattern — isolating resources into separate pools.\n\n"
                    "Named after ship bulkheads: watertight compartments that prevent\n"
                    "a single breach from sinking the entire ship.\n\n"
                    "  Without bulkhead: one shared thread pool.\n"
                    "    Slow Service B → all threads blocked → Service C calls fail too.\n\n"
                    "  With bulkhead: separate thread pools per dependency.\n"
                    "    Pool for B (10 threads) — exhausted, B calls fail.\n"
                    "    Pool for C (10 threads) — unaffected, C calls succeed.\n\n"
                    "Bulkhead can be implemented at multiple levels:\n"
                    "  - Thread pools per dependency\n"
                    "  - Connection pools per dependency\n"
                    "  - Separate process/container per service\n"
                    "  - Separate infrastructure per tenant (multi-tenant isolation)"
                ),
                "options": [
                    "Circuit breaker",
                    "Rate limiting",
                    "Bulkhead pattern",
                    "Retry with backoff",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Named after watertight compartments in a ship's hull.",
                    "Isolate resources so one slow dependency can't consume everything.",
                ],
            },
        ],
    },

    # ── ZONE 8: DESIGN INTERVIEWS ──────────────────────────────────────
    "design_interviews": {
        "id": "design_interviews",
        "name": "Design Interviews",
        "subtitle": "URL Shortener, Chat System, Notification Service & How to Approach Design",
        "color": "bright_white",
        "icon": "🏗️",
        "commands": ["clarify", "estimate", "high-level-design", "deep-dive", "tradeoffs"],
        "challenges": [
            {
                "id": "di_1",
                "type": "quiz",
                "title": "The Framework",
                "question": (
                    "You're given a system design interview question.\n"
                    "What should you do FIRST?"
                ),
                "lesson": (
                    "System design interview framework:\n\n"
                    "  1. CLARIFY requirements (5 min)\n"
                    "     - Functional: what does the system do?\n"
                    "     - Non-functional: scale, latency, availability, consistency?\n"
                    "     - Scope: what's in/out for this discussion?\n\n"
                    "  2. ESTIMATE scale (3 min)\n"
                    "     - Users, requests/sec, storage, bandwidth\n\n"
                    "  3. HIGH-LEVEL DESIGN (10 min)\n"
                    "     - Components, data flow, APIs\n\n"
                    "  4. DEEP DIVE (15 min)\n"
                    "     - Detailed design of critical components\n\n"
                    "  5. WRAP UP (5 min)\n"
                    "     - Tradeoffs, bottlenecks, future improvements\n\n"
                    "Never jump to the solution. Clarify first."
                ),
                "options": [
                    "Start drawing the architecture diagram immediately",
                    "Clarify requirements — ask what the system needs to do and at what scale",
                    "Choose the database technology",
                    "List all the microservices you'll need",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Before designing anything, you need to know what you're building.",
                    "Requirements first. Always. Ask questions before drawing boxes.",
                ],
            },
            {
                "id": "di_2",
                "type": "quiz",
                "title": "URL Shortener: Storage",
                "question": (
                    "Design a URL shortener (like bit.ly).\n"
                    "100M URLs created per month. Each short URL maps to one long URL.\n\n"
                    "What is the core data model?"
                ),
                "lesson": (
                    "URL shortener core: a key-value mapping.\n\n"
                    "  short_code (PK) → long_url\n"
                    "  'abc123'        → 'https://example.com/very/long/path'\n\n"
                    "Key generation strategies:\n"
                    "  - Base62 encoding of an auto-increment ID\n"
                    "    (a-z, A-Z, 0-9 = 62 chars. 7 chars = 62^7 = 3.5 trillion combos)\n"
                    "  - Random generation + collision check\n"
                    "  - MD5/SHA hash of the URL, take first N characters\n\n"
                    "Read:write ratio is heavily read-biased (100:1 or more).\n"
                    "Cache popular short codes in Redis for sub-ms redirects.\n"
                    "Storage: key-value store (DynamoDB, Redis) or relational DB."
                ),
                "options": [
                    "A graph database linking URLs to users",
                    "A key-value mapping: short_code → long_url",
                    "A relational schema with 5 normalized tables",
                    "A document store with nested URL metadata",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "At its core, a URL shortener maps a short code to a long URL.",
                    "The simplest model: key (short code) → value (original URL).",
                ],
            },
            {
                "id": "di_3",
                "type": "quiz",
                "title": "URL Shortener: Redirect",
                "question": (
                    "A user visits https://short.url/abc123.\n"
                    "The server looks up 'abc123' and finds the long URL.\n\n"
                    "What HTTP status code should the redirect use if you want\n"
                    "search engines to attribute traffic to the original URL?"
                ),
                "lesson": (
                    "HTTP redirect status codes:\n\n"
                    "  301 Moved Permanently\n"
                    "    Browser caches the redirect. Future requests skip the short URL\n"
                    "    server entirely. Good for SEO (transfers link juice).\n"
                    "    Bad for analytics (subsequent visits are invisible to you).\n\n"
                    "  302 Found (Temporary Redirect)\n"
                    "    Browser does NOT cache. Every click hits the short URL server.\n"
                    "    Good for analytics (you see every click).\n"
                    "    Bad for SEO (doesn't transfer link juice).\n\n"
                    "For a URL shortener that tracks clicks: use 302.\n"
                    "For pure SEO redirection: use 301."
                ),
                "options": [
                    "200 OK with the page content",
                    "301 Moved Permanently",
                    "302 Found (Temporary Redirect)",
                    "307 Temporary Redirect",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The question asks about SEO — attributing traffic to the original URL.",
                    "301 is the permanent redirect that transfers link authority.",
                ],
            },
            {
                "id": "di_4",
                "type": "quiz",
                "title": "Chat System: Protocol",
                "question": (
                    "You're designing a real-time chat system. Messages must appear\n"
                    "instantly — no polling.\n\n"
                    "What protocol enables persistent bidirectional communication\n"
                    "between client and server?"
                ),
                "lesson": (
                    "WebSockets — persistent, full-duplex communication over a single TCP\n"
                    "connection.\n\n"
                    "  HTTP: client sends request → server responds → connection done.\n"
                    "         Client must poll for updates. Wasteful.\n\n"
                    "  Long polling: client sends request → server holds it open until\n"
                    "                new data is available. Better, but still one-directional\n"
                    "                per request.\n\n"
                    "  WebSocket: client and server establish a persistent connection.\n"
                    "             Either side can send data at any time.\n"
                    "             No polling. No overhead per message.\n\n"
                    "Chat systems, multiplayer games, live dashboards, and collaborative\n"
                    "editing all use WebSockets for real-time communication."
                ),
                "options": [
                    "HTTP long polling",
                    "WebSockets",
                    "Server-Sent Events (SSE)",
                    "gRPC streaming",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You need persistent bidirectional communication — not just server→client.",
                    "It starts as an HTTP upgrade request and becomes a persistent TCP connection.",
                ],
            },
            {
                "id": "di_5",
                "type": "quiz",
                "title": "Notification Service: Delivery",
                "question": (
                    "Your notification service needs to deliver push notifications,\n"
                    "emails, and SMS. Each channel has different latency and failure\n"
                    "characteristics.\n\n"
                    "What architecture pattern decouples notification creation from delivery?"
                ),
                "lesson": (
                    "Event-driven architecture with message queues.\n\n"
                    "  1. Service creates notification event → publishes to message queue\n"
                    "  2. Separate workers consume from the queue:\n"
                    "     - Push notification worker → APNs/FCM\n"
                    "     - Email worker → SendGrid/SES\n"
                    "     - SMS worker → Twilio/SNS\n\n"
                    "Benefits:\n"
                    "  - Each channel scales independently\n"
                    "  - If email service is down, push and SMS still work\n"
                    "  - Retry logic per channel (SMS retry != email retry)\n"
                    "  - Rate limiting per channel (SMS is expensive, email is cheap)\n"
                    "  - Priority queues (security alerts before marketing)\n\n"
                    "The notification service doesn't know or care HOW messages are delivered.\n"
                    "It publishes an event. Workers handle the rest."
                ),
                "options": [
                    "Synchronous API calls to each notification provider",
                    "A message queue with separate workers for each delivery channel",
                    "A single worker that sends all notification types sequentially",
                    "Direct database polling by each notification provider",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Decouple creation from delivery. Each channel should scale independently.",
                    "A message queue lets each delivery worker process at its own pace.",
                ],
            },
            {
                "id": "di_6",
                "type": "quiz",
                "title": "Back-of-Envelope Estimation",
                "question": (
                    "You're designing a system for 10M daily active users.\n"
                    "Each user makes ~50 requests/day on average.\n\n"
                    "What is the approximate requests per second (RPS)?"
                ),
                "lesson": (
                    "Back-of-envelope estimation:\n\n"
                    "  10M users x 50 requests/day = 500M requests/day\n"
                    "  500M / 86,400 seconds/day ≈ ~5,800 RPS (average)\n\n"
                    "Peak traffic is typically 2-3x average:\n"
                    "  Peak: ~12,000 - 18,000 RPS\n\n"
                    "Useful approximations:\n"
                    "  1 day ≈ 100,000 seconds (actually 86,400)\n"
                    "  1 million requests/day ≈ 12 RPS\n"
                    "  1 billion requests/day ≈ 12,000 RPS\n\n"
                    "In interviews, round aggressively. The goal is order of magnitude,\n"
                    "not precision. 'About 6,000 RPS' is good enough.\n"
                    "The point is showing your thought process."
                ),
                "options": [
                    "About 500 RPS",
                    "About 6,000 RPS",
                    "About 60,000 RPS",
                    "About 500,000 RPS",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "500M requests per day. There are about 86,400 seconds in a day.",
                    "500,000,000 / 86,400 ≈ 5,800. Round to about 6,000.",
                ],
            },
        ],
    },
}
