import json
import requests

def create_pull_request(project_name, repo_name, title, description, head_branch, base_branch, git_token):
    """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = f"https://github.com/api/v3/repos/{project_name}/{repo_name}/pulls"
    headers = {
        "Authorization": f"token {git_token}",
        "Content-Type": "application/json"
        }

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=payload)

    if not r.ok:
        f"Request Failed: {r.reason}"
    else:
        f"Request Succeed:{r.request}"



if __name__ == '__main__':
    
    create_pull_request(
    "<qian-deng>", # project_name
    "<pta-training>", # repo_name
    "Test", # title
    "New change", # description
    input("Please input the head_branch"), # head_branch
    "yibo/dev", # base_branch
    "<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>", # git_token
    )


