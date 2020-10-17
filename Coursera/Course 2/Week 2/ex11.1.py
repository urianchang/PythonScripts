#Exercise 11.1

import re

searchword = raw_input("Enter a regular expression: ")

file = open("mbox.txt")
count = 0

for line in file:
    line = line.rstrip()
    x = re.search(searchword, line) 
    if x:
        count += 1
        
print "mbox.txt had", count, "lines that matched", searchword
    


