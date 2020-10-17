# Exercise 4.7 "Grades"

def computegrade(g) : 
    if g >= 0.0 and g <= 1.0 :
        if g >= 0.9 :
            print "You got an A."
        elif g >= 0.8 :
            print "You got a B."
        elif g >= 0.7 : 
            print "You got a C."
        elif g >= 0.6 : 
            print "You got a D."
        else : 
            print "You got an F."
    else :
        print "Error! Score does not meet parameters. Please try again."
        quit()
        
try : 
    grade = float(raw_input("Please enter your score: "))
    print "Thank you."
    print "Calculating..."
except :
    print "Error! Please enter a numerical value."
    quit()
    
computegrade(grade)