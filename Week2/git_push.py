from git import Repo
import os


dirfile = os.path.abspath('git_push.py')
repo = Repo(dirfile)
g = repo.git

while True:
    try:
        g.push()
    except Exception as e:
        print(e)
    else:
        print("Successful push!")
        break
