# Exercise 10.3

fname = raw_input("Enter file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened: ", fname 
    exit()

counts = dict()
for line in fhandle :
    line.strip()
    words = line.split()
    for word in words :
        letters = list(word.lower())
        for letter in letters :
            counts[letter] = counts.get(letter, 0) + 1
print counts








