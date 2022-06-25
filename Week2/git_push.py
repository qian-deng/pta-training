import argparse
import logging
import sys

import requests

OWNER_NAME = "qian-deng"
REPO_NAME = "pta-training"
BASE_BRANCH = "master"
GIT_TOKEN = "<TOKEN>"


def create_pull_request(title, description, head_branch):
    """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = f"https://api.github.com/repos/{OWNER_NAME}/{REPO_NAME}/pulls"
    headers = {
        "Authorization": f"token {GIT_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": BASE_BRANCH,
    }

    r = requests.post(git_pulls_api, headers=headers, json=payload)

    if not r.ok:
        logging.error(f"Request Failed: [{r.status_code}] {r.reason}, {r.text}")
        return
    logging.info(f"Request Succeed: new pull request url {r.json()['html_url']}")


if __name__ == "__main__":
    # Accept user input with input
    # head_branch = input("Please input the head_branch: ")
    # Bonus: accpet user input with argparser
    parser = argparse.ArgumentParser(description="Create a pull request")
    parser.add_argument("branch", type=str, help="head branch")
    parser.add_argument(
        "-t",
        "--title",
        default="Automatically created by git_push script",
        type=str,
        help="title",
    )
    parser.add_argument(
        "-d", "--description", default="Changes", type=str, help="description"
    )
    args = parser.parse_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info(
        f"Creating a pull request '{args.title}' from head branch:"
        f"{args.branch} with description {args.description}."
    )
    create_pull_request(
        title=args.title,
        description=args.description,
        head_branch=args.branch,
    )
