# Assignment 3.3

score = raw_input("Please enter your score:\n")

try: 
    a = float(score)
except:
    print "Bad score"
    quit()

if a <= 1.0 and a >= 0.0 :
    if a >= 0.9 :
        print "A"
    elif a >= 0.8 :
        print "B"
    elif a >= 0.7 :
        print "C"
    elif a >= 0.6 :
        print "D"
    elif a < 0.6 :
        print "F"
else :
    print "Bad score"
    quit()