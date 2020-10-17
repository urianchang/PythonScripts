# Exercise 7.1

fname = raw_input("Enter a file name: ")

# If lazy...
if len(fname) == 0 :
    fname = "mbox-short.txt"

try : 
    fhand = open(fname)
except :
    print "File cannot be opened: ", fname
    exit()
    
for line in fhand :
    line = line.rstrip().upper()
    print line
