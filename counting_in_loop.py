# COUNTING IN A LOOP

'''zork = 0 # set the variable to zero, normally this would be called 'Count'
print('Before', zork)

for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1 # increment by 1 # set the variable to zero and then we incremented by 1, that gives us the count.

    print(zork, thing)

print('After', zork)'''


# SUMMING IN A LOOP
'''zork = 0 # set the variable to zero, normally this would be called count

print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing

    print(zork, thing)

print('After', zork)'''

# to ADD UP a VALUE we encounter in a loop, we introduce a SUM VARIABLE THAT STARTS AT O
# and we add the VALUE to the sum each time through the loop. That gives us the Total or Sum.

# difference between a 'Count' and a 'Total', is that instead of adding 1 to the variable, we add the 'thing' you're running


# FINDING THE AVERAGE IN A LOOP

'''count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)'''

# An average just combines the counting and sum patterns and divides when the loop is done.

# FILTERING IN A LOOP

'''print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')'''

# we use an if statement in the loop to catch/filter the values we are looking for.


# SEARCH USING A BOOLEAN VARIABLE

'''found = False
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)'''

# if we just want to search and know if a value was found, we use a variable that starts at False and is set
# to True as soon as we find what we are looking for

# HOW TO FIND THE SMALLEST VALUE

# smallest_so_far = -1 # starting with -1 here is incorrect, it's a flag value, we can't pick a number for this
# so we will use None type value

smallest = None # THIS IS A FLAG VALUE, it means here the smallest will only be None the first through the loop
                # but after that we'll just ignore this little part. THIS IS CALLED PRIMING US, GETTING STARTED

print('Before')

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
    
print('After', smallest)

# PYTHON OPERATOR 'is' here above in light blue implies 'is the same as', similar to, but stronger than == .
# This is a logical operator 
 # 'is not' is also a logical operator 
# i put is and is not in quotation marks, but this not a string is just to highlight their use

# we usually use is and is not for True, False and None


