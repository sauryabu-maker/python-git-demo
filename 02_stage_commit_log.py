"""Practice staging, commits, and history inspection."""
from pathlib import Path
from common import run_git, require_repo

print("PRACTICE 2 — ADD, COMMIT, LOG")
require_repo()

demo = Path("git_python_demo.txt")
if not demo.exists():
    demo.write_text("Created by the Git Python practice script.\n", encoding="utf-8")
    print(f"Created {demo}. It is not committed automatically.")

run_git("status", "--short")
run_git("add", "--", str(demo))
run_git("status", "--short")
run_git("diff", "--staged")

answer = input("Commit this demo file now? Type yes to commit: ").strip().lower()
if answer == "yes":
    message = input("Commit message [Add Python Git demo file]: ").strip()
    if not message:
        message = "Add Python Git demo file"
    run_git("commit", "-m", message, check=True)
else:
    print("Skipped commit. The file remains staged.")

run_git("log", "--oneline", "--decorate", "-5")
run_git("show", "--stat", "HEAD")
run_git("ls-files")

print("""
Related commands:
  git add .                  stage changes in current directory
  git add filename.py        stage one file
  git commit -m "message"    create a commit
  git log --oneline --graph --decorate --all
  git show HEAD               inspect latest commit
  git ls-files                list tracked files

Use 'git add .' carefully: it may stage files you did not intend to commit.
""")
