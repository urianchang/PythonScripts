#Assignment

import re

fname = raw_input("Enter file name: ")
fhand = open(fname, 'r')

total = []

for line in fhand :
    x = re.findall('[0-9]+', line)
    for num in x:
        total.append(int(num))
        
y = sum(total)
print y