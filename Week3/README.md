# Week3 Content

## What is merge conflict

If Developer A tries to edit code that Developer B is editing a conflict may occur.
Conflicts generally arise when two people have changed the same lines in a file, or if one developer deleted a file while another developer was modifying it. In these cases, Git cannot automatically determine what is correct.

## When merge conflict can happen

### With local changes in workspace or staging area

Git fails to start the merge because these pending changes could be written over by the commits that are being merged in.

#### Use `git stash`

Temporarily shelve (or stash) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on.

##### Stashing your work

`git stash` takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.

##### Re-applying your stashed changes

`git stash pop` or `git stash apply` reapply previously stashed changes.
`pop` removes the changes from your stash, while `apply` keep them in your stash.

##### Stashing untracked/ignored files

`-u`(`--include-untracked`) stashes untracked file.
`-a`(`--all`) stashes both untacked and ignored files.

### With current local branch

Indicate conflict between the current local branch and the branch being merged.

### How to identify merge conflicts

`git status` returns unmerged path due to conflicts.

```
On branch demo-conflict
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both added:      Week3/demo_conflict.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

### Conflict markers

```
<<<<<<< HEAD
This is to demo how to create conflicts.
=======
This is also to demo how to create conflicts.
>>>>>>> create-merge-conflict-2
```

The `=======` line is the "center" of the conflict. All the content between the center and the `<<<<<<<` HEAD line is content that exists in the current branch. Alternatively all content between the center and `>>>>>>>` _create-merge-conflict-2_ is content that is present in the merging branch.

## Homework

Write a script to merge one branch into another. Identify conflicts if exist and print conflict details.

- Accept testing branch and merge branch from user input
- Check out to a temp branch from the testing branch
- Merge merge branch into the temp branch
- If there are conflicts, output conflict details
- If no merge conflicts, output "Merge succeeded!"

Tips

- Use [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run) to call git commands, e.g. `git checkout`, `git merge`
- You need to read conflicted file name from the returned `CompletedProcess.stderr` ([CompletedProcess](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess)) instacne from `subprocess.run`
- Use [with open("filename")](https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/) to read a file line by line
- You can use string match to find lines with conflict markers

Bonus

- Use regex to find lines with conflict markers

## Readings

- [git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)
- [merge conflict](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [python regular expression](https://docs.python.org/3/library/re.html)
