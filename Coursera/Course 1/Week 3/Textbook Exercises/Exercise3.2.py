# Exercise 3.2

hours = raw_input("How many hours did you work this week?\n")
try:
    a = float(hours)
    print "Thank you."
except:
    print "Error! Please use numerical input."
    quit()

rate = raw_input("How much do you get paid per hour?\n")
try:
    b = float(rate)
    print "Thank you."
except:
    print "Error! Please use numerical input."
    quit()

# Worked Exercise Method
# try:
#   inp = raw_input("Enter Hours: ")
#   hours = float(inp)
#   inp = raw_input("Enter Rate: ")
#   rate = float(inp)
#except:
#   print "Error, please enter numeric input"
#   quit()

if a > 40 : 
    pay = float((40*b)+((a-40)*(1.5*b)))
    print "You will be paid:", pay , "dollars this week."  
else : 
    pay = float(a*b)
    print "You will be paid:", pay , "dollars this week."  