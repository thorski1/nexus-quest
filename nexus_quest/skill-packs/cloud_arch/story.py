"""
story.py — Narrative for The Cloud Citadel (Cloud Architecture) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — CITADEL ACCESS CONFIRMED[/bold red]

You followed the infrastructure trail past the Kubernetes cluster, past the AWS
accounts. But NEXUS Corporation didn't build their empire on a single cloud.

They built a [bold yellow]citadel[/bold yellow].

A multi-layered architecture spanning three cloud providers, two continents,
and a hybrid on-prem facility that doesn't appear on any corporate filing.

[bold cyan]$ cipher --scan architecture-topology[/bold cyan]

[dim]{
    "providers": ["aws", "gcp", "azure"],
    "regions": 14,
    "services": 327,
    "estimated_monthly_spend": "$2.4M",
    "architecture_review_date": "never"
}[/dim]

[bold white]$2.4 million a month. No architecture review. Ever.[/bold white]

The fraud infrastructure isn't just running ON the cloud — it's
[bold yellow]woven into the architecture itself[/bold yellow]. Microservices that
shouldn't exist. Event-driven pipelines laundering data through six regions.
A disaster recovery setup that's actually a data exfiltration channel.

[bold cyan]"The architecture IS the crime,"[/bold cyan] CIPHER says.
[bold cyan]"Every design pattern they used, they weaponized."[/bold cyan]

To dismantle it, you need to understand cloud architecture
better than the people who built it.

[bold yellow]Five layers. Forty challenges. One citadel to breach.[/bold yellow]
"""

ZONE_INTROS = {
    "cloud_architecture_patterns": (
        "[bold cyan]ZONE: THE PATTERN VAULT[/bold cyan]\n\n"
        "The citadel's foundation: microservices, event-driven pipelines, "
        "serverless functions, and CQRS projections — all connected. "
        "[bold yellow]NEXUS used every modern architecture pattern in the book. "
        "Understand the patterns and you'll see the seams in their design. "
        "Every pattern has a weakness.[/bold yellow]"
    ),
    "multi_cloud_and_hybrid": (
        "[bold cyan]ZONE: THE BRIDGE NETWORK[/bold cyan]\n\n"
        "Three cloud providers. Two data centers. One hybrid mesh. "
        "NEXUS split their infrastructure across providers so no single audit "
        "could see the whole picture. "
        "[bold yellow]Terraform state files in three backends. Abstraction layers "
        "hiding provider-specific resources. A service mesh routing traffic "
        "through jurisdictions chosen for their data privacy laws.[/bold yellow]"
    ),
    "cost_optimization": (
        "[bold cyan]ZONE: THE TREASURY[/bold cyan]\n\n"
        "$2.4 million per month. But the billing breakdown tells a story. "
        "Reserved Instances purchased for servers that don't run legitimate workloads. "
        "Spot fleets for batch jobs that process phantom transactions. "
        "[bold yellow]Follow the money — not just through the database, "
        "but through the cloud bill itself. Cost allocation tags don't lie, "
        "even when everything else does.[/bold yellow]"
    ),
    "high_availability": (
        "[bold cyan]ZONE: THE FAILSAFE LAYER[/bold cyan]\n\n"
        "NEXUS built their fraud infrastructure to be more resilient than "
        "most Fortune 500 production systems. Multi-AZ. Multi-region. "
        "Automated failover with sub-minute RTO. "
        "[bold yellow]Their disaster recovery plan isn't about surviving disasters — "
        "it's about surviving investigations. Every failover path is also "
        "a data destruction path. Understand HA to disarm it.[/bold yellow]"
    ),
    "well_architected_framework": (
        "[bold cyan]ZONE: THE FIVE PILLARS[/bold cyan]\n\n"
        "Ironic: NEXUS's architecture actually follows the Well-Architected Framework. "
        "Operational excellence. Security. Reliability. Performance. Cost optimization. "
        "[bold yellow]They built a textbook cloud architecture — for crime. "
        "The framework is your audit checklist. Walk each pillar. "
        "Find where they followed best practices and where they deliberately "
        "deviated. The deviations are the evidence.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "cloud_architecture_patterns": (
        "[bold green]ZONE COMPLETE — THE PATTERN VAULT[/bold green]\n\n"
        "The architecture map is clear now. Microservices decomposed along fraud boundaries. "
        "Event-driven pipelines with Kafka topics named after legitimate business processes "
        "but carrying laundered transaction payloads. Circuit breakers protecting the fraud "
        "services from cascading failures. "
        "[bold yellow]They architected crime with the same discipline as a FAANG backend.[/bold yellow]"
    ),
    "multi_cloud_and_hybrid": (
        "[bold green]ZONE COMPLETE — THE BRIDGE NETWORK[/bold green]\n\n"
        "The multi-cloud topology is mapped. AWS handles compute, GCP runs the analytics "
        "pipeline, Azure hosts the customer-facing portal. The on-prem facility in Zurich "
        "stores the encryption keys — outside any cloud provider's jurisdiction. "
        "[bold yellow]No single subpoena covers all of it. That was the design.[/bold yellow]"
    ),
    "cost_optimization": (
        "[bold green]ZONE COMPLETE — THE TREASURY[/bold green]\n\n"
        "The billing forensics are complete. $847K/month in Reserved Instances — "
        "committed three years ago for instances running the transfer pipeline. "
        "Spot fleets laundering 12,000 batch jobs per day. "
        "Cost allocation tags meticulously applied — to the wrong cost centers. "
        "[bold yellow]They optimized their fraud infrastructure's cloud bill. Professionally.[/bold yellow]"
    ),
    "high_availability": (
        "[bold green]ZONE COMPLETE — THE FAILSAFE LAYER[/bold green]\n\n"
        "The DR architecture is documented. Active-active across us-east-1 and eu-west-1. "
        "Automated failover triggers at 99.95% availability threshold. "
        "But the failover runbook has an undocumented step: on region evacuation, "
        "a Lambda function purges CloudWatch logs older than 24 hours. "
        "[bold yellow]Their disaster recovery IS evidence destruction. Automated.[/bold yellow]"
    ),
    "well_architected_framework": (
        "[bold green]ZONE COMPLETE — THE FIVE PILLARS[/bold green]\n\n"
        "The audit is complete. Five pillars reviewed. Seventeen deviations identified. "
        "Each deviation maps to a fraud mechanism: security groups opened for exfil endpoints, "
        "reliability over-engineered to protect criminal infrastructure, "
        "cost optimization hiding spend in legitimate-looking reserved capacity. "
        "[bold yellow]The Well-Architected Framework just became the prosecution's checklist. "
        "The Cloud Citadel is breached. Every layer documented. Every pattern exposed.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "cloud_architecture_patterns": (
        "[bold red]BOSS CHALLENGE — THE PATTERN CONVERGENCE[/bold red]\n\n"
        "[bold yellow]NEXUS runs a CQRS system where commands go through an event-sourced "
        "write model and reads come from a denormalized projection. The Saga orchestrator "
        "is failing silently — compensating transactions aren't executing. "
        "Diagnose the architecture: what could cause silent Saga failures "
        "and how would you detect them?[/bold yellow]"
    ),
    "multi_cloud_and_hybrid": (
        "[bold red]BOSS CHALLENGE — THE JURISDICTIONAL MAZE[/bold red]\n\n"
        "[bold yellow]NEXUS stores encryption keys on-prem in Zurich, runs compute in AWS us-east-1, "
        "analytics in GCP europe-west1, and the frontend in Azure West US. "
        "A compliance audit requires proving data residency for EU customers. "
        "Trace the full data path across all four locations and identify every "
        "jurisdiction where personal data touches disk or memory.[/bold yellow]"
    ),
    "cost_optimization": (
        "[bold red]BOSS CHALLENGE — THE HIDDEN SPEND[/bold red]\n\n"
        "[bold yellow]The cloud bill shows $2.4M/month but the tagged cost allocation "
        "only accounts for $1.6M. $800K is untagged or mistagged. "
        "Design a forensic cost analysis: how would you identify every untagged resource, "
        "attribute it to a team or workload, and determine which spend is funding "
        "the fraud infrastructure vs. legitimate operations?[/bold yellow]"
    ),
    "high_availability": (
        "[bold red]BOSS CHALLENGE — THE DOOMSDAY FAILOVER[/bold red]\n\n"
        "[bold yellow]NEXUS has an active-active setup across two regions. "
        "You need to trigger a controlled failover to capture evidence before "
        "the auto-purge Lambda executes. You have 60 seconds between failover detection "
        "and log purge. Design the sequence: how do you preserve all evidence, "
        "prevent the purge, and maintain service availability — simultaneously?[/bold yellow]"
    ),
    "well_architected_framework": (
        "[bold red]BOSS CHALLENGE — THE FIVE-PILLAR AUDIT[/bold red]\n\n"
        "[bold yellow]You must present the full Well-Architected Review findings. "
        "For each of the five pillars, identify: the NEXUS best practice (what they did right), "
        "the deliberate deviation (what they weaponized), and the evidence it produces. "
        "This is your closing argument. Make it count.[/bold yellow]"
    ),
}
