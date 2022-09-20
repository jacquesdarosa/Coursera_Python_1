# enter a number: 42
# Nice work

# enter a number: forty-two
# Not a number

rawstr = input("enter a number: ")

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print('Not a number')

    