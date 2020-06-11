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