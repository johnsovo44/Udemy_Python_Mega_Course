# opening file with a python. 
# store the file in a variable. It's an object that is stored in ram

myfile = open("Udemy_Python_Mega_Course\\Auxillary Resources\\Section 11\\fruits.txt") 

# this creates file objects, but there isn't much you can do with it unless you are explicit about it. THis will just open it and pretty much remove it from memory if nothing happens. 

print(myfile.read())
print()

# coding exercise (open the bear file and read)

file = open("Udemy_Python_Mega_Course\\Auxillary Resources\\Section 11\\bear.txt")

print(file.read())
print()

# Keep in mind that the file cursor goes to the bottom after opening the file. If you print it twice you can see this. It will print it out, but the second time it won't.

# what you can do instead is put the read method into a variable, that way you can print that out as many times as you like

myfile = open("Udemy_Python_Mega_Course\\Auxillary Resources\\Section 11\\fruits.txt") 

content = myfile.read()

print('1st')
print(content)
print('2nd')
print(content)
print()

# it's good practice to close a file once you are done with it. 

myfile = open("Udemy_Python_Mega_Course\\Auxillary Resources\\Section 11\\fruits.txt") # hear we are creating an object and opening the file

content = myfile.read() # this is an object to read the file's contents

myfile.close() # this is the method to use to close the file. Once its closed if you read it again you will get an error.

# a better way to do this is with the 'with' content manager.

with open("Udemy_Python_Mega_Course\\Auxillary Resources\\Section 11\\fruits.txt") as myfile:
    content = myfile.read()

print('Using the "with" content manager')
print(content)
print()

# it's basically the same thing written above but more organized. No need to actually use the close method cause the with content manager does it implicitly. 

with open ("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\fruits.txt") as file:
    content = file.read()

print('basic path read')
print(content)
print()

# let's a create a new file and write to it

with open("vegetables.txt", 'w') as file:
    file.write("Tomato")

# side note: For some reason when this creates files it is creating them outside of the udemy folder instead of in the same folder where this section 11 file exist. Odd. I can actually specify where I would like for the file to be written.

with open("Udemy_Python_Mega_Course/vegtables2.txt", 'w') as file:
    file.write("Another Tomato")

# be careful what file you create because if you use a name that has already been created then you will overwrite the file.

# you can also create new information and write line by line...

with open ("Udemy_Python_Mega_Course/vegtables2.txt", 'w') as file:
    file.write("Another Tomato\nA Cucumber\nOne more Tomato")
    file.write("\nGarlic")

# Coding Exercise (print out the first 90 chars of bear.txt)

with open ("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\bear.txt") as file:
    content = file.read()

print(content[0:90])

# Coding Exercise (create a function to search for a character in a string from a file)

def char_finder(filepath, char):

    with open(str(filepath)) as file:
        content = file.read()
    return content.count(str(char))

print(char_finder("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\bear.txt","o"))

# coding exercise (write the first 90 characters to a new file)

with open ("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\bear.txt") as file:
    content = file.read()

with open("Udemy_Python_Mega_Course/first.txt", 'w') as file:
    file.write(content[:90])

# what if we want to add more lines to an existing file? 

with open("Udemy_Python_Mega_Course/vegtables2.txt", 'a') as myfile:
    myfile.write("\nOkra")

# the 'a' or append clause allows you to add to an existing file, but you actually can't read it. There are two things you need to do first.

with open("Udemy_Python_Mega_Course/vegtables2.txt", 'a+') as myfile:
    myfile.write("\nZucchini")
    myfile.seek(0)
    content = myfile.read()
print(content) # this will allow you to read it multiple times.

# Coding Exercise (append one doc to the other)

def append_docs(filepath1 = "Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\vegetables.txt", filepath2 = "Udemy_Python_Mega_Course\Auxillary Resources\Section 11\\fruits.txt"):

   file1 = open(filepath1)
   content = file1.read()

   with open(filepath2, 'a+') as myfile:
       myfile.write(content)

append_docs()

# coding exercise (append content two more times)

counter = 0
thres = 2

file = open("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\data.txt")
content = file.read()

while counter < thres:

    with open("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\data.txt", 'a') as myfile:
        myfile.seek(0)
        myfile.write("\n")
        myfile.write(content)
    
    counter += 1

# the way the instructor solved it was a bit cleaner

with open("Udemy_Python_Mega_Course\Auxillary Resources\Section 11\data.txt", "a+") as file:
    file.seek(0) # first find the first row
    content = file.read() # grab all the content
    file.seek(0) # go back to the first row
    file.write(content)
    file.write(content)






