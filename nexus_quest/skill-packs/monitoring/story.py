"""
story.py - Narrative text for Monitoring skill pack (The Watchtower)
Theme: The tower sees all. Every metric, every log, every trace — if you know where to look.
CIPHER cyberpunk narrative.
"""

INTRO_STORY = """
The tower was always there. You just couldn't see it.

[bold white]Buried in the infrastructure of the Ninth Sector, behind firewalls
and forgotten DNS entries, the Watchtower was the corp's original monitoring
system. Built by the first generation of site reliability engineers before
they were called that. Before dashboards. Before SLOs. Before the pager
became a way of life.[/bold white]

It was supposed to see everything. Every metric. Every log. Every trace.
Every anomaly in every service across every region. A single pane of glass
for an empire of microservices.

Then they stopped maintaining it.

The Prometheus instances drifted out of sync. The Grafana dashboards filled
with "No Data" panels. The Alertmanager fired so many false positives that
the on-call team auto-archived the channel. The ELK cluster ran out of disk
and started dropping logs silently.

[bold magenta]The system was still running. The users were still experiencing errors.
And the Watchtower was blind.[/bold magenta]

Three days ago, a silent failure in the payment service cost the corp
$2.3 million. No alert fired. No dashboard turned red. No log was indexed.
The failure was discovered when a customer tweeted about it.

[bold white]You've been brought in to rebuild the Watchtower from the ground up.[/bold white]

Prometheus. Grafana. Loki. PagerDuty. Datadog. Every tool in the monitoring
arsenal. Every signal from every service. Collected, correlated, visualized,
and alerted on — correctly this time.

The tower must see everything. And this time, it will.

[bold cyan]The signal is out there. Climb the tower. Learn to see.[/bold cyan]
"""

ZONE_INTROS = {
    "prometheus_promql": """
[bold cyan]== THE METRIC FORGE ==[/bold cyan]

The foundation of the Watchtower is metrics. Numbers. Time series. The
heartbeat of every service rendered as counters, gauges, and histograms.

Prometheus sits at the center — pulling metrics from every service, every
node, every exporter. But Prometheus is only as good as the queries you
write against it. PromQL is the language of the Metric Forge. Learn it,
and the numbers speak. Fail, and you're staring at graphs that mean nothing.

The corp's Prometheus cluster is running. Barely. Twelve exporters, three
broken. Scrape intervals misconfigured. Retention set to 15 days on a
disk that holds 7. The counters are counting, but nobody knows what
they're counting or why.

[yellow]Prometheus[/yellow] — pull-based metrics collection and time-series storage.
[yellow]PromQL[/yellow] — the query language for slicing and dicing time-series data.
[yellow]Metric types[/yellow] — counter, gauge, histogram, summary — each for a different purpose.
[yellow]Service discovery[/yellow] — how Prometheus finds what to scrape.

[italic]"A metric without a query is just a number. A query
without understanding is just noise."[/italic]
""",
    "grafana_dashboards": """
[bold cyan]== THE GLASS WALL ==[/bold cyan]

The metrics are flowing. Now you need eyes.

Grafana is the Glass Wall — the visualization layer that turns raw
time series into something a human brain can process at 3 AM with
one eye open and coffee going cold.

The corp has forty-seven Grafana dashboards. Thirty show "No Data."
Ten show metrics nobody remembers defining. Seven actually work, but
they're all owned by one engineer who left six months ago and nobody
knows how to edit them.

You're going to tear them down and rebuild. Fewer dashboards. Better
panels. Template variables so one dashboard serves twenty services.
Annotations that mark deployments. Alerts that actually mean something.

[yellow]Panels[/yellow] — time series, stat, gauge, heatmap, table — choose wisely.
[yellow]Variables[/yellow] — template dropdowns that make dashboards reusable.
[yellow]Annotations[/yellow] — event markers that correlate deployments with behavior changes.
[yellow]Alerting[/yellow] — Grafana and Alertmanager working together.

[italic]"A dashboard that lies is worse than no dashboard.
The Glass Wall must be transparent — or it's just a wall."[/italic]
""",
    "log_management": """
[bold cyan]== THE ARCHIVE VAULT ==[/bold cyan]

Metrics tell you WHAT is happening. Logs tell you WHY.

The corp's logging situation is dire. Five hundred gigabytes of unstructured
plain text per day, scattered across a hundred nodes. The only search tool
is SSH and grep. The ELK cluster crashed three weeks ago and nobody noticed
because the alerts for the alerting system were also broken.

You're going to rebuild the logging pipeline. Structured JSON. Centralized
storage. Indexed, searchable, filterable. Loki for the cost-conscious
services. Elasticsearch for the ones that need full-text search. Correlation
IDs in every line so logs connect to traces connect to metrics.

The Archive Vault holds every secret of what happened and why. But only
if you can read it.

[yellow]ELK Stack[/yellow] — Elasticsearch, Logstash, Kibana for full-text log search.
[yellow]Grafana Loki[/yellow] — label-indexed log aggregation, like Prometheus but for logs.
[yellow]Structured logging[/yellow] — JSON key-value pairs instead of plain text.
[yellow]Log correlation[/yellow] — trace IDs that connect logs to distributed traces.

[italic]"An unstructured log is a message in a bottle. It might
reach the right shore. It probably won't."[/italic]
""",
    "alerting_oncall": """
[bold cyan]== THE SIGNAL TOWER ==[/bold cyan]

The metrics are flowing. The dashboards are live. The logs are structured.
Now comes the hardest part: deciding what to SCREAM about.

The corp's on-call engineer received four hundred and twelve alerts last
week. Eleven required action. The rest were noise. The engineer before
this one quit. The one before that transferred teams. The current one
has a Slack filter that auto-archives everything from Alertmanager.

This is alert fatigue. It is the single most dangerous failure mode in
operational practice. When every alert is noise, no alert is signal.
The $2.3 million payment failure? An alert existed for it. It was
auto-archived along with the other 401 noise alerts that week.

You're rebuilding alerting from SLOs down. Define what matters. Set
error budgets. Alert on burn rate, not raw thresholds. Every alert
gets a runbook. Every page requires action. Everything else is a
dashboard, not a page.

[yellow]SLIs / SLOs / SLAs[/yellow] — what you measure, what you target, what you promise.
[yellow]Error budgets[/yellow] — the math that balances reliability and velocity.
[yellow]PagerDuty[/yellow] — incident routing, escalation, and on-call management.
[yellow]Runbooks[/yellow] — step-by-step procedures that make 3 AM survivable.

[italic]"If an alert doesn't require immediate human action,
delete it. Your on-call engineers' sanity depends on it."[/italic]
""",
    "apm_profiling": """
[bold cyan]== THE DEEP SCAN ==[/bold cyan]

The Watchtower sees the surface. Metrics, logs, dashboards, alerts.
But some problems hide deeper. Inside the code. Inside the runtime.
Inside the distributed call chain where a single slow database query
cascades into a timeout that cascades into a retry storm that takes
down the entire checkout flow.

APM — Application Performance Monitoring — sees what infrastructure
monitoring can't. It instruments the code itself. Every function call.
Every database query. Every HTTP request between services. Traced,
timed, and stored.

Datadog. New Relic. Dynatrace. Elastic APM. OpenTelemetry feeding
Jaeger or Tempo. The tools differ. The principle is the same: follow
the request from the edge to the database and back, and measure
everything along the way.

Flame graphs show you where your code spends its time. Service maps
show you which services talk to which. Continuous profiling compares
performance before and after every deploy.

[yellow]Distributed tracing[/yellow] — follow requests across service boundaries.
[yellow]Flame graphs[/yellow] — visualize CPU/memory usage by function call path.
[yellow]Service maps[/yellow] — topology view of service dependencies and health.
[yellow]Continuous profiling[/yellow] — always-on performance snapshots for comparison.

[italic]"The dashboard says latency is high. The trace says where.
The flame graph says why. You need all three."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "prometheus_promql": """
[bold green]THE METRIC FORGE — OPERATIONAL.[/bold green]

Prometheus is scraping. The exporters are healthy. PromQL queries return
meaningful data. Counters, gauges, histograms — you know which type for
which purpose. Service discovery finds new pods automatically.

The metrics pipeline is the heartbeat of the Watchtower. It beats steady now.

[bold cyan]The Glass Wall is next. Time to give the metrics eyes.[/bold cyan]
""",
    "grafana_dashboards": """
[bold green]THE GLASS WALL — TRANSPARENT.[/bold green]

Forty-seven broken dashboards replaced with twelve that work. Template
variables. Meaningful panels. Annotations marking every deployment.
Heatmaps showing latency distributions. Stat panels for the KPIs.

The Glass Wall shows truth now. No more "No Data." No more lies.

[bold cyan]The Archive Vault awaits. Time to make the logs searchable.[/bold cyan]
""",
    "log_management": """
[bold green]THE ARCHIVE VAULT — INDEXED.[/bold green]

Structured JSON. Correlation IDs. Centralized in Loki and Elasticsearch.
Searchable, filterable, aggregatable. Log levels enforced. Retention
tiered. The grep-and-SSH days are over.

A single query now finds every log line from every service for any request.

[bold cyan]The Signal Tower. Time to decide what deserves a page.[/bold cyan]
""",
    "alerting_oncall": """
[bold green]THE SIGNAL TOWER — CALIBRATED.[/bold green]

Four hundred alerts per week down to fourteen. Every one actionable. Every
one linked to a runbook. Every one backed by an SLO and error budget.
Burn rate alerts instead of raw thresholds. Escalation policies that work.

The on-call engineer un-muted Slack. The $2.3 million silent failure
can never happen again.

[bold cyan]The Deep Scan. Time to look inside the code itself.[/bold cyan]
""",
    "apm_profiling": """
[bold yellow]★ ★ ★  THE DEEP SCAN — COMPLETE.  ★ ★ ★[/bold yellow]

[bold white]The Watchtower is rebuilt.[/bold white]

Prometheus scrapes every service. Grafana renders every metric. Loki indexes
every log. Alertmanager routes every alert. PagerDuty pages the right person.
Datadog traces every request. Flame graphs expose every bottleneck.

The silent $2.3 million failure? The system that allowed it no longer exists.
In its place: a Watchtower that sees every metric, every log, every trace,
every anomaly across every service in every region.

[bold magenta]The tower stands. The signals flow. Nothing hides in the dark anymore.
Every request leaves a trail. Every failure triggers a response. Every
on-call engineer has a runbook. Every dashboard tells the truth.[/bold magenta]

[bold yellow]WATCHTOWER OPERATIVE: TOWER KEEPER. MONITORING: COMPLETE.[/bold yellow]
""",
}

BOSS_INTROS = {
    "prometheus_promql": "[bold red]⚠  FORGE TRIAL: The PromQL Gauntlet[/bold red]\nThe metrics are flowing. Prove you can query them under pressure.",
    "grafana_dashboards": "[bold red]⚠  GLASS TRIAL: The Dashboard Audit[/bold red]\nForty-seven dashboards. Prove you know which panels, variables, and practices matter.",
    "log_management": "[bold red]⚠  VAULT TRIAL: The Log Investigation[/bold red]\nFive hundred GB per day. Prove you can structure, search, and correlate them.",
    "alerting_oncall": "[bold red]⚠  TOWER TRIAL: The On-Call Simulation[/bold red]\nThe pager is live. Four hundred alerts. Prove you know which ones matter.",
    "apm_profiling": "[bold red]★  DEEP TRIAL: The Performance Investigation[/bold red]\nLatency spiked. The trace is waiting. Prove you can follow it to root cause.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_signal":         ("First Watch", "Read your first signal from the Watchtower. The tower acknowledged your presence."),
    "forge_master":         ("Forge Master", "Cleared The Metric Forge. Prometheus, PromQL, counters, gauges, histograms — the metrics speak to you now."),
    "glass_keeper":         ("Glass Keeper", "Cleared The Glass Wall. Dashboards that tell the truth. Panels that matter. Variables that scale."),
    "vault_archivist":      ("Vault Archivist", "Cleared The Archive Vault. Structured, indexed, correlated. The logs yield their secrets."),
    "signal_commander":     ("Signal Commander", "Cleared The Signal Tower. Every alert actionable. Every page backed by a runbook. Alert fatigue: eliminated."),
    "deep_scanner":         ("Deep Scanner", "Cleared The Deep Scan. Traces followed. Flame graphs read. Performance bottlenecks exposed."),
    "streak_3":             ("Locked On", "3 correct in a row. The Watchtower is tuning to your frequency."),
    "streak_5":             ("Clear Signal", "5 in a row. The noise is gone. Only signal remains."),
    "streak_10":            ("PERFECT WATCH", "10 in a row. The tower bends to your will. Every signal, read perfectly."),
    "no_hints":             ("Unaided Watch", "Cleared a zone without hints. Your eyes were sharp enough alone."),
    "speed_demon":          ("Instant Read", "Answered in under 5 seconds. The signal was read before the question finished."),
    "level_10":             ("Junior Watcher", "Level 10. The dashboards are starting to make sense at a glance."),
    "level_20":             ("Senior Watcher", "Level 20. You read flame graphs the way other people read email."),
    "level_30":             ("Tower Keeper", "Maximum level. The Watchtower is yours. Every signal, every service, every trace — seen."),
    "completionist":        ("All-Seeing Eye", "Every zone. Every challenge. Total monitoring mastery achieved."),
    "boss_slayer":          ("Trial Survivor", "Beat your first boss challenge. The noise tried to hide the signal. It failed."),
}
