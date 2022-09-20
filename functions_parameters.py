# A parameter is a variable which we use in the function definition.
# it is a "handle" that allows the code in the function to access the arguments for a
# particular function invocation

# video Functions part 2 - Building functions 4.2 coursera

# 1st function

'''def greeting(lang):

    if lang == "es":
        print('Hola')
    elif lang == "fr":
        print('Bonjour')
    else:
        print('Hello')

# lang here is a parameter or alias for en, es or fr

greeting('es')
greeting('en')
greeting('fr')'''

# RETURN VALUES

# often a function will take its arguments, do some computation, and RETURN a value to be used as the value of the function call in the
# calling expression . The RETURN keyword is used for this.

'''def greet():
    return 'Hello'
print(greet(), 'John')
print(greet(), 'Mary')''' # this is a slightly different function def greet() just to illustrate the RETURN VALUE

# now we're combining the first function def greeting() with a RETURN VALUE


def greeting(lang):

    if lang == "es":
        return 'Hola'
    elif lang == "fr":
        return 'Bonjour'
    else:
        return 'Hello'

print(greeting('en'), 'Paul')
print(greeting('es'), 'Pablo')
print(greeting('fr'), 'Jean')

print(greeting('xZ'), 'Mary') # I inserted this last argument 'xZ' to check the else statement would work with any argument than 'en' as showed 
# in the video. Result: it works!


# A FRUITFUL FUNCTION IS ONE THAT PRODUCES A result(or RETURN VALUE)

# THE RETURN STATEMENT ends the function execution and "SENDS BACK" the RESULT of the function




