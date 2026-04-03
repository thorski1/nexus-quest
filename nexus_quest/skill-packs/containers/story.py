"""
story.py - Narrative text for Containers skill pack (The Container Yard)
Theme: A hardened freight yard where containers move through inspection bays,
       build docks, registries, orchestration grids, and security checkpoints.
CIPHER cyberpunk narrative.
"""

INTRO_STORY = """
The [bold cyan]Container Yard[/bold cyan] sits at the edge of the Ninth Sector's industrial zone.

[bold white]Three square kilometers of automated freight infrastructure. Every shipping
container in the sector — every workload, every service, every batch job — passes
through this yard before it reaches a production rail. The yard is the supply chain.
Control the yard, and you control what runs.[/bold white]

Six months ago, someone did exactly that.

A compromised base image — embedded three layers deep in a multi-stage build — made
it past the vulnerability scanners, past the signing checks, past the admission
controllers. It ran for eleven weeks in production before anyone noticed.

The root cause wasn't a zero-day. It wasn't a novel technique. The image was running
as root. The filesystem was writable. The seccomp profile was disabled for
"compatibility." The registry had no lifecycle policy — images from 2021 were still
tagged as production-ready.

[bold magenta]You've been brought in as the Yard Inspector. Your mandate: understand every layer
of the container stack, from kernel primitives to registry operations to orchestration
to hardening. Not just Docker commands — the actual mechanics. Namespaces. Cgroups.
OCI specs. Build optimization. Registry architecture. Orchestrator internals.
Security boundaries.[/bold magenta]

The yard has five inspection bays. Each one goes deeper.

The containers are waiting. The manifests are on the dock.

[bold cyan]Start with what's underneath. Start with the kernel.[/bold cyan]
"""

ZONE_INTROS = {
    "container_internals": """
[bold cyan]== THE KERNEL BASEMENT ==[/bold cyan]

Before you can secure a container, you need to understand what a container actually is.

Not the Docker abstraction. Not the marketing definition. The kernel primitives.
A container is a process — running inside a set of [yellow]namespaces[/yellow] that isolate
what it can see, constrained by [yellow]cgroups[/yellow] that limit what it can consume,
with a [yellow]layered filesystem[/yellow] assembled from read-only image layers and one
writable layer on top.

There is no "container" kernel object. There is no hypervisor. There is no VM.
Just namespaces, cgroups, and a filesystem. Everything else — Docker, Podman,
containerd, CRI-O — is orchestration around these three primitives.

The [yellow]OCI spec[/yellow] defines how images are built and how containers are run.
The reference implementation is [yellow]runc[/yellow]. But runc is replaceable. The spec is not.

[italic]"If you don't understand the kernel primitives, you don't understand
containers. You just understand the CLI."[/italic]
""",
    "dockerfile_best_practices": """
[bold cyan]== THE BUILD LAB ==[/bold cyan]

The build dock is where images are assembled. Every Dockerfile is a recipe.
Every recipe produces layers. Every layer is cached, distributed, and stored —
whether you intended it or not.

The compromised image that breached the yard was 1.2GB. It was built from
[yellow]ubuntu:latest[/yellow] — not pinned, not versioned, not reproducible. It ran
[yellow]apt-get update[/yellow] in one layer and [yellow]apt-get install[/yellow] in another. It had no
[yellow].dockerignore[/yellow]. The build context included the .git directory, three .env
files, and a 400MB test dataset.

The final image contained the Go compiler, the source code, the test suite,
and the production binary. It could have been 12MB. It was 1.2GB.

[italic]"The Dockerfile tells you everything about how the team builds software.
Most of the time, what it tells you is: carelessly."[/italic]
""",
    "container_registries": """
[bold cyan]== THE ARTIFACT VAULT ==[/bold cyan]

The registry is the distribution layer. Every image in the yard passes through
here — pulled, tagged, pushed, replicated, scanned, signed, and stored.

The vault handles images from Docker Hub, from ECR, from Harbor, from Artifact
Registry. Some signed. Some not. Some scanned. Some carrying CVEs that were
reported eighteen months ago and never patched.

The image that breached the yard was pushed to the internal registry under a
tag that matched the production image: [yellow]myapp:v2.1.4[/yellow]. Same tag. Different
contents. No one verified the digest. No one checked the signature. The CI/CD
pipeline pulled and deployed automatically.

[italic]"A tag is a label. A digest is a fingerprint. Labels can be forged.
Fingerprints cannot."[/italic]
""",
    "orchestration_beyond_k8s": """
[bold cyan]== THE DISPATCH GRID ==[/bold cyan]

Kubernetes gets the headlines. But the container world is bigger than K8s.

The Dispatch Grid manages workloads across four orchestration systems. Nomad
runs the batch processing — heterogeneous workloads, some containers, some raw
binaries, all scheduled by the same engine. ECS runs the AWS-native services
on Fargate — serverless, no instances to manage. Docker Swarm handles the
legacy stack — simple, reliable, built into Docker itself. And Podman runs
the security-sensitive workloads — daemonless, rootless, no central point of
compromise.

Each orchestrator has its own model for defining workloads, scaling them,
networking them, and recovering from failures. Each one makes different trade-offs
between simplicity and power.

[italic]"Kubernetes is not the only answer. Sometimes it's not even the right question."[/italic]
""",
    "container_security": """
[bold cyan]== THE HARDENED PERIMETER ==[/bold cyan]

This is the final inspection bay. The one that matters most.

Every container that leaves this yard for production must pass through the
security checkpoint. Rootless execution. Minimal capabilities. Read-only
filesystem. Seccomp profiles applied. AppArmor profiles loaded. Images signed.
SBOMs generated. Supply chain provenance verified.

The container that breached the yard failed every one of these checks. But the
checks weren't enforced. They were documented. They were in the runbook. They
were in the compliance spreadsheet. But the [yellow]--privileged[/yellow] flag was on the
docker run command, and nobody questioned it.

Documentation doesn't stop breaches. Enforcement does.

[italic]"Security isn't a layer you add at the end. It's a constraint you
apply at every layer, from the base image to the runtime."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "container_internals": """
[bold green]THE KERNEL BASEMENT — MAPPED.[/bold green]

Namespaces. Cgroups. OverlayFS. Copy-on-write. OCI runtime spec. runc. PSI.

You understand what a container actually is — not the abstraction, but the
kernel primitives. A process in a set of namespaces, constrained by cgroups,
with a layered filesystem. No hypervisor. No VM. Just Linux.

The foundation is set. Everything above this — images, orchestration, security —
is built on these primitives.

[bold cyan]The Build Lab is next. Time to see how images are actually constructed.[/bold cyan]
""",
    "dockerfile_best_practices": """
[bold green]THE BUILD LAB — OPTIMIZED.[/bold green]

Multi-stage builds. Layer caching strategies. Distroless base images.
.dockerignore. Exec form vs shell form. The difference between a 1.2GB
image and a 12MB image.

You can read a Dockerfile and immediately identify the anti-patterns:
split apt-get update, COPY before dependency install, shell form entrypoints,
missing USER instructions, bloated build contexts.

The images leaving your build dock are minimal, cached, and reproducible.

[bold cyan]The Artifact Vault. Where images are stored, distributed, signed, and scanned.[/bold cyan]
""",
    "container_registries": """
[bold green]THE ARTIFACT VAULT — SECURED.[/bold green]

Harbor. ECR. Artifact Registry. Cosign. Trivy. Syft. Digests vs tags.
Lifecycle policies. SBOMs. The full registry operations toolkit.

You know the difference between a tag (mutable label) and a digest
(immutable fingerprint). You know how to sign an image, scan it for
vulnerabilities, generate an SBOM, and enforce all of these at deployment time.

No unsigned image leaves this vault. No unscanned image reaches production.

[bold cyan]The Dispatch Grid. Orchestration beyond Kubernetes.[/bold cyan]
""",
    "orchestration_beyond_k8s": """
[bold green]THE DISPATCH GRID — CHARTED.[/bold green]

Nomad task drivers. ECS Fargate task definitions. Docker Swarm services
and manager nodes. Podman's daemonless, rootless architecture.

You understand that container orchestration is not a single-vendor problem.
Different workloads need different schedulers. Batch processing, serverless,
legacy infrastructure, security-critical workloads — each has an orchestrator
that fits.

The grid is mapped. The workloads are dispatched.

[bold cyan]The Hardened Perimeter. The final bay. Security from base image to runtime.[/bold cyan]
""",
    "container_security": """
[bold yellow]--- THE HARDENED PERIMETER — LOCKED DOWN. ---[/bold yellow]

[bold white]The Container Yard is fully secured.[/bold white]

USER instructions. Dropped capabilities. Seccomp profiles. AppArmor confinement.
Read-only filesystems. User namespace remapping. Image signing and verification.
Supply chain provenance. SLSA levels.

Every container that leaves this yard is hardened:
  - Non-root user
  - Minimal capabilities (--cap-drop ALL + explicit adds)
  - Read-only root filesystem
  - Seccomp profile applied
  - Image signed and verified
  - SBOM generated and attached
  - Provenance attestation recorded

The image that breached the yard six months ago would not make it past
the first checkpoint now. Not because you added more tools. Because you
understand what you're defending and why each control exists.

[bold magenta]The yard is operational. The perimeter is hardened.
The containers move through inspection, build, registry, dispatch, and
security — every layer accounted for, every control enforced.[/bold magenta]

[bold yellow]YARD INSPECTOR STATUS: PERIMETER SEALED. SUPPLY CHAIN VERIFIED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "container_internals": "[bold red]>>> KERNEL AUDIT: The Namespace Challenge[/bold red]\nA container escaped its PID namespace. Prove you understand the kernel primitives that were supposed to prevent it.",
    "dockerfile_best_practices": "[bold red]>>> BUILD REVIEW: The 1.2GB Image[/bold red]\nThe bloated image is on the dock. Identify every optimization that should have been applied and wasn't.",
    "container_registries": "[bold red]>>> REGISTRY FORENSICS: The Forged Tag[/bold red]\nSame tag, different image. Someone pushed a compromised build. Prove you know how to detect and prevent it.",
    "orchestration_beyond_k8s": "[bold red]>>> DISPATCH TEST: The Multi-Orchestrator Grid[/bold red]\nFour orchestrators, four workload types. Prove you know which tool fits which problem and why.",
    "container_security": "[bold red]>>> HARDENING AUDIT: The Privileged Container[/bold red]\nThe container is running as root, with all capabilities, writable filesystem, no seccomp, no AppArmor. Lock it down. Every control. Prove you know the full hardening stack.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Layer Inspected", "Read your first container primitive. The yard acknowledged your credentials."),
    "kernel_operative": ("Kernel Mapped", "Cleared the Kernel Basement. Namespaces, cgroups, OCI spec — you know what a container actually is."),
    "build_engineer": ("Build Optimized", "Cleared the Build Lab. Multi-stage, distroless, layer caching — your images are minimal and reproducible."),
    "registry_warden": ("Vault Secured", "Cleared the Artifact Vault. Images signed, scanned, and pinned by digest. No unsigned artifact leaves."),
    "dispatch_commander": ("Grid Charted", "Cleared the Dispatch Grid. Nomad, ECS, Swarm, Podman — you speak every orchestrator's language."),
    "perimeter_sealed": ("YARD INSPECTOR: PERIMETER SEALED", "Cleared the Hardened Perimeter. Every security control applied. Supply chain verified. The yard is locked down."),
    "streak_3": ("Clean Scan", "3 correct in a row. Your container knowledge is building momentum."),
    "streak_5": ("Cached Layer", "5 in a row. You're building knowledge like an optimized multi-stage build — only what's needed, nothing wasted."),
    "streak_10": ("IMMUTABLE DIGEST", "10 in a row. Your understanding is content-addressable. Tamper-proof. Verified."),
    "no_hints": ("No Docs Needed", "Cleared a zone without hints. The OCI spec is already in your head."),
    "speed_demon": ("Sub-5 Inspection", "Answered in under 5 seconds. The manifest was already parsed before you finished reading."),
    "level_10": ("Dock Worker", "Level 10. You can tell a namespace from a cgroup without checking the docs."),
    "level_20": ("Yard Supervisor", "Level 20. You read Dockerfiles the way compilers read code — structurally, not just linearly."),
    "level_30": ("Master Inspector", "Maximum level. From kernel primitives to supply chain attestation, every layer is accounted for."),
    "completionist": ("Full Yard Inspected", "Every zone. Every challenge. Total container infrastructure mastery."),
    "boss_slayer": ("Misconfiguration Caught", "Beat your first boss challenge. The container thought it was secure. It wasn't."),
}
