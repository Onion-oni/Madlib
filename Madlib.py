def madlib():
    #First we input the parts of speech we will be using.
    setting = input('location: ')
    adjective = input('adjective: ')
    #once we have our inputs, the code will return the story with the elements inputted above
    return 'Our story takes place here in ' + setting + '. The sunsets here in ' + setting + ' are among some of the most ' + adjective + ' in the world.'
    #future plans include using libraries like spaCy to verify parts of speech being entered.
