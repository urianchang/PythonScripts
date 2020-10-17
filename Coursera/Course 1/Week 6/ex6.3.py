#Exercise 6.3

def count(string, letter) :
    x = 0
    for y in string:
        if y == letter:
            x = x + 1
    print "The letter "+letter+" appears "+str(x)+" time(s) in the string: "+string
    
count(raw_input("Please enter a string: \n") , raw_input("Which letter do you want to count? \n"))