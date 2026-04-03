"""
zones.py - All zone and challenge data for Git Advanced: The Version Vault
5 zones, 8 challenges each (40 total).
Challenge types: quiz (options as list), text (options as [])
"""

ZONES = {
    "rebase_history": {
        "id": "rebase_history",
        "name": "Rebase & History Rewriting",
        "subtitle": "Interactive Rebase, Fixup & Autosquash",
        "color": "magenta",
        "icon": "\u2694",
        "commands": [
            "git rebase -i",
            "git commit --fixup",
            "git commit --squash",
            "git rebase --autosquash",
            "git filter-branch",
            "git filter-repo",
        ],
        "challenges": [
            {
                "id": "rh_1",
                "type": "quiz",
                "question": "During an interactive rebase, you want to combine a commit into the previous one AND discard its commit message. Which action keyword do you use?",
                "options": [
                    "squash — combine and concatenate both messages",
                    "fixup — combine and discard this commit's message",
                    "drop — remove the commit entirely",
                    "reword — change the commit message only",
                ],
                "answer": "b",
                "lesson": (
                    "fixup (or 'f') combines the commit into the one above it in the rebase todo list,\n"
                    "but discards the fixup commit's message entirely. The result is a single commit\n"
                    "with the original message preserved.\n\n"
                    "squash (or 's') also combines, but opens your editor to let you merge both messages.\n"
                    "fixup is squash's quieter sibling — use it when the commit was just a typo fix\n"
                    "or minor correction that doesn't deserve its own line in history."
                ),
                "xp": 15,
            },
            {
                "id": "rh_2",
                "type": "text",
                "question": "What command creates a fixup commit that will automatically be combined with commit abc1234 during an autosquash rebase?",
                "options": [],
                "answer": "git commit --fixup=abc1234",
                "lesson": (
                    "git commit --fixup=<commit> creates a new commit whose message is\n"
                    "'fixup! <original message>'. When you later run git rebase -i --autosquash,\n"
                    "git automatically reorders the fixup commit right after its target and\n"
                    "marks it with the 'fixup' action.\n\n"
                    "This is the professional workflow for cleaning up history:\n"
                    "  1. Make the fix\n"
                    "  2. git commit --fixup=<target>\n"
                    "  3. git rebase -i --autosquash <base>\n"
                    "The fixup is applied automatically — no manual reordering needed."
                ),
                "xp": 20,
            },
            {
                "id": "rh_3",
                "type": "quiz",
                "question": "You run git rebase -i HEAD~5. In the editor, you change the action for the third commit from 'pick' to 'edit'. What happens when the rebase reaches that commit?",
                "options": [
                    "The commit is applied and the rebase continues automatically",
                    "The commit is applied and the rebase pauses, dropping you to the shell to amend it",
                    "The commit is skipped entirely",
                    "The commit message editor opens for that commit only",
                ],
                "answer": "b",
                "lesson": (
                    "The 'edit' action applies the commit, then pauses the rebase so you can:\n"
                    "  - Amend the commit (git commit --amend)\n"
                    "  - Split it into multiple commits (git reset HEAD~1, then commit pieces)\n"
                    "  - Add or remove files\n"
                    "  - Make any other changes\n\n"
                    "When you're done, run git rebase --continue to proceed.\n"
                    "This is the most powerful interactive rebase action — it gives you\n"
                    "full control over what that commit becomes."
                ),
                "xp": 15,
            },
            {
                "id": "rh_4",
                "type": "text",
                "question": "What flag do you pass to git rebase -i so that commits created with --fixup and --squash are automatically reordered and marked?",
                "options": [],
                "answer": "--autosquash",
                "lesson": (
                    "git rebase -i --autosquash automatically reorders commits whose messages\n"
                    "start with 'fixup!' or 'squash!' to appear right after their target commits,\n"
                    "and sets their action to fixup or squash respectively.\n\n"
                    "Pro tip: set rebase.autoSquash=true in your git config to make this the\n"
                    "default behavior for all interactive rebases:\n"
                    "  git config --global rebase.autoSquash true\n\n"
                    "This turns --fixup/--squash commits into a seamless history-cleanup workflow."
                ),
                "xp": 20,
            },
            {
                "id": "rh_5",
                "type": "quiz",
                "question": "You need to remove a file containing secrets from every commit in your repository's history. Which modern tool is recommended over git filter-branch?",
                "options": [
                    "git rebase -i — interactively edit each commit",
                    "git filter-repo — fast, safe Python-based history rewriter",
                    "git reset --hard — wipe back to before the secret was added",
                    "git rm --cached — remove from index only",
                ],
                "answer": "b",
                "lesson": (
                    "git-filter-repo is the officially recommended replacement for git filter-branch.\n"
                    "It's dramatically faster (10-100x), safer, and has a cleaner API.\n\n"
                    "Example: remove a file from all history:\n"
                    "  git filter-repo --invert-paths --path secrets.env\n\n"
                    "git filter-branch is deprecated because it's slow, has confusing semantics,\n"
                    "and can produce broken histories in edge cases. The git project itself\n"
                    "recommends filter-repo as the replacement.\n\n"
                    "After rewriting history, all commit hashes change — every collaborator\n"
                    "must re-clone or carefully rebase onto the new history."
                ),
                "xp": 15,
            },
            {
                "id": "rh_6",
                "type": "quiz",
                "question": "During an interactive rebase, you realize you've made a mistake and want to abort the entire operation, restoring the branch to its pre-rebase state. What command do you run?",
                "options": [
                    "git rebase --skip",
                    "git rebase --abort",
                    "git rebase --quit",
                    "git reset --hard ORIG_HEAD",
                ],
                "answer": "b",
                "lesson": (
                    "git rebase --abort completely cancels the in-progress rebase and restores\n"
                    "the branch to exactly where it was before the rebase started.\n\n"
                    "Related commands:\n"
                    "  --skip      skip the current conflicting commit and continue\n"
                    "  --continue  proceed after resolving conflicts\n"
                    "  --quit      stop rebasing but don't reset (leaves partial rebase)\n\n"
                    "ORIG_HEAD is also set before a rebase, so git reset --hard ORIG_HEAD works\n"
                    "after a completed rebase — but --abort is the clean way during one."
                ),
                "xp": 10,
            },
            {
                "id": "rh_7",
                "type": "text",
                "question": "You want to split the most recent commit into two separate commits. After running git reset HEAD~1 (which undoes the commit but keeps changes staged), what is the next step to begin creating the first of the two new commits?",
                "options": [],
                "answer": "git add",
                "lesson": (
                    "Splitting a commit is a two-phase process:\n\n"
                    "  1. git reset HEAD~1  (undo the commit, keep changes in working tree)\n"
                    "     Note: with --mixed (default), changes become unstaged.\n"
                    "  2. git add <subset-of-files>  (stage only what belongs in the first commit)\n"
                    "  3. git commit -m 'First part'\n"
                    "  4. git add <remaining-files>\n"
                    "  5. git commit -m 'Second part'\n\n"
                    "During an interactive rebase, mark the commit as 'edit', then follow\n"
                    "the same process. Finish with git rebase --continue."
                ),
                "xp": 20,
            },
            {
                "id": "rh_boss",
                "type": "quiz",
                "question": "You have 10 commits on a feature branch. Commits 3 and 7 are fixup commits (created with --fixup). You run: git rebase -i --autosquash main. After the rebase completes, how many commits will remain?",
                "options": [
                    "10 — autosquash only reorders, doesn't reduce commit count",
                    "8 — the two fixup commits are folded into their targets",
                    "9 — only one fixup is applied per rebase run",
                    "7 — fixup commits and their targets are both removed",
                ],
                "answer": "b",
                "lesson": (
                    "Each --fixup commit is folded into its target commit, reducing the total\n"
                    "count by one per fixup. Two fixup commits = two fewer commits = 8 remaining.\n\n"
                    "The resulting commits have:\n"
                    "  - The combined changes of target + fixup\n"
                    "  - The original target's commit message (fixup discards its own message)\n"
                    "  - A new hash (because the content changed)\n\n"
                    "This is the standard professional workflow for keeping feature branch history\n"
                    "clean before merging to main."
                ),
                "xp": 25,
            },
        ],
    },
    "cherry_pick_bisect": {
        "id": "cherry_pick_bisect",
        "name": "Cherry-Pick & Bisect",
        "subtitle": "Surgical Commits, Binary Search & Blame",
        "color": "yellow",
        "icon": "\U0001f50d",
        "commands": [
            "git cherry-pick",
            "git bisect",
            "git blame",
            "git log --first-parent",
        ],
        "challenges": [
            {
                "id": "cpb_1",
                "type": "quiz",
                "question": "git cherry-pick applies a commit from another branch to your current branch. What does it actually create?",
                "options": [
                    "A reference pointing to the original commit",
                    "A new commit with the same diff but a different hash",
                    "A merge commit linking both branches",
                    "A symbolic link to the original commit object",
                ],
                "answer": "b",
                "lesson": (
                    "Cherry-pick replays the changes introduced by a commit onto your current branch\n"
                    "as a brand new commit. The new commit has:\n"
                    "  - The same diff (code changes)\n"
                    "  - A different parent (your current HEAD)\n"
                    "  - A different hash (because parent changed)\n"
                    "  - The same author info (preserved from original)\n"
                    "  - You as the committer\n\n"
                    "This means the 'same' change now exists as two different commits.\n"
                    "If both branches later merge, git may or may not detect the duplication."
                ),
                "xp": 15,
            },
            {
                "id": "cpb_2",
                "type": "text",
                "question": "What command starts a git bisect session, marking the current commit as bad?",
                "options": [],
                "answer": "git bisect start",
                "lesson": (
                    "git bisect uses binary search to find the commit that introduced a bug.\n\n"
                    "The workflow:\n"
                    "  1. git bisect start\n"
                    "  2. git bisect bad          (current commit has the bug)\n"
                    "  3. git bisect good <hash>  (this older commit was fine)\n"
                    "  4. Git checks out the midpoint. You test. Mark good or bad.\n"
                    "  5. Repeat until git identifies the exact commit.\n"
                    "  6. git bisect reset        (return to original HEAD)\n\n"
                    "For N commits, bisect finds the culprit in log2(N) steps.\n"
                    "1000 commits? About 10 tests."
                ),
                "xp": 15,
            },
            {
                "id": "cpb_3",
                "type": "quiz",
                "question": "You want to automate git bisect using a test script that exits 0 for good and non-zero for bad. What command configures this?",
                "options": [
                    "git bisect auto ./test.sh",
                    "git bisect run ./test.sh",
                    "git bisect script ./test.sh",
                    "git bisect exec ./test.sh",
                ],
                "answer": "b",
                "lesson": (
                    "git bisect run <script> automates the entire bisect process.\n\n"
                    "Git checks out each midpoint and runs your script:\n"
                    "  - Exit code 0 = good (bug not present)\n"
                    "  - Exit code 1-124, 126-127 = bad (bug is present)\n"
                    "  - Exit code 125 = skip (can't test this commit)\n\n"
                    "Example: git bisect run make test\n"
                    "Example: git bisect run python -c 'import mymodule; assert mymodule.works()'\n\n"
                    "This can find a regression in a 10,000-commit history in under a minute\n"
                    "if your test script is fast."
                ),
                "xp": 20,
            },
            {
                "id": "cpb_4",
                "type": "text",
                "question": "What git command shows the last commit that modified each line of a file?",
                "options": [],
                "answer": "git blame",
                "lesson": (
                    "git blame <file> annotates each line with:\n"
                    "  - The commit hash that last modified it\n"
                    "  - The author\n"
                    "  - The timestamp\n"
                    "  - The line number and content\n\n"
                    "Useful flags:\n"
                    "  -L 10,20     only blame lines 10-20\n"
                    "  -w           ignore whitespace changes\n"
                    "  -M           detect moved lines within a file\n"
                    "  -C           detect lines moved from other files\n"
                    "  -C -C -C    detect across all commits (expensive but thorough)\n\n"
                    "git blame -w -C -C is the forensic analyst's best friend."
                ),
                "xp": 10,
            },
            {
                "id": "cpb_5",
                "type": "quiz",
                "question": "You cherry-pick a commit and get a conflict. After resolving the conflict, what command do you run to finalize the cherry-pick?",
                "options": [
                    "git cherry-pick --continue",
                    "git commit",
                    "git cherry-pick --resolve",
                    "Both A and B will work",
                ],
                "answer": "d",
                "lesson": (
                    "After resolving a cherry-pick conflict, both approaches work:\n"
                    "  - git cherry-pick --continue  (the 'official' way)\n"
                    "  - git commit                  (also works, since the cherry-pick state is tracked)\n\n"
                    "Other conflict resolution options:\n"
                    "  --abort    cancel the cherry-pick entirely\n"
                    "  --skip     skip this commit (in a multi-commit cherry-pick)\n\n"
                    "To cherry-pick without auto-committing (useful for combining changes):\n"
                    "  git cherry-pick --no-commit <hash>"
                ),
                "xp": 15,
            },
            {
                "id": "cpb_6",
                "type": "quiz",
                "question": "git blame shows a commit that just reformatted code. You want to look through that commit to find the real author who wrote the logic. What flag helps?",
                "options": [
                    "-w — ignore whitespace-only changes",
                    "-n — show original line numbers",
                    "-e — show email instead of author name",
                    "-s — suppress author name",
                ],
                "answer": "a",
                "lesson": (
                    "git blame -w ignores whitespace changes when assigning blame.\n"
                    "This 'sees through' commits that only reformatted code, attributing\n"
                    "each line to the commit that last changed its actual content.\n\n"
                    "For deeper archaeology:\n"
                    "  -M    detect moved/copied lines within the same file\n"
                    "  -C    detect lines moved from other files in the same commit\n"
                    "  -C -C detect lines moved from other files in any commit\n\n"
                    "Stack them: git blame -w -M -C -C <file>\n"
                    "This is how you find the true origin of code that's been shuffled around."
                ),
                "xp": 15,
            },
            {
                "id": "cpb_7",
                "type": "text",
                "question": "What command cherry-picks a range of commits from abc1234 (exclusive) to def5678 (inclusive) onto your current branch?",
                "options": [],
                "answer": "git cherry-pick abc1234..def5678",
                "lesson": (
                    "git cherry-pick supports commit ranges using the .. syntax:\n"
                    "  git cherry-pick A..B\n"
                    "  Applies commits AFTER A up to and including B.\n\n"
                    "Important: A is exclusive (not included), B is inclusive.\n"
                    "To include A as well, use A^..B or A~1..B.\n\n"
                    "Each commit in the range is applied as a separate new commit.\n"
                    "If any commit conflicts, the cherry-pick pauses for resolution.\n"
                    "Use --continue/--abort/--skip to manage multi-commit cherry-picks."
                ),
                "xp": 20,
            },
            {
                "id": "cpb_boss",
                "type": "quiz",
                "question": "You're bisecting a regression across 512 commits. Git bisect uses binary search. What is the maximum number of steps needed to find the exact offending commit?",
                "options": [
                    "9 — log2(512) = 9",
                    "256 — half of 512",
                    "10 — log2(512) + 1",
                    "512 — worst case checks every commit",
                ],
                "answer": "a",
                "lesson": (
                    "Git bisect performs a binary search: each step halves the remaining\n"
                    "candidates. For N commits, it takes at most ceil(log2(N)) steps.\n\n"
                    "  512 commits: log2(512) = 9 steps\n"
                    "  1024 commits: 10 steps\n"
                    "  1,000,000 commits: ~20 steps\n\n"
                    "This is why bisect is so powerful — even enormous repositories can be\n"
                    "searched in under 25 manual tests. With 'git bisect run' automating\n"
                    "the test, the entire process takes seconds to minutes."
                ),
                "xp": 25,
            },
        ],
    },
    "worktrees_submodules": {
        "id": "worktrees_submodules",
        "name": "Worktrees & Submodules",
        "subtitle": "Parallel Workspaces & Nested Repositories",
        "color": "green",
        "icon": "\U0001f333",
        "commands": [
            "git worktree",
            "git submodule",
            "git subtree",
            "git sparse-checkout",
        ],
        "challenges": [
            {
                "id": "ws_1",
                "type": "quiz",
                "question": "git worktree add ../hotfix main creates a new working tree. What is the key advantage over simply cloning the repo again?",
                "options": [
                    "Worktrees share the same .git directory — no extra disk space for objects",
                    "Worktrees automatically sync changes between each other",
                    "Worktrees can only be created for remote branches",
                    "Worktrees create shallow copies without full history",
                ],
                "answer": "a",
                "lesson": (
                    "git worktree lets you check out multiple branches simultaneously,\n"
                    "each in its own directory, all sharing a single .git object store.\n\n"
                    "  git worktree add ../hotfix main\n"
                    "  Creates a directory '../hotfix' checked out to 'main'.\n\n"
                    "Benefits:\n"
                    "  - No disk duplication — objects are shared\n"
                    "  - No network fetch needed\n"
                    "  - Each worktree has its own index and working tree\n"
                    "  - You cannot check out the same branch in two worktrees\n\n"
                    "Use case: review a PR while your feature branch has uncommitted work."
                ),
                "xp": 15,
            },
            {
                "id": "ws_2",
                "type": "text",
                "question": "What command lists all active worktrees for the current repository?",
                "options": [],
                "answer": "git worktree list",
                "lesson": (
                    "git worktree list shows every worktree linked to the repository:\n"
                    "  /home/dev/project       abc1234 [main]\n"
                    "  /home/dev/project-fix   def5678 [hotfix]\n\n"
                    "Each line shows: path, HEAD commit, and branch name.\n\n"
                    "Management commands:\n"
                    "  git worktree add <path> <branch>   create a new worktree\n"
                    "  git worktree remove <path>         remove a worktree\n"
                    "  git worktree prune                 clean up stale entries\n"
                    "  git worktree lock <path>           prevent pruning of a worktree"
                ),
                "xp": 10,
            },
            {
                "id": "ws_3",
                "type": "quiz",
                "question": "What does git submodule add https://github.com/lib/core.git vendor/core actually store in the parent repository?",
                "options": [
                    "A full copy of the submodule's entire .git directory",
                    "A .gitmodules file entry and a special commit reference (gitlink) in the tree",
                    "A symbolic link to the cloned submodule",
                    "A compressed tarball of the submodule at the pinned commit",
                ],
                "answer": "b",
                "lesson": (
                    "When you add a submodule, the parent repo stores:\n"
                    "  1. An entry in .gitmodules (URL and path mapping)\n"
                    "  2. A 'gitlink' — a tree entry that points to a specific commit hash\n"
                    "     in the submodule (mode 160000 in git internals)\n\n"
                    "The submodule's .git data goes into .git/modules/<name>/ in the parent.\n"
                    "The submodule directory itself is a regular checkout.\n\n"
                    "This means the parent repo pins the submodule to an exact commit.\n"
                    "Updating requires: cd vendor/core && git pull && cd .. && git add vendor/core"
                ),
                "xp": 15,
            },
            {
                "id": "ws_4",
                "type": "text",
                "question": "After cloning a repo that contains submodules, the submodule directories are empty. What single command initializes and clones all submodules recursively?",
                "options": [],
                "answer": "git submodule update --init --recursive",
                "lesson": (
                    "git submodule update --init --recursive does three things:\n"
                    "  --init       registers submodules listed in .gitmodules\n"
                    "  update       checks out the pinned commit in each submodule\n"
                    "  --recursive  does the same for nested submodules\n\n"
                    "Alternative: clone with --recurse-submodules from the start:\n"
                    "  git clone --recurse-submodules <url>\n\n"
                    "Common pain point: submodule directories appear empty because\n"
                    "git clone does NOT automatically init submodules by default."
                ),
                "xp": 20,
            },
            {
                "id": "ws_5",
                "type": "quiz",
                "question": "What is the fundamental difference between git submodule and git subtree?",
                "options": [
                    "Subtree embeds the dependency's code directly in the parent repo's tree; submodule stores only a reference",
                    "Submodule is newer and replaces subtree entirely",
                    "Subtree only works with local repositories, not remote URLs",
                    "Submodule merges histories; subtree keeps them separate",
                ],
                "answer": "a",
                "lesson": (
                    "Submodule: stores a pointer (gitlink) to a commit in an external repo.\n"
                    "  - External repo must be cloned separately\n"
                    "  - Contributors must run submodule init/update\n"
                    "  - Clean separation, but adds workflow complexity\n\n"
                    "Subtree: copies the external repo's files directly into your tree.\n"
                    "  - No special commands needed for contributors\n"
                    "  - Changes can be pushed back upstream with git subtree push\n"
                    "  - Simpler workflow, but pollutes your commit history\n\n"
                    "Rule of thumb: submodule for large dependencies you don't modify;\n"
                    "subtree for small libraries you actively develop alongside your code."
                ),
                "xp": 15,
            },
            {
                "id": "ws_6",
                "type": "quiz",
                "question": "git sparse-checkout allows you to check out only specific directories from a large monorepo. Which command enables the cone mode sparse-checkout pattern?",
                "options": [
                    "git sparse-checkout set --cone src/",
                    "git checkout --sparse src/",
                    "git clone --filter=sparse src/",
                    "git worktree add --sparse src/",
                ],
                "answer": "a",
                "lesson": (
                    "git sparse-checkout controls which directories appear in your working tree.\n\n"
                    "Setup:\n"
                    "  git sparse-checkout init --cone\n"
                    "  git sparse-checkout set src/ docs/\n\n"
                    "Cone mode (recommended) uses directory-based patterns for speed.\n"
                    "Non-cone mode supports full gitignore-style patterns but is slower.\n\n"
                    "Combined with partial clone (--filter=blob:none), this lets you work\n"
                    "in a 10GB monorepo while only downloading the 50MB you need.\n\n"
                    "  git clone --filter=blob:none --sparse <url>\n"
                    "  git sparse-checkout set src/my-service/"
                ),
                "xp": 20,
            },
            {
                "id": "ws_7",
                "type": "text",
                "question": "What command removes a worktree located at ../hotfix-branch and cleans up its administrative files?",
                "options": [],
                "answer": "git worktree remove ../hotfix-branch",
                "lesson": (
                    "git worktree remove <path> deletes the worktree directory and its\n"
                    "administrative files in .git/worktrees/.\n\n"
                    "If the worktree has uncommitted changes, git refuses to remove it.\n"
                    "Use --force to override (you'll lose uncommitted work).\n\n"
                    "If a worktree was manually deleted (rm -rf), run:\n"
                    "  git worktree prune\n"
                    "This cleans up stale administrative entries for worktrees that\n"
                    "no longer exist on disk."
                ),
                "xp": 15,
            },
            {
                "id": "ws_boss",
                "type": "quiz",
                "question": "Your team's monorepo has 200 submodules. A CI pipeline runs git submodule update --init --recursive and takes 15 minutes. What optimization would have the biggest impact?",
                "options": [
                    "Use git submodule update --init --recursive --jobs 8 to parallelize clones",
                    "Convert all submodules to subtrees",
                    "Use git submodule update --depth 1 for shallow clones only",
                    "Replace submodules with npm packages",
                ],
                "answer": "a",
                "lesson": (
                    "The --jobs (or -j) flag parallelizes submodule operations:\n"
                    "  git submodule update --init --recursive --jobs 8\n\n"
                    "By default, submodules are cloned sequentially — one at a time.\n"
                    "With 200 submodules, parallelizing to 8 concurrent clones can\n"
                    "reduce wall time by 80%+.\n\n"
                    "Other optimizations:\n"
                    "  --depth 1         shallow clone (helps, but less impactful)\n"
                    "  --filter=blob:none  partial clone (Git 2.29+)\n"
                    "  submodule.fetchJobs=8 in git config (persistent setting)\n\n"
                    "Converting 200 submodules to subtrees would be a massive, risky migration."
                ),
                "xp": 25,
            },
        ],
    },
    "git_internals": {
        "id": "git_internals",
        "name": "Git Internals",
        "subtitle": "Objects, Refs, Reflog & Packfiles",
        "color": "red",
        "icon": "\u2699",
        "commands": [
            "git cat-file",
            "git rev-parse",
            "git reflog",
            "git fsck",
            "git gc",
            "git verify-pack",
        ],
        "challenges": [
            {
                "id": "gi_1",
                "type": "quiz",
                "question": "Git's object store has four types of objects. Which of these is NOT a git object type?",
                "options": [
                    "blob — stores file contents",
                    "tree — stores directory listings",
                    "branch — stores a pointer to a commit",
                    "tag — stores an annotated tag with metadata",
                ],
                "answer": "c",
                "lesson": (
                    "Git has exactly four object types:\n"
                    "  1. blob   — raw file contents (no filename, no permissions)\n"
                    "  2. tree   — a directory listing mapping names to blobs/trees + permissions\n"
                    "  3. commit — points to a tree, has parent(s), author, committer, message\n"
                    "  4. tag    — annotated tag: points to an object, has tagger, date, message\n\n"
                    "A branch is NOT an object — it's a reference (a file in .git/refs/heads/\n"
                    "containing a commit hash). This distinction is fundamental to understanding git."
                ),
                "xp": 15,
            },
            {
                "id": "gi_2",
                "type": "text",
                "question": "What plumbing command displays the type of a git object given its hash? (e.g., to determine if abc1234 is a blob, tree, commit, or tag)",
                "options": [],
                "answer": "git cat-file -t",
                "lesson": (
                    "git cat-file is the Swiss Army knife for inspecting git objects:\n"
                    "  -t <hash>   show the type (blob, tree, commit, tag)\n"
                    "  -p <hash>   pretty-print the contents\n"
                    "  -s <hash>   show the size in bytes\n\n"
                    "Example:\n"
                    "  $ git cat-file -t abc1234\n"
                    "  commit\n"
                    "  $ git cat-file -p abc1234\n"
                    "  tree def5678...\n"
                    "  parent 789abc...\n"
                    "  author Jane <jane@co.com> 1700000000 +0000\n\n"
                    "This is a 'plumbing' command — meant for scripts and debugging,\n"
                    "not everyday use. But it reveals how git actually stores data."
                ),
                "xp": 20,
            },
            {
                "id": "gi_3",
                "type": "quiz",
                "question": "Where does git store the reflog entries for the HEAD reference?",
                "options": [
                    ".git/objects/reflog/HEAD",
                    ".git/logs/HEAD",
                    ".git/refs/reflog/HEAD",
                    ".git/HEAD.log",
                ],
                "answer": "b",
                "lesson": (
                    "The reflog is stored in .git/logs/:\n"
                    "  .git/logs/HEAD              reflog for HEAD\n"
                    "  .git/logs/refs/heads/main   reflog for the main branch\n\n"
                    "Each line records: old-hash new-hash author timestamp action\n\n"
                    "The reflog is LOCAL ONLY — it's never pushed or pulled.\n"
                    "Default expiry: 90 days for reachable entries, 30 for unreachable.\n\n"
                    "This is why the reflog is invaluable for recovery: it records\n"
                    "every HEAD movement including resets, rebases, and checkouts —\n"
                    "even ones that 'lose' commits from the branch history."
                ),
                "xp": 15,
            },
            {
                "id": "gi_4",
                "type": "text",
                "question": "What command resolves a symbolic reference like HEAD to its full commit hash?",
                "options": [],
                "answer": "git rev-parse HEAD",
                "lesson": (
                    "git rev-parse translates any git reference into a SHA-1 hash:\n"
                    "  git rev-parse HEAD           → full 40-char hash of current commit\n"
                    "  git rev-parse main            → hash of main branch tip\n"
                    "  git rev-parse HEAD~3          → hash of 3 commits before HEAD\n"
                    "  git rev-parse --short HEAD    → abbreviated hash (7 chars)\n\n"
                    "It also resolves special references:\n"
                    "  git rev-parse --git-dir       → path to .git directory\n"
                    "  git rev-parse --show-toplevel → path to repo root\n\n"
                    "Essential in scripts where you need the exact hash, not a symbolic name."
                ),
                "xp": 15,
            },
            {
                "id": "gi_5",
                "type": "quiz",
                "question": "git gc (garbage collection) packs loose objects into packfiles. What triggers automatic garbage collection?",
                "options": [
                    "Every commit automatically triggers gc",
                    "gc runs when loose object count exceeds gc.auto threshold (default 6700)",
                    "gc only runs when manually invoked",
                    "gc runs on a daily cron schedule",
                ],
                "answer": "b",
                "lesson": (
                    "Git auto-gc triggers when the number of loose objects exceeds gc.auto\n"
                    "(default: 6700) or the number of packfiles exceeds gc.autoPackLimit (50).\n\n"
                    "What gc does:\n"
                    "  1. Packs loose objects into .git/objects/pack/*.pack files\n"
                    "  2. Removes unreachable objects older than gc.pruneExpire (2 weeks)\n"
                    "  3. Compresses packfiles using delta compression\n"
                    "  4. Removes stale reflog entries\n\n"
                    "Commands that trigger auto-gc: commit, merge, rebase, fetch.\n"
                    "Manual: git gc --auto (respects thresholds), git gc (always runs)."
                ),
                "xp": 20,
            },
            {
                "id": "gi_6",
                "type": "quiz",
                "question": "git fsck (file system check) reports dangling objects. What is a 'dangling commit'?",
                "options": [
                    "A commit with a corrupted hash",
                    "A commit not reachable from any branch, tag, or reflog entry",
                    "A commit whose parent has been deleted",
                    "A commit that references a missing blob",
                ],
                "answer": "b",
                "lesson": (
                    "A dangling object is one that exists in .git/objects/ but is not\n"
                    "reachable from any reference (branch, tag, reflog, stash).\n\n"
                    "Common causes of dangling commits:\n"
                    "  - Amended commits (the pre-amend version is now dangling)\n"
                    "  - Rebased commits (the pre-rebase versions dangle)\n"
                    "  - Reset --hard (commits after the reset point dangle)\n\n"
                    "Dangling objects are not lost — they exist until gc prunes them.\n"
                    "  git fsck --no-reflogs  finds objects only reachable via reflog\n"
                    "  git fsck --unreachable shows all unreachable objects\n\n"
                    "Recovery: git cherry-pick <dangling-hash> or git branch recover <hash>"
                ),
                "xp": 15,
            },
            {
                "id": "gi_7",
                "type": "text",
                "question": "What command shows the contents of a packfile, including object types, sizes, and delta chains?",
                "options": [],
                "answer": "git verify-pack -v",
                "lesson": (
                    "git verify-pack -v <packfile.idx> shows detailed packfile contents:\n"
                    "  SHA-1 type size size-in-pack offset [depth base-SHA-1]\n\n"
                    "Delta chains show how git compresses similar objects:\n"
                    "  - A base object is stored in full\n"
                    "  - Similar objects are stored as deltas (diffs) against the base\n"
                    "  - Depth indicates how many deltas deep (pack.depth, default 50)\n\n"
                    "Packfiles are how git achieves remarkable storage efficiency.\n"
                    "A repo with 10,000 similar files may compress to 1% of raw size.\n\n"
                    "Location: .git/objects/pack/*.pack (data) and *.idx (index)"
                ),
                "xp": 20,
            },
            {
                "id": "gi_boss",
                "type": "quiz",
                "question": "You accidentally ran git reset --hard HEAD~5 and lost 5 commits. The reflog still has them. What is the most direct way to recover?",
                "options": [
                    "git cherry-pick the 5 commits one by one from the reflog",
                    "git reset --hard HEAD@{1} to restore the branch to its previous position",
                    "git fsck --lost-found to dump dangling commits to .git/lost-found/",
                    "git gc --prune=now to force recovery",
                ],
                "answer": "b",
                "lesson": (
                    "HEAD@{1} refers to where HEAD was one move ago — which is exactly\n"
                    "where it was before the reset. So:\n"
                    "  git reset --hard HEAD@{1}\n"
                    "instantly restores the branch pointer to its previous position,\n"
                    "recovering all 5 'lost' commits.\n\n"
                    "The reflog records every HEAD movement:\n"
                    "  git reflog\n"
                    "  abc1234 HEAD@{0}: reset: moving to HEAD~5\n"
                    "  def5678 HEAD@{1}: commit: Added feature X   <-- this is what you want\n\n"
                    "This is why the reflog is called git's safety net.\n"
                    "It's also why gc.reflogExpire (90 days) matters for disaster recovery."
                ),
                "xp": 25,
            },
        ],
    },
    "advanced_workflows": {
        "id": "advanced_workflows",
        "name": "Advanced Workflows",
        "subtitle": "Trunk-Based, Gitflow, Monorepos & Hooks",
        "color": "blue",
        "icon": "\U0001f680",
        "commands": [
            "git hook",
            "git config core.hooksPath",
            "git merge --no-ff",
            "git tag -s",
        ],
        "challenges": [
            {
                "id": "aw_1",
                "type": "quiz",
                "question": "In trunk-based development, what is the maximum recommended lifetime of a feature branch?",
                "options": [
                    "1-2 days — merge to trunk frequently to minimize divergence",
                    "1-2 weeks — align with sprint cycles",
                    "Until the feature is complete, regardless of duration",
                    "Feature branches are never used — all commits go directly to trunk",
                ],
                "answer": "a",
                "lesson": (
                    "Trunk-based development (TBD) keeps branches short-lived (1-2 days max)\n"
                    "to minimize merge pain and integration risk.\n\n"
                    "Core principles:\n"
                    "  - trunk (main) is always releasable\n"
                    "  - Feature branches live at most 1-2 days\n"
                    "  - Feature flags hide incomplete work in production\n"
                    "  - CI runs on every push to trunk\n\n"
                    "TBD is used by Google, Meta, and most high-performing teams.\n"
                    "Long-lived branches are the #1 cause of painful merges and\n"
                    "integration failures."
                ),
                "xp": 15,
            },
            {
                "id": "aw_2",
                "type": "quiz",
                "question": "In Gitflow, which branch do hotfixes branch from and merge back into?",
                "options": [
                    "Branch from develop, merge to main",
                    "Branch from main, merge to both main AND develop",
                    "Branch from release, merge to main",
                    "Branch from main, merge to main only",
                ],
                "answer": "b",
                "lesson": (
                    "Gitflow hotfix workflow:\n"
                    "  1. Branch from main (production): git checkout -b hotfix/fix-crash main\n"
                    "  2. Fix the bug, commit\n"
                    "  3. Merge to main: the production fix goes live\n"
                    "  4. Merge to develop: the fix is included in future releases\n\n"
                    "If a release branch exists, merge to release instead of develop.\n\n"
                    "Gitflow branches:\n"
                    "  main     — production-ready code\n"
                    "  develop  — integration branch for next release\n"
                    "  feature/ — new features (branch from/merge to develop)\n"
                    "  release/ — release prep (branch from develop, merge to main + develop)\n"
                    "  hotfix/  — production fixes (branch from main, merge to main + develop)"
                ),
                "xp": 15,
            },
            {
                "id": "aw_3",
                "type": "text",
                "question": "What git config setting specifies a custom directory for git hooks (replacing .git/hooks/)?",
                "options": [],
                "answer": "core.hooksPath",
                "lesson": (
                    "git config core.hooksPath <path> redirects hook execution to a custom directory.\n\n"
                    "Default: .git/hooks/ (not tracked by git, local to each clone)\n"
                    "Custom: any directory, including one tracked in the repo.\n\n"
                    "Example: share hooks with your team:\n"
                    "  mkdir .githooks\n"
                    "  # add pre-commit, commit-msg hooks to .githooks/\n"
                    "  git config core.hooksPath .githooks\n\n"
                    "This is the modern way to enforce team-wide hooks without\n"
                    "requiring each developer to manually symlink into .git/hooks/.\n"
                    "Tools like Husky (JS) and pre-commit (Python) also solve this."
                ),
                "xp": 20,
            },
            {
                "id": "aw_4",
                "type": "quiz",
                "question": "A pre-commit hook exits with a non-zero status code. What happens?",
                "options": [
                    "The commit proceeds but a warning is logged",
                    "The commit is aborted entirely",
                    "The hook output is added to the commit message",
                    "Git retries the hook up to 3 times before aborting",
                ],
                "answer": "b",
                "lesson": (
                    "Git hooks follow Unix conventions:\n"
                    "  - Exit 0 = success, operation proceeds\n"
                    "  - Exit non-zero = failure, operation is aborted\n\n"
                    "Common pre-commit hook uses:\n"
                    "  - Lint code (eslint, flake8, rustfmt)\n"
                    "  - Run fast tests\n"
                    "  - Check for secrets (detect-secrets, gitleaks)\n"
                    "  - Enforce formatting (prettier, black)\n\n"
                    "To bypass a hook in emergencies: git commit --no-verify\n"
                    "(This skips pre-commit AND commit-msg hooks. Use sparingly.)"
                ),
                "xp": 10,
            },
            {
                "id": "aw_5",
                "type": "quiz",
                "question": "In a monorepo strategy, what is the primary purpose of CODEOWNERS files?",
                "options": [
                    "Define file-level build dependencies",
                    "Automatically assign reviewers based on which files are changed in a PR",
                    "Restrict which users can clone specific directories",
                    "Map files to CI pipeline stages",
                ],
                "answer": "b",
                "lesson": (
                    "CODEOWNERS maps file patterns to teams/users who must review changes:\n\n"
                    "  # .github/CODEOWNERS\n"
                    "  /src/auth/      @security-team\n"
                    "  /infra/         @platform-team\n"
                    "  *.sql           @dba-team\n"
                    "  /docs/          @docs-team\n\n"
                    "When a PR modifies matching files, the listed teams are\n"
                    "automatically added as required reviewers.\n\n"
                    "In monorepos with 50+ teams, CODEOWNERS is essential for:\n"
                    "  - Routing reviews to the right people\n"
                    "  - Preventing accidental changes to critical paths\n"
                    "  - Enforcing review requirements per directory"
                ),
                "xp": 15,
            },
            {
                "id": "aw_6",
                "type": "text",
                "question": "What hook runs after a commit message is entered but before the commit is finalized, allowing you to validate or modify the commit message?",
                "options": [],
                "answer": "commit-msg",
                "lesson": (
                    "The commit-msg hook receives the path to the commit message file\n"
                    "as its first argument. It can:\n"
                    "  - Validate the message format (e.g., require 'JIRA-123' prefix)\n"
                    "  - Modify the message (e.g., append ticket numbers)\n"
                    "  - Reject the commit (exit non-zero)\n\n"
                    "Hook execution order for git commit:\n"
                    "  1. pre-commit    — check staged changes\n"
                    "  2. prepare-commit-msg — set up the default message\n"
                    "  3. commit-msg    — validate/modify the final message\n"
                    "  4. post-commit   — notification (cannot abort)\n\n"
                    "Conventional Commits tools use commit-msg to enforce:\n"
                    "  feat: / fix: / chore: / docs: prefixes."
                ),
                "xp": 20,
            },
            {
                "id": "aw_7",
                "type": "quiz",
                "question": "Your monorepo has 500 microservices. You want CI to only build services whose files changed in a PR. What git command helps determine which files changed between the PR branch and main?",
                "options": [
                    "git diff --name-only main...HEAD",
                    "git log --all --oneline",
                    "git status --porcelain",
                    "git ls-files --modified",
                ],
                "answer": "a",
                "lesson": (
                    "git diff --name-only main...HEAD lists files changed on the PR branch\n"
                    "since it diverged from main (the three-dot syntax is key).\n\n"
                    "Two-dot vs three-dot:\n"
                    "  main..HEAD   changes from main's tip to HEAD (includes main's new commits)\n"
                    "  main...HEAD  changes since the merge base (only the PR's changes)\n\n"
                    "CI pipeline pattern:\n"
                    "  1. CHANGED=$(git diff --name-only main...HEAD)\n"
                    "  2. Determine which service directories are affected\n"
                    "  3. Only build/test those services\n\n"
                    "Tools like Nx, Turborepo, and Bazel automate this with\n"
                    "dependency-aware 'affected' commands."
                ),
                "xp": 15,
            },
            {
                "id": "aw_boss",
                "type": "quiz",
                "question": "Your team adopts signed commits (git commit -S). A developer pushes an unsigned commit. The server-side pre-receive hook should reject it. What does the hook check?",
                "options": [
                    "Whether the commit message contains 'Signed-off-by'",
                    "Whether each pushed commit has a valid GPG/SSH signature verified by git verify-commit",
                    "Whether the .gitconfig has user.signingkey set",
                    "Whether the commit was made with --no-verify",
                ],
                "answer": "b",
                "lesson": (
                    "A pre-receive hook enforcing signed commits runs:\n"
                    "  git verify-commit <hash>\n"
                    "for each commit in the push. Non-zero exit = signature invalid or missing.\n\n"
                    "Signed commits use GPG or SSH keys:\n"
                    "  git config user.signingkey <key-id>\n"
                    "  git config commit.gpgsign true\n"
                    "  git commit -S -m 'signed commit'\n\n"
                    "Note: 'Signed-off-by' (git commit -s) is a DCO assertion, NOT a\n"
                    "cryptographic signature. It's just a trailer line in the message.\n"
                    "git commit -S (uppercase) is the actual GPG/SSH signature.\n\n"
                    "GitHub and GitLab can show 'Verified' badges on signed commits."
                ),
                "xp": 25,
            },
        ],
    },
}

ZONE_ORDER = [
    "rebase_history",
    "cherry_pick_bisect",
    "worktrees_submodules",
    "git_internals",
    "advanced_workflows",
]
