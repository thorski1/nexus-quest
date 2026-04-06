"""
story.py — Narrative for The Security Pipeline (devsecops skill pack).
Theme: The pipeline is the perimeter. Secure the software supply chain
from first commit to runtime or NEXUS will exploit every gap.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — DEVSECOPS DIVISION[/bold red]

The compromise didn't start in production. It started in a pull request.

A dependency with a typosquatted name slipped past code review. The CI
pipeline had no SAST scanner, no SCA check, no signature verification.
The build ran. The artifact shipped. The container deployed with a
backdoored library that phoned home every 30 seconds — exfiltrating
secrets from environment variables that were never meant to be there.

By the time Falco flagged the anomalous egress traffic, NEXUS had been
inside for eleven days. Eleven days of harvesting credentials, mapping
internal services, pivoting through network policies that allowed all
egress by default.

CIPHER's voice cuts through the noise: [bold cyan]"The pipeline was the
perimeter — and you left it wide open. No static analysis. No secret
scanning. No SBOM. No signature on the artifact. No admission control.
No runtime detection. Every stage was a door you forgot to lock."[/bold cyan]

[bold white]"How do we fix this?"[/bold white]

[bold cyan]"You don't fix it. You rebuild it. Shift-left security into
every pipeline stage. Scan the code. Manage the secrets. Verify the
supply chain. Lock down the runtime. Prove compliance continuously —
not once a quarter with a spreadsheet."[/bold cyan]

A pause. Then: [bold cyan]"Security isn't a stage you add at the end
of the pipeline. It IS the pipeline. Every commit, every build, every
deploy — secured, verified, attested. That's DevSecOps."[/bold cyan]

[italic]Initializing security pipeline framework... 5 sectors to fortify.[/italic]
"""

ZONE_INTROS = {
    "shift_left_security": (
        "[bold cyan]ZONE 1 — SHIFT LEFT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The cheapest bug to fix is the one you catch "
        "before it merges. SAST finds insecure code patterns in the IDE. "
        "DAST hammers the running application like an attacker would. SCA "
        "maps every dependency to every known CVE. Integrate all three into "
        "CI — not as optional checks that developers skip, but as gates "
        "that block the merge. Shift left or pay ten times more to fix it "
        "in production.'[/bold white]"
    ),
    "secret_management": (
        "[bold cyan]ZONE 2 — THE VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The backdoored library found twelve API keys "
        "in environment variables — three of them were root credentials for "
        "production databases. Hardcoded. Never rotated. Visible in build "
        "logs. Secret management isn't optional — it's existential. Vault, "
        "sealed secrets, external secrets operators, automatic rotation — "
        "secrets should be injected at runtime, scoped to the workload, "
        "and rotated before an attacker can use them.'[/bold white]"
    ),
    "supply_chain_security": (
        "[bold cyan]ZONE 3 — THE CHAIN OF TRUST[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The typosquatted package had 200 downloads "
        "before anyone noticed. No one checked the signature because there "
        "was no signature. No one audited the SBOM because there was no "
        "SBOM. Software supply chain security means knowing exactly what's "
        "in your artifacts — every dependency, every layer, every binary. "
        "SBOM, Sigstore, SLSA provenance, admission controllers that reject "
        "unsigned images. Trust nothing that isn't attested.'[/bold white]"
    ),
    "runtime_security": (
        "[bold cyan]ZONE 4 — THE WATCHTOWER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The container ran for eleven days with an "
        "active backdoor. No one noticed because no one was watching the "
        "syscalls. Falco would have caught it on day one — an unexpected "
        "outbound connection, a shell spawned inside a container, a binary "
        "written to /tmp. eBPF traces kernel-level behavior without agents. "
        "Network policies restrict lateral movement. Runtime security is "
        "your last line of defense — make it count.'[/bold white]"
    ),
    "compliance_as_code": (
        "[bold cyan]ZONE 5 — THE AUDIT TRAIL[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The auditors asked for evidence of encryption "
        "at rest, access controls, and incident response procedures. The "
        "team spent three weeks assembling screenshots. That's not compliance "
        "— that's archaeology. Compliance as code means CIS benchmarks run "
        "in CI. SOC 2 controls are policy-as-code with OPA. HIPAA requirements "
        "are automated checks, not checkbox spreadsheets. Continuous compliance "
        "means you're always audit-ready — not scrambling once a quarter.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "shift_left_security": (
        "[bold green]ZONE CLEAR — SHIFT LEFT[/bold green]\n\n"
        "SAST, DAST, SCA — integrated into every pipeline, gating every merge. "
        "Vulnerabilities are caught at the source, not discovered in production. "
        "CIPHER: 'The left side of the pipeline is locked down. "
        "Insecure code doesn't make it past the first gate.'"
    ),
    "secret_management": (
        "[bold green]ZONE CLEAR — THE VAULT[/bold green]\n\n"
        "Secrets centralized, encrypted, rotated, and injected at runtime. "
        "No more hardcoded credentials. No more eternal API keys in env vars. "
        "CIPHER: 'The vault is sealed. Secrets are ephemeral, scoped, "
        "and rotated. Even if they're stolen, they expire before they're useful.'"
    ),
    "supply_chain_security": (
        "[bold green]ZONE CLEAR — THE CHAIN OF TRUST[/bold green]\n\n"
        "Every artifact has an SBOM, a signature, and provenance metadata. "
        "Admission controllers reject anything unsigned or unattested. "
        "CIPHER: 'The supply chain is verified. Every dependency is known. "
        "Every artifact is signed. NEXUS can't slip a trojan through the build anymore.'"
    ),
    "runtime_security": (
        "[bold green]ZONE CLEAR — THE WATCHTOWER[/bold green]\n\n"
        "Falco watches syscalls. eBPF traces kernel events. Network policies "
        "enforce zero-trust lateral movement. Anomalies trigger alerts in seconds. "
        "CIPHER: 'The watchtower is manned. Every unexpected syscall, every "
        "anomalous connection — detected and contained. Eleven silent days "
        "will never happen again.'"
    ),
    "compliance_as_code": (
        "[bold green]ZONE CLEAR — THE AUDIT TRAIL[/bold green]\n\n"
        "CIS benchmarks automated. SOC 2 controls codified. HIPAA requirements "
        "verified on every deploy. Compliance is continuous, not quarterly. "
        "CIPHER: 'The audit trail is permanent. Every control is tested on "
        "every commit. The auditors won't find gaps — because the pipeline "
        "won't let gaps ship.'"
    ),
}

BOSS_INTROS = {
    "shift_left_security": (
        "[bold red]BOSS CHALLENGE — PIPELINE SECURITY AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'A team's CI pipeline runs unit tests and "
        "deploys on merge. No SAST, no SCA, no DAST. Last week a developer "
        "committed an SQL injection vulnerability and a dependency with a "
        "critical CVE. Both shipped to production. Design the security "
        "gates for this pipeline — what tools, what order, what blocks "
        "the merge vs. what warns.'[/bold white]"
    ),
    "secret_management": (
        "[bold red]BOSS CHALLENGE — SECRET SPRAWL REMEDIATION[/bold red]\n\n"
        "[bold white]CIPHER: 'A git-secrets scan reveals 23 hardcoded "
        "credentials across 14 repositories. AWS keys, database passwords, "
        "API tokens — some committed years ago, never rotated. Design the "
        "remediation plan: immediate triage, rotation strategy, migration "
        "to centralized secret management, and prevention controls.'[/bold white]"
    ),
    "supply_chain_security": (
        "[bold red]BOSS CHALLENGE — COMPROMISED DEPENDENCY[/bold red]\n\n"
        "[bold white]CIPHER: 'A popular npm package your services depend on "
        "was compromised — the maintainer's account was hijacked and a "
        "malicious version published. Your CI pulled it automatically. "
        "How do you detect which builds are affected, contain the blast "
        "radius, and prevent this class of attack going forward?'[/bold white]"
    ),
    "runtime_security": (
        "[bold red]BOSS CHALLENGE — CONTAINER BREAKOUT DETECTION[/bold red]\n\n"
        "[bold white]CIPHER: 'Falco fires three alerts in rapid succession: "
        "a shell spawned in a production container, a binary written to /tmp, "
        "and an outbound connection to an IP in a known C2 range. The "
        "container is in a namespace with network policies allowing all "
        "egress. Walk me through your response — detection to containment "
        "to forensics — and the policy changes to prevent recurrence.'[/bold white]"
    ),
    "compliance_as_code": (
        "[bold red]BOSS CHALLENGE — AUDIT AUTOMATION DESIGN[/bold red]\n\n"
        "[bold white]CIPHER: 'Your company needs SOC 2 Type II certification. "
        "The auditor needs evidence of 47 controls — access management, "
        "encryption, logging, incident response, change management. Currently "
        "it takes the team 4 weeks to gather evidence manually. Design a "
        "compliance-as-code system that provides continuous evidence "
        "collection. What tools, what policies, what pipeline stages?'[/bold white]"
    ),
}
