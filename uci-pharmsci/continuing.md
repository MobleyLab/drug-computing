# Tips for continuing work in the course

After having followed `getting-started.md`, there will still be some things to know going forward.

## Working with git and github

I will typically make some updates (fixes, improvements, etc.) to course materials as the course progresses and push these to the course GitHub site.

In the [getting started materials](getting-started.md) I recommended getting a copy of the GitHub repository by using `git clone`, which is really the best way of doing it. This information will assume you've done things that way, but see below if you've instead downloaded a zip file of the GitHub repository

When I make updates, you will want to go to the directory where you have the github contents and download updates using this command:
`git pull origin master`
which tells git to obtain (pull) the latest updates from the main (master) location on GitHub.

**However**, if you have been making modifications to Jupyter notebooks (e.g. trying them out in classs!) on your computer and I've changed the same notebooks, this procedure will not work - git will warn you that this would overwrite your local changes and it won't let you proceed.
The easiest thing to do (if you're not used to git) is just to rename your copies of the notebook(s) in question, then repeat the command.

Usually this also means that anytime you want to make extensive changes to code or a notebook (such as if you are doing homework assignments) you should be sure to make a copy of the original notebook and work on that, rather than just working on the notebook itself. That way if I change something and you want to pull down updates to the file I changed, you'll already have things set up for it to work without conflicting with your edits.
(If we had more time I'd teach you how to use git to manage these issues, but that's outside the scope of this class.)
