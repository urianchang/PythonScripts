# Assignment 7.1

# Use words.txt as the file name

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh :
    line = line.rstrip().upper()
    print line