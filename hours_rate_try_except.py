
# Worked exercise : 3.2 Coursera video

'''Hours = input('enter no hours=')
Rate = input('enter rate=')
fh = float(Hours)
fr = float(Rate)
print(fh, fr)
x = fh * fr
print('PAY=', x)

if fh > 40 :
  print('Overtime')
else:
  print('Regular')'''

#other version of the same code above, but computing different rate for Overtime
'''Hours = input('enter no hours=')
Rate = input('enter rate=')
fh = float(Hours)
fr = float(Rate)

if fh > 40 :
# print('Overtime') # the instructor is better in real code not to print all that, for it could bug the code
   regular = fh * fr
   overtime = (fh - 40)*(fr*0.5)
# print(reg, ovt) # the instructor is better in real code not to print all that, for it could bug the code
   xt = regular + overtime

  
else:

# print('Regular') # the instructor is better in real code not to print all that, for it could bug the could
    xt = fh * fr
print('PAY=', xt)'''

# using try and except for avoiding errors like input of a string instead of an integer 

Hours = input('enter no hours= ')
Rate = input('enter rate= ')
try:  # watch video 3.2 More Conditional Statements
    fh = float(Hours)
    fr = float(Rate)

except:
        print('Error, please insert a numeric input')
        quit()
print(fh, fr)
if fh > 40 :
      regular = fh * fr
      overtime = (fh - 40)*(fr*0.5)
      xt = regular + overtime
else:
    xt = fh * fr
print('PAY=', xt)



