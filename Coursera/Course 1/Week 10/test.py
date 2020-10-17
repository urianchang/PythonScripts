fname = raw_input("Enter file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened: ", fname 
    exit()

counts = dict()
for line in fhandle :
    words =(line.strip()).lower().split()
    for word in words :
        letter = list(word)
        