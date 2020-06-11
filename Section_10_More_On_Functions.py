# functions with Multiple Args

# some functions need more than one arg. 

def area(a,b):
    return a*b 

# here we specified the number of args but placing them in as parameters.

# coding exercise (takes in two strings and concatenates them)

def string_func(string1, string2):
    return string1+string2

# there are two different types of arguments

# non-keyword args (positional args)
def area (a, b):
    return a*b

print(area(4, 5))
# 4 is in the same position of a, and 5 with b.

# ...and keyword arguments (non-positional args)
def area (a, b):
    return a*b

print(area(a=4, b=5))

# keep in mind that when we create the function the variables we create are called parameters, while the variables we input when we call the function are called arguments. We can either just enter in the values or we can specify which parameter we would like the value to be stored. Keyword args vs Non keyword args. 

# with keyword args/parameters we can have default values too.
def area(a, b=5):
    return a*b

print(area(4))
# because we specified b upfront we don't have to call it later on.
# b is not fixed for ever either, we could place a value there if we wanted to.
# also a default parameter cannot go before a non-default parameter.

#what if we needed more than one arg but don't know how much yet?

def mean(*args):
    return sum(args)/len(args)

print(mean(1,2,3,5,7,4,3))
print(mean(1,3,45))
# any variable name after the asterisk is fine but args is best to use.
# args is a tuple, and you can manipulate that.

# coding exercise (Create a function that calculates the mean)

def mean(*args):
    return sum(args)/len(args)

# coding exercise (Create a function that turns strings into a list of strings)
def string_list(*args):
    out = [x.upper() for x in args]
    return sorted(out)

# its important to note that whateve you type in, it should come out in ABC order.

print(string_list("hello","world"))

# just like how we can have an arbitrary number of positional args we can also have an arbitrary number of keyword args

def mean (**kwargs):
    return kwargs

print(mean(a=1,b=2,c=3))
# keyword args are a dicitionary, not a tuple. 

# coding exercise (build a function that finds the sum of kwargs such that it equals 9)

def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(a=1,b=3,c=5))