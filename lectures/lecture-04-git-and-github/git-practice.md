## This is how we will practice using git and github

### Basics

Let's create a directory, and a few (two) files in a directory:

```
mkdir "astr302-$USER"
cd "astr302-$USER"
echo "# My first ASTR 302 git repository" > README.md
echo "A file I do not whish to track" > AnotherFile.txt
```

I'll now create a git _repository_ where git will store snapshot of these files, using the `git init` command:

```
git init
```

Now git will be able to "track" (store snapshots of) files in your current directory. You have to run `git init` only once for that directory.

Running `git init` created a directory named `.git`, where the snapshots will be stored:

```
ls -l .git
```

If you want to send someone all of your snapshots, it's as easy as copying this directory (but there's a better way! more later!)

Some more bookkeeping before we begin. We need to tell git what our name and preferred e-mail are:

```
git config --global user.email “mjuric@astro.washington.edu”
git config --global user.name “Mario Juric"
```

Now we can begin! Git doesn't automatically snapshot the contents of everything in the directory -- you have to tell it what is the set of files I want it to snapshot. We do this using the `git add` command. For example:

```
git add README.md
```

Note that at this point, we didn’t take a snapshot yet. To do that, we use the `git commit` command:

```
git commit
```

We've just created a snapshot, which is referred to as a _commit_ in git. Running `git commit` opens an editor in which you can write your _commit message_. This is meant to be a short description of the set of files (or changes to files; we’ll show that in a minute). It should remind you what this snapshot is about (or tell others with whom you share this code) .

A convention for commit messages is to start with a short (\<70 characters) one-line description of the reason for the commit, followed by a blank line, followed by a longer paragraph (if needed). See [here](https://github.com/erlang/otp/wiki/writing-good-commit-messages) for an example of how to write useful commit messages.

At this point, git has stored a single commit:

```
git log
```

We can also check the status of the files in my directory
```
git status
```

Let’s now edit the README.md and check the status again:
```
echo "">> README.md
echo "We’re practicing git here." >> README.md

git status
```

Committing all these changes:
```
git commit -a

git log
```
The `-a` argument to `git commit` tells git to commit all files it's tracking and that have changed. Alternatively, you could've ran `git add` for every file individually, before running `git commit`. Note that `git add` serves two somewhat different purposes: it tells git which files to track, but it also tells git which files to include into the next commit (as an aside: these can be viewed as being one and the same...).

How to see the differences to a previous version:
```
git diff HEAD^
```

Git keeps a history of all commits. The top of this history is called the “HEAD”. Adding a ^ means “one before head”.

Let’s make more changes:
```
git add AnotherFile.txt
git commit
```

And a prettier log may be shown with:

```
git log --oneline
```

### Branches

Imagine you have your program/analysis working reasonably well. Now you want to make some changes, but are worried you’ll mess up your code if they don’t work out. One way to do it is to just copy the whole directory into a backup folder.

But git provides a facility — branches — to do it much more effectively. Creating a branch is like creating a parallel universe: what happens there won’t affect what’s in the “main” universe (called the _master branch_). You're free to experiment with your changes on a different branch, and then merge it back into _master_ once you're happy with the results.

Let's create and check out a branch named `new-feature`.

```
git branch

git branch new-feature
git branch

git checkout new-feature
git branch

\# A shorthand for create-and-checkout-a-branch is `git checkout -b new-feature`

```

Let’s make some edits:
```
echo "New edits" >> README.md
git status
git commit -a
```

See the history:
```
git log --oneline
git log --oneline --decorate
```
Note how individual commits are identified by their _commit id_, a 40-character unique checksum such as 9e130f7b1ff3bfdcf23702ee18da5b7cdc8b6ef4 (a so-called SHA1 hash).

We can switch back to the `master` branch
```
git checkout master
cat README.md
```

Note how there’s no change from the new-feature branch (as expected).

We can go ahead and also make some changes on master:
```
echo "Another tracked file" > AnotherFile.txt
git commit -a
```

Let's look at how all this looks like:
```
git log --oneline --decorate
git log --oneline --decorate --graph --all
```

Now we can bring the two sets of changes together: “merge” the two branches.

```
git merge new-feature
git log --oneline --decorate --graph --all
```

This is “branch & merge” technique is a powerful way to incrementally develop analyses or codes.

### Tagging, working with branches

Remembering a particular version — tagging:
```
git tag v1.0 bc54184ae2e8963eaad7c254f5b11c1153459ab0
git log --oneline --decorate --graph --all
```

Checking out a previous version:
```
git checkout v1.0
git checkout -b bugfix-1
```

Resetting master to a previous version:
```
git reset --hard v1.0
```

### Github

How do we effectivelly share the repositories? This is where github comes in.

* Let’s make sure you all have accounts on github. Create a new repository, and then:

```
git remote add origin git@github.com:mjuric/astr302-mjuric.git
git push -u origin master
```

(where you should replace the URL (the web address) in the first line with the one for your repository. Note that GitHub will give you an address starting with `https://` by default -- unless you've set up SSH keys, use that one.

The second command _copies_ all the commits stored on your local hard drive (the `.git` repository) to GitHub. Now refresh the page on github and see what it lets you do!

You can consider the copy on github as your 'backup copy'. Even if you lose your entire computer, the commits of your files are safe and sound on github.

As you make new changes and new commits, don't forget to occasionally push them to GitHub:
```
git push
```
Note that you don't have to specify `origin master` as your destination, as `-u` made git remember it.

### Collaboration with github

Github is excellent at collaboratively working on software w/o stepping over each other’s toes. It has a very different philosophy compare to (e.g.) Google docs. There, you edit in real time, together with everyone else. With git, you make a _clone_ of the repository you wish to edit, make your changes, and suggest to the original author that they should merge those changes by making a “Pull Request”. That allows one to have more control and review over what changes are accepted.

* Let's practice:
  - Please pair up.
  - Open an issue in your partner's repository, reporting that README.md is poorly formatted
  - Partner: Reply to the issue by politely agreeing it’s a good idea, and asking the reporter to send a pull request ("send a PR").
  - Contributor: Fork the repository by clicking the fork button on github. This will create a _clone_ of your partner's repository in your own GitHub account. This clone contains a copy of everything in the original (usually referred to as 'upstream') repository. GitHub also remembers where you forked the repository from.
  - Next, clone your clone to your computer:
  ```
      git clone https://github.com/mjuric/astr302-mjuric
  ```
  This will now copy the repository from github to your own computer, where you can freely edit it.
  - Make the edits -- edit README.md to add newlines between each sentence.
  - Next, commit those changes:
  ```
      git commit -a
  ```
  - These changes have now been committed locally (into the `.git` directory, if you want to know the specifics). Push them back to github:
  ```
      git push
  ```
  - On GitHub, create a pull request.
  - Partner: Accept a pull request.

### Syncing with Upstream

  * When you pushed the ‘fork’ button on github, the result was a full-fledged, but independent, clone of the original repository. If the original repository changes, you don’t get those changes by default. That way you can independently work on your own copy w/o worrying that someone will change things underneath you.
  * The issue is what to do when you *do* want changes from the upstream repository. That’s easy — use git’s capability to merge new changes from the upstream repository.

  * First, tell git about the upstream repository:

    git remote add upstream git@github.com:mjuric/astr302-mjuric

    You have to do this only once!

  * Now, say:

      git pull upstream master

    And this will fetch upstream changes.

    Now we can push it back:

      git push

    and view the changes on github.

  * For more information:
    - https://help.github.com/articles/configuring-a-remote-for-a-fork/
    - https://help.github.com/articles/syncing-a-fork/

### Merge conflicts
  - Another common occurrence are merge conflicts. This is when there are conflicting changes in two branches.

To practice this, let’s have everyone clone my repo:
  * clone my repository
  * edit README.md
  * commit it.
  * Now I’ll edit the file as well
  * Once I do it, try to run a `git pull`.
