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
    "cloudwatch_and_monitoring": (
        "[bold cyan]ZONE: THE OBSERVATION LAYER[/bold cyan]\n\n"
        "CloudWatch is the audit trail they forgot to audit. "
        "Every Lambda invocation, every RDS connection spike, every IAM credential use — "
        "[bold yellow]all logged, all queryable. "
        "The monitoring they set up to watch their systems "
        "also recorded everything they tried to hide.[/bold yellow]"
    ),
    "cloudformation_and_iac": (
        "[bold cyan]ZONE: THE BLUEPRINT ARCHIVE[/bold cyan]\n\n"
        "The entire NEXUS AWS infrastructure was provisioned with CloudFormation. "
        "Every Stack has a history. Every template is versioned. "
        "[bold yellow]The original infrastructure template — before the phantom subsidiaries "
        "were added — is still in the S3 template bucket. "
        "CloudFormation drift detection will show exactly what changed.[/bold yellow]"
    ),
    "ecs_and_containers": (
        "[bold cyan]ZONE: THE CONTAINER FLEET[/bold cyan]\n\n"
        "Not everything runs in the Kubernetes cluster. "
        "The payment-processing microservices run on ECS Fargate — "
        "separate from the main cluster, separate audit trail, separate IAM scope. "
        "[bold yellow]The Task Roles tell you what each service was allowed to touch. "
        "One service's Task Role includes `s3:GetObject` on the compliance archive.[/bold yellow]"
    ),
    "elb_and_autoscaling": (
        "[bold cyan]ZONE: THE SCALING LAYER[/bold cyan]\n\n"
        "Behind the public endpoints: Auto Scaling Groups, Launch Templates, "
        "and Application Load Balancers managing traffic to dozens of targets. "
        "[bold yellow]Someone modified the Launch Template 14 months ago. "
        "The User Data script runs on every instance. On every boot. "
        "You need to understand load balancing and auto scaling completely "
        "to trace what those instances have been doing.[/bold yellow]"
    ),
    "route53_and_cdn": (
        "[bold cyan]ZONE: THE EDGE LAYER[/bold cyan]\n\n"
        "DNS controls what resolves to what. CDN controls what gets cached where. "
        "Together, they control the first and last hop of every request. "
        "[bold yellow]An unknown Route 53 health check. Unusual cache invalidations. "
        "A domain that shouldn't exist pointing somewhere it shouldn't go. "
        "The edge layer is where the exfiltration channel lives.[/bold yellow]"
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
    "cloudwatch_and_monitoring": (
        "[bold green]ZONE COMPLETE — THE OBSERVATION LAYER[/bold green]\n\n"
        "CloudWatch Logs Insights query: `filter @message like /transfer-/ | stats count(*) by bin(30d)`. "
        "9,847 transfer events. Every one timestamped. "
        "The metric filter they set up for alerting — never connected to an alarm. "
        "[bold yellow]They built the monitoring. They just never turned on the notifications.[/bold yellow]"
    ),
    "cloudformation_and_iac": (
        "[bold green]ZONE COMPLETE — THE BLUEPRINT ARCHIVE[/bold green]\n\n"
        "CloudFormation drift detected: 14 resources modified outside the template. "
        "The S3 template bucket: original template from 3 years ago, before the phantom subsidiaries. "
        "Change set comparison shows exactly which IAM roles were added, which Lambda functions appeared. "
        "[bold yellow]Infrastructure as code is also infrastructure as evidence.[/bold yellow]"
    ),
    "ecs_and_containers": (
        "[bold green]ZONE COMPLETE — THE CONTAINER FLEET[/bold green]\n\n"
        "The compliance-reader ECS service: Task Role includes `s3:GetObject` on the compliance archive. "
        "CloudWatch Container Insights shows it made 847 calls to that bucket in the last 90 days. "
        "The service definition names a specific IAM user as its deployer. "
        "[bold yellow]Same user as the Lambda functions. The same hand built all of it.[/bold yellow]"
    ),
    "elb_and_autoscaling": (
        "[bold green]ZONE COMPLETE — THE SCALING LAYER[/bold green]\n\n"
        "Launch Template version history: 4 versions. The rogue User Data was added in version 2. "
        "The deployer IAM ARN: `arn:aws:iam::012345678901:user/nexus-ops-automation`. "
        "The same credential you found in the Kubernetes cluster. "
        "[bold yellow]One compromised key. Every layer of the infrastructure.[/bold yellow]"
    ),
    "route53_and_cdn": (
        "[bold green]ZONE COMPLETE — THE EDGE LAYER[/bold green]\n\n"
        "Route 53 query logs: 14,000 queries to `drain.internal.nexus-corp.com` in 90 days. "
        "Each query encodes 63 characters of payload in the subdomain. "
        "CloudFront invalidations: triggered by the same Lambda function from the automation engine. "
        "[bold yellow]The evidence dossier is complete. Every layer mapped. "
        "Eleven years of fraud — dismantled.[/bold yellow]"
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
    "cloudwatch_and_monitoring": (
        "[bold red]BOSS CHALLENGE — THE INVISIBLE ALARM[/bold red]\n\n"
        "[bold yellow]A metric filter exists that counts ERROR events in the Lambda log group. "
        "The metric has been publishing data for 3 years. "
        "There are no alarms on the metric. No dashboards. No notifications. "
        "Write a CloudWatch Logs Insights query to reconstruct what those errors were "
        "and when they peaked — using only the log data.[/bold yellow]"
    ),
    "cloudformation_and_iac": (
        "[bold red]BOSS CHALLENGE — THE TAMPERED STACK[/bold red]\n\n"
        "[bold yellow]A CloudFormation Stack shows UPDATE_COMPLETE but drift detection shows "
        "7 resources have been modified outside CloudFormation. "
        "Two of those resources are IAM roles. "
        "Walk through exactly how you would reconstruct the full change history: "
        "what changed, when, and by which IAM identity — using only AWS-native tools.[/bold yellow]"
    ),
    "ecs_and_containers": (
        "[bold red]BOSS CHALLENGE — THE CONTAINER ESCAPE[/bold red]\n\n"
        "[bold yellow]An ECS Fargate task has a Task Role with AdministratorAccess attached. "
        "The container image was pulled from a public ECR repository. "
        "List every way a compromised container could use those permissions to move laterally "
        "through the AWS account — and explain what should have been done differently.[/bold yellow]"
    ),
    "elb_and_autoscaling": (
        "[bold red]BOSS CHALLENGE — THE SILENT LAUNCH TEMPLATE[/bold red]\n\n"
        "[bold yellow]Every EC2 instance spun up by the Auto Scaling Group is running an undeclared "
        "process. The Launch Template's User Data was modified 14 months ago by a deactivated IAM user. "
        "Describe every step to: detect the current User Data content, create a clean Launch Template "
        "version, force instance refresh, and audit the ASG health check history "
        "to estimate how long the rogue process has been running.[/bold yellow]"
    ),
    "route53_and_cdn": (
        "[bold red]BOSS CHALLENGE — THE DNS EXFIL CHANNEL[/bold red]\n\n"
        "[bold yellow]A CloudFront distribution is serving `assets.nexus-corp.com`. "
        "An unusual Route 53 health check is configured on a subdomain that doesn't resolve to any "
        "known service. CloudFront cache hit rates dropped 30% last week — something is forcing "
        "cache invalidations. Walk through: how to audit Route 53 health checks for unknown endpoints, "
        "how to review CloudFront invalidation history, and what DNS-based exfiltration looks like "
        "in Route 53 query logs.[/bold yellow]"
    ),
}
