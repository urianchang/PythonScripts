# Exercise 3.1

hours = raw_input("How many hours did you work this week?\n")
a = float(hours)
print "Thank you."

rate = raw_input("How much do you get paid per hour?\n")
b = float(rate)
print "Thank you."
print "Calculating..."

if a > 40 : 
    pay = float((40*b)+((a-40)*(1.5*b)))
    print "You will be paid:", pay , "dollars this week."  
else : 
    pay = float(a*b)
    print "You will be paid:", pay , "dollars this week."  