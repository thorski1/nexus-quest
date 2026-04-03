"""
zones.py - All zone and challenge data for Monitoring skill pack (The Watchtower)
Theme: The tower sees all. Every metric, every log, every trace — if you know where to look.
Challenge types: quiz (multiple choice, a/b/c/d) and text (free-form answer)
"""

ZONE_ORDER = [
    "prometheus_promql",
    "grafana_dashboards",
    "log_management",
    "alerting_oncall",
    "apm_profiling",
]

ZONES = {
    # ── ZONE 1: PROMETHEUS & PROMQL ──────────────────────────────────────
    "prometheus_promql": {
        "id": "prometheus_promql",
        "name": "The Metric Forge",
        "subtitle": "Prometheus, PromQL, and the Language of Time Series",
        "color": "cyan",
        "icon": "🔥",
        "challenges": [
            {
                "id": "prom_1",
                "type": "quiz",
                "title": "Metric Types — Counter",
                "question": "Which Prometheus metric type is monotonically increasing and resets only on process restart?",
                "lesson": (
                    "A Counter is a cumulative metric that only goes up (or resets to zero\n"
                    "on restart). Use it for things you count: requests served, errors\n"
                    "encountered, bytes sent.\n\n"
                    "Never use a counter for values that can decrease (like active\n"
                    "connections or queue depth). That's what gauges are for.\n\n"
                    "To get a useful rate from a counter, use rate() or irate() in PromQL:\n"
                    "  rate(http_requests_total[5m])"
                ),
                "options": [
                    "Counter",
                    "Gauge",
                    "Histogram",
                    "Summary",
                ],
                "answer": "a",
                "hints": [
                    "Think about a metric that counts total events since process start.",
                    "It never decreases during normal operation — only resets on restart.",
                ],
                "xp": 25,
            },
            {
                "id": "prom_2",
                "type": "quiz",
                "title": "Metric Types — Gauge",
                "question": "You need to monitor the current number of active database connections. Which Prometheus metric type should you use?",
                "lesson": (
                    "A Gauge represents a single numerical value that can go up AND down.\n"
                    "Examples: temperature, memory usage, active connections, queue depth.\n\n"
                    "Unlike counters, gauges have no rate() semantics — their current\n"
                    "value IS the information. You can use min_over_time(), max_over_time(),\n"
                    "and avg_over_time() to analyze gauge behavior over windows."
                ),
                "options": [
                    "Counter",
                    "Gauge",
                    "Histogram",
                    "Summary",
                ],
                "answer": "b",
                "hints": [
                    "Active connections can increase and decrease.",
                    "You need a metric type that represents a point-in-time snapshot.",
                ],
                "xp": 25,
            },
            {
                "id": "prom_3",
                "type": "quiz",
                "title": "Metric Types — Histogram",
                "question": "Which Prometheus metric type lets you calculate arbitrary quantiles (p50, p95, p99) server-side from stored data?",
                "lesson": (
                    "A Histogram samples observations (usually request durations or response\n"
                    "sizes) and counts them in configurable buckets. It exposes:\n"
                    "  _bucket — cumulative counters for each bucket boundary\n"
                    "  _sum — total sum of observed values\n"
                    "  _count — total number of observations\n\n"
                    "The key advantage: you can compute arbitrary quantiles server-side\n"
                    "using histogram_quantile(). A Summary computes quantiles client-side\n"
                    "and cannot be aggregated across instances."
                ),
                "options": [
                    "Counter",
                    "Gauge",
                    "Histogram",
                    "Summary",
                ],
                "answer": "c",
                "hints": [
                    "Summaries compute quantiles client-side and can't be re-aggregated.",
                    "This type uses configurable buckets to store distribution data.",
                ],
                "xp": 25,
            },
            {
                "id": "prom_4",
                "type": "text",
                "title": "Scrape Model",
                "question": (
                    "Prometheus collects metrics by periodically making HTTP requests\n"
                    "to targets' /metrics endpoints.\n\n"
                    "Is Prometheus a PULL-based or PUSH-based monitoring system?\n\n"
                    "Answer with one word: pull or push."
                ),
                "lesson": (
                    "Prometheus uses a PULL model. The server scrapes targets at a\n"
                    "configured interval (typically 15-60 seconds) by sending HTTP GET\n"
                    "requests to their /metrics endpoint.\n\n"
                    "Advantages of pull:\n"
                    "  - Easy to tell if a target is down (scrape fails)\n"
                    "  - Targets don't need to know about Prometheus\n"
                    "  - No risk of overwhelming the monitoring system with pushes\n\n"
                    "For short-lived jobs that can't be scraped, Prometheus provides\n"
                    "the Pushgateway as a bridge."
                ),
                "options": [],
                "answer": "pull",
                "hints": [
                    "The server initiates the connection, not the application.",
                    "Think about how Prometheus discovers and collects from targets.",
                ],
                "xp": 30,
            },
            {
                "id": "prom_5",
                "type": "quiz",
                "title": "rate() Function",
                "question": "What does the PromQL function rate(http_requests_total[5m]) calculate?",
                "lesson": (
                    "rate() calculates the per-second average rate of increase of a\n"
                    "counter over a time window. It handles counter resets automatically.\n\n"
                    "rate(http_requests_total[5m]) means: 'how many requests per second\n"
                    "on average over the last 5 minutes?'\n\n"
                    "Important: rate() should only be used with counters. Using it on\n"
                    "gauges produces meaningless results. The window (e.g., [5m]) should\n"
                    "be at least 4x your scrape interval to handle missed scrapes."
                ),
                "options": [
                    "The per-second average rate of increase over the last 5 minutes",
                    "The total number of requests in the last 5 minutes",
                    "The maximum request rate observed in any 1-second window",
                    "The current instantaneous request rate",
                ],
                "answer": "a",
                "hints": [
                    "rate() returns a per-second value, not a total count.",
                    "The [5m] is the lookback window for computing the average.",
                ],
                "xp": 25,
            },
            {
                "id": "prom_6",
                "type": "quiz",
                "title": "Label Selectors",
                "question": "In PromQL, what does this query return?\n\n  http_requests_total{status=~\"5..\"}",
                "lesson": (
                    "The =~ operator is a regex match on label values. The pattern \"5..\"\n"
                    "matches any status code starting with 5 (500, 502, 503, etc.).\n\n"
                    "Label matchers:\n"
                    "  =   exact match\n"
                    "  !=  not equal\n"
                    "  =~  regex match\n"
                    "  !~  negative regex match\n\n"
                    "Labels are the dimensions of your metrics. Every unique combination\n"
                    "of label values creates a separate time series. This is where\n"
                    "cardinality comes from."
                ),
                "options": [
                    "All HTTP requests with any status code",
                    "Only HTTP requests with status code exactly 500",
                    "All HTTP requests with 5xx status codes (500, 502, 503, etc.)",
                    "All HTTP requests excluding 5xx status codes",
                ],
                "answer": "c",
                "hints": [
                    "The =~ operator performs a regex match.",
                    "\"5..\" is a regex: 5 followed by any two characters.",
                ],
                "xp": 25,
            },
            {
                "id": "prom_7",
                "type": "text",
                "title": "histogram_quantile()",
                "question": (
                    "You want to calculate the 99th percentile request latency from a\n"
                    "histogram metric called http_request_duration_seconds.\n\n"
                    "Complete this PromQL expression:\n"
                    "  histogram_quantile(____, rate(http_request_duration_seconds_bucket[5m]))\n\n"
                    "What value goes in the blank? Answer with the decimal number only."
                ),
                "lesson": (
                    "histogram_quantile(0.99, ...) computes the 99th percentile.\n\n"
                    "The first argument is the quantile as a float between 0 and 1:\n"
                    "  0.5  = 50th percentile (median)\n"
                    "  0.95 = 95th percentile\n"
                    "  0.99 = 99th percentile\n\n"
                    "The second argument must be a rate() over the _bucket metric.\n"
                    "Using rate() ensures correct calculation across scrape intervals\n"
                    "and counter resets."
                ),
                "options": [],
                "answer": "0.99",
                "hints": [
                    "Quantiles are expressed as a decimal between 0 and 1.",
                    "The 99th percentile = 99/100 as a decimal.",
                ],
                "xp": 30,
            },
            {
                "id": "prom_8",
                "type": "quiz",
                "title": "Service Discovery",
                "question": "How does Prometheus typically discover which targets to scrape in a Kubernetes environment?",
                "lesson": (
                    "In Kubernetes, Prometheus uses the Kubernetes service discovery\n"
                    "mechanism (kubernetes_sd_configs) to automatically discover pods,\n"
                    "services, endpoints, and nodes.\n\n"
                    "Pods annotated with prometheus.io/scrape: 'true' are automatically\n"
                    "picked up. Relabeling rules extract the scrape port, path, and\n"
                    "scheme from annotations.\n\n"
                    "This is far superior to static configs — new services are discovered\n"
                    "automatically as they deploy, with no manual configuration needed."
                ),
                "options": [
                    "Static configuration files that must be updated on every deployment",
                    "Kubernetes service discovery via API, using pod annotations",
                    "DNS round-robin queries against a service name",
                    "Each pod pushes its address to Prometheus on startup",
                ],
                "answer": "b",
                "hints": [
                    "Prometheus integrates natively with Kubernetes' API server.",
                    "Think about annotations like prometheus.io/scrape: 'true'.",
                ],
                "xp": 25,
            },
        ],
    },
    # ── ZONE 2: GRAFANA DASHBOARDS ───────────────────────────────────────
    "grafana_dashboards": {
        "id": "grafana_dashboards",
        "name": "The Glass Wall",
        "subtitle": "Dashboards, Panels, Variables, and Visual Signals",
        "color": "green",
        "icon": "📊",
        "challenges": [
            {
                "id": "graf_1",
                "type": "quiz",
                "title": "Panel Types",
                "question": "You want to display the current value of a single metric (e.g., total active users right now). Which Grafana panel type is most appropriate?",
                "lesson": (
                    "The Stat panel (formerly Singlestat) displays a single large number,\n"
                    "optionally with a sparkline showing recent trend. It's ideal for\n"
                    "KPI dashboards: active users, error rate, deployment count.\n\n"
                    "Common panel types:\n"
                    "  Time series — line/area/bar charts over time\n"
                    "  Stat — single big number with optional sparkline\n"
                    "  Gauge — circular/bar gauge for values within a range\n"
                    "  Table — tabular data display\n"
                    "  Heatmap — 2D histogram (e.g., latency distribution over time)"
                ),
                "options": [
                    "Time series panel",
                    "Stat panel",
                    "Table panel",
                    "Heatmap panel",
                ],
                "answer": "b",
                "hints": [
                    "You want a single, prominent number — not a chart or table.",
                    "This panel type replaced 'Singlestat' in newer Grafana versions.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_2",
                "type": "quiz",
                "title": "Template Variables",
                "question": "What is the primary purpose of Grafana template variables (the dropdowns at the top of a dashboard)?",
                "lesson": (
                    "Template variables make dashboards reusable. Instead of creating\n"
                    "separate dashboards for each service or environment, you create\n"
                    "one dashboard with variables like $service, $namespace, $env.\n\n"
                    "Variables can be populated from:\n"
                    "  - Label values in Prometheus (label_values query)\n"
                    "  - Custom static lists\n"
                    "  - Other datasources\n\n"
                    "Queries in panels use these variables: rate(http_requests_total{service=\"$service\"}[5m])\n"
                    "When the user selects a different service from the dropdown, all panels update."
                ),
                "options": [
                    "To store user preferences and themes",
                    "To make dashboards reusable by parameterizing queries with selectable values",
                    "To define alert thresholds that can be changed without editing queries",
                    "To control which users can see which panels",
                ],
                "answer": "b",
                "hints": [
                    "Think about why you'd want a dropdown for 'service' or 'environment'.",
                    "It's about making one dashboard serve many use cases.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_3",
                "type": "quiz",
                "title": "Dashboard Best Practice",
                "question": "A team has 47 dashboards. 30 show 'No Data.' What is the most likely root cause?",
                "lesson": (
                    "Dashboard sprawl is one of the most common observability anti-patterns.\n"
                    "Teams create dashboards for every incident, never delete them, and\n"
                    "don't maintain them as metrics change or services evolve.\n\n"
                    "Best practices:\n"
                    "  - Every dashboard should have an owner\n"
                    "  - Dashboards should be version-controlled (as code)\n"
                    "  - Review and prune quarterly\n"
                    "  - Use folders and naming conventions\n"
                    "  - Start with USE/RED method dashboards, not ad hoc ones"
                ),
                "options": [
                    "Grafana's data source connection is misconfigured",
                    "The Prometheus retention period is too short",
                    "Dashboard sprawl — dashboards were created and never maintained as metrics changed",
                    "The network firewall is blocking Grafana from reaching Prometheus",
                ],
                "answer": "c",
                "hints": [
                    "If only 30 of 47 are broken, the data source itself is working.",
                    "Think about what happens when dashboards are created but never updated.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_4",
                "type": "text",
                "title": "Grafana Alerting",
                "question": (
                    "In Grafana, you can define alert rules that evaluate queries and\n"
                    "fire notifications. What is the name of the component that handles\n"
                    "routing, grouping, and silencing of alerts in the Prometheus/Grafana\n"
                    "ecosystem?\n\n"
                    "Answer with the single-word component name (no spaces)."
                ),
                "lesson": (
                    "Alertmanager handles the routing, grouping, deduplication, and\n"
                    "silencing of alerts from Prometheus and Grafana.\n\n"
                    "Key features:\n"
                    "  Grouping — combines related alerts into one notification\n"
                    "  Inhibition — suppresses alerts when a related, higher-severity alert fires\n"
                    "  Silencing — temporarily mutes specific alerts during maintenance\n"
                    "  Routing — sends alerts to different receivers based on labels\n\n"
                    "Without Alertmanager, every alert rule fires independently,\n"
                    "flooding on-call engineers with duplicate notifications."
                ),
                "options": [],
                "answer": "alertmanager",
                "hints": [
                    "It's a standalone component in the Prometheus ecosystem.",
                    "Its name literally describes what it does — manages alerts.",
                ],
                "xp": 30,
            },
            {
                "id": "graf_5",
                "type": "quiz",
                "title": "Dashboard as Code",
                "question": "What is the primary benefit of managing Grafana dashboards as code (e.g., using Grafonnet or Terraform)?",
                "lesson": (
                    "Dashboards as code (using Grafonnet/Jsonnet, Terraform, or the\n"
                    "Grafana API) provides:\n\n"
                    "  Version control — track changes, review diffs, roll back\n"
                    "  Reproducibility — deploy identical dashboards across environments\n"
                    "  Automation — CI/CD pipelines create/update dashboards on deploy\n"
                    "  Standardization — templates enforce consistent layout/queries\n\n"
                    "Manual dashboard creation via the UI leads to drift between\n"
                    "environments, undocumented changes, and the 'No Data' problem\n"
                    "when metrics change but dashboards don't."
                ),
                "options": [
                    "Dashboards load faster when defined in code",
                    "Version control, reproducibility, and consistent deployment across environments",
                    "Grafana requires code-based dashboards for alerting to work",
                    "Code-based dashboards use less storage than UI-created ones",
                ],
                "answer": "b",
                "hints": [
                    "Think about what you gain when any configuration is stored in Git.",
                    "Reproducibility and version history are the main benefits.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_6",
                "type": "quiz",
                "title": "Heatmap Panels",
                "question": "A Grafana heatmap panel showing request latency over time displays colors from green to red. What does a bright red cell indicate?",
                "lesson": (
                    "In a heatmap, each cell represents a bucket of values at a point\n"
                    "in time. The color intensity shows the count of observations in\n"
                    "that bucket. Bright red = high concentration of requests at that\n"
                    "latency value during that time window.\n\n"
                    "Heatmaps are excellent for visualizing latency distributions\n"
                    "because they show the full shape of the distribution, not just\n"
                    "a single percentile. You can spot bimodal distributions, outliers,\n"
                    "and shifts that p99 alone would hide."
                ),
                "options": [
                    "A single request with extremely high latency",
                    "A high concentration of requests at that latency value during that time period",
                    "An error condition where the service was down",
                    "The p99 latency exceeded the SLO threshold",
                ],
                "answer": "b",
                "hints": [
                    "Heatmap cells represent counts of observations in a bucket.",
                    "Color intensity = density, not severity.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_7",
                "type": "quiz",
                "title": "Data Source Configuration",
                "question": "You add Prometheus as a data source in Grafana. What URL would you typically configure for a Prometheus server running on the same host?",
                "lesson": (
                    "Prometheus' default port is 9090, so the standard data source URL\n"
                    "is http://localhost:9090 (or the service name in Docker/Kubernetes,\n"
                    "e.g., http://prometheus:9090).\n\n"
                    "The connection is from Grafana's backend to Prometheus — not from\n"
                    "the browser. So 'localhost' refers to the Grafana server, not the\n"
                    "user's machine. In Kubernetes, you'd use the service DNS name\n"
                    "like http://prometheus-server.monitoring.svc.cluster.local:9090."
                ),
                "options": [
                    "http://localhost:3000",
                    "http://localhost:9090",
                    "http://localhost:9200",
                    "http://localhost:8080",
                ],
                "answer": "b",
                "hints": [
                    "Port 3000 is Grafana itself. Think about Prometheus' default port.",
                    "Prometheus serves its API and UI on this well-known port.",
                ],
                "xp": 25,
            },
            {
                "id": "graf_8",
                "type": "quiz",
                "title": "Annotations",
                "question": "What is the purpose of annotations in Grafana dashboards?",
                "lesson": (
                    "Annotations are vertical markers on time series panels that mark\n"
                    "specific events: deployments, config changes, incidents, scaling\n"
                    "events.\n\n"
                    "They overlay event context onto metric graphs, letting you correlate\n"
                    "behavior changes with specific actions. 'Latency spiked — oh, there\n"
                    "was a deployment 2 minutes before.'\n\n"
                    "Annotations can come from:\n"
                    "  - Manual entries via the Grafana API\n"
                    "  - CI/CD pipelines (deploy markers)\n"
                    "  - Alert state changes\n"
                    "  - External event sources"
                ),
                "options": [
                    "To add code comments to dashboard JSON for documentation",
                    "To mark events like deployments on time series graphs for correlation",
                    "To annotate specific metric values as anomalous for ML training",
                    "To add text labels to individual data points in a chart",
                ],
                "answer": "b",
                "hints": [
                    "Think about vertical lines on a graph marking 'something happened here.'",
                    "They help correlate metric changes with real-world events.",
                ],
                "xp": 25,
            },
        ],
    },
    # ── ZONE 3: LOG MANAGEMENT ───────────────────────────────────────────
    "log_management": {
        "id": "log_management",
        "name": "The Archive Vault",
        "subtitle": "ELK, Loki, Structured Logging, and the Search for Signal",
        "color": "yellow",
        "icon": "📜",
        "challenges": [
            {
                "id": "log_1",
                "type": "quiz",
                "title": "ELK Stack Components",
                "question": "The ELK stack consists of three components. What does the 'L' stand for?",
                "lesson": (
                    "ELK = Elasticsearch + Logstash + Kibana.\n\n"
                    "  Elasticsearch — distributed search and analytics engine (stores/indexes logs)\n"
                    "  Logstash — server-side data processing pipeline (ingests, transforms, ships)\n"
                    "  Kibana — visualization and exploration UI\n\n"
                    "In modern deployments, Filebeat (a lightweight shipper) often replaces\n"
                    "Logstash for collection, with Logstash handling transformation only.\n"
                    "The stack is sometimes called 'Elastic Stack' now."
                ),
                "options": [
                    "Linux",
                    "Logstash",
                    "Loki",
                    "LogDNA",
                ],
                "answer": "b",
                "hints": [
                    "It's the original pipeline component that processes and ships logs.",
                    "The name suggests it 'stashes' logs somewhere.",
                ],
                "xp": 25,
            },
            {
                "id": "log_2",
                "type": "quiz",
                "title": "Loki vs Elasticsearch",
                "question": "What is the key architectural difference between Grafana Loki and Elasticsearch for log storage?",
                "lesson": (
                    "Loki indexes only metadata (labels) and stores log content as\n"
                    "compressed chunks. Elasticsearch indexes the full text of every\n"
                    "log line.\n\n"
                    "Loki's approach:\n"
                    "  + Much cheaper storage and lower resource usage\n"
                    "  + Simpler operations (less state to manage)\n"
                    "  - Slower for full-text search across all logs\n"
                    "  - Must filter by labels first, then grep within streams\n\n"
                    "Elasticsearch's approach:\n"
                    "  + Fast full-text search across all logs\n"
                    "  - Expensive — indexes are large and resource-hungry\n"
                    "  - Complex to operate (shard management, cluster health)"
                ),
                "options": [
                    "Loki indexes only labels/metadata, not the full log content; Elasticsearch full-text indexes everything",
                    "Loki stores logs in memory; Elasticsearch uses disk",
                    "Loki only works with Grafana; Elasticsearch works with any frontend",
                    "Loki uses SQL queries; Elasticsearch uses its own DSL",
                ],
                "answer": "a",
                "hints": [
                    "Think about what each system indexes — the full text or just labels.",
                    "Loki is often described as 'like Prometheus, but for logs.'",
                ],
                "xp": 25,
            },
            {
                "id": "log_3",
                "type": "quiz",
                "title": "Structured Logging",
                "question": "Why is structured logging (JSON) preferred over plain text logging in production systems?",
                "lesson": (
                    "Structured logs (JSON) can be parsed, indexed, filtered, and\n"
                    "aggregated by machines. Plain text requires regex parsing that is\n"
                    "fragile and expensive.\n\n"
                    "Plain text: 'ERROR 2024-01-15 Connection refused to db-primary port 5432'\n"
                    "Structured: {\"level\":\"error\",\"ts\":\"2024-01-15T...\",\"msg\":\"connection_refused\",\n"
                    "  \"target\":\"db-primary\",\"port\":5432,\"service\":\"api\"}\n\n"
                    "With structured logs you can: filter by service, aggregate error\n"
                    "counts per target, correlate with traces via request_id fields,\n"
                    "and build dashboards — all without writing a single regex."
                ),
                "options": [
                    "Structured logs are smaller in size and cheaper to store",
                    "Structured logs enable machine parsing, filtering, aggregation, and cross-signal correlation",
                    "Structured logs are required by most cloud providers",
                    "Structured logs are easier for humans to read in a terminal",
                ],
                "answer": "b",
                "hints": [
                    "Think about what a log aggregation system can do with key-value pairs.",
                    "Filtering, aggregating, and correlating all require structure.",
                ],
                "xp": 25,
            },
            {
                "id": "log_4",
                "type": "text",
                "title": "Log Levels",
                "question": (
                    "In the standard logging severity hierarchy, which level is MORE\n"
                    "severe: WARN or ERROR?\n\n"
                    "Answer with one word."
                ),
                "lesson": (
                    "The standard severity hierarchy from least to most severe:\n"
                    "  DEBUG → INFO → WARN → ERROR → FATAL/CRITICAL\n\n"
                    "ERROR is more severe than WARN.\n\n"
                    "  DEBUG — detailed diagnostic info, off in production\n"
                    "  INFO — normal operational events (startup, config loaded)\n"
                    "  WARN — something unexpected but recoverable (retrying, fallback)\n"
                    "  ERROR — operation failed, requires attention\n"
                    "  FATAL — application cannot continue\n\n"
                    "In production, the minimum level is usually INFO or WARN.\n"
                    "Enabling DEBUG in production generates enormous volume."
                ),
                "options": [],
                "answer": "error",
                "hints": [
                    "Think about which one indicates a more serious problem.",
                    "A warning is recoverable; the other means something actually failed.",
                ],
                "xp": 30,
            },
            {
                "id": "log_5",
                "type": "quiz",
                "title": "Log Correlation",
                "question": "What field should be included in every log line to enable correlation with distributed traces?",
                "lesson": (
                    "A trace ID (or correlation ID / request ID) links logs to traces.\n\n"
                    "When a request enters your system, it gets assigned a unique trace ID.\n"
                    "Every service that handles the request includes this ID in its log\n"
                    "lines. Now you can:\n\n"
                    "  1. Find a trace showing high latency\n"
                    "  2. Copy the trace ID\n"
                    "  3. Search logs for that ID\n"
                    "  4. See every log line from every service for that request\n\n"
                    "This is the connective tissue between observability pillars.\n"
                    "Without it, logs and traces are separate, uncorrelated data sets."
                ),
                "options": [
                    "The hostname of the server",
                    "A trace ID or correlation ID shared across all services handling the request",
                    "The user's IP address",
                    "The Git commit hash of the deployed code",
                ],
                "answer": "b",
                "hints": [
                    "You need a unique identifier that follows a request across services.",
                    "It should appear in both logs and traces for cross-referencing.",
                ],
                "xp": 25,
            },
            {
                "id": "log_6",
                "type": "quiz",
                "title": "Log Shipping Architecture",
                "question": "In a typical log shipping pipeline, what is the role of a lightweight agent like Filebeat or Promtail?",
                "lesson": (
                    "Lightweight log shippers (Filebeat, Promtail, Fluentbit) run as\n"
                    "agents on each node. They:\n\n"
                    "  - Tail log files and collect new entries\n"
                    "  - Add metadata (hostname, container name, labels)\n"
                    "  - Buffer data locally to handle downstream outages\n"
                    "  - Ship logs to a central aggregator (Elasticsearch, Loki, etc.)\n\n"
                    "They are intentionally lightweight — minimal CPU/memory footprint —\n"
                    "unlike Logstash which is a heavy JVM-based processing pipeline.\n"
                    "The pattern is: lightweight shipper → optional pipeline → storage."
                ),
                "options": [
                    "To parse and transform log formats into structured JSON",
                    "To collect log files from each node and ship them to a central store with minimal resource usage",
                    "To replace Elasticsearch as the primary log storage backend",
                    "To aggregate logs in memory and serve queries directly to users",
                ],
                "answer": "b",
                "hints": [
                    "The key word is 'lightweight' — minimal footprint on each node.",
                    "They collect and forward, not process or store.",
                ],
                "xp": 25,
            },
            {
                "id": "log_7",
                "type": "quiz",
                "title": "Log Retention",
                "question": "Your logging system ingests 500 GB/day. Storage costs are rising. What is the most effective strategy to reduce costs while preserving debugging capability?",
                "lesson": (
                    "Tiered retention is the standard approach:\n\n"
                    "  Hot tier (0-7 days) — full resolution, fast queries, expensive storage\n"
                    "  Warm tier (7-30 days) — full resolution, slower queries, cheaper storage\n"
                    "  Cold tier (30-90 days) — sampled or aggregated, archive storage\n"
                    "  Delete after 90 days (unless compliance requires longer)\n\n"
                    "Combined with:\n"
                    "  - Drop DEBUG/TRACE level logs at the pipeline level\n"
                    "  - Sample high-volume, low-value log streams\n"
                    "  - Compress older logs\n\n"
                    "Never keep all logs at full resolution forever. The cost is exponential."
                ),
                "options": [
                    "Delete all logs older than 24 hours",
                    "Implement tiered retention — hot/warm/cold storage with decreasing resolution over time",
                    "Switch all logging to DEBUG level for maximum detail",
                    "Store all logs indefinitely but compress them",
                ],
                "answer": "b",
                "hints": [
                    "Think about keeping recent logs readily available and archiving older ones.",
                    "Different ages of data need different storage tiers and access speeds.",
                ],
                "xp": 25,
            },
            {
                "id": "log_8",
                "type": "text",
                "title": "LogQL Basics",
                "question": (
                    "In Grafana Loki, you query logs using LogQL. A basic query starts\n"
                    "with a log stream selector in curly braces.\n\n"
                    "To find all logs from the 'api' service, you write:\n"
                    "  {service=\"api\"}\n\n"
                    "To then filter for lines containing the word 'error', what\n"
                    "operator do you pipe to? Answer with the operator symbol(s) only.\n\n"
                    "Hint: {service=\"api\"} ___ \"error\""
                ),
                "lesson": (
                    "The |= operator in LogQL is a line filter that keeps only lines\n"
                    "containing the specified string:\n\n"
                    "  {service=\"api\"} |= \"error\"\n\n"
                    "LogQL line filters:\n"
                    "  |=  contains string\n"
                    "  !=  does not contain string\n"
                    "  |~  matches regex\n"
                    "  !~  does not match regex\n\n"
                    "LogQL's design is intentional: first select streams by label\n"
                    "(cheap, indexed lookup), then filter within those streams\n"
                    "(sequential scan). This is why Loki is cheaper than Elasticsearch —\n"
                    "it only scans the streams you select."
                ),
                "options": [],
                "answer": "|=",
                "hints": [
                    "It's a two-character operator: a pipe symbol followed by something.",
                    "The pipe | plus equals = makes a 'contains' filter.",
                ],
                "xp": 30,
            },
        ],
    },
    # ── ZONE 4: ALERTING & ON-CALL ───────────────────────────────────────
    "alerting_oncall": {
        "id": "alerting_oncall",
        "name": "The Signal Tower",
        "subtitle": "PagerDuty, Runbooks, SLOs, and the War on Alert Fatigue",
        "color": "red",
        "icon": "🚨",
        "challenges": [
            {
                "id": "alert_1",
                "type": "quiz",
                "title": "Alert Fatigue",
                "question": "An on-call engineer received 400 alerts last week. Only 11 required action. What is this problem called?",
                "lesson": (
                    "Alert fatigue is the desensitization that occurs when engineers\n"
                    "receive too many non-actionable alerts. The consequences are severe:\n\n"
                    "  - Engineers start ignoring alerts (auto-archive, mute channels)\n"
                    "  - Real incidents get lost in the noise\n"
                    "  - On-call burnout leads to attrition\n"
                    "  - MTTR increases because nobody trusts the pager\n\n"
                    "The fix: every alert must be actionable. If it doesn't require\n"
                    "a human to do something RIGHT NOW, it's a dashboard metric,\n"
                    "not a page. Delete the alert."
                ),
                "options": [
                    "Alert fatigue",
                    "Signal degradation",
                    "Monitoring debt",
                    "Incident inflation",
                ],
                "answer": "a",
                "hints": [
                    "It's named after the human response to being overwhelmed by warnings.",
                    "The word 'fatigue' describes exhaustion from repetitive stimulation.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_2",
                "type": "quiz",
                "title": "SLIs, SLOs, and SLAs",
                "question": "What is the correct relationship between SLI, SLO, and SLA?",
                "lesson": (
                    "SLI (Service Level Indicator) — a metric that measures service quality.\n"
                    "  Example: the proportion of requests completing in < 200ms.\n\n"
                    "SLO (Service Level Objective) — a target value for an SLI.\n"
                    "  Example: 99.9% of requests complete in < 200ms.\n\n"
                    "SLA (Service Level Agreement) — a contract with consequences.\n"
                    "  Example: if we fail the SLO, the customer gets a credit.\n\n"
                    "The relationship: SLI is WHAT you measure, SLO is the TARGET\n"
                    "you set, SLA is the PROMISE (with penalties) you make externally."
                ),
                "options": [
                    "SLI is the metric, SLO is the target for that metric, SLA is a contract with consequences for missing the SLO",
                    "SLI is the alert rule, SLO is the escalation policy, SLA is the runbook",
                    "SLI and SLO are the same thing; SLA is the legal version",
                    "SLA defines the metric, SLO defines the measurement method, SLI is the report",
                ],
                "answer": "a",
                "hints": [
                    "Think: what do you MEASURE, what do you TARGET, what do you PROMISE.",
                    "Indicators indicate, Objectives set goals, Agreements have consequences.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_3",
                "type": "quiz",
                "title": "Error Budgets",
                "question": "Your SLO is 99.9% availability. In a 30-day month, how much downtime does your error budget allow?",
                "lesson": (
                    "Error budget = 1 - SLO target.\n\n"
                    "99.9% availability = 0.1% allowed downtime.\n"
                    "30 days = 43,200 minutes.\n"
                    "0.1% of 43,200 = 43.2 minutes.\n\n"
                    "The error budget is the mathematical framework that balances\n"
                    "reliability and velocity. When the budget is healthy, ship fast.\n"
                    "When it's burning, slow down and fix reliability.\n\n"
                    "  99%    = 7.2 hours/month (aggressive for most services)\n"
                    "  99.9%  = 43.2 minutes/month\n"
                    "  99.99% = 4.3 minutes/month (extremely tight)"
                ),
                "options": [
                    "4.3 minutes",
                    "43.2 minutes",
                    "7.2 hours",
                    "0 minutes — 99.9% means no downtime",
                ],
                "answer": "b",
                "hints": [
                    "Calculate: 30 days * 24 hours * 60 minutes * 0.001.",
                    "0.1% of total minutes in a 30-day month.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_4",
                "type": "quiz",
                "title": "PagerDuty Escalation",
                "question": "In PagerDuty, what happens when an incident is not acknowledged within the configured timeout?",
                "lesson": (
                    "PagerDuty escalation policies define what happens when an alert\n"
                    "isn't acknowledged:\n\n"
                    "  1. Alert fires → Primary on-call is paged\n"
                    "  2. Acknowledgment timeout (e.g., 5 min) → escalate to next level\n"
                    "  3. Next level timeout → escalate again (manager, team lead, etc.)\n\n"
                    "Escalation ensures no alert falls through the cracks. Even if the\n"
                    "primary on-call is asleep/unavailable, someone gets paged.\n\n"
                    "Best practice: 3 escalation levels max. If nobody responds after 3,\n"
                    "you have a staffing problem, not a tooling problem."
                ),
                "options": [
                    "The alert is automatically resolved and closed",
                    "The alert is escalated to the next person or level in the escalation policy",
                    "The alert is moved to a low-priority queue for business hours",
                    "PagerDuty sends an email summary but takes no further action",
                ],
                "answer": "b",
                "hints": [
                    "Think about what 'escalation policy' means when someone doesn't respond.",
                    "The goal is to ensure SOMEONE handles the incident.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_5",
                "type": "text",
                "title": "Runbook Purpose",
                "question": (
                    "A document that provides step-by-step instructions for responding\n"
                    "to a specific alert or incident scenario is called a ____.\n\n"
                    "Answer with one word."
                ),
                "lesson": (
                    "A runbook is a documented procedure for responding to an alert\n"
                    "or operational scenario. Every actionable alert should link to one.\n\n"
                    "A good runbook contains:\n"
                    "  - What this alert means (not just the metric)\n"
                    "  - Impact assessment steps\n"
                    "  - Immediate mitigation actions\n"
                    "  - Diagnostic steps to find root cause\n"
                    "  - Escalation criteria (when to wake up more people)\n"
                    "  - Post-mitigation cleanup steps\n\n"
                    "Runbooks are the difference between 'I got paged and panicked'\n"
                    "and 'I got paged and followed the procedure.'"
                ),
                "options": [],
                "answer": "runbook",
                "hints": [
                    "The name literally describes a book of procedures you 'run' through.",
                    "It's a standard term in incident management and SRE.",
                ],
                "xp": 30,
            },
            {
                "id": "alert_6",
                "type": "quiz",
                "title": "Burn Rate Alerts",
                "question": "What is a 'burn rate' in the context of SLO-based alerting?",
                "lesson": (
                    "Burn rate measures how fast you're consuming your error budget\n"
                    "relative to the SLO window.\n\n"
                    "  Burn rate 1x = consuming budget at the exact rate that would\n"
                    "  exhaust it by the end of the window (barely making SLO).\n"
                    "  Burn rate 10x = consuming budget 10x faster than sustainable.\n\n"
                    "SLO-based alerting uses burn rates instead of raw thresholds:\n"
                    "  - Burn rate > 14x for 2 min → page immediately (fast burn)\n"
                    "  - Burn rate > 6x for 30 min → page (medium burn)\n"
                    "  - Burn rate > 1x for 6 hours → ticket (slow burn)\n\n"
                    "This approach dramatically reduces false positives compared to\n"
                    "simple threshold alerts."
                ),
                "options": [
                    "The rate at which alert notifications are sent per hour",
                    "The rate at which the error budget is being consumed relative to the SLO window",
                    "The CPU burn rate of the monitoring system itself",
                    "The rate at which on-call engineers experience burnout",
                ],
                "answer": "b",
                "hints": [
                    "Think about 'burning through' a budget — how fast is it being spent.",
                    "It's relative to the total error budget for the SLO period.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_7",
                "type": "quiz",
                "title": "Alert Routing",
                "question": "You want critical database alerts to page the DBA team and non-critical ones to go to a Slack channel. How should this be configured in Alertmanager?",
                "lesson": (
                    "Alertmanager routes alerts based on label matching:\n\n"
                    "  route:\n"
                    "    receiver: default-slack\n"
                    "    routes:\n"
                    "      - match:\n"
                    "          team: dba\n"
                    "          severity: critical\n"
                    "        receiver: dba-pagerduty\n"
                    "      - match:\n"
                    "          team: dba\n"
                    "          severity: warning\n"
                    "        receiver: dba-slack\n\n"
                    "Labels on alerts (team, severity, service, env) drive the routing.\n"
                    "Good label hygiene on alerts is critical — without consistent labels,\n"
                    "routing rules become fragile spaghetti."
                ),
                "options": [
                    "Create separate Alertmanager instances for each team",
                    "Use routing rules in Alertmanager that match on labels like severity and team",
                    "Have each team write their own Prometheus alert rules with hardcoded receivers",
                    "Use a custom webhook that reads the alert text and decides where to send it",
                ],
                "answer": "b",
                "hints": [
                    "Alertmanager has a built-in routing tree based on label matchers.",
                    "Labels like 'severity' and 'team' determine which receiver gets the alert.",
                ],
                "xp": 25,
            },
            {
                "id": "alert_8",
                "type": "quiz",
                "title": "On-Call Best Practices",
                "question": "Which practice most effectively reduces on-call burnout while maintaining incident response quality?",
                "lesson": (
                    "On-call rotation best practices:\n\n"
                    "  - Rotate frequently (weekly, not monthly)\n"
                    "  - Follow-the-sun across time zones when possible\n"
                    "  - Compensate on-call time (money or time off)\n"
                    "  - Every page must be actionable (reduce noise first)\n"
                    "  - Blameless postmortems after major incidents\n"
                    "  - Runbooks for every alert\n"
                    "  - Primary + secondary on-call for escalation\n\n"
                    "The single most impactful change is reducing alert noise.\n"
                    "An engineer paged 5 times for real issues is fine. An engineer\n"
                    "paged 50 times for noise burns out in weeks."
                ),
                "options": [
                    "Assign one dedicated engineer to permanent on-call duty",
                    "Reduce alert noise so every page is actionable, rotate frequently, and compensate on-call time",
                    "Disable all alerts during weekends and holidays",
                    "Route all alerts to a Slack channel instead of paging",
                ],
                "answer": "b",
                "hints": [
                    "Burnout comes from noise and lack of rest, not from real incidents.",
                    "The answer combines multiple practices: noise reduction, rotation, and compensation.",
                ],
                "xp": 25,
            },
        ],
    },
    # ── ZONE 5: APM & PROFILING ──────────────────────────────────────────
    "apm_profiling": {
        "id": "apm_profiling",
        "name": "The Deep Scan",
        "subtitle": "Datadog, New Relic, Flame Graphs, and Distributed Tracing",
        "color": "magenta",
        "icon": "🔬",
        "challenges": [
            {
                "id": "apm_1",
                "type": "quiz",
                "title": "What is APM?",
                "question": "What does APM stand for in the context of application monitoring?",
                "lesson": (
                    "APM = Application Performance Monitoring (or Management).\n\n"
                    "APM tools (Datadog APM, New Relic, Dynatrace, Elastic APM) provide:\n\n"
                    "  - Service maps — visual topology of service dependencies\n"
                    "  - Distributed traces — follow requests across services\n"
                    "  - Error tracking — aggregate and classify exceptions\n"
                    "  - Performance metrics — latency, throughput, error rate per endpoint\n"
                    "  - Code-level visibility — slow queries, N+1s, memory leaks\n\n"
                    "APM goes beyond infrastructure metrics to measure application\n"
                    "behavior from the user's perspective."
                ),
                "options": [
                    "Application Performance Monitoring",
                    "Automated Process Management",
                    "Application Permission Model",
                    "Alert Priority Matrix",
                ],
                "answer": "a",
                "hints": [
                    "The 'P' stands for Performance — monitoring how well your app performs.",
                    "It's a well-known industry term used by Datadog, New Relic, and others.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_2",
                "type": "quiz",
                "title": "Distributed Tracing Concepts",
                "question": "In distributed tracing, what is a 'span'?",
                "lesson": (
                    "A span represents a single unit of work within a trace.\n\n"
                    "A trace is the full journey of a request. A span is one step in\n"
                    "that journey: one service call, one database query, one cache lookup.\n\n"
                    "Each span contains:\n"
                    "  - Operation name (e.g., 'GET /api/users')\n"
                    "  - Start time and duration\n"
                    "  - Parent span ID (creates the tree structure)\n"
                    "  - Tags/attributes (http.status_code, db.statement, etc.)\n"
                    "  - Status (OK, ERROR)\n\n"
                    "Spans nest: a parent span (API call) contains child spans\n"
                    "(auth check, DB query, cache write)."
                ),
                "options": [
                    "The total end-to-end latency of a request",
                    "A single unit of work within a trace, representing one operation",
                    "The network hop between two services",
                    "A sampling window for collecting trace data",
                ],
                "answer": "b",
                "hints": [
                    "Think of a trace as a tree — each node in the tree is one of these.",
                    "It has a start time, duration, and parent-child relationship.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_3",
                "type": "quiz",
                "title": "Flame Graphs",
                "question": "What does the WIDTH of a bar in a flame graph represent?",
                "lesson": (
                    "In a flame graph, the width of a bar represents the amount of\n"
                    "time (or samples) spent in that function.\n\n"
                    "  Width = time/samples in that function (wider = more time)\n"
                    "  Height = call stack depth (taller = deeper call chain)\n"
                    "  Color = usually arbitrary or based on package/module\n\n"
                    "To find performance bottlenecks: look for wide bars (functions\n"
                    "consuming lots of time) and 'plateaus' (wide, flat tops where\n"
                    "the function itself is doing work, not calling sub-functions).\n\n"
                    "Flame graphs were invented by Brendan Gregg and are the single\n"
                    "most effective tool for understanding CPU profiles."
                ),
                "options": [
                    "The amount of memory allocated by the function",
                    "The number of times the function was called",
                    "The amount of time (or samples) spent in that function",
                    "The depth of the function in the call stack",
                ],
                "answer": "c",
                "hints": [
                    "Wider means the function consumed more of the profiled resource.",
                    "In CPU flame graphs, width represents time on CPU.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_4",
                "type": "text",
                "title": "Context Propagation",
                "question": (
                    "In distributed tracing, trace context is passed between services\n"
                    "via HTTP. The W3C standard header for propagating trace context\n"
                    "is called:\n\n"
                    "Answer with the exact header name (lowercase, with hyphen)."
                ),
                "lesson": (
                    "The W3C Trace Context standard defines the 'traceparent' header\n"
                    "for propagating trace context across service boundaries.\n\n"
                    "Format: traceparent: 00-<trace-id>-<parent-span-id>-<flags>\n"
                    "Example: traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01\n\n"
                    "Before W3C standardization, each vendor had its own header:\n"
                    "  Zipkin: X-B3-TraceId\n"
                    "  Jaeger: uber-trace-id\n"
                    "  AWS: X-Amzn-Trace-Id\n\n"
                    "OpenTelemetry uses the W3C standard by default, enabling\n"
                    "interoperability across vendors and languages."
                ),
                "options": [],
                "answer": "traceparent",
                "hints": [
                    "It's a W3C standard header — think about what a child span needs from its parent.",
                    "The header name describes the relationship: trace + parent.",
                ],
                "xp": 30,
            },
            {
                "id": "apm_5",
                "type": "quiz",
                "title": "Datadog vs New Relic",
                "question": "Both Datadog and New Relic are commercial APM platforms. What is the fundamental pricing model difference that most impacts cost?",
                "lesson": (
                    "Pricing models for APM vendors:\n\n"
                    "  Datadog — charges per host + per ingested metric/span/log volume.\n"
                    "  New Relic — charges per ingested GB of data (data-plus model)\n"
                    "  plus per full-platform user.\n\n"
                    "The key cost driver in both is data volume. More services, more\n"
                    "traces, more custom metrics = higher bills.\n\n"
                    "Cost control strategies:\n"
                    "  - Sample traces (keep 100% of errors, sample success)\n"
                    "  - Control custom metric cardinality\n"
                    "  - Set log ingestion limits\n"
                    "  - Use head-based or tail-based sampling"
                ),
                "options": [
                    "Datadog charges per host; New Relic charges primarily per ingested data volume and user seats",
                    "Datadog is free for small teams; New Relic requires an enterprise license",
                    "Datadog only supports cloud; New Relic supports on-premises",
                    "There is no significant pricing difference — both charge per user",
                ],
                "answer": "a",
                "hints": [
                    "One charges based on infrastructure size, the other on data volume.",
                    "Think about what drives the bill up in each platform.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_6",
                "type": "quiz",
                "title": "Trace Sampling",
                "question": "What is the difference between head-based and tail-based trace sampling?",
                "lesson": (
                    "Head-based sampling: the decision to sample a trace is made at\n"
                    "the START (the 'head') of the request. The first service decides\n"
                    "randomly, and all downstream services respect that decision.\n"
                    "  + Simple, low overhead\n"
                    "  - May discard interesting traces (errors, slow requests)\n\n"
                    "Tail-based sampling: ALL spans are collected, and the decision\n"
                    "is made AFTER the trace completes (at the 'tail').\n"
                    "  + Can keep all errors, all slow traces, sample the rest\n"
                    "  - Requires a collector that buffers complete traces\n"
                    "  - Higher resource usage\n\n"
                    "Tail-based is better for quality but harder to implement.\n"
                    "OpenTelemetry Collector supports both strategies."
                ),
                "options": [
                    "Head-based decides at request start; tail-based decides after the trace completes, allowing decisions based on outcome",
                    "Head-based samples HTTP headers; tail-based samples response bodies",
                    "Head-based runs on the client; tail-based runs on the server",
                    "They are different names for the same sampling approach",
                ],
                "answer": "a",
                "hints": [
                    "Think about WHEN the sampling decision is made: beginning vs end.",
                    "One can't know if a request was slow/errored; the other can.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_7",
                "type": "quiz",
                "title": "Service Maps",
                "question": "An APM service map shows your microservices with arrows between them. One arrow is thick and red. What does this typically indicate?",
                "lesson": (
                    "Service maps in APM tools visualize service dependencies and health:\n\n"
                    "  Arrow direction — shows which service calls which\n"
                    "  Arrow thickness — proportional to request volume\n"
                    "  Arrow/node color — indicates health (green=healthy, red=errors)\n\n"
                    "A thick red arrow means: high traffic AND high error rate on\n"
                    "that service-to-service path.\n\n"
                    "Service maps are the first place to look during an incident.\n"
                    "They immediately show you which services are affected and which\n"
                    "dependencies are failing — without you needing to know the\n"
                    "architecture in advance."
                ),
                "options": [
                    "The network connection between those services is encrypted",
                    "High request volume with a high error rate on that service-to-service connection",
                    "The service was recently deployed",
                    "The service is using more CPU than its allocation",
                ],
                "answer": "b",
                "hints": [
                    "Thickness represents traffic volume; color represents health/errors.",
                    "Red typically indicates problems — errors, failures, or degradation.",
                ],
                "xp": 25,
            },
            {
                "id": "apm_8",
                "type": "quiz",
                "title": "Continuous Profiling",
                "question": "What is 'continuous profiling' and why is it different from on-demand profiling?",
                "lesson": (
                    "On-demand profiling: you attach a profiler to a process when you\n"
                    "suspect a problem. You get a snapshot of what's happening NOW.\n\n"
                    "Continuous profiling: a low-overhead profiler runs ALL THE TIME\n"
                    "in production. Every minute, it captures a CPU/memory/allocation\n"
                    "profile and stores it with timestamps.\n\n"
                    "Tools: Datadog Continuous Profiler, Pyroscope, Parca, Google Cloud Profiler.\n\n"
                    "The killer feature: you can compare profiles BEFORE and AFTER\n"
                    "a deployment. 'This function went from 5% to 40% of CPU after\n"
                    "yesterday's release.' You can't do that with on-demand profiling\n"
                    "because you don't have the 'before' snapshot."
                ),
                "options": [
                    "Continuous profiling only runs in staging; on-demand runs in production",
                    "Continuous profiling captures profiles constantly in production, enabling comparison across time and deployments",
                    "Continuous profiling is cheaper because it uses sampling",
                    "They are the same thing — continuous is just a marketing term",
                ],
                "answer": "b",
                "hints": [
                    "The key differentiator is ALWAYS running vs. running when you choose to.",
                    "Think about comparing performance before and after a change.",
                ],
                "xp": 25,
            },
        ],
    },
}
