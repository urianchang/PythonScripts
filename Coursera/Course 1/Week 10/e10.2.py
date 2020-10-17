# Exercise 10.2

fname = raw_input("Enter file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened: ", fname 
    exit()
    
hours = dict()  
for line in fhandle :
    line.strip()
    if not line.startswith("From ") : continue
    words = line.split()
    time = words[5]
    hour = time.split(":")
    hours[hour[0]] = hours.get(hour[0], 0) + 1
    
lst = list()
for hour, count in hours.items() :
    lst.append((hour, count))
    
lst.sort()

for hour, count in lst:
    print hour, count