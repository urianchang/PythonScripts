#Exercise 11.2

import re

fname = raw_input("Enter file name: ")
fhand = open(fname)

total = []
count = 0

for line in fhand :
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if len(x) > 0 :
        count += 1
        total.append(float(x[0]))

y = sum(total)
print y/count