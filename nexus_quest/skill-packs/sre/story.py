"""
story.py - Narrative text for SRE skill pack (The Reliability Engine)
Theme: CIPHER cyberpunk. The grid must hold. Reliability is not luck — it is engineering.
"""

INTRO_STORY = """
The first alert came at [bold cyan]03:12 UTC[/bold cyan].

[bold white]NODE-7 UNREACHABLE. FAILOVER INITIATED.[/bold white]

By 03:14, the cascade had begun. The payment gateway timed out waiting for
the session store. The session store was backed by the node that just died.
The load balancer kept routing traffic to the degraded cluster because nobody
had set health checks on the dependency — only the container.

By 03:27, the error rate crossed 40%. The on-call engineer's pager fired.
She opened the runbook. It said: "Restart the service." She restarted it.
It crashed again. The runbook had nothing else.

By 03:48, the CEO was in the Slack channel asking "what is happening?"
Nobody had an answer because nobody had practiced this scenario. Nobody
had defined what "healthy" meant. Nobody had an error budget. Nobody had
even agreed on what constituted "down."

[bold white]You are a Reliability Engineer.[/bold white]

[bold magenta]CIPHER Corp's grid is held together by luck and late nights. Their
SLOs are vibes. Their incident process is "whoever is awake handles it."
Their post-mortems blame the last person who deployed. Their on-call rotation
is burning out every engineer who touches it.[/bold magenta]

You have been hired to rebuild the reliability practice from first principles.
Error budgets. Incident command. Capacity planning. Resilience patterns.
On-call that does not destroy people.

The grid is live. The users are online. The next failure is already approaching.

[bold cyan]The system will break. Your job is to make sure it bends first.[/bold cyan]
"""

ZONE_INTROS = {
    "sre_fundamentals": """
[bold cyan]== THE ERROR BUDGET ==[/bold cyan]

Before you can fix reliability, you need to define it.

Not "the site is up." Not "nobody is complaining." Reliability is a number.
A ratio. Good requests over total requests. Measured, targeted, budgeted.

SLIs tell you what is happening. SLOs tell you what should be happening.
Error budgets tell you how much room you have between the two. This is
not philosophy — it is math. And the math is what aligns the business
with engineering.

When the budget is healthy, ship fast. When the budget is burning, slow
down. No arguments. No politics. Just numbers.

CIPHER Corp has never measured an SLI. They are about to.

[italic]"Reliability is not 'as high as possible.' It is a budget.
Spend it wisely."[/italic]
""",
    "incident_management": """
[bold cyan]== THE WAR ROOM ==[/bold cyan]

The alert fired. The channel lit up. Twelve engineers are online.
Nobody knows who is in charge. Three people are investigating three
different theories. Nobody is communicating to stakeholders. The
customer support team is writing their own status page because
engineering has gone silent.

This is what incident response looks like without a process.

Severity levels give you a common language. Incident commanders give
you coordination. Post-mortems give you learning. Blameless culture
gives you honesty. Without these, every incident is chaos — and
the same failure repeats because nobody documented what happened.

CIPHER Corp has had the same database connection pool exhaustion
three times this quarter. There is no post-mortem for any of them.

[italic]"An incident without a post-mortem is a lesson refused.
The system will teach it again."[/italic]
""",
    "capacity_planning": """
[bold cyan]== THE LOAD FORGE ==[/bold cyan]

CIPHER Corp's biggest customer just signed a contract that will 3x
their traffic in six weeks. The engineering lead's response: "We'll
scale when we need to."

They will need to at 2 AM on launch day. The database will hit its
connection limit. The autoscaler will take 8 minutes to provision
new instances. The CDN will cache-miss on every asset for the new
customer's content. The payment service, which was never load-tested,
will discover its bottleneck is a single-threaded webhook handler.

Capacity planning is not about predicting the future. It is about
knowing your limits, maintaining headroom, and having a plan for
when the limits are reached.

[italic]"The time to find your system's breaking point is not
during your biggest customer's launch day."[/italic]
""",
    "reliability_patterns": """
[bold cyan]== THE FAULT LINE ==[/bold cyan]

Every system fails. The question is not if, but how.

A service without resilience patterns fails catastrophically. One
slow database query cascades through every dependent service. One
overloaded endpoint brings down the entire application. One network
partition turns a minor blip into a total outage.

A service WITH resilience patterns fails gracefully. Circuit breakers
stop the cascade. Retries with backoff prevent thundering herds.
Bulkheads isolate failures. Timeouts prevent resource exhaustion.
Load shedding protects critical functionality.

CIPHER Corp's services have no circuit breakers. No bulkheads.
No timeouts on internal calls. Last month, a third-party API went
slow — not down, just slow — and it brought down everything.

[italic]"You cannot prevent failure. You can only choose
how your system fails."[/italic]
""",
    "oncall_operations": """
[bold cyan]== THE NIGHT WATCH ==[/bold cyan]

Three engineers have quit CIPHER Corp in the last six months.
All three cited the on-call rotation as a primary reason.

The rotation is 1-in-3. The alerts fire 15-20 times per shift.
Most are not actionable. The runbooks are outdated or missing.
There is no escalation path — the on-call engineer is expected
to handle everything, regardless of domain expertise. There are
no game days. No incident simulations. The first time most
engineers practice incident response is during a real incident.

On-call is the most human part of SRE. The pager wakes a real
person. The stress is real. The burnout is real. A sustainable
on-call practice is not a nice-to-have — it is a retention
requirement and a reliability requirement. Burned-out engineers
make worse decisions at 3 AM.

[italic]"On-call should be manageable, compensated, and trained for.
If it is none of these, your best people will leave."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "sre_fundamentals": """
[bold green]THE ERROR BUDGET — ESTABLISHED.[/bold green]

SLIs defined. SLOs set. Error budgets calculated. CIPHER Corp now
has a mathematical framework for balancing velocity and reliability.

When the budget is healthy, features ship. When the budget burns,
the team stabilizes. No more arguments about "move fast" versus
"be careful." The numbers decide.

Toil has been identified and capped at 50%. The remaining engineering
time goes to automation that permanently reduces operational burden.

[bold cyan]The War Room is next. Time to learn how to fight the fire.[/bold cyan]
""",
    "incident_management": """
[bold green]THE WAR ROOM — OPERATIONAL.[/bold green]

Severity levels defined. Incident commanders assigned. Post-mortem
templates created. Blameless culture established.

The database connection pool exhaustion happened again last week.
This time, the response took 8 minutes instead of 45. The IC
coordinated the response. The mitigation was in the runbook.
The post-mortem produced three action items — with owners and deadlines.

The same incident will not happen a fourth time.

[bold cyan]The Load Forge awaits. Time to know your limits before they find you.[/bold cyan]
""",
    "capacity_planning": """
[bold green]THE LOAD FORGE — CALIBRATED.[/bold green]

Load tests run. Bottlenecks identified. Autoscaling configured.
Headroom maintained. Cost optimized.

The 3x traffic event arrived. The autoscaler responded in time
because headroom absorbed the initial spike. The database handled
the load because the connection pooling was right-sized after load
testing. The webhook handler was rewritten to be concurrent after
the soak test revealed the bottleneck.

The launch went smoothly. Nobody was paged.

[bold cyan]The Fault Line. Time to build systems that bend without breaking.[/bold cyan]
""",
    "reliability_patterns": """
[bold green]THE FAULT LINE — FORTIFIED.[/bold green]

Circuit breakers installed. Retries tuned with backoff and jitter.
Bulkheads isolating critical paths. Timeouts set on every call.
Load shedding protecting core functionality. Idempotency keys on
every mutation.

The third-party API went slow again last Tuesday. This time, the
circuit breaker tripped after 5 failures. The service returned
cached data for 3 minutes. The breaker half-opened, tested the
connection, and closed when the API recovered.

Zero user impact. Zero pages. Zero incidents.

[bold cyan]The Night Watch. The final zone. Make on-call sustainable.[/bold cyan]
""",
    "oncall_operations": """
[bold yellow]--- THE NIGHT WATCH — STANDING. ---[/bold yellow]

[bold white]The reliability practice is complete.[/bold white]

Runbooks written for every alert. Escalation policies defined.
Game days run monthly. Follow-the-sun rotation in place. Alert
fatigue eliminated — the on-call engineer receives 2 pages per
shift, and every one is actionable.

The three engineers who quit? One came back. She said the on-call
rotation was the reason she left and the reason she returned.

CIPHER Corp's grid is no longer held together by luck. It is held
together by error budgets, incident processes, capacity plans,
resilience patterns, and an on-call rotation that does not break
the people who carry the pager.

[bold magenta]The system will still fail. Every system does. But now it bends
before it breaks. The response is practiced. The recovery is fast.
The lessons are captured. And the engineers are rested enough to
make good decisions at 3 AM.[/bold magenta]

[bold yellow]RELIABILITY ENGINEER: GRID MASTER. THE RELIABILITY ENGINE: ONLINE.[/bold yellow]
""",
}

BOSS_INTROS = {
    "sre_fundamentals": "[bold red]-- BUDGET AUDIT: The Numbers Test[/bold red]\nSLIs, SLOs, error budgets — prove you can speak the language of reliability.",
    "incident_management": "[bold red]-- INCIDENT SIM: The Chaos Test[/bold red]\nThe alert fired. The channel is live. Prove you can manage the response.",
    "capacity_planning": "[bold red]-- LOAD SPIKE: The Capacity Test[/bold red]\nTraffic is surging. Prove you know your limits and have a plan.",
    "reliability_patterns": "[bold red]-- CASCADE FAILURE: The Resilience Test[/bold red]\nA dependency is down. Prove your patterns hold the line.",
    "oncall_operations": "[bold red]* NIGHT SHIFT: The Pager Test[/bold red]\nThe pager fired at 3 AM. Prove you can respond, escalate, and survive.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_page":           ("First Page Answered", "Responded to your first alert. The grid acknowledged you."),
    "budget_keeper":        ("Budget Keeper", "Cleared The Error Budget. You speak SLIs, SLOs, and error budgets fluently."),
    "war_room_commander":   ("War Room Commander", "Cleared The War Room. Incidents have structure now. Chaos has a process."),
    "load_forger":          ("Load Forger", "Cleared The Load Forge. You know the limits before the traffic finds them."),
    "fault_line_engineer":  ("Fault Line Engineer", "Cleared The Fault Line. Circuit breakers, bulkheads, backoff — the patterns hold."),
    "night_watch_captain":  ("Night Watch Captain", "Cleared The Night Watch. On-call is sustainable. The pager is manageable."),
    "streak_3":             ("Stable Signal", "3 correct in a row. The system is holding steady."),
    "streak_5":             ("Five Nines Streak", "5 in a row. Your reliability knowledge is approaching five nines."),
    "streak_10":            ("ZERO DOWNTIME", "10 in a row. Flawless. The grid does not waver under your watch."),
    "no_hints":             ("No Runbook Needed", "Cleared a zone without hints. You did not need the runbook."),
    "speed_demon":          ("Rapid Response", "Answered in under 5 seconds. Faster than the pager timeout."),
    "level_10":             ("Junior SRE", "Level 10. You can hold the pager without fear."),
    "level_20":             ("Senior SRE", "Level 20. You design the systems that others carry pagers for."),
    "level_30":             ("Principal SRE", "Maximum level. The grid bends to your will. Reliability is your craft."),
    "completionist":        ("Grid Master", "Every zone. Every challenge. Total reliability achieved."),
    "boss_slayer":          ("Incident Survived", "Beat your first boss challenge. The outage thought it had you. It did not."),
}
