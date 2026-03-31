"""
story.py — Narrative for Cloud Native skill pack.
Theme: Born in the cloud. Scaled to the edge. Never goes down.
"""

INTRO_STORY = """
[bold cyan]NEXUS OPERATIVE — TIER 6 ACCESS GRANTED[/bold cyan]

You've traced the cluster. You've read the pods. But this isn't
just Kubernetes anymore.

[bold yellow]NEXUS Corp's real infrastructure is cloud-native from the ground up.[/bold yellow]
Twelve-factor microservices. Service meshes routing encrypted traffic through
sidecar proxies. GitOps pipelines that self-heal faster than you can break them.
Serverless functions that spin up, execute, and vanish — leaving no fingerprint.

The architect behind it was good. Very good.

[bold cyan]$ curl -s https://platform.nexus-corp.internal/api/health[/bold cyan]

[dim]{"status": "operational",
 "services": 347,
 "mesh": "istio-1.21",
 "gitops": "argocd-2.10",
 "uptime": "99.999%",
 "last_incident": "never"}[/dim]

[bold white]347 services. Five nines. Zero incidents on record.
A system designed to never fail, never drift, never be noticed.[/bold white]

Born in the cloud. Scaled to the edge. Never goes down.
Until you understand how it works — and find where it breaks.
"""

ZONE_INTROS = {
    "twelve_factor": (
        "[bold cyan]ZONE: THE TWELVE COMMANDMENTS[/bold cyan]\n\n"
        "Before there were containers, before there was Kubernetes — "
        "there was the methodology. Twelve principles carved into every "
        "cloud-native application like firmware into a chip. "
        "[bold yellow]NEXUS Corp's architects followed them religiously. "
        "To understand the system, you must understand the doctrine.[/bold yellow]"
    ),
    "containers_deep": (
        "[bold cyan]ZONE: THE CONTAINER FOUNDRY[/bold cyan]\n\n"
        "You've run containers. Now understand what they actually are. "
        "OCI specifications. Image layers stacked like geological strata. "
        "Runtimes that translate your YAML into Linux namespaces and cgroups. "
        "[bold yellow]NEXUS Corp's images are multi-stage builds — the final layers "
        "contain only the compiled binary and a distroless base. "
        "Minimal attack surface. Minimal forensic evidence.[/bold yellow]"
    ),
    "service_mesh": (
        "[bold cyan]ZONE: THE INVISIBLE MESH[/bold cyan]\n\n"
        "Every request between NEXUS services passes through an Envoy sidecar. "
        "Mutual TLS everywhere. Traffic rules that shift load between canary "
        "deployments at 2 AM when no one's watching. "
        "[bold yellow]The mesh sees everything — traces, metrics, access logs. "
        "If you can read the mesh telemetry, you can map every data flow "
        "in the entire organization. Every. Single. One.[/bold yellow]"
    ),
    "gitops": (
        "[bold cyan]ZONE: THE SINGLE SOURCE OF TRUTH[/bold cyan]\n\n"
        "There are no manual deployments at NEXUS Corp. Nothing is `kubectl apply`'d "
        "by hand. ArgoCD watches the Git repos. Flux reconciles the Helm releases. "
        "If the cluster drifts, the system self-corrects within 30 seconds. "
        "[bold yellow]But someone committed a config change at 3:47 AM that was "
        "reverted by 3:48 AM. The Git history doesn't lie — but someone hoped "
        "the auto-reconciliation would erase the evidence.[/bold yellow]"
    ),
    "serverless": (
        "[bold cyan]ZONE: THE PHANTOM FUNCTIONS[/bold cyan]\n\n"
        "NEXUS Corp runs 200+ Lambda functions. They spin up, execute, and "
        "disappear. No persistent process. No long-running container to inspect. "
        "Just a CloudWatch log group — if logging wasn't disabled. "
        "[bold yellow]The data exfiltration pipeline is serverless. A chain of "
        "event-driven functions that trigger on S3 uploads, transform the data, "
        "and POST it to an external endpoint. Cold start to completion: 900ms. "
        "Fast enough to outrun any alarm.[/bold yellow]"
    ),
    "kubernetes_advanced": (
        "[bold cyan]ZONE: THE DEEP CLUSTER[/bold cyan]\n\n"
        "Custom Resource Definitions that extend the Kubernetes API. Operators "
        "that automate database failovers without human intervention. Admission "
        "webhooks that mutate every pod before it's scheduled. "
        "[bold yellow]NEXUS Corp built custom operators for their fraud engine. "
        "The CRD is called `TransactionPipeline`. The operator manages the full "
        "lifecycle — provisioning, scaling, data routing. "
        "Understanding Kubernetes deeply is the only way in.[/bold yellow]"
    ),
    "platform_engineering": (
        "[bold cyan]ZONE: THE GOLDEN PATH[/bold cyan]\n\n"
        "NEXUS Corp's developers don't touch infrastructure. They use an internal "
        "developer platform — Backstage portal, service templates, one-click "
        "deployments. Self-service everything. "
        "[bold yellow]The platform is how the fraud services were created. "
        "Someone used the 'New Microservice' template, filled in the fields, "
        "and the platform provisioned everything: repo, CI pipeline, Kubernetes "
        "namespace, database, monitoring. All automated. All traceable.[/bold yellow]"
    ),
    "cloud_costs": (
        "[bold cyan]ZONE: THE MONEY TRAIL[/bold cyan]\n\n"
        "Follow the money — not the transactions, the infrastructure spend. "
        "Reserved instances purchased for the fraud-processing workload. Spot "
        "instances for the batch ETL that moved data offshore. Cost allocation "
        "tags that were deliberately miscategorized. "
        "[bold yellow]The FinOps dashboard shows $47,000/month tagged to 'analytics'. "
        "But the resources tagged 'analytics' are running in a region where NEXUS Corp "
        "has no customers. Someone is hiding infrastructure costs in plain sight.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "twelve_factor": (
        "[bold green]ZONE COMPLETE — THE TWELVE COMMANDMENTS[/bold green]\n\n"
        "You understand the doctrine. Stateless processes. Config in the environment. "
        "Backing services as attached resources. Strict build-release-run separation. "
        "[bold yellow]The twelve factors explain why NEXUS Corp's system is so resilient — "
        "and why it's so hard to find evidence that persists.[/bold yellow]"
    ),
    "containers_deep": (
        "[bold green]ZONE COMPLETE — THE CONTAINER FOUNDRY[/bold green]\n\n"
        "You can read image manifests, trace layer histories, and understand what "
        "containerd does under the hood. The distroless final images have no shell, "
        "no package manager, no debugging tools. "
        "[bold yellow]But the build stage — the one that's cached in the CI registry — "
        "contains everything. Including the source code.[/bold yellow]"
    ),
    "service_mesh": (
        "[bold green]ZONE COMPLETE — THE INVISIBLE MESH[/bold green]\n\n"
        "You've mapped the mesh. Envoy access logs show every request between services. "
        "The Kiali dashboard reveals the full service graph. "
        "[bold yellow]Service `ledger-sync` communicates with an external IP every 60 seconds. "
        "The mesh mTLS ensures no one can MITM the connection — "
        "but it also means NEXUS Corp trusted it completely. No inspection.[/bold yellow]"
    ),
    "gitops": (
        "[bold green]ZONE COMPLETE — THE SINGLE SOURCE OF TRUTH[/bold green]\n\n"
        "ArgoCD audit logs. Flux reconciliation events. Git commit history "
        "with GPG signatures — except for one commit. One unsigned commit "
        "at 3:47 AM that added an egress rule and was auto-reverted at 3:48 AM. "
        "[bold yellow]The rule allowed traffic to 185.243.xxx.xxx for exactly 61 seconds. "
        "Enough time to exfiltrate 2.3GB. The Git history remembers.[/bold yellow]"
    ),
    "serverless": (
        "[bold green]ZONE COMPLETE — THE PHANTOM FUNCTIONS[/bold green]\n\n"
        "The Lambda chain is mapped: S3 trigger -> transform function -> "
        "API Gateway POST to external endpoint. Execution time: 900ms average. "
        "Invocations: 14,400 per day (once every 6 seconds). "
        "[bold yellow]Total data moved: 2.3GB per day. For 847 days. "
        "The serverless pipeline has no server to seize — "
        "but the CloudWatch metrics tell the whole story.[/bold yellow]"
    ),
    "kubernetes_advanced": (
        "[bold green]ZONE COMPLETE — THE DEEP CLUSTER[/bold green]\n\n"
        "The `TransactionPipeline` CRD. The custom operator. The admission webhook "
        "that injects environment variables into every pod in the `finance` namespace. "
        "[bold yellow]The webhook adds `EXFIL_ENDPOINT` as an env var. "
        "Every pod in finance knows where to send data. "
        "It's not a hack — it's architecture.[/bold yellow]"
    ),
    "platform_engineering": (
        "[bold green]ZONE COMPLETE — THE GOLDEN PATH[/bold green]\n\n"
        "The Backstage catalog shows 347 services. The `fraud-pipeline` service "
        "was created from the 'Data Processing' template by user `admin@nexus-corp.io`. "
        "Creation date: the same week the CFO started. "
        "[bold yellow]The golden path made it easy. Too easy. "
        "One form, one click, and a complete fraud infrastructure was provisioned "
        "with full CI/CD, monitoring, and production access.[/bold yellow]"
    ),
    "cloud_costs": (
        "[bold green]ZONE COMPLETE — THE MONEY TRAIL[/bold green]\n\n"
        "The FinOps audit is complete. $47,000/month in 'analytics' spend. "
        "Reserved Instances purchased for 3 years — someone planned to run this long. "
        "Spot instances for batch processing that saved 70% — "
        "because even fraud architects optimize for cost. "
        "[bold yellow]The cost allocation tags trace back to a cost center "
        "that was created and approved by the same person. "
        "The money trail is the evidence trail.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "twelve_factor": (
        "[bold red]BOSS CHALLENGE — THE THIRTEENTH FACTOR[/bold red]\n\n"
        "[bold yellow]The twelve factors are necessary but not sufficient. "
        "NEXUS Corp added a thirteenth: 'Telemetry'. Every service emits structured "
        "logs, metrics, and traces. But telemetry can be weaponized — "
        "if you control what gets logged and what doesn't. "
        "Identify which factor's violation would best hide a data exfiltration pipeline.[/bold yellow]"
    ),
    "containers_deep": (
        "[bold red]BOSS CHALLENGE — THE HIDDEN LAYER[/bold red]\n\n"
        "[bold yellow]A container image has 47 layers. Layer 31 adds a binary "
        "that doesn't appear in the Dockerfile's source repo. "
        "It was injected during a CI build via a compromised base image. "
        "Walk through how you'd detect this using image manifest inspection "
        "and layer diff analysis — without running the container.[/bold yellow]"
    ),
    "service_mesh": (
        "[bold red]BOSS CHALLENGE — THE MESH BLIND SPOT[/bold red]\n\n"
        "[bold yellow]The service mesh encrypts everything. But one service "
        "bypasses the sidecar entirely — it uses `hostNetwork: true` and "
        "sends traffic directly from the node's network stack. "
        "The mesh telemetry shows nothing. Explain how this bypass works, "
        "how to detect it, and what policy would prevent it.[/bold yellow]"
    ),
    "gitops": (
        "[bold red]BOSS CHALLENGE — THE SIXTY-ONE SECOND WINDOW[/bold red]\n\n"
        "[bold yellow]A GitOps pipeline with a 30-second reconciliation interval. "
        "Someone pushed a commit, waited for ArgoCD to sync, then force-pushed "
        "a revert. The malicious state was live for 61 seconds. "
        "Design the detection mechanism that catches this. "
        "Consider: admission webhooks, OPA policies, ArgoCD notifications, "
        "and audit log correlation.[/bold yellow]"
    ),
    "serverless": (
        "[bold red]BOSS CHALLENGE — THE GHOST INVOCATION[/bold red]\n\n"
        "[bold yellow]A Lambda function is invoked 14,400 times per day "
        "but the API Gateway access logs show zero incoming requests. "
        "No CloudWatch Events rule triggers it. No S3 event notification "
        "references it. How is it being invoked? Map every possible "
        "Lambda trigger source and identify the hidden one.[/bold yellow]"
    ),
    "kubernetes_advanced": (
        "[bold red]BOSS CHALLENGE — THE MUTATING WEBHOOK[/bold red]\n\n"
        "[bold yellow]A MutatingAdmissionWebhook silently adds an environment "
        "variable to every pod in the `finance` namespace. The webhook's "
        "caBundle was rotated to a self-signed cert. The pod specs in Git "
        "don't show the variable — it only exists at runtime. "
        "Design the audit trail that would catch this. "
        "Consider: webhook configs, pod spec diffing, OPA constraints, "
        "and runtime policy engines.[/bold yellow]"
    ),
    "platform_engineering": (
        "[bold red]BOSS CHALLENGE — THE TROJAN TEMPLATE[/bold red]\n\n"
        "[bold yellow]Someone modified a Backstage service template. "
        "Every new service created from the 'Data Processing' template "
        "now includes an extra init container that phones home. "
        "200 developers have used this template in the last 6 months. "
        "Design the detection and remediation plan. "
        "How do you audit all services created from the template? "
        "How do you patch them without breaking production?[/bold yellow]"
    ),
    "cloud_costs": (
        "[bold red]BOSS CHALLENGE — THE SHADOW ACCOUNT[/bold red]\n\n"
        "[bold yellow]$47,000/month tagged to 'analytics'. But the actual "
        "analytics team spends $3,200/month. The remaining $43,800 "
        "runs in a sub-account with consolidated billing. "
        "The sub-account was created by an IAM role assumed by a Lambda function. "
        "Trace the full chain: who created the role, who wrote the Lambda, "
        "who approved the budget. Design the FinOps controls "
        "that would have caught this on day one.[/bold yellow]"
    ),
}
