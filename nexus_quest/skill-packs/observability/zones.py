"""
zones.py - All zone and challenge data for Observability skill pack (Signal Corps)
Theme: You can't fix what you can't see. The signals are everywhere — learn to read them.
Challenge types: quiz (multiple choice, a/b/c/d)
"""

ZONE_ORDER = [
    "observability_fundamentals",
    "logging",
    "metrics_and_monitoring",
    "distributed_tracing",
    "alerting",
    "debugging_production",
    "cost_and_scale",
]

ZONES = {
    # ── ZONE 1: OBSERVABILITY FUNDAMENTALS ──────────────────────────────
    "observability_fundamentals": {
        "id": "observability_fundamentals",
        "name": "The Three Pillars",
        "subtitle": "Logs, Metrics, Traces — The Foundation of Signal",
        "color": "cyan",
        "icon": "📡",
        "challenges": [
            {
                "id": "obs_fund_1",
                "type": "quiz",
                "title": "The Three Pillars",
                "question": "What are the three pillars of observability?",
                "lesson": (
                    "The three pillars of observability are logs, metrics, and traces.\n\n"
                    "Logs: timestamped records of discrete events.\n"
                    "Metrics: numeric measurements aggregated over time.\n"
                    "Traces: records of a request's journey through distributed services.\n\n"
                    "Together they give you the ability to ask arbitrary questions\n"
                    "about your system's behavior — not just the questions you\n"
                    "anticipated when you built the dashboards."
                ),
                "options": [
                    "Logs, metrics, and traces",
                    "CPU, memory, and disk",
                    "Alerts, dashboards, and runbooks",
                    "Uptime, latency, and throughput",
                ],
                "answer": "a",
                "hints": [
                    "Think about the three distinct signal types, not the resources they measure.",
                    "One records events, one aggregates numbers, one follows requests.",
                ],
                "xp": 25,
            },
            {
                "id": "obs_fund_2",
                "type": "quiz",
                "title": "Observability vs Monitoring",
                "question": "What is the key difference between observability and monitoring?",
                "lesson": (
                    "Monitoring tells you WHEN something is wrong — predefined checks\n"
                    "against known failure modes. Observability lets you ask WHY.\n\n"
                    "Monitoring: 'Is CPU above 90%? Alert.'\n"
                    "Observability: 'Why did latency spike for users in region X\n"
                    "on requests that hit service Y through path Z?'\n\n"
                    "Monitoring is a subset of observability. You need both, but\n"
                    "observability gives you the power to debug novel failures\n"
                    "you never anticipated."
                ),
                "options": [
                    "Monitoring uses dashboards; observability does not",
                    "Monitoring checks known conditions; observability lets you explore unknown unknowns",
                    "Observability only works in the cloud; monitoring works anywhere",
                    "They are different names for the same practice",
                ],
                "answer": "b",
                "hints": [
                    "Think about what happens when something breaks that you didn't predict.",
                    "One is about known failure modes, the other about asking new questions.",
                ],
                "xp": 25,
            },
            {
                "id": "obs_fund_3",
                "type": "quiz",
                "title": "Structured Data",
                "question": "Why is structured data (e.g., JSON logs, labeled metrics) critical for observability?",
                "lesson": (
                    "Structured data can be parsed, indexed, filtered, and correlated\n"
                    "by machines. Unstructured data requires humans to read it.\n\n"
                    "A plain text log: 'Error: connection refused to db-primary'\n"
                    "A structured log: {\"level\":\"error\",\"service\":\"api\",\"target\":\"db-primary\",\n"
                    "  \"error\":\"connection_refused\",\"latency_ms\":3002}\n\n"
                    "The structured version can be filtered (service=api), aggregated\n"
                    "(count errors per target), and correlated with metrics and traces.\n"
                    "Without structure, you're just reading text files."
                ),
                "options": [
                    "It makes logs smaller and cheaper to store",
                    "It enables machine parsing, filtering, aggregation, and correlation across signals",
                    "It is required by compliance regulations like SOC2",
                    "It only matters for metrics, not for logs or traces",
                ],
                "answer": "b",
                "hints": [
                    "Think about what a computer can do with JSON that it can't do with plain text.",
                    "Filtering, aggregating, correlating — all require structure.",
                ],
                "xp": 25,
            },
            {
                "id": "obs_fund_4",
                "type": "quiz",
                "title": "Signal Cardinality",
                "question": "In observability, what does 'high cardinality' mean?",
                "lesson": (
                    "Cardinality is the number of unique values a field can have.\n\n"
                    "Low cardinality: HTTP method (GET, POST, PUT, DELETE) — ~5 values.\n"
                    "High cardinality: user_id — millions of unique values.\n\n"
                    "High-cardinality dimensions are powerful for debugging (you can\n"
                    "filter to a single user or request), but they explode the number\n"
                    "of metric time series your system stores. A metric with labels\n"
                    "{method, status, user_id} creates a time series for EVERY unique\n"
                    "combination. 5 methods x 10 statuses x 1M users = 50M series.\n\n"
                    "This is the fundamental tension in observability: high cardinality\n"
                    "gives you the best debugging power but the highest cost."
                ),
                "options": [
                    "The system is generating too many alerts",
                    "A field or label has a very large number of unique values",
                    "The data is being sampled at too high a rate",
                    "Logs are being written faster than they can be ingested",
                ],
                "answer": "b",
                "hints": [
                    "Think about unique values — how many distinct entries can a field have?",
                    "user_id is high cardinality. HTTP method is low cardinality.",
                ],
                "xp": 30,
            },
            {
                "id": "obs_fund_5",
                "type": "quiz",
                "title": "Telemetry Pipeline",
                "question": "What is the role of a telemetry pipeline (e.g., OpenTelemetry Collector, Vector, Fluentd)?",
                "lesson": (
                    "A telemetry pipeline sits between your applications and your\n"
                    "observability backends. It receives, processes, and routes signals.\n\n"
                    "Key functions:\n"
                    "  - Collection: gather logs, metrics, traces from many sources\n"
                    "  - Processing: parse, filter, enrich, sample, transform\n"
                    "  - Routing: send different signals to different backends\n\n"
                    "Without a pipeline, every application must know about every\n"
                    "backend. With a pipeline, applications emit signals to one place\n"
                    "and the pipeline decides where they go. This decouples your\n"
                    "application instrumentation from your backend infrastructure."
                ),
                "options": [
                    "It replaces your monitoring dashboards with a single CLI tool",
                    "It collects, processes, and routes telemetry from applications to backends",
                    "It generates synthetic test traffic to validate alerting rules",
                    "It encrypts all observability data for compliance purposes",
                ],
                "answer": "b",
                "hints": [
                    "Think about what sits between your apps and your storage backends.",
                    "Collect, process, route — that's the pipeline's job.",
                ],
                "xp": 30,
            },
            {
                "id": "obs_fund_6",
                "type": "quiz",
                "title": "MELT Signals",
                "question": "Which signal type is best suited for answering 'what is the 99th percentile latency of my API over the last hour'?",
                "lesson": (
                    "Metrics are numeric measurements aggregated over time. They are\n"
                    "the right signal for questions about rates, percentiles, and trends.\n\n"
                    "Logs could answer this, but you'd need to parse timestamps and\n"
                    "latency values from every log line and compute the percentile\n"
                    "yourself. Metrics pre-aggregate this data.\n\n"
                    "Traces could also answer this, but traces are typically sampled\n"
                    "and may not represent the full population accurately for\n"
                    "aggregate statistics.\n\n"
                    "Rule of thumb:\n"
                    "  Metrics → aggregate questions (rates, percentiles, counts)\n"
                    "  Logs → discrete event details (what happened at time T)\n"
                    "  Traces → request flow (which services did request X touch)"
                ),
                "options": [
                    "Logs — they contain the raw request data",
                    "Traces — they record every request's journey",
                    "Metrics — they store pre-aggregated numeric measurements over time",
                    "Alerts — they fire when latency exceeds a threshold",
                ],
                "answer": "c",
                "hints": [
                    "You need aggregated numeric data over a time window.",
                    "Which signal type stores numbers and supports percentile queries natively?",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 2: LOGGING ─────────────────────────────────────────────────
    "logging": {
        "id": "logging",
        "name": "The Log Stream",
        "subtitle": "Structured Logging, Centralization, and Retention",
        "color": "green",
        "icon": "📜",
        "challenges": [
            {
                "id": "log_1",
                "type": "quiz",
                "title": "Structured Logging",
                "question": "What is the primary advantage of structured logging (JSON) over plain text logs?",
                "lesson": (
                    "Structured logs emit key-value pairs (typically JSON) instead of\n"
                    "free-form text. This means machines can parse them without regex.\n\n"
                    "Plain text: '2024-01-15 ERROR Failed to connect to db-primary after 3s'\n"
                    "Structured: {\"ts\":\"2024-01-15T...\",\"level\":\"error\",\n"
                    "  \"msg\":\"connection_failed\",\"target\":\"db-primary\",\"timeout_s\":3}\n\n"
                    "Structured logs enable:\n"
                    "  - Filtering: level=error AND target=db-primary\n"
                    "  - Aggregation: count errors per service per minute\n"
                    "  - Correlation: join with traces via request_id field\n"
                    "  - Alerting: trigger when error count > threshold"
                ),
                "options": [
                    "Structured logs use less disk space than plain text",
                    "Structured logs can be parsed, filtered, and aggregated by machines without custom regex",
                    "Structured logs are required by Kubernetes",
                    "Structured logs automatically include stack traces",
                ],
                "answer": "b",
                "hints": [
                    "Think about what a log aggregation system can do with JSON vs a random string.",
                    "Parsing, filtering, aggregating — all require predictable structure.",
                ],
                "xp": 25,
            },
            {
                "id": "log_2",
                "type": "quiz",
                "title": "Log Levels",
                "question": "In standard log level hierarchies (DEBUG, INFO, WARN, ERROR, FATAL), what does setting the log level to WARN mean?",
                "lesson": (
                    "Log levels form a severity hierarchy. Setting the level to WARN\n"
                    "means only WARN, ERROR, and FATAL messages are emitted.\n"
                    "DEBUG and INFO are suppressed.\n\n"
                    "Hierarchy (lowest to highest severity):\n"
                    "  DEBUG → detailed diagnostic information\n"
                    "  INFO  → normal operational events\n"
                    "  WARN  → unexpected but recoverable situations\n"
                    "  ERROR → failures that need attention\n"
                    "  FATAL → unrecoverable failures, process will exit\n\n"
                    "Production typically runs at INFO or WARN. DEBUG is for\n"
                    "development or temporary troubleshooting — it generates\n"
                    "enormous volume and can impact performance."
                ),
                "options": [
                    "Only WARN messages are logged; all others are suppressed",
                    "All messages at WARN severity and above (WARN, ERROR, FATAL) are logged",
                    "All messages are logged but WARN messages are highlighted",
                    "WARN messages are sent to a separate warning log file",
                ],
                "answer": "b",
                "hints": [
                    "Log levels work as a threshold, not a filter for a single level.",
                    "Setting a level means 'this severity and everything more severe.'",
                ],
                "xp": 25,
            },
            {
                "id": "log_3",
                "type": "quiz",
                "title": "Centralized Logging",
                "question": "Why is centralized logging essential in a microservices architecture?",
                "lesson": (
                    "In a microservices environment, a single user request might\n"
                    "touch 10+ services running on different hosts. If each service\n"
                    "writes logs to its local filesystem, debugging requires SSH-ing\n"
                    "into every host and manually correlating timestamps.\n\n"
                    "Centralized logging sends all logs to a single searchable system.\n"
                    "You can search across all services, filter by request ID, and\n"
                    "see the complete timeline of events in one place.\n\n"
                    "Common centralized logging stacks:\n"
                    "  - ELK: Elasticsearch, Logstash, Kibana\n"
                    "  - PLG: Promtail, Loki, Grafana\n"
                    "  - Cloud-native: CloudWatch Logs, Stackdriver, Datadog Logs"
                ),
                "options": [
                    "It reduces the total volume of logs generated",
                    "It aggregates logs from all services into one searchable location for cross-service debugging",
                    "It is only needed if you have more than 100 services",
                    "It automatically fixes the errors found in the logs",
                ],
                "answer": "b",
                "hints": [
                    "Imagine debugging a request that touched 12 services on 8 hosts.",
                    "One place to search vs SSH-ing into every box.",
                ],
                "xp": 25,
            },
            {
                "id": "log_4",
                "type": "quiz",
                "title": "ELK vs Loki",
                "question": "What is a key architectural difference between Elasticsearch (ELK stack) and Grafana Loki for log storage?",
                "lesson": (
                    "Elasticsearch indexes the full content of every log line.\n"
                    "This makes arbitrary full-text search very fast but requires\n"
                    "significant compute and storage for indexing.\n\n"
                    "Loki indexes only the metadata labels (like service, namespace,\n"
                    "pod) and stores the log content as compressed chunks.\n"
                    "This is much cheaper but means you must filter by labels first,\n"
                    "then grep within the matching streams.\n\n"
                    "Trade-off:\n"
                    "  Elasticsearch: faster arbitrary search, higher resource cost\n"
                    "  Loki: much lower cost, requires label-first query patterns\n\n"
                    "Loki's approach mirrors how Prometheus stores metrics — labeled\n"
                    "streams rather than full-text indexes."
                ),
                "options": [
                    "Loki only works with Kubernetes; Elasticsearch works anywhere",
                    "Elasticsearch full-text indexes all log content; Loki indexes only labels and stores content as compressed chunks",
                    "Elasticsearch is open source; Loki is proprietary",
                    "There is no meaningful difference; they are interchangeable",
                ],
                "answer": "b",
                "hints": [
                    "Think about what each system indexes vs what it stores as raw data.",
                    "One indexes everything; the other indexes only the labels.",
                ],
                "xp": 30,
            },
            {
                "id": "log_5",
                "type": "quiz",
                "title": "Log Rotation",
                "question": "What problem does log rotation solve?",
                "lesson": (
                    "Log rotation prevents log files from consuming all available\n"
                    "disk space. Without rotation, a busy service can fill a disk\n"
                    "in hours, causing the service itself to crash.\n\n"
                    "Rotation strategies:\n"
                    "  - Size-based: rotate when file exceeds N megabytes\n"
                    "  - Time-based: rotate daily, weekly, etc.\n"
                    "  - Combined: rotate daily OR at 100MB, whichever comes first\n\n"
                    "After rotation, old files are typically:\n"
                    "  - Compressed (gzip)\n"
                    "  - Retained for N days\n"
                    "  - Deleted after retention period\n\n"
                    "Tools: logrotate (Linux), Docker's --log-opt max-size/max-file,\n"
                    "or let your centralized logging system handle retention."
                ),
                "options": [
                    "It encrypts old logs to prevent unauthorized access",
                    "It prevents log files from growing unbounded and filling up disk space",
                    "It converts plain text logs to structured JSON format",
                    "It replicates logs across multiple servers for redundancy",
                ],
                "answer": "b",
                "hints": [
                    "What happens if a log file grows forever on a finite disk?",
                    "The disk fills up. The service crashes. Rotation prevents this.",
                ],
                "xp": 25,
            },
            {
                "id": "log_6",
                "type": "quiz",
                "title": "Contextual Logging",
                "question": "What is the most important field to include in every log line for cross-service request correlation?",
                "lesson": (
                    "A request ID (or correlation ID or trace ID) is a unique\n"
                    "identifier generated at the entry point and passed through\n"
                    "every service in the call chain.\n\n"
                    "When every log line includes this ID, you can search for it\n"
                    "in your centralized logging system and see every event from\n"
                    "every service related to that single request, in order.\n\n"
                    "Without a request ID, correlating logs across services requires\n"
                    "matching timestamps and guessing — which breaks down at scale.\n\n"
                    "Best practice: generate a UUID at the API gateway or edge,\n"
                    "propagate it via HTTP header (X-Request-ID), and include it\n"
                    "in every log line and every span."
                ),
                "options": [
                    "The hostname of the server that generated the log",
                    "A unique request ID or correlation ID propagated across all services",
                    "The name of the function that generated the log",
                    "The git commit hash of the deployed code",
                ],
                "answer": "b",
                "hints": [
                    "How do you find every log line from every service for ONE user request?",
                    "You need a unique ID that follows the request everywhere.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 3: METRICS AND MONITORING ──────────────────────────────────
    "metrics_and_monitoring": {
        "id": "metrics_and_monitoring",
        "name": "The Metric Grid",
        "subtitle": "Prometheus, Grafana, and the Numbers That Matter",
        "color": "yellow",
        "icon": "📊",
        "challenges": [
            {
                "id": "met_1",
                "type": "quiz",
                "title": "Pull vs Push",
                "question": "Prometheus uses a pull-based model for collecting metrics. What does this mean?",
                "lesson": (
                    "In a pull model, the monitoring system (Prometheus) periodically\n"
                    "scrapes HTTP endpoints on your services to collect metrics.\n"
                    "Services expose a /metrics endpoint; Prometheus fetches from it.\n\n"
                    "In a push model (StatsD, Datadog Agent, InfluxDB), services\n"
                    "actively send metrics to the monitoring system.\n\n"
                    "Pull advantages:\n"
                    "  - Prometheus controls the scrape rate\n"
                    "  - Easy to tell if a target is down (scrape fails)\n"
                    "  - No need for services to know where Prometheus lives\n\n"
                    "Push advantages:\n"
                    "  - Works for short-lived jobs (batch, lambda)\n"
                    "  - Services behind firewalls can push out\n"
                    "  - No need to expose an HTTP endpoint"
                ),
                "options": [
                    "Services push metrics to Prometheus at regular intervals",
                    "Prometheus scrapes HTTP endpoints on services at configured intervals",
                    "Prometheus reads metrics directly from application log files",
                    "A sidecar container collects metrics and forwards them to Prometheus",
                ],
                "answer": "b",
                "hints": [
                    "Pull means Prometheus initiates the connection, not the service.",
                    "Services expose /metrics; Prometheus fetches it on a schedule.",
                ],
                "xp": 25,
            },
            {
                "id": "met_2",
                "type": "quiz",
                "title": "Metric Types",
                "question": "Which Prometheus metric type is appropriate for tracking the current number of in-flight HTTP requests?",
                "lesson": (
                    "Prometheus has four core metric types:\n\n"
                    "Counter: monotonically increasing value. Only goes up (or resets\n"
                    "  to zero on restart). Use for: total requests, total errors.\n\n"
                    "Gauge: value that can go up AND down. Use for: current queue\n"
                    "  depth, in-flight requests, temperature, memory usage.\n\n"
                    "Histogram: samples observations and counts them in buckets.\n"
                    "  Use for: request duration, response size.\n\n"
                    "Summary: like histogram but calculates quantiles on the client.\n"
                    "  Use rarely — histograms are more flexible and aggregatable.\n\n"
                    "In-flight requests go up when a request starts and down when\n"
                    "it completes — that's a gauge."
                ),
                "options": [
                    "Counter — it counts total requests",
                    "Gauge — it tracks a value that can increase and decrease",
                    "Histogram — it buckets request durations",
                    "Summary — it calculates percentiles on the client",
                ],
                "answer": "b",
                "hints": [
                    "In-flight requests go up when a request starts, down when it ends.",
                    "Which metric type represents a value that can both increase and decrease?",
                ],
                "xp": 30,
            },
            {
                "id": "met_3",
                "type": "quiz",
                "title": "Histograms",
                "question": "Why are histograms preferred over summaries for tracking request latency in Prometheus?",
                "lesson": (
                    "Histograms and summaries both track distributions (like latency),\n"
                    "but they differ in a critical way:\n\n"
                    "Histograms:\n"
                    "  - Count observations into configurable buckets (e.g., <100ms, <500ms, <1s)\n"
                    "  - Can be aggregated across instances (sum the bucket counts)\n"
                    "  - Quantiles computed at query time via histogram_quantile()\n\n"
                    "Summaries:\n"
                    "  - Compute quantiles on the client side\n"
                    "  - CANNOT be aggregated across instances (you can't average percentiles)\n"
                    "  - Fixed quantiles chosen at instrumentation time\n\n"
                    "Rule: use histograms unless you have a specific reason not to.\n"
                    "The ability to aggregate across instances is critical in a\n"
                    "horizontally scaled environment."
                ),
                "options": [
                    "Histograms use less memory than summaries",
                    "Histograms can be aggregated across multiple instances; summaries cannot",
                    "Histograms provide exact percentiles; summaries are approximations",
                    "Histograms are the only type supported by Grafana",
                ],
                "answer": "b",
                "hints": [
                    "Think about 10 instances each computing their own p99 — can you combine them?",
                    "You can sum histogram buckets across instances. You can't average percentiles.",
                ],
                "xp": 35,
            },
            {
                "id": "met_4",
                "type": "quiz",
                "title": "PromQL Basics",
                "question": "In PromQL, what does the rate() function do when applied to a counter metric?",
                "lesson": (
                    "rate() calculates the per-second average rate of increase of a\n"
                    "counter over a time range. It's the most common PromQL function.\n\n"
                    "Example: rate(http_requests_total[5m])\n"
                    "  → per-second request rate averaged over the last 5 minutes\n\n"
                    "Why you need rate() for counters:\n"
                    "  - Counters only go up, so raw values aren't useful for dashboards\n"
                    "  - rate() handles counter resets (from process restarts) gracefully\n"
                    "  - It gives you 'requests per second' instead of 'total requests ever'\n\n"
                    "Related functions:\n"
                    "  irate() → instantaneous rate (last two data points)\n"
                    "  increase() → total increase over the range (rate * seconds)"
                ),
                "options": [
                    "It returns the current value of the counter",
                    "It calculates the per-second average rate of increase over a time range",
                    "It resets the counter to zero",
                    "It converts the counter into a gauge",
                ],
                "answer": "b",
                "hints": [
                    "A counter only goes up. rate() tells you how fast it's climbing.",
                    "rate(http_requests_total[5m]) gives you requests per second.",
                ],
                "xp": 30,
            },
            {
                "id": "met_5",
                "type": "quiz",
                "title": "Grafana Dashboards",
                "question": "What is a Grafana dashboard variable (template variable) used for?",
                "lesson": (
                    "Dashboard variables let you create reusable dashboards where\n"
                    "users can select values from dropdowns to filter all panels.\n\n"
                    "Example: a variable $service that queries for all service names.\n"
                    "Every panel uses {service=~\"$service\"} in its PromQL.\n"
                    "Selecting 'api-gateway' from the dropdown filters all panels.\n\n"
                    "Types of variables:\n"
                    "  - Query: populated from a data source query\n"
                    "  - Custom: static list of values\n"
                    "  - Interval: time range intervals ($__interval)\n"
                    "  - Data source: select which data source to query\n\n"
                    "Without variables, you'd need separate dashboards for every\n"
                    "service, environment, and region. With variables, one dashboard\n"
                    "serves all of them."
                ),
                "options": [
                    "It stores alert thresholds that trigger notifications",
                    "It lets users select filter values from dropdowns to dynamically adjust all panels",
                    "It defines the refresh rate of the dashboard",
                    "It configures authentication for the data source",
                ],
                "answer": "b",
                "hints": [
                    "Think about a dropdown at the top of a dashboard that says 'Service: ____'.",
                    "One dashboard, many services — variables make it reusable.",
                ],
                "xp": 25,
            },
            {
                "id": "met_6",
                "type": "quiz",
                "title": "Alerting Rules",
                "question": "In Prometheus Alertmanager, what is the purpose of the 'for' duration in an alerting rule?",
                "lesson": (
                    "The 'for' clause specifies how long a condition must be true\n"
                    "before the alert transitions from 'pending' to 'firing'.\n\n"
                    "Example:\n"
                    "  alert: HighErrorRate\n"
                    "  expr: rate(http_errors_total[5m]) > 0.05\n"
                    "  for: 10m\n\n"
                    "This means the error rate must exceed 5% for 10 continuous\n"
                    "minutes before the alert fires. A brief spike that resolves\n"
                    "in 2 minutes won't trigger a notification.\n\n"
                    "Without 'for', every momentary threshold crossing fires an alert.\n"
                    "This leads to alert fatigue — a flood of notifications for\n"
                    "transient conditions that resolve on their own."
                ),
                "options": [
                    "It defines how often the alerting rule is evaluated",
                    "It specifies how long the condition must persist before the alert fires",
                    "It sets the cooldown period between repeated alert notifications",
                    "It determines the time range for the PromQL query",
                ],
                "answer": "b",
                "hints": [
                    "A brief spike shouldn't wake someone up at 3 AM.",
                    "The 'for' clause prevents firing on transient threshold crossings.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 4: DISTRIBUTED TRACING ─────────────────────────────────────
    "distributed_tracing": {
        "id": "distributed_tracing",
        "name": "The Trace Lattice",
        "subtitle": "Following Requests Through the Distributed Maze",
        "color": "magenta",
        "icon": "🔗",
        "challenges": [
            {
                "id": "trace_1",
                "type": "quiz",
                "title": "What Is a Trace?",
                "question": "In distributed tracing, what does a 'trace' represent?",
                "lesson": (
                    "A trace represents the complete journey of a single request\n"
                    "through a distributed system. It's a tree of 'spans' — each\n"
                    "span representing a unit of work in one service.\n\n"
                    "Example: user hits /checkout\n"
                    "  Trace ID: abc-123\n"
                    "  ├── Span: api-gateway (50ms)\n"
                    "  │   ├── Span: auth-service (10ms)\n"
                    "  │   ├── Span: cart-service (15ms)\n"
                    "  │   └── Span: payment-service (20ms)\n"
                    "  │       └── Span: stripe-api (18ms)\n\n"
                    "Each span records: service name, operation, start time,\n"
                    "duration, status, and key-value attributes (tags)."
                ),
                "options": [
                    "A log file that records all events in a service",
                    "The end-to-end journey of a single request across all services it touches",
                    "A metric that measures the total latency of an API endpoint",
                    "A network packet capture between two services",
                ],
                "answer": "b",
                "hints": [
                    "Think about following one request from the edge to the database and back.",
                    "A trace is a tree of spans, each representing work in one service.",
                ],
                "xp": 25,
            },
            {
                "id": "trace_2",
                "type": "quiz",
                "title": "Spans and Context",
                "question": "How is trace context propagated between services in a distributed system?",
                "lesson": (
                    "Trace context is propagated via HTTP headers (or message\n"
                    "metadata for async systems). The W3C Trace Context standard\n"
                    "uses the 'traceparent' header.\n\n"
                    "Format: traceparent: 00-{trace-id}-{parent-span-id}-{flags}\n\n"
                    "When Service A calls Service B:\n"
                    "  1. Service A creates a span and generates a span ID\n"
                    "  2. Service A adds traceparent header to the outgoing request\n"
                    "  3. Service B extracts the header and creates a child span\n"
                    "  4. Service B's span references A's span as its parent\n\n"
                    "This is called 'context propagation' and it's what connects\n"
                    "all the individual spans into a single coherent trace.\n"
                    "Without it, you have isolated spans with no relationships."
                ),
                "options": [
                    "Each service queries a central trace database to find its parent span",
                    "Via HTTP headers (like W3C traceparent) or message metadata passed between services",
                    "Through shared log files that all services write to",
                    "By matching timestamps across services after the fact",
                ],
                "answer": "b",
                "hints": [
                    "How does Service B know it's part of the same trace as Service A?",
                    "Something must be passed in the request from A to B — a header.",
                ],
                "xp": 30,
            },
            {
                "id": "trace_3",
                "type": "quiz",
                "title": "OpenTelemetry",
                "question": "What is OpenTelemetry (OTel)?",
                "lesson": (
                    "OpenTelemetry is an open-source, vendor-neutral observability\n"
                    "framework. It provides APIs, SDKs, and tools for generating,\n"
                    "collecting, and exporting telemetry data (traces, metrics, logs).\n\n"
                    "Key components:\n"
                    "  - API: defines how to create spans, metrics, etc.\n"
                    "  - SDK: implements the API with processing and export\n"
                    "  - Collector: receives, processes, and exports telemetry\n"
                    "  - Auto-instrumentation: instruments common libraries automatically\n\n"
                    "OTel is a CNCF project and the industry standard for\n"
                    "instrumentation. It merged OpenTracing and OpenCensus.\n\n"
                    "Key value: instrument once, export to any backend (Jaeger,\n"
                    "Zipkin, Datadog, Honeycomb, etc.). No vendor lock-in."
                ),
                "options": [
                    "A proprietary tracing tool built by Datadog",
                    "A vendor-neutral open-source framework for generating, collecting, and exporting telemetry",
                    "A Grafana plugin for visualizing trace data",
                    "A Kubernetes operator that automatically deploys Prometheus",
                ],
                "answer": "b",
                "hints": [
                    "It's open source, vendor neutral, and covers all three signal types.",
                    "It merged OpenTracing and OpenCensus into one standard.",
                ],
                "xp": 25,
            },
            {
                "id": "trace_4",
                "type": "quiz",
                "title": "Jaeger vs Zipkin",
                "question": "Both Jaeger and Zipkin are open-source distributed tracing backends. What is Jaeger's key advantage?",
                "lesson": (
                    "Both Jaeger and Zipkin store and visualize distributed traces.\n\n"
                    "Jaeger (by Uber, CNCF graduated):\n"
                    "  - Designed for cloud-native scale\n"
                    "  - Supports multiple storage backends (Cassandra, Elasticsearch, Kafka)\n"
                    "  - Adaptive sampling built in\n"
                    "  - Native OpenTelemetry integration\n\n"
                    "Zipkin (by Twitter):\n"
                    "  - Simpler to deploy and operate\n"
                    "  - Smaller footprint\n"
                    "  - Longer history, mature ecosystem\n\n"
                    "In practice, many teams now use the OpenTelemetry Collector\n"
                    "as the tracing frontend and choose their backend based on\n"
                    "scale requirements and existing infrastructure."
                ),
                "options": [
                    "Jaeger has a built-in alerting system; Zipkin does not",
                    "Jaeger is designed for cloud-native scale with flexible storage backends and adaptive sampling",
                    "Jaeger supports more programming languages than Zipkin",
                    "Jaeger is the only backend compatible with OpenTelemetry",
                ],
                "answer": "b",
                "hints": [
                    "Think about what you need at scale: flexible storage, sampling.",
                    "Jaeger was built by Uber specifically for large-scale distributed systems.",
                ],
                "xp": 30,
            },
            {
                "id": "trace_5",
                "type": "quiz",
                "title": "Correlation IDs",
                "question": "What is the relationship between a trace ID and a correlation ID?",
                "lesson": (
                    "A trace ID uniquely identifies one trace (one request's journey).\n"
                    "A correlation ID is a broader concept — any unique ID used to\n"
                    "correlate related events across systems.\n\n"
                    "In practice, many teams use the trace ID AS the correlation ID.\n"
                    "It appears in:\n"
                    "  - Every span in the trace\n"
                    "  - Every log line (as a field)\n"
                    "  - HTTP headers between services\n\n"
                    "This creates a powerful debugging workflow:\n"
                    "  1. See an error in logs → grab the trace_id\n"
                    "  2. Search for that trace_id in your tracing UI → see the full request path\n"
                    "  3. Click a span → see the associated logs for that span\n\n"
                    "This is 'correlated observability' — linking all three pillars\n"
                    "through a shared identifier."
                ),
                "options": [
                    "They are completely unrelated concepts from different domains",
                    "A correlation ID is used for logs; a trace ID is used only for spans",
                    "A trace ID often serves as the correlation ID, linking traces, logs, and metrics for one request",
                    "A correlation ID replaces the trace ID when using Zipkin instead of Jaeger",
                ],
                "answer": "c",
                "hints": [
                    "How do you link a log line to a trace to a metric? A shared ID.",
                    "Many teams use the trace ID as their correlation ID across all signals.",
                ],
                "xp": 30,
            },
            {
                "id": "trace_6",
                "type": "quiz",
                "title": "Trace Sampling",
                "question": "Why do most production systems sample traces instead of recording 100% of them?",
                "lesson": (
                    "At scale, recording every trace is prohibitively expensive.\n"
                    "A service handling 10,000 requests/second generates 10,000\n"
                    "traces/second, each with multiple spans, each with attributes.\n\n"
                    "Sampling strategies:\n"
                    "  - Head sampling: decide at the start (e.g., sample 10% of requests)\n"
                    "  - Tail sampling: decide after the trace completes (e.g., keep\n"
                    "    all traces with errors or latency > 1s, sample the rest)\n\n"
                    "Tail sampling is more powerful — it ensures you keep interesting\n"
                    "traces — but requires buffering complete traces before deciding,\n"
                    "which adds complexity.\n\n"
                    "OpenTelemetry Collector supports both strategies. A common\n"
                    "pattern: 100% of errors, 100% of slow requests, 1% of everything else."
                ),
                "options": [
                    "Sampling reduces network latency between services",
                    "Recording every trace at scale is prohibitively expensive in storage and compute",
                    "Tracing backends can only store a fixed number of traces",
                    "Sampling is required by the OpenTelemetry specification",
                ],
                "answer": "b",
                "hints": [
                    "10,000 requests/second x multiple spans x attributes = enormous data volume.",
                    "Cost and storage are the primary drivers for sampling.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 5: ALERTING ────────────────────────────────────────────────
    "alerting": {
        "id": "alerting",
        "name": "The Alert Channel",
        "subtitle": "SLOs, Error Budgets, and Fighting Alert Fatigue",
        "color": "red",
        "icon": "🚨",
        "challenges": [
            {
                "id": "alert_1",
                "type": "quiz",
                "title": "Alert Fatigue",
                "question": "What is alert fatigue and why is it dangerous?",
                "lesson": (
                    "Alert fatigue occurs when on-call engineers receive so many\n"
                    "alerts that they start ignoring them. The signal drowns in noise.\n\n"
                    "Causes:\n"
                    "  - Alerts that fire but require no action (false positives)\n"
                    "  - Duplicate alerts for the same incident\n"
                    "  - Low-severity conditions routed to pagers\n"
                    "  - Missing 'for' duration — alerts fire on transient spikes\n\n"
                    "The danger: when a critical alert fires among hundreds of\n"
                    "noise alerts, it gets the same response as everything else —\n"
                    "ignored or slow-acknowledged.\n\n"
                    "The fix: every alert must be actionable. If you receive it,\n"
                    "you must need to do something. If not, delete the alert."
                ),
                "options": [
                    "Engineers become desensitized to alerts due to high volume, causing them to miss critical issues",
                    "Alerts arrive too slowly because the monitoring system is overloaded",
                    "Engineers disable all alerts to reduce noise, leaving the system unmonitored",
                    "Alert fatigue only affects systems with more than 1000 services",
                ],
                "answer": "a",
                "hints": [
                    "What happens when you get 200 alerts a day, most of which require no action?",
                    "You stop reading them. The real one gets buried.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_2",
                "type": "quiz",
                "title": "SLIs and SLOs",
                "question": "What is the relationship between an SLI, an SLO, and an SLA?",
                "lesson": (
                    "SLI (Service Level Indicator): a quantitative measure of service\n"
                    "  behavior. Example: 'the proportion of requests served in < 200ms.'\n\n"
                    "SLO (Service Level Objective): a target value for an SLI.\n"
                    "  Example: '99.9% of requests served in < 200ms over 30 days.'\n\n"
                    "SLA (Service Level Agreement): a contract with consequences.\n"
                    "  Example: 'if we violate the SLO, the customer gets credits.'\n\n"
                    "Relationship: SLI is what you measure. SLO is what you aim for.\n"
                    "SLA is the business contract built on top.\n\n"
                    "Not all services need SLAs, but every service should have SLOs.\n"
                    "SLOs give you a shared definition of 'good enough' that both\n"
                    "engineering and product can agree on."
                ),
                "options": [
                    "SLI is the metric, SLO is the target for that metric, SLA is the contractual guarantee",
                    "SLA is the metric, SLO is the target, SLI is the contract",
                    "They are three different names for the same concept",
                    "SLI measures uptime, SLO measures latency, SLA measures throughput",
                ],
                "answer": "a",
                "hints": [
                    "Think: what do you measure, what target do you set, what do you promise?",
                    "Indicator → Objective → Agreement. Measurement → Target → Contract.",
                ],
                "xp": 30,
            },
            {
                "id": "alert_3",
                "type": "quiz",
                "title": "Error Budgets",
                "question": "If your SLO is 99.9% availability over 30 days, how much downtime does your error budget allow?",
                "lesson": (
                    "An error budget is the inverse of your SLO — it's the amount\n"
                    "of unreliability you can tolerate.\n\n"
                    "SLO: 99.9% availability over 30 days\n"
                    "Error budget: 0.1% of 30 days = 43.2 minutes of downtime\n\n"
                    "Calculation:\n"
                    "  30 days × 24 hours × 60 minutes = 43,200 minutes\n"
                    "  43,200 × 0.001 = 43.2 minutes\n\n"
                    "Error budgets change the conversation:\n"
                    "  Budget remaining → ship features, take risks\n"
                    "  Budget exhausted → freeze deployments, focus on reliability\n\n"
                    "This gives engineering and product a shared framework for\n"
                    "balancing velocity and reliability. It's not about perfection —\n"
                    "it's about spending your error budget wisely."
                ),
                "options": [
                    "About 4.3 minutes per month",
                    "About 43 minutes per month",
                    "About 7 hours per month",
                    "About 8.7 hours per month",
                ],
                "answer": "b",
                "hints": [
                    "30 days = 43,200 minutes. 0.1% of that is...",
                    "43,200 × 0.001 = 43.2 minutes.",
                ],
                "xp": 35,
            },
            {
                "id": "alert_4",
                "type": "quiz",
                "title": "On-Call Practices",
                "question": "Which of these is a best practice for on-call rotations?",
                "lesson": (
                    "Effective on-call practices prevent burnout and ensure fast\n"
                    "incident response:\n\n"
                    "  - Rotate regularly (weekly or biweekly)\n"
                    "  - Provide compensation (pay, time off, or both)\n"
                    "  - Ensure every alert is actionable — if it pages, it matters\n"
                    "  - Maintain runbooks for common incidents\n"
                    "  - Have escalation paths (primary → secondary → manager)\n"
                    "  - Conduct blameless postmortems after incidents\n"
                    "  - Track on-call load — pages per shift, MTTR, sleep interrupts\n\n"
                    "The goal: on-call should be sustainable. If engineers dread\n"
                    "their rotation, the system is broken — either too many alerts,\n"
                    "too few runbooks, or too little support."
                ),
                "options": [
                    "The most senior engineer should always be on call to ensure fast resolution",
                    "Alerts should be routed to a shared Slack channel instead of paging individuals",
                    "Every paging alert must be actionable, with runbooks and clear escalation paths",
                    "On-call engineers should handle both alerting and feature development simultaneously",
                ],
                "answer": "c",
                "hints": [
                    "What makes on-call sustainable vs miserable?",
                    "Actionable alerts, runbooks, escalation, and compensation.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_5",
                "type": "quiz",
                "title": "Runbooks",
                "question": "What is the primary purpose of a runbook in incident response?",
                "lesson": (
                    "A runbook is a documented procedure for diagnosing and resolving\n"
                    "a known type of incident. It turns tribal knowledge into a\n"
                    "repeatable process that any on-call engineer can follow.\n\n"
                    "A good runbook contains:\n"
                    "  - What triggered this alert and what it means\n"
                    "  - Diagnostic steps: what to check, what commands to run\n"
                    "  - Remediation steps: how to fix or mitigate\n"
                    "  - Escalation: when and who to escalate to\n"
                    "  - Links: dashboards, logs, relevant architecture docs\n\n"
                    "Runbooks reduce MTTR (Mean Time to Recovery) because the on-call\n"
                    "engineer doesn't have to figure out the procedure from scratch\n"
                    "at 3 AM. The procedure is already written."
                ),
                "options": [
                    "To document the architecture of the system for new hires",
                    "To provide step-by-step diagnosis and remediation procedures for known incident types",
                    "To replace the need for on-call engineers by automating all responses",
                    "To track the history of all past incidents in a searchable format",
                ],
                "answer": "b",
                "hints": [
                    "It's 3 AM, an alert fires, and you've never seen this service before.",
                    "What document do you need? One with step-by-step instructions.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_6",
                "type": "quiz",
                "title": "PagerDuty and Routing",
                "question": "In PagerDuty (or similar incident management tools), what is an 'escalation policy'?",
                "lesson": (
                    "An escalation policy defines what happens when an alert is not\n"
                    "acknowledged within a certain time.\n\n"
                    "Typical escalation chain:\n"
                    "  0 min: page the primary on-call engineer\n"
                    "  5 min: if not acknowledged, page the secondary on-call\n"
                    "  15 min: if still not acknowledged, page the engineering manager\n"
                    "  30 min: if still not acknowledged, page the VP of Engineering\n\n"
                    "Escalation policies ensure no alert goes unhandled. They also\n"
                    "allow routing based on service, severity, and time of day.\n\n"
                    "Integration: Prometheus Alertmanager → PagerDuty → on-call schedule\n"
                    "→ escalation policy → notification (push, SMS, phone call)."
                ),
                "options": [
                    "A rule that suppresses duplicate alerts for the same incident",
                    "A chain of contacts notified in sequence if the alert is not acknowledged in time",
                    "A policy that automatically resolves alerts after a timeout",
                    "A filter that routes low-severity alerts to email instead of pager",
                ],
                "answer": "b",
                "hints": [
                    "What happens if the primary on-call doesn't respond?",
                    "The alert escalates to the next person in the chain.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 6: DEBUGGING PRODUCTION ────────────────────────────────────
    "debugging_production": {
        "id": "debugging_production",
        "name": "The Signal Floor",
        "subtitle": "Reading Dashboards, Correlating Signals, Finding Root Cause",
        "color": "blue",
        "icon": "🔍",
        "challenges": [
            {
                "id": "debug_1",
                "type": "quiz",
                "title": "The USE Method",
                "question": "The USE method (Utilization, Saturation, Errors) is used for debugging performance problems. What does 'Saturation' measure?",
                "lesson": (
                    "The USE method (by Brendan Gregg) provides a systematic approach\n"
                    "to performance analysis for every resource (CPU, memory, disk, network):\n\n"
                    "Utilization: how busy the resource is (% time busy)\n"
                    "  Example: CPU at 85% utilization\n\n"
                    "Saturation: how much extra work is queued (waiting)\n"
                    "  Example: CPU run queue length of 12 (work waiting for CPU time)\n\n"
                    "Errors: count of error events for the resource\n"
                    "  Example: disk I/O errors, network packet drops\n\n"
                    "The method works by checking U, S, and E for every resource.\n"
                    "If CPU saturation is high (long run queue), you've found the\n"
                    "bottleneck — even if utilization looks acceptable."
                ),
                "options": [
                    "The percentage of the resource's capacity currently in use",
                    "The amount of extra work queued because the resource is fully busy",
                    "The number of errors encountered by the resource",
                    "The total throughput the resource is handling",
                ],
                "answer": "b",
                "hints": [
                    "Utilization = how busy. Errors = what broke. Saturation = what's waiting.",
                    "Think of a queue — work piling up because the resource can't keep up.",
                ],
                "xp": 35,
            },
            {
                "id": "debug_2",
                "type": "quiz",
                "title": "The RED Method",
                "question": "The RED method (Rate, Errors, Duration) is used for monitoring what type of system component?",
                "lesson": (
                    "The RED method (by Tom Wilkie) is for request-driven services:\n\n"
                    "Rate: requests per second\n"
                    "Errors: failed requests per second\n"
                    "Duration: time per request (latency distribution)\n\n"
                    "USE is for resources (CPU, disk, network).\n"
                    "RED is for services (APIs, microservices, endpoints).\n\n"
                    "Together they cover both infrastructure and application layers:\n"
                    "  - RED tells you: 'the checkout service is slow'\n"
                    "  - USE tells you: 'because the database server's disk is saturated'\n\n"
                    "Google's Four Golden Signals (latency, traffic, errors, saturation)\n"
                    "combine elements of both methods."
                ),
                "options": [
                    "Hardware resources like CPU and memory",
                    "Request-driven services like APIs and microservices",
                    "Network infrastructure like routers and load balancers",
                    "Batch processing jobs and scheduled tasks",
                ],
                "answer": "b",
                "hints": [
                    "Rate of requests, errors in requests, duration of requests — all request-focused.",
                    "USE = resources, RED = services.",
                ],
                "xp": 30,
            },
            {
                "id": "debug_3",
                "type": "quiz",
                "title": "Correlating Signals",
                "question": "During an incident, you see high API latency on a Grafana dashboard. What is the most effective next step?",
                "lesson": (
                    "Effective debugging correlates signals across the three pillars:\n\n"
                    "1. Metrics tell you WHAT is wrong: latency is high\n"
                    "2. Traces tell you WHERE: which services in the request path are slow\n"
                    "3. Logs tell you WHY: error messages, stack traces, specific failures\n\n"
                    "Workflow:\n"
                    "  Dashboard shows high latency (metrics)\n"
                    "  → Find a slow trace for that time window (traces)\n"
                    "  → Identify the slow span (traces)\n"
                    "  → Look at logs for that service/time (logs)\n"
                    "  → Root cause: database connection pool exhausted\n\n"
                    "This is why correlated observability (shared trace IDs across\n"
                    "all signals) is so powerful — it creates a direct path from\n"
                    "'something is wrong' to 'here is why.'"
                ),
                "options": [
                    "Restart the API service immediately to restore performance",
                    "Check traces for the affected time window to identify which service or span is slow",
                    "Increase the API server's CPU allocation in case it's resource-constrained",
                    "Wait 10 minutes to see if the latency resolves on its own",
                ],
                "answer": "b",
                "hints": [
                    "Metrics told you something is wrong. What tells you where?",
                    "Traces show you the request path and which service is the bottleneck.",
                ],
                "xp": 30,
            },
            {
                "id": "debug_4",
                "type": "quiz",
                "title": "Incident Timelines",
                "question": "During a postmortem, why is constructing a detailed incident timeline critical?",
                "lesson": (
                    "An incident timeline is a minute-by-minute record of what\n"
                    "happened, what was observed, and what actions were taken.\n\n"
                    "Why it matters:\n"
                    "  - Reveals the gap between when the problem started and when it\n"
                    "    was detected (detection latency)\n"
                    "  - Shows whether actions taken helped or made things worse\n"
                    "  - Identifies missing observability (we didn't know because\n"
                    "    we had no metric for X)\n"
                    "  - Drives concrete improvements to monitoring and alerting\n\n"
                    "A good timeline uses UTC timestamps and includes:\n"
                    "  - System events (deployments, config changes, autoscaling)\n"
                    "  - Alerts fired and acknowledged\n"
                    "  - Human actions (rollback, restart, escalation)\n"
                    "  - Recovery confirmation"
                ),
                "options": [
                    "To assign blame to the person who caused the incident",
                    "To create a minute-by-minute record that reveals detection gaps, response effectiveness, and areas to improve",
                    "To calculate the exact financial cost of the downtime",
                    "To satisfy compliance requirements for incident documentation",
                ],
                "answer": "b",
                "hints": [
                    "Blameless postmortems focus on the system, not the person.",
                    "The timeline reveals what you could have detected earlier.",
                ],
                "xp": 30,
            },
            {
                "id": "debug_5",
                "type": "quiz",
                "title": "Flame Graphs",
                "question": "What does a flame graph visualize?",
                "lesson": (
                    "A flame graph (by Brendan Gregg) visualizes stack traces\n"
                    "aggregated over time, showing where a program spends its time.\n\n"
                    "How to read one:\n"
                    "  - X-axis: sorted alphabetically (NOT time — width = proportion)\n"
                    "  - Y-axis: stack depth (bottom = entry point, top = leaf function)\n"
                    "  - Width of a bar: proportion of total samples in that function\n\n"
                    "A wide bar means that function (and its children) consumed\n"
                    "a large proportion of CPU time. A wide bar at the TOP of the\n"
                    "stack means the function itself is the bottleneck (not its\n"
                    "children).\n\n"
                    "Use cases: CPU profiling, memory allocation profiling,\n"
                    "off-CPU analysis (time spent waiting), I/O analysis."
                ),
                "options": [
                    "Network traffic flow between microservices",
                    "Aggregated stack traces showing where a program spends its CPU time",
                    "The temperature and fan speeds of server hardware",
                    "The timeline of events during an incident",
                ],
                "answer": "b",
                "hints": [
                    "Think about profiling — where does the code spend its time?",
                    "Stack traces, aggregated, visualized. Wide bars = time spent there.",
                ],
                "xp": 35,
            },
            {
                "id": "debug_6",
                "type": "quiz",
                "title": "Golden Signals",
                "question": "Google's 'Four Golden Signals' for monitoring user-facing systems are latency, traffic, errors, and what?",
                "lesson": (
                    "The Four Golden Signals (from Google's SRE book):\n\n"
                    "Latency: time to serve a request\n"
                    "  Important: distinguish successful vs failed request latency.\n"
                    "  A fast error (500 in 2ms) should not lower your average.\n\n"
                    "Traffic: demand on the system (requests/sec, sessions, etc.)\n\n"
                    "Errors: rate of failed requests (explicit 5xx, implicit — wrong\n"
                    "  content, policy violations, timeouts)\n\n"
                    "Saturation: how full the system is. How close are you to the\n"
                    "  limits? CPU, memory, I/O, queue depth.\n\n"
                    "If you can only measure four things about a service, measure\n"
                    "these. They cover the user experience (latency, errors),\n"
                    "the demand (traffic), and the capacity (saturation)."
                ),
                "options": [
                    "Availability — the percentage of time the system is operational",
                    "Throughput — the number of operations per second",
                    "Saturation — how close the system is to its capacity limits",
                    "Reliability — the percentage of requests that succeed",
                ],
                "answer": "c",
                "hints": [
                    "Latency, traffic, errors, and... how 'full' the system is.",
                    "It's about capacity — how close are you to your limits?",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 7: COST AND SCALE ──────────────────────────────────────────
    "cost_and_scale": {
        "id": "cost_and_scale",
        "name": "The Data Furnace",
        "subtitle": "Cardinality, Sampling, Retention, and the Bill",
        "color": "white",
        "icon": "💰",
        "challenges": [
            {
                "id": "cost_1",
                "type": "quiz",
                "title": "Cardinality Explosion",
                "question": "A Prometheus metric http_request_duration has labels {method, path, status, user_id}. With 5 methods, 100 paths, 10 statuses, and 1M users, how many time series does this create?",
                "lesson": (
                    "Cardinality explosion occurs when label combinations multiply\n"
                    "to create an unmanageable number of time series.\n\n"
                    "Calculation: 5 × 100 × 10 × 1,000,000 = 5 BILLION time series\n\n"
                    "This will crash Prometheus. The fix: never put high-cardinality\n"
                    "values (user IDs, request IDs, IP addresses) in metric labels.\n\n"
                    "Rules of thumb:\n"
                    "  - Labels should have low cardinality (< 100 unique values)\n"
                    "  - High-cardinality data belongs in logs and traces, not metrics\n"
                    "  - If you need per-user metrics, pre-aggregate (e.g., by user tier)\n\n"
                    "Metrics are for aggregate trends. Logs and traces are for\n"
                    "individual events. Putting individual identifiers in metric\n"
                    "labels conflates the two."
                ),
                "options": [
                    "5,000 time series",
                    "1,000,115 time series",
                    "5 billion time series",
                    "It depends on the scrape interval",
                ],
                "answer": "c",
                "hints": [
                    "Multiply ALL the unique values: 5 × 100 × 10 × 1,000,000.",
                    "user_id with 1M unique values is the problem — that's high cardinality.",
                ],
                "xp": 35,
            },
            {
                "id": "cost_2",
                "type": "quiz",
                "title": "Sampling Strategies",
                "question": "What is the advantage of tail-based sampling over head-based sampling for traces?",
                "lesson": (
                    "Head-based sampling decides whether to record a trace at the\n"
                    "START of the request (before you know what will happen).\n"
                    "Example: randomly sample 10% of all requests.\n\n"
                    "Tail-based sampling decides AFTER the trace is complete.\n"
                    "Example: keep all traces with errors or latency > 1s;\n"
                    "sample 1% of everything else.\n\n"
                    "Tail-based advantages:\n"
                    "  - Keeps 100% of interesting traces (errors, slow, unusual)\n"
                    "  - Discards only boring, successful, fast requests\n"
                    "  - Better debugging signal per byte stored\n\n"
                    "Tail-based disadvantages:\n"
                    "  - Requires buffering all spans until the trace completes\n"
                    "  - More complex infrastructure (OTel Collector tail sampling processor)\n"
                    "  - Adds latency to the telemetry pipeline"
                ),
                "options": [
                    "Tail sampling uses less memory because it buffers fewer spans",
                    "Tail sampling decides after seeing the complete trace, so it can keep errors and slow traces while discarding the rest",
                    "Tail sampling is simpler to implement than head sampling",
                    "Tail sampling works without an OpenTelemetry Collector",
                ],
                "answer": "b",
                "hints": [
                    "Head sampling decides before the request; tail decides after.",
                    "After seeing the whole trace, you know which ones are worth keeping.",
                ],
                "xp": 35,
            },
            {
                "id": "cost_3",
                "type": "quiz",
                "title": "Retention Policies",
                "question": "Why do observability systems use different retention periods for different data types (e.g., 15 days for raw metrics, 1 year for aggregated metrics)?",
                "lesson": (
                    "Raw, high-resolution data is expensive to store. Aggregated\n"
                    "data is much smaller but loses detail.\n\n"
                    "Typical tiered retention:\n"
                    "  Raw metrics (15s resolution): keep 15 days\n"
                    "  1-minute rollups: keep 90 days\n"
                    "  1-hour rollups: keep 1 year\n"
                    "  1-day rollups: keep 3 years\n\n"
                    "For debugging a current incident, you need 15-second resolution.\n"
                    "For capacity planning, 1-hour resolution over 6 months is fine.\n"
                    "For annual trend analysis, daily rollups are sufficient.\n\n"
                    "This tiered approach can reduce storage costs by 90%+ while\n"
                    "preserving the ability to answer questions at every timescale.\n"
                    "Tools like Thanos, Cortex, and Mimir implement this natively."
                ),
                "options": [
                    "Compliance regulations require different retention for different data",
                    "Raw data is expensive to store long-term; aggregated data preserves trends at a fraction of the cost",
                    "Older data becomes inaccurate and must be discarded",
                    "Storage systems can only handle one resolution at a time",
                ],
                "answer": "b",
                "hints": [
                    "15-second resolution for 3 years = enormous storage bill.",
                    "Aggregate old data: keep the trends, lose the detail, save the money.",
                ],
                "xp": 30,
            },
            {
                "id": "cost_4",
                "type": "quiz",
                "title": "Observability Costs",
                "question": "In a typical SaaS observability platform (Datadog, New Relic, etc.), what is the primary cost driver?",
                "lesson": (
                    "SaaS observability pricing is typically based on data volume:\n\n"
                    "  - Metrics: cost per custom metric or time series per month\n"
                    "  - Logs: cost per GB ingested (and sometimes per GB stored)\n"
                    "  - Traces: cost per span or per GB ingested\n"
                    "  - Hosts: cost per monitored host per month\n\n"
                    "The biggest surprise for most teams: log ingestion.\n"
                    "A single verbose microservice can generate 100+ GB of logs\n"
                    "per day. At $0.10-$0.30 per GB, that's $10-30/day for ONE service.\n\n"
                    "Cost control strategies:\n"
                    "  - Drop debug logs in production\n"
                    "  - Sample traces (keep 100% errors, 1-10% success)\n"
                    "  - Avoid high-cardinality metric labels\n"
                    "  - Set retention policies aggressively\n"
                    "  - Use the telemetry pipeline to filter before it hits the backend"
                ),
                "options": [
                    "The number of dashboards and alerts configured",
                    "The volume of data ingested — metrics, logs, traces, and spans",
                    "The number of engineers with login access to the platform",
                    "The number of integrations enabled (Kubernetes, AWS, etc.)",
                ],
                "answer": "b",
                "hints": [
                    "Think about what scales with your system: data volume.",
                    "More services, more logs, more metrics, more traces = higher bill.",
                ],
                "xp": 30,
            },
            {
                "id": "cost_5",
                "type": "quiz",
                "title": "Right-Sizing Observability",
                "question": "What is the 'build vs buy' trade-off in observability tooling?",
                "lesson": (
                    "Build (self-hosted): Prometheus + Grafana + Loki + Jaeger\n"
                    "  Pros: no per-GB costs, full control, no vendor lock-in\n"
                    "  Cons: operational burden (upgrades, scaling, storage), need\n"
                    "        dedicated team to maintain, feature lag vs SaaS\n\n"
                    "Buy (SaaS): Datadog, New Relic, Honeycomb, Grafana Cloud\n"
                    "  Pros: zero ops burden, faster time to value, advanced features\n"
                    "  Cons: per-GB/per-host costs scale with data volume, vendor\n"
                    "        lock-in, less control over retention and processing\n\n"
                    "Hybrid: self-host core metrics (Prometheus), SaaS for traces\n"
                    "and logs where the operational complexity is higher.\n\n"
                    "The break-even point depends on your team size, data volume,\n"
                    "and the cost of engineering time vs SaaS bills."
                ),
                "options": [
                    "Building is always cheaper; SaaS is always more expensive at any scale",
                    "Self-hosted tools have no cost since they are open source",
                    "Self-hosted gives control and avoids per-GB fees but requires operational investment; SaaS trades money for reduced ops burden",
                    "SaaS tools always provide better data quality than self-hosted alternatives",
                ],
                "answer": "c",
                "hints": [
                    "Open source isn't free — someone has to run it, scale it, upgrade it.",
                    "The trade-off: engineering time vs SaaS bill. Both are real costs.",
                ],
                "xp": 30,
            },
            {
                "id": "cost_6",
                "type": "quiz",
                "title": "Pipeline Filtering",
                "question": "How can a telemetry pipeline (like OpenTelemetry Collector) reduce observability costs?",
                "lesson": (
                    "The telemetry pipeline sits between your applications and your\n"
                    "backends. It can transform data before it reaches (and costs\n"
                    "money in) your storage/SaaS backend.\n\n"
                    "Cost-reducing pipeline operations:\n"
                    "  - Drop: remove debug-level logs before ingestion\n"
                    "  - Sample: keep 100% of errors, 5% of successful traces\n"
                    "  - Filter: drop metrics from non-production namespaces\n"
                    "  - Transform: remove high-cardinality labels from metrics\n"
                    "  - Aggregate: pre-aggregate metrics to reduce time series count\n"
                    "  - Route: send critical data to SaaS, bulk data to cheap storage\n\n"
                    "The key insight: filter BEFORE ingestion. Every byte that hits\n"
                    "your backend costs money. The pipeline is where you decide what's\n"
                    "worth keeping."
                ),
                "options": [
                    "By compressing all data with gzip before sending it to backends",
                    "By filtering, sampling, and transforming telemetry before it reaches the backend, reducing ingested volume",
                    "By caching frequently accessed dashboards to reduce query load",
                    "By replacing SaaS backends with local file storage",
                ],
                "answer": "b",
                "hints": [
                    "The cheapest byte is the one that never reaches your backend.",
                    "Filter, sample, transform — all in the pipeline, before ingestion.",
                ],
                "xp": 30,
            },
        ],
    },
}
