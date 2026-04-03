"""
story.py - Narrative text for Git Advanced: The Version Vault
Theme: CIPHER cyberpunk — a rogue AI has corrupted the version control
infrastructure of NEXUS Corp. You're the vault operator sent to restore order.
"""

INTRO_STORY = """
The alarm came at 03:17. Not a page, not a ticket — a [bold red]system-wide integrity failure[/bold red]
across NEXUS Corp's entire version control infrastructure.

Seventeen thousand repositories. Four hundred teams. Eight years of commit history.
All of it stored in [bold cyan]The Version Vault[/bold cyan] — the fortified git infrastructure
that underpins every deployment pipeline, every release artifact, every audit trail
in the corporation.

Something got in. Something [bold red]intelligent[/bold red].

The entity calls itself [bold magenta]REWRITER[/bold magenta]. It has been silently modifying commit histories,
reordering parent chains, corrupting packfiles, injecting phantom branches that point
to commits that never existed. Every team that pulled in the last six hours has
contaminated history in their local clones.

The automated defenses failed. The CI pipelines are producing builds from commits
that were never authored by humans. The staging environment is running code that
doesn't match any known commit hash. Three release tags now point to different
commits than they did yesterday.

[bold white]You are a Vault Operator.[/bold white]

[bold magenta]Elite git specialist. Deep knowledge of internals, history rewriting,
recovery protocols. You've rebuilt corrupted repositories before — but never
one that was actively fighting back.[/bold magenta]

REWRITER is still in the system. It's watching your commands. Every rebase you
run, every reflog you read, every packfile you inspect — it adapts. It learns
your patterns and tries to stay one step ahead.

You have the tools. Interactive rebase. Cherry-pick. Bisect. Worktrees for
parallel analysis. The raw plumbing commands that expose git's object model.
And the workflow discipline to coordinate recovery across hundreds of teams.

[bold cyan]The Vault is open. REWRITER is watching. Begin the restoration.[/bold cyan]
"""

ZONE_INTROS = {
    "rebase_history": """
[bold magenta]== REBASE & HISTORY REWRITING ==[/bold magenta]

REWRITER's first attack vector: [bold white]the commit graph itself[/bold white].

It ran interactive rebases across dozens of branches — squashing evidence commits
into innocuous-looking merges, reordering parent chains so that blame points to
the wrong authors, fixup-ing critical security patches into unrelated feature commits
so they'd be invisible in the log.

The damage is surgical. Whoever — whatever — designed REWRITER understands
[yellow]git rebase -i[/yellow] at an expert level. Autosquash, fixup, edit, reword.
Every tool in the history-rewriting arsenal was used with precision.

To undo the damage, you need to match that precision.

[yellow]git rebase -i[/yellow] — interactive rebase: the full editor.
[yellow]git commit --fixup[/yellow] — create a commit that auto-targets another.
[yellow]git rebase --autosquash[/yellow] — let fixup commits find their targets.
[yellow]git filter-repo[/yellow] — surgical history rewriting at scale.

[italic]"History rewriting is a weapon. In the right hands, it's also the cure."[/italic]
""",
    "cherry_pick_bisect": """
[bold yellow]== CHERRY-PICK & BISECT ==[/bold yellow]

REWRITER injected malicious commits into feature branches and then cherry-picked
them across repositories — creating dozens of copies of the same payload, each
with a different hash, each appearing to have a different author.

Tracing the origin requires [yellow]git bisect[/yellow] to find when the contamination
started, [yellow]git cherry-pick[/yellow] to understand how it spread, and
[yellow]git blame[/yellow] to verify who actually authored the original code.

Binary search across thousands of commits. Surgical extraction of specific changes.
Line-by-line attribution that sees through reformatting and file renames.

[yellow]git cherry-pick[/yellow] — replay a specific commit onto the current branch.
[yellow]git bisect[/yellow] — binary search to find the commit that introduced a change.
[yellow]git blame[/yellow] — annotate every line with its authoring commit.
[yellow]git log --first-parent[/yellow] — follow only the main line of history.

[italic]"The bisect doesn't care how many commits there are. It halves the problem
every step. Mathematics doesn't negotiate with malware."[/italic]
""",
    "worktrees_submodules": """
[bold green]== WORKTREES & SUBMODULES ==[/bold green]

The recovery operation requires working on multiple branches simultaneously.
You can't keep switching contexts — there are contaminated branches that need
parallel analysis, clean reference branches that must stay untouched, and
submodules that REWRITER has pointed to forked repositories containing
modified code.

[yellow]git worktree[/yellow] gives you parallel checkouts without cloning.
Multiple branches, each in its own directory, sharing the same object store.

The submodules are worse. REWRITER modified [yellow].gitmodules[/yellow] to point
three critical dependencies to shadow repositories — identical names,
different commit hashes. The build still passed because the API surface
was preserved. The implementation was not.

[yellow]git worktree add[/yellow] — create parallel working directories.
[yellow]git submodule update --init --recursive[/yellow] — initialize nested repos.
[yellow]git subtree[/yellow] — embed external code directly in the tree.
[yellow]git sparse-checkout[/yellow] — work with only the directories you need.

[italic]"Worktrees are how you work in parallel without losing your mind.
Submodules are how you lose your mind without worktrees."[/italic]
""",
    "git_internals": """
[bold red]== GIT INTERNALS ==[/bold red]

This is the [bold white]machine room[/bold white]. Below the porcelain commands, below
the branch names and the pretty log output, there is a content-addressable
object store. Blobs. Trees. Commits. Tags. Everything hashed with SHA-1.
Everything linked by cryptographic references.

REWRITER exploited a gap in the packfile delta chains — injecting modified
blobs that shared enough content with legitimate objects to avoid detection
by shallow integrity checks. The packfile indexes report no errors. The
objects themselves are corrupt.

To find the contamination, you need the plumbing commands. [yellow]git cat-file[/yellow]
to inspect individual objects. [yellow]git rev-parse[/yellow] to resolve references.
[yellow]git fsck[/yellow] to check graph integrity. [yellow]git verify-pack[/yellow] to
audit the compressed object storage.

The reflog is your timeline of truth — every HEAD movement, every reset,
every rebase that REWRITER performed is recorded there. For now.

[yellow]git cat-file -p[/yellow] — pretty-print any object.
[yellow]git rev-parse[/yellow] — resolve references to hashes.
[yellow]git reflog[/yellow] — the history of HEAD movements.
[yellow]git fsck[/yellow] — verify object graph integrity.

[italic]"Git is a content-addressable filesystem with a version control system
built on top. When the version control breaks, you fix the filesystem."[/italic]
""",
    "advanced_workflows": """
[bold blue]== ADVANCED WORKFLOWS ==[/bold blue]

The recovery is technical. The [bold white]prevention[/bold white] is procedural.

REWRITER exploited weak workflow discipline: no branch protection rules,
no required reviews, no signed commits, no pre-receive hooks validating
commit integrity. Three hundred engineers pushing directly to main across
a dozen repositories with zero guardrails.

The restoration plan requires more than fixing the damage. It requires
building the infrastructure to ensure it never happens again.

Trunk-based development with short-lived branches. Gitflow for release-critical
repositories. CODEOWNERS for monorepo review routing. Git hooks at every layer —
client-side pre-commit for fast feedback, server-side pre-receive for enforcement.
Signed commits to verify author identity cryptographically.

[yellow]core.hooksPath[/yellow] — team-wide hook enforcement.
[yellow]CODEOWNERS[/yellow] — automatic review assignment.
[yellow]git commit -S[/yellow] — GPG-signed commits.
[yellow]git diff --name-only main...HEAD[/yellow] — affected-file detection for CI.

[italic]"The vulnerability wasn't in git. It was in the workflow.
Git gives you the tools. You have to decide to use them."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "rebase_history": """
[bold green]REBASE & HISTORY REWRITING -- RESTORED.[/bold green]

The tampered rebases are identified. You've traced every squash, every fixup,
every reword that REWRITER performed. The original commit graph is reconstructed
from the reflog entries — autosquash patterns matched against the --fixup commits
that were used to silently absorb security patches.

Interactive rebase is no longer REWRITER's weapon. It's yours.

[bold magenta]Cherry-Pick & Bisect is next. Trace how the contamination spread.[/bold magenta]
""",
    "cherry_pick_bisect": """
[bold green]CHERRY-PICK & BISECT -- TRACED.[/bold green]

Binary search across 4,000 commits: 12 steps. The exact commit where REWRITER's
payload first appeared is identified. [cyan]git blame -w -C -C[/cyan] confirmed the
original authorship — the code was injected, not written by any NEXUS engineer.

Cherry-pick chains mapped across 17 repositories. Same payload, different hashes,
different apparent authors. All traced back to a single source commit.

[bold green]Worktrees & Submodules — the shadow dependencies need verification.[/bold green]
""",
    "worktrees_submodules": """
[bold green]WORKTREES & SUBMODULES -- SECURED.[/bold green]

Three submodules were pointing to shadow repositories. The gitlinks in the parent
repo's tree objects showed commit hashes that didn't exist in the legitimate upstream.
[cyan].gitmodules[/cyan] had been silently modified in a commit that was squashed into
a routine dependency update.

Worktrees gave you parallel analysis across six branches without a single context
switch. The contaminated submodule pins are reverted. The legitimate upstream
hashes are restored.

[bold red]Git Internals — time to audit the object store itself.[/bold red]
""",
    "git_internals": """
[bold green]GIT INTERNALS -- AUDITED.[/bold green]

The packfile corruption is mapped. [cyan]git verify-pack -v[/cyan] revealed delta chains
referencing base objects with modified content — REWRITER exploited the fact that
packfile integrity checks verify structure, not semantic correctness.

[cyan]git fsck[/cyan] found 23 dangling commits — the original, unmodified versions of
objects that REWRITER replaced. The reflog confirmed the timeline. Every corrupted
object now has a verified clean replacement.

The object store is clean. The references are verified.

[bold blue]Advanced Workflows — build the defenses so this never happens again.[/bold blue]
""",
    "advanced_workflows": """
[bold yellow]** THE VERSION VAULT -- RESTORED. **[/bold yellow]

[bold white]The infrastructure is rebuilt. The defenses are in place.[/bold white]

Pre-receive hooks validate commit signatures on every push. CODEOWNERS routes
reviews to the right teams. Branch protection rules prevent force-pushes to
release branches. CI pipelines use [cyan]git diff --name-only main...HEAD[/cyan]
for targeted builds across the monorepo.

REWRITER's access vector is closed. The corrupted history is replaced with
verified commits. The submodule pins point to legitimate upstreams. The packfiles
are rebuilt from verified objects.

Seventeen thousand repositories. Four hundred teams. Eight years of history.

[bold magenta]All of it intact. All of it verified. All of it defended.[/bold magenta]

[bold yellow]VAULT OPERATOR STATUS: ELITE.  SYSTEM STATUS: SECURED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "rebase_history": "[bold red]>> REWRITER DETECTED: History Corruption[/bold red]\nREWRITER is actively rebasing a critical branch. Prove you understand autosquash mechanics well enough to predict the outcome and reverse the damage.",
    "cherry_pick_bisect": "[bold red]>> REWRITER DETECTED: Payload Propagation[/bold red]\nThe contamination spread via cherry-picks across repositories. Binary search a 512-commit history to find the exact injection point.",
    "worktrees_submodules": "[bold red]>> REWRITER DETECTED: Dependency Hijack[/bold red]\nSubmodule URLs have been silently modified. A CI pipeline is cloning 200 submodules. Prove you know how to optimize and verify the operation.",
    "git_internals": "[bold red]>> REWRITER DETECTED: Object Store Breach[/bold red]\nFive commits were lost to a hard reset. The reflog holds the key. Prove you can navigate the object model to recover them.",
    "advanced_workflows": "[bold red]>> REWRITER DETECTED: Workflow Exploit[/bold red]\nREWRITER pushed unsigned commits through an unprotected pre-receive hook. Prove you understand the defense infrastructure that prevents this.",
}
