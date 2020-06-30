# there are a ton of builtin modules, methods and functions

dir(str) # check out a sample by running this code.

username = 'pypypy'
len(username)

# this stuff comes ready to go soon as you install python.

# There are modules too that you haven't experimented with yet...

while True:
    with open("data.txt") as file:
        print(file.read())

# this loop here will read this file for ever. What if we don't want that

import sys
sys.builtin_module_names

# we can look up what modules python has builtin for us to find the right thing.
# let's use time

import time
dir(time)
# we can see what we can do with that module.
# there is method called sleep let's use that.

time.sleep(3) # this will pause the script execution for 3 seconds.

# let's re-write our script above
import time
while True:
    with open("data.txt") as file:
        print(file.read())
        time.sleep(10)

import time
while True:
    print("Hello world")
    time.sleep(5)

# this is all fine and dandy but what if the file is deleted, will the script run?
# No. We would get an error and the script would stop completely.
# to solve this we can use the OS module.

import os # not among the builtins, its actually a bit different.
# if you type in sys.prefix, copy the path, and type start [path] in terminal you will navigate to it. Go to lib, the python version you are using and you will find what are called "Standard Python Modules". These are all written in python code. DO NOT CHANGE ANYTHING IN HERE.

# if you use dir(os) you'll discover a method called path in Os. let's use it.

import time

while True:
    if os.path.exists("data.txt"): # check to see if the file even exist first.
        with open("data.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(5)
