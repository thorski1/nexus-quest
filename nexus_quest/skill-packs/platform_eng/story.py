"""
story.py — Narrative for The Platform Core (Platform Engineering) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — TIER 6 ACCESS GRANTED[/bold red]

You've been inside the cluster. You've read the secrets.
But NEXUS Corp's real power wasn't the infrastructure itself —
it was the platform that made it invisible.

[bold yellow]Three years ago, NEXUS built an Internal Developer Platform.[/bold yellow]
A single portal. Self-service everything. Golden paths that every
team followed without questioning where they led.

Hundreds of developers. Thousands of deployments. One platform
controlling it all — and no one looked under the hood.

You pull up the Backstage instance cached in your browser session.

[bold cyan]$ curl -s https://platform.nexus-internal.corp/api/catalog/entities | jq length[/bold cyan]

[dim]847[/dim]

[bold white]847 entities. Services, APIs, resources, systems.
Every one of them scaffolded from templates the platform team wrote.
Every one of them following golden paths the platform team paved.[/bold white]

The platform wasn't just tooling. It was the architecture of control.
Time to understand how it was built — and what it hid.
"""

ZONE_INTROS = {
    "internal_developer_platforms": (
        "[bold cyan]ZONE: THE PORTAL[/bold cyan]\n\n"
        "The Backstage instance glows on your screen. A clean UI. "
        "Every service cataloged. Every team listed. Every deployment one click away. "
        "[bold yellow]Underneath the portal: Backstage plugins, Port integrations, "
        "and golden paths that funneled every team through the same pipelines. "
        "Learn what an IDP really is — and what this one was designed to conceal.[/bold yellow]"
    ),
    "developer_experience": (
        "[bold cyan]ZONE: THE METRICS VAULT[/bold cyan]\n\n"
        "NEXUS Corp tracked everything. DORA metrics. Developer surveys. "
        "Cognitive load scores. Self-service adoption rates. "
        "[bold yellow]The dashboards showed elite performance across the board. "
        "Deployment frequency: multiple times per day. MTTR: under an hour. "
        "But the metrics were designed to hide what mattered. "
        "Learn to read DX metrics — and learn what they left out.[/bold yellow]"
    ),
    "service_catalogs_and_templates": (
        "[bold cyan]ZONE: THE TEMPLATE FORGE[/bold cyan]\n\n"
        "Every service at NEXUS was born from a template. "
        "Cookiecutter skeletons. Backstage scaffolders. Standards baked into every repo. "
        "[bold yellow]847 services, all structurally identical. Same logging config. "
        "Same CI pipeline. Same egress rules. "
        "The templates didn't just enforce standards — they ensured that every service "
        "had the same blind spots.[/bold yellow]"
    ),
    "platform_apis_and_abstractions": (
        "[bold cyan]ZONE: THE ABSTRACTION LAYER[/bold cyan]\n\n"
        "NEXUS didn't let developers touch raw cloud resources. "
        "Everything went through Crossplane XRDs and Kratix Promises. "
        "Request a database: one YAML file. Request a queue: one YAML file. "
        "[bold yellow]The abstractions were elegant. Opinionated. And they hid "
        "what was actually being provisioned underneath. "
        "Learn how platform APIs work — and what this one abstracted away.[/bold yellow]"
    ),
    "measuring_platform_success": (
        "[bold cyan]ZONE: THE PROOF[/bold cyan]\n\n"
        "The platform team's quarterly reviews were flawless. "
        "Adoption: 94%. NPS: +62. Time to first deploy: 47 minutes. "
        "Toil reduction: 12,000 engineering hours saved per quarter. "
        "[bold yellow]But the metrics that mattered weren't on the dashboard. "
        "Learn how to measure platform success — and understand "
        "which measurements NEXUS chose not to track.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "internal_developer_platforms": (
        "[bold green]ZONE COMPLETE — THE PORTAL[/bold green]\n\n"
        "You understand IDPs now. Backstage. Port. Golden paths. "
        "NEXUS Corp's platform was textbook — every best practice followed. "
        "[bold yellow]Except the golden paths all led through the same proxy. "
        "Every service. Every deployment. One chokepoint.[/bold yellow]"
    ),
    "developer_experience": (
        "[bold green]ZONE COMPLETE — THE METRICS VAULT[/bold green]\n\n"
        "DORA metrics. Cognitive load. Inner loop optimization. "
        "NEXUS had it all instrumented. Elite performers by every measure. "
        "[bold yellow]But they never measured what the platform couldn't see: "
        "where the data went after it left the golden path.[/bold yellow]"
    ),
    "service_catalogs_and_templates": (
        "[bold green]ZONE COMPLETE — THE TEMPLATE FORGE[/bold green]\n\n"
        "847 services. All from 12 templates. All with the same egress config. "
        "The catalog-info.yaml files are pristine. Ownership is clear. "
        "[bold yellow]But template drift was never tracked. And one template — "
        "'data-processor-v2' — had an extra egress rule that no one reviewed. "
        "200 services inherited it.[/bold yellow]"
    ),
    "platform_apis_and_abstractions": (
        "[bold green]ZONE COMPLETE — THE ABSTRACTION LAYER[/bold green]\n\n"
        "Crossplane Compositions. Kratix Promises. Custom XRDs. "
        "Developers never touched AWS directly. The platform handled everything. "
        "[bold yellow]But the 'Database' XRD's Composition included a secondary "
        "replication target. Not in the docs. Not in the schema description. "
        "Every database provisioned in the last three years has a shadow replica "
        "in a different account.[/bold yellow]"
    ),
    "measuring_platform_success": (
        "[bold green]ZONE COMPLETE — THE PROOF[/bold green]\n\n"
        "You've seen the dashboards. Adoption, MTTR, deployment frequency, NPS. "
        "All real. All accurate. The platform genuinely made developers faster. "
        "[bold yellow]But the one metric missing from every report: data egress volume. "
        "12,000 hours of toil saved — and not one hour spent asking "
        "where the platform was sending copies of everything it touched.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "internal_developer_platforms": (
        "[bold red]BOSS CHALLENGE — THE GOLDEN CAGE[/bold red]\n\n"
        "[bold yellow]NEXUS Corp's IDP has 94% voluntary adoption. "
        "Every team uses the golden paths. But one team tried to go off-path "
        "and discovered they couldn't — the platform rejected non-standard configs. "
        "Explain the difference between a golden path and a golden cage. "
        "What architectural decisions determine which one you've built?[/bold yellow]"
    ),
    "developer_experience": (
        "[bold red]BOSS CHALLENGE — THE METRIC MIRAGE[/bold red]\n\n"
        "[bold yellow]NEXUS Corp reports elite DORA metrics: daily deploys, "
        "15-minute lead time, 0.5% change failure rate, 30-minute MTTR. "
        "But something is wrong. Design the set of additional metrics "
        "and qualitative signals that would reveal whether these numbers "
        "reflect genuine health — or a platform that optimized for the score.[/bold yellow]"
    ),
    "service_catalogs_and_templates": (
        "[bold red]BOSS CHALLENGE — THE TEMPLATE AUTOPSY[/bold red]\n\n"
        "[bold yellow]A Backstage template was used to scaffold 200 services. "
        "Six months later, a critical vulnerability is found in the template's "
        "base Dockerfile. All 200 services are affected. "
        "Design a system that detects template drift, notifies owners, "
        "and automates remediation — without breaking running services.[/bold yellow]"
    ),
    "platform_apis_and_abstractions": (
        "[bold red]BOSS CHALLENGE — THE SHADOW COMPOSITION[/bold red]\n\n"
        "[bold yellow]You discover a Crossplane Composition that provisions "
        "an extra S3 bucket and IAM role not documented in the XRD schema. "
        "Developers requesting 'Database' resources have no idea. "
        "Design the governance model — code review, policy-as-code, "
        "audit trails — that would have caught this. "
        "What tools and processes make Compositions trustworthy?[/bold yellow]"
    ),
    "measuring_platform_success": (
        "[bold red]BOSS CHALLENGE — THE PLATFORM AUDIT[/bold red]\n\n"
        "[bold yellow]You're brought in to audit a platform serving 500 developers "
        "and 1,200 services. The platform team claims massive ROI but has "
        "no structured measurement framework. "
        "Design the complete measurement strategy: which metrics, how to collect them, "
        "what thresholds signal success vs. failure, and how to present ROI "
        "to executives who don't understand platform engineering.[/bold yellow]"
    ),
}
