# How do we approach a problem? The best way is to break down the problem into chunks. THis can be translated into programming with a function. Setting aside code for each particular aspect of the problem. Below we will do that. 

def sentence_maker(phrase):
    """
    Question mark or Period? That is the question. To determine that we will create a list of words. If they are at the beginning of the setence then its a question, if not then it is a regular sentence. Also we will capitalize it. 
    """
    questions = ("how", "what", "why", "when", "where")
    capitalized = phrase.capitalize() # use this to capitalize the phrase
    if phrase.startswith(questions):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

results = []  # creating a container to hold our user inputs
while True: # create a while loop that breaks if they enter in the event they type a particular phrase. 
    user_input = input("Say Something: ") # we ask for user input each time the loop starts over
    if user_input == "\end": # if the user enters in a particular phrase
        break # then we will break the loop
    else: # otherwise...
        results.append(sentence_maker(user_input)) # append the user input to the list after it has gone through the sentence_maker function where it determines if it is a question or not and gives it either a question mark or a period. 

print(" ".join(results)) # we can join the items in the list with .join()


