"""
Terraform skill pack narrative — The Blueprint Layer
"""

INTRO_STORY = """
[bold cyan]◈◈◈  THE NEXUS FILES — THE BLUEPRINT LAYER  ◈◈◈[/bold cyan]

[dim]You've cracked the Kubernetes cluster. You've mapped the AWS account.
But somewhere behind all of it — behind the IAM roles, the EC2 fleets,
the RDS instances — there's a blueprint.[/dim]

[bold white]CIPHER: 'Every resource in that account was provisioned by code.
They didn't click through the console like amateurs.
They used Terraform. IaC. Infrastructure as Code.
And that means there's a state file — a living record of every
resource they ever created, modified, or destroyed.'[/bold white]

[dim]You find the S3 backend config buried in a Git repo.
A bucket name. An encryption key. A DynamoDB lock table.
CIPHER decrypts the credentials.[/dim]

[bold yellow]terraform state pull[/bold yellow]

[dim]The state file downloads. 12 MB of JSON.
Every phantom subsidiary. Every backdoor IAM role.
Every forensically significant resource — timestamped, named, attributed.

This isn't just evidence. This is the blueprint of the fraud.
And now you understand how to read it.[/dim]

[bold cyan]Learn Terraform. Read the blueprint. Own the truth.[/bold cyan]
"""

ZONE_INTROS = {
    "hcl_fundamentals": (
        "[bold cyan]◈  ZONE 1: HCL FUNDAMENTALS  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Before you can read the blueprint, you need to understand"
        " the language it's written in. HCL — HashiCorp Configuration Language."
        " Declarative. Human-readable. Deceptively simple on the surface.'[/bold white]\n\n"
        "[dim]The state file points back to source configs. You find a Git repo."
        " Dozens of .tf files. Every resource they ever provisioned, described"
        " in blocks. You start at the beginning — the syntax.[/dim]"
    ),
    "variables_and_outputs": (
        "[bold cyan]◈  ZONE 2: VARIABLES AND OUTPUTS  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Nobody hardcodes account IDs in a fraud operation."
        " They parameterise everything. One codebase, twelve subsidiary accounts,"
        " all driven by variables. Find the variable files and you find"
        " the full scope of the operation.'[/bold white]\n\n"
        "[dim]You pull the tfvars files from each workspace. Each subsidiary"
        " has its own values injected at runtime. The output blocks"
        " expose ARNs, endpoint URLs, resource IDs — the full map"
        " of what each environment produced.[/dim]"
    ),
    "state_management": (
        "[bold cyan]◈  ZONE 3: STATE MANAGEMENT  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The state file is the ground truth. Terraform keeps"
        " a record of every resource it manages — IDs, attributes, dependencies."
        " It's their receipt. And it's stored in S3 with versioning enabled."
        " Every change, every deletion — all of it logged.'[/bold white]\n\n"
        "[dim]You pull the state versions from S3. The history goes back"
        " three years. You can see exactly when each phantom entity was"
        " created, when it was modified, and what resources vanished"
        " the night before the audit was announced.[/dim]"
    ),
    "providers_and_registry": (
        "[bold cyan]◈  ZONE 4: PROVIDERS AND REGISTRY  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Providers are the bridge — Terraform speaks HCL,"
        " the provider translates that into API calls. AWS, Kubernetes, Vault,"
        " even internal systems. Check which providers they pinned and"
        " at what versions. Version constraints tell a story.'[/bold white]\n\n"
        "[dim]The provider block shows aws ~> 5.0, pinned."
        " A custom provider with a private registry URL."
        " That custom provider is communicating with something"
        " that isn't in the public Terraform Registry.[/dim]"
    ),
    "resource_lifecycle": (
        "[bold cyan]◈  ZONE 5: RESOURCE LIFECYCLE  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Lifecycle rules tell Terraform how to handle"
        " create, update, and destroy operations. They were using"
        " prevent_destroy on the money accounts. And create_before_destroy"
        " on the shell companies — so there was never a gap in operation."
        " Forensically, this tells us they planned for continuity.'[/bold white]\n\n"
        "[dim]The lifecycle blocks are almost clinical in their precision."
        " Whoever wrote this understood Terraform deeply."
        " You're starting to build a profile of the architect.[/dim]"
    ),
    "modules": (
        "[bold cyan]◈  ZONE 6: MODULES  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'They didn't repeat themselves. Every subsidiary"
        " account was provisioned from the same module — parameterised,"
        " versioned, pulled from a private module registry."
        " One module. Twelve instances. Twelve shell companies."
        " All from the same blueprint.'[/bold white]\n\n"
        "[dim]The module source points to an internal registry."
        " Version 2.3.1. You find the module — it provisions"
        " the full fraud stack: VPC, IAM, S3 data store,"
        " Lambda for fund movement, CloudWatch for obfuscation."
        " All in 200 lines of HCL.[/dim]"
    ),
    "data_sources": (
        "[bold cyan]◈  ZONE 7: DATA SOURCES  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Data sources are how Terraform reads the world"
        " without managing it. They were using data sources to query"
        " existing resources — VPCs they didn't create, AMIs from"
        " a private catalogue, Route53 zones. It tells us what they"
        " assumed already existed.'[/bold white]\n\n"
        "[dim]Cross-referencing the data source queries against"
        " the existing account inventory reveals a shadow infrastructure"
        " that predates the Terraform configs by two years."
        " The hand-provisioned foundation they built on top of.[/dim]"
    ),
    "workspaces_and_environments": (
        "[bold cyan]◈  ZONE 8: WORKSPACES AND ENVIRONMENTS  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Each subsidiary ran in its own Terraform workspace."
        " Dev, staging, prod — and twelve fraud workspaces alongside them."
        " The workspace isolation meant each environment had its own state."
        " They were hiding in plain sight alongside legitimate infrastructure.'[/bold white]\n\n"
        "[dim]You list the workspaces. The legitimate ones look like any"
        " engineering team's setup. But workspace names like nexus-cayman-1"
        " and nexus-bvi-3 are not standard environments.[/dim]"
    ),
    "plan_and_apply_workflow": (
        "[bold cyan]◈  ZONE 9: PLAN AND APPLY WORKFLOW  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The CI/CD logs survived. Every terraform plan"
        " and apply was recorded — who triggered it, when, what changed."
        " They used -auto-approve in the pipeline. No manual review."
        " Resources spun up and down without a human ever seeing"
        " the diff.'[/bold white]\n\n"
        "[dim]The pipeline logs show automated apply runs at 2 AM"
        " on the first of every month. Always the same operator token."
        " Always the same pattern. You've found the automation layer.[/dim]"
    ),
    "aws_with_terraform": (
        "[bold cyan]◈  ZONE 10: AWS WITH TERRAFORM  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Time to put it all together. The whole fraud"
        " stack was AWS resources written in HCL. EC2, S3, IAM, VPC —"
        " you know the AWS services, you know Terraform syntax."
        " Now you read the actual configs that provisioned the operation.'[/bold white]\n\n"
        "[dim]The resource blocks are dense but legible now."
        " aws_iam_role.fund_processor. aws_s3_bucket.evidence_store."
        " aws_lambda_function.transfer_executor."
        " Every line is a piece of the fraud map.[/dim]"
    ),
    "advanced_patterns": (
        "[bold cyan]◈  ZONE 11: ADVANCED PATTERNS  ◈[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The final layer. They were using for_each"
        " to spin up twelve identical environments from one resource block."
        " Dynamic blocks to generate rules programmatically."
        " templatefile() to inject runtime values into scripts."
        " This isn't script-kiddie work. This is production Terraform.'[/bold white]\n\n"
        "[dim]You reach the final module — the one that provisions"
        " all twelve subsidiaries from a single ZONES variable."
        " One resource block. Twelve instances. Twelve crimes."
        " You understand it completely now.[/dim]"
    ),
}

ZONE_COMPLETIONS = {
    "hcl_fundamentals": (
        "[bold green]✓  HCL DECODED[/bold green]\n\n"
        "[dim]You can read the blueprint now. The resource blocks, the provider"
        " configurations, the argument syntax — it's no longer noise."
        " You're reading their infrastructure like a document.[/dim]"
    ),
    "variables_and_outputs": (
        "[bold green]✓  VARIABLES MAPPED[/bold green]\n\n"
        "[dim]Every tfvars file logged. The output values cross-referenced"
        " against account inventories. The full parameterisation scheme"
        " of the fraud operation is documented.[/dim]"
    ),
    "state_management": (
        "[bold green]✓  STATE FILE IN HAND[/bold green]\n\n"
        "[dim]Three years of state history pulled from S3."
        " Resource creation timestamps, deletion events, the pre-audit"
        " cleanup attempt — all preserved in versioned state.[/dim]"
    ),
    "providers_and_registry": (
        "[bold green]✓  PROVIDERS TRACED[/bold green]\n\n"
        "[dim]The custom provider is identified. It's a wrapper around"
        " an internal API that processed fund movements."
        " You've found the bridge between infrastructure and finance.[/dim]"
    ),
    "resource_lifecycle": (
        "[bold green]✓  LIFECYCLE RULES DOCUMENTED[/bold green]\n\n"
        "[dim]The prevent_destroy and create_before_destroy configurations"
        " are logged as evidence of intentional design."
        " The architect knew what they were building.[/dim]"
    ),
    "modules": (
        "[bold green]✓  MODULE REGISTRY ACCESSED[/bold green]\n\n"
        "[dim]The fraud module is downloaded, versioned, and preserved."
        " All twelve subsidiary instantiations mapped."
        " The 200-line blueprint of the operation is in your possession.[/dim]"
    ),
    "data_sources": (
        "[bold green]✓  SHADOW INFRASTRUCTURE FOUND[/bold green]\n\n"
        "[dim]The pre-Terraform foundation is mapped. Two years of"
        " hand-provisioned resources that Terraform managed but didn't create."
        " The full timeline of the fraud is now reconstructed.[/dim]"
    ),
    "workspaces_and_environments": (
        "[bold green]✓  ALL WORKSPACES CATALOGUED[/bold green]\n\n"
        "[dim]Twelve fraud workspaces alongside legitimate environments."
        " State files for each pulled and preserved."
        " The scope of the operation — twelve jurisdictions, twelve shell companies.[/dim]"
    ),
    "plan_and_apply_workflow": (
        "[bold green]✓  PIPELINE LOGS SECURED[/bold green]\n\n"
        "[dim]Every plan and apply logged. The automation timestamps."
        " The operator tokens. The CI/CD configuration that ran"
        " unreviewed applies at 2 AM for three years.[/dim]"
    ),
    "aws_with_terraform": (
        "[bold green]✓  AWS RESOURCES MAPPED[/bold green]\n\n"
        "[dim]Every AWS resource in the fraud stack identified and documented."
        " IAM roles, S3 buckets, Lambda functions, VPCs."
        " The complete cloud architecture of the fraud, in HCL.[/dim]"
    ),
    "advanced_patterns": (
        "[bold green]✓  BLUEPRINT COMPLETE[/bold green]\n\n"
        "[bold white]CIPHER: 'That's everything. The full terraform codebase,"
        " the state files, the module registry, the pipeline logs."
        " We have the complete picture of how they built it,"
        " how they ran it, and how they tried to cover it up.\n\n"
        "This is the blueprint layer. And now you can read it."
        " All of it.'[/bold white]\n\n"
        "[dim]You archive the evidence package. Twelve subsidiaries."
        " Eleven Terraform zones. One complete fraud operation,"
        " documented in Infrastructure as Code.[/dim]"
    ),
}

BOSS_INTROS = {
    "hcl_fundamentals": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: THE RESOURCE BLOCK  ◈[/bold red]\n\n"
        "[bold white]'You've seen the syntax. Now prove you can read a complete"
        " resource configuration — provider, type, name, arguments,"
        " and meta-arguments. The blueprint is dense. One wrong read"
        " and you miss critical evidence.'[/bold white]"
    ),
    "variables_and_outputs": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: VARIABLE TYPES  ◈[/bold red]\n\n"
        "[bold white]'The tfvars files use complex types — objects, lists of maps,"
        " optional attributes. If you can't parse the type constraints,"
        " you can't reconstruct what values they were injecting"
        " into the fraud stack at runtime.'[/bold white]"
    ),
    "state_management": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: STATE COMMANDS  ◈[/bold red]\n\n"
        "[bold white]'The state file has drift — resources that exist in AWS"
        " but were removed from state to hide them. You need to use"
        " terraform state commands to reconstruct what was there."
        " Every state command matters.'[/bold white]"
    ),
    "providers_and_registry": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: VERSION CONSTRAINTS  ◈[/bold red]\n\n"
        "[bold white]'The custom provider version pinning is deliberate."
        " Understanding version constraint operators — ~>, >=, =, != —"
        " will tell you exactly which provider capabilities they were"
        " locking in and which vulnerabilities they were avoiding.'[/bold white]"
    ),
    "resource_lifecycle": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: LIFECYCLE RULES  ◈[/bold red]\n\n"
        "[bold white]'The money accounts have prevent_destroy and ignore_changes."
        " Understanding exactly what these do under the hood is the"
        " difference between knowing they protected the resources"
        " and proving they intentionally made them undeletable.'[/bold white]"
    ),
    "modules": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: MODULE SOURCES  ◈[/bold red]\n\n"
        "[bold white]'The module source URL uses a private registry with"
        " a specific version ref. Parsing module source syntax correctly"
        " tells you the exact version of the fraud blueprint they deployed"
        " and when they last updated it.'[/bold white]"
    ),
    "data_sources": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: DATA BLOCK SYNTAX  ◈[/bold red]\n\n"
        "[bold white]'The data sources reference resources by complex filters."
        " Understanding how to read data block syntax — type, name,"
        " filter arguments — is how you identify which existing"
        " infrastructure they were attaching the fraud stack to.'[/bold white]"
    ),
    "workspaces_and_environments": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: WORKSPACE ISOLATION  ◈[/bold red]\n\n"
        "[bold white]'The workspace setup used TF_WORKSPACE environment variables"
        " in the pipeline. Understanding workspace state isolation tells you"
        " exactly which resources were in each subsidiary workspace"
        " and which state they were protecting.'[/bold white]"
    ),
    "plan_and_apply_workflow": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: PLAN OUTPUT READING  ◈[/bold red]\n\n"
        "[bold white]'The saved plan files are in the CI/CD artifacts."
        " Reading a terraform plan output — understanding + create,"
        " ~ update, - destroy, -/+ replace — is how you reconstruct"
        " exactly what changed in each automated run.'[/bold white]"
    ),
    "aws_with_terraform": (
        "[bold red]◈  CIPHER BOSS CHALLENGE: FULL RESOURCE BLOCK  ◈[/bold red]\n\n"
        "[bold white]'The money-movement Lambda. The IAM role that powers it."
        " The S3 bucket it writes to. Three resource blocks, all connected."
        " Read them correctly and you have the complete mechanism"
        " of the fund transfer operation.'[/bold white]"
    ),
    "advanced_patterns": (
        "[bold red]◈  CIPHER FINAL BOSS: THE FRAUD LOOP  ◈[/bold red]\n\n"
        "[bold white]'One resource block. for_each = toset(var.subsidiaries)."
        " Twelve instances. This is the smoking gun — the single piece"
        " of code that proves all twelve shell companies were deliberately"
        " provisioned from the same template by the same operator."
        " Read it. Understand it. That's your case.'[/bold white]"
    ),
}
