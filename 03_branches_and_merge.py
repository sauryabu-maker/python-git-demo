"""Practice branches and a safe local merge."""
from pathlib import Path
from common import run_git, require_repo

print("PRACTICE 3 — BRANCHES AND MERGE")
require_repo()

run_git("branch", "--show-current")
run_git("branch", "-vv")
run_git("log", "--oneline", "--decorate", "-5")

current = run_git("branch", "--show-current")
branch_name = "python-feature-demo"

check = run_git("show-ref", "--verify", "--quiet", f"refs/heads/{branch_name}")
if check.returncode == 0:
    print(f"Branch '{branch_name}' already exists; switching to it.")
    run_git("switch", branch_name, check=True)
else:
    run_git("switch", "-c", branch_name, check=True)

demo = Path("feature_demo.txt")
demo.write_text("This file was created on python-feature-demo.\n", encoding="utf-8")
run_git("add", "--", str(demo))
run_git("commit", "-m", "Add feature demo file", check=True)
run_git("switch", current.stdout.strip() if current.returncode == 0 else "master", check=True)

print("\nThe feature branch has one new commit. Merge it into the branch you returned to?")
answer = input("Type yes to merge: ").strip().lower()
if answer == "yes":
    run_git("merge", "--no-edit", branch_name, check=True)
else:
    print("Skipped merge. The feature branch remains available.")

run_git("branch", "-vv")
run_git("log", "--oneline", "--graph", "--decorate", "--all", "-10")

print("""
Branch commands:
  git branch                    list local branches
  git branch feature            create a branch
  git switch feature            switch branches
  git switch -c feature          create and switch
  git checkout feature           older alternative to switch
  git merge feature              merge feature into current branch
  git branch -d feature          delete a merged local branch

If you already have uncommitted changes, commit or safely stash them before
switching/merging. Resolve merge conflicts manually, then git add the resolved
files and complete the merge commit if Git requests it.
""")
