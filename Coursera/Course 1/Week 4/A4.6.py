# Assignment 4.6

def computepay(h,r):
    if h > 40 : 
        pay = float((40*r)+((h-40)*(1.5*r))) 
    else : 
        pay = float(h*r) 
    return pay

hrs = float(raw_input("Enter Hours: "))

rate = float(raw_input("Enter Rate: "))

p = computepay(hrs, rate)

print p
