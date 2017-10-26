# A crash course in Linux and Vi(m)

The following information assumes that you are working in a bash shell environment, such as via running bash on Windows, or that you are working in a Linux/Unix environment on your own computer (such as on a Linux machine, or in Terminal/iTerm2/etc. under Mac OS X).

A brief mention of formatting is warranted.
When lengthy commands are given here they will often be included in a gray box, including the command prompt and in some cases the output.
At other times, commands will be given inline with the rest of the text in a special font like `this`, usually just when the commands are short.
Occasionally, quotes will be used to help items stand out from the text; these quotes are not intended to be typed.

What follows is a *very brief* intro to some absolute essentials on these topics.
Plenty more is available via Google.
See also the [bash cheatsheet](bash_cheatsheet.jpg) available here.

## What is Linux

Linux is just another way to interact with and manipulate files and run programs and commands. It works based on a command-line prompt and text commands that are typed into this prompt. Commands usually follow the format (command name) (things to act on) as will become clear below. Often, options can be specified as well, usually with a dash notation indicating what kind of option is being provided.

## Crucial Linux commands
Key operations include listing files and navigating between directories; moving, copying, deleting, and renaming files; making new directories (folders are called directories in Linux), listing what files are present, and copying files between computers, among other things.
Editing files is also important, and will be discussed in the context of the vi editor, below.

One major thing to know in the context of all of the commands below is that items not in the current directory can be accessed using the `/` notation to refer to the "path" (or location) of a particular file.
For example, if I am in my home directory which contains a directory "bananas" containing the file "potatoes.txt", I can refer to "bananas/potatoes.txt".

Another common feature is that many commands allow optional arguments to be specified that modify the behavior of the command.
See the `man` command discussed below for more information.

### Navigational and informational operations:

- To list the contents of a directory, use the `ls` command, which prints names of things (files, other directories, programs...) found there. For example, I might have:
```bash
[dmobley@mycomputer ~]$ ls
all_small_molecules	  	equil_nvt.0.log	projects
analyze_umbrella_mol.py 	gyrase		 	readxvg.py
asymmetry_erratum	  	ibuprofen	 	readxvg.pyc
```
This also accepts paths, such as `ls all_small_molecules` to list the contents of that directory.
A common additional option to ls is `-l` which provides a long list including file sizes and dates modified.

- To navigate between directories, use the `cd` (change dir) command, such as `cd all_small_molecules`. But what if you want to change to a directory that is NOT within the current directory, such as the directory you were in before you typed `cd all_small_molecules`? Linux provides a way to do that -- `..` means the parent directory, so `cd ..` tells Linux to take you back to the directory containing the one you are in.

- Sometimes, it is useful to orient yourself and find out where you are. `ls` helps you do this by looking at your surroundings, but even that isn’t enough always. `pwd` (print working directory) is another useful command that specifies exactly what set of folders you are in, all the way back to the base of the file system:
```bash
[dmobley@gplogin1 ~]$ pwd
/home/dmobley
```
This is saying that I am in the dmobley directory within the home directory. It turns out this is MY “home” directory, the name for a special directory that I automatically start off in every time I log in.

- Sometimes, documentation is essential. `man` is a manual command which accepts the name of another standard Linux command and provides usage information. For example, `man ls` will tell you all about how to use `ls` and what options it takes.

### File operations:

- Moving files: Moving files in Linux can really be renaming them, or putting them somewhere else, or both. The relevant command is `mv` and the basic format is `mv file1 directory1/file2` or variants of this. Here, file1 is moved to directory1 and renamed as file2.
- Copying files: This is the `cp` command in Linux, and the format is just the same as `mv` but the outcome is different -- a copy is made rather than moving the file. For example, `cp file1 directory1/file2` copies file1 to file2; note that directory 1 must already exist. Sometimes, one wants to copy a directory; in this case, the copy must be done recursively with the -r option: `cp -r directory2 directory3`. This will result in a copy of directory2 being placed within directory3.
- Deleting files is done via the `rm` command, i.e. `rm file1`. Again, directories must be removed recursively, such as `rm -r directory1`
- Making new directories is done via `mkdir`, such as `mkdir directory4` to make a new empty directory by that name.

### Useful shortcuts

Linux has loads of useful shortcuts. Learning as many of these will mostly be up to you, but here are a couple of my favorites:
- Use the tab key to autocomplete words. For example, if I am typing the command `mv plants.txt new_plants.txt` in a directory containing two text files, `plants.txt` and `pianos.txt`, I can type `mv pl` and then hit tab to get `mv plants.txt`, then type the rest of the command. This is especially useful for long file names involving directory names (paths).
- Use the up and down arrows to get back previous commands you typed -- for example, if you mistyped a command and need to change something and do it again, use the up arrow to get it back and then edit it
- When editing a line of text, use ctrl-e to go to the end of the line and ctrl-a to go to the beginning
- Many directories have shortcuts, such as `~` for your home directory, `.` for the current directory, `..` for the directory containing your current directory, `../..` for the directory containing THAT directory, and so on.
- Wildcards: Often, one might want to do something only to certain files. For example, I might have hundreds of files in a directory and want to see only files that end with the characters .txt. Wildcard characters provide an easy way to do this. The `*` character means "match any character," so `ls *.txt` will list all files beginning with any characters and ending with .txt in the present directory. Multiple wildcard characters are acceptable, so `ls directory*/b*.txt` will look in all directories with names beginning `directory` and list all text files beginning with the character b and ending with the letters `.txt`. Some other commands aside from ls accept wildcard characters as well.

### Other essentials
- Absolute versus relative paths: When a location of a file or directory is specified, if the location does not begin with a `/`, this means it is specified relative to your current directory (as printed by `pwd`). This is called a relative path, and they are tricky -- to use one, you have to know where you are. An absolute path is one that begins with a `/` -- it works regardless of where you are (where you’ve `cd`’d to) so in that sense they are preferable, though they do get much longer and more cumbersome and there are some special cases where relative paths are preferable. An example will help -- let’s say you tell a labmate to look on a shared computer in `bio/calculations`, a relative path. This assumes that they are going to be looking within the same directory you’re referring to -- a directory containing the `bio` subdirectory. That’s fine, but if you don’t tell them you’re assuming that, they may get back to you and ask, "There’s no `bio` directory!". So, it may be better to tell them, "Look in /home/dmobley/bio/calculations". This is an absolute path (begins with `/`) and will work without you having to explain where the bio directory is (since the path itself tells where it is). It is, however, more cumbersome, so you if you wanted to refer to other subdirectories of `bio`, you might switch back to relative paths: "Within that same `bio` subdirectory, you can find X in the `analysis` subdirectory."

### Your shell and environment

Linux’s command prompt environment is called a shell. It is actually possible to use different shells. While all of the basic commands are the same, some commands are different, and if you wanted to write a script to perform a complicated, repetitive series of commands, the way this would be written depends on the shell.

Another major factor in using Linux and the command prompt is your "environment" and your "environment variables". Think of this as an analogy to an office environment -- your environment is the stuff that's around you that you can easily use. It’s the same thing here. The environment specifies what programs and software you can use, and where they are found. This is usually specified in a particular file, in terms of a set of places Linux will look to find programs and commands. For bash this is in your home directory (~) as a hidden file, `.bash_profile`. (Any filename beginning with a period is by default hidden.) You shouldn’t need to do anything with it in this course except when instructed, but know that it exists, and again, if you find yourself using a different computer system and installing new software on it, you may need to think about editing your environment variables (the things in this file that actually specify where software is installed) to make them point to the software you need.
