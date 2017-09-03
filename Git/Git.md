# Git
See also:

 - https://swcarpentry.github.io/git-novice
 - http://rogerdudler.github.io/git-guide/

## Setup
Set global configuration
```{bash}
git config --global user.name "John Doe"
git config --global user.email "mail@example.com"
git config --global color.ui "auto"
```
List all configured values
```{bash}
git config --list
```

## Creating a Repository
First we create a new directory, then we initialize it as a repository
```{bash}
mkdir paper
cd paper
git init
```
Verify that it is indeed a repository
```{bash}
git status
```

## Tracking Changes
Create a file called `article.md`
```{bash}
nano article.md
```
and enter the following text
```
# Report about some interesting findings
```
Verify that git noticed some changes with
```{bash}
git status
```
Add the changes to the staging area
```{bash}
git add article.md
```
Again check with
```{bash}
git status
```
Now commit the changes to the repository and provide a message
```{bash}
git commit -m "Start writing article about my findings"
```
Re-check `git status`.
Have a look in the log
```{bash}
git log
```
We will now introduce some changes. Open the file again with `nano article.md` and add a second line
```
## Introduction
```
Use `git status` again.
To see the introduced changes use
```{bash}
git diff
```
Add and commit the new content
```{bash}
git add article.md
git commit -m "Add introduction section"
```
Repeat the above steps as often as you want.
You can check your commits with `git log` at any time.

## Exploring History
Introduce some changes with `nano article.md` and do not add or commit them.
Explore your changes against the current and previous versions
```{bash}
git diff HEAD article.md
git diff HEAD~1 article.md
git diff HEAD~2 article.md
```
Explore all changes in comparison to a specific version, first find the hash sum for your desired commit using `git log` and then
```{bash}
git diff <hash-sum> article.md
# for example (this will probably not work for you)
git diff 373e6b6e9d86dab310b95642660e7b4c07054c1e article.md
# this can be shortened as long as the beginning of the hash sum is unique
git diff 373e6b6 article.md
```
Revert the changes you have not yet added or committed
```{bash}
git checkout HEAD article.md
# or just
git checkout -- article.md
```

## Ignoring things
Create some files you don't want to track
```{bash}
mkdir results
touch a.dat b.dat c.dat results/a.out results/b.out
```
Check `git status`
Ignore the files by creating a special file `nano .gitignore` with the content
```
*.dat
results/
```
Check again with `git status`.
Add `.gitignore` and commit your changes.

## Remote repositories
To work with remote repositories, e.g. on GitLab important commands are
```{bash}
# Clone a repository to your local machine
git clone https://fgoth@git.physik.uni-wuerzburg.de/SWC-06-2017/publicproject.git
# Get changes from the server
git pull
# Publish your local changes on the server
git push
```

