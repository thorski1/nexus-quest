"""
story.py — Narrative for The Cloud Layer (AWS) skill pack.
"""

INTRO_STORY = """
[bold red]NEXUS OPERATIVE — CLOUD ACCESS CONFIRMED[/bold red]

The cluster gave you the keys.

In the audit-eraser pod's environment variables: AWS credentials.
Not a service account. Not limited-scope. A named IAM user — [yellow]nexus-ops-automation[/yellow] —
with an access key that hasn't been rotated in [bold white]three years[/bold white].

[bold cyan]$ aws sts get-caller-identity[/bold cyan]

[dim]{
    "Account": "012345678901",
    "Arn": "arn:aws:iam::012345678901:user/nexus-ops-automation",
    "UserId": "AIDAEXAMPLEID"
}[/dim]

[bold white]You're in.[/bold white]

NEXUS Corporation's cloud infrastructure: the S3 buckets backing the evidence
archive, the RDS cluster holding the unredacted financial records, the Lambda
functions that automatically moved money between the phantom subsidiaries.

The Kubernetes cluster was the on-prem infrastructure.
[bold yellow]AWS is where the real data lives.[/bold yellow]

Three-year-old credentials. No rotation. No monitoring.

[bold cyan]"Whoever set this up either didn't know,"[/bold cyan] CIPHER says,
[bold cyan]"or didn't care."[/bold cyan]

Time to find out which.
"""

ZONE_INTROS = {
    "iam_and_security": (
        "[bold cyan]ZONE: IDENTITY LAYER[/bold cyan]\n\n"
        "The IAM configuration is your attack surface map. "
        "[bold yellow]Find the misconfigured policies. Find the overprivileged roles. "
        "Find the user that shouldn't have the permissions it has. "
        "Understand IAM completely — it controls everything.[/bold yellow]"
    ),
    "ec2_and_compute": (
        "[bold cyan]ZONE: THE MACHINE FLEET[/bold cyan]\n\n"
        "Forty-seven EC2 instances. Most are tagged with legitimate workload names. "
        "[bold yellow]Three are tagged `ops-temp` and have been running for 1,100 days. "
        "'Temp' indeed. Find what's on them and how they're accessed.[/bold yellow]"
    ),
    "s3_and_storage": (
        "[bold cyan]ZONE: THE BUCKET LIST[/bold cyan]\n\n"
        "S3 buckets are where NEXUS keeps everything. Financial archives, audit logs, "
        "contract documents, deployment artifacts. "
        "[bold yellow]And one bucket — `nexus-compliance-archive` — has a bucket policy "
        "that never got the public-block treatment. Check what's inside.[/bold yellow]"
    ),
    "vpc_and_networking": (
        "[bold cyan]ZONE: THE NETWORK TOPOLOGY[/bold cyan]\n\n"
        "NEXUS's VPC was designed to keep things separated. On paper. "
        "[bold yellow]In practice, the network ACLs were misconfigured three years ago "
        "and nobody noticed. The private subnets aren't as private as they think.[/bold yellow]"
    ),
    "rds_and_databases": (
        "[bold cyan]ZONE: THE PRIMARY ARCHIVE[/bold cyan]\n\n"
        "This is the one. The RDS cluster holding eleven years of unredacted financial data. "
        "[bold yellow]The Kubernetes database was a replica. This is the source of truth. "
        "The backup retention is 35 days. The oldest snapshots are the most important.[/bold yellow]"
    ),
    "lambda_and_serverless": (
        "[bold cyan]ZONE: THE AUTOMATION ENGINE[/bold cyan]\n\n"
        "Forty-three Lambda functions. Most are boring infrastructure glue. "
        "[bold yellow]But six are named with the same prefix as the phantom subsidiaries: "
        "`transfer-{subsidiary_id}`. These ran on a schedule. "
        "CloudWatch logs will tell you what they did.[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "iam_and_security": (
        "[bold green]ZONE COMPLETE — IDENTITY LAYER[/bold green]\n\n"
        "The IAM audit is complete. The `nexus-ops-automation` user has "
        "`AdministratorAccess`. That's the entire account with one compromised key. "
        "[bold yellow]Someone intentionally over-provisioned it.[/bold yellow]"
    ),
    "ec2_and_compute": (
        "[bold green]ZONE COMPLETE — THE MACHINE FLEET[/bold green]\n\n"
        "The three `ops-temp` instances are running proprietary financial software "
        "with no audit logging enabled. They're in a security group that allows "
        "inbound from a CIDR block that belongs to a shell company in the fraud trail. "
        "[bold yellow]These aren't temp instances. They're infrastructure.[/bold yellow]"
    ),
    "s3_and_storage": (
        "[bold green]ZONE COMPLETE — THE BUCKET LIST[/bold green]\n\n"
        "The `nexus-compliance-archive` bucket: versioning enabled, 11 years of objects. "
        "Every quarterly compliance report — but the versions tell a story: "
        "documents were modified after submission. The originals are in the older versions. "
        "[bold yellow]S3 versioning preserved what they tried to overwrite.[/bold yellow]"
    ),
    "vpc_and_networking": (
        "[bold green]ZONE COMPLETE — NETWORK TOPOLOGY[/bold green]\n\n"
        "The VPC misconfiguration is documented. The 'private' RDS cluster "
        "is reachable from the public subnet through a NACL rule that allows "
        "all traffic from the shell company's IP range. "
        "[bold yellow]That's a deliberate backdoor.[/bold yellow]"
    ),
    "rds_and_databases": (
        "[bold green]ZONE COMPLETE — PRIMARY ARCHIVE[/bold green]\n\n"
        "The oldest snapshot restored. The unredacted transaction records: "
        "exactly matching the evidence from the Kubernetes cluster, "
        "but with additional metadata columns that were stripped in the replica. "
        "[bold yellow]The metadata columns contain the signatory names.[/bold yellow]"
    ),
    "lambda_and_serverless": (
        "[bold green]ZONE COMPLETE — AUTOMATION ENGINE[/bold green]\n\n"
        "The six transfer Lambda functions: CloudWatch logs show 9,847 executions "
        "over eleven years. Each execution moved money between the phantom subsidiaries "
        "on a schedule that correlated with federal contract payment cycles. "
        "[bold yellow]Fully automated. Fully documented in the logs they forgot to disable.[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "iam_and_security": (
        "[bold red]BOSS CHALLENGE — THE PERMISSION MAZE[/bold red]\n\n"
        "[bold yellow]An IAM role has three attached policies, two inline policies, "
        "and is assumed by a service with its own resource policy. "
        "What are the effective permissions? "
        "Reason through the evaluation logic completely.[/bold yellow]"
    ),
    "ec2_and_compute": (
        "[bold red]BOSS CHALLENGE — THE FORENSIC IMAGE[/bold red]\n\n"
        "[bold yellow]An EC2 instance is being terminated in 10 minutes. "
        "You need to preserve every byte of evidence on it. "
        "What do you do? Walk through every step before the window closes.[/bold yellow]"
    ),
    "s3_and_storage": (
        "[bold red]BOSS CHALLENGE — THE DELETED OBJECT[/bold red]\n\n"
        "[bold yellow]An S3 object was 'deleted' but versioning was enabled. "
        "A lifecycle rule was also applied. "
        "Is the original content still recoverable? "
        "Prove your answer with the complete version/delete-marker mechanics.[/bold yellow]"
    ),
    "vpc_and_networking": (
        "[bold red]BOSS CHALLENGE — THE TRAFFIC PATH[/bold red]\n\n"
        "[bold yellow]An EC2 instance in a private subnet is trying to reach an S3 bucket. "
        "The request is failing. List every component in the request path "
        "and identify where the block could be.[/bold yellow]"
    ),
    "rds_and_databases": (
        "[bold red]BOSS CHALLENGE — THE RECOVERY WINDOW[/bold red]\n\n"
        "[bold yellow]An RDS database was deleted 6 days ago. The retention period was 7 days. "
        "The final snapshot was skipped. "
        "Can you restore it? What are your options? What data might be lost?[/bold yellow]"
    ),
    "lambda_and_serverless": (
        "[bold red]BOSS CHALLENGE — THE COLD TRAIL[/bold red]\n\n"
        "[bold yellow]A Lambda function was deleted 90 days ago. The CloudWatch log group was also deleted. "
        "The function executed 47,000 times. "
        "What evidence might still exist in the AWS environment? "
        "Think through every service that might have captured output or invocation data.[/bold yellow]"
    ),
}
