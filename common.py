"""Shared helpers for the Git Bash Python practice files."""
import subprocess
import sys


def run_git(*args, check=False):
    """Run a Git command and print its output. Returns the CompletedProcess."""
    command = ["git", *args]
    print("\n$ " + " ".join(command))
    try:
        result = subprocess.run(
            command, text=True, capture_output=True, check=False
        )
    except FileNotFoundError:
        print("ERROR: Git was not found. Install Git for Windows and reopen Git Bash.")
        sys.exit(1)

    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n",
              file=sys.stderr)
    if check and result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}.")
    return result


def require_repo():
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        text=True, capture_output=True
    )
    if result.returncode != 0:
        print("ERROR: This folder is not inside a Git repository.")
        print("In Git Bash, cd to your practice repository and try again.")
        sys.exit(1)
