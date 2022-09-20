# video coursera 5.3 Finding the largest value

# MAKING SMART LOOPS
# The trick is 'knowing' something about the whole loop when you are
# stuck writing code that only sees one entry at a time.

# 1st step: SET SOME VARIABLES TO INITIAL VALUES
 # for thing in data:
        # Look for something or do something to each
         # entry separately, updating a variable

    # Look at the variables

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

# FINDING THE LARGEST VALUE

largest_so_far = -1

print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
    
print('After', largest_so_far)

