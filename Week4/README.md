# Week4 Content

## Git Blame

Annotates each line in the given file with information from the revision which last modified the line. It is the display of author metadata attached to specific committed lines in a file.

### Restrict the output within certain line range

`git blame -L [start],[end] [filename]`

```
(env) qiandeng@MacBook-Pro-2 Week4 % git blame -L 1,5 ../Week3/git_merge.py
9b8ccd8b (qian deng 2022-07-14 17:28:33 -0700 1) import argparse
9b8ccd8b (qian deng 2022-07-14 17:28:33 -0700 2) from base64 import encode
9b8ccd8b (qian deng 2022-07-14 17:28:33 -0700 3) import subprocess
9b8ccd8b (qian deng 2022-07-14 17:28:33 -0700 4) import logging
9b8ccd8b (qian deng 2022-07-14 17:28:33 -0700 5) import sys
```

### Ignore whitespace changes

`git blame -w [filename]`

### Track file content changes

`git log -S [content] -- [filename]`

```
(env) qiandeng@MacBook-Pro-2 Week4 % git log -S 'Homework' -- ../Week3/README.md
commit 5d27a8a94216037d28508e8b5c03271bb8a4bac6
Author: qian deng <dengqianwork@gmail.com>
Date:   Mon Jun 20 16:47:35 2022 -0700

    update week3 doc
```

## Regular Expression

A regular expression (or RE) specifies a set of strings that matches it.
`.` matches any character except a newline

`^` matches the start of the string

`$` matches the end of the string or just before the newline at the end of the string

`*` matches 0 or more repetitions of the preceding RE, as many repetitions as are possible, e.g. `ab*` matches `a`, `ab`, `abbb` and etc.

`+` matches 1 or more repetitions of the preceding RE, e.g. `ab+` matches `ab` but does not match `a`.

`?` matches 0 or 1 repetitions of the preceding RE, e.g. `ab?` matches either `a` or `ab`

`{m}` specifies that exactly m copies of the previous RE should be matched

`\` either escapes special characters or signals a special sequence

`[]` is used to indicate a set of characters, e.g. `[a-z]` matches any lowercase ASCII letter

`|` `A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.

`\b` matches the empty string, but only at the beginning or end of a word, e.g. `foo\b` matches `foo`, `foo bar` but not `foobar`

`\d` matches any Unicode decimal digit

`\s` matches Unicode whitespace characters

`\w` matches Unicode word characters

### re.match

If zero or more characters at **the beginning** of string match the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern.

### re.search

Scan through string looking for **the first location** where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern.

To practice and test RE, [regexr.com](https://regexr.com/) is very helpful

## Homework

Write a script to find conflicts in a file and print the authors who made the conflicts

- A file with conflicts `merge.txt` is provided
- Read the file line by line and record line numbers with conflict markers
- Use `git blame` to get the authors of lines with conflicts
- Print conflicting line numbers and related author names

## Readings

- [Git blame](https://git-scm.com/docs/git-blame)
- [Git log](https://git-scm.com/docs/git-log)
- [Python regular expression](https://docs.python.org/3/library/re.html)
