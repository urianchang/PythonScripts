# Exercise 5.1

count = 0 
total = 0
max = None
min = None

while True:
    x = raw_input("Enter a number: ")
    
    if x == "done" or x == "Done" : 
        break
    
    # Check for empty line
    if len(x) < 1 : 
        break
    
    try : 
        num = float(x)
    except :
        print "Invalid input"
        continue
    
    count = count + 1
    
    total = total + num
    
    avg = float(total/count)
    
    if max is None or num > max :
        max = num
    
    if min is None or num < min :
        min = num

print total, count, avg


    
    
