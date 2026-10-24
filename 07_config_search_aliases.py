"""Read common configuration and repository inspection commands."""
from common import run_git, require_repo

print("PRACTICE 7 — CONFIG, SEARCH, ALIASES")
require_repo()

run_git("config", "--get", "user.name")
run_git("config", "--get", "user.email")
run_git("config", "--list", "--show-origin")
run_git("show-ref", "--heads")
run_git("shortlog", "-sn", "--all")
run_git("grep", "-n", "TODO", "--", "*.py")
run_git("log", "-1", "--format=%h %an %ad %s", "--date=short")

print("""
Useful commands:
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  git config --list
  git grep "TODO"             search tracked files
  git blame filename.py       show who last changed each line
  git shortlog -sn --all      summarize commits by author
  git describe --tags         describe current commit using nearby tag
  git show-ref --heads        list local branch refs

Example alias:
  git config --global alias.st "status --short --branch"
Then use:
  git st

Aliases are shortcuts; they do not create new Git functionality.
""")
