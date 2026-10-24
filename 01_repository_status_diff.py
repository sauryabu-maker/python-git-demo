"""Practice Git repository status and differences."""
from common import run_git, require_repo

print("PRACTICE 1 — REPOSITORY STATUS AND DIFF")
require_repo()

run_git("--version")
run_git("status", "--short", "--branch")
run_git("status")
run_git("diff")
run_git("diff", "--stat")
run_git("diff", "--staged")

print("""
Try this in Git Bash:
  echo "A new line" >> README.md
  git status
  git diff
Then run this Python file again.

Concepts:
- git status: shows changed, staged, and untracked files.
- git diff: shows unstaged changes.
- git diff --staged: shows changes already staged for commit.
- git init: creates a repository; it is intentionally not run here.
""")
