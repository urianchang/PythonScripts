# Exercises 4.4 - 4.6

# Exercise 4.4
# Answer: D

# Exercise 4.5
# Answer: D

# Exercise 4.6

def computepay(hours, rate):
    if hours > 40 : 
        pay = float((40*rate)+((hours-40)*(1.5*rate)))  
    else : 
        pay = float(hours*rate)
    return pay

try:
    hours = float(raw_input("Enter Hours: "))
    rate = float(raw_input("Enter Rate: "))
except:
    print "Error! Please use numerical input."
    quit()

pay = computepay(hours, rate)
print "You will be paid", pay ,"dollars this week."