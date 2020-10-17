#Exercise 9.1

fname = raw_input("Enter the file name: ")
fhandle = open(fname, "r")
text = fhandle.read()
words = text.split()

counts = dict()
for word in words : 
    counts[word] = counts.get(word, 0) + 1
    
print "to" in words