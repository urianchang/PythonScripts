# Find New Revision lines

import re

fname = raw_input("Enter file name: ")
searchword = raw_input("Enter search term: ")
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    if re.search(searchword, line):
        print line