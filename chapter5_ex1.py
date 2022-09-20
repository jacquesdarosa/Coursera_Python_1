# exercise using try and except

num = 0 # for the count
total = 0.0

while True: # writing this as an infinite loop
    sval = input('Enter a number: ') # string value is sval variable here.
    
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1
    total = total + fval
print('ALL DONE')

print(total, num, total/num)

