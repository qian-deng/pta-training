import requests


def create_pull_request(owner_name, repo_name, title, description, head_branch, base_branch, git_token):
    """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = f"https://api.github.com/repos/{owner_name}/{repo_name}/pulls"
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
        json=payload)

    if not r.ok:
        print(f"Request Failed: {r.status_code} {r.reason}, {r.text}")
        return
    print(f"Request Succeed: new pull request url {r.json()['html_url']}")



if __name__ == '__main__':
    head_branch = input("Please input the head_branch: ")
    create_pull_request(
        "qian-deng", # owner_name
        "pta-training", # repo_name
        "Test", # title
        "New change", # description
        head_branch, # head_branch
        "yibo/dev", # base_branch
        "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", # git_token
    )


