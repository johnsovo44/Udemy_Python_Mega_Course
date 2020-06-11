temps = [221,234,340,230]

new_temps = [] # create an empty container for our updated variables
for temp in temps: # create for loop to update each result
    new_temps.append(temp/10) # we will append to the list the value divided by 10 

print(new_temps) # print the results

new_temps = [temp/10 for temp in temps] # create a variable called temp and divide it by 10. For each item in temps we will call it temp. 

print(new_temps) # print the results

# list comprehension can include if statements too...

temps = [221, 234, 340, -9999, 230]

new_temps = [temp/10 for temp in temps if temp != -9999] # we will create variable called temp that will be divided by 10. For each item in the list temps we will call it temp and this will only apply to items that are not equal to -9999

print(new_temps)

# coding exercise (create a list that only prints out numbers)
def list_func(list_):
    new_list = [num for num in list_ if isinstance(num, int) or isinstance(num, float) == True]
    return new_list

list_ = [99,'no data', 95.0, 94, 'no data','93']
print(list_func(list_))

# coding exercise (only return numbers greater than 0)
def list_func(list_):
    new_list = [num for num in list_ if num > 0]
    return new_list

list_ = [-5,3,-1, 101]
print(list_func(list_))

# List Comprehension with if-Esle Conditional

# for if else statements inside list comprehension always remember that the for loop goes at that end. Should look like this

temps = [221, 234, 340, -9999, 230]

new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]
# divide the value by 10 if the value is not -9999, if it is -9999 make it 0
print(new_temps)

# coding exercise (list of strings and numbers, but turn strings into 0)
def list_func(list_):
    new_list = [num if isinstance(num, int) else 0 for num in list_]
    return new_list

list_ = [99,'no data', 95.0, 94, 'no data','93']
print(list_func(list_))

# coding exercise (sum up floats that are string data types)
def list_func(list_):
    new_list = [float(num) if isinstance(num, str) else num for num in list_]
    return sum(new_list)

list_ = ['1.2','2.6','3.3']
print(list_func(list_))