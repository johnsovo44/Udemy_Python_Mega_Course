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