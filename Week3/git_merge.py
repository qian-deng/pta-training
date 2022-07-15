import argparse
from base64 import encode
import subprocess
import logging
import sys

TEMP_BRANCH = "temp-merge"
CONFLICTING_FILES = "CONFLICTS"


def git_stash():
    # Save local changes before proceeding
    subprocess.run(["git", "stash"])


def git_unstash():
    # Save local changes before proceeding
    subprocess.run(["git", "stash", "pop"])


def get_conflicting_files():
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=U"], encoding="utf-8"
        ).strip()
        return set(output.splitlines())
    except subprocess.CalledProcessError:
        logging.error("Failed to get conflicting files")
        return None


def get_current_head():
    return subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        encoding="utf-8",
    ).strip()


def merge(commit_message, ref):
    try:
        subprocess.check_call(["git", "merge", "--no-ff", "-m", commit_message, ref])
        return True
    except subprocess.CalledProcessError:
        logging.error(f"Failed to merge {ref}")
        return False


def stage_all_files():
    subprocess.check_call(["git", "add", "--all", "--verbose"])


def commit(commit_message):
    try:
        subprocess.check_call(
            ["git", "commit", "--no-verify", "-a", "-m", commit_message]
        )
        return True
    except subprocess.CalledProcessError:
        logging.error("Failed to commit")
        return False


def get_status():
    try:
        return subprocess.check_output(["git", "status"], encoding="utf-8").strip()
    except subprocess.CalledProcessError:
        logging.error("Failed to get git status")
        return None


def merge_branch(base, head):
    # Save current head branch
    cur_head = get_current_head()
    logging.info(f"Current head is {cur_head}")
    git_stash()
    # Fetch both head and base branches
    subprocess.check_call(["git", "fetch", "origin", head, base])
    # Checkout head branch to a local temp branch
    subprocess.check_call(["git", "checkout", "-b", TEMP_BRANCH, head])
    # Merge base branch into the local temp branch
    commit_message = f"Merge {base} into {head}"
    if not merge(commit_message, base):
        file_content = (
            f"Conflicting files are: {', '.join(get_conflicting_files())}\n"
            "******************DETAILS******************\n"
            f"{get_status()}"
        )
        with open(CONFLICTING_FILES, "w") as conflict_file:
            conflict_file.write(file_content)
        logging.info(file_content)
    # Stage all changes and commit
    stage_all_files()
    commit(commit_message)
    logging.info(f"Merged {base} into {head}")
    # Reset to the head branch
    subprocess.run(["git", "checkout", cur_head])
    git_unstash()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge branches")
    parser.add_argument("branch", type=str, help="head branch")
    parser.add_argument("base", type=str, help="base branch")
    args = parser.parse_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info(f"Merging branch '{args.branch}' into '{args.base}'")
    merge_branch(
        base=args.base,
        head=args.branch,
    )
