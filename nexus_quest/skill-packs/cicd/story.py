"""
story.py — Narrative for Pipeline Ops (CI/CD) skill pack.
Theme: The pipeline never sleeps. Build, test, deploy, repeat.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — TIER 5 ACCESS GRANTED[/bold red]

The breach didn't come through the firewall. It didn't come through
a misconfigured S3 bucket or a leaked SSH key. It came through
[bold yellow]the pipeline itself[/bold yellow].

Someone compromised the CI/CD system at NEXUS Corp — the automated
machinery that builds, tests, and deploys every line of code
that reaches production. Every microservice. Every database migration.
Every configuration change.

The pipeline runs 340 times a day. It has not stopped in 1,247 days.

[bold cyan]$ gh run list --limit 5[/bold cyan]

[dim]STATUS  NAME                    BRANCH   EVENT  DURATION
✓       deploy-production       main     push   4m 12s
✓       deploy-production       main     push   3m 58s
✓       deploy-production       main     push   4m 31s
✗       deploy-production       main     push   0m 47s
✓       deploy-production       main     push   4m 09s[/dim]

[bold white]One failure. Forty-seven seconds. Then it passed again.[/bold white]

That forty-seven-second failure was the insertion point. A poisoned
workflow file merged through an auto-approved PR. The test stage
was bypassed with a `[skip ci]` tag. The build stage injected a
backdoor into the Docker image. The deploy stage pushed it to
production before anyone looked at the diff.

[bold magenta]You are a Pipeline Forensics Operative.[/bold magenta]

You trace code from commit to container. You read workflow YAML
like other people read email. You know that the pipeline is
not just automation — it is the [bold white]chain of custody[/bold white] between
a developer's intent and what actually runs in production.

Someone broke that chain. You're going to find out how.

[bold cyan]The pipeline logs are open. The workflows are waiting. Start from the fundamentals.[/bold cyan]
"""

ZONE_INTROS = {
    "cicd_fundamentals": (
        "[bold cyan]ZONE: THE FOUNDATION[/bold cyan]\n\n"
        "Before you can trace the breach, you need to understand what you're looking at. "
        "CI/CD is not a tool — it's a philosophy. Continuous Integration. Continuous Delivery. "
        "Continuous Deployment. Three concepts that sound similar but differ in one critical way: "
        "[bold yellow]how far automation goes before a human has to say 'yes.'[/bold yellow]\n\n"
        "The pipeline is the spine of modern software delivery. Code enters at one end. "
        "Tested, validated, packaged artifacts emerge at the other. "
        "Understand the spine before you trace the nerve damage."
    ),
    "github_actions": (
        "[bold cyan]ZONE: THE WORKFLOW ENGINE[/bold cyan]\n\n"
        "NEXUS Corp runs everything through GitHub Actions. Every push, every pull request, "
        "every scheduled cron — triggers a workflow defined in YAML, living inside the repository "
        "at `.github/workflows/`. "
        "[bold yellow]The attacker modified a workflow file. The modification passed code review "
        "because no one reads YAML diffs carefully enough. "
        "You will.[/bold yellow]"
    ),
    "testing_in_pipelines": (
        "[bold cyan]ZONE: THE TEST GAUNTLET[/bold cyan]\n\n"
        "The pipeline's immune system: automated tests. Unit tests catch logic errors. "
        "Integration tests catch connection failures. End-to-end tests catch workflow breakage. "
        "Code coverage measures how much of the codebase the tests actually touch. "
        "[bold yellow]The poisoned commit bypassed every test stage. "
        "Understanding how testing gates work is how you understand how they were defeated.[/bold yellow]"
    ),
    "build_and_artifacts": (
        "[bold cyan]ZONE: THE BUILD FORGE[/bold cyan]\n\n"
        "Code doesn't deploy itself. It gets compiled, bundled, containerized — "
        "transformed from source into artifact. Docker images. Binary packages. "
        "Static bundles. Each one tagged, hashed, and stored in a registry. "
        "[bold yellow]The backdoor was injected during the Docker build stage. "
        "A modified Dockerfile pulled a base image from an unauthorized registry. "
        "The layer cache hid it.[/bold yellow]"
    ),
    "deployment_strategies": (
        "[bold cyan]ZONE: THE DEPLOYMENT THEATER[/bold cyan]\n\n"
        "Getting code to production is not a binary event. Blue-green deployments "
        "run two environments side by side. Canary releases send 5% of traffic to the new version. "
        "Rolling updates replace pods one at a time. Feature flags decouple deploy from release. "
        "[bold yellow]NEXUS Corp uses blue-green deployments. The attacker flipped the switch "
        "during a scheduled deployment window so the poisoned build went live "
        "alongside fifty legitimate changes.[/bold yellow]"
    ),
    "infrastructure_as_code_cicd": (
        "[bold cyan]ZONE: THE INFRA PIPELINE[/bold cyan]\n\n"
        "Infrastructure changes flow through the same pipeline as application code. "
        "Terraform plans run on pull requests. Applies run on merge to main. "
        "Drift detection catches manual changes. GitOps makes the repository the single source of truth. "
        "[bold yellow]The attacker added a Terraform module that opened a security group — "
        "port 22 from 0.0.0.0/0. The plan output showed the change. "
        "The reviewer approved it without reading the plan.[/bold yellow]"
    ),
    "monitoring_and_observability": (
        "[bold cyan]ZONE: THE WATCHTOWER[/bold cyan]\n\n"
        "The pipeline doesn't end at deploy. Post-deployment verification, health checks, "
        "SLO monitoring, alerting rules, and automated rollback triggers — "
        "this is the feedback loop that closes the circle. "
        "[bold yellow]The breach was detectable. The error rate spiked 0.3% for eleven minutes "
        "after the poisoned deploy. The alert threshold was set at 1%. "
        "No one was paged. No one looked.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "cicd_fundamentals": (
        "[bold green]ZONE COMPLETE — THE FOUNDATION[/bold green]\n\n"
        "You understand the pipeline from end to end. CI merges and validates. "
        "CD packages and delivers. Continuous Deployment pushes to production without human gates. "
        "[bold yellow]NEXUS Corp claimed they had human gates. The logs say otherwise.[/bold yellow]"
    ),
    "github_actions": (
        "[bold green]ZONE COMPLETE — THE WORKFLOW ENGINE[/bold green]\n\n"
        "Workflows, triggers, jobs, steps, secrets, matrix builds — you can read them all. "
        "The poisoned workflow used a `workflow_dispatch` trigger with a `repository_dispatch` fallback. "
        "[bold yellow]Clever. The attacker could trigger the pipeline remotely "
        "without pushing a single commit.[/bold yellow]"
    ),
    "testing_in_pipelines": (
        "[bold green]ZONE COMPLETE — THE TEST GAUNTLET[/bold green]\n\n"
        "Unit, integration, e2e. Coverage gates. Fail-fast. Parallel test stages. "
        "You understand every layer of the testing defense — and every way to bypass it. "
        "[bold yellow]The `[skip ci]` tag in the commit message. That's all it took.[/bold yellow]"
    ),
    "build_and_artifacts": (
        "[bold green]ZONE COMPLETE — THE BUILD FORGE[/bold green]\n\n"
        "Docker builds, multi-stage layers, artifact registries, cache poisoning — "
        "you can trace an image from Dockerfile to running container. "
        "[bold yellow]The unauthorized base image contained a reverse shell "
        "that activated 72 hours after deployment. Delayed detonation.[/bold yellow]"
    ),
    "deployment_strategies": (
        "[bold green]ZONE COMPLETE — THE DEPLOYMENT THEATER[/bold green]\n\n"
        "Blue-green, canary, rolling, feature flags, rollback. "
        "Every strategy has a window of vulnerability — the moment when new code is live "
        "but not yet validated. "
        "[bold yellow]The attacker knew that window was 4 minutes and 12 seconds. "
        "They timed the injection perfectly.[/bold yellow]"
    ),
    "infrastructure_as_code_cicd": (
        "[bold green]ZONE COMPLETE — THE INFRA PIPELINE[/bold green]\n\n"
        "Terraform plan, apply, drift detection, GitOps, state management. "
        "Infrastructure as code means infrastructure as evidence. "
        "[bold yellow]The security group change is in the Terraform state file. "
        "The attacker can't rewrite that without invalidating the state lock.[/bold yellow]"
    ),
    "monitoring_and_observability": (
        "[bold yellow]★ ★ ★  ZONE COMPLETE — THE WATCHTOWER  ★ ★ ★[/bold yellow]\n\n"
        "[bold white]The full pipeline is mapped.[/bold white]\n\n"
        "From commit to container to canary to production to health check to alert. "
        "Every stage. Every gate. Every bypass the attacker exploited.\n\n"
        "The 0.3% error spike. The 47-second failed build. The `[skip ci]` tag. "
        "The unauthorized Docker base image. The Terraform security group change. "
        "The blue-green switch timed to a deployment window.\n\n"
        "[bold magenta]The pipeline is the chain of custody. "
        "Break any link and the whole chain fails. "
        "You found every broken link.[/bold magenta]\n\n"
        "[bold yellow]PIPELINE FORENSICS STATUS: DEVOPS MASTER.  CASE STATUS: RESOLVED.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "cicd_fundamentals": (
        "[bold red]BOSS CHALLENGE — THE PIPELINE AUDIT[/bold red]\n\n"
        "[bold yellow]The CTO claims they practice Continuous Deployment. "
        "The pipeline config says otherwise. Prove you understand "
        "the difference between delivery and deployment — and which one they actually have.[/bold yellow]"
    ),
    "github_actions": (
        "[bold red]BOSS CHALLENGE — THE HIDDEN TRIGGER[/bold red]\n\n"
        "[bold yellow]A workflow runs every night at 3 AM. It wasn't triggered by push, "
        "pull_request, or schedule. The run history shows `repository_dispatch`. "
        "Prove you understand every trigger mechanism and how this one was weaponized.[/bold yellow]"
    ),
    "testing_in_pipelines": (
        "[bold red]BOSS CHALLENGE — THE BYPASSED GATE[/bold red]\n\n"
        "[bold yellow]The test suite has 94% coverage. The poisoned code was in the 6%. "
        "Explain how coverage gates can fail, how `[skip ci]` bypasses them entirely, "
        "and what policy would have caught this.[/bold yellow]"
    ),
    "build_and_artifacts": (
        "[bold red]BOSS CHALLENGE — THE POISONED IMAGE[/bold red]\n\n"
        "[bold yellow]The production Docker image has a layer that doesn't match the Dockerfile. "
        "The layer cache shows a pull from an external registry. "
        "Trace the image from source to artifact and identify the injection point.[/bold yellow]"
    ),
    "deployment_strategies": (
        "[bold red]BOSS CHALLENGE — THE ZERO-DOWNTIME BREACH[/bold red]\n\n"
        "[bold yellow]The attacker deployed malicious code using the blue-green strategy. "
        "No downtime. No alerts. Traffic was shifted during the standard window. "
        "Describe the rollback procedure and explain why automated canary analysis "
        "would have caught this.[/bold yellow]"
    ),
    "infrastructure_as_code_cicd": (
        "[bold red]BOSS CHALLENGE — THE DRIFT EXPLOIT[/bold red]\n\n"
        "[bold yellow]Someone ran `terraform apply` locally, bypassing the pipeline entirely. "
        "The state file shows changes that don't match any PR. "
        "Describe the GitOps controls that would prevent this and how "
        "drift detection would surface it.[/bold yellow]"
    ),
    "monitoring_and_observability": (
        "[bold red]★  FINAL ANALYSIS — THE SILENT BREACH[/bold red]\n\n"
        "[bold yellow]The error rate spiked 0.3% for 11 minutes. The alert threshold was 1%. "
        "The breach went undetected for 72 hours. "
        "Design the monitoring, alerting, and SLO policy that would have caught it "
        "in under 5 minutes.[/bold yellow]"
    ),
}
