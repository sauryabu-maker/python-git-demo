"""
git_essential_commands.py
=========================
Demonstrates ALL 10 commands from the "Essential commands to remember" table,
step by step, exactly the way a small team uses them:

    1.  git clone URL              Copy a remote repository
    2.  git branch                 List local branches
    3.  git switch branch-name     Switch branches
    4.  git diff                   Inspect unstaged changes
    5.  git add .                  Stage changes in the current directory
    6.  git commit -m "message"    Save staged changes
    7.  git log --oneline          View compact commit history
    8.  git push                   Upload local commits
    9.  git pull                   Fetch and integrate remote changes
    10. git merge branch-name      Merge another branch

HOW TO RUN (Windows):   py git_essential_commands.py
Requirement: Git installed (run  git --version  to check).

SAFE TO RUN: everything happens inside a folder called  git_demo_workspace  created
next to this file. Your real projects and global Git settings are never touched.
GitHub is replaced by a local "bare" repository, so no account or internet is needed.
(In real life, the URL would be  https://github.com/USERNAME/attendance-app.git )
"""

import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent / "git_demo_workspace"
STEP_NO = 0


# ----------------------------------------------------------------------------
# Small helper functions (so the Git steps below stay easy to read)
# ----------------------------------------------------------------------------
def git(args, cwd):
    """Run one git command, print it like a terminal, and show its output."""
    print(f"\n$ git {args}")
    env = dict(os.environ, GIT_EDITOR="true", GIT_TERMINAL_PROMPT="0")
    result = subprocess.run(["git"] + shlex.split(args), cwd=cwd,
                            capture_output=True, text=True, env=env)
    output = (result.stdout + result.stderr).strip()
    if output:
        print(output)
    if result.returncode != 0:
        sys.exit(f"\nThis command failed (exit code {result.returncode}). Stopping.")
    return result


def write_file(folder, name, text, append=False):
    """Create or extend a file (same effect as  echo "..." > file  in a terminal)."""
    with open(Path(folder) / name, "a" if append else "w", encoding="utf-8") as f:
        f.write(text + "\n")


def step(command, purpose, explanation):
    """Print a clearly numbered heading before each command."""
    global STEP_NO
    STEP_NO += 1
    print("\n" + "=" * 72)
    print(f"STEP {STEP_NO}:  {command}")
    print(f"Purpose : {purpose}")
    print(f"Why     : {explanation}")
    print("=" * 72)


def set_identity(cwd, name, email):
    """Tell Git who is committing - for THIS repository only (not --global)."""
    git(f'config user.name "{name}"', cwd)
    git(f'config user.email "{email}"', cwd)


def reset_workspace():
    """Delete the previous demo (read-only .git files need chmod on Windows)."""
    def force_delete(func, path, _):
        os.chmod(path, 0o700)
        func(path)
    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE, onerror=force_delete)
    WORKSPACE.mkdir(parents=True)


# ----------------------------------------------------------------------------
# 0. Preparation: check Git, then create a pretend "GitHub" repository
# ----------------------------------------------------------------------------
try:
    version = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
except FileNotFoundError:
    sys.exit("Git is not installed (or not in PATH). Install Git, reopen the terminal, try again.")

print(f"Using {version}")
reset_workspace()

# The "remote" plays the role of GitHub. 'bare' means it only stores history (no files).
remote = WORKSPACE / "attendance-app.git"
remote.mkdir()
git("init --bare -b main", remote)

# Seed it with a first commit so there is something to clone (like a GitHub repo with a README).
seed = WORKSPACE / "_seed"
seed.mkdir()
git("init -b main", seed)
set_identity(seed, "Team Lead", "lead@example.com")
write_file(seed, "app.py", "print('Attendance App')")
git("add .", seed)
git('commit -m "Create attendance application"', seed)
git(f"remote add origin {remote.as_posix()}", seed)
git("push -u origin main", seed)

REMOTE_URL = remote.as_posix()   # stands in for https://github.com/USERNAME/attendance-app.git

# ----------------------------------------------------------------------------
# STEP 1 - git clone URL
# ----------------------------------------------------------------------------
step("git clone URL",
     "Copy a remote repository to your computer",
     "Downloads all files AND the full history, and links the copy to the remote as 'origin'.")
dev_a = WORKSPACE / "developerA"
git(f"clone {REMOTE_URL} developerA", WORKSPACE)
set_identity(dev_a, "Developer A", "a@example.com")
print("\nDeveloper A now has the project in:", dev_a)

# ----------------------------------------------------------------------------
# STEP 2 - git branch
# ----------------------------------------------------------------------------
step("git branch",
     "List local branches",
     "The * marks the branch you are on. 'git branch NAME' (with a name) creates a new branch.")
git("branch", dev_a)                       # only 'main' exists
git("branch login-feature", dev_a)         # create a branch for our new feature
git("branch", dev_a)                       # now two branches; we are still on main

# ----------------------------------------------------------------------------
# STEP 3 - git switch branch-name
# ----------------------------------------------------------------------------
step("git switch branch-name",
     "Switch branches",
     "Moves you onto another branch so your commits go there, leaving main untouched and stable.")
git("switch login-feature", dev_a)
git("branch", dev_a)                       # * has moved to login-feature

# ----------------------------------------------------------------------------
# STEP 4 - git diff
# ----------------------------------------------------------------------------
step("git diff",
     "Inspect unstaged changes",
     "Shows exactly which lines you changed but have NOT yet staged. Use it to review your work.")
write_file(dev_a, "app.py", "print('Student login')", append=True)   # change an existing file
write_file(dev_a, "login.py", "print('Login page')")                 # brand-new file
git("diff", dev_a)                         # shows the app.py change (new files appear after 'add')
print("\nNote: login.py is a NEW file, so git diff does not list it until it is staged.")

# ----------------------------------------------------------------------------
# STEP 5 - git add .
# ----------------------------------------------------------------------------
step("git add .",
     "Stage changes in the current directory",
     "Selects every changed/new file here to be part of the next commit. Nothing is saved yet.")
git("status --short", dev_a)               # before: files are modified/untracked
git("add .", dev_a)
git("status --short", dev_a)               # after: files are staged (green in a normal terminal)

# ----------------------------------------------------------------------------
# STEP 6 - git commit -m "message"
# ----------------------------------------------------------------------------
step('git commit -m "message"',
     "Save staged changes",
     "Creates a permanent snapshot in your LOCAL history. Write messages that say what changed.")
git('commit -m "Add student login feature"', dev_a)

# ----------------------------------------------------------------------------
# STEP 7 - git log --oneline
# ----------------------------------------------------------------------------
step("git log --oneline",
     "View compact commit history",
     "One line per commit: short ID + message. Newest first. 'HEAD ->' shows where you are.")
git("log --oneline", dev_a)

# ----------------------------------------------------------------------------
# STEP 8 - git push
# ----------------------------------------------------------------------------
step("git push",
     "Upload local commits",
     "Sends your commits to the remote (GitHub) so teammates can see them.")
print("\nFirst push of a NEW branch needs '-u origin <branch>' once. It links the local branch")
print("to the remote branch; after that, plain 'git push' is enough.")
git("push -u origin login-feature", dev_a)

# Prove the plain 'git push' works afterwards: make a small extra commit and push it.
write_file(dev_a, "login.py", "print('Password check')", append=True)
git("add .", dev_a)
git('commit -m "Add password check"', dev_a)
git("push", dev_a)                         # <- the plain command from the table

# ----------------------------------------------------------------------------
# STEP 9 - git pull
# ----------------------------------------------------------------------------
step("git pull",
     "Fetch and integrate remote changes",
     "Downloads new commits from the remote and merges them into your current branch.")
print("\nMeanwhile, Developer B (a teammate) pushes a new commit to main...")
dev_b = WORKSPACE / "developerB"
git(f"clone {REMOTE_URL} developerB", WORKSPACE)
set_identity(dev_b, "Developer B", "b@example.com")
write_file(dev_b, "report.py", "print('Attendance report')")
git("add .", dev_b)
git('commit -m "Add attendance report"', dev_b)
git("push", dev_b)

print("\nBack on Developer A's computer: switch to main and pull B's work.")
git("switch main", dev_a)
git("log --oneline", dev_a)                # A's main does not have B's commit yet
git("pull", dev_a)
git("log --oneline", dev_a)                # now it does

# ----------------------------------------------------------------------------
# STEP 10 - git merge branch-name
# ----------------------------------------------------------------------------
step("git merge branch-name",
     "Merge another branch",
     "Brings the commits of login-feature into the branch you are on (main).")
git("merge login-feature", dev_a)          # histories diverged, so Git creates a merge commit
git("log --oneline --graph", dev_a)        # picture of how the branches joined
git("push", dev_a)                         # share the merged main with the team
git("branch", dev_a)

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("DONE - all 10 essential commands were used:")
print("""
  git clone URL            copy a remote repository
  git branch               list local branches (or create one with a name)
  git switch branch-name   switch branches
  git diff                 inspect unstaged changes
  git add .                stage changes in the current directory
  git commit -m "message"  save staged changes
  git log --oneline        view compact commit history
  git push                 upload local commits
  git pull                 fetch and integrate remote changes
  git merge branch-name    merge another branch
""")
print(f"Explore the result in: {WORKSPACE}")
print("Open a terminal in git_demo_workspace\\developerA and try:  git log --oneline --graph --all")
print("=" * 72)
