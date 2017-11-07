# A First Crash Course in Python

Here, I aim to provide some absolute essentials on Python to supplement the Jupyter notebook material also provided here. You will, however, certainly need to do additional reading, so I provide some additional references as well.

## Additional resources

One useful reference is the [Non-Programmer’s Tutorial for Python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3), which some of my students have found useful.
It is written geared towards someone who has done no programming before, and does not provide a complete overview of the language.
Another good source is [Python 3 Object Oriented Programming - Second Edition](https://www.amazon.com/dp/1784398780/ref=cm_sw_r_cp_api_7o79zbP8G8WYY) by Dusty Phillips

The Python introduction Jupyter notebooks also provided in this directory (from M. Scott Shell) are more appropriate for people who have at least some background in programming.
These notebooks provide a lot of examples and give a much more complete introduction to the language than this materia.

## Introduction to programming and Python

Programs are a sequence of instructions to the computer (really, a "compiler" or "interpreter") that run from top to bottom.

All programming languages, including Python, have certain basic features.
These include: decisions or loops, which have the ability apply conditions (if x, do y) or loop over a sequence while a condition is met (while x is true, do z; for every member of q, do w).
Data structures store information -- for example, numerical information (integers or floats (decimal numbers)), text (also known as strings), or (at least in Python) generic information stored in a sequence (in lists) or by keys (in dictionaries).
Variables are names used to access a particular instance of a data structure. For example, `x=32` stores the value 32 in the variable x.
Programs also have commands -- things that do stuff, such as `x+y` or `print(x)` and so on.

In Python, punctuation and formatting can be crucial to meaning.
Your set of instructions simply won’t work if it’s missing a close parenthesis after an open parenthesis, or missing a colon where there needs to be one, and so on. Also, spacing can be key -- in Python, it is used to indicate pieces of the program which are subordinate to or controlled by other pieces, as we will see.

There are two (or three, depending on how you count) main ways to interact with Python, which itself is a program you can access from the command-line or in other ways.
The first is to actually type the word `python` or `ipython` (the latter being an improved python interpreter called interactive python) on the command prompt and access the interactive "interpreter" and type Python commands in to it.
This is the best for learning Python, but the downside is that you aren’t saving what you’re doing so you can reuse it later.
The second main way to interact with Python is to type things you would have typed into the interpreter into a separate text file with a filename ending with `.py` and store them.
Then, this file itself can be run through python from the command line.
This provides a powerful way to store commands to reuse or edit, and to build up complicated programs you couldn’t easily type in all at once or which you might want to modify later.
You can also access the Python interpreter via other formats such as Jupyter notebooks, for example; Jupyter notebooks provide somewhat of a hybrid of the above two approaches in that they allow interactive use AND storing of files for reuse, though they do not themselves comprise tools which are independently useful.

For the purposes of this writeup, we will assume you have opened python by typing `python` or `ipython` at the command prompt to open the interactive interpreter, though much of our discussion here will also apply to Jupter notebooks with minimal adaptation.

## Getting going in Python and data structures

Start your Python experience by typing `python` on the command line:
```
>>>This is the python interpeter waiting for you to type something. Let’s do a very simple program:
>>> x = 'Hello World'
>>> print(x)
Hello World
```
Here, anything following `>>>` is something YOU type, and anything not after those characters is something Python prints out.
Here, `'Hello World'` is a Python string, a data structure that can store a sequence of any kind of characters (including special characters, such as tabs (`\t`) and the newline or carriage return character (`\n`)).
Strings can use single or double quotes, e.g. `"Hello World"` or `'Hello World'`.
Here, we create a new variable or object `x` by assigning it to store the string we defined.
Then, we use the print command to print the contents of `x`.
As noted, there are many different data structures or types available in Python.
We just saw strings.
Integers are a common one used for storing whole numbers:
```
>>> y=12
>>> y/4
3
```

However, we also often need numbers which have decimal places.
In Python these are called floating point numbers or "floats", and the difference between integers and floats is handled automatically:
```
>>> z = 12.
>>> z/5
2.4
>>> print(z/5)
2.4
```

Conversion between types is done using the name of the target type.
It is not needed very often, but occasionally -- most often when converting between things that are significantly different in type, such a a string and an integer:
```
>> z
12.0
>>> int(z)
12
>>> y = "2"
>>> int(y)
2
```

Python also handles special data types called "Boolean" data, which have two values, either `True` or `False`.
(These are not in quotes as they are not strings -- Python recognizes these as special keywords).


Lists are generic Python data structures that can contain pretty much anything.
They are defined using square brackets, and items can be added to lists by appending them:
```
>>> a=[]
>>> a.append(1)
>>> a.append('test')
>>> a.append(1.43)
>>> print(a)
[1, 'test', 1.43]
>>> b = [0,2,'another list', 'final entry']
>>> print(b)
[0, 2, 'another list', 'final entry']
>>> c=a+b
>>> c
[1, 'test', 1.43, 0, 2, 'another list', 'final entry']
```

The above code creates an empty list named a, and adds the items `1`, `test`, and `1.43` to the list by appending them (adding them at the end), then prints it.
It then creates a second list with some strings in it, prints it, and creates a third list out of a combination of `a` and `b`.

It’s worth noting at this point that common operations, such as `+`, have different meanings in Python depending on what type of data they are operating on.
`1+2` has the common mathematical meaning, but adding two strings together means something different, and adding two lists together means something else entirely.
Adding a string and a number together will result in an error, as Python doesn’t know what you intend in this case.

## Objects and decisions in Python

Everything in Python is an object.
An object is something with properties and functions (actions which can be performed) that can be accessed via dot notation.
For example, we already saw the append function, which is a function attached to a list object which allows adding to the list.
But lists have several other useful functions:
```
>>> c
[1, 'test', 1.43, 0, 2, 'another list', 'final entry']
>>> c.index('test')
1
>>> c.remove('another list')
>>> c.reverse()
>>> c
['final entry', 2, 0, 1.43, 'test', 1]
```

Python provides information on these modules and properties via the `dir` command, which accepts a Python object and gives you back a list of things that can be applied to the object.

```
>>> dir(c)
['__add__', '__class__', ..., 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(c.count)
count(...)
    L.count(value) -> integer -- return number of occurrences of value
```

Ignore those entries beginning with `__`, and focus on `append`, `count`, `extend`, `index`, `insert`, and so on.
These are all functions which act on a list.
You can find out more about any of them using the help command, i.e. `help(c.insert)` for help on what the insert function does and what it needs in order to work.

Decisions are another very important part of any programming language.
Often we want to do something only if certain conditions are met.
An `if` statement provides a means of doing this, running statements within a following indented block of text (program) only if the condition is met.
It can be supplemented by `elif` and `else` statements -- `elif` (standing for "else if") providing a means to do something else only if an additional condition is met, and else provides a fallback -- if no conditions are met, what’s inside `else` is done.
For example:
```
>>> a=1
>>> if a==4:
...     print a
... elif a==2:
...     print a*a
... else:
...     print a*a+1
...
2
```
Here, indentation (extra spaces) is used to designate "blocks" of code -- that is, sections of code which are inside the if statement and only run if the condition is met.
When the indentation ends, the blocks end.
(In interactive mode, as here, there is an extra carriage return to end the block as well).

Decisions are based on comparisons, and a variety of different tools for making comparisons are available.
In Python, the `=` sign is used to set one thing equal to another, and a double equals sign is used to compare two things for equality -- hence `if a==4` in the example above.
Other common comparisons include `<` for less than, `>` for greater than, `!=` or `!>` for not equal, `<=` for less than or equal to, and so on.
Logical and mathematical operations are also permitted -- for example, `if (a==b and c!=2)` or `if not (a or b):` or `if (a-b < 2):`

A `while` statement is another common kind of decision (and the simplest loop, or repeated task), running an indented block of code as long as a certain condition is true:
```
>>> ct = 5
>>> while (ct > 1):
...     print(ct)
...     ct = ct - 1
...
5
4
3
2
```
Here, you can see that `ct` is initially set to 5.
The while loop runs as long as it is larger than 1, so we then enter the while loop. ‘ct’ is printed, and then we compute “ct - 1”, which is 5-1 or 4.
This is then stored back to ‘ct’.
Now, ct = 4, and we go back to the top of the while loop to see if the condition (ct > 1) is still met.
It is, so we print ct again, subtract one again, and so on. The countdown continues as long as ct is greater than 1.

This example uses another common feature in many programming languages -- a seemingly impossible equation such as `ct = ct -1`.
 These kinds of statements are always executed beginning with the right, so, as noted, we first evaluate the right hand side to get a value, and then store this value back in `ct`.
 So, despite its algebraic impossibility, it makes perfect sense in a computer program.

`While` loops are the simplest loops, but `for` loops are the most common.
`For` loops take a sequence of entries (such as a list of numbers or values; in Python, this is called an iterable) and run the specified code for each entry in that sequence.
For example:

```
>>> elements = ['hello','world', ', ', 'again']
>>> for elem in elements:
...     print elem
...
hello
world
,
again
```
Here, `elements` is a list of entries.
The `for` loop looks at each entry in turn and prints it.
Since the print statement switches to a new line every time it prints, our entries get spread across lines.

It’s worth noting that the basic syntax of a for loop is `for (your choice) in (sequence name)` where (sequence name) is the name of the list or sequence of items to work on, and (your choice) is a name you specify.
It’s usually a good idea to make this descriptive, but you can really make it anything you want -- so in our example above, we could have said, `for banana in elements:`, and then asked it to `print(banana)`.

Common mathematical operations are all available in Python as expected -- plus, minus, and divide (/) all have their usual functions. Exponentiation is done by `**`: `a=x**2` takes the contents of `x` and squares it.
It’s also possible to take remainders: `z = 13%4` takes the remainder of 13/4, which is 1.
Operations of the sort `x = x+1` or `y = y-1` are so common that there is even a shorthand for these expressions: `x+=1` or `y-=1`.
Try it for yourself.
This also works for division: `z/=3`, for example.
Other operations, such as sqrt for square root, log for natural logarithms, and log10 for logarithms in base 10, as well as common trig functions, are available in standard numerical libraries such as `numpy` or `math`.
(Libraries are extra toolsets you can ‘import’ into Python to get additional functionality).

## Slicing for lists and strings (and elsewhere)

Often we will want to work with just part of a list or a string, perhaps a group of elements. For example, we might want just specific characters from a particular line. (Some homework tracks will see this problem in an assignment). This can be done with a technique called slicing:
```
>>> line = "This is the line we're working on right now."
>>> line[16:20]
" we'"
>>> line[1]
'h'
```

Slicing takes just certain characters from a list or string (here, a string).
This particular case first requests characters 16 through (but not including) character number 20. Slicing always works this way -- the first entry number is included, but the endpoint is not included.
It’s also worth noting that `line[1]` points to character `h`, which is the second character on the line.
This is because for historical reasons Python starts counting with character 0, so line[0] would point to `T`.

Slicing can get a lot more complicated (and powerful) as highlighted in these examples, which you’re encouraged to try out for yourself:
```
>>> line[:20]
"This is the line we'"
>>> line[20:]
're working on right now.'
>>> line[:-5]
"This is the line we're working on right"
>>> line = line[7:20]
>>> line
" the line we'"
```

In the first two cases, when no character number is specified before or after the colon, it is assumed that you mean either from the start of the list or string (in the case that the left entry is missing) or to the end of the list or string (in the case the right entry is missing).
Negative numbers can also be provided, and these count back from the end.
Lastly, we reset `line` to be just a subset of the original string.

While all of these examples are for a string, they work in essentially the same way on lists.

## Using Python noninteractively

As noted above, using Python noninteractively (from the command line) is more common for big tasks or when we are making a tool which will be of general use.
This allows us to avoid retyping things when we need them again, allows us to reuse our code, and allows for easy troubleshooting (though Jupyter notebooks also allow for this).
Using it noninteractively simply amounts to typing Python commands into a text file (with name ending .py) and running it from the command prompt:
```python
x = [0,1,2,3,4,5]
y=[]
for i in x:
    y.append( i*i-1 )
z = x+y
print(z)
```

Running from the command prompt:
```
[dmobley-Pro:~] dmobley% python test.py
[0, 1, 2, 3, 4, 5, -1, 0, 3, 8, 15, 24]
```

## Functions in Python are reusable tools

Python functions are tools you can think of as a black box.
They take something in, do something with it, and give something back, and you shouldn’t have to know what goes on inside the box in order to be able to put things into it and get them out.
Python has many built in functions, but it’s also possible to write your own, and we will see quite a bit of this.
Think of it as making your own reusable, general purpose tools.
It’s also worth noting that functions can take in any number of items, and give back any number of items, including none.
Here are a couple (somewhat silly) functions to illustrate by way of example:

```
>>> def multiply(a,b):
...     c = a*b
...     return c
...
>>> multiply(77,43)
3311

>>> a = [1, 2, 3, 4, 5, 6]
>>> def modifylist(list):
...     list.append(33)
...     
>>> modifylist(a)
>>> a
[1, 2, 3, 4, 5, 6, 33]

>>> def printstuff():
...     print(“WARNING: Executed the printstuff function.”)
...
>>> printstuff()
WARNING: Executed the printstuff function.
```

Here we have three examples -- `multiply`, which takes two things in and gives back one; `modifylist`, which takes one thing in and gives back none (simply modifying the thing put into it) and `printstuff()`, which takes no things in and gives back nothing (simply printing a message).

A function always starts with a `def` statement, which defines it.
It also takes zero or more `arguments`, given within the parentheses after its name.
When it is first defined with a `def` statement, these arguments are just names -- for example, multiply is said to take two arguments, which for the purposes of the definition are called `a` and `b`.
What the function does is defined in terms of these names (multiply a and b together), but the names are not used outside the function definition.
Think of the names as describing things that go on inside the black box -- if you’re going to use the black box, you don’t need to know the names, you just need to know what goes in and what comes out.
That’s why when multiply is actually used, it’s `multiply(77,43)`. If we can see inside the box, we can see that 77 is going to go into the name `a` and 43 is going to go into the name `b` and they’ll get multiplied together.
But we don’t have to know that to use the box.
We just need to know we put two values into it and it gives back the product.

If a function is to give anything back, it does so by the `return` statement.
Here, we see it returning one value, but `return` can also give back multiple values, such as `return a, b, c, d` for example, which would give back all four items.

If you’re going to use a black box, you don’t necessarily need to know what goes on inside it, but you do need to know what it’s supposed to do and what it takes in and gives back.
Python provides a powerful way of doing this called "doc strings".
These make it possible for Python’s built in help to work for functions you have written as well.
For example:

```
>>> def a(x, y):
...   """Adds two variables x and y, of any type.  Returns single value."""
...   return x + y
... <hit return>
>>> help(a)
Help on function a in module __main__:

a(x, y)
    Adds two variables x and y, of any type.  Returns single value.
```

This doesn’t appear critical when it comes to a simple function like `add`, which there’s really no point in using and which is trivial.
But it becomes crucial for real functions in order for them to be useful to people other than their author, or over the long term.

Python code reuse and readability is also improved by commenting. Python allows lines marked with a `#` symbol at their beginning to be ignored.
These are called comments, and should be used to explain key features of what you are doing *always*.
For example, you might put in your program:
```python
#Compose a new list consisting of the squares of elements in the original list
b = [ elem*elem for elem in a]
```

The line beginning with `#` is informative but will be ignored by Python.

## Python modules are packages of code that can be used from other programs

Python modules are extensions of a sort, providing additional functionality that you or others may need from your Python programs.
Many are already provided with Python, but others are available for a wide variety of common tasks.
You may even write your own.
Any Python file containing Python code you have written can also be used as a module.
We already mentioned several examples of modules, such as `math` and `numpy`, which we will see again for numerical operations.
But you might also have written your own module for working with prime numbers.
To use this within Python, you might do this, if you already have a file `primes.py` containing some tools you want to use (such as the `nextprime` function).
```
>>> import primes
>>> primes.nextprime()
```
Existing modules already have a lot of useful functionality.
Suppose we want, in Python, to get a list of what is available in the directory where we’re working (like we might get from the Linux `ls` command).
We can do this:

```
>>> import os
>>> os.listdir(‘.’)
[..., 'Applications', 'bin', 'calendar', 'Desktop', 'Documents', 'Downloads', 'Illustrations', 'Library', 'local', 'mbox', ... ]
```
This provides a list of what is available in the present directory.
(Note that with ipython or Jupyter notebooks, you can actually use the `ls` command directly!).

There are also (in the ‘os’ module and elsewhere) tools for doing most of the common Linux file operations, as well as running tasks directly at the command line.

## File operations in Python are a strong point for Python

File input and output in Python is rather easy. To open a file, we do this, and help is available:
```
>>> file = open('README', 'r')
>>> help(file)
```
Opening a file takes options such as `"r"`` to open in read mode, `"w"`` to open for writing, and `"a"`` to open in append mode (where items can be added to the end of the file).
Once a file is open, various options are available, such as:

- `file.readlines()`, `file.writelines(name)`: Read or write lines as a list of strings
- `file.readline()`, `file.writeline(name)`: Read or write a single line
- `file.close()`: Close the file when done reading or writing (and save).

## Programming requires some planning

One of the most frequent problems I encounter in teaching students is that they begin trying to write a program before they understand the logical components of the task they are trying to complete.
This always results in confused failures.
Think about trying to speak in a new foreign language, for example.
Before you begin to express yourself in the new language, you have to understand what you want to say in your native language, then you begin to work through how to communicate that message in the new language.

Similarly, with programming, before you sit down and start trying to write a program, you must make sure you understand your task.
Then, break your task into small steps and describe them in English (if you are a beginner, I suggest actually doing this in outline format on a piece of paper, though more advanced students may do this in their heads).
Write down a description of what each major step is, and then outline in detail each minor step in that process, in English.
If a step is too hard, it means you don’t understand it well enough or haven’t broken it down enough, so break it down further.

Once you have it outlined in detail, think about how you translate each English statement into Python, and begin working on your program.
Do keep in mind, as you do so, that any repeated steps or steps you may use in another program should probably be written as functions.

One goal of good programming is to make your code reusable -- both by yourself later (5 years from now when you’ve forgotten!), or by someone else who doesn’t have you around to explain it to them.
This means that good code should be commented, explaining your goals, major steps, and then a variety of intermediate steps along the way.
Use descriptive variable names: `filename` makes a better variable name for the name of a file than `i`, and so on.
And, generally, write reusable functions for repetitive or general tasks -- a tool you use here could be used again in the next problem if you make it reusable.

## Pointers for troubleshooting

Inevitably, programs don’t work as you would like.
My first suggestion is to try things in the Python interpreter (within Python itself) before trying them from the command line when possible, as this can provide useful information.
Also, use `print` statements -- printing contents of variables throughout the code can help you see what’s going on.
Step through the code if necessary -- there are ways to do this using something called a debugger.

Also, test components of your program separately.
If you use a bunch of functions together, make sure each one works separately.
Each step or component ought to work individually before you try and make them work together.

If your problem is too confusing, simplify by breaking it into smaller steps.


## Illustrative examples
###Sum of the squares of integers:

```python
#Not this
for i in range(1,21):
   sum = i**2


#Not this either
for i in range(1,21):
   sum = sum+i**2
```
Here, “range” is a builtin Python function that gives back a list beginning at the first number and ending before the second, so we’re asking to loop over the list `[1, 2, 3, ..., 20]`.
That part is OK.
But the first example goes wrong because it simply makes `sum` BE the square of `i`.
The loop is right, and `i` is right, but the final value in sum will be `400`, which is not what we want.

The second example won’t work at all.
It’s closer, but `sum` isn’t defined except inside the `for` loop.
The first time we get there, what will `sum` be when we evaluate the right hand side of the equation? It won’t be anything, and so Python won’t understand it.
Rather, we need to do this:
```python
#Compute the sum of the squares of the first 20 integers
sum = 0
for i in range(1,21):
   sum = sum+i**2
```

We have to set `sum=0` outside the `for` loop so it’s already defined when we need to use it inside the loop.

### Printing only lines with a certain word from a file:
```python
Next, consider reading a text file and printing only lines containing a certain word:
file = open('dummytext.txt', 'r')
text = file.readlines()
file.close()

for line in text:
    if ‘comfort’ in line:
        print(line)
```
This uses the readlines function attached to the file object to read in all the lines from the file into a list we call ‘text’. It then looks at each line of text individually (naming them ‘line’) and prints the line out if the word ‘comfort’ occurs on the line.

### Multiply elements of two lists together, but skip certain results:
Now, let’s take two lists and multiply their elements together, composing a new list. But let’s also stipulate that we don’t want any elements larger than 150 in the new list.

```python
list1 = range(0,15)
list2 = range(15,30)

newlist = []
for (idx, elem) in enumerate(list1):
    prod = elem*list2[idx]
    if prod<150:
        newlist.append(prod)
print(list1, list2, newlist)
```
Here, we define two lists using the range function as discussed above -- `list1` running from 0 to 14 and list2 running from 15 through 29.
Note that these have the same number of elements.
We want to multiply the first element of the first list by the first element of the second, the 2nd of the 1st with the 2nd of the 2nd and so on.
One way to do this is with a `for` loop. But we want to store the results into a new list, so, like with our sum a couple examples above, we set up a new list (`newlist`) outside the `for` loop so it already exists when we need it.

Then, the `for` loop looks a little unconventional.
The thing is, now we want to track not just what value we are working on, but what element number we’re working on.
That is, we want to know we’re on the first element of list 1, so we can look up the first element of list 2.
So, we use another feature of a `for` loop, which allows us to have multiple things change at the same time.
`enumerate` is a Python built in function that takes a list (or certain other sequential data types) and gives back the numbers of the items and their values.
So, `enumerate(list1)` will give us back the pairs `0,0`; `1,1`; `2,2`; and so on (kind of boring in this case since they are the same, but for `list2` it would be more interesting -- `enumerate(list2)` would be `0,15`; `1,16`; and so on).
Now, inside our `for` loop, we take `elem`, which is the element of the first list we’re looking at, and multiply it by the corresponding element of the second list (`list2[idx]`, the idx-th element in `list2`).
This gets stored to `prod`.
We then check if `prod` is less than 150, and if it is, we store it to our new list.
And that’s the end!


### On to something mildly useful -- let’s find the first N prime numbers!
Next, let’s find the first N prime numbers.
Remember, a prime is a number divisible only by itself and 1.

```python
#!/bin/env python

#N is limit for how many primes we want to find
N = 50

#Start with 2 as the first prime; ignore 1 since every number is
#divisible by 1
primesfound = [2]
#Track which number to look at next
ct = 3

#Loop until we find N primes
while len(primesfound) < N:
    #Track whether we have found the number we are looking at NOT to   
    #be a prime
    notprime = False
    #Loop over every element of our existing primes to see whether
    #our new number is divisible by one of these
    for elem in primesfound:
        #Check to see if it is divisible; if so, break out of the
        #loop and go on to next number
        if ct%elem == 0:
            notprime = True
            break
    #If our number is not divisible (that is if it is prime) track it
    if not notprime:
        primesfound.append(ct)
    #Go on to next number
    ct += 1

print(primesfound)
```
Here, we start off by specifying how many prime numbers we want -- in this case, 50.
And we jump start the process by listing prime numbers we already know, beginning with just the number 2. We start a list to track every prime we’ve already found, and a counter ‘ct’ to track which number to look at next.

We’ll look for prime numbers in the direct way here -- start at a low number (3) and work our way up.
Every time we get to a number, we’ll check whether it’s divisible by any of the prime numbers we already know, and if it is, it’s not a prime.
If it’s not divisible by one, it’s a prime.
That’s what the while loop is about -- it is going to keep going until we have found N prime numbers.
It starts by assuming a number is prime, and starts a tracking variable `notprime` to track whether we’ve found it’s NOT prime.
Then, it looks through all the primes we already know about using a `for` loop, and if our current number is found to be divisible by any known prime (remainder 0) it sets `notprime = True` and runs the `break` command.
`break` is a command that exits out of the last loop, so in this case that means leaving the `for` loop.
Then, we come to the last `if` statement.
If we haven’t found the number is not a prime by finding something it’s divisible by (that is, if it IS a prime) we add it to our list.
Either way, when we get to the end of the while loop, we go on to the next number.

Note that there are probably much more efficient ways to find prime numbers -- this is just the most direct way.


### A simple function example -- factorials

Let’s try and calculate a factorial, and let’s make a reusable function to do it.
We want our function to be a black box.
It will take a (positive) integer, and return the number’s factorial (the product of the number itself with all smaller integers, i.e. `3!` (3 factorial) is `3*2*1 = 6`).
First, let’s do this the simple (but longer) way:
```python
def factorial( num ):
	"""Take a positive integer and return its factorial."""
	total = num
	next = total - 1
 	while next > 1:
		total = total*next
		next = next - 1
	return total
```

What happens here?
Let’s suppose we put in the number `4`, and think it through.
`total` is set to `4`, and we set `next` to `3`, and then we hit the `while` loop. `next` is greater than `1`, so we enter the `while` loop. `total` now gets set to `total` (4) `* next` (3) which is 12. Then we subtract `1` from `next`, so we’ll look at `2` next.
We then check to see if `2` is greater than `1` and it is, so we go back to the top of the `while` loop.
Now `total` gets set to `total` (12) `* next` (2) which is 24, and `next` gets set to `1`.
Now, we check to see if we take another trip through the `while`, but `next` is now `1` (which is not greater than `1`), so we are done.
So our black box spits back out the result currently in `total` -- 24.

If you don’t follow that 100% and you’re planning on doing anything involving Python, go back and work through it one line at a time.
Start at the top filling in what each variable is until you hit the end of the while loop.
Then go back to the top of the while loop and do it again, switching to a different color pen or a different spot on your paper.
Keep going until you get to the end.

So, that’s not bad -- a factorial function that works, consisting of 6 lines of code. That seems pretty good, but in fact there’s an even shorter function that will do the same thing:

```python
def factorial( num ):
	"""Take a positive integer and return its factorial."""
	total = num
	for value in range(1,num):
		total = total*value
	return total
```
This one is a bit harder to understand (since it does the multiplication in reverse order), but the result is the same.
In fact, to the user of these functions, it wouldn’t matter which one were used, since it’s only what’s inside the box which is different -- input and output are the same.  


## Common mistakes in Python

Here are some common mistakes.
Python is good about telling you what mistake you’ve made, but at first it is hard to understand what it’s saying.
Try some of these out to see what error messages you get and start getting a feel for how it tells you what the problem is.

```
#Error 1
for i in range(5)
   print(i)

#Error 2
b = 2
a = sqrt(float(b+2.)


#”scope” errors -- this works but maybe not how you would think
for i in range(20):
   a = []
   a.append(i)
print a

#type errors
a = ‘test string’
b = 2
c = a+b
```

### A small word of caution about lists and assignment
Python often handles assignment by pointing.
For example, setting `a=1` creates the number 1 in the computer’s memory, and points the variable a to it.
This means that copying doesn’t necessarily work as one might expect, especially for lists or dictionaries.
Watch out for setting `a = [1, 2, 3]` and `b=a`.
After subsequently setting `b[1] = 0`, `print(a)` gives `[1,0,3]`.
Somehow changing `b` changed `a`!
That’s because `b` was pointing TO `a`, so changing an entry of `b` changes what `b` is pointing to -- that is, `a`.
This behavior can be avoided by making sure that `b` is a copy of a when that is intended (`import copy`, then `b = copy.copy(a)`).

This is not true for some types of data -- numbers are "immutable" so, for technical reasons, setting `a=b` and then changing `b` simply changes what `b` points to.

This can be confusing.
The point is, just be careful not to assume that `b=a` makes `b` a COPY of `a`, though it does for numbers.


# Numerical Operations in Python

## Why NumPy and SciPy

Python is not a "compiled" language, where code is compiled’ for the computer to run in advance, a step that takes some time.
This is both good and bad, and the bad is that it tends to be slower than many other languages, at least for doing large numerical calculations.
One way around this is to use Python "modules" that are built in other languages that DO work well for numerics.
We will use several of these here.
NumPy (Numeric Python) provides basic routines for manipulating arrays or matrices and other numeric data.
SciPy (Scientific Python) extends NumPy by providing additional routines such as minimization, Fourier transformations, statistical packages and a large variety of other tools.
Because these are precompiled and written in other languages, they are faster (though the user doesn’t need to know about this part to use them).

### Reminder: Import modules to access their functionality

NumPy and SciPy have to be imported into Python before you can use them:
```
>>> import numpy
>>> #Access using numpy.X
>>> #OR:
>>> import numpy as np
>>> #Access using np.X; this will be assumed in what follows
```
The code which follows will assume you have used `import numpy as np`, so that numpy tools are accessed via `np.X`

## Working with data in NumPy

While NumPy has a lot in it, the key data structure we will see the most here is an NumPy array.
It is like a Python list, but it contains numerical data, which must all have the same type (either a float or an integer (int)).
However, it is much more efficient for numerical operations than a list, and many common tasks can be done very quickly on these arrays.
One major difference from lists is that arrays are given a size in advance, while lists can be expanded using append.

It is easy to create NumPy arrays, and there are several ways to do it:
```
>>> a = [ 1, 4, 5, 8]
>>> b = np.array( a, float )
>>> c = np.zeros( (10), int )
>>> b
array([ 1.,  4.,  5.,  8.])
>>> c
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>> type(c)
<type 'numpy.ndarray'>
```
Here you can see example array creations by either converting a list to a (1 dimensional) array, or creating a new array from scratch out of zeros.
In the latter case, the (10) specifies the size of the array.

Multidimensional arrays are also possible (of arbitrary dimensionality), and different "axes" or directions in the arrays are accessed using commas within the brackets for the array, as illustrated here:
```
>>> a = np.array( [ [1,2,3], [4, 5, 6] ], float )
>>> a
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])
>>> a[0,0]
1.0
>>> a[0,1]
2.0
```

Let’s suppose we want to read a bunch of numbers from a file, with one stored on each line of a text file, and put it into a NumPy array.
How do we do this when we can’t append to an array, and have to set its size initially?
This illustrates one approach:
```
>>> #Open a file and read lines
>>> file = open(‘tmp.txt’, ‘r’)
>>> text = file.readlines()
>>> file.close()
>>> #Allocate storage for data from file
>>> data = np.zeros( (len(text)), float )
>>> #Loop over lines in text, manipulating and storing to data array
>>> for (linenum, line) in enumerate(text):
...     #(code to parse line would go here)
...     data[linenum] = ...	The example is missing the code to actually get the number from each line (which would depend on the file format) but should be enough to illustrate the key idea -- first determine how many entries will need to be stored (such as by looking at the length of the file), then read the data and store it.
	Arrays can also be sliced in a matter much the same as slicing of lists:
>>> a = np.array( [ [1,2,3], [4, 5, 6] ], float )
>>> a[0,:]
array([ 1.,  2.,  3.])
>>> a[:,2]
array([ 3.,  6.])
>>> a[-1:, -2:]
array([[ 5.,  6.]])
```
Note, as in lists, the use of ‘:’.
When ‘:’ alone is specified in a particular direction, it means all elements in that direction -- for example, ‘a[:,2]’ means all rows and the #2 (third) column in array ‘a’.2D arrays can be thought of as having rows and columns, so the first index is the row number and the second is the column number.

NumPy also has a particularly convenient `numpy.loadtxt` function specifically for processing text files with common layouts; it can often be used to shortcut the above.

Often, we need to determine certain things about arrays, such as their shape (‘a.shape’), their length (‘len(a)’ gives the length along the first axis), or whether certain values are present:
```
>>> a = np.array( [ [1,2,3], [4, 5, 6] ], float )
>>> 2 in a
True
>>> 0 in a
False
```

Arrays can also be converted (back) to lists: `a.tolist()`.
Combining arrays also is different from combining lists -- combining arrays is done by concatenation: `c = np.concatenate(a,b)`, for example.

## Math in NumPy

For array math, the arrays should be the same size (typically).
`+`, `-`, `*`, `%`, `**` all do operations on the arrays in an element-by-element way as you might expect.
It’s worth noting that for multidimensional arrays, multiplication (`*`) performs element-by-element multiplication.
(If you’ve had linear algebra or worked with matrices, this might seem strange and you might expect matrix multiplication, but there are functions that will do that if that’s what you want).

Arrays, unlike lists, can handle simple additions or subtractions (or even multiplications) of non-arrays. For example:
```
>>> a = np.array([1,2,3], float)
>>> a+=2
>>> a
array([ 3.,  4.,  5.])
```

NumPy provides many mathematical functions and constants, including functions such as `abs` (absolute value), `sign` (the sign of a number), `sqrt` (square root), `log`, `log10`, `exp`, `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `sinh`, `cosh`, `tanh`, `arcsinh`...
Constants include `pi` and `e`.
There are also many functions for whole array operations, such as `a.sum()` to sum elements in the array.
Other functions are applied in the same way and include `prod` (product of elements), `mean`, `var` (variance), `std` (standard deviation), `min`, and `max`. `argmin` and `argmax` give indices of minimum and maximum values.

Application of these can also be limited to a particular axis (direction) using the optional axis argument:
```
>>> a = np.array([[0, 2], [3, -1], [3, 5]], float)
>>> a.mean(axis=0)
array([ 2.,  2.])
```

Standard comparisons can be performed on arrays; these return arrays of Boolean (True/False) values. For example:
```
>>> a = np.array([1, 3, 0], float)
>>> b = np.array([0, 3, 2], float)
>>> a > b
array([ True, False, False], dtype=bool)
```

NumPy also provides an extremely powerful function named `where` which can be used to easily select only certain elements of an array:
```
>>> coordinates = np.array( [0.0, 0.45, 0.75, 0.13, 0.89, 1.47, 0.14], float )
>>> interesting_residues = [ True, False, False, True, True, False, True ]
>>> indices = np.where( interesting_residues )
>>> interesting_coordinates = coordinates[indices]  #See p. 15, NumPy writeup
>>> interesting_coordinates
array([ 0.  ,  0.13,  0.89,  0.14])
>>> np.where( coordinates < 0.3 )
(array([0, 3, 6]),)
```

Logical operations can also be used in constructing conditions for selecting elements of an array.
NumPy provides `logical_and` and `logical_or`, so, for example, one can ask for `where( logical_and(a > 0, a<3))` to obtain indices where elements of a are greater than zero but less than 3.


### Additional references on NumPy

For additional information on NumPy, check out the documentation on the NumPy site (http://numpy.scipy.org/).

## Making plots and graphics within Python
### Matplotlib/Pylab plotting tips and tricks

Matplotlib and the connected libraries pylab/pyplot provide a lot of useful tools for making plots and graphics directly within Python and either displaying them to your screen or saving them to a graphics file in one of a variety of formats.

Making really basic plots is simple, and is highly recommended anytime you need to visualize data you already have within Python -- it will take you more time to get the data out of Python into some other format than it will to plot within Python, and Python can make publication quality plots using these libraries.

Here’s a basic example:
```
>>> import pylab as pl
>>> import numpy as np
>>> xvals = np.arange(10)
>>> yvals = [0,5,7,3,13,7,-5,8,3,7]
>>> pl.plot(xvals, yvals)
>>> pl.savefig('firstplot.pdf')
```
At the most basic level, Pylab plots a set of x values (in a list or array) versus a set of y values.
Axis labels, legends, and all of the other typical plot options are available. Graphics can be output to various formats, including pdf (here), jpg, png, svg and so on.
Axis labels can be added using `xlabel`, `ylabel`, and so on; limits can be adjusted using `xlim`, `ylim`, and similar.
Symbols and line styles can be specified with an optional argument to the plot command, such as ‘plot(x, y, ‘mo’)’ to plot magenta circles (for formatting info, see help(plot)).

By default, issuing a second plot command will simply ADD to your existing plot, but you can create a new plot using `figure()`.
Lots of documentation and examples are available online and you can find them easily using Google.
See also the help command.

You will likely end up making some plots within Python, so you may need to refer back to this section.

## Random number generation
### Computational science often requires "random" numbers

Often, we want to do something with a certain probability. For example, we may have two choices for what to do next, and decide to pick one with a 50% probability.
That means that we essentially have to have the computer "throw a coin" -- basically, it needs to pick a random number to determine whether or not this event happens.

There are many applications of this; one example is in assigning initial velocities to objects in a molecular simulation.
We know what the average velocity ought to be given a target temperature, but we are not given any information on velocities of particular particles.
So, one way to deal with this is to give particles random initial velocities selected in such a way that they have the correct average velocity.
So, we need to be able to pick "randomly", but computers can’t actually generate random numbers (they can’t throw coins) -- if you program them to do something, they do it, which is a deterministic rather than a random process. So, what we actually do in computational science is generate "pseudorandom numbers" -- numbers that are generated deterministically from an initially starting point, but distributed in a way that is very similar to random.
These can be used to make apparently random choices -- and many are good enough that for practical purposes the numbers generated do behave like random numbers (though there are also bad random number generators!).

NumPy has a random number generator available in its `random` module:
```
>>> np.random.seed(293423)
>>> np.random.rand(5)
array([ 0.40783762,  0.7550402 ,  0.00919317,  0.01713451,  0.95299583])
>>> np.random.random()
0.70110427435769551
>>> np.random.randint(5, 10)
9
```
This initializes the random number generator by providing a ‘seed’ number, then generates 5 random numbers stored in an array. It also generates one additional number (a float) after that, and then a random integer between 5 and 10.

## Interfacing Python with Other Languages
### Optional: You can write your own fast external libraries

As noted above, Python is not particularly fast at high performance numerics, so libraries like NumPy and SciPy provide routines written in other languages (Fortran or C++) which can be used within Python to provide good performance. It is actually possible to write these sorts of modules yourself without much effort, if you know some Fortran or C++, e.g. with `cython` or `f2py` or similar tools.


## Author(s):
David L. Mobley

## Acknowledgments
This was motivated by (and possibly adapts some of) much earlier material from M. Scott Shell from around 2008.
