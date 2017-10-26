# Why do we need all this computer stuff?

In this class, we plan to do some calculations.
I want you to have some understanding of how the techniques you’ve learned about actually work, and there is no substitute for actually using them.
But, for you to actually do anything with computational techniques, you need a bit more computer background than you pick up doing e-mail and browsing the web.

The first key ingredient we need is some Linux (basically, command-line or BASH) background.
Virtually all scientific computing takes place in the Linux environment (not Mac OS X or Windows, though both can be used to interface with it; Mac in particular is built on Linux foundations).
This environment provides a lot of power, but it takes a bit of getting used to.
You will often working with a command-line text prompt that asks you to enter what you want to do, rather than working with windows and drag-and-drop of files.
This means you need a bit of training.

Beyond being able to move and manipulate files and folders or "directories" in Linux, you need to be able to edit files, typically text files.
A key editor here is the program “vi” (also “vim”), which is a command-line text editor (though as noted, [Atom is a highly recommended alternative](https://github.com/MobleyLab/drug-computing/tree/master/uci-pharmsci#requirements) which is more modern).
Again, this won’t look like your typical word processor with drop down menus and so on. Rather, it relies on commands you type.
Thus, again, there’s some background to learn.

Finally, many of the tasks we do are extremely repetitive.
A molecular dynamics simulation, for example, consists of calculating the forces between the same atoms over and over again and, once each set of forces are calculated, moving the atoms a tiny amount and then repeating. Computers are great at doing these kinds of repetitive tasks, but we need to write instructions to tell them how to do it, which means a (simple) computer program.
Similarly, in the pharmaceutical industry, you might need to look through a database of a million compounds with a computational method to find the ones with a particular set of properties or shape that you are interested in.
Who wants to look through a million compounds?
A computer is great at this -- but you have to tell it what to look for.
So, most of the tasks we want to do throw us back at needing to write instructions to the computer, which means we need a bit of programming.
Here, we will use Python -- a programming language about as simple and natural as it can get.
It’s relatively easy to learn, but does have lots of real world applications outside this class.

Documents contained here give a bit of a crash course in Linux (or the `bash` shell, which these days now (finally) also runs on Windows), vi, and Python.
The class itself gives a crash course in Python, but if you need to pick up vi and Linux you’ll need to draw on this document and materials online.
You’ll get lots more chance to work with these (and some additional training in them) in the context of your assignments.

The very first step in getting started is to set up your computer via the [getting started](../getting_started.md) instructions.
