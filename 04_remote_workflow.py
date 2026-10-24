"""Guided remote commands. Network-changing actions require confirmation."""
from common import run_git, require_repo

print("PRACTICE 4 — REMOTE WORKFLOW")
require_repo()
run_git("remote", "-v")

print("""
Remote concepts:
  git remote add origin URL   connect this local repository to a remote
  git fetch origin            download remote refs/objects, without merging
  git pull                    fetch and integrate changes
  git push -u origin master   publish the local master branch
  git clone URL               create a new local copy of a remote repository

Do not use a placeholder URL. Create a repository on GitHub first if needed.
""")

url = input("Optional GitHub repository URL (press Enter to skip): ").strip()
if url:
    remotes = run_git("remote").stdout.split()
    if "origin" not in remotes:
        if input("Add this URL as remote 'origin'? Type yes: ").strip().lower() == "yes":
            run_git("remote", "add", "origin", url, check=True)
    else:
        print("Remote 'origin' already exists. Current remote details:")
        run_git("remote", "-v")

    run_git("remote", "-v")
    action = input("Choose fetch, pull, push, or skip: ").strip().lower()
    if action in {"fetch", "pull", "push"}:
        print(f"About to run: git {action} origin")
        if action == "push":
            branch = run_git("branch", "--show-current").stdout.strip()
            print(f"This may publish branch '{branch}' to the shared remote.")
            if input("Proceed with push? Type yes: ").strip().lower() != "yes":
                print("Push cancelled.")
                raise SystemExit(0)
            run_git("push", "-u", "origin", branch, check=True)
        elif action == "fetch":
            if input("Fetch remote changes? Type yes: ").strip().lower() == "yes":
                run_git("fetch", "origin", check=True)
        else:
            if input("Pull changes into your current branch? Type yes: ").strip().lower() == "yes":
                run_git("pull", check=True)
    elif action != "skip":
        print("Unrecognized choice; no remote operation performed.")

print("""
To clone another repository, run this separately in the parent folder:
  git clone https://github.com/OWNER/REPOSITORY.git

Authentication is handled by your Git credential manager / configured SSH key.
Never put passwords or personal access tokens directly in Python source code.
""")
