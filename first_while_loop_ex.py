
# while is the keyword for the indefinite loop

'''n = 5

while n > 0:
    print(n)
    n = n -1
print('Blastoff')
print(n)'''

# Blastoff means the loop has ended

# an example of infinite loop 

'''n = 5
while n > 0:
   print('Lather') # like a shampoo
   print('Rinse')
print('Dry off')'''

# here the loop will not stop.. HELL YEAH: the loop won't end.. SO THE SOLUTION IS GIVEN ABOVE is to have an iteration variable like n = n -1


# LOOPS(repeated steps) have iteration variables that change each time through a loop. 
# Often these iteration variables go through a sequence of numbers.

# ANOTHER LOOP

'''n = 0
while n > 0:
      print('Lather')
      print('Rinse')
print('Dry off')''' # this loop will ONLY print Dry off


# BREAKING OUT OF A LOOP - GETS YOU OUT OF THE LOOP

'''while True:
    line = input(':') # here i chose instead of '>' like in the video, i chose ':' to input whatever the person wants
    if line == 'done':
        break
    print(line)
print('Done')'''

 # FINISHING AN ITERATION WITH CONTINUE - IT DOES NOT GET YOU OUT OF THE LOOP, IT GOES TO THE NEXT ITERATION 

 # THe CONTINUE statement ends the current iteration and jumps to the top of the loop and starts the next iteration

while True:
    line = input(':')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('DONE')

# output:
#:hello there
#hello there
#:# don't print this
#:print this!
#:done
#DONE