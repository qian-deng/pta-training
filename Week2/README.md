# Week2 Content

## Python Virtual Environment

Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories. Virtual environemtn can be isolated from system site directories.

### Install Python3 on Mac

- Install [homebrew](https://brew.sh/#install) (Mac package management tool)
- `brew install python`

### Use venv

venv is the build-in virtual environment support in Python3. It allows you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation.

#### Creating a virtual environment

`python3 -m venv env`

#### Activating a virtual environment

`source ./env/bin/activate`

when you run `which python`, it should return the path of Python interpreter localted in the `env`, e.g. `env/bin/python`.

#### Leaving the virtual environment

`deactivate`

### Use pip

pip is the reference Python package manager. It’s used to install and update packages.

#### Installing pip

Pip should be installed already with `python-pip` package.
Upgrade pip to the latest `python3 -m pip install --upgrade pip`.

#### Installing a package

`pip install requests`
To install a specific version `pip install reqeusts>=2.0.0,<3.0.0`

## Development Workflow

1. Sync with remote master, `git pull origin master`
2. Checkout to a new development branch, `git checkout -b [new-branch-name]`
3. Make chanages locally and commit the change, `git add` and then `git commit`
4. Push the change to remote, `git push origin [new-branch-name]`
5. Open a new pull request
6. Request code review, run tests and etc.
7. Merge

## Github Rest API

[Overview](https://docs.github.com/en/rest/pulls)

### Github pull request api

[Create a pull request](https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request)

```
curl -XPOST -H "Authorization: token <token>" https://api.github.com/repos/qian-deng/pta-training/pulls -d '{"title":"Amazing new feature","body":"Awesome changes!","head":"student/dev","base":"master"}'
```

## Homework

Write a script using Github pull request api to open a pull request.

### Prepartion

- Create [github developer access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### Requirements

- Accept a remote development branch name from user input
- Open a pull request using the provided branch as the head branch and `master` as the base branch
- Report any failures
- Print the generated Pull Request html url

Tips

- use input() to take input from stdin
- assume the remote branch exists
- use try/catch to report failures

#### Bonus

- Use [argparse](https://docs.python.org/3/library/argparse.html) to accept user input

## Readings

- [Homebrew Simple Installation Guide](https://treehouse.github.io/installation-guides/mac/homebrew)
- [Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments)
- [Github Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [Git Merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)
- [pip requirement.txt usage](https://note.nkmk.me/en/python-pip-install-requirements/)
