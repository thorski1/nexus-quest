"""
story.py - Narrative text for Observability skill pack (Signal Corps)
Theme: You can't fix what you can't see. The signals are everywhere — learn to read them.
"""

INTRO_STORY = """
The dashboard went dark at [bold cyan]2:47 AM[/bold cyan].

[bold white]Not an outage. Worse.[/bold white] The system was still running. Requests were still
flowing. But the metrics stopped updating. The logs stopped shipping.
The traces stopped correlating. Somewhere between the application and
the observability stack, every signal went silent.

The services were up. The users were experiencing errors. And nobody
could see a thing.

By the time the on-call engineer SSH'd into a production node and tailed
the raw logs, forty-three minutes had passed. Forty-three minutes of
degraded service, failed payments, and angry users — invisible to every
dashboard, every alert, every automated response.

[bold white]You are a Signal Corps operative.[/bold white]

[bold magenta]The corp that hired you doesn't have a monitoring problem. They have an
observability problem. Their dashboards show green when the system is on fire.
Their alerts fire for things that don't matter and stay silent for things
that do. Their traces stop at the service boundary. Their logs are
unstructured, unindexed, and unreadable by anything except grep.[/bold magenta]

You've been brought in to rebuild their observability from the ground up.
Every signal. Every metric. Every trace. Every log line. Correlated,
structured, and actionable.

The system is live. The signals are waiting to be read.

[bold cyan]You can't fix what you can't see. Start by learning to see.[/bold cyan]
"""

ZONE_INTROS = {
    "observability_fundamentals": """
[bold cyan]== THE THREE PILLARS ==[/bold cyan]

Before you can fix anything, you need to understand what observability IS.

Not monitoring. Not dashboards. Not alerts. Observability is a property
of a system — the ability to understand its internal state by examining
its external outputs. Logs, metrics, traces. The three pillars.

Monitoring asks: "Is this thing I know about broken?"
Observability asks: "What is broken, and why, even if I've never seen this failure before?"

The corp's current setup can answer the first question. Sometimes.
Your job is to build a system that can answer the second. Always.

[italic]"You can't fix what you can't see. And right now,
you're blind."[/italic]
""",
    "logging": """
[bold cyan]== THE LOG STREAM ==[/bold cyan]

The first signal. The oldest signal. And the most abused.

The corp's services write logs. Hundreds of gigabytes per day.
Unstructured. Plain text. Scattered across a hundred nodes. The only
way to search them is SSH and grep. The only people who can read them
are the people who wrote the code.

Structured logging changes everything. JSON with consistent fields.
Centralized in one searchable system. Filterable, aggregatable,
correlatable with traces and metrics.

[yellow]Structured logging[/yellow] — JSON key-value pairs instead of plain text.
[yellow]Log levels[/yellow] — DEBUG, INFO, WARN, ERROR, FATAL — severity as a filterable field.
[yellow]Centralized logging[/yellow] — ELK, Loki, CloudWatch — one place to search everything.

[italic]"A log line without structure is a message in a bottle.
It might wash up on the right shore. Probably won't."[/italic]
""",
    "metrics_and_monitoring": """
[bold cyan]== THE METRIC GRID ==[/bold cyan]

Logs tell you what happened. Metrics tell you how much, how fast, how often.

The corp has Prometheus running. Sort of. Twelve exporters, three of them
broken. A Grafana instance with forty-seven dashboards, thirty of which
show "No Data." The alerting rules fire so often that the on-call engineer
has a Slack filter that auto-archives them.

Metrics are the backbone of operational awareness. Counters, gauges,
histograms — each serves a different purpose. PromQL gives you the
language to query them. Grafana gives you the eyes.

[yellow]Prometheus[/yellow] — pull-based metrics collection and storage.
[yellow]Grafana[/yellow] — visualization and dashboarding.
[yellow]PromQL[/yellow] — the query language for time-series data.
[yellow]Alertmanager[/yellow] — routes alerts based on rules and severity.

[italic]"A dashboard that shows green when the system is on fire
is worse than no dashboard at all. It breeds false confidence."[/italic]
""",
    "distributed_tracing": """
[bold cyan]== THE TRACE LATTICE ==[/bold cyan]

A user clicks "checkout." The request hits the API gateway, flows to the
cart service, bounces to inventory, calls the payment processor, triggers
a notification, and writes to three databases. Total time: 2.3 seconds.
Where did the time go?

Without tracing, you guess. You check individual service logs and try to
correlate timestamps. You add timing statements. You SSH into boxes and
run ad hoc queries. At 3 AM. While the pager is going off.

With tracing, you pull up the trace. You see every span. You see which
service took 1.8 seconds of the 2.3. You click into it and see the
database query that ran a full table scan.

[yellow]OpenTelemetry[/yellow] — vendor-neutral instrumentation framework.
[yellow]Spans[/yellow] — individual units of work within a trace.
[yellow]Context propagation[/yellow] — passing trace IDs between services via headers.
[yellow]Jaeger / Zipkin[/yellow] — open-source trace storage and visualization.

[italic]"Tracing doesn't just show you where the request went.
It shows you where it got stuck."[/italic]
""",
    "alerting": """
[bold cyan]== THE ALERT CHANNEL ==[/bold cyan]

The corp's on-call engineer received four hundred and twelve alerts
last week. Eleven of them required action. The rest were noise.

The engineer who was on call before that quit. The one before that
transferred to a team that doesn't carry a pager. The current one
has a Slack rule that mutes everything from Alertmanager.

This is alert fatigue. It is the single most dangerous failure mode
in operational practice. When every alert is noise, no alert is signal.

You're going to rebuild the alerting system from SLOs down. Define what
matters. Measure it. Alert only when the error budget is burning.
Everything else is a dashboard, not a page.

[yellow]SLIs / SLOs / SLAs[/yellow] — what you measure, what you target, what you promise.
[yellow]Error budgets[/yellow] — the math that balances velocity and reliability.
[yellow]PagerDuty[/yellow] — incident routing, escalation, and on-call management.
[yellow]Runbooks[/yellow] — step-by-step procedures that make 3 AM pages survivable.

[italic]"If an alert doesn't require action, it shouldn't exist.
Delete it. Your on-call engineers will thank you."[/italic]
""",
    "debugging_production": """
[bold cyan]== THE SIGNAL FLOOR ==[/bold cyan]

The alert fired. The page went out. You're awake. The dashboard is open.
Now what?

This is where observability either saves you or fails you. The dashboard
shows latency is high. Great. Which service? Which endpoint? Which
dependency? Is it a new deployment? A database issue? A downstream
provider? A capacity problem?

The answer is in the signals — but only if you know how to read them.
USE for resources. RED for services. Golden Signals for the big picture.
Flame graphs for the code. Correlation IDs to connect logs to traces.

The skills in this zone are the skills that matter at 3 AM when the
pager goes off and the incident channel is filling up.

[yellow]USE method[/yellow] — Utilization, Saturation, Errors (for resources).
[yellow]RED method[/yellow] — Rate, Errors, Duration (for services).
[yellow]Flame graphs[/yellow] — visualize where your code spends its time.
[yellow]Signal correlation[/yellow] — connecting metrics, traces, and logs via shared IDs.

[italic]"The dashboard tells you something is wrong. The traces
tell you where. The logs tell you why. You need all three."[/italic]
""",
    "cost_and_scale": """
[bold cyan]== THE DATA FURNACE ==[/bold cyan]

The observability stack is working. The signals are flowing. The dashboards
are green (actually green this time, not lying-green). The alerts are
actionable. The traces connect end to end.

Then the bill arrives.

Fourteen thousand dollars a month. For observability. The CFO wants to
know why you're spending more on watching the system than on running it.

This is the final challenge. Observability at scale is an engineering
problem AND an economics problem. Every metric label is a cost decision.
Every log line is a storage decision. Every trace span is a budget line.

[yellow]Cardinality[/yellow] — the hidden multiplier that explodes your metric storage.
[yellow]Sampling[/yellow] — keeping the signal, reducing the volume.
[yellow]Retention policies[/yellow] — tiered storage for different time horizons.
[yellow]Pipeline filtering[/yellow] — dropping noise before it hits your backend.

[italic]"The cheapest observability data is the data you never ingest.
The most expensive is the data you needed but didn't keep."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "observability_fundamentals": """
[bold green]THE THREE PILLARS — UNDERSTOOD.[/bold green]

Logs, metrics, traces. The three distinct signal types that, together,
give you the ability to understand any system behavior — anticipated
or not.

You know the difference between monitoring and observability.
You understand cardinality. You know which signal type answers which
question. The foundation is set.

[bold cyan]The Log Stream is next. Time to structure the chaos.[/bold cyan]
""",
    "logging": """
[bold green]THE LOG STREAM — STRUCTURED.[/bold green]

JSON. Key-value pairs. Consistent fields. Correlation IDs in every line.
Centralized in a searchable system where you can filter by service,
by level, by request ID, by anything.

The corp's grep-and-SSH days are over. A single query now finds
every log line from every service for a single user request.

[bold cyan]The Metric Grid awaits. Time to give the dashboards meaning.[/bold cyan]
""",
    "metrics_and_monitoring": """
[bold green]THE METRIC GRID — OPERATIONAL.[/bold green]

Prometheus scraping. Grafana rendering. PromQL querying. Alertmanager
routing. Counters counting, gauges gauging, histograms bucketing.

The thirty dead dashboards have been replaced with six that matter.
The alert rules have 'for' durations. The on-call engineer can read
the Slack channel again.

[bold cyan]The Trace Lattice. Follow the requests through the distributed maze.[/bold cyan]
""",
    "distributed_tracing": """
[bold green]THE TRACE LATTICE — CONNECTED.[/bold green]

OpenTelemetry instrumented. Context propagating. Spans nesting.
Jaeger storing. Every request leaves a trail you can follow from
the edge to the database and back.

The checkout latency mystery? Payment service. Database query.
Full table scan. Found it in thirty seconds with a single trace.

[bold cyan]The Alert Channel. Time to make the pager meaningful again.[/bold cyan]
""",
    "alerting": """
[bold green]THE ALERT CHANNEL — REBUILT.[/bold green]

Four hundred alerts per week → twelve. Every one actionable. Every one
linked to a runbook. Every one tied to an SLO and an error budget.

The on-call engineer un-muted Slack. That's how you know it's working.

[bold cyan]The Signal Floor. When the page goes off, this is how you debug.[/bold cyan]
""",
    "debugging_production": """
[bold green]THE SIGNAL FLOOR — MASTERED.[/bold green]

USE for resources. RED for services. Golden Signals for the overview.
Flame graphs for the code paths. Correlation IDs to connect every signal.

You can go from "latency is high" to "this database query on this service
for this request" in under two minutes. That's observability.

[bold cyan]The Data Furnace. The signals are flowing — now manage the cost.[/bold cyan]
""",
    "cost_and_scale": """
[bold yellow]★ ★ ★  THE DATA FURNACE — OPTIMIZED.  ★ ★ ★[/bold yellow]

[bold white]The observability stack is complete.[/bold white]

Signals flowing. Dashboards accurate. Alerts actionable. Traces correlated.
Logs structured. Costs controlled.

The cardinality explosion was caught and fixed. The sampling strategy
keeps 100% of errors and 5% of everything else. The retention policy
tiers raw data at 15 days, rollups at a year. The pipeline filters
debug logs before they hit the backend.

The monthly bill dropped from $14,000 to $3,200. The CFO stopped asking
questions. The on-call engineers stopped quitting.

[bold magenta]You can see everything now. Every signal. Every service. Every request.
The system is no longer a black box. It's a glass box, and you built the glass.[/bold magenta]

[bold yellow]SIGNAL CORPS OPERATIVE: ALL-SEEING EYE. OBSERVABILITY: COMPLETE.[/bold yellow]
""",
}

BOSS_INTROS = {
    "observability_fundamentals": "[bold red]⚠  SIGNAL CHECK: The Pillar Test[/bold red]\nLogs, metrics, traces — prove you know which signal answers which question.",
    "logging": "[bold red]⚠  LOG AUDIT: The Structure Test[/bold red]\nThe logs are flowing. Prove you can structure, centralize, and correlate them.",
    "metrics_and_monitoring": "[bold red]⚠  METRIC ANALYSIS: The Dashboard Test[/bold red]\nPrometheus is scraping. Grafana is rendering. Prove you can query and alert on what matters.",
    "distributed_tracing": "[bold red]⚠  TRACE WALK: The Correlation Test[/bold red]\nA request touched seven services. Follow the spans and find the bottleneck.",
    "alerting": "[bold red]⚠  ALERT TRIAGE: The Fatigue Test[/bold red]\nFour hundred alerts a week. Prove you know which ones matter and why.",
    "debugging_production": "[bold red]⚠  INCIDENT RESPONSE: The 3 AM Test[/bold red]\nThe pager fired. The dashboard is red. Prove you can correlate signals and find root cause.",
    "cost_and_scale": "[bold red]★  COST AUDIT: The Bill Test[/bold red]\nThe observability bill arrived. Prove you can reduce it without losing signal.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_signal":         ("First Signal Read", "Read your first observability signal. The system acknowledged your presence."),
    "pillar_keeper":        ("Pillar Keeper", "Cleared The Three Pillars. You know logs, metrics, and traces — and when to use each."),
    "log_architect":        ("Log Architect", "Cleared The Log Stream. Structured, centralized, and correlated. grep is no longer your only tool."),
    "metric_operator":      ("Metric Operator", "Cleared The Metric Grid. Prometheus, Grafana, PromQL, and alerting rules that actually work."),
    "trace_walker":         ("Trace Walker", "Cleared The Trace Lattice. You can follow a request through a dozen services and find the bottleneck."),
    "alert_surgeon":        ("Alert Surgeon", "Cleared The Alert Channel. Every remaining alert is actionable. The on-call team can breathe again."),
    "signal_detective":     ("Signal Detective", "Cleared The Signal Floor. USE, RED, flame graphs — you debug production like a surgeon."),
    "cost_controller":      ("Cost Controller", "Cleared The Data Furnace. The bill dropped by 75% and the signal quality went up."),
    "streak_3":             ("Signal Lock", "3 correct in a row. Your signal reading is becoming instinctive."),
    "streak_5":             ("Tuned In", "5 in a row. The noise is fading. Only signal remains."),
    "streak_10":            ("PERFECT FREQUENCY", "10 in a row. You don't just read signals — you ARE signal."),
    "no_hints":             ("Unaided Observation", "Cleared a zone without hints. Your eyes were enough."),
    "speed_demon":          ("Reflex Read", "Answered in under 5 seconds. The signal was read before the question was finished."),
    "level_10":             ("Junior Analyst", "Level 10. Dashboards are starting to make sense at a glance."),
    "level_20":             ("Senior Analyst", "Level 20. You read flame graphs the way other people read email — quickly and without surprise."),
    "level_30":             ("Master Signal Operative", "Maximum level. You see everything. You miss nothing. The system is glass."),
    "completionist":        ("Full Spectrum", "Every zone. Every challenge. Total observability achieved."),
    "boss_slayer":          ("Signal Found", "Beat your first boss challenge. The noise thought it could hide. It couldn't."),
}
