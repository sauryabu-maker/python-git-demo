"""Inspect safe undo/recovery commands; destructive operations are not run."""
from common import run_git, require_repo

print("PRACTICE 5 — UNDO AND RECOVERY")
require_repo()
run_git("status")
run_git("log", "--oneline", "-5")
run_git("reflog", "-5")

print("""
Choose the command that matches what you want to undo. Examples are shown only;
this script does not execute them automatically.

1) Unstage a file but keep its edits:
     git restore --staged filename.py

2) Discard unstaged edits to a tracked file (DESTRUCTIVE):
     git restore filename.py

3) Create a new commit that reverses an earlier commit (usually safer for shared history):
     git revert COMMIT_ID

4) Move the current branch pointer (can lose reachable work if used incorrectly):
     git reset --soft HEAD~1
     git reset --mixed HEAD~1
     git reset --hard HEAD~1    # DESTRUCTIVE: discards working-tree changes

5) Recover/inspect recent branch movements:
     git reflog

6) Amend the most recent commit (changes commit history):
     git commit --amend

Before using restore/reset/clean, inspect:
     git status
     git diff
     git diff --staged

Do not copy a destructive command unless you understand exactly what it changes.
""")
