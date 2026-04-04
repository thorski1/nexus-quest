"""
IaC skill pack narrative — The Blueprint Engine
"""

INTRO_STORY = """
[bold cyan]◈◈◈  THE NEXUS FILES — THE BLUEPRINT ENGINE  ◈◈◈[/bold cyan]

[dim]You've traced the money. You've mapped the accounts.
But the infrastructure that powers the operation — the servers, the pipelines,
the policies — none of it was built by hand. It was engineered.
Codified. Version-controlled. Automated.[/dim]

[bold white]CIPHER: 'They didn't just use Terraform. That was one layer.
The real operation runs on a stack of IaC tools — Pulumi for the
compute layer, Ansible for server configuration, ArgoCD syncing
Kubernetes manifests from a private Git repo. And every tool
has its own state, its own audit trail, its own evidence.'[/bold white]

[dim]You pull the Git history. Hundreds of commits across
four repositories. Infrastructure definitions in TypeScript,
YAML playbooks, Kubernetes manifests, OPA policies.
Each repo tells a different part of the story.[/dim]

[bold yellow]git log --all --oneline | wc -l
    847[/bold yellow]

[dim]Eight hundred and forty-seven commits.
Every provisioning decision. Every scaling event.
Every policy exception they granted themselves.
The blueprint isn't one file — it's an engine.
And now you need to understand how every part works.[/dim]

[bold cyan]Master the IaC stack. Read the engine. Own the infrastructure.[/bold cyan]
"""

ZONE_INTROS = {
    "iac_fundamentals": (
        "[bold cyan]◈  ZONE 1: IAC FUNDAMENTALS  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Before you dig into specific tools, you need to understand"
        " the philosophy. Declarative vs imperative. Idempotency. Drift."
        " State. These concepts cut across every IaC tool — Terraform,"
        " Pulumi, CloudFormation, Ansible. Get these wrong and you'll"
        " misread every config you find.'[/bold white]\n\n"
        "[dim]You open the first repository. The README references"
        " 'idempotent provisioning' and 'drift detection.'"
        " The commit messages mention 'convergence failures.'"
        " You need the vocabulary before you can read the code.[/dim]"
    ),
    "pulumi_and_cdk": (
        "[bold cyan]◈  ZONE 2: PULUMI & CDK  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The compute layer isn't Terraform. It's Pulumi —"
        " TypeScript, full programming language, real loops and conditionals."
        " And for the AWS-native services, they used CDK."
        " Same idea: infrastructure defined in code, not config."
        " But this code is harder to read. It's dense. Abstract."
        " You need to understand constructs, stacks, and outputs.'[/bold white]\n\n"
        "[dim]The Pulumi repo is 40 TypeScript files. Classes, interfaces,"
        " async functions generating infrastructure. A ComponentResource"
        " called 'SubsidiaryStack' that takes a config object and"
        " provisions an entire environment. This is a different level"
        " of IaC sophistication.[/dim]"
    ),
    "ansible_config_mgmt": (
        "[bold cyan]◈  ZONE 3: ANSIBLE & CONFIGURATION MANAGEMENT  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Provisioning creates the servers. Configuration management"
        " sets them up. Ansible playbooks install software, deploy configs,"
        " manage services, enforce state. The operation's servers weren't"
        " hand-configured — every one was Ansible-managed."
        " Roles for the proxy tier. Roles for the data exfil nodes."
        " All in YAML. All version-controlled.'[/bold white]\n\n"
        "[dim]You find the Ansible repository. Sixty-three roles."
        " An inventory file with dynamic groups pulled from AWS."
        " Playbooks that run at 3 AM via cron. Handlers that"
        " restart services when configs change. This is how"
        " they kept hundreds of servers in lockstep.[/dim]"
    ),
    "gitops_and_argocd": (
        "[bold cyan]◈  ZONE 4: GITOPS & ARGOCD  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The Kubernetes layer is pure GitOps. ArgoCD"
        " watches a Git repo, syncs manifests to the cluster,"
        " and self-heals any drift. Nobody runs kubectl apply."
        " Push to Git, ArgoCD deploys. That means the Git history"
        " IS the deployment history. Every merge is a deployment."
        " Every revert is a rollback. It's all there.'[/bold white]\n\n"
        "[dim]The ArgoCD dashboard shows 23 applications."
        " All synced. All healthy. An App of Apps pattern"
        " bootstrapping the entire cluster from a single"
        " root application. The reconciliation loop runs"
        " every 3 minutes. Any manual change gets overwritten."
        " Git is the only way in.[/dim]"
    ),
    "iac_testing_and_security": (
        "[bold cyan]◈  ZONE 5: IAC TESTING & SECURITY  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Here's where it gets interesting. They had"
        " security scanning — Checkov, tfsec, OPA policies."
        " But look closer. The OPA policies have exceptions."
        " Certain resource types bypass encryption checks."
        " Certain namespaces skip network policy enforcement."
        " The security tooling was there — with carefully crafted"
        " holes exactly where the operation needed them.'[/bold white]\n\n"
        "[dim]You read the Rego policies. Hundreds of rules."
        " Professional, thorough, well-documented."
        " And then you find the exception list."
        " Six resource patterns excluded from deny rules."
        " Six patterns that match the fraud infrastructure"
        " exactly. The security was real. The exceptions"
        " were the crime.[/dim]"
    ),
}

ZONE_COMPLETIONS = {
    "iac_fundamentals": (
        "[bold green]✓  IAC FOUNDATIONS LOCKED[/bold green]\n\n"
        "[dim]Declarative, imperative, idempotent, convergent —"
        " the vocabulary is yours now. You can read any IaC config"
        " and understand the philosophy behind it."
        " Drift is no longer an abstract concept."
        " You know what to look for.[/dim]"
    ),
    "pulumi_and_cdk": (
        "[bold green]✓  PROGRAMMATIC IAC DECODED[/bold green]\n\n"
        "[dim]TypeScript infrastructure. ComponentResources."
        " Stacks and outputs. The Pulumi codebase is readable now."
        " You can trace the SubsidiaryStack constructor and see"
        " exactly what resources each instance provisions."
        " The CDK constructs map to CloudFormation stacks."
        " Both paths documented.[/dim]"
    ),
    "ansible_config_mgmt": (
        "[bold green]✓  CONFIGURATION LAYER MAPPED[/bold green]\n\n"
        "[dim]Sixty-three roles catalogued. The inventory cross-referenced"
        " with the AWS account. Dynamic groups confirmed —"
        " every server tagged for the operation was in the"
        " playbook's target list. The 3 AM cron schedule"
        " matches the fund transfer windows.[/dim]"
    ),
    "gitops_and_argocd": (
        "[bold green]✓  GITOPS PIPELINE TRACED[/bold green]\n\n"
        "[dim]Every deployment is a Git commit. Every rollback"
        " is a revert. The ArgoCD application manifests are"
        " preserved. Twenty-three applications. The sync history"
        " tells you exactly when each service was deployed,"
        " updated, and scaled. The deployment timeline"
        " is the operation timeline.[/dim]"
    ),
    "iac_testing_and_security": (
        "[bold green]✓  BLUEPRINT ENGINE FULLY MAPPED[/bold green]\n\n"
        "[bold white]CIPHER: 'That's the complete IaC stack. Provisioning,"
        " configuration, deployment, and security — all codified,"
        " all version-controlled, all evidence.\n\n"
        "The six OPA exceptions are the smoking gun."
        " Professional-grade security tooling with surgical holes."
        " Someone who understood policy-as-code used that knowledge"
        " to create the perfect blind spots.\n\n"
        "The Blueprint Engine is mapped. Every tool, every config,"
        " every exception. The infrastructure tells the story.'[/bold white]\n\n"
        "[dim]You archive the complete IaC evidence package."
        " Four repositories. Eight hundred and forty-seven commits."
        " Five layers of infrastructure automation."
        " One deliberate, engineered operation.[/dim]"
    ),
}

BOSS_INTROS = {
    "iac_fundamentals": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: DRIFT DETECTION  ◈[/bold red]\n\n"
        "[bold white]'You know the theory. Now prove it. When infrastructure"
        " drifts from its declared state, you need to predict exactly"
        " what the IaC tool will do on the next run."
        " Read the scenario. Predict the outcome.'[/bold white]"
    ),
    "pulumi_and_cdk": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: RESOURCE RESOLUTION  ◈[/bold red]\n\n"
        "[bold white]'The Pulumi code creates a bucket with a logical name."
        " But logical names and physical names aren't the same thing"
        " in Pulumi. If you can't trace a logical resource to its"
        " physical counterpart, you can't map the infrastructure."
        " Read the code. What actually gets created?'[/bold white]"
    ),
    "ansible_config_mgmt": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: HANDLER LOGIC  ◈[/bold red]\n\n"
        "[bold white]'The Ansible playbooks use handlers to restart services"
        " after configuration changes. Understanding when a handler"
        " fires and when it doesn't is the difference between"
        " knowing which servers were reconfigured and which"
        " were left untouched. Read the play. Predict the behavior.'[/bold white]"
    ),
    "gitops_and_argocd": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: RECONCILIATION OVERRIDE  ◈[/bold red]\n\n"
        "[bold white]'Someone tried to manually scale a deployment in the cluster."
        " ArgoCD is watching. Self-heal is on. Auto-sync is enabled."
        " What happens next? If you understand the reconciliation loop,"
        " you know the answer before it happens.'[/bold white]"
    ),
    "iac_testing_and_security": (
        "[bold red]◈  CIPHER FINAL BOSS: THE POLICY EXCEPTION  ◈[/bold red]\n\n"
        "[bold white]'The OPA policy is clear: no unencrypted S3 buckets."
        " But someone submitted a plan with an unencrypted bucket."
        " Read the Rego. Understand the deny rule."
        " What does the policy engine do? This is where"
        " security automation meets infrastructure reality."
        " Read it. Understand it. That's the evidence.'[/bold white]"
    ),
}
