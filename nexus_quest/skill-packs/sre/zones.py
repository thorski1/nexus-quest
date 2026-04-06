"""
zones.py - All zone and challenge data for SRE skill pack (The Reliability Engine)
Theme: CIPHER cyberpunk. The grid must hold. Reliability is not luck — it is engineering.
Challenge types: quiz (multiple choice, a/b/c/d) and text (free-text short answer)
"""

ZONE_ORDER = [
    "sre_fundamentals",
    "incident_management",
    "capacity_planning",
    "reliability_patterns",
    "oncall_operations",
]

ZONES = {
    # ── ZONE 1: SRE FUNDAMENTALS ──────────────────────────────────────────
    "sre_fundamentals": {
        "id": "sre_fundamentals",
        "name": "The Error Budget",
        "subtitle": "SLIs, SLOs, SLAs — The Language of Reliability",
        "color": "cyan",
        "icon": "[ ]",
        "challenges": [
            {
                "id": "sre_fund_1",
                "type": "quiz",
                "title": "The Indicator",
                "question": "In SRE, what is a Service Level Indicator (SLI)?",
                "lesson": (
                    "An SLI is a quantitative measure of a specific aspect of the\n"
                    "level of service provided. It is a ratio — good events over\n"
                    "total events — expressed as a percentage.\n\n"
                    "Examples:\n"
                    "  - Request latency: % of requests served under 200ms\n"
                    "  - Availability: % of successful requests (non-5xx)\n"
                    "  - Throughput: % of requests handled within capacity\n\n"
                    "SLIs are the raw signal. Everything else — SLOs, SLAs,\n"
                    "error budgets — is derived from them. If your SLIs are\n"
                    "wrong, everything downstream is wrong too."
                ),
                "options": [
                    "A quantitative measure of service performance, such as request latency or availability",
                    "A contractual agreement between a provider and a customer",
                    "The maximum amount of downtime allowed per quarter",
                    "A dashboard that shows real-time system health",
                ],
                "answer": "a",
                "hints": [
                    "Think about raw measurement, not targets or contracts.",
                    "It is a ratio: good events divided by total events.",
                ],
                "xp": 25,
            },
            {
                "id": "sre_fund_2",
                "type": "quiz",
                "title": "The Objective",
                "question": "What is the relationship between an SLI and an SLO?",
                "lesson": (
                    "An SLO (Service Level Objective) is a target value or range\n"
                    "for an SLI. The SLI is the measurement; the SLO is the goal.\n\n"
                    "SLI: 'We measured that 99.3% of requests completed under 200ms.'\n"
                    "SLO: 'We target 99.5% of requests under 200ms.'\n\n"
                    "SLOs are internal targets chosen by engineering. They should be\n"
                    "set based on user expectations, not on what the system can\n"
                    "theoretically achieve. A system that can do 99.99% but whose\n"
                    "users only need 99.5% should target 99.5% — the gap is your\n"
                    "error budget for velocity."
                ),
                "options": [
                    "An SLO is the contractual penalty for missing an SLI",
                    "An SLO is a target value for an SLI — the goal you set for your measurement",
                    "An SLI replaces SLOs when you adopt SRE practices",
                    "An SLO is the same as an SLA but for internal teams",
                ],
                "answer": "b",
                "hints": [
                    "One is the measurement, the other is the target for that measurement.",
                    "SLI = what you measure. SLO = what you aim for.",
                ],
                "xp": 25,
            },
            {
                "id": "sre_fund_3",
                "type": "quiz",
                "title": "The Agreement",
                "question": "How does an SLA differ from an SLO?",
                "lesson": (
                    "An SLA (Service Level Agreement) is a formal contract between\n"
                    "a provider and a customer that specifies consequences for\n"
                    "missing service level targets.\n\n"
                    "SLO: internal engineering target. 'We aim for 99.9% uptime.'\n"
                    "SLA: external contract. 'If uptime drops below 99.5%, we\n"
                    "issue credits.'\n\n"
                    "SLAs should always be looser than SLOs. If your SLO is 99.9%,\n"
                    "your SLA might promise 99.5%. The gap gives you a warning\n"
                    "buffer — you breach the SLO (internal alarm) before you\n"
                    "breach the SLA (financial and reputational damage)."
                ),
                "options": [
                    "SLAs are more aggressive targets than SLOs",
                    "SLAs are only used in open-source projects",
                    "An SLA is a contractual commitment with consequences, while an SLO is an internal target",
                    "There is no practical difference between SLAs and SLOs",
                ],
                "answer": "c",
                "hints": [
                    "Think about what happens when a target is missed. Who cares?",
                    "One involves contracts and consequences. The other is internal.",
                ],
                "xp": 25,
            },
            {
                "id": "sre_fund_4",
                "type": "text",
                "title": "The Budget",
                "question": "If your SLO is 99.9% availability over 30 days, approximately how many minutes of downtime does your error budget allow?",
                "options": [],
                "answer": "43",
                "lesson": (
                    "Error budget = 1 - SLO target.\n\n"
                    "30 days = 43,200 minutes.\n"
                    "Error budget = 0.1% of 43,200 = 43.2 minutes.\n\n"
                    "This is the key insight of SRE: reliability is not 'as high\n"
                    "as possible.' It is a budget to be spent. Those 43 minutes\n"
                    "are your currency for deploying new features, running\n"
                    "experiments, and taking calculated risks.\n\n"
                    "When the budget is healthy, push features fast.\n"
                    "When the budget is burning, slow down and stabilize."
                ),
                "hints": [
                    "30 days = 43,200 minutes. What is 0.1% of that?",
                    "Multiply 43,200 by 0.001.",
                ],
                "xp": 30,
            },
            {
                "id": "sre_fund_5",
                "type": "quiz",
                "title": "Budget Policy",
                "question": "What should an SRE team do when the error budget is nearly exhausted?",
                "lesson": (
                    "When the error budget is burning fast or nearly gone, the SRE\n"
                    "team should freeze feature releases and focus on reliability.\n\n"
                    "This is the error budget policy in action:\n"
                    "  - Budget healthy -> ship features, take risks\n"
                    "  - Budget burning -> slow deployments, investigate\n"
                    "  - Budget exhausted -> feature freeze, reliability only\n\n"
                    "This is NOT punishment. It is a rational allocation of\n"
                    "engineering effort. The error budget is the mechanism that\n"
                    "aligns product velocity with reliability. Without it, the\n"
                    "argument is 'move fast' vs 'be careful' — politics.\n"
                    "With it, the argument is math."
                ),
                "options": [
                    "Increase the SLO target to create more budget",
                    "Freeze feature launches and focus engineering effort on reliability improvements",
                    "Switch to a different monitoring tool",
                    "Immediately page all engineers to fix production issues",
                ],
                "answer": "b",
                "hints": [
                    "When the budget runs out, what kind of work takes priority?",
                    "Reliability work — not new features — until the budget recovers.",
                ],
                "xp": 30,
            },
            {
                "id": "sre_fund_6",
                "type": "text",
                "title": "Toil Identifier",
                "question": "In SRE, what is the term for manual, repetitive, automatable operational work that scales linearly with service growth?",
                "options": [],
                "answer": "toil",
                "lesson": (
                    "Toil is work that is manual, repetitive, automatable, tactical,\n"
                    "lacking enduring value, and scales linearly with service growth.\n\n"
                    "Examples of toil:\n"
                    "  - Manually restarting a service every time it crashes\n"
                    "  - Hand-editing config files for each new customer\n"
                    "  - Running a script to rotate credentials every month\n"
                    "  - Manually acknowledging alerts that require no action\n\n"
                    "Google's SRE model targets keeping toil below 50% of an\n"
                    "SRE's time. The other 50% goes to engineering work that\n"
                    "permanently reduces toil or improves reliability."
                ),
                "hints": [
                    "It rhymes with 'oil' and is a four-letter word.",
                    "Google's SRE book names this as the enemy of engineering time.",
                ],
                "xp": 25,
            },
            {
                "id": "sre_fund_7",
                "type": "quiz",
                "title": "The Nines",
                "question": "What is the practical difference between 99.9% and 99.99% availability?",
                "lesson": (
                    "Each additional nine is roughly a 10x reduction in allowed\n"
                    "downtime:\n\n"
                    "  99%    = 3.65 days/year   (87.6 hours)\n"
                    "  99.9%  = 8.76 hours/year  (525.6 minutes)\n"
                    "  99.99% = 52.6 minutes/year\n"
                    "  99.999% = 5.26 minutes/year\n\n"
                    "Going from three nines to four nines does not mean 'a little\n"
                    "better.' It means your entire architecture, deployment process,\n"
                    "testing strategy, and on-call practice must be 10x more\n"
                    "disciplined. The cost curve is exponential. Most services\n"
                    "do not need — and cannot justify — four nines."
                ),
                "options": [
                    "Almost none — both are above 99%",
                    "About 10x less allowed downtime, requiring fundamentally different engineering approaches",
                    "99.99% requires a multi-cloud setup; 99.9% does not",
                    "99.99% is only achievable with dedicated hardware",
                ],
                "answer": "b",
                "hints": [
                    "Calculate the downtime for each. The jump is larger than you think.",
                    "8.76 hours vs 52.6 minutes. That is a 10x difference.",
                ],
                "xp": 30,
            },
            {
                "id": "sre_fund_8",
                "type": "quiz",
                "title": "SRE vs DevOps",
                "question": "How did Google's original SRE team describe the relationship between SRE and DevOps?",
                "lesson": (
                    "'SRE is what happens when you ask a software engineer to\n"
                    "design an operations team.' — Ben Treynor Sloss\n\n"
                    "DevOps is a set of cultural practices and principles.\n"
                    "SRE is a specific implementation of those principles with\n"
                    "concrete practices: error budgets, SLOs, toil budgets,\n"
                    "blameless postmortems, and capped operational load.\n\n"
                    "DevOps says: 'Dev and Ops should collaborate.'\n"
                    "SRE says: 'Here is exactly how, with these metrics,\n"
                    "these policies, and these practices.'\n\n"
                    "Think of it as: class SRE implements DevOps."
                ),
                "options": [
                    "SRE replaces DevOps entirely",
                    "SRE implements DevOps principles with concrete practices and measurable targets",
                    "SRE is focused on security while DevOps is focused on speed",
                    "DevOps is for startups; SRE is for enterprises",
                ],
                "answer": "b",
                "hints": [
                    "Think of the relationship as interface vs implementation.",
                    "One is the philosophy, the other is the practice.",
                ],
                "xp": 25,
            },
        ],
    },

    # ── ZONE 2: INCIDENT MANAGEMENT ───────────────────────────────────────
    "incident_management": {
        "id": "incident_management",
        "name": "The War Room",
        "subtitle": "Severity, Command, Post-Mortems — Managing the Fire",
        "color": "red",
        "icon": "[!]",
        "challenges": [
            {
                "id": "inc_mgmt_1",
                "type": "quiz",
                "title": "Severity Classification",
                "question": "What typically defines a SEV-1 (Severity 1) incident?",
                "lesson": (
                    "Severity levels classify incidents by impact and urgency:\n\n"
                    "  SEV-1: Complete service outage or critical data loss\n"
                    "         affecting all users. All hands on deck.\n"
                    "  SEV-2: Major feature degraded. Significant user impact.\n"
                    "         On-call team engaged, others on standby.\n"
                    "  SEV-3: Minor feature impacted. Limited user impact.\n"
                    "         On-call investigates during business hours.\n"
                    "  SEV-4: Cosmetic issue or minor bug. No urgency.\n\n"
                    "The key is that severity is about USER IMPACT, not about\n"
                    "what component broke. A database failover that is invisible\n"
                    "to users is not a SEV-1 just because a database went down."
                ),
                "options": [
                    "Any issue that triggers an alert in PagerDuty",
                    "A complete outage or critical failure affecting all or most users",
                    "A bug reported by a single customer",
                    "Any deployment that requires a rollback",
                ],
                "answer": "b",
                "hints": [
                    "Think about the scope of user impact, not the component that failed.",
                    "SEV-1 means broad, critical impact — the system is down for everyone.",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_2",
                "type": "quiz",
                "title": "Incident Commander",
                "question": "What is the primary role of an Incident Commander (IC) during a major incident?",
                "lesson": (
                    "The Incident Commander coordinates the response. They do NOT\n"
                    "debug the issue themselves. Their responsibilities:\n\n"
                    "  - Own the incident timeline and communication\n"
                    "  - Assign roles: investigators, communicators, scribes\n"
                    "  - Make decisions about escalation and mitigation\n"
                    "  - Keep stakeholders informed with regular updates\n"
                    "  - Decide when to declare the incident resolved\n\n"
                    "The IC is the conductor, not the musician. The worst thing\n"
                    "an IC can do is start debugging — because then nobody is\n"
                    "coordinating, and you have a room full of people\n"
                    "investigating different theories with no shared context."
                ),
                "options": [
                    "Personally fix the root cause of the issue as fast as possible",
                    "Coordinate the response, manage communication, and make escalation decisions",
                    "Write the post-mortem report after the incident is resolved",
                    "Monitor social media for user complaints during the outage",
                ],
                "answer": "b",
                "hints": [
                    "The IC is a coordinator, not a debugger.",
                    "Think conductor of an orchestra, not a soloist.",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_3",
                "type": "text",
                "title": "The Post-Mortem",
                "question": "What is the standard name for the document written after an incident to analyze what happened, why, and how to prevent recurrence?",
                "options": [],
                "answer": "post-mortem",
                "lesson": (
                    "A post-mortem (also: postmortem, incident review, retrospective)\n"
                    "is a structured analysis written after an incident.\n\n"
                    "Standard sections:\n"
                    "  - Summary: what happened, impact, duration\n"
                    "  - Timeline: minute-by-minute events\n"
                    "  - Root cause: the underlying technical failure\n"
                    "  - Contributing factors: what made it worse\n"
                    "  - Action items: concrete steps to prevent recurrence\n"
                    "  - Lessons learned: what worked, what did not\n\n"
                    "A post-mortem that does not produce action items is just\n"
                    "storytelling. A post-mortem that blames individuals instead\n"
                    "of systems will ensure nobody reports failures honestly."
                ),
                "hints": [
                    "It is a Latin phrase meaning 'after death.'",
                    "Two words, hyphenated. Written after every significant incident.",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_4",
                "type": "quiz",
                "title": "Blameless Culture",
                "question": "Why do SRE teams practice 'blameless post-mortems'?",
                "lesson": (
                    "Blameless post-mortems focus on systemic failures, not\n"
                    "individual mistakes. The principle: if a human can cause\n"
                    "a catastrophic failure, the system is the problem, not\n"
                    "the human.\n\n"
                    "Why blameless?\n"
                    "  - People who fear punishment hide information\n"
                    "  - Hidden information means you cannot fix root causes\n"
                    "  - Unfixed root causes mean the same incident repeats\n"
                    "  - Blame creates a culture of CYA, not improvement\n\n"
                    "Blameless does NOT mean accountability-free. Teams are\n"
                    "still responsible for action items. But 'Engineer X made\n"
                    "a mistake' becomes 'The deployment system allowed a bad\n"
                    "config to reach production without validation.'"
                ),
                "options": [
                    "To avoid legal liability when customers sue",
                    "Because individuals cannot be held responsible for system failures",
                    "Because blame discourages honest reporting, hiding the information needed to fix systemic issues",
                    "To make post-mortems faster and easier to write",
                ],
                "answer": "c",
                "hints": [
                    "What happens when people are afraid to admit mistakes?",
                    "They hide information. Hidden information means unfixed root causes.",
                ],
                "xp": 30,
            },
            {
                "id": "inc_mgmt_5",
                "type": "quiz",
                "title": "Mitigation vs Fix",
                "question": "During an active incident, what is the difference between mitigation and a fix?",
                "lesson": (
                    "Mitigation stops the bleeding. A fix addresses the root cause.\n\n"
                    "Mitigation examples:\n"
                    "  - Rolling back a bad deploy\n"
                    "  - Redirecting traffic away from a failing region\n"
                    "  - Restarting crashed processes\n"
                    "  - Enabling a feature flag to disable broken functionality\n\n"
                    "Fix examples:\n"
                    "  - Patching the bug that caused the crash\n"
                    "  - Adding connection pooling to prevent database overload\n"
                    "  - Fixing the race condition in the deployment pipeline\n\n"
                    "During an incident, ALWAYS mitigate first. Get users back\n"
                    "to a working state. Root cause analysis and permanent fixes\n"
                    "happen after the bleeding stops."
                ),
                "options": [
                    "There is no difference; they mean the same thing",
                    "Mitigation restores service quickly; a fix addresses the root cause permanently",
                    "A fix is faster than mitigation",
                    "Mitigation is only used for SEV-1 incidents",
                ],
                "answer": "b",
                "hints": [
                    "One stops the bleeding now. The other heals the wound later.",
                    "During an incident, which do you do first?",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_6",
                "type": "quiz",
                "title": "Communication Protocol",
                "question": "During a major incident, how often should status updates be communicated to stakeholders?",
                "lesson": (
                    "Regular, predictable updates are critical during incidents.\n"
                    "The standard practice is every 15-30 minutes, even if there\n"
                    "is no new information.\n\n"
                    "Why update when nothing has changed?\n"
                    "  - Silence breeds panic. Stakeholders assume the worst.\n"
                    "  - 'No update' updates confirm the team is still working.\n"
                    "  - Predictable cadence reduces interruptions from anxious\n"
                    "    managers asking 'any update?'\n\n"
                    "Template: 'Status: investigating. Impact: [description].\n"
                    "Current theory: [hypothesis]. Next update: [time].'\n\n"
                    "The worst thing during an incident is radio silence.\n"
                    "The second worst is an update channel flooded with noise."
                ),
                "options": [
                    "Only when the incident is fully resolved",
                    "At regular intervals (e.g., every 15-30 minutes), even if there is no new information",
                    "Only when a new root cause theory is identified",
                    "Continuously, streaming all debug output to the stakeholder channel",
                ],
                "answer": "b",
                "hints": [
                    "Silence during an incident is worse than saying 'still investigating.'",
                    "Regular cadence, even with 'no change' updates.",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_7",
                "type": "text",
                "title": "The Rollback",
                "question": "What is the single most common and effective mitigation action during a deployment-related incident?",
                "options": [],
                "answer": "rollback",
                "lesson": (
                    "When a deployment causes an incident, the fastest mitigation\n"
                    "is almost always rolling back to the last known good version.\n\n"
                    "Rollback should be:\n"
                    "  - Fast: under 5 minutes, ideally automated\n"
                    "  - Safe: tested regularly, not just in emergencies\n"
                    "  - Available: the previous version must still be deployable\n"
                    "  - Practiced: the team should know the command by heart\n\n"
                    "The instinct to 'fix forward' during an incident is usually\n"
                    "wrong. Debugging under pressure is slow and error-prone.\n"
                    "Roll back, restore service, then investigate calmly."
                ),
                "hints": [
                    "It means reverting to the previous version.",
                    "Two syllables. Roll + back.",
                ],
                "xp": 25,
            },
            {
                "id": "inc_mgmt_8",
                "type": "quiz",
                "title": "Action Items",
                "question": "What makes a good post-mortem action item?",
                "lesson": (
                    "Good action items are specific, assigned, and time-bound.\n\n"
                    "Bad action item: 'Improve monitoring.'\n"
                    "Good action item: 'Add latency SLO alert for checkout\n"
                    "  service with a 5-minute burn rate window. Owner: @alice.\n"
                    "  Due: 2024-02-15.'\n\n"
                    "Bad: 'Be more careful with deployments.'\n"
                    "Good: 'Add canary deployment step that checks error rate\n"
                    "  for 10 minutes before proceeding. Owner: @bob.\n"
                    "  Due: 2024-02-20.'\n\n"
                    "Action items without owners will never be completed.\n"
                    "Action items without deadlines will drift indefinitely.\n"
                    "Action items that say 'be more careful' are not action items."
                ),
                "options": [
                    "Broad and aspirational, like 'improve reliability'",
                    "Specific, assigned to an owner, and time-bound with a concrete deliverable",
                    "Focused on identifying who made the mistake",
                    "Optional suggestions that the team can consider in the next sprint",
                ],
                "answer": "b",
                "hints": [
                    "Think about what makes any task completable: specificity, ownership, deadline.",
                    "'Improve monitoring' is not an action item. 'Add X alert by Y date, owner Z' is.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 3: CAPACITY PLANNING ─────────────────────────────────────────
    "capacity_planning": {
        "id": "capacity_planning",
        "name": "The Load Forge",
        "subtitle": "Scaling, Testing, Headroom — Engineering for Tomorrow's Traffic",
        "color": "yellow",
        "icon": "[^]",
        "challenges": [
            {
                "id": "cap_plan_1",
                "type": "quiz",
                "title": "Load Testing",
                "question": "What is the primary purpose of load testing in capacity planning?",
                "lesson": (
                    "Load testing determines how your system behaves under expected\n"
                    "and peak traffic conditions. It answers the question: 'How\n"
                    "much can this system handle before it degrades?'\n\n"
                    "Types of load testing:\n"
                    "  - Baseline: normal expected traffic\n"
                    "  - Stress: traffic beyond expected peak\n"
                    "  - Spike: sudden burst of traffic\n"
                    "  - Soak/endurance: sustained load over long periods\n\n"
                    "Load testing is not about 'will it crash?' It is about\n"
                    "finding the degradation curve — at what point does latency\n"
                    "increase? At what point do errors start? Where is the\n"
                    "bottleneck — CPU, memory, database connections, network?"
                ),
                "options": [
                    "To find and fix all bugs before production",
                    "To determine system behavior and limits under expected and peak traffic conditions",
                    "To verify that the application code compiles correctly",
                    "To test the UI for visual regressions",
                ],
                "answer": "b",
                "hints": [
                    "It is about understanding capacity limits, not finding bugs.",
                    "What happens to latency and errors as traffic increases?",
                ],
                "xp": 25,
            },
            {
                "id": "cap_plan_2",
                "type": "quiz",
                "title": "Horizontal vs Vertical",
                "question": "What is the key difference between horizontal and vertical scaling?",
                "lesson": (
                    "Vertical scaling (scale up): add more resources to an\n"
                    "existing machine — more CPU, RAM, disk.\n"
                    "  Pros: simple, no code changes\n"
                    "  Cons: hard limits, single point of failure, expensive\n\n"
                    "Horizontal scaling (scale out): add more machines.\n"
                    "  Pros: near-infinite scale, fault tolerance\n"
                    "  Cons: complexity (state management, load balancing,\n"
                    "  data consistency)\n\n"
                    "Most modern systems are designed to scale horizontally.\n"
                    "Databases are the usual exception — scaling a database\n"
                    "horizontally (sharding) is one of the hardest problems\n"
                    "in distributed systems."
                ),
                "options": [
                    "Horizontal adds machines; vertical adds resources to existing machines",
                    "Vertical is for databases; horizontal is for application servers only",
                    "Horizontal scaling is always cheaper than vertical scaling",
                    "They are different names for the same technique",
                ],
                "answer": "a",
                "hints": [
                    "Think about adding more boxes vs making the box bigger.",
                    "Out vs up. Width vs height.",
                ],
                "xp": 25,
            },
            {
                "id": "cap_plan_3",
                "type": "quiz",
                "title": "Autoscaling Triggers",
                "question": "Which metric is most commonly used as the primary autoscaling trigger for stateless web services?",
                "lesson": (
                    "CPU utilization is the most common autoscaling trigger for\n"
                    "stateless web services because it directly correlates with\n"
                    "request processing load.\n\n"
                    "Common autoscaling strategies:\n"
                    "  - Target tracking: maintain CPU at 60-70%\n"
                    "  - Step scaling: add 2 instances if CPU > 80%\n"
                    "  - Scheduled: scale up before known traffic peaks\n"
                    "  - Custom: scale on request queue depth or latency\n\n"
                    "Warning: autoscaling on memory is risky for web services\n"
                    "because memory often does not correlate with traffic.\n"
                    "A memory leak looks like 'more traffic' to the autoscaler,\n"
                    "and it will keep adding instances until the budget explodes."
                ),
                "options": [
                    "Disk I/O utilization",
                    "CPU utilization",
                    "Number of running containers",
                    "Network packet count",
                ],
                "answer": "b",
                "hints": [
                    "For stateless web services, which resource is consumed most directly by requests?",
                    "It is the most universal resource metric.",
                ],
                "xp": 25,
            },
            {
                "id": "cap_plan_4",
                "type": "text",
                "title": "Headroom Percentage",
                "question": "In capacity planning, what is the commonly recommended minimum percentage of headroom to maintain above peak expected traffic?",
                "options": [],
                "answer": "50",
                "lesson": (
                    "The standard recommendation is to maintain at least 50%\n"
                    "headroom above your peak expected traffic. Some teams use\n"
                    "the 'N+1' or 'N+2' model instead.\n\n"
                    "Why 50%?\n"
                    "  - Traffic spikes can be sudden and unpredictable\n"
                    "  - Autoscaling takes time (minutes, not seconds)\n"
                    "  - Failure of one component shifts load to others\n"
                    "  - Seasonal events (Black Friday, product launches)\n"
                    "    can 2-3x normal traffic\n\n"
                    "Headroom is insurance. It costs money to maintain idle\n"
                    "capacity, but it costs more money to go down during\n"
                    "your biggest traffic day of the year."
                ),
                "hints": [
                    "It is a round number and common rule of thumb.",
                    "Half again above peak. Think about what percentage that is.",
                ],
                "xp": 30,
            },
            {
                "id": "cap_plan_5",
                "type": "quiz",
                "title": "Cost Optimization",
                "question": "What is the most effective first step in cloud cost optimization for compute resources?",
                "lesson": (
                    "Right-sizing is the most impactful first step. Most cloud\n"
                    "instances are over-provisioned — running on larger instance\n"
                    "types than the workload requires.\n\n"
                    "Steps for cost optimization (in order of impact):\n"
                    "  1. Right-size: match instance types to actual usage\n"
                    "  2. Reserved/committed: 1-3 year commitments for 40-70% savings\n"
                    "  3. Spot/preemptible: for fault-tolerant workloads, 60-90% savings\n"
                    "  4. Autoscaling: scale down during low traffic\n"
                    "  5. Architecture: serverless for spiky workloads\n\n"
                    "A common pattern: a team runs 20 m5.2xlarge instances 24/7.\n"
                    "Actual CPU usage averages 15%. Right-sizing to m5.large\n"
                    "and adding autoscaling cuts the bill by 70%."
                ),
                "options": [
                    "Migrate everything to serverless immediately",
                    "Right-size instances by matching instance types to actual resource utilization",
                    "Switch to a different cloud provider with lower prices",
                    "Reduce the number of environments from three to one",
                ],
                "answer": "b",
                "hints": [
                    "Start by looking at what you are already paying for and whether you need it.",
                    "Most instances are bigger than they need to be.",
                ],
                "xp": 30,
            },
            {
                "id": "cap_plan_6",
                "type": "quiz",
                "title": "The Bottleneck",
                "question": "In capacity planning, what does 'the bottleneck' refer to?",
                "lesson": (
                    "The bottleneck is the single component that limits the\n"
                    "overall throughput of the system. Scaling anything other\n"
                    "than the bottleneck will not improve total capacity.\n\n"
                    "This is Amdahl's Law in practice. If the database can\n"
                    "handle 1,000 queries/second and the application servers\n"
                    "can generate 10,000 queries/second, adding more application\n"
                    "servers does nothing. The database is the bottleneck.\n\n"
                    "Finding the bottleneck requires measurement, not guessing.\n"
                    "Common bottlenecks:\n"
                    "  - Database connections or query throughput\n"
                    "  - Network bandwidth between services\n"
                    "  - CPU on compute-intensive services\n"
                    "  - External API rate limits"
                ),
                "options": [
                    "The most expensive component in the infrastructure",
                    "The component with the most recent incidents",
                    "The single component that limits overall system throughput",
                    "The service with the oldest codebase",
                ],
                "answer": "c",
                "hints": [
                    "Think about what constrains the whole system.",
                    "Scaling anything else does not help until this is resolved.",
                ],
                "xp": 25,
            },
            {
                "id": "cap_plan_7",
                "type": "quiz",
                "title": "Soak Testing",
                "question": "What does a soak test (endurance test) reveal that a short load test cannot?",
                "lesson": (
                    "Soak tests run sustained load for hours or days to reveal\n"
                    "time-dependent failures:\n\n"
                    "  - Memory leaks: gradual increase leading to OOM kills\n"
                    "  - Connection pool exhaustion: slow leak of connections\n"
                    "  - Disk space: logs, temp files, database growth\n"
                    "  - Cache invalidation issues: stale data accumulation\n"
                    "  - Certificate or token expiration during the test\n"
                    "  - GC pressure: increasing pause times under sustained load\n\n"
                    "A 10-minute load test might show the system handles 5,000\n"
                    "RPS perfectly. A 48-hour soak test at 5,000 RPS reveals\n"
                    "that memory usage grows 10MB/hour and the service OOM-kills\n"
                    "after 36 hours."
                ),
                "options": [
                    "Whether the application can handle high request rates",
                    "Time-dependent issues like memory leaks, connection exhaustion, and resource degradation",
                    "Whether the UI renders correctly under load",
                    "How the application handles invalid input",
                ],
                "answer": "b",
                "hints": [
                    "What goes wrong only after hours or days of continuous load?",
                    "Think about resources that slowly accumulate or deplete.",
                ],
                "xp": 30,
            },
            {
                "id": "cap_plan_8",
                "type": "text",
                "title": "N+1 Redundancy",
                "question": "In the capacity model where you provision enough resources to survive the loss of one component, what is this pattern called?",
                "options": [],
                "answer": "N+1",
                "lesson": (
                    "N+1 redundancy means provisioning one more unit than you\n"
                    "need to handle peak load. If you need 3 servers for peak\n"
                    "traffic, you run 4.\n\n"
                    "Variants:\n"
                    "  N+1: survive one failure (most common)\n"
                    "  N+2: survive two simultaneous failures\n"
                    "  2N: full redundancy (double everything)\n"
                    "  2N+1: double plus one spare\n\n"
                    "N+1 is the minimum for production services. If you cannot\n"
                    "survive the loss of one instance, you are one hardware\n"
                    "failure away from an outage.\n\n"
                    "For critical services, N+2 accounts for the scenario where\n"
                    "one instance is down for maintenance when another fails."
                ),
                "hints": [
                    "N is what you need. Add 1 for safety.",
                    "A letter plus a number. Very short answer.",
                ],
                "xp": 25,
            },
        ],
    },

    # ── ZONE 4: RELIABILITY PATTERNS ──────────────────────────────────────
    "reliability_patterns": {
        "id": "reliability_patterns",
        "name": "The Fault Line",
        "subtitle": "Circuit Breakers, Retries, Bulkheads — Building for Failure",
        "color": "magenta",
        "icon": "[~]",
        "challenges": [
            {
                "id": "rel_pat_1",
                "type": "quiz",
                "title": "Circuit Breaker",
                "question": "What is the purpose of the circuit breaker pattern in distributed systems?",
                "lesson": (
                    "A circuit breaker prevents a failing downstream service from\n"
                    "cascading failures to its callers. Like an electrical circuit\n"
                    "breaker, it 'trips' when failures exceed a threshold.\n\n"
                    "States:\n"
                    "  CLOSED: requests flow normally. Failures are counted.\n"
                    "  OPEN: requests fail immediately without calling the\n"
                    "    downstream service. Fast failure instead of slow timeout.\n"
                    "  HALF-OPEN: after a cooldown, a single test request is\n"
                    "    allowed through. If it succeeds, circuit closes.\n"
                    "    If it fails, circuit stays open.\n\n"
                    "Without a circuit breaker, a failing database can cascade\n"
                    "to every service that calls it, each waiting for timeouts,\n"
                    "exhausting their connection pools, and failing their own\n"
                    "callers in turn."
                ),
                "options": [
                    "To retry failed requests automatically until they succeed",
                    "To stop calling a failing service and fail fast, preventing cascade failures",
                    "To encrypt traffic between microservices",
                    "To balance load evenly across healthy instances",
                ],
                "answer": "b",
                "hints": [
                    "Think about what a physical circuit breaker does — it stops the flow.",
                    "The goal is to fail FAST instead of fail SLOW.",
                ],
                "xp": 30,
            },
            {
                "id": "rel_pat_2",
                "type": "quiz",
                "title": "Retry with Backoff",
                "question": "Why should retries use exponential backoff with jitter instead of immediate retries?",
                "lesson": (
                    "Immediate retries at full speed can create a 'retry storm'\n"
                    "that overwhelms an already struggling service.\n\n"
                    "Exponential backoff: wait 1s, then 2s, then 4s, then 8s.\n"
                    "Each retry waits longer, giving the downstream service\n"
                    "time to recover.\n\n"
                    "Jitter: add randomness to the backoff interval.\n"
                    "Without jitter, all clients back off to the same schedule\n"
                    "and retry simultaneously — creating synchronized spikes\n"
                    "called 'thundering herd.'\n\n"
                    "With jitter: client A retries at 1.3s, client B at 1.7s,\n"
                    "client C at 0.9s. The load is spread out."
                ),
                "options": [
                    "To save bandwidth — fewer retries means lower network costs",
                    "Immediate retries are not supported by most HTTP libraries",
                    "To avoid overwhelming a struggling service with synchronized retry storms",
                    "Exponential backoff is required by the HTTP specification",
                ],
                "answer": "c",
                "hints": [
                    "What happens when 10,000 clients all retry at the same instant?",
                    "Thundering herd. The backoff and jitter spread the load.",
                ],
                "xp": 30,
            },
            {
                "id": "rel_pat_3",
                "type": "text",
                "title": "The Bulkhead",
                "question": "What reliability pattern isolates components so that a failure in one does not consume all shared resources and bring down the entire system?",
                "options": [],
                "answer": "bulkhead",
                "lesson": (
                    "The bulkhead pattern is named after the compartments in a\n"
                    "ship's hull. If one compartment floods, the bulkheads\n"
                    "prevent the water from reaching other compartments.\n\n"
                    "In software:\n"
                    "  - Separate thread pools per downstream service\n"
                    "  - Separate connection pools per dependency\n"
                    "  - Separate process pools for different workloads\n"
                    "  - Resource limits per tenant in multi-tenant systems\n\n"
                    "Example: if your service calls Database A and API B using\n"
                    "a shared connection pool of 100, and API B starts timing\n"
                    "out, all 100 connections get stuck waiting for API B.\n"
                    "Database A calls also fail — even though Database A is fine.\n"
                    "With bulkheads: 50 connections for A, 50 for B. B's failure\n"
                    "is isolated."
                ),
                "hints": [
                    "Named after a structural feature on ships that prevents flooding.",
                    "It isolates failures to one compartment.",
                ],
                "xp": 30,
            },
            {
                "id": "rel_pat_4",
                "type": "quiz",
                "title": "Graceful Degradation",
                "question": "What is graceful degradation in the context of system reliability?",
                "lesson": (
                    "Graceful degradation means continuing to provide partial\n"
                    "service when a component fails, rather than failing completely.\n\n"
                    "Examples:\n"
                    "  - Recommendation engine down? Show popular items instead\n"
                    "  - Search index slow? Return cached results from 5 min ago\n"
                    "  - Payment processor failing? Queue the transaction\n"
                    "  - Image service down? Show placeholder images\n"
                    "  - Personalization unavailable? Show the default experience\n\n"
                    "The key design question: 'When X fails, what is the minimum\n"
                    "viable experience we can still deliver?'\n\n"
                    "Every critical dependency should have a degraded fallback.\n"
                    "A system with no fallbacks has a binary state: working or\n"
                    "down. A system with good degradation paths has many states\n"
                    "between 'perfect' and 'down.'"
                ),
                "options": [
                    "Automatically shutting down the system when any component fails",
                    "Providing reduced but functional service when a component fails, instead of total failure",
                    "Gradually reducing server capacity to save costs during low traffic",
                    "Slowly migrating from one technology stack to another",
                ],
                "answer": "b",
                "hints": [
                    "Think about what a good user experience looks like during partial failure.",
                    "Partial service is better than no service.",
                ],
                "xp": 25,
            },
            {
                "id": "rel_pat_5",
                "type": "quiz",
                "title": "Timeout Strategy",
                "question": "Why is setting appropriate timeouts critical for system reliability?",
                "lesson": (
                    "Without timeouts, a slow or unresponsive downstream service\n"
                    "causes callers to wait indefinitely, holding connections,\n"
                    "threads, and memory.\n\n"
                    "The cascade:\n"
                    "  1. Service B becomes slow (not down, just slow)\n"
                    "  2. Service A calls B, waits with no timeout\n"
                    "  3. A's thread pool fills up waiting for B\n"
                    "  4. A stops responding to its own callers\n"
                    "  5. Service C, which calls A, now hangs too\n"
                    "  6. The entire system is down because B was SLOW\n\n"
                    "Timeout guidelines:\n"
                    "  - Always set timeouts. No exceptions.\n"
                    "  - Timeouts should decrease as you go up the call chain\n"
                    "  - A 30-second timeout on an API that users expect to\n"
                    "    respond in 200ms is effectively no timeout at all"
                ),
                "options": [
                    "Timeouts reduce network bandwidth usage",
                    "Without timeouts, slow dependencies consume resources indefinitely and cascade failures upstream",
                    "Timeouts are only needed for external API calls, not internal services",
                    "Timeouts are a security feature that prevents DDoS attacks",
                ],
                "answer": "b",
                "hints": [
                    "What happens to resources (threads, connections) when you wait forever?",
                    "A slow service is worse than a down service — it ties up everything.",
                ],
                "xp": 25,
            },
            {
                "id": "rel_pat_6",
                "type": "quiz",
                "title": "Idempotency",
                "question": "Why is idempotency important for retry safety in distributed systems?",
                "lesson": (
                    "An idempotent operation produces the same result whether\n"
                    "executed once or multiple times. This is critical for retries\n"
                    "because you often do not know if the first request succeeded.\n\n"
                    "Scenario: you send a payment request. The network times out.\n"
                    "Did the payment go through? You do not know. If you retry:\n"
                    "  - Idempotent: the system recognizes the duplicate and\n"
                    "    returns the original result. Customer charged once.\n"
                    "  - Not idempotent: the payment processes again.\n"
                    "    Customer charged twice.\n\n"
                    "Implementation: use idempotency keys — unique identifiers\n"
                    "sent with each request. The server checks if it has already\n"
                    "processed that key and returns the cached response."
                ),
                "options": [
                    "Idempotency makes requests faster by caching responses",
                    "It ensures retried operations do not produce duplicate side effects",
                    "Idempotency is only relevant for database write operations",
                    "It prevents unauthorized users from repeating requests",
                ],
                "answer": "b",
                "hints": [
                    "What happens if you charge a credit card twice because of a retry?",
                    "Same request, same result, no matter how many times you send it.",
                ],
                "xp": 30,
            },
            {
                "id": "rel_pat_7",
                "type": "text",
                "title": "The Shed",
                "question": "What reliability pattern involves intentionally dropping low-priority requests during overload to protect critical functionality?",
                "options": [],
                "answer": "load shedding",
                "lesson": (
                    "Load shedding is the deliberate rejection of requests when\n"
                    "the system is overloaded, prioritizing critical traffic.\n\n"
                    "Without load shedding, overload degrades ALL requests:\n"
                    "everyone gets slow responses, timeouts, and errors.\n\n"
                    "With load shedding:\n"
                    "  - Critical requests (payments, auth) continue working\n"
                    "  - Non-critical requests (analytics, recommendations)\n"
                    "    are rejected with HTTP 503\n"
                    "  - The system stays healthy for what matters most\n\n"
                    "Implementation:\n"
                    "  - Priority queues with admission control\n"
                    "  - Token bucket rate limiters per priority tier\n"
                    "  - Adaptive: measure latency, shed when it rises"
                ),
                "hints": [
                    "Two words. The system sheds something when overloaded.",
                    "Think of an electrical grid dropping non-essential circuits.",
                ],
                "xp": 30,
            },
            {
                "id": "rel_pat_8",
                "type": "quiz",
                "title": "Chaos Engineering",
                "question": "What is the core principle of chaos engineering?",
                "lesson": (
                    "Chaos engineering is the practice of deliberately injecting\n"
                    "failures into production systems to verify they can tolerate\n"
                    "them. The core principle: 'If you don't test failure, failure\n"
                    "will test you.'\n\n"
                    "Netflix's Chaos Monkey randomly kills production instances.\n"
                    "If the system handles it gracefully, the resilience is real.\n"
                    "If it doesn't, better to find out now than during Black Friday.\n\n"
                    "Steps:\n"
                    "  1. Define 'steady state' (normal system behavior)\n"
                    "  2. Hypothesize that steady state continues during failure\n"
                    "  3. Inject failure (kill instance, add latency, block traffic)\n"
                    "  4. Observe whether steady state was maintained\n"
                    "  5. Fix what broke\n\n"
                    "Chaos engineering is not breaking things randomly. It is\n"
                    "forming hypotheses about resilience and testing them."
                ),
                "options": [
                    "Randomly breaking production systems to test the on-call team's response time",
                    "Proactively injecting controlled failures to verify system resilience before real failures occur",
                    "Running all tests in a chaotic order to find race conditions",
                    "Deliberately introducing bugs to test code review processes",
                ],
                "answer": "b",
                "hints": [
                    "It is proactive, not reactive. Controlled, not random.",
                    "Netflix Chaos Monkey. Break it on purpose, fix what fails.",
                ],
                "xp": 30,
            },
        ],
    },

    # ── ZONE 5: ON-CALL & OPERATIONS ──────────────────────────────────────
    "oncall_operations": {
        "id": "oncall_operations",
        "name": "The Night Watch",
        "subtitle": "Runbooks, Escalation, Game Days — Surviving the Pager",
        "color": "green",
        "icon": "[*]",
        "challenges": [
            {
                "id": "oncall_1",
                "type": "quiz",
                "title": "The Runbook",
                "question": "What should a good runbook contain?",
                "lesson": (
                    "A runbook is a step-by-step procedure for responding to a\n"
                    "specific alert or operational task. It is the difference\n"
                    "between 'figure it out at 3 AM' and 'follow the steps.'\n\n"
                    "Essential runbook sections:\n"
                    "  - Alert description: what triggered and why it matters\n"
                    "  - Impact assessment: who/what is affected\n"
                    "  - Diagnostic steps: commands to run, things to check\n"
                    "  - Mitigation steps: how to restore service\n"
                    "  - Escalation criteria: when to wake someone else up\n"
                    "  - Verification: how to confirm the fix worked\n\n"
                    "A runbook written by the person who knows the system\n"
                    "enables the person who does NOT know the system to\n"
                    "respond effectively. That is the entire point."
                ),
                "options": [
                    "Only the commands to restart the service",
                    "Step-by-step diagnostic, mitigation, escalation, and verification procedures for specific alerts",
                    "A history of all past incidents related to the service",
                    "The architecture diagram and source code repository links",
                ],
                "answer": "b",
                "hints": [
                    "Think about what you need at 3 AM when the pager goes off.",
                    "Diagnosis, mitigation, escalation, verification. A complete response guide.",
                ],
                "xp": 25,
            },
            {
                "id": "oncall_2",
                "type": "quiz",
                "title": "Escalation Policy",
                "question": "When should an on-call engineer escalate an incident?",
                "lesson": (
                    "Escalation criteria should be predefined, not left to judgment\n"
                    "at 3 AM when you are tired and stressed.\n\n"
                    "Escalate when:\n"
                    "  - The incident exceeds your domain knowledge\n"
                    "  - The runbook does not cover this scenario\n"
                    "  - Mitigation attempts have failed after N minutes\n"
                    "  - The severity is higher than your authorization level\n"
                    "  - Customer-facing impact is growing\n"
                    "  - You are unsure and the risk is high\n\n"
                    "The cardinal sin of on-call is NOT escalating because\n"
                    "you are afraid of waking someone up. A 30-minute delayed\n"
                    "escalation during a SEV-1 can turn a bad incident into\n"
                    "a catastrophic one.\n\n"
                    "Rule: escalate early, escalate often. Nobody was ever fired\n"
                    "for escalating too quickly."
                ),
                "options": [
                    "Only when the on-call engineer has exhausted every possible fix",
                    "When predefined criteria are met: runbook exhausted, time limit reached, or severity exceeds authorization",
                    "Never — the on-call engineer is expected to handle everything alone",
                    "Only during business hours when the next tier is available",
                ],
                "answer": "b",
                "hints": [
                    "Escalation should be based on predefined criteria, not heroics.",
                    "Better to escalate too early than too late.",
                ],
                "xp": 25,
            },
            {
                "id": "oncall_3",
                "type": "quiz",
                "title": "Alert Fatigue",
                "question": "What is the primary danger of alert fatigue for an on-call engineer?",
                "lesson": (
                    "Alert fatigue occurs when an on-call engineer receives so\n"
                    "many alerts that they begin ignoring or auto-dismissing them.\n\n"
                    "The progression:\n"
                    "  1. Too many non-actionable alerts fire\n"
                    "  2. The engineer starts auto-acknowledging without reading\n"
                    "  3. A real, critical alert fires among the noise\n"
                    "  4. It gets auto-acknowledged like the rest\n"
                    "  5. Major outage goes unnoticed for hours\n\n"
                    "The fix is not 'pay more attention.' The fix is reducing\n"
                    "noise. Every alert must be actionable. If an alert fires\n"
                    "and the correct response is 'do nothing,' delete the alert.\n\n"
                    "Target: on-call engineers should receive no more than\n"
                    "2 pages per 12-hour shift on average."
                ),
                "options": [
                    "It increases cloud monitoring costs significantly",
                    "Real critical alerts get ignored because the engineer is desensitized by constant non-actionable noise",
                    "It causes the alerting system to crash from volume",
                    "It makes post-mortems too long to write",
                ],
                "answer": "b",
                "hints": [
                    "When everything is an emergency, nothing is an emergency.",
                    "The real alert drowns in the noise.",
                ],
                "xp": 30,
            },
            {
                "id": "oncall_4",
                "type": "text",
                "title": "The Game Day",
                "question": "What is the name for a planned exercise where teams simulate real incidents to practice response procedures?",
                "options": [],
                "answer": "game day",
                "lesson": (
                    "A game day is a planned incident simulation exercise.\n"
                    "The team practices responding to realistic failure scenarios\n"
                    "in a controlled environment.\n\n"
                    "Game day benefits:\n"
                    "  - Tests runbooks against real scenarios\n"
                    "  - Reveals gaps in tooling and documentation\n"
                    "  - Builds muscle memory for incident response\n"
                    "  - Reduces panic during real incidents\n"
                    "  - Identifies single points of knowledge\n\n"
                    "Format:\n"
                    "  - A facilitator injects a simulated failure\n"
                    "  - The on-call team responds as if it were real\n"
                    "  - Observers note what worked and what did not\n"
                    "  - A debrief identifies improvements\n\n"
                    "Game days should feel uncomfortable. If they are easy,\n"
                    "the scenarios are not realistic enough."
                ),
                "hints": [
                    "Two words. Think of sports practice before the real game.",
                    "A planned exercise to simulate real incidents.",
                ],
                "xp": 25,
            },
            {
                "id": "oncall_5",
                "type": "quiz",
                "title": "On-Call Rotation",
                "question": "What is the recommended minimum on-call rotation length to prevent burnout?",
                "lesson": (
                    "Most SRE teams use weekly rotations with specific constraints:\n\n"
                    "  - Minimum rotation length: 1 week (shorter is too disruptive)\n"
                    "  - Maximum on-call frequency: 1 week in 4 (25% of time)\n"
                    "  - Better target: 1 week in 6 (17% of time)\n"
                    "  - Handoff during business hours, not at midnight\n"
                    "  - Time off after a heavy on-call week\n\n"
                    "Teams smaller than 4-6 people should NOT carry a dedicated\n"
                    "on-call rotation — the frequency will cause burnout.\n"
                    "Options: shared on-call with another team, follow-the-sun\n"
                    "rotation across time zones, or an on-call pool.\n\n"
                    "On-call compensation (extra pay, time off, reduced load)\n"
                    "is not optional. It is a retention requirement."
                ),
                "options": [
                    "1 day — engineers should rotate daily for fairness",
                    "1 week, with no more than 25% of total time spent on-call",
                    "1 month — longer rotations reduce context-switching",
                    "On-call should be permanent for senior engineers only",
                ],
                "answer": "b",
                "hints": [
                    "Too short is disruptive. Too long causes burnout.",
                    "One week on, at least three weeks off.",
                ],
                "xp": 25,
            },
            {
                "id": "oncall_6",
                "type": "quiz",
                "title": "Operational Readiness",
                "question": "What should be verified before a new service is approved for production on-call support?",
                "lesson": (
                    "A Production Readiness Review (PRR) verifies that a service\n"
                    "meets the minimum bar for on-call support.\n\n"
                    "Checklist:\n"
                    "  - SLOs defined and measured\n"
                    "  - Alerts configured with runbooks\n"
                    "  - Monitoring dashboards exist and are maintained\n"
                    "  - Rollback procedure documented and tested\n"
                    "  - Capacity plan with headroom defined\n"
                    "  - On-call rotation staffed and trained\n"
                    "  - Incident response plan documented\n"
                    "  - Load testing completed\n"
                    "  - Dependency map documented\n\n"
                    "A service without these is not ready for production.\n"
                    "Adding it to on-call rotation without them is setting\n"
                    "the on-call engineer up for failure."
                ),
                "options": [
                    "Only that the code has passed all unit tests",
                    "SLOs, alerts with runbooks, monitoring, rollback procedures, capacity plans, and staffed on-call rotation",
                    "That the service has been running in staging for at least 30 days",
                    "Approval from the VP of Engineering",
                ],
                "answer": "b",
                "hints": [
                    "Think about everything an on-call engineer needs to support a service.",
                    "SLOs, alerts, runbooks, monitoring, rollback, capacity — the full checklist.",
                ],
                "xp": 30,
            },
            {
                "id": "oncall_7",
                "type": "quiz",
                "title": "Follow the Sun",
                "question": "What is the 'follow-the-sun' on-call model?",
                "lesson": (
                    "Follow-the-sun distributes on-call across teams in different\n"
                    "time zones so that on-call always falls during business hours\n"
                    "for whoever is holding the pager.\n\n"
                    "Example:\n"
                    "  - US team: on-call 8 AM - 4 PM PST\n"
                    "  - EU team: on-call 8 AM - 4 PM CET\n"
                    "  - APAC team: on-call 8 AM - 4 PM JST\n\n"
                    "Benefits:\n"
                    "  - No overnight pages for anyone\n"
                    "  - Engineers are alert and rested during their shift\n"
                    "  - Reduced burnout and improved retention\n"
                    "  - Better incident response quality\n\n"
                    "Challenges:\n"
                    "  - Requires teams in 3+ time zones\n"
                    "  - Handoff procedures must be excellent\n"
                    "  - Knowledge must be distributed, not siloed"
                ),
                "options": [
                    "On-call rotates between team members each day based on who is awake",
                    "On-call responsibility transfers between teams in different time zones so it always falls during business hours",
                    "Engineers move to different offices each quarter to share the burden",
                    "A single team covers all hours but works in 4-hour shifts",
                ],
                "answer": "b",
                "hints": [
                    "It follows the sun around the globe.",
                    "Multiple teams, multiple time zones, always daytime for the person on-call.",
                ],
                "xp": 25,
            },
            {
                "id": "oncall_8",
                "type": "quiz",
                "title": "Wheel of Misfortune",
                "question": "What is Google's 'Wheel of Misfortune' exercise?",
                "lesson": (
                    "The Wheel of Misfortune is Google's gamified version of\n"
                    "incident response training. A spinner selects a random\n"
                    "past incident, and the team role-plays the response.\n\n"
                    "How it works:\n"
                    "  - Select a real past incident (anonymized)\n"
                    "  - One engineer plays the on-call responder\n"
                    "  - The facilitator plays the 'system' — feeding symptoms\n"
                    "  - The team observes and takes notes\n"
                    "  - Debrief: what went well, what could improve\n\n"
                    "This is more effective than documentation because:\n"
                    "  - Practice builds muscle memory\n"
                    "  - It reveals assumptions people did not know they had\n"
                    "  - It is safe — mistakes have no production impact\n"
                    "  - It spreads institutional knowledge from past incidents\n\n"
                    "Every SRE team should run these monthly."
                ),
                "options": [
                    "A random selection process for assigning on-call shifts",
                    "A role-playing exercise where teams practice responding to past incidents",
                    "A tool that randomly kills production services to test resilience",
                    "A dashboard that shows which team has the most incidents",
                ],
                "answer": "b",
                "hints": [
                    "Google SRE practice. It involves a spinner and role-playing.",
                    "Teams re-enact past incidents to build response skills.",
                ],
                "xp": 30,
            },
        ],
    },
}
