#Exercise 9.2

import string

fname = raw_input("Enter the file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened:", fname
    exit()
    
dates = dict()
for line in fhandle :
    line.strip()
    if not line.startswith("From ") : continue
    date = line.split()
    dates[date[2]] = dates.get(date[2], 0) + 1

print dates

