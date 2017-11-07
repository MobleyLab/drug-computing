# A crash course in Vi(m)

This provides a brief introduction to a standard, powerful Linux text editor often called vi (but which typically really refers to vim).
See also the [vi cheatsheet](vi_cheatsheet.pdf) provided here.

## Using Vi to edit text -- the basics

Vi is an incredibly powerful command-line text editor.
However, since it works from the command-line, it isn’t menu driven like most Word processing or text editor programs you are used to.
This, combined with its power, can make it a little bit tricky to get started on.
But it's extremely helpful for scientific computing; while you may want to use more user-friendly text editors on your own computer (such as Atom), if you get deeply into computation you will likely end up using some remote computers/computer clusters where you will want a quick editor to just change a file or two and you can be certain vi/vim will be installed.

Here, I provide some of the absolute essentials, but I also recommend going through a tutorial if you use it regularly.
Lots more info is available via Google. And, know that vi (or its slightly more advanced colleague `vim`, which usually is what you end up using when you run the vi command), is quite an advanced text editor (as addressed by this "Why Use Vi" column: http://www.viemu.com/a-why-vi-vim.html), so if you’re after a powerful text editor, this is a good one to learn.

So, what are the essentials? First, how to open vi -- simply type `vi` from the Linux command prompt, or, to edit a specific file with it, “vi myfile.txt”, for example. If the myfile.txt file exists, it will be opened in vi; if it does not, it will be created.

Once in vi, you will typically see a terminal screen with the contents (or partial contents) of your file in it, and a single line at the bottom listing the name of your file.
You can navigate this file using the arrow keys or a variety of different keyboard commands.
If the file is empty or mostly empty, you may also see a lot of `~` characters denoting empty lines.

It’s important to know that vi has two primary working modes, "command mode" and an "edit mode" which actually comes in several different flavors, the most common of which is "insert mode", for inserting new text or deleting old text.
Depending on which mode you are in, what you type will get different behaviors.
In command mode, for example, characters you type are understood to be commands (things like "copy this line" and "paste what I copied here" or "delete that line" and so on).
In insert mode, most of what you type is understood as characters to insert or delete -- that is, what you normally expect when you type into a text file.

One of the most important things to know, then, is how to switch between these modes.
When you open a file, you begin in command mode, so if you want to start typing into the file, switch to insert mode using the command `i`.
You should notice that now the text at the bottom of your window should say `---INSERT---` indicating that you are in the insert mode.
Type whatever you want, using the delete keys as normal to delete things you don’t want, etc. Then, when you are done editing, use the escape key to go back to command mode.

That’s fine, but what if you want to save your work? Or exit? No menus are apparent, but it turns out saving is done with a command from command mode. Specifically, in command mode (which you enter by typing escape), type `:w` -- yes, a colon followed by a w. Then hit enter, and your work gets saved. You should see a message to this effect at the bottom. What about quitting? `:q`. However, vi won’t let you quit without saving unless you tell it you really mean it, so to quit with unsaved work, `:q!`. Or, if you want to save and quit at the same time, `:wq`.

Those are the absolute basics of vi, but it is a powerful text editor. For example, it can easily indent blocks of computer code, perform powerful search and replace operations, repeat previous commands to prevent repetitive typing, and all kinds of other things. If you find yourself doing some repetitive editing task, odds are vi can help you do it much faster. Tons of help is available online with Google.

One other feature that is incredibly useful is that vi understands programming languages such as Python, which we’ll be working on in this class, and it is able to actually highlight the syntax, helping to make your code more legible, showing you where you have ended parentheses, and so on. You DO have to be using an ssh or Terminal program which supports color for this to work, but most of the recommended options above should meet these criteria. (It also has to be turned on).

## Setting some recommended options for vi

By default, vi doesn't do that much with your files which is exciting/helpful, but there are some simple options I recommend turning on. If you are a previous user of `vi`, don't worry about doing the following, but if you are NOT, I suggest you go ahead and copy the provided `.vimrc` from this directory to your home directory (e.g. `cp .vimrc ~/.vimrc`); it has some settings to turn on auto-indentation of python code, syntax highlighting, conversion of tabs to spaces, etc.
The tab/space issue is especially helpful when writing Python code (which relies heavily on indentation) if you ever use the tab key, as otherwise you will end up indenting some lines with spaces and other lines with tabs, which can cause Python to have problems in some circumstances (and also cause problems for anyone else reading your files who has vi set to display tabs differently than you). Short version: Turn this on, and you can use tab OR space to indent your code, and vi and Python will both properly understand your indentation. 
