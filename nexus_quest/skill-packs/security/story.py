"""
story.py — Narrative for Security Ops (security skill pack).
Theme: The digital fortress needs architects, not just walls.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — SECURITY OPERATIONS DIVISION[/bold red]

The breach started three weeks ago. A single misconfigured IAM policy —
wildcard permissions on a storage bucket nobody audited. By the time the
alert fired, NEXUS had exfiltrated 40GB of encrypted credentials, session
tokens, and private keys.

You thought firewalls and passwords were enough. They never are.

CIPHER's voice is calm but urgent: [bold cyan]"The exfiltration wasn't
sophisticated. It didn't need to be. They walked through an open door —
a door nobody knew existed because nobody modeled the threats, nobody
reviewed the policies, nobody checked the locks."[/bold cyan]

A security dashboard flickers on your screen. Red indicators everywhere.
Exposed ports. Unrotated keys. Containers running as root. JWTs signed
with 'none'. A SIEM full of alerts nobody triaged.

[bold white]"Where do I start?"[/bold white]

[bold cyan]"From the foundation. The CIA triad. Then authentication,
encryption, web security, containers, cloud, incident response. Not just
tools — the thinking behind them. Defense in depth isn't a product you
install. It's a discipline you practice."[/bold cyan]

A pause. Then: [bold cyan]"The digital fortress needs architects, not just
walls. Anyone can build a wall. An architect knows where the walls need to
go — and what to do when one falls."[/bold cyan]

[italic]Initializing security operations framework... 8 sectors to secure.[/italic]
"""

ZONE_INTROS = {
    "security_fundamentals": (
        "[bold cyan]ZONE 1 — THE FOUNDATION[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Before you touch a firewall rule or write an auth check, "
        "you need the mental model. Confidentiality, Integrity, Availability — the CIA "
        "triad. Every security decision you make maps back to these three properties. "
        "Threat models, attack surfaces, defense in depth, least privilege — this is "
        "how security architects think. Learn the foundation or every wall you build "
        "will have the wrong shape.'[/bold white]"
    ),
    "authentication": (
        "[bold cyan]ZONE 2 — THE GATEKEEPER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS got in because a service account had a password "
        "that was never rotated, stored in plain text in an environment variable. "
        "No MFA. No session rotation. An OAuth token with scope:* that never expired. "
        "Authentication is the front door — passwords, hashing, MFA, OAuth2, JWTs, "
        "sessions. If the gatekeeper is weak, nothing behind it matters.'[/bold white]"
    ),
    "encryption": (
        "[bold cyan]ZONE 3 — THE CIPHER VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The exfiltrated data was encrypted at rest. But NEXUS "
        "stole the encryption keys too — they were in the same bucket as the data. "
        "Encryption without key management is a locked door with the key taped to "
        "the frame. Symmetric, asymmetric, TLS, certificates, PKI, forward secrecy — "
        "you need to understand the cryptographic building blocks of trust.'[/bold white]"
    ),
    "web_security": (
        "[bold cyan]ZONE 4 — THE ATTACK SURFACE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The internal admin panel had no CSRF protection, "
        "reflected user input without encoding, and built SQL queries with string "
        "concatenation. Three vulnerabilities. Three open doors. OWASP documented "
        "every one of them a decade ago. XSS, CSRF, SQL injection, CORS, CSP — "
        "the web application layer is where most breaches begin.'[/bold white]"
    ),
    "container_security": (
        "[bold cyan]ZONE 5 — THE SEALED VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The containers were running as root with the Docker "
        "socket mounted. One exploit gave NEXUS access to the host. The base image "
        "hadn't been scanned in six months — 47 critical CVEs. API keys were baked "
        "into image layers. The supply chain was compromised from the start. "
        "Container security isn't just Docker — it's images, privileges, secrets, "
        "and every dependency in between.'[/bold white]"
    ),
    "cloud_security": (
        "[bold cyan]ZONE 6 — THE CLOUD PERIMETER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The S3 bucket was public. The IAM policy used "
        "wildcards for both action and resource. Security groups allowed SSH "
        "from 0.0.0.0/0. CloudTrail was disabled in two regions. The shared "
        "responsibility model says the cloud provider secures the infrastructure — "
        "everything else is on you. IAM, security groups, logging, encryption — "
        "the cloud perimeter is your responsibility.'[/bold white]"
    ),
    "incident_response": (
        "[bold cyan]ZONE 7 — THE WAR ROOM[/bold cyan]\n\n"
        "[bold white]CIPHER: 'When the breach was detected, the team panicked. "
        "Someone rebooted the compromised server — destroying volatile evidence. "
        "Someone else emailed the all-company list — tipping off the attacker. "
        "There was no playbook. No containment plan. No forensic preservation. "
        "Detection, containment, eradication, recovery, post-mortem — incident "
        "response is a discipline. Practice it before you need it.'[/bold white]"
    ),
    "security_culture": (
        "[bold cyan]ZONE 8 — THE HUMAN FIREWALL[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Tools don't secure systems. People do. The team "
        "that never threat-modeled. The pipeline with no SAST. The developer who "
        "committed secrets because nobody told them about gitleaks. Security is "
        "not a gate at the end — it's a guardrail that runs the entire length. "
        "DevSecOps, shift-left, security champions, secure SDLC — build security "
        "into the culture or keep rebuilding walls after they fall.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "security_fundamentals": (
        "[bold green]ZONE CLEAR — THE FOUNDATION[/bold green]\n\n"
        "CIA triad, threat models, attack surfaces, defense in depth, least privilege — "
        "the mental model is set. Every security control you build from here "
        "will map back to these fundamentals. "
        "CIPHER: 'Now you think like a security architect. The foundation holds.'"
    ),
    "authentication": (
        "[bold green]ZONE CLEAR — THE GATEKEEPER[/bold green]\n\n"
        "Passwords, hashing, MFA, OAuth2, JWTs, session management — the front door "
        "is reinforced. No more plaintext passwords. No more eternal tokens. "
        "CIPHER: 'The gatekeeper is strong. Every identity is verified, "
        "every session is scoped, every token expires.'"
    ),
    "encryption": (
        "[bold green]ZONE CLEAR — THE CIPHER VAULT[/bold green]\n\n"
        "Symmetric, asymmetric, TLS, certificates, PKI, forward secrecy — "
        "the cryptographic foundation is solid. Keys are managed. Data is encrypted "
        "at rest and in transit. "
        "CIPHER: 'The vault is sealed. Even if they intercept the traffic, "
        "they can't read it. Even if they steal last year's key, "
        "they can't decrypt last year's sessions.'"
    ),
    "web_security": (
        "[bold green]ZONE CLEAR — THE ATTACK SURFACE[/bold green]\n\n"
        "SQL injection, XSS, CSRF, CORS, CSP — the OWASP Top 10 is mapped and "
        "mitigated. Inputs are sanitized. Outputs are encoded. Policies are set. "
        "CIPHER: 'The application layer is hardened. The three open doors "
        "are sealed. NEXUS can't walk through the web anymore.'"
    ),
    "container_security": (
        "[bold green]ZONE CLEAR — THE SEALED VAULT[/bold green]\n\n"
        "Images scanned, privileges dropped, secrets externalized, supply chain verified. "
        "No more root containers. No more baked-in credentials. "
        "CIPHER: 'The containers are sealed. Minimal base, non-root user, "
        "scanned dependencies, runtime secrets. The vault holds.'"
    ),
    "cloud_security": (
        "[bold green]ZONE CLEAR — THE CLOUD PERIMETER[/bold green]\n\n"
        "IAM scoped, security groups locked, S3 Block Public Access enabled, "
        "CloudTrail logging everywhere. The shared responsibility model is understood. "
        "CIPHER: 'The cloud perimeter is yours now. No more wildcard policies. "
        "No more public buckets. Every API call is logged.'"
    ),
    "incident_response": (
        "[bold green]ZONE CLEAR — THE WAR ROOM[/bold green]\n\n"
        "Preparation, detection, containment, eradication, recovery, post-mortem — "
        "the incident response playbook is written and practiced. "
        "CIPHER: 'When the next breach comes — and it will — "
        "you'll contain it in minutes, not weeks. Evidence preserved. "
        "Root cause found. Lessons learned. The war room is ready.'"
    ),
    "security_culture": (
        "[bold green]ZONE CLEAR — THE HUMAN FIREWALL[/bold green]\n\n"
        "DevSecOps, shift-left, security champions, secure SDLC — security is "
        "woven into the culture, not bolted on at the end. "
        "CIPHER: 'The digital fortress has its architect now. "
        "Not just walls — a discipline. Not just tools — a culture. "
        "NEXUS exploited a system without security thinking. "
        "That system no longer exists.'"
    ),
}

BOSS_INTROS = {
    "security_fundamentals": (
        "[bold red]BOSS CHALLENGE — THREAT MODEL ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'A new microservice accepts user input, "
        "stores PII in a database, and communicates with three internal services. "
        "Apply the CIA triad — identify the top threat to each property "
        "and name the defense. Think like an architect.'[/bold white]"
    ),
    "authentication": (
        "[bold red]BOSS CHALLENGE — CREDENTIAL AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'The compromised service account used a "
        "SHA-1 hashed password with no salt, no MFA, and an OAuth token "
        "with no expiration. Walk me through every failure and the "
        "correct implementation for each.'[/bold white]"
    ),
    "encryption": (
        "[bold red]BOSS CHALLENGE — KEY COMPROMISE SCENARIO[/bold red]\n\n"
        "[bold white]CIPHER: 'The TLS private key for api.corp.internal was "
        "found in a public GitHub repository. Assess the damage. "
        "Does forward secrecy save past sessions? What's the revocation "
        "and remediation plan?'[/bold white]"
    ),
    "web_security": (
        "[bold red]BOSS CHALLENGE — VULNERABILITY TRIAGE[/bold red]\n\n"
        "[bold white]CIPHER: 'A pen test report shows: stored XSS in comments, "
        "SQL injection in search, missing CSRF tokens on the admin panel, "
        "and CORS allowing any origin. Rank by severity. "
        "Fix the most critical one first. Explain why.'[/bold white]"
    ),
    "container_security": (
        "[bold red]BOSS CHALLENGE — CONTAINER ESCAPE PATH[/bold red]\n\n"
        "[bold white]CIPHER: 'A container runs as root with the Docker socket "
        "mounted and the host PID namespace shared. Trace the escape path "
        "from application exploit to host-level access. "
        "Then lock it down — every control, every flag.'[/bold white]"
    ),
    "cloud_security": (
        "[bold red]BOSS CHALLENGE — IAM POLICY REVIEW[/bold red]\n\n"
        "[bold white]CIPHER: 'This IAM policy was attached to a CI/CD role: "
        "Action s3:*, ec2:*, iam:* on Resource *. The role's credentials "
        "were exposed in a build log. Assess the blast radius. "
        "Write the scoped replacement policy.'[/bold white]"
    ),
    "incident_response": (
        "[bold red]BOSS CHALLENGE — ACTIVE BREACH SIMULATION[/bold red]\n\n"
        "[bold white]CIPHER: 'CloudTrail shows AssumeRole from an unknown IP, "
        "followed by ListBuckets, GetObject on the credentials bucket, "
        "and CreateAccessKey on an admin user. The breach is active. "
        "Walk me through your response — minute by minute.'[/bold white]"
    ),
    "security_culture": (
        "[bold red]BOSS CHALLENGE — SECURITY PROGRAM DESIGN[/bold red]\n\n"
        "[bold white]CIPHER: 'A 50-person engineering org has no security program. "
        "No threat modeling. No SAST. No dependency scanning. No incident "
        "response plan. Design the first 90 days: what do you implement, "
        "in what order, and why? Priorities, not perfection.'[/bold white]"
    ),
}
