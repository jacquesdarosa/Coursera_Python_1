# ARGUMENTS, PARAMETERS, AND RESULTS


big = max('Hello world')
print(big)

# result of the above print is w

'''def max(inp):
    blah
    blah
    for x in inp:
        blah
        blah
    return 'w' ''' # this how the instructor explains how the max function works in this case above... Blah blah is just to illustrate
    # that the function checks whatever is written below it and then return the value.

# MULTIPLE PARAMETERS / ARGUMENTS

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


# SOME FUNCTIONS DO NOT RETURN VALUES and are called non-fruitful functions or a VOID FUNCTION
# if they return values they are called fruitful functions


