"""
story.py — Narrative for The Cluster (Kubernetes) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — TIER 4 ACCESS GRANTED[/bold red]

You've compromised the server. You've read the filesystem.
But the real infrastructure isn't on bare metal anymore.

[bold yellow]NEXUS Corp moved everything to Kubernetes three years ago.[/bold yellow]
Every microservice, every database proxy, every internal API —
running inside containers, inside pods, inside a managed cluster.

You pull up the kubeconfig file left cached in /root/.kube/config.
Your terminal connects.

[bold cyan]$ kubectl get nodes[/bold cyan]

[dim]NAME                 STATUS   ROLES           AGE
nexus-node-01        Ready    control-plane   847d
nexus-node-02        Ready    worker          847d
nexus-node-03        Ready    worker          847d[/dim]

[bold white]Three nodes. Hundreds of pods. Somewhere in there — the evidence.[/bold white]

The cluster is live. The fraud runs inside it.
Time to learn how to navigate.
"""

ZONE_INTROS = {
    "pods_and_deployments": (
        "[bold cyan]ZONE: POD BAY[/bold cyan]\n\n"
        "The cluster's basic units are pods — containers wrapped in metadata, "
        "scheduled across nodes by an algorithm that doesn't care what the containers do. "
        "[bold yellow]Learn to list them, watch them, understand what keeps them running.[/bold yellow]"
    ),
    "services_and_networking": (
        "[bold cyan]ZONE: THE MESH[/bold cyan]\n\n"
        "Pods die and are reborn with new IPs. Services are the stable names that survive. "
        "[bold yellow]Find the internal DNS names. Find the ports. Map the traffic flow "
        "from the ingress controller down to the fraud-processing pods.[/bold yellow]"
    ),
    "configmaps_and_secrets": (
        "[bold cyan]ZONE: THE VAULT[/bold cyan]\n\n"
        "The credentials are in here somewhere. Database passwords. API keys. "
        "All stored as Kubernetes Secrets — base64 encoded, not encrypted. "
        "[bold yellow]Understand how they're mounted. Understand how to read them.[/bold yellow]"
    ),
    "namespaces_and_rbac": (
        "[bold cyan]ZONE: ACCESS CONTROL[/bold cyan]\n\n"
        "The cluster is divided into namespaces. Each division has its own RBAC rules. "
        "[bold yellow]The 'finance' namespace is locked down. "
        "But the service account you have might have a misconfigured RoleBinding. "
        "Find the gap.[/bold yellow]"
    ),
    "helm_charts": (
        "[bold cyan]ZONE: THE DEPLOYMENT HISTORY[/bold cyan]\n\n"
        "NEXUS Corp uses Helm to manage its deployments. "
        "Every chart has a history. Every upgrade has a log. "
        "[bold yellow]The version timestamps might match the fraud window. "
        "Learn to read them.[/bold yellow]"
    ),
    "persistent_volumes": (
        "[bold cyan]ZONE: THE STORAGE LAYER[/bold cyan]\n\n"
        "The fraud engine isn't stateless. It has to persist its ledger somewhere inside the cluster. "
        "[bold yellow]Find the PersistentVolumeClaims. Find what's bound to them. "
        "The evidence is on a volume — and volumes outlive pods.[/bold yellow]"
    ),
    "resource_management": (
        "[bold cyan]ZONE: RESOURCE ALLOCATION[/bold cyan]\n\n"
        "The fraud-processing namespace has no ResourceQuotas, no LimitRanges. "
        "It's been consuming 40% of cluster CPU for two years without anyone noticing. "
        "[bold yellow]Understand how resource requests and limits work. "
        "Understand how the HPA kept it scaled up — always.[/bold yellow]"
    ),
    "network_policies": (
        "[bold cyan]ZONE: THE FIREWALL GAPS[/bold cyan]\n\n"
        "There are no NetworkPolicies in the NEXUS cluster. None. "
        "Every pod can reach every other pod, every database, every API endpoint. "
        "[bold yellow]Learn how NetworkPolicies work — because understanding the absence "
        "of them explains how the fraud data moved so freely.[/bold yellow]"
    ),
    "cluster_troubleshooting": (
        "[bold cyan]ZONE: FORENSIC MODE[/bold cyan]\n\n"
        "Some pods are crashing. That's suspicious — or useful. "
        "[bold yellow]Crashed pods leave logs. Previous container logs. Events. "
        "Someone tried to cover their tracks. The cluster remembers anyway.[/bold yellow]"
    ),
    "statefulsets_and_daemonsets": (
        "[bold cyan]ZONE: THE ORDERED MACHINES[/bold cyan]\n\n"
        "The fraud database isn't a Deployment. It's a StatefulSet. "
        "Each pod has a stable identity. Each pod has its own storage. "
        "[bold yellow]pod-0, pod-1, pod-2 — three replicas of the ledger, "
        "each holding a shard of the transaction history. "
        "Understand StatefulSets and you understand how the data was structured.[/bold yellow]"
    ),
    "ingress_and_jobs": (
        "[bold cyan]ZONE: THE ENTRY POINTS[/bold cyan]\n\n"
        "Everything reaches the cluster through the Ingress controller. "
        "Every batch cleanup task ran as a Job. "
        "[bold yellow]Ingress routing rules define what was publicly reachable. "
        "Job history shows what automated tasks ran — and when. "
        "The evidence packager ran as a CronJob for eleven years.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "pods_and_deployments": (
        "[bold green]ZONE COMPLETE — POD BAY[/bold green]\n\n"
        "You can see every running workload in the cluster. "
        "The fraud-processing deployment: 12 replicas, always running. "
        "[bold yellow]Someone didn't want it to go down.[/bold yellow]"
    ),
    "services_and_networking": (
        "[bold green]ZONE COMPLETE — THE MESH[/bold green]\n\n"
        "Traffic map acquired. The `transaction-processor` service routes to 12 pods. "
        "All behind an ingress with no authentication. "
        "[bold yellow]That's your entry point into the live data.[/bold yellow]"
    ),
    "configmaps_and_secrets": (
        "[bold green]ZONE COMPLETE — THE VAULT[/bold green]\n\n"
        "The database credentials are in a Secret named `db-master-creds`. "
        "Not encrypted. Not rotated in 847 days. "
        "[bold yellow]That's the connection string to the fraud archive.[/bold yellow]"
    ),
    "namespaces_and_rbac": (
        "[bold green]ZONE COMPLETE — ACCESS CONTROL[/bold green]\n\n"
        "Found it: a service account in the `monitoring` namespace "
        "with a RoleBinding that grants it read access to the `finance` namespace. "
        "[bold yellow]Someone forgot that monitoring can see everything.[/bold yellow]"
    ),
    "helm_charts": (
        "[bold green]ZONE COMPLETE — DEPLOYMENT HISTORY[/bold green]\n\n"
        "`helm history fraud-engine` — 47 releases. "
        "The first release was 3 days after the CFO joined. "
        "[bold yellow]The timestamps tell the whole story.[/bold yellow]"
    ),
    "persistent_volumes": (
        "[bold green]ZONE COMPLETE — THE STORAGE LAYER[/bold green]\n\n"
        "Found it: a PVC named `ledger-data` bound to a 500Gi EBS volume. "
        "The PVC has `reclaimPolicy: Retain` — whoever set this up knew the data needed to survive. "
        "[bold yellow]The volume contains eleven years of raw transaction logs. "
        "Uncompressed. Unencrypted. Waiting.[/bold yellow]"
    ),
    "resource_management": (
        "[bold green]ZONE COMPLETE — RESOURCE ALLOCATION[/bold green]\n\n"
        "The HPA target: 80% CPU. The fraud pods never dropped below 78%. "
        "Someone tuned this to keep the scaling active at all times — "
        "always 12 replicas, always processing. "
        "[bold yellow]The resource configuration is evidence of intent.[/bold yellow]"
    ),
    "network_policies": (
        "[bold green]ZONE COMPLETE — THE FIREWALL GAPS[/bold green]\n\n"
        "Zero NetworkPolicies. The `finance` namespace: fully reachable from `monitoring`, "
        "`logging`, `ingress`, and every other namespace. "
        "The fraud pod had unrestricted egress to the Lambda function endpoints. "
        "[bold yellow]The absence of controls was the control.[/bold yellow]"
    ),
    "cluster_troubleshooting": (
        "[bold green]ZONE COMPLETE — FORENSIC MODE[/bold green]\n\n"
        "The previous logs of the `audit-eraser` pod — still there. "
        "Kubernetes held onto them. "
        "[bold yellow]The audit logs weren't erased. They were moved. "
        "And you know where they went.[/bold yellow]"
    ),
    "statefulsets_and_daemonsets": (
        "[bold green]ZONE COMPLETE — THE ORDERED MACHINES[/bold green]\n\n"
        "The StatefulSet: `fraud-db`. Three replicas. "
        "pod-0 holds the primary shard — 847GB. The PVC is still bound. "
        "The DaemonSet log collector on every node has been shipping to an external endpoint "
        "for three years. [bold yellow]Not CloudWatch. Not S3. An external IP.[/bold yellow]"
    ),
    "ingress_and_jobs": (
        "[bold green]ZONE COMPLETE — THE ENTRY POINTS[/bold green]\n\n"
        "The CronJob: `evidence-packager`. Schedule: `0 3 * * *`. "
        "Running since cluster creation. Creating an archive, encrypting it, "
        "shipping it to an S3 bucket not in this account. "
        "[bold yellow]It ran last night. You have less time than you thought.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "pods_and_deployments": (
        "[bold red]BOSS CHALLENGE — THE PHANTOM WORKLOAD[/bold red]\n\n"
        "[bold yellow]There's a Deployment with no labels, no name in any chart, "
        "running since before the Kubernetes migration. "
        "What keeps it alive? Where is it scheduled? No hints — just `kubectl`.[/bold yellow]"
    ),
    "services_and_networking": (
        "[bold red]BOSS CHALLENGE — THE INVISIBLE ROUTE[/bold red]\n\n"
        "[bold yellow]Traffic is reaching a pod that has no Service. "
        "No ingress rule points to it. But packets arrive. "
        "Explain how. Prove you understand every path traffic can take.[/bold yellow]"
    ),
    "configmaps_and_secrets": (
        "[bold red]BOSS CHALLENGE — THE DOUBLE-MOUNTED SECRET[/bold red]\n\n"
        "[bold yellow]A Pod mounts the same Secret both as an env var AND as a file. "
        "The env var shows one value. The file shows another. "
        "How is this possible? What happened?[/bold yellow]"
    ),
    "namespaces_and_rbac": (
        "[bold red]BOSS CHALLENGE — THE PRIVILEGE ESCALATION[/bold red]\n\n"
        "[bold yellow]A ServiceAccount has only `get` permission on Pods. "
        "Show the chain of steps that could let it read Secrets anyway. "
        "Think through every indirect path.[/bold yellow]"
    ),
    "helm_charts": (
        "[bold red]BOSS CHALLENGE — THE DRIFT DETECTION[/bold red]\n\n"
        "[bold yellow]The running cluster state doesn't match the Helm release. "
        "Resources were modified outside Helm. "
        "Which command reveals the drift? What happened to the release history?[/bold yellow]"
    ),
    "persistent_volumes": (
        "[bold red]BOSS CHALLENGE — THE ORPHANED VOLUME[/bold red]\n\n"
        "[bold yellow]A PVC was deleted but the PV has `reclaimPolicy: Retain`. "
        "The PV is now in Released state — the data still exists. "
        "Walk through every step needed to re-bind that PV to a new PVC "
        "and mount it in a new Pod to recover the data.[/bold yellow]"
    ),
    "resource_management": (
        "[bold red]BOSS CHALLENGE — THE RUNAWAY WORKLOAD[/bold red]\n\n"
        "[bold yellow]A namespace has no ResourceQuota. A single Deployment scaled to 200 replicas "
        "and consumed all cluster memory. Other workloads are being evicted. "
        "Walk through every step — in order — to stabilize the cluster "
        "without losing in-flight data.[/bold yellow]"
    ),
    "network_policies": (
        "[bold red]BOSS CHALLENGE — THE POLICY AUDIT[/bold red]\n\n"
        "[bold yellow]The `finance` namespace needs to: accept traffic only from `api-gateway`, "
        "connect out only to `postgres` and a specific external IP, "
        "and block all other ingress and egress. "
        "Write the complete NetworkPolicy spec — including the default deny rules — "
        "that achieves this.[/bold yellow]"
    ),
    "cluster_troubleshooting": (
        "[bold red]BOSS CHALLENGE — THE FORENSIC FINAL[/bold red]\n\n"
        "[bold yellow]A Pod ran for 12 hours, produced critical output, then was deleted. "
        "The logs are gone. The events have expired. "
        "What mechanisms could have preserved that evidence? "
        "What should have been configured from the start?[/bold yellow]"
    ),
    "statefulsets_and_daemonsets": (
        "[bold red]BOSS CHALLENGE — THE STATEFUL INTERROGATION[/bold red]\n\n"
        "[bold yellow]The `fraud-db` StatefulSet must be scaled down from 3 to 1 replica safely "
        "to preserve pod-0's data for extraction. Describe every step: "
        "the termination order, what happens to pod-1 and pod-2's PVCs, "
        "how to verify pod-0 is healthy before extraction begins, "
        "and why using `kubectl delete pod` instead of scaling down would be dangerous.[/bold yellow]"
    ),
    "ingress_and_jobs": (
        "[bold red]BOSS CHALLENGE — THE CRON INTERCEPT[/bold red]\n\n"
        "[bold yellow]The `evidence-packager` CronJob runs at `0 3 * * *`. It's 02:47. "
        "You have 13 minutes. Describe every kubectl command to: "
        "suspend the CronJob immediately, verify no active Jobs are running, "
        "patch the Job template to point its output to your own S3 bucket, "
        "and re-enable the CronJob — all without deleting it "
        "so the attacker doesn't know you've been here.[/bold yellow]"
    ),
}
