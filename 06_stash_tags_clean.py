"""Practice stash and tags; git clean is displayed but never run."""
from common import run_git, require_repo

print("PRACTICE 6 — STASH, TAGS, CLEAN")
require_repo()
run_git("status")
run_git("stash", "list")
run_git("tag", "--list")
run_git("log", "--oneline", "--decorate", "-5")

print("""
Stash examples:
  git stash push -m "work in progress"
  git stash list
  git stash show -p stash@{0}
  git stash apply stash@{0}   apply but keep the stash
  git stash pop               apply and remove the stash if successful

Tag examples:
  git tag                     list tags
  git tag v1.0                create a lightweight tag at current commit
  git tag -a v1.0 -m "Release 1.0"  annotated tag
  git show v1.0               inspect tag
  git push origin v1.0        publish a tag
  git push origin --tags      publish all tags

Cleanup warning:
  git clean -n                preview untracked files that would be removed
  git clean -fd               removes untracked files/directories (DESTRUCTIVE)

This script intentionally does NOT run git clean, stash pop, or create tags.
""")
