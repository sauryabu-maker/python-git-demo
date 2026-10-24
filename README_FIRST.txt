GIT BASH + PYTHON PRACTICE PACK
===============================

PURPOSE
-------
These Python files run real Git commands using Python's subprocess module.
Run them from Git Bash on Windows. They are designed for learning in a separate
practice repository, not for running in your Windows home folder.

IMPORTANT SAFETY RULE
--------------------
Do NOT initialize Git in /c/Users/SOURYA just for practice. That folder may
contain personal files. Use the dedicated folder below.

STEP 1 — CHECK INSTALLATION
---------------------------
Open Git Bash and run:
    git --version
    python --version

If "python" is not recognized, try:
    py --version
Then run scripts with:
    py 01_repository_status_diff.py

STEP 2 — CREATE A PRACTICE FOLDER
---------------------------------
In Git Bash:
    cd ~
    mkdir -p GitPracticePython
    cd GitPracticePython
    git init -b master

If your Git version does not support "git init -b master", use:
    git init
    git branch -M master

Create an initial file and commit:
    echo "# Git practice" > README.md
    git add README.md
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    git commit -m "Initial commit"

STEP 3 — EXTRACT THIS ZIP
-------------------------
Extract all .py files into:
    C:\Users\SOURYA\GitPracticePython
(or another folder you prefer)

Then in Git Bash, navigate there. Example:
    cd ~/GitPracticePython

The scripts expect the current directory to be a Git repository. They do not
create a repository automatically and they do not change to another folder.

STEP 4 — RUN THE SCRIPTS
------------------------
    python 01_repository_status_diff.py
    python 02_stage_commit_log.py
    python 03_branches_and_merge.py
    python 04_remote_workflow.py
    python 05_undo_and_recovery.py
    python 06_stash_tags_clean.py
    python 07_config_search_aliases.py
    python 08_git_command_reference.py

You can also right-click a .py file in PyCharm and choose Run, but set its
working directory to your GitPracticePython repository.

WHAT EACH FILE COVERS
---------------------
01_repository_status_diff.py:
  git --version, init (explained only), status, diff, diff --staged

02_stage_commit_log.py:
  add, commit, log, show, ls-files

03_branches_and_merge.py:
  branch, switch, checkout (legacy alternative), merge, merge conflicts overview

04_remote_workflow.py:
  remote -v, remote add, fetch, pull, push, clone (guided; asks before network actions)
  A GitHub URL and authentication are required for remote operations.

05_undo_and_recovery.py:
  restore, restore --staged, reset (explained), revert, reflog
  Potentially destructive examples are displayed but NOT automatically run.

06_stash_tags_clean.py:
  stash, tag, clean (clean is only displayed with a warning; not run)

07_config_search_aliases.py:
  config, show-ref, grep, blame, shortlog, describe, aliases

08_git_command_reference.py:
  A categorized quick reference for common commands.

CORE GIT COMMANDS COVERED
-------------------------
Repository: init, clone
State: status, diff, diff --staged, log, show, ls-files
Staging/history: add, commit, commit --amend (reference only)
Branches: branch, switch, checkout, merge, rebase (reference only)
Remote: remote, fetch, pull, push
Undo/recovery: restore, reset, revert, reflog
Temporary work: stash
Tags: tag, describe
Inspection/search: show-ref, grep, blame, shortlog
Configuration: config, alias
Cleanup: clean (warning only)
Other useful commands: mv, rm, diff --stat, log --oneline --graph --decorate --all

NOTE
----
Git has many more specialized commands; this pack covers common day-to-day
commands for beginners and junior software developer workflows. Review each
script before running it. Remote actions can affect a shared repository.
