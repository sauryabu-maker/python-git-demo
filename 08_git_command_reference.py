"""Printable quick reference for common Git commands."""
COMMANDS = {
    "Start and inspect": [
        "git --version",
        "git init",
        "git clone URL",
        "git status",
        "git status --short --branch",
    ],
    "Stage and commit": [
        "git add filename",
        "git add .",
        "git diff",
        "git diff --staged",
        'git commit -m "message"',
        "git log --oneline --graph --decorate --all",
        "git show HEAD",
        "git ls-files",
    ],
    "Branches and integration": [
        "git branch",
        "git branch feature",
        "git switch feature",
        "git switch -c feature",
        "git merge feature",
        "git rebase main  # understand before using on shared branches",
    ],
    "Remote collaboration": [
        "git remote -v",
        "git remote add origin URL",
        "git fetch origin",
        "git pull",
        "git push -u origin branch-name",
    ],
    "Undo and recovery": [
        "git restore --staged filename",
        "git restore filename  # discards unstaged edits",
        "git revert COMMIT_ID",
        "git reset --soft HEAD~1",
        "git reflog",
    ],
    "Temporary work and releases": [
        'git stash push -m "message"',
        "git stash list",
        "git stash pop",
        "git tag",
        'git tag -a v1.0 -m "Release 1.0"',
        "git describe --tags",
    ],
    "Inspection and maintenance": [
        "git config --list",
        'git grep "TODO"',
        "git blame filename",
        "git shortlog -sn --all",
        "git diff --stat",
        "git clean -n  # preview only",
    ],
    "File operations": [
        "git mv oldname newname",
        "git rm filename",
        "git rm --cached filename  # stop tracking but keep local file",
    ],
}

if __name__ == "__main__":
    for section, commands in COMMANDS.items():
        print(f"\n=== {section} ===")
        for command in commands:
            print("  " + command)
    print("""
Tip: Git commands run in the repository where Git Bash is currently located.
Use 'pwd' to see the current directory and 'git status' to check the repository.
""")
