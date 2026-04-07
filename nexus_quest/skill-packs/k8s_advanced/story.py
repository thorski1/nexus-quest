"""
story.py — Narrative for The Cluster Depths (Advanced Kubernetes) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — TIER 7 ACCESS GRANTED[/bold red]

You cracked the cluster once. Pods, Services, ConfigMaps — child's play now.
But the real infrastructure was always deeper.

[bold yellow]NEXUS Corp's architects built a second layer.[/bold yellow]
Custom operators that self-heal. Service meshes that encrypt pod-to-pod traffic.
CSI drivers that provision encrypted volumes on demand.
RBAC policies so tangled that three former SREs quit rather than audit them.

You pull up the kubeconfig. This time the prompt looks different.

[bold cyan]$ kubectl get crds | wc -l[/bold cyan]

[dim]147[/dim]

[bold cyan]$ kubectl get nodes -o wide[/bold cyan]

[dim]NAME                 STATUS   ROLES           AGE    VERSION   INTERNAL-IP    OS-IMAGE
nexus-core-01        Ready    control-plane   1204d  v1.29.2   10.0.0.11      Ubuntu 22.04
nexus-core-02        Ready    control-plane   1204d  v1.29.2   10.0.0.12      Ubuntu 22.04
nexus-core-03        Ready    control-plane   1204d  v1.29.2   10.0.0.13      Ubuntu 22.04
nexus-worker-01      Ready    worker          1204d  v1.29.2   10.0.1.11      Ubuntu 22.04
nexus-worker-02      Ready    worker          1204d  v1.29.2   10.0.1.12      Ubuntu 22.04
nexus-worker-03      Ready    worker          847d   v1.28.6   10.0.1.13      Ubuntu 22.04
nexus-worker-04      Ready    worker          847d   v1.28.6   10.0.1.14      Ubuntu 22.04
nexus-gpu-01         Ready    worker          302d   v1.29.2   10.0.2.11      Ubuntu 22.04[/dim]

[bold white]Eight nodes. Three control planes. Version skew on two workers.
147 Custom Resource Definitions. A Cilium mesh. Encrypted etcd.
This is production-grade chaos.[/bold white]

The surface cluster was a decoy. The real operation runs here —
in the depths where only senior engineers tread.

[bold red]Time to go deeper.[/bold red]
"""

ZONE_INTROS = {
    "custom_resources_operators": (
        "[bold cyan]ZONE: THE OPERATOR VAULT[/bold cyan]\n\n"
        "Standard Kubernetes resources weren't enough for NEXUS. "
        "They built custom operators — autonomous controllers that watch custom resources "
        "and reconcile state without human intervention. "
        "[bold yellow]CRDs, controller-runtime, finalizers, owner references — "
        "the operator pattern is how the fraud system became self-healing. "
        "Understand it or you'll never shut it down.[/bold yellow]"
    ),
    "networking_deep_dive": (
        "[bold cyan]ZONE: THE DEEP MESH[/bold cyan]\n\n"
        "Forget ClusterIP services. The real networking layer is three levels down. "
        "Cilium replaced kube-proxy. eBPF programs route packets in kernel space. "
        "Istio sidecars encrypt every hop with mTLS. "
        "[bold yellow]The fraud traffic is invisible to standard `tcpdump` — "
        "it's wrapped in service mesh encryption. Learn how it flows, "
        "or you'll never intercept it.[/bold yellow]"
    ),
    "storage_statefulsets": (
        "[bold cyan]ZONE: THE PERSISTENCE ENGINE[/bold cyan]\n\n"
        "The fraud ledger isn't just a PVC anymore. It's a distributed storage system — "
        "CSI drivers provisioning encrypted EBS volumes, StorageClasses with custom parameters, "
        "volume snapshots taken every 6 hours. "
        "[bold yellow]The data is replicated across three availability zones. "
        "You need to understand the entire storage stack to find every copy.[/bold yellow]"
    ),
    "security_rbac": (
        "[bold cyan]ZONE: THE IDENTITY LABYRINTH[/bold cyan]\n\n"
        "The cluster's RBAC configuration is 4,000 lines of YAML. "
        "ServiceAccounts with cross-namespace bindings. Pod Security Admission replacing PSPs. "
        "Secrets encrypted at rest with a KMS plugin. OPA Gatekeeper enforcing admission policies. "
        "[bold yellow]Somewhere in this labyrinth, there's a privilege escalation path "
        "that the fraud operators used. Find it.[/bold yellow]"
    ),
    "cluster_operations": (
        "[bold cyan]ZONE: THE CONTROL PLANE[/bold cyan]\n\n"
        "Two workers are running v1.28.6 while the rest are on v1.29.2. "
        "The etcd cluster hasn't been backed up in 90 days. "
        "Node affinity rules are scattering fraud pods across all workers. "
        "[bold yellow]You need to understand cluster upgrades, etcd operations, "
        "node management, and cost optimization to take control of this infrastructure. "
        "The fraud operators knew these systems better than the SRE team.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "custom_resources_operators": (
        "[bold green]ZONE COMPLETE — THE OPERATOR VAULT[/bold green]\n\n"
        "You've mapped every CRD in the cluster. The `FraudPipeline` custom resource "
        "has a controller that auto-recreates itself if deleted. Finalizers block removal. "
        "Owner references cascade through three layers of resources. "
        "[bold yellow]The operator is the immune system. Now you know how to bypass it.[/bold yellow]"
    ),
    "networking_deep_dive": (
        "[bold green]ZONE COMPLETE — THE DEEP MESH[/bold green]\n\n"
        "You've traced the packet path: Cilium eBPF → Envoy sidecar → mTLS tunnel → "
        "destination pod. The `CiliumNetworkPolicy` allows egress to three external IPs "
        "that don't belong to any known NEXUS account. "
        "[bold yellow]The exfiltration endpoints are in the network policy itself.[/bold yellow]"
    ),
    "storage_statefulsets": (
        "[bold green]ZONE COMPLETE — THE PERSISTENCE ENGINE[/bold green]\n\n"
        "Three `VolumeSnapshots` taken at 03:00 UTC — right after the CronJob runs. "
        "The CSI driver encrypts at rest with a KMS key that rotates monthly. "
        "But the snapshot from 90 days ago used the old key — and that key is still in etcd. "
        "[bold yellow]You have the key. You have the snapshot. You have the data.[/bold yellow]"
    ),
    "security_rbac": (
        "[bold green]ZONE COMPLETE — THE IDENTITY LABYRINTH[/bold green]\n\n"
        "Found the escalation path: a ServiceAccount in `monitoring` has `escalate` verb on Roles. "
        "It can create RoleBindings that grant more permissions than it holds. "
        "OPA Gatekeeper has an exception for the `system:fraud-controller` group. "
        "[bold yellow]The backdoor was in the admission policy exceptions.[/bold yellow]"
    ),
    "cluster_operations": (
        "[bold green]ZONE COMPLETE — THE CONTROL PLANE[/bold green]\n\n"
        "The version-skewed workers are running the fraud pods — pinned there by nodeAffinity. "
        "Upgrading those nodes would force a reschedule and break the pipeline. "
        "The etcd backup gap is intentional — no snapshots means no forensic recovery of deleted CRDs. "
        "[bold yellow]Every operational gap was engineered. Now you control the plane.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "custom_resources_operators": (
        "[bold red]BOSS CHALLENGE — THE UNKILLABLE OPERATOR[/bold red]\n\n"
        "[bold yellow]The `fraud-controller` operator watches a CRD called `FraudPipeline`. "
        "Deleting the CR triggers a finalizer that recreates it. "
        "Deleting the operator Deployment triggers the operator's own operator. "
        "Describe the exact sequence of operations to permanently remove this self-healing system "
        "without triggering any reconciliation loops.[/bold yellow]"
    ),
    "networking_deep_dive": (
        "[bold red]BOSS CHALLENGE — THE INVISIBLE EXFILTRATION[/bold red]\n\n"
        "[bold yellow]Data is leaving the cluster but `kubectl get networkpolicy` shows deny-all. "
        "Cilium is running in full enforcement mode. No NodePort services exist. "
        "Yet 500MB leaves every night at 03:00. "
        "Explain every possible mechanism for this exfiltration "
        "and which Cilium/Hubble commands would prove it.[/bold yellow]"
    ),
    "storage_statefulsets": (
        "[bold red]BOSS CHALLENGE — THE SNAPSHOT HEIST[/bold red]\n\n"
        "[bold yellow]You need to recover data from a VolumeSnapshot that was created by a CSI driver "
        "using a KMS key you don't have direct access to. The snapshot is 90 days old. "
        "The key was rotated. Walk through every step: finding the old key ID in etcd, "
        "creating a new PVC from the snapshot, and mounting it in an ephemeral debug pod "
        "to extract the fraud ledger — all without alerting the monitoring stack.[/bold yellow]"
    ),
    "security_rbac": (
        "[bold red]BOSS CHALLENGE — THE RBAC MAZE[/bold red]\n\n"
        "[bold yellow]Starting from a ServiceAccount that has only `get` on `pods` in namespace `default`, "
        "chain together a privilege escalation using: a misconfigured RoleBinding, "
        "a pod with `automountServiceAccountToken: true` running in a privileged namespace, "
        "and a token review API exploit. Show every kubectl command in the chain "
        "and explain why each step is possible.[/bold yellow]"
    ),
    "cluster_operations": (
        "[bold red]BOSS CHALLENGE — THE ZERO-DOWNTIME TAKEOVER[/bold red]\n\n"
        "[bold yellow]You need to: upgrade two version-skewed workers from v1.28.6 to v1.29.2, "
        "take an etcd snapshot without stopping the API server, "
        "drain the fraud pods to nodes you control using taints and tolerations, "
        "and rotate all ServiceAccount tokens — in that order, "
        "with zero downtime to the fraud pipeline (so they don't notice). "
        "Describe every command and the exact risk at each step.[/bold yellow]"
    ),
}
