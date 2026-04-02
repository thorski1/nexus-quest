"""
zones.py — Microservices zones and challenges for The Service Mesh.

5 zones, 8 challenges each (40 total). Mix of quiz and text challenges.
"""

ZONE_ORDER = [
    "microservice_fundamentals",
    "communication_patterns",
    "service_discovery",
    "data_management",
    "observability_resilience",
]

ZONES = {
    # ── ZONE 1: MICROSERVICE FUNDAMENTALS ─────────────────────────────
    "microservice_fundamentals": {
        "id": "microservice_fundamentals",
        "name": "The Decomposition Chamber",
        "subtitle": "Monoliths vs Microservices, Bounded Contexts & Service Boundaries",
        "color": "cyan",
        "icon": "\u2702",
        "commands": ["DECOMPOSE", "BOUND", "EXTRACT", "ISOLATE", "SPLIT"],
        "challenges": [
            {
                "id": "mf_1",
                "type": "quiz",
                "title": "Monolith vs Microservices",
                "question": (
                    "A team has a single deployable application with tightly coupled modules\n"
                    "for billing, user management, and inventory.\n\n"
                    "What is the primary architectural risk of this monolithic approach?"
                ),
                "options": [
                    "Each module runs in its own container",
                    "A failure in one module can cascade and bring down the entire application",
                    "Modules can be deployed independently without coordination",
                    "Horizontal scaling applies to individual modules",
                ],
                "answer": "b",
                "lesson": (
                    "In a monolith, all modules share a single process and deployment unit.\n\n"
                    "A memory leak in billing can starve the user management module of resources.\n"
                    "A deadlock in inventory can freeze the entire application. A bad deploy to\n"
                    "one module requires redeploying everything.\n\n"
                    "Microservices isolate failure domains. When billing crashes, users can\n"
                    "still log in and browse inventory. The blast radius is contained."
                ),
                "xp": 25,
                "hints": [
                    "Think about what happens when a single module fails in a shared process.",
                    "In a monolith, all modules share memory, threads, and deployment lifecycle.",
                ],
            },
            {
                "id": "mf_2",
                "type": "quiz",
                "title": "Bounded Context",
                "question": (
                    "In Domain-Driven Design, a bounded context defines the boundary\n"
                    "within which a particular domain model is valid.\n\n"
                    "What does a bounded context help you determine when decomposing a monolith?"
                ),
                "options": [
                    "The programming language each service should use",
                    "The correct service boundaries based on domain semantics",
                    "The number of containers needed per service",
                    "The database schema for the entire system",
                ],
                "answer": "b",
                "lesson": (
                    "A bounded context is a DDD concept that defines the boundary around\n"
                    "a domain model where terms have specific meaning.\n\n"
                    "Example: 'Customer' in the Billing context has payment methods and invoices.\n"
                    "'Customer' in the Shipping context has addresses and delivery preferences.\n"
                    "Same word, different models. Different bounded contexts.\n\n"
                    "Each bounded context maps naturally to a microservice boundary.\n"
                    "Services that share a bounded context should probably be one service."
                ),
                "xp": 25,
                "hints": [
                    "It's about where a domain model's meaning is consistent and unambiguous.",
                    "Think of it as the semantic boundary — where the same word means the same thing.",
                ],
            },
            {
                "id": "mf_3",
                "type": "text",
                "question": (
                    "You are decomposing a monolith into microservices. Each service should\n"
                    "own its own data and be deployable independently.\n\n"
                    "What is the name of the principle that states each microservice should\n"
                    "have its own private database (two words, no abbreviations)?"
                ),
                "options": [],
                "answer": "database per service",
                "lesson": (
                    "Database Per Service is a core microservices principle.\n\n"
                    "Each service owns its data store. No other service can access it directly.\n"
                    "Communication happens only through the service's API.\n\n"
                    "Benefits:\n"
                    "  - Services can choose the best storage engine for their data\n"
                    "  - Schema changes don't break other services\n"
                    "  - Services can scale their storage independently\n\n"
                    "The tradeoff: cross-service queries become harder. You can't just\n"
                    "JOIN across service boundaries. You need patterns like API composition\n"
                    "or CQRS to assemble data from multiple services."
                ),
                "xp": 30,
                "hints": [
                    "Each service gets its own private storage — no shared databases.",
                    "The pattern name literally describes what each service has: its own ___.",
                ],
            },
            {
                "id": "mf_4",
                "type": "quiz",
                "title": "Strangler Fig Pattern",
                "question": (
                    "Your team wants to migrate from a monolith to microservices incrementally,\n"
                    "without a risky big-bang rewrite.\n\n"
                    "Which migration pattern routes traffic to new services while gradually\n"
                    "retiring monolith functionality?"
                ),
                "options": [
                    "Strangler Fig pattern",
                    "Sidecar pattern",
                    "Ambassador pattern",
                    "Bulkhead pattern",
                ],
                "answer": "a",
                "lesson": (
                    "The Strangler Fig pattern (named after the strangler fig tree that\n"
                    "grows around and eventually replaces its host) enables incremental\n"
                    "migration from monolith to microservices.\n\n"
                    "How it works:\n"
                    "  1. Place a routing layer (facade) in front of the monolith\n"
                    "  2. Extract one feature into a new microservice\n"
                    "  3. Route traffic for that feature to the new service\n"
                    "  4. Repeat until the monolith is empty\n\n"
                    "The monolith and microservices coexist during migration.\n"
                    "No big-bang cutover. No rewrite risk."
                ),
                "xp": 25,
                "hints": [
                    "Named after a plant that gradually wraps around and replaces its host.",
                    "A facade intercepts requests and routes them to old or new implementations.",
                ],
            },
            {
                "id": "mf_5",
                "type": "quiz",
                "title": "Single Responsibility",
                "question": (
                    "A microservice handles user authentication, sends welcome emails,\n"
                    "generates PDF invoices, and manages subscription billing.\n\n"
                    "What design principle is this service violating?"
                ),
                "options": [
                    "Interface Segregation Principle",
                    "Single Responsibility Principle",
                    "Open/Closed Principle",
                    "Dependency Inversion Principle",
                ],
                "answer": "b",
                "lesson": (
                    "The Single Responsibility Principle applied to microservices:\n"
                    "each service should do one thing well.\n\n"
                    "A service that handles auth, emails, PDFs, and billing has four\n"
                    "reasons to change. A bug in PDF generation requires redeploying\n"
                    "the auth system. Scaling email sending means scaling billing too.\n\n"
                    "Better: auth-service, notification-service, invoice-service,\n"
                    "billing-service. Each owns its domain, scales independently,\n"
                    "and deploys without affecting the others."
                ),
                "xp": 25,
                "hints": [
                    "This service has multiple reasons to change — that's the violation.",
                    "Each microservice should have exactly one reason to be redeployed.",
                ],
            },
            {
                "id": "mf_6",
                "type": "text",
                "question": (
                    "In microservices architecture, what term describes the combination\n"
                    "of a service's public API contract plus its observable behavior that\n"
                    "other services depend on?\n\n"
                    "Hint: changing this without coordination can break consumers.\n"
                    "(Two words)"
                ),
                "options": [],
                "answer": "service contract",
                "lesson": (
                    "A service contract is the published interface that consumers depend on.\n\n"
                    "It includes:\n"
                    "  - API endpoints, request/response schemas\n"
                    "  - Event formats published to message brokers\n"
                    "  - SLAs (latency, availability, throughput)\n"
                    "  - Error codes and their meanings\n\n"
                    "Backward-compatible changes (adding fields) are safe.\n"
                    "Breaking changes (removing fields, changing types) require versioning\n"
                    "and consumer coordination. This is why contract testing exists."
                ),
                "xp": 30,
                "hints": [
                    "It's the agreement between producer and consumer about how they interact.",
                    "Think of it as a formal promise about the service's interface.",
                ],
            },
            {
                "id": "mf_7",
                "type": "quiz",
                "title": "Deployment Independence",
                "question": (
                    "A core benefit of microservices is independent deployability.\n\n"
                    "Which practice most directly enables teams to deploy services\n"
                    "independently without breaking consumers?"
                ),
                "options": [
                    "Using the same programming language for all services",
                    "Backward-compatible API versioning",
                    "Sharing a database across services",
                    "Deploying all services at the same time",
                ],
                "answer": "b",
                "lesson": (
                    "Independent deployability requires backward-compatible changes.\n\n"
                    "If service A adds a new field to its response, service B (the consumer)\n"
                    "should keep working — it just ignores the new field.\n"
                    "If service A removes a field, service B breaks.\n\n"
                    "Strategies:\n"
                    "  - Additive changes only (never remove, only deprecate)\n"
                    "  - URL versioning: /v1/users, /v2/users\n"
                    "  - Header versioning: Accept: application/vnd.api+json;version=2\n"
                    "  - Consumer-driven contract tests to catch breaking changes"
                ),
                "xp": 25,
                "hints": [
                    "Deploying independently means your changes can't break other services.",
                    "The key is making sure your interface changes are additive, not destructive.",
                ],
            },
            {
                "id": "mf_8",
                "type": "quiz",
                "title": "Anti-Pattern: Distributed Monolith",
                "question": (
                    "A team split their monolith into 12 services, but every change requires\n"
                    "coordinated deployment of multiple services. Teams can't release independently.\n"
                    "Services share a single database.\n\n"
                    "What anti-pattern is this?"
                ),
                "options": [
                    "Service mesh sprawl",
                    "Distributed monolith",
                    "Nano-service fragmentation",
                    "Event storm",
                ],
                "answer": "b",
                "lesson": (
                    "A distributed monolith has all the complexity of microservices\n"
                    "with none of the benefits.\n\n"
                    "Symptoms:\n"
                    "  - Coordinated deployments required across services\n"
                    "  - Shared database with cross-service table access\n"
                    "  - Tight temporal coupling (service A must call B before C)\n"
                    "  - Changes in one service require changes in several others\n\n"
                    "You've added network latency, serialization overhead, and operational\n"
                    "complexity — but you haven't gained independent deployability or\n"
                    "fault isolation. Worse than a well-designed monolith."
                ),
                "xp": 30,
                "hints": [
                    "It looks like microservices but behaves like a monolith over the network.",
                    "The key symptom: you can't deploy one service without deploying others.",
                ],
            },
        ],
    },

    # ── ZONE 2: COMMUNICATION PATTERNS ────────────────────────────────
    "communication_patterns": {
        "id": "communication_patterns",
        "name": "The Signal Grid",
        "subtitle": "Sync vs Async, REST, gRPC, Message Queues & Event-Driven Architecture",
        "color": "green",
        "icon": "\u21c4",
        "commands": ["REQUEST", "PUBLISH", "SUBSCRIBE", "STREAM", "INVOKE"],
        "challenges": [
            {
                "id": "cp_1",
                "type": "quiz",
                "title": "Synchronous vs Asynchronous",
                "question": (
                    "Service A calls Service B over HTTP and blocks until it receives a response.\n"
                    "Service A cannot continue processing until Service B replies.\n\n"
                    "What type of communication is this?"
                ),
                "options": [
                    "Asynchronous messaging",
                    "Event-driven communication",
                    "Synchronous request-response",
                    "Publish-subscribe",
                ],
                "answer": "c",
                "lesson": (
                    "Synchronous communication: the caller blocks and waits for a response.\n\n"
                    "  Sync: Service A → HTTP request → Service B → response → A continues\n"
                    "  Async: Service A → message to queue → A continues immediately\n\n"
                    "Synchronous is simpler to implement but creates temporal coupling.\n"
                    "If Service B is slow or down, Service A is also blocked or failing.\n\n"
                    "Use sync when you need an immediate response (e.g., user-facing reads).\n"
                    "Use async when you can tolerate eventual processing (e.g., sending emails)."
                ),
                "xp": 25,
                "hints": [
                    "The caller waits — it's blocked until the response arrives.",
                    "HTTP request-response where the client hangs until the server replies.",
                ],
            },
            {
                "id": "cp_2",
                "type": "quiz",
                "title": "gRPC vs REST",
                "question": (
                    "Your team needs high-performance, low-latency communication between\n"
                    "internal microservices. The services exchange structured data with\n"
                    "strict schemas, and you want bidirectional streaming.\n\n"
                    "Which protocol is most appropriate?"
                ),
                "options": [
                    "REST over HTTP/1.1 with JSON",
                    "GraphQL with subscriptions",
                    "gRPC with Protocol Buffers",
                    "SOAP with XML",
                ],
                "answer": "c",
                "lesson": (
                    "gRPC is a high-performance RPC framework built on HTTP/2.\n\n"
                    "  - Protocol Buffers (protobuf) for binary serialization (smaller, faster)\n"
                    "  - HTTP/2 multiplexing (multiple requests on one connection)\n"
                    "  - Bidirectional streaming (client and server stream simultaneously)\n"
                    "  - Strict schema via .proto files with code generation\n\n"
                    "REST with JSON is better for:\n"
                    "  - Public APIs (human-readable, browser-friendly)\n"
                    "  - Simple CRUD operations\n"
                    "  - When clients are diverse (mobile, web, third-party)\n\n"
                    "gRPC is better for:\n"
                    "  - Internal service-to-service communication\n"
                    "  - High-throughput, low-latency requirements\n"
                    "  - Streaming use cases"
                ),
                "xp": 25,
                "hints": [
                    "Binary serialization + HTTP/2 + strict schemas + streaming.",
                    "This protocol uses .proto files and is built by Google.",
                ],
            },
            {
                "id": "cp_3",
                "type": "text",
                "question": (
                    "In event-driven architecture, a component publishes events to a broker\n"
                    "and multiple consumers receive those events independently.\n\n"
                    "What is the name of this messaging pattern? (Three words, hyphenated)"
                ),
                "options": [],
                "answer": "publish-subscribe pattern",
                "lesson": (
                    "Publish-Subscribe (pub/sub) decouples producers from consumers.\n\n"
                    "The publisher doesn't know who will consume the event.\n"
                    "The subscriber doesn't know who published it.\n"
                    "The broker (Kafka, RabbitMQ, SNS) handles routing.\n\n"
                    "  Publisher → Topic/Exchange → Subscriber A\n"
                    "                             → Subscriber B\n"
                    "                             → Subscriber C\n\n"
                    "Benefits:\n"
                    "  - Adding new consumers doesn't require changing the publisher\n"
                    "  - Services are decoupled in time and space\n"
                    "  - Natural fit for event-driven microservices"
                ),
                "xp": 30,
                "hints": [
                    "One side publishes, the other side subscribes. The broker is in between.",
                    "Often abbreviated as pub/sub.",
                ],
            },
            {
                "id": "cp_4",
                "type": "quiz",
                "title": "Message Queue Guarantees",
                "question": (
                    "Your order processing system must guarantee that every order event\n"
                    "is processed exactly once, even if the consumer crashes mid-processing.\n\n"
                    "Which delivery guarantee are you aiming for?"
                ),
                "options": [
                    "At-most-once delivery",
                    "At-least-once delivery",
                    "Exactly-once delivery",
                    "Best-effort delivery",
                ],
                "answer": "c",
                "lesson": (
                    "Message delivery guarantees:\n\n"
                    "  At-most-once: fire and forget. Message may be lost. No retries.\n"
                    "  At-least-once: message is retried until acknowledged. May be duplicated.\n"
                    "  Exactly-once: message is processed once and only once.\n\n"
                    "Exactly-once is the hardest to achieve. In practice, most systems\n"
                    "implement at-least-once delivery with idempotent consumers.\n\n"
                    "Kafka achieves effectively-exactly-once with idempotent producers,\n"
                    "transactional writes, and consumer offset management. But true\n"
                    "exactly-once across distributed systems remains notoriously difficult."
                ),
                "xp": 25,
                "hints": [
                    "Not 'at least once' (that allows duplicates). Not 'at most once' (that allows loss).",
                    "The strictest guarantee — processed once, no duplicates, no loss.",
                ],
            },
            {
                "id": "cp_5",
                "type": "quiz",
                "title": "API Gateway Pattern",
                "question": (
                    "Your microservices architecture has 20 services. Mobile clients need\n"
                    "to call multiple services to render a single screen. Each service has\n"
                    "its own authentication mechanism.\n\n"
                    "What pattern provides a single entry point that handles routing,\n"
                    "authentication, and request aggregation?"
                ),
                "options": [
                    "Service mesh",
                    "API Gateway",
                    "Load balancer",
                    "Reverse proxy",
                ],
                "answer": "b",
                "lesson": (
                    "An API Gateway is the single entry point for all client requests.\n\n"
                    "Responsibilities:\n"
                    "  - Request routing to the correct microservice\n"
                    "  - Authentication and authorization (centralized)\n"
                    "  - Rate limiting and throttling\n"
                    "  - Request aggregation (combine multiple service calls)\n"
                    "  - Protocol translation (REST to gRPC, etc.)\n"
                    "  - Response caching\n\n"
                    "Examples: Kong, AWS API Gateway, Netflix Zuul, Envoy.\n\n"
                    "Without a gateway, clients must know the address of every service,\n"
                    "handle authentication per service, and make N calls for N services."
                ),
                "xp": 25,
                "hints": [
                    "A single front door that routes, authenticates, and aggregates.",
                    "Think of it as the receptionist for your entire microservices system.",
                ],
            },
            {
                "id": "cp_6",
                "type": "text",
                "question": (
                    "When Service A calls Service B, and Service B calls Service C,\n"
                    "and Service C calls Service D — all synchronously — what is this\n"
                    "communication anti-pattern called?\n\n"
                    "Hint: it creates deep dependency chains with compounding latency.\n"
                    "(Two words)"
                ),
                "options": [],
                "answer": "service chaining",
                "lesson": (
                    "Service chaining creates deep synchronous dependency chains.\n\n"
                    "  A → B → C → D\n\n"
                    "Problems:\n"
                    "  - Latency compounds: total latency = A + B + C + D\n"
                    "  - Availability compounds: if any service is down, the chain breaks\n"
                    "  - Availability = 99.9% ^ 4 = 99.6% (four nines becomes less than three)\n"
                    "  - Debugging is hard: which service in the chain is slow?\n\n"
                    "Mitigation:\n"
                    "  - Use async messaging to break the chain\n"
                    "  - Use event-driven patterns instead of synchronous calls\n"
                    "  - Aggregate data via an API Gateway or BFF pattern"
                ),
                "xp": 30,
                "hints": [
                    "A calls B calls C calls D — each one waits for the next.",
                    "The requests form a chain of synchronous dependencies.",
                ],
            },
            {
                "id": "cp_7",
                "type": "quiz",
                "title": "Backend for Frontend",
                "question": (
                    "Your mobile app needs a minimal response with 3 fields.\n"
                    "Your web app needs a rich response with 20 fields.\n"
                    "Both call the same backend services.\n\n"
                    "What pattern creates dedicated backend services tailored to each frontend?"
                ),
                "options": [
                    "Backend for Frontend (BFF)",
                    "Adapter pattern",
                    "Facade pattern",
                    "Proxy pattern",
                ],
                "answer": "a",
                "lesson": (
                    "Backend for Frontend (BFF) creates a separate backend per client type.\n\n"
                    "  Mobile App → Mobile BFF → microservices\n"
                    "  Web App    → Web BFF    → microservices\n"
                    "  Admin UI   → Admin BFF  → microservices\n\n"
                    "Each BFF is optimized for its client:\n"
                    "  - Mobile BFF returns minimal payloads (bandwidth matters)\n"
                    "  - Web BFF returns rich payloads (bandwidth is cheaper)\n"
                    "  - Admin BFF includes extra fields and actions\n\n"
                    "Without BFF, you end up with one API that serves all clients poorly —\n"
                    "over-fetching for mobile, under-fetching for web."
                ),
                "xp": 25,
                "hints": [
                    "Each frontend gets its own dedicated backend layer.",
                    "The pattern name literally describes what it is: a backend for each frontend.",
                ],
            },
            {
                "id": "cp_8",
                "type": "quiz",
                "title": "Idempotency in Messaging",
                "question": (
                    "Your payment service processes messages from a queue. Due to network\n"
                    "issues, the same 'charge customer' message is delivered twice.\n\n"
                    "What property must the payment service have to avoid double-charging?"
                ),
                "options": [
                    "Atomicity",
                    "Idempotency",
                    "Consistency",
                    "Durability",
                ],
                "answer": "b",
                "lesson": (
                    "An idempotent operation produces the same result whether called\n"
                    "once or multiple times.\n\n"
                    "For payment processing:\n"
                    "  - Store a unique idempotency key (e.g., order ID) with each charge\n"
                    "  - Before processing, check if that key was already processed\n"
                    "  - If yes, return the cached result. If no, process and store.\n\n"
                    "This is critical in distributed systems where at-least-once delivery\n"
                    "means messages can be duplicated. The consumer must handle duplicates\n"
                    "gracefully. Design every message handler to be idempotent."
                ),
                "xp": 30,
                "hints": [
                    "Processing the same message twice should produce the same outcome.",
                    "The operation's result doesn't change no matter how many times it runs.",
                ],
            },
        ],
    },

    # ── ZONE 3: SERVICE DISCOVERY & LOAD BALANCING ────────────────────
    "service_discovery": {
        "id": "service_discovery",
        "name": "The Registry Nexus",
        "subtitle": "Service Discovery, Load Balancing, Consul, Envoy & Circuit Breakers",
        "color": "yellow",
        "icon": "\U0001f50d",
        "commands": ["DISCOVER", "REGISTER", "ROUTE", "BALANCE", "BREAK"],
        "challenges": [
            {
                "id": "sd_1",
                "type": "quiz",
                "title": "Service Discovery",
                "question": (
                    "In a microservices environment, services scale up and down dynamically.\n"
                    "IP addresses change with each deployment.\n\n"
                    "What mechanism allows services to find each other without hardcoded addresses?"
                ),
                "options": [
                    "DNS round-robin only",
                    "Service discovery",
                    "Static configuration files",
                    "Manual IP assignment",
                ],
                "answer": "b",
                "lesson": (
                    "Service discovery provides dynamic name resolution for microservices.\n\n"
                    "Two patterns:\n"
                    "  Client-side discovery: the client queries a registry and chooses an instance\n"
                    "    Client → Registry → [instance1, instance2, instance3] → Client picks one\n\n"
                    "  Server-side discovery: a load balancer queries the registry on behalf of the client\n"
                    "    Client → Load Balancer → Registry → route to instance\n\n"
                    "Tools: Consul, etcd, Eureka, Kubernetes DNS.\n\n"
                    "Without service discovery, you're maintaining a spreadsheet of IP addresses\n"
                    "that becomes stale with every deployment."
                ),
                "xp": 25,
                "hints": [
                    "Services register themselves; other services look them up by name.",
                    "It's like a phone book for microservices — names to addresses.",
                ],
            },
            {
                "id": "sd_2",
                "type": "text",
                "question": (
                    "HashiCorp's service discovery tool provides a distributed service mesh\n"
                    "with health checking, KV store, and service registration.\n\n"
                    "What is the name of this tool? (One word)"
                ),
                "options": [],
                "answer": "Consul",
                "lesson": (
                    "Consul is a service mesh and service discovery tool by HashiCorp.\n\n"
                    "Features:\n"
                    "  - Service registration and discovery via DNS or HTTP API\n"
                    "  - Health checking (HTTP, TCP, gRPC, script-based)\n"
                    "  - Key-value store for configuration\n"
                    "  - Service mesh with mTLS and traffic management\n"
                    "  - Multi-datacenter support\n\n"
                    "Services register with a local Consul agent. Other services query\n"
                    "Consul to find healthy instances. Failed health checks automatically\n"
                    "remove unhealthy instances from the registry."
                ),
                "xp": 30,
                "hints": [
                    "Made by the same company that makes Terraform and Vault.",
                    "It starts with 'C' and rhymes with 'consul' (because it is).",
                ],
            },
            {
                "id": "sd_3",
                "type": "quiz",
                "title": "Circuit Breaker Pattern",
                "question": (
                    "Service A calls Service B. Service B starts timing out, causing\n"
                    "Service A's thread pool to fill up with blocked threads.\n"
                    "Service A is now also failing.\n\n"
                    "What pattern prevents this cascading failure?"
                ),
                "options": [
                    "Retry pattern",
                    "Circuit breaker pattern",
                    "Throttling pattern",
                    "Queue-based load leveling",
                ],
                "answer": "b",
                "lesson": (
                    "The circuit breaker pattern prevents cascading failures.\n\n"
                    "Three states:\n"
                    "  CLOSED:    requests flow normally. Failures are counted.\n"
                    "  OPEN:      failures exceeded threshold. Requests fail immediately\n"
                    "             (no waiting for timeout). Fast failure.\n"
                    "  HALF-OPEN: after a cooldown, allow one test request.\n"
                    "             If it succeeds, close the circuit. If it fails, reopen.\n\n"
                    "Libraries: Hystrix (Netflix, deprecated), Resilience4j, Polly (.NET).\n"
                    "Service meshes like Istio/Envoy implement circuit breaking at the\n"
                    "infrastructure level — no code changes needed."
                ),
                "xp": 25,
                "hints": [
                    "Named after the electrical component that trips when current is too high.",
                    "It has three states: closed, open, and half-open.",
                ],
            },
            {
                "id": "sd_4",
                "type": "quiz",
                "title": "Load Balancing Algorithms",
                "question": (
                    "You have 3 service instances with different CPU capacities.\n"
                    "Instance A has 4 cores, B has 2 cores, C has 1 core.\n\n"
                    "Which load balancing algorithm distributes requests proportionally\n"
                    "to each instance's capacity?"
                ),
                "options": [
                    "Round-robin",
                    "Random",
                    "Weighted round-robin",
                    "Least connections",
                ],
                "answer": "c",
                "lesson": (
                    "Load balancing algorithms:\n\n"
                    "  Round-robin: rotate through instances equally (1, 2, 3, 1, 2, 3...)\n"
                    "  Weighted round-robin: rotate proportionally (4 to A, 2 to B, 1 to C)\n"
                    "  Least connections: send to the instance with fewest active requests\n"
                    "  Random: pick any instance randomly\n"
                    "  IP hash: same client IP always goes to the same instance (sticky sessions)\n\n"
                    "Weighted round-robin is ideal when instances have different capacities.\n"
                    "Least connections adapts to real-time load differences.\n"
                    "Round-robin assumes all instances are equal."
                ),
                "xp": 25,
                "hints": [
                    "Standard round-robin treats all instances equally. You need proportional distribution.",
                    "The answer adds a weighting factor to the basic rotation algorithm.",
                ],
            },
            {
                "id": "sd_5",
                "type": "text",
                "question": (
                    "Originally built at Lyft, this high-performance L4/L7 proxy is widely\n"
                    "used as a sidecar proxy in service meshes like Istio.\n\n"
                    "What is the name of this proxy? (One word)"
                ),
                "options": [],
                "answer": "Envoy",
                "lesson": (
                    "Envoy is a high-performance edge and service proxy.\n\n"
                    "Key capabilities:\n"
                    "  - L4 (TCP) and L7 (HTTP, gRPC) load balancing\n"
                    "  - Automatic retries, circuit breaking, rate limiting\n"
                    "  - Observability: distributed tracing, metrics, access logging\n"
                    "  - mTLS for service-to-service encryption\n"
                    "  - Hot restart with zero downtime\n\n"
                    "In Istio, Envoy runs as a sidecar next to every service instance.\n"
                    "All traffic flows through Envoy, which enforces policies, collects\n"
                    "metrics, and manages mTLS — without changing application code."
                ),
                "xp": 30,
                "hints": [
                    "Built at Lyft, now a CNCF graduated project. Used as Istio's data plane.",
                    "Named after a diplomatic messenger. Starts with 'E'.",
                ],
            },
            {
                "id": "sd_6",
                "type": "quiz",
                "title": "Health Checks",
                "question": (
                    "Your service discovery system needs to know if a service instance\n"
                    "is healthy before routing traffic to it.\n\n"
                    "Which health check type verifies that the application can actually\n"
                    "process requests, not just that the process is running?"
                ),
                "options": [
                    "TCP port check",
                    "Process ID check",
                    "HTTP readiness probe",
                    "Disk space check",
                ],
                "answer": "c",
                "lesson": (
                    "Health check types:\n\n"
                    "  Liveness probe: is the process alive? (restart if not)\n"
                    "  Readiness probe: can it handle requests? (remove from LB if not)\n"
                    "  Startup probe: has it finished initializing? (don't check liveness yet)\n\n"
                    "A readiness probe hits an HTTP endpoint (e.g., GET /health/ready)\n"
                    "that verifies database connectivity, cache availability, and\n"
                    "dependency health. A process can be alive but not ready.\n\n"
                    "Example: service is running but its database connection pool is exhausted.\n"
                    "Liveness passes (process is alive). Readiness fails (can't serve requests).\n"
                    "Traffic is routed to other healthy instances."
                ),
                "xp": 25,
                "hints": [
                    "Just checking that a port is open doesn't mean the app can process work.",
                    "This probe checks if the service is ready to receive traffic.",
                ],
            },
            {
                "id": "sd_7",
                "type": "quiz",
                "title": "Service Mesh",
                "question": (
                    "Your team wants to add mTLS, traffic management, and observability\n"
                    "to all inter-service communication without changing application code.\n\n"
                    "What infrastructure layer provides these capabilities?"
                ),
                "options": [
                    "API Gateway",
                    "Service mesh",
                    "Container orchestrator",
                    "Message broker",
                ],
                "answer": "b",
                "lesson": (
                    "A service mesh is a dedicated infrastructure layer for service-to-service\n"
                    "communication.\n\n"
                    "Architecture:\n"
                    "  Data plane: sidecar proxies (Envoy) handle all traffic\n"
                    "  Control plane: manages configuration, policies, certificates\n\n"
                    "Capabilities:\n"
                    "  - mTLS encryption between all services (zero-trust)\n"
                    "  - Traffic management (canary deploys, A/B testing, retries)\n"
                    "  - Observability (distributed tracing, metrics, access logs)\n"
                    "  - Circuit breaking and fault injection\n\n"
                    "Examples: Istio, Linkerd, Consul Connect.\n"
                    "The application code doesn't change — the mesh handles it at the proxy level."
                ),
                "xp": 25,
                "hints": [
                    "It's an infrastructure layer with sidecar proxies, not an application-level tool.",
                    "Istio and Linkerd are the two most well-known implementations.",
                ],
            },
            {
                "id": "sd_8",
                "type": "quiz",
                "title": "Retry with Exponential Backoff",
                "question": (
                    "Service A's request to Service B fails. You want to retry, but\n"
                    "retrying immediately at full rate could overwhelm Service B.\n\n"
                    "What retry strategy progressively increases the wait time between attempts?"
                ),
                "options": [
                    "Immediate retry with fixed interval",
                    "Retry with exponential backoff and jitter",
                    "Retry once and fail",
                    "Retry indefinitely with no delay",
                ],
                "answer": "b",
                "lesson": (
                    "Exponential backoff increases wait time exponentially between retries.\n\n"
                    "  Attempt 1: wait 100ms\n"
                    "  Attempt 2: wait 200ms\n"
                    "  Attempt 3: wait 400ms\n"
                    "  Attempt 4: wait 800ms\n\n"
                    "Jitter adds randomness to avoid thundering herd:\n"
                    "  wait = min(base * 2^attempt + random(0, base), max_wait)\n\n"
                    "Without jitter, all clients retry at the same time (synchronized retries),\n"
                    "creating a traffic spike that can cause the next failure.\n\n"
                    "Always set a max retry count and max wait time.\n"
                    "Combine with circuit breakers for comprehensive resilience."
                ),
                "xp": 30,
                "hints": [
                    "Each retry waits longer than the last: 1s, 2s, 4s, 8s...",
                    "Adding randomness prevents all clients from retrying at the same instant.",
                ],
            },
        ],
    },

    # ── ZONE 4: DATA MANAGEMENT ───────────────────────────────────────
    "data_management": {
        "id": "data_management",
        "name": "The Consistency Engine",
        "subtitle": "Saga Pattern, CQRS, Event Sourcing & Eventual Consistency",
        "color": "magenta",
        "icon": "\U0001f5c4",
        "commands": ["SAGA", "PROJECT", "SOURCE", "COMPENSATE", "REPLAY"],
        "challenges": [
            {
                "id": "dm_1",
                "type": "quiz",
                "title": "The Saga Pattern",
                "question": (
                    "An e-commerce order involves three services: Order, Payment, and Inventory.\n"
                    "You can't use a distributed transaction (2PC) because the services\n"
                    "have independent databases.\n\n"
                    "What pattern manages this distributed business transaction?"
                ),
                "options": [
                    "Two-phase commit",
                    "Saga pattern",
                    "Outbox pattern",
                    "Change data capture",
                ],
                "answer": "b",
                "lesson": (
                    "The Saga pattern manages distributed transactions as a sequence\n"
                    "of local transactions.\n\n"
                    "Each service performs its local transaction and publishes an event.\n"
                    "The next service listens and performs its transaction.\n"
                    "If any step fails, compensating transactions undo previous steps.\n\n"
                    "  1. Order Service: create order → publish OrderCreated\n"
                    "  2. Payment Service: charge card → publish PaymentProcessed\n"
                    "  3. Inventory Service: reserve stock → publish StockReserved\n\n"
                    "If Payment fails:\n"
                    "  → Payment publishes PaymentFailed\n"
                    "  → Order Service runs compensating transaction: cancel order\n\n"
                    "Two saga types: choreography (events) and orchestration (coordinator)."
                ),
                "xp": 25,
                "hints": [
                    "A sequence of local transactions with compensating actions on failure.",
                    "Named after the Norse literary form — a long story told in episodes.",
                ],
            },
            {
                "id": "dm_2",
                "type": "quiz",
                "title": "Choreography vs Orchestration",
                "question": (
                    "In a saga, you need to decide how services coordinate.\n\n"
                    "In the choreography approach, how do services know what to do next?"
                ),
                "options": [
                    "A central coordinator tells each service what to do",
                    "Each service listens for events and reacts independently",
                    "Services poll a shared database for the next step",
                    "A workflow engine schedules each service call",
                ],
                "answer": "b",
                "lesson": (
                    "Saga coordination styles:\n\n"
                    "  Choreography: each service listens for events and decides its own action.\n"
                    "    Order → event → Payment → event → Inventory\n"
                    "    No central coordinator. Services are decoupled.\n"
                    "    Good for simple sagas (3-4 steps).\n"
                    "    Harder to understand as the saga grows.\n\n"
                    "  Orchestration: a central coordinator tells each service what to do.\n"
                    "    Coordinator → Order → Coordinator → Payment → Coordinator → Inventory\n"
                    "    Single point of control. Easier to understand and debug.\n"
                    "    Good for complex sagas with many steps and branches.\n"
                    "    Risk: the orchestrator can become a bottleneck."
                ),
                "xp": 25,
                "hints": [
                    "No conductor — each musician watches the others and plays their part.",
                    "Think of a dance where everyone reacts to each other's movements.",
                ],
            },
            {
                "id": "dm_3",
                "type": "text",
                "question": (
                    "A pattern that separates the read model from the write model,\n"
                    "allowing you to optimize each independently. Writes go to one store,\n"
                    "reads come from a denormalized projection.\n\n"
                    "What is this pattern called? (Acronym, 4 letters)"
                ),
                "options": [],
                "answer": "CQRS",
                "lesson": (
                    "CQRS = Command Query Responsibility Segregation.\n\n"
                    "  Commands (writes) → Write Model → normalized, optimized for consistency\n"
                    "  Queries (reads)   → Read Model  → denormalized, optimized for queries\n\n"
                    "The read model is a projection — a pre-computed view of the data\n"
                    "optimized for specific query patterns.\n\n"
                    "Benefits:\n"
                    "  - Scale reads and writes independently\n"
                    "  - Optimize each model for its purpose\n"
                    "  - Read model can be in a different database (Elasticsearch, Redis)\n\n"
                    "Tradeoff: eventual consistency between write and read models.\n"
                    "The read model is updated asynchronously after writes."
                ),
                "xp": 30,
                "hints": [
                    "Separate the C (commands/writes) from the Q (queries/reads).",
                    "Four letters. The RS stands for Responsibility Segregation.",
                ],
            },
            {
                "id": "dm_4",
                "type": "quiz",
                "title": "Event Sourcing",
                "question": (
                    "Instead of storing the current state of an entity, you store\n"
                    "every state change as an immutable event.\n\n"
                    "What is the primary benefit of event sourcing?"
                ),
                "options": [
                    "Simpler database schema",
                    "Complete audit trail and ability to rebuild state at any point in time",
                    "Faster write performance than traditional CRUD",
                    "Eliminates the need for a database",
                ],
                "answer": "b",
                "lesson": (
                    "Event sourcing stores state as a sequence of immutable events.\n\n"
                    "Traditional CRUD:  UPDATE account SET balance = 80 WHERE id = 1\n"
                    "Event sourcing:    AccountCreated(balance=100)\n"
                    "                   MoneyWithdrawn(amount=20)\n"
                    "                   → current state: balance = 80\n\n"
                    "Benefits:\n"
                    "  - Complete audit trail (every change is recorded)\n"
                    "  - Temporal queries (what was the state at 3pm yesterday?)\n"
                    "  - Rebuild state by replaying events\n"
                    "  - Debug by replaying the exact sequence of events\n\n"
                    "Tradeoffs:\n"
                    "  - Event store grows indefinitely (need snapshotting)\n"
                    "  - Querying current state requires replaying or using projections\n"
                    "  - Event schema evolution is complex"
                ),
                "xp": 25,
                "hints": [
                    "You never lose information — every change is an immutable fact.",
                    "You can 'time travel' by replaying events up to any point.",
                ],
            },
            {
                "id": "dm_5",
                "type": "quiz",
                "title": "Eventual Consistency",
                "question": (
                    "After a write to Service A, Service B's read model takes 200ms\n"
                    "to reflect the change. During that window, reads from B return stale data.\n\n"
                    "What consistency model describes this behavior?"
                ),
                "options": [
                    "Strong consistency",
                    "Linearizability",
                    "Eventual consistency",
                    "Causal consistency",
                ],
                "answer": "c",
                "lesson": (
                    "Eventual consistency: if no new updates are made, all replicas\n"
                    "will eventually converge to the same value.\n\n"
                    "Consistency spectrum:\n"
                    "  Strong:    every read returns the most recent write (expensive)\n"
                    "  Causal:    reads reflect causally related writes in order\n"
                    "  Eventual:  replicas converge given enough time (cheapest)\n\n"
                    "In microservices, eventual consistency is the norm because:\n"
                    "  - Services have separate databases\n"
                    "  - Cross-service updates are asynchronous\n"
                    "  - Strong consistency across services requires distributed locks\n\n"
                    "Design your UI for eventual consistency: show pending states,\n"
                    "optimistic updates, and retry mechanisms."
                ),
                "xp": 25,
                "hints": [
                    "The data will be consistent... eventually, after propagation completes.",
                    "Not strong, not causal — the weakest but most scalable guarantee.",
                ],
            },
            {
                "id": "dm_6",
                "type": "text",
                "question": (
                    "To reliably publish events after a database write (without distributed\n"
                    "transactions), you write the event to a table in the same database\n"
                    "as part of the local transaction. A separate process reads that table\n"
                    "and publishes to the message broker.\n\n"
                    "What is this pattern called? (Two words)"
                ),
                "options": [],
                "answer": "outbox pattern",
                "lesson": (
                    "The Transactional Outbox pattern solves the dual-write problem.\n\n"
                    "The problem: you need to update a database AND publish an event.\n"
                    "If you do them separately, one might succeed and the other fail.\n\n"
                    "The solution:\n"
                    "  1. In the same database transaction:\n"
                    "     - Update the business table\n"
                    "     - Insert an event record into the 'outbox' table\n"
                    "  2. A separate process (relay) polls the outbox table\n"
                    "  3. The relay publishes each event to the message broker\n"
                    "  4. The relay marks the event as published\n\n"
                    "The local transaction guarantees atomicity.\n"
                    "The relay guarantees eventual delivery to the broker."
                ),
                "xp": 30,
                "hints": [
                    "Write the event to a table in the same transaction as the business data.",
                    "The table acts as a mailbox that a relay process picks up from.",
                ],
            },
            {
                "id": "dm_7",
                "type": "quiz",
                "title": "CAP Theorem",
                "question": (
                    "The CAP theorem states that a distributed system can provide at most\n"
                    "two of three guarantees simultaneously.\n\n"
                    "What are the three guarantees?"
                ),
                "options": [
                    "Consistency, Availability, Partition tolerance",
                    "Concurrency, Atomicity, Performance",
                    "Caching, Authentication, Persistence",
                    "Compression, Availability, Parallelism",
                ],
                "answer": "a",
                "lesson": (
                    "CAP Theorem (Brewer's Theorem):\n\n"
                    "  C - Consistency: every read returns the most recent write\n"
                    "  A - Availability: every request gets a response (no timeouts)\n"
                    "  P - Partition tolerance: system works despite network splits\n\n"
                    "In a distributed system, network partitions are inevitable.\n"
                    "So the real choice is: during a partition, do you choose\n"
                    "Consistency (reject requests) or Availability (serve stale data)?\n\n"
                    "  CP systems: MongoDB, HBase, Redis (single master)\n"
                    "  AP systems: Cassandra, DynamoDB, CouchDB\n\n"
                    "Most microservices architectures choose AP with eventual consistency."
                ),
                "xp": 25,
                "hints": [
                    "Three letters: C, A, P. One is about data freshness, one about uptime.",
                    "Network partitions will happen. The question is what you sacrifice.",
                ],
            },
            {
                "id": "dm_8",
                "type": "quiz",
                "title": "Change Data Capture",
                "question": (
                    "You need to synchronize data between the Order service's PostgreSQL\n"
                    "database and the Search service's Elasticsearch index in real-time.\n\n"
                    "What technique captures database changes from the write-ahead log\n"
                    "and streams them to other systems?"
                ),
                "options": [
                    "Database triggers",
                    "Polling with timestamps",
                    "Change Data Capture (CDC)",
                    "Dual writes",
                ],
                "answer": "c",
                "lesson": (
                    "Change Data Capture (CDC) reads the database's transaction log\n"
                    "and streams changes to downstream systems.\n\n"
                    "  PostgreSQL WAL → Debezium → Kafka → Elasticsearch\n\n"
                    "Benefits over alternatives:\n"
                    "  - No application code changes (reads the log, not the app)\n"
                    "  - Captures all changes including direct SQL modifications\n"
                    "  - Low overhead (reads the log the DB already writes)\n"
                    "  - Preserves ordering of changes\n\n"
                    "Debezium is the most popular open-source CDC tool.\n"
                    "It supports PostgreSQL, MySQL, MongoDB, SQL Server, and Oracle.\n\n"
                    "CDC is the foundation for keeping read models, caches, and search\n"
                    "indexes synchronized with the source of truth."
                ),
                "xp": 30,
                "hints": [
                    "It reads the database's own transaction log — no application changes needed.",
                    "Debezium is the most well-known open-source tool for this.",
                ],
            },
        ],
    },

    # ── ZONE 5: OBSERVABILITY & RESILIENCE ────────────────────────────
    "observability_resilience": {
        "id": "observability_resilience",
        "name": "The Chaos Forge",
        "subtitle": "Distributed Tracing, Bulkheads, Chaos Engineering & Fault Tolerance",
        "color": "red",
        "icon": "\U0001f525",
        "commands": ["TRACE", "ISOLATE", "INJECT", "MONITOR", "RECOVER"],
        "challenges": [
            {
                "id": "or_1",
                "type": "quiz",
                "title": "Three Pillars of Observability",
                "question": (
                    "Observability in distributed systems rests on three pillars\n"
                    "that together provide full visibility into system behavior.\n\n"
                    "What are the three pillars of observability?"
                ),
                "options": [
                    "Logs, metrics, and traces",
                    "Alerts, dashboards, and reports",
                    "CPU, memory, and disk",
                    "Uptime, latency, and throughput",
                ],
                "answer": "a",
                "lesson": (
                    "The three pillars of observability:\n\n"
                    "  Logs:    discrete events with context (what happened)\n"
                    "           Structured logs (JSON) are searchable and parseable.\n\n"
                    "  Metrics: numeric measurements over time (how much, how fast)\n"
                    "           Counters, gauges, histograms. Prometheus, StatsD.\n\n"
                    "  Traces:  the journey of a request across services (where and how long)\n"
                    "           Each service adds a span. Spans form a trace.\n\n"
                    "Logs tell you what happened. Metrics tell you how the system is performing.\n"
                    "Traces tell you where time is spent across service boundaries.\n"
                    "You need all three to debug distributed systems."
                ),
                "xp": 25,
                "hints": [
                    "Three types of telemetry data: events, numbers over time, and request flows.",
                    "One is about text events, one is about numbers, one is about request paths.",
                ],
            },
            {
                "id": "or_2",
                "type": "text",
                "question": (
                    "In distributed tracing, a request enters the system and receives\n"
                    "a unique identifier that is propagated to every service the request\n"
                    "touches. Each service adds its own segment to the overall trace.\n\n"
                    "What is the name for each service's individual segment within a trace?\n"
                    "(One word)"
                ),
                "options": [],
                "answer": "span",
                "lesson": (
                    "A span represents a single unit of work in a distributed trace.\n\n"
                    "  Trace: the entire journey of a request\n"
                    "  Span:  one service's contribution to that journey\n\n"
                    "  Trace ID: abc123\n"
                    "    ├── Span: API Gateway (12ms)\n"
                    "    ├── Span: Auth Service (5ms)\n"
                    "    ├── Span: Order Service (45ms)\n"
                    "    │   └── Span: Database query (30ms)\n"
                    "    └── Span: Payment Service (120ms)\n\n"
                    "Each span records: service name, operation, start time, duration,\n"
                    "status, and parent span ID (for nesting).\n\n"
                    "Tools: Jaeger, Zipkin, AWS X-Ray, OpenTelemetry."
                ),
                "xp": 30,
                "hints": [
                    "A trace is made up of multiple of these — one per service or operation.",
                    "Rhymes with 'plan'. It spans the duration of one operation.",
                ],
            },
            {
                "id": "or_3",
                "type": "quiz",
                "title": "Bulkhead Pattern",
                "question": (
                    "Service A has one thread pool shared across all downstream calls.\n"
                    "When Service B becomes slow, all threads are consumed waiting for B,\n"
                    "and calls to healthy Service C also fail.\n\n"
                    "What pattern isolates resources so one slow dependency can't exhaust\n"
                    "resources needed by others?"
                ),
                "options": [
                    "Circuit breaker",
                    "Bulkhead pattern",
                    "Timeout pattern",
                    "Retry pattern",
                ],
                "answer": "b",
                "lesson": (
                    "The bulkhead pattern isolates resources into separate pools.\n\n"
                    "Named after ship bulkheads — watertight compartments that prevent\n"
                    "a breach in one section from flooding the entire vessel.\n\n"
                    "  Without bulkheads:\n"
                    "    [Shared thread pool: 100 threads]\n"
                    "    Service B slow → 100 threads blocked → Service C calls fail\n\n"
                    "  With bulkheads:\n"
                    "    [Pool for B: 30 threads] [Pool for C: 30 threads] [Pool for D: 40 threads]\n"
                    "    Service B slow → 30 threads blocked → Service C unaffected\n\n"
                    "Implementation: separate thread pools, connection pools, or\n"
                    "semaphores per downstream dependency."
                ),
                "xp": 25,
                "hints": [
                    "Named after a ship's watertight compartments that contain flooding.",
                    "Isolate resources so one failure domain can't consume everything.",
                ],
            },
            {
                "id": "or_4",
                "type": "quiz",
                "title": "Chaos Engineering",
                "question": (
                    "Your team wants to proactively test system resilience by deliberately\n"
                    "injecting failures in production — killing instances, adding latency,\n"
                    "and partitioning networks.\n\n"
                    "What discipline is this?"
                ),
                "options": [
                    "Penetration testing",
                    "Load testing",
                    "Chaos engineering",
                    "Fuzz testing",
                ],
                "answer": "c",
                "lesson": (
                    "Chaos engineering is the discipline of experimenting on a system\n"
                    "to build confidence in its ability to withstand turbulent conditions.\n\n"
                    "Pioneered by Netflix (Chaos Monkey, Simian Army).\n\n"
                    "Process:\n"
                    "  1. Define steady state (normal system behavior)\n"
                    "  2. Hypothesize that steady state continues during failure\n"
                    "  3. Inject failure (kill instance, add latency, corrupt data)\n"
                    "  4. Observe: did the system maintain steady state?\n"
                    "  5. If not, fix the weakness before it happens in production\n\n"
                    "Tools: Chaos Monkey, Gremlin, Litmus, AWS Fault Injection Simulator.\n\n"
                    "You don't wait for production failures to find weaknesses.\n"
                    "You create controlled failures to find them first."
                ),
                "xp": 25,
                "hints": [
                    "Deliberately breaking things in production to find weaknesses first.",
                    "Netflix pioneered this with a tool named after a primate.",
                ],
            },
            {
                "id": "or_5",
                "type": "text",
                "question": (
                    "Netflix built a tool that randomly terminates virtual machine instances\n"
                    "in production to ensure services can tolerate instance failures.\n\n"
                    "What is this tool called? (Two words)"
                ),
                "options": [],
                "answer": "Chaos Monkey",
                "lesson": (
                    "Chaos Monkey is Netflix's original chaos engineering tool.\n\n"
                    "It randomly kills EC2 instances in production during business hours.\n"
                    "The premise: if your service can't handle a single instance dying,\n"
                    "it will definitely fail during a real outage.\n\n"
                    "Part of the Simian Army:\n"
                    "  - Chaos Monkey: kills instances\n"
                    "  - Latency Monkey: injects artificial delays\n"
                    "  - Chaos Gorilla: kills an entire availability zone\n"
                    "  - Chaos Kong: kills an entire region\n\n"
                    "The result: Netflix services are designed from day one to handle\n"
                    "instance failures gracefully. Redundancy isn't optional."
                ),
                "xp": 30,
                "hints": [
                    "A simian that creates chaos. Built by Netflix.",
                    "Two words: an adjective describing disorder + a primate.",
                ],
            },
            {
                "id": "or_6",
                "type": "quiz",
                "title": "SLOs and Error Budgets",
                "question": (
                    "Your service has a 99.9% availability SLO. In a 30-day month,\n"
                    "that allows approximately 43 minutes of downtime.\n\n"
                    "What is the remaining allowed downtime called in SRE practice?"
                ),
                "options": [
                    "Maintenance window",
                    "Error budget",
                    "Grace period",
                    "Recovery time objective",
                ],
                "answer": "b",
                "lesson": (
                    "An error budget is the allowed amount of unreliability.\n\n"
                    "  SLO: 99.9% availability\n"
                    "  Error budget: 0.1% of total time = ~43 minutes/month\n\n"
                    "If you've used 20 minutes of downtime, you have 23 minutes left.\n"
                    "If the budget is exhausted, freeze feature releases and focus on reliability.\n\n"
                    "Error budgets align development and operations:\n"
                    "  - Dev wants to ship features fast (risk of instability)\n"
                    "  - Ops wants stability (risk of stagnation)\n"
                    "  - Error budget: ship fast while budget remains, stabilize when it's spent\n\n"
                    "This is a core Google SRE concept from the SRE book."
                ),
                "xp": 25,
                "hints": [
                    "It's a budget — an allowance of acceptable unreliability.",
                    "When this is spent, you stop shipping features and fix reliability.",
                ],
            },
            {
                "id": "or_7",
                "type": "quiz",
                "title": "Distributed Tracing Propagation",
                "question": (
                    "For distributed tracing to work across services, the trace context\n"
                    "must be passed from one service to the next.\n\n"
                    "How is trace context typically propagated between services?"
                ),
                "options": [
                    "Stored in a shared database",
                    "Passed via HTTP headers (e.g., traceparent)",
                    "Encoded in the request body",
                    "Broadcast via UDP multicast",
                ],
                "answer": "b",
                "lesson": (
                    "Trace context propagation uses HTTP headers.\n\n"
                    "  W3C Trace Context standard:\n"
                    "    traceparent: 00-<trace-id>-<span-id>-<flags>\n"
                    "    tracestate: vendor-specific data\n\n"
                    "  Older formats:\n"
                    "    X-B3-TraceId (Zipkin B3 format)\n"
                    "    uber-trace-id (Jaeger)\n\n"
                    "Each service:\n"
                    "  1. Reads the trace context from incoming headers\n"
                    "  2. Creates a new span with the trace ID\n"
                    "  3. Adds the trace context to outgoing request headers\n\n"
                    "OpenTelemetry standardizes this across languages and tools.\n"
                    "Without header propagation, you get disconnected spans —\n"
                    "individual service logs with no end-to-end picture."
                ),
                "xp": 25,
                "hints": [
                    "The context rides along with the request, not stored externally.",
                    "HTTP has a standard way to attach metadata to requests.",
                ],
            },
            {
                "id": "or_8",
                "type": "quiz",
                "title": "Graceful Degradation",
                "question": (
                    "Your product page calls a recommendation service for 'You might also like.'\n"
                    "The recommendation service goes down.\n\n"
                    "What resilience strategy shows the product page without recommendations\n"
                    "instead of returning a 500 error?"
                ),
                "options": [
                    "Fail fast",
                    "Graceful degradation",
                    "Automatic failover",
                    "Hot standby",
                ],
                "answer": "b",
                "lesson": (
                    "Graceful degradation: when a non-critical dependency fails,\n"
                    "the system continues with reduced functionality.\n\n"
                    "  Full functionality: Product page + recommendations + reviews + ads\n"
                    "  Degraded: Product page + reviews (recommendations and ads unavailable)\n"
                    "  Core only: Product page with static content\n\n"
                    "Implementation:\n"
                    "  - Identify critical vs non-critical dependencies\n"
                    "  - Wrap non-critical calls in circuit breakers\n"
                    "  - Return cached data or empty defaults on failure\n"
                    "  - Never let a non-critical failure take down the core experience\n\n"
                    "Amazon, Netflix, and Google all practice graceful degradation.\n"
                    "The page loads. It might not have everything. But it loads."
                ),
                "xp": 30,
                "hints": [
                    "The system degrades its functionality gracefully rather than failing completely.",
                    "Show what you can, hide what you can't — don't crash the whole page.",
                ],
            },
        ],
    },
}
