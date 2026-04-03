"""
zones.py - All zone and challenge data for Containers skill pack (The Container Yard)
Theme: Deep container knowledge beyond basic Docker — internals, best practices,
       registries, alternative orchestrators, and security hardening.
Challenge types: quiz (multiple choice, a/b/c/d) and text (free-form answer)
"""

ZONE_ORDER = [
    "container_internals",
    "dockerfile_best_practices",
    "container_registries",
    "orchestration_beyond_k8s",
    "container_security",
]

ZONES = {
    # ── ZONE 1: CONTAINER INTERNALS ──────────────────────────────────────
    "container_internals": {
        "id": "container_internals",
        "name": "The Kernel Basement",
        "subtitle": "Namespaces, Cgroups, Overlay FS, and the OCI Spec",
        "color": "cyan",
        "icon": "🔬",
        "challenges": [
            {
                "id": "ci_1",
                "type": "quiz",
                "question": (
                    "Containers achieve process isolation using a Linux kernel feature\n"
                    "that partitions kernel resources so that one set of processes sees\n"
                    "one set of resources while another set sees a different set.\n\n"
                    "What is this kernel feature called?"
                ),
                "options": [
                    "Namespaces",
                    "Cgroups",
                    "SELinux contexts",
                    "Capabilities",
                ],
                "answer": "a",
                "lesson": (
                    "Linux namespaces provide isolation for system resources.\n"
                    "Each namespace type isolates a different resource:\n\n"
                    "  PID   — process IDs (container sees its own PID 1)\n"
                    "  NET   — network stack (own interfaces, IPs, routes)\n"
                    "  MNT   — mount points (own filesystem tree)\n"
                    "  UTS   — hostname and domain name\n"
                    "  IPC   — inter-process communication\n"
                    "  USER  — user and group IDs\n"
                    "  CGROUP — cgroup root directory\n\n"
                    "A container is, at its core, a process running inside a set of\n"
                    "namespaces. There is no 'container' kernel object — just namespaces\n"
                    "applied to a process."
                ),
                "xp": 25,
            },
            {
                "id": "ci_2",
                "type": "quiz",
                "question": (
                    "You need to limit a container to use a maximum of 512MB of RAM\n"
                    "and 1.5 CPU cores. Which Linux kernel feature enforces these\n"
                    "resource limits?"
                ),
                "options": [
                    "Namespaces",
                    "Control groups (cgroups)",
                    "seccomp filters",
                    "iptables rules",
                ],
                "answer": "b",
                "lesson": (
                    "Control groups (cgroups) limit, account for, and isolate resource\n"
                    "usage (CPU, memory, disk I/O, network) of a collection of processes.\n\n"
                    "Key cgroup subsystems:\n"
                    "  memory  — set hard/soft memory limits; OOM killer triggers at limit\n"
                    "  cpu     — allocate CPU shares, set CFS quota/period\n"
                    "  blkio   — limit block I/O rates per device\n"
                    "  pids    — limit number of processes (fork bomb protection)\n\n"
                    "cgroups v2 (unified hierarchy) is the modern default. It merges all\n"
                    "controllers under a single hierarchy and adds pressure stall\n"
                    "information (PSI) for detecting resource contention."
                ),
                "xp": 25,
            },
            {
                "id": "ci_3",
                "type": "text",
                "question": (
                    "Container images use a layered filesystem. When a container starts,\n"
                    "a thin writable layer is placed on top of the read-only image layers.\n\n"
                    "What is the name of the default storage driver that implements this\n"
                    "layered filesystem in modern Docker installations?\n\n"
                    "Answer with two words (e.g., overlay2)."
                ),
                "options": [],
                "answer": "overlay2",
                "lesson": (
                    "overlay2 is the default storage driver for Docker on modern Linux.\n"
                    "It uses the OverlayFS kernel module to merge multiple directories\n"
                    "(layers) into a single unified view.\n\n"
                    "How it works:\n"
                    "  lowerdir  — read-only image layers (stacked)\n"
                    "  upperdir  — writable container layer (copy-on-write)\n"
                    "  workdir   — internal scratch space for atomic operations\n"
                    "  merged    — the unified view the container process sees\n\n"
                    "When a container modifies a file from a lower layer, OverlayFS\n"
                    "copies it up to the upper layer first (copy-on-write). This is\n"
                    "why writing to large files in containers can be slow — the entire\n"
                    "file is copied, not just the changed bytes."
                ),
                "xp": 30,
            },
            {
                "id": "ci_4",
                "type": "quiz",
                "question": (
                    "The OCI (Open Container Initiative) defines two core specifications.\n"
                    "One is the Image Spec (how images are built and distributed).\n\n"
                    "What is the other core OCI specification?"
                ),
                "options": [
                    "The Runtime Spec (how containers are created and run)",
                    "The Network Spec (how containers communicate)",
                    "The Storage Spec (how layers are persisted)",
                    "The Security Spec (how containers are hardened)",
                ],
                "answer": "a",
                "lesson": (
                    "The OCI defines two core specs:\n\n"
                    "  1. Image Spec (image-spec)\n"
                    "     Defines the format of container images: manifest, config,\n"
                    "     layer tarballs, content-addressable storage.\n\n"
                    "  2. Runtime Spec (runtime-spec)\n"
                    "     Defines how to run a 'filesystem bundle' — the lifecycle\n"
                    "     of a container process: create, start, stop, delete.\n"
                    "     The reference implementation is runc.\n\n"
                    "There is also the Distribution Spec (how images are pushed/pulled\n"
                    "from registries), added later.\n\n"
                    "OCI compliance means any OCI image can run on any OCI runtime.\n"
                    "Docker, Podman, containerd, CRI-O — all OCI-compliant."
                ),
                "xp": 25,
            },
            {
                "id": "ci_5",
                "type": "text",
                "question": (
                    "Inside a container, processes believe they are the only ones\n"
                    "running. The init process inside the container has PID 1 from\n"
                    "the container's perspective.\n\n"
                    "Which specific Linux namespace type provides this PID isolation?\n\n"
                    "Answer with the namespace name (three letters)."
                ),
                "options": [],
                "answer": "pid",
                "lesson": (
                    "The PID namespace isolates the process ID number space.\n"
                    "Processes in different PID namespaces can have the same PID.\n\n"
                    "Key behaviors:\n"
                    "  - The first process in a new PID namespace gets PID 1\n"
                    "  - PID 1 has special signal handling (won't die from SIGTERM\n"
                    "    unless it explicitly handles it)\n"
                    "  - Processes in the container can't see host processes\n"
                    "  - The host CAN see container processes (with different PIDs)\n\n"
                    "This is why 'kill 1' from inside a container behaves differently\n"
                    "than you'd expect — and why proper signal handling in your\n"
                    "entrypoint matters for graceful shutdown."
                ),
                "xp": 30,
            },
            {
                "id": "ci_6",
                "type": "quiz",
                "question": (
                    "When a container writes to a file that exists in a read-only\n"
                    "image layer, the file must first be copied to the writable layer.\n\n"
                    "What is this mechanism called?"
                ),
                "options": [
                    "Copy-on-write (CoW)",
                    "Write-ahead logging (WAL)",
                    "Memory-mapped I/O (mmap)",
                    "Direct I/O (DIO)",
                ],
                "answer": "a",
                "lesson": (
                    "Copy-on-write (CoW) is the mechanism that makes layered filesystems\n"
                    "efficient. Layers share unchanged files; only modified files are\n"
                    "copied to the writable layer.\n\n"
                    "Performance implications:\n"
                    "  - First write to a large file is slow (full copy to upper layer)\n"
                    "  - Subsequent writes to the same file are fast (already in upper)\n"
                    "  - Deleting a lower-layer file creates a 'whiteout' file in upper\n"
                    "  - The image layers remain untouched and reusable\n\n"
                    "This is why databases in containers should use volumes, not the\n"
                    "container filesystem — CoW overhead on heavy write workloads is\n"
                    "significant."
                ),
                "xp": 25,
            },
            {
                "id": "ci_7",
                "type": "quiz",
                "question": (
                    "The low-level container runtime that Docker and containerd use\n"
                    "by default to actually create and run containers is the OCI\n"
                    "reference implementation.\n\n"
                    "What is it called?"
                ),
                "options": [
                    "runc",
                    "crun",
                    "gVisor",
                    "Kata Containers",
                ],
                "answer": "a",
                "lesson": (
                    "runc is the OCI reference implementation for the runtime spec.\n"
                    "It's a small CLI tool that spawns and runs containers given an\n"
                    "OCI bundle (a root filesystem + config.json).\n\n"
                    "The container runtime stack:\n"
                    "  Docker CLI -> dockerd -> containerd -> runc\n"
                    "  Kubernetes -> CRI -> containerd/CRI-O -> runc\n\n"
                    "Alternatives to runc:\n"
                    "  crun     — written in C, faster startup, lower memory\n"
                    "  gVisor   — application kernel, stronger isolation\n"
                    "  Kata     — lightweight VMs, hardware isolation\n"
                    "  youki    — written in Rust\n\n"
                    "You can swap runc for any OCI-compliant runtime without changing\n"
                    "your images or orchestration layer."
                ),
                "xp": 25,
            },
            {
                "id": "ci_8",
                "type": "text",
                "question": (
                    "Linux cgroups v2 introduced a feature that provides per-resource\n"
                    "pressure metrics, allowing you to detect when processes are\n"
                    "stalling due to resource contention (CPU, memory, I/O).\n\n"
                    "What is this feature called? (three-letter abbreviation)"
                ),
                "options": [],
                "answer": "psi",
                "lesson": (
                    "PSI (Pressure Stall Information) is a cgroups v2 feature that\n"
                    "exposes metrics about resource contention.\n\n"
                    "PSI tracks three resources:\n"
                    "  /proc/pressure/cpu    — CPU pressure\n"
                    "  /proc/pressure/memory — memory pressure\n"
                    "  /proc/pressure/io     — I/O pressure\n\n"
                    "Each file reports 'some' and 'full' stall percentages:\n"
                    "  some — at least one task stalled on the resource\n"
                    "  full — ALL tasks stalled (nothing productive happening)\n\n"
                    "PSI is critical for container autoscaling decisions — it tells\n"
                    "you not just utilization, but whether the workload is actually\n"
                    "suffering from resource limits."
                ),
                "xp": 30,
            },
        ],
    },

    # ── ZONE 2: DOCKERFILE BEST PRACTICES ────────────────────────────────
    "dockerfile_best_practices": {
        "id": "dockerfile_best_practices",
        "name": "The Build Lab",
        "subtitle": "Multi-Stage Builds, Layer Caching, Distroless, and .dockerignore",
        "color": "yellow",
        "icon": "🏗️",
        "challenges": [
            {
                "id": "df_1",
                "type": "quiz",
                "question": (
                    "You're building a Go application. The build toolchain is 800MB\n"
                    "but the compiled binary is 12MB. You want the final image to\n"
                    "contain only the binary.\n\n"
                    "Which Dockerfile technique achieves this?"
                ),
                "options": [
                    "Multi-stage build",
                    "Squash layers",
                    "Use FROM scratch as base",
                    "RUN rm -rf /usr/local/go after compilation",
                ],
                "answer": "a",
                "lesson": (
                    "Multi-stage builds use multiple FROM instructions in a single\n"
                    "Dockerfile. Each FROM starts a new build stage. You can copy\n"
                    "artifacts from one stage to another, discarding everything else.\n\n"
                    "Example:\n"
                    "  FROM golang:1.22 AS builder\n"
                    "  WORKDIR /app\n"
                    "  COPY . .\n"
                    "  RUN go build -o /app/server\n\n"
                    "  FROM gcr.io/distroless/static\n"
                    "  COPY --from=builder /app/server /server\n"
                    "  CMD [\"/server\"]\n\n"
                    "Result: final image contains only the binary (~12MB) instead of\n"
                    "the full Go toolchain (~800MB). Build tools, source code, and\n"
                    "intermediate files never make it to the final image."
                ),
                "xp": 25,
            },
            {
                "id": "df_2",
                "type": "quiz",
                "question": (
                    "Docker caches each layer during builds. If a layer hasn't changed,\n"
                    "Docker reuses the cached version instead of rebuilding it.\n\n"
                    "Which of these Dockerfile patterns BEST leverages layer caching\n"
                    "for a Node.js application?"
                ),
                "options": [
                    "COPY . . then RUN npm install",
                    "COPY package*.json . then RUN npm install then COPY . .",
                    "RUN npm install then COPY . .",
                    "COPY . . then RUN npm ci --production",
                ],
                "answer": "b",
                "lesson": (
                    "Layer caching rule: if any file in a COPY/ADD instruction changes,\n"
                    "that layer AND all subsequent layers are invalidated.\n\n"
                    "Optimal pattern for Node.js:\n"
                    "  COPY package.json package-lock.json ./\n"
                    "  RUN npm ci\n"
                    "  COPY . .\n\n"
                    "Why this works:\n"
                    "  1. package*.json rarely changes -> npm install layer is cached\n"
                    "  2. Source code changes often -> only the final COPY is rebuilt\n"
                    "  3. npm ci is deterministic (uses lock file exactly)\n\n"
                    "If you COPY . . first, ANY source file change invalidates the\n"
                    "npm install layer, forcing a full reinstall every build."
                ),
                "xp": 25,
            },
            {
                "id": "df_3",
                "type": "quiz",
                "question": (
                    "Google's distroless container images are designed for production.\n"
                    "They contain your application and its runtime dependencies — nothing else.\n\n"
                    "What is MISSING from distroless images that exists in standard base images?"
                ),
                "options": [
                    "Shell, package manager, and common Unix utilities",
                    "The Linux kernel",
                    "Shared libraries (libc, libssl)",
                    "The /proc and /sys filesystems",
                ],
                "answer": "a",
                "lesson": (
                    "Distroless images (gcr.io/distroless/*) contain:\n"
                    "  - Your application binary or interpreted code\n"
                    "  - Runtime libraries (libc, libssl, etc.)\n"
                    "  - CA certificates, timezone data, /etc/passwd\n\n"
                    "They do NOT contain:\n"
                    "  - Shell (no sh, bash, ash)\n"
                    "  - Package manager (no apt, apk, yum)\n"
                    "  - Utilities (no curl, wget, ls, cat)\n\n"
                    "Security benefit: if an attacker gets code execution inside a\n"
                    "distroless container, there's no shell to drop into, no tools\n"
                    "to download payloads with, no package manager to install anything.\n\n"
                    "Debugging trade-off: you can't exec into a distroless container\n"
                    "for troubleshooting. Use ephemeral debug containers (kubectl debug)\n"
                    "or sidecar containers instead."
                ),
                "xp": 25,
            },
            {
                "id": "df_4",
                "type": "text",
                "question": (
                    "You notice your Docker build context is 2GB because it's sending\n"
                    "node_modules/, .git/, and build artifacts to the daemon.\n\n"
                    "What file do you create in your project root to exclude files\n"
                    "and directories from the build context?\n\n"
                    "Answer with the filename (including the dot)."
                ),
                "options": [],
                "answer": ".dockerignore",
                "lesson": (
                    ".dockerignore works like .gitignore but for the Docker build context.\n"
                    "It prevents files from being sent to the Docker daemon during builds.\n\n"
                    "Common entries:\n"
                    "  .git\n"
                    "  node_modules\n"
                    "  *.md\n"
                    "  .env\n"
                    "  dist/\n"
                    "  __pycache__\n"
                    "  .pytest_cache\n\n"
                    "Why it matters:\n"
                    "  - Build context is tar'd and sent to the daemon (even remote daemons)\n"
                    "  - Large contexts slow down every build\n"
                    "  - Sensitive files (.env, credentials) in the context can end up\n"
                    "    in image layers if COPY . . is used\n\n"
                    "Without .dockerignore, COPY . . copies EVERYTHING in the build context."
                ),
                "xp": 30,
            },
            {
                "id": "df_5",
                "type": "quiz",
                "question": (
                    "You have this Dockerfile:\n\n"
                    "  RUN apt-get update\n"
                    "  RUN apt-get install -y curl\n\n"
                    "A colleague says this is a known anti-pattern. Why?"
                ),
                "options": [
                    "The apt-get update layer gets cached separately; install may use stale package lists",
                    "apt-get update requires root permissions that containers don't have",
                    "Two RUN instructions create two layers, which exceeds the layer limit",
                    "apt-get install -y is dangerous because it auto-confirms removals",
                ],
                "answer": "a",
                "lesson": (
                    "Splitting apt-get update and apt-get install into separate RUN\n"
                    "instructions is a caching bug.\n\n"
                    "The problem:\n"
                    "  1. RUN apt-get update -> cached layer with package lists from day 1\n"
                    "  2. Later, you add a new package to the install line\n"
                    "  3. Layer 1 (update) is still cached -> stale package lists\n"
                    "  4. Layer 2 (install) rebuilds but can't find the new package\n\n"
                    "Correct pattern — combine in one RUN:\n"
                    "  RUN apt-get update && \\\n"
                    "      apt-get install -y --no-install-recommends curl && \\\n"
                    "      rm -rf /var/lib/apt/lists/*\n\n"
                    "The rm at the end removes the package lists from the layer,\n"
                    "reducing image size."
                ),
                "xp": 25,
            },
            {
                "id": "df_6",
                "type": "text",
                "question": (
                    "In a multi-stage Dockerfile, you want to copy the compiled binary\n"
                    "from a stage named 'builder' into the final image.\n\n"
                    "Complete the instruction: COPY ___=builder /app/bin /usr/local/bin/\n\n"
                    "Answer with the flag (including the --)."
                ),
                "options": [],
                "answer": "--from",
                "lesson": (
                    "COPY --from=<stage> copies files from a previous build stage\n"
                    "instead of the build context.\n\n"
                    "Usage:\n"
                    "  COPY --from=builder /app/bin /usr/local/bin/\n"
                    "  COPY --from=0 /app/bin /usr/local/bin/   (by stage index)\n\n"
                    "You can also copy from external images:\n"
                    "  COPY --from=nginx:latest /etc/nginx/nginx.conf /etc/nginx/\n\n"
                    "This is the key mechanism that makes multi-stage builds work.\n"
                    "The final image only contains what you explicitly COPY --from.\n"
                    "Everything else (compilers, build deps, source code) stays in\n"
                    "the build stage and is discarded."
                ),
                "xp": 30,
            },
            {
                "id": "df_7",
                "type": "quiz",
                "question": (
                    "You want the absolute smallest possible base image — it contains\n"
                    "nothing at all. No OS, no shell, no libraries. Just an empty\n"
                    "filesystem you add to.\n\n"
                    "What is this special Docker base image called?"
                ),
                "options": [
                    "FROM scratch",
                    "FROM alpine:empty",
                    "FROM null",
                    "FROM busybox:minimal",
                ],
                "answer": "a",
                "lesson": (
                    "FROM scratch is a special empty base image. It contains nothing.\n"
                    "You must provide everything your application needs.\n\n"
                    "Use cases:\n"
                    "  - Statically compiled Go binaries (no libc dependency)\n"
                    "  - Statically compiled Rust binaries\n"
                    "  - Base images for other images (e.g., Alpine itself is FROM scratch)\n\n"
                    "What you lose:\n"
                    "  - No shell -> can't use shell form CMD/ENTRYPOINT\n"
                    "  - No libc -> dynamically linked binaries won't work\n"
                    "  - No CA certs -> HTTPS calls fail unless you add them\n"
                    "  - No timezone data -> time operations may fail\n\n"
                    "Typical scratch image size: just the binary. A Go HTTP server\n"
                    "can be under 10MB."
                ),
                "xp": 25,
            },
            {
                "id": "df_8",
                "type": "quiz",
                "question": (
                    "Your Dockerfile has this instruction:\n\n"
                    "  ENTRYPOINT [\"python\", \"app.py\"]\n\n"
                    "This is the 'exec form.' What happens differently when you use\n"
                    "the 'shell form' instead: ENTRYPOINT python app.py?"
                ),
                "options": [
                    "The process runs as a child of /bin/sh -c, preventing proper signal handling",
                    "The process runs with elevated privileges",
                    "The process cannot access environment variables",
                    "The process ignores the CMD instruction entirely",
                ],
                "answer": "a",
                "lesson": (
                    "Exec form vs shell form has critical implications:\n\n"
                    "  Exec form: ENTRYPOINT [\"python\", \"app.py\"]\n"
                    "  -> python runs as PID 1\n"
                    "  -> Receives signals directly (SIGTERM for graceful shutdown)\n"
                    "  -> No variable expansion ($VAR won't be substituted)\n\n"
                    "  Shell form: ENTRYPOINT python app.py\n"
                    "  -> Runs as: /bin/sh -c 'python app.py'\n"
                    "  -> sh is PID 1, python is a child process\n"
                    "  -> SIGTERM goes to sh, NOT to python\n"
                    "  -> Container may not shut down gracefully (10s timeout, then SIGKILL)\n\n"
                    "Always use exec form for ENTRYPOINT in production. If you need\n"
                    "shell features (variable expansion, pipes), use a shell script\n"
                    "as the entrypoint with exec to replace the shell process."
                ),
                "xp": 25,
            },
        ],
    },

    # ── ZONE 3: CONTAINER REGISTRIES ─────────────────────────────────────
    "container_registries": {
        "id": "container_registries",
        "name": "The Artifact Vault",
        "subtitle": "Harbor, ECR, GCR, Image Signing, and Vulnerability Scanning",
        "color": "magenta",
        "icon": "🏛️",
        "challenges": [
            {
                "id": "cr_1",
                "type": "quiz",
                "question": (
                    "Your organization needs a self-hosted, open-source container\n"
                    "registry with built-in vulnerability scanning, RBAC, image\n"
                    "replication across sites, and audit logging.\n\n"
                    "Which registry best fits this description?"
                ),
                "options": [
                    "Harbor",
                    "Docker Hub",
                    "Nexus Repository",
                    "GitHub Container Registry",
                ],
                "answer": "a",
                "lesson": (
                    "Harbor is a CNCF graduated project — an enterprise-grade,\n"
                    "open-source container registry.\n\n"
                    "Key features:\n"
                    "  - Vulnerability scanning (Trivy integration by default)\n"
                    "  - Role-based access control (RBAC) with LDAP/AD/OIDC\n"
                    "  - Image replication across multiple registries\n"
                    "  - Content trust and image signing (Notary/Cosign)\n"
                    "  - Audit logging for compliance\n"
                    "  - Garbage collection for storage management\n"
                    "  - Webhook notifications\n\n"
                    "Harbor sits in front of a distribution/registry backend and adds\n"
                    "the enterprise features that Docker Distribution alone lacks."
                ),
                "xp": 25,
            },
            {
                "id": "cr_2",
                "type": "quiz",
                "question": (
                    "You're using AWS and want to store container images close to your\n"
                    "ECS/EKS workloads. Which AWS service is purpose-built as a\n"
                    "container image registry?"
                ),
                "options": [
                    "Amazon ECR (Elastic Container Registry)",
                    "Amazon S3 with Docker Distribution",
                    "AWS CodeArtifact",
                    "Amazon EFS (Elastic File System)",
                ],
                "answer": "a",
                "lesson": (
                    "Amazon ECR (Elastic Container Registry) is AWS's managed\n"
                    "container registry service.\n\n"
                    "Key features:\n"
                    "  - Integrated with IAM for authentication (no separate creds)\n"
                    "  - Image scanning via Amazon Inspector (or basic Clair scanning)\n"
                    "  - Cross-region and cross-account replication\n"
                    "  - Lifecycle policies (auto-delete old/untagged images)\n"
                    "  - Encryption at rest (KMS)\n"
                    "  - VPC endpoints (pull images without internet access)\n\n"
                    "Authentication:\n"
                    "  aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com\n\n"
                    "ECR Public is the public registry variant (like Docker Hub but on AWS)."
                ),
                "xp": 25,
            },
            {
                "id": "cr_3",
                "type": "text",
                "question": (
                    "You want to cryptographically verify that a container image\n"
                    "was built by your CI/CD pipeline and hasn't been tampered with.\n"
                    "The Sigstore project provides a tool for signing OCI artifacts\n"
                    "using keyless signing with OIDC identities.\n\n"
                    "What is this signing tool called? (one word)"
                ),
                "options": [],
                "answer": "cosign",
                "lesson": (
                    "Cosign (part of the Sigstore project) signs and verifies\n"
                    "container images and other OCI artifacts.\n\n"
                    "Signing modes:\n"
                    "  Key-based:  cosign sign --key cosign.key <image>\n"
                    "  Keyless:    cosign sign <image>  (uses OIDC identity + Fulcio CA)\n\n"
                    "Keyless flow:\n"
                    "  1. Authenticate via OIDC (GitHub Actions, Google, etc.)\n"
                    "  2. Fulcio issues a short-lived signing certificate\n"
                    "  3. Signature is recorded in Rekor (transparency log)\n"
                    "  4. Certificate expires, but the Rekor entry proves it was valid\n\n"
                    "Verification:\n"
                    "  cosign verify --certificate-identity=<email> --certificate-oidc-issuer=<issuer> <image>\n\n"
                    "Kubernetes admission controllers (like Kyverno or OPA Gatekeeper)\n"
                    "can enforce that only signed images are deployed."
                ),
                "xp": 30,
            },
            {
                "id": "cr_4",
                "type": "quiz",
                "question": (
                    "Your security team requires that no container image with a\n"
                    "CRITICAL or HIGH CVE can be deployed to production. The scanning\n"
                    "must happen automatically when images are pushed to the registry.\n\n"
                    "Which open-source scanner (now the default in Harbor) would you use?"
                ),
                "options": [
                    "Trivy",
                    "Nessus",
                    "Nmap",
                    "OWASP ZAP",
                ],
                "answer": "a",
                "lesson": (
                    "Trivy (by Aqua Security) is the most widely adopted open-source\n"
                    "container vulnerability scanner.\n\n"
                    "What it scans:\n"
                    "  - OS packages (Alpine, Debian, Ubuntu, RHEL, etc.)\n"
                    "  - Application dependencies (npm, pip, go.mod, Gemfile, etc.)\n"
                    "  - IaC misconfigurations (Terraform, Kubernetes manifests)\n"
                    "  - Secrets in image layers\n\n"
                    "Usage:\n"
                    "  trivy image nginx:latest\n"
                    "  trivy image --severity HIGH,CRITICAL myapp:v1.2\n"
                    "  trivy fs .                  (scan local project)\n"
                    "  trivy k8s --report summary  (scan running cluster)\n\n"
                    "Trivy is the default scanner in Harbor and is widely used in\n"
                    "CI/CD pipelines (GitHub Actions, GitLab CI, etc.)."
                ),
                "xp": 25,
            },
            {
                "id": "cr_5",
                "type": "quiz",
                "question": (
                    "An image tag like 'myapp:latest' is mutable — someone can push\n"
                    "a different image under the same tag. To guarantee you're pulling\n"
                    "the exact same image every time, you should reference it by its\n"
                    "content-addressable identifier.\n\n"
                    "What is this identifier called?"
                ),
                "options": [
                    "Image digest (sha256 hash)",
                    "Image ID",
                    "Layer checksum",
                    "Build number",
                ],
                "answer": "a",
                "lesson": (
                    "An image digest is a sha256 hash of the image manifest. It is\n"
                    "immutable — if any bit of the image changes, the digest changes.\n\n"
                    "Reference by tag (mutable):\n"
                    "  docker pull myapp:v1.2\n\n"
                    "Reference by digest (immutable):\n"
                    "  docker pull myapp@sha256:abc123...\n\n"
                    "Why digests matter:\n"
                    "  - Tags can be overwritten (especially 'latest')\n"
                    "  - In a supply chain attack, an attacker pushes a new image\n"
                    "    under an existing tag\n"
                    "  - Digests guarantee bit-for-bit reproducibility\n\n"
                    "Best practice: pin production deployments to digests, not tags.\n"
                    "Use tags for human readability, digests for machine guarantees."
                ),
                "xp": 25,
            },
            {
                "id": "cr_6",
                "type": "text",
                "question": (
                    "Google Cloud's managed container registry service (the newer one\n"
                    "that replaced the original Container Registry) stores images in\n"
                    "regional repositories with fine-grained IAM.\n\n"
                    "What is this service called? (two words, no 'Google' prefix)"
                ),
                "options": [],
                "answer": "artifact registry",
                "lesson": (
                    "Google Artifact Registry is the successor to Google Container\n"
                    "Registry (GCR). It stores not just container images but also\n"
                    "language packages (npm, Maven, Python, etc.).\n\n"
                    "Key features:\n"
                    "  - Regional and multi-regional repositories\n"
                    "  - Fine-grained IAM (per-repository, not just per-project)\n"
                    "  - Vulnerability scanning (integration with Container Analysis)\n"
                    "  - Supports Docker, OCI, Helm charts, and language packages\n"
                    "  - VPC Service Controls for private access\n\n"
                    "Repository URL format:\n"
                    "  <region>-docker.pkg.dev/<project>/<repo>/<image>:<tag>\n\n"
                    "GCR (gcr.io) still works but is in maintenance mode.\n"
                    "All new projects should use Artifact Registry."
                ),
                "xp": 30,
            },
            {
                "id": "cr_7",
                "type": "quiz",
                "question": (
                    "Your ECR lifecycle policy should automatically clean up images\n"
                    "to control storage costs. Which strategy is MOST appropriate for\n"
                    "production repositories?"
                ),
                "options": [
                    "Expire untagged images after N days; keep last N tagged images",
                    "Delete all images older than 7 days",
                    "Keep only the 'latest' tag and delete everything else",
                    "Manually delete images quarterly",
                ],
                "answer": "a",
                "lesson": (
                    "ECR lifecycle policies automate image cleanup based on rules.\n\n"
                    "Best practices:\n"
                    "  1. Expire untagged images (build artifacts) after 1-7 days\n"
                    "  2. Keep the last N tagged images (e.g., 20) for rollback\n"
                    "  3. Never auto-delete images that are currently deployed\n\n"
                    "Example policy rules:\n"
                    "  - Rule 1: imageCountMoreThan 20, tagStatus: tagged -> expire\n"
                    "  - Rule 2: sinceImagePushed 1 day, tagStatus: untagged -> expire\n\n"
                    "Similar features exist in:\n"
                    "  - Harbor: tag retention policies\n"
                    "  - Artifact Registry: cleanup policies\n"
                    "  - Docker Hub: inactive image retention (paid plans)\n\n"
                    "Registry storage costs are real. Without lifecycle policies,\n"
                    "registries grow unbounded."
                ),
                "xp": 25,
            },
            {
                "id": "cr_8",
                "type": "quiz",
                "question": (
                    "You want to generate and attach a Software Bill of Materials\n"
                    "(SBOM) to your container image to document every package and\n"
                    "dependency inside it.\n\n"
                    "Which tool generates SBOMs from container images?"
                ),
                "options": [
                    "Syft",
                    "Cosign",
                    "Trivy",
                    "Notary",
                ],
                "answer": "a",
                "lesson": (
                    "Syft (by Anchore) generates Software Bills of Materials (SBOMs)\n"
                    "from container images, filesystems, and archives.\n\n"
                    "Usage:\n"
                    "  syft <image>                 (default table output)\n"
                    "  syft <image> -o spdx-json    (SPDX format)\n"
                    "  syft <image> -o cyclonedx     (CycloneDX format)\n\n"
                    "SBOM + vulnerability scanning workflow:\n"
                    "  1. Build image\n"
                    "  2. Generate SBOM with Syft\n"
                    "  3. Scan SBOM with Grype (Anchore's vulnerability scanner)\n"
                    "  4. Attach SBOM to image with Cosign (cosign attach sbom)\n"
                    "  5. Sign image with Cosign\n\n"
                    "SBOMs are increasingly required by regulation (US Executive Order\n"
                    "14028) and enterprise procurement. They make vulnerability\n"
                    "tracking tractable across your entire container fleet."
                ),
                "xp": 25,
            },
        ],
    },

    # ── ZONE 4: CONTAINER ORCHESTRATION BEYOND K8S ───────────────────────
    "orchestration_beyond_k8s": {
        "id": "orchestration_beyond_k8s",
        "name": "The Dispatch Grid",
        "subtitle": "Nomad, ECS, Docker Swarm, and Podman",
        "color": "green",
        "icon": "🌐",
        "challenges": [
            {
                "id": "ob_1",
                "type": "quiz",
                "question": (
                    "HashiCorp Nomad can orchestrate not just containers but also\n"
                    "VMs, Java JARs, raw binaries, and batch jobs using a single\n"
                    "scheduler.\n\n"
                    "What are the pluggable components that let Nomad run different\n"
                    "workload types called?"
                ),
                "options": [
                    "Task drivers",
                    "Providers",
                    "Executors",
                    "Plugins",
                ],
                "answer": "a",
                "lesson": (
                    "Nomad uses task drivers to support different workload types.\n\n"
                    "Built-in task drivers:\n"
                    "  docker  — runs Docker containers\n"
                    "  exec    — runs raw binaries in isolated environments\n"
                    "  java    — runs Java JARs\n"
                    "  raw_exec — runs binaries without isolation (use carefully)\n"
                    "  qemu   — runs VMs\n\n"
                    "Community drivers: Podman, Firecracker, containerd, LXC, etc.\n\n"
                    "This flexibility is Nomad's key differentiator from Kubernetes.\n"
                    "A single Nomad cluster can schedule containers alongside legacy\n"
                    "Java applications and batch processing jobs — no need for\n"
                    "separate orchestration systems."
                ),
                "xp": 25,
            },
            {
                "id": "ob_2",
                "type": "text",
                "question": (
                    "In Nomad, the unit of work that defines one or more tasks that\n"
                    "should be co-located on the same machine is called a task group.\n\n"
                    "The top-level object that contains task groups and defines the\n"
                    "desired state of a deployment is called a ___.\n\n"
                    "Answer with one word."
                ),
                "options": [],
                "answer": "job",
                "lesson": (
                    "Nomad's hierarchy:\n\n"
                    "  Job\n"
                    "    -> Task Group (co-located tasks, like a K8s Pod)\n"
                    "      -> Task (single unit of work — a container, binary, etc.)\n\n"
                    "Job types:\n"
                    "  service  — long-running services (like a web server)\n"
                    "  batch    — short-lived jobs that run to completion\n"
                    "  system   — runs on every node (like a K8s DaemonSet)\n"
                    "  sysbatch — batch job that runs once on every node\n\n"
                    "Jobs are defined in HCL (HashiCorp Configuration Language) or JSON\n"
                    "and submitted with: nomad job run <file>.nomad\n\n"
                    "Nomad's scheduler places task groups onto client nodes based on\n"
                    "resource requirements, constraints, and affinities."
                ),
                "xp": 30,
            },
            {
                "id": "ob_3",
                "type": "quiz",
                "question": (
                    "AWS ECS (Elastic Container Service) has two launch types.\n"
                    "One runs your containers on EC2 instances you manage. The other\n"
                    "runs them serverlessly — AWS manages the compute.\n\n"
                    "What is the serverless launch type called?"
                ),
                "options": [
                    "Fargate",
                    "Lambda",
                    "App Runner",
                    "Lightsail",
                ],
                "answer": "a",
                "lesson": (
                    "ECS Fargate is the serverless launch type for ECS.\n\n"
                    "EC2 launch type:\n"
                    "  - You manage the EC2 instances (patching, scaling, capacity)\n"
                    "  - You pay for the EC2 instances whether or not tasks are running\n"
                    "  - More control, more operational burden\n\n"
                    "Fargate launch type:\n"
                    "  - AWS manages the compute (no EC2 instances to manage)\n"
                    "  - You pay per task (vCPU + memory per second)\n"
                    "  - No SSH access to the underlying host\n"
                    "  - Faster to set up, less control over the host environment\n\n"
                    "ECS concepts:\n"
                    "  Task Definition — like a Pod spec (image, CPU, memory, ports)\n"
                    "  Task — a running instance of a task definition\n"
                    "  Service — maintains desired count of tasks + load balancing\n"
                    "  Cluster — logical grouping of tasks and services"
                ),
                "xp": 25,
            },
            {
                "id": "ob_4",
                "type": "quiz",
                "question": (
                    "Docker Swarm mode is Docker's built-in orchestration. A Swarm\n"
                    "cluster has two types of nodes.\n\n"
                    "Which node type makes scheduling decisions and stores the\n"
                    "cluster state?"
                ),
                "options": [
                    "Manager nodes",
                    "Worker nodes",
                    "Master nodes",
                    "Control-plane nodes",
                ],
                "answer": "a",
                "lesson": (
                    "Docker Swarm has two node types:\n\n"
                    "  Manager nodes:\n"
                    "    - Store cluster state (Raft consensus)\n"
                    "    - Schedule services onto nodes\n"
                    "    - Serve the Swarm API\n"
                    "    - Can also run workloads (by default)\n"
                    "    - Recommended: 3 or 5 managers (odd number for quorum)\n\n"
                    "  Worker nodes:\n"
                    "    - Execute tasks assigned by managers\n"
                    "    - Report task state back to managers\n"
                    "    - Cannot make scheduling decisions\n\n"
                    "Initialize a swarm:  docker swarm init\n"
                    "Join as worker:      docker swarm join --token <worker-token>\n"
                    "Join as manager:     docker swarm join --token <manager-token>\n\n"
                    "Swarm is simpler than Kubernetes but less feature-rich.\n"
                    "Good for small teams that want orchestration without the K8s\n"
                    "operational complexity."
                ),
                "xp": 25,
            },
            {
                "id": "ob_5",
                "type": "quiz",
                "question": (
                    "Podman is a daemonless container engine that is CLI-compatible\n"
                    "with Docker. One of its key architectural differences is that\n"
                    "it does not require a daemon running as root.\n\n"
                    "What is this capability called?"
                ),
                "options": [
                    "Rootless containers",
                    "Unprivileged mode",
                    "User-space isolation",
                    "Sandboxed execution",
                ],
                "answer": "a",
                "lesson": (
                    "Podman runs containers without a root daemon.\n\n"
                    "Docker architecture:\n"
                    "  docker CLI -> dockerd (root daemon) -> containerd -> runc\n\n"
                    "Podman architecture:\n"
                    "  podman CLI -> conmon (per-container) -> runc/crun\n"
                    "  No central daemon. Each container has its own conmon process.\n\n"
                    "Rootless benefits:\n"
                    "  - No root daemon = smaller attack surface\n"
                    "  - Container compromise can't escalate to root on the host\n"
                    "  - Each user has their own container storage and namespace\n"
                    "  - Compliant with environments that prohibit root daemons\n\n"
                    "Podman also supports pods (groups of containers sharing\n"
                    "namespaces), directly compatible with Kubernetes pod concepts."
                ),
                "xp": 25,
            },
            {
                "id": "ob_6",
                "type": "text",
                "question": (
                    "In ECS, the specification that defines which container image to\n"
                    "run, how much CPU and memory to allocate, port mappings, and\n"
                    "environment variables is called a ___.\n\n"
                    "Answer with two words (e.g., task definition)."
                ),
                "options": [],
                "answer": "task definition",
                "lesson": (
                    "An ECS Task Definition is a JSON document that describes one or\n"
                    "more containers that form an application.\n\n"
                    "Key fields:\n"
                    "  family             — name of the task definition\n"
                    "  containerDefinitions — array of container specs:\n"
                    "    image            — container image URI\n"
                    "    cpu / memory     — resource limits\n"
                    "    portMappings     — host-to-container port mapping\n"
                    "    environment      — env vars\n"
                    "    secrets          — refs to SSM/Secrets Manager\n"
                    "    logConfiguration — logging driver (usually awslogs)\n"
                    "  taskRoleArn       — IAM role the task assumes\n"
                    "  executionRoleArn  — IAM role for pulling images and logging\n\n"
                    "Task definitions are versioned (family:revision). You create a\n"
                    "new revision for each change, and update the service to use it."
                ),
                "xp": 30,
            },
            {
                "id": "ob_7",
                "type": "quiz",
                "question": (
                    "In Docker Swarm, the unit of deployment that defines a desired\n"
                    "state (image, replicas, update policy, network, ports) is called\n"
                    "a ___.\n\n"
                    "What is it?"
                ),
                "options": [
                    "A service",
                    "A stack",
                    "A task",
                    "A deployment",
                ],
                "answer": "a",
                "lesson": (
                    "Docker Swarm services define the desired state of your workload.\n\n"
                    "Create a service:\n"
                    "  docker service create --name web --replicas 3 -p 80:80 nginx\n\n"
                    "Key properties:\n"
                    "  --replicas N       — desired number of running tasks\n"
                    "  --update-delay 10s — delay between updating each task\n"
                    "  --rollback-config  — automatic rollback on failure\n"
                    "  --constraint       — placement constraints (e.g., node.role==worker)\n\n"
                    "Swarm hierarchy:\n"
                    "  Service — desired state declaration\n"
                    "    -> Task — atomic scheduling unit (one container instance)\n"
                    "      -> Container — the running process\n\n"
                    "Stacks (docker stack deploy) are groups of related services\n"
                    "defined in a compose file and deployed as a unit."
                ),
                "xp": 25,
            },
            {
                "id": "ob_8",
                "type": "quiz",
                "question": (
                    "You want to replace Docker with Podman but your team has muscle\n"
                    "memory for 'docker' commands. Podman supports this directly.\n\n"
                    "What makes the migration trivial for CLI users?"
                ),
                "options": [
                    "Podman is CLI-compatible; 'alias docker=podman' works for most commands",
                    "Podman includes a built-in Docker daemon emulator",
                    "Podman automatically converts Dockerfiles to Podman format",
                    "Podman uses the same binary name as Docker",
                ],
                "answer": "a",
                "lesson": (
                    "Podman is a drop-in CLI replacement for Docker.\n\n"
                    "These commands work identically:\n"
                    "  podman pull nginx          (docker pull nginx)\n"
                    "  podman run -d nginx        (docker run -d nginx)\n"
                    "  podman build -t app .      (docker build -t app .)\n"
                    "  podman ps                  (docker ps)\n"
                    "  podman images              (docker images)\n\n"
                    "Migration path:\n"
                    "  alias docker=podman  (in .bashrc/.zshrc)\n\n"
                    "Key differences to be aware of:\n"
                    "  - No daemon (each container is a child of your shell)\n"
                    "  - Rootless by default\n"
                    "  - Pods are a first-class concept\n"
                    "  - podman generate kube -> generates K8s YAML from containers\n"
                    "  - podman play kube -> runs K8s YAML locally\n\n"
                    "Docker Compose support: podman-compose or podman with the\n"
                    "docker-compose compatible socket."
                ),
                "xp": 25,
            },
        ],
    },

    # ── ZONE 5: CONTAINER SECURITY ───────────────────────────────────────
    "container_security": {
        "id": "container_security",
        "name": "The Hardened Perimeter",
        "subtitle": "Rootless, Seccomp, AppArmor, Image Scanning, Supply Chain",
        "color": "red",
        "icon": "🛡️",
        "challenges": [
            {
                "id": "cs_1",
                "type": "quiz",
                "question": (
                    "By default, Docker containers run processes as root (UID 0)\n"
                    "inside the container. If the container runtime has a vulnerability,\n"
                    "this root user could become root on the host.\n\n"
                    "What Dockerfile instruction should you use to run as a non-root user?"
                ),
                "options": [
                    "USER",
                    "RUN useradd",
                    "RUNAS",
                    "SETUID",
                ],
                "answer": "a",
                "lesson": (
                    "The USER instruction sets the user (and optionally group) for\n"
                    "all subsequent RUN, CMD, and ENTRYPOINT instructions.\n\n"
                    "Pattern:\n"
                    "  RUN addgroup --system app && adduser --system --ingroup app app\n"
                    "  USER app\n"
                    "  COPY --chown=app:app . /app\n"
                    "  CMD [\"./server\"]\n\n"
                    "Why it matters:\n"
                    "  - Root in container = root on host (without user namespace remapping)\n"
                    "  - Container escape + root = full host compromise\n"
                    "  - Non-root limits blast radius even if escape occurs\n\n"
                    "Note: RUN useradd creates the user. USER sets which user runs\n"
                    "the process. You need both — useradd creates it, USER activates it."
                ),
                "xp": 25,
            },
            {
                "id": "cs_2",
                "type": "quiz",
                "question": (
                    "Linux seccomp (secure computing mode) filters can restrict which\n"
                    "system calls a container process is allowed to make.\n\n"
                    "Docker applies a default seccomp profile that blocks ~44 syscalls.\n"
                    "Which of these dangerous syscalls is blocked by default?"
                ),
                "options": [
                    "reboot (reboot the host machine)",
                    "read (read from file descriptors)",
                    "write (write to file descriptors)",
                    "open (open files)",
                ],
                "answer": "a",
                "lesson": (
                    "Docker's default seccomp profile blocks syscalls that are\n"
                    "dangerous from inside a container.\n\n"
                    "Blocked syscalls include:\n"
                    "  reboot      — reboot the host\n"
                    "  mount/umount — modify the filesystem hierarchy\n"
                    "  kexec_load  — load a new kernel\n"
                    "  swapon/off  — modify swap\n"
                    "  clock_settime — change system clock\n"
                    "  bpf         — load BPF programs into the kernel\n\n"
                    "Custom profiles:\n"
                    "  docker run --security-opt seccomp=custom.json <image>\n\n"
                    "Disable seccomp (dangerous!):\n"
                    "  docker run --security-opt seccomp=unconfined <image>\n\n"
                    "In Kubernetes, seccomp profiles are set via the pod security\n"
                    "context or PodSecurityStandards (Baseline/Restricted)."
                ),
                "xp": 25,
            },
            {
                "id": "cs_3",
                "type": "quiz",
                "question": (
                    "AppArmor is a Linux kernel security module that confines programs\n"
                    "based on a profile defining allowed file access, network access,\n"
                    "and capabilities.\n\n"
                    "Docker applies a default AppArmor profile. What does it primarily\n"
                    "restrict?"
                ),
                "options": [
                    "Write access to /proc, /sys, and mount operations inside the container",
                    "All network traffic in and out of the container",
                    "CPU and memory usage of the container",
                    "Access to environment variables",
                ],
                "answer": "a",
                "lesson": (
                    "Docker's default AppArmor profile (docker-default) restricts:\n\n"
                    "  - Writing to /proc (process information pseudo-filesystem)\n"
                    "  - Writing to /sys (kernel and device configuration)\n"
                    "  - Mount operations inside the container\n"
                    "  - Access to sensitive /proc entries (/proc/sysrq-trigger, etc.)\n\n"
                    "AppArmor vs seccomp:\n"
                    "  seccomp   — filters WHICH syscalls can be made\n"
                    "  AppArmor  — filters WHAT RESOURCES a process can access\n"
                    "  Both work together. They are complementary, not alternatives.\n\n"
                    "Custom AppArmor profile:\n"
                    "  docker run --security-opt apparmor=my-custom-profile <image>\n\n"
                    "Disable (dangerous!):\n"
                    "  docker run --security-opt apparmor=unconfined <image>\n\n"
                    "Note: AppArmor is Debian/Ubuntu-based. RHEL/CentOS use SELinux."
                ),
                "xp": 25,
            },
            {
                "id": "cs_4",
                "type": "text",
                "question": (
                    "You want to run Docker containers where the root user inside the\n"
                    "container maps to an unprivileged user on the host. This way,\n"
                    "even a container escape as 'root' results in a non-root user on\n"
                    "the host.\n\n"
                    "What is the Docker daemon feature that enables this UID/GID\n"
                    "remapping? (two words, with a hyphen)"
                ),
                "options": [],
                "answer": "user-namespace",
                "lesson": (
                    "User namespace remapping (userns-remap) maps UIDs/GIDs inside\n"
                    "the container to unprivileged UIDs/GIDs on the host.\n\n"
                    "Configuration:\n"
                    "  /etc/docker/daemon.json:\n"
                    "  { \"userns-remap\": \"default\" }\n\n"
                    "How it works:\n"
                    "  Container UID 0 (root) -> Host UID 100000 (unprivileged)\n"
                    "  Container UID 1        -> Host UID 100001\n"
                    "  ... and so on\n\n"
                    "Implications:\n"
                    "  - Container 'root' has NO privileges on the host\n"
                    "  - File permissions on bind mounts may need adjustment\n"
                    "  - Some workloads may break if they genuinely need root\n\n"
                    "This is different from the USER instruction in Dockerfiles.\n"
                    "USER runs as non-root INSIDE the container. userns-remap makes\n"
                    "even container root unprivileged on the HOST."
                ),
                "xp": 30,
            },
            {
                "id": "cs_5",
                "type": "quiz",
                "question": (
                    "In container supply chain security, you want to ensure that\n"
                    "the image your CI/CD pipeline built is the same image that gets\n"
                    "deployed to production — with cryptographic proof.\n\n"
                    "Which practice addresses this?"
                ),
                "options": [
                    "Sign images in CI and verify signatures at deployment with admission control",
                    "Use the 'latest' tag so you always get the most recent build",
                    "Store images in a private registry behind a VPN",
                    "Run vulnerability scans before every deployment",
                ],
                "answer": "a",
                "lesson": (
                    "Container supply chain security requires cryptographic guarantees\n"
                    "that what you built is what you deploy.\n\n"
                    "The supply chain attack vector:\n"
                    "  1. Attacker gains registry write access\n"
                    "  2. Pushes malicious image under an existing tag\n"
                    "  3. Next deployment pulls the compromised image\n\n"
                    "Defense in depth:\n"
                    "  1. Sign images (Cosign/Notary) in CI after build\n"
                    "  2. Record build provenance (SLSA framework)\n"
                    "  3. Verify signatures at deploy time (admission controllers)\n"
                    "     - Kyverno: ClusterPolicy with verifyImages\n"
                    "     - OPA Gatekeeper: custom ConstraintTemplate\n"
                    "     - Connaisseur: standalone admission controller\n"
                    "  4. Pin images by digest, not tag\n"
                    "  5. Generate and verify SBOMs\n\n"
                    "Private registries and VPNs add access control but do NOT\n"
                    "provide tamper detection."
                ),
                "xp": 25,
            },
            {
                "id": "cs_6",
                "type": "quiz",
                "question": (
                    "Docker's --privileged flag gives a container almost all the\n"
                    "capabilities of the host. Instead of --privileged, you should\n"
                    "grant only the specific Linux capabilities your container needs.\n\n"
                    "Which flag adds a single specific capability?"
                ),
                "options": [
                    "--cap-add",
                    "--security-opt",
                    "--privilege-add",
                    "--allow-cap",
                ],
                "answer": "a",
                "lesson": (
                    "Linux capabilities split root privileges into distinct units.\n"
                    "Instead of all-or-nothing root, you can grant specific permissions.\n\n"
                    "Common capabilities:\n"
                    "  NET_BIND_SERVICE — bind to ports below 1024\n"
                    "  NET_RAW          — use raw sockets (for ping)\n"
                    "  SYS_TIME         — set system clock\n"
                    "  SYS_PTRACE       — trace/debug other processes\n"
                    "  SYS_ADMIN        — broad admin ops (avoid if possible)\n\n"
                    "Docker flags:\n"
                    "  --cap-add NET_RAW     — add a capability\n"
                    "  --cap-drop ALL        — drop all capabilities\n"
                    "  --cap-add NET_BIND_SERVICE --cap-drop ALL  — minimal set\n\n"
                    "Best practice: drop ALL, then add back only what you need.\n"
                    "  docker run --cap-drop ALL --cap-add NET_BIND_SERVICE <image>\n\n"
                    "--privileged grants ALL capabilities plus host device access.\n"
                    "Never use --privileged in production."
                ),
                "xp": 25,
            },
            {
                "id": "cs_7",
                "type": "text",
                "question": (
                    "You want to make the container's root filesystem read-only so\n"
                    "that even if an attacker gets code execution, they cannot write\n"
                    "to the filesystem (except for explicitly mounted volumes).\n\n"
                    "What docker run flag enables a read-only root filesystem?\n\n"
                    "Answer with the full flag (including --)."
                ),
                "options": [],
                "answer": "--read-only",
                "lesson": (
                    "--read-only mounts the container's root filesystem as read-only.\n\n"
                    "Usage:\n"
                    "  docker run --read-only <image>\n\n"
                    "Applications that need to write temp files:\n"
                    "  docker run --read-only --tmpfs /tmp --tmpfs /run <image>\n\n"
                    "Benefits:\n"
                    "  - Attackers cannot drop binaries, scripts, or tools\n"
                    "  - No modifications to application files\n"
                    "  - Forces explicit declaration of writable paths\n"
                    "  - Complements non-root USER and dropped capabilities\n\n"
                    "In Kubernetes:\n"
                    "  securityContext:\n"
                    "    readOnlyRootFilesystem: true\n\n"
                    "Combine with emptyDir volumes for paths that need writes.\n"
                    "This is a simple, high-impact security hardening step."
                ),
                "xp": 30,
            },
            {
                "id": "cs_8",
                "type": "quiz",
                "question": (
                    "The SLSA (Supply-chain Levels for Software Artifacts) framework\n"
                    "defines levels of supply chain integrity. At the highest level\n"
                    "(SLSA Build L3), which guarantee is provided?"
                ),
                "options": [
                    "The build ran on a hardened, isolated platform with tamper-proof provenance",
                    "The source code was reviewed by at least two developers",
                    "All dependencies were scanned for vulnerabilities",
                    "The artifact was deployed to production with zero downtime",
                ],
                "answer": "a",
                "lesson": (
                    "SLSA (pronounced 'salsa') is a framework for supply chain\n"
                    "integrity, created by Google and adopted by the OpenSSF.\n\n"
                    "Build levels:\n"
                    "  L0 — No guarantees\n"
                    "  L1 — Build process is documented and produces provenance\n"
                    "  L2 — Build runs on a hosted service with signed provenance\n"
                    "  L3 — Build runs on a hardened, isolated platform;\n"
                    "        provenance is tamper-proof and non-falsifiable\n\n"
                    "Provenance is a signed attestation that says:\n"
                    "  'This artifact was built from THIS source, by THIS builder,\n"
                    "   using THIS process, at THIS time.'\n\n"
                    "Tools:\n"
                    "  - slsa-verifier: verify SLSA provenance\n"
                    "  - GitHub Actions: SLSA3 builder (reusable workflow)\n"
                    "  - Cosign + in-toto: attach and verify attestations\n\n"
                    "SLSA doesn't replace vulnerability scanning — it ensures the\n"
                    "artifact you're scanning is the one that was actually built."
                ),
                "xp": 25,
            },
        ],
    },
}
