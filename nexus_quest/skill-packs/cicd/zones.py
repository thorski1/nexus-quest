"""
zones.py — CI/CD skill pack zones for NEXUS.
7 zones, ~40 challenges. The pipeline never sleeps.
"""

from engine.zone import Zone
from engine.challenge import Challenge

ZONE_ORDER = [
    "cicd_fundamentals",
    "github_actions",
    "testing_in_pipelines",
    "build_and_artifacts",
    "deployment_strategies",
    "infrastructure_as_code_cicd",
    "monitoring_and_observability",
]

# ---------------------------------------------------------------------------
# ZONE 1 — CI/CD Fundamentals
# ---------------------------------------------------------------------------
ZONES = {
    "cicd_fundamentals": Zone(
        id="cicd_fundamentals",
        title="CI/CD Fundamentals",
        description="What CI/CD is, continuous integration vs delivery vs deployment, and the anatomy of a pipeline.",
        challenges=[
            Challenge(
                id="cicd_fund_1",
                type="quiz",
                prompt="What does 'CI' stand for in CI/CD?",
                options=[
                    "Container Integration",
                    "Continuous Integration",
                    "Code Inspection",
                    "Cluster Initialization",
                ],
                answer="b",
                explanation=(
                    "Continuous Integration (CI) is the practice of frequently merging code changes "
                    "into a shared repository, where automated builds and tests verify each integration. "
                    "The goal: detect integration errors as early as possible, ideally on every commit."
                ),
                hints=["It's about integrating code changes frequently", "The 'C' stands for Continuous"],
                xp=25,
            ),
            Challenge(
                id="cicd_fund_2",
                type="quiz",
                prompt="What is the key difference between Continuous Delivery and Continuous Deployment?",
                options=[
                    "Continuous Delivery uses Docker; Continuous Deployment does not",
                    "Continuous Delivery requires a manual approval gate before production; Continuous Deployment is fully automated",
                    "Continuous Deployment only applies to microservices",
                    "There is no difference — they are synonyms",
                ],
                answer="b",
                explanation=(
                    "Continuous Delivery means every change is automatically built, tested, and staged "
                    "for release — but a human must approve the final push to production. "
                    "Continuous Deployment removes that gate: every change that passes the pipeline "
                    "goes to production automatically. The difference is one button click."
                ),
                hints=["Think about who presses the final 'deploy' button", "One has a human gate; the other doesn't"],
                xp=30,
            ),
            Challenge(
                id="cicd_fund_3",
                type="quiz",
                prompt="In a typical CI/CD pipeline, which stage runs FIRST?",
                options=[
                    "Deploy to production",
                    "Source — code is committed and pushed",
                    "Run end-to-end tests",
                    "Build Docker images",
                ],
                answer="b",
                explanation=(
                    "Every pipeline begins with the Source stage — a code change triggers the pipeline. "
                    "This is typically a push to a branch, a pull request, or a tag creation. "
                    "The standard order: Source -> Build -> Test -> Deploy."
                ),
                hints=["What triggers the pipeline in the first place?", "Code has to exist before it can be built"],
                xp=25,
            ),
            Challenge(
                id="cicd_fund_4",
                type="quiz",
                prompt="What is the primary benefit of running CI on every commit?",
                options=[
                    "It makes deployments faster by skipping tests",
                    "It catches integration errors early, when they are cheapest to fix",
                    "It eliminates the need for code review",
                    "It automatically writes unit tests for new code",
                ],
                answer="b",
                explanation=(
                    "The core value of CI: rapid feedback. When developers integrate frequently "
                    "and every integration is verified by automated build and test, bugs are caught "
                    "within minutes of introduction — not days or weeks later when the context is lost."
                ),
                hints=["Think about when bugs are cheapest to fix", "The word 'early' is key"],
                xp=25,
            ),
            Challenge(
                id="cicd_fund_5",
                type="quiz",
                prompt="A pipeline has stages: Build, Test, Deploy. The Test stage fails. What should happen?",
                options=[
                    "The Deploy stage runs anyway with a warning",
                    "The pipeline stops — Deploy is never reached",
                    "The Build stage re-runs automatically",
                    "The failure is logged but deployment continues",
                ],
                answer="b",
                explanation=(
                    "Pipeline stages are gates. If a stage fails, subsequent stages do not execute. "
                    "This is the fundamental safety mechanism of CI/CD: broken code never reaches production "
                    "because the pipeline halts at the first failure. This is called 'fail-fast' behavior."
                ),
                hints=["Stages act as quality gates", "Would you deploy code that failed its tests?"],
                xp=25,
            ),
            Challenge(
                id="cicd_fund_6",
                type="quiz",
                prompt="What is a 'pipeline artifact'?",
                options=[
                    "A YAML file that defines the pipeline",
                    "A build output (binary, image, bundle) that is stored and passed between stages",
                    "A failed test report",
                    "A git branch created by the pipeline",
                ],
                answer="b",
                explanation=(
                    "An artifact is any file or package produced by a pipeline stage and consumed by "
                    "a later stage or stored for deployment. Examples: compiled binaries, Docker images, "
                    "test reports, static site bundles. Artifacts are the tangible output of the pipeline."
                ),
                hints=["Think about what the build stage produces", "It's something you can store and deploy later"],
                xp=25,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 2 — GitHub Actions
    # ---------------------------------------------------------------------------
    "github_actions": Zone(
        id="github_actions",
        title="GitHub Actions",
        description="Workflows, triggers, jobs, steps, the Actions marketplace, secrets, and matrix builds.",
        challenges=[
            Challenge(
                id="gha_1",
                type="quiz",
                prompt="Where must GitHub Actions workflow files be stored in a repository?",
                options=[
                    ".github/actions/",
                    ".github/workflows/",
                    ".ci/workflows/",
                    "workflows/ at the repository root",
                ],
                answer="b",
                explanation=(
                    "GitHub Actions workflow files must live in `.github/workflows/` and be YAML files. "
                    "GitHub automatically detects and runs workflows from this directory. "
                    "Any `.yml` or `.yaml` file in that path is treated as a workflow definition."
                ),
                hints=["It's inside the .github directory", "The folder name matches what it contains"],
                xp=25,
            ),
            Challenge(
                id="gha_2",
                type="quiz",
                prompt="Which trigger causes a workflow to run when code is pushed to the `main` branch?",
                options=[
                    "on: commit: branches: [main]",
                    "on: push: branches: [main]",
                    "on: merge: target: main",
                    "on: deploy: branch: main",
                ],
                answer="b",
                explanation=(
                    "The `on: push` trigger fires when commits are pushed to a repository. "
                    "Adding `branches: [main]` filters it to only fire on pushes to the main branch. "
                    "Other common triggers: `pull_request`, `schedule`, `workflow_dispatch`, `repository_dispatch`."
                ),
                hints=["The event name matches the git operation", "Push code, trigger on push"],
                xp=25,
            ),
            Challenge(
                id="gha_3",
                type="quiz",
                prompt="In a GitHub Actions workflow, what is the relationship between jobs and steps?",
                options=[
                    "Steps contain jobs — each step can run multiple jobs",
                    "Jobs and steps are the same thing",
                    "Jobs contain steps — each job is a sequence of steps that run on the same runner",
                    "Jobs run sequentially; steps run in parallel",
                ],
                answer="c",
                explanation=(
                    "A workflow contains one or more jobs. Each job runs on a runner (a VM or container) "
                    "and contains a sequence of steps. Steps within a job share the same filesystem and "
                    "run sequentially. Jobs, by default, run in parallel unless dependencies are declared."
                ),
                hints=["Think of it as a hierarchy: workflow > jobs > steps", "Steps share a runner within a job"],
                xp=30,
            ),
            Challenge(
                id="gha_4",
                type="quiz",
                prompt="How are sensitive values like API keys stored and accessed in GitHub Actions?",
                options=[
                    "Hardcoded in the workflow YAML file",
                    "Stored as GitHub Secrets and accessed via `${{ secrets.NAME }}`",
                    "Passed as command-line arguments to the runner",
                    "Stored in a .env file committed to the repository",
                ],
                answer="b",
                explanation=(
                    "GitHub Secrets are encrypted values stored at the repository, environment, or organization level. "
                    "They are accessed in workflows using the `${{ secrets.SECRET_NAME }}` expression. "
                    "Secrets are masked in logs and never exposed in workflow output. "
                    "Never hardcode secrets in YAML or commit them to the repository."
                ),
                hints=["GitHub has a built-in secrets management feature", "The syntax uses double curly braces"],
                xp=30,
            ),
            Challenge(
                id="gha_5",
                type="quiz",
                prompt="What does a matrix strategy in GitHub Actions do?",
                options=[
                    "Runs the same job multiple times with different parameter combinations",
                    "Creates a visual dashboard of pipeline results",
                    "Encrypts workflow outputs using a key matrix",
                    "Defines the order in which jobs must execute",
                ],
                answer="a",
                explanation=(
                    "A matrix strategy generates multiple job runs from variable combinations. "
                    "Example: `matrix: { os: [ubuntu, windows], node: [16, 18] }` creates 4 jobs — "
                    "one for each combination. This is how you test across multiple OS versions, "
                    "language versions, or configurations in a single workflow."
                ),
                hints=["Think of a grid of test configurations", "It multiplies job runs across variable combos"],
                xp=35,
            ),
            Challenge(
                id="gha_6",
                type="quiz",
                prompt="What is a reusable workflow in GitHub Actions?",
                options=[
                    "A workflow that retries failed steps automatically",
                    "A workflow defined in one repository that can be called from workflows in other repositories",
                    "A workflow that only runs on reusable runners",
                    "A workflow template stored in the GitHub marketplace",
                ],
                answer="b",
                explanation=(
                    "Reusable workflows are called with `uses: org/repo/.github/workflows/file.yml@ref`. "
                    "They accept inputs and secrets, run as a separate job, and return outputs. "
                    "This allows organizations to standardize pipeline logic across many repositories "
                    "without duplicating YAML."
                ),
                hints=["The key word is 'reusable' — used across repos", "Called with the `uses` keyword pointing to another repo"],
                xp=35,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 3 — Testing in Pipelines
    # ---------------------------------------------------------------------------
    "testing_in_pipelines": Zone(
        id="testing_in_pipelines",
        title="Testing in Pipelines",
        description="Unit, integration, and e2e tests. Test stages, code coverage, and fail-fast strategies.",
        challenges=[
            Challenge(
                id="test_1",
                type="quiz",
                prompt="Which type of test verifies that a single function or method works correctly in isolation?",
                options=[
                    "End-to-end test",
                    "Integration test",
                    "Unit test",
                    "Smoke test",
                ],
                answer="c",
                explanation=(
                    "Unit tests verify individual functions, methods, or classes in isolation. "
                    "They are fast (milliseconds each), have no external dependencies (databases, APIs), "
                    "and form the base of the testing pyramid. A CI pipeline typically runs hundreds "
                    "or thousands of unit tests in seconds."
                ),
                hints=["The smallest 'unit' of code", "Tests one thing in isolation, no external dependencies"],
                xp=25,
            ),
            Challenge(
                id="test_2",
                type="quiz",
                prompt="What does an integration test verify that a unit test does not?",
                options=[
                    "That the code compiles without errors",
                    "That multiple components work together correctly (e.g., app + database)",
                    "That the UI renders correctly in a browser",
                    "That the code follows style guidelines",
                ],
                answer="b",
                explanation=(
                    "Integration tests verify that multiple components interact correctly — "
                    "your application code talking to a real database, an API calling another API, "
                    "a message producer and consumer working together. They are slower than unit tests "
                    "because they require real infrastructure (or close approximations like testcontainers)."
                ),
                hints=["The clue is in the name: integration", "What happens when components talk to each other?"],
                xp=25,
            ),
            Challenge(
                id="test_3",
                type="quiz",
                prompt="In the testing pyramid, which layer has the MOST tests?",
                options=[
                    "End-to-end tests (top)",
                    "Integration tests (middle)",
                    "Unit tests (bottom)",
                    "Manual tests (outside the pyramid)",
                ],
                answer="c",
                explanation=(
                    "The testing pyramid: many unit tests at the base, fewer integration tests in the middle, "
                    "and very few e2e tests at the top. Unit tests are fast and cheap; e2e tests are slow "
                    "and brittle. A healthy ratio might be 70% unit, 20% integration, 10% e2e."
                ),
                hints=["The pyramid is widest at the bottom", "Which tests are fastest and cheapest to write?"],
                xp=25,
            ),
            Challenge(
                id="test_4",
                type="quiz",
                prompt="A pipeline has 'fail-fast' enabled on a matrix of 6 test jobs. Job 2 fails. What happens?",
                options=[
                    "Only Job 2 stops; the other 5 continue",
                    "All 6 jobs are cancelled immediately",
                    "The remaining jobs continue but the pipeline is marked as failed",
                    "Job 2 retries 3 times before the pipeline fails",
                ],
                answer="b",
                explanation=(
                    "Fail-fast (default in GitHub Actions matrix strategies) cancels all remaining matrix jobs "
                    "as soon as any one job fails. This saves runner minutes and provides faster feedback. "
                    "To disable it: `strategy: { fail-fast: false }` — useful when you want results from "
                    "all matrix combinations regardless of individual failures."
                ),
                hints=["'Fail-fast' means stop everything at the first failure", "It cancels the siblings, not just the one that failed"],
                xp=30,
            ),
            Challenge(
                id="test_5",
                type="quiz",
                prompt="What does 'code coverage' measure?",
                options=[
                    "How many developers contributed to the codebase",
                    "The percentage of code lines/branches executed during test runs",
                    "How many tests pass vs. fail",
                    "The number of code reviews completed per sprint",
                ],
                answer="b",
                explanation=(
                    "Code coverage measures the percentage of your source code that is exercised by your test suite. "
                    "Common metrics: line coverage (lines executed), branch coverage (if/else paths taken), "
                    "and function coverage (functions called). 80% line coverage is a common threshold — "
                    "but coverage measures quantity, not quality. 100% coverage does not mean 0 bugs."
                ),
                hints=["It's about how much code the tests actually run", "Measured as a percentage of lines or branches"],
                xp=30,
            ),
            Challenge(
                id="test_6",
                type="quiz",
                prompt="A coverage gate requires 80% line coverage. A PR drops coverage from 82% to 79%. What should happen?",
                options=[
                    "The pipeline passes — 79% is close enough",
                    "The pipeline fails — the coverage gate blocks the merge",
                    "The pipeline warns but allows the merge",
                    "The pipeline automatically generates tests to restore coverage",
                ],
                answer="b",
                explanation=(
                    "Coverage gates are hard thresholds. If the pipeline is configured to require 80% coverage, "
                    "any PR that drops below that threshold fails the check and blocks the merge. "
                    "This prevents coverage erosion over time and forces developers to write tests "
                    "for new code. The gate is only as strong as the team's willingness to enforce it."
                ),
                hints=["Gates are pass/fail — there is no 'close enough'", "79% < 80% threshold"],
                xp=30,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 4 — Build and Artifacts
    # ---------------------------------------------------------------------------
    "build_and_artifacts": Zone(
        id="build_and_artifacts",
        title="Build and Artifacts",
        description="Build steps, Docker image builds, artifact storage, caching, and multi-stage builds.",
        challenges=[
            Challenge(
                id="build_1",
                type="quiz",
                prompt="In a CI pipeline, what is the primary purpose of the 'build' stage?",
                options=[
                    "To run all automated tests",
                    "To compile source code and produce deployable artifacts",
                    "To deploy code to staging",
                    "To scan code for security vulnerabilities",
                ],
                answer="b",
                explanation=(
                    "The build stage transforms source code into deployable artifacts — "
                    "compiled binaries, Docker images, bundled JavaScript, packaged libraries. "
                    "It verifies that the code compiles/transpiles successfully and produces "
                    "the output that downstream stages (test, deploy) will consume."
                ),
                hints=["What does 'build' mean in software?", "It produces something you can deploy"],
                xp=25,
            ),
            Challenge(
                id="build_2",
                type="quiz",
                prompt="Why is Docker layer caching important in CI pipelines?",
                options=[
                    "It encrypts Docker images for secure storage",
                    "It reuses unchanged layers from previous builds, dramatically reducing build time",
                    "It allows multiple containers to share the same network",
                    "It compresses images for faster download",
                ],
                answer="b",
                explanation=(
                    "Docker images are built in layers. Each instruction in a Dockerfile creates a layer. "
                    "If a layer hasn't changed since the last build, Docker reuses the cached version "
                    "instead of rebuilding it. In CI, this can reduce build times from 10 minutes to 30 seconds. "
                    "Order matters: put rarely-changing layers (OS, dependencies) before frequently-changing ones (source code)."
                ),
                hints=["Think about what 'cache' means — reusing previous work", "Unchanged layers don't need to be rebuilt"],
                xp=30,
            ),
            Challenge(
                id="build_3",
                type="quiz",
                prompt="What is a multi-stage Docker build?",
                options=[
                    "A build that runs on multiple CI runners simultaneously",
                    "A Dockerfile with multiple FROM instructions that separates build-time dependencies from the runtime image",
                    "A build that deploys to multiple environments",
                    "A build that creates images for multiple CPU architectures",
                ],
                answer="b",
                explanation=(
                    "Multi-stage builds use multiple FROM instructions in a single Dockerfile. "
                    "The first stage installs build tools and compiles code. The final stage copies "
                    "only the compiled output into a minimal base image. Result: production images "
                    "that are 10-100x smaller because they don't contain compilers, dev dependencies, or source code."
                ),
                hints=["Multiple FROM statements in one Dockerfile", "Separate what you need to BUILD from what you need to RUN"],
                xp=35,
            ),
            Challenge(
                id="build_4",
                type="quiz",
                prompt="Where should CI pipeline artifacts (Docker images, packages) be stored?",
                options=[
                    "In the git repository alongside the source code",
                    "In an artifact registry (e.g., Docker Hub, GitHub Packages, ECR, Artifactory)",
                    "On the CI runner's local filesystem",
                    "In a shared NFS mount accessible to all developers",
                ],
                answer="b",
                explanation=(
                    "Artifacts belong in dedicated registries — Docker images in a container registry "
                    "(ECR, GCR, Docker Hub), packages in a package registry (npm, PyPI, Maven Central), "
                    "binaries in an artifact store (Artifactory, GitHub Packages). Registries provide "
                    "versioning, access control, and distribution. Never store build artifacts in git."
                ),
                hints=["Git stores source code, not binaries", "There are dedicated systems for storing built outputs"],
                xp=25,
            ),
            Challenge(
                id="build_5",
                type="quiz",
                prompt="A CI build takes 12 minutes. Dependency installation accounts for 9 minutes. What should you do?",
                options=[
                    "Skip dependency installation and hope the runner has them cached",
                    "Cache dependencies between pipeline runs using a cache key based on the lockfile hash",
                    "Install fewer dependencies",
                    "Run the build on a faster runner and accept the cost",
                ],
                answer="b",
                explanation=(
                    "Dependency caching is a standard CI optimization. The cache key is typically based on "
                    "the hash of the lockfile (package-lock.json, poetry.lock, go.sum). When the lockfile "
                    "hasn't changed, the cached dependencies are restored instead of re-downloaded. "
                    "In GitHub Actions: `actions/cache` or the built-in cache in `actions/setup-node`."
                ),
                hints=["If dependencies haven't changed, why download them again?", "The lockfile hash makes a good cache key"],
                xp=30,
            ),
            Challenge(
                id="build_6",
                type="quiz",
                prompt="What is image tagging in the context of a CI/CD pipeline?",
                options=[
                    "Adding metadata labels to Docker images for versioning and identification",
                    "Marking images as 'do not deploy'",
                    "Compressing images to reduce storage costs",
                    "Scanning images for vulnerabilities",
                ],
                answer="a",
                explanation=(
                    "Image tags identify specific versions of a Docker image — `myapp:v1.2.3`, "
                    "`myapp:latest`, `myapp:abc123` (commit SHA). Tags are how the deploy stage knows "
                    "which exact image to run. Best practice: tag with the git SHA for traceability, "
                    "use semantic version tags for releases, and avoid relying solely on `latest`."
                ),
                hints=["Tags are version labels for images", "Think: how does the deploy stage know WHICH image to pull?"],
                xp=30,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 5 — Deployment Strategies
    # ---------------------------------------------------------------------------
    "deployment_strategies": Zone(
        id="deployment_strategies",
        title="Deployment Strategies",
        description="Blue-green, canary, rolling updates, feature flags, and rollback procedures.",
        challenges=[
            Challenge(
                id="deploy_1",
                type="quiz",
                prompt="In a blue-green deployment, what are the 'blue' and 'green' environments?",
                options=[
                    "Development and staging environments",
                    "Two identical production environments — one active, one idle with the new version",
                    "Primary and disaster recovery data centers",
                    "Frontend and backend server groups",
                ],
                answer="b",
                explanation=(
                    "Blue-green deployment maintains two identical production environments. "
                    "Blue runs the current version; Green is deployed with the new version. "
                    "Once Green is verified, traffic is switched from Blue to Green instantly. "
                    "Rollback is instant: switch traffic back to Blue. The cost: double the infrastructure."
                ),
                hints=["Two identical environments, only one serves traffic at a time", "Switching between them is instant"],
                xp=30,
            ),
            Challenge(
                id="deploy_2",
                type="quiz",
                prompt="What is a canary deployment?",
                options=[
                    "Deploying to a single test server before full rollout",
                    "Routing a small percentage of production traffic to the new version while monitoring for errors",
                    "Deploying only during off-peak hours",
                    "Running the new version in a sandbox without real traffic",
                ],
                answer="b",
                explanation=(
                    "Canary deployment routes a small percentage (e.g., 5%) of real production traffic "
                    "to the new version. If error rates, latency, or other metrics stay healthy, "
                    "traffic is gradually shifted (10%, 25%, 50%, 100%). If metrics degrade, "
                    "traffic is shifted back to the old version. Named after canaries in coal mines."
                ),
                hints=["Named after the coal mine safety practice", "Small percentage of real traffic goes to the new version first"],
                xp=30,
            ),
            Challenge(
                id="deploy_3",
                type="quiz",
                prompt="How does a rolling update deploy new code?",
                options=[
                    "All instances are replaced simultaneously",
                    "Instances are replaced one at a time (or in small batches) while the service stays available",
                    "A completely new cluster is created and traffic is migrated",
                    "The old version is stopped, then the new version is started",
                ],
                answer="b",
                explanation=(
                    "Rolling updates replace instances incrementally — one or a few at a time. "
                    "At any point during the rollout, both old and new versions are running. "
                    "The service never goes down. Kubernetes Deployments use rolling updates by default: "
                    "`maxSurge` and `maxUnavailable` control the pace."
                ),
                hints=["Gradual replacement, not all at once", "Some old and some new instances run simultaneously"],
                xp=25,
            ),
            Challenge(
                id="deploy_4",
                type="quiz",
                prompt="What is a feature flag?",
                options=[
                    "A git branch naming convention for feature work",
                    "A runtime toggle that enables or disables a feature without deploying new code",
                    "A CI pipeline stage that validates feature completeness",
                    "A deployment tag that marks which features are included in a release",
                ],
                answer="b",
                explanation=(
                    "Feature flags (feature toggles) are runtime configuration that controls whether "
                    "a feature is active — without deploying new code. Deploy the code with the flag off, "
                    "enable it for 1% of users, then 10%, then 100%. If something breaks, flip the flag "
                    "off instantly. Feature flags decouple deployment from release."
                ),
                hints=["It's a runtime switch, not a deployment mechanism", "Decouple 'deploy' from 'release'"],
                xp=30,
            ),
            Challenge(
                id="deploy_5",
                type="quiz",
                prompt="A production deployment causes a spike in 500 errors. What is the fastest remediation?",
                options=[
                    "Debug the error in production and push a hotfix",
                    "Roll back to the previous known-good version",
                    "Scale up the number of instances to handle the load",
                    "Restart all production servers",
                ],
                answer="b",
                explanation=(
                    "Rollback is the fastest way to restore service when a deployment causes errors. "
                    "With blue-green: switch traffic back to the previous environment. "
                    "With Kubernetes: `kubectl rollout undo deployment/myapp`. "
                    "With feature flags: disable the flag. Always fix forward later — "
                    "first priority is restoring service for users."
                ),
                hints=["Speed is critical — what's the fastest action?", "Go back to what was working 5 minutes ago"],
                xp=30,
            ),
            Challenge(
                id="deploy_6",
                type="quiz",
                prompt="Why is a 'recreate' deployment strategy considered risky for production?",
                options=[
                    "It uses too many resources during the transition",
                    "It causes downtime — all old instances are terminated before new ones start",
                    "It doesn't support rollback",
                    "It requires manual approval for each instance",
                ],
                answer="b",
                explanation=(
                    "The Recreate strategy terminates all existing instances before starting new ones. "
                    "During the gap — which can be seconds or minutes — the service is completely unavailable. "
                    "This is acceptable for development environments or batch workloads, "
                    "but never for user-facing production services that require high availability."
                ),
                hints=["What happens between stopping the old and starting the new?", "There's a gap where nothing is running"],
                xp=25,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 6 — Infrastructure as Code in CI/CD
    # ---------------------------------------------------------------------------
    "infrastructure_as_code_cicd": Zone(
        id="infrastructure_as_code_cicd",
        title="Infrastructure as Code in CI/CD",
        description="Terraform in pipelines, plan/apply workflow, drift detection, and GitOps principles.",
        challenges=[
            Challenge(
                id="iac_1",
                type="quiz",
                prompt="In a CI/CD pipeline, when should `terraform plan` run?",
                options=[
                    "Only after terraform apply succeeds",
                    "On pull requests — to show what changes will be made before they are approved",
                    "Only in production, never in CI",
                    "After deployment, to verify the infrastructure matches",
                ],
                answer="b",
                explanation=(
                    "Terraform plan should run on every pull request. The plan output shows exactly "
                    "what infrastructure changes will occur — resources created, modified, or destroyed. "
                    "Reviewers can read the plan before approving the PR. This is the 'review before apply' pattern "
                    "and is fundamental to safe infrastructure automation."
                ),
                hints=["When should reviewers see what will change?", "It's a preview that runs before the actual change"],
                xp=30,
            ),
            Challenge(
                id="iac_2",
                type="quiz",
                prompt="When should `terraform apply` run in a CI/CD pipeline?",
                options=[
                    "On every commit to any branch",
                    "Only on merge to main (or the designated trunk branch), after plan was reviewed and approved",
                    "Manually, from a developer's local machine",
                    "On a daily schedule regardless of code changes",
                ],
                answer="b",
                explanation=(
                    "Terraform apply should only run after the plan has been reviewed and the PR is merged. "
                    "Typically: plan runs on PR, apply runs on merge to main. This ensures that no "
                    "infrastructure change is made without review. Running apply on every commit or "
                    "from local machines bypasses the review process and creates drift."
                ),
                hints=["Apply makes real changes — when should that happen?", "After the plan was reviewed and the code was merged"],
                xp=30,
            ),
            Challenge(
                id="iac_3",
                type="quiz",
                prompt="What is 'drift' in the context of Infrastructure as Code?",
                options=[
                    "When Terraform code is refactored but behavior stays the same",
                    "When the actual infrastructure state differs from what the code defines",
                    "When two developers modify the same Terraform file",
                    "When Terraform providers are updated to new versions",
                ],
                answer="b",
                explanation=(
                    "Drift occurs when someone modifies infrastructure manually (via console, CLI, or ad-hoc scripts) "
                    "without updating the Terraform code. The actual state diverges from the declared state. "
                    "Drift is dangerous because the code no longer reflects reality. "
                    "Drift detection: run `terraform plan` periodically — any planned changes indicate drift."
                ),
                hints=["The real world doesn't match the code", "Someone made a manual change outside Terraform"],
                xp=30,
            ),
            Challenge(
                id="iac_4",
                type="quiz",
                prompt="What is the core principle of GitOps?",
                options=[
                    "All developers must use git for version control",
                    "The git repository is the single source of truth — all changes flow through PRs and the pipeline enforces the desired state",
                    "Git hooks replace all CI/CD pipelines",
                    "Operations teams must review every git commit",
                ],
                answer="b",
                explanation=(
                    "GitOps: the git repository is the single source of truth for both application code "
                    "and infrastructure. All changes are made via pull requests. The pipeline automatically "
                    "reconciles the actual state with the declared state in git. No manual changes. "
                    "No local applies. If it's not in git, it doesn't exist."
                ),
                hints=["Git is the source of truth for EVERYTHING", "Changes only happen through the repo, never manually"],
                xp=35,
            ),
            Challenge(
                id="iac_5",
                type="quiz",
                prompt="Why should Terraform state files NEVER be committed to a git repository?",
                options=[
                    "They are too large for git to handle",
                    "They contain sensitive data (passwords, keys, resource IDs) and change frequently, causing merge conflicts",
                    "Git cannot track binary files",
                    "Terraform regenerates them automatically on every run",
                ],
                answer="b",
                explanation=(
                    "Terraform state files contain the full state of your infrastructure — including "
                    "database passwords, API keys, and resource identifiers in plaintext. They also change "
                    "on every apply, creating constant merge conflicts. Store state in a remote backend "
                    "(S3 + DynamoDB, Terraform Cloud, GCS) with encryption and state locking."
                ),
                hints=["Think about what's inside the state file", "Sensitive data + frequent changes = bad for git"],
                xp=35,
            ),
            Challenge(
                id="iac_6",
                type="quiz",
                prompt="What does Terraform state locking prevent?",
                options=[
                    "Unauthorized users from reading the state file",
                    "Two pipeline runs from modifying infrastructure simultaneously, causing corruption",
                    "Terraform from destroying existing resources",
                    "Drift between the state file and actual infrastructure",
                ],
                answer="b",
                explanation=(
                    "State locking prevents concurrent modifications. If two pipelines run `terraform apply` "
                    "simultaneously, they could both read the same state, make conflicting changes, "
                    "and corrupt the state file. A lock (via DynamoDB, Consul, or Terraform Cloud) "
                    "ensures only one operation runs at a time. The second operation waits or fails."
                ),
                hints=["What happens if two applies run at the exact same time?", "It's a concurrency problem"],
                xp=35,
            ),
        ],
    ),

    # ---------------------------------------------------------------------------
    # ZONE 7 — Monitoring and Observability
    # ---------------------------------------------------------------------------
    "monitoring_and_observability": Zone(
        id="monitoring_and_observability",
        title="Monitoring and Observability",
        description="Post-deploy checks, health checks, alerting, SLOs, and incident triggers.",
        challenges=[
            Challenge(
                id="mon_1",
                type="quiz",
                prompt="What is a post-deployment health check?",
                options=[
                    "A manual review of deployment logs by the team lead",
                    "An automated verification that the newly deployed service is running and responding correctly",
                    "A security scan that runs after deployment",
                    "A rollback trigger that fires 24 hours after deployment",
                ],
                answer="b",
                explanation=(
                    "Post-deployment health checks are automated tests that verify the new deployment "
                    "is functional — the service responds to HTTP requests, key endpoints return 200s, "
                    "database connections work. If health checks fail, the pipeline can automatically "
                    "trigger a rollback. This is the final gate before a deployment is considered complete."
                ),
                hints=["Automated, not manual", "Verifies the service actually works after deploying"],
                xp=25,
            ),
            Challenge(
                id="mon_2",
                type="quiz",
                prompt="What is an SLO (Service Level Objective)?",
                options=[
                    "A contract between a vendor and customer with financial penalties",
                    "A target for service reliability (e.g., 99.9% availability, p99 latency < 200ms)",
                    "A deployment schedule that defines when releases can happen",
                    "A security compliance framework for production services",
                ],
                answer="b",
                explanation=(
                    "An SLO is an internal target for service reliability — '99.9% of requests succeed' "
                    "or 'p99 latency stays below 200ms.' SLOs define what 'healthy' means in measurable terms. "
                    "SLIs (indicators) are the metrics. SLOs are the targets. SLAs (agreements) are the contracts. "
                    "When an SLO is at risk, deployments should be frozen and the error budget reviewed."
                ),
                hints=["It's a target, not a contract", "Think: 'our service should be this reliable'"],
                xp=30,
            ),
            Challenge(
                id="mon_3",
                type="quiz",
                prompt="What is an 'error budget' in the context of SRE and CI/CD?",
                options=[
                    "The financial budget allocated to fixing production bugs",
                    "The allowed amount of unreliability — the gap between 100% and the SLO target",
                    "The maximum number of errors a test suite can have before failing",
                    "The time budget for incident response",
                ],
                answer="b",
                explanation=(
                    "If your SLO is 99.9% availability, your error budget is 0.1% — about 43 minutes of "
                    "downtime per month. The error budget is spent by outages, slow deployments, and failed "
                    "rollouts. When the budget is exhausted, the team should freeze deployments and focus "
                    "on reliability. Error budgets turn reliability into a measurable, spendable resource."
                ),
                hints=["How much unreliability are you allowed?", "100% minus SLO target = error budget"],
                xp=35,
            ),
            Challenge(
                id="mon_4",
                type="quiz",
                prompt="Which of the 'three pillars of observability' helps trace a single request across multiple microservices?",
                options=[
                    "Logs",
                    "Metrics",
                    "Distributed traces",
                    "Health checks",
                ],
                answer="c",
                explanation=(
                    "The three pillars of observability: Logs (discrete events), Metrics (aggregated measurements), "
                    "and Traces (request paths across services). Distributed tracing follows a single request "
                    "through every microservice it touches — API gateway to auth service to database to cache — "
                    "showing latency at each hop. Tools: Jaeger, Zipkin, OpenTelemetry, AWS X-Ray."
                ),
                hints=["Following a single request through multiple services", "The answer is about tracing the path, not counting or recording"],
                xp=30,
            ),
            Challenge(
                id="mon_5",
                type="quiz",
                prompt="An alert fires every time CPU usage exceeds 70% for 10 seconds. This generates 50 alerts per day, most of which are harmless. What is this called?",
                options=[
                    "Alert fatigue caused by a noisy/low-threshold alert",
                    "Effective monitoring with high sensitivity",
                    "A well-tuned SLO-based alert",
                    "Proactive incident detection",
                ],
                answer="a",
                explanation=(
                    "Alert fatigue: when too many non-actionable alerts train operators to ignore them. "
                    "The fix: alert on symptoms (error rate, latency) not causes (CPU, memory). "
                    "Use SLO-based alerting: alert when the error budget burn rate indicates the SLO "
                    "will be breached within hours. A good alert is actionable, urgent, and rare."
                ),
                hints=["50 alerts/day that are mostly harmless = a problem", "When you get too many alerts, you stop paying attention"],
                xp=35,
            ),
            Challenge(
                id="mon_6",
                type="quiz",
                prompt="After deploying a new version, which automated action should trigger if the error rate exceeds the SLO threshold?",
                options=[
                    "Send a Slack notification and wait for manual review",
                    "Automatic rollback to the previous version",
                    "Scale up instances to handle the errors",
                    "Disable monitoring until the issue is resolved",
                ],
                answer="b",
                explanation=(
                    "Automated rollback is the correct response when post-deploy metrics breach SLO thresholds. "
                    "The pipeline should monitor key metrics (error rate, latency, saturation) for a bake period "
                    "after deployment. If thresholds are breached, the previous version is restored automatically. "
                    "This is the feedback loop that makes CI/CD safe: deploy fast, detect fast, rollback fast."
                ),
                hints=["What's the fastest way to stop the bleeding?", "The pipeline should fix itself, not wait for a human"],
                xp=40,
            ),
        ],
    ),
}
