# Assignment 3.1

hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Rate:")
r = float(rate)

if h < 40 :
    pay = float(h*r)
    print pay
else : 
    pay = float((40*r)+((h-40)*(1.5*r)))
    print pay
    
